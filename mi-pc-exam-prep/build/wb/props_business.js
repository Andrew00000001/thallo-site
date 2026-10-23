/* ---------- Sketch props: business, law, retail, medical and office ----------
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
function rot(pts, cx, cy, deg){ const a=rad(deg), co=Math.cos(a), si=Math.sin(a); return pts.map(([x,y])=>[cx+(x-cx)*co-(y-cy)*si, cy+(x-cx)*si+(y-cy)*co]); }
function rbox(cx, cy, w, h, deg){ return rot([[cx-w/2,cy-h/2],[cx+w/2,cy-h/2],[cx+w/2,cy+h/2],[cx-w/2,cy+h/2]], cx, cy, deg||0); }
function star(cx, cy, R, r, n, a0){ const pts=[]; for(let i=0;i<2*n;i++){ const a=rad((a0==null?-90:a0)+i*180/n), q=i%2?r:R; pts.push([cx+q*Math.cos(a), cy+q*Math.sin(a)]); } return pts; }
function sector(cx, cy, r, a0, a1){ const pts=[[cx,cy]], n=Math.max(2, Math.round((a1-a0)/15)); for(let i=0;i<=n;i++){ const a=rad(a0+(a1-a0)*i/n); pts.push([cx+r*Math.cos(a), cy+r*Math.sin(a)]); } return pts; }
function stadium(cx, cy, len, th, deg, half){ // capsule outline; half = 'l' | 'r' for one half only
  const r=th/2, hl=len/2-r, pts=[];
  if(half!=='l') for(let a=-90;a<=90;a+=30) pts.push([cx+hl+r*Math.cos(rad(a)), cy+r*Math.sin(rad(a))]);
  else pts.push([cx,cy-r],[cx,cy+r]);
  if(half!=='r') for(let a=90;a<=270;a+=30) pts.push([cx-hl+r*Math.cos(rad(a)), cy+r*Math.sin(rad(a))]);
  else pts.push([cx,cy+r],[cx,cy-r]);
  return rot(pts, cx, cy, deg||0);
}
function gline(c, x1, y, x2, o){ c.line(x1, y, x2, y, Object.assign({cls:'thin', color:'gray', rough:0.5}, o)); }  // gray "writing" line
const TINY = 0.9;   // c.k below this = drawn very small (e.g. held in a person's hand): flat fills, single thin strokes
const tiny = c => c.k < TINY;
const tf = (col, o) => Object.assign({fill:col, fs:'solid', cls:'thin', single:true, rough:0.5}, o);   // tiny-mode flat fill
const tl = o => Object.assign({cls:'thin', single:true, rough:0.4}, o);                                 // tiny-mode line
const tn = col => ({fill:col, fs:'solid', nostroke:true, rough:0.4});                                   // tiny-mode fill only
function fitText(s, maxW, maxSize){ const w=SK.tw(s,1)||0.5*String(s).length; return Math.min(maxSize, maxW/Math.max(w,0.1)); }

/* ---------- Law and licensing ---------- */

// gavel: judge's gavel over its sound block. o.block (default true), o.strike (impact lines: the ruling lands)
P.gavel = {w:72, h:60, dh:10, draw(c,o){
  const hx=24, hy=19, ang=36, ca=Math.cos(rad(ang)), sa=Math.sin(rad(ang));
  if(tiny(c)){
    if(o.block!==false) c.rrect(3, 46, 38, 11, 3, tf('brown'));
    c.poly(rbox(hx+33*ca, hy+33*sa, 44, 7, ang), tf('brown'));
    c.poly(rbox(hx, hy, 36, 18, ang+90), tf('brown'));
    [-13, 13].forEach(t=>c.poly(rbox(hx+t*Math.cos(rad(ang+90)), hy+t*Math.sin(rad(ang+90)), 5, 18, ang+90), tn('yellow')));
    return;
  }
  if(o.block!==false){ sRR(c,3,46,38,11,3,{fill:'brown', gap:6}); c.line(6,50.5,38,50.5,{cls:'thin', rough:0.5}); }
  if(o.strike){ [[8,40,3,34],[16,38,15,31],[30,40,36,35]].forEach(l=>c.line(l[0],l[1],l[2],l[3],{color:'orange', rough:0.4})); }
  sPoly(c, rbox(hx+33*ca, hy+33*sa, 40, 6, ang), {fill:'brown', gap:5});         // handle
  c.circle(hx+54*ca, hy+54*sa, 8, {fill:'brown', fs:'solid'});                    // knob
  sPoly(c, rbox(hx, hy, 34, 16, ang+90), {fill:'brown', gap:6});                  // head
  [-12.5, 12.5].forEach(t=>sPoly(c, rbox(hx+t*Math.cos(rad(ang+90)), hy+t*Math.sin(rad(ang+90)), 4, 18, ang+90), {fill:'yellow', fs:'solid', rough:0.5}));
}};

// scale: scales of justice. o.tilt: -1 (left pan lower/heavier), 0 (balanced, default), 1 (right pan lower);
//   o.left / o.right: prop name resting in that pan (e.g. 'money', 'house'), o.leftOpt / o.rightOpt
P.scale = {w:92, h:80, dh:18, draw(c,o){
  const t=Math.max(-1, Math.min(1, +o.tilt||0)), d=8*t, cx=46, by=22;
  sPoly(c, [[30,78],[62,78],[56,70],[36,70]], {fill:'brown', gap:6});
  sRect(c, 43, 14, 6, 56, {fill:'yellow', gap:5});
  c.circle(cx, 9, 9, {fill:'yellow', fs:'solid'});
  const L=[16, by-d], R=[76, by+d];
  c.line(L[0], L[1], R[0], R[1], {cls:'bold'});
  c.dot(cx, by, 4.5);
  [[L,o.left,o.leftOpt],[R,o.right,o.rightOpt]].forEach(([p,item,io])=>{
    const py=p[1]+27;
    if(item) c.sub(p[0], py-7, 13, item, io||{});
    c.line(p[0], p[1], p[0]-13, py, {cls:'thin'}); c.line(p[0], p[1], p[0]+13, py, {cls:'thin'});
    c.dot(p[0], p[1], 3.5);
    c.arc(p[0], py, 30, 15, 0, 180, {closed:true, fill:'yellow', gap:5});
  });
}};

