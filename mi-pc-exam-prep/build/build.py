#!/usr/bin/env python3
"""Assemble the study app: validate research JSON, convert study guides, embed data into the template."""
import json, re, sys, os, glob
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from md2html import convert

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.environ.get('RES') or os.path.join(HERE, '..', 'research')
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'mi-pc-exam-prep.html')

TOPICS = ['reg', 'gen', 'basics', 'mi', 'dwelling', 'ho', 'auto', 'cpp', 'bop', 'wc', 'other']
T2S = {'reg': 'reg', 'gen': 'gen', 'basics': 'basics', 'mi': 'basics', 'dwelling': 'dwelling', 'ho': 'ho',
       'auto': 'auto', 'cpp': 'cpp', 'bop': 'bop', 'wc': 'wc', 'other': 'other'}
# Study-guide order and labels follow the PSI outline order.
GUIDE = [
    ('logistics', 'Exam Day & Licensing Steps', 'Before you test', []),
    ('reg', 'Insurance Regulation', '10% · 15 items', ['reg']),
    ('gen', 'General Insurance', '10.5% · 16 items', ['gen']),
    ('basics', 'P&C Basics', '20% · 30 items (with MI laws)', ['basics']),
    ('mi', 'Michigan Laws & Required Provisions', 'part of P&C Basics', ['basics']),
    ('dwelling', 'Dwelling Policy', '2.5% · 4 items', ['dwelling']),
    ('ho', 'Homeowners Policy', '15% · 22 items', ['ho']),
    ('auto', 'Automobile Insurance', '15% · 22 items', ['auto']),
    ('cpp', 'Commercial Package Policy', '12% · 18 items', ['cpp']),
    ('bop', 'Businessowners Policy', '6% · 9 items', ['bop']),
    ('wc', "Workers' Compensation", '5% · 8 items', ['wc']),
    ('other', 'Other Coverages & Options', '4% · 6 items', ['other']),
]
SHUFFLE_BLOCK = re.compile(r'\b(all|none) of the above\b|\bboth [A-D] and [A-D]\b|\bneither [A-D] nor [A-D]\b|\b[A-D] (and|or) [A-D]\b|\b(choices?|answers?) [A-D]\b')
# A choice that starts with a number (optionally $), with an optional unit word, e.g. "$1,500", "30 days", "20%".
NUM_LEAD = re.compile(r'^\s*(\$)?(\d[\d,]*(?:\.\d+)?)\s*(%|(?:days?|years?|months?|weeks?|hours?|minutes?)\b)?', re.I)

errors, warns = [], []
questions, cards, numbers = [], [], []
blocks = {}
logistics_md = ''

for path in sorted(glob.glob(os.path.join(RES, '*_questions.json'))):
    data = json.load(open(path))
    for q in data:
        qid = q.get('id')
        if q.get('topic') not in TOPICS: errors.append(f'{qid}: bad topic {q.get("topic")}')
        ch = q.get('choices')
        if not isinstance(ch, list) or len(ch) != 4: errors.append(f'{qid}: needs 4 choices'); continue
        if len(set(c.strip().lower() for c in ch)) != 4: errors.append(f'{qid}: duplicate choices')
        if q.get('answer') not in (0, 1, 2, 3): errors.append(f'{qid}: bad answer index'); continue
        if not q.get('q') or not q.get('explain'): errors.append(f'{qid}: missing stem/explain')
        if not q.get('source'): warns.append(f'{qid}: no source')
        out = {k: q[k] for k in ('id', 'topic', 'sub', 'q', 'choices', 'answer', 'explain', 'source') if k in q}
        if any(SHUFFLE_BLOCK.search(c) for c in ch): out['noShuffle'] = True
        # Exam convention: numeric answer sets are listed in ascending order, not shuffled.
        nums = [NUM_LEAD.match(c) for c in ch]
        if all(nums) and len({(m.group(1) or '', (m.group(3) or '').lower().rstrip('s')) for m in nums}) == 1:
            order = sorted(range(4), key=lambda i: float(nums[i].group(2).replace(',', '')))
            out['choices'] = [ch[i] for i in order]
            out['answer'] = order.index(q['answer'])
            out['noShuffle'] = True
        questions.append(out)

for path in sorted(glob.glob(os.path.join(RES, '*_cards.json'))):
    area = os.path.basename(path).split('_')[0]
    for i, c in enumerate(json.load(open(path)), 1):
        t = c.get('topic')
        if t not in T2S: errors.append(f'card {area}#{i}: bad topic {t}'); continue
        if not c.get('front') or not c.get('back'): errors.append(f'card {area}#{i}: empty'); continue
        cards.append({'id': f'{area}-c{i:03d}', 'sec': T2S[t], 'front': c['front'], 'back': c['back'], 'source': c.get('source', '')})

for path in sorted(glob.glob(os.path.join(RES, '*_numbers.json'))):
    for n in json.load(open(path)):
        if not all(n.get(k) for k in ('group', 'item', 'value')): errors.append(f'number row incomplete: {n}'); continue
        numbers.append({k: n.get(k, '') for k in ('group', 'item', 'value', 'source')})

