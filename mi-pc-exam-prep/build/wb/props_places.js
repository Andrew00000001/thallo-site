/* ---------- Sketch props: places, buildings, animals, farm and Michigan ----------
   Same conventions as props_core.js: {w, h, dh, anchors?, draw(c, opt, el)}; draw in the prop's own w x h box. */
(()=>{
const P = SK.PROPS;
const rad = d => d*Math.PI/180;
const TH = {cls:'thin'}, LT = {cls:'thin', rough:0.5};
// rectangle with a round top (x,y = top-left of its box), as polygon points
function arch(x, y, w, h, n){ const r=w/2, pts=[[x,y+h]]; n=n||8; for(let i=0;i<=n;i++){ const a=rad(180+180*i/n); pts.push([x+r+r*Math.cos(a), y+r+r*Math.sin(a)]); } pts.push([x+w,y+h]); return pts; }
function win(c, x, y, w, h, mull){ c.rect(x,y,w,h,{fill:'sky', gap:6, cls:'soft'}); if(mull!==false) c.line(x+w/2,y,x+w/2,y+h,TH); }

/* ===== Homes ===== */
// mobilehome: single-wide manufactured home on blocks. o.color: side stripe (default teal), o.wall: wall hatch color, o.roof, o.wheels: on wheels instead of blocks
P.mobilehome = {w:130, h:60, dh:16, anchors:{door:()=>[96,36], roof:()=>[65,10]},
  draw(c, o){
    const st=o.color||'teal';
    c.poly([[3,18.5],[12,10],[118,10],[127,18.5]],{fill:o.roof||'gray', gap:8});
    c.rect(7,18,116,30,{fill:o.wall||null, gap:13, cls:'soft'});
    c.rect(7,38,82,3.5,{color:st, fill:st, fs:'solid', rough:0.4}); c.rect(103,38,20,3.5,{color:st, fill:st, fs:'solid', rough:0.4});
    [13,37,61].forEach(x=>win(c,x,22,17,11)); win(c,107,22,11,11,false);
    c.rect(90,23,12,25,{fill:'brown', gap:6}); c.dot(99.5,36,2);
    c.rect(87,48,18,5,{}); c.rect(85,53,22,5,{});
    c.line(7,43,1,50,{cls:'bold'}); c.dot(1.5,50,3);
    if(o.wheels){ [42,58].forEach(x=>{ c.circle(x,51.5,13,{fill:'paper', fs:'solid'}); c.dot(x,51.5,3); }); }
    else [12,38,64,112].forEach(x=>c.rect(x,48,9,10,{fill:'gray', gap:4, cls:'soft'}));
  }};

// condo: row of attached townhouse units. o.n: units (default 3), o.roofs: roof colors, cycled (default red, brown, blue)
P.condo = {w:140, h:84, dh:26, anchors:{roof:()=>[70,12]},
  draw(c, o){
    const n=Math.max(2, Math.min(6, o.n||3)), uw=128/n, roofs=o.roofs||['red','brown','blue'];
    for(let i=0;i<n;i++){ const x=6+i*uw, m=x+uw/2; c.poly([[x-3,34],[m,12],[x+uw+3,34]],{fill:roofs[i%roofs.length], gap:10}); }
    c.rect(6,33,128,49,{});
    for(let i=1;i<n;i++) c.line(6+i*uw,33,6+i*uw,82);
    for(let i=0;i<n;i++){ const x=6+i*uw, m=x+uw/2, ww=Math.min(15, uw*0.38);
      win(c, m-ww/2, 39, ww, 11);
      const dw=Math.min(11, uw*0.26); c.rect(x+uw*0.62, 60, dw, 22, {fill:'brown', gap:6});
      win(c, x+uw*0.12, 62, Math.min(14, uw*0.36), 11);
    }
  }};

// garage: detached garage. o.open: door rolled up (dark inside), o.roof: roof color (default red)
P.garage = {w:80, h:70, dh:18, anchors:{door:()=>[40,52], roof:()=>[40,6]},
  draw(c, o){
    c.poly([[2,29],[40,6],[78,29]],{fill:o.roof||'red', gap:10});
    c.rect(8,28,64,40,{});
    c.circle(40,20,8,{fill:'paper', fs:'solid'}); c.line(36,20,44,20,TH);
    c.rect(16,36,48,32,{});
    if(o.open){ c.line(16,41,64,41,TH); c.poly([[16,44],[64,44],[64,68],[16,68]],{nostroke:true, fill:'ink', gap:4}); c.line(16,44,64,44); }
    else { for(let y=42.5;y<68;y+=6.4) c.line(16,y,64,y,TH); c.rect(36,58.5,8,2.5,{fill:'ink', fs:'solid', rough:0.3}); }
  }};

/* ===== Farm ===== */
// barn: farm barn with gambrel roof, hayloft and X doors. o.color: wall color (default red)
P.barn = {w:90, h:86, dh:24, anchors:{door:()=>[45,70], roof:()=>[45,4]},
  draw(c, o){
    const col=o.color||'red';
    c.poly([[10,84],[10,40],[18,20],[45,7],[72,20],[80,40],[80,84]],{fill:col, gap:9});
    c.poly([[3,43],[14,18],[45,3],[76,18],[87,43]],{open:true, cls:'bold'});
    c.rect(37,22,16,14,{fill:'paper', fs:'solid'}); c.line(37,22,53,36,TH); c.line(53,22,37,36,TH);
    c.rect(26,50,38,34,{fill:'paper', fs:'solid'}); c.line(45,50,45,84);
    c.line(26,50,45,84,TH); c.line(45,50,26,84,TH); c.line(45,50,64,84,TH); c.line(64,50,45,84,TH);
    c.rect(14,52,8,8,{fill:'paper', fs:'solid'}); c.rect(68,52,8,8,{fill:'paper', fs:'solid'});
  }};

// crops: a row of crops on a strip of soil. o.type: 'corn' (default) | 'wheat', o.n: stalks (default 6), o.damaged: snapped, flattened and browned (hail, wind, drought)
P.crops = {w:120, h:56, dh:13,
  draw(c, o){
    const n=o.n||6, sp=112/n, wheat=o.type==='wheat';
    const dead={color:'brown', fill:'brown', fs:'solid'};
    for(let i=0;i<n;i++){ const x=4+sp*(i+0.5), s=i%2?1:-1;
      if(o.damaged){ const v=i%3, head=(hx,hy)=>c.blob([[hx,hy],[hx+2.5,hy+4],[hx+2,hy+9],[hx-0.5,hy+5]],{fill:'yellow', gap:3});
        const leaf=(lx,ly,d)=>c.blob([[lx,ly],[lx+5*d,ly+3],[lx+7*d,ly+9],[lx+3*d,ly+5]],dead);
        if(v===0){ c.line(x,48,x,33); c.poly([[x-1.6,33.5],[x-0.6,31],[x+0.4,33.5],[x+1.6,31.5]],{open:true, rough:0.4});
          c.line(x+2,47,x+16,43.5); if(wheat) head(x+16,40); else { leaf(x,38,1); c.ellipse(x+8,45.6,8,3.2,{fill:'yellow', fs:'solid', color:'orange', rough:0.4}); } }
        else if(v===1){ c.poly([[x,48],[x+1,22],[x+9,17],[x+13,27]],{open:true});
          if(wheat) head(x+13,27); else { leaf(x+0.5,34,-1); leaf(x+11,22,1); } }
        else { c.poly([[x,48],[x,20],[x-8,32]],{open:true});
          if(wheat) head(x-8,32); else { leaf(x,38,1); leaf(x-5,25,-1); } }
        continue;
      }
      if(wheat){
        c.curve([[x,48],[x+1,30],[x+2,16]]);
        c.blob([[x+2,2],[x+5,8],[x+5,16],[x+2,19],[x-1,16],[x-1,8]],{fill:'yellow', gap:3, color:'ink'});
        for(let k=0;k<3;k++){ c.line(x+2,6+k*4,x+6,4+k*4,LT); c.line(x+2,6+k*4,x-2,4+k*4,LT); }
        c.curve([[x+1,34],[x+6,30],[x+9,31]],TH);
      } else {
        c.line(x,48,x,6);
        c.blob([[x,40],[x-7*s,32],[x-13*s,32],[x-7*s,35]],{fill:'green', fs:'solid', color:'green'});
        c.blob([[x,30],[x+7*s,22],[x+12*s,22],[x+6*s,26]],{fill:'green', fs:'solid', color:'green'});
        c.blob([[x,18],[x-6*s,11],[x-10*s,12],[x-5*s,15]],{fill:'green', fs:'solid', color:'green'});
        c.ellipse(x-3.5*s,27,5,12,{fill:'yellow', fs:'solid', color:'orange', rough:0.5});
        c.line(x,6,x-3,1,LT); c.line(x,6,x+3,1,LT); c.line(x,6,x,1,LT);
      }
    }
    c.poly([[0,48],[120,48],[120,54],[0,54]],{nostroke:true, fill:'brown', gap:5});
    c.curve([[0,48],[30,47],[60,48.5],[90,47],[120,48]]);
  }};

// tractor: farm tractor facing right (big rear wheel). o.color: body (default green)
P.tractor = {w:116, h:84, dh:18, anchors:{front:()=>[110,56], roof:()=>[40,6]},
  draw(c, o){
    const col=o.color||'green';
    c.rect(81,18,4,22,{fill:'gray', fs:'solid'}); c.curve([[83,16],[86,11],[82,7],[87,3]],{color:'gray', cls:'thin'});
    c.poly([[46,38],[100,38],[108,44],[108,62],[46,62]],{fill:col, gap:8});
    for(let x=101;x<108;x+=3) c.line(x,46,x,60,TH);
    c.rect(18,6,42,5,{fill:col, gap:4});
    c.line(23,11,23,38); c.line(56,11,56,38);
    c.rect(26,14,27,20,{fill:'sky', gap:6, cls:'soft'});
    c.poly([[8,48],[14,36],[58,36],[62,48]],{fill:col, gap:6});
    c.circle(34,58,48,{fill:'paper', fs:'solid'}); c.circle(34,58,40,{cls:'thin'});
    for(let a=0;a<360;a+=30){ const r=rad(a); c.line(34+20*Math.cos(r),58+20*Math.sin(r),34+24*Math.cos(r),58+24*Math.sin(r),LT); }
    c.circle(34,58,17,{fill:'yellow', gap:4}); c.dot(34,58,4);
    c.circle(94,69,28,{fill:'paper', fs:'solid'}); c.circle(94,69,11,{fill:'yellow', gap:4}); c.dot(94,69,3);
  }};

/* ===== Town ===== */
// warehouse: long low warehouse with roll-up loading doors. o.name: sign text on the wall, o.n: loading doors (default 3), o.roof
P.warehouse = {w:140, h:70, dh:22,
  draw(c, o){
    const n=Math.max(1, Math.min(4, o.n||3)), dw=24, span=96, sp=n>1?(span-dw)/(n-1):0;
    c.poly([[2,22],[12,10],[128,10],[138,22]],{fill:o.roof||'gray', gap:9});
    c.rect(6,21,128,47,{});
    if(o.name) c.text(62,33,o.name,{size:8});
    else for(let x=16;x<104;x+=16) c.rect(x,25,10,5,{fill:'sky', gap:4, cls:'soft'});
    for(let i=0;i<n;i++){ const x=n>1?12+i*sp:48; c.rect(x,38,dw,30,{}); for(let y=42.5;y<68;y+=4.6) c.line(x,y,x+dw,y,TH); }
    c.rect(114,46,11,22,{fill:'brown', gap:6}); c.dot(122.5,57,1.8);
    c.rect(110,38,6,4,{fill:'yellow', fs:'solid', rough:0.4});
  }};

// hospital: hospital with a red-cross sign tower and an entrance canopy. o.name: optional word on the canopy
P.hospital = {w:110, h:96, dh:30, anchors:{top:()=>[55,4], door:()=>[55,86]},
  draw(c, o){
    c.rect(37,3,36,28,{fill:'paper', fs:'solid'});
    c.poly([[51,7],[59,7],[59,13],[65,13],[65,21],[59,21],[59,27],[51,27],[51,21],[45,21],[45,13],[51,13]],{color:'red', fill:'red', fs:'solid', rough:0.4});
    c.rect(6,31,98,63,{});
    [36,52].forEach(y=>[12,28,49,70,86].forEach(x=>c.rect(x,y,12,10,{fill:'sky', gap:5, cls:'soft'})));
    [12,28,70,86].forEach(x=>c.rect(x,75,12,10,{fill:'sky', gap:5, cls:'soft'}));
    c.rect(44,73,22,21,{fill:'sky', gap:6, cls:'soft'}); c.line(55,73,55,94,TH);
    c.rect(38,66,34,6,{fill:'red', gap:4});
    if(o.name) c.text(55,71.2,o.name,{size:5});
  }};

// courthouse: courthouse with pediment (scales of justice), six columns and wide steps. o.name (default "COURT")
P.courthouse = {w:120, h:100, dh:32, anchors:{top:()=>[60,5]},
  draw(c, o){
    c.poly([[6,33],[60,5],[114,33]],{fill:'gray', gap:9, cls:'soft'});
    c.line(60,13,60,29,LT); c.line(50,16,70,16,LT);
    [50,70].forEach(x=>{ c.line(x,16,x-4,23,LT); c.line(x,16,x+4,23,LT); c.arc(x,23,9,6,0,180,{closed:true, fill:'yellow', fs:'solid', rough:0.4}); });
    c.rect(10,33,100,10,{}); c.text(60,41.2,o.name||'COURT',{size:8.5});
    for(let i=0;i<6;i++){ const x=15+i*16.6; c.rect(x,43,7,37,{}); c.line(x-1.5,45,x+8.5,45,LT); }
    c.rect(56.5,62,8,18,{fill:'brown', gap:5});
    c.rect(8,80,104,6,{fill:'gray', gap:6, cls:'soft'}); c.rect(4,86,112,6,{fill:'gray', gap:6, cls:'soft'}); c.rect(0,92,120,6,{fill:'gray', gap:6, cls:'soft'});
  }};

// bank: classic bank with green pediment, $ coin, columns and "BANK". o.name (default "BANK")
P.bank = {w:100, h:96, dh:30, anchors:{top:()=>[50,6]},
  draw(c, o){
    c.poly([[4,32],[50,6],[96,32]],{fill:'green', gap:9});
    c.circle(50,22,14,{fill:'paper', fs:'solid', color:'green'}); c.text(50,26.5,'$',{size:11, color:'green'});
    c.rect(8,32,84,10,{}); c.text(50,40.4,o.name||'BANK',{size:8.5});
    [14,35,56,77].forEach(x=>c.rect(x,42,9,40,{}));
    c.rect(45,62,10,20,{fill:'brown', gap:5});
    c.rect(6,82,88,6,{fill:'gray', gap:6}); c.rect(2,88,96,6,{fill:'gray', gap:6});
  }};

// school: school with bell tower, clock, flag and "SCHOOL" over the doors. o.name (default "SCHOOL")
P.school = {w:130, h:100, dh:30, anchors:{top:()=>[65,2], door:()=>[65,88]},
  draw(c, o){
    c.line(16,46,16,16,TH); c.poly([[16,16],[31,18],[31,27],[16,25]],{fill:'red', gap:4});
    c.rect(4,44,122,5,{fill:'gray', gap:5});
    c.rect(6,49,118,49,{});
    [11,27,93,109].forEach(x=>{ win(c,x,55,12,11); win(c,x,75,12,11); });
    c.rect(59,6,12,13,{}); c.arc(65,15,7,8,180,360,{fill:'yellow', fs:'solid', closed:true, rough:0.4});
    c.poly([[55,8],[65,0],[75,8]],{fill:'red', gap:5});
    c.rect(44,32,42,66,{fill:'paper', fs:'solid'});
    c.poly([[40,34],[65,16],[90,34]],{fill:'red', gap:9});
    c.circle(65,27.5,8,{fill:'paper', fs:'solid'}); c.line(65,27.5,65,25,LT); c.line(65,27.5,67,28,LT);
    c.text(65,46,o.name||'SCHOOL',{size:7});
    win(c,49,52,10,10,false); win(c,71,52,10,10,false);
    c.rect(55,72,20,26,{fill:'brown', gap:6}); c.line(65,72,65,98,TH);
  }};

// church: church with steeple and cross, rose window, arched door and pointed windows. o.roof (default red)
P.church = {w:80, h:110, dh:34, anchors:{top:()=>[40,1], door:()=>[40,98]},
  draw(c, o){
    c.poly([[6,64],[40,44],[74,64]],{fill:o.roof||'red', gap:9});
    c.rect(12,63,56,45,{});
    c.rect(31,32,18,32,{fill:'paper', fs:'solid'});
    c.poly(arch(36,38,8,12),{});
    c.poly([[29,33],[40,12],[51,33]],{fill:'gray', gap:6});
    c.line(40,1,40,13,{cls:'bold'}); c.line(35.5,5,44.5,5,{cls:'bold'});
    c.circle(40,73,11,{fill:'sky', gap:5, cls:'soft'}); c.line(40,68,40,78,LT); c.line(35,73,45,73,LT);
    c.poly(arch(33,86,14,22),{fill:'brown', gap:6});
    [17,56].forEach(x=>c.poly([[x,90],[x,78],[x+3.5,73],[x+7,78],[x+7,90]],{fill:'sky', gap:5, cls:'soft'}));
  }};

// restaurant: restaurant with a name sign, scalloped awning and a plate-fork-knife window. o.name (default "DINER", e.g. "TONY'S PIZZA"), o.awning color (default red), o.signColor
P.restaurant = {w:120, h:94, dh:30, anchors:{door:()=>[92,80], sign:()=>[60,6]},
  draw(c, o){
    const name=o.name||'DINER', sz=Math.min(11, 102/Math.max(1, SK.tw(name,1))), col=o.awning||'red';
    c.rect(8,24,104,68,{});
    c.rect(4,5,112,19,{fill:'paper', fs:'solid'}); c.text(60,14.5+sz*0.36,name,{size:sz, color:o.signColor||'red'});
    for(let i=0;i<8;i++){ const x=8+i*13, pts=[[x,25],[x+13,25],[x+13,33]];
      for(let k=1;k<6;k++){ const a=rad(180*k/6); pts.push([x+6.5+6.5*Math.cos(a), 33+4.5*Math.sin(a)]); }
      pts.push([x,33]); c.poly(pts,{fill:i%2?'paper':col, fs:i%2?'solid':'hachure', gap:5, rough:0.6}); }
    c.rect(14,46,54,32,{fill:'sky', gap:9, cls:'soft'});
    c.circle(41,62,15,{fill:'paper', fs:'solid'}); c.circle(41,62,9,LT);
    c.line(28,52,28,73); c.line(25.5,52,25.5,57,LT); c.line(30.5,52,30.5,57,LT); c.curve([[25.5,57],[28,60],[30.5,57]],LT);
    c.poly([[53,52],[56,53],[56,63],[53,63]],{fill:'paper', fs:'solid', rough:0.5}); c.line(54.5,63,54.5,73);
    c.rect(80,46,22,46,{fill:'brown', gap:7}); c.dot(97,70,2);
    c.rect(83,50,16,8,{fill:'paper', fs:'solid'}); c.text(91,56.6,'OPEN',{size:5, color:'green'});
  }};

// gasstation: gas station with canopy, two pumps and a price sign. o.price (default "3.49"), o.color: canopy band (default red)
P.gasstation = {w:130, h:80, dh:24, anchors:{top:()=>[78,6]},
  draw(c, o){
    const col=o.color||'red';
    c.line(14,40,14,78,{cls:'bold'}); c.rect(3,12,22,28,{fill:'paper', fs:'solid'});
    c.text(14,22,'GAS',{size:7.5, color:col}); c.text(14,34,o.price||'3.49',{size:7});
    c.rect(30,4,98,4,{fill:'gray', gap:4}); c.rect(30,8,98,11,{fill:col, gap:6});
    c.rect(42,19,5,59,{}); c.rect(111,19,5,59,{});
    c.rect(54,72,50,6,{fill:'gray', gap:5});
    [58,86].forEach(x=>{ c.rrect(x,40,14,32,2,{fill:'paper', fs:'solid'}); c.rect(x+3,44,8,6,{fill:'sky', gap:3}); c.rect(x,56,14,4,{color:col, fill:col, fs:'solid', rough:0.4});
      c.curve([[x+14,48],[x+19,54],[x+18,64]],TH); c.rect(x+16.5,62,3,6,{fill:'ink', fs:'solid', rough:0.3}); });
  }};

// construction: building going up: steel frame, scaffolding with planks, traffic cone. o.crane: tower crane lowering a beam
P.construction = {w:110, h:100, dh:30,
  draw(c, o){
    const B={cls:'bold'};
    if(o.crane){
      c.rect(100,6,6,92,{fill:'yellow', gap:4}); for(let y=6;y<98;y+=8) c.line(100,y,106,y+8,LT);
      c.rect(30,3,80,5,{fill:'yellow', gap:4}); for(let x=30;x<110;x+=8) c.line(x,8,x+4,3,LT);
      c.rect(102,8,8,6,{fill:'gray', fs:'solid'});
      c.line(80,8,80,33,LT); c.line(80,33,70,38,LT); c.line(80,33,90,38,LT);
      c.rect(68,38,24,4,{fill:'orange', fs:'solid'});
    }
    // scaffolding
    c.line(4,98,4,34,TH); c.line(18,98,18,34,TH);
    [78,58,38].forEach(y=>{ c.line(4,y+20,18,y,LT); c.rect(1,y-1,20,2.5,{fill:'brown', fs:'solid', color:'brown', rough:0.4}); });
    // steel frame
    c.line(24,98,24,18,B); c.line(46,98,46,18,B); c.line(68,98,68,18,B); c.line(90,98,90,58,B);
    c.line(24,78,90,78,B); c.line(24,58,90,58,B); c.line(24,38,68,38,B); c.line(24,18,68,18,B);
    c.line(24,98,46,78,LT); c.line(46,78,68,98,LT); c.line(46,58,68,38,LT); c.line(68,78,90,58,LT); c.line(24,38,46,18,LT);
    c.rect(22,96,70,3,{fill:'gray', fs:'solid'});
    if(!o.crane){ c.poly([[96,98],[100,84],[104,98]],{fill:'orange', fs:'solid'}); c.line(98,92,102,92,{color:'paper', cls:'bold'}); c.line(93,98,107,98); }
  }};

// crane: tower crane. o.load: 'beam' (default) | 'box' | 'none', o.color (default yellow)
P.crane = {w:100, h:110, dh:36, anchors:{hook:()=>[22,62]},
  draw(c, o){
    const col=o.color||'yellow', ld=o.load||'beam';
    c.line(73,2,6,13,LT); c.line(73,2,96,13,LT);
    c.poly([[68,13],[73,2],[78,13]],{open:true});
    c.rect(4,13,92,6,{fill:col, gap:5});
    for(let x=4;x<96;x+=8){ c.line(x,19,x+4,13,LT); c.line(x+4,13,x+8,19,LT); }
    c.rect(84,19,12,9,{fill:'gray', gap:4});
    c.rect(58,19,10,9,{fill:'sky', gap:4, cls:'soft'});
    c.rect(68,19,10,83,{fill:col, gap:6});
    for(let y=19;y<101;y+=10){ c.line(68,y,78,Math.min(102,y+10),LT); c.line(68,y,78,y,LT); }
    c.rect(60,102,26,6,{fill:'gray', gap:5});
    c.rect(18,19,8,3.5,{fill:'ink', fs:'solid', rough:0.3}); c.line(22,22,22,57,LT);
    c.curve([[22,57],[22,61],[20,63],[18,61]],{cls:'bold'});
    if(ld==='beam'){ c.line(21,60,8,68,LT); c.line(21,60,36,68,LT); c.rect(4,68,36,5,{fill:'orange', gap:4}); }
    else if(ld==='box'){ c.line(21,60,12,68,LT); c.line(21,60,32,68,LT); c.rect(10,68,24,18,{fill:'brown', gap:6}); c.line(10,77,34,77,TH); }
  }};

/* ===== Roads ===== */
// road: two-lane road strip, long and flat. o.center: 'dash' (default) | 'double' | 'none', o.pothole: a pothole in the near lane, o.crack
P.road = {w:240, h:24, dh:7,
  draw(c, o){
    c.poly([[0,2],[240,2],[240,22],[0,22]],{nostroke:true, fill:'gray', gap:8, cls:'soft'});
    c.line(0,2,240,2,{rough:0.6}); c.line(0,22,240,22,{rough:0.6});
    const ctr=o.center||'dash';
    if(ctr==='dash') for(let x=6;x<240;x+=26) c.rect(x,11,13,2,{color:'yellow', fill:'yellow', fs:'solid', rough:0.3});
    else if(ctr==='double'){ c.line(0,10.6,240,10.6,{color:'yellow', rough:0.4}); c.line(0,13.2,240,13.2,{color:'yellow', rough:0.4}); }
    if(o.pothole){ c.ellipse(156,17.5,22,5,{fill:'ink', gap:3}); c.line(146,16,140,14,LT); c.line(166,16,172,13.5,LT); }
    if(o.crack) c.poly([[60,4],[64,8],[61,12],[66,16],[63,20]],{open:true, cls:'thin'});
  }};

// bridge: suspension bridge over water (two towers, cables, hangers). o.color: towers (default red), o.water:false hides the water, o.broken: deck snapped in the middle
P.bridge = {w:160, h:64, dh:18,
  draw(c, o){
    const col=o.color||'red';
    const cy = x => x<=40 ? 34-28*(x/40)+5*(x/40)*(1-x/40) : x>=120 ? 34-28*((160-x)/40)+5*((160-x)/40)*(1-(160-x)/40) : 6+22*(1-((x-80)/40)**2);
    if(o.water!==false){ for(let r=0;r<2;r++){ const y=52+r*6, pts=[]; for(let x=0;x<=160;x+=10) pts.push([x, y+(x/10%2?2.5:-1)]); c.curve(pts,{color:'blue'}); } }
    [36,116].forEach(x=>{ c.rect(x,4,8,52,{fill:col, gap:5}); c.line(x,14,x+8,14,TH); c.line(x,26,x+8,26,TH); });
    const pts=[]; for(let x=0;x<=160;x+=5) pts.push([x, cy(x)<6?6:cy(x)]); c.curve(pts.map(p=>[p[0], p[1]]),{});
    for(let x=8;x<160;x+=8){ if(Math.abs(x-40)<5 || Math.abs(x-120)<5) continue; const y=cy(x); if(y<33) c.line(x,y,x,34,LT); }
    if(o.broken){ c.poly([[0,34],[74,34],[78,44],[0,40]],{fill:'gray', gap:5}); c.poly([[86,46],[90,34],[160,34],[160,40]],{fill:'gray', gap:5}); }
    else { c.poly([[0,34],[160,34],[160,40],[0,40]],{fill:'gray', gap:5}); }
  }};

/* ===== Animals ===== */
// dog: side view dog facing right. o.mood: 'happy' (default, tongue out, wagging) | 'angry' (bares teeth, hackles up), o.color: fur (default brown)
P.dog = {w:86, h:60, dh:12, anchors:{head:()=>[66,6], face:()=>[72,22]},
  draw(c, o){
    const col=o.color||'brown', angry=o.mood==='angry';
    if(angry) c.curve([[15,30],[9,24],[8,15]],{cls:'bold'});
    else { c.curve([[15,30],[7,25],[5,15],[9,10]],{cls:'bold'}); c.curve([[2,9],[1,14]],LT); c.curve([[12,6],[15,8]],LT); }
    [[18,40],[27,41],[47,41],[56,40]].forEach(([x,y])=>{ c.rect(x,y,6,15,{fill:col, gap:5}); c.ellipse(x+4,56,9,4,{fill:'paper', fs:'solid', rough:0.5}); });
    c.blob([[14,28],[24,23],[44,23],[58,25],[63,33],[58,42],[40,44],[20,44],[12,38]],{fill:col, gap:8});
    if(angry) c.poly([[24,25],[27,18],[30,24],[33,17],[36,23],[39,16],[42,23],[45,17],[48,24]],{open:true});
    c.circle(64,20,22,{fill:'paper', fs:'solid'}); c.circle(64,20,22,{nostroke:true, fill:col, gap:6, cls:'soft'});
    c.blob([[70,20],[80,19],[84,24],[80,30],[70,30]],{fill:'paper', fs:'solid'});
    c.dot(83,21.5,4.5);
    c.blob([[57,11],[63,9],[61,25],[55,23]],{fill:col, gap:3});
    c.line(53,26,58,33,{color:'red', cls:'bold'});
    if(angry){
      c.dot(67,16,3); c.line(62,11,70,15,{cls:'bold'});
      c.poly([[68,26],[82,25],[80,32],[70,32]],{fill:'paper', fs:'solid'});
      c.poly([[69,26],[71,29],[73,26],[75,29],[77,26],[79,29],[81,25.5]],{open:true, cls:'thin'});
      c.poly([[70,32],[72,29.5],[74,32],[76,29.5],[78,32],[80,30]],{open:true, cls:'thin'});
    } else {
      c.dot(67,16,3); c.arc(76,27,10,5,20,160);
      c.blob([[75,29],[79,29],[79,34],[77,36],[75,34]],{color:'red', fill:'pink', fs:'solid'});
    }
  }};

// cat: sitting cat, front view. o.color: fur (default orange), o.mood: 'angry' (hissing, ears back)
P.cat = {w:50, h:64, dh:12, anchors:{head:()=>[25,4], face:()=>[25,20]},
  draw(c, o){
    const col=o.color||'orange', angry=o.mood==='angry';
    c.curve([[38,58],[46,52],[47,40],[42,32]],{cls:'bold'});
    c.blob([[25,28],[36,34],[41,48],[39,60],[25,62],[11,60],[9,48],[14,34]],{fill:col, gap:8});
    c.ellipse(19,61,9,4.5,{fill:'paper', fs:'solid', rough:0.5}); c.ellipse(31,61,9,4.5,{fill:'paper', fs:'solid', rough:0.5});
    if(angry){ c.poly([[12,15],[5,6],[19,10]],{fill:col, gap:4}); c.poly([[31,10],[45,6],[38,15]],{fill:col, gap:4}); }
    else { c.poly([[13,14],[12,1],[22,9]],{fill:col, gap:4}); c.poly([[28,9],[38,1],[37,14]],{fill:col, gap:4}); }
    c.ellipse(25,19,28,24,{fill:'paper', fs:'solid'}); c.ellipse(25,19,28,24,{nostroke:true, fill:col, gap:7, cls:'soft'});
    if(angry){ c.line(16,14,22,17,{cls:'bold'}); c.line(34,14,28,17,{cls:'bold'}); c.dot(19.5,18,2.6); c.dot(30.5,18,2.6);
      c.arc(25,26,10,7,180,360,{closed:true, fill:'paper', fs:'solid'}); c.line(22,23,22.6,25.5,LT); c.line(28,23,27.4,25.5,LT); }
    else { c.ellipse(19.5,17.5,3.4,4.6,{fill:'ink', fs:'solid', rough:0.3}); c.ellipse(30.5,17.5,3.4,4.6,{fill:'ink', fs:'solid', rough:0.3});
      c.arc(23,24,4,3.2,0,180,LT); c.arc(27,24,4,3.2,0,180,LT); }
    c.poly([[23.3,21.4],[26.7,21.4],[25,23.4]],{color:'pink', fill:'pink', fs:'solid', rough:0.3});
    c.line(19,23,6,21,LT); c.line(19,25,6,27,LT); c.line(31,23,44,21,LT); c.line(31,25,44,27,LT);
  }};

// deer: Michigan whitetail, side view facing right. o.antlers:false = doe, o.pose: 'stand' (default) | 'leap' (jumping, e.g. into a car's path)
P.deer = {w:94, h:92, dh:19, anchors:{head:o=>o.antlers===false?[70,13]:[76,1], face:()=>[82,30]},
  draw(c, o){
    const col='brown', B={cls:'bold'};
    const legs = o.pose==='leap'
      ? [[[28,58],[16,68],[3,74]],[[35,60],[23,72],[10,81]],[[62,60],[75,64],[71,73]],[[68,58],[81,60],[79,69]]]
      : [[[28,59],[24,72],[28,89]],[[36,61],[34,74],[37,89]],[[60,61],[60,75],[60,89]],[[66,59],[68,74],[67,89]]];
    legs.forEach(l=>{ c.poly(l,{open:true, cls:'bold'}); const e=l[2]; c.rect(e[0]-1.8,e[1]-1.2,3.6,2.8,{fill:'ink', fs:'solid', rough:0.3}); });
    c.blob([[20,44],[12,35],[15,32],[25,40]],{fill:'paper', fs:'solid'});
    c.blob([[20,44],[32,39],[52,38],[59,36],[63,28],[68,22],[76,25],[76,38],[75,50],[72,57],[64,62],[40,62],[26,60],[18,53]],{fill:col, gap:8});
    c.blob([[64,24],[71,20],[79,22],[89,29],[90,33],[86,35],[75,32],[67,29]],{fill:col, gap:6});
    c.blob([[66,23],[55,14],[61,12],[71,19]],{fill:col, gap:4});
    c.blob([[83,33],[88,34],[85,36]],{fill:'paper', fs:'solid', rough:0.3});
    c.dot(75,26,3); c.dot(89.3,31,3.4);
    if(o.antlers!==false){
      c.curve([[73,20],[70,13],[73,7],[80,4],[90,5]],B);
      c.line(71,14,65,7,B); c.line(73.5,8,72,1,B); c.line(79,4.6,80,0,B); c.line(85,4.4,88,0.5,B);
      c.curve([[76,21],[78,16],[83,13]],TH); c.line(78.5,15.5,76.5,10,TH);
    }
  }};

// cow: Holstein dairy cow, side view facing right. o.spots: spot color (default ink)
P.cow = {w:96, h:66, dh:14, anchors:{head:()=>[84,8], face:()=>[86,26]},
  draw(c, o){
    const sp=o.spots||'ink';
    c.curve([[15,22],[9,30],[8,46]]); c.blob([[8,45],[11,49],[8,54],[5,49]],{fill:'ink', fs:'solid'});
    [[20,46],[28,46],[60,46],[68,46]].forEach(([x,y])=>{ c.rect(x,y,6,15,{}); c.rect(x,61,6,3,{fill:'ink', fs:'solid', rough:0.3}); });
    c.rrect(14,18,62,30,10,{fill:'paper', fs:'solid'});
    c.blob([[24,19],[34,20],[37,28],[30,33],[22,29]],{color:sp, fill:sp, gap:3});
    c.blob([[48,27],[58,25],[62,33],[54,40],[46,36]],{color:sp, fill:sp, gap:3});
    c.blob([[66,19],[74,22],[72,30],[66,27]],{color:sp, fill:sp, gap:3});
    c.blob([[44,48],[56,48],[55,54],[45,54]],{color:'pink', fill:'pink', fs:'solid'});
    c.curve([[78,13],[76,8],[78,4]],{cls:'bold'}); c.curve([[86,13],[88,8],[87,4]],{cls:'bold'});
    c.poly([[75,17],[66,13],[70,21]],{fill:sp, gap:3});
    c.blob([[74,14],[88,13],[93,26],[92,36],[80,37],[74,26]],{fill:'paper', fs:'solid'});
    c.blob([[78,15],[86,14],[84,22],[79,22]],{color:sp, fill:sp, gap:3});
    c.ellipse(87,33,14,9,{fill:'pink', fs:'solid', color:'pink'}); c.ellipse(87,33,14,9,{});
    c.dot(85,33,2); c.dot(90,33,2); c.dot(82,23,3);
  }};

// horse: horse, side view facing right, with mane and tail. o.color: coat (default brown)
P.horse = {w:100, h:88, dh:19, anchors:{head:()=>[80,3], face:()=>[90,26]},
  draw(c, o){
    const col=o.color||'brown';
    c.blob([[19,42],[10,48],[7,62],[10,76],[14,64],[19,52]],{fill:'ink', gap:3});
    [[[27,56],[24,70],[27,84]],[[35,57],[35,84]],[[62,57],[62,84]],[[69,55],[71,70],[69,84]]].forEach(l=>{ c.poly(l,{open:true, cls:'bold'}); const e=l[l.length-1]; c.rect(e[0]-2.8,e[1]-0.5,5.6,3.5,{fill:'ink', fs:'solid', rough:0.3}); });
    c.blob([[20,41],[34,37],[58,37],[64,33],[70,23],[77,13],[86,22],[82,34],[78,45],[76,52],[67,58],[34,58],[22,56],[16,48]],{fill:col, gap:8});
    c.blob([[76,14],[82,9],[88,12],[97,28],[95,33],[89,34],[84,26]],{fill:col, gap:6});
    c.poly([[77,11.5],[77,2],[82,9]],{fill:col, gap:3});
    c.blob([[76,10],[70,16],[65,26],[60,36],[64,37],[69,27],[74,18],[80,12]],{fill:'ink', gap:2.5});
    c.dot(83,17,3.2); c.dot(93.5,29.5,2.6);
  }};

// bird: small songbird, side view facing right. o.color: body (default blue), o.breast: breast color (e.g. 'orange' for a Michigan robin), o.fly: wings up in flight
P.bird = {w:44, h:32, dh:6, anchors:{head:()=>[32,2]},
  draw(c, o){
    const col=o.color||'blue';
    c.poly([[11,16],[1,9],[2,15],[11,22]],{fill:col, gap:3.5});
    if(!o.fly){ c.line(20,26,19,31,LT); c.line(26,26,27,31,LT); c.line(16.5,31,21,31,LT); c.line(25,31,29.5,31,LT); }
    c.blob([[8,18],[16,12],[25,11],[28,5],[33,3],[38,6],[39,11],[36,18],[30,24],[22,27],[13,25]],{fill:col, gap:5});
    if(o.breast) c.blob([[37.5,12],[35.5,19],[29,24.5],[31,17]],{color:o.breast, fill:o.breast, fs:'solid'});
    c.poly([[38.6,7],[44,9.6],[38.6,12]],{color:'orange', fill:'orange', fs:'solid', rough:0.4});
    c.dot(33.5,7.6,2.6);
    if(o.fly) c.poly([[14,15],[9,0],[19,5],[26,13]],{fill:col, gap:3.5});
    else { c.curve([[12,16],[19,14],[27,17],[22,21],[15,21]],{}); c.line(16,18,22,18.5,LT); }
  }};

// mouse: gray mouse (rodent), side view facing right, long tail
P.mouse = {w:64, h:32, dh:7, anchors:{head:()=>[44,4]},
  draw(c, o){
    c.curve([[13,25],[5,24],[2,16],[7,9],[11,10]],{});
    c.line(30,27,28,30,LT); c.line(46,26,47,30,LT);
    c.blob([[12,25],[15,15],[28,8],[42,10],[54,17],[60,21],[54,25],[30,28]],{fill:'gray', gap:6});
    c.circle(42,10,12,{fill:'paper', fs:'solid'}); c.circle(42,10,7,{nostroke:true, fill:'pink', fs:'solid', cls:'soft'});
    c.dot(51,16,2.6); c.dot(60.5,21,3,{color:'pink'});
    c.line(57,20,64,17,LT); c.line(57,21.5,64,22,LT); c.line(57,23,63,26,LT);
  }};

// bug: insect (termite / ant), top view facing right. o.wings: termite swarmer wings, o.color: body (default brown)
P.bug = {w:56, h:40, dh:7,
  draw(c, o){
    const col=o.color||'brown';
    [[26,16,20,8,14,5],[31,15.5,31,5,27,2],[35,16,41,8,46,5]].forEach(([a,b,d,e,f,g])=>{ c.poly([[a,b],[d,e],[f,g]],{open:true, rough:0.6}); c.poly([[a,40-b],[d,40-e],[f,40-g]],{open:true, rough:0.6}); });
    c.curve([[45,17],[50,12],[55,11]],TH); c.curve([[45,23],[50,28],[55,29]],TH);
    c.ellipse(15,20,24,15,{fill:col, gap:4}); [10,15,20].forEach(x=>c.curve([[x,13.6],[x-1,20],[x,26.4]],LT));
    c.ellipse(31,20,10,9,{fill:col, gap:4});
    c.ellipse(41,20,11,10,{fill:col, gap:4});
    c.dot(44,17.5,2); c.dot(44,22.5,2);
    if(o.wings){ c.blob([[30,18],[16,10],[2,11],[4,16],[18,18]],{fill:'sky', gap:3, cls:'soft'}); c.blob([[30,22],[16,30],[2,29],[4,24],[18,22]],{fill:'sky', gap:3, cls:'soft'}); }
  }};

/* ===== Michigan and water ===== */
const MI_LP=[[-86.82,41.76],[-84.81,41.70],[-83.45,41.73],[-83.17,42.05],[-83.10,42.30],[-82.87,42.45],[-82.80,42.60],[-82.50,42.62],[-82.42,43.00],[-82.52,43.50],[-82.62,43.85],[-82.62,44.07],
  [-83.00,44.05],[-83.32,43.92],[-83.60,43.72],[-83.90,43.62],[-83.95,43.85],[-83.70,44.02],[-83.45,44.25],[-83.33,44.45],[-83.32,44.85],[-83.43,45.05],[-83.38,45.30],[-83.80,45.42],[-84.20,45.60],
  [-84.47,45.65],[-84.73,45.78],[-85.10,45.76],[-85.00,45.45],[-84.95,45.38],[-85.27,45.30],[-85.42,44.90],[-85.60,44.76],[-85.62,45.10],[-85.62,45.21],[-85.78,45.00],[-86.05,44.90],[-86.24,44.62],
  [-86.32,44.25],[-86.46,43.95],[-86.54,43.65],[-86.40,43.30],[-86.23,43.05],[-86.21,42.77],[-86.28,42.42],[-86.48,42.12]];
const MI_UP=[[-83.90,46.00],[-84.10,46.25],[-84.35,46.50],[-84.60,46.45],[-84.95,46.48],[-84.96,46.77],[-85.45,46.73],[-85.98,46.67],[-86.65,46.42],[-87.10,46.50],[-87.40,46.55],[-87.73,46.85],
  [-88.10,46.88],[-88.40,46.78],[-88.30,47.00],[-88.00,47.20],[-87.70,47.42],[-87.95,47.47],[-88.20,47.45],[-88.55,47.25],[-88.65,47.10],[-89.00,46.95],[-89.40,46.85],[-89.80,46.78],[-90.42,46.57],
  [-90.12,46.34],[-89.40,46.20],[-88.70,46.00],[-88.10,45.90],[-87.80,45.35],[-87.60,45.10],[-87.40,45.45],[-87.05,45.75],[-86.95,45.95],[-86.70,45.85],[-86.60,45.60],[-86.40,45.85],[-86.25,45.95],
  [-85.80,46.08],[-85.45,46.10],[-85.00,46.00],[-84.73,45.90],[-84.40,45.98]];
const MI_CITY={detroit:[-83.05,42.33], grandrapids:[-85.67,42.96], lansing:[-84.55,42.73], annarbor:[-83.74,42.28], kalamazoo:[-85.59,42.29], flint:[-83.69,43.01],
  traversecity:[-85.62,44.76], marquette:[-87.40,46.54], holland:[-86.11,42.79], saginaw:[-83.95,43.42], muskegon:[-86.25,43.23]};
const miP = p => [(p[0]+90.6)*0.707*16.4+3, (47.6-p[1])*16.4+2];
const miPin = o => miP(Array.isArray(o.pin) ? o.pin : (MI_CITY[o.pin] || MI_CITY.lansing));
// michigan: outline map of Michigan (Lower Peninsula mitten + Upper Peninsula). o.fill (default green), o.pin: city key (detroit, grandrapids, lansing, annarbor, kalamazoo, flint, traversecity, marquette, holland, saginaw, muskegon) or [lon,lat], o.pinLabel: text beside the pin (o.pinSize, default 7)
P.michigan = {w:100, h:100, dh:30, anchors:{pin:o=>o.pin?miPin(o):[60,60]},
  draw(c, o){
    const f=o.fill||'green';
    c.poly(MI_UP.map(miP),{fill:f, gap:7, cls:'soft', rough:0.5});
    c.poly(MI_LP.map(miP),{fill:f, gap:7, cls:'soft', rough:0.5});
    if(o.pin){ const q=miPin(o); c.circle(q[0],q[1],8,{color:'red', rough:0.4}); c.dot(q[0],q[1],3.6,{color:'red'});
      if(o.pinLabel){ const sz=o.pinSize||7, tw=SK.tw(o.pinLabel,sz), left=q[0]<62 || q[0]+6+tw>100, x0=left?q[0]-6-tw:q[0]+6;
        c.rect(x0-1,q[1]-sz*0.55,tw+2,sz*0.95,{nostroke:true, fill:'paper', fs:'solid'});
        c.text(left?q[0]-6:q[0]+6,q[1]+sz*0.3,o.pinLabel,{size:sz, align:left?'end':'start', color:'red'}); } }
  }};

// lake: lake with a wavy shoreline, waves, cattails and pines on the far shore. o.dock: small wooden dock, o.boat: little sailboat, o.trees:false hides the pines
P.lake = {w:120, h:56, dh:14,
  draw(c, o){
    if(o.trees!==false) [[96,20,10],[106,22,8],[14,20,8]].forEach(([x,b,s])=>{ c.line(x,b,x,b+2,LT); c.poly([[x-s/2,b],[x,b-s*1.5],[x+s/2,b]],{fill:'green', gap:3}); });
    const wat=[[6,34],[14,24],[32,19],[52,21],[72,17],[96,20],[114,28],[113,38],[98,45],[76,47],[56,51],[34,49],[14,45]];
    c.blob(wat,{fill:'blue', gap:7, cls:'soft'});
    [[30,30],[60,27],[46,40],[82,36],[94,28]].forEach(([x,y])=>c.curve([[x,y],[x+3,y-2.5],[x+6,y],[x+9,y-2.5],[x+12,y]],{color:'blue'}));
    [[9,50,7,33],[13,52,14,36],[18,52,21,39]].forEach(([a,b,d,e])=>{ c.line(a,b,d,e,LT); c.ellipse(d+(d-a)*0.05,e+3,3.4,8,{color:'brown', fill:'brown', fs:'solid', rough:0.4}); });
    [[40,53],[70,53.5],[104,49]].forEach(([x,y])=>{ c.poly([[x-4,y],[x-2,y-4],[x,y],[x+2,y-5],[x+4,y]],{open:true, color:'green', rough:0.4}); });
    if(o.dock){ c.poly([[86,50],[95,48],[90,33],[83,34]],{fill:'brown', gap:4}); c.line(84.5,39,92,38,LT); c.line(85.5,44,93.5,43,LT); }
    if(o.boat){ c.poly([[52,31],[68,31],[65,35],[55,35]],{fill:'brown', gap:4}); c.line(60,31,60,16); c.poly([[60,17],[60,30],[68,29]],{fill:'paper', fs:'solid'}); c.poly([[60,19],[60,30],[53,29]],{fill:'red', gap:3}); }
  }};
})();