// handshake: two hands shaking (deal, agreement, contract). o.left / o.right: sleeve colors (default 'blue' / 'gray')
P.handshake = {w:100, h:58, dh:10, draw(c,o){
  const lc=o.left||'blue', rc=o.right||'gray';
  sPoly(c, [[0,23],[15,19],[20,45],[2,50]], {fill:lc, gap:7});
  sBlob(c, [[19,22],[34,18],[52,21],[57,34],[46,46],[22,46]], {});                 // left hand (behind)
  sPoly(c, [[100,22],[78,18],[73,44],[98,50]], {fill:rc, gap:7});
  sBlob(c, [[75,19],[62,15],[50,17],[46,28],[50,40],[62,45],[75,44]], {});         // right hand back
  for(let i=3;i>=0;i--) c.poly(stadium(43-i*1.2, 23.5+i*6.2, 18-i, 6.4, -8), {fill:'paper', fs:'solid', rough:0.6});   // right fingers wrapping over
  c.poly(stadium(45, 16.5, 22, 7.5, -10), {fill:'paper', fs:'solid', rough:0.6});  // left thumb on top
  sPoly(c, [[13,19],[20,18],[25,44],[18,45]], {fill:'paper', fs:'solid'});
  sPoly(c, [[80,18],[73,17],[68,43],[75,44]], {fill:'paper', fs:'solid'});
}};

// certificate: framed certificate / license with a ribbon seal. o.title (default 'CERTIFICATE'), o.frame (default true; false = loose document),
//   o.seal (seal color, default 'red'), o.name (optional line of text under the title)
P.certificate = {w:86, h:66, dh:14, draw(c,o){
  if(tiny(c)){
    if(o.frame!==false) c.rect(2, 2, 82, 62, tf('brown')); c.rect(9, 9, 68, 48, o.frame!==false ? tn('paper') : tf('paper'));
    c.line(18, 22, 68, 22, tl({color:'blue', cls:''})); c.line(20, 34, 50, 34, tl({color:'gray'}));
    c.circle(63, 44, 16, tf(o.seal||'red')); return;
  }
  if(o.frame!==false){ sRect(c, 2, 2, 82, 62, {fill:'brown', gap:5}); sRect(c, 9, 9, 68, 48, {fill:'paper', fs:'solid'}); }
  else { sRect(c, 5, 5, 76, 56, {fill:'paper', fs:'solid'}); c.rect(9, 9, 68, 48, {cls:'thin', color:o.seal||'red', rough:0.5}); }
  const t=o.title||'CERTIFICATE';
  c.text(43, 22, t, {size:fitText(t, 56, 9), color:'blue'});
  if(o.name) c.text(43, 33, o.name, {size:fitText(o.name, 48, 7)}); else { gline(c, 20, 30, 66); gline(c, 24, 36, 62); }
  c.curve([[16,50],[20,44],[23,50],[27,44],[33,49]], {color:'blue', cls:'thin'}); gline(c, 15, 52, 38);
  const sc=o.seal||'red';
  c.poly([[57,48],[53,60],[57,57],[60,61],[61,49]], {fill:sc, fs:'solid', rough:0.5});
  c.poly([[64,49],[66,61],[68,57],[72,59],[68,47]], {fill:sc, fs:'solid', rough:0.5});
  c.poly(star(63, 44, 9, 7, 12, 0), {fill:sc, fs:'solid', rough:0.4});
  c.circle(63, 44, 9, {color:'paper', cls:'thin', rough:0.4});
}};

// idcard: license / ID card with a photo. o.title (header text, default 'LICENSE'), o.color (header band, default 'blue')
P.idcard = {w:72, h:46, dh:8, draw(c,o){
  const col=o.color||'blue', t=o.title||'LICENSE';
  if(tiny(c)){ c.rrect(2, 2, 68, 42, 5, tf('paper')); c.rect(4, 4, 64, 11, tn(col)); c.rect(9, 19, 19, 21, tn('sky')); c.circle(18.5, 27, 9, tn('paper'));
    c.line(34, 24, 62, 24, tl({color:'gray'})); c.line(34, 33, 56, 33, tl({color:'gray'})); return; }
  sRR(c, 2, 2, 68, 42, 5, {fill:'paper', fs:'solid'});
  c.poly([[7,3],[65,3],[69,6],[69,14],[3,14],[3,6]], {fill:col, fs:'solid', nostroke:true, rough:0.4});
  c.rrect(2, 2, 68, 42, 5, {});
  c.text(36, 11.5, t, {size:fitText(t, 54, 8), color:'paper'});
  c.rect(8, 18, 20, 22, {fill:'sky', gap:5, cls:'soft'});
  c.arc(18, 41, 16, 16, 180, 360, {fill:'paper', fs:'solid', rough:0.5});
  c.circle(18, 27, 8, {fill:'paper', fs:'solid', rough:0.5});
  gline(c, 34, 22, 62); gline(c, 34, 29, 56); gline(c, 34, 36, 60);
}};

// badge: police / license badge. o.star (6-point sheriff star instead of a shield), o.text (short word in the center, e.g. 'POLICE'), o.color (metal, default 'yellow')
P.badge = {w:50, h:54, dh:8, draw(c,o){
  const col=o.color||'yellow';
  if(tiny(c)){ c.poly(o.star ? star(25, 28, 24, 12, 6) : [[25,3],[31,8],[40,5],[46,12],[45,27],[39,40],[25,51],[11,40],[5,27],[4,12],[10,5],[19,8]], tf(col)); c.circle(25, 27, 14, tn('blue')); return; }
  if(o.star){
    const pts=star(25, 28, 24, 12, 6);
    sPoly(c, pts, {fill:col, gap:5});
    pts.filter((p,i)=>i%2===0).forEach(p=>c.circle(p[0], p[1], 5, {fill:col, fs:'solid', rough:0.4}));
    c.circle(25, 28, 16, {fill:'paper', fs:'solid'});
    if(o.text) c.text(25, 30.5, o.text, {size:fitText(o.text, 13, 7)}); else c.poly(star(25, 28, 6, 2.6, 5), {fill:'blue', fs:'solid', rough:0.3});
    return;
  }
  sPoly(c, [[25,3],[31,8],[40,5],[46,12],[45,27],[39,40],[25,51],[11,40],[5,27],[4,12],[10,5],[19,8]], {fill:col, gap:5});
  c.circle(25, 27, 22, {fill:'paper', fs:'solid'});
  if(o.text) c.text(25, 30, o.text, {size:fitText(o.text, 18, 7.5), color:'blue'}); else c.poly(star(25, 27, 8, 3.4, 5), {fill:'blue', fs:'solid', rough:0.3});
}};

