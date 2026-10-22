/* ---------- Watch: narrated, animated lessons ---------- */
const LESSONS = DATA.lessons || [];
const LBY = Object.fromEntries(LESSONS.map(l=>[l.id,l]));
const ICONS = DATA.icons || {};
function icon(name, cls){ const p=ICONS[name]; return p ? `<svg class="ic ${cls||''}" viewBox="0 0 24 24" aria-hidden="true">${p}</svg>` : ''; }
function lessonState(id){ return (P.lessons||{})[id] || null; }
function lessonsDone(){ return LESSONS.filter(l=>{ const s=lessonState(l.id); return s && s.done; }).length; }
function nextLesson(){
  const inProg = LESSONS.find(l=>{ const s=lessonState(l.id); return s && !s.done && s.pos>5; });
  return inProg || LESSONS.find(l=>{ const s=lessonState(l.id); return !s || !s.done; }) || null;
}
const mmss = s => { s=Math.max(0,Math.floor(s||0)); return Math.floor(s/60)+':'+String(s%60).padStart(2,'0'); };

function renderWatch(opts){
  if(opts && opts.id && LBY[opts.id]){ openLesson(opts.id, opts); return; }
  lpClose();
  const el=$('#view-watch');
  if(!LESSONS.length){ el.innerHTML='<div class="panel"><p class="muted" style="margin:0">No lessons in this build.</p></div>'; return; }
  const done=lessonsDone(), mins=Math.round(LESSONS.reduce((s,l)=>s+l.timing.dur,0)/60), nx=nextLesson();
  const card = l => {
    const s=lessonState(l.id), st = s&&s.done ? '<span class="chip good">Watched</span>' : s&&s.pos>5 ? `<span class="chip">Stopped at ${mmss(s.pos)}</span>` : '';
    return `<button class="lcard" data-act="lesson" data-id="${l.id}">
      <span class="lnum">${l.id.slice(1)}</span>
      <span class="lbody"><span class="lt">${esc(l.title)}</span><span class="ls">${esc(l.summary)}</span>
      <span class="lmeta mono">${mmss(l.timing.dur)} · ${l.scenes.filter(x=>x.type==='quiz').length} quick checks ${st}</span></span>
      <span class="lplay" aria-hidden="true">${icon('play')}</span></button>`;
  };
  const groups = SECTIONS.map(s=>({s, ls:LESSONS.filter(l=>l.sec===s.key)})).filter(g=>g.ls.length);
  el.innerHTML = `<div class="stack">
    <div class="panel">
      <h2>Video lessons</h2>
      <p class="muted lede" style="margin:6px 0 12px">Short narrated lessons with animated diagrams. Each one stops for quick questions: answering from memory is what makes it stick. Every fact was checked against the app's study material and the laws and forms behind it.</p>
      <div class="row" style="gap:18px;align-items:center">
        ${nx?`<button class="btn primary cta-big" data-act="lesson" data-id="${nx.id}">${icon('play','btn-ic')} ${lessonState(nx.id)&&lessonState(nx.id).pos>5?'Continue':'Watch'}: ${esc(nx.title)}</button>`:''}
        <span class="mono small muted">${done} of ${LESSONS.length} watched · about ${mins} min in all</span>
      </div>
    </div>
    ${groups.map(g=>`<section><h3 class="lgroup">${esc(g.s.name)} <span class="mono small muted">${g.s.pct}% of the exam</span></h3><div class="lgrid">${g.ls.map(card).join('')}</div></section>`).join('')}
  </div>`;
}

