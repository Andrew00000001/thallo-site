/* ---------- Watch: narrated, interactive whiteboard lessons ---------- */
const LESSONS = DATA.lessons || [];
const LBY = Object.fromEntries(LESSONS.map(l=>[l.id,l]));
const ICONS = DATA.icons || {};
function icon(name, cls){ const p=ICONS[name]; return p ? `<svg class="ic ${cls||''}" viewBox="0 0 24 24" aria-hidden="true">${p}</svg>` : ''; }
const GATES = new Set(['quiz','swipe','sort','explore','slider','choice']);
function lessonState(id){
  const s=(P.lessons||{})[id]; if(!s) return null;
  const L=LBY[id];
  if(L && L.ver && s.ver!==L.ver){ s.pos=0; s.gates={}; s.quiz={}; s.ver=L.ver; }   // the lesson was rewritten: old positions no longer line up
  return s;
}
function lessonStateW(id){ P.lessons=P.lessons||{}; const s=P.lessons[id] || (P.lessons[id]={pos:0, done:0, gates:{}}); s.gates=s.gates||{}; if(LBY[id] && LBY[id].ver) s.ver=LBY[id].ver; return s; }
function lessonsDone(){ return LESSONS.filter(l=>{ const s=lessonState(l.id); return s && s.done; }).length; }
function nextLesson(){
  const inProg = LESSONS.find(l=>{ const s=lessonState(l.id); return s && !s.done && s.pos>5; });
  return inProg || LESSONS.find(l=>{ const s=lessonState(l.id); return !s || !s.done; }) || null;
}
const mmss = s => { s=Math.max(0,Math.floor(s||0)); return Math.floor(s/60)+':'+String(s%60).padStart(2,'0'); };
const gateCount = L => L.scenes.filter(x=>GATES.has(x.type)).length;
function gateMax(sc){ return sc.type==='swipe' ? sc.cards.length : sc.type==='sort' ? sc.items.length : sc.type==='slider' ? (sc.goal?1:0) : 1; }
const lessonStarsMax = L => L.scenes.reduce((s,sc)=>s+(GATES.has(sc.type)?gateMax(sc):0),0);

function renderWatch(opts){
  if(opts && opts.id && LBY[opts.id]){ openLesson(opts.id, opts); return; }
  lpClose();
  const el=$('#view-watch');
  if(!LESSONS.length){ el.innerHTML='<div class="panel"><p class="muted" style="margin:0">No lessons in this build.</p></div>'; return; }
  const done=lessonsDone(), mins=Math.round(LESSONS.reduce((s,l)=>s+l.timing.dur,0)/60), nx=nextLesson();
  const card = l => {
    const s=lessonState(l.id), st = s&&s.done ? '<span class="chip good">Watched</span>' : s&&s.pos>5 ? `<span class="chip">Stopped at ${mmss(s.pos)}</span>` : '';
    const stars = s && s.gates ? Object.values(s.gates).reduce((a,g)=>a+(g||0),0) : 0, smax=lessonStarsMax(l);
    const t0=l.scenes[0], thumb = t0 && t0.draw && t0.draw.length && typeof SK!=='undefined';
    return `<button class="lcard ${thumb?'has-thumb':''}" data-act="lesson" data-id="${l.id}">
      ${thumb?`<span class="lthumb" data-thumb="${l.id}" aria-hidden="true"><span class="lnum">${l.id.slice(1)}</span></span>`:`<span class="lnum">${l.id.slice(1)}</span>`}
      <span class="lbody"><span class="lt">${esc(l.title)}</span><span class="ls">${esc(l.summary)}</span>
      <span class="lmeta mono">${mmss(l.timing.dur)} · ${gateCount(l)} activities${stars?` · ★ ${stars}/${smax}`:''} ${st}</span></span>
      <span class="lplay" aria-hidden="true">${icon('play')}</span></button>`;
  };
  const groups = SECTIONS.map(s=>({s, ls:LESSONS.filter(l=>l.sec===s.key)})).filter(g=>g.ls.length);
  el.innerHTML = `<div class="stack">
    <div class="panel">
      <h2>Video lessons</h2>
      <p class="muted lede" style="margin:6px 0 12px">Short narrated whiteboard lessons: real-life stories where you choose what happens next, drawings that explain each term, and activities you tap, sort and drag. Earn stars as you go. Every fact was checked against the app's study material and the laws and forms behind it.</p>
      <div class="row" style="gap:18px;align-items:center">
        ${nx?`<button class="btn primary cta-big" data-act="lesson" data-id="${nx.id}">${icon('play','btn-ic')} ${lessonState(nx.id)&&lessonState(nx.id).pos>5?'Continue':'Watch'}: ${esc(nx.title)}</button>`:''}
        <span class="mono small muted">${done} of ${LESSONS.length} watched · about ${mins} min of narration</span>
      </div>
    </div>
    ${groups.map(g=>`<section><h3 class="lgroup">${esc(g.s.name)} <span class="mono small muted">${g.s.pct}% of the exam</span></h3><div class="lgrid">${g.ls.map(card).join('')}</div></section>`).join('')}
  </div>`;
  // each card shows the lesson's opening drawing (drawn once it scrolls into view)
  const draw = h => { if(h.dataset.done) return; h.dataset.done=1; const L=LBY[h.dataset.thumb]; try{ const R=SK.render(L.scenes[0].draw, {w:90, h:72, key:L.id+':thumb'}); SK.showAll(R); h.prepend(R.svg); }catch(e){} };
  const hs=el.querySelectorAll('[data-thumb]');
  if('IntersectionObserver' in window){ const io=new IntersectionObserver(es=>es.forEach(e=>{ if(e.isIntersecting){ draw(e.target); io.unobserve(e.target); } }), {rootMargin:'200px'}); hs.forEach(h=>io.observe(h)); }
  else hs.forEach(draw);
}

/* --- audio sources ---
   The viewer may refuse to stream media files, so the narration tries, in order:
   0 the embedded bytes from a blob: URL, 1 the same bytes as a data: URI (or the file),
   2 Web Audio (decoded in the page, outside media-element rules), then silent captions. */
