#!/usr/bin/env python3
"""Validate a narrated lesson file. Usage: python3 -I validate.py <lesson.json> [...]
Prints OK or a list of problems. Exit code 1 on any problem."""
import json, os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
S = os.path.normpath(os.path.join(HERE, '..'))
ICON_DIR = os.environ.get('ICONS') or os.path.join(HERE, 'icons_dl', 'package', 'icons')
ICONS = {os.path.basename(p)[:-4] for p in glob.glob(os.path.join(ICON_DIR, '*.svg'))}
QS = {}
for p in glob.glob(os.path.join(os.environ.get('RES') or os.path.join(S, 'final'), '*_questions.json')):
    for q in json.load(open(p)):
        QS[q['id']] = q
MN = {}
for p in glob.glob(os.path.join(os.environ.get('LEARN') or os.path.join(S, 'learn'), 'mn_*.final.json')):
    for m in json.load(open(p)):
        MN[m['id']] = m
SECS = ['reg', 'gen', 'basics', 'dwelling', 'ho', 'auto', 'cpp', 'bop', 'wc', 'other']
T2S = {'reg': 'reg', 'gen': 'gen', 'basics': 'basics', 'mi': 'basics', 'dwelling': 'dwelling', 'ho': 'ho', 'auto': 'auto',
       'cpp': 'cpp', 'bop': 'bop', 'wc': 'wc', 'other': 'other'}
GUIDES = ['logistics', 'reg', 'gen', 'basics', 'mi', 'dwelling', 'ho', 'auto', 'cpp', 'bop', 'wc', 'other']
TYPES = ['title', 'bullets', 'steps', 'compare', 'timeline', 'table', 'formula', 'scenario', 'bignum', 'quiz', 'hook', 'recap']

# ---------- spoken-form normalizer ----------
ONES = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
TENS = 'zero ten twenty thirty forty fifty sixty seventy eighty ninety'.split()
ORD = {'one': 'first', 'two': 'second', 'three': 'third', 'five': 'fifth', 'eight': 'eighth', 'nine': 'ninth', 'twelve': 'twelfth'}

