(function(){
'use strict';
const DATA = JSON.parse(document.getElementById('data').textContent);
const SECTIONS = [
  {key:'reg',      name:'Insurance Regulation',           pct:10,   items:15, topics:['reg']},
  {key:'gen',      name:'General Insurance',              pct:10.5, items:16, topics:['gen']},
  {key:'basics',   name:'P&C Basics + Michigan Laws',     pct:20,   items:30, topics:['basics','mi']},
  {key:'dwelling', name:'Dwelling Policy',                pct:2.5,  items:4,  topics:['dwelling']},
  {key:'ho',       name:'Homeowners Policy',              pct:15,   items:22, topics:['ho']},
  {key:'auto',     name:'Automobile (incl. MI No-Fault)', pct:15,   items:22, topics:['auto']},
  {key:'cpp',      name:'Commercial Package Policy',      pct:12,   items:18, topics:['cpp']},
  {key:'bop',      name:'Businessowners Policy',          pct:6,    items:9,  topics:['bop']},
  {key:'wc',       name:"Workers' Compensation",          pct:5,    items:8,  topics:['wc']},
  {key:'other',    name:'Other Coverages & Options',      pct:4,    items:6,  topics:['other']}
];
const SEC = Object.fromEntries(SECTIONS.map(s=>[s.key,s]));
const T2S = {}; SECTIONS.forEach(s=>s.topics.forEach(t=>T2S[t]=s.key));
const QS = DATA.questions.map(q=>Object.assign({}, q, {sec:T2S[q.topic]})).filter(q=>q.sec);
const QBY = Object.fromEntries(QS.map(q=>[q.id,q]));
const CARDS = DATA.cards;
const MN = DATA.mnemonics || [], CP = DATA.pairs || [], VS = DATA.visuals || [], MS = DATA.matchsets || [];
const MN_BY_Q = {}; MN.forEach(m=>(m.question_ids||[]).forEach(id=>{ if(QBY[id]) (MN_BY_Q[id]=MN_BY_Q[id]||[]).push(m); }));
const PASS = 0.74, LETTERS = ['A','B','C','D'];
const DAY = 86400000, IV = [0,1,3,7,16,35,75];
const STREAK_MIN = 10;

/* ---------- utilities ---------- */
const $ = (s,el=document)=>el.querySelector(s);
const esc = s => String(s==null?'':s).replace(/[&<>"']/g, c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const pct = (a,b)=> b ? Math.round(100*a/b) : 0;
function shuffle(a){ a=a.slice(); for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1)); [a[i],a[j]]=[a[j],a[i]];} return a; }
function fmtTime(ms){ ms=Math.max(0,ms); const s=Math.floor(ms/1000), h=Math.floor(s/3600), m=Math.floor(s%3600/60), ss=s%60; return (h?h+':':'')+String(m).padStart(h?2:1,'0')+':'+String(ss).padStart(2,'0'); }
function lsGet(k){ try{ const v=localStorage.getItem(k); return v?JSON.parse(v):null; }catch(e){ return null; } }
function lsSet(k,v){ try{ localStorage.setItem(k, JSON.stringify(v)); }catch(e){} }
function lsDel(k){ try{ localStorage.removeItem(k); }catch(e){} }
function dayKey(d){ d=d||new Date(); return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0'); }
function startOfToday(){ const d=new Date(); d.setHours(0,0,0,0); return d.getTime(); }
function addDays(d,n){ const x=new Date(d); x.setDate(x.getDate()+n); return x; }
const money = n => '$'+Math.round(n).toLocaleString('en-US');

/* ---------- progress store ---------- */
const LS_KEY = 'mipc-progress-v1';
function blank(){ return {v:2, q:{}, cards:{}, exams:[], xp:0, days:{}, badges:{}, journal:{}, bestCombo:0, bestStreak:0,
  settings:{examDate:'', dailyGoal:40, recall:false, confidence:true}, games:{boss:{}, match:{}}, mn:{}, cp:{}, updated:0}; }
function migrate(p){
  const b = blank();
  p = Object.assign(b, p||{});
  p.settings = Object.assign(blank().settings, p.settings||{});
  p.games = Object.assign({boss:{}, match:{}}, p.games||{});
  ['q','cards','days','badges','journal','mn','cp'].forEach(k=>{ if(!p[k] || typeof p[k]!=='object') p[k]={}; });
  if(!Array.isArray(p.exams)) p.exams=[];
  Object.keys(p.q).forEach(id=>{ const s=p.q[id]; if(s.box==null){ s.box = s.last?1:0; s.due = s.last ? (s.t||Date.now())+DAY : 0; } });
  Object.keys(p.cards).forEach(id=>{ const c=p.cards[id]; if(typeof c==='number') p.cards[id]={box:c, due:0}; });
  p.v = 2;
  return p;
}
let P = migrate(lsGet(LS_KEY));
const sync = {ref:null, timer:null, writing:false, again:false};
function setSyncLabel(t){ const el=$('#sync'); if(el) el.textContent=t; }
function save(){
  P.updated = Date.now();
  lsSet(LS_KEY, P);
  if(!sync.ref) return;
  clearTimeout(sync.timer);
  sync.timer = setTimeout(flush, 1500);
}
async function flush(){
  if(!sync.ref) return;
  if(sync.writing){ sync.again=true; return; }
  sync.writing=true;
  try{ await sync.ref.set(JSON.parse(JSON.stringify(P))); setSyncLabel('Progress: saved to your account'); }
  catch(e){ setSyncLabel('Progress: this browser'); if(e && (e.code==='invalid_argument'||e.code==='revoked'||e.code==='not_granted')) sync.ref=null; }
  sync.writing=false;
  if(sync.again){ sync.again=false; flush(); }
}
async function initSync(){
  try{
    if(!window.claude || !window.claude.use) return;
    const [db,user] = await Promise.all([window.claude.use('db'), window.claude.use('user')]);
    if(!db || !user) return;
    const id = await user.id();
    if(!id) return;
    const ref = db.doc('data/users/'+id+'/progress');
    const snap = await ref.get();
    sync.ref = ref;
    if(snap.exists){
      const remote = snap.data() || {};
      if((remote.updated||0) >= (P.updated||0)){ P = migrate(JSON.parse(JSON.stringify(remote))); lsSet(LS_KEY,P); }
      else flush();
    } else if(P.updated){ flush(); }
    setSyncLabel('Progress: saved to your account');
    if(VIEW==='home') renderHome();
  }catch(e){ /* stay on browser storage */ }
}

/* ---------- day log, XP, levels, streaks ---------- */
function today(){ const k=dayKey(); return P.days[k] || (P.days[k]={n:0,c:0,xp:0}); }
function pruneDays(){ const ks=Object.keys(P.days).sort(); while(ks.length>200){ delete P.days[ks.shift()]; } }
const TITLES = [[1,'Applicant'],[3,'Pre-licensing Student'],[6,'Exam Candidate'],[10,'Test-Day Ready'],[15,'Licensed Producer'],[21,'Agency Pro'],[28,'Insurance Legend']];
function levelOf(xp){
  const level = Math.floor(Math.sqrt(Math.max(0,xp)/40))+1;
  const lo = 40*(level-1)*(level-1), hi = 40*level*level;
  let title = TITLES[0][1]; TITLES.forEach(([l,t])=>{ if(level>=l) title=t; });
  return {level, title, lo, hi, frac:(xp-lo)/(hi-lo)};
}
let goalToastDay = null;
function addXP(n){
  if(!n) return;
  const before = levelOf(P.xp).level;
  P.xp += n; today().xp += n;
  const after = levelOf(P.xp);
  if(after.level>before){ toast(`<b>Level ${after.level}</b> reached: ${esc(after.title)}`); confetti(); }
}
function studyDay(k){ const d=P.days[k]; return !!(d && d.n>=STREAK_MIN); }
function streak(){
  let d=new Date(), s=0;
  if(!studyDay(dayKey(d))) d=addDays(d,-1);
  while(studyDay(dayKey(d))){ s++; d=addDays(d,-1); }
  return s;
}
function logAnswer(ok){
  const d=today(); d.n++; if(ok) d.c++;
  pruneDays();
  const s=streak(); if(s>P.bestStreak) P.bestStreak=s;
  if(d.n===P.settings.dailyGoal && goalToastDay!==dayKey()){ goalToastDay=dayKey(); P.goalMet=(P.goalMet||0)+1; toast('<b>Daily goal met.</b> Nice work.'); confetti(); addXP(20); }
}
function totalAnswered(){ return Object.values(P.q).reduce((s,x)=>s+(x.a||0),0); }
function seenCount(){ return QS.filter(q=>P.q[q.id]).length; }

/* ---------- spaced repetition ---------- */
function srsAnswer(id, ok, conf){
  const s = P.q[id] || {a:0,c:0,last:0,t:0,box:0,due:0};
  s.a++; if(ok) s.c++; s.last = ok?1:0; s.t = Date.now();
  if(ok){
    if(conf==='guess') s.box = 1;
    else if(conf==='unsure') s.box = Math.max(1, s.box||0);
    else s.box = Math.min(IV.length-1, (s.box||0)+1);
    s.due = startOfToday() + IV[s.box]*DAY; s.cw = 0;
  } else {
    s.box = 0; s.due = Date.now(); s.cw = conf==='sure' ? 1 : 0;
  }
  s.conf = conf || null;
  P.q[id] = s;
  logAnswer(ok);
}
function dueIds(){
  const now=Date.now();
  return QS.filter(q=>P.q[q.id] && (P.q[q.id].due||0)<=now)
    .sort((a,b)=>{ const x=P.q[a.id], y=P.q[b.id]; return (y.cw||0)-(x.cw||0) || (x.box||0)-(y.box||0) || (x.due||0)-(y.due||0); })
    .map(q=>q.id);
}
function newWeighted(n){
  const out=[];
  SECTIONS.forEach(s=>{
    const pool = shuffle(QS.filter(q=>q.sec===s.key && !P.q[q.id]));
    out.push(...pool.slice(0, Math.ceil(n*s.items/150)+1));
  });
  return shuffle(out).slice(0,n).map(q=>q.id);
}
function qLevel(id){ const s=P.q[id]; if(!s) return 0; if(!s.last) return 1; if((s.box||0)<=1) return 2; if((s.box||0)===2) return 3; return 4; }
function secMastery(key){ const qs=QS.filter(q=>q.sec===key); return qs.length ? qs.filter(q=>qLevel(q.id)>=3).length/qs.length : 0; }
function secStats(key){
  const qs = QS.filter(q=>q.sec===key);
  let seen=0, lastRight=0;
  qs.forEach(q=>{ const s=P.q[q.id]; if(s){ seen++; if(s.last) lastRight++; } });
  return {total:qs.length, seen, lastRight, acc: seen? lastRight/seen : null};
}
function missedIds(secKey){ return QS.filter(q=>(!secKey||q.sec===secKey) && P.q[q.id] && !P.q[q.id].last).map(q=>q.id); }
function predicted(){
  let w=0, sum=0;
  SECTIONS.forEach(s=>{ const st=secStats(s.key); if(st.acc!==null){ w+=s.pct; sum+=s.pct*st.acc; } });
  return w ? sum/w : null;
}

/* ---------- badges ---------- */
const BADGES = [
  {id:'first', t:'First step', d:'Answer your first question', f:()=>totalAnswered()>=1},
  {id:'q100', t:'Century', d:'Answer 100 questions', f:()=>totalAnswered()>=100},
  {id:'q500', t:'Workhorse', d:'Answer 500 questions', f:()=>totalAnswered()>=500},
  {id:'seenall', t:'Full coverage', d:'See every question in the bank', f:()=>seenCount()>=QS.length},
  {id:'goal', t:'Goal getter', d:'Hit your daily goal', f:()=>(P.goalMet||0)>=1},
  {id:'streak3', t:'On a roll', d:'3-day study streak', f:()=>P.bestStreak>=3},
  {id:'streak7', t:'Habit formed', d:'7-day study streak', f:()=>P.bestStreak>=7},
  {id:'combo10', t:'Hot hand', d:'10 right in a row', f:()=>P.bestCombo>=10},
  {id:'mock1', t:'Dress rehearsal', d:'Finish a mock exam', f:()=>P.exams.length>=1},
  {id:'mockpass', t:'Passing grade', d:'74%+ on a mock exam', f:()=>P.exams.some(e=>e.score/e.total>=PASS)},
  {id:'mock85', t:'Book the exam', d:'85%+ on two mock exams', f:()=>P.exams.filter(e=>e.score/e.total>=0.85).length>=2},
  {id:'light15', t:'Lightning fast', d:'15+ in a Lightning Round', f:()=>(P.games.lightBest||0)>=15},
  {id:'surv25', t:'Survivor', d:'25+ in Survival', f:()=>(P.games.survBest||0)>=25},
  {id:'boss3', t:'Boss slayer', d:'Defeat 3 section bosses', f:()=>Object.values(P.games.boss).filter(b=>b.won).length>=3},
  {id:'bossall', t:'Final boss', d:'Defeat all 10 section bosses', f:()=>SECTIONS.every(s=>P.games.boss[s.key] && P.games.boss[s.key].won)},
  {id:'match5', t:'Matchmaker', d:'Clear 5 match sets', f:()=>Object.keys(P.games.match).length>=5},
  {id:'hooks25', t:'Memory athlete', d:'Learn 25 memory hooks', f:()=>Object.keys(P.mn).length>=25},
  {id:'pairs5', t:'Sharp eye', d:'Ace 5 confusion drills', f:()=>Object.values(P.cp).filter(v=>v>=1).length>=5},
  {id:'math10', t:'Number cruncher', d:'Solve 10 math lab problems', f:()=>(P.games.math||0)>=10},
].concat(SECTIONS.map(s=>({id:'m_'+s.key, t:'Mastered: '+s.name, d:'85% of the section answered right twice', f:()=>secMastery(s.key)>=0.85})));
function checkBadges(){
  let earned=false;
  BADGES.forEach(b=>{ if(!P.badges[b.id] && b.f()){ P.badges[b.id]=Date.now(); toast(`Badge earned: <b>${esc(b.t)}</b>`); confetti(); addXP(25); earned=true; } });
  if(earned) save();
}

/* ---------- toasts & confetti ---------- */
function toast(html){
  const box=$('#toasts'); if(!box) return;
  const t=document.createElement('div'); t.className='toast'; t.innerHTML=html; box.appendChild(t);
  while(box.children.length>2) box.firstElementChild.remove();
  setTimeout(()=>t.remove(), 2800);
}
const reduceMotion = (()=>{ try{ return window.matchMedia('(prefers-reduced-motion: reduce)').matches; }catch(e){ return false; } })();
function confetti(){
  if(reduceMotion) return;
  const c=$('#confetti'); if(!c || !c.getContext) return;
  const ctx=c.getContext('2d'); const W=c.width=window.innerWidth, H=c.height=window.innerHeight;
  const cs=getComputedStyle(document.documentElement);
  const colors=['--accent','--good','--gold','--bad','--warn'].map(v=>cs.getPropertyValue(v).trim()||'#888');
  const parts=Array.from({length:110},()=>({x:W/2+(Math.random()-.5)*W*.3, y:H*.35, vx:(Math.random()-.5)*9, vy:-Math.random()*9-3, r:Math.random()*6+3, c:colors[Math.floor(Math.random()*colors.length)], a:Math.random()*6}));
  let t0=null;
  function frame(ts){ if(t0===null) t0=ts; const dt=ts-t0; ctx.clearRect(0,0,W,H);
    parts.forEach(p=>{ p.vy+=0.25; p.x+=p.vx; p.y+=p.vy; p.a+=0.2; ctx.save(); ctx.translate(p.x,p.y); ctx.rotate(p.a); ctx.fillStyle=p.c; ctx.fillRect(-p.r/2,-p.r/4,p.r,p.r/2); ctx.restore(); });
    if(dt<1600) requestAnimationFrame(frame); else ctx.clearRect(0,0,W,H); }
  requestAnimationFrame(frame);
}

/* ---------- navigation ---------- */
let VIEW = 'home';
let timers = [];
function clearTimers(){ timers.forEach(t=>{ clearInterval(t); clearTimeout(t); }); timers=[]; }
function go(v, opts){
  if(VIEW==='games' && v!=='games' && GAME && GAME.live) endGame(true);
  VIEW = v;
  document.querySelectorAll('.tab').forEach(t=>{ const on=t.dataset.view===v; t.setAttribute('aria-selected', String(on)); if(on && t.scrollIntoView) t.scrollIntoView({block:'nearest',inline:'nearest'}); });
  document.querySelectorAll('.view').forEach(el=>el.hidden = (el.id!=='view-'+v));
  if(v==='home') renderHome();
  if(v==='study') renderStudy(opts&&opts.sec);
  if(v==='memory') renderMemory(opts);
  if(v==='practice') renderPractice(opts);
  if(v==='games') renderGames(opts);
  if(v==='math') renderMath(opts);
  if(v==='exam') renderExam();
  if(v==='cards') renderCards(opts&&opts.sec);
  if(v==='numbers') renderNumbers();
  window.scrollTo({top:0});
}
document.querySelectorAll('.tab').forEach(t=>t.addEventListener('click',()=>go(t.dataset.view)));

/* ---------- Today (dashboard) ---------- */
function meterClass(acc){ return acc===null?'':(acc>=0.85?'good':acc>=PASS?'warn':'bad'); }
function ringSVG(n, goal){
  const r=38, C=2*Math.PI*r, f=Math.min(1, goal? n/goal : 0);
  return `<svg class="ring" viewBox="0 0 92 92" role="img" aria-label="${n} of ${goal} questions today"><circle class="bgc" cx="46" cy="46" r="${r}"></circle><circle class="fgc" cx="46" cy="46" r="${r}" stroke-dasharray="${C.toFixed(1)}" stroke-dashoffset="${(C*(1-f)).toFixed(1)}" transform="rotate(-90 46 46)"></circle><text x="46" y="48" text-anchor="middle">${n}</text><text class="sub" x="46" y="62" text-anchor="middle">of ${goal}</text></svg>`;
}
function daysLeft(){
  const d=P.settings.examDate; if(!d) return null;
  const [y,m,dd]=d.split('-').map(Number); const ex=new Date(y,m-1,dd).getTime();
  return Math.round((ex-startOfToday())/DAY);
}
function planText(){
  const dl=daysLeft(); if(dl===null) return '';
  if(dl<0) return 'Your exam date has passed. Update it in Settings below.';
  if(dl===0) return 'Exam day. Skim Key numbers and your memory hooks, then go in rested.';
  const unseen=QS.length-seenCount(), due=dueIds().length;
  const perDay=Math.max(20, Math.ceil((unseen+due)/Math.max(1,dl-2)) + 10);
  const mockAdvice = dl<=7 ? 'Take a full mock exam every other day this week.' : dl<=21 ? 'Take one full mock exam each week.' : 'Start mock exams once you have seen most of the bank.';
  return `About <b>${perDay} questions a day</b> covers every unseen question and keeps your reviews current, with 2 light days before the exam. ${mockAdvice}`;
}
function sparkSVG(){
  const ds=[]; for(let i=13;i>=0;i--){ const k=dayKey(addDays(new Date(),-i)); ds.push({k, n:(P.days[k]||{}).n||0}); }
  const mx=Math.max(10, ...ds.map(d=>d.n)); const W=280,H=60,bw=W/14;
  return `<svg viewBox="0 0 ${W} ${H+14}" style="width:100%;max-width:320px;height:auto" role="img" aria-label="Questions answered over the last 14 days">${ds.map((d,i)=>{ const h=Math.round((d.n/mx)*H); return `<rect x="${(i*bw+2).toFixed(1)}" y="${H-h}" width="${(bw-4).toFixed(1)}" height="${Math.max(h,1)}" rx="2" fill="${d.n>=STREAK_MIN?'var(--accent)':'var(--line)'}"><title>${d.k}: ${d.n}</title></rect>`; }).join('')}<text x="0" y="${H+12}" font-size="10" fill="var(--muted)" font-family="var(--f-mono)">14 days ago</text><text x="${W}" y="${H+12}" font-size="10" fill="var(--muted)" text-anchor="end" font-family="var(--f-mono)">today</text></svg>`;
}
function masteryMap(){
  return SECTIONS.map(s=>{
    const subs = {};
    QS.filter(q=>q.sec===s.key).forEach(q=>{ const k=q.sub||'General'; (subs[k]=subs[k]||[]).push(q.id); });
    const tiles = Object.keys(subs).sort().map(sub=>{
      const ids=subs[sub], lv=ids.map(qLevel).filter(x=>x>0);
      const m = lv.length ? Math.max(1, Math.round(lv.reduce((a,b)=>a+b,0)/lv.length)) : 0;
      return `<button data-sub="${esc(sub)}" data-sec="${s.key}" data-m="${m}" title="${esc(sub)} (${ids.length} question${ids.length>1?'s':''})" aria-label="${esc(sub)}"></button>`;
    }).join('');
    return `<div class="msec"><div class="small"><b>${esc(s.name)}</b><div class="muted mono" style="font-size:11px">${Math.round(secMastery(s.key)*100)}% solid or mastered</div></div><div class="tiles">${tiles}</div></div>`;
  }).join('');
}
function renderHome(){
  checkBadges();
  const el=$('#view-home');
  const t=today(), goal=P.settings.dailyGoal, st=streak(), lv=levelOf(P.xp);
  const due=dueIds().length, unseen=QS.length-seenCount();
  const pr=predicted(), dl=daysLeft();
  const verdict = pr===null ? `<span class="pill">No answers yet</span>` : pr>=0.85 ? `<span class="pill good">On track</span>` : pr>=PASS ? `<span class="pill warn">Borderline</span>` : `<span class="pill bad">Below passing</span>`;
  const rows = SECTIONS.map(s=>{ const stt=secStats(s.key), acc=stt.acc;
    return `<tr><td><button class="btn ghost small" data-act="practice-sec" data-sec="${s.key}" style="padding:4px 8px;text-align:left">${esc(s.name)}</button></td><td class="num">${s.pct}%</td><td class="num">${s.items}</td><td class="num">${stt.seen}/${stt.total}</td><td style="min-width:120px"><div class="row" style="gap:8px;flex-wrap:nowrap"><div class="meter ${meterClass(acc)}" style="flex:1"><span style="width:${acc===null?0:Math.round(acc*100)}%"></span></div><span class="mono small" style="width:38px;text-align:right">${acc===null?'—':Math.round(acc*100)+'%'}</span></div></td></tr>`; }).join('');
  const earned = BADGES.filter(b=>P.badges[b.id]).length;
  el.innerHTML = `
  <div class="stack">
    <div class="today-hero">
      <div class="panel">
        <div class="row" style="justify-content:space-between;align-items:flex-start;gap:18px">
          <div class="stack" style="gap:12px;flex:1;min-width:220px">
            <div class="eyebrow" style="color:var(--muted)">Today</div>
            <div class="statrow">
              <div class="stat"><span class="n"><span class="flame" aria-hidden="true"></span>${st}</span><span class="l">day streak</span></div>
              <div class="stat"><span class="n">${due}</span><span class="l">reviews due</span></div>
              <div class="stat"><span class="n">${unseen}</span><span class="l">not seen yet</span></div>
            </div>
            <div>
              <div class="row" style="justify-content:space-between"><span class="level">Level ${lv.level} · ${esc(lv.title)}</span><span class="mono small muted">${P.xp} XP</span></div>
              <div class="xpbar" style="margin-top:6px"><span style="width:${Math.round(lv.frac*100)}%"></span></div>
              <div class="mono small muted" style="margin-top:4px">${lv.hi-P.xp} XP to level ${lv.level+1}</div>
            </div>
            <div class="row">
              <button class="btn primary cta-big" data-act="review">Start today's session</button>
              <button class="btn" data-act="lightning">Lightning round</button>
            </div>
            <p class="small muted" style="margin:0">Today's session fills what's left of your daily goal (at least 10 questions). Due reviews come first, starting with confident-but-wrong answers, then your weakest questions. Any spots left go to new questions from every section, weighted like the exam, and once you have seen them all, to the questions coming due soonest.</p>
          </div>
          ${ringSVG(t.n, goal)}
        </div>
      </div>
      <div class="panel stack" style="gap:14px">
        <div>
          <div class="eyebrow" style="color:var(--muted)">Exam day</div>
          ${dl===null ? `<p style="margin:6px 0">Set your exam date to get a countdown and a daily target.</p><div class="row"><input type="date" id="exam-date" aria-label="Exam date"><button class="btn" data-act="set-date">Save date</button></div>`
            : `<div class="row" style="align-items:baseline;gap:10px;margin-top:6px"><span class="countdown">${Math.max(dl,0)}</span><span class="muted">day${dl===1?'':'s'} until your exam</span></div><p class="small" style="margin:8px 0 0">${planText()}</p>`}
        </div>
        <div>
          <div class="eyebrow" style="color:var(--muted)">Projected score</div>
          <div class="row" style="gap:12px;align-items:baseline;margin-top:6px"><span class="score-big" style="font-size:44px">${pr===null?'—':Math.round(pr*100)+'%'}</span>${verdict}</div>
          <p class="muted small" style="margin:6px 0 0">Weighted by the PSI outline from your latest answer on each question you have answered. Sections you haven't started are left out until you answer one. Passing is 74% (111 of 150); aim for 85%+.</p>
        </div>
        <div>${sparkSVG()}</div>
      </div>
    </div>

    <div class="panel">
      <div class="row" style="justify-content:space-between"><h2>Mastery map</h2><span class="small muted">Each square is one outline topic, colored by the average of the questions you have answered in it (unanswered questions don't count). Tap one to practice it.</span></div>
      <div class="legend" style="margin:8px 0 14px"><span><i style="background:var(--tile0)"></i>Not started</span><span><i style="background:var(--tile1)"></i>Missed last time</span><span><i style="background:var(--tile2)"></i>Learning</span><span><i style="background:var(--tile3)"></i>Getting solid</span><span><i style="background:var(--tile4)"></i>Mastered</span></div>
      <div class="mastery" id="mastery">${masteryMap()}</div>
    </div>

    <div class="dash">
      <div class="panel">
        <h2>Exam blueprint &amp; your accuracy</h2>
        <p class="muted small" style="margin:0 0 10px">Weights and item counts are from PSI's Michigan Property and Casualty Producer/Solicitor content outline (Series 16-81).</p>
        <div class="tbl"><table><thead><tr><th>Section</th><th class="num">Weight</th><th class="num">Exam items</th><th class="num">Seen</th><th>Accuracy</th></tr></thead><tbody>${rows}</tbody></table></div>
      </div>
      <div class="stack">
        <div class="panel">
          <h3>Before test day</h3>
          <div class="tbl" style="margin-top:8px"><table class="small"><tbody>
            <tr><td>License application</td><td>File through NIPR: $10 + $5 fee for a producer license, $20 + $5 for a solicitor. DIFS lists this as step 1. It stays valid 180 days (six months for a solicitor), so pass the exam within that window or refile and pay again.</td></tr>
            <tr><td>Prelicensing course</td><td>40 hours, finished before the exam (certificate good 12 months)</td></tr>
            <tr><td>Exam fee</td><td>$41 to PSI</td></tr>
            <tr><td>Where</td><td>In person at a PSI test center (remote testing ended in June 2025)</td></tr>
            <tr><td>Bring</td><td>Unexpired government ID with photo and signature; arrive 30 minutes early</td></tr>
            <tr><td>Passing score</td><td>Good 12 months from the pass date</td></tr>
          </tbody></table></div>
          <button class="btn" data-act="study-logistics" style="margin-top:12px">Full exam-day guide</button>
        </div>
        <div class="panel settings">
          <h3>Settings</h3>
          <div class="stack" style="gap:10px;margin-top:10px">
            <label class="field" for="set-goal">Daily goal (questions)
              <select id="set-goal">${[20,30,40,60,80,100].map(n=>`<option ${n===goal?'selected':''}>${n}</option>`).join('')}</select>
            </label>
            <label class="toggle"><input type="checkbox" id="set-conf" ${P.settings.confidence?'checked':''}> Ask how sure I am before showing the answer</label>
            <label class="toggle"><input type="checkbox" id="set-recall" ${P.settings.recall?'checked':''}> Hide the choices until I try to recall the answer</label>
            ${dl!==null?`<div class="row"><input type="date" id="exam-date" value="${esc(P.settings.examDate)}" aria-label="Exam date"><button class="btn" data-act="set-date">Change exam date</button></div>`:''}
            <div class="row"><button class="btn ghost small" data-act="reset">Reset progress</button><span class="small muted">${sync.ref?'Saved to your account':'Saved in this browser'}</span></div>
            <div id="reset-box"></div>
          </div>
        </div>
      </div>
    </div>

    <div class="panel">
      <div class="row" style="justify-content:space-between"><h2>Badges</h2><span class="mono small muted">${earned} of ${BADGES.length}</span></div>
      <div class="badges" style="margin-top:12px">${BADGES.map(b=>`<div class="badge ${P.badges[b.id]?'on':''}"><span class="medal" aria-hidden="true">${P.badges[b.id]?'★':'·'}</span><div style="min-width:0"><div class="bt">${esc(b.t)}</div><div class="bd">${esc(b.d)}</div></div></div>`).join('')}</div>
    </div>
  </div>`;
  $('#set-goal').addEventListener('change', e=>{ P.settings.dailyGoal=+e.target.value; save(); renderHome(); });
  $('#set-conf').addEventListener('change', e=>{ P.settings.confidence=e.target.checked; save(); });
  $('#set-recall').addEventListener('change', e=>{ P.settings.recall=e.target.checked; save(); });
  $('#mastery').addEventListener('click', e=>{ const b=e.target.closest('button[data-sub]'); if(!b) return; const ids=QS.filter(q=>q.sec===b.dataset.sec && (q.sub||'General')===b.dataset.sub).map(q=>q.id); startSession({kind:'practice', ids:shuffle(ids), label:b.dataset.sub}); go('practice'); });
}

/* ---------- Learn (study guide) ---------- */
let STUDY_SEC = null;
function renderStudy(sec){
  if(sec) STUDY_SEC = sec;
  const guides = DATA.guide;
  if(!STUDY_SEC || !guides.find(g=>g.id===STUDY_SEC)) STUDY_SEC = guides[0].id;
  const el = $('#view-study');
  const g = guides.find(x=>x.id===STUDY_SEC);
  const hooks = MN.filter(m=>(g.secs||[]).includes(m.sec)).length;
  el.innerHTML = `
  <div class="study">
    <div>
      <label class="field" for="study-q" style="margin-bottom:10px">Search the guide
        <input type="search" id="study-q" placeholder="e.g. coinsurance, PIP, vacancy">
      </label>
      <nav class="toc" aria-label="Study guide sections">
        ${guides.map(x=>`<button data-g="${x.id}" aria-current="${x.id===STUDY_SEC}"><span>${esc(x.title)}</span>${x.weight?`<span class="w">${esc(x.weight)}</span>`:''}</button>`).join('')}
      </nav>
    </div>
    <article class="guide ${g.id==='howto'?'howto':''}" id="guide-body">
      <div class="eyebrow" style="color:var(--muted)">${esc(g.weight||'')}</div>
      <h2>${esc(g.title)}</h2>
      ${g.secs && g.secs.length ? `<div class="row" style="margin:12px 0 4px">${g.secs.map(k=>`<button class="btn primary" data-act="practice-sec" data-sec="${k}">Practice ${esc(SEC[k].name)}</button>`).join('')}${hooks?`<button class="btn" data-act="hooks-sec" data-sec="${g.secs[0]}">Memory hooks (${hooks})</button>`:''}<button class="btn" data-act="cards-sec" data-sec="${g.secs[0]}">Flashcards</button></div>`:''}
      <div id="guide-content">${g.html}</div>
    </article>
  </div>`;
  el.querySelectorAll('.toc button').forEach(b=>b.addEventListener('click',()=>{ renderStudy(b.dataset.g); window.scrollTo({top:0}); }));
  const input = $('#study-q');
  input.addEventListener('input', ()=>searchGuide(input.value));
}
function searchGuide(q){
  q = q.trim().toLowerCase();
  const body = $('#guide-content');
  if(!q){ const g = DATA.guide.find(x=>x.id===STUDY_SEC); body.innerHTML = g.html; return; }
  const hits = [];
  DATA.guide.forEach(g=>{
    const tmp = document.createElement('div'); tmp.innerHTML = g.html;
    tmp.querySelectorAll('li, p, tr').forEach(n=>{
      if(n.tagName==='LI' && n.querySelector('li')) return;
      if(n.textContent.toLowerCase().includes(q)) hits.push({g, html: n.tagName==='TR' ? '<div class="tbl"><table><tbody>'+n.outerHTML+'</tbody></table></div>' : '<p>'+n.innerHTML+'</p>'});
    });
  });
  const re = new RegExp(q.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'),'gi');
  body.innerHTML = hits.length ? `<p class="muted">${hits.length} match${hits.length===1?'':'es'} across the guide</p>` + hits.slice(0,200).map(h=>`<div style="border-top:1px solid var(--line);padding-top:6px;margin-top:6px"><div class="eyebrow" style="color:var(--muted)">${esc(h.g.title)}</div>${highlight(h.html, re)}</div>`).join('') : `<div class="empty">No matches for “${esc(q)}”.</div>`;
}
function highlight(html, re){
  const tmp=document.createElement('div'); tmp.innerHTML=html;
  const walker=document.createTreeWalker(tmp, NodeFilter.SHOW_TEXT); const nodes=[]; while(walker.nextNode()) nodes.push(walker.currentNode);
  nodes.forEach(n=>{ re.lastIndex=0; if(!re.test(n.nodeValue)) return; re.lastIndex=0; const span=document.createElement('span'); span.innerHTML=esc(n.nodeValue).replace(re, m=>'<mark>'+m+'</mark>'); n.replaceWith(span); });
  return tmp.innerHTML;
}

/* ---------- Memory: hooks, confusion pairs, visuals ---------- */
let MEM = {tab:'hooks', sec:'all', q:'', selftest:false, pair:null, drill:null};
function secChips(cur, items){
  const used = new Set(items.map(x=>x.sec));
  return `<div class="subtabs" role="group" aria-label="Filter by section"><button class="chip" data-msec="all" aria-pressed="${cur==='all'}">All</button>${SECTIONS.filter(s=>used.has(s.key)).map(s=>`<button class="chip" data-msec="${s.key}" aria-pressed="${cur===s.key}">${esc(s.name)}</button>`).join('')}</div>`;
}
function renderMemory(opts){
  if(opts){ if(opts.tab) MEM.tab=opts.tab; if(opts.sec) MEM.sec=opts.sec; }
  const el=$('#view-memory');
  const tabs = `<div class="subtabs" role="tablist" aria-label="Memory aids"><button class="chip" data-mtab="hooks" aria-pressed="${MEM.tab==='hooks'}">Memory hooks (${MN.length})</button><button class="chip" data-mtab="pairs" aria-pressed="${MEM.tab==='pairs'}">Confusion pairs (${CP.length})</button><button class="chip" data-mtab="visuals" aria-pressed="${MEM.tab==='visuals'}">Picture summaries (${VS.length})</button></div>`;
  let body='';
  if(MEM.tab==='hooks') body = hooksHTML();
  if(MEM.tab==='pairs') body = MEM.pair ? pairHTML() : pairsListHTML();
  if(MEM.tab==='visuals') body = visualsHTML();
  el.innerHTML = `<div class="stack"><div class="panel lede" style="max-width:none"><h2>Memory aids</h2><p class="muted" style="margin:0">Hooks turn lists and numbers into something your brain can grab. Confusion pairs drill the look-alike terms the exam loves to swap. Every hook lists the exact facts it stands for, so the trick never replaces the rule.</p></div>${tabs}${body}</div>`;
  el.querySelectorAll('[data-mtab]').forEach(b=>b.addEventListener('click',()=>{ MEM.tab=b.dataset.mtab; MEM.pair=null; MEM.drill=null; renderMemory(); }));
  el.querySelectorAll('[data-msec]').forEach(b=>b.addEventListener('click',()=>{ MEM.sec=b.dataset.msec; renderMemory(); }));
  const s=$('#mem-q'); if(s){ s.addEventListener('input',()=>{ MEM.q=s.value; const pos=s.selectionStart; renderMemory(); const s2=$('#mem-q'); s2.focus(); try{s2.setSelectionRange(pos,pos);}catch(e){} }); }
  const st=$('#mem-self'); if(st) st.addEventListener('change',()=>{ MEM.selftest=st.checked; renderMemory(); });
  el.querySelectorAll('[data-reveal]').forEach(b=>b.addEventListener('click',()=>{ b.closest('.hook').querySelector('.hk').style.filter='none'; b.remove(); }));
  el.querySelectorAll('[data-learn]').forEach(b=>b.addEventListener('click',()=>{ const id=b.dataset.learn; if(!P.mn[id]){ P.mn[id]=Date.now(); addXP(2); checkBadges(); save(); } b.textContent='Learned'; b.disabled=true; }));
  el.querySelectorAll('[data-hookq]').forEach(b=>b.addEventListener('click',()=>{ const m=MN.find(x=>x.id===b.dataset.hookq); const ids=(m.question_ids||[]).filter(id=>QBY[id]); if(ids.length){ startSession({kind:'practice', ids:shuffle(ids), label:'Hook: '+m.title}); go('practice'); } }));
  el.querySelectorAll('[data-pair]').forEach(b=>b.addEventListener('click',()=>{ MEM.pair=b.dataset.pair; MEM.drill=null; renderMemory(); window.scrollTo({top:0}); }));
  const back=$('#pair-back'); if(back) back.addEventListener('click',()=>{ MEM.pair=null; MEM.drill=null; renderMemory(); });
  const dr=$('#drill-start'); if(dr) dr.addEventListener('click',()=>{ const p=CP.find(x=>x.id===MEM.pair); MEM.drill={i:0, right:0, order:shuffle(p.drills.map((_,i)=>i)), ans:null}; renderMemory(); });
  el.querySelectorAll('[data-dans]').forEach(b=>b.addEventListener('click',()=>drillAnswer(b.dataset.dans)));
  const dn=$('#drill-next'); if(dn) dn.addEventListener('click',()=>{ MEM.drill.i++; MEM.drill.ans=null; renderMemory(); });
}
function hooksHTML(){
  const q=MEM.q.trim().toLowerCase();
  const list = MN.filter(m=>(MEM.sec==='all'||m.sec===MEM.sec) && (!q || JSON.stringify(m).toLowerCase().includes(q)));
  const learned = MN.filter(m=>P.mn[m.id]).length;
  return `${secChips(MEM.sec, MN)}
  <div class="row" style="justify-content:space-between;margin-bottom:12px"><label class="field" for="mem-q" style="min-width:240px">Search hooks<input type="search" id="mem-q" value="${esc(MEM.q)}" placeholder="e.g. PIP, coinsurance, burglary"></label><label class="toggle"><input type="checkbox" id="mem-self" ${MEM.selftest?'checked':''}> Self-test: hide each hook until I try to recall it</label><span class="mono small muted">${learned} of ${MN.length} learned</span></div>
  ${list.length ? `<div class="hook-grid">${list.map(m=>`
    <div class="hook">
      <div class="row" style="justify-content:space-between;gap:6px"><span class="pill">${esc(m.technique)}</span><span class="mono small muted">${esc(SEC[m.sec]?SEC[m.sec].name:'')}</span></div>
      <div class="ht">${esc(m.title)}</div>
      <div class="hk" style="${MEM.selftest?'filter:blur(7px)':''}">${esc(m.hook)}</div>
      ${MEM.selftest?`<button class="btn small" data-reveal="1">Reveal hook</button>`:''}
      <ul>${(m.unpack||[]).map(u=>`<li>${esc(u)}</li>`).join('')}</ul>
      ${m.watch_out?`<div class="watch"><b>Watch out:</b> ${esc(m.watch_out)}</div>`:''}
      <cite>${esc(m.source)}</cite>
      <div class="row" style="margin-top:auto">${(m.question_ids||[]).some(id=>QBY[id])?`<button class="btn small" data-hookq="${m.id}">Practice (${(m.question_ids||[]).filter(id=>QBY[id]).length})</button>`:''}<button class="btn ghost small" data-learn="${m.id}" ${P.mn[m.id]?'disabled':''}>${P.mn[m.id]?'Learned':'Mark learned'}</button></div>
    </div>`).join('')}</div>` : `<div class="empty">No hooks match.</div>`}`;
}
function pairsListHTML(){
  const list = CP.filter(p=>MEM.sec==='all'||p.sec===MEM.sec);
  return `${secChips(MEM.sec, CP)}<div class="hook-grid">${list.map(p=>`<div class="hook"><div class="row" style="justify-content:space-between"><span class="mono small muted">${esc(SEC[p.sec]?SEC[p.sec].name:'')}</span>${P.cp[p.id]!=null?`<span class="pill ${P.cp[p.id]>=1?'good':'warn'}">Best ${Math.round(P.cp[p.id]*100)}%</span>`:''}</div><div class="ht" style="font-size:17px">${esc(p.title)}</div><div class="small muted">${esc(p.tell)}</div><div class="row" style="margin-top:auto"><button class="btn small primary" data-pair="${p.id}">Study &amp; drill</button></div></div>`).join('')}</div>`;
}
function pairHTML(){
  const p = CP.find(x=>x.id===MEM.pair);
  const head = `<div class="row" style="justify-content:space-between"><button class="btn ghost" id="pair-back">All pairs</button><span class="mono small muted">${esc(SEC[p.sec]?SEC[p.sec].name:'')}</span></div><h2 style="margin:10px 0">${esc(p.title)}</h2>`;
  const sides = `<div class="pairs">${p.sides.map(s=>`<div class="side"><h4>${esc(s.name)}</h4><ul>${s.points.map(x=>`<li>${esc(x)}</li>`).join('')}</ul></div>`).join('')}</div><div class="tell">${esc(p.tell)}</div><cite>${esc(p.source)}</cite>`;
  if(!MEM.drill) return `<div class="panel">${head}${sides}<div class="row" style="margin-top:14px"><button class="btn primary" id="drill-start">Drill it (${p.drills.length} quick calls)</button></div></div>`;
  const D=MEM.drill;
  if(D.i>=D.order.length){
    const frac=D.right/D.order.length; P.cp[p.id]=Math.max(P.cp[p.id]||0, frac); save(); checkBadges();
    return `<div class="panel">${head}<div class="score-big">${D.right}/${D.order.length}</div><p class="muted">${frac>=1?'Perfect. These two will not trip you up.':'Review the side-by-side above and drill again.'}</p><div class="row"><button class="btn primary" id="drill-start">Drill again</button></div>${sides}</div>`;
  }
  const d=p.drills[D.order[D.i]];
  return `<div class="panel">${head}<div class="mono small muted">Call ${D.i+1} of ${D.order.length}</div><p class="stem" style="margin-top:8px">${esc(d.prompt)}</p>
    <div class="row">${p.sides.map(s=>{ let cls='btn'; if(D.ans){ if(s.name===d.answer) cls+=' primary'; } return `<button class="${cls}" data-dans="${esc(s.name)}" ${D.ans?'disabled':''}>${esc(s.name)}</button>`; }).join('')}</div>
    ${D.ans?`<div class="feedback ${D.ans===d.answer?'':'bad'}"><strong class="v">${D.ans===d.answer?'Correct':'Not quite'}</strong> <span class="muted">It's ${esc(d.answer)}.</span><p>${esc(d.why)}</p></div><div class="qnav"><span></span><button class="btn primary" id="drill-next">Next</button></div>`:''}</div>`;
}
function drillAnswer(name){
  const D=MEM.drill; if(!D || D.ans) return;
  const p=CP.find(x=>x.id===MEM.pair); const d=p.drills[D.order[D.i]];
  D.ans=name; if(name===d.answer){ D.right++; addXP(5); }
  save(); renderMemory();
}
function visualHTML(v){
  let body='';
  if(v.kind==='table') body = `<div class="tbl"><table><thead><tr>${(v.columns||[]).map(c=>`<th>${esc(c)}</th>`).join('')}</tr></thead><tbody>${(v.rows||[]).map(r=>`<tr>${r.map(c=>`<td>${esc(c)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
  else body = `<ol class="vsteps ${v.kind==='timeline'?'timeline':''}">${(v.steps||[]).map((s,i)=>`<li><span class="dot">${i+1}</span><div><b>${esc(s.label)}</b><div class="small">${esc(s.detail)}</div></div></li>`).join('')}</ol>`;
  return `<div class="panel"><div class="row" style="justify-content:space-between"><h3>${esc(v.title)}</h3><span class="mono small muted">${esc(SEC[v.sec]?SEC[v.sec].name:'')}</span></div><div style="margin-top:10px">${body}</div>${(v.notes||[]).length?`<ul class="small muted" style="margin:10px 0 0;padding-left:18px">${v.notes.map(n=>`<li>${esc(n)}</li>`).join('')}</ul>`:''}<p style="margin:8px 0 0"><cite>${esc(v.source)}</cite></p></div>`;
}
function visualsHTML(){
  const list = VS.filter(v=>MEM.sec==='all'||v.sec===MEM.sec);
  return `${secChips(MEM.sec, VS)}<div class="stack">${list.map(visualHTML).join('')}</div>`;
}

/* ---------- question session engine (practice, review, boss, survival) ---------- */
let SES = null;
const SES_KEY = 'mipc-session-v2';
function makeItem(id){ const q=QBY[id]; return {id, order: q.noShuffle?[0,1,2,3]:shuffle([0,1,2,3]), picked:null, conf:null}; }
function startSession(o){
  const ids = (o.ids||[]).filter(id=>QBY[id]);
  SES = {kind:o.kind||'practice', label:o.label||'Practice', sec:o.sec||null, items:ids.map(makeItem), idx:0, stage:'answer', shown:false,
         right:0, wrong:0, combo:0, xp:0, lives:o.kind==='survival'?3:null, target:o.kind==='boss'?8:null,
         recall: o.recall!=null ? o.recall : P.settings.recall, askConf: o.askConf!=null ? o.askConf : P.settings.confidence, done:false, pool:o.pool||null};
  if(SES.kind==='practice'||SES.kind==='review') lsSet(SES_KEY, SES); else lsDel(SES_KEY);
}
function renderPractice(opts){
  if(opts && (opts.sec || opts.ids || opts.review)){
    if(opts.review) startReview();
    else if(opts.ids) startSession({kind:'practice', ids:opts.ids, label:opts.label||'Practice'});
    else startSession({kind:'practice', ids:pickForSec(opts.sec, opts.n||20, opts.mode||'smart'), label:SEC[opts.sec].name, sec:opts.sec});
  }
  if(SES && !SES.done && SES.items.length && (SES.kind==='practice'||SES.kind==='review')){ drawQ('#view-practice'); return; }
  if(SES && SES.done && (SES.kind==='practice'||SES.kind==='review')){ drawEnd('#view-practice'); return; }
  const el=$('#view-practice');
  const saved=(lsGet('mipc-pr-cfg')||{}).sec||'all';
  const due=dueIds().length;
  el.innerHTML = `
  <div class="stack">
    <div class="panel">
      <h2>Practice</h2>
      <p class="muted" style="margin:0 0 6px">Instant feedback, the reason and the source after every answer, plus a memory hook when one covers the question. ${QS.length} questions in the bank; ${due} due for review.</p>
      <p class="muted small" style="margin:0 0 14px">Written in PSI's published item format: four options, one best answer, "EXCEPT" items, policies named by title and Michigan law named by subject. The real exam's questions are confidential, so these are original questions, not copies.</p>
      <div class="row" style="margin-bottom:14px"><button class="btn primary" data-act="review">Start today's session</button></div>
      <div class="row" style="align-items:flex-end">
        <label class="field" for="pr-sec">Section
          <select id="pr-sec"><option value="all">All sections (weighted like the exam)</option>${SECTIONS.map(s=>`<option value="${s.key}" ${saved===s.key?'selected':''}>${esc(s.name)} (${QS.filter(q=>q.sec===s.key).length})</option>`).join('')}</select>
        </label>
        <label class="field" for="pr-n">Questions<select id="pr-n"><option>10</option><option selected>20</option><option>50</option><option value="999">All</option></select></label>
        <label class="field" for="pr-mode">Order<select id="pr-mode"><option value="smart">Due, missed and unseen first</option><option value="missed">Only questions I missed</option><option value="random">Fully random</option></select></label>
        <button class="btn primary" id="pr-go">Start</button>
      </div>
      <div class="row" style="margin-top:12px;gap:18px">
        <label class="toggle"><input type="checkbox" id="pr-conf" ${P.settings.confidence?'checked':''}> Rate how sure I am</label>
        <label class="toggle"><input type="checkbox" id="pr-recall" ${P.settings.recall?'checked':''}> Recall first (hide choices)</label>
      </div>
      <p class="kbd" style="margin:14px 0 0">Keyboard: 1–4 or A–D to answer · S / U / G for sure, unsure, guess · Space shows choices · Enter for next</p>
    </div>
  </div>`;
  $('#pr-conf').addEventListener('change', e=>{ P.settings.confidence=e.target.checked; save(); });
  $('#pr-recall').addEventListener('change', e=>{ P.settings.recall=e.target.checked; save(); });
  $('#pr-go').addEventListener('click', ()=>{
    const sec=$('#pr-sec').value; lsSet('mipc-pr-cfg',{sec});
    P.settings.confidence=$('#pr-conf').checked; P.settings.recall=$('#pr-recall').checked; save();
    const n=+$('#pr-n').value, mode=$('#pr-mode').value;
    const ids = sec==='all' ? weightedIds(n, mode) : shuffle(pickForSec(sec, n, mode));
    if(!ids.length){ toast('No questions match that choice yet.'); return; }
    startSession({kind:'practice', ids, label: sec==='all'?'Mixed sections':SEC[sec].name, sec: sec==='all'?null:sec});
    drawQ('#view-practice');
  });
}
function pickIds(pool, n, mode){
  if(mode==='missed') pool = pool.filter(q=>P.q[q.id] && !P.q[q.id].last);
  if(mode==='random') return shuffle(pool).slice(0,n).map(q=>q.id);
  const now=Date.now();
  const due = pool.filter(q=>P.q[q.id] && (P.q[q.id].due||0)<=now).sort((a,b)=>(P.q[b.id].cw||0)-(P.q[a.id].cw||0)||(P.q[a.id].box||0)-(P.q[b.id].box||0));
  const unseen = shuffle(pool.filter(q=>!P.q[q.id]));
  const rest = pool.filter(q=>P.q[q.id] && (P.q[q.id].due||0)>now).sort((a,b)=>(P.q[a.id].due||0)-(P.q[b.id].due||0));
  return due.concat(unseen, rest).slice(0,n).map(q=>q.id);
}
function pickForSec(sec, n, mode){ return pickIds(QS.filter(q=>q.sec===sec), n, mode); }
function weightedIds(n, mode){
  const out=[];
  SECTIONS.forEach(s=>{ out.push(...pickIds(QS.filter(q=>q.sec===s.key), Math.max(1, Math.round(n*s.items/150)), mode)); });
  return shuffle(out).slice(0, n);
}
function startReview(){
  const goal=P.settings.dailyGoal, done=today().n;
  const target=Math.max(10, goal-done);
  let ids = dueIds().slice(0, target);
  if(ids.length<target) ids = ids.concat(newWeighted(target-ids.length));
  if(ids.length<target){ const have=new Set(ids); ids = ids.concat(QS.filter(q=>!have.has(q.id)).sort((a,b)=>((P.q[a.id]||{}).due||0)-((P.q[b.id]||{}).due||0)).slice(0, target-ids.length).map(q=>q.id)); }
  startSession({kind:'review', ids: ids.slice(0,target), label:"Today's session"});
}
function choiceHTML(item, mode){
  const q = QBY[item.id], reveal = mode==='reveal', locked = mode==='locked';
  return `<ul class="choices">${item.order.map((ci,pos)=>{
    let cls='choice'; const pressed = item.picked===ci;
    if(reveal){ if(ci===q.answer) cls+=' is-right'; else if(pressed) cls+=' is-wrong'; }
    return `<li><button class="${cls}" data-ci="${ci}" aria-pressed="${pressed&&!reveal}" ${reveal||locked?'disabled':''}><span class="k">${LETTERS[pos]}</span><span>${esc(q.choices[ci])}</span></button></li>`;
  }).join('')}</ul>`;
}
function hookBox(id){
  const ms = MN_BY_Q[id]; if(!ms || !ms.length) return '';
  const m = ms[0];
  return `<div class="memo"><div class="eyebrow" style="color:var(--accent)">Memory hook · ${esc(m.technique)}</div><div class="hk">${esc(m.hook)}</div><ul class="small" style="margin:6px 0 0;padding-left:18px">${(m.unpack||[]).map(u=>`<li>${esc(u)}</li>`).join('')}</ul>${m.watch_out?`<div class="watch" style="margin-top:6px"><b>Watch out:</b> ${esc(m.watch_out)}</div>`:''}</div>`;
}
function explainHTML(item){
  const q = QBY[item.id], ok = item.picked===q.answer, pos = item.order.indexOf(q.answer);
  const tags = ['Misread the question','Did not know it','Mixed up two ideas','Changed my answer'];
  return `<div class="feedback ${ok?'':'bad'}" role="status">
    <strong class="v">${ok?'Correct':'Incorrect'}</strong> <span class="muted">Answer: ${LETTERS[pos]}. ${esc(q.choices[q.answer])}</span>
    ${!ok && item.conf==='sure' ? `<p class="small" style="color:var(--bad);margin:6px 0 0">You were sure about this one. Confident mistakes are worth extra attention: it will come back first in your reviews.</p>`:''}
    <p>${esc(q.explain)}</p>
    ${q.source?`<p><cite>Source: ${esc(q.source)}</cite></p>`:''}
    ${!ok?`<div class="row small" style="gap:6px;margin-top:6px"><span class="muted">Why did I miss it?</span>${tags.map(t=>`<button class="chip" data-tag="${esc(t)}" aria-pressed="${P.journal[item.id]===t}">${esc(t)}</button>`).join('')}</div>`:''}
  </div>${hookBox(item.id)}`;
}
function sesHUD(){
  const S=SES, n=S.items.length;
  if(S.kind==='survival') return `<div class="hud"><span class="pill">Survival</span><span class="big">${S.right}</span><div class="lives" aria-label="${S.lives} lives left">${[0,1,2].map(i=>`<i class="${i<S.lives?'':'lost'}"></i>`).join('')}</div></div>`;
  if(S.kind==='boss'){ const hpLeft = Math.max(0, S.target - S.right); return `<div class="hud"><span class="pill">Boss: ${esc(SEC[S.sec].name)}</span><div class="row" style="flex:1;min-width:200px;gap:8px"><span class="mono small">HP</span><div class="hp"><span style="width:${100*hpLeft/S.target}%"></span></div></div><span class="mono small muted">Q ${Math.min(S.idx+1,n)} of ${n} · ${S.right} hit${S.right===1?'':'s'} · need ${S.target}</span></div>`; }
  return `<div class="qhead"><span class="pill">${esc(S.label)}</span><span class="mono small muted">Question ${S.idx+1} of ${n} · ${S.right} right${S.combo>=3?` · <b style="color:var(--good)">${S.combo} in a row</b>`:''}</span></div><div class="progress"><span style="width:${pct(S.idx+(S.stage==='feedback'?1:0),n)}%"></span></div>`;
}
function drawQ(sel){
  const el=$(sel); const S=SES; const it=S.items[S.idx], q=QBY[it.id];
  const hideChoices = S.recall && !S.shown && S.stage==='answer';
  let choices;
  if(hideChoices) choices = `<div class="reveal-box">Think of your answer before you look. Pulling it from memory is itself practice. <div style="margin-top:10px"><button class="btn primary" id="q-show">Show choices</button></div></div>`;
  else choices = choiceHTML(it, S.stage==='feedback'?'reveal':'pick');
  el.innerHTML = `
  <div class="qwrap">
    ${sesHUD()}
    <div class="eyebrow" style="color:var(--muted);margin-bottom:6px">${esc(SEC[q.sec].name)}${q.sub?' · '+esc(q.sub):''}</div>
    <p class="stem">${esc(q.q)}</p>
    ${choices}
    ${S.stage==='confidence'?`<div class="conf" role="group" aria-label="How sure are you?"><span class="q">How sure are you?</span><button class="btn" data-conf="sure">Sure (S)</button><button class="btn" data-conf="unsure">Unsure (U)</button><button class="btn" data-conf="guess">Guessed (G)</button></div>`:''}
    ${S.stage==='feedback'? explainHTML(it):''}
    <div class="qnav">
      <button class="btn ghost" id="q-quit">${S.kind==='boss'||S.kind==='survival'?'Leave game':'End session'}</button>
      ${S.stage==='feedback'? `<button class="btn primary" id="q-next">${nextLabel()}</button>`:''}
    </div>
  </div>`;
  const sh=$('#q-show'); if(sh) sh.addEventListener('click', ()=>{ S.shown=true; drawQ(sel); });
  el.querySelectorAll('.choice:not([disabled])').forEach(b=>b.addEventListener('click',()=>pickChoice(+b.dataset.ci, sel)));
  el.querySelectorAll('[data-conf]').forEach(b=>b.addEventListener('click',()=>finalize(b.dataset.conf, sel)));
  el.querySelectorAll('[data-tag]').forEach(b=>b.addEventListener('click',()=>{ P.journal[it.id]=b.dataset.tag; save(); el.querySelectorAll('[data-tag]').forEach(x=>x.setAttribute('aria-pressed', String(x===b))); }));
  $('#q-quit').addEventListener('click', ()=>{ S.done=true; persistSes(); drawEnd(sel); });
  const nx=$('#q-next'); if(nx){ nx.addEventListener('click', ()=>nextQ(sel)); nx.focus({preventScroll:true}); }
}
function nextLabel(){ const S=SES; if(S.kind==='survival') return S.lives>0?'Next question':'See results'; return S.idx+1<S.items.length?'Next question':'See results'; }
function persistSes(){ if(SES && (SES.kind==='practice'||SES.kind==='review')) lsSet(SES_KEY, SES); }
function pickChoice(ci, sel){
  const S=SES, it=S.items[S.idx]; if(S.stage!=='answer' && S.stage!=='confidence') return;
  it.picked=ci;
  if(S.askConf){ S.stage='confidence'; persistSes(); drawQ(sel); }
  else finalize(null, sel);
}
function finalize(conf, sel){
  const S=SES, it=S.items[S.idx], q=QBY[it.id]; if(S.stage==='feedback' || it.picked===null) return;
  it.conf=conf; it.fin=true; const ok = it.picked===q.answer;
  srsAnswer(it.id, ok, conf);
  if(ok){ S.right++; S.combo++; if(S.combo>P.bestCombo) P.bestCombo=S.combo; const x=10+(S.combo>=5?5:0); S.xp+=x; addXP(x); }
  else { S.wrong++; S.combo=0; S.xp+=2; addXP(2); if(S.kind==='survival') S.lives--; }
  S.stage='feedback'; checkBadges(); save(); persistSes(); drawQ(sel);
  const qw=$(sel+' .qwrap'); if(qw) qw.classList.add(ok?'flash-good':'flash-bad');
}
function nextQ(sel){
  const S=SES;
  if(S.kind==='survival'){
    if(S.lives<=0){ S.done=true; return drawEnd(sel); }
    if(S.idx+1>=S.items.length){ const more = survivalMore(); S.items.push(...more.map(makeItem)); }
  } else if(S.kind==='boss' && S.idx+1>=S.items.length){ S.done=true; return drawEnd(sel); }
  if(S.idx+1<S.items.length){ S.idx++; S.stage='answer'; S.shown=false; persistSes(); drawQ(sel); window.scrollTo({top:0}); }
  else { S.done=true; persistSes(); drawEnd(sel); }
}
function drawEnd(sel){
  const el=$(sel), S=SES;
  const answered = S.items.filter(i=>i.fin);
  const wrong = answered.filter(i=>i.picked!==QBY[i.id].answer);
  let head = '';
  if(S.kind==='boss'){
    const won = S.right>=S.target;
    const rec = P.games.boss[S.sec] || {best:0, won:false};
    rec.best = Math.max(rec.best, S.right); if(won && !rec.won){ rec.won=true; addXP(50); toast(`<b>Boss defeated:</b> ${esc(SEC[S.sec].name)}`); confetti(); }
    P.games.boss[S.sec]=rec; checkBadges(); save();
    head = `<div class="eyebrow" style="color:var(--muted)">Boss battle · ${esc(SEC[S.sec].name)}</div><div class="row" style="gap:14px;align-items:baseline;margin-top:6px"><span class="score-big">${S.right}/${S.items.length}</span>${won?'<span class="pill good">Defeated</span>':'<span class="pill bad">The boss survived</span>'}</div><p class="muted" style="margin:6px 0 0">${won?'You hit '+S.target+'+ out of 10.':'You need '+S.target+' of 10. Study the misses below and try again.'}</p>`;
  } else if(S.kind==='survival'){
    const best = Math.max(P.games.survBest||0, S.right); const isBest = S.right>(P.games.survBest||0); P.games.survBest=best; checkBadges(); save();
    head = `<div class="eyebrow" style="color:var(--muted)">Survival</div><div class="row" style="gap:14px;align-items:baseline;margin-top:6px"><span class="score-big">${S.right}</span>${isBest&&S.right>0?'<span class="pill good">New best</span>':`<span class="pill">Best ${best}</span>`}</div><p class="muted" style="margin:6px 0 0">Correct answers before losing 3 lives. +${S.xp} XP.</p>`;
  } else {
    head = `<div class="eyebrow" style="color:var(--muted)">${esc(S.label)}</div><div class="row" style="gap:14px;align-items:baseline;margin-top:6px"><span class="score-big">${answered.length?pct(S.right,answered.length)+'%':'—'}</span><span class="muted">${S.right} of ${answered.length} answered correctly · +${S.xp} XP</span></div>`;
  }
  el.innerHTML = `
  <div class="stack qwrap">
    <div class="panel">${head}
      <div class="row" style="margin-top:14px">
        ${S.kind==='boss'?`<button class="btn primary" data-act="boss" data-sec="${S.sec}">Fight again</button><button class="btn" data-act="games">All games</button>`:S.kind==='survival'?`<button class="btn primary" data-act="survival">Play again</button><button class="btn" data-act="games">All games</button>`:`<button class="btn primary" id="end-new">New session</button>`}
        ${wrong.length?`<button class="btn" id="end-redo">Retry the ${wrong.length} I missed</button>`:''}
      </div>
    </div>
    ${wrong.length? `<div class="panel"><h3>Review what you missed</h3>${wrong.map(it=>{const q=QBY[it.id];return `<div style="border-top:1px solid var(--line);padding-top:12px;margin-top:12px"><p style="margin:0 0 6px;font-weight:600">${esc(q.q)}</p><p style="margin:0" class="small">Your answer: <span style="color:var(--bad)">${esc(q.choices[it.picked])}</span><br>Correct: <span style="color:var(--good)">${esc(q.choices[q.answer])}</span></p><p class="small" style="margin:6px 0 0">${esc(q.explain)}</p>${q.source?`<p style="margin:4px 0 0"><cite>${esc(q.source)}</cite></p>`:''}${hookBox(it.id)}</div>`;}).join('')}</div>`:''}
  </div>`;
  const nw=$('#end-new'); if(nw) nw.addEventListener('click', ()=>{ SES=null; lsDel(SES_KEY); renderPractice(); });
  const rd=$('#end-redo'); if(rd) rd.addEventListener('click', ()=>{ startSession({kind:'practice', ids:wrong.map(i=>i.id), label:'Retry missed'}); go('practice'); });
}

/* ---------- Games ---------- */
let GAME = null; // lightning / match state
function renderGames(opts){
  if(opts && opts.game==='boss'){ startBoss(opts.sec); return; }
  if(opts && opts.game==='survival'){ startSurvival(); return; }
  if(opts && opts.game==='lightning'){ startLightning(); return; }
  if(SES && !SES.done && (SES.kind==='boss'||SES.kind==='survival')){ drawQ('#view-games'); return; }
  if(SES && SES.done && (SES.kind==='boss'||SES.kind==='survival')){ drawEnd('#view-games'); SES=null; return; }
  const el=$('#view-games');
  const bosses = SECTIONS.map(s=>{ const r=P.games.boss[s.key]; return `<button class="btn ${r&&r.won?'':'ghost'}" data-act="boss" data-sec="${s.key}" style="justify-content:space-between;display:flex;gap:8px;width:100%"><span>${esc(s.name)}</span><span class="mono small">${r?(r.won?'Defeated':'Best '+r.best+'/10'):'—'}</span></button>`; }).join('');
  el.innerHTML = `
  <div class="stack">
    <div class="panel lede" style="max-width:none"><h2>Games</h2><p class="muted" style="margin:0">Lightning round, Survival and Boss battles use the practice-question bank (original questions, not actual exam questions) and count toward your reviews. Match drills term pairs. Every game earns XP and badges, and each one is short and a little competitive with yourself.</p></div>
    <div class="gamegrid">
      <div class="game"><h3>Lightning round</h3><p class="small muted" style="margin:0">60 seconds. Answer as many as you can. Streaks multiply your score.</p><span class="best">Best: ${P.games.lightBest||0}</span><button class="btn primary" data-act="lightning">Play</button></div>
      <div class="game"><h3>Survival</h3><p class="small muted" style="margin:0">No clock. Three lives. How far can you go?</p><span class="best">Best: ${P.games.survBest||0}</span><button class="btn primary" data-act="survival">Play</button></div>
      <div class="game"><h3>Match</h3><p class="small muted" style="margin:0">Pair each term with its meaning. Beat your best time.</p><span class="best">Sets cleared: ${Object.keys(P.games.match).length} of ${MS.length}</span><button class="btn primary" data-act="match-menu" ${MS.length?'':'disabled'}>Play</button></div>
    </div>
    <div class="panel"><h3>Boss battles</h3><p class="small muted" style="margin:4px 0 12px">10 questions from one section, weighted to the ones you miss. Get 8 right to defeat the boss.</p><div class="stack" style="gap:6px">${bosses}</div></div>
  </div>`;
}
function startBoss(sec){
  const pool=QS.filter(q=>q.sec===sec);
  const weak = shuffle(pool.filter(q=>P.q[q.id] && !P.q[q.id].last));
  const unseen = shuffle(pool.filter(q=>!P.q[q.id]));
  const rest = shuffle(pool.filter(q=>P.q[q.id] && P.q[q.id].last));
  const ids = weak.slice(0,5).concat(unseen, rest).slice(0,10).map(q=>q.id);
  startSession({kind:'boss', ids, sec, label:'Boss', askConf:false, recall:false});
  drawQ('#view-games');
}
function survivalMore(){
  const used=new Set(SES?SES.items.map(i=>i.id):[]);
  return shuffle(QS.filter(q=>!used.has(q.id))).slice(0,20).map(q=>q.id);
}
function startSurvival(){
  SES=null; const ids=shuffle(QS).slice(0,20).map(q=>q.id);
  startSession({kind:'survival', ids, label:'Survival', askConf:false, recall:false});
  drawQ('#view-games');
}
function startLightning(){
  clearTimers();
  GAME = {type:'lightning', live:true, ends:Date.now()+60000, score:0, combo:0, mult:1, item:null, misses:[], answered:0, lock:false};
  nextLightning();
  timers.push(setInterval(()=>{ const t=$('#lt-timer'); const left=GAME.ends-Date.now(); if(t) t.textContent=Math.max(0,Math.ceil(left/1000))+'s'; if(left<=0) endGame(); }, 250));
}
function nextLightning(){
  const q = shuffle(QS)[0]; GAME.item = makeItem(q.id); GAME.lock=false; drawLightning();
}
function drawLightning(fb){
  const el=$('#view-games'); const it=GAME.item, q=QBY[it.id];
  el.innerHTML = `<div class="qwrap"><div class="hud"><span class="pill">Lightning round</span><span class="big" id="lt-timer">${Math.max(0,Math.ceil((GAME.ends-Date.now())/1000))}s</span><span class="big">${GAME.score}<span class="mono small muted"> pts${GAME.mult>1?' · x'+GAME.mult:''}</span></span></div>
    <p class="stem">${esc(q.q)}</p>${choiceHTML(it, fb?'reveal':'pick')}<div class="qnav"><button class="btn ghost" id="lt-quit">Stop</button></div></div>`;
  el.querySelectorAll('.choice:not([disabled])').forEach(b=>b.addEventListener('click',()=>answerLightning(+b.dataset.ci)));
  $('#lt-quit').addEventListener('click', ()=>endGame());
}
function answerLightning(ci){
  if(!GAME || GAME.lock || !GAME.live) return;
  GAME.lock=true; const it=GAME.item, q=QBY[it.id]; it.picked=ci; const ok=ci===q.answer;
  srsAnswer(it.id, ok, null); GAME.answered++;
  if(ok){ GAME.combo++; GAME.mult = GAME.combo>=8?3:GAME.combo>=4?2:1; GAME.score += GAME.mult; addXP(5); if(GAME.combo>P.bestCombo) P.bestCombo=GAME.combo; }
  else { GAME.combo=0; GAME.mult=1; GAME.misses.push({id:it.id, picked:ci}); }
  save();
  drawLightning(true);
  timers.push(setTimeout(()=>{ if(GAME && GAME.live) nextLightning(); }, ok?450:1300));
}
function endGame(silent){
  clearTimers();
  if(!GAME) return;
  const G=GAME; G.live=false;
  if(G.type==='lightning'){
    const isBest = G.score>(P.games.lightBest||0); P.games.lightBest=Math.max(P.games.lightBest||0, G.score); checkBadges(); save();
    if(silent){ GAME=null; return; }
    const el=$('#view-games');
    el.innerHTML = `<div class="stack qwrap"><div class="panel"><div class="eyebrow" style="color:var(--muted)">Lightning round</div><div class="row" style="gap:14px;align-items:baseline;margin-top:6px"><span class="score-big">${G.score}</span>${isBest&&G.score>0?'<span class="pill good">New best</span>':`<span class="pill">Best ${P.games.lightBest}</span>`}</div><p class="muted" style="margin:6px 0 0">${G.answered} answered, ${G.misses.length} missed.</p><div class="row" style="margin-top:14px"><button class="btn primary" data-act="lightning">Play again</button><button class="btn" data-act="games">All games</button></div></div>
    ${G.misses.length?`<div class="panel"><h3>Learn from the misses</h3>${G.misses.map(m=>{const q=QBY[m.id];return `<div style="border-top:1px solid var(--line);padding-top:12px;margin-top:12px"><p style="margin:0 0 6px;font-weight:600">${esc(q.q)}</p><p class="small" style="margin:0">Correct: <span style="color:var(--good)">${esc(q.choices[q.answer])}</span></p><p class="small" style="margin:6px 0 0">${esc(q.explain)}</p>${hookBox(m.id)}</div>`;}).join('')}</div>`:''}</div>`;
  }
  if(G.type==='match' && silent){ GAME=null; return; }
  GAME=null;
}
function renderMatchMenu(){
  const el=$('#view-games');
  el.innerHTML = `<div class="stack"><div class="row" style="justify-content:space-between"><h2>Match</h2><button class="btn ghost" data-act="games">All games</button></div>
  <div class="hook-grid">${MS.map(s=>{ const r=P.games.match[s.id]; return `<div class="hook"><span class="mono small muted">${esc(SEC[s.sec]?SEC[s.sec].name:'')}</span><div class="ht">${esc(s.title)}</div><span class="mono small muted">${s.pairs.length} pairs${r?` · best ${Math.round(r.t/1000)}s, ${r.m} miss${r.m===1?'':'es'}`:''}</span><div class="row" style="margin-top:auto"><button class="btn primary small" data-match="${s.id}">${r?'Play again':'Play'}</button></div></div>`; }).join('')}</div></div>`;
  el.querySelectorAll('[data-match]').forEach(b=>b.addEventListener('click',()=>startMatch(b.dataset.match)));
}
function startMatch(id){
  clearTimers();
  const set = MS.find(s=>s.id===id);
  GAME = {type:'match', live:true, set, left:shuffle(set.pairs.map((p,i)=>i)), right:shuffle(set.pairs.map((p,i)=>i)), done:new Set(), selL:null, selR:null, misses:0, start:Date.now()};
  drawMatch();
  timers.push(setInterval(()=>{ const t=$('#mt-timer'); if(t && GAME) t.textContent=Math.floor((Date.now()-GAME.start)/1000)+'s'; }, 500));
}
function drawMatch(missL, missR){
  const G=GAME, el=$('#view-games');
  el.innerHTML = `<div class="stack"><div class="hud"><span class="pill">${esc(G.set.title)}</span><span class="big" id="mt-timer">${Math.floor((Date.now()-G.start)/1000)}s</span><span class="mono small muted">${G.done.size}/${G.set.pairs.length} matched · ${G.misses} miss${G.misses===1?'':'es'}</span></div>
  <div class="match"><div class="col">${G.left.map(i=>`<button class="mitem ${G.done.has(i)?'done':''} ${missL===i?'miss':''}" data-l="${i}" aria-pressed="${G.selL===i}" ${G.done.has(i)?'disabled':''}>${esc(G.set.pairs[i].a)}</button>`).join('')}</div>
  <div class="col">${G.right.map(i=>`<button class="mitem ${G.done.has(i)?'done':''} ${missR===i?'miss':''}" data-r="${i}" aria-pressed="${G.selR===i}" ${G.done.has(i)?'disabled':''}>${esc(G.set.pairs[i].b)}</button>`).join('')}</div></div>
  <div class="row"><button class="btn ghost" data-act="match-menu">Back to sets</button></div><p style="margin:0"><cite>${esc(G.set.source)}</cite></p></div>`;
  el.querySelectorAll('[data-l]').forEach(b=>b.addEventListener('click',()=>{ G.selL=+b.dataset.l; tryMatch(); }));
  el.querySelectorAll('[data-r]').forEach(b=>b.addEventListener('click',()=>{ G.selR=+b.dataset.r; tryMatch(); }));
}
function tryMatch(){
  const G=GAME; if(G.selL===null || G.selR===null){ drawMatch(); return; }
  if(G.selL===G.selR){ G.done.add(G.selL); G.selL=G.selR=null; drawMatch(); if(G.done.size===G.set.pairs.length) finishMatch(); }
  else { const l=G.selL, r=G.selR; G.misses++; G.selL=G.selR=null; drawMatch(l, r); }
}
function finishMatch(){
  clearTimers();
  const G=GAME, t=Date.now()-G.start, prev=P.games.match[G.set.id];
  addXP(prev?5:15);
  if(!prev || t<prev.t || (t===prev.t && G.misses<prev.m)) P.games.match[G.set.id]={t, m:G.misses};
  checkBadges(); save(); G.live=false;
  const el=$('#view-games');
  el.insertAdjacentHTML('afterbegin', `<div class="panel" style="margin-bottom:16px"><div class="row" style="gap:14px;align-items:baseline"><span class="score-big">${Math.round(t/1000)}s</span><span class="muted">${G.misses} miss${G.misses===1?'':'es'}${!prev||t<prev.t?' · new best':''}</span></div><div class="row" style="margin-top:12px"><button class="btn primary" data-match-again="${G.set.id}">Play again</button><button class="btn" data-act="match-menu">Other sets</button></div></div>`);
  const a=el.querySelector('[data-match-again]'); if(a) a.addEventListener('click',()=>startMatch(a.dataset.matchAgain));
  GAME=null;
}

/* ---------- Math lab ---------- */
const r100 = n => Math.round(n/100)*100, r1000 = n => Math.round(n/1000)*1000;
function rint(a,b){ return a+Math.floor(Math.random()*(b-a+1)); }
function pick(a){ return a[Math.floor(Math.random()*a.length)]; }
const GEN = {
  coins: {name:'Commercial property coinsurance', src:'ISO Building and Personal Property Coverage Form (CP 00 10 10 12), Additional Conditions: Coinsurance', make(){
    const value=r1000(rint(200,900)*1000), pctc=pick([80,90,100]), required=value*pctc/100;
    const under = Math.random()<0.75; const limit = under ? r1000(required*rint(50,95)/100) : r1000(required*rint(100,110)/100);
    const loss=r100(rint(Math.round(value*0.05/100),Math.round(value*0.4/100))*100), ded=pick([500,1000,2500]);
    const ratio=Math.min(1, limit/required);
    let pay = ratio<1 ? loss*limit/required - ded : loss - ded; pay=Math.max(0, Math.min(pay, limit));
    const steps = ratio<1 ? [`Required insurance = ${money(value)} × ${pctc}% = ${money(required)}`, `Carried ÷ required = ${money(limit)} ÷ ${money(required)} = ${(limit/required).toFixed(4)}`, `Loss × (carried ÷ required) = ${money(loss)} × ${money(limit)} ÷ ${money(required)} = ${money(loss*limit/required)}`, `Subtract the deductible: ${money(loss*limit/required)} − ${money(ded)} = ${money(loss*limit/required-ded)}`, `Pay that amount or the limit, whichever is less: ${money(pay)}`]
      : [`Required insurance = ${money(value)} × ${pctc}% = ${money(required)}`, `The insured carries ${money(limit)}, which meets the requirement, so no penalty applies`, `Loss − deductible = ${money(loss)} − ${money(ded)} = ${money(loss-ded)}`, `Pay that amount or the limit, whichever is less: ${money(pay)}`];
    return {text:`A building worth ${money(value)} at the time of loss is insured for ${money(limit)} under a commercial property policy with ${pctc===80?'an':'a'} ${pctc}% coinsurance clause and a ${money(ded)} deductible. A covered loss of ${money(loss)} occurs. How much does the insurer pay?`, answer:Math.round(pay), steps};
  }},
  horc: {name:'Homeowners replacement cost (80% rule)', src:'ISO Homeowners 3 – Special Form (HO 00 03 05 11), Section I Conditions, Loss Settlement (Coverage A and B)', make(){
    const rc=r1000(rint(200,600)*1000), under=Math.random()<0.6;
    const limit = under ? r1000(rc*rint(50,78)/100) : r1000(rc*rint(80,100)/100);
    const loss=r100(rint(Math.round(rc*0.03/100),Math.round(rc*0.2/100))*100), dep=pick([20,25,30,40]), acv=Math.round(loss*(100-dep)/100);
    let pay, steps;
    const need=rc*0.8;
    if(limit>=need){ pay=Math.min(loss, limit); steps=[`80% of replacement cost = ${money(rc)} × 80% = ${money(need)}`, `Coverage A of ${money(limit)} is at least ${money(need)}, so the loss is paid at replacement cost`, `Pay ${money(pay)} (not more than the limit)`]; }
    else { const prop = loss*limit/need; pay=Math.min(Math.max(acv, prop), limit); steps=[`80% of replacement cost = ${money(rc)} × 80% = ${money(need)}`, `Coverage A of ${money(limit)} is less than ${money(need)}, so pay the greater of ACV or the proportional amount`, `ACV of the damage = ${money(loss)} − ${dep}% depreciation = ${money(acv)}`, `Proportional amount = ${money(loss)} × ${money(limit)} ÷ ${money(need)} = ${money(prop)}`, `Pay the greater: ${money(pay)}`]; }
    return {text:`A home with a replacement cost of ${money(rc)} is insured under an HO-3 (2011 ISO form) with a Coverage A limit of ${money(limit)}. A covered loss to the dwelling costs ${money(loss)} to repair, and the insured completes the repairs. Depreciation on the damaged part is ${dep}%. Ignoring the deductible, how much does the insurer pay?`, answer:Math.round(pay), steps};
  }},
  prorata: {name:'Other insurance: pro rata by limits', src:'Pro rata (proportional) other-insurance method, as in ISO Homeowners 3 (HO 00 03 05 11), Section I Conditions, Other Insurance And Service Agreement', make(){
    const a=r1000(rint(50,300)*1000), b=r1000(rint(50,300)*1000), loss=r1000(rint(20, Math.round((a+b)/1000*0.9))*1000);
    const sa=Math.min(a, loss*a/(a+b));
    return {text:`Two property policies cover the same building: Policy A with a ${money(a)} limit and Policy B with a ${money(b)} limit. Both share losses pro rata (in proportion to their limits). A covered ${money(loss)} loss occurs. Ignoring deductibles, how much does Policy A pay?`, answer:Math.round(sa), steps:[`Total insurance = ${money(a)} + ${money(b)} = ${money(a+b)}`, `Policy A's share = ${money(a)} ÷ ${money(a+b)} = ${(a/(a+b)).toFixed(4)}`, `Policy A pays ${money(loss)} × ${(a/(a+b)).toFixed(4)} = ${money(sa)}`]};
  }},
  equal: {name:'Other insurance: contribution by equal shares', src:'ISO Commercial General Liability Coverage Form (CG 00 01 04 13), Section IV Condition 4.c, Method of Sharing', make(){
    const lims=[pick([100000,250000,500000]), pick([250000,500000,1000000])].sort((x,y)=>x-y), loss=r1000(rint(Math.round(lims[0]/1000)+50, Math.round((lims[0]+lims[1])/1000)-10)*1000);
    let rem=loss, paid=[0,0], active=[0,1], steps=[];
    const share = Math.min(lims[0], loss/2); paid=[share, share]; rem=loss-2*share; steps.push(`Each insurer pays equal amounts until one reaches its limit or the loss is paid: ${money(share)} each`);
    if(rem>0){ const add=Math.min(rem, lims[1]-share); paid[1]+=add; rem-=add; steps.push(`Policy 1 is exhausted at ${money(lims[0])}; Policy 2 pays the remaining ${money(add)}`); }
    steps.push(`Policy 2 pays ${money(paid[1])} in total`);
    return {text:`Two primary CGL policies (2013 ISO form) cover the same loss, and both permit contribution by equal shares. Policy 1 has a ${money(lims[0])} limit and Policy 2 a ${money(lims[1])} limit. The covered loss is ${money(loss)}. How much does Policy 2 pay?`, answer:Math.round(paid[1]), steps};
  }},
  pipwork: {name:'Michigan PIP work loss (monthly)', src:'MCL 500.3107(1)(b); DIFS Bulletin 2026-20-INS ($7,455 per 30 days, accidents Oct. 1, 2026 – Sept. 30, 2027)', make(){
    const gross=r100(rint(20,140)*100), cap=7455, net=gross*0.85, pay=Math.min(net, cap);
    return {text:`An injured person's gross income was ${money(gross)} per 30 days before a Michigan auto accident on ${pick(['November 3, 2026','January 15, 2027','March 9, 2027','June 20, 2027'])}. She cannot work and earns no income during the period, and she does not show that her tax advantage is lower than 15%. What is the most PIP pays for work loss for one 30-day period?`, answer:Math.round(pay), steps:[`Reduce gross income by 15% (PIP work loss is not taxable): ${money(gross)} × 85% = ${money(net)}`, `Monthly maximum for accidents Oct. 1, 2026 – Sept. 30, 2027: ${money(cap)}`, `Pay the lesser: ${money(pay)}`]};
  }},
  wcprem: {name:"Workers' compensation premium", src:'Michigan WC Placement Facility (CAOM) Basic Manual, Ed. 09/26, Rule Six A–B (rate per $100 of payroll), G and I (experience modification)', make(){
    const payroll=rint(40,450)*2000, rate=pick([0.85,1.40,2.25,3.10,4.75,6.20]), mod=pick([0.80,0.92,1.00,1.15,1.25]);
    const manual=Math.round(payroll/100*rate), modp=manual*Math.round(mod*100)/100;
    return {text:`An employer's annual payroll in one class is ${money(payroll)}. The rate is $${rate.toFixed(2)} per $100 of payroll and the experience modification factor is ${mod.toFixed(2)}. Ignoring premium discounts and other adjustments, what is the modified premium?`, answer:Math.round(modp), steps:[`Payroll in hundreds = ${money(payroll)} ÷ 100 = ${(payroll/100).toLocaleString('en-US')}`, `Manual premium = ${(payroll/100).toLocaleString('en-US')} × $${rate.toFixed(2)} = ${money(manual)}`, `Modified premium = ${money(manual)} × ${mod.toFixed(2)} = ${money(modp)}`]};
  }},
  acv: {name:'Actual cash value (straight-line)', src:'Actual cash value = replacement cost minus depreciation (IRMI "actual cash value", method 1)', make(){
    const rc=r100(rint(8,60)*100), life=pick([5,8,10,12,15,20]), age=rint(1,life-1), dep=rc*age/life, acv=rc-dep;
    return {text:`A covered item would cost ${money(rc)} to replace new. It has a useful life of ${life} years and was ${age} years old at the time of loss. Using straight-line depreciation, what is its actual cash value?`, answer:Math.round(acv), steps:[`Depreciation = ${money(rc)} × ${age}/${life} = ${money(dep)}`, `ACV = ${money(rc)} − ${money(dep)} = ${money(acv)}`]};
  }},
  split: {name:'Split liability limits', src:'Split limits: per-person and per-accident bodily injury limits (ISO Personal Auto Policy, Part A, Limit of Liability)', make(){
    const pp=pick([50000,100000,250000]), pa=pp*pick([2,3]), n=pick([2,3]);
    const inj=Array.from({length:n},()=>r1000(rint(Math.round(pp*0.2/1000), Math.round(pp*1.6/1000))*1000));
    const each=inj.map(x=>Math.min(x,pp)), sum=each.reduce((a,b)=>a+b,0), pay=Math.min(sum,pa);
    return {text:`A driver with bodily injury limits of ${money(pp)} per person / ${money(pa)} per accident causes an accident that injures ${n} people, with damages of ${inj.map(money).join(', ')}. How much does the policy pay in total for bodily injury?`, answer:Math.round(pay), steps:[`Cap each person at ${money(pp)}: ${each.map(money).join(' + ')} = ${money(sum)}`, `Cap the total at the per-accident limit of ${money(pa)}: pay ${money(pay)}`]};
  }},
  lossratio: {name:'Loss ratio', src:'Loss ratio = incurred losses ÷ earned premium (IRMI "loss ratio")', make(){
    const ep=r1000(rint(200,2000)*1000), lr=rint(35,95), losses=Math.round(ep*lr/100);
    return {text:`An insurer earned ${money(ep)} in premium on a line of business and incurred ${money(losses)} in losses. What is its loss ratio, as a whole percent?`, answer:Math.round(losses/ep*100), steps:[`Loss ratio = incurred losses ÷ earned premium = ${money(losses)} ÷ ${money(ep)} = ${(losses/ep*100).toFixed(1)}%`], unit:'%'};
  }}
};
let MLAB = {type:'coins', prob:null, ans:null};
function renderMath(){
  const el=$('#view-math');
  if(!MLAB.prob) MLAB.prob = GEN[MLAB.type].make();
  const p=MLAB.prob, solved = MLAB.ans!==null, ok = solved && Math.abs(MLAB.ans - p.answer) <= (p.unit ? 0.5 : Math.max(1, Math.abs(p.answer)*0.001));
  el.innerHTML = `
  <div class="stack">
    <div class="panel lede" style="max-width:none"><h2>Math lab</h2><p class="muted" style="margin:0">Several outline topics involve arithmetic: coinsurance, loss valuation, other-insurance sharing and workers' comp premium. Each problem is generated fresh, so you practice the method, not the answer. Work it on paper, then check the steps.</p></div>
    <div class="subtabs" role="group" aria-label="Problem type">${Object.keys(GEN).map(k=>`<button class="chip" data-mt="${k}" aria-pressed="${MLAB.type===k}">${esc(GEN[k].name)}</button>`).join('')}</div>
    <div class="panel mathbox">
      <p class="stem" style="margin:0">${esc(p.text)}</p>
      <div class="row"><label class="field" for="m-ans">Your answer${p.unit?' (%)':' ($)'}<input type="number" id="m-ans" inputmode="decimal" step="any" ${solved?'disabled':''} value="${solved?esc(MLAB.ans):''}"></label><button class="btn primary" id="m-check" ${solved?'disabled':''} style="align-self:flex-end">Check</button><button class="btn" id="m-new" style="align-self:flex-end">New problem</button></div>
      ${solved?`<div class="feedback ${ok?'':'bad'}"><strong class="v">${ok?'Correct':'Not quite'}</strong> <span class="muted">Answer: ${p.unit?p.answer+'%':money(p.answer)}</span></div><div class="worked"><b>Worked solution</b><ol>${p.steps.map(s=>`<li>${esc(s)}</li>`).join('')}</ol><cite>${esc(GEN[MLAB.type].src)}</cite></div>`:`<p class="small muted" style="margin:0">Round to the nearest dollar${p.unit?' (or whole percent)':''}.</p>`}
    </div>
  </div>`;
  el.querySelectorAll('[data-mt]').forEach(b=>b.addEventListener('click',()=>{ MLAB={type:b.dataset.mt, prob:null, ans:null}; renderMath(); }));
  const chk=()=>{ const v=parseFloat($('#m-ans').value); if(isNaN(v)) return; MLAB.ans=v; const good=Math.abs(v-p.answer)<=(p.unit ? 0.5 : Math.max(1,Math.abs(p.answer)*0.001)); if(good){ P.games.math=(P.games.math||0)+1; addXP(8); checkBadges(); save(); } renderMath(); };
  $('#m-check').addEventListener('click', chk);
  const inp=$('#m-ans'); if(inp && !solved){ inp.addEventListener('keydown', e=>{ if(e.key==='Enter'){ e.preventDefault(); chk(); } }); }
  $('#m-new').addEventListener('click', ()=>{ MLAB.prob=null; MLAB.ans=null; renderMath(); const i=$('#m-ans'); if(i) i.focus(); });
}

/* ---------- Mock exam ---------- */
let EX = null; const EX_KEY='mipc-exam-v1'; let tick=null;
function buildExam(){
  const ids=[], short=[];
  SECTIONS.forEach(s=>{ const pick=pickIds(QS.filter(q=>q.sec===s.key), s.items, 'smart'); if(pick.length<s.items) short.push(s.name); ids.push(...pick); });
  return {items: shuffle(ids).map(makeItem), idx:0, start:Date.now(), ends:Date.now()+150*60*1000, submitted:false, confirm:false, short};
}
function renderExam(){
  clearInterval(tick);
  const el=$('#view-exam');
  if(EX && !EX.submitted){ drawExamQ(); return; }
  if(EX && EX.submitted){ drawExamResult(); return; }
  const hist=P.exams.slice(-8).reverse();
  el.innerHTML = `<div class="stack"><div class="panel lede"><h2>Full mock exam</h2><p style="margin:0 0 8px">150 questions in 2 hours 30 minutes, drawn section by section in the same proportions as the real PSI exam. No feedback until you submit, just like test day. You can flag questions and jump around.</p><p class="muted small" style="margin:0 0 14px">The timer keeps running if you leave this tab. Your exam resumes if the page reloads.</p><button class="btn primary" id="ex-go">Start the 150-question exam</button></div>
  ${hist.length?`<div class="panel"><h3>Past mock exams</h3><div class="tbl"><table><thead><tr><th>Date</th><th class="num">Score</th><th class="num">Correct</th><th>Result</th><th class="num">Time used</th></tr></thead><tbody>${hist.map(e=>`<tr><td>${new Date(e.t).toLocaleDateString()}</td><td class="num">${pct(e.score,e.total)}%</td><td class="num">${e.score}/${e.total}</td><td>${e.score/e.total>=PASS?'<span class="pill good">Pass</span>':'<span class="pill bad">Fail</span>'}</td><td class="num">${fmtTime(e.used||0)}</td></tr>`).join('')}</tbody></table></div></div>`:''}</div>`;
  $('#ex-go').addEventListener('click', ()=>{ EX=buildExam(); lsSet(EX_KEY,EX); drawExamQ(); });
}
function examAnswered(){ return EX.items.filter(i=>i.picked!==null).length; }
function drawExamQ(){
  const el=$('#view-exam'); const it=EX.items[EX.idx], q=QBY[it.id]; const n=EX.items.length, ans=examAnswered();
  el.innerHTML = `<div class="exam"><div class="qwrap"><div class="qhead"><span class="pill">Mock exam</span><span class="mono small muted">Question ${EX.idx+1} of ${n}</span></div><div class="progress"><span style="width:${pct(ans,n)}%"></span></div><p class="stem">${esc(q.q)}</p>${choiceHTML(it,'pick')}
    <div class="qnav"><div class="row"><button class="btn" id="ex-prev" ${EX.idx===0?'disabled':''}>Previous</button><button class="btn ghost" id="ex-flag" aria-pressed="${!!it.flagged}">${it.flagged?'Unflag':'Flag for review'}</button></div><button class="btn primary" id="ex-next">${EX.idx+1<n?'Next':'Review & submit'}</button></div></div>
    <aside class="side panel"><div class="row" style="justify-content:space-between"><span class="eyebrow" style="color:var(--muted)">Time left</span><span class="timer" id="ex-timer">${fmtTime(EX.ends-Date.now())}</span></div><p class="small muted" style="margin:6px 0 10px">${ans} of ${n} answered · ${EX.items.filter(i=>i.flagged).length} flagged</p>
    <div class="grid" id="ex-grid">${EX.items.map((x,i)=>`<button data-i="${i}" class="${x.picked!==null?'ans':''} ${x.flagged?'flag':''} ${i===EX.idx?'cur':''}" aria-label="Question ${i+1}${x.picked!==null?', answered':''}${x.flagged?', flagged':''}">${i+1}</button>`).join('')}</div>
    <button class="btn" id="ex-submit" style="width:100%;margin-top:14px">Submit exam</button><div id="ex-confirm"></div>${EX.short&&EX.short.length?`<p class="small muted" style="margin:10px 0 0">Bank has fewer questions than the exam uses for: ${esc(EX.short.join(', '))}.</p>`:''}</aside></div>`;
  el.querySelectorAll('.choice').forEach(b=>b.addEventListener('click',()=>{ it.picked=+b.dataset.ci; lsSet(EX_KEY,EX); drawExamQ(); }));
  $('#ex-prev').addEventListener('click',()=>examGo(EX.idx-1));
  $('#ex-next').addEventListener('click',()=>{ if(EX.idx+1<n) examGo(EX.idx+1); else askSubmit(); });
  $('#ex-flag').addEventListener('click',()=>{ it.flagged=!it.flagged; lsSet(EX_KEY,EX); drawExamQ(); });
  $('#ex-grid').addEventListener('click',e=>{ const b=e.target.closest('button'); if(b) examGo(+b.dataset.i); });
  $('#ex-submit').addEventListener('click', askSubmit);
  if(EX.confirm) askSubmit();
  clearInterval(tick);
  tick=setInterval(()=>{ const left=EX.ends-Date.now(), t=$('#ex-timer'); if(t){ t.textContent=fmtTime(left); t.classList.toggle('low', left<10*60*1000); } if(left<=0){ clearInterval(tick); submitExam(); } }, 1000);
}
function examGo(i){ if(i<0||i>=EX.items.length) return; EX.idx=i; EX.confirm=false; lsSet(EX_KEY,EX); drawExamQ(); }
function askSubmit(){
  EX.confirm=true; const un=EX.items.length-examAnswered(), fl=EX.items.filter(i=>i.flagged).length;
  $('#ex-confirm').innerHTML=`<div class="confirm small"><strong>Submit now?</strong><br>${un?un+' unanswered (scored as wrong). ':''}${fl?fl+' flagged. ':''}You can't change answers after submitting.<div class="row" style="margin-top:10px"><button class="btn primary" id="ex-yes">Submit</button><button class="btn" id="ex-no">Keep working</button></div></div>`;
  $('#ex-yes').addEventListener('click', submitExam);
  $('#ex-no').addEventListener('click', ()=>{ EX.confirm=false; $('#ex-confirm').innerHTML=''; });
}
function submitExam(){
  clearInterval(tick);
  if(!EX || EX.submitted) return;
  EX.submitted=true; EX.confirm=false;
  const used=Math.min(Date.now(),EX.ends)-EX.start, bySec={}; let score=0;
  EX.items.forEach(it=>{ const q=QBY[it.id], ok=it.picked===q.answer; bySec[q.sec]=bySec[q.sec]||[0,0]; bySec[q.sec][1]++; if(ok){bySec[q.sec][0]++; score++;} srsAnswer(it.id, ok, null); });
  EX.result={score, total:EX.items.length, bySec, used};
  P.exams.push({t:Date.now(), score, total:EX.items.length, bySec, used}); if(P.exams.length>30) P.exams=P.exams.slice(-30);
  addXP(score); if(score/EX.items.length>=PASS) confetti();
  checkBadges(); save(); lsSet(EX_KEY,EX); drawExamResult(); window.scrollTo({top:0});
}
let EX_FILTER='wrong';
function drawExamResult(){
  const el=$('#view-exam'), r=EX.result, passed=r.score/r.total>=PASS;
  const list=EX.items.map((it,i)=>({it,i,q:QBY[it.id]})).filter(o=>EX_FILTER==='all'||(EX_FILTER==='wrong'?o.it.picked!==o.q.answer:o.it.flagged));
  el.innerHTML = `<div class="stack"><div class="panel"><div class="result-hero"><div><div class="eyebrow" style="color:var(--muted)">Mock exam result</div><div class="row" style="gap:14px;align-items:baseline;margin-top:6px"><span class="score-big">${pct(r.score,r.total)}%</span>${passed?'<span class="pill good">Pass</span>':'<span class="pill bad">Fail</span>'}</div><p class="muted" style="margin:6px 0 0">${r.score} of ${r.total} correct · passing is 74% (111 of 150) · time used ${fmtTime(r.used)}</p></div><div class="row"><button class="btn primary" id="ex-again">New mock exam</button><button class="btn" id="ex-drill">Drill the questions I missed</button></div></div>
  <div class="tbl" style="margin-top:18px"><table><thead><tr><th>Section</th><th class="num">Correct</th><th style="min-width:120px">Score</th></tr></thead><tbody>${SECTIONS.map(s=>{const v=r.bySec[s.key]||[0,0], a=v[1]?v[0]/v[1]:null; return `<tr><td>${esc(s.name)}</td><td class="num">${v[0]}/${v[1]}</td><td><div class="row" style="gap:8px;flex-wrap:nowrap"><div class="meter ${meterClass(a)}" style="flex:1"><span style="width:${a===null?0:Math.round(a*100)}%"></span></div><span class="mono small" style="width:38px;text-align:right">${a===null?'—':Math.round(a*100)+'%'}</span></div></td></tr>`;}).join('')}</tbody></table></div></div>
  <div class="panel"><div class="row" style="justify-content:space-between"><h3>Review</h3><div class="row" role="group" aria-label="Filter review"><button class="chip" data-f="wrong" aria-pressed="${EX_FILTER==='wrong'}">Missed</button><button class="chip" data-f="flag" aria-pressed="${EX_FILTER==='flag'}">Flagged</button><button class="chip" data-f="all" aria-pressed="${EX_FILTER==='all'}">All</button></div></div>
  ${list.length?list.map(({it,i,q})=>`<div style="border-top:1px solid var(--line);padding-top:14px;margin-top:14px"><div class="eyebrow" style="color:var(--muted)">Q${i+1} · ${esc(SEC[q.sec].name)}</div><p style="margin:4px 0 10px;font-weight:600">${esc(q.q)}</p>${choiceHTML(it,'reveal')}${it.picked===null?'<p class="small" style="color:var(--bad)">Not answered.</p>':''}<p class="small" style="margin:10px 0 0">${esc(q.explain)}</p>${q.source?`<p style="margin:4px 0 0"><cite>${esc(q.source)}</cite></p>`:''}</div>`).join(''):'<div class="empty" style="margin-top:12px">Nothing in this filter.</div>'}</div></div>`;
  el.querySelectorAll('[data-f]').forEach(b=>b.addEventListener('click',()=>{ EX_FILTER=b.dataset.f; drawExamResult(); }));
  $('#ex-again').addEventListener('click', ()=>{ EX=null; lsDel(EX_KEY); renderExam(); });
  $('#ex-drill').addEventListener('click', ()=>{ const ids=EX.items.filter(it=>it.picked!==QBY[it.id].answer).map(it=>it.id); startSession({kind:'practice', ids, label:'Missed on mock exam'}); go('practice'); });
}

/* ---------- Flashcards (spaced) ---------- */
let FC=null;
function cardDue(c){ const s=P.cards[c.id]; return !s || (s.due||0)<=Date.now(); }
function renderCards(sec){
  const el=$('#view-cards');
  if(sec){ FC=null; lsSet('mipc-fc-cfg',{sec}); }
  const cur = sec || (lsGet('mipc-fc-cfg')||{}).sec || 'all';
  const pool = CARDS.filter(c=>cur==='all'||c.sec===cur);
  if(!FC || FC.sec!==cur){
    const due = pool.filter(c=>P.cards[c.id] && cardDue(c)).sort((a,b)=>(P.cards[a.id].box||0)-(P.cards[b.id].box||0));
    const fresh = shuffle(pool.filter(c=>!P.cards[c.id]));
    FC = {sec:cur, queue:due.concat(fresh).map(c=>c.id), flipped:false};
  }
  const mastered = pool.filter(c=>(P.cards[c.id]||{}).box>=3).length, dueN=pool.filter(c=>P.cards[c.id] && cardDue(c)).length;
  const card = FC.queue[0] ? CARDS.find(c=>c.id===FC.queue[0]) : null;
  el.innerHTML = `<div class="stack"><div class="row" style="justify-content:space-between;align-items:flex-end"><label class="field" for="fc-sec">Deck<select id="fc-sec"><option value="all">All decks (${CARDS.length})</option>${SECTIONS.map(s=>{const k=CARDS.filter(c=>c.sec===s.key).length; return k?`<option value="${s.key}" ${cur===s.key?'selected':''}>${esc(s.name)} (${k})</option>`:'';}).join('')}</select></label><span class="mono small muted">${dueN} due · ${mastered} of ${pool.length} mastered</span></div>
  ${card?`<div class="card-stage"><div class="fcard ${FC.flipped?'flipped':''}" id="fc" tabindex="0" role="button" aria-label="Flip card"><div class="fface"><span class="lab">${esc(SEC[card.sec]?SEC[card.sec].name:'')}</span><div class="t">${esc(card.front)}</div><span class="kbd">Say the answer out loud, then tap or press Space to flip</span></div><div class="fface back"><span class="lab">Answer</span><div class="b">${esc(card.back)}</div>${card.source?`<cite>${esc(card.source)}</cite>`:''}</div></div></div>
  <div class="row"><button class="btn" id="fc-again" ${FC.flipped?'':'disabled'}>Again</button><button class="btn primary" id="fc-good" ${FC.flipped?'':'disabled'}>Got it</button><span class="kbd">${FC.queue.length} in this round · cards you get right come back later and later</span></div>`
  :`<div class="empty">Nothing due in this deck right now. <button class="btn" id="fc-restart">Study ahead anyway</button></div>`}</div>`;
  $('#fc-sec').addEventListener('change', e=>renderCards(e.target.value));
  const c=$('#fc');
  if(c){
    const flip=()=>{ FC.flipped=!FC.flipped; c.classList.toggle('flipped',FC.flipped); $('#fc-again').disabled=!FC.flipped; $('#fc-good').disabled=!FC.flipped; };
    c.addEventListener('click', flip); c.addEventListener('keydown', e=>{ if(e.key===' '||e.key==='Enter'){ e.preventDefault(); flip(); } });
    $('#fc-again').addEventListener('click', ()=>gradeCard(card.id,false)); $('#fc-good').addEventListener('click', ()=>gradeCard(card.id,true));
    const ae=document.activeElement; if(!ae || ae===document.body || ae.classList.contains('tab')) c.focus({preventScroll:true});
  }
  const rs=$('#fc-restart'); if(rs) rs.addEventListener('click', ()=>{ FC={sec:cur, queue:shuffle(pool).map(x=>x.id), flipped:false}; renderCards(); });
}
function gradeCard(id, ok){
  const s=P.cards[id]||{box:0,due:0};
  if(ok){ s.box=Math.min(IV.length-1,(s.box||0)+1); s.due=startOfToday()+IV[s.box]*DAY; addXP(3); } else { s.box=0; s.due=Date.now(); }
  P.cards[id]=s; save(); checkBadges();
  FC.queue.shift(); if(!ok) FC.queue.splice(Math.min(3,FC.queue.length),0,id);
  FC.flipped=false; renderCards();
}

/* ---------- Key numbers ---------- */
function renderNumbers(){
  const el=$('#view-numbers'), groups={};
  (DATA.numbers||[]).forEach(n=>{ (groups[n.group]=groups[n.group]||[]).push(n); });
  el.innerHTML = `<div class="stack"><div class="panel"><h2>Key numbers</h2><p class="muted lede" style="margin:0">Dollar limits, percentages and deadlines that show up on the exam, each tied to the statute, form or agency page it came from. Tip: cover the middle column and quiz yourself.</p><label class="field" for="kn-q" style="margin-top:12px;max-width:340px">Filter<input type="search" id="kn-q" placeholder="e.g. days, PIP, vacancy"></label></div><div id="kn-body" class="stack"></div></div>`;
  const draw=q=>{ q=(q||'').toLowerCase(); $('#kn-body').innerHTML = Object.keys(groups).map(g=>{ const rows=groups[g].filter(n=>!q||(n.item+' '+n.value+' '+(n.source||'')).toLowerCase().includes(q)); if(!rows.length) return ''; return `<div class="panel"><h3 style="margin-bottom:8px">${esc(g)}</h3><div class="tbl"><table class="kn"><tbody>${rows.map(n=>`<tr><td>${esc(n.item)}</td><td class="v">${esc(n.value)}</td><td><cite>${esc(n.source||'')}</cite></td></tr>`).join('')}</tbody></table></div></div>`; }).join('') || '<div class="empty">No matches.</div>'; };
  draw(''); $('#kn-q').addEventListener('input', e=>draw(e.target.value));
}

/* ---------- global events ---------- */
document.addEventListener('click', e=>{
  const b=e.target.closest('[data-act]'); if(!b) return;
  const act=b.dataset.act;
  if(act==='review'){ startReview(); go('practice'); }
  if(act==='lightning'){ go('games',{game:'lightning'}); }
  if(act==='survival'){ SES=null; go('games',{game:'survival'}); }
  if(act==='boss'){ SES=null; go('games',{game:'boss', sec:b.dataset.sec}); }
  if(act==='games'){ SES=null; if(GAME&&GAME.live) endGame(true); go('games'); }
  if(act==='match-menu'){ if(GAME&&GAME.live) endGame(true); VIEW='games'; document.querySelectorAll('.view').forEach(el=>el.hidden=(el.id!=='view-games')); document.querySelectorAll('.tab').forEach(t=>t.setAttribute('aria-selected', String(t.dataset.view==='games'))); renderMatchMenu(); }
  if(act==='practice-sec'){ go('practice',{sec:b.dataset.sec, n:20, mode:'smart'}); }
  if(act==='cards-sec') go('cards',{sec:b.dataset.sec});
  if(act==='hooks-sec') go('memory',{tab:'hooks', sec:b.dataset.sec});
  if(act==='study-logistics') go('study',{sec:'logistics'});
  if(act==='set-date'){ const v=($('#exam-date')||{}).value; if(v){ P.settings.examDate=v; save(); renderHome(); toast('Exam date saved.'); } }
  if(act==='reset') $('#reset-box').innerHTML=`<div class="confirm small"><strong>Erase all progress?</strong> Answers, reviews, XP, badges, mock exams and flashcards will be cleared.<div class="row" style="margin-top:10px"><button class="btn primary" data-act="reset-yes">Erase</button><button class="btn" data-act="reset-no">Cancel</button></div></div>`;
  if(act==='reset-no') $('#reset-box').innerHTML='';
  if(act==='reset-yes'){ P=blank(); save(); SES=null; EX=null; lsDel(SES_KEY); lsDel(EX_KEY); renderHome(); }
});
document.addEventListener('keydown', e=>{
  if(e.target.matches('input,select,textarea')) return;
  const k=e.key.toLowerCase();
  const n=['1','2','3','4'].indexOf(k)>=0 ? ['1','2','3','4'].indexOf(k) : ['a','b','c','d'].indexOf(k);
  const sel = VIEW==='practice' ? '#view-practice' : VIEW==='games' ? '#view-games' : null;
  if(sel && SES && !SES.done && (VIEW==='practice' ? (SES.kind==='practice'||SES.kind==='review') : (SES.kind==='boss'||SES.kind==='survival')) && !(GAME&&GAME.live)){
    const it=SES.items[SES.idx];
    if(SES.stage==='answer' && SES.recall && !SES.shown){ if(k===' '||k==='enter'){ e.preventDefault(); SES.shown=true; drawQ(sel); } return; }
    if((SES.stage==='answer'||SES.stage==='confidence') && n>=0){ e.preventDefault(); pickChoice(it.order[n], sel); return; }
    if(SES.stage==='confidence'){ const m={s:'sure',u:'unsure',g:'guess',enter:'sure'}[k]; if(m){ e.preventDefault(); finalize(m, sel); } return; }
    if(SES.stage==='feedback' && k==='enter'){ e.preventDefault(); nextQ(sel); return; }
  }
  if(VIEW==='games' && GAME && GAME.live && GAME.type==='lightning' && n>=0 && !GAME.lock){ e.preventDefault(); answerLightning(GAME.item.order[n]); }
  if(VIEW==='exam' && EX && !EX.submitted){
    const it=EX.items[EX.idx];
    if(n>=0){ it.picked=it.order[n]; lsSet(EX_KEY,EX); drawExamQ(); e.preventDefault(); }
    else if(k==='enter'){ if(EX.idx+1<EX.items.length) examGo(EX.idx+1); e.preventDefault(); }
    else if(k==='arrowleft') examGo(EX.idx-1);
    else if(k==='arrowright') examGo(EX.idx+1);
  }
  if(VIEW==='cards' && (k===' '||k==='enter') && (e.target===document.body||e.target===document.documentElement)){ const c=$('#fc'); if(c){ e.preventDefault(); c.click(); } }
});

function renderFoot(){
  $('#foot').innerHTML = `<p><strong>Sources.</strong> ${esc(DATA.meta.sourcesNote)}</p><p>Content verified ${esc(DATA.meta.verified)}. ${QS.length} questions · ${CARDS.length} flashcards · ${MN.length} memory hooks · ${CP.length} confusion pairs. Rules change: check PSI's current Michigan candidate bulletin and content outline before your test date.</p><p>Not affiliated with PSI or the Michigan Department of Insurance and Financial Services. Practice questions are original and are not actual exam questions.</p>`;
}
function start(hot){
  if(hot && hot.EX) EX=hot.EX; else { const ex=lsGet(EX_KEY); if(ex && ex.items && ex.items.every(i=>QBY[i.id])) EX=ex; }
  if(hot && hot.SES) SES=hot.SES; else { const s=lsGet(SES_KEY); if(s && s.items && !s.done && s.items.every(i=>QBY[i.id])) SES=s; }
  renderFoot();
  go((hot && hot.VIEW && hot.VIEW!=='games') ? hot.VIEW : (EX && !EX.submitted ? 'exam' : 'home'));
  initSync();
}
window.__mipc = { gen: GEN, srsAnswer, levelOf, P: ()=>P, ses: ()=>SES, today }; // test hooks
if(window.claude && window.claude.hot){ try{ window.claude.hot.snapshot(()=>({EX, SES, VIEW})); }catch(e){} }
if(window.claude && window.claude.hot && window.claude.hot.ready) window.claude.hot.ready(start);
else start((window.claude && window.claude.hot && window.claude.hot.data) || {});
})();