for path in sorted(glob.glob(os.path.join(RES, '*_facts.md'))):
    md = open(path).read()
    parts = re.split(r'^# (\w+):[ \t]*(.*)$', md, flags=re.M)
    if len(parts) < 4: errors.append(f'{os.path.basename(path)}: no "# key: Title" H1 blocks'); continue
    for i in range(1, len(parts), 3):
        key, body = parts[i], parts[i + 2]
        if key not in T2S and key != 'logistics': errors.append(f'{path}: unknown block {key}'); continue
        blocks[key] = blocks.get(key, '') + body

LEARN = os.environ.get('LEARN') or os.path.join(HERE, '..', 'learn')
SECS = {'reg','gen','basics','dwelling','ho','auto','cpp','bop','wc','other'}
qids = {q['id'] for q in questions}
mnemonics, pairs, visuals, matchsets = [], [], [], []
for path in sorted(glob.glob(os.path.join(LEARN, '*.final.json'))):
    kind = os.path.basename(path)[:2]
    for it in json.load(open(path)):
        iid = it.get('id', '?')
        if it.get('sec') not in SECS: errors.append(f'{iid}: bad sec {it.get("sec")}'); continue
        if kind == 'mn':
            if not all(it.get(k) for k in ('title','hook','technique','source')) or not it.get('unpack'): errors.append(f'{iid}: incomplete hook'); continue
            missing = [x for x in it.get('question_ids', []) if x not in qids]
            if missing: warns.append(f'{iid}: dropped unknown question ids {missing}')
            it['question_ids'] = [x for x in it.get('question_ids', []) if x in qids]
            mnemonics.append({k: it.get(k, '') for k in ('id','sec','title','technique','hook','unpack','watch_out','source','question_ids')})
        elif kind == 'cp':
            names = [sd.get('name') for sd in it.get('sides', [])]
            if len(names) < 2 or len(set(names)) != len(names): errors.append(f'{iid}: bad sides'); continue
            bad = [d for d in it.get('drills', []) if d.get('answer') not in names or not d.get('prompt')]
            if bad or not it.get('drills'): errors.append(f'{iid}: drill answers not among sides'); continue
            pairs.append({k: it.get(k, '') for k in ('id','sec','title','sides','tell','drills','source')})
        elif kind == 'vs':
            if it.get('kind') == 'table':
                cols = it.get('columns') or []
                if not cols or any(len(r) != len(cols) for r in it.get('rows', [])): errors.append(f'{iid}: table rows/columns mismatch'); continue
            elif it.get('kind') in ('steps','timeline'):
                if not it.get('steps'): errors.append(f'{iid}: no steps'); continue
            else: errors.append(f'{iid}: bad kind'); continue
            visuals.append({k: it.get(k, '' if k not in ('columns','rows','steps','notes') else []) for k in ('id','sec','title','kind','columns','rows','steps','notes','source')})
        elif kind == 'ms':
            prs = it.get('pairs', [])
            if not (3 <= len(prs) <= 10): errors.append(f'{iid}: pair count {len(prs)}'); continue
            if len({x['a'].strip().lower() for x in prs}) != len(prs) or len({x['b'].strip().lower() for x in prs}) != len(prs): errors.append(f'{iid}: duplicate terms'); continue
            matchsets.append({k: it.get(k, '') for k in ('id','sec','title','pairs','source')})
allids = [x['id'] for x in mnemonics + pairs + visuals + matchsets]
for k, v in Counter(allids).items():
    if v > 1: errors.append(f'duplicate learn id {k}')
howto_path = os.path.join(LEARN, 'howto.final.md')
howto_html = convert(open(howto_path).read()) if os.path.exists(howto_path) else ''

def guide_html(md):
    # Wrap the Flags section in a callout so unverified/changing items stand out.
    m = re.search(r'^##\s+Flags.*$', md, flags=re.M)
    if m:
        main, flags = md[:m.start()], md[m.end():]
        return convert(main) + '<div class="flags"><h4>Watch-outs: changing values &amp; source notes</h4>' + convert(flags) + '</div>'
    return convert(md)

GROUP_ORDER = ['Exam Logistics', 'Licensing & Regulation', 'Policy Provisions & Claims', 'Michigan Property Laws', 'Dwelling Policy',
               'Homeowners Policy', 'Michigan Auto / No-Fault', 'Personal Auto Policy', 'Commercial Auto', 'Commercial Lines',
               'Businessowners', "Workers' Compensation", 'Other Coverages / NFIP / Surplus Lines']
numbers.sort(key=lambda n: GROUP_ORDER.index(n['group']) if n['group'] in GROUP_ORDER else 99)
guide = []
if howto_html:
    guide.append({'id': 'howto', 'title': 'Start here: how to study', 'weight': 'Read first', 'secs': [], 'html': howto_html})
for key, title, weight, secs in GUIDE:
    if key in blocks:
        guide.append({'id': key, 'title': title, 'weight': weight, 'secs': secs, 'html': guide_html(blocks[key])})
    else:
        warns.append(f'guide block missing: {key}')

