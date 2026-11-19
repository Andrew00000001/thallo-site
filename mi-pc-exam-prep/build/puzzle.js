/* ---------- Picture puzzle: every right answer uncovers one piece of a hidden hand-drawn picture; guess it to score ----------
   A 4 x 4 jigsaw covers a drawing from the whiteboard prop library. Right answers anywhere (sessions, practice, games, mock
   exams) uncover a random piece. A right guess is worth 1 point plus 1 for every piece still hidden, minus 1 per wrong guess
   (never less than 1). Progress lives in P.puz = {done:{id:{r,t,pts,best,n,hidden,shown}}, play:{"id@r":{id,r,rev,wrong,t}}}:
   finished pictures, and the pictures in play (normally one; two devices may each have started one). Both merge by union across
   devices (mergePuz), so the order copies meet in never matters. Reads never change progress: pzCur() works out the picture in
   play without storing it. */
const PUZ = DATA.puzzles || [];
const PUZBY = Object.fromEntries(PUZ.map((p,i)=>[p.id, Object.assign({ord:i}, p)]));
const PZN = 4, PZK = PZN*PZN;
let PZ_LAST = null;     // the piece uncovered most recently {id, k, t}: it fades out on the next draw
let PZ_SOLVED = null;   // a picture just guessed {id, pts, hidden, t}: shown whole until the learner moves on
const pzDone = () => (P.puz && P.puz.done) || {};
function pzRound(){ const d=pzDone(); return PUZ.length ? 1 + Math.min(...PUZ.map(p=>(d[p.id] && d[p.id].r) || 0)) : 1; }
function pzNextId(){ const d=pzDone(), R=pzRound(), p=PUZ.find(p=>((d[p.id] && d[p.id].r) || 0) < R); return p ? p.id : null; }
function pzLive(c){ if(!c || !PUZBY[c.id]) return false; const d=pzDone()[c.id]; return ((d && d.r) || 0) < (c.r || 1); }
function pzPlaying(){ const pl = (P.puz && P.puz.play) || {}; return Object.keys(pl).map(k=>pl[k]).filter(pzLive).reduce((a,b)=>a ? later(a, b, c=>c.r||1, c=>c.t||0) : b, null); }
function pzCur(){   // the picture in play (read only)
  const c = pzPlaying(); if(c) return c;
  const id = pzNextId(); return id ? {id, r:pzRound(), rev:[], wrong:0} : null;
}
function pzCurW(){  // the picture in play, made part of the progress record (for changes)
  P.puz = P.puz || {}; P.puz.done = P.puz.done || {}; P.puz.play = P.puz.play || {};
  let c = pzPlaying();
  if(!c){ const n = pzCur(); if(!n) return null; c = P.puz.play[n.id+'@'+n.r] = {id:n.id, r:n.r, rev:[], wrong:0, t:Date.now()}; }
  return c;
}
function pzFinish(c){   // the picture is done: it leaves play, along with any other finished ones
  const pl = P.puz.play || {}; delete pl[c.id+'@'+(c.r||1)];
  Object.keys(pl).forEach(k=>{ if(!pzLive(pl[k])) delete pl[k]; });
}
const pzScore = c => Math.max(1, 1 + (PZK - c.rev.length) - (c.wrong || 0));
const pzTotal = () => Object.values(pzDone()).reduce((s,d)=>s + (d.pts || 0), 0);
const pzSolvedCount = () => Object.values(pzDone()).filter(d=>(d.n || 0) > 0).length;
function puzzleAward(){   // a right answer: uncover one random hidden piece
  if(!PUZ.length) return false;
  const c = pzCurW(); if(!c) return false;
  const hidden = []; for(let k=0; k<PZK; k++) if(!c.rev.includes(k)) hidden.push(k);
  if(!hidden.length) return false;
  const k = hidden[Math.floor(Math.random()*hidden.length)];
  c.rev = c.rev.concat([k]).sort((a,b)=>a-b);
  PZ_LAST = {id:c.id, k, t:Date.now()};
  return true;
}