// magnifier: magnifying glass, handle to the lower right. o.inside (prop name seen in the lens, e.g. 'house'), o.insideOpt, o.color (handle, default 'brown')
P.magnifier = {w:60, h:60, dh:10, draw(c,o){
  const u=Math.SQRT1_2;
  if(tiny(c)){ c.poly(rbox(24+35*u, 24+35*u, 24, 9, 45), tf(o.color||'brown')); c.circle(24, 24, 38, tf('paper')); c.circle(24, 24, 30, tn('sky')); c.circle(24, 24, 38, tl({cls:''})); return; }
  sPoly(c, rbox(24+35*u, 24+35*u, 22, 8, 45), {fill:o.color||'brown', gap:5});
  sPoly(c, rbox(24+22*u, 24+22*u, 6, 10, 45), {fill:'gray', fs:'solid', rough:0.5});
  c.circle(24, 24, 38, {fill:'paper', fs:'solid'});
  if(o.inside) c.sub(24, 25, 20, o.inside, o.insideOpt||{});
  else { c.circle(24, 24, 33, {fill:'sky', gap:6, cls:'soft', nostroke:true}); c.arc(24, 24, 24, 24, 195, 250, {cls:'thin', rough:0.4}); }
  c.circle(24, 24, 38, {cls:'bold'});
}};

/* ---------- Shop and goods ---------- */

// cashregister: shop cash register. o.open (cash drawer out, bills showing), o.amount (display text, default '$12'), o.color (body, default 'teal')
P.cashregister = {w:86, h:74, dh:14, draw(c,o){
  const col=o.color||'teal';
  sRect(c, 13, 10, 14, 18, {fill:'paper', fs:'solid', rough:0.5}); gline(c, 16, 15, 24); gline(c, 16, 20, 22);
  sRect(c, 54, 20, 6, 8, {fill:'gray', fs:'solid', rough:0.4});
  sRR(c, 40, 4, 34, 17, 2, {fill:'ink', fs:'solid', cls:'soft'});
  c.text(57, 16.5, o.amount||'$12', {size:9, color:'green'});
  sPoly(c, [[10,27],[76,27],[80,52],[6,52]], {fill:col, gap:9});
  for(let r=0;r<3;r++) for(let k=0;k<5;k++){ const x=14+k*11.5-r*1.2, y=31+r*6.6; c.rect(x, y, 8, 4.4, {fill:'paper', fs:'solid', rough:0.3, cls:'thin'}); }
  if(o.open){
    sRect(c, 6, 52, 74, 6, {fill:'gray', gap:7, cls:'soft'});
    [[12,49],[24,48],[36,49]].forEach(([x,y])=>c.rect(x, y, 10, 8, {fill:'green', fs:'solid', rough:0.4, cls:'soft2'}));
    sRect(c, 2, 58, 82, 14, {fill:'gray', gap:7});
    c.line(34, 65, 52, 65, {cls:'bold'});
  } else {
    sRect(c, 4, 52, 78, 18, {fill:'gray', gap:8, cls:'soft'});
    c.line(34, 61, 52, 61, {cls:'bold'});
  }
}};

// oven: brick pizza oven. o.fire (flames in the mouth, smoke from the chimney), o.pizza (a pizza sitting in the mouth)
P.oven = {w:96, h:86, dh:22, draw(c,o){
  if(o.fire) c.curve([[66,14],[70,9],[64,5],[70,0]], {color:'gray', cls:'thin'});
  sRect(c, 60, 14, 11, 20, {fill:'gray', gap:6});
  c.arc(48, 54, 86, 82, 180, 360, {closed:true, fill:'paper', fs:'solid', nostroke:true});
  c.arc(48, 54, 86, 82, 180, 360, {closed:true, fill:'red', gap:9});
  [[22,30,30,32],[64,30,72,32],[14,44,22,44],[74,44,82,44],[36,22,44,21],[52,21,60,22]].forEach(l=>c.line(l[0],l[1],l[2],l[3],{color:'brown', cls:'thin', rough:0.5}));
  c.arc(48, 54, 38, 36, 180, 360, {closed:true, fill:'ink', fs:'solid', cls:'soft'});
  if(o.fire) c.sub(48, 46, 15, 'fire', {});
  if(o.pizza) c.ellipse(o.fire?60:48, 52, 18, 5, {fill:'yellow', fs:'solid', rough:0.5});
  sRect(c, 4, 54, 88, 28, {fill:'gray', gap:10, cls:'soft'});
  [[4,63,92,63],[4,72,92,72]].forEach(l=>c.line(l[0],l[1],l[2],l[3],{cls:'thin', rough:0.4}));
  [[24,54,24,63],[56,54,56,63],[84,54,84,63],[12,63,12,72],[40,63,40,72],[70,63,70,72],[26,72,26,82],[56,72,56,82],[82,72,82,82]].forEach(l=>c.line(l[0],l[1],l[2],l[3],{cls:'thin', rough:0.4}));
}};

// pizza: whole pizza, top view, cut in 6 slices. o.slice (one slice instead), o.missing (slices eaten, 0-5), o.cut (slice lines, default true)
P.pizza = {w:60, h:60, dh:10, draw(c,o){
  if(c.k < 1.4){   // small: flat colors read better than hatching
    if(o.slice){ c.poly([[9,14],[51,14],[30,57]], tf('yellow')); c.rrect(5, 6, 50, 11, 5, tf('orange')); [[23,25],[36,26]].forEach(([x,y])=>c.circle(x, y, 10, tn('red'))); return; }
    c.circle(30, 30, 56, tf('orange')); c.circle(30, 30, 42, tn('yellow'));
    [[30,18],[41,36],[19,36]].forEach(([x,y])=>c.circle(x, y, 11, tn('red'))); return;
  }
  if(o.slice){
    sPoly(c, [[9,14],[51,14],[30,57]], {fill:'yellow', gap:5});
    c.curve([[24,40],[23,46],[25,48]], {color:'orange', cls:'thin'});
    sRR(c, 5, 6, 50, 11, 5, {fill:'orange', gap:4});
    [[22,24],[37,25],[30,37]].forEach(([x,y])=>c.circle(x, y, 8, {fill:'red', fs:'solid', rough:0.4}));
    return;
  }
  const miss=Math.max(0, Math.min(5, o.missing|0)), a0=-90+miss*60;
  if(!miss){ c.circle(30, 30, 56, {fill:'orange', gap:5, cls:'soft'}); c.circle(30, 30, 44, {fill:'paper', fs:'solid', nostroke:true}); c.circle(30, 30, 44, {fill:'yellow', gap:6}); }
  else { sPoly(c, sector(30, 30, 28, a0, 270), {fill:'orange', gap:5, cls:'soft'}); c.poly(sector(30, 30, 22, a0, 270), {fill:'paper', fs:'solid', nostroke:true}); c.poly(sector(30, 30, 22, a0, 270), {fill:'yellow', gap:6}); }
  if(o.cut!==false) for(let i=miss;i<6;i++){ const a=rad(-90+i*60); c.line(30, 30, 30+27*Math.cos(a), 30+27*Math.sin(a), {cls:'thin', rough:0.5}); }
  for(let i=miss;i<6;i++){ const a=rad(-60+i*60), r=i%2?14:12; c.circle(30+r*Math.cos(a), 30+r*Math.sin(a), 8, {fill:'red', fs:'solid', rough:0.4}); }
}};