def w99(n):
    if n < 20: return ONES[n]
    return TENS[n // 10] + ('' if n % 10 == 0 else ' ' + ONES[n % 10])
def w999(n):
    h, r = divmod(n, 100)
    out = []
    if h: out.append(ONES[h] + ' hundred')
    if r or not h: out.append(w99(r))
    return ' '.join(out)
def n2w(n):
    if n == 0: return 'zero'
    parts = []
    for div, name in ((10**12, 'trillion'), (10**9, 'billion'), (10**6, 'million'), (1000, 'thousand')):
        if n >= div:
            q, n = divmod(n, div); parts.append(w999(q) + ' ' + name)
    if n: parts.append(w999(n))
    return ' '.join(parts)
def year(n):
    if 2000 <= n <= 2009: return n2w(n)
    a, b = divmod(n, 100)
    return w99(a) + ' ' + ('hundred' if b == 0 else ('oh ' + ONES[b] if b < 10 else w99(b)))
def ordinal(n):
    w = n2w(n).split(); last = w[-1]
    if last in ORD: w[-1] = ORD[last]
    elif last.endswith('y'): w[-1] = last[:-1] + 'ieth'
    else: w[-1] = last + 'th'
    return ' '.join(w)

def num_words(tok, years):
    """tok like 1,000 or 2.5 or 2020"""
    if '.' in tok:
        a, b = tok.split('.', 1)
        return n2w(int(a.replace(',', '') or 0)) + ' point ' + ' '.join(ONES[int(d)] for d in b)
    n = int(tok.replace(',', ''))
    if years and ',' not in tok and len(tok) == 4 and 1900 <= n <= 2099: return year(n)
    return n2w(n)

ROMAN = {'I': 'one', 'II': 'two', 'III': 'three', 'IV': 'four', 'V': 'five', 'VI': 'six'}
def roman_sections(s):
    def rep(m):
        return m.group(1) + ' ' + re.sub(r'\b(VI|IV|V|I{1,3})\b', lambda r: ROMAN[r.group(1)], m.group(2))
    return re.sub(r'\b(Sections?)\s+((?:(?:VI|IV|V|I{1,3})\b(?:\s*(?:,|and|or|through|to|-)\s*)?)+)', rep, s)

CONTRACTIONS = {"isn't": 'is not', "aren't": 'are not', "wasn't": 'was not', "weren't": 'were not', "doesn't": 'does not',
                "don't": 'do not', "didn't": 'did not', "can't": 'cannot', "won't": 'will not', "wouldn't": 'would not',
                "shouldn't": 'should not', "couldn't": 'could not', "hasn't": 'has not', "haven't": 'have not', "hadn't": 'had not', "mustn't": 'must not'}
def expand_neg(s):
    s = s.replace('\u2019', "'")
    return re.sub(r"\b(" + '|'.join(re.escape(k) for k in CONTRACTIONS) + r")\b", lambda m: (lambda r: r[0].upper() + r[1:] if m.group(1)[0].isupper() else r)(CONTRACTIONS[m.group(1).lower()]), s, flags=re.I)

ACRO_AI = {'ACV', 'ALE', 'AAI', 'ARM', 'AM', 'AOP', 'AI', 'ATV', 'ADA', 'ISO', 'IRMI', 'ID', 'IRS', 'IRA', 'IL'}
def join_caps(m):
    letters = m.group(0).split(' ')
    j = ''.join(letters)
    if letters[0] in ('A', 'I') and j not in ACRO_AI:
        return letters[0] + ' ' + ''.join(letters[1:])
    return j

def normalize(s, years=True):
    s = expand_neg(roman_sections(s))
    s = re.sub(r'\b([AaPp])\.\s?[Mm]\.', lambda m: m.group(1).lower() + 'm ', s)
    s = re.sub(r'\b(\d{1,2}):(\d{2})\b', lambda m: n2w(int(m.group(1))) + ' ' + ('' if m.group(2) == '00' else ('oh ' + ONES[int(m.group(2))] if int(m.group(2)) < 10 else w99(int(m.group(2))))), s)
    s = re.sub(r'\b[A-Z](?: [A-Z])+\b', join_caps, s)
    s = s.replace("'", '').replace('\u2019', '')
    s = re.sub(r'\b([Nn]on)[- ](?=[a-z])', r'\1', s)
    s = s.replace('’', "'").replace('‘', "'").replace('–', '-').replace('—', ' ').replace('&', ' and ')
    # $1 million / $2.5 billion
    s = re.sub(r'\$(\d[\d,]*(?:\.\d+)?)\s*(million|billion|thousand)\b', lambda m: num_words(m.group(1), False) + ' ' + m.group(2) + ' dollars', s)
    s = re.sub(r'\$(\d[\d,]*(?:\.\d+)?)', lambda m: num_words(m.group(1), False) + ' dollars', s)
    s = re.sub(r'(\d[\d,]*(?:\.\d+)?)\s*%', lambda m: num_words(m.group(1), False) + ' percent', s)
    s = re.sub(r'\b(\d+)(st|nd|rd|th)\b', lambda m: ordinal(int(m.group(1))), s)
    s = re.sub(r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2})\b', lambda m: m.group(1) + ' ' + ordinal(int(m.group(2))), s)
    s = re.sub(r'\d[\d,]*(?:\.\d+)?', lambda m: ' ' + num_words(m.group(0).rstrip(','), years) + ' ', s)
    s = s.lower().replace('-', ' ')
    s = re.sub(r"[^a-z' ]+", ' ', s)
    toks = [t.strip("'") for t in s.split()]
    toks = [t for t in toks if t]
    out, run = [], []
    for t in toks + ['']:
        if len(t) == 1 and (t not in ('a', 'i') or run):
            run.append(t); continue
        if run:
            out.append(''.join(run)); run = []
        if t: out.append(t)
    return [t for t in out if t != 'and']

def same(text, say):
    a, b = normalize(say), normalize(text)
    if a == b: return None
    b2 = normalize(text, years=False)
    if a == b2: return None
    i = next((k for k in range(min(len(a), len(b))) if a[k] != b[k]), min(len(a), len(b)))
    return f'text and say differ at word {i}: say "{" ".join(a[max(0,i-4):i+5])}" vs text "{" ".join(b[max(0,i-4):i+5])}"'

