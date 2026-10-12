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

meta = {
    'verified': os.environ.get('VERIFIED', 'October 2026'),
    'sourcesNote': ('Michigan Compiled Laws (Insurance Code of 1956, Act 218; Workers\' Disability Compensation Act, Act 317 of 1969; '
                    'Michigan Vehicle Code), read from legislature.mi.gov; PSI\'s Michigan content outline for Series 16-81; Michigan DIFS; '
                    'FEMA/NFIP; U.S. Treasury (TRIA); ISO and NCCI standard policy forms (editions named in each section).'),
}
data = {'questions': questions, 'cards': cards, 'numbers': numbers, 'guide': guide,
'meta': meta}

print(f'questions {len(questions)}  cards {len(cards)}  numbers {len(numbers)}  guide {len(guide)}')
print('per section:', dict(per_sec))
print('answer positions:', dict(pos))
for w in warns: print('WARN', w)
for e in errors: print('ERROR', e)
if errors: sys.exit(1)

tpl = open(os.path.join(HERE, 'template.html')).read()
blob = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
html = tpl.replace('__DATA__', blob)
open(OUT, 'w').write(html)
print('wrote', OUT, f'{len(html)/1024:.0f} KB')
