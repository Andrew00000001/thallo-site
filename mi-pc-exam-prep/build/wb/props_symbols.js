/* ---------- Sketch props: symbols, charts, games of chance and weather perils ----------
   Same contract as props_core.js: {w, h, dh, anchors?, draw(c, opt, el)}; draw in the prop's own w x h box.
   Variants are listed in the one-line comment above each prop. */
(()=>{
const P = SK.PROPS;

/* helpers */
const rad = d => d*Math.PI/180;
const back = () => ({fill:'paper', fs:'solid', nostroke:true});           // paper underlay: hides what is behind a hatched shape
function sPoly(c, pts, o){ c.poly(pts, back()); c.poly(pts, o); }
function sRect(c, x, y, w, h, o){ c.rect(x, y, w, h, back()); c.rect(x, y, w, h, o); }
function sRR(c, x, y, w, h, r, o){ c.rrect(x, y, w, h, r, back()); c.rrect(x, y, w, h, r, o); }
function sBlob(c, pts, o){ c.blob(pts, back()); c.blob(pts, o); }
function sCirc(c, cx, cy, d, o){ c.circle(cx, cy, d, back()); c.circle(cx, cy, d, o); }
function rot(pts, cx, cy, deg){ const a=rad(deg), co=Math.cos(a), si=Math.sin(a); return pts.map(([x,y])=>[cx+(x-cx)*co-(y-cy)*si, cy+(x-cx)*si+(y-cy)*co]); }
function rbox(cx, cy, w, h, deg){ return rot([[cx-w/2,cy-h/2],[cx+w/2,cy-h/2],[cx+w/2,cy+h/2],[cx-w/2,cy+h/2]], cx, cy, deg||0); }
function star(cx, cy, R, r, n, a0){ const pts=[]; for(let i=0;i<2*n;i++){ const a=rad((a0==null?-90:a0)+i*180/n), q=i%2?r:R; pts.push([cx+q*Math.cos(a), cy+q*Math.sin(a)]); } return pts; }
function sector(cx, cy, r, a0, a1){ const pts=[[cx,cy]], n=Math.max(2, Math.round((a1-a0)/12)); for(let i=0;i<=n;i++){ const a=rad(a0+(a1-a0)*i/n); pts.push([cx+r*Math.cos(a), cy+r*Math.sin(a)]); } return pts; }
function arcPts(cx, cy, rx, ry, a0, a1, step){ const pts=[], n=Math.max(1, Math.round(Math.abs(a1-a0)/(step||15))); for(let i=0;i<=n;i++){ const a=rad(a0+(a1-a0)*i/n); pts.push([cx+rx*Math.cos(a), cy+ry*Math.sin(a)]); } return pts; }
function stadium(cx, cy, len, th, deg){ const r=th/2, hl=len/2-r, pts=[];
  for(let a=-90;a<=90;a+=30) pts.push([cx+hl+r*Math.cos(rad(a)), cy+r*Math.sin(rad(a))]);
  for(let a=90;a<=270;a+=30) pts.push([cx-hl+r*Math.cos(rad(a)), cy+r*Math.sin(rad(a))]);
  return rot(pts, cx, cy, deg||0); }
function thick(pts, w){ // outline polygon around a polyline (round caps): turns a pen path into a fat "balloon" stroke
  const n=pts.length, h=w/2, L=[], R=[], dir=i=>{ const a=pts[Math.max(0,i-1)], b=pts[Math.min(n-1,i+1)]; const dx=b[0]-a[0], dy=b[1]-a[1], l=Math.hypot(dx,dy)||1; return [dx/l, dy/l]; };
  for(let i=0;i<n;i++){ const [dx,dy]=dir(i); L.push([pts[i][0]-dy*h, pts[i][1]+dx*h]); R.push([pts[i][0]+dy*h, pts[i][1]-dx*h]); }
  const cap=(p, th0)=>{ const out=[]; for(let k=1;k<6;k++){ const t=rad(th0-180*k/6); out.push([p[0]+h*Math.cos(t), p[1]+h*Math.sin(t)]); } return out; };
  const de=dir(n-1), d0=dir(0), te=Math.atan2(de[1],de[0])*180/Math.PI, t0=Math.atan2(d0[1],d0[0])*180/Math.PI;
  return L.concat(cap(pts[n-1], te+90), R.slice().reverse(), cap(pts[0], t0-90));
}
function roundPoly(pts, r){ // polygon with rounded corners
  const out=[], n=pts.length;
  for(let i=0;i<n;i++){ const p=pts[(i+n-1)%n], v=pts[i], q=pts[(i+1)%n];
    const u1=[p[0]-v[0], p[1]-v[1]], u2=[q[0]-v[0], q[1]-v[1]], l1=Math.hypot(...u1)||1, l2=Math.hypot(...u2)||1, rr=Math.min(r, l1/2.2, l2/2.2);
    const a=[v[0]+u1[0]/l1*rr, v[1]+u1[1]/l1*rr], b=[v[0]+u2[0]/l2*rr, v[1]+u2[1]/l2*rr];
    for(let k=0;k<=3;k++){ const t=k/3, m=1-t; out.push([m*m*a[0]+2*m*t*v[0]+t*t*b[0], m*m*a[1]+2*m*t*v[1]+t*t*b[1]]); } }
  return out;
}
function arrowHead(c, tip, from, len, o){ const ang=Math.atan2(tip[1]-from[1], tip[0]-from[0]);
  c.poly([[tip[0]-len*Math.cos(ang-0.5), tip[1]-len*Math.sin(ang-0.5)], tip, [tip[0]-len*Math.cos(ang+0.5), tip[1]-len*Math.sin(ang+0.5)]], Object.assign({open:true, rough:0.5}, o)); }
function fitText(s, maxW, maxSize){ const w=SK.tw(s,1)||0.5*String(s).length; return Math.min(maxSize, maxW/Math.max(w,0.1)); }
const CYC = ['blue','orange','green','red','purple','teal','pink','yellow'];
const TINY = 0.9;   // c.k below this = drawn very small (e.g. held in a person's hand): flat fills, single thin strokes
const tiny = c => c.k < TINY;
const tf = (col, o) => Object.assign({fill:col, fs:'solid', cls:'thin', single:true, rough:0.5}, o);   // tiny-mode flat fill
const tl = o => Object.assign({cls:'thin', single:true, rough:0.4}, o);                                 // tiny-mode line
const tn = col => ({fill:col, fs:'solid', nostroke:true, rough:0.4});                                   // tiny-mode fill only

/* ---------- Chance and luck ---------- */

// dice: a pair of dice. o.a / o.b: front-face values 1-6 (default 5 and 3), o.color: body color (default white with ink pips; a color = colored dice with white pips)
const PIPS = {1:[[.5,.5]], 2:[[.27,.27],[.73,.73]], 3:[[.27,.27],[.5,.5],[.73,.73]], 4:[[.27,.27],[.73,.27],[.27,.73],[.73,.73]],
  5:[[.27,.27],[.73,.27],[.5,.5],[.27,.73],[.73,.73]], 6:[[.28,.25],[.72,.25],[.28,.5],[.72,.5],[.28,.75],[.72,.75]]};
function die(c, x, y, s, ang, v, tv, col){
  const d=s*0.32, cx=x+s/2, cy=y+s/2, R=pts=>rot(pts, cx, cy, ang);
  sPoly(c, R([[x+s,y],[x+s+d,y-d],[x+s+d,y+s-d],[x+s,y+s]]), col?{fill:col, gap:4}:{fill:'gray', gap:5, cls:'soft'});
  sPoly(c, R([[x,y],[x+d,y-d],[x+s+d,y-d],[x+s,y]]), col?{fill:col, gap:7, cls:'soft'}:{fill:'paper', fs:'solid'});
  sPoly(c, R([[x,y],[x+s,y],[x+s,y+s],[x,y+s]]), col?{fill:col, gap:7}:{fill:'paper', fs:'solid'});
  const pip=col?{fill:'paper', fs:'solid', rough:0.3, cls:'thin', single:true}:{fill:'ink', fs:'solid', color:'ink', rough:0.3, single:true, cls:'thin'};
  (PIPS[v]||PIPS[5]).forEach(([u,w])=>{ const p=R([[x+u*s, y+w*s]])[0]; if(col) c.circle(p[0], p[1], s*0.2, pip); else c.dot(p[0], p[1], s*0.17); });
  (PIPS[tv]||[]).forEach(([u,w])=>{ const p=R([[x+u*s+(1-w)*d, y-(1-w)*d]])[0]; c.ellipse(p[0], p[1], s*(col?0.18:0.15), s*(col?0.1:0.08), pip); });
}
P.dice = {w:84, h:58, dh:12, draw(c,o){
  if(tiny(c)){ [[46,22,26,14,+o.b||3],[6,22,29,-9,+o.a||5]].forEach(([x,y,s,ang,v])=>{ const d=s*0.32, R=p=>rot(p, x+s/2, y+s/2, ang);
    c.poly(R([[x,y],[x+d,y-d],[x+s+d,y-d],[x+s+d,y+s-d],[x+s,y+s],[x,y+s]]), tf(o.color||'paper')); c.poly(R([[x+s+0.8,y],[x+s+d-0.5,y-d+1],[x+s+d-0.5,y+s-d],[x+s+0.8,y+s-0.8]]), tn('gray'));
    (PIPS[v]||PIPS[5]).forEach(([u,w])=>{ const q=R([[x+u*s, y+w*s]])[0]; c.dot(q[0], q[1], s*0.2, {color:o.color?'paper':'ink'}); }); }); return; }
  die(c, 46, 22, 26, 14, +o.b||3, 2, o.color);
  die(c, 6, 22, 29, -9, +o.a||5, 1, o.color);
}};

// coin: one big coin, slightly turned so its edge shows. o.sym (symbol on the face, default '$'), o.color (metal: 'yellow' gold (default), 'gray' silver, 'brown' copper)
P.coin = {w:54, h:52, dh:10, draw(c,o){
  const col=o.color||'yellow', ec=col==='yellow'?'orange':col;
  if(tiny(c)){ c.circle(29.5, 27, 44, tf(ec)); c.circle(25, 25, 46, tf(col)); c.text(25, 35, o.sym||'$', {size:fitText(o.sym||'$', 24, 29), color:col==='yellow'?'orange':'ink', bold:true}); return; }
  c.ellipse(29.5, 27, 44, 47, back()); c.ellipse(29.5, 27, 44, 47, {fill:ec, gap:4});
  sCirc(c, 25, 25, 46, {fill:col, gap:7});
  c.circle(25, 25, 34, {cls:'thin', color:ec, rough:0.5});
  const s=o.sym||'$';
  c.text(25, 35, s, {size:fitText(s, 24, 29), color:col==='yellow'?'orange':'ink', bold:true});
}};

// lottery: lottery ticket with a torn-off stub, a title and number balls. o.title (default 'LOTTO'), o.nums (up to 4 short strings, default ['7','21','3','9']), o.color (stub and balls, default 'orange')
P.lottery = {w:86, h:50, dh:10, draw(c,o){
  const col=o.color||'orange', t=o.title||'LOTTO', nums=(o.nums||['7','21','3','9']).slice(0,4);
  if(tiny(c)){ c.rect(2, 4, 82, 42, tf('paper')); c.rect(3, 5, 19, 40, tn(col)); c.line(32, 17, 74, 17, tl({color:'red', cls:''})); [38,53,68].forEach(x=>c.circle(x, 33, 11, tf('paper', {color:col}))); return; }
  c.rect(2, 4, 82, 42, back());
  c.rect(2, 4, 20, 42, {fill:col, gap:5, nostroke:true, cls:'soft'});
  c.rect(2, 4, 82, 42, {rough:0.7});
  for(let y=6.5;y<44;y+=5) c.line(22, y, 22, y+2.4, {cls:'thin', rough:0.3, single:true});
  c.poly(star(12, 25, 8.5, 3.6, 5), {fill:'yellow', fs:'solid', rough:0.4});
  c.text(53, 19.5, t, {size:fitText(t, 52, 12.5), color:'red', bold:true});
  const sp=55/nums.length;
  nums.forEach((n,i)=>{ const x=26+sp*(i+0.5); c.circle(x, 34, 12, {fill:'paper', fs:'solid', color:col, rough:0.5}); c.text(x, 36.6, n, {size:fitText(n, 8.5, 7)}); });
}};

// seesaw: balance beam on a triangle pivot (trade-off, balance). o.tilt: -1 (left end down), 0 (level, default), 1 (right end down);
//   o.left / o.right: prop name sitting on that end (e.g. 'person', 'money', 'house'), o.leftOpt / o.rightOpt, o.size (their height, default 22), o.color (pivot, default 'gray')
P.seesaw = {w:100, h:56, dh:14, draw(c,o){
  const t=Math.max(-1, Math.min(1, +o.tilt||0)), ang=t*13, cx=50, cy=27.5, ca=Math.cos(rad(ang)), sa=Math.sin(rad(ang)), sz=o.size||22;
  sPoly(c, [[50,29],[37,53],[63,53]], {fill:o.color||'gray', gap:6});
  c.line(30, 53, 70, 53, {rough:0.5});
  [[-1,o.left,o.leftOpt],[1,o.right,o.rightOpt]].forEach(([s,item,io])=>{ if(!item) return; const px=cx+s*36*ca, py=cy+s*36*sa, off=2.2+sz/2; c.sub(px+sa*off, py-ca*off, sz, item, io||{}); });
  sPoly(c, rbox(cx, cy, 96, 5, ang), {fill:'brown', gap:5});
  c.dot(cx, cy, 4);
}};

/* ---------- Charts and numbers ---------- */

// piechart: pie chart. o.slices: list of percentages (default [50,30,20]), o.colors: slice colors (default cycles blue, orange, green, red, purple, teal, pink, yellow),
//   o.pop: index of one slice pulled out of the pie
P.piechart = {w:60, h:60, dh:14, draw(c,o){
  const sl=(o.slices&&o.slices.length?o.slices:[50,30,20]).map(v=>Math.max(0,+v||0)), tot=sl.reduce((a,b)=>a+b,0)||1, cols=o.colors||CYC, cx=30, cy=30, r=26;
  let a=-90; const segs=sl.map((v,i)=>{ const a0=a; a+=v/tot*360; return {a0, a1:a, col:cols[i%cols.length], i}; }).filter(s=>s.a1-s.a0>0.5);
  const hat=s=>({fill:s.col, gap:5.5, angle:s.i%2?41:-41});
  if(tiny(c)){ segs.forEach(s=>c.poly(sector(cx, cy, r, s.a0, s.a1), tn(s.col))); c.circle(cx, cy, 2*r, tl({cls:''})); return; }
  if(o.pop==null){
    c.circle(cx, cy, 2*r, back());
    segs.forEach(s=>c.poly(sector(cx, cy, r, s.a0, s.a1), Object.assign(hat(s), {nostroke:true})));
    if(segs.length>1) segs.forEach(s=>c.line(cx, cy, cx+r*Math.cos(rad(s.a0)), cy+r*Math.sin(rad(s.a0)), {rough:0.5}));
    c.circle(cx, cy, 2*r, {});
  } else segs.forEach(s=>{ const m=rad((s.a0+s.a1)/2), off=s.i===+o.pop?5:0; sPoly(c, sector(cx+off*Math.cos(m), cy+off*Math.sin(m), r-2, s.a0, s.a1), Object.assign(hat(s), {rough:0.6})); });
}};

// barchart: bar chart on axes. o.values: bar heights 0-100 (default [30,55,45,85]), o.color: one color for every bar (default cycles blue, green, orange, purple, red, teal),
//   o.trend: 'up' | 'down' (a trend arrow over the bars)
const BARC = ['blue','green','orange','purple','red','teal'];
P.barchart = {w:70, h:60, dh:14, draw(c,o){
  const v=(o.values&&o.values.length?o.values:[30,55,45,85]).map(x=>Math.max(0, Math.min(100, +x||0))), n=v.length, x0=12, x1=66, y0=56, H=44, slot=(x1-x0)/n, bw=slot*0.64;
  if(tiny(c)){ v.forEach((h,i)=>{ const x=x0+slot*i+(slot-bw)/2, bh=Math.max(0.6, h/100*H); c.rect(x, y0-bh, bw, bh, tn(o.color||BARC[i%BARC.length])); }); c.poly([[8,4],[8,y0],[68,y0]], tl({open:true, cls:''})); return; }
  v.forEach((h,i)=>{ const x=x0+slot*i+(slot-bw)/2, bh=Math.max(0.6, h/100*H); sRect(c, x, y0-bh, bw, bh, {fill:o.color||BARC[i%BARC.length], gap:5.5, rough:0.6}); });
  c.line(8, 4, 8, y0, {rough:0.6}); c.line(8, y0, 68, y0, {rough:0.6});
  if(o.trend){ const up=o.trend!=='down', a=up?[14,40]:[14,8], b=up?[64,4]:[64,40], col=up?'green':'red';
    c.curve([a, [(a[0]+b[0])/2, (a[1]+b[1])/2+(up?4:-4)], b], {color:col, cls:'bold'}); arrowHead(c, b, [(a[0]+b[0])/2+8, (a[1]+b[1])/2+(up?3:-3)], 8, {color:col, cls:'bold'}); }
}};

// percent: a big % sign in a ring (rates, interest, discount). o.color (ring, default 'green')
P.percent = {w:52, h:52, dh:10, draw(c,o){
  if(tiny(c)){ c.circle(26, 26, 48, tf(o.color||'green')); c.circle(26, 26, 33, tn('paper')); c.line(33, 15, 19, 37, tl({cls:''})); c.circle(19.5, 18.5, 8, tl()); c.circle(32.5, 33.5, 8, tl()); return; }
  sCirc(c, 26, 26, 48, {fill:o.color||'green', gap:5});
  c.circle(26, 26, 35, {fill:'paper', fs:'solid'});
  c.line(34, 14, 18, 38, {cls:'bold'});
  c.circle(19, 18, 8.5, {cls:'bold', rough:0.4}); c.circle(33, 34, 8.5, {cls:'bold', rough:0.4});
}};

// stairs: steps rising to the right (growth, step by step, climbing the ladder). o.n (steps, default 4), o.color (default 'blue'),
//   o.flag (goal flag on the top step), o.arrow (rising arrow above the steps)
P.stairs = {w:80, h:64, dh:14, draw(c,o){
  const n=Math.max(2, Math.min(8, o.n||4)), x0=5, x1=75, yb=60, top=o.flag||o.arrow?22:8, sw=(x1-x0)/n, sh=(yb-top)/n, pts=[[x0,yb]];
  for(let i=0;i<n;i++){ pts.push([x0+i*sw, yb-(i+1)*sh], [x0+(i+1)*sw, yb-(i+1)*sh]); }
  pts.push([x1, yb]);
  if(tiny(c)){ c.poly(pts, tf(o.color||'blue')); return; }
  sPoly(c, pts, {fill:o.color||'blue', gap:7});
  for(let i=1;i<n;i++) c.line(x0+i*sw, yb-i*sh, x0+i*sw, yb, {cls:'thin', rough:0.4});
  if(o.flag){ const fx=x1-sw/2, fy=yb-n*sh; c.line(fx, fy, fx, fy-20, {}); c.poly([[fx,fy-20],[fx+13,fy-16],[fx,fy-12]], {fill:'red', fs:'solid', rough:0.4}); }
  if(o.arrow){ const a=[x0+2, yb-sh-12], b=[x1-(o.flag?sw:4), top-14]; c.curve([a, [(a[0]+b[0])/2-4, (a[1]+b[1])/2+2], b], {color:'green', cls:'bold'}); arrowHead(c, b, [(a[0]+b[0])/2, (a[1]+b[1])/2], 8, {color:'green', cls:'bold'}); }
}};

/* ---------- Ideas, goals and rewards ---------- */

// gears: two meshing gears (machinery, process, "how it works"). o.n: 1 or 2 gears (default 2), o.color / o.color2 (default 'gray' / 'orange')
function gear(cx, cy, R, n, dep, ph){ const pts=[], st=360/n, ri=R-dep;
  for(let i=0;i<n;i++){ const a=ph+i*st; [[-0.5,ri],[-0.23,ri],[-0.13,R],[0.13,R],[0.23,ri]].forEach(([f,r])=>{ const t=rad(a+f*st); pts.push([cx+r*Math.cos(t), cy+r*Math.sin(t)]); }); }
  return pts; }
P.gears = {w:66, h:62, dh:12, draw(c,o){
  if(tiny(c)){ const one=o.n===1, g=one?[33,31,28]:[26,36,23]; if(!one) c.poly(gear(49.4, 14.9, 14, 7, 5, 138), tf(o.color2||'orange')); c.poly(gear(g[0], g[1], g[2], 10, 7, -60), tf(o.color||'gray')); c.circle(g[0], g[1], 12, tn('paper')); return; }
  if(o.n===1){ sPoly(c, gear(33, 31, 28, 10, 7, -90), {fill:o.color||'gray', gap:6, rough:0.6}); c.circle(33, 31, 20, {fill:'paper', fs:'solid'}); c.dot(33, 31, 7); return; }
  sPoly(c, gear(26, 36, 23, 10, 6, -60), {fill:o.color||'gray', gap:6, rough:0.6});
  c.circle(26, 36, 16, {fill:'paper', fs:'solid'}); c.dot(26, 36, 6);
  sPoly(c, gear(49.4, 14.9, 14, 7, 5, 138), {fill:o.color2||'orange', gap:5, rough:0.6});
  c.circle(49.4, 14.9, 9, {fill:'paper', fs:'solid'}); c.dot(49.4, 14.9, 3.5);
}};

// lightbulb: light bulb (idea, insight). o.off (unlit: no glow or rays), o.color (glow, default 'yellow')
P.lightbulb = {w:56, h:70, dh:14, draw(c,o){
  const on=!o.off, glass=arcPts(28, 25, 18, 18, 140, 400, 20).concat([[35,42],[34,48],[22,48],[21,42]]);
  if(tiny(c)){ if(on) [-150,-90,-30].forEach(a=>{ const t=rad(a); c.line(28+24*Math.cos(t), 25+24*Math.sin(t), 28+31*Math.cos(t), 25+31*Math.sin(t), tl({color:'orange', cls:''})); }); c.blob(glass, tf(on?(o.color||'yellow'):'paper')); c.rect(21, 47, 14, 12, tf('gray')); return; }
  if(on) for(let a=-180;a<=0;a+=30){ const t=rad(a); c.line(28+23*Math.cos(t), 25+23*Math.sin(t), 28+30*Math.cos(t), 25+30*Math.sin(t), {color:'orange', rough:0.5}); }
  sBlob(c, glass, on?{fill:o.color||'yellow', gap:6}:{});
  c.poly([[24,47],[24,36],[26,30],[28,35],[30,30],[32,36],[32,47]], {open:true, cls:'thin', color:on?'orange':'gray', rough:0.4});
  sRR(c, 21, 47, 14, 12, 2, {fill:'gray', gap:4});
  c.line(21.5, 51, 34.5, 51, {cls:'thin', rough:0.3}); c.line(21.5, 55, 34.5, 55, {cls:'thin', rough:0.3});
  c.arc(28, 59, 8, 7, 0, 180, {closed:true, fill:'ink', fs:'solid', rough:0.4});
  if(on) c.arc(28, 25, 22, 22, 200, 250, {cls:'thin', color:'paper', rough:0.4});
}};

// target: archery bullseye with an arrow stuck in it (goal, aim). o.arrow (default true), o.miss (arrow lands in the outer ring instead), o.color (rings, default 'red')
P.target = {w:64, h:62, dh:14, draw(c,o){
  const col=o.color||'red', cx=27, cy=35;
  if(tiny(c)){ c.circle(cx, cy, 52, tf(col)); c.circle(cx, cy, 34, tn('paper')); c.circle(cx, cy, 17, tn(col)); if(o.arrow!==false){ const H=o.miss?[cx+21,cy+18]:[cx,cy]; c.line(H[0], H[1], H[0]+22, H[1]-20, tl({cls:''})); c.circle(H[0]+22, H[1]-20, 9, tn('yellow')); } return; }
  sCirc(c, cx, cy, 52, {fill:col, gap:5});
  c.circle(cx, cy, 38, {fill:'paper', fs:'solid'});
  c.circle(cx, cy, 24, {fill:col, gap:4});
  c.circle(cx, cy, 10, {fill:col, fs:'solid', rough:0.4});
  if(o.arrow===false) return;
  const H=o.miss?[cx+21, cy+18]:[cx, cy], u=[0.73,-0.68], n=[0.68,0.73], ln=o.miss?24:34, T=[H[0]+u[0]*ln, H[1]+u[1]*ln], f=(t,s)=>[T[0]+u[0]*t+n[0]*s, T[1]+u[1]*t+n[1]*s];
  c.line(H[0], H[1], T[0], T[1], {cls:'bold', rough:0.4});
  c.poly([f(1,0), f(-9,0), f(-6,6), f(4,6)], {fill:'yellow', fs:'solid', rough:0.4});
  c.poly([f(1,0), f(-9,0), f(-6,-6), f(4,-6)], {fill:'yellow', fs:'solid', rough:0.4});
  if(o.miss) [[-5,4,-9,7],[0,6,0,11],[5,4,9,7]].forEach(([a,b,d,e])=>c.line(H[0]+a, H[1]+b, H[0]+d, H[1]+e, {cls:'thin', rough:0.4}));
}};

// trophy: winner's cup on a stand. o.color (metal, default 'yellow'; 'gray' = silver), o.text (short text on the cup instead of a star, e.g. '#1')
P.trophy = {w:60, h:66, dh:14, draw(c,o){
  const col=o.color||'yellow';
  if(tiny(c)){ c.arc(12, 17, 16, 18, 90, 270, tl({cls:''})); c.arc(48, 17, 16, 18, -90, 90, tl({cls:''})); c.poly(arcPts(30, 6, 19, 32, 0, 180, 15), tf(col)); c.rect(26, 36, 8, 14, tn(col)); c.rect(14, 50, 32, 13, tf('brown')); return; }
  c.arc(12, 17, 16, 18, 90, 270, {cls:'bold'}); c.arc(48, 17, 16, 18, -90, 90, {cls:'bold'});
  sPoly(c, [[27,37],[33,37],[35,49],[25,49]], {fill:col, gap:4});
  sPoly(c, arcPts(30, 6, 19, 32, 0, 180, 15), {fill:col, gap:6});
  c.line(10, 6, 50, 6, {cls:'bold', rough:0.5});
  if(o.text) c.text(30, 22, o.text, {size:fitText(o.text, 20, 12), bold:true});
  else c.poly(star(30, 17, 8, 3.4, 5), {fill:'paper', fs:'solid', rough:0.4});
  sRR(c, 19, 48, 22, 6, 2, {fill:col, gap:4});
  sRect(c, 14, 54, 32, 10, {fill:'brown', gap:5});
}};

// medal: medal on a two-colored ribbon. o.color (metal, default 'yellow'), o.ribbon ([left, right] colors, default ['blue','red']), o.n (short text on the medal instead of a star, e.g. '1')
P.medal = {w:46, h:70, dh:14, draw(c,o){
  const rb=o.ribbon||['blue','red'], col=o.color||'yellow';
  if(tiny(c)){ c.poly([[30,2],[42,2],[28,40],[19,36]], tn(rb[1])); c.poly([[4,2],[16,2],[27,36],[18,40]], tn(rb[0])); c.circle(23, 51, 32, tf(col)); return; }
  sPoly(c, [[30,2],[42,2],[28,40],[19,36]], {fill:rb[1], gap:5});
  sPoly(c, [[4,2],[16,2],[27,36],[18,40]], {fill:rb[0], gap:5});
  sCirc(c, 23, 51, 32, {fill:col, gap:5});
  c.circle(23, 51, 21, {cls:'thin', color:col==='yellow'?'orange':'ink', rough:0.4});
  if(o.n!=null) c.text(23, 56.5, String(o.n), {size:fitText(String(o.n), 14, 15), bold:true});
  else c.poly(star(23, 51.5, 8, 3.4, 5), {fill:'paper', fs:'solid', rough:0.4});
}};

// star: five-point star (rating, quality, favorite). o.color (default 'yellow'), o.empty (outline only, e.g. a missing rating star)
P.star = {w:50, h:48, dh:10, draw(c,o){
  const pts=star(25, 26.5, 24, 10, 5);
  if(tiny(c)){ c.poly(pts, tf(o.empty?'paper':(o.color||'yellow'))); return; }
  if(o.empty) c.poly(pts, {fill:'paper', fs:'solid', rough:0.6}); else sPoly(c, pts, {fill:o.color||'yellow', gap:5, rough:0.6});
}};

// heart: heart (love, health, care). o.color (default 'red'), o.broken (cracked in two halves)
function heartPt(t){ const x=16*Math.pow(Math.sin(t),3), y=13*Math.cos(t)-5*Math.cos(2*t)-2*Math.cos(3*t)-Math.cos(4*t); return [26+1.42*x, 4+(12-y)*1.4]; }
P.heart = {w:52, h:48, dh:10, draw(c,o){
  const col=o.color||'red', N=28, pts=t0=>{ const out=[]; for(let i=0;i<=N/2;i++) out.push(heartPt(t0+i*2*Math.PI/N)); return out; };
  if(tiny(c) && !o.broken){ const all=[]; for(let i=0;i<N;i++) all.push(heartPt(i*2*Math.PI/N)); c.poly(all, tf(col)); return; }
  if(!o.broken){ const all=[]; for(let i=0;i<N;i++) all.push(heartPt(i*2*Math.PI/N)); sPoly(c, all, {fill:col, gap:5, rough:0.6}); return; }
  const zig=[[26,10.8],[22,18],[29,25],[23,32],[27,38],[26,44.6]];
  sPoly(c, rot(pts(Math.PI).concat(zig.slice(1,-1)), 26, 44, -7).map(([x,y])=>[x-2.5,y]), {fill:col, gap:5, rough:0.6});
  sPoly(c, rot(pts(0).concat(zig.slice(1,-1).reverse()), 26, 44, 7).map(([x,y])=>[x+2.5,y]), {fill:col, gap:5, rough:0.6});
}};

// crown: king's crown (top choice, premium). o.color (default 'yellow')
P.crown = {w:62, h:48, dh:10, draw(c,o){
  const col=o.color||'yellow';
  if(tiny(c)){ c.poly([[7,38],[4,13],[18,26],[31,7],[44,26],[58,13],[55,38]], tf(col)); c.rect(5, 36, 52, 9, tf('orange')); return; }
  sPoly(c, [[7,38],[4,13],[18,26],[31,7],[44,26],[58,13],[55,38]], {fill:col, gap:6, rough:0.6});
  [[4,12],[31,6],[58,12]].forEach(([x,y])=>c.circle(x, y, 7, {fill:col, fs:'solid', rough:0.4}));
  sRR(c, 5, 36, 52, 9, 2, {fill:'orange', gap:4});
  c.dot(17, 40.5, 5, {color:'blue'}); c.dot(31, 40.5, 6, {color:'red'}); c.dot(45, 40.5, 5, {color:'green'});
}};

// puzzle: one jigsaw puzzle piece (fit, missing piece). o.color (default 'blue')
P.puzzle = {w:56, h:56, dh:12, draw(c,o){
  const pts=[[10,14],[23,14]].concat(arcPts(27, 8, 6.5, 6.5, 125, 415, 20), [[31,14],[44,14],[44,27]], arcPts(50, 31, 6.5, 6.5, 215, 505, 20),
    [[44,35],[44,48],[31,48]], arcPts(27, 42, 6, 6, 55, -235, 20), [[23,48],[10,48],[10,35]], arcPts(16, 31, 6, 6, 145, -145, 20), [[10,27]]);
  if(tiny(c)){ c.poly(pts, tf(o.color||'blue')); return; }
  sPoly(c, pts, {fill:o.color||'blue', gap:6, rough:0.5});
}};

// brain: brain, side view (thinking, knowledge, smart choice). o.color (default 'pink')
P.brain = {w:62, h:50, dh:12, draw(c,o){
  const col=o.color||'pink';
  if(tiny(c)){ c.rect(35, 33, 7, 14, tn(col)); c.blob([[8,30],[4,20],[9,10],[19,5],[31,3],[44,4],[54,9],[59,19],[57,28],[50,34],[38,36],[26,38],[15,37]], tf(col)); c.curve([[29,7],[27,14],[33,19],[29,27]], tl()); return; }
  sPoly(c, [[36,33],[43,33],[41,47],[35,47]], {fill:col, gap:4});
  c.ellipse(48, 35, 17, 11, back()); c.ellipse(48, 35, 17, 11, {fill:col, gap:4, rough:0.5});
  c.curve([[41,34.5],[48,36],[55,34]], {cls:'thin', rough:0.4}); c.curve([[42,37.5],[48,39],[54,37.5]], {cls:'thin', rough:0.4});
  sBlob(c, [[8,30],[4,20],[9,10],[19,5],[31,3],[44,4],[54,9],[59,19],[57,28],[50,34],[38,36],[26,38],[15,37]], {fill:col, gap:7, cls:'soft'});
  [[[13,15],[19,18],[16,24],[23,28]], [[29,7],[27,14],[33,19],[29,27],[35,32]], [[42,8],[46,15],[41,21],[47,27]], [[9,26],[14,31],[20,33]], [[51,15],[54,22]]].forEach(p=>c.curve(p, {cls:'thin', rough:0.5}));
}};

// eye: an open eye (watch, notice, inspection). o.color (iris, default 'blue'), o.lashes (default true), o.closed (shut eye)
P.eye = {w:64, h:40, dh:8, draw(c,o){
  const up=[], lo=[];
  for(let i=0;i<=10;i++){ const t=i/10, x=4+56*t, b=4*t*(1-t); up.push([x, 20-16*b]); lo.push([x, 20+14*b]); }
  const lash=(sgn)=>[0.2,0.35,0.5,0.65,0.8].forEach(t=>{ const x=4+56*t, b=4*t*(1-t), y=20+sgn*(sgn<0?16:14)*b, dx=(t-0.5)*9; c.line(x, y+sgn*0.5, x+dx, y+sgn*6.5, {cls:'thin', rough:0.4}); });
  if(o.closed){ c.curve(lo, {}); if(o.lashes!==false) lash(1); return; }
  sPoly(c, up.concat(lo.slice(1,-1).reverse()), {fill:'paper', fs:'solid', rough:0.5});
  c.circle(32, 20, 24, {fill:o.color||'blue', gap:4, rough:0.5});
  c.dot(32, 20, 10); c.dot(36, 16, 4, {color:'paper'});
  c.curve(up, {rough:0.5});
  if(o.lashes!==false) lash(-1);
}};

// magnet: horseshoe magnet, poles pointing right, with pull lines (attraction, drawing customers in). o.lines (pull lines, default true), o.color (default 'red')
P.magnet = {w:66, h:56, dh:12, draw(c,o){
  const pts=[[50,4],[24,4]].concat(arcPts(24, 28, 24, 24, 270, 90, 15), [[50,52],[50,40],[24,40]], arcPts(24, 28, 12, 12, 90, 270, 20), [[50,16]]);
  if(tiny(c)){ c.poly(pts, tf(o.color||'red')); c.rect(40, 5, 10, 10, tn('gray')); c.rect(40, 41, 10, 10, tn('gray')); return; }
  sPoly(c, pts, {fill:o.color||'red', gap:6, rough:0.6});
  sRect(c, 39, 4, 12, 12, {fill:'gray', fs:'solid', cls:'soft'}); sRect(c, 39, 40, 12, 12, {fill:'gray', fs:'solid', cls:'soft'});
  if(o.lines!==false) [[57,10,14],[61,18,26],[57,26,14]].forEach(([x,y,h],i)=>c.arc(x-4, 28, 8+i%2*6, i%2?32:20, -60, 60, {cls:'thin', color:'gray', rough:0.4}));
}};

// scissors: open scissors (cut costs, cancel). o.color (handles, default 'red')
P.scissors = {w:66, h:46, dh:10, draw(c,o){
  const col=o.color||'red', ring=(x,y)=>{ c.ellipse(x, y, 21, 16, back()); c.ellipse(x, y, 21, 16, {fill:col, gap:3.5, rough:0.5}); c.ellipse(x, y, 11, 7, {fill:'paper', fs:'solid', rough:0.4}); };
  if(tiny(c)){ c.poly([[27,21],[36,27.5],[64,38.5],[37,20.5]], tf('gray')); c.poly([[27,25],[36,18.5],[64,7.5],[37,25.5]], tf('gray')); [[12,12],[12,34]].forEach(([x,y])=>{ c.ellipse(x, y, 21, 16, tf(col)); c.ellipse(x, y, 9, 6, tn('paper')); }); return; }
  sPoly(c, thick([[20,15.5],[29,21.5]], 5.5), {fill:col, fs:'solid', rough:0.4}); ring(12, 12);
  sPoly(c, [[27,21],[36,27.5],[64,38.5],[37,20.5]], {fill:'gray', gap:4, rough:0.5});
  sPoly(c, thick([[20,30.5],[29,24.5]], 5.5), {fill:col, fs:'solid', rough:0.4}); ring(12, 34);
  sPoly(c, [[27,25],[36,18.5],[64,7.5],[37,25.5]], {fill:'gray', gap:4, rough:0.5});
  c.dot(32, 23, 4.5);
}};

// cycle: two curved arrows chasing each other in a circle (renewal, repeat, recycle). o.colors ([first, second], default ['green','blue'])
function arcArrow(cx, cy, r, th, a0, a1, tipDeg){ const ro=r+th/2, ri=r-th/2, fl=5.5;
  const outer=arcPts(cx, cy, ro, ro, a0, a1, 12), inner=arcPts(cx, cy, ri, ri, a1, a0, 12), t=rad(a1+tipDeg), e=rad(a1);
  return outer.concat([[cx+(ro+fl)*Math.cos(e), cy+(ro+fl)*Math.sin(e)], [cx+r*Math.cos(t), cy+r*Math.sin(t)], [cx+(ri-fl)*Math.cos(e), cy+(ri-fl)*Math.sin(e)]], inner); }
P.cycle = {w:56, h:56, dh:12, draw(c,o){
  const cl=o.colors||['green','blue'];
  if(tiny(c)){ c.poly(arcArrow(28, 28, 19, 8, 195, 318, 28), tf(cl[0])); c.poly(arcArrow(28, 28, 19, 8, 15, 138, 28), tf(cl[1])); return; }
  sPoly(c, arcArrow(28, 28, 19, 8, 195, 318, 28), {fill:cl[0], gap:5, rough:0.5});
  sPoly(c, arcArrow(28, 28, 19, 8, 15, 138, 28), {fill:cl[1], gap:5, rough:0.5});
}};

/* ---------- Warnings and marks ---------- */

// warning: warning triangle with '!' (risk, caution, hazard). o.color (default 'yellow')
P.warning = {w:58, h:52, dh:12, draw(c,o){
  if(tiny(c)){ c.poly(roundPoly([[29,3],[56,49],[2,49]], 5), tf(o.color||'yellow')); c.poly([[26,17],[32,17],[30.8,35],[27.2,35]], tn('ink')); c.dot(29, 41.5, 5.5); return; }
  sPoly(c, roundPoly([[29,3],[56,49],[2,49]], 5), {fill:o.color||'yellow', gap:5, cls:'bold', rough:0.6});
  c.poly([[26.3,18],[31.7,18],[30.6,35],[27.4,35]], {fill:'ink', fs:'solid', rough:0.3});
  c.dot(29, 41.5, 5);
}};

// question: big question mark (unknown, uncertainty, "what if?"). o.color (default 'blue')
P.question = {w:40, h:60, dh:12, draw(c,o){
  const path=arcPts(20, 17, 11, 11, 200, 400, 15).concat([[22,32],[20,36],[20,40]]), col=o.color||'blue';
  if(tiny(c)){ c.poly(thick(path, 9), tf(col)); c.circle(20, 51.5, 10, tf(col)); return; }
  sPoly(c, thick(path, 8.5), {fill:col, gap:4.5, rough:0.5});
  sCirc(c, 20, 51.5, 10, {fill:col, gap:3.5, rough:0.4});
}};

// exclaim: big exclamation mark (important, alert, surprise). o.color (default 'red')
P.exclaim = {w:28, h:60, dh:12, draw(c,o){
  const col=o.color||'red';
  if(tiny(c)){ c.poly(roundPoly([[6,4],[22,4],[17,40],[11,40]], 3), tf(col)); c.circle(14, 51, 11, tf(col)); return; }
  sPoly(c, roundPoly([[6,4],[22,4],[17,40],[11,40]], 3), {fill:col, gap:4.5, rough:0.5});
  sCirc(c, 14, 51, 11, {fill:col, gap:3.5, rough:0.4});
}};

// thumbsup / thumbsdown: a hand giving a thumbs up (approved, good choice) or down (denied, bad idea). o.color (sleeve, default 'green' up / 'red' down)
function hand(c, o, up){
  const Y=pts=>up?pts:pts.map(([x,y])=>[x, 62-y]);
  if(tiny(c)){ c.poly(Y([[2,30],[15,28],[17,58],[3,58]]), tf(o.color||(up?'green':'red'))); c.poly(Y(stadium(23.5, 17, 30, 12.5, -77)), tf('paper'));
    c.poly(Y(roundPoly([[14,29],[24,26],[44,27],[50,34],[49,58],[15,58]], 5)), tf('paper')); [38.8,46.1].forEach(y=>{ const a=Y([[36,y],[49,y]]); c.line(a[0][0], a[0][1], a[1][0], a[1][1], tl()); }); return; }
  sPoly(c, Y([[2,30],[15,28],[17,58],[3,58]]), {fill:o.color||(up?'green':'red'), gap:5});
  sPoly(c, Y(stadium(23.5, 17, 30, 12.5, -77)), {fill:'paper', fs:'solid', rough:0.6});
  sPoly(c, Y(roundPoly([[14,29],[24,26],[34,26],[38,58],[15,58]], 5)), {fill:'paper', fs:'solid', rough:0.6});
  c.curve(Y([[18,33],[22,31],[27,31]]), {cls:'thin', rough:0.4});
  [19,20,19,16].forEach((len,i)=>sPoly(c, Y(stadium(41-(20-len)/2, 31.5+i*7.3, len, 7.8, 0)), {fill:'paper', fs:'solid', rough:0.5}));
}
P.thumbsup = {w:54, h:62, dh:12, draw(c,o){ hand(c, o, true); }};
P.thumbsdown = {w:54, h:62, dh:12, draw(c,o){ hand(c, o, false); }};

// chain: a row of chain links (connection, liability chain, weakest link). o.n (links, default 5), o.broken (the middle link snapped open), o.color (default 'gray')
P.chain = {w:112, h:36, dh:8, draw(c,o){
  const n=Math.max(2, Math.min(9, o.n||5)), col=o.color||'gray', sp=20, mid=Math.floor(n/2), cy=18, br=!!o.broken;
  const X=i=>56+(i-(n-1)/2)*sp+(br?(i<mid?-5:i>mid?5:0):0);
  for(let i=0;i<n;i+=2){ if(br && i===mid) continue; sPoly(c, stadium(X(i), cy, 30, 18, 0), {fill:col, gap:5, rough:0.6}); c.poly(stadium(X(i), cy, 21, 7.5, 0), {fill:'paper', fs:'solid', rough:0.5}); }
  for(let i=1;i<n;i+=2){ if(br && i===mid) continue; sPoly(c, stadium(X(i), cy, 30, 6.5, 0), {fill:col, gap:3.5, rough:0.6}); }
  if(br){ const x=X(mid);
    [-1,1].forEach(s=>sPoly(c, thick([[x+s*1.5, cy-6.3],[x+s*7, cy-6.3]].concat(arcPts(x+s*7, cy, 6.3, 6.3, s<0?270:-90, s<0?90:90, 30)).concat([[x+s*1.5, cy+6.3]]).map(([px,py])=>[px+s*3,py]), 5.5), {fill:col, gap:4, rough:0.5}));
    [[0,-9,0,-15],[2,-7,6,-12],[-2,-7,-6,-12],[0,9,0,15]].forEach(([a,b,d,e])=>c.line(x+a, cy+b, x+d, cy+e, {color:'orange', cls:'thin', rough:0.4}));
  }
}};

// hourglass: sand timer (time running out, deadline, waiting period). o.sand: share of sand still in the top bulb, 0-1 (default 0.5), o.color (frame, default 'brown')
P.hourglass = {w:44, h:66, dh:14, draw(c,o){
  const s=Math.max(0, Math.min(1, o.sand!=null?+o.sand:0.5)), fc=o.color||'brown';
  if(tiny(c)){ c.poly([[11,8],[33,8],[23.5,33],[33,58],[11,58],[20.5,33]], tf('paper')); if(s>0.05){ const y0=31-s*19, hw=Math.min(9.5, 2+(31-y0)/13*6.5); c.poly([[22-hw,y0],[22+hw,y0],[22,31]], tn('yellow')); }
    if(s<0.95){ const h=3+(1-s)*13; c.poly([[13,57],[31,57],[22,57-h]], tn('yellow')); } c.rect(3, 2, 38, 7, tf(fc)); c.rect(3, 57, 38, 7, tf(fc)); return; }
  c.line(8, 8, 8, 58, {cls:'bold', color:fc}); c.line(36, 8, 36, 58, {cls:'bold', color:fc});
  sBlob(c, [[11,8.5],[22,8],[33,8.5],[32,19],[24.5,31],[24.5,35],[32,47],[33,57.5],[22,58],[11,57.5],[12,47],[19.5,35],[19.5,31],[12,19]], {rough:0.5});
  const sand={fill:'yellow', fs:'solid', color:'orange', cls:'thin', rough:0.4};
  if(s>0.02){ const y0=31-s*19, hw=2+(31-y0)/13*6.5; c.poly([[22-Math.min(hw,10),y0],[22+Math.min(hw,10),y0],[22,31.5]], sand); }
  if(s<0.98){ const h=3+(1-s)*13; c.poly([[13,56.5],[31,56.5],[27,56.5-h*0.55],[22,56.5-h],[17,56.5-h*0.55]], sand); }
  if(s>0.02 && s<0.98) c.line(22, 32, 22, 55, {color:'orange', cls:'thin', rough:0.3, single:true});
  sRR(c, 3, 2, 38, 7, 2.5, {fill:fc, gap:4}); sRR(c, 3, 57, 38, 7, 2.5, {fill:fc, gap:4});
}};

// thermometer: thermometer (heat, risk level, rising rates). o.level: 0-1 (default 0.7), o.color (liquid, default 'red'; 'blue' for cold)
P.thermometer = {w:34, h:76, dh:14, draw(c,o){
  const lv=Math.max(0, Math.min(1, o.level!=null?+o.level:0.7)), col=o.color||'red', yt=55-lv*46;
  if(tiny(c)){ c.rrect(11, 3, 12, 58, 6, tf('paper')); c.rect(14.5, yt, 5, 58-yt, tn(col)); c.circle(17, 63, 21, tf(col)); return; }
  c.rrect(11, 3, 12, 58, 6, back());
  c.circle(17, 63, 21, back());
  c.rrect(14.5, yt, 5, 63-yt, 2, {fill:col, fs:'solid', nostroke:true, rough:0.3});
  c.circle(17, 63, 14, {fill:col, fs:'solid', rough:0.3});
  c.poly(arcPts(17, 63, 10.5, 10.5, -62, 242, 20).concat([[11,54],[11,9]], arcPts(17, 9, 6, 6, 180, 360, 30), [[23,54]]), {rough:0.6});
  for(let y=12;y<=52;y+=8) c.line(23.5, y, y%16===12?30:27.5, y, {cls:'thin', rough:0.3});
}};

// funnel: sales funnel with colored layers (narrowing down, filtering, conversion). o.layers (bands, 0-4, default 3), o.colors (band colors, default ['blue','teal','green','orange']), o.drops (dots falling out the spout, 0-3)
P.funnel = {w:60, h:66, dh:14, draw(c,o){
  const nl=Math.max(0, Math.min(4, o.layers!=null?o.layers:3)), cl=o.colors||['blue','teal','green','orange'];
  const xl=y=>3+(y-10)/34*22, xr=y=>57-(y-10)/34*22, body=[[3,10],[57,10],[35,44],[35,60],[25,60],[25,44]];
  c.poly(body, back());
  if(nl){ const ys=[]; for(let i=0;i<=nl;i++) ys.push(10+i*34/nl);
    for(let i=0;i<nl;i++){ const a=ys[i], b=ys[i+1]; c.poly([[xl(a),a],[xr(a),a],[xr(b),b],[xl(b),b]], {fill:cl[i%cl.length], gap:4, nostroke:true, angle:i%2?41:-41}); }
    for(let i=1;i<nl;i++){ const y=ys[i]; c.curve([[xl(y),y],[30,y+3.5],[xr(y),y]], {cls:'thin', rough:0.4}); } }
  else c.poly(body, {fill:'gray', gap:7, nostroke:true, cls:'soft'});
  c.poly(body, {rough:0.6});
  c.ellipse(30, 10, 54, 11, {fill:'paper', fs:'solid', rough:0.5});
  c.ellipse(30, 10, 44, 6, {fill:'ink', fs:'solid', cls:'soft', nostroke:true, rough:0.4});
  for(let i=0;i<Math.min(3, o.drops|0);i++) c.dot(30, 64+i*6, 4.5-i*0.6, {color:'green'});
}};

/* ---------- Places and the world ---------- */

// globe: planet Earth (worldwide, everywhere). o.grid (latitude/longitude lines instead of continents), o.stand (desk globe on a stand)
const GLAND=[[[9,15],[17,9],[25,11],[24,18],[19,22],[22,27],[20,33],[23,38],[19,48],[15,42],[14,33],[10,27],[6,22]], [[32,10],[41,7],[47,13],[44,19],[49,26],[47,34],[41,44],[37,40],[36,31],[31,26],[34,19]]];
P.globe = {w:58, h:58, dh:12, draw(c,o){
  const cx=29, cy=o.stand?26:29, d=o.stand?46:52, k=d/52, T=pts=>pts.map(([x,y])=>[cx+(x-29)*k, cy+(y-29)*k]);
  if(tiny(c)){ c.circle(cx, cy, d, tf('sky')); if(!o.grid) GLAND.forEach(l=>c.blob(T(l), tn('green'))); else c.ellipse(cx, cy, d*0.42, d, tl()); return; }
  if(o.stand){ c.arc(cx, cy, d+8, d+8, 20, 160, {cls:'bold', color:'brown'}); c.line(cx, cy+d/2+4, cx, 53, {cls:'bold', color:'brown'}); sRR(c, 16, 52, 26, 5, 2, {fill:'brown', gap:4}); }
  sCirc(c, cx, cy, d, {fill:'sky', gap:6, cls:'soft', nostroke:true});
  if(o.grid){ c.ellipse(cx, cy, d, d*0.32, {cls:'thin', rough:0.5}); c.ellipse(cx, cy, d*0.42, d, {cls:'thin', rough:0.5}); c.line(cx, cy-d/2, cx, cy+d/2, {cls:'thin', rough:0.4}); c.line(cx-d/2, cy, cx+d/2, cy, {cls:'thin', rough:0.4}); }
  else {
    GLAND.forEach(l=>sBlob(c, T(l), {fill:'green', gap:4.5, rough:0.5}));
  }
  c.circle(cx, cy, d, {});
}};

/* ---------- Perils and effects ---------- */

// boom: comic explosion burst (sudden loss, accident, impact). o.text (word in the middle, e.g. 'BOOM', 'POW'), o.color (outer burst, default 'orange')
const BJ=[1,0.78,1.05,0.85,0.95,0.8,1.1,0.82,1,0.76,1.06,0.84];
P.boom = {w:72, h:62, dh:14, draw(c,o){
  const burst=(R,r,sy)=>{ const pts=[]; for(let i=0;i<24;i++){ const a=rad(-90+i*15), q=(i%2?r:R)*BJ[(i>>1)%12]; pts.push([36+q*Math.cos(a), 31+q*Math.sin(a)*sy]); } return pts; };
  sPoly(c, burst(34, 21, 0.86), {fill:o.color||'orange', gap:5, rough:0.6});
  c.poly(burst(22, 13, 0.86), {fill:'yellow', fs:'solid', rough:0.5, color:'orange'});
  if(o.text) c.text(36, 35.5, o.text, {size:fitText(o.text, 30, 12), color:'red', bold:true});
}};

// crack: crack splitting the ground (earthquake, sinkhole, foundation damage). o.shake (tremor marks above the ground, default true)
P.crack = {w:100, h:40, dh:10, draw(c,o){
  c.poly([[0,13],[44,13],[50,38],[56,15],[100,15],[100,38],[0,38]], {fill:'brown', gap:8, nostroke:true, cls:'soft'});
  c.line(0, 13, 39, 13, {}); c.line(61, 15.5, 100, 15.5, {});
  sPoly(c, [[38,13],[46,19],[42,25],[48,31],[47,38],[53,29],[56,23],[54,18],[62,15.5]], {fill:'ink', gap:2.6, rough:0.6});
  c.poly([[39,13.5],[31,17],[24,16],[18,19]], {open:true, cls:'thin', rough:0.5}); c.poly([[61,16],[70,20],[78,19],[84,22]], {open:true, cls:'thin', rough:0.5});
  c.poly([[44,22],[36,26],[30,25]], {open:true, cls:'thin', rough:0.5}); c.poly([[54,26],[63,29],[70,28]], {open:true, cls:'thin', rough:0.5});
  if(o.shake!==false){ [[16,5],[84,7]].forEach(([x,y],j)=>[0,1].forEach(i=>{ const s=j?1:-1; c.arc(x+s*i*4, y, 6+i*4, 9+i*5, s<0?120:-60, s<0?240:60, {cls:'thin', color:'gray', rough:0.3}); })); }
}};

// tornado: twister funnel with spinning debris (windstorm). o.debris (default true), o.color (default 'gray')
P.tornado = {w:60, h:80, dh:18, draw(c,o){
  const col=o.color||'gray', rows=[[6,54,0],[16,44,3],[26,35,5],[36,27,5],[46,20,3],[55,14,0],[63,9,-2],[71,5,-1]];
  const L=rows.map(([y,w,dx])=>[30+dx-w/2, y]), R=rows.map(([y,w,dx])=>[30+dx+w/2, y]).reverse();
  sBlob(c, L.concat([[29,76]], R, [[30,2]]), {fill:col, gap:7, cls:'soft', rough:0.6});
  rows.slice(1).forEach(([y,w,dx])=>c.arc(30+dx, y-2, w, 6, 10, 170, {color:col==='gray'?'ink':col, cls:'thin', rough:0.4}));
  if(o.debris!==false){ c.line(6, 52, 11, 49, {color:'brown', cls:'bold'}); c.line(49, 60, 54, 63, {color:'brown', cls:'bold'}); c.dot(10, 66, 3.5, {color:'brown'}); c.dot(50, 48, 3, {color:'brown'});
    c.arc(30, 76, 34, 8, 170, 370, {cls:'thin', color:col, rough:0.4}); }
}};

// hail: dark cloud dropping hailstones (hail damage). o.big (bigger stones)
P.hail = {w:80, h:88, dh:22, draw(c,o){
  if(P.cloud) P.cloud.draw(c, {dark:true}); else c.blob([[14,40],[4,30],[10,18],[24,16],[30,6],[46,4],[56,14],[70,14],[78,26],[72,38],[60,42]], {fill:'gray', gap:9});
  const k=o.big?1.45:1;
  [[16,55,9],[35,61,11],[54,54,9],[69,65,10],[23,76,9],[47,79,10],[66,84,7]].forEach(([x,y,d],i)=>{
    c.line(x-2, y-d*k/2-3, x-4, y-d*k/2-8, {color:'gray', cls:'thin', rough:0.3, single:true});
    c.circle(x, y, d*k, {fill:'white', fs:'solid', rough:0.4}); c.arc(x, y, d*k*0.6, d*k*0.6, 200, 260, {color:'sky', cls:'thin', rough:0.3});
  });
}};

// ice: icicles hanging from a roof gutter (ice dam, winter damage). o.n (icicles, default 11), o.snow (snow on the gutter, default true)
const ICL=[14,26,18,32,20,28,13,30,22,16,24,19,27];
P.ice = {w:110, h:46, dh:10, draw(c,o){
  const n=Math.max(1, Math.min(13, o.n||11)), sp=100/n;
  for(let i=0;i<n;i++){ const x=5+sp*(i+0.5), L=ICL[i%ICL.length], hw=Math.min(4.2, sp*0.42);
    sPoly(c, [[x-hw,10],[x+hw,10],[x+1.2,10+L*0.6],[x+0.3,10+L],[x-1.3,10+L*0.55]], {fill:'sky', gap:4, rough:0.5});
    if(i%3===1) c.dot(x+0.3, 14+L, 2.2, {color:'sky'}); }
  sRR(c, 2, 4, 106, 7, 2.5, {fill:'gray', gap:5});
  if(o.snow!==false) sBlob(c, [[3,5],[8,0],[20,1],[33,-1.5],[48,0.5],[63,-1],[78,0.5],[92,-1.2],[104,0.5],[107,5]], {fill:'white', fs:'solid', rough:0.5});
}};

// flood: wide band of rising flood water with ripples; place it over the bottom of a house or street. o.debris (floating plank and ball), o.color (default 'blue')
P.flood = {w:200, h:44, dh:11, draw(c,o){
  const col=o.color||'blue', top=[];
  for(let x=0;x<=200;x+=12.5) top.push([x, 9+((x/12.5)%2?3.5:-1.5)]);
  const body=top.concat([[200,44],[0,44]]);
  c.poly(body, {fill:col, fs:'solid', nostroke:true, cls:'soft'});
  c.poly(body, {fill:col, gap:9, nostroke:true, cls:'soft'});
  c.curve(top, {color:col, cls:'bold'});
  [[30,22,18],[78,30,22],[128,21,16],[168,32,20],[52,38,14],[108,39,16]].forEach(([x,y,w])=>c.arc(x, y, w, 5, 200, 340, {color:col, cls:'thin', rough:0.4}));
  if(o.debris){ c.poly(rbox(150, 8, 30, 5, -8), {fill:'brown', gap:4, rough:0.5}); c.circle(60, 7, 8, {fill:'red', gap:3.5, rough:0.4}); }
}};

// puff: smoke puffs rising, small to large (smoke damage, gone up in smoke). o.n (3 or 4 puffs, default 4), o.color (default 'gray')
P.puff = {w:46, h:64, dh:14, draw(c,o){
  const col=o.color||'gray', all=[[22,16,27],[27,35,20],[19,49,14],[24,59,9]], pf=o.n===3?all.slice(0,3).map(([x,y,d])=>[x,y+6,d]):all;
  pf.forEach(([x,y,d],j)=>{ const pts=[], nb=d>18?7:5; for(let i=0;i<42;i++){ const a=i/42*2*Math.PI, q=d/2*(0.84+0.16*Math.abs(Math.sin(nb*a/2+j))); pts.push([x+q*Math.cos(a), y+q*Math.sin(a)]); } sPoly(c, pts, {fill:col, gap:5, cls:'soft', color:col, rough:0.4}); });
}};

// sparkle: twinkle stars (new, clean, shiny, magic). o.color (default 'yellow')
function spark(cx, cy, R){ const r=R*0.26; return [[cx,cy-R],[cx+r,cy-r],[cx+R,cy],[cx+r,cy+r],[cx,cy+R],[cx-r,cy+r],[cx-R,cy],[cx-r,cy-r]]; }
P.sparkle = {w:50, h:50, dh:10, draw(c,o){
  const col=o.color||'yellow';
  sPoly(c, spark(20, 29, 18), {fill:col, gap:4, rough:0.4});
  sPoly(c, spark(40, 12, 9.5), {fill:col, fs:'solid', rough:0.3});
  sPoly(c, spark(41, 39, 6.5), {fill:col, fs:'solid', rough:0.3});
  c.dot(7, 8, 3.5, {color:col}); c.dot(46, 25, 2.6, {color:col});
}};

})();
