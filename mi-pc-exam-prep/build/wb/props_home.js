/* ---------- Sketch props: home, belongings and household systems ----------
   Same contract as props_core.js: {w, h, dh, anchors?, draw(c, opt, el)}; draw in the prop's own w x h box.
   Variants are listed in the one-line comment above each prop. */
(()=>{
const P = SK.PROPS;

/* helpers */
const TINY = 0.9;   // c.k below this = drawn very small (e.g. held in a person's hand): use flat fills and single thin strokes
const back = () => ({fill:'paper', fs:'solid', nostroke:true});           // paper underlay: hides what is behind a hatched shape
function sPoly(c, pts, o){ c.poly(pts, back()); c.poly(pts, o); }
function sRect(c, x, y, w, h, o){ c.rect(x, y, w, h, back()); c.rect(x, y, w, h, o); }
function sRR(c, x, y, w, h, r, o){ c.rrect(x, y, w, h, r, back()); c.rrect(x, y, w, h, r, o); }
function sBlob(c, pts, o){ c.blob(pts, back()); c.blob(pts, o); }
function drop(c, x, y, s, o){ // water drop, point up
  c.poly([[x,y-s],[x+0.38*s,y-0.05*s],[x+0.5*s,y+0.35*s],[x+0.3*s,y+0.62*s],[x,y+0.7*s],[x-0.3*s,y+0.62*s],[x-0.5*s,y+0.35*s],[x-0.38*s,y-0.05*s]],
    Object.assign({color:'blue', fill:'blue', fs:'solid', rough:0.3, single:true}, o));
}
function jets(c, x, y, rays, o){ // water jets from (x,y): rays = [[dx,dy,bend],...]
  rays.forEach(([dx,dy,b])=>{ const mx=x+dx*0.5-dy*b, my=y+dy*0.5+dx*b; c.curve([[x,y],[mx,my],[x+dx,y+dy]], Object.assign({color:'blue'}, o)); });
}
function sparkle(c, x, y, s, col){ c.line(x,y-s,x,y+s,{color:col||'orange', cls:'thin', rough:0.3}); c.line(x-s*0.8,y,x+s*0.8,y,{color:col||'orange', cls:'thin', rough:0.3}); }
function crack(c, x, y, rays, o){ rays.forEach(r=>c.poly([[x,y]].concat(r), Object.assign({open:true, cls:'thin', rough:0.4}, o))); }
function tuft(c, x, y, s){ c.poly([[x-2*s,y],[x-1.2*s,y-4*s],[x-0.3*s,y],[x+0.6*s,y-5*s],[x+1.2*s,y],[x+2.2*s,y-3.5*s]],{open:true, color:'green', cls:'thin', rough:0.5}); }

/* ---------- Furniture and electronics ---------- */

// sofa: o.color (fabric hatch, default 'teal'), o.pillow (default true)
P.sofa = {w:100, h:58, dh:12, draw(c,o){
  const col=o.color||'teal';
  c.rrect(14,4,72,32,8,{fill:col, gap:9});
  if(o.pillow!==false) sBlob(c,[[24,17],[36,15],[38,29],[25,31]],{fill:'yellow', gap:5});
  sRect(c,20,32,30,12,{fill:col, gap:8, cls:'soft'}); sRect(c,50,32,30,12,{fill:col, gap:8, cls:'soft'});
  sRect(c,18,44,64,6,{fill:col, gap:7});
  sRR(c,2,20,18,31,8,{fill:col, gap:8}); sRR(c,80,20,18,31,8,{fill:col, gap:8});
  c.line(7,51,6,56,{cls:'bold'}); c.line(93,51,94,56,{cls:'bold'});
}};

// tv: flat screen on a stand. o.broken (cracked screen), o.off (dark screen), o.retro (old box TV with rabbit ears)
P.tv = {w:80, h:64, dh:11, anchors:{screen:()=>[40,27]}, draw(c,o){
  const scr = o.off ? {fill:'ink', gap:3.5, cls:'soft'} : {fill:'sky', gap:6, cls:'soft'};
  if(o.retro){
    c.line(40,16,27,3,{cls:'thin'}); c.line(40,16,54,2,{cls:'thin'}); c.dot(27,3,3); c.dot(54,2,3);
    c.arc(40,19,16,10,180,360,{closed:true, fill:'ink', fs:'solid', cls:'soft'});
    sRR(c,6,18,68,40,6,{fill:'brown', gap:8});
    sRR(c,12,24,42,28,7,scr);
    c.circle(63,31,7,{fill:'paper', fs:'solid'}); c.circle(63,43,7,{fill:'paper', fs:'solid'});
    c.line(16,58,13,63,{cls:'bold'}); c.line(64,58,67,63,{cls:'bold'});
    if(o.broken) crack(c,30,35,[[[26,30],[19,27]],[[35,30],[42,27]],[[37,39],[46,44]],[[28,41],[24,49]],[[24,36],[14,38]]]);
    return;
  }
  c.rrect(3,4,74,46,3,{fill:'ink', fs:'solid', cls:'soft'});
  sRect(c,8,9,64,36,scr);
  if(!o.off && !o.broken){ c.poly([[8,45],[22,31],[31,39],[45,25],[72,45]],{fill:'green', gap:6, rough:0.6}); c.circle(60,18,8,{color:'orange', fill:'yellow', fs:'solid', rough:0.5}); }
  if(o.broken){
    c.poly([[28,19],[31,18],[33,21],[31,24],[28,23]],{fill:'ink', fs:'solid', rough:0.4});
    crack(c,30,21,[[[25,15],[18,10]],[[35,15],[40,9]],[[38,22],[48,20],[60,26]],[[34,27],[38,35],[36,44]],[[26,26],[17,31],[9,29]],[[25,21],[9,18]]]);
  }
  c.poly([[35,50],[45,50],[46,57],[34,57]],{fill:'ink', fs:'solid', cls:'soft'});
  c.rrect(20,57,40,4,2,{fill:'ink', fs:'solid', cls:'soft'});
}};

// laptop: open laptop, front view. o.broken (cracked screen), o.off (dark screen)
P.laptop = {w:80, h:56, dh:7, anchors:{screen:()=>[40,20]}, draw(c,o){
  c.rrect(14,2,52,37,3,{fill:'ink', fs:'solid', cls:'soft'});
  sRect(c,18,6,44,29, o.off ? {fill:'ink', gap:3.5, cls:'soft'} : {fill:'sky', gap:6, cls:'soft'});
  if(!o.off && !o.broken){ c.rect(22,10,36,5,{fill:'blue', fs:'solid', rough:0.4, cls:'soft'}); [19,24,29].forEach((y,i)=>c.line(23,y,[52,46,40][i],y,{cls:'thin', rough:0.4})); }
  if(o.broken) crack(c,34,18,[[[28,12],[22,8]],[[40,12],[46,7]],[[42,20],[54,23],[61,22]],[[36,25],[40,34]],[[29,22],[20,27]]]);
  sPoly(c,[[14,39],[66,39],[78,50],[2,50]],{fill:'gray', gap:6, cls:'soft'});
  sPoly(c,[[20,41],[60,41],[63,45.5],[17,45.5]],{fill:'ink', gap:2.4, cls:'thin', rough:0.5});
  c.rrect(2,50,76,4,2,{fill:'ink', fs:'solid', cls:'soft'});
}};

// ring: gold diamond ring. o.gem (stone hatch color, default 'sky')
P.ring = {w:50, h:60, dh:6, draw(c,o){
  c.circle(25,41,34,{color:'orange', fill:'yellow', fs:'solid'});
  c.circle(25,41,23,{color:'orange', fill:'paper', fs:'solid'});
  c.poly([[19,21],[31,21],[28,26],[22,26]],{color:'orange', fill:'yellow', fs:'solid', rough:0.4});
  sPoly(c,[[19,3],[31,3],[37,10],[25,23],[13,10]],{fill:o.gem||'sky', gap:4, cls:'soft', rough:0.5});
  [[13,10,37,10],[19,3,22,10],[31,3,28,10],[22,10,25,23],[28,10,25,23]].forEach(l=>c.line(l[0],l[1],l[2],l[3],{cls:'thin', rough:0.3}));
  sparkle(c,42,5,4); sparkle(c,8,17,2.6);
}};

P.diamondring = P.ring;   // alias: the scene renderer treats p:'ring' as the circle-highlight primitive, so scenes must use 'diamondring'

// camera: photo camera, front view. o.flash (default true: lit flash with sparkle lines)
P.camera = {w:72, h:52, dh:6, draw(c,o){
  c.rrect(18,5,24,12,3,{fill:'ink', fs:'solid', cls:'soft'});
  c.rrect(51,8,10,6,2,{fill:'red', fs:'solid'});
  sRR(c,3,13,66,36,6,{fill:'gray', gap:7, cls:'soft'});
  c.line(13,13,13,49,{cls:'thin'});
  c.circle(36,31,31,{fill:'paper', fs:'solid'}); c.circle(36,31,21,{fill:'sky', gap:4, cls:'soft'}); c.circle(36,31,9,{fill:'ink', fs:'solid', cls:'soft'});
  c.arc(36,31,15,15,200,250,{cls:'thin', rough:0.3});
  c.rect(52,18,12,6,{fill:'yellow', fs:'solid', rough:0.5});
  if(o.flash){ [[58,14,58,7],[64,15,69,9],[52,15,47,9]].forEach(l=>c.line(l[0],l[1],l[2],l[3],{color:'orange', cls:'thin'})); }
}};

// guitar: acoustic guitar, upright. o.color (body hatch, default 'orange')
P.guitar = {w:44, h:100, dh:15, draw(c,o){
  sBlob(c,[[22,40],[32,41],[36,49],[31,59],[38,69],[40,82],[33,94],[22,98],[11,94],[4,82],[6,69],[13,59],[8,49],[12,41]],{fill:o.color||'orange', gap:6});
  c.circle(22,66,12,{fill:'ink', fs:'solid'});
  sRect(c,19,12,6,46,{fill:'brown', fs:'solid', cls:'soft2'});
  [20,28,36,44].forEach(y=>c.line(19,y,25,y,{color:'paper', cls:'thin', rough:0.3}));
  sPoly(c,[[15,1],[29,1],[27,13],[17,13]],{fill:'brown', fs:'solid'});
  [[13,4],[13,9],[31,4],[31,9]].forEach(p=>c.dot(p[0],p[1],3));
  c.rect(14,82,16,4,{fill:'ink', fs:'solid', rough:0.5});
  c.line(21,57,21,83,{cls:'thin', color:'gray', rough:0.3}); c.line(23,57,23,83,{cls:'thin', color:'gray', rough:0.3});
}};

// bicycle: faces right. o.color (frame, default 'red')
P.bicycle = {w:120, h:74, dh:13, draw(c,o){
  const col=o.color||'red', F={color:col, cls:'bold'};
  [26,94].forEach(x=>{ c.circle(x,50,42,{}); c.circle(x,50,34,{cls:'thin', color:'gray'});
    [0,60,120].forEach(a=>{ const r=a*Math.PI/180; c.line(x-16*Math.cos(r),50-16*Math.sin(r),x+16*Math.cos(r),50+16*Math.sin(r),{cls:'thin', color:'gray', rough:0.4}); }); c.dot(x,50,4); });
  c.line(26,50,56,52,F); c.line(26,50,49,25,F); c.line(56,52,47,18,F); c.line(48,24,85,24,F); c.line(56,52,84,30,F);
  c.line(87,18,84,32,F); c.line(84,32,94,50,F);
  c.poly([[38,15],[53,14],[51,19],[41,19]],{fill:'ink', fs:'solid', rough:0.5});
  c.poly([[87,19],[88,12],[80,10]],{open:true, cls:'bold'});
  c.circle(56,52,10,{cls:'thin'}); c.line(56,52,62,61,{cls:'bold'}); c.line(58,61,67,61,{cls:'bold'});
}};

/* ---------- Home systems (water, heat) ---------- */

// washer: front-loading washing machine. o.hose (burst supply hose spraying water), o.color (body hatch, default none)
P.washer = {w:60, h:70, dh:13, anchors:{hose:()=>[78,58]}, draw(c,o){
  if(o.hose){
    c.ellipse(76,67,34,6,{color:'blue', fill:'blue', gap:5, cls:'soft'});
    c.curve([[55,22],[64,24],[66,38],[66,52],[71,58],[77,59]],{color:'gray', cls:'bold'});
    c.poly([[76,57],[78,58.5],[76.5,60],[79,61]],{open:true, cls:'thin'});
  }
  sRR(c,4,4,52,62,4, o.color ? {fill:o.color, gap:12, cls:'soft'} : {});
  c.line(4,17,56,17);
  c.rect(10,8,16,6,{fill:'ink', fs:'solid', cls:'soft', rough:0.4}); c.circle(45,10.5,8,{fill:'paper', fs:'solid'}); c.line(45,10.5,47.5,7.5,{cls:'thin'});
  c.circle(30,42,36,{fill:'paper', fs:'solid', cls:'bold'});
  c.circle(30,42,26,{fill:'sky', gap:5, cls:'soft'});
  c.curve([[22,46],[27,40],[33,45],[38,39]],{color:'blue', cls:'thin'}); c.circle(25,37,4,{color:'blue', cls:'thin', rough:0.3}); c.circle(35,49,3,{color:'blue', cls:'thin', rough:0.3});
  c.rect(9,66,6,3,{fill:'ink', fs:'solid', rough:0.3}); c.rect(45,66,6,3,{fill:'ink', fs:'solid', rough:0.3});
  if(o.hose){
    jets(c,78,58,[[10,-16,0.15],[18,-8,0.12],[2,-20,-0.12],[16,2,0.1]]);
    [[89,40],[97,48],[80,36],[96,61],[86,33]].forEach((p,i)=>drop(c,p[0],p[1],i%2?3:4));
  }
}};

// waterheater: tank water heater with hot/cold pipes. o.leak (drips, rust crack and a puddle)
P.waterheater = {w:52, h:86, dh:18, anchors:{top:()=>[25,6]}, draw(c,o){
  if(o.leak) c.ellipse(25,81,58,8,{color:'blue', fill:'blue', gap:5, cls:'soft'});
  c.rect(12,0,4,12,{fill:'blue', fs:'solid', rough:0.4}); c.rect(34,0,4,12,{fill:'red', fs:'solid', rough:0.4});
  sRR(c,6,8,38,70,9,{fill:'gray', gap:12, cls:'soft'});
  c.arc(25,15,37,9,15,165,{cls:'thin'}); c.arc(25,70,37,8,15,165,{cls:'thin'});
  c.rect(44,22,6,5,{fill:'ink', fs:'solid', cls:'soft', rough:0.4}); c.line(49,27,49,46,{cls:'bold', color:'gray'});
  c.rect(15,46,20,13,{fill:'paper', fs:'solid'});
  c.circle(21,52.5,6,{fill:'paper', fs:'solid'}); c.line(21,52.5,22.5,50,{cls:'thin'});
  c.sub(29,52.5,7,'fire');
  c.line(10,78,10,82,{cls:'bold'}); c.line(40,78,40,82,{cls:'bold'});
  if(o.leak){
    c.poly([[34,62],[37,65],[35,67],[38,71]],{open:true, color:'brown', cls:'bold', rough:0.5});
    drop(c,36,75,4); drop(c,15,76,3.4); drop(c,49,50,3.4);
  }
}};

// furnace: forced-air furnace with ductwork and a flame window. o.off (no flame), o.smoke (gray smoke from the top, e.g. malfunction)
P.furnace = {w:56, h:86, dh:17, draw(c,o){
  if(o.smoke) c.sub(42,-8,30,'smoke');
  c.rect(20,0,16,7,{fill:'gray', gap:5, cls:'soft'});
  sPoly(c,[[8,16],[48,16],[44,6],[12,6]],{fill:'gray', gap:6, cls:'soft'});
  sRect(c,6,16,44,66,{});
  c.rect(12,22,32,22,{});
  c.rect(19,27,18,12,{fill:'ink', fs:'solid', cls:'soft', rough:0.5});
  if(!o.off) c.sub(28,33,10,'fire');
  for(let i=0;i<5;i++) c.line(13,53+i*5,43,53+i*5,{cls:'thin', rough:0.5});
  c.dot(41,25.5,2.5,{color:'green'});
  c.line(5,83,51,83,{cls:'bold'});
}};

// pipe: horizontal water pipe. o.burst (crack spraying water), o.frozen (icy pipe with icicles and frost)
P.pipe = {w:100, h:44, dh:7, anchors:{burst:()=>[50,17]}, draw(c,o){
  const ice=!!o.frozen;
  c.rect(10,17,80,10,{fill:ice?'sky':'gray', gap:5, cls:'soft'});
  [[3,14],[89,14]].forEach(([x,y])=>c.rect(x,y,8,16,{fill:ice?'sky':'gray', fs:'solid', cls:'soft'}));
  c.rect(67,15.5,5,13,{fill:ice?'sky':'gray', fs:'solid', cls:'soft', rough:0.5});
  if(ice){
    [[16,9],[23,6],[34,11],[41,7],[58,10],[64,6],[78,12],[84,7]].forEach(([x,l])=>c.poly([[x-2.6,27],[x+2.6,27],[x,27+l]],{color:'sky', fill:'sky', fs:'solid', cls:'soft', rough:0.4}));
    c.sub(22,8,10,'snow'); c.sub(80,7,8,'snow');
    [[36,13],[60,13]].forEach(([x,y])=>c.line(x,y,x+5,y-1,{color:'sky', cls:'thin'}));
  }
  if(o.burst){
    c.poly([[48,17],[51.5,19.5],[48.5,22.5],[51.5,25],[49,27]],{open:true, cls:'bold', rough:0.4});
    jets(c,50,17,[[-14,-12,0.1],[-3,-16,0.08],[8,-15,-0.08],[17,-10,-0.1]]);
    [[34,4],[46,0],[59,1],[69,6]].forEach((p,i)=>drop(c,p[0],p[1],i%2?3:3.6));
    drop(c,50,33,3.6); drop(c,47,40,3);
  }
}};

// window: four-pane window with sill. o.broken (impact hole with cracks, shards on the sill)
P.window = {w:60, h:64, dh:14, anchors:{glass:()=>[20,20]}, draw(c,o){
  sRect(c,3,3,54,54,{});
  c.rect(8,8,44,44,{fill:'sky', gap:7, cls:'soft'});
  if(o.broken){
    const hole=[]; for(let i=0;i<10;i++){ const r=i*36*Math.PI/180, d=i%2?3.4:7.5; hole.push([19+d*Math.cos(r), 19+d*Math.sin(r)]); }
    c.poly(hole,{fill:'paper', fs:'solid', rough:0.3});
    [[[26.5,19],[28,20.5],[30,21]],[[21.3,26.1],[22,28.5],[23,30]],[[12.9,23.4],[10,25.5],[8,27]],[[12.9,14.6],[10,12],[8,11]],[[21.3,11.9],[22.5,9.5],[23,8]]]
      .forEach(r=>c.poly(r,{open:true, rough:0.4}));
    c.arc(19,19,19,19,95,190,{cls:'thin', rough:0.4}); c.arc(19,19,19,19,280,350,{cls:'thin', rough:0.4});
    crack(c,30,38,[[[36,42],[44,41]],[[34,46],[38,52]]]);
  }
  c.line(30,8,30,52,{cls:'bold'}); c.line(8,30,52,30,{cls:'bold'});
  c.rect(8,8,44,44,{});
  sRect(c,0,57,60,5,{fill:'gray', gap:5, cls:'soft'});
  if(o.broken){ c.poly([[12,57],[15,53],[17,57]],{fill:'sky', fs:'solid', cls:'soft', rough:0.3}); c.poly([[40,57],[44,54.5],[45,57]],{fill:'sky', fs:'solid', cls:'soft', rough:0.3}); }
}};

/* ---------- Yard ---------- */

// fence: white picket fence. o.color (hatch the wood, e.g. 'brown'), o.broken (a missing and a leaning picket, snapped rail)
P.fence = {w:120, h:52, dh:10, draw(c,o){
  const f = o.color ? {fill:o.color, gap:6, cls:'soft'} : {};
  if(o.broken){ sRect(c,2,18,58,5,f); sRect(c,72,18,46,5,f); c.poly([[60,18],[62,20],[60,23]],{open:true, cls:'thin'}); c.poly([[72,18],[70,20.5],[72,23]],{open:true, cls:'thin'}); }
  else sRect(c,2,18,116,5,f);
  sRect(c,2,36,116,5,f);
  for(let i=0;i<8;i++){
    const x=3+i*15; let pts=[[x,12],[x+5,5],[x+10,12],[x+10,50],[x,50]];
    if(o.broken && i===4) continue;
    if(o.broken && i===5){ const a=0.42, cx=x, cy=50; pts=pts.map(([px,py])=>[cx+(px-cx)*Math.cos(a)+(py-cy)*Math.sin(a), cy-(px-cx)*Math.sin(a)+(py-cy)*Math.cos(a)]); }
    sPoly(c,pts,f);
  }
  if(o.broken){ c.poly([[62,50],[66,47],[68,50]],{cls:'thin'}); }
}};

// pool: in-ground pool with a ladder. o.float (default true: a ring float)
P.pool = {w:120, h:62, dh:14, draw(c,o){
  sRR(c,3,20,114,40,13,{});
  c.rrect(9,25,102,30,10,{fill:'sky', gap:5});
  [[18,34],[46,46],[60,32]].forEach(([x,y])=>c.curve([[x,y],[x+4,y-1.6],[x+8,y],[x+12,y-1.6],[x+16,y]],{color:'blue', cls:'thin'}));
  if(o.float!==false){ c.ellipse(34,40,20,10,{fill:'red', fs:'solid', rough:0.5}); c.ellipse(34,40,9,4.5,{fill:'sky', fs:'solid', rough:0.4}); [[26,38,28,42],[40,38,42,42]].forEach(l=>c.line(l[0],l[1],l[2],l[3],{color:'paper', cls:'bold', rough:0.3})); }
  const rail=(dx,dy)=>c.curve([[86+dx,22+dy],[86+dx,10+dy],[89+dx,6+dy],[93+dx,8+dy],[94+dx,20+dy],[95+dx,34+dy]],{cls:'bold'});
  rail(0,0); rail(9,4);
  c.line(94.3,27,103.3,31,{cls:'bold'}); c.line(94.8,33,103.8,37,{cls:'bold'});
}};

// trampoline: round backyard trampoline. o.net (safety net with poles)
P.trampoline = {w:100, h:64, dh:12, draw(c,o){
  const ey=x=>30+13*Math.sqrt(Math.max(0,1-((x-50)/48)**2));
  [[10,22],[42,58],[78,90]].forEach(([a,b])=>c.poly([[a,ey(a)-1],[a,58],[a+2.5,61],[b-2.5,61],[b,58],[b,ey(b)-1]],{open:true, cls:'bold', rough:0.6}));
  c.ellipse(50,30,96,26,back()); c.ellipse(50,30,96,26,{fill:'blue', gap:6});
  c.ellipse(50,30,76,16,back()); c.ellipse(50,30,76,16,{fill:'ink', fs:'solid', cls:'soft'});
  for(let a=0;a<360;a+=24){ const r=a*Math.PI/180, cs=Math.cos(r), sn=Math.sin(r); c.line(50+38*cs,30+8*sn,50+44*cs,30+11*sn,{cls:'thin', rough:0.3}); }
  if(o.net){
    c.poly([[4,8],[96,8],[96,30],[90,38],[70,42],[50,43],[30,42],[10,38],[4,30]],{nostroke:true, fill:'gray', fs:'cross-hatch', gap:6, cls:'soft'});
    [[4,30],[96,30],[28,42],[72,42]].forEach(([x,y])=>c.line(x,y,x,8,{cls:'bold', rough:0.5}));
    c.ellipse(50,8,92,10,{cls:'thin'});
  }
}};

// grill: kettle barbecue grill. o.color (default 'red'), o.smoke (default true), o.fire (flames out of the lid)
P.grill = {w:60, h:80, dh:14, draw(c,o){
  const col=o.color||'red';
  c.line(22,58,11,76,{cls:'bold'}); c.line(38,58,49,76,{cls:'bold'}); c.line(30,60,30,72,{});
  c.line(16,68,44,68,{cls:'thin'});
  c.circle(11,76,7,{fill:'paper', fs:'solid'}); c.circle(49,76,7,{fill:'paper', fs:'solid'});
  c.arc(30,38,48,48,0,180,{closed:true, fill:col, gap:7});
  c.arc(30,37,48,46,180,360,{closed:true, fill:col, gap:7});
  c.line(5,38,55,38,{cls:'bold'});
  c.rrect(54,40,8,3.5,1.5,{fill:'ink', fs:'solid'});
  c.line(26,14,26,10,{}); c.line(34,14,34,10,{}); c.rrect(22,7,16,4,2,{fill:'ink', fs:'solid'});
  if(o.fire){ c.sub(8,33,10,'fire'); c.sub(52,33,10,'fire'); c.sub(30,4,26,'fire'); }
  if(o.smoke!==false && !o.fire){ c.curve([[16,16],[13,11],[17,7],[14,1]],{color:'gray'}); c.curve([[44,16],[47,11],[43,7],[46,1]],{color:'gray'}); }
}};

// mailbox: rural mailbox on a post. o.color (box hatch, default 'blue'), o.flag (default true: red flag up), o.letters (letters sticking out)
P.mailbox = {w:52, h:80, dh:14, draw(c,o){
  c.rect(21,36,9,42,{fill:'brown', gap:5});
  tuft(c,15,78,1.1); tuft(c,36,78,1);
  if(o.flag!==false){ c.line(41,30,41,4,{cls:'bold'}); c.poly([[41,4],[51,4],[51,11],[41,11]],{fill:'red', fs:'solid', rough:0.5}); }
  const pts=[[4,38],[4,24]]; for(let i=1;i<=5;i++){ const a=(180+i*15)*Math.PI/180; pts.push([14+10*Math.cos(a), 24+10*Math.sin(a)]); }
  for(let i=0;i<=5;i++){ const a=(270+i*15)*Math.PI/180; pts.push([38+10*Math.cos(a), 24+10*Math.sin(a)]); }
  pts.push([48,38]);
  if(o.flag!==false){ sPoly(c,pts,{fill:o.color||'blue', gap:7}); c.line(41,30,41,38,{cls:'bold'}); }
  else sPoly(c,pts,{fill:o.color||'blue', gap:7});
  c.line(10,16,10,38,{cls:'thin'}); c.dot(7,27,2.6);
  if(o.letters){ sRect(c,-4,22,10,7,{}); c.poly([[-4,22],[1,26],[6,22]],{open:true, cls:'thin'}); sRect(c,-2,29,9,6,{}); }
}};

/* ---------- Kitchen and valuables ---------- */

// fridge: two-door refrigerator. o.spoiled (stink lines: food spoiled in a power outage), o.color (body hatch)
P.fridge = {w:52, h:92, dh:24, draw(c,o){
  if(o.spoiled){ [[16,-12],[26,-14],[36,-12]].forEach(([x,y])=>c.curve([[x,y+14],[x-3,y+10],[x+2,y+6],[x-2,y+1]],{color:'green'})); }
  sRR(c,4,3,44,86,5, o.color ? {fill:o.color, gap:12, cls:'soft'} : {});
  c.line(4,30,48,30);
  c.line(41,12,41,24,{cls:'bold'}); c.line(41,38,41,58,{cls:'bold'});
  c.rect(12,40,13,14,{fill:'yellow', fs:'solid', rough:0.5}); c.line(14.5,45,22,45,{cls:'thin', rough:0.3}); c.line(14.5,49,20,49,{cls:'thin', rough:0.3}); c.dot(18.5,40,3,{color:'red'});
  c.dot(15,14,3.4,{color:'green'}); c.dot(22,18,3.4,{color:'blue'});
  c.rect(9,89,6,3,{fill:'ink', fs:'solid', rough:0.3}); c.rect(37,89,6,3,{fill:'ink', fs:'solid', rough:0.3});
}};

// painting: framed landscape painting on an easel. o.wall (hanging on a nail, no easel)
P.painting = {w:72, h:90, dh:18, draw(c,o){
  const dy = o.wall ? 12 : 0;
  if(o.wall){ c.dot(36,dy-2,3); c.poly([[14,dy+12],[36,dy-2],[58,dy+12]],{open:true, cls:'thin'}); }
  else { const E={color:'brown', cls:'bold'}; c.line(37,3,42,88,{color:'brown'}); c.line(35,1,13,88,E); c.line(37,1,59,88,E); }
  sRect(c,9,dy+11,54,45,{fill:'orange', gap:5});
  sRect(c,16,dy+18,40,31,{});
  c.circle(47,dy+26,8,{color:'orange', fill:'yellow', fs:'solid', rough:0.4});
  c.poly([[16,dy+49],[27,dy+31],[35,dy+41],[43,dy+33],[56,dy+49]],{fill:'green', gap:5, rough:0.6});
  if(!o.wall) c.rect(10,57,52,4,{fill:'brown', fs:'solid', rough:0.5});
}};

// silverware: fork, knife and spoon. o.gold (gold instead of silver)
P.silverware = {w:56, h:62, dh:8, draw(c,o){
  const m = o.gold ? {fill:'yellow', fs:'solid', cls:'soft2'} : {fill:'gray', fs:'solid', cls:'soft'};
  // fork
  [7,10.5,14,17.5].forEach(x=>c.line(x,3,x,15,{rough:0.4}));
  c.curve([[7,14],[8,19],[12.2,21.5],[16.5,19],[17.5,14]],{rough:0.4});
  sRR(c,9.7,21,5,38,2.5,m);
  // knife
  sPoly(c,[[25,32],[25,6],[27.5,2.5],[31,5],[33,14],[33,32]],m);
  sRR(c,24,31,10,28,3.5,{fill:'ink', fs:'solid', cls:'soft'});
  // spoon
  c.ellipse(46,13,14,21,Object.assign({rough:0.5}, m));
  sRR(c,43.8,22,4.6,37,2.3,m);
  sparkle(c,52,4,3,o.gold?'orange':'sky');
}};

// lawnmower: push mower, faces right. o.color (deck, default 'red'), o.grass (default true: grass tufts)
P.lawnmower = {w:100, h:70, dh:12, draw(c,o){
  const col=o.color||'red';
  c.line(36,40,10,6,{cls:'bold'}); c.line(6.5,8.5,13.5,3.5,{cls:'bold'});
  c.curve([[14,10],[19,13],[21,18]],{cls:'thin'});
  c.line(50,30,22,22,{cls:'thin', color:'gray'});
  sRR(c,44,25,28,17,4,{fill:'gray', gap:6, cls:'soft'}); c.rect(53,20,9,5,{fill:'ink', fs:'solid', rough:0.4});
  sPoly(c,[[28,40],[84,40],[92,49],[92,54],[26,54],[26,46]],{fill:col, gap:7});
  [34,82].forEach(x=>{ c.circle(x,56,17,{fill:'paper', fs:'solid'}); c.circle(x,56,6,{fill:'ink', fs:'solid', cls:'soft'}); });
  if(o.grass!==false){ tuft(c,8,66,1.3); tuft(c,58,67,1.1); tuft(c,97,66,1.2); [[96,50],[99,45],[94,44]].forEach(p=>c.line(p[0],p[1],p[0]+1.5,p[1]-2,{color:'green', cls:'thin', rough:0.3})); }
}};

// snowblower: walk-behind snow blower, faces right, throwing snow. o.color (default 'orange')
P.snowblower = {w:104, h:74, dh:13, draw(c,o){
  const col=o.color||'orange';
  c.line(40,36,12,6,{cls:'bold'}); c.line(8.5,9,15.5,3,{cls:'bold'});
  c.curve([[16,9],[21,13],[23,18]],{cls:'thin'});
  sPoly(c,[[66,32],[73,32],[75,16],[86,10],[87,3],[72,6],[66,16]],{fill:col, gap:5});
  sRR(c,34,28,28,20,4,{fill:'gray', gap:6, cls:'soft'}); c.rect(42,23,9,5,{fill:'ink', fs:'solid', rough:0.4});
  sRR(c,58,30,40,32,8,{fill:col, gap:7});
  c.arc(98,46,14,26,90,270,{closed:true, fill:'ink', fs:'solid', cls:'soft'}); c.line(58,62,100,62,{cls:'bold'}); c.dot(72,40,3);
  c.circle(44,58,24,{fill:'paper', fs:'solid'}); c.circle(44,58,9,{fill:'ink', fs:'solid', cls:'soft'});
  [[0,2],[45,2.6],[90,2],[135,2.6],[180,2],[225,2.6],[270,2],[315,2.6]].forEach(([a,d])=>{ const r=a*Math.PI/180; c.line(44+10.5*Math.cos(r),58+10.5*Math.sin(r),44+12.5*Math.cos(r),58+12.5*Math.sin(r),{cls:'thin', rough:0.3}); });
  c.poly([[56,72],[66,66],[84,65],[98,64],[106,68],[106,72]],{nostroke:true, fill:'sky', gap:5, cls:'soft'}); c.curve([[56,72],[66,66],[84,65],[98,64],[106,68]],{color:'sky'});
  [[93,4,4],[99,10,3],[96,-2,3],[102,2,2.6],[90,11,2.6],[104,-6,2.4]].forEach(([x,y,d])=>c.circle(x,y,d,{color:'sky', fill:'sky', fs:'solid', cls:'soft', rough:0.3}));
}};

// ladder: straight ladder. o.step (A-frame step ladder), o.color (rails, default 'orange')
P.ladder = {w:44, h:104, dh:26, draw(c,o){
  const f={fill:o.color||'orange', fs:'solid', cls:'soft'};
  if(o.step){
    const xf=y=>7+14*(102-y)/97;
    sPoly(c,[[37,102],[42,102],[29,5],[24,5]],{fill:'gray', fs:'solid', cls:'soft'});
    c.line(xf(56),56,37-13*(46)/97,56,{cls:'thin'});
    sPoly(c,[[2,102],[7,102],[21,5],[16,5]],f);
    [84,64,44,24].forEach(y=>sRect(c,xf(y)-2,y,12,3.6,f));
    sRR(c,12,0,20,6,2,{fill:'ink', fs:'solid', cls:'soft'});
    return;
  }
  sPoly(c,[[4,102],[9,102],[15,2],[11,2]],f); sPoly(c,[[35,102],[40,102],[33,2],[29,2]],f);
  for(let y=12;y<=96;y+=12){ const l=9+6*(102-y)/100-1, r=35-4*(102-y)/100+1; c.rect(l,y-1.4,r-l,2.8,f); }
}};

// toolbox: red metal toolbox with handle. o.color (default 'red'), o.open (no lid, tools sticking out)
P.toolbox = {w:70, h:52, dh:7, draw(c,o){
  const col=o.color||'red';
  if(o.open){
    sPoly(c,[[8,8],[12.5,8],[20,25],[15.5,25]],{fill:'gray', fs:'solid', cls:'soft'});
    c.circle(10,4,11,back()); c.circle(10,4,11,{fill:'gray', fs:'solid', cls:'soft'}); c.circle(10,4,4.5,{fill:'paper', fs:'solid'});   // wrench
    c.line(50,24,51.5,12,{cls:'bold'}); sRR(c,48,0,7,13,2.5,{fill:'yellow', fs:'solid'});                                 // screwdriver
    c.sub(31,9,24,'hammer');
    sRect(c,4,22,62,26,{fill:col, gap:8}); c.rect(29,30,12,6,{fill:'ink', fs:'solid', cls:'soft'});
    return;
  }
  c.poly([[24,14],[26,5],[44,5],[46,14]],{open:true, cls:'bold'});
  sPoly(c,[[4,22],[9,13],[61,13],[66,22]],{fill:col, gap:6});
  sRect(c,4,22,62,26,{fill:col, gap:8});
  c.rect(14,19,7,7,{fill:'gray', fs:'solid', rough:0.4}); c.rect(49,19,7,7,{fill:'gray', fs:'solid', rough:0.4});
}};

// hammer: claw hammer, upright
P.hammer = {w:56, h:64, dh:8, draw(c,o){
  sRR(c,24,14,8,48,3.5,{fill:'brown', gap:4});
  c.rrect(23.5,46,9,16,3.5,{fill:'ink', fs:'solid', cls:'soft'});
  sPoly(c,[[18,6],[9,6],[3,10],[1,17],[8,13],[18,15]],{fill:'gray', fs:'solid', cls:'soft'});
  sRect(c,17,3,16,14,{fill:'gray', fs:'solid', cls:'soft'});
  sRect(c,33,5,11,10,{fill:'gray', fs:'solid', cls:'soft'});
  sRR(c,44,3,5,14,1.5,{fill:'gray', fs:'solid', cls:'soft'});
}};

// key: house key (brass)
P.key = {w:64, h:30, dh:4, draw(c,o){
  const t=c.k<1.6, f={fill:o.color||'yellow', fs:'solid', single:t, cls:t?'thin':'', rough:0.6};
  c.poly([[24,10.5],[58,10.5],[62,15],[58,19.5],[54,19.5],[54,27],[49,27],[49,22.5],[45,22.5],[45,26],[40,26],[40,19.5],[24,19.5]],f);
  c.circle(14,15,27,f); c.circle(8.5,15,7,{fill:'paper', fs:'solid', single:t, cls:'thin', rough:0.4});
  if(!t) c.line(28,15,52,15,{cls:'thin', rough:0.3});
}};

// lock: padlock. o.broken (shackle cut and sprung open, cracked body), o.open (unlocked, shackle lifted)
P.lock = {w:44, h:58, dh:7, draw(c,o){
  const B={cls:'bold', rough:0.6};
  if(o.open){ c.arc(17,18,28,30,180,360,B); c.arc(17,18,16,20,180,360,B); c.line(3,18,3,30,B); c.line(9,18,9,30,B); c.line(25,18,25,24,B); c.line(31,18,31,24,B); }
  else if(o.broken){
    c.arc(22,24,28,32,180,282,B); c.arc(22,24,16,20,180,290,B); c.line(8,24,8,30,B); c.line(14,24,14,30,B);
    c.arc(26,17,28,32,300,360,B); c.arc(26,17,16,20,300,360,B); c.line(40,17,40,23,B); c.line(34,17,34,23,B);
    sparkle(c,30,6,3.5,'orange');
  }
  else { c.arc(22,24,28,32,180,360,B); c.arc(22,24,16,20,180,360,B); c.line(8,24,8,30,B); c.line(36,24,36,30,B); c.line(14,24,14,30,B); c.line(30,24,30,30,B); }
  sRR(c,3,28,38,28,4,{fill:'yellow', gap:5});
  c.dot(22,38.5,6.5); c.poly([[20.5,40],[23.5,40],[25,48],[19,48]],{fill:'ink', fs:'solid', rough:0.3});
  if(o.broken) c.poly([[34,28],[31,34],[36,38],[32,44],[35,49]],{open:true, cls:'bold', rough:0.5});
}};

// safe: steel safe with a dial. o.open (door swung open: cash and gold inside), o.empty (with o.open: nothing inside)
P.safe = {w:60, h:66, dh:12, draw(c,o){
  c.rect(8,58,9,6,{fill:'ink', fs:'solid', rough:0.4}); c.rect(43,58,9,6,{fill:'ink', fs:'solid', rough:0.4});
  sRR(c,3,3,54,56,3,{fill:'gray', gap:7, cls:'soft'});
  if(o.open){
    sRect(c,9,9,42,44,{fill:'ink', fs:'solid', cls:'soft'});
    c.line(9,31,51,31,{});
    if(!o.empty){ c.sub(30,23,12,'money'); [[14,45],[26,45],[20,39]].forEach(([x,y])=>c.poly([[x,y+7],[x+12,y+7],[x+10,y],[x+2,y]],{color:'orange', fill:'yellow', fs:'solid', rough:0.4})); }
    sPoly(c,[[9,9],[-12,4],[-12,58],[9,53]],{fill:'gray', gap:7, cls:'soft'});
    c.ellipse(-2,31,7,14,{fill:'paper', fs:'solid'});
    return;
  }
  sRect(c,9,9,42,44,{});
  c.circle(25,31,20,{fill:'paper', fs:'solid'});
  for(let i=0;i<8;i++){ const a=i*45*Math.PI/180; c.line(25+7*Math.cos(a),31+7*Math.sin(a),25+9.3*Math.cos(a),31+9.3*Math.sin(a),{cls:'thin', rough:0.3}); }
  c.circle(25,31,7,{fill:'ink', fs:'solid', cls:'soft'}); c.dot(25,31,2.4);
  c.rrect(41,22,4.5,18,2,{fill:'ink', fs:'solid'});
  c.rect(6,15,4,7,{fill:'ink', fs:'solid', rough:0.3}); c.rect(6,40,4,7,{fill:'ink', fs:'solid', rough:0.3});
}};

// briefcase: leather briefcase. o.color (default 'brown')
P.briefcase = {w:60, h:48, dh:7, draw(c,o){
  if(c.k<TINY){ c.poly([[22,14],[22,6],[38,6],[38,14]],{open:true, cls:'bold', rough:0.4, single:true}); c.rrect(3,13,54,32,4,{fill:o.color||'brown', fs:'solid', cls:'thin', single:true}); c.rect(26,20,8,7,{fill:'yellow', fs:'solid', nostroke:true}); return; }
  c.poly([[22,14],[22,6],[38,6],[38,14]],{open:true, cls:'bold', rough:0.5});
  sRR(c,3,13,54,32,4,{fill:o.color||'brown', gap:7});
  c.line(3,24,57,24,{});
  c.rect(12,21,7,6,{fill:'yellow', fs:'solid', rough:0.4}); c.rect(41,21,7,6,{fill:'yellow', fs:'solid', rough:0.4});
}};

// coffee: coffee mug. o.color (mug hatch, default 'red'), o.steam (default true)
P.coffee = {w:52, h:52, dh:5, draw(c,o){
  if(c.k<TINY){ if(o.steam!==false) c.curve([[22,11],[18,7],[24,4],[20,-2]],{color:'gray', cls:'thin', single:true}); c.arc(36,30,22,20,-75,75,{cls:'bold', single:true});
    c.poly([[8,14],[38,14],[37,42],[33,47],[13,47],[9,42]],{fill:o.color||'red', fs:'solid', cls:'thin', single:true}); c.ellipse(23,15,26,5,{fill:'brown', fs:'solid', nostroke:true}); return; }
  if(o.steam!==false){ c.curve([[18,12],[15,8],[19,5],[16,0]],{color:'gray'}); c.curve([[28,12],[25,8],[29,5],[26,0]],{color:'gray'}); }
  c.arc(36,30,22,20,-75,75,{cls:'bold'});
  sPoly(c,[[8,14],[38,14],[37,42],[33,47],[13,47],[9,42]],{fill:o.color||'red', gap:7});
  c.ellipse(23,14,30,6,{fill:'brown', fs:'solid'});
}};

// gift: wrapped present with bow. o.color (paper, default 'red'), o.ribbon (default 'yellow')
P.gift = {w:52, h:56, dh:7, draw(c,o){
  const col=o.color||'red', rb={fill:o.ribbon||'yellow', fs:'solid'};
  if(c.k<TINY){ const r2={fill:o.ribbon||'yellow', fs:'solid', cls:'thin', single:true}; c.rect(6,19,40,34,{fill:col, fs:'solid', cls:'thin', single:true}); c.rect(22,19,8,34,{fill:o.ribbon||'yellow', fs:'solid', nostroke:true});
    c.blob([[26,18],[16,6],[9,9],[12,17]],r2); c.blob([[26,18],[36,6],[43,9],[40,17]],r2); return; }
  sRect(c,7,26,38,27,{fill:col, gap:7});
  sRect(c,4,18,44,9,{fill:col, gap:6});
  c.rect(22,18,8,35,rb);
  c.blob([[26,17],[17,6],[10,8],[12,15]],rb); c.blob([[26,17],[35,6],[42,8],[40,15]],rb);
  c.circle(26,17,7,rb);
}};

// jewelry: open jewelry box with a pearl necklace spilling out. o.necklace (just the necklace with a pendant)
P.jewelry = {w:64, h:56, dh:8, draw(c,o){
  const pearls=(x0,x1,y0,dip,n)=>{ const pts=[]; for(let i=0;i<=n;i++){ const t=i/n; pts.push([x0+(x1-x0)*t, y0+dip*Math.sin(Math.PI*t)]); }
    c.curve(pts,{cls:'thin', color:'gray', rough:0.3}); pts.forEach(p=>c.circle(p[0],p[1],4.2,{fill:'paper', fs:'solid', rough:0.3, cls:'thin'})); };
  if(o.necklace){
    pearls(10,54,6,34,14);
    c.poly([[32,40],[37,45],[32,53],[27,45]],{fill:'red', fs:'solid', rough:0.3}); c.line(32,40,32,38,{cls:'thin'});
    sparkle(c,44,48,3.5);
    return;
  }
  sPoly(c,[[8,28],[3,6],[61,6],[56,28]],{fill:'purple', gap:7});
  sPoly(c,[[12,26],[8.5,10],[55.5,10],[52,26]],{fill:'pink', fs:'solid', cls:'soft'});
  sRect(c,5,28,54,24,{fill:'purple', gap:8});
  c.rect(28,28,8,5,{fill:'yellow', fs:'solid', rough:0.4});
  pearls(14,50,29,15,10);
  c.poly([[32,43],[36,47],[32,52],[28,47]],{fill:'red', fs:'solid', rough:0.3});
  sparkle(c,57,4,4);
}};
})();