let ACTX = null;
function unlockAudio(){
  try{
    if(!ACTX){ const AC = window.AudioContext || window.webkitAudioContext; if(AC) ACTX = new AC(); }
    if(ACTX && ACTX.state === 'suspended') ACTX.resume().catch(()=>{});
  }catch(e){ ACTX = null; }
}
class WAPlayer {
  constructor(bytes){ this.bytes=bytes; this.buf=null; this.node=null; this.offset=0; this.t0=0; this.rate=1; this.paused=true; this.running=false; this.ls={}; this.tu=0; }
  addEventListener(k, f){ (this.ls[k] = this.ls[k] || []).push(f); }
  emit(k){ (this.ls[k] || []).forEach(f=>{ try{ f(); }catch(e){} }); }
  get duration(){ return this.buf ? this.buf.duration : NaN; }
  get currentTime(){ return this.running && ACTX ? Math.min(this.duration, this.offset + (ACTX.currentTime - this.t0) * this.rate) : this.offset; }
  set currentTime(t){ const on=this.running; if(on) this.stopNode(); this.offset=Math.max(0, +t || 0); if(on) this.startNode(); }
  get playbackRate(){ return this.rate; }
  set playbackRate(r){ const t=this.currentTime, on=this.running; if(on) this.stopNode(); this.rate=+r || 1; this.offset=t; if(on) this.startNode(); }
  decode(){
    if(this.buf) return Promise.resolve(this.buf);
    if(!ACTX) return Promise.reject(new Error('no audio context'));
    return new Promise((res, rej)=>{ const p = ACTX.decodeAudioData(this.bytes.slice(0), res, rej); if(p && p.then) p.then(res, rej); }).then(b=>(this.buf=b));
  }
  startNode(){
    if(!this.buf || this.offset >= this.buf.duration - 0.01) return;
    const n = ACTX.createBufferSource(); n.buffer=this.buf; n.playbackRate.value=this.rate; n.connect(ACTX.destination);
    n.onended = ()=>{ if(this.node===n){ this.offset=this.currentTime; this.running=false; this.paused=true; this.node=null; clearInterval(this.tu); this.emit('ended'); } };
    this.t0 = ACTX.currentTime; n.start(0, this.offset); this.node=n; this.running=true;
    clearInterval(this.tu); this.tu=setInterval(()=>this.emit('timeupdate'), 250);
  }
  stopNode(){ if(this.node){ const n=this.node; this.offset=this.currentTime; this.node=null; n.onended=null; try{ n.stop(); }catch(e){} } this.running=false; clearInterval(this.tu); }
  play(){
    if(!this.paused) return Promise.resolve();
    this.paused=false; unlockAudio();
    return this.decode().then(()=>{ if(!this.paused && !this.running) this.startNode(); }).catch(e=>{ this.paused=true; this.emit('error'); throw e; });
  }
  pause(){ this.paused=true; this.stopNode(); }
  removeAttribute(){ this.pause(); }
  load(){}
}
function attachMedia(m, L){
  m.addEventListener('error', ()=>{ if(LP.L===L) nextSource(m); });
  m.addEventListener('ended', ()=>{ if(LP.L===L && LP.audio===m) lpFinish(); });
  m.addEventListener('timeupdate', ()=>{ if(LP.L===L && LP.audio===m && LP.playing) lpTick(false); });
  return m;
}
function embeddedEl(L){ return L.audio && L.audio[0]==='#' ? document.getElementById(L.audio.slice(1)) : null; }
function embeddedBytes(L){
  const el=embeddedEl(L); if(!el) return null;
  try{ return decodeBlock(el); }catch(e){ return null; }
}
function fetchURL(u, ms){   // resolves to the file's bytes, or null on any failure or after ms
  return new Promise(res=>{
    let done=false; const end=b=>{ if(!done){ done=true; clearTimeout(t); res(b); } }, t=setTimeout(()=>end(null), ms);
    fetch(u).then(r=>{ if(!r.ok) throw new Error('HTTP '+r.status); return r.arrayBuffer(); }).then(end, ()=>end(null));
  });
}
function fetchBytes(L){
  const net = typeof fetch==='function' && location.protocol!=='file:';
  // full-quality audio published next to the page; the compact copy inside the page is the fallback (file:// or offline)
  const hq = L.audioHQ && net ? fetchURL(L.audioHQ, 6000) : Promise.resolve(null);
  return hq.then(b=>{
    if(b && b.byteLength){ L.hqOk=true; if(LP.L===L) LP.bytes=b; return b; }
    if(embeddedEl(L)) return embeddedBytes(L);
    if(!L.audio || !net) return null;
    return fetchURL(L.audio, 15000).then(b2=>{ if(b2 && LP.L===L) LP.bytes=b2; return b2; });
  });
}
function startSources(L){
  LP.srcStage=0; LP.bytes=null; LP.audio=null; LP.pendingPlay=false;
  if(!L.audio){ goVirtual(0, false, true); return; }
  setReady(false);
  LP.bytesP = fetchBytes(L);
  let settled=false;
  const timer=setTimeout(()=>{ if(!settled && LP.L===L && !LP.audio){ settled=true; LP.srcStage=1; useSource(directSource(L), L); } }, 8000);
  LP.bytesP.then(b=>{
    if(settled || LP.L!==L) return; settled=true; clearTimeout(timer);
    if(b && window.URL && URL.createObjectURL){
      LP.blobUrl = URL.createObjectURL(new Blob([b], {type: L.audioType || 'audio/mpeg'}));
      const a=new Audio(); a.preload='auto'; a.src=LP.blobUrl; useSource(a, L);
    } else { LP.srcStage=1; useSource(directSource(L), L); }
  });
}
function directSource(L){
  const a=new Audio(); a.preload='auto';
  const el=embeddedEl(L);
  if(el){ const b=LP.bytes || embeddedBytes(L); let s=''; const u=new Uint8Array(b||new ArrayBuffer(0)); for(let i=0;i<u.length;i+=32768) s+=String.fromCharCode.apply(null, u.subarray(i,i+32768)); a.src='data:'+(L.audioType||'audio/webm')+';base64,'+btoa(s); }
  else a.src=L.audio;
  return a;
}
function useSource(m, L){
  if(LP.L!==L || LP.virtual) return;
  attachMedia(m, L);
  const t=lpTime();
  LP.audio=m;
  try{ m.currentTime=t; }catch(e){}
  try{ m.playbackRate=LP.rate; }catch(e){}
  setReady(true);
  if(LP.playing || LP.pendingPlay){ LP.pendingPlay=false; LP.playing=true; playMedia(m); lpLoop(); lpUI(); }
}
function setReady(on){
  const b=$('#lp-over [data-act="lp-start"]'); if(b){ b.disabled=!on; if(!on){ b.dataset.label=b.dataset.label||b.innerHTML; b.textContent='Loading audio…'; } else if(b.dataset.label){ b.innerHTML=b.dataset.label; } }
}
async function nextSource(from){
  const L = LP.L;
  if(!L || LP.virtual || from!==LP.audio || from._failed) return;
  from._failed = true;
  const was = LP.playing;
  try{ from.pause(); }catch(e){}
  LP.playing = was;
  while(LP.L===L){
    LP.srcStage++;
    if(LP.srcStage===1){ useSource(directSource(L), L); return; }
    if(LP.srcStage===2){
      const bytes = await LP.bytesP; if(LP.L!==L) return;
      if(bytes && (window.AudioContext || window.webkitAudioContext)){ useSource(new WAPlayer(bytes), L); return; }
      continue;
    }
    goVirtual(lpTime(), was); return;
  }
}
function playMedia(m){
  const pr = m.play();
  if(pr && pr.then) pr.then(()=>{ const o=$('#lp-note'); if(o && !LP.virtual) o.hidden=true; }, ()=>{});
  if(pr && pr.catch) pr.catch(e=>{
    if(!LP.L || LP.audio!==m) return;
    if(e && e.name==='NotAllowedError'){ LP.playing=false; lpUI(); const o=$('#lp-note'); if(o){ o.hidden=false; o.textContent='Tap Play to start the sound.'; } }
    else nextSource(m);
  });
}

/* --- sound effects (synthesized, no files) --- */
const SFX = {
  on(){ return P.settings.sfx!==false; },
  play(kind){
    if(!this.on()) return; unlockAudio(); if(!ACTX || ACTX.state!=='running') return;
    try{
      const t=ACTX.currentTime;
      const tone=(f,dt,dur,type,vol,f2)=>{ const o=ACTX.createOscillator(), g=ACTX.createGain(); o.type=type||'sine'; o.frequency.setValueAtTime(f,t+dt); if(f2) o.frequency.exponentialRampToValueAtTime(f2,t+dt+dur);
        g.gain.setValueAtTime(0.0001,t+dt); g.gain.exponentialRampToValueAtTime(vol,t+dt+0.012); g.gain.exponentialRampToValueAtTime(0.0001,t+dt+dur); o.connect(g); g.connect(ACTX.destination); o.start(t+dt); o.stop(t+dt+dur+0.03); };
      const noise=(dt,dur,vol,fc,q)=>{ const n=Math.floor(ACTX.sampleRate*dur), b=ACTX.createBuffer(1,n,ACTX.sampleRate), d=b.getChannelData(0); let s=7; for(let i=0;i<n;i++){ s=(s*16807)%2147483647; d[i]=(s/1073741823.5-1)*(1-i/n); }
        const src=ACTX.createBufferSource(), f=ACTX.createBiquadFilter(), g=ACTX.createGain(); src.buffer=b; f.type='bandpass'; f.frequency.value=fc; f.Q.value=q||0.8; g.gain.value=vol; src.connect(f); f.connect(g); g.connect(ACTX.destination); src.start(t+dt); };
      switch(kind){
        case 'ding': tone(880,0,.16,'sine',.11); tone(1318,.08,.3,'sine',.09); break;
        case 'buzz': tone(150,0,.24,'square',.035,105); break;
        case 'pop': tone(420,0,.09,'sine',.07,880); break;
        case 'stamp': noise(0,.14,.5,260,0.6); tone(95,0,.16,'sine',.12,55); break;
        case 'whoosh': noise(0,.4,.25,1400,0.5); break;
        case 'click': tone(1500,0,.025,'square',.025); break;
        case 'crash': noise(0,.5,.7,700,0.4); tone(70,0,.35,'sine',.13,38); break;
        case 'tada': [523,659,784,1047].forEach((f,i)=>tone(f,i*.08,.38,'triangle',.07)); break;
        case 'cash': tone(1568,0,.08,'square',.03); tone(2093,.07,.25,'triangle',.06); break;
        case 'boing': tone(220,0,.35,'sine',.09,520); break;
      }
    }catch(e){}
  }
};

/* --- player state --- */
const LP = {L:null, audio:null, virtual:false, playing:false, vbase:0, vt0:0, rate:1, raf:0, scene:-1, sig:'', gate:{}, gs:{}, awaiting:-1, ended:false, lastSave:0, srcStage:0, bytes:null, bytesP:null, blobUrl:null, sk:[], lastT:0, stars:0};
function lpDur(){ return LP.L ? LP.L.timing.dur : 0; }
function lpTime(){
  if(!LP.L) return 0;
  if(LP.virtual) return LP.playing ? Math.min(lpDur(), LP.vbase + (performance.now()-LP.vt0)/1000*LP.rate) : LP.vbase;
  return LP.audio ? LP.audio.currentTime : (LP.vbase || 0);
}
function lpPlay(){
  if(!LP.L) return;
  if(LP.ended){ lpSeek(0); LP.ended=false; }
  if(LP.awaiting>=0) return;
  hideOverlay();
  LP.playing=true; stageClass();
  if(LP.virtual){ LP.vt0=performance.now(); unlockAudio(); }
  else if(!LP.audio){ unlockAudio(); LP.playing=false; LP.pendingPlay=true; const o=$('#lp-note'); if(o){ o.hidden=false; o.textContent='Loading audio…'; } lpUI(); return; }
  else { unlockAudio(); try{ LP.audio.playbackRate=LP.rate; }catch(e){} playMedia(LP.audio); }
  lpLoop(); lpUI();
}
function lpPause(){
  if(!LP.L) return;
  if(LP.virtual){ LP.vbase=lpTime(); }
  else if(LP.audio) LP.audio.pause();
  LP.playing=false; stageClass(); lpSavePos(true); lpUI();
}
function stageClass(){ const s=$('#lp-stage'); if(s) s.classList.toggle('sk-paused', !LP.playing && LP.awaiting<0); }
function lpSeek(t){
  if(!LP.L) return;
  t=Math.max(0, Math.min(lpDur(), t));
  if(LP.virtual){ LP.vbase=t; LP.vt0=performance.now(); }
  else if(LP.audio){ try{ LP.audio.currentTime=t; }catch(e){} }
  else LP.vbase=t;
  LP.ended = false;
  lpTick(true, t);
}
function goVirtual(tIn, wasIn, silentBuild){
  const t = tIn!=null ? tIn : (LP.audio ? LP.audio.currentTime : 0);
  if(wasIn!=null) LP.playing = wasIn;
  if(LP.audio){ try{ LP.audio.pause(); LP.audio.removeAttribute('src'); }catch(e){} }
  LP.virtual=true; LP.vbase=t||0; LP.vt0=performance.now(); LP.cc=true;
  const n=$('#lp-note');
  if(n && !silentBuild){ n.hidden=false; n.textContent = (LP.L && embeddedEl(LP.L))
    ? 'This browser could not play the lesson audio, so captions are on. Chrome, Edge and Firefox play it.'
    : 'Audio could not load here, so captions are on and the lesson plays silently.'; }
  if(LP.playing){ LP.vt0=performance.now(); lpLoop(); }
  lpTick(true); lpUI();
}
function lpLoop(){ cancelAnimationFrame(LP.raf); const f=()=>{ if(!LP.L || !LP.playing) return; lpTick(false); LP.raf=requestAnimationFrame(f); }; LP.raf=requestAnimationFrame(f); }
function lpClose(){
  if(LP.L){ lpSavePos(true); }
  cancelAnimationFrame(LP.raf);
  if(LP.audio){ try{ LP.audio.pause(); LP.audio.removeAttribute('src'); LP.audio.load(); }catch(e){} }
  if(LP.blobUrl){ try{ URL.revokeObjectURL(LP.blobUrl); }catch(e){} }
  Object.assign(LP, {L:null, audio:null, virtual:false, playing:false, scene:-1, sig:'', gate:{}, gs:{}, awaiting:-1, ended:false, srcStage:0, bytes:null, bytesP:null, blobUrl:null, sk:[], lastT:0, stars:0});
}
function lpSavePos(force){
  if(!LP.L || LP.L.preview) return;
  const now=Date.now(); if(!force && now-LP.lastSave<5000) return; LP.lastSave=now;
  const s = lessonStateW(LP.L.id);
  s.pos = LP.ended ? 0 : Math.round(lpTime()); s.seen=now; save();
}

