/* ---------- Sketch: hand-drawn whiteboard drawings (rough.js) ----------
   Layout units: a full canvas is 160 x 80 (x right, y down); element x,y are centers.
   Internally everything is drawn at 10x so rough.js's hand-drawn wobble looks natural. */
const SK = (()=>{
const U = 10, NS = 'http://www.w3.org/2000/svg';
const CW = /*@@CHARW@@*/null;  // Patrick Hand advance widths (chars 32..126) at font size 1
const GEN = rough.generator();
const PROPS = {};
const ICONS_SK = (typeof DATA!=='undefined' && DATA.skicons) || {};
const COLORS = ['ink','blue','red','green','orange','purple','yellow','gray','brown','sky','pink','teal','white','paper'];

/* --- text metrics --- */
function tw(s, size){ let w=0; for(const ch of String(s)){ const c=ch.charCodeAt(0); w += (CW && c>=32 && c<127) ? CW[c-32] : 0.5; } return w*size; }
function wrap(s, size, maxW){
  const out=[];
  String(s).split('\n').forEach(par=>{
    const words=par.split(/\s+/).filter(Boolean); let cur='';
    for(const w of words){ const t=cur?cur+' '+w:w; if(cur && tw(t,size)>maxW){ out.push(cur); cur=w; } else cur=t; }
    out.push(cur);
  });
  return out;
}
function hash(s){ let h=2166136261; s=String(s); for(let i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return ((h>>>0)%2147483000)+1; }
const dist=(a,b)=>Math.hypot(a[0]-b[0],a[1]-b[1]);
function plen(q, closed){ let s=0; for(let i=1;i<q.length;i++) s+=dist(q[i-1],q[i]); if(closed && q.length>2) s+=dist(q[q.length-1],q[0]); return s; }
const rad=d=>d*Math.PI/180;

/* --- drawing context: props draw in their own w x h box; Ctx maps to canvas units --- */
class Ctx {
  constructor(o){
    Object.assign(this, o);
    this.n=0; this.items=[]; this.texts=[]; this.bb=[1e9,1e9,-1e9,-1e9];
    this.cs=Math.cos(rad(this.rot||0)); this.sn=Math.sin(rad(this.rot||0));
  }
  P(x,y){
    let dx=(x-this.pw/2)*this.k, dy=(y-this.ph/2)*this.k; if(this.flip) dx=-dx;
    const X=this.ox+dx*this.cs-dy*this.sn, Y=this.oy+dx*this.sn+dy*this.cs;
    if(X<this.bb[0]) this.bb[0]=X; if(Y<this.bb[1]) this.bb[1]=Y; if(X>this.bb[2]) this.bb[2]=X; if(Y>this.bb[3]) this.bb[3]=Y;
    return [X,Y];
  }
  opt(o){
    o=o||{}; const c=o.color||this.color||'ink';
    const r={seed:((this.seed+7919*(++this.n))%2147483000)+1, roughness:o.rough!=null?o.rough:(this.rough!=null?this.rough:1), bowing:o.bow!=null?o.bow:1,
      stroke:o.nostroke?'none':'s-'+c, strokeWidth:1, fixedDecimalPlaceDigits:1, maxRandomnessOffset:o.mro!=null?o.mro:2};
    if(o.fill){ r.fill='f-'+(o.fill===true?c:o.fill); r.fillStyle=o.fs||'hachure'; r.hachureGap=o.gap||13; r.hachureAngle=o.angle!=null?o.angle:-41; r.fillWeight=1; }
    if(o.single) r.disableMultiStroke=true;
    return r;
  }
  add(dr, o, len){ this.items.push({dr, cls:(o&&o.cls)||'', len:Math.max(20,len||100), fast:o&&o.fast}); return this; }
  line(x1,y1,x2,y2,o){ const a=this.P(x1,y1), b=this.P(x2,y2); return this.add(GEN.line(a[0],a[1],b[0],b[1],this.opt(o)), o, dist(a,b)); }
  poly(pts,o){ const q=pts.map(p=>this.P(p[0],p[1])); const op=this.opt(o); return this.add(o&&o.open?GEN.linearPath(q,op):GEN.polygon(q,op), o, plen(q,!(o&&o.open))); }
  rect(x,y,w,h,o){ if(o&&o.r) return this.rrect(x,y,w,h,o.r,o); return this.poly([[x,y],[x+w,y],[x+w,y+h],[x,y+h]],o); }
  rrect(x,y,w,h,r,o){
    r=Math.min(r,w/2,h/2); const pts=[], seg=(cx,cy,a0)=>{ for(let i=0;i<=3;i++){ const a=rad(a0+i*30); pts.push([cx+r*Math.cos(a), cy+r*Math.sin(a)]); } };
    seg(x+w-r,y+r,-90); seg(x+w-r,y+h-r,0); seg(x+r,y+h-r,90); seg(x+r,y+r,180);
    return this.poly(pts, Object.assign({rough:0.7}, o));
  }
  curve(pts,o){ const q=pts.map(p=>this.P(p[0],p[1])); return this.add(GEN.curve(q,this.opt(o)), o, plen(q,false)); }
  blob(pts,o){ // closed smooth shape through points
    const q=pts.concat([pts[0],pts[1]]).map(p=>this.P(p[0],p[1])); return this.add(GEN.curve(q,this.opt(o)), o, plen(q,false));
  }
  ellipse(cx,cy,w,h,o){ const c=this.P(cx,cy); this.P(cx-w/2,cy-h/2); this.P(cx+w/2,cy+h/2); return this.add(GEN.ellipse(c[0],c[1],w*this.k,h*this.k,this.opt(o)), o, Math.PI*(w+h)/2*this.k); }
  circle(cx,cy,d,o){ return this.ellipse(cx,cy,d,d,o); }
  dot(cx,cy,d,o){ return this.ellipse(cx,cy,d,d,Object.assign({fill:(o&&o.color)||this.color||'ink', fs:'solid', rough:0.4, cls:'dotted', single:true}, o)); }
  arc(cx,cy,w,h,a0,a1,o){ // degrees, 0 = right, positive = clockwise on screen
    const c=this.P(cx,cy); let s=a0, e=a1; if(this.flip){ s=180-a1; e=180-a0; } const rr=this.rot||0; s+=rr; e+=rr;
    this.P(cx-w/2,cy-h/2); this.P(cx+w/2,cy+h/2);
    return this.add(GEN.arc(c[0],c[1],w*this.k,h*this.k,rad(s),rad(e),!!(o&&o.closed),this.opt(o)), o, Math.PI*(w+h)/2*this.k*Math.abs(a1-a0)/360);
  }
  text(x,y,s,o){ o=o||{}; const c=this.P(x,y); const size=(o.size||10)*this.k; const half=tw(s,size)/2;
    this.bb[0]=Math.min(this.bb[0],c[0]-half); this.bb[2]=Math.max(this.bb[2],c[0]+half);
    this.texts.push({x:c[0], y:c[1], s:String(s), size, color:o.color||this.color||'ink', anchor:o.align||'middle', bold:!!o.bold, rot:(this.rot||0)+(o.rot||0)}); return this; }
  sub(px,py,ph,name,opt,extra){ // draw another prop inside this one: center (px,py) local, height ph local
    const P=PROPS[name]; if(!P) return this;
    const c=this.P(px,py), k=ph*this.k/P.h;
    const s=new Ctx(Object.assign({ox:c[0], oy:c[1], k, flip:extra&&extra.flip?!this.flip:this.flip, rot:this.rot, pw:P.w, ph:P.h, color:(extra&&extra.color)||this.color, seed:this.seed+(++this.n)*104729, rough:this.rough}));
    P.draw(s, opt||{}, {});
    this.items.push(...s.items); this.texts.push(...s.texts);
    this.bb=[Math.min(this.bb[0],s.bb[0]),Math.min(this.bb[1],s.bb[1]),Math.max(this.bb[2],s.bb[2]),Math.max(this.bb[3],s.bb[3])];
    return this;
  }
}

/* --- element builders --- */
function propBox(P, el){
  const k = el.h ? el.h*U/P.h : el.w ? el.w*U/P.w : (P.dh||20)*U/P.h;
  return k;
}
function lucidePaths(name){ return ICONS_SK[name] || null; }

function makeCtx(el, P, seed, k, cx, cy){
  return new Ctx({ox:cx, oy:cy, k, flip:!!el.flip, rot:el.rot||0, pw:P.w, ph:P.h, color:el.color||P.color||'ink', seed, rough:el.rough});
}

// Primitive "props" that size themselves from text or geometry
function textBlock(c, el, defSize, defW){
  const size=(el.size||defSize)*U, maxW=(el.w||defW)*U;
  const lines=wrap(el.text||'', size, maxW), lh=size*1.12;
  const w=Math.max(...lines.map(l=>tw(l,size))), h=lines.length*lh;
  return {size, lines, lh, w, h};
}
function emitLines(c, x, y, tb, o){ // y = center of block
  const top=y-tb.h/2+tb.lh*0.78;
  tb.lines.forEach((l,i)=>c.texts.push({x, y:top+i*tb.lh, s:l, size:tb.size, color:o.color||'ink', anchor:o.anchor||'middle', bold:!!o.bold, rot:o.rot||0}));
  const x0 = o.anchor==='start'?x : o.anchor==='end'?x-tb.w : x-tb.w/2;
  c.bb=[Math.min(c.bb[0],x0),Math.min(c.bb[1],y-tb.h/2),Math.max(c.bb[2],x0+tb.w),Math.max(c.bb[3],y+tb.h/2)];
}
const PRIM = {
  label(el, seed){
    const c=new Ctx({ox:0,oy:0,k:1,pw:0,ph:0,seed,color:el.color||'ink'}); const tb=textBlock(c, el, 4.5, 60);
    const x=el.x*U, y=el.y*U, anchor=el.align==='left'?'start':el.align==='right'?'end':'middle';
    const x0 = anchor==='start'?x : anchor==='end'?x-tb.w : x-tb.w/2;
    if(el.bg){ const p=0.5*U; c.add(GEN.rectangle(x0-p, y-tb.h/2-p*0.6, tb.w+2*p, tb.h+p*1.2, {fill:'f-'+el.bg, fillStyle:'solid', stroke:'none', seed, roughness:1.2}), {cls:'hi'}, 1); }
    emitLines(c, x, y, tb, {color:el.color||'ink', anchor, bold:el.bold, rot:el.rot});
    if(el.box){ const p=1.2*U; c.add(GEN.rectangle(x0-p, y-tb.h/2-p, tb.w+2*p, tb.h+2*p, c.opt({color:el.boxColor||el.color})), {}, 2*(tb.w+tb.h)); c.bb=[x0-p,y-tb.h/2-p,x0+tb.w+p,y+tb.h/2+p]; }
    if(el.under){ const yy=y+tb.h/2+0.6*U; c.add(GEN.line(x0, yy, x0+tb.w, yy+0.3*U, c.opt({color:el.underColor||el.color||'ink'})), {}, tb.w); }
    return c;
  },
  num(el, seed){ return PRIM.label(Object.assign({size:10, bold:true}, el), seed); },
  note(el, seed){
    const c=new Ctx({ox:0,oy:0,k:1,pw:0,ph:0,seed,color:'ink'}); const tb=textBlock(c, el, 4, (el.w||34)-4);
    const W=Math.max((el.w||34)*U, tb.w+4*U), H=Math.max(el.hh?el.hh*U:0, tb.h+4*U), x=el.x*U, y=el.y*U;
    c.add(GEN.rectangle(x-W/2, y-H/2, W, H, {fill:'f-'+(el.paper||'yellow'), fillStyle:'solid', stroke:'none', seed, roughness:0.8}), {cls:'paper'}, 1);
    c.add(GEN.rectangle(x-W/2, y-H/2, W, H, c.opt({color:el.color||'ink', rough:0.8})), {}, 2*(W+H));
    emitLines(c, x, y, tb, {color:el.ink||'ink', bold:el.bold});
    c.bb=[x-W/2,y-H/2,x+W/2,y+H/2];
    return c;
  },
  stamp(el, seed){
    const c=new Ctx({ox:0,oy:0,k:1,pw:0,ph:0,seed,color:el.color||'red', rot:el.rot!=null?el.rot:-8});
    const size=(el.size||6)*U, txt=String(el.text||'').toUpperCase(), w=tw(txt,size)*1.04+3.4*U, h=size*1.5, x=el.x*U, y=el.y*U;
    const R=(px,py)=>{ const r=rad(el.rot!=null?el.rot:-8), dx=px-x, dy=py-y; return [x+dx*Math.cos(r)-dy*Math.sin(r), y+dx*Math.sin(r)+dy*Math.cos(r)]; };
    const box=(m)=>[R(x-w/2-m,y-h/2-m),R(x+w/2+m,y-h/2-m),R(x+w/2+m,y+h/2+m),R(x-w/2-m,y+h/2+m)];
    c.add(GEN.polygon(box(0), c.opt({rough:1.4})), {}, 2*(w+h)); c.add(GEN.polygon(box(0.9*U), c.opt({rough:1.2})), {}, 2*(w+h));
    c.texts.push({x, y:y+size*0.34, s:txt, size, color:el.color||'red', anchor:'middle', bold:true, rot:el.rot!=null?el.rot:-8, stamp:true});
    c.bb=[x-w/2-U,y-h/2-U,x+w/2+U,y+h/2+U];
    return c;
  },
  box(el, seed){
    const c=new Ctx({ox:0,oy:0,k:1,pw:0,ph:0,seed,color:el.color||'ink'});
    const W=(el.w||40)*U, H=(el.hh||el.h||30)*U, x=el.x*U, y=el.y*U;
    const o={color:el.color}; if(el.fill){ o.fill=el.fill; o.fs=el.fs||'hachure'; }
    if(el.r) c.rrect(x-W/2,y-H/2,W,H,el.r*U,o); else c.add(GEN.rectangle(x-W/2,y-H/2,W,H,c.opt(Object.assign({rough:0.9},o))), {}, 2*(W+H));
    if(el.dash) c.items[c.items.length-1].cls+=' dash';
    if(el.title){ const tb=textBlock(c,{text:el.title,size:el.size||4.2,w:(el.w||40)-4},4.2,36); emitLines(c, x, y-H/2+tb.h/2+1.2*U, tb, {color:el.titleColor||el.color||'ink', bold:true}); }
    c.bb=[x-W/2,y-H/2,x+W/2,y+H/2];
    return c;
  },
  circle(el, seed){
    const c=new Ctx({ox:0,oy:0,k:1,pw:0,ph:0,seed,color:el.color||'ink'}); const d=(el.r||10)*2*U;
    const o={color:el.color}; if(el.fill){ o.fill=el.fill; o.fs=el.fs||'hachure'; }
    c.add(GEN.ellipse(el.x*U, el.y*U, d, d, c.opt(o)), {}, Math.PI*d);
    if(el.text){ const tb=textBlock(c,{text:el.text,size:el.size||4.5,w:(el.r||10)*1.6},4.5,20); emitLines(c, el.x*U, el.y*U, tb, {color:el.textColor||el.color||'ink', bold:el.bold}); }
    c.bb=[el.x*U-d/2, el.y*U-d/2, el.x*U+d/2, el.y*U+d/2];
    return c;
  },
  check(el, seed){ const c=new Ctx({ox:el.x*U,oy:el.y*U,k:(el.h||8)*U/10,pw:10,ph:10,seed,color:el.color||'green'}); c.poly([[1,5.5],[4,8.8],[9.4,1]],{open:true, cls:'bold'}); return c; },
  cross(el, seed){ const c=new Ctx({ox:el.x*U,oy:el.y*U,k:(el.h||8)*U/10,pw:10,ph:10,seed,color:el.color||'red'}); c.line(1.5,1.5,8.5,8.5,{cls:'bold'}); c.line(8.5,1.5,1.5,8.5,{cls:'bold'}); return c; },
  line(el, seed, R){
    const c=new Ctx({ox:0,oy:0,k:1,pw:0,ph:0,seed,color:el.color||'ink'});
    const a=R.pt(el.from), b=R.pt(el.to); c.add(GEN.line(a[0],a[1],b[0],b[1],c.opt({})), {cls:el.dash?'dash':''}, dist(a,b));
    c.bb=[Math.min(a[0],b[0]),Math.min(a[1],b[1]),Math.max(a[0],b[0]),Math.max(a[1],b[1])]; return c;
  },
  divider(el, seed, R){ return PRIM.line(Object.assign({from:[el.x,(el.y0!=null?el.y0:4)], to:[el.x,(el.y1!=null?el.y1:(R&&R.H?R.H/U-4:68))], dash:true, color:el.color||'gray'}, el), seed, {pt:p=>[p[0]*U,p[1]*U]}); },
  arrow(el, seed, R){
    const c=new Ctx({ox:0,oy:0,k:1,pw:0,ph:0,seed,color:el.color||'ink'});
    let a=R.pt(el.from), b=R.pt(el.to);
    const gap=(el.gap!=null?el.gap:1.5)*U;
    if(typeof el.from==='string') a=R.edge(el.from, b, gap) || a;
    if(typeof el.to==='string') b=R.edge(el.to, a, gap) || b;
    const L=dist(a,b), bend=(el.bend!=null?el.bend:0.12)*L, mx=(a[0]+b[0])/2, my=(a[1]+b[1])/2, nx=-(b[1]-a[1])/(L||1), ny=(b[0]-a[0])/(L||1);
    const m=[mx+nx*bend, my+ny*bend];
    c.add(GEN.curve([a,m,b], c.opt({})), {cls:(el.dash?'dash ':'')+(el.bold?'bold':'')}, L);
    const head=(tip, from)=>{ const ang=Math.atan2(tip[1]-from[1], tip[0]-from[0]), hl=Math.min(2.6*U, L*0.35);
      const p1=[tip[0]-hl*Math.cos(ang-0.45), tip[1]-hl*Math.sin(ang-0.45)], p2=[tip[0]-hl*Math.cos(ang+0.45), tip[1]-hl*Math.sin(ang+0.45)];
      c.add(GEN.linearPath([p1,tip,p2], c.opt({rough:0.6})), {cls:el.bold?'bold':''}, 2*hl); };
    if(el.head!=='none') head(b, m);
    if(el.head==='both') head(a, m);
    c.bb=[Math.min(a[0],b[0],m[0]),Math.min(a[1],b[1],m[1]),Math.max(a[0],b[0],m[0]),Math.max(a[1],b[1],m[1])];
    if(el.label){ const tb=textBlock(c,{text:el.label,size:el.size||3.8,w:el.w||30},3.8,30); const off=(el.loff!=null?el.loff:3)*U; emitLines(c, m[0]+nx*off*(bend<0?-1:1), m[1]+ny*off*(bend<0?-1:1), tb, {color:el.labelColor||el.color||'ink'}); }
    return c;
  },
  bubble(el, seed, R){
    const c=new Ctx({ox:0,oy:0,k:1,pw:0,ph:0,seed,color:el.color||'ink'}); const tb=textBlock(c, el, 4, (el.w||40)-5);
    const W=tb.w+5*U, H=tb.h+3.6*U, x=el.x*U, y=el.y*U;
    let tgt = el.to!=null ? R.anchor(el.to, 'head') : null;
    if(el.think){
      c.add(GEN.ellipse(x,y,W*1.18,H*1.35,c.opt({fill:'paper',fs:'solid',rough:1.1})), {cls:'paper'}, Math.PI*(W+H));
      if(tgt){ for(let i=1;i<=3;i++){ const t=0.25+i*0.2, px=x+(tgt[0]-x)*t, py=y+(tgt[1]-y)*t, d=(1.6-i*0.35)*U; c.add(GEN.ellipse(px,py,d,d,c.opt({fill:'paper',fs:'solid'})), {}, Math.PI*d); } }
      c.bb=[x-W*0.59,y-H*0.675,x+W*0.59,y+H*0.675];
    } else {
      const r=Math.min(2.4*U,H/2), pts=[];
      const seg=(cx,cy,a0)=>{ for(let i=0;i<=3;i++){ const a=rad(a0+i*30); pts.push([cx+r*Math.cos(a), cy+r*Math.sin(a)]); } };
      // the tail leaves from whichever edge faces the speaker, so it never crosses the text
      let side=null, tip=null, tx=0, ty=0;
      if(tgt){
        const nx=(tgt[0]-x)/(W/2), ny=(tgt[1]-y)/(H/2);
        side = (Math.abs(nx) > Math.abs(ny) && Math.abs(nx) > 1) ? (nx>0?'r':'l') : (ny>0?'b':'t');
        tip=[tgt[0]+(x-tgt[0])*0.18, tgt[1]+(y-tgt[1])*0.18];
        tx=Math.max(x-W/2+r+1.5*U, Math.min(x+W/2-r-1.5*U, x+(tgt[0]-x)*0.35));
        ty=Math.max(y-H/2+r+1.2*U, Math.min(y+H/2-r-1.2*U, y+(tgt[1]-y)*0.35));
        if(Math.min(H/2-r, 1.6*U) < 1.2*U && (side==='l'||side==='r')) side = ny>0?'b':'t';   // too short for a side tail
      }
      const half=1.6*U, hv=Math.min(half, H/2-r-0.2*U);
      seg(x+W/2-r,y-H/2+r,-90);
      if(side==='r') pts.push([x+W/2,ty-hv], tip, [x+W/2,ty+hv]);
      seg(x+W/2-r,y+H/2-r,0);
      if(side==='b') pts.push([tx+half,y+H/2], tip, [tx-half,y+H/2]);
      seg(x-W/2+r,y+H/2-r,90);
      if(side==='l') pts.push([x-W/2,ty+hv], tip, [x-W/2,ty-hv]);
      seg(x-W/2+r,y-H/2+r,180);
      if(side==='t') pts.push([tx-half,y-H/2], tip, [tx+half,y-H/2]);
      c.add(GEN.polygon(pts, c.opt({fill:'paper', fs:'solid', rough:0.7})), {cls:'paper-s'}, plen(pts,true));
      c.bb=[x-W/2,y-H/2,x+W/2,y+H/2];
    }
    emitLines(c, x, y, tb, {color:el.ink||'ink', bold:el.bold});
    return c;
  },
  ring(el, seed, R){
    const c=new Ctx({ox:0,oy:0,k:1,pw:0,ph:0,seed,color:el.color||'orange'}); const b=R.bbox(el.on); if(!b) return c;
    const p=(el.pad!=null?el.pad:1.5)*U, w=b[2]-b[0]+2*p, h=b[3]-b[1]+2*p;
    c.add(GEN.ellipse((b[0]+b[2])/2,(b[1]+b[3])/2,w*1.12,h*1.12,c.opt({rough:1.3, bow:2})), {cls:'bold'}, Math.PI*(w+h)/2);
    c.bb=[b[0]-p,b[1]-p,b[2]+p,b[3]+p]; return c;
  },
  xout(el, seed, R){
    const c=new Ctx({ox:0,oy:0,k:1,pw:0,ph:0,seed,color:el.color||'red'}); const b=R.bbox(el.on); if(!b) return c;
    c.add(GEN.line(b[0],b[1],b[2],b[3],c.opt({})), {cls:'bold'}, dist([b[0],b[1]],[b[2],b[3]]));
    c.add(GEN.line(b[2],b[1],b[0],b[3],c.opt({})), {cls:'bold'}, dist([b[0],b[1]],[b[2],b[3]]));
    c.bb=b.slice(); return c;
  },
  icon(el, seed){ // any Lucide icon, re-drawn by hand
    const c=new Ctx({ox:el.x*U,oy:el.y*U,k:(el.h||12)*U/24,pw:24,ph:24,seed,color:el.color||'ink'});
    const d=lucidePaths(el.name)||[]; const k=c.k, x0=c.ox-12*k, y0=c.oy-12*k;
    d.forEach(pd=>{ const dr=GEN.path(pd, {seed:((seed+7919*(++c.n))%2147483000)+1, roughness:0.35, maxRandomnessOffset:0.35, bowing:0.5, stroke:'s-'+(el.color||'ink'), strokeWidth:1, fixedDecimalPlaceDigits:2}); c.items.push({dr, cls:'icon', len:90, sw:(4.6/k).toFixed(3), tf:`translate(${x0.toFixed(1)} ${y0.toFixed(1)}) scale(${k.toFixed(3)})`}); });
    c.bb=[x0,y0,x0+24*k,y0+24*k]; return c;
  },
};
const REF_PRIMS = new Set(['arrow','bubble','ring','xout','line']);

/* --- build a canvas from element specs --- */
function el$(tag, attrs){ const e=document.createElementNS(NS, tag); for(const k in attrs) if(attrs[k]!=null) e.setAttribute(k, attrs[k]); return e; }
function render(elements, o){
  o=o||{}; const W=(o.w||160)*U, H=(o.h||80)*U, key=o.key||'sk';
  const placed={}, ctxs=[];
  const R = { W, H,
    pt(v){ if(Array.isArray(v)) return [v[0]*U, v[1]*U]; const p=placed[v]; return p ? [(p.bb[0]+p.bb[2])/2,(p.bb[1]+p.bb[3])/2] : [W/2,H/2]; },
    bbox(id){ const p=placed[id]; return p ? p.bb.slice() : null; },
    anchor(v, name){ if(Array.isArray(v)) return [v[0]*U, v[1]*U]; const p=placed[v]; if(!p) return null; if(p.anchors && p.anchors[name]) return p.anchors[name]; return [(p.bb[0]+p.bb[2])/2, p.bb[1]]; },
    edge(id, toward, gap){ const p=placed[id]; if(!p) return null; const b=p.bb, cx=(b[0]+b[2])/2, cy=(b[1]+b[3])/2, hw=(b[2]-b[0])/2+gap, hh=(b[3]-b[1])/2+gap;
      const dx=toward[0]-cx, dy=toward[1]-cy; if(!dx && !dy) return [cx,cy]; const t=Math.min(hw/Math.abs(dx||1e-9), hh/Math.abs(dy||1e-9)); return [cx+dx*Math.min(t,1), cy+dy*Math.min(t,1)]; },
  };
  const build = (el, i) => {
    const seed=hash(key+':'+(el.id||i)+':'+(el.p||''));
    let c;
    if(PRIM[el.p]) c=PRIM[el.p](el, seed, R);
    else if(PROPS[el.p]){ const P=PROPS[el.p], k=propBox(P, el); c=makeCtx(el, P, seed, k, el.x*U, el.y*U); P.draw(c, el.opt||{}, el);
      if(P.anchors){ c.anchors={}; for(const a in P.anchors){ const q=P.anchors[a](el.opt||{}); const s=c.bb.slice(); c.anchors[a]=c.P(q[0],q[1]); c.bb=s; } }
      if(el.label){ const lb=PRIM.label({text:el.label, x:el.x, y:(c.bb[3]/U)+(el.lsize||4)*0.85+0.6, size:el.lsize||4, color:el.lcolor||el.color||'ink', w:el.lw||40}, seed+5); c.items.push(...lb.items); c.texts.push(...lb.texts); c.bb[3]=lb.bb[3]; c.bb[0]=Math.min(c.bb[0],lb.bb[0]); c.bb[2]=Math.max(c.bb[2],lb.bb[2]); }
    }
    else { c=PRIM.label({text:'['+el.p+'?]', x:el.x||80, y:el.y||40, color:'red'}, seed); c.missing=true; }
    c.el=el; c.i=i;
    if(el.id) placed[el.id]=c;
    ctxs[i]=c;
  };
  elements.forEach((el,i)=>{ if(!REF_PRIMS.has(el.p) || (el.p==='line' && !el.from && !el.to)) build(el,i); });
  elements.forEach((el,i)=>{ if(REF_PRIMS.has(el.p)) build(el,i); });
  const svg=el$('svg', {viewBox:`0 0 ${W} ${H}`, class:'sk', preserveAspectRatio:o.par||'xMidYMid meet', role:'img', 'aria-label':o.alt||null});
  const out=[];
  ctxs.forEach((c,i)=>{
    const el=c.el, g=el$('g', {class:'sk-el', 'data-i':i, 'data-id':el.id||null}), hh=el$('g', {class:'sk-h'});
    const a=el$('g', {class:'sk-a a-'+(el.anim || (el.p==='stamp'?'stamp':['label','num','note','bubble'].includes(el.p)?'write':'draw'))});
    const lp=el$('g', {class:'sk-l'+(el.loop?' l-'+el.loop:'')});
    g.appendChild(hh); hh.appendChild(a); a.appendChild(lp);
    // schedule strokes
    const strokes=[];
    c.items.forEach(it=>{
      const paths=GEN.toPaths(it.dr);
      paths.forEach(p=>{
        let cls, col;
        if(p.fill && p.fill!=='none'){ cls='sk-solid'; col=p.fill.slice(2); }
        else if(String(p.stroke).startsWith('f-')){ cls='sk-f dr'; col=p.stroke.slice(2); }
        else if(String(p.stroke).startsWith('s-')){ cls=/\bdash\b/.test(it.cls||'')?'sk-s':'sk-s dr'; col=p.stroke.slice(2); }   // dashes can't use the draw-on trick
        else return;
        const node=el$('path', {d:p.d, class:`${cls} c-${col} ${it.cls||''}`.trim(), pathLength:cls.includes('dr')?'1':null, transform:it.tf||null});
        if(it.sw) node.style.strokeWidth=it.sw;
        strokes.push({node, len: cls.startsWith('sk-f') ? it.len*0.5 : it.len, fill:cls.startsWith('sk-f')||cls==='sk-solid'});
      });
    });
    const total=strokes.reduce((s,x)=>s+(x.fill?0:x.len),0) || 1;
    const T=Math.max(0.45, Math.min(el.speed?el.speed:2.4, 0.35+total/5200));
    let t=0;
    strokes.forEach(s=>{
      if(s.fill){ s.node.style.setProperty('--d', (Math.max(0,t-0.15)).toFixed(2)+'s'); s.node.style.setProperty('--t', '0.5s'); }
      else { const d=T*s.len/total; s.node.style.setProperty('--d', t.toFixed(2)+'s'); s.node.style.setProperty('--t', Math.max(0.12,d).toFixed(2)+'s'); t+=d*0.92; }
      lp.appendChild(s.node);
    });
    c.texts.forEach((tx,j)=>{
      const n=el$('text', {x:tx.x.toFixed(1), y:tx.y.toFixed(1), 'font-size':tx.size.toFixed(1), 'text-anchor':tx.anchor, class:`sk-t c-${tx.color}${tx.bold?' b':''}${tx.stamp?' st':''}`, transform:tx.rot?`rotate(${tx.rot} ${tx.x.toFixed(1)} ${tx.y.toFixed(1)})`:null});
      n.textContent=tx.s; n.style.setProperty('--d', (t*0.6+j*0.18).toFixed(2)+'s'); n.style.setProperty('--t', Math.min(1.2,0.25+tx.s.length*0.035).toFixed(2)+'s');
      lp.appendChild(n);
    });
    const dur = Math.max(t, ...c.texts.map((x,j)=>t*0.6+j*0.18+Math.min(1.2,0.25+x.s.length*0.035)), 0.5);
    if(el.move){ g.style.setProperty('--mt', (el.move.dur||1.4)+'s'); }
    const bb=c.bb.map(v=>v/U);
    g.style.setProperty('--ox', ((c.bb[0]+c.bb[2])/2).toFixed(0)+'px'); g.style.setProperty('--oy', ((c.bb[1]+c.bb[3])/2).toFixed(0)+'px');
    g.style.setProperty('--by', c.bb[3].toFixed(0)+'px');
    out.push({g, el, i, dur, bb, missing:!!c.missing});
    svg.appendChild(g);
  });
  return {svg, els:out, w:W/U, h:H/U};
}

/* --- timing: which elements are visible at time t --- */
function plan(R, beats, beatText, cues){
  // beats: [[t0,t1],...] for the scene; returns appear/move/exit times per element
  R.els.forEach(x=>{
    const el=x.el, at=Math.max(0, Math.min(beats.length-1, el.at||0)), b=beats[at] || [0,0];
    const cueT = (bi, word) => { if(!word) return 0; const ck=cues && cues[bi] && cues[bi][word.toLowerCase()]; if(ck!=null) return ck;
      const txt=(beatText[bi]||'').toLowerCase(), j=txt.search(new RegExp('\\b'+word.toLowerCase().replace(/[.*+?^${}()|[\]\\]/g,'\\$&'))); return j<0 ? 0 : (beats[bi][1]-beats[bi][0])*j/Math.max(1,txt.length); };
    x.ta = b[0] + cueT(at, el.cue) + (el.delay||0);
    if(el.move){ const mi=Math.max(0, Math.min(beats.length-1, el.move.at!=null?el.move.at:at)), mb=beats[mi]||b; x.tm = mb[0] + cueT(mi, el.move.cue) + (el.move.delay||0); }
    if(el.out!=null){ const oi=Math.max(0, Math.min(beats.length-1, el.out)); x.to=(beats[oi]||b)[0]; }
  });
}
function update(R, t, opts){
  opts=opts||{};
  R.els.forEach(x=>{
    const g=x.g, inNow = t >= x.ta-0.001;
    if(inNow){
      if(!g.classList.contains('in')){ g.classList.add('in'); if(opts.instant || t - x.ta > 0.35) g.classList.add('now'); else if(opts.onShow) opts.onShow(x); }
    } else if(g.classList.contains('in')) g.classList.remove('in','now','moved','out');
    if(x.el.move){
      const mv = inNow && t >= x.tm-0.001;
      if(mv && !g.classList.contains('moved')){ const dx=(x.el.move.to[0]-x.el.x)*U, dy=(x.el.move.to[1]-x.el.y)*U, inst=opts.instant || t-x.tm>0.35;
        g.classList.toggle('mnow', !!inst); g.style.setProperty('--mx', dx+'px'); g.style.setProperty('--my', dy+'px'); g.classList.add('moved'); if(opts.onMove && !inst) opts.onMove(x); }
      else if(!mv && g.classList.contains('moved')){ g.classList.add('mnow'); g.classList.remove('moved'); g.style.setProperty('--mx','0px'); g.style.setProperty('--my','0px'); }
    }
    if(x.to!=null) g.classList.toggle('out', t >= x.to);
    const hl = opts.hl && x.el.id && opts.hl.includes(x.el.id);
    g.classList.toggle('hl', !!hl);
  });
}
function showAll(R){ R.els.forEach(x=>{ x.g.classList.add('in','now'); if(x.el.move){ x.g.style.setProperty('--mx', (x.el.move.to[0]-x.el.x)*U+'px'); x.g.style.setProperty('--my', (x.el.move.to[1]-x.el.y)*U+'px'); x.g.classList.add('moved'); } if(x.el.out!=null) x.g.classList.add('out'); }); }
function bboxes(R){ return R.els.map(x=>({i:x.i, id:x.el.id||null, p:x.el.p, bb:x.bb.map(v=>+v.toFixed(1)), missing:x.missing, at:x.el.at||0, out:x.el.out})); }

return {PROPS, PRIM, render, plan, update, showAll, bboxes, tw, wrap, U, COLORS, Ctx};
})();