/* guessing: lenient about case, articles, plurals, spacing and small typos; "close" words get a nudge instead of a penalty */
function pzNorm(s){
  return String(s || '').toLowerCase().normalize('NFKD').replace(/[̀-ͯ]/g, '').replace(/&/g, ' and ').replace(/[^a-z0-9 ]+/g, ' ')
    .replace(/\s+/g, ' ').trim().replace(/^(it s|its|it is|this is|that s|thats|that is|i think it s|i think|maybe|a|an|the)\s+/, '').replace(/^(a|an|the)\s+/, '').trim();
}
const pzSing = w => w.length>4 && /ies$/.test(w) ? w.slice(0,-3)+'y' : w.length>4 && /(sses|xes|zes|ches|shes)$/.test(w) ? w.slice(0,-2) : w.length>3 && /[^s]s$/.test(w) ? w.slice(0,-1) : w;
const pzCanon = s => pzNorm(s).split(' ').filter(Boolean).map(pzSing).join(' ');
function pzLev(a, b){
  if(a===b) return 0; const m=a.length, n=b.length; if(!m || !n) return m || n;
  let prev = Array.from({length:n+1}, (_,j)=>j);
  for(let i=1; i<=m; i++){ const cur=[i]; for(let j=1; j<=n; j++) cur[j] = Math.min(prev[j]+1, cur[j-1]+1, prev[j-1]+(a[i-1]===b[j-1]?0:1)); prev = cur; }
  return prev[n];
}
let PZ_NAMES = null;   // every picture's own names, to tell "a different picture" from a near miss
function pzNames(){
  if(PZ_NAMES) return PZ_NAMES;
  PZ_NAMES = new Map();
  PUZ.forEach(q=>[q.answer].concat(q.accept || []).map(pzCanon).filter(Boolean).forEach(n=>{ const k = n.replace(/ /g, ''); if(!PZ_NAMES.has(k)) PZ_NAMES.set(k, new Set()); PZ_NAMES.get(k).add(q.id); }));
  return PZ_NAMES;
}
function pzMatch(p, guess){   // 'right' | 'close' | 'wrong' | 'empty'
  const g = pzCanon(guess); if(!g) return 'empty';
  const gc = g.replace(/ /g, '');
  const goods = [p.answer].concat(p.accept || []).map(pzCanon).filter(Boolean);
  for(const a of goods){ if(g===a || gc===a.replace(/ /g, '')) return 'right'; }
  const other = pzNames().get(gc), foreign = !!(other && !other.has(p.id));   // it names another picture ("piggy bank" is not the bank)
  if(!foreign) for(const a of goods){
    const ac = a.replace(/ /g, '');
    const tol = ac.length>=10 ? 2 : ac.length>=6 ? 1 : 0;   // short words: no typo slack ("nail" is not "hail")
    if(tol && Math.abs(gc.length-ac.length)<=tol && pzLev(gc, ac)<=tol) return 'right';
    if(a.length>=3 && g.endsWith(' '+a)) return 'right';   // describing words in front: "a big tornado", "yellow school bus" (not "house cat" for a house)
  }
  for(const c of (p.close || []).map(pzCanon).filter(Boolean)) if(g===c || g.endsWith(' '+c)) return 'close';
  return 'wrong';
}
function puzzleGuess(text){
  const c0 = pzCur(); if(!c0) return {state:'none'};
  const p = PUZBY[c0.id], m = pzMatch(p, text);
  if(m==='empty' || m==='close') return {state:m};
  const c = pzCurW();
  if(m==='right'){
    const pts = pzScore(c), hidden = PZK - c.rev.length, d = P.puz.done[c.id] || {};
    P.puz.done[c.id] = {r:c.r, t:Date.now(), pts:(d.pts||0)+pts, best:Math.max(d.best||0, pts), n:(d.n||0)+1, hidden:Math.max(d.hidden||0, hidden)};
    pzFinish(c); PZ_SOLVED = {id:c.id, pts, hidden, t:Date.now()}; PZ_LAST = null;
    addXP(pts*3); save(); checkBadges();
    return {state:'right', pts, hidden, id:c.id};
  }
  c.wrong = (c.wrong || 0) + 1; save();
  return {state:'wrong', wrong:c.wrong};
}
function puzzleGiveUp(){   // only once every piece is uncovered: shows the answer, no points, and moves on
  const c = pzCurW(); if(!c || c.rev.length < PZK) return null;
  const d = P.puz.done[c.id] || {};
  P.puz.done[c.id] = Object.assign({}, d, {r:c.r, t:Date.now(), pts:d.pts||0, n:d.n||0, shown:1});
  pzFinish(c); PZ_SOLVED = {id:c.id, pts:0, hidden:0, t:Date.now(), shown:true}; PZ_LAST = null; save();
  return c.id;
}
function pzHints(p, c){
  const out = [`<span class="chip">${esc(p.category || 'Picture')}</span>`], ans = String(p.answer).trim(), words = ans.split(/\s+/);
  if((c.wrong||0) >= 1) out.push(`<span class="chip">${words.length>1 ? words.length+' words: '+words.map(w=>w.length).join(' + ')+' letters' : ans.length+' letters'}</span>`);
  if((c.wrong||0) >= 2) out.push(`<span class="chip">Starts with ${esc(ans[0].toUpperCase())}</span>`);
  return out.join('');
}