/* --- player state --- */
const LP = {L:null, audio:null, virtual:false, playing:false, vbase:0, vt0:0, rate:1, raf:0, scene:-1, sig:'', quiz:{}, awaiting:-1, ended:false, lastSave:0};
function lpDur(){ return LP.L ? LP.L.timing.dur : 0; }
function lpTime(){
  if(!LP.L) return 0;
  if(LP.virtual) return LP.playing ? Math.min(lpDur(), LP.vbase + (performance.now()-LP.vt0)/1000*LP.rate) : LP.vbase;
  return LP.audio ? LP.audio.currentTime : 0;
}
function lpPlay(){
  if(!LP.L) return;
  if(LP.ended){ lpSeek(0); LP.ended=false; }
  if(LP.awaiting>=0) return;
  hideOverlay();
  LP.playing=true;
  if(LP.virtual){ LP.vt0=performance.now(); }
  else { LP.audio.playbackRate=LP.rate; const pr=LP.audio.play(); if(pr && pr.catch) pr.catch(()=>{ if(LP.audio && LP.audio.error) goVirtual(); else { LP.playing=false; lpUI(); } }); }
  lpLoop(); lpUI();
}
function lpPause(){
  if(!LP.L) return;
  if(LP.virtual){ LP.vbase=lpTime(); }
  else if(LP.audio) LP.audio.pause();
  LP.playing=false; lpSavePos(true); lpUI();
}
function lpSeek(t){
  if(!LP.L) return;
  t=Math.max(0, Math.min(lpDur(), t));
  if(LP.virtual){ LP.vbase=t; LP.vt0=performance.now(); }
  else if(LP.audio){ try{ LP.audio.currentTime=t; }catch(e){} }
  LP.ended = false;
  lpTick(true, t);
}
function goVirtual(){
  const t = LP.audio ? LP.audio.currentTime : 0;
  if(LP.audio){ LP.audio.pause(); LP.audio.removeAttribute('src'); }
  LP.virtual=true; LP.vbase=t||0; LP.vt0=performance.now(); LP.cc=true;
  const n=$('#lp-note'); if(n){ n.hidden=false; n.textContent='Audio could not load here, so captions are on and the lesson plays silently.'; }
  if(LP.playing){ LP.vt0=performance.now(); lpLoop(); }
  lpTick(true); lpUI();
}
function lpLoop(){ cancelAnimationFrame(LP.raf); const f=()=>{ if(!LP.L || !LP.playing) return; lpTick(false); LP.raf=requestAnimationFrame(f); }; LP.raf=requestAnimationFrame(f); }
function lpClose(){
  if(LP.L){ lpSavePos(true); }
  cancelAnimationFrame(LP.raf);
  if(LP.audio){ LP.audio.pause(); LP.audio.removeAttribute('src'); try{ LP.audio.load(); }catch(e){} }
  Object.assign(LP, {L:null, audio:null, virtual:false, playing:false, scene:-1, sig:'', quiz:{}, awaiting:-1, ended:false});
}
function lpSavePos(force){
  if(!LP.L) return;
  const now=Date.now(); if(!force && now-LP.lastSave<5000) return; LP.lastSave=now;
  P.lessons = P.lessons || {};
  const s = P.lessons[LP.L.id] || (P.lessons[LP.L.id]={pos:0, done:0, quiz:{}});
  s.pos = LP.ended ? 0 : Math.round(lpTime()); s.seen=now; save();
}

/* --- timing lookup --- */
function stateAt(t){
  const L=LP.L, T=L.timing.scenes;
  let si=0; for(let i=0;i<T.length;i++){ if(T[i].t0<=t+0.001) si=i; }
  const sc=L.scenes[si], tm=T[si], beats=sc.beats.concat(sc.reveal||[]);
  let bi=-1; tm.beats.forEach((b,i)=>{ if(b[0]<=t+0.05) bi=i; });
  let show=0, tell=false, answer=false, hl=null;
  for(let i=0;i<=Math.max(bi,0);i++){ const b=beats[i]; if(!b) continue; if(b.show!=null) show=b.show; if(b.tell) tell=true; if(b.answer) answer=true; }
  if(bi>=0 && beats[bi] && beats[bi].hl!=null) hl=beats[bi].hl;
  const cap = bi>=0 && t <= tm.beats[bi][1]+0.6 ? beats[bi].text : '';
  return {si, bi, show, tell, answer, hl, cap};
}