// cart: shopping cart, faces right. o.full (groceries in the basket), o.color (basket tint)
P.cart = {w:86, h:72, dh:14, draw(c,o){
  if(o.full){
    sRect(c, 26, 6, 10, 18, {fill:'green', gap:5}); c.rect(28, 2, 6, 5, {fill:'green', fs:'solid', rough:0.4});
    sBlob(c, [[38,20],[42,9],[54,7],[62,14],[60,22]], {fill:'brown', gap:6});
    c.circle(66, 16, 11, {fill:'red', fs:'solid', cls:'soft2'}); c.line(66,10.5,68,7,{color:'green'});
  }
  c.poly([[2,8],[10,10],[16,20]], {open:true, cls:'bold'});
  sPoly(c, [[14,20],[82,20],[74,48],[22,48]], o.color?{fill:o.color, gap:8, cls:'soft'}:{});
  for(let i=1;i<6;i++){ const t=i/6; c.line(14+68*t, 20, 22+52*t, 48, {cls:'thin', color:'gray', rough:0.5}); }
  c.line(18, 34, 78, 34, {cls:'thin', color:'gray', rough:0.5});
  c.poly([[22,48],[25,57],[74,57]], {open:true});
  [[31,64],[68,64]].forEach(([x,y])=>{ c.circle(x, y, 11, {fill:'paper', fs:'solid'}); c.dot(x, y, 3); });
}};

// box: closed cardboard shipping box, 3/4 view. o.open (flaps up), o.label (short text on the front label), o.tape (default true).
//   NOTE: 'box' is also a built-in primitive, so as a top-level element use the alias 'parcel' (same drawing); 'box' works via sub/hold.
P.box = {w:64, h:60, dh:10, draw(c,o){
  if(tiny(c)){
    c.poly([[42,24],[60,14],[60,48],[42,58]], tf('brown'));
    c.poly([[4,24],[42,24],[42,58],[4,58]], tf('brown', {cls:'thin soft2'}));
    c.poly([[4,24],[22,14],[60,14],[42,24]], tf('orange', {cls:'thin soft'}));
    c.rect(10, 34, 18, 12, tn('paper')); return;
  }
  if(o.open){
    sPoly(c, [[4,24],[0,12],[18,6],[22,14]], {fill:'brown', gap:8, cls:'soft'});
    sPoly(c, [[42,24],[52,8],[64,4],[60,14]], {fill:'brown', gap:8, cls:'soft'});
  }
  sPoly(c, [[42,24],[60,14],[60,48],[42,58]], {fill:'brown', gap:6});
  sPoly(c, [[4,24],[42,24],[42,58],[4,58]], {fill:'brown', gap:11, cls:'soft'});
  if(o.open) sPoly(c, [[4,24],[22,14],[60,14],[42,24]], {fill:'ink', fs:'solid', cls:'soft'});
  else {
    sPoly(c, [[4,24],[22,14],[60,14],[42,24]], {fill:'brown', gap:14, cls:'soft'});
    if(o.tape!==false){ c.poly([[11,20],[49,20],[53,18],[15,18]], {fill:'yellow', fs:'solid', rough:0.4, cls:'soft2'}); c.poly([[49,20],[53,18],[53,30],[49,32]], {fill:'yellow', fs:'solid', rough:0.4, cls:'soft2'}); }
  }
  sRect(c, 10, 34, 20, 13, {fill:'paper', fs:'solid', rough:0.5});
  if(o.label) c.text(20, 43.5, o.label, {size:fitText(o.label, 17, 7)}); else { gline(c, 13, 38.5, 27); gline(c, 13, 43, 24); }
}};
P.parcel = P.box;

// pallet: boxes stacked on a wooden shipping pallet. o.n (box layers 1-3, default 3), o.wrap (plastic stretch-wrap lines)
P.pallet = {w:92, h:74, dh:16, draw(c,o){
  const n=Math.max(1, Math.min(3, o.n||3));
  c.rect(4, 59, 84, 5, {fill:'brown', gap:5});
  [6,41,76].forEach(x=>c.rect(x, 64, 10, 6, {fill:'brown', gap:4}));
  c.rect(4, 70, 84, 3, {fill:'brown', fs:'solid', rough:0.4, cls:'soft2'});
  const bx=(x,y)=>{ sRect(c, x, y, 26, 18, {fill:'brown', gap:9, cls:'soft'}); c.line(x+13, y, x+13, y+6, {color:'yellow', cls:'bold', rough:0.3}); c.rect(x+4, y+10, 9, 5, {fill:'paper', fs:'solid', rough:0.4, cls:'thin'}); };
  [6,33,60].forEach(x=>bx(x, 41));
  if(n>1) [19.5,46.5].forEach(x=>bx(x, 23));
  if(n>2) bx(33, 5);
  if(o.wrap){ [[5,45,87,48],[5,52,87,55]].concat(n>1?[[18,28,74,31],[18,34,74,37]]:[]).forEach(l=>c.line(l[0],l[1],l[2],l[3],{color:'sky', cls:'thin', rough:0.6})); }
}};

/* ---------- Medical ---------- */

// firstaid: first aid kit (case with a white cross). o.color (case, default 'red')
P.firstaid = {w:64, h:54, dh:10, draw(c,o){
  if(tiny(c)){ c.arc(32, 14, 26, 18, 180, 360, tl({cls:''})); c.rrect(4, 13, 56, 39, 6, tf(o.color||'red')); c.rect(28, 21, 8, 24, tn('white')); c.rect(20, 29, 24, 8, tn('white')); return; }
  c.arc(32, 14, 26, 18, 180, 360, {cls:'bold'});
  sRR(c, 4, 13, 56, 39, 6, {fill:o.color||'red', gap:7});
  const cx=32, cy=33, a=5, b=13;
  c.poly([[cx-a,cy-b],[cx+a,cy-b],[cx+a,cy-a],[cx+b,cy-a],[cx+b,cy+a],[cx+a,cy+a],[cx+a,cy+b],[cx-a,cy+b],[cx-a,cy+a],[cx-b,cy+a],[cx-b,cy-a],[cx-a,cy-a]], {fill:'white', fs:'solid', rough:0.5});
}};

