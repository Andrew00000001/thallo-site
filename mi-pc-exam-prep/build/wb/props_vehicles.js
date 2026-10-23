/* ---------- Sketch props: vehicles, watercraft, equipment and road things ----------
   Same conventions as props_core.js: {w, h, dh, anchors?, draw(c, opt, el)}; draw in the prop's own w x h box.
   Vehicles face right (use the element's flip to face left). Scale matches props_core car (about 0.25 canvas units per box unit). */
(()=>{
const P = SK.PROPS;
const rad = d => d*Math.PI/180;
const TH = {cls:'thin'}, LT = {cls:'thin', rough:0.5};
const wheel = (c, x, y, d) => { c.circle(x,y,d,{fill:'paper', fs:'solid'}); c.circle(x,y,d*0.36,LT); };
const glass = (c, pts) => c.poly(pts,{fill:'sky', gap:6, cls:'soft'});
const lamp = (c, x, y, w, h, col) => c.rect(x,y,w,h,{color:col, fill:col, fs:'solid', rough:0.4});
const fit = (s, maxW, maxSize) => Math.min(maxSize, maxW/Math.max(1e-6, SK.tw(s,1)));
const rotp = (pts, cx, cy, deg) => { const a=rad(deg), cs=Math.cos(a), sn=Math.sin(a); return pts.map(([x,y])=>[cx+(x-cx)*cs-(y-cy)*sn, cy+(x-cx)*sn+(y-cy)*cs]); };
// little flashing rays around a point, fanned between two angles (deg, 0 = right, clockwise)
const rays = (c, x, y, r0, r1, a0, a1, n, col) => { for(let i=0;i<n;i++){ const a=rad(a0+(a1-a0)*(n>1?i/(n-1):0.5)); c.line(x+r0*Math.cos(a), y+r0*Math.sin(a), x+r1*Math.cos(a), y+r1*Math.sin(a),{color:col, rough:0.5}); } };
// wavy water band: waterline at y, from x0 to x1, hatch down to y+depth
const waterBand = (c, x0, x1, y, depth) => {
  c.poly([[x0,y+1],[x1,y+1],[x1,y+depth],[x0,y+depth]],{nostroke:true, fill:'blue', color:'blue', gap:9, cls:'soft'});
  for(let r=0;r<2;r++){ const yy=y+r*depth*0.55, pts=[]; for(let x=x0;x<=x1+0.1;x+=10) pts.push([x, yy+(((x-x0)/10)%2?2.5:-1)]); c.curve(pts,{color:'blue'}); }
};

/* ===== Two-wheelers and small rides ===== */
// motorcycle: street motorcycle, side view facing right. o.color: tank and tail (default red)
P.motorcycle = {w:100, h:64, dh:12, anchors:{front:()=>[96,40], seat:()=>[30,20]},
  draw(c, o){
    const col=o.color||'red';
    c.line(36,26,21,45,{cls:'bold'});
    c.rrect(38,29,22,17,3,{fill:'gray', gap:5});
    c.line(40,44,20,46,{cls:'bold'});
    c.line(66,12,80,46,{cls:'bold'});
    c.poly([[54,47],[36,47],[22,42]],{open:true, color:'gray', cls:'bold'});
    wheel(c,20,46,30); c.dot(20,46,3.5);
    wheel(c,80,46,30); c.dot(80,46,3.5);
    c.arc(20,46,37,37,195,320,{color:col, cls:'bold'});
    c.arc(80,46,37,37,215,340,{color:col, cls:'bold'});
    c.poly([[10,23],[17,17],[42,19],[42,26],[13,27]],{fill:'ink', gap:4});
    c.poly([[41,27],[45,17],[59,13],[67,19],[62,29],[43,30]],{fill:col, gap:6});
    lamp(c,6,22,4,4,'red');
    c.circle(73,22,9,{fill:'yellow', fs:'solid'});
    c.line(57,9,68,12,{cls:'bold'});
  }};

// atv: four-wheeler (quad bike), side view facing right. o.color: fenders and body (default red)
P.atv = {w:104, h:70, dh:13, anchors:{front:()=>[102,36], seat:()=>[40,20]},
  draw(c, o){
    const col=o.color||'red';
    [[22,52],[82,52]].forEach(([x,y])=>{ c.circle(x,y,32,{fill:'paper', fs:'solid'}); c.circle(x,y,32,{nostroke:true, fill:'ink', gap:4, cls:'soft'}); c.circle(x,y,14,{fill:'paper', fs:'solid'}); c.dot(x,y,3.5); });
    c.rrect(42,38,20,12,3,{fill:'gray', gap:4});
    c.poly([[34,30],[70,30],[64,42],[40,42]],{fill:col, gap:7});
    c.poly([[2,40],[6,29],[40,27],[44,40]],{fill:col, gap:7});
    c.poly([[60,38],[66,27],[96,27],[102,39]],{fill:col, gap:7});
    c.poly([[20,27],[25,20],[54,20],[57,27]],{fill:'ink', gap:4});
    c.line(68,28,62,12,{cls:'bold'}); c.line(56,12,70,10,{cls:'bold'});
    c.line(4,23,26,23,TH); c.line(8,23,8,28,TH); c.line(22,23,22,27,TH);
    c.line(72,21,96,21,TH); c.line(76,21,76,27,TH); c.line(92,21,92,27,TH);
    c.ellipse(100,33,5,6,{fill:'yellow', fs:'solid', rough:0.4});
  }};

// golfcart: golf cart with canopy and a golf bag on the back, facing right. o.color: roof and seat (default green), o.body: body color (default white)
P.golfcart = {w:96, h:84, dh:15, anchors:{roof:()=>[48,4], front:()=>[94,60]},
  draw(c, o){
    const col=o.color||'green';
    [[2,12,6,24],[10,8,10,24],[17,11,14,24]].forEach(([x1,y1,x2,y2])=>{ c.line(x1,y1,x2,y2,LT); c.ellipse(x1,y1,6,3.5,{fill:'gray', fs:'solid', rough:0.4}); });
    c.poly([[4,24],[16,24],[18,56],[8,56]],{fill:'brown', gap:5});
    c.line(20,12,22,52,{cls:'bold'});
    glass(c,[[76,12],[82,12],[87,44],[81,44]]);
    c.line(76,12,81,44,{cls:'bold'});
    c.rrect(10,5,78,8,3,{fill:col, gap:5});
    c.rrect(24,30,9,24,3,{fill:col, gap:5});
    c.rrect(24,46,32,8,3,{fill:col, gap:5});
    c.poly([[8,54],[58,54],[64,44],[86,44],[94,56],[94,68],[8,68]],{fill:o.body||'paper', fs:o.body?'hachure':'solid', gap:9});
    c.line(68,44,62,33); c.line(57,32,67,34,{cls:'bold'});
    wheel(c,26,70,18); wheel(c,78,70,18);
  }};

// snowmobile: snowmobile with front ski and rear track, facing right. o.color: body (default red), o.snow:false hides the snow spray and ground
P.snowmobile = {w:120, h:62, dh:13, anchors:{front:()=>[116,50], seat:()=>[30,24]},
  draw(c, o){
    const col=o.color||'red';
    if(o.snow!==false){
      c.curve([[0,60],[30,58],[60,60],[90,58],[120,60]],{color:'gray', cls:'thin'});
      [[4,40,4],[2,48,3],[8,34,3],[6,54,3.5],[0,30,2.5]].forEach(([x,y,d])=>c.circle(x,y,d,{color:'sky', rough:0.4, cls:'thin'}));
    }
    c.rrect(10,40,62,15,7,{fill:'ink', gap:4, cls:'soft'});
    [20,36,52,64].forEach(x=>c.circle(x,47.5,7,{fill:'paper', fs:'solid', rough:0.4}));
    c.line(88,42,92,55,{cls:'bold'});
    c.curve([[68,56],[100,56],[112,54],[117,47]],{cls:'bold'});
    c.poly([[8,43],[10,32],[46,30],[60,22],[84,24],[108,37],[112,44],[8,45]],{fill:col, gap:7});
    c.poly([[12,32],[16,25],[46,24],[48,30]],{fill:'ink', gap:4});
    glass(c,[[62,22],[65,8],[73,8],[76,23]]);
    c.line(52,14,62,15,{cls:'bold'}); c.line(57,15,58,23);
    c.ellipse(101,35,8,5,{fill:'yellow', fs:'solid', rough:0.4});
  }};

/* ===== Cars, vans, trucks ===== */
const CARP=[[6,40],[8,26],[30,22],[44,8],[84,8],[100,24],[116,28],[118,42],[108,44]];
const sh = (pts, dx, dy) => pts.map(([x,y])=>[x+dx,y+dy]);
// crumple mark on a front corner (same look as the core car's o.dent)
const dent = (c, x, y) => c.poly([[x,y],[x+4,y+6],[x-1,y+10],[x+5,y+15]],{open:true, cls:'bold'});

// police: police car with red and blue light bar and POLICE on the door, facing right. o.color: body (default blue), o.lights:false = no flashing rays, o.text (default 'POLICE'), o.dent
P.police = {w:120, h:64, dh:15, anchors:{front:()=>[118,42], roof:()=>[64,6]},
  draw(c, o){
    const col=o.color||'blue', d=8;
    if(o.lights!==false){ rays(c,54,8,6,11,195,265,3,'red'); rays(c,76,8,6,11,275,345,3,'blue'); }
    c.rect(52,9,4,6,{rough:0.4}); c.rect(72,9,4,6,{rough:0.4});
    lamp(c,50,5,13,5,'red'); lamp(c,63,5,13,5,'blue');
    c.poly(sh(CARP,0,d),{fill:col, gap:10});
    glass(c,sh([[48,12],[60,12],[60,24],[38,24]],0,d)); glass(c,sh([[64,12],[82,12],[94,24],[64,24]],0,d));
    const t=o.text||'POLICE', s=fit(t,44,9);
    c.rect(38,29+d,52,11,{fill:'paper', fs:'solid', rough:0.5});
    c.text(64,34.5+d+s*0.34,t,{size:s, bold:true});
    wheel(c,32,44+d,20); wheel(c,92,44+d,20);
    c.rect(110,30+d,6,5,{fill:'yellow', fs:'solid', rough:0.4});
    if(o.dent) dent(c,104,26+d);
  }};

// rental: car with a big hanging "RENTAL" tag tied to its roof, facing right. o.color: car (default blue), o.text (default 'RENTAL'), o.tag: tag color (default yellow), o.dent
P.rental = {w:120, h:84, dh:21, anchors:{tag:()=>[72,14], front:()=>[118,62], roof:()=>[64,36]},
  draw(c, o){
    c.sub(60,56,56,'car',{color:o.color||'blue', dent:o.dent});
    c.curve([[44,15],[38,24],[46,32],[56,36]],{cls:'thin'});
    c.poly([[40,15],[48,5],[104,5],[104,25],[48,25]],{fill:'paper', fs:'solid'});
    c.poly([[40,15],[48,5],[104,5],[104,25],[48,25]],{nostroke:true, fill:o.tag||'yellow', gap:6, cls:'soft'});
    c.circle(47,15,4,{rough:0.4, cls:'thin'});
    const t=o.text||'RENTAL', s=fit(t,48,13);
    c.text(77,15+s*0.34,t,{size:s, bold:true});
  }};

// van: minivan / passenger van facing right. o.color: body (default gray), o.cargo: windowless cargo van, o.name: business name on the side (implies cargo), o.dent
P.van = {w:120, h:64, dh:15, anchors:{front:()=>[118,40], roof:()=>[50,6]},
  draw(c, o){
    const col=o.color||'gray', cargo=!!(o.cargo||o.name);
    c.poly([[6,52],[5,14],[10,8],[86,8],[102,25],[115,29],[117,50]],{fill:col, gap:10});
    glass(c,[[72,12],[85,12],[96,25],[72,25]]);
    if(!cargo){ c.rect(46,12,22,13,{fill:'sky', gap:6, cls:'soft'}); c.rect(20,12,22,13,{fill:'sky', gap:6, cls:'soft'}); c.rect(8,12,8,13,{fill:'sky', gap:6, cls:'soft'}); }
    c.line(70,9,70,50,TH); c.line(44,9,44,50,TH);
    if(o.name){ const s=fit(o.name,50,10); c.rect(10,24,58,15,{fill:'paper', fs:'solid', rough:0.5}); c.text(39,31.5+s*0.34,o.name,{size:s, bold:true}); }
    wheel(c,28,50,20); wheel(c,96,50,20);
    c.rect(109,33,6,5,{fill:'yellow', fs:'solid', rough:0.4});
    if(o.dent) dent(c,103,27);
  }};

// pickup: pickup truck with an open bed at the back, facing right. o.color: body (default green), o.load: boxes in the bed, o.dent
P.pickup = {w:130, h:60, dh:15, anchors:{front:()=>[126,40], bed:()=>[30,22], roof:()=>[70,10]},
  draw(c, o){
    const col=o.color||'green';
    if(o.load){ c.rect(10,12,18,16,{fill:'brown', gap:6}); c.line(19,12,19,28,LT); c.rect(30,18,20,10,{fill:'brown', gap:6}); }
    c.poly([[4,48],[4,26],[56,26],[56,48]],{fill:col, gap:10});
    c.line(6,30,54,30,TH);
    c.poly([[56,48],[56,10],[84,10],[98,26],[124,29],[126,48]],{fill:col, gap:10});
    glass(c,[[62,14],[82,14],[93,26],[62,26]]);
    c.line(86,28,86,46,TH);
    wheel(c,28,48,22); wheel(c,104,48,22);
    c.rect(118,32,6,5,{fill:'yellow', fs:'solid', rough:0.4}); lamp(c,4,30,3,6,'red');
    if(o.dent) dent(c,111,28);
  }};

// bus: yellow school bus, side view facing right. o.color: body (default yellow), o.text (default 'SCHOOL BUS'), o.stop: stop arm swung out
P.bus = {w:200, h:80, dh:20, anchors:{front:()=>[196,54], roof:()=>[80,6], door:()=>[153,40]},
  draw(c, o){
    const col=o.color||'yellow';
    c.rrect(4,6,160,58,6,{fill:col, gap:9});
    c.poly([[163,34],[186,36],[194,44],[196,64],[163,64]],{fill:col, gap:9});
    for(let i=0;i<7;i++) c.rect(10+i*19.4,24,16,15,{fill:'sky', gap:6, cls:'soft'});
    c.rect(146,20,15,42,{}); glass(c,[[148,22],[159,22],[159,39],[148,39]]); c.line(153.5,41,153.5,60,TH);
    c.line(4,46,146,46); c.line(4,54,146,54);
    const t=o.text||'SCHOOL BUS', s=fit(t,124,13);
    c.text(76,12+s*0.66,t,{size:s, bold:true});
    if(o.stop){ const oc=[]; for(let k=0;k<8;k++){ const a=rad(22.5+45*k); oc.push([132+7*Math.cos(a), 48+7*Math.sin(a)]); } c.poly(oc,{color:'red', fill:'red', fs:'solid', rough:0.4}); }
    wheel(c,36,64,24); wheel(c,174,64,24);
    c.rect(189,46,6,5,{fill:'yellow', fs:'solid', rough:0.4});
    c.line(162,64,198,64,{cls:'bold'});
  }};

// ambulance: box ambulance with red cross, stripe and roof lights, facing right. o.lights:false = no flashing rays
P.ambulance = {w:150, h:76, dh:18, anchors:{front:()=>[146,54], roof:()=>[56,6]},
  draw(c, o){
    if(o.lights!==false){ rays(c,13,6,6,11,200,280,3,'red'); rays(c,99,6,6,11,260,340,3,'red'); }
    lamp(c,8,5,10,5,'red'); lamp(c,94,5,10,5,'red');
    c.rect(4,10,104,52,{fill:'paper', fs:'solid'});
    c.poly([[108,24],[126,24],[140,42],[146,44],[146,62],[108,62]],{fill:'paper', fs:'solid'});
    glass(c,[[112,28],[124,28],[134,42],[112,42]]);
    lamp(c,4,48,142,5,'red');
    c.poly([[50,16],[62,16],[62,24],[70,24],[70,36],[62,36],[62,44],[50,44],[50,36],[42,36],[42,24],[50,24]],{color:'red', fill:'red', fs:'solid', rough:0.5});
    c.line(14,14,14,58,TH);
    wheel(c,30,62,22); wheel(c,124,62,22);
    c.rect(140,47,5,5,{fill:'yellow', fs:'solid', rough:0.4});
  }};

// towtruck: tow truck facing right. Default wrecker with boom and hook; o.flatbed: flatbed carrier, o.car: a car on the flatbed (true or a color), o.color: body (default orange)
P.towtruck = {w:150, h:76, dh:18, anchors:{front:()=>[146,54], hook:()=>[24,50]},
  draw(c, o){
    const col=o.color||'orange';
    if(o.flatbed){
      c.poly([[0,47],[4,42],[104,42],[104,50],[4,50]],{fill:'gray', gap:5});
      if(o.car) c.sub(54,26.4,34,'car',{color:typeof o.car==='string'?o.car:'blue'});
    } else {
      c.poly([[74,42],[86,42],[36,5],[28,10]],{fill:'gray', gap:4});
      c.line(31,9,24,38);
      c.line(24,37,24,45,{cls:'bold'}); c.arc(19,45,11,13,0,210,{cls:'bold'}); c.dot(24,37,4);
      c.rect(12,42,88,16,{fill:col, gap:9}); c.line(40,42,40,58,TH); c.line(70,42,70,58,TH);
      c.line(2,52,12,52,{cls:'bold'}); c.line(3,48,3,56,{cls:'bold'});
    }
    c.rect(4,56,98,5,{fill:'ink', gap:3});
    c.poly([[100,62],[100,24],[122,24],[134,42],[146,44],[146,62]],{fill:col, gap:9});
    glass(c,[[104,28],[120,28],[128,42],[104,42]]);
    lamp(c,105,19,14,5,'orange');
    if(o.lights) rays(c,112,18,5,10,220,320,3,'orange');
    wheel(c,32,62,22); wheel(c,124,62,22);
    c.rect(140,47,5,5,{fill:'yellow', fs:'solid', rough:0.4});
  }};

// dumptruck: dump truck facing right. o.color: body (default yellow), o.load: dirt heaped in the bed, o.dump: bed tipped up with dirt pouring out the back
P.dumptruck = {w:150, h:88, dh:20, anchors:{front:()=>[146,62], bed:()=>[54,30]},
  draw(c, o){
    const col=o.color||'yellow', tip=o.dump?-18:0, R=pts=>rotp(pts,8,60,tip);
    if(o.dump){
      c.blob([[-2,85],[3,76],[11,71],[20,75],[26,85]],{color:'brown', fill:'brown', gap:4});
      [[4,54,5],[11,57,4.5],[2,61,4],[9,64,5],[15,62,3.5],[5,68,4],[12,69,3.5],[17,67,2.5]].forEach(([x,y,d])=>c.circle(x,y,d,{color:'brown', fill:'brown', fs:'solid', rough:0.6}));
      c.line(56,62,62,R([[62,60]])[0][1],{cls:'bold'});
    } else if(o.load){
      c.blob([[8,28],[22,16],[46,10],[72,11],[92,17],[102,28]],{color:'brown', fill:'brown', gap:6});
    }
    c.poly(R([[100,26],[122,24],[122,30],[104,32]]),{fill:col, gap:5});
    c.poly(R([[4,26],[104,26],[104,60],[20,60],[4,44]]),{fill:col, gap:8});
    const rl=R([[4,31],[104,31]]); c.line(rl[0][0],rl[0][1],rl[1][0],rl[1][1],TH);
    [28,52,78].forEach(x=>{ const q=R([[x,31],[x-4,60]]); c.line(q[0][0],q[0][1],q[1][0],q[1][1],TH); });
    c.rect(4,60,104,5,{fill:'ink', gap:3});
    c.poly([[106,66],[106,35],[127,35],[139,50],[146,52],[146,66]],{fill:col, gap:9});
    glass(c,[[110,39],[125,39],[133,50],[110,50]]);
    wheel(c,o.dump?38:26,70,26); wheel(c,o.dump?64:54,70,26); wheel(c,126,70,26);
    c.rect(140,52,5,5,{fill:'paper', fs:'solid', rough:0.4});
  }};

/* ===== Big rigs for living: RVs and trailers ===== */
// rv: Class C motorhome with over-cab bunk, facing right. o.color: side stripe and cab (default teal)
P.rv = {w:180, h:90, dh:22, anchors:{front:()=>[176,62], roof:()=>[70,6], door:()=>[61,70]},
  draw(c, o){
    const col=o.color||'teal';
    c.rect(58,3,22,8,{fill:'gray', gap:5});
    c.rrect(6,10,130,64,6,{fill:'paper', fs:'solid'});
    c.poly([[134,12],[158,14],[166,22],[166,36],[134,36]],{fill:'paper', fs:'solid'});
    c.poly([[134,36],[148,36],[160,54],[174,57],[176,74],[134,74]],{fill:col, gap:9});
    glass(c,[[138,40],[147,40],[156,54],[138,54]]);
    c.poly([[6,48],[100,48],[134,40],[134,46],[100,54],[6,54]],{color:col, fill:col, gap:5});
    c.rect(16,20,26,14,{fill:'sky', gap:6, cls:'soft'}); c.line(29,20,29,34,TH);
    c.rect(86,20,34,14,{fill:'sky', gap:6, cls:'soft'}); c.line(103,20,103,34,TH);
    c.rect(142,20,16,9,{fill:'sky', gap:5, cls:'soft'});
    c.rect(52,20,18,52,{}); c.rect(55,24,12,10,{fill:'sky', gap:5, cls:'soft'}); c.dot(67,48,2.4);
    c.rect(54,74,14,4,{});
    wheel(c,32,74,24); wheel(c,152,74,24);
    c.rect(170,62,5,5,{fill:'yellow', fs:'solid', rough:0.4});
  }};

// trailer: travel trailer (towable camper) with hitch tongue on the right. o.color: stripe (default orange)
P.trailer = {w:140, h:70, dh:16, anchors:{hitch:()=>[137,56], roof:()=>[60,6], door:()=>[42,56]},
  draw(c, o){
    const col=o.color||'orange';
    c.line(118,46,137,56,{cls:'bold'}); c.line(118,54,137,56,{cls:'bold'}); c.dot(137,56,5);
    c.rrect(120,34,8,12,3,{fill:'gray', gap:4});
    c.line(128,52,128,66); c.line(124,66,132,66,{cls:'bold'});
    c.rrect(6,6,112,50,13,{fill:'paper', fs:'solid'});
    lamp(c,6,38,112,4,col);
    c.rect(16,16,22,14,{fill:'sky', gap:6, cls:'soft'});
    c.rect(84,16,24,14,{fill:'sky', gap:6, cls:'soft'}); c.line(96,16,96,30,TH);
    c.rect(44,16,15,40,{}); c.rect(47,20,9,8,{fill:'sky', gap:5, cls:'soft'}); c.dot(56,38,2.2);
    c.arc(80,56,26,24,180,360);
    wheel(c,80,57,20);
  }};

/* ===== Water ===== */
// boat: small motorboat with outboard motor on water, facing right. o.color: hull (default red), o.water:false hides the water
P.boat = {w:120, h:64, dh:13, anchors:{front:()=>[116,26], top:()=>[70,12]},
  draw(c, o){
    const col=o.color||'red';
    c.rrect(1,8,13,17,3,{fill:'ink', gap:4});
    c.rect(4,25,5,22,{fill:'gray', gap:4});
    glass(c,[[58,21],[66,5],[76,5],[80,19]]);
    c.line(84,17,112,14,LT); c.line(88,17,88,13,LT); c.line(100,16,100,12,LT);
    c.poly([[7,24],[117,15],[106,30],[92,44],[13,44]],{fill:col, gap:8});
    c.line(11,32,106,26,TH);
    if(o.water!==false){ waterBand(c,0,120,42,18); c.curve([[112,30],[118,36],[120,42]],{color:'blue', cls:'thin'}); }
  }};

// sailboat: sailboat with mainsail and jib on water, facing right. o.color: hull (default blue), o.sail: sail color (default white), o.water:false hides the water
P.sailboat = {w:90, h:100, dh:24, anchors:{top:()=>[46,2], front:()=>[88,74]},
  draw(c, o){
    const col=o.color||'blue', sf=o.sail?{fill:o.sail, gap:8, cls:'soft'}:{fill:'paper', fs:'solid'};
    c.poly([[46,3],[34,7],[46,11]],{color:'red', fill:'red', fs:'solid', rough:0.4});
    c.poly([[44,12],[44,66],[8,66]],sf);
    c.poly([[49,14],[84,66],[51,66]],sf);
    c.line(46,2,46,70,{cls:'bold'});
    c.line(6,67,46,67,{cls:'bold'});
    [30,48].forEach(y=>c.line(44,y,44-(y-12)*36/54,y,{cls:'thin', color:'gray'}));
    c.poly([[2,70],[88,70],[76,86],[14,86]],{fill:col, gap:8});
    if(o.water!==false) waterBand(c,0,90,83,15);
  }};

// jetski: personal watercraft (jet ski) on water, facing right. o.color: body (default yellow), o.spray:false hides the spray, o.water:false hides the water
P.jetski = {w:100, h:56, dh:10, anchors:{front:()=>[98,34], seat:()=>[36,20]},
  draw(c, o){
    const col=o.color||'yellow';
    if(o.spray!==false){ c.curve([[14,38],[6,30],[3,18]],{color:'sky'}); c.curve([[12,40],[3,36],[0,28]],{color:'sky', cls:'thin'}); [[8,14,3],[2,24,2.5],[12,22,2.5]].forEach(([x,y,d])=>c.circle(x,y,d,{color:'sky', rough:0.4, cls:'thin'})); }
    c.poly([[8,34],[70,31],[98,34],[90,43],[14,43]],{fill:col, gap:6});
    c.poly([[14,34],[22,26],[54,24],[64,18],[82,22],[95,33]],{fill:col, gap:6});
    c.poly([[20,26],[24,19],[52,18],[54,24]],{fill:'ink', gap:4});
    c.line(16,38,92,37,TH);
    c.line(66,20,61,8,{cls:'bold'}); c.line(55,8,67,6,{cls:'bold'});
    if(o.water!==false) waterBand(c,0,100,40,15);
  }};

/* ===== Equipment ===== */
// forklift: forklift facing right with mast and forks. o.color: body (default orange), o.load: pallet with a box on the forks, o.raised: forks lifted high
P.forklift = {w:96, h:90, dh:16, anchors:{forks:o=>[88,o.raised?46:74], roof:()=>[40,12]},
  draw(c, o){
    const col=o.color||'orange', up=o.raised?-30:0;
    c.rect(66,6,8,74,{fill:'gray', gap:5});
    c.line(22,46,26,12,{cls:'bold'}); c.line(58,46,58,12,{cls:'bold'}); c.line(20,12,62,12,{cls:'bold'}); c.line(30,12,30,16,TH); c.line(42,12,42,16,TH);
    c.poly([[4,72],[3,56],[10,46],[62,46],[64,72]],{fill:col, gap:8});
    c.poly([[24,46],[25,32],[31,32],[31,41],[42,41],[42,46]],{fill:'ink', gap:4});
    c.line(54,46,50,34); c.line(45,33,55,35,{cls:'bold'});
    c.rect(74,54+up,6,24,{fill:'ink', gap:4});
    c.line(77,78+up,96,78+up,{cls:'bold'});
    if(o.load){ c.rect(80,72+up,16,5,{fill:'brown', gap:4}); c.rect(81,54+up,15,18,{fill:'brown', gap:7, cls:'soft'}); c.line(81,60+up,96,60+up,LT); }
    wheel(c,50,76,22); wheel(c,16,79,16);
  }};

// bulldozer: crawler bulldozer with blade, facing right. o.color: body and blade (default yellow)
P.bulldozer = {w:136, h:84, dh:19, anchors:{front:()=>[132,60], roof:()=>[36,6]},
  draw(c, o){
    const col=o.color||'yellow';
    c.rect(80,12,5,20,{fill:'gray', gap:3});
    c.rect(16,10,40,32,{}); c.rect(21,15,30,21,{fill:'sky', gap:6, cls:'soft'});
    c.rect(12,6,48,6,{fill:col, gap:4});
    c.poly([[8,58],[8,42],[60,42],[60,30],[96,32],[100,42],[100,58]],{fill:col, gap:8});
    [68,76,84,92].forEach(x=>c.line(x,36,x,44,LT));
    c.rrect(4,58,98,22,11,{fill:'ink', gap:5, cls:'soft'});
    [[15,69,16],[34,71,9],[52,71,9],[70,71,9],[91,69,16]].forEach(([x,y,d])=>{ c.circle(x,y,d,{fill:'paper', fs:'solid', rough:0.5}); c.dot(x,y,2.4); });
    c.line(98,50,114,54,{cls:'bold'}); c.line(94,66,114,70,{cls:'bold'});
    c.poly([[110,26],[122,28],[130,40],[133,58],[129,80],[112,80],[116,60],[114,42]],{fill:col, gap:6});
  }};

/* ===== Air ===== */
// plane: airplane, side view facing right. o.kind: 'jet' (airliner, default) | 'prop' (small single-engine plane), o.color: tail, wing and stripe (default blue)
P.plane = {w:180, h:64, dh:16, anchors:{front:()=>[178,34], top:()=>[16,4]},
  draw(c, o){
    const col=o.color||'blue';
    if(o.kind==='prop'){
      c.poly([[22,30],[12,8],[24,8],[40,28]],{fill:col, gap:6});
      c.blob([[18,30],[60,26],[120,24],[150,26],[160,32],[150,42],[110,44],[40,40]],{fill:'paper', fs:'solid'});
      glass(c,[[108,26],[128,25],[134,32],[110,33]]);
      c.line(30,35,150,36,{color:col});
      c.poly([[64,16],[150,16],[150,22],[64,22]],{fill:col, gap:5});
      c.line(116,22,104,34,TH); c.line(70,22,84,32,TH);
      c.poly([[22,34],[8,38],[14,41],[36,38]],{fill:col, gap:5});
      c.line(110,43,104,54); c.line(140,40,144,54); wheel(c,104,55,10); wheel(c,145,55,10);
      c.ellipse(166,34,5,30,{cls:'thin', rough:0.5}); c.circle(161,34,6,{fill:'gray', fs:'solid', rough:0.4});
      return;
    }
    c.poly([[16,30],[8,4],[22,4],[44,28]],{fill:col, gap:7});
    c.blob([[18,28],[60,26],[150,26],[166,28],[177,35],[170,42],[150,44],[50,44],[24,40],[13,33]],{fill:'paper', fs:'solid'});
    for(let x=46;x<144;x+=8) c.dot(x,32,3.4,{color:'sky'});
    c.poly([[160,29],[168,29],[173,34],[162,35]],{fill:'sky', fs:'solid', rough:0.4});
    c.rect(150,29,6,11,{cls:'thin', rough:0.4});
    c.line(22,38,170,38,{color:col});
    c.poly([[22,36],[6,41],[14,43],[36,40]],{fill:col, gap:5});
    c.poly([[78,38],[106,38],[86,60],[72,60]],{fill:col, gap:6});
    c.rrect(90,44,24,10,4,{fill:'gray', gap:4});
  }};

/* ===== Road things ===== */
// trafficlight: traffic signal on a pole. o.on: 'red' (default) | 'yellow' | 'green' | 'none'
P.trafficlight = {w:36, h:96, dh:20, anchors:{top:()=>[18,3]},
  draw(c, o){
    const on=o.on||'red', ys={red:16, yellow:35, green:54};
    c.rect(15,66,6,27,{fill:'gray', gap:4}); c.line(8,94,28,94,{cls:'bold'});
    c.rrect(5,4,26,62,6,{fill:'ink', gap:5, cls:'soft'});
    ['red','yellow','green'].forEach(k=>{ const y=ys[k];
      c.circle(18,y,15,k===on?{fill:k, fs:'solid'}:{fill:'paper', fs:'solid'});
      if(k!==on) c.circle(18,y,9,{color:k, cls:'thin', rough:0.4});
      if(k===on){ c.line(-1,y-4,3,y-2,{color:k, rough:0.4}); c.line(-1,y+4,3,y+2,{color:k, rough:0.4}); c.line(33,y-2,37,y-4,{color:k, rough:0.4}); c.line(33,y+2,37,y+4,{color:k, rough:0.4}); }
    });
  }};

// stopsign: red octagonal STOP sign on a post. o.text (default 'STOP')
P.stopsign = {w:50, h:96, dh:18, anchors:{top:()=>[25,1]},
  draw(c, o){
    c.rect(22,44,6,49,{fill:'gray', gap:4}); c.line(14,94,36,94,{cls:'bold'});
    const oc=(r)=>{ const p=[]; for(let k=0;k<8;k++){ const a=rad(22.5+45*k); p.push([25+r*Math.cos(a), 24+r*Math.sin(a)]); } return p; };
    c.poly(oc(24),{fill:'red', fs:'solid'});
    c.poly(oc(20),{color:'paper', cls:'thin', rough:0.4});
    const t=o.text||'STOP', s=fit(t,32,15);
    c.text(25,24+s*0.36,t,{size:s, color:'paper', bold:true});
  }};

// cone: orange traffic cone with reflective bands. o.color (default orange)
P.cone = {w:44, h:56, dh:8,
  draw(c, o){
    const col=o.color||'orange', xl=y=>18-(y-4)*10/45, xr=y=>26+(y-4)*10/45;
    c.poly([[18,4],[26,4],[36,49],[8,49]],{fill:col, fs:'solid'});
    [[16,22],[30,36]].forEach(([a,b])=>c.poly([[xl(a),a],[xr(a),a],[xr(b),b],[xl(b),b]],{fill:'paper', fs:'solid', rough:0.4}));
    c.rect(2,48,40,6,{fill:col, fs:'solid'});
  }};

// gaspump: gas station fuel pump with price screen, hose and nozzle. o.color: body (default red), o.price: screen text (default '$3.49'; '' for a blank screen)
P.gaspump = {w:60, h:96, dh:18, anchors:{top:()=>[24,3], nozzle:()=>[52,42]},
  draw(c, o){
    const col=o.color||'red';
    c.rect(2,88,44,6,{fill:'gray', gap:4});
    c.rrect(6,6,36,83,5,{fill:col, gap:9});
    c.rect(4,3,40,8,{fill:col, fs:'solid'});
    c.rect(11,16,26,15,{fill:'paper', fs:'solid', rough:0.5});
    const t=o.price!=null?o.price:'$3.49'; if(t){ const s=fit(t,22,10); c.text(24,23.5+s*0.34,t,{size:s, bold:true}); }
    c.rect(14,38,20,12,{fill:'paper', fs:'solid', rough:0.5}); [18,24,30].forEach(x=>{ c.dot(x,42,2.2); c.dot(x,47,2.2); });
    c.curve([[42,76],[54,78],[58,62],[54,47]],{cls:'bold'});
    c.poly([[42,38],[53,38],[58,44],[53,47],[48,44],[42,44]],{fill:'ink', gap:3});
  }};

// crash: comic-book collision burst with a shout word. o.text (default 'CRASH!'), o.color: burst (default yellow), o.ink: word color (default red)
P.crash = {w:110, h:80, dh:16, anchors:{center:()=>[55,40]},
  draw(c, o){
    const n=12, J=[1,0.86,1.06,0.92,1,0.8,1.08,0.9,0.98,0.84,1.04,0.9], burst=(rx,ry,k)=>{ const p=[]; for(let i=0;i<2*n;i++){ const a=rad(-90+i*180/n), r=i%2?0.6:J[(i/2)|0]*k+ (1-k); p.push([55+rx*r*Math.cos(a), 40+ry*r*Math.sin(a)]); } return p; };
    c.poly(burst(54,39,1),{color:'red', fill:o.color||'yellow', fs:'solid'});
    c.poly(burst(44,31,0.6),{color:'orange', fill:'paper', fs:'solid', rough:0.7});
    const t=o.text||'CRASH!', s=fit(t,56,20);
    c.text(55,40+s*0.34,t,{size:s, color:o.ink||'red', bold:true, rot:-7});
  }};
})();