/* the board: the drawing (rendered once per picture) under 16 jigsaw pieces that are the same on every device */
const PZ_PIC = {}, PZ_GEO = {};
function pzPicture(id){
  if(PZ_PIC[id] != null) return PZ_PIC[id];
  let html = '';
  try{ const R = SK.render(PUZBY[id].draw, {w:100, h:100, key:'pz-'+id}); SK.showAll(R); R.svg.setAttribute('aria-hidden', 'true'); R.svg.classList.add('pz-pic'); html = R.svg.outerHTML; }catch(e){ html = ''; }
  return PZ_PIC[id] = html;
}
function pzRand(seed){ let s = 2166136261; for(const ch of String(seed)) s = Math.imul(s ^ ch.charCodeAt(0), 16777619) >>> 0; return ()=>{ s = (Math.imul(s, 1664525) + 1013904223) >>> 0; return s/4294967296; }; }
function pzPieces(id){
  if(PZ_GEO[id]) return PZ_GEO[id];
  const rnd = pzRand('pz:'+id), w = 100/PZN, H = [], V = [], f = x => Math.round(x*100)/100;
  for(let r=1; r<PZN; r++){ H[r] = []; for(let c=0; c<PZN; c++) H[r][c] = rnd()<.5 ? 1 : -1; }
  for(let r=0; r<PZN; r++){ V[r] = []; for(let c=1; c<PZN; c++) V[r][c] = rnd()<.5 ? 1 : -1; }
  // a classic knob, symmetric about the middle of the edge, so a shared edge drawn backwards is the same curve
  const K = [[.36,0],[.40,0],[.42,-.03],[.39,-.08],[.34,-.17],[.44,-.24],[.50,-.24],[.56,-.24],[.66,-.17],[.61,-.08],[.58,-.03],[.60,0],[.64,0]];
  const edge = (x0,y0,x1,y1,sg) => {
    if(!sg) return `L${f(x1)} ${f(y1)}`;
    const dx=x1-x0, dy=y1-y0, pt = ([u,v]) => [x0+dx*u-dy*v*sg, y0+dy*u+dx*v*sg], q = K.map(pt);
    return `L${f(q[0][0])} ${f(q[0][1])}` + [1,4,7,10].map(i=>'C'+q.slice(i,i+3).map(p=>f(p[0])+' '+f(p[1])).join(' ')).join('') + `L${f(x1)} ${f(y1)}`;
  };
  const out = [];
  for(let r=0; r<PZN; r++) for(let c=0; c<PZN; c++){
    const x0=c*w, y0=r*w, x1=x0+w, y1=y0+w;
    out.push({k:r*PZN+c, d:`M${f(x0)} ${f(y0)}` + edge(x0,y0,x1,y0, r>0 ? H[r][c] : 0) + edge(x1,y0,x1,y1, c<PZN-1 ? V[r][c+1] : 0)
      + edge(x1,y1,x0,y1, r<PZN-1 ? -H[r+1][c] : 0) + edge(x0,y1,x0,y0, c>0 ? -V[r][c] : 0) + 'Z'});
  }
  return PZ_GEO[id] = out;
}
function pzBoardHTML(id, rev, slot, anim){
  const pieces = pzPieces(id).filter(p=>!rev.includes(p.k) || p.k===anim);
  const label = rev.length>=PZK ? 'Picture puzzle: every piece uncovered' : `Picture puzzle: ${rev.length} of ${PZK} pieces uncovered`;
  return `<div class="pz-board pz-at-${slot}" role="img" aria-label="${label}">${pzPicture(id)}<svg class="pz-cover" viewBox="0 0 100 100" aria-hidden="true">`
    + pieces.map(p=>`<path class="pz-pc${p.k===anim ? ' pz-go' : ''}" d="${p.d}"/>`).join('') + `</svg></div>`;
}
function pzBoardFor(c, slot){
  const anim = PZ_LAST && PZ_LAST.id===c.id && Date.now()-PZ_LAST.t < 2500 ? PZ_LAST.k : -1;
  return pzBoardHTML(c.id, c.rev, slot, anim);
}

