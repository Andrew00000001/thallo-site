// Opens the built website (site/) in a headless browser, on a desktop and a phone screen, and checks that it starts,
// that every screen opens and shows content, that each lesson's audio files are there, that the picture puzzle is set
// up, that progress survives a reload, and that none of this raises a JavaScript error. The automatic publishing
// (.github/workflows/publish-mi-pc-exam-prep.yml) runs it before publishing; it exits non-zero on any problem.
//
// usage (from mi-pc-exam-prep, after python3 build/site.py):  node build/site_smoke.js site
// needs the playwright package and its Chromium. The page loads Firebase from the live site's /__/firebase/ files when
// they can be reached (so the site's sign-in code runs too), and starts without them otherwise.
const http = require('http'), fs = require('fs'), path = require('path');
const { chromium } = require('playwright');

const ROOT = path.resolve(process.argv[2] || 'site');
const LIVE = process.env.SITE_URL || 'https://mi-pc-exam-prep.firebaseapp.com';
const VIEWS = ['home', 'watch', 'study', 'memory', 'numbers', 'practice', 'cards', 'math', 'games', 'exam'];
const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.json': 'application/json',
  '.webmanifest': 'application/manifest+json', '.png': 'image/png', '.ico': 'image/x-icon', '.webm': 'audio/webm' };

const server = http.createServer((req, res) => {
  let p = decodeURIComponent(new URL(req.url, 'http://local').pathname);
  if (p.endsWith('/')) p += 'index.html';
  const f = path.join(ROOT, p);
  if (!f.startsWith(ROOT + path.sep) || !fs.existsSync(f) || !fs.statSync(f).isFile()) { res.writeHead(404); res.end(); return; }
  res.writeHead(200, { 'Content-Type': TYPES[path.extname(f)] || 'application/octet-stream', 'Content-Length': fs.statSync(f).size });
  if (req.method === 'HEAD') { res.end(); return; }
  fs.createReadStream(f).pipe(res);
});

let failed = 0;
const check = (ok, what, info) => { console.log((ok ? 'ok   ' : 'FAIL ') + what + (ok || info === undefined ? '' : ': ' + JSON.stringify(info).slice(0, 400))); if (!ok) failed++; };

(async () => {
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const base = `http://127.0.0.1:${server.address().port}/`;
  const browser = await chromium.launch();
  try {
    for (const [w, h, label] of [[1280, 900, 'desktop'], [390, 844, 'phone']]) {
      const ctx = await browser.newContext({ viewport: { width: w, height: h }, reducedMotion: 'reduce' });
      const page = await ctx.newPage();
      const errors = [];
      page.on('pageerror', e => errors.push(e.message));
      await page.route('**/__/firebase/**', async route => {
        try { await route.fulfill({ response: await route.fetch({ url: LIVE + new URL(route.request().url()).pathname, timeout: 20000 }) }); }
        catch (e) { await route.abort(); }
      });
      await page.goto(base);
      await page.waitForFunction(() => window.__mipc && document.querySelector('#view-home'), null, { timeout: 60000 });
      await page.waitForTimeout(500);

      const site = await page.evaluate(() => ({ site: !!(window.claude && window.claude.site), firebase: !!(window.claude && window.claude.site && window.claude.site.ok) }));
      check(site.site, `${label}: website mode (sign-in code present)`, site);
      console.log(`     ${label}: Firebase ${site.firebase ? 'loaded from the live site' : 'not reachable; checked without it'}`);

      const data = await page.evaluate(() => { const D = window.__mipc.data(); return { questions: D.questions.length, lessons: D.lessons.length, cards: (D.cards || []).length }; });
      check(data.questions > 0 && data.lessons > 0 && data.cards > 0, `${label}: content loaded (${data.questions} questions, ${data.lessons} lessons, ${data.cards} flashcards)`, data);

      for (const v of VIEWS) {
        await page.evaluate(v => window.__mipc.go(v), v);
        await page.waitForTimeout(150);
        const shown = await page.evaluate(v => { const el = document.getElementById('view-' + v); return el ? { hidden: el.hidden, text: el.innerText.trim().length } : null; }, v);
        check(shown && !shown.hidden && shown.text > 20, `${label}: ${v} screen opens`, shown);
      }

      const pz = await page.evaluate(() => ({ total: window.__mipc.pz.total(), pictures: window.__mipc.pz.list().length, cur: !!window.__mipc.pz.cur() }));
      check(pz.pictures > 0 && pz.cur, `${label}: picture puzzle ready (${pz.pictures} pictures)`, pz);

      if (label === 'desktop') {
        const audio = await page.evaluate(async () => {
          const bad = [];
          for (const l of window.__mipc.data().lessons) for (const u of [l.audio, l.audioHQ]) {
            const r = u ? await fetch(u, { method: 'HEAD' }) : null;
            if (!r || r.status !== 200) bad.push([l.id, u, r && r.status]);
          }
          return bad;
        });
        check(audio.length === 0, `${label}: every lesson's audio files are there`, audio);

        const id = await page.evaluate(() => { const q = window.__mipc.data().questions[0].id; window.__mipc.srsAnswer(q, true, 'sure'); window.__mipc.save(); return q; });
        await page.waitForTimeout(300);
        await page.reload();
        await page.waitForFunction(() => window.__mipc && document.querySelector('#view-home'), null, { timeout: 60000 });
        const kept = await page.evaluate(id => !!(window.__mipc.P().q || {})[id], id);
        check(kept, `${label}: an answer is still there after reloading`);
      }

      check(errors.length === 0, `${label}: no JavaScript errors`, errors);
      await ctx.close();
    }
  } finally {
    await browser.close();
    server.close();
  }
  console.log(failed ? `${failed} check(s) failed` : 'all checks passed');
  process.exit(failed ? 1 : 0);
})().catch(e => { console.error('smoke test crashed:', e); process.exit(1); });