/* --- timing lookup --- */
function beatsOf(sc){ return sc.beats.concat(sc.reveal||[]); }
function stateAt(t){
  const L=LP.L, T=L.timing.scenes;
  let si=0; for(let i=0;i<T.length;i++){ if(T[i].t0<=t+0.001) si=i; }
  const sc=L.scenes[si], tm=T[si], beats=beatsOf(sc);
  let bi=-1; tm.beats.forEach((b,i)=>{ if(b[0]<=t+0.05) bi=i; });
  let show=0, tell=false, answer=false, hl=null;
  for(let i=0;i<=Math.max(bi,0);i++){ const b=beats[i]; if(!b) continue; if(b.show!=null) show=b.show; if(b.tell) tell=true; if(b.answer) answer=true; }
  if(bi>=0 && beats[bi] && beats[bi].hl!=null) hl=beats[bi].hl;
  let cap = bi>=0 && t <= tm.beats[bi][1]+0.6 ? beats[bi].text : '';
  let who = bi>=0 && t <= tm.beats[bi][1]+0.3 ? (beats[bi].speaker||beats[bi].voice||'') : '';
  if(sc.type==='choice' && tm.ob) tm.ob.forEach((seg,k)=>seg.forEach((b,j)=>{ if(t>=b[0]-0.05 && t<=b[1]+0.6){ const ob=sc.options[k].beats[j]; cap=ob.text; who=t<=b[1]+0.3?(ob.speaker||ob.voice||''):''; hl=ob.hl!=null?ob.hl:null; } }));
  return {si, bi, show, tell, answer, hl, cap, who};
}

