// Screenshot every scene of a lesson in the real player (silent preview with estimated timing) and report layout problems.
// node lshot.js <lesson.json> <outdir> [--theme dark] [--scenes 2,5] [--app preview_body.html] [--w 1280] [--states]
//   --states  also capture activities after "skip" (answers shown) and, for drawings, the first beat
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
const fs = require('fs'), path = require('path');
const args = process.argv.slice(2), opt = k => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : null; };
const L = JSON.parse(fs.readFileSync(args[0], 'utf8')), out = args[1]; fs.mkdirSync(out, { recursive: true });
const app = path.resolve(opt('--app') || path.join(__dirname, '..', 'preview_body.html'));
const wrapped = path.join(path.dirname(app), '.wrapped_' + path.basename(app));
if (!fs.existsSync(wrapped) || fs.statSync(wrapped).mtimeMs < fs.statSync(app).mtimeMs)
  fs.writeFileSync(wrapped + '.' + process.pid, '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>body{margin:0;font:14px system-ui}[hidden]{display:none!important}</style></head><body>' + fs.readFileSync(app, 'utf8') + '</body></html>'), fs.renameSync(wrapped + '.' + process.pid, wrapped);
(async () => {
  const br = await chromium.launch(); const W = +(opt('--w') || 1280);
  const pg = await br.newPage({ viewport: { width: W, height: W < 600 ? 844 : Math.round(W * 0.72) } });
  const errs = []; pg.on('pageerror', e => errs.push(String(e))); pg.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  if (opt('--theme') === 'dark') await pg.emulateMedia({ colorScheme: 'dark' });
  await pg.goto('file://' + wrapped); await pg.evaluate(() => document.fonts.ready);
  await pg.evaluate(l => window.__mipc.lp.preview(l), L);
  const only = opt('--scenes') ? opt('--scenes').split(',').map(Number) : L.scenes.map((s, i) => i);
  const report = [];
  const shoot = async (name) => { const st = await pg.$('#lp-stage'); await st.screenshot({ path: path.join(out, name) }); return name; };
  const layout = () => pg.evaluate(() => {
    const w = [], box = document.querySelector('#lp-scene'), pan = box.querySelector('.sx-panel');
    if (box.scrollHeight > box.clientHeight + 2) w.push(`scene content overflows the stage by ${box.scrollHeight - box.clientHeight}px (text shrunk to ${box.firstElementChild.style.fontSize || '1em'})`);
    if (pan && pan.scrollHeight > pan.clientHeight + 2) w.push(`side panel overflows by ${pan.scrollHeight - pan.clientHeight}px`);
    const fs = box.firstElementChild && box.firstElementChild.style.fontSize; if (fs && parseFloat(fs) < 0.85) w.push(`text had to shrink to ${fs} to fit: too much text`);
    const cap = document.querySelector('#lp-cap'); if (cap && !cap.hidden) { const c = cap.getBoundingClientRect();
      box.querySelectorAll('button,input,.gx-why,.st-why,.gx-info,.gx-fail,.gx-win').forEach(b => { const r = b.getBoundingClientRect(); if (r.width && r.left < c.right && r.right > c.left && r.top < c.bottom && r.bottom > c.top) w.push(`the caption bar covers "${(b.textContent || b.className).trim().slice(0, 40)}"`); }); }
    return w; });
  for (const si of only) {
    const sc = L.scenes[si], gate = ['quiz', 'swipe', 'sort', 'explore', 'slider', 'choice'].includes(sc.type);
    const nb = sc.beats.length;
    await pg.evaluate(([si, bi]) => window.__mipc.lp.jump(si, bi), [si, gate ? nb - 1 : null]);
    await pg.evaluate(() => window.__mipc.lp.pause());
    await pg.waitForTimeout(900);
    await pg.evaluate(() => { const s = document.querySelector('#lp-stage'); s.classList.remove('sk-paused'); s.classList.add('sk-static'); s.querySelectorAll('.gx-card .sk-el').forEach(e => e.classList.add('in')); });
    await pg.waitForTimeout(100);
    const shots = [await shoot(`${L.id}-s${String(si).padStart(2, '0')}-${sc.type}.png`)];
    const warn = await layout();
    const boxes = await pg.evaluate(() => window.__mipc.lp.boxes());
    if (sc.draw && boxes[0]) {
      const els = sc.draw, bb = boxes[0], dims = { sketch: [160, 72], explore: [160, 72], title: [90, 72], choice: [160, 58] }[sc.type] || [80, 72];
      const solid = bb.filter(b => !['arrow', 'ring', 'xout', 'line', 'divider', 'box'].includes(b.p));
      for (const b of bb) { if (b.missing) warn.push(`draw[${b.i}] (${b.p}): unknown prop`); if (b.bb[0] < -1 || b.bb[1] < -1 || b.bb[2] > dims[0] + 1 || b.bb[3] > dims[1] + 1) warn.push(`draw[${b.i}] (${b.id || b.p}) goes off the ${dims[0]}x${dims[1]} canvas: [${b.bb.join(', ')}]`); }
      for (let i = 0; i < solid.length; i++) for (let j = i + 1; j < solid.length; j++) {
        const a = solid[i].bb, c = solid[j].bb, ea = els[solid[i].i], ec = els[solid[j].i];
        if (ea.over || ec.over) continue;
        if ((ea.out != null && ea.out <= (ec.at || 0)) || (ec.out != null && ec.out <= (ea.at || 0))) continue;
        const ix = Math.max(0, Math.min(a[2], c[2]) - Math.max(a[0], c[0])), iy = Math.max(0, Math.min(a[3], c[3]) - Math.max(a[1], c[1]));
        const small = Math.min((a[2] - a[0]) * (a[3] - a[1]), (c[2] - c[0]) * (c[3] - c[1])) || 1;
        if (ix * iy / small > 0.12) warn.push(`draw[${solid[i].i}] (${solid[i].id || solid[i].p}) and draw[${solid[j].i}] (${solid[j].id || solid[j].p}) overlap ${Math.round(ix * iy / small * 100)}% (set "over": true on one if intended)`);
      }
    }
    if (args.includes('--states') && sc.type === 'choice') {
      const order = sc.options.map((o, k) => k).sort((a, b) => (sc.options[a].ok ? 1 : 0) - (sc.options[b].ok ? 1 : 0));
      for (const k of order) {
        await pg.evaluate(([si, bi]) => window.__mipc.lp.jump(si, bi), [si, nb - 1]); await pg.evaluate(() => window.__mipc.lp.pause());
        await pg.evaluate(k => window.__mipc.lp.choose(k), k); await pg.waitForTimeout(80);
        await pg.evaluate(([si, k]) => { const tm = window.__mipc.lp.tm(si); const seg = tm.ob[k]; window.__mipc.lp.seek(seg[seg.length - 1][1] + 0.4); }, [si, k]);
        await pg.waitForTimeout(150); await pg.evaluate(() => window.__mipc.lp.pause()); await pg.waitForTimeout(700);
        await pg.evaluate(() => { const s = document.querySelector('#lp-stage'); s.classList.remove('sk-paused'); s.classList.add('sk-static'); });
        shots.push(await shoot(`${L.id}-s${String(si).padStart(2, '0')}-choice-opt${k}${sc.options[k].ok ? '-win' : '-fail'}.png`));
        warn.push(...(await layout()).map(w => `option ${k}: ` + w));
        if (!sc.options[k].ok) await pg.evaluate(() => window.__mipc.lp.retry());
      }
    }
    else if (args.includes('--states')) {
      if (gate) { await pg.evaluate(() => { const b = document.querySelector('[data-act="lp-skip"]'); if (b) b.click(); }); await pg.waitForTimeout(150); await pg.evaluate(() => window.__mipc.lp.pause()); await pg.evaluate(si => { const T = window.__mipc.lp.state(); }, si);
        await pg.evaluate(([si]) => { const st = window.__mipc.lp; }, [si]); await pg.waitForTimeout(300); shots.push(await shoot(`${L.id}-s${String(si).padStart(2, '0')}-${sc.type}-answers.png`)); }
      else if (sc.draw && nb > 1) { await pg.evaluate(([si]) => window.__mipc.lp.jump(si, 0), [si]); await pg.evaluate(() => window.__mipc.lp.pause()); await pg.waitForTimeout(400); await pg.evaluate(() => { const s = document.querySelector('#lp-stage'); s.classList.remove('sk-paused'); s.classList.add('sk-static'); }); shots.push(await shoot(`${L.id}-s${String(si).padStart(2, '0')}-${sc.type}-beat0.png`)); }
    }
    report.push({ scene: si, type: sc.type, shots, warnings: warn });
  }
  console.log(JSON.stringify({ lesson: L.id, errors: errs, scenes: report }, null, 1));
  await br.close();
})();
