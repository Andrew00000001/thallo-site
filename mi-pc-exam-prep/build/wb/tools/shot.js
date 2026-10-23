// Render a sketch spec to PNG and report layout problems.
// node shot.js <spec.json|-> <out.png> [--theme dark] [--px 8]     spec: {w,h,elements} or [elements]
// node shot.js --gallery <out.png> [--theme dark] [--cols 6] [--only a,b,c]
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
const fs = require('fs'), path = require('path');
const args = process.argv.slice(2), opt = k => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : null; };
const LAB = 'file://' + path.join(__dirname, '..', opt('--lab') || 'lab.html');
(async () => {
  const br = await chromium.launch(); const pg = await br.newPage({ deviceScaleFactor: 1 });
  const errs = []; pg.on('pageerror', e => errs.push(String(e))); pg.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  if (opt('--theme') === 'dark') await pg.emulateMedia({ colorScheme: 'dark' });
  await pg.goto(LAB); await pg.evaluate(() => document.fonts.ready);
  const px = +(opt('--px') || 8);
  if (args[0] === '--gallery') {
    let names = await pg.evaluate(() => propList()); const only = opt('--only'); if (only) names = only.split(',');
    const list = names.map(n => ({ p: n }));
    await pg.setViewportSize({ width: (+(opt('--cols') || 6)) * 44 * px, height: 800 });
    await pg.evaluate(([l, px, c]) => renderGallery(l, px, c), [list, px, +(opt('--cols') || 6)]);
    const st = await pg.$('#stage'); await st.screenshot({ path: args[1] });
    console.log(JSON.stringify({ props: names.length, errors: errs }));
  } else {
    const spec = JSON.parse(args[0] === '-' ? fs.readFileSync(0, 'utf8') : fs.readFileSync(args[0], 'utf8'));
    const w = spec.w || 160, h = spec.h || 80;
    await pg.setViewportSize({ width: w * px, height: h * px });
    const bb = await pg.evaluate(([s, px]) => renderScene(s, px), [spec, px]);
    await pg.waitForTimeout(50);
    const st = await pg.$('#stage'); await st.screenshot({ path: args[1] });
    const warn = [];
    const solid = bb.filter(b => !['arrow', 'ring', 'xout', 'line', 'divider', 'box'].includes(b.p));
    for (const b of bb) {
      if (b.missing) warn.push(`element ${b.i} (${b.p}): unknown prop`);
      if (b.bb[0] < -1 || b.bb[1] < -1 || b.bb[2] > w + 1 || b.bb[3] > h + 1) warn.push(`element ${b.i} (${b.id || b.p}) goes off the canvas: [${b.bb.join(', ')}]`);
    }
    const els = spec.elements || spec;
    for (let i = 0; i < solid.length; i++) for (let j = i + 1; j < solid.length; j++) {
      const a = solid[i].bb, c = solid[j].bb, ea = els[solid[i].i], ec = els[solid[j].i];
      if (ea.over || ec.over) continue;
      if ((ea.out != null && ea.out <= (ec.at || 0)) || (ec.out != null && ec.out <= (ea.at || 0))) continue;
      const ix = Math.max(0, Math.min(a[2], c[2]) - Math.max(a[0], c[0])), iy = Math.max(0, Math.min(a[3], c[3]) - Math.max(a[1], c[1]));
      const small = Math.min((a[2] - a[0]) * (a[3] - a[1]), (c[2] - c[0]) * (c[3] - c[1])) || 1;
      if (ix * iy / small > 0.12) warn.push(`elements ${solid[i].i} (${solid[i].id || solid[i].p}) and ${solid[j].i} (${solid[j].id || solid[j].p}) overlap ${Math.round(ix * iy / small * 100)}%`);
    }
    console.log(JSON.stringify({ warnings: warn, errors: errs, boxes: bb.map(b => `${b.i}:${b.id || b.p} [${b.bb.join(',')}]`) }));
  }
  await br.close();
})();