/* --- scene markup --- */
const SKDIM = {full:[160,72], half:[80,72], card:[100,56], title:[90,72], choice:[160,58]};
function canvasHTML(which, dims, extra){ return `<div class="sx-canvas" data-sk="${which}" data-dims="${dims[0]}x${dims[1]}"><div class="sx-fit" style="--ar:${dims[0]}/${dims[1]}">${extra||''}</div></div>`; }
function sceneHTML(sc, si){
  const T = sc.title ? `<h3 class="st-title">${esc(sc.title)}</h3>` : '';
  const it = (i, inner, cls) => `<div class="st-it ${cls||''}" data-i="${i}">${inner}</div>`;
  const split = (panel) => sc.draw && sc.draw.length ? `<div class="sx-split">${canvasHTML('main', SKDIM.half)}<div class="sx-panel">${panel}</div></div>` : panel;
  switch(sc.type){
    case 'title': return `<div class="sx-split sx-titlewrap"><div class="st-titlecard"><div class="st-eyebrow mono">Lesson ${esc(LP.L.id.slice(1))}</div><h2>${esc(sc.title)}</h2><p>${esc(sc.subtitle)}</p></div>${sc.draw&&sc.draw.length?canvasHTML('main', SKDIM.title):''}</div>`;
    case 'sketch': return T+canvasHTML('main', SKDIM.full);
    case 'term': return T+`<div class="sx-split">${canvasHTML('main', SKDIM.half)}<div class="sx-panel"><div class="sx-term">
        <div class="st-it sx-word" data-i="0"><span class="mono">${esc(sc.kind||'Term')}</span><b>${esc(sc.term)}</b></div>
        <div class="st-it sx-row" data-i="1"><span class="sx-k">In plain English</span><p>${esc(sc.plain)}</p></div>
        <div class="st-it sx-row" data-i="2"><span class="sx-k">Real life</span><p>${esc(sc.example)}</p></div>
        ${sc.exam?`<div class="st-it sx-row sx-exam" data-i="3"><span class="sx-k">${icon('triangle-alert','st-smic')} On the exam</span><p>${esc(sc.exam)}</p></div>`:''}
      </div></div></div>`;
    case 'bullets': return T+split(`<div class="st-list ${sc.items.length<=3&&!(sc.draw&&sc.draw.length)?'st-cols':''}">${sc.items.map((x,i)=>it(i, `${x.icon?icon(x.icon,'st-itic'):''}<div><b>${esc(x.label)}</b>${x.detail?`<span>${esc(x.detail)}</span>`:''}</div>`, 'st-card')).join('')}</div>`);
    case 'steps': return T+split(`<div class="st-steps ${sc.ladder?'st-ladder':''}">${(sc.ladder?sc.items.map((x,i)=>[x,i]).reverse():sc.items.map((x,i)=>[x,i])).map(([x,i])=>it(i, `<span class="st-num">${i+1}</span><div><b>${esc(x.label)}</b>${x.detail?`<span>${esc(x.detail)}</span>`:''}</div>`, 'st-card'+(sc.ladder?` st-rung" style="--rung:${i}`:''))).join('')}</div>`);
    case 'compare': return T+`<div class="st-compare c${sc.columns.length}">${sc.columns.map((c,i)=>it(i, `<div class="st-colh">${c.icon?icon(c.icon,'st-itic'):''}<b>${esc(c.name)}</b></div><ul>${c.points.map(p=>`<li>${esc(p)}</li>`).join('')}</ul>`, 'st-card')).join('')}</div>${sc.tell?`<div class="st-tell" data-tell>${icon('lightbulb','st-itic')}<span>${esc(sc.tell)}</span></div>`:''}`;
    case 'timeline': return T+`<div class="st-timeline">${sc.items.map((x,i)=>it(i, `<span class="st-at mono">${esc(x.at)}</span><span class="st-dot"></span><b class="tl-l">${esc(x.label)}</b>${x.detail?`<span class="tl-d">${esc(x.detail)}</span>`:''}`)).join('')}</div>`;
    case 'table': return T+`<div class="st-tablewrap"><table class="st-table"><thead><tr>${sc.columns.map(c=>`<th>${esc(c)}</th>`).join('')}</tr></thead><tbody>${sc.items.map((r,i)=>`<tr class="st-it" data-i="${i}">${r.map(c=>`<td>${esc(c)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
    case 'formula': return T+split(`${sc.given&&sc.given.length?`<div class="st-given">${sc.given.map(g=>`<span class="chip">${esc(g)}</span>`).join('')}</div>`:''}<div class="st-formula">${sc.items.map((x,i)=>it(i, `<span class="fl">${esc(x.label)}</span><span class="fx mono">${esc(x.expr)}</span><span class="fv">${esc(x.value)}</span>`, i===sc.items.length-1?'st-result':'')).join('')}</div>`);
    case 'scenario': return T+split(`<div class="st-story">${icon(sc.icon||'user','st-itic')}<p>${esc(sc.story)}</p></div><div class="st-list">${(sc.items||[]).map((x,i)=>it(i, `<span class="st-num">${i+1}</span><div><b>${esc(x.label)}</b>${x.detail?`<span>${esc(x.detail)}</span>`:''}</div>`, 'st-card')).join('')}</div><div class="st-answer" data-answer>${icon('circle-check','st-itic')}<span>${esc(sc.answer)}</span></div>`);
    case 'bignum': return T+split(`<div class="st-big n${sc.items.length}">${sc.items.map((x,i)=>it(i, `<span class="bv">${esc(x.value)}</span><span class="bl">${esc(x.label)}</span>`, 'st-card')).join('')}</div>`);
    case 'hook': return T+split(`<div class="st-hook">${icon('lightbulb','st-bigic')}<p class="hk">${esc(sc.hook)}</p></div><div class="st-list">${(sc.items||[]).map((x,i)=>it(i, `<span>${esc(x)}</span>`, 'st-card st-small')).join('')}</div>`);
    case 'recap': return `<h3 class="st-title">${esc(sc.title||'Key takeaways')}</h3>`+split(`<div class="st-list">${sc.items.map((x,i)=>it(i, `${icon('circle-check','st-itic')}<span>${esc(x)}</span>`, 'st-card')).join('')}</div>`);
    case 'quiz': return split(`<div class="st-quiz" id="gx-${si}">${quizHTML(sc, si)}</div>`);
    case 'swipe': return T+`<div class="gx-swipe" id="gx-${si}">${swipeHTML(sc, si)}</div>`;
    case 'sort': return T+`<div class="gx-sort" id="gx-${si}">${sortHTML(sc, si)}</div>`;
    case 'explore': return T+canvasHTML('main', SKDIM.full, `<div class="gx-spots" id="gx-spots-${si}"></div>`)+`<div class="gx-explore" id="gx-${si}">${exploreHTML(sc, si)}</div>`;
    case 'slider': return T+split(`<div class="gx-slider" id="gx-${si}">${sliderHTML(sc, si)}</div>`);
    case 'choice': return T+canvasHTML('main', SKDIM.choice)+`<div class="gx-choice" id="gx-${si}">${chooseHTML(sc, si)}</div>`;
  }
  return '';
}
const gateEyebrow = (label, ic) => `<div class="st-eyebrow mono">${icon(ic||'brain','st-smic')} ${esc(label)}</div>`;
function skipBtn(si){ return LP.gate[si] ? '' : `<button class="st-skip" data-act="lp-skip">Skip and show the answer</button>`; }

/* quiz */
function quizHTML(sc, si){
  const q=LP.gate[si];
  return `${gateEyebrow(sc.warmup?'Take a guess':'Quick check')}<p class="st-q">${esc(sc.q)}</p>
    <div class="st-choices">${sc.choices.map((c,i)=>{ let cls=''; if(q){ if(i===sc.answer) cls='right'; else if(i===q.pick) cls='wrong'; }
      return `<button class="st-choice ${cls}" data-act="lp-pick" data-i="${i}" ${q?'disabled':''}><span class="mono">${LETTERS[i]}</span><span>${esc(c)}</span></button>`; }).join('')}</div>
    <div class="st-why" ${q?'':'hidden'}>${q?`<b>${q.skip?'Answer:':q.pts?'Correct!':'Not quite.'}</b> ${esc(sc.why)}`:''}</div>
    ${q?'':`<button class="st-skip" data-act="lp-skip">Show the answer</button>`}`;
}
function lpPick(i){
  const si=LP.scene, sc=LP.L.scenes[si]; if(!sc || sc.type!=='quiz' || LP.gate[si]) return;
  const ok = i===sc.answer;
  SFX.play(ok?'ding':'buzz');
  gateDone(si, ok?1:0, {pick:i});
}

/* swipe: one card at a time, pick a side */
function swipeHTML(sc, si){
  const g=LP.gs[si] || (LP.gs[si]={i:0, picks:[]}), done=LP.gate[si];
  if(done || g.i>=sc.cards.length){
    const right=g.picks.filter((p,k)=>p===sc.cards[k].answer).length;
    return `${gateEyebrow('Your call','target')}<div class="gx-sum"><b>${done&&done.skip?'Answers':`${right} of ${sc.cards.length} right`}</b>
      <ol>${sc.cards.map((c,k)=>`<li class="${g.picks[k]===c.answer?'ok':g.picks[k]==null?'':'no'}"><span>${esc(c.text)}</span> <b>${esc(sc.options[c.answer])}</b></li>`).join('')}</ol></div>
      ${done?'':`<button class="btn primary" data-act="gx-swipe-done">Continue</button>`}`;
  }
  const c=sc.cards[g.i], pick=g.picks[g.i];
  return `${gateEyebrow(`Your call · ${g.i+1} of ${sc.cards.length}`,'target')}
    <div class="gx-card ${pick!=null?(pick===c.answer?'ok':'no'):''}">
      ${c.draw&&c.draw.length?canvasHTML('card'+g.i, SKDIM.card):''}
      <p class="gx-ct">${esc(c.text)}</p>
    </div>
    <div class="gx-opts">${sc.options.map((o,k)=>`<button class="btn gx-opt ${pick!=null&&k===c.answer?'right':''} ${pick===k&&k!==c.answer?'wrong':''}" data-act="gx-swipe" data-k="${k}" ${pick!=null?'disabled':''}>${esc(o)}</button>`).join('')}</div>
    ${pick!=null?`<div class="gx-why"><b>${pick===c.answer?'Right!':'Not quite.'}</b> ${esc(c.why)} <button class="btn small primary" data-act="gx-swipe-next">${g.i+1<sc.cards.length?'Next card':'See results'}</button></div>`:skipBtn(si)}`;
}
function gxSwipe(k){
  const si=LP.scene, sc=LP.L.scenes[si], g=LP.gs[si]; if(!g || LP.gate[si] || g.picks[g.i]!=null) return;
  g.picks[g.i]=k; SFX.play(k===sc.cards[g.i].answer?'ding':'buzz'); rerenderGate(si);
}
function gxSwipeNext(){ const si=LP.scene, g=LP.gs[si]; if(!g) return; g.i++; SFX.play('click'); rerenderGate(si); }
function gxSwipeDone(){ const si=LP.scene, sc=LP.L.scenes[si], g=LP.gs[si]; gateDone(si, g.picks.filter((p,k)=>p===sc.cards[k].answer).length); }

/* sort: drop each item in a bin */
function sortHTML(sc, si){
  const g=LP.gs[si] || (LP.gs[si]={place:{}, sel:null, checked:false}), done=LP.gate[si];
  const show = done || g.checked;
  const skipped = done && done.skip;
  const chip = (x,k) => { const ok=show && g.place[k]===x.bin;
    return `<button class="gx-chip ${g.sel===k?'sel':''} ${show?(skipped?'ans':ok?'ok':'no'):''}" data-act="gx-chip" data-k="${k}" ${show?'disabled':''}>${esc(x.text)}${show&&!ok?`<small>${esc(x.why||('Belongs in: '+sc.bins[x.bin].name))}</small>`:''}</button>`; };
  const tray = sc.items.map((x,k)=>[x,k]).filter(([x,k])=>!show && g.place[k]==null);
  const all = Object.keys(g.place).length===sc.items.length;
  return `${gateEyebrow('Sort it out','layers')}
    ${!show?`<p class="gx-hint">${g.sel!=null?'Now tap the box where it belongs.':'Tap a card, then tap a box. (Or drag it.)'}</p>`:''}
    <div class="gx-tray">${tray.map(([x,k])=>chip(x,k)).join('')}</div>
    <div class="gx-bins b${sc.bins.length}">${sc.bins.map((b,bi)=>`<div class="gx-bin ${g.sel!=null&&!show?'armed':''}" data-act="gx-bin" data-b="${bi}" role="button" tabindex="${g.sel!=null&&!show?0:-1}"><h4>${esc(b.name)}</h4>
      ${sc.items.map((x,k)=>[x,k]).filter(([x,k])=>(show?(skipped?x.bin===bi:(g.place[k]!=null?g.place[k]===bi:x.bin===bi)):g.place[k]===bi)).map(([x,k])=>chip(x,k)).join('')}</div>`).join('')}</div>
    ${show ? (done?'':`<div class="gx-why"><b>${sc.items.filter((x,k)=>g.place[k]===x.bin).length} of ${sc.items.length} in the right box.</b> <button class="btn small primary" data-act="gx-sort-done">Continue</button></div>`)
      : all ? `<button class="btn primary" data-act="gx-sort-check">Check my sorting</button>` : skipBtn(si)}`;
}
function gxChip(k){ const si=LP.scene, g=LP.gs[si]; if(!g || g.checked) return; if(g.place[k]!=null){ delete g.place[k]; } g.sel = g.sel===k ? null : k; SFX.play('click'); rerenderGate(si); }
function gxBin(b){ const si=LP.scene, g=LP.gs[si]; if(!g || g.sel==null || g.checked) return; g.place[g.sel]=b; g.sel=null; SFX.play('pop'); rerenderGate(si); }
function gxSortCheck(){ const si=LP.scene, sc=LP.L.scenes[si], g=LP.gs[si]; g.checked=true; const r=sc.items.filter((x,k)=>g.place[k]===x.bin).length; SFX.play(r===sc.items.length?'tada':r>=sc.items.length/2?'ding':'buzz'); rerenderGate(si); }
function gxSortDone(){ const si=LP.scene, sc=LP.L.scenes[si], g=LP.gs[si]; gateDone(si, sc.items.filter((x,k)=>g.place[k]===x.bin).length); }

/* explore: tap the hotspots on a drawing */
function exploreHTML(sc, si){
  const g=LP.gs[si] || (LP.gs[si]={seen:{}, cur:null}), done=LP.gate[si], n=Object.keys(g.seen).length;
  const sp = g.cur!=null ? sc.spots[g.cur] : null;
  return `<div class="gx-info ${sp?'on':''}">${sp?`<b>${esc(sp.label)}</b><span>${esc(sp.text)}</span>`:done?`<ul class="gx-all">${sc.spots.map(x=>`<li><b>${esc(x.label)}</b></li>`).join('')}</ul>`:`<span class="gx-hint">Tap each glowing spot on the drawing.</span>`}</div>
    <div class="gx-row"><span class="mono small">${done&&done.skip?'All spots shown':`${n} of ${sc.spots.length} found`}</span>
    ${done?'':(n===sc.spots.length?`<button class="btn small primary" data-act="gx-explore-done">Continue</button>`:skipBtn(si))}</div>`;
}
function placeSpots(si){
  const sc=LP.L.scenes[si], lay=$('#gx-spots-'+si), R=LP.sk[0]; if(!lay || !R) return;
  const g=LP.gs[si] || (LP.gs[si]={seen:{}, cur:null}), done=LP.gate[si];
  lay.innerHTML = sc.spots.map((s,k)=>{ const x=R.els.find(e=>e.el.id===s.on); if(!x) return ''; const b=x.bb, cx=(b[0]+b[2])/2/R.w*100, cy=(b[1]+b[3])/2/R.h*100;
    return `<button class="gx-spot ${g.seen[k]||done?'seen':''} ${g.cur===k?'cur':''}" style="left:${cx.toFixed(1)}%;top:${cy.toFixed(1)}%" data-act="gx-spot" data-k="${k}" aria-label="${esc(s.label)}"><span>${g.seen[k]||done?'✓':'+'}</span></button>`; }).join('');
}
function gxSpot(k){ const si=LP.scene, g=LP.gs[si]; if(!g) return; g.seen[k]=1; g.cur=k; SFX.play('pop');
  const sc=LP.L.scenes[si]; if(LP.sk[0]) SK.update(LP.sk[0], lpTime(), {hl:[sc.spots[k].on]}); LP.spotHl=sc.spots[k].on;
  rerenderGate(si); placeSpots(si); }
function gxExploreDone(){ const si=LP.scene; LP.spotHl=null; gateDone(si, 1); }

/* slider: a live calculator */
const CALC = {
  coins:{ x:'limit', f(p){ const req=p.value*p.pct/100, under=p.limit<req, raw=under? p.loss*p.limit/req : p.loss, pay=Math.max(0, Math.min(raw-p.ded, p.limit));
    return {pay, lines: under ? [[`Should carry: ${p.pct}% × ${money(p.value)}`, money(req)], [`Did ÷ should: ${money(p.limit)} ÷ ${money(req)}`, (p.limit/req).toFixed(3)], [`Loss × ratio: ${money(p.loss)} × ${(p.limit/req).toFixed(3)}`, money(raw)], [`Minus the ${money(p.ded)} deductible`, money(raw-p.ded)]]
      : [[`Should carry: ${p.pct}% × ${money(p.value)}`, money(req)], [`Carried ${money(p.limit)}: requirement met, no penalty`, '✓'], [`Loss minus the ${money(p.ded)} deductible`, money(p.loss-p.ded)]], result:['Insurer pays', money(pay)]}; }},
  horc:{ x:'limit', f(p){ const need=p.rc*0.8, ok=p.limit>=need, prop=p.loss*p.limit/need, pay= ok? Math.min(p.loss,p.limit) : Math.min(Math.max(p.acv,prop),p.limit);
    return {pay, lines: ok ? [[`80% of replacement cost: 80% × ${money(p.rc)}`, money(need)], [`Coverage A ${money(p.limit)} meets it: full replacement cost`, '✓']]
      : [[`Should carry: 80% × ${money(p.rc)}`, money(need)], [`Did ÷ should: ${money(p.limit)} ÷ ${money(need)}`, String(+(p.limit/need).toFixed(3))], [`Proportional: ${money(p.loss)} × ${+(p.limit/need).toFixed(3)}`, money(prop)], [`Actual cash value of the damage`, money(p.acv)], [`Pay the greater of the two`, money(Math.max(p.acv,prop))]], result:['Insurer pays (no deductible shown)', money(pay)]}; }},
  deductible:{ x:'loss', f(p){ const pay=Math.max(0, Math.min(p.loss-p.ded, p.limit||Infinity));
    return {pay, lines:[[`Loss`, money(p.loss)], [`Minus your deductible`, '− '+money(p.ded)]].concat(p.limit?[[`Capped at the limit`, money(p.limit)]]:[]), result:['Insurer pays', money(pay)]}; }},
  prorata:{ x:'loss', f(p){ const tot=p.a+p.b, sa=Math.min(p.a, p.loss*p.a/tot), sb=Math.min(p.b, p.loss*p.b/tot);
    return {pay:sa, lines:[[`Total insurance: ${money(p.a)} + ${money(p.b)}`, money(tot)], [`${p.na||'Policy A'} share: ${money(p.a)} ÷ ${money(tot)}`, Math.round(p.a/tot*100)+'%'], [`${p.nb||'Policy B'} pays`, money(sb)]], result:[`${p.na||'Policy A'} pays`, money(sa)]}; }},
  split:{ x:'inj1', f(p){ const inj=[p.inj1].concat(p.others||[]), each=inj.map(v=>Math.min(v,p.pp)), sum=each.reduce((a,b)=>a+b,0), pay=Math.min(sum,p.pa);
    return {pay, lines: inj.map((v,i)=>[`Person ${i+1}: ${money(v)}, capped at ${money(p.pp)} per person`, money(each[i])]).concat([[`Total, capped at ${money(p.pa)} per accident`, money(pay)]]), result:['Policy pays for injuries', money(pay)]}; }},
  wcprem:{ x:'payroll', f(p){ const manual=p.payroll/100*p.rate, mod=manual*p.mod;
    return {pay:mod, lines:[[`Payroll ÷ 100: ${money(p.payroll)} ÷ 100`, (p.payroll/100).toLocaleString('en-US')], [`× rate ${'$'+p.rate.toFixed(2)} per $100`, money(manual)], [`× experience mod ${p.mod.toFixed(2)}`, money(mod)]], result:['Premium', money(mod)]}; }},
  lossratio:{ x:'losses', f(p){ const r=p.losses/p.premium*100;
    return {pay:r, lines:[[`Losses ÷ earned premium: ${money(p.losses)} ÷ ${money(p.premium)}`, r.toFixed(1)+'%']], result:['Loss ratio', Math.round(r)+'%']}; }},
  acv:{ x:'age', f(p){ const dep=p.rc*p.age/p.life, a=p.rc-dep;
    return {pay:a, lines:[[`Depreciation: ${money(p.rc)} × ${p.age} ÷ ${p.life} years`, money(dep)], [`Replacement cost minus depreciation`, money(a)]], result:['Actual cash value', money(a)]}; }},
};
function sliderVals(sc, si){ const g=LP.gs[si] || (LP.gs[si]={v:sc.var.start, hit:false}); const p=Object.assign({}, sc.params); p[sc.var.key||CALC[sc.calc].x]=g.v; return {g, p, r:CALC[sc.calc].f(p)}; }
function goalMet(sc, r){ const G=sc.goal; if(!G) return false; const v=r.pay; return G.op==='eq' ? Math.abs(v-G.value)<0.5 : G.op==='lte' ? v<=G.value+0.5 : v>=G.value-0.5; }
function sliderHTML(sc, si){
  const {g, r} = sliderVals(sc, si), done=LP.gate[si], fmt=sc.var.money===false ? (v=>Number(v).toLocaleString('en-US')) : money;
  return `${gateEyebrow('Try it','calculator')}${sc.goal?`<p class="gx-goal">${esc(sc.goal.text)}</p>`:''}
    <label class="gx-sl"><span>${esc(sc.var.label)}: <b class="mono" id="gx-v-${si}">${fmt(g.v)}</b></span>
      <input type="range" min="${sc.var.min}" max="${sc.var.max}" step="${sc.var.step}" value="${g.v}" data-gx-slider="${si}" aria-label="${esc(sc.var.label)}"></label>
    <div class="gx-calc" id="gx-calc-${si}">${calcLines(r)}</div>
    <div class="gx-row">${g.hit?`<span class="gx-ok">${icon('circle-check','st-smic')} ${esc(sc.goal.done||'You found it!')}</span>`:''}
      ${done?'':`<button class="btn small ${g.hit||!sc.goal?'primary':''}" data-act="gx-slider-done">${g.hit||!sc.goal?'Continue':'Skip and continue'}</button>`}</div>`;
}
function calcLines(r){ return r.lines.map(l=>`<div class="gx-line"><span>${esc(l[0])}</span><b class="mono">${esc(l[1])}</b></div>`).join('')+`<div class="gx-line gx-res"><span>${esc(r.result[0])}</span><b>${esc(r.result[1])}</b></div>`; }
function gxSlider(si, v){
  const sc=LP.L.scenes[si]; const g=LP.gs[si]; g.v=+v; const {r}=sliderVals(sc, si);
  const fmt=sc.var.money===false ? (x=>Number(x).toLocaleString('en-US')) : money;
  const lv=$('#gx-v-'+si); if(lv) lv.textContent=fmt(g.v); const c=$('#gx-calc-'+si); if(c) c.innerHTML=calcLines(r);
  if(sc.goal && !g.hit && goalMet(sc, r)){ g.hit=true; SFX.play('cash'); rerenderGate(si); }
}
function gxSliderDone(){ const si=LP.scene, sc=LP.L.scenes[si], g=LP.gs[si] || (LP.gs[si]={v:sc.var.start, hit:false});
  if(sc.goal && !g.hit){ for(let v=sc.var.min; v<=sc.var.max+1e-9; v+=sc.var.step){ g.v=v; if(goalMet(sc, sliderVals(sc, si).r)) break; } }   // show the answer the reveal talks about
  gateDone(si, g.hit ? 1 : 0); }

/* choice: pick what the character does, watch what happens (wrong picks end in a FAIL, try again) */
function choiceState(si){ return LP.gs[si] || (LP.gs[si]={phase:'ask', k:null, tried:{}, first:null}); }
function chooseHTML(sc, si){
  const g=choiceState(si), done=LP.gate[si], w=sc.options.findIndex(o=>o.ok), nf=sc.options.length-1, found=Object.keys(g.tried).filter(k=>!sc.options[k].ok).length;
  const eb=gateEyebrow(sc.ask||'What would you do?','target');
  if(done) return `${eb}<div class="gx-win"><span class="gx-winword">${done.skip?'The right move':done.pts?'Nailed it!':'You got there!'}</span><p><b>${esc(sc.options[w].label)}.</b> ${esc(sc.options[w].win)}</p>${found&&!done.skip?`<span class="mono small">Fails found: ${found} of ${nf}</span>`:''}</div>`;
  if(g.phase==='out') return `${eb}<p class="gx-hint gx-watch">Let's see what happens…</p>`;
  if(g.phase==='fail'){ const o=sc.options[g.k]; return `${eb}<div class="gx-fail"><span class="gx-failword">FAIL</span><p>${esc(o.fail)}</p><button class="btn primary" data-act="gx-retry">Try again</button><span class="mono small">Fails found: ${found} of ${nf}</span></div>`; }
  return `${eb}<div class="gx-chs n${sc.options.length}">${sc.options.map((o,k)=>`<button class="gx-ch ${g.tried[k]?'tried':''}" data-act="gx-choose" data-k="${k}"><span class="gx-chn">${k+1}</span><span>${esc(o.label)}</span>${g.tried[k]?'<em>FAIL</em>':''}</button>`).join('')}</div>
    <div class="gx-row">${found?`<span class="mono small">Fails found: ${found} of ${nf}</span>`:'<span></span>'}${skipBtn(si)}</div>`;
}
function choiceEls(sc, si){
  const g=choiceState(si), done=LP.gate[si], w=sc.options.findIndex(o=>o.ok);
  if(done) return {els:sc.options[w].draw, mode:'static'};
  if(g.phase==='out') return {els:sc.options[g.k].draw, mode:'out', k:g.k};
  if(g.phase==='fail'){ const o=sc.options[g.k], fa=o.failAt||sc.failAt||[136,10]; return {els:o.draw.concat([{p:'stamp', text:'FAIL', x:fa[0], y:fa[1], color:'red', size:8, rot:-10}]), mode:'static'}; }
  return {els:sc.draw, mode:'ask'};
}
function gxChoose(k){
  const si=LP.scene, sc=LP.L.scenes[si], g=choiceState(si); if(LP.gate[si] || g.phase==='out') return;
  const seg=LP.L.timing.scenes[si].ob[k];
  g.phase='out'; g.k=k; g.tried[k]=1; if(g.first==null) g.first=k;
  SFX.play('click'); LP.awaiting=-1; LP.scene=-1;
  lpSeek(seg[0][0]-0.12); lpPlay();
}
function gxRetry(){
  const si=LP.scene, g=choiceState(si); if(g.phase!=='fail') return;
  g.phase='ask'; g.k=null; LP.scene=-1; SFX.play('boing');
  lpSeek(LP.L.timing.scenes[si].q); LP.awaiting=si; stageClass();
  const b=$('#lp-stage .gx-ch'); if(b) b.focus({preventScroll:true});
}

/* gate plumbing */
function rerenderGate(si){
  const sc=LP.L.scenes[si], box=$('#gx-'+si); if(!box) return;
  const html = sc.type==='quiz'?quizHTML(sc,si):sc.type==='swipe'?swipeHTML(sc,si):sc.type==='sort'?sortHTML(sc,si):sc.type==='explore'?exploreHTML(sc,si):sc.type==='choice'?chooseHTML(sc,si):sliderHTML(sc,si);
  box.innerHTML=html; mountCanvases(box, sc, si, true); fitScene();
}
function gateDone(si, pts, extra){
  const L=LP.L, sc=L.scenes[si]; if(LP.gate[si]) return;
  const max=gateMax(sc);
  LP.gate[si]=Object.assign({pts, max}, extra||{});
  if(!L.preview){ const s=lessonStateW(L.id); if(s.gates[si]==null){ s.gates[si]=pts; if(pts) addXP(pts); } save(); }
  LP.stars += pts; hud(pts>0);
  if(sc.type==='quiz') rerenderGate(si); else rerenderGate(si);
  if(sc.type==='explore') placeSpots(si);
  const tm=L.timing.scenes[si];
  LP.awaiting=-1;
  if(lpTime() < tm.r){ lpSeek(tm.r); }
  lpPlay();
}
function lpSkip(){
  const si=LP.scene, sc=LP.L&&LP.L.scenes[si]; if(!sc || LP.gate[si]) return;
  if(sc.type==='slider' && sc.goal){ const g=LP.gs[si] || (LP.gs[si]={v:sc.var.start, hit:false}); for(let v=sc.var.min; v<=sc.var.max+1e-9; v+=sc.var.step){ g.v=v; if(goalMet(sc, sliderVals(sc, si).r)) break; } }   // show the answer the reveal talks about
  LP.gate[si]={pts:0, max:gateMax(sc), skip:true, pick:-1};
  LP.awaiting=-1; rerenderGate(si); if(sc.type==='explore') placeSpots(si);
  lpSeek(LP.L.timing.scenes[si].r); lpPlay();
}
function hud(bump){ const h=$('#lp-hud'); if(!h) return; h.innerHTML=`★ <b>${LP.stars}</b>`; if(bump){ h.classList.remove('bump'); void h.offsetWidth; h.classList.add('bump'); } }

/* --- drawings --- */
function sceneBeatTexts(sc){ return beatsOf(sc).map(b=>b.text); }
function mountCanvases(root, sc, si, gateOnly){
  root.querySelectorAll('[data-sk]').forEach(h=>{
    const which=h.dataset.sk; if(gateOnly && which==='main') return;
    if(h.querySelector('svg.sk')) return;
    const dims=h.dataset.dims.split('x').map(Number);
    const ch = which==='main' && sc.type==='choice' ? choiceEls(sc, si) : null;
    const els = ch ? ch.els : which==='main' ? sc.draw : which.startsWith('card') ? sc.cards[+which.slice(4)].draw : null;
    if(!els || !els.length || typeof SK==='undefined') return;
    const R=SK.render(els, {w:dims[0], h:dims[1], key:LP.L.id+':'+si+':'+which+(ch&&ch.k!=null?':o'+ch.k:''), alt:sc.alt||sc.title||''});
    h.querySelector('.sx-fit').prepend(R.svg);
    const tm=LP.L.timing.scenes[si];
    if(ch && ch.mode==='static'){ SK.showAll(R); }
    else if(ch && ch.mode==='out'){ SK.plan(R, tm.ob[ch.k], sc.options[ch.k].beats.map(b=>b.text), tm.ocues && tm.ocues[ch.k]); LP.sk.push(R); }
    else if(which==='main'){ SK.plan(R, tm.beats, sceneBeatTexts(sc), tm.cues); LP.sk.push(R); }
    else { R.els.forEach((x,k)=>setTimeout(()=>{ x.g.classList.add('in'); if(x.el.sfx) SFX.play(x.el.sfx); }, 120+k*260)); }
  });
}

function layoutSrc(){
  const src=$('#lp-src'), box=$('#lp-scene'), cap=$('#lp-cap'); if(!src || !box) return;
  const h = src.textContent ? src.offsetHeight : 0, gap = Math.max(10, src.offsetParent ? parseFloat(getComputedStyle(src).bottom) || 10 : 10);
  const narrow = box.clientWidth < 560, capRoom = (LP.cc || LP.virtual) ? (cap ? parseFloat(getComputedStyle(cap).fontSize) * (narrow ? 5 : 3.5) : 48) : 0;   // keep captions off the activity buttons
  box.style.paddingBottom = Math.max(54, h + gap + 18 + capRoom) + 'px';
  if(cap) cap.style.bottom = (h + gap + 8) + 'px';
}
function fitScene(){
  layoutSrc();
  const box=$('#lp-scene'), inner=box && box.firstElementChild; if(!inner) return;
  inner.style.fontSize='';
  const panel = box.querySelector('.sx-panel');
  const over = () => box.scrollHeight>box.clientHeight+1 || (panel && panel.scrollHeight>panel.clientHeight+1);
  box.classList.add('fitting');   // measure without the slide-in offsets
  let f=1; for(let k=0; k<8 && over(); k++){ f-=0.06; inner.style.fontSize=f.toFixed(2)+'em'; }
  box.classList.remove('fitting');
}
let fitTimer=0;
window.addEventListener('resize', ()=>{ clearTimeout(fitTimer); fitTimer=setTimeout(()=>{ if(LP.L) fitScene(); }, 120); });
document.addEventListener('fullscreenchange', ()=>{ if(LP.L) setTimeout(fitScene, 60); });
document.addEventListener('visibilitychange', ()=>{ if(document.hidden && LP.L && LP.virtual && LP.playing) lpPause(); });
function lpTick(force, tOverride){
  if(!LP.L) return;
  const t = tOverride!=null ? tOverride : lpTime(), L=LP.L, T=L.timing.scenes;
  const s = stateAt(t);
  const sc=L.scenes[s.si], tm=T[s.si], isGate=GATES.has(sc.type);
  // choice: an outcome plays, then FAIL (wait for "Try again") or success (continue to the explanation)
  let chOut = false;
  if(sc.type==='choice' && !LP.gate[s.si]){
    const g=choiceState(s.si), ob=tm.ob||[];
    if(g.phase==='out'){
      const seg=ob[g.k], end=seg[seg.length-1][1]+0.3;
      if(t >= end && t < tm.r+0.5){
        if(sc.options[g.k].ok){ g.phase='win'; SFX.play('tada'); gateDone(s.si, g.first===g.k?1:0, {pick:g.k}); return; }
        g.phase='fail'; SFX.play('buzz'); lpPause(); LP.awaiting=s.si; stageClass(); force=true;
      } else if(t < seg[0][0]-0.4 || t >= tm.r+0.5){ g.phase='ask'; g.k=null; force=true; }
      else chOut = true;
    } else if(g.phase==='ask' && LP.playing && ob.some(seg=>seg.length && t>=seg[0][0]-0.05 && t<tm.r)){
      lpPause(); LP.awaiting=s.si; stageClass(); if(!LP.virtual && LP.audio){ try{ LP.audio.currentTime=tm.q; }catch(e){} } else LP.vbase=tm.q; force=true;
    }
  }
  // gate: stop at the end of the prompt until the learner finishes the activity
  if(isGate && !chOut && !(sc.type==='choice' && LP.gs[s.si] && LP.gs[s.si].phase==='fail') && !LP.gate[s.si] && LP.playing && t >= tm.q-0.03 && t < tm.r){
    lpPause(); LP.awaiting=s.si; stageClass(); if(!LP.virtual && LP.audio){ try{ LP.audio.currentTime=tm.q; }catch(e){} } else LP.vbase=tm.q;
    const b=$('#lp-stage .st-q, #lp-stage .gx-opt, #lp-stage .gx-chip, #lp-stage .gx-spot, #lp-stage [data-gx-slider], #lp-stage .gx-ch'); if(b){ if(!b.matches('button,input')) b.tabIndex=-1; b.focus({preventScroll:true}); }
  }
  if(isGate && !LP.gate[s.si] && t >= tm.r){ LP.gate[s.si]={pts:0, max:gateMax(sc), skip:true, pick:-1}; if(LP.awaiting===s.si) LP.awaiting=-1; force=true; }
  const jump = force || Math.abs(t-LP.lastT) > 0.75; LP.lastT=t;
  if(s.si!==LP.scene || force){
    if(s.si!==LP.scene){ LP.awaiting = (isGate && !LP.gate[s.si] && t>=tm.q-0.03 && t<tm.r && !(sc.type==='choice' && LP.gs[s.si] && LP.gs[s.si].phase==='out')) ? s.si : -1; LP.spotHl=null; }
    LP.scene=s.si; LP.sk=[];
    const src=$('#lp-src'); if(src) src.textContent = sc.src ? 'Source: '+sc.src : '';
    const box=$('#lp-scene'); if(box){ box.className='st-scene t-'+sc.type; box.innerHTML='<div class="st-inner">'+sceneHTML(sc, s.si)+'</div>'; box.scrollTop=0; mountCanvases(box, sc, s.si, false); if(sc.type==='explore') placeSpots(s.si); fitScene(); }
    LP.sig='';
  }
  const sig = [s.si,s.show,s.hl,s.tell,s.answer].join('|');
  if(sig!==LP.sig){
    LP.sig=sig;
    document.querySelectorAll('#lp-scene .st-it').forEach(e=>{ const i=+e.dataset.i; e.classList.toggle('in', i<s.show || (sc.type==='term' && s.show===0 && false)); e.classList.toggle('hl', i===s.hl); });
    const tl=$('#lp-scene [data-tell]'); if(tl) tl.classList.toggle('in', s.tell);
    const an=$('#lp-scene [data-answer]'); if(an) an.classList.toggle('in', s.answer);
  }
  if(LP.sk.length){
    const hl = LP.spotHl ? [LP.spotHl] : typeof s.hl==='string' ? [s.hl] : Array.isArray(s.hl) ? s.hl : null;
    LP.sk.forEach(R=>SK.update(R, t, {instant: jump, hl, onShow: x=>{ if(!LP.playing) return; const k=x.el.sfx || (x.el.p==='stamp'?'stamp':null); if(k) SFX.play(k); },
      onMove: x=>{ if(LP.playing && x.el.move.sfx) SFX.play(x.el.move.sfx); }}));
  }
  const cap=$('#lp-cap'); if(cap){ const on=(LP.cc||LP.virtual) && s.cap; cap.hidden=!on; if(on && cap.textContent!==s.cap) cap.textContent=s.cap; cap.dataset.who=s.who&&s.who!=='narrator'?castName(s.who):''; }
  const r=$('#lp-range'); if(r && document.activeElement!==r) r.value=t.toFixed(1);
  const tt=$('#lp-time'); if(tt) tt.textContent=mmss(t)+' / '+mmss(lpDur());
  const fill=$('#lp-fill'); if(fill) fill.style.width=(lpDur()? t/lpDur()*100 : 0)+'%';
  if(LP.playing) lpSavePos(false);
  if(LP.playing && t >= lpDur()-0.05) lpFinish();
}
function lpUI(){
  const b=$('#lp-play'); if(b){ b.innerHTML = icon(LP.playing?'pause':'play') + `<span class="sr">${LP.playing?'Pause':'Play'}</span>`; b.setAttribute('aria-label', LP.playing?'Pause':'Play'); }
  const cc=$('#lp-cc'); if(cc) cc.setAttribute('aria-pressed', String(!!LP.cc));
  const fx=$('#lp-sfx'); if(fx){ fx.setAttribute('aria-pressed', String(SFX.on())); fx.innerHTML=icon(SFX.on()?'volume-2':'volume-x')+'<span class="sr">Sound effects</span>'; }
}
function hideOverlay(){ const o=$('#lp-over'); if(o) o.hidden=true; }
function lpFinish(){
  if(!LP.L || LP.ended) return;
  LP.ended=true; LP.playing=false; cancelAnimationFrame(LP.raf); stageClass();
  if(!LP.virtual && LP.audio) LP.audio.pause();
  const L=LP.L;
  let first=false;
  if(!L.preview){ const s=lessonStateW(L.id); first=!s.done; s.done = s.done || Date.now(); s.pos=0; }
  const smax=lessonStarsMax(L), stars=LP.stars;
  SFX.play('tada');
  if(first){ addXP(20); toast(`Lesson complete: <b>+20 XP</b>`); }
  if(!L.preview){ checkBadges(); save(); }
  lpUI();
  const nx = LESSONS[LESSONS.indexOf(L)+1];
  const o=$('#lp-over');
  if(o){ o.hidden=false; o.innerHTML=`<div class="st-end"><div class="st-eyebrow mono">Lesson ${esc(L.id.slice(1))} complete</div><h2>${esc(L.title)}</h2>
    <div class="st-stars" aria-label="${stars} of ${smax} stars">${'★'.repeat(Math.min(stars,30))}<span>${'★'.repeat(Math.max(0,Math.min(smax,30)-Math.min(stars,30)))}</span></div>
    <p>${smax?`You earned ${stars} of ${smax} stars in the activities. `:''}Lock it in with ${L.check.length} exam-style questions from the bank.</p>
    <div class="row" style="justify-content:center"><button class="btn primary" data-act="lp-check">Check yourself (${L.check.length})</button>
    ${nx?`<button class="btn" data-act="lesson" data-id="${nx.id}">Next: ${esc(nx.title)}</button>`:''}
    <button class="btn ghost" data-act="lp-replay">Watch again</button></div></div>`; }
}
function openLesson(id, opts){
  lpClose();
  const L=(opts && opts.lesson) || LBY[id]; if(!L) return;
  LP.L=L; LP.gate={}; LP.gs={}; LP.stars=0; LP.cc = !!(P.settings.captions); LP.rate = P.settings.lessonRate || 1;
  const el=$('#view-watch');
  const st=L.preview?null:lessonState(id), resume = st && !st.done && st.pos>5 && st.pos<L.timing.dur-5 ? st.pos : 0;   // no resume at the very end
  const marks = L.timing.scenes.map((s,i)=>`<span class="lp-mark ${GATES.has(L.scenes[i].type)?'q':''}" style="left:${(s.t0/L.timing.dur*100).toFixed(2)}%"></span>`).join('');
  const sources = (L.sources||[]).map(esc).join('; ');
  el.innerHTML = `<div class="lp stack">
    <div class="row" style="justify-content:space-between;align-items:center;gap:10px">
      <button class="btn ghost small" data-act="watch-list">${icon('chevron-left','btn-ic')} All lessons</button>
      <span class="mono small muted">${esc(SEC[L.sec]?SEC[L.sec].name:'')}</span>
    </div>
    <h2 style="margin:0">${esc(L.title)}</h2>
    <div class="stage wb" id="lp-stage">
      <div class="st-scene" id="lp-scene"></div>
      <div class="st-hud mono" id="lp-hud" title="Stars earned in this lesson">★ <b>0</b></div>
      <div class="st-src mono" id="lp-src"></div>
      <div class="st-cap" id="lp-cap" hidden aria-live="off"></div>
      <div class="st-over" id="lp-over"><div class="st-start">
        <div class="st-eyebrow mono">Lesson ${esc(L.id.slice(1))} · ${mmss(L.timing.dur)} · ${gateCount(L)} activities</div>
        <h2>${esc(L.title)}</h2>
        <ul>${L.objectives.map(o=>`<li>${esc(o)}</li>`).join('')}</ul>
        <button class="btn primary cta-big" data-act="lp-start">${icon('play','btn-ic')} ${resume?`Resume at ${mmss(resume)}`:'Play lesson'}</button>
        ${resume?`<button class="st-skip" data-act="lp-restart">Start from the beginning</button>`:''}
        <p class="small st-tip">Sound on. The video pauses for activities: tap, sort and slide to keep going.</p>
      </div></div>
    </div>
    <p class="small muted" id="lp-note" hidden></p>
    <div class="lp-bar"><div class="lp-track"><span class="lp-fill" id="lp-fill"></span>${marks}</div>
      <input type="range" id="lp-range" min="0" max="${L.timing.dur}" step="0.1" value="0" aria-label="Lesson position"></div>
    <div class="lp-ctrl">
      <button class="btn small" data-act="lp-prev" aria-label="Previous scene">${icon('skip-back')}</button>
      <button class="btn primary lp-pp" id="lp-play" data-act="lp-toggle" aria-label="Play">${icon('play')}</button>
      <button class="btn small" data-act="lp-next" aria-label="Next scene">${icon('skip-forward')}</button>
      <span class="mono small" id="lp-time">0:00 / ${mmss(L.timing.dur)}</span>
      <span class="lp-sp"></span>
      <label class="small muted" for="lp-rate">Speed <select id="lp-rate">${[0.75,1,1.25,1.5,1.75].map(r=>`<option value="${r}" ${r===LP.rate?'selected':''}>${r}×</option>`).join('')}</select></label>
      <button class="btn small" id="lp-sfx" data-act="lp-sfx" aria-pressed="true" title="Sound effects"></button>
      <button class="btn small" id="lp-cc" data-act="lp-cc" aria-pressed="${LP.cc}" title="Captions">CC</button>
      ${document.fullscreenEnabled?`<button class="btn small" data-act="lp-full" aria-label="Full screen">${icon('maximize')}</button>`:''}
    </div>
    <div class="row" style="gap:8px"><button class="btn" data-act="lp-check">Check yourself (${L.check.length} questions)</button>
      <button class="btn ghost" data-act="lp-guide">Read this in the study guide</button></div>
    <details class="panel lp-trans"><summary>Transcript</summary>
      ${L.scenes.map((sc,si)=>`<div class="lp-tsc"><button class="linkish mono small" data-act="lp-goto" data-si="${si}">${mmss(L.timing.scenes[si].t0)}</button> ${beatsOf(sc).map(b=>(b.voice&&b.voice!=='narrator'?`<b>${esc(b.speaker||castName(b.voice))}:</b> `:'')+esc(b.text)).join(' ')}</div>`).join('')}
      <p class="small muted" style="margin:10px 0 0">Sources: ${sources}</p>
    </details>
  </div>`;
  startSources(L);
  $('#lp-range').addEventListener('input', e=>{ LP.awaiting=-1; lpSeek(+e.target.value); });
  $('#lp-rate').addEventListener('change', e=>{ const t=lpTime(); LP.rate=+e.target.value; P.settings.lessonRate=LP.rate; save(); if(LP.virtual){ LP.vbase=t; LP.vt0=performance.now(); } else if(LP.audio) LP.audio.playbackRate=LP.rate; });
  const stage=$('#lp-stage');
  stage.addEventListener('input', e=>{ const s=e.target.closest('[data-gx-slider]'); if(s) gxSlider(+s.dataset.gxSlider, s.value); });
  sortDrag(stage);
  LP.scene=-1; lpSeek(resume); lpUI(); hud(false); stageClass();
  if(opts && opts.autoplay){ lpPlay(); }
}
const CAST_NAMES = {dana:'Dana', sam:'Sam', jen:'Jen', tony:'Tony', rosa:'Rosa', kid:'Kid', adjuster:'Adjuster', judge:'Judge', thief:'Thief', worker:'Worker', doctor:'Doctor', boss:'Boss', neighbor:'Neighbor', grandma:'Grandma', regulator:'Regulator'};
function castName(v){ return CAST_NAMES[v] || v; }   // a beat's own "speaker" name passes through unchanged
function sortDrag(stage){
  let drag=null;
  stage.addEventListener('pointerdown', e=>{ const c=e.target.closest('.gx-chip'); if(!c || c.disabled) return; drag={k:+c.dataset.k, x:e.clientX, y:e.clientY, el:c, moved:false}; });
  stage.addEventListener('pointermove', e=>{ if(!drag) return; const dx=e.clientX-drag.x, dy=e.clientY-drag.y; if(!drag.moved && Math.hypot(dx,dy)>8){ drag.moved=true; drag.el.classList.add('dragging'); try{ drag.el.setPointerCapture(e.pointerId); }catch(_){} }
    if(drag.moved){ drag.el.style.transform=`translate(${dx}px,${dy}px)`; stage.querySelectorAll('.gx-bin').forEach(b=>{ const r=b.getBoundingClientRect(); b.classList.toggle('over', e.clientX>=r.left&&e.clientX<=r.right&&e.clientY>=r.top&&e.clientY<=r.bottom); }); } });
  const end=e=>{ if(!drag) return; const d=drag; drag=null; if(!d.moved) return; d.el.style.transform=''; d.el.classList.remove('dragging'); let hit=null;
    stage.querySelectorAll('.gx-bin').forEach(b=>{ const r=b.getBoundingClientRect(); if(e.clientX>=r.left&&e.clientX<=r.right&&e.clientY>=r.top&&e.clientY<=r.bottom) hit=+b.dataset.b; b.classList.remove('over'); });
    const si=LP.scene, g=LP.gs[si]; if(g && hit!=null && !g.checked){ g.place[d.k]=hit; g.sel=null; SFX.play('pop'); rerenderGate(si); } d.el._noclick=true; setTimeout(()=>{ d.el._noclick=false; }, 0); };
  stage.addEventListener('pointerup', end); stage.addEventListener('pointercancel', end);
}
function lpScene(d){
  if(!LP.L) return;
  const T=LP.L.timing.scenes, t=lpTime(), cur=stateAt(t).si;
  let to = d<0 ? (t - T[cur].t0 > 2 ? cur : Math.max(0,cur-1)) : Math.min(T.length-1, cur+1);
  if(d>0 && cur===T.length-1){ lpSeek(lpDur()); lpFinish(); return; }
  LP.awaiting=-1; lpSeek(T[to].t0);
}
function lessonActs(act, b){
  if(act==='watch-list'){ lpClose(); renderWatch(); window.scrollTo({top:0}); return true; }
  if(act==='lesson'){ if(VIEW!=='watch') go('watch',{id:b.dataset.id}); else { openLesson(b.dataset.id); window.scrollTo({top:0}); } return true; }
  if(act==='watch-next'){ const n=nextLesson(); if(n) go('watch',{id:n.id}); else go('watch'); return true; }
  if(act==='lp-start'){ hideOverlay(); lpPlay(); return true; }
  if(act==='lp-restart'){ lpSeek(0); lpPlay(); return true; }
  if(act==='lp-replay'){ LP.gate={}; LP.gs={}; LP.stars=0; hud(false); LP.ended=false; lpSeek(0); lpPlay(); return true; }
  if(act==='lp-toggle'){ if(LP.awaiting>=0) return true; LP.playing ? lpPause() : lpPlay(); return true; }
  if(act==='lp-prev'){ lpScene(-1); return true; }
  if(act==='lp-next'){ lpScene(1); return true; }
  if(act==='lp-pick'){ lpPick(+b.dataset.i); return true; }
  if(act==='lp-skip'){ lpSkip(); return true; }
  if(act==='gx-swipe'){ gxSwipe(+b.dataset.k); return true; }
  if(act==='gx-swipe-next'){ gxSwipeNext(); return true; }
  if(act==='gx-swipe-done'){ gxSwipeDone(); return true; }
  if(act==='gx-chip'){ if(b._noclick) return true; const bin=b.closest('.gx-bin'), g=LP.gs[LP.scene];
    if(bin && g && g.sel!=null && g.sel!==+b.dataset.k){ gxBin(+bin.dataset.b); return true; }   // dropping onto a box that already holds cards
    gxChip(+b.dataset.k); return true; }
  if(act==='gx-bin'){ gxBin(+b.dataset.b); return true; }
  if(act==='gx-sort-check'){ gxSortCheck(); return true; }
  if(act==='gx-sort-done'){ gxSortDone(); return true; }
  if(act==='gx-spot'){ gxSpot(+b.dataset.k); return true; }
  if(act==='gx-explore-done'){ gxExploreDone(); return true; }
  if(act==='gx-slider-done'){ gxSliderDone(); return true; }
  if(act==='gx-choose'){ gxChoose(+b.dataset.k); return true; }
  if(act==='gx-retry'){ gxRetry(); return true; }
  if(act==='lp-goto'){ LP.awaiting=-1; lpSeek(LP.L.timing.scenes[+b.dataset.si].t0); hideOverlay(); return true; }
  if(act==='lp-cc'){ LP.cc=!LP.cc; P.settings.captions=LP.cc; save(); lpTick(true); fitScene(); lpUI(); return true; }
  if(act==='lp-sfx'){ P.settings.sfx = !SFX.on(); save(); lpUI(); if(SFX.on()) SFX.play('pop'); return true; }
  if(act==='lp-full'){ const s=$('#lp-stage'); if(document.fullscreenElement) document.exitFullscreen(); else if(s && s.requestFullscreen) s.requestFullscreen().catch(()=>{}); return true; }
  if(act==='lp-check'){ const L=LP.L; lpPause(); go('practice',{ids:L.check, label:'Lesson check: '+L.title}); return true; }
  if(act==='lp-guide'){ const g=LP.L.guide; lpPause(); go('study',{sec:g}); return true; }
  return false;
}
function lessonKeys(e, k){
  if(VIEW!=='watch' || !LP.L) return false;
  const qs = LP.L.scenes[LP.scene];
  if(qs && qs.type==='quiz' && !LP.gate[LP.scene] && !(e.target.closest && e.target.closest('input,select,textarea'))){ const n=['1','2','3','4'].indexOf(k); if(n>=0 && n<qs.choices.length){ e.preventDefault(); lpPick(n); return true; } }
  if(qs && qs.type==='choice' && !LP.gate[LP.scene] && choiceState(LP.scene).phase==='ask' && !(e.target.closest && e.target.closest('input,select,textarea'))){ const n=['1','2','3','4'].indexOf(k); if(n>=0 && n<qs.options.length){ e.preventDefault(); gxChoose(n); return true; } }
  if(qs && qs.type==='choice' && choiceState(LP.scene).phase==='fail' && (k==='enter'||k==='r')){ e.preventDefault(); gxRetry(); return true; }
  if(qs && qs.type==='swipe' && !LP.gate[LP.scene]){ const n=['1','2','3'].indexOf(k); const g=LP.gs[LP.scene]; if(n>=0 && n<qs.options.length && g && g.picks[g.i]==null && g.i<qs.cards.length){ e.preventDefault(); gxSwipe(n); return true; } }
  if((k==='enter'||k===' ') && e.target.matches && e.target.matches('.gx-bin')){ e.preventDefault(); gxBin(+e.target.dataset.b); return true; }
  if(e.target.closest && e.target.closest('button,select,input,summary,a,[role="button"]')) { if(!(k===' ' && e.target.id==='lp-play')) return false; }
  if(k===' '||k==='k'){ e.preventDefault(); if(LP.awaiting<0){ LP.playing?lpPause():lpPlay(); } return true; }
  if(k==='arrowleft'){ e.preventDefault(); lpScene(-1); return true; }
  if(k==='arrowright'){ e.preventDefault(); lpScene(1); return true; }
  if(k==='c'){ lessonActs('lp-cc'); return true; }
  return false;
}
function lessonsForGuide(gid){ return LESSONS.filter(l=>l.guide===gid); }

/* --- preview (authoring tools): open a lesson object with estimated timing and no audio --- */
function estimateTiming(L){
  let t=0; const scenes=L.scenes.map(sc=>{ const s={t0:+t.toFixed(3), beats:[]}; const seq=sc.beats.map(b=>['b',b]).concat((sc.reveal||[]).map(b=>['r',b]));
    const dur=b=>Math.max(1.2, b.say.split(/\s+/).length/2.45);
    seq.forEach(([k,b],i)=>{ if(k==='r' && s.q==null){ s.q=+t.toFixed(3); t+=0.5;
        if(sc.type==='choice'){ s.ob=sc.options.map(o=>{ const seg=o.beats.map(ob=>{ const d=dur(ob), x=[+t.toFixed(3), +(t+d).toFixed(3)]; t+=d+0.32; return x; }); t+=0.5; return seg; }); }
        s.r=+t.toFixed(3); }
      const d=dur(b); s.beats.push([+t.toFixed(3), +(t+d).toFixed(3)]); t+=d; if(i<seq.length-1) t+=0.32; });
    if(GATES.has(sc.type) && s.q==null){ s.q=+t.toFixed(3); s.r=+t.toFixed(3); }
    s.t1=+t.toFixed(3); t+=0.8; return s; });
  return {dur:+t.toFixed(3), scenes};
}