# ---------- checks ----------
def check(path):
    P = []
    def err(m): P.append(m)
    try: L = json.load(open(path))
    except Exception as e: return [f'JSON parse error: {e}']
    def lim(v, n, where):
        if not isinstance(v, str) or not v.strip(): err(f'{where}: missing text'); return
        if len(v) > n: err(f'{where}: {len(v)} chars > {n}')
    for k in ('id', 'sec', 'guide', 'title', 'summary', 'objectives', 'scenes', 'check', 'sources'):
        if k not in L: err(f'missing field {k}')
    if P: return P
    if not re.fullmatch(r'L\d\d', L['id']): err('id must be like L07')
    if os.path.basename(path).split('.')[0] != L['id']: err('file name must start with the lesson id')
    if L['sec'] not in SECS: err(f'sec must be one of {SECS}')
    if L['guide'] not in GUIDES: err(f'guide must be one of {GUIDES}')
    lim(L['title'], 70, 'title'); lim(L['summary'], 160, 'summary')
    if not 2 <= len(L['objectives']) <= 4: err('objectives: 2-4 items')
    for i, o in enumerate(L['objectives']): lim(o, 90, f'objectives[{i}]')
    if not 3 <= len(L['check']) <= 5: err('check: 3-5 question ids')
    for q in L['check']:
        if q not in QS: err(f'check: unknown question id {q}')
    if len(set(L['check'])) != len(L['check']): err('check: duplicate ids')
    for h in L.get('hooks', []):
        if h not in MN: err(f'hooks: unknown memory hook id {h}')
    if not L['sources']: err('sources: empty')
    sc = L['scenes']
    if not 8 <= len(sc) <= 14: err(f'scenes: {len(sc)} (need 8-14)')
    if sc and sc[0].get('type') != 'title': err('first scene must be type title')
    if sc and sc[-1].get('type') != 'recap': err('last scene must be type recap')
    nquiz = sum(1 for s in sc if s.get('type') == 'quiz')
    if not 2 <= nquiz <= 3: err(f'{nquiz} quiz scenes (need 2-3)')
    if not any(s.get('type') in ('scenario', 'formula') for s in sc): err('need at least one scenario or formula scene')
    words = 0
    for si, s in enumerate(sc):
        W = f'scenes[{si}]'
        t = s.get('type')
        if t not in TYPES: err(f'{W}: bad type {t}'); continue
        if t not in ('title', 'quiz') and t != 'recap': lim(s.get('title'), 60, f'{W}.title')
        if t == 'recap' and s.get('title'): lim(s['title'], 60, f'{W}.title')
        if t not in ('title', 'quiz', 'recap'):
            lim(s.get('src'), 140, f'{W}.src')
        elif s.get('src'): lim(s['src'], 140, f'{W}.src')
        if s.get('icon') and s['icon'] not in ICONS: err(f'{W}: unknown icon {s["icon"]}')
        items = s.get('items', [])
        n = None
        if t == 'title':
            lim(s.get('title'), 70, f'{W}.title'); lim(s.get('subtitle'), 110, f'{W}.subtitle')
            if s.get('icon') is None: err(f'{W}: title scene needs an icon')
        elif t in ('bullets', 'steps'):
            if not 2 <= len(items) <= 5: err(f'{W}: 2-5 items')
            for i, it in enumerate(items):
                lim(it.get('label'), 48, f'{W}.items[{i}].label')
                if it.get('detail') is not None: lim(it['detail'], 110, f'{W}.items[{i}].detail')
                if it.get('icon') and it['icon'] not in ICONS: err(f'{W}.items[{i}]: unknown icon {it["icon"]}')
            n = len(items)
        elif t == 'compare':
            cols = s.get('columns', [])
            if not 2 <= len(cols) <= 3: err(f'{W}: 2-3 columns')
            for ci, c in enumerate(cols):
                lim(c.get('name'), 32, f'{W}.columns[{ci}].name')
                if c.get('icon') and c['icon'] not in ICONS: err(f'{W}.columns[{ci}]: unknown icon {c["icon"]}')
                if not 1 <= len(c.get('points', [])) <= 4: err(f'{W}.columns[{ci}]: 1-4 points')
                for pi, p in enumerate(c.get('points', [])): lim(p, 80, f'{W}.columns[{ci}].points[{pi}]')
            if s.get('tell') is not None: lim(s['tell'], 140, f'{W}.tell')
            n = len(cols)
        elif t == 'timeline':
            if not 2 <= len(items) <= 6: err(f'{W}: 2-6 items')
            for i, it in enumerate(items):
                lim(it.get('at'), 16, f'{W}.items[{i}].at'); lim(it.get('label'), 40, f'{W}.items[{i}].label')
                if it.get('detail') is not None: lim(it['detail'], 90, f'{W}.items[{i}].detail')
            n = len(items)
        elif t == 'table':
            cols = s.get('columns', [])
            if not 2 <= len(cols) <= 4: err(f'{W}: 2-4 columns')
            for ci, c in enumerate(cols): lim(c, 24, f'{W}.columns[{ci}]')
            if not 2 <= len(items) <= 6: err(f'{W}: 2-6 rows')
            for ri, r in enumerate(items):
                if not isinstance(r, list) or len(r) != len(cols): err(f'{W}.items[{ri}]: row must have {len(cols)} cells'); continue
                for ci, c in enumerate(r): lim(c, 44, f'{W}.items[{ri}][{ci}]')
            n = len(items)
        elif t == 'formula':
            g = s.get('given', [])
            if len(g) > 4: err(f'{W}: given max 4')
            for i, x in enumerate(g): lim(x, 60, f'{W}.given[{i}]')
            if not 2 <= len(items) <= 5: err(f'{W}: 2-5 lines')
            for i, it in enumerate(items):
                lim(it.get('label'), 40, f'{W}.items[{i}].label'); lim(it.get('expr'), 60, f'{W}.items[{i}].expr'); lim(it.get('value'), 24, f'{W}.items[{i}].value')
            n = len(items)
        elif t == 'scenario':
            lim(s.get('story'), 260, f'{W}.story'); lim(s.get('answer'), 140, f'{W}.answer')
            if len(items) > 4: err(f'{W}: max 4 items')
            for i, it in enumerate(items):
                lim(it.get('label'), 48, f'{W}.items[{i}].label')
                if it.get('detail') is not None: lim(it['detail'], 110, f'{W}.items[{i}].detail')
            n = len(items)
            if not any(b.get('answer') for b in s.get('beats', [])): err(f'{W}: one beat must set "answer": true')
        elif t == 'bignum':
            if not 1 <= len(items) <= 4: err(f'{W}: 1-4 items')
            for i, it in enumerate(items): lim(it.get('value'), 14, f'{W}.items[{i}].value'); lim(it.get('label'), 50, f'{W}.items[{i}].label')
            n = len(items)
        elif t == 'quiz':
            lim(s.get('q'), 200, f'{W}.q')
            ch = s.get('choices', [])
            if not 3 <= len(ch) <= 4: err(f'{W}: 3-4 choices')
            for i, c in enumerate(ch): lim(c, 80, f'{W}.choices[{i}]')
            if len({c.strip().lower() for c in ch}) != len(ch): err(f'{W}: duplicate choices')
            if s.get('answer') not in range(len(ch)): err(f'{W}: answer index out of range')
            if not s.get('reveal'): err(f'{W}: reveal beats required')
            lim(s.get('why'), 200, f'{W}.why')
        elif t == 'hook':
            lim(s.get('hook'), 160, f'{W}.hook')
            if s.get('mn'):
                if s['mn'] not in MN: err(f'{W}: unknown mn {s["mn"]}')
                elif MN[s['mn']]['hook'].strip() != s['hook'].strip(): err(f'{W}: hook text must match {s["mn"]} exactly')
            if len(items) > 4: err(f'{W}: max 4 items')
            for i, it in enumerate(items): lim(it if isinstance(it, str) else None, 100, f'{W}.items[{i}]')
            n = len(items)
        elif t == 'recap':
            if not 3 <= len(items) <= 5: err(f'{W}: 3-5 items')
            for i, it in enumerate(items): lim(it if isinstance(it, str) else None, 70, f'{W}.items[{i}]')
            n = len(items)
        beats = s.get('beats', [])
        allb = beats + (s.get('reveal', []) if t == 'quiz' else [])
        if not beats: err(f'{W}: no beats')
        last = 0
        for bi, b in enumerate(allb):
            BW = f'{W}.beats[{bi}]'
            lim(b.get('text'), 300, f'{BW}.text'); lim(b.get('say'), 300, f'{BW}.say')
            say = b.get('say') or ''
            if re.search(r'[0-9$%§&/+=<>#@]', say): err(f'{BW}.say: digits/symbols not allowed (write numbers as words)')
            if re.search(r'\b(e\.g|i\.e|etc)\b', say + ' ' + (b.get('text') or ''), re.I): err(f'{BW}: no e.g./i.e./etc.')
            if re.search(r'[/+=<>#@§]', b.get('text') or ''): err(f'{BW}.text: write "and", "or", "per", "plus" instead of / + = < > # @ §')
            if re.search(r'\b(MCL|U\.?S\.?C|CFR)\b', say): err(f'{BW}.say: do not read citations aloud')
            d = same(b.get('text') or '', say)
            if d: err(f'{BW}: {d}')
            words += len(say.split())
            if n is not None and 'show' in b:
                if not isinstance(b['show'], int) or b['show'] < last or b['show'] > n: err(f'{BW}.show must be a non-decreasing int 0..{n}')
                else: last = b['show']
            if 'hl' in b and (n is None or not isinstance(b['hl'], int) or not 0 <= b['hl'] < n): err(f'{BW}.hl out of range')
        if n and t not in ('quiz', 'title') and last != n: err(f'{W}: the last beat must show all {n} items (show: {n})')
    if not 420 <= words <= 820: err(f'narration is {words} words (need 420-820)')
    return P

if __name__ == '__main__':
    bad = 0
    for p in sys.argv[1:]:
        r = check(p)
        if r:
            bad += 1; print(f'{p}: {len(r)} problem(s)'); [print('  -', x) for x in r]
        else:
            L = json.load(open(p)); w = sum(len(b['say'].split()) for s in L['scenes'] for b in s['beats'] + s.get('reveal', []))
            print(f'{p}: OK ({len(L["scenes"])} scenes, {w} words, about {w/155:.1f} min)')
    sys.exit(1 if bad else 0)
