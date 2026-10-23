/* ---------- Sketch props: people and core scenery ----------
   Each prop: {w, h, dh (default height in layout units), anchors?, draw(c, opt, el)}.
   Draw in the prop's own w x h box. c.line/poly/rect/rrect/curve/blob/ellipse/circle/dot/arc/text/sub. */
(()=>{
const P = SK.PROPS;

/* People. Cast presets give each recurring character a fixed look. */
const CAST = {
  dana:    {hair:'bob', hairColor:'brown', shirt:'blue', badge:true},                    // the insurance agent (producer)
  sam:     {hair:'short', shirt:'green', beard:true},                                    // homeowner, Sam Miller
  jen:     {hair:'long', shirt:'teal'},                                                  // Jen Miller
  tony:    {hair:'short', shirt:'red', mustache:true, hat:'chef', apron:true},          // Tony, pizza shop owner
  rosa:    {hair:'pony', shirt:'purple'},                                                // driver and commuter
  kid:     {hair:'spiky', shirt:'orange', hat:'cap'},
  adjuster:{hair:'short', shirt:'gray', glasses:true, tie:true},
  judge:   {hair:'short', shirt:'ink', robe:true, glasses:true},
  thief:   {hair:'none', shirt:'gray', hat:'beanie', mask:true, stripes:true},
  worker:  {hair:'short', shirt:'orange', hat:'hardhat', vest:true},
  doctor:  {hair:'short', shirt:'white', coat:true, glasses:true},
  boss:    {hair:'short', shirt:'blue', tie:true, suit:true},
  neighbor:{hair:'curly', shirt:'brown'},
  grandma: {hair:'bun', hairColor:'gray', shirt:'pink', glasses:true},
  regulator:{hair:'bob', shirt:'gray', glasses:true, badge:true},
  person:  {hair:'short', shirt:'gray'},
};
P.person = {w:44, h:100, dh:26,
  anchors:{head:()=>[22,4], hand:o=>armEnds(o.pose||'stand')[1], face:()=>[22,16]},
  draw(c, o){
    const L = Object.assign({}, CAST[o.who||'person']||CAST.person, o);
    const pose=L.pose||'stand', mood=L.mood||'happy', sc=L.shirt||'gray';
    // legs
    const legs = pose==='run' ? [[19,62,8,90],[25,62,36,88]] : pose==='sit' ? [[18,62,34,64],[26,62,40,66]] : pose==='walk' ? [[19,62,13,92],[25,62,31,92]] : [[19,62,15,93],[25,62,29,93]];
    legs.forEach(l=>c.line(l[0],l[1],l[2],l[3]));
    if(pose==='sit'){ c.line(34,64,34,92); c.line(40,66,40,93); }
    else { c.line(legs[0][2],legs[0][3],legs[0][2]-4,legs[0][3]+0.5,{rough:0.5}); c.line(legs[1][2],legs[1][3],legs[1][2]+4,legs[1][3]+0.5,{rough:0.5}); }
    // torso
    if(L.robe){ c.poly([[13,30],[31,30],[36,90],[8,90]],{fill:'ink', gap:9}); }
    else if(L.coat){ c.poly([[13,30],[31,30],[34,72],[10,72]],{fill:'white', fs:'solid'}); c.line(22,30,22,72); }
    else c.rrect(13,29,18,35,5,{fill:sc, gap:10});
    if(L.stripes){ [38,46,54].forEach(y=>c.line(14,y,30,y,{cls:'thin'})); }
    if(L.apron){ c.poly([[15,40],[29,40],[30,66],[14,66]],{fill:'white', fs:'solid', color:'ink'}); }
    if(L.vest){ c.poly([[13,30],[18,30],[18,63],[13,63]],{fill:'orange'}); c.poly([[26,30],[31,30],[31,63],[26,63]],{fill:'orange'}); }
    if(L.tie){ c.poly([[21,31],[23,31],[24,46],[22,49],[20,46]],{fill:'red', fs:'solid'}); }
    if(L.suit){ c.line(16,30,21,42); c.line(28,30,23,42); }
    if(L.badge){ c.rect(24.5,35,5,4,{color:'blue', rough:0.5}); }
    // arms
    const [e1,h1,e2,h2] = (()=>{ const a=armEnds(pose); return [a[2],a[0],a[3],a[1]]; })();
    c.poly([[14,32],e1,h1],{open:true}); c.poly([[30,32],e2,h2],{open:true});
    c.dot(h1[0],h1[1],3.2,{color:'ink'}); c.dot(h2[0],h2[1],3.2,{color:'ink'});
    // head
    c.circle(22,16,19,{fill:'paper', fs:'solid'});
    hair(c, L);
    if(L.mask){ c.rect(12.5,11.5,19,5,{fill:'ink', fs:'solid', rough:0.5}); }
    face(c, mood, L);
    if(L.glasses){ c.circle(17.6,15,5.2,{rough:0.4, cls:'thin'}); c.circle(26.4,15,5.2,{rough:0.4, cls:'thin'}); c.line(20.2,15,23.8,15,{cls:'thin'}); }
    if(L.beard){ c.arc(22,19,16,12,10,170,{cls:'thin'}); c.arc(22,20,13,10,20,160,{cls:'thin'}); }
    if(L.mustache){ c.curve([[16.5,20.8],[19.5,19.2],[22,20.2],[24.5,19.2],[27.5,20.8]],{cls:'bold'}); }
    hat(c, L);
    // held item
    if(L.hold){ const hp = armEnds(pose)[1]; c.sub(hp[0]+5, hp[1]-4, holdSize(L.hold), L.hold, L.holdOpt||{}); }
    if(L.sign){ const hp=armEnds('point')[1]; c.rect(30,4,40,18,{fill:'paper', fs:'solid', rough:0.6}); c.line(34,22,30,40); c.text(50,16,L.sign,{size:7.5}); }
  }};
function holdSize(n){ return {money:12, policy:16, phone:11, paper:14, briefcase:14, key:9, pizza:12, wrench:13, clipboard:16, sign:16, coffee:9, gift:12, bankcheck:10}[n] || 14; }
function armEnds(pose){
  // returns [left hand, right hand, left elbow, right elbow] in person box coords
  switch(pose){
    case 'wave':  return [[10,58],[38,8],[8,46],[38,22]];
    case 'point': return [[10,58],[43,30],[8,46],[35,32]];
    case 'shrug': return [[3,28],[41,28],[4,42],[40,42]];
    case 'cheer': return [[3,6],[41,6],[6,20],[38,20]];
    case 'think': return [[10,58],[26,24],[8,46],[36,40]];
    case 'hold':  return [[30,46],[36,44],[10,46],[34,52]];
    case 'sad':   return [[13,60],[31,60],[12,48],[32,48]];
    case 'run':   return [[3,36],[42,30],[8,46],[36,44]];
    case 'stop':  return [[10,58],[43,22],[8,46],[38,30]];
    case 'sit':   return [[24,52],[34,52],[12,48],[30,50]];
    case 'walk':  return [[8,56],[36,56],[10,45],[34,45]];
    default:      return [[9,58],[35,58],[9,46],[35,46]];
  }
}
function face(c, mood, L){
  const ey=15;
  if(mood==='shocked'){ c.circle(18,ey,3,{rough:0.3,cls:'thin'}); c.circle(26,ey,3,{rough:0.3,cls:'thin'}); c.dot(18,ey,1.3); c.dot(26,ey,1.3); c.circle(22,21.5,3.6,{rough:0.4}); c.line(15.5,9.5,19.5,9,{cls:'thin'}); c.line(24.5,9,28.5,9.5,{cls:'thin'}); return; }
  if(mood==='sleep'){ c.arc(18,ey,4,3,0,180,{cls:'thin'}); c.arc(26,ey,4,3,0,180,{cls:'thin'}); }
  else { c.dot(18,ey,2.2); c.dot(26,ey,2.2); }
  if(mood==='happy'){ c.arc(22,19.2,9,6,15,165); }
  else if(mood==='smirk'){ c.curve([[18,21.5],[22,21.8],[26,19.4]]); }
  else if(mood==='sad'){ c.arc(22,24,9,6,200,340); }
  else if(mood==='worried'){ c.curve([[17.5,22],[19.5,20.8],[22,22],[24.5,20.8],[26.5,22]]); c.line(15.6,11.6,19.6,10.4,{cls:'thin'}); c.line(24.4,10.4,28.4,11.6,{cls:'thin'}); }
  else if(mood==='angry'){ c.arc(22,24,9,5,205,335); c.line(15.6,10.2,19.8,12,{cls:'bold'}); c.line(24.2,12,28.4,10.2,{cls:'bold'}); }
  else if(mood==='laugh'){ c.arc(22,19.5,10,8,0,180,{closed:true, fill:'ink', fs:'solid'}); }
  else c.line(18.5,21,25.5,21);
}
function hair(c, L){
  const col=L.hairColor||'ink', h=L.hair||'short';
  if(h==='none') return;
  if(h==='short'){ c.curve([[12.5,13],[14,7.5],[19,5.5],[25,5.5],[30,8],[31.5,13]],{color:col, cls:'bold'}); }
  else if(h==='spiky'){ c.poly([[12.5,12],[14,5],[17,8],[19,3.5],[22,7.5],[25,3.5],[27,8],[30,5],[31.5,12]],{open:true, color:col}); }
  else if(h==='curly'){ for(let i=0;i<6;i++) c.circle(13.5+i*3.4, 8-Math.sin(i/5*Math.PI)*2.5, 5,{color:col, rough:0.6, cls:'thin'}); }
  else if(h==='bob'){ c.curve([[12,22],[11.5,12],[15,6.5],[22,5],[29,6.5],[32.5,12],[32,22]],{color:col, cls:'bold'}); c.curve([[14,9],[20,10.5],[27,8.5]],{color:col}); }
  else if(h==='long'){ c.curve([[12.5,30],[11,16],[14,7],[22,5],[30,7],[33,16],[31.5,30]],{color:col, cls:'bold'}); }
  else if(h==='pony'){ c.curve([[12.5,13],[14,7],[22,5],[30,7.5],[31.5,13]],{color:col, cls:'bold'}); c.curve([[31,9],[37,12],[38,20],[35,26]],{color:col, cls:'bold'}); }
  else if(h==='bun'){ c.curve([[12.5,13],[14,7],[22,5.5],[30,7],[31.5,13]],{color:col}); c.circle(22,3.2,7,{color:col, fill:col, gap:5}); }
}
function hat(c, L){
  const t=L.hat; if(!t) return;
  if(t==='cap'){ c.poly([[12.5,10],[14.5,4],[22,2.5],[29.5,4],[31.5,10]],{fill:L.hatColor||'red', gap:6}); c.line(29.5,10,38,10.6,{cls:'bold'}); }
  else if(t==='hardhat'){ c.arc(22,10,22,15,180,360,{closed:true, fill:'yellow', gap:6}); c.line(9,10,35,10,{cls:'bold'}); }
  else if(t==='chef'){ c.blob([[14,7],[13,-3],[19,-6],[25,-6],[31,-3],[30,7]],{fill:'white', fs:'solid'}); c.line(14,7,30,7); }
  else if(t==='beanie'){ c.arc(22,10,21,16,180,360,{closed:true, fill:L.hatColor||'ink', gap:5}); c.circle(22,1.5,3.5,{fill:L.hatColor||'ink', fs:'solid'}); }
  else if(t==='top'){ c.rect(15,-6,14,14,{fill:'ink', gap:5}); c.line(10,8,34,8,{cls:'bold'}); }
}

/* Buildings */
P.house = {w:100, h:92, dh:30, anchors:{door:()=>[50,84], roof:()=>[50,10], chimney:()=>[73,8]},
  draw(c, o){
    c.rect(68,6,10,20,{fill:'brown', gap:8});
    c.poly([[4,44],[50,8],[96,44]],{fill:o.roof||'red', gap:11});
    c.rect(12,42,76,48,{fill:o.wall||null, gap:14});
    c.rect(43,62,15,28,{fill:'brown', gap:7}); c.dot(54.5,77,2);
    [[19,52],[67,52]].forEach(([x,y])=>{ c.rect(x,y,15,14,{fill:'sky', gap:8, cls:'soft'}); c.line(x+7.5,y,x+7.5,y+14,{cls:'thin'}); c.line(x,y+7,x+15,y+7,{cls:'thin'}); });
    if(o.garage){ c.rect(88,56,30,34,{}); c.poly([[86,58],[103,46],[120,58]],{fill:o.roof||'red', gap:11}); for(let y=62;y<88;y+=5) c.line(92,y,114,y,{cls:'thin'}); }
  }};
P.shed = {w:60, h:56, dh:16, draw(c,o){ c.poly([[2,22],[30,4],[58,22]],{fill:o.roof||'brown', gap:10}); c.rect(8,21,44,33,{}); c.rect(22,31,16,23,{}); c.line(22,31,38,54,{cls:'thin'}); c.line(38,31,22,54,{cls:'thin'}); }};
P.store = {w:120, h:90, dh:30, anchors:{door:()=>[60,84]},
  draw(c, o){
    c.rect(8,22,104,66,{});
    c.rect(4,8,112,16,{fill:'paper', fs:'solid'}); c.text(60,20.5,o.name||'SHOP',{size:11});
    const cols=['red','paper']; for(let i=0;i<8;i++){ c.poly([[8+i*13,24],[21+i*13,24],[21+i*13,34],[8+i*13,34]],{fill:o.awning||cols[i%2], fs:i%2?'solid':'hachure', gap:6, rough:0.6}); }
    c.rect(16,44,30,26,{fill:'sky', gap:9, cls:'soft'}); c.rect(74,44,30,26,{fill:'sky', gap:9, cls:'soft'});
    c.rect(51,50,18,38,{fill:'brown', gap:7});
  }};
P.insurer = {w:100, h:96, dh:30, anchors:{top:()=>[50,4]},
  draw(c, o){
    c.poly([[6,30],[50,6],[94,30]],{fill:'blue', gap:10, cls:'soft'});
    c.rect(10,30,80,8,{}); c.text(50,36.5,o.name||'INSURANCE CO.',{size:7.2});
    for(let i=0;i<4;i++){ c.rect(16+i*19,40,8,42,{}); }
    c.rect(6,84,88,8,{fill:'gray', gap:8}); c.sub(50,20,12,'shield',{});
  }};
P.office = {w:70, h:100, dh:32, draw(c,o){ c.rect(8,6,54,92,{}); for(let r=0;r<5;r++) for(let k=0;k<3;k++) c.rect(15+k*16,13+r*15,10,9,{fill:'sky', gap:6, cls:'soft'}); c.rect(29,84,12,14,{fill:'brown', gap:6}); if(o.name) c.text(35,4,o.name,{size:7}); }};
P.factory = {w:120, h:84, dh:28, draw(c,o){ c.rect(80,6,12,40,{fill:'gray', gap:8}); c.poly([[6,82],[6,36],[30,22],[30,36],[54,22],[54,36],[78,22],[78,36],[114,36],[114,82]],{}); for(let k=0;k<4;k++) c.rect(14+k*25,50,14,12,{fill:'sky', gap:6, cls:'soft'}); c.rect(92,58,16,24,{fill:'brown', gap:7}); c.curve([[86,4],[90,-3],[84,-9],[92,-15]],{color:'gray', cls:'thin'}); if(o.name) c.text(50,76,o.name,{size:7}); }};
P.apartment = {w:80, h:110, dh:34, draw(c,o){ c.rect(6,8,68,100,{}); c.rect(4,4,72,6,{fill:'gray', gap:6}); for(let r=0;r<5;r++) for(let k=0;k<3;k++) c.rect(13+k*21,16+r*17,11,10,{fill:'sky', gap:6, cls:'soft'}); c.rect(33,92,14,16,{fill:'brown', gap:6}); }};

/* Vehicles */
P.car = {w:120, h:56, dh:14, anchors:{front:()=>[118,34], roof:()=>[60,8]},
  draw(c, o){
    const col=o.color||'red';
    c.poly([[6,40],[8,26],[30,22],[44,8],[84,8],[100,24],[116,28],[118,42],[108,44]],{open:false, fill:col, gap:10});
    c.poly([[48,12],[60,12],[60,24],[38,24]],{fill:'sky', gap:6, cls:'soft'}); c.poly([[64,12],[82,12],[94,24],[64,24]],{fill:'sky', gap:6, cls:'soft'});
    c.circle(32,44,20,{fill:'paper', fs:'solid'}); c.circle(32,44,7,{cls:'thin'}); c.circle(92,44,20,{fill:'paper', fs:'solid'}); c.circle(92,44,7,{cls:'thin'});
    c.rect(110,30,6,5,{fill:'yellow', fs:'solid', rough:0.4});
    if(o.dent){ c.poly([[104,26],[108,32],[103,36],[109,41]],{open:true, color:'ink', cls:'bold'}); }
  }};
P.truck = {w:130, h:66, dh:16, draw(c,o){ const col=o.color||'blue'; c.poly([[6,52],[6,30],[70,30],[70,52]],{fill:col, gap:10}); c.poly([[70,52],[70,14],[100,14],[116,32],[124,34],[124,52]],{fill:col, gap:10}); c.poly([[76,18],[98,18],[110,32],[76,32]],{fill:'sky', gap:6, cls:'soft'}); [30,98].forEach(x=>{ c.circle(x,54,20,{fill:'paper', fs:'solid'}); c.circle(x,54,7,{cls:'thin'}); }); }};
P.semi = {w:200, h:76, dh:20, draw(c,o){ c.rect(4,8,128,52,{fill:o.trailer||'paper', fs:o.trailer?'hachure':'solid', gap:12}); if(o.name) c.text(68,40,o.name,{size:12}); c.poly([[136,60],[136,22],[170,22],[186,40],[196,42],[196,60]],{fill:o.color||'red', gap:10}); c.poly([[142,26],[166,26],[178,40],[142,40]],{fill:'sky', gap:6, cls:'soft'}); [24,52,110,150,182].forEach(x=>{ c.circle(x,62,18,{fill:'paper', fs:'solid'}); c.circle(x,62,6,{cls:'thin'}); }); }};

/* Nature and perils */
P.tree = {w:70, h:100, dh:28, draw(c,o){
  c.poly([[30,98],[32,58],[38,58],[40,98]],{fill:'brown', gap:7});
  c.blob([[35,4],[50,8],[62,22],[64,40],[54,58],[35,62],[16,58],[6,40],[8,22],[20,8]],{fill:'green', gap:10});
  if(o.fall){ c.line(28,98,42,98); }
}};
P.fire = {w:44, h:56, dh:12, draw(c,o){
  c.blob([[22,2],[30,14],[38,24],[40,38],[34,50],[22,55],[10,50],[4,38],[7,26],[14,18],[16,28],[20,14]],{color:'red', fill:'orange', fs:'solid', cls:'soft2'});
  c.blob([[22,22],[28,32],[30,42],[26,50],[18,50],[14,42],[17,34]],{color:'orange', fill:'yellow', fs:'solid'});
}};
P.smoke = {w:50, h:60, dh:14, draw(c){ c.blob([[20,56],[10,48],[12,38],[22,34],[18,24],[26,14],[36,16],[40,26],[36,36],[42,44],[34,54]],{color:'gray', fill:'gray', gap:9, cls:'soft'}); }};
P.cloud = {w:80, h:46, dh:12, draw(c,o){ c.blob([[14,40],[4,30],[10,18],[24,16],[30,6],[46,4],[56,14],[70,14],[78,26],[72,38],[60,42]],{color:o.dark?'ink':'gray', fill:o.dark?'gray':null, gap:9}); }};
P.rain = {w:80, h:80, dh:22, draw(c,o){ P.cloud.draw(c,{dark:true}); for(let i=0;i<7;i++){ const x=10+i*10, y=50+(i%2)*8; c.line(x,y,x-4,y+12,{color:'blue', cls:'thin'}); } }};
P.storm = {w:80, h:84, dh:24, draw(c,o){ P.cloud.draw(c,{dark:true}); c.poly([[40,44],[30,62],[40,62],[32,82],[52,56],[42,56],[50,44]],{color:'orange', fill:'yellow', fs:'solid'}); }};
P.lightning = {w:30, h:50, dh:12, draw(c){ c.poly([[18,2],[4,28],[15,28],[8,48],[27,20],[16,20],[24,2]],{color:'orange', fill:'yellow', fs:'solid'}); }};
P.snow = {w:40, h:40, dh:8, draw(c){ for(let a=0;a<180;a+=60){ const r=rad2(a); c.line(20-18*Math.cos(r),20-18*Math.sin(r),20+18*Math.cos(r),20+18*Math.sin(r),{color:'sky'}); } c.circle(20,20,6,{color:'sky', cls:'thin'}); }};
P.sun = {w:50, h:50, dh:12, draw(c){ c.circle(25,25,22,{color:'orange', fill:'yellow', fs:'solid'}); for(let a=0;a<360;a+=45){ const r=rad2(a); c.line(25+16*Math.cos(r),25+16*Math.sin(r),25+23*Math.cos(r),25+23*Math.sin(r),{color:'orange'}); } }};
P.wind = {w:70, h:40, dh:10, draw(c){ c.curve([[2,10],[30,8],[48,10],[54,4],[48,0]],{color:'gray'}); c.curve([[8,22],[44,20],[62,22],[68,14],[60,10]],{color:'gray'}); c.curve([[2,34],[28,32],[40,34],[44,28]],{color:'gray'}); }};
P.water = {w:120, h:30, dh:8, draw(c,o){ for(let r=0;r<2;r++){ const y=8+r*12, pts=[]; for(let x=0;x<=120;x+=10) pts.push([x, y+(x/10%2?4:-1)]); c.curve(pts,{color:'blue'}); } if(o.fill!==false) c.poly([[0,12],[120,12],[120,30],[0,30]],{nostroke:true, fill:'blue', gap:10, color:'blue', cls:'soft'}); }};

/* Money and paper */
P.money = {w:56, h:34, dh:9, draw(c,o){ for(let i=2;i>=0;i--){ const x=4+i*3, y=4+i*4; c.rect(x,y,44,22,{fill:'green', gap:9, cls:'soft'}); } c.circle(28,15,10,{color:'green'}); c.text(28,19.5,'$',{size:12, color:'green'}); }};
P.bill = {w:50, h:26, dh:7, draw(c){ c.rect(2,2,46,22,{fill:'green', gap:9, cls:'soft'}); c.circle(25,13,10,{color:'green'}); c.text(25,17.5,'$',{size:11, color:'green'}); }};
P.coins = {w:40, h:34, dh:8, draw(c){ for(let i=0;i<4;i++) c.ellipse(20,28-i*6,30,9,{color:'orange', fill:'yellow', fs:'solid'}); c.text(20,10,'$',{size:7,color:'orange'}); }};
P.moneybag = {w:50, h:56, dh:14, draw(c){ c.blob([[18,14],[10,26],[6,42],[14,54],[36,54],[44,42],[40,26],[32,14]],{color:'brown', fill:'yellow', gap:8, cls:'soft'}); c.poly([[16,4],[34,4],[30,14],[20,14]],{color:'brown'}); c.text(25,44,'$',{size:20, color:'green'}); }};
P.policy = {w:40, h:52, dh:16, anchors:{top:()=>[20,0]}, draw(c,o){
  c.poly([[2,2],[30,2],[38,10],[38,50],[2,50]],{fill:'paper', fs:'solid'}); c.poly([[30,2],[30,10],[38,10]],{open:true, cls:'thin'});
  c.text(19,13.5,o.title||'POLICY',{size:o.tsize||7.5, color:o.tcolor||'blue'});
  for(let i=0;i<5;i++) c.line(7,21+i*5.6,i%2?28:33,21+i*5.6,{cls:'thin', color:'gray'});
  if(o.sign) c.curve([[8,47],[12,43],[15,47],[19,43],[24,46]],{color:'blue', cls:'thin'});
}};
P.paper = P.policy;
P.clipboard = {w:40, h:54, dh:15, draw(c,o){ c.rect(3,6,34,46,{fill:'brown', gap:8, cls:'soft'}); c.rect(7,10,26,38,{fill:'paper', fs:'solid'}); c.rect(13,2,14,7,{fill:'gray', fs:'solid'}); for(let i=0;i<4;i++){ c.line(10,17+i*8,13,20+i*8,{color:'green', cls:'thin'}); c.line(13,20+i*8,16,14+i*8,{color:'green', cls:'thin'}); c.line(18,17+i*8,30,17+i*8,{cls:'thin', color:'gray'}); } }};
P.bankcheck = {w:60, h:28, dh:7, draw(c,o){ c.rect(2,2,56,24,{fill:'paper', fs:'solid'}); c.text(10,11,'PAY',{size:5, align:'start'}); c.line(20,10,52,10,{cls:'thin',color:'gray'}); c.text(46,20,o.amount||'$',{size:6, color:'green'}); c.curve([[8,22],[12,18],[16,22],[22,18]],{color:'blue',cls:'thin'}); }};
P.calendar = {w:44, h:44, dh:12, draw(c,o){ c.rect(3,6,38,36,{fill:'paper', fs:'solid'}); c.rect(3,6,38,10,{fill:'red', gap:5}); c.line(13,2,13,10,{cls:'bold'}); c.line(31,2,31,10,{cls:'bold'}); c.text(22,36,o.n!=null?String(o.n):'30',{size:o.size||17, color:'ink'}); if(o.label) c.text(22,14,o.label,{size:6,color:'paper'}); }};
P.clock = {w:44, h:44, dh:12, draw(c,o){ c.circle(22,22,40,{fill:'paper', fs:'solid'}); for(let i=0;i<12;i++){ const r=rad2(i*30); c.line(22+16*Math.cos(r),22+16*Math.sin(r),22+18.5*Math.cos(r),22+18.5*Math.sin(r),{cls:'thin'}); } const h=rad2((o.h||3)*30-90), m=rad2((o.m||0)*6-90); c.line(22,22,22+10*Math.cos(h),22+10*Math.sin(h),{cls:'bold'}); c.line(22,22,22+15*Math.cos(m),22+15*Math.sin(m)); c.dot(22,22,3); }};
P.shield = {w:40, h:46, dh:12, draw(c,o){ c.poly([[20,2],[37,8],[35,28],[20,44],[5,28],[3,8]],{fill:o.color||'blue', gap:8}); if(o.check!==false) c.poly([[12,22],[18,29],[29,14]],{open:true, color:o.markColor||'green', cls:'bold'}); }};
P.umbrella = {w:70, h:70, dh:18, draw(c,o){ c.arc(35,30,66,48,180,360,{closed:true, fill:o.color||'blue', gap:9}); c.line(35,30,35,64); c.arc(30,64,10,10,0,180); }};
P.phone = {w:26, h:44, dh:10, draw(c){ c.rrect(2,2,22,40,4,{fill:'ink', fs:'solid', cls:'soft'}); c.rect(5,7,16,26,{fill:'sky', gap:5}); c.dot(13,37.5,3); }};

const rad2 = d => d*Math.PI/180;
})();