// crutches: a pair of underarm crutches. o.n (1 = a single crutch)
function crutch(c, bx, by, deg){
  const T=p=>rot(p, bx, by, deg);
  c.poly(T([[bx-8,by-88],[bx-2.5,by-34],[bx+2.5,by-34],[bx+8,by-88]]), {open:true, cls:'bold'});
  c.poly(T([[bx-2,by-34],[bx+2,by-34],[bx+2,by-6],[bx-2,by-6]]), {fill:'gray', fs:'solid', rough:0.4});
  c.poly(T([[bx-3,by-6],[bx+3,by-6],[bx+3,by],[bx-3,by]]), {fill:'ink', fs:'solid', rough:0.4});
  c.poly(T([[bx-10,by-97],[bx+10,by-97],[bx+10,by-89],[bx-10,by-89]]), {fill:'gray', gap:4});
  c.poly(T([[bx-6.5,by-63],[bx+6.5,by-63],[bx+6.5,by-58],[bx-6.5,by-58]]), {fill:'gray', fs:'solid', rough:0.4});
}
P.crutches = {w:52, h:100, dh:20, draw(c,o){
  if(o.n===1){ crutch(c, 26, 98, 0); return; }
  crutch(c, 14, 98, 0); crutch(c, 38, 98, 0);
}};

// wheelchair: side view, facing right. o.who (cast name of a person seated in it, e.g. 'grandma'), o.mood, o.color (seat, default 'blue')
P.wheelchair = {w:66, h:86, dh:18, draw(c,o){
  const col=o.color||'blue';
  if(o.who) c.sub(34, 35, 74, 'person', {who:o.who, pose:'sit', mood:o.mood||'happy'});
  c.poly([[10,14],[18,14],[23,48],[48,48],[50,66],[59,66]], {open:true});
  c.poly([[19,18],[25,18],[27.5,46],[22.5,46]], {fill:col, gap:5});
  c.rect(23, 42, 25, 6, {fill:col, gap:5});
  c.poly([[24,31],[44,31],[46,48]], {open:true});
  c.circle(28, 60, 44, {cls:'bold'});
  c.circle(28, 60, 37, {cls:'thin'});
  for(let a=0;a<180;a+=45){ const r=rad(a); c.line(28-18*Math.cos(r), 60-18*Math.sin(r), 28+18*Math.cos(r), 60+18*Math.sin(r), {cls:'thin', color:'gray', rough:0.4}); }
  c.dot(28, 60, 5);
  c.line(49, 58, 57, 72);
  c.circle(58, 77, 10, {fill:'paper', fs:'solid'}); c.dot(58, 77, 3);
}};

// hospitalbed: hospital bed, side view, head at the left. o.patient (head on the pillow, blanket over the body), o.iv (IV drip stand), o.color (blanket, default 'sky')
P.hospitalbed = {w:114, h:72, dh:16, draw(c,o){
  const col=o.color||'sky';
  if(o.iv){ c.line(6, 6, 6, 66); c.line(1, 66, 11, 66); c.line(2, 8, 10, 8); c.rrect(1, 9, 9, 13, 3, {fill:'sky', gap:4, cls:'soft'}); c.curve([[6,22],[10,32],[18,36],[26,38]], {cls:'thin', color:'gray'}); }
  sRR(c, 12, 16, 8, 44, 2, {fill:'gray', gap:5});
  sRR(c, 100, 26, 8, 34, 2, {fill:'gray', gap:5});
  sRect(c, 20, 38, 80, 8, {});
  if(o.patient){
    sBlob(c, [[20,32],[32,30],[34,37],[21,38]], {});
    c.circle(29, 29, 13, {fill:'paper', fs:'solid'}); c.arc(26, 28, 3.5, 2.5, 0, 180, {cls:'thin'}); c.arc(32, 28, 3.5, 2.5, 0, 180, {cls:'thin'}); c.arc(29, 32, 4, 2.4, 20, 160, {cls:'thin'});
    sBlob(c, [[34,38],[38,31],[60,29],[84,30],[98,34],[99,40],[34,40]], {fill:col, gap:6});
  } else {
    sBlob(c, [[21,32],[33,30],[35,37],[22,38]], {});
    sPoly(c, [[64,34],[99,34],[99,40],[64,40]], {fill:col, gap:6});
  }
  c.line(20, 50, 100, 50, {cls:'bold'});
  c.rect(42, 44, 36, 4, {fill:'gray', fs:'solid', rough:0.4, cls:'soft'});
  [[26,26],[94,94]].forEach(([x])=>{ c.line(x, 50, x, 61); c.circle(x, 64, 8, {fill:'paper', fs:'solid'}); });
}};

// pills: prescription pill bottle with loose capsules. o.spill (default true), o.color (bottle, default 'orange')
P.pills = {w:52, h:58, dh:8, draw(c,o){
  if(tiny(c)){ c.rrect(6, 16, 26, 40, 3, tf(o.color||'orange')); c.rect(3, 5, 32, 12, tf('white')); c.rect(10, 26, 18, 20, tn('paper'));
    if(o.spill!==false) c.poly(stadium(43, 50, 16, 8, -35), tf('red')); return; }
  sRR(c, 6, 16, 26, 40, 3, {fill:o.color||'orange', gap:6});
  sRR(c, 3, 5, 32, 12, 2, {fill:'white', fs:'solid'});
  [9,14,19,24,29].forEach(x=>c.line(x, 7, x, 15, {cls:'thin', color:'gray', rough:0.3}));
  sRect(c, 9, 25, 20, 21, {fill:'paper', fs:'solid', rough:0.5});
  c.text(19, 40, 'Rx', {size:11, color:'blue'});
  if(o.spill!==false){
    c.poly(stadium(43, 50, 16, 7.5, -35), back()); c.poly(stadium(43, 50, 16, 7.5, -35, 'l'), {fill:'red', fs:'solid', rough:0.3, nostroke:true}); c.poly(stadium(43, 50, 16, 7.5, -35), {rough:0.4});
    c.circle(43, 35, 9, {fill:'white', fs:'solid', rough:0.4}); c.line(40, 35, 46, 35, {cls:'thin', rough:0.3});
  }
}};