ids = Counter(q['id'] for q in questions)
for k, v in ids.items():
    if v > 1: errors.append(f'duplicate question id {k}')
stems = Counter(re.sub(r'\W+', ' ', q['q'].lower()).strip() for q in questions)
for k, v in stems.items():
    if v > 1: warns.append(f'duplicate stem: {k[:80]}')

per_sec = Counter(T2S[q['topic']] for q in questions)
need = {'reg': 15, 'gen': 16, 'basics': 30, 'dwelling': 4, 'ho': 22, 'auto': 22, 'cpp': 18, 'bop': 9, 'wc': 8, 'other': 6}
for s, n in need.items():
    if per_sec[s] < n: warns.append(f'section {s}: only {per_sec[s]} questions (mock exam needs {n})')
pos = Counter(q['answer'] for q in questions)


SHELL = """
<header class="jacket">
  <div class="wrap">
    <div>
      <div class="eyebrow">Michigan DIFS · PSI exam series 16-81</div>
      <h1>Property &amp; Casualty Producer Exam Prep</h1>
    </div>
    <dl class="decl" aria-label="Exam specifications">
      <div><dt>Items</dt><dd>150</dd></div>
      <div><dt>Time</dt><dd>2 h 30 m</dd></div>
      <div><dt>Pass</dt><dd>74%</dd></div>
      <div><dt>Need</dt><dd>111 right</dd></div>
    </dl>
  </div>
</header>
<div class="tabs-bar">
  <div class="wrap" style="display:flex">
    <nav class="tabs" role="tablist" aria-label="Sections">
      <button class="tab" role="tab" id="tab-home" data-view="home" aria-selected="true">Today</button>
      <button class="tab" role="tab" id="tab-study" data-view="study" aria-selected="false">Learn</button>
      <button class="tab" role="tab" id="tab-memory" data-view="memory" aria-selected="false">Memory aids</button>
      <button class="tab" role="tab" id="tab-practice" data-view="practice" aria-selected="false">Practice</button>
      <button class="tab" role="tab" id="tab-games" data-view="games" aria-selected="false">Games</button>
      <button class="tab" role="tab" id="tab-math" data-view="math" aria-selected="false">Math lab</button>
      <button class="tab" role="tab" id="tab-exam" data-view="exam" aria-selected="false">Mock exam</button>
      <button class="tab" role="tab" id="tab-cards" data-view="cards" aria-selected="false">Flashcards</button>
      <button class="tab" role="tab" id="tab-numbers" data-view="numbers" aria-selected="false">Key numbers</button>
    </nav>
    <span class="sync" id="sync">Progress: this browser</span>
  </div>
</div>
<main class="wrap">
  <section class="view" id="view-home"></section>
  <section class="view" id="view-study" hidden></section>
  <section class="view" id="view-memory" hidden></section>
  <section class="view" id="view-practice" hidden></section>
  <section class="view" id="view-games" hidden></section>
  <section class="view" id="view-math" hidden></section>
  <section class="view" id="view-exam" hidden></section>
  <section class="view" id="view-cards" hidden></section>
  <section class="view" id="view-numbers" hidden></section>
  <footer class="foot" id="foot"></footer>
</main>
<div id="toasts" aria-live="polite"></div>
<canvas id="confetti" aria-hidden="true"></canvas>
"""

def compose():
    v1 = open(os.path.join(HERE, 'template_v1.html')).read()
    head = v1[:v1.index('</style>')]
    extra = open(os.path.join(HERE, 'extra.css')).read()
    js = open(os.path.join(HERE, 'app.js')).read()
    return head + '\n' + extra + '\n</style>\n' + SHELL + '\n<script id="data" type="application/json">__DATA__</script>\n<script>\n' + js + '\n</script>\n'

meta = {
    'verified': os.environ.get('VERIFIED', 'October 2026'),
    'sourcesNote': ('Michigan Compiled Laws (Insurance Code of 1956, Act 218; Workers\' Disability Compensation Act, Act 317 of 1969; '
                    'Michigan Vehicle Code), read from legislature.mi.gov; PSI\'s Michigan content outline for Series 16-81; Michigan DIFS; '
                    'FEMA/NFIP; U.S. Treasury (TRIA); ISO and NCCI standard policy forms (editions named in each section).'),
}
data = {'questions': questions, 'cards': cards, 'numbers': numbers, 'guide': guide, 'meta': meta,
        'mnemonics': mnemonics, 'pairs': pairs, 'visuals': visuals, 'matchsets': matchsets}

print(f'questions {len(questions)}  cards {len(cards)}  numbers {len(numbers)}  guide {len(guide)}  hooks {len(mnemonics)}  pairs {len(pairs)}  visuals {len(visuals)}  matchsets {len(matchsets)}')
print('per section:', dict(per_sec))
print('answer positions:', dict(pos))
for w in warns: print('WARN', w)
for e in errors: print('ERROR', e)
if errors: sys.exit(1)

tpl = compose()
blob = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
html = tpl.replace('__DATA__', blob)
open(OUT, 'w').write(html)
print('wrote', OUT, f'{len(html)/1024:.0f} KB')