/* views: a panel on Today, a small board beside each question, a dialog from anywhere, and the collection */
function pzGuessForm(slot){
  return `<form class="pz-guess" data-slot="${slot}" autocomplete="off" novalidate><label class="sr" for="pz-in-${slot}">Your guess</label>`
    + `<input id="pz-in-${slot}" class="pz-in" type="text" maxlength="60" placeholder="What's the picture?" enterkeyhint="go" autocapitalize="off" autocomplete="off" spellcheck="false">`
    + `<button class="btn primary" type="submit">Guess</button></form><div class="pz-msg small" data-slot="${slot}" aria-live="polite"></div>`;
}
function pzSolvedHTML(slot){
  const s = PZ_SOLVED, p = PUZBY[s.id]; if(!p) return '';
  const card = p.card && CARDS.find(c=>c.id===p.card);
  return `<div class="pz-body${slot==='modal' ? ' pz-body-modal' : ''}"><div class="pz-left">${pzBoardHTML(s.id, Array.from({length:PZK}, (_,k)=>k), slot, -1)}</div><div class="stack pz-side">`
    + (s.shown ? `<h2 class="pz-title">It was: ${esc(p.answer)}</h2><p class="small muted" style="margin:0">No points this time. The next picture is ready.</p>`
      : `<h2 class="pz-title">You got it: ${esc(p.answer)}!</h2><p class="pz-pts"><b>+${s.pts}</b> point${s.pts===1?'':'s'}${s.hidden ? ` · guessed with ${s.hidden} piece${s.hidden===1?'':'s'} still hidden` : ''}</p>`)
    + (card ? `<div class="pz-card small"><div class="eyebrow" style="color:var(--muted)">Related flashcard</div><div><b>${esc(card.front)}</b></div><div>${esc(card.back)}</div></div>` : '')
    + `<div class="row"><button class="btn primary" data-act="pz-next">Next picture</button><button class="btn ghost small" data-act="pz-collection">Collection</button></div></div></div>`;
}
function puzzlePanelHTML(){
  if(!PUZ.length) return '';
  const head = `<div class="row" style="justify-content:space-between;gap:8px;align-items:baseline"><h2 style="margin:0">Picture puzzle</h2><span class="mono small muted">${pzTotal()} pt${pzTotal()===1?'':'s'} · ${pzSolvedCount()} of ${PUZ.length} pictures</span></div>`;
  if(PZ_SOLVED) return `<div class="panel pz-panel" id="pz-panel">${head}${pzSolvedHTML('today')}</div>`;
  const c = pzCur(); if(!c) return '';
  const p = PUZBY[c.id], hidden = PZK - c.rev.length;
  return `<div class="panel pz-panel" id="pz-panel">${head}<div class="pz-body"><div class="pz-left">${pzBoardFor(c, 'today')}</div><div class="stack pz-side">`
    + `<p class="small muted" style="margin:0">Every question you get right uncovers a piece. Guess the picture any time: it's worth 1 point plus 1 for each piece still hidden. A wrong guess costs a point.</p>`
    + `<div class="row pz-hints">${pzHints(p, c)}</div>${pzGuessForm('today')}`
    + `<div class="row small"><span class="pill">${c.rev.length} of ${PZK} pieces</span><span class="pill good">Worth ${pzScore(c)} now</span>${hidden===0 ? '<button class="btn ghost small" data-act="pz-reveal">Show the answer</button>' : ''}<button class="btn ghost small" data-act="pz-collection">Collection</button></div>`
    + `</div></div></div>`;
}
function puzzleMiniHTML(){   // beside a question: small board, pieces, and a way in to guess
  if(!PUZ.length) return '';
  const c = pzCur(); if(!c) return '';
  const fresh = PZ_LAST && PZ_LAST.id===c.id && Date.now()-PZ_LAST.t < 2500;
  return `<button class="pz-mini${fresh ? ' pz-fresh' : ''}" type="button" data-act="pz-open" aria-label="Picture puzzle: ${c.rev.length} of ${PZK} pieces. Open it to guess.">${pzBoardFor(c, 'mini')}`
    + `<span class="pz-mini-l"><b>${c.rev.length}/${PZK}</b> pieces${fresh ? ' <span class="pz-plus">+1</span>' : ''}<span class="pz-mini-g">Guess</span></span></button>`;
}
function puzzleFbHTML(ok){   // in the answer feedback (phones and tablets): what this right answer did for the puzzle
  if(!PUZ.length || !ok) return '';
  const c = pzCur(); if(!c) return '';
  const fresh = PZ_LAST && PZ_LAST.id===c.id && Date.now()-PZ_LAST.t < 60000, full = c.rev.length>=PZK;
  if(!fresh && !full) return '';
  return `<button class="pz-fb" type="button" data-act="pz-open" aria-label="Picture puzzle: ${c.rev.length} of ${PZK} pieces. Open it to guess.">${pzBoardFor(c, 'fb')}`
    + `<span>${fresh ? `<b>+1 puzzle piece</b> · ${c.rev.length} of ${PZK}` : '<b>Every piece is uncovered</b>'}</span><span class="pz-mini-g">Guess</span></button>`;
}
let PZ_MODAL = null;
function pzModalHTML(){
  if(PZ_SOLVED) return pzSolvedHTML('modal');
  const c = pzCur(); if(!c) return '<p>No puzzle right now.</p>';
  const p = PUZBY[c.id], hidden = PZK - c.rev.length;
  return `<div class="pz-body pz-body-modal"><div class="pz-left">${pzBoardFor(c, 'modal')}</div><div class="stack pz-side"><h2 class="pz-title">What's the picture?</h2>`
    + `<div class="row pz-hints">${pzHints(p, c)}</div>${pzGuessForm('modal')}`
    + `<div class="row small"><span class="pill">${c.rev.length} of ${PZK} pieces</span><span class="pill good">Worth ${pzScore(c)} now</span>${hidden===0 ? '<button class="btn ghost small" data-act="pz-reveal">Show the answer</button>' : ''}</div></div></div>`;
}
function puzzleOpen(what){
  closePuzzle();
  const back = document.activeElement;
  const wrap = document.createElement('div'); wrap.className = 'pz-modal'; wrap.setAttribute('role', 'dialog'); wrap.setAttribute('aria-modal', 'true');
  wrap.setAttribute('aria-label', what==='collection' ? 'Picture collection' : 'Picture puzzle');
  wrap.innerHTML = `<div class="pz-sheet panel"><button class="btn ghost small pz-x" data-act="pz-close" aria-label="Close">Close</button><div class="pz-content">${what==='collection' ? pzCollectionHTML() : pzModalHTML()}</div></div>`;
  document.body.appendChild(wrap); PZ_MODAL = {el:wrap, what, back};
  const inp = wrap.querySelector('.pz-in'); (inp || wrap.querySelector('.pz-x')).focus({preventScroll:true});
}
function closePuzzle(){ if(!PZ_MODAL) return; const m = PZ_MODAL; PZ_MODAL = null; m.el.remove(); if(m.back && m.back.focus && document.body.contains(m.back)) m.back.focus({preventScroll:true}); }
function pzRefreshModal(){ if(PZ_MODAL && PZ_MODAL.what==='puzzle'){ const box = PZ_MODAL.el.querySelector('.pz-content'); if(box){ box.innerHTML = pzModalHTML(); const inp = box.querySelector('.pz-in'); if(inp) inp.focus({preventScroll:true}); } } }
function pzCollectionHTML(){
  const d = pzDone(), list = PUZ.filter(p=>d[p.id]);
  const tiles = list.map(p=>{ const e = d[p.id]; return `<figure class="pz-tile">${pzBoardHTML(p.id, Array.from({length:PZK}, (_,k)=>k), 'tile', -1)}<figcaption><b>${esc(p.answer)}</b><span class="small muted">${e.n ? `${e.pts} pt${e.pts===1?'':'s'}` : 'answer shown'}</span></figcaption></figure>`; }).join('');
  const left = PUZ.length - list.length;
  return `<h2 class="pz-title">Your picture collection</h2><p class="small muted">${pzSolvedCount()} of ${PUZ.length} pictures solved · ${pzTotal()} points</p>`
    + (list.length ? `<div class="pz-gallery">${tiles}${left ? `<div class="pz-tile pz-unknown" aria-label="${left} more to find"><span>?</span><span class="small muted">${left} more to find</span></div>` : ''}</div>` : `<p>Solve your first picture puzzle to start your collection.</p>`);
}
function pzRefreshViews(){   // after a piece or a guess: redraw what shows the puzzle, keeping what the learner typed
  const panel = $('#pz-panel'); if(panel && VIEW==='home'){ const t = document.createElement('div'); t.innerHTML = puzzlePanelHTML(); if(t.firstElementChild) panel.replaceWith(t.firstElementChild); }
  const mini = document.querySelector('.pz-mini'); if(mini){ const t = document.createElement('div'); t.innerHTML = puzzleMiniHTML(); if(t.firstElementChild) mini.replaceWith(t.firstElementChild); else mini.remove(); }
}
function pzSay(slot, html, cls){ document.querySelectorAll(`.pz-msg[data-slot="${slot}"]`).forEach(m=>{ m.className = 'pz-msg small ' + (cls || ''); m.innerHTML = html; }); }
function puzzleSubmit(form){
  const slot = form.dataset.slot, inp = form.querySelector('.pz-in'), val = inp ? inp.value : '';
  const r = puzzleGuess(val);
  if(r.state==='empty') return;
  if(r.state==='close'){ pzSay(slot, 'Close! Try to be more specific.', 'warn-t'); if(inp) inp.select(); return; }
  if(r.state==='wrong'){
    try{ SFX.play('buzz'); }catch(e){}
    if(slot==='modal') pzRefreshModal(); else pzRefreshViews();
    pzSay(slot, `Not quite. ${r.wrong>=2 ? 'Another hint is up.' : r.wrong===1 ? 'A hint is up.' : ''}`, 'bad-t');
    const again = document.querySelector(`.pz-guess[data-slot="${slot}"] .pz-in`); if(again){ again.value = val; again.select(); }
    return;
  }
  if(r.state==='right'){
    try{ SFX.play('tada'); }catch(e){} confetti();
    toast(`Picture solved: <b>${esc(PUZBY[r.id].answer)}</b> · +${r.pts} point${r.pts===1?'':'s'}`, 4000);
    if(slot==='modal') pzRefreshModal(); else pzRefreshViews();
  }
}