// stethoscope: doctor's stethoscope
P.stethoscope = {w:62, h:66, dh:10, draw(c,o){
  c.curve([[14,6],[12,18],[18,30],[30,38]], {cls:'bold'});
  c.curve([[42,6],[46,18],[42,30],[30,38]], {cls:'bold'});
  c.dot(14, 5, 5); c.dot(42, 5, 5);
  c.curve([[30,38],[28,50],[34,60],[46,60],[52,52],[52,44]], {cls:'bold'});
  c.circle(52, 40, 14, {fill:'gray', fs:'solid'});
  c.circle(52, 40, 7, {fill:'paper', fs:'solid', rough:0.4});
}};

/* ---------- Office and tech ---------- */

// computer: desktop monitor with keyboard and mouse. o.screen: 'lines' (default) | 'chart' | 'alert' (hacked: red warning) | 'lock' | 'off'
P.computer = {w:86, h:70, dh:14, anchors:{screen:()=>[42,24]}, draw(c,o){
  const s=o.screen||'lines';
  c.rrect(10, 2, 64, 44, 4, {fill:'ink', fs:'solid', cls:'soft'});
  const scr = s==='off' ? {fill:'ink', gap:3.5, cls:'soft'} : s==='alert' ? {fill:'red', gap:6, cls:'soft'} : {fill:'sky', gap:6, cls:'soft'};
  sRect(c, 15, 7, 54, 34, scr);
  if(s==='lines'){ c.rect(19, 11, 30, 6, {fill:'blue', fs:'solid', rough:0.4, cls:'soft2'}); [22,27,32].forEach((y,i)=>c.line(20, y, [62,54,58][i], y, {cls:'thin', rough:0.4})); }
  else if(s==='chart'){ [[22,30],[31,24],[40,27],[49,17],[58,13]].forEach(([x,y],i)=>c.rect(x, y, 6, 38-y, {fill:['blue','blue','blue','green','green'][i], fs:'solid', rough:0.4, cls:'soft2'})); c.line(19, 38, 66, 38, {cls:'thin'}); }
  else if(s==='alert'){ sPoly(c, [[42,10],[54,35],[30,35]], {fill:'yellow', fs:'solid', rough:0.5}); c.text(42, 33, '!', {size:13, bold:true}); }
  else if(s==='lock'){ c.arc(42, 21, 12, 14, 180, 360, {cls:'bold'}); sRR(c, 34, 20, 16, 14, 2, {fill:'yellow', fs:'solid'}); c.dot(42, 27, 3); }
  c.poly([[37,46],[47,46],[49,53],[35,53]], {fill:'ink', fs:'solid', cls:'soft', rough:0.5});
  c.rrect(28, 52, 28, 4, 2, {fill:'ink', fs:'solid', cls:'soft'});
  sPoly(c, [[12,59],[66,59],[70,67],[8,67]], {fill:'gray', gap:6, cls:'soft'});
  c.line(14, 63, 66, 63, {cls:'thin', rough:0.4});
  sRR(c, 74, 58, 9, 11, 4, {});
}};

// server: server rack (data center, cyber). o.alert (red warning lights and a warning sign), o.n (units, default 6)
P.server = {w:52, h:98, dh:22, draw(c,o){
  const n=Math.max(3, Math.min(7, o.n||6)), H=78/n;
  sRR(c, 4, 2, 44, 90, 3, {fill:'ink', fs:'solid', cls:'soft'});
  for(let i=0;i<n;i++){
    const y=8+i*H;
    sRect(c, 9, y, 34, H-3.5, {fill:'paper', fs:'solid', rough:0.5});
    c.line(13, y+(H-3.5)/2, 27, y+(H-3.5)/2, {cls:'thin', color:'gray', rough:0.3});
    c.dot(33, y+(H-3.5)/2, 3.2, {color:o.alert && i%2===0 ? 'red' : 'green'});
    c.dot(38.5, y+(H-3.5)/2, 3.2, {color:o.alert ? 'red' : (i%3===1 ? 'orange' : 'green')});
  }
  c.rect(9, 92, 7, 4, {fill:'ink', fs:'solid', rough:0.4}); c.rect(36, 92, 7, 4, {fill:'ink', fs:'solid', rough:0.4});
  if(o.alert){ sPoly(c, [[26,28],[42,58],[10,58]], {fill:'yellow', fs:'solid', rough:0.5}); c.text(26, 55, '!', {size:16, bold:true, color:'red'}); }
}};

// envelope: letter envelope. o.open (flap up, letter peeking out), o.seal (red wax seal on the flap), o.color (paper tint)
P.envelope = {w:62, h:48, dh:8, draw(c,o){
  const y0=10, y1=46, mid=31;
  if(tiny(c)){ c.rect(2, y0, 58, y1-y0, tf(o.color||'paper')); c.poly([[3,y0+1],[31,mid],[59,y0+1]], tl({open:true, cls:''})); if(o.seal) c.circle(31, mid-1, 10, tn('red')); return; }
  if(o.open){
    sPoly(c, [[2,y0],[31,-4],[60,y0]], {fill:o.color||null, gap:8, cls:'soft'});
    sRect(c, 9, 2, 44, 28, {fill:'paper', fs:'solid'}); gline(c, 14, 9, 46); gline(c, 14, 14, 42); gline(c, 14, 19, 44);
    sRect(c, 2, y0, 58, y1-y0, {fill:o.color||null, gap:8, cls:'soft'});
    c.poly([[2,y0],[31,mid],[60,y0]], {open:true});
    return;
  }
  sRect(c, 2, y0, 58, y1-y0, {fill:o.color||null, gap:8, cls:'soft'});
  c.poly([[2,y1],[24,24],[38,24],[60,y1]], {open:true, cls:'thin', color:'gray'});
  sPoly(c, [[2,y0],[31,mid],[60,y0]], {fill:o.color||null, gap:8, cls:'soft'});
  if(o.seal) c.circle(31, mid-1, 9, {fill:'red', fs:'solid', rough:0.5});
}};

// megaphone: bullhorn facing right. o.waves (sound lines, default true), o.color (default 'red')
P.megaphone = {w:72, h:52, dh:10, draw(c,o){
  if(tiny(c)){ c.rect(22, 32, 8, 15, tf('gray')); c.rect(6, 18, 16, 16, tf('gray')); c.poly([[20,18],[50,6],[50,46],[20,34]], tf(o.color||'red')); c.ellipse(50, 26, 10, 40, tf('paper'));
    if(o.waves!==false) c.arc(53, 26, 30, 36, -45, 45, tl()); return; }
  sPoly(c, [[22,32],[30,32],[29,47],[22,47]], {fill:'ink', fs:'solid', cls:'soft', rough:0.5});
  sRR(c, 6, 18, 16, 16, 3, {fill:'gray', gap:5});
  sPoly(c, [[20,18],[50,6],[50,46],[20,34]], {fill:o.color||'red', gap:7});
  c.ellipse(50, 26, 10, 40, {fill:'paper', fs:'solid'});
  c.ellipse(50, 26, 5, 30, {cls:'thin'});
  if(o.waves!==false){ c.arc(53, 26, 22, 26, -45, 45, {rough:0.5}); c.arc(53, 26, 34, 42, -45, 45, {rough:0.5}); }
}};