/* --- scene markup --- */
function sceneHTML(sc, si){
  const T = sc.title ? `<h3 class="st-title">${esc(sc.title)}</h3>` : '';
  const it = (i, inner, cls) => `<div class="st-it ${cls||''}" data-i="${i}">${inner}</div>`;
  switch(sc.type){
    case 'title': return `<div class="st-titlecard">${icon(sc.icon,'st-bigic')}<div class="st-eyebrow mono">Lesson ${esc(LP.L.id.slice(1))}</div><h2>${esc(sc.title)}</h2><p>${esc(sc.subtitle)}</p></div>`;
    case 'bullets': return T+`<div class="st-list ${sc.items.length<=3?'st-cols':''}">${sc.items.map((x,i)=>it(i, `${x.icon?icon(x.icon,'st-itic'):''}<div><b>${esc(x.label)}</b>${x.detail?`<span>${esc(x.detail)}</span>`:''}</div>`, 'st-card')).join('')}</div>`;
    case 'steps': return T+`<div class="st-steps ${sc.ladder?'st-ladder':''}">${(sc.ladder?sc.items.map((x,i)=>[x,i]).reverse():sc.items.map((x,i)=>[x,i])).map(([x,i])=>it(i, `<span class="st-num">${i+1}</span><div><b>${esc(x.label)}</b>${x.detail?`<span>${esc(x.detail)}</span>`:''}</div>`, 'st-card'+(sc.ladder?` st-rung" style="--rung:${i}`:''))).join('')}</div>`;
    case 'compare': return T+`<div class="st-compare c${sc.columns.length}">${sc.columns.map((c,i)=>it(i, `<div class="st-colh">${c.icon?icon(c.icon,'st-itic'):''}<b>${esc(c.name)}</b></div><ul>${c.points.map(p=>`<li>${esc(p)}</li>`).join('')}</ul>`, 'st-card')).join('')}</div>${sc.tell?`<div class="st-tell" data-tell>${icon('lightbulb','st-itic')}<span>${esc(sc.tell)}</span></div>`:''}`;
    case 'timeline': return T+`<div class="st-timeline">${sc.items.map((x,i)=>it(i, `<span class="st-at mono">${esc(x.at)}</span><span class="st-dot"></span><b class="tl-l">${esc(x.label)}</b>${x.detail?`<span class="tl-d">${esc(x.detail)}</span>`:''}`)).join('')}</div>`;
    case 'table': return T+`<div class="st-tablewrap"><table class="st-table"><thead><tr>${sc.columns.map(c=>`<th>${esc(c)}</th>`).join('')}</tr></thead><tbody>${sc.items.map((r,i)=>`<tr class="st-it" data-i="${i}">${r.map(c=>`<td>${esc(c)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
    case 'formula': return T+`${sc.given&&sc.given.length?`<div class="st-given">${sc.given.map(g=>`<span class="chip">${esc(g)}</span>`).join('')}</div>`:''}<div class="st-formula">${sc.items.map((x,i)=>it(i, `<span class="fl">${esc(x.label)}</span><span class="fx mono">${esc(x.expr)}</span><span class="fv">${esc(x.value)}</span>`, i===sc.items.length-1?'st-result':'')).join('')}</div>`;
    case 'scenario': return T+`<div class="st-story">${icon(sc.icon||'user','st-itic')}<p>${esc(sc.story)}</p></div><div class="st-list">${(sc.items||[]).map((x,i)=>it(i, `<span class="st-num">${i+1}</span><div><b>${esc(x.label)}</b>${x.detail?`<span>${esc(x.detail)}</span>`:''}</div>`, 'st-card')).join('')}</div><div class="st-answer" data-answer>${icon('circle-check','st-itic')}<span>${esc(sc.answer)}</span></div>`;
    case 'bignum': return T+`<div class="st-big n${sc.items.length}">${sc.items.map((x,i)=>it(i, `<span class="bv">${esc(x.value)}</span><span class="bl">${esc(x.label)}</span>`, 'st-card')).join('')}</div>`;
    case 'quiz': {
      const q=LP.quiz[si];
      return `<div class="st-quiz"><div class="st-eyebrow mono">${icon('brain','st-smic')} Quick check</div><p class="st-q">${esc(sc.q)}</p>
        <div class="st-choices">${sc.choices.map((c,i)=>{ let cls=''; if(q){ if(i===sc.answer) cls='right'; else if(i===q.pick) cls='wrong'; }
          return `<button class="st-choice ${cls}" data-act="lp-pick" data-i="${i}" ${q?'disabled':''}><span class="mono">${LETTERS[i]}</span><span>${esc(c)}</span></button>`; }).join('')}</div>
        <div class="st-why" ${q?'':'hidden'}>${q?`<b>${q.skip?'Answer':q.ok?'Correct.':'Not quite.'}</b> ${esc(sc.why)}`:''}</div>
        ${q?'':`<button class="st-skip" data-act="lp-skip">Show the answer</button>`}</div>`;
    }
    case 'hook': return T+`<div class="st-hook">${icon('lightbulb','st-bigic')}<p class="hk">${esc(sc.hook)}</p></div><div class="st-list">${(sc.items||[]).map((x,i)=>it(i, `<span>${esc(x)}</span>`, 'st-card st-small')).join('')}</div>`;
    case 'recap': return `<h3 class="st-title">${esc(sc.title||'Key takeaways')}</h3><div class="st-list">${sc.items.map((x,i)=>it(i, `${icon('circle-check','st-itic')}<span>${esc(x)}</span>`, 'st-card')).join('')}</div>`;
  }
  return '';
}
function layoutSrc(){
  const src=$('#lp-src'), box=$('#lp-scene'), cap=$('#lp-cap'); if(!src || !box) return;
  const h = src.textContent ? src.offsetHeight : 0, gap = Math.max(10, src.offsetParent ? parseFloat(getComputedStyle(src).bottom) || 10 : 10);
  box.style.paddingBottom = Math.max(64, h + gap + 22) + 'px';
  if(cap) cap.style.bottom = (h + gap + 8) + 'px';
}
function fitScene(){
  layoutSrc();
  const box=$('#lp-scene'), inner=box && box.firstElementChild; if(!inner) return;
  inner.style.fontSize='';
  let f=1; for(let k=0; k<7 && box.scrollHeight>box.clientHeight+1; k++){ f-=0.06; inner.style.fontSize=f.toFixed(2)+'em'; }
}
let fitTimer=0;
window.addEventListener('resize', ()=>{ clearTimeout(fitTimer); fitTimer=setTimeout(()=>{ if(LP.L) fitScene(); }, 120); });
document.addEventListener('fullscreenchange', ()=>{ if(LP.L) setTimeout(fitScene, 60); });
document.addEventListener('visibilitychange', ()=>{ if(document.hidden && LP.L && LP.virtual && LP.playing) lpPause(); });
function lpTick(force, tOverride){
  if(!LP.L) return;
  const t = tOverride!=null ? tOverride : lpTime(), L=LP.L, T=L.timing.scenes;
  const s = stateAt(t);
  // quiz gate: stop at the end of the question until the learner answers
  const sc=L.scenes[s.si], tm=T[s.si];
  if(sc.type==='quiz' && !LP.quiz[s.si] && LP.playing && t >= tm.q-0.03 && t < tm.r){
    lpPause(); LP.awaiting=s.si; if(!LP.virtual && LP.audio){ try{ LP.audio.currentTime=tm.q; }catch(e){} } else LP.vbase=tm.q;
    const b=$('#lp-stage .st-q'); if(b){ b.tabIndex=-1; b.focus({preventScroll:true}); }
  }
  if(sc.type==='quiz' && !LP.quiz[s.si] && t >= tm.r){ LP.quiz[s.si]={pick:-1, ok:false, skip:true}; if(LP.awaiting===s.si) LP.awaiting=-1; force=true; }
  if(s.si!==LP.scene || force){
    if(s.si!==LP.scene){ LP.awaiting = (sc.type==='quiz' && !LP.quiz[s.si] && t>=tm.q-0.03 && t<tm.r) ? s.si : -1; }
    LP.scene=s.si;
    const src=$('#lp-src'); if(src) src.textContent = sc.src ? 'Source: '+sc.src : '';
    const box=$('#lp-scene'); if(box){ box.className='st-scene t-'+sc.type; box.innerHTML='<div class="st-inner">'+sceneHTML(sc, s.si)+'</div>'; box.scrollTop=0; fitScene(); }
    LP.sig='';
  }
  const sig = [s.si,s.show,s.hl,s.tell,s.answer].join('|');
  if(sig!==LP.sig){
    LP.sig=sig;
    document.querySelectorAll('#lp-scene .st-it').forEach(e=>{ const i=+e.dataset.i; e.classList.toggle('in', i<s.show); e.classList.toggle('hl', i===s.hl); });
    const tl=$('#lp-scene [data-tell]'); if(tl) tl.classList.toggle('in', s.tell);
    const an=$('#lp-scene [data-answer]'); if(an) an.classList.toggle('in', s.answer);
  }
  const cap=$('#lp-cap'); if(cap){ const on=(LP.cc||LP.virtual) && s.cap; cap.hidden=!on; if(on && cap.textContent!==s.cap) cap.textContent=s.cap; }
  const r=$('#lp-range'); if(r && document.activeElement!==r) r.value=t.toFixed(1);
  const tt=$('#lp-time'); if(tt) tt.textContent=mmss(t)+' / '+mmss(lpDur());
  const fill=$('#lp-fill'); if(fill) fill.style.width=(lpDur()? t/lpDur()*100 : 0)+'%';
  if(LP.playing) lpSavePos(false);
  if(LP.playing && t >= lpDur()-0.05) lpFinish();
}
function lpUI(){
  const b=$('#lp-play'); if(b){ b.innerHTML = icon(LP.playing?'pause':'play') + `<span class="sr">${LP.playing?'Pause':'Play'}</span>`; b.setAttribute('aria-label', LP.playing?'Pause':'Play'); }
  const cc=$('#lp-cc'); if(cc) cc.setAttribute('aria-pressed', String(!!LP.cc));
}
function hideOverlay(){ const o=$('#lp-over'); if(o) o.hidden=true; }
function lpFinish(){
  if(!LP.L || LP.ended) return;
  LP.ended=true; LP.playing=false; cancelAnimationFrame(LP.raf);
  if(!LP.virtual && LP.audio) LP.audio.pause();
  const L=LP.L; P.lessons=P.lessons||{};
  const s=P.lessons[L.id] || (P.lessons[L.id]={pos:0, done:0, quiz:{}});
  const first=!s.done;
  s.done = s.done || Date.now(); s.pos=0;
  const qs=Object.values(LP.quiz).filter(q=>!q.skip), right=qs.filter(q=>q.ok).length;
  if(first){ addXP(20); toast(`Lesson complete: <b>+20 XP</b>`); }
  checkBadges(); save(); lpUI();
  const nx = LESSONS[LESSONS.indexOf(L)+1];
  const o=$('#lp-over');
  if(o){ o.hidden=false; o.innerHTML=`<div class="st-end"><div class="st-eyebrow mono">Lesson ${esc(L.id.slice(1))} complete</div><h2>${esc(L.title)}</h2>
    <p>${qs.length?`Quick checks: ${right} right out of ${qs.length} you answered (this lesson has ${L.scenes.filter(x=>x.type==='quiz').length}). `:''}Lock it in with ${L.check.length} exam-style questions from the bank.</p>
    <div class="row" style="justify-content:center"><button class="btn primary" data-act="lp-check">Check yourself (${L.check.length})</button>
    ${nx?`<button class="btn" data-act="lesson" data-id="${nx.id}">Next: ${esc(nx.title)}</button>`:''}
    <button class="btn ghost" data-act="lp-replay">Watch again</button></div></div>`; }
}
function openLesson(id, opts){
  lpClose();
  const L=LBY[id]; if(!L) return;
  LP.L=L; LP.quiz={}; LP.cc = !!(P.settings.captions); LP.rate = P.settings.lessonRate || 1;
  const el=$('#view-watch');
  const st=lessonState(id), resume = st && !st.done && st.pos>5 ? st.pos : 0;
  const marks = L.timing.scenes.map((s,i)=>`<span class="lp-mark ${L.scenes[i].type==='quiz'?'q':''}" style="left:${(s.t0/L.timing.dur*100).toFixed(2)}%"></span>`).join('');
  const sources = (L.sources||[]).map(esc).join('; ');
  el.innerHTML = `<div class="lp stack">
    <div class="row" style="justify-content:space-between;align-items:center;gap:10px">
      <button class="btn ghost small" data-act="watch-list">${icon('chevron-left','btn-ic')} All lessons</button>
      <span class="mono small muted">${esc(SEC[L.sec]?SEC[L.sec].name:'')}</span>
    </div>
    <h2 style="margin:0">${esc(L.title)}</h2>
    <div class="stage" id="lp-stage">
      <div class="st-scene" id="lp-scene"></div>
      <div class="st-src mono" id="lp-src"></div>
      <div class="st-cap" id="lp-cap" hidden aria-live="off"></div>
      <div class="st-over" id="lp-over"><div class="st-start">
        <div class="st-eyebrow mono">Lesson ${esc(L.id.slice(1))} · ${mmss(L.timing.dur)}</div>
        <h2>${esc(L.title)}</h2>
        <ul>${L.objectives.map(o=>`<li>${esc(o)}</li>`).join('')}</ul>
        <button class="btn primary cta-big" data-act="lp-start">${icon('play','btn-ic')} ${resume?`Resume at ${mmss(resume)}`:'Play lesson'}</button>
        ${resume?`<button class="st-skip" data-act="lp-restart">Start from the beginning</button>`:''}
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
      <button class="btn small" id="lp-cc" data-act="lp-cc" aria-pressed="${LP.cc}" title="Captions">CC</button>
      ${document.fullscreenEnabled?`<button class="btn small" data-act="lp-full" aria-label="Full screen">${icon('maximize')}</button>`:''}
    </div>
    <div class="row" style="gap:8px"><button class="btn" data-act="lp-check">Check yourself (${L.check.length} questions)</button>
      <button class="btn ghost" data-act="lp-guide">Read this in the study guide</button></div>
    <details class="panel lp-trans"><summary>Transcript</summary>
      ${L.scenes.map((sc,si)=>`<div class="lp-tsc"><button class="linkish mono small" data-act="lp-goto" data-si="${si}">${mmss(L.timing.scenes[si].t0)}</button> ${sc.beats.concat(sc.reveal||[]).map(b=>esc(b.text)).join(' ')}</div>`).join('')}
      <p class="small muted" style="margin:10px 0 0">Sources: ${sources}</p>
    </details>
  </div>`;
  LP.audio = new Audio(); LP.audio.preload='auto'; LP.audio.src=L.audio;
  LP.audio.addEventListener('error', ()=>{ if(LP.L===L && !LP.virtual) goVirtual(); });
  LP.audio.addEventListener('ended', ()=>{ if(LP.L===L) lpFinish(); });
  LP.audio.addEventListener('timeupdate', ()=>{ if(LP.L===L && LP.playing) lpTick(false); });
  $('#lp-range').addEventListener('input', e=>{ lpSeek(+e.target.value); });
  $('#lp-rate').addEventListener('change', e=>{ const t=lpTime(); LP.rate=+e.target.value; P.settings.lessonRate=LP.rate; save(); if(LP.virtual){ LP.vbase=t; LP.vt0=performance.now(); } else if(LP.audio) LP.audio.playbackRate=LP.rate; });
  LP.scene=-1; lpSeek(resume); lpUI();
  if(opts && opts.autoplay){ lpPlay(); }
}
function lpPick(i){
  const si=LP.scene, sc=LP.L.scenes[si]; if(!sc || sc.type!=='quiz' || LP.quiz[si]) return;
  const ok = i===sc.answer;
  LP.quiz[si]={pick:i, ok};
  P.lessons=P.lessons||{}; const s=P.lessons[LP.L.id] || (P.lessons[LP.L.id]={pos:0, done:0, quiz:{}});
  s.quiz = s.quiz||{}; if(s.quiz[si]==null){ s.quiz[si]=ok?1:0; if(ok) addXP(2); }
  LP.awaiting=-1;
  lpTick(true, lpTime());
  lpSeek(LP.L.timing.scenes[si].r); lpPlay();
}
function lpSkip(){ const si=LP.scene; if(!LP.L || LP.quiz[si]) return; LP.quiz[si]={pick:-1, ok:false, skip:true}; LP.awaiting=-1; lpSeek(LP.L.timing.scenes[si].r); lpPlay(); }
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
  if(act==='lp-replay'){ LP.quiz={}; LP.ended=false; lpSeek(0); lpPlay(); return true; }
  if(act==='lp-toggle'){ if(LP.awaiting>=0) return true; LP.playing ? lpPause() : lpPlay(); return true; }
  if(act==='lp-prev'){ lpScene(-1); return true; }
  if(act==='lp-next'){ lpScene(1); return true; }
  if(act==='lp-pick'){ lpPick(+b.dataset.i); return true; }
  if(act==='lp-skip'){ lpSkip(); return true; }
  if(act==='lp-goto'){ LP.awaiting=-1; lpSeek(LP.L.timing.scenes[+b.dataset.si].t0); hideOverlay(); return true; }
  if(act==='lp-cc'){ LP.cc=!LP.cc; P.settings.captions=LP.cc; save(); lpTick(true); lpUI(); return true; }
  if(act==='lp-full'){ const s=$('#lp-stage'); if(document.fullscreenElement) document.exitFullscreen(); else if(s && s.requestFullscreen) s.requestFullscreen().catch(()=>{}); return true; }
  if(act==='lp-check'){ const L=LP.L; lpPause(); go('practice',{ids:L.check, label:'Lesson check: '+L.title}); return true; }
  if(act==='lp-guide'){ const g=LP.L.guide; lpPause(); go('study',{sec:g}); return true; }
  return false;
}
function lessonKeys(e, k){
  if(VIEW!=='watch' || !LP.L) return false;
  const qs = LP.L.scenes[LP.scene];
  if(qs && qs.type==='quiz' && !LP.quiz[LP.scene]){ const n=['1','2','3','4'].indexOf(k); if(n>=0 && n<qs.choices.length){ e.preventDefault(); lpPick(n); return true; } }
  if(e.target.closest && e.target.closest('button,select,input,summary,a')) { if(!(k===' ' && e.target.id==='lp-play')) return false; }
  if(k===' '||k==='k'){ e.preventDefault(); if(LP.awaiting<0){ LP.playing?lpPause():lpPlay(); } return true; }
  if(k==='arrowleft'){ e.preventDefault(); lpScene(-1); return true; }
  if(k==='arrowright'){ e.preventDefault(); lpScene(1); return true; }
  if(k==='c'){ lessonActs('lp-cc'); return true; }
  return false;
}
function lessonsForGuide(gid){ return LESSONS.filter(l=>l.guide===gid); }