// sign: signboard on a post. o.text (a short word or two; '\n' for a second line), o.color (board border tint), o.tcolor (text color)
P.sign = {w:72, h:86, dh:20, draw(c,o){
  const tny=tiny(c);
  if(tny){ c.rect(32, 36, 8, 46, tf('brown')); c.rect(4, 6, 64, 32, tf('paper')); if(o.color) c.rect(4, 6, 64, 32, tl({color:o.color, cls:''}));
    const t=String(o.text==null?'':o.text).replace(/\n/g,' ');
    if(t) c.text(36, 22+fitText(t, 58, 22)*0.34, t, {size:fitText(t, 58, 22), color:o.tcolor||'ink'}); else { c.line(14, 18, 58, 18, tl()); c.line(14, 26, 50, 26, tl()); }
    return; }
  sRect(c, 33, 36, 6, 46, {fill:'brown', gap:5});
  c.line(22, 82, 50, 82, {rough:0.6});
  sRR(c, 4, 6, 64, 32, 3, {fill:'paper', fs:'solid'});
  if(o.color) c.rrect(7.5, 9.5, 57, 25, 2, {color:o.color, rough:0.5});
  const lines=String(o.text==null?'':o.text).split('\n').filter(s=>s.length).slice(0,2);
  if(!lines.length){ gline(c, 14, 18, 58, {color:'ink'}); gline(c, 14, 26, 50, {color:'ink'}); return; }
  const size=Math.min(...lines.map(l=>fitText(l, 54, lines.length>1?11:15)));
  if(lines.length===1) c.text(36, 22+size*0.34, lines[0], {size, color:o.tcolor||'ink'});
  else lines.forEach((l,i)=>c.text(36, 20+i*11.5-1.5+size*0.2, l, {size, color:o.tcolor||'ink'}));
}};

// folder: manila file folder with papers. o.label (short text on the front), o.color (default 'yellow'), o.papers (default true)
P.folder = {w:66, h:52, dh:10, draw(c,o){
  const col=o.color||'yellow';
  if(tiny(c)){ c.poly([[4,8],[22,8],[26,14],[62,14],[62,48],[4,48]], tf(col, {cls:'thin soft'})); if(o.papers!==false) c.rect(26, 7, 30, 20, tf('paper')); c.rect(4, 22, 58, 26, tf(col)); return; }
  sPoly(c, [[4,8],[22,8],[26,14],[62,14],[62,48],[4,48]], {fill:col, gap:9, cls:'soft'});
  if(o.papers!==false){ sRect(c, 24, 9, 32, 20, {fill:'paper', fs:'solid', rough:0.5}); sRect(c, 29, 5, 30, 20, {fill:'paper', fs:'solid', rough:0.5}); gline(c, 33, 11, 54); gline(c, 33, 16, 50); }
  sPoly(c, [[4,22],[62,22],[62,48],[4,48]], {fill:col, gap:7});
  if(o.label){ sRect(c, 18, 28, 30, 11, {fill:'paper', fs:'solid', rough:0.5}); c.text(33, 36.5, o.label, {size:fitText(o.label, 26, 7.5)}); }
}};

// filecabinet: metal filing cabinet. o.n (drawers 2-4, default 4), o.open (top drawer pulled out with files), o.color (default 'gray')
P.filecabinet = {w:52, h:92, dh:20, draw(c,o){
  const n=Math.max(2, Math.min(4, o.n||4)), col=o.color||'gray', H=(84-2)/n;
  sRect(c, 5, 4, 42, 86, {fill:col, gap:10, cls:'soft'});
  for(let i=0;i<n;i++){
    const y=7+i*H;
    if(o.open && i===0){
      c.rect(9, y, 34, H-4, {fill:'ink', fs:'solid', cls:'soft'});
      sPoly(c, [[9,y+1],[43,y+1],[50,y+9],[2,y+9]], {fill:'paper', fs:'solid'});
      [[12,'blue'],[20,'yellow'],[28,'green'],[36,'red']].forEach(([x,cl],k)=>c.poly([[x,y-3+k%2*2],[x+6,y-3+k%2*2],[x+6.5,y+6],[x-0.5,y+6]], {fill:cl, fs:'solid', rough:0.4, cls:'soft2'}));
      sRect(c, 2, y+9, 48, H-4, {fill:col, gap:8});
      c.rect(19, y+12, 14, 5, {fill:'paper', fs:'solid', rough:0.4, cls:'thin'});
      c.line(18, y+9+(H-4)/2+3, 34, y+9+(H-4)/2+3, {cls:'bold'});
      continue;
    }
    sRect(c, 9, y, 34, H-4, {});
    c.rect(20, y+4, 12, 5, {fill:'paper', fs:'solid', rough:0.4, cls:'thin'});
    c.line(19, y+(H-4)/2+3, 33, y+(H-4)/2+3, {cls:'bold'});
  }
}};

// desk: office desk (drawers on the left) with a computer. o.computer (default true), o.screen (passed to the computer), o.mug (default true), o.papers (paper stack)
P.desk = {w:120, h:80, dh:18, draw(c,o){
  if(o.computer!==false) c.sub(70, 21, 36, 'computer', {screen:o.screen});
  if(o.mug!==false){ sRR(c, 22, 26, 9, 12, 2, {fill:'red', gap:4}); c.arc(31, 31.5, 7, 7, 270, 450, {cls:'thin'}); c.curve([[25,22],[27,19],[25,16]], {color:'gray', cls:'thin'}); }
  if(o.papers){ c.rect(98, 34, 16, 4, {fill:'paper', fs:'solid'}); c.rect(99, 31, 15, 3, {fill:'paper', fs:'solid'}); }
  sRect(c, 4, 38, 112, 7, {fill:'brown', gap:6});
  sRect(c, 10, 45, 32, 33, {fill:'brown', gap:12, cls:'soft'});
  [55.5,66.5].forEach(y=>c.line(10, y, 42, y, {cls:'thin'}));
  [50,61,72].forEach(y=>c.line(22, y, 30, y, {cls:'bold'}));
  sRect(c, 104, 45, 7, 33, {fill:'brown', gap:6});
}};

// chair: office swivel chair, front view. o.color (default 'blue')
P.chair = {w:52, h:82, dh:16, draw(c,o){
  const col=o.color||'blue';
  sRR(c, 13, 2, 26, 36, 8, {fill:col, gap:7});
  c.line(26, 38, 26, 44, {cls:'bold'});
  c.poly([[6,36],[6,46],[12,46]], {open:true}); c.poly([[46,36],[46,46],[40,46]], {open:true});
  sRR(c, 6, 44, 40, 9, 4, {fill:col, gap:6});
  sRect(c, 23, 53, 6, 12, {fill:'gray', fs:'solid', rough:0.4});
  c.line(26, 66, 6, 74); c.line(26, 66, 46, 74); c.line(26, 66, 20, 75); c.line(26, 66, 32, 75);
  [[6,77],[46,77],[19,78],[33,78]].forEach(([x,y])=>c.circle(x, y, 5.5, {fill:'ink', fs:'solid', rough:0.4}));
}};

/* ---------- Money and payments ---------- */

// piggybank: piggy bank facing right. o.coin (a coin dropping into the slot), o.color (default 'pink')
P.piggybank = {w:82, h:66, dh:12, draw(c,o){
  const col=o.color||'pink';
  c.curve([[10,36],[4,33],[5,28],[9,30],[7,34],[2,36]], {cls:'thin'});
  [[18,52],[56,52]].forEach(([x,y])=>sRR(c, x, y, 8, 12, 2, {fill:col, gap:5}));
  sBlob(c, [[10,38],[16,24],[34,17],[54,18],[68,28],[72,40],[64,52],[40,57],[18,52]], {fill:col, gap:8});
  [[26,54],[62,52]].forEach(([x,y])=>sRR(c, x, y, 8, 12, 2, {fill:col, gap:5}));
  sPoly(c, [[50,19],[56,8],[62,22]], {fill:col, gap:4});
  c.ellipse(72, 38, 10, 14, {fill:'paper', fs:'solid'}); c.dot(71, 35.5, 2.5); c.dot(71, 40.5, 2.5);
  c.dot(60, 30, 3.6);
  c.line(32, 21, 46, 20, {cls:'bold', rough:0.4});
  if(o.coin){ c.circle(39, 9, 13, {fill:'yellow', fs:'solid', color:'orange'}); c.text(39, 13, '$', {size:10, color:'orange'}); }
}};

// wallet: leather wallet with cash sticking out. o.empty (no cash: open and empty), o.color (default 'brown')
P.wallet = {w:66, h:48, dh:8, draw(c,o){
  const col=o.color||'brown';
  if(tiny(c)){ if(!o.empty) c.rect(12, 4, 42, 16, tf('green')); c.rrect(4, 14, 58, 32, 5, tf(col)); c.rrect(32, 20, 30, 18, 4, tl({cls:''})); c.circle(38, 29, 6, tn('yellow')); return; }
  if(!o.empty){ sRect(c, 10, 2, 40, 18, {fill:'green', gap:7, cls:'soft'}); sRect(c, 16, 6, 40, 16, {fill:'green', gap:7, cls:'soft'}); c.circle(36, 10, 7, {color:'green', cls:'thin', rough:0.4}); }
  sRR(c, 4, 14, 58, 32, 5, {fill:col, gap:9});
  sRR(c, 32, 20, 30, 18, 4, {fill:col, gap:6});
  c.dot(38, 29, 4, {color:'yellow'});
  if(o.empty){ c.blob([[34,7],[27,2],[25,8],[33,10]], {fill:'gray', fs:'solid', cls:'soft', rough:0.5}); c.blob([[38,7],[45,2],[47,8],[39,10]], {fill:'gray', fs:'solid', cls:'soft', rough:0.5}); c.line(36, 4, 36, 12, {cls:'bold', rough:0.3}); c.curve([[36,13],[30,15],[24,13]], {cls:'thin', color:'gray'}); }
}};

// creditcard: bank card with chip. o.color (default 'blue'), o.back (magnetic stripe side)
P.creditcard = {w:64, h:42, dh:7, draw(c,o){
  if(tiny(c)){ c.rrect(2, 2, 60, 38, 4, tf(o.color||'blue')); if(o.back) c.rect(3, 9, 58, 8, tn('ink')); else { c.rect(9, 11, 13, 10, tn('yellow')); c.line(8, 30, 54, 30, tl({color:'paper', cls:''})); } return; }
  sRR(c, 2, 2, 60, 38, 4, {fill:o.color||'blue', gap:7});
  if(o.back){ c.rect(2.5, 9, 59, 8, {fill:'ink', fs:'solid', rough:0.3}); c.rect(8, 22, 34, 7, {fill:'paper', fs:'solid', rough:0.4}); return; }
  sRR(c, 9, 11, 12, 10, 2, {fill:'yellow', fs:'solid'});
  c.line(9, 16, 21, 16, {cls:'thin', rough:0.3});
  [8,22,36,50].forEach(x=>c.line(x, 29, x+9, 29, {cls:'bold', rough:0.4}));
  c.line(8, 35, 30, 35, {cls:'thin', rough:0.4});
}};

// receipt: long paper receipt with $ lines and a total. o.n (item lines 2-6, default 4), o.total (total text, default '$$$')
P.receipt = {w:40, h:82, dh:14, draw(c,o){
  const n=Math.max(2, Math.min(6, o.n||4));
  if(tiny(c)){ const q=[[4,2],[36,2],[36,74]]; for(let i=0;i<4;i++) q.push([36-(i+0.5)*8, i%2?74:80]); q.push([4,74]); c.poly(q, tf('paper'));
    [14,26,38,50].forEach(y=>c.line(9, y, 31, y, tl({color:'gray'}))); c.line(9, 62, 31, 62, tl({color:'green', cls:'bold'})); return; }
  const pts=[[4,2],[36,2],[36,74]]; for(let i=0;i<8;i++) pts.push([36-(i+0.5)*4, i%2?74:79]); pts.push([4,74]);
  sPoly(c, pts, {fill:'paper', fs:'solid', rough:0.5});
  c.line(13, 10, 27, 10, {cls:'bold', rough:0.4});
  const top=18, step=Math.min(9, 36/n);
  for(let i=0;i<n;i++){ const y=top+i*step; gline(c, 8, y, 21); c.text(31, y+2.4, '$', {size:Math.min(7.5, step*1.1), color:'green'}); }
  const ty=top+n*step+2;
  c.line(7, ty, 33, ty, {cls:'thin', rough:0.4});
  c.text(20, ty+11, o.total||'$$$', {size:fitText(o.total||'$$$', 26, 10), color:'green', bold:true});
}};

})();
