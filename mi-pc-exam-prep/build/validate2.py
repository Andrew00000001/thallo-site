#!/usr/bin/env python3
"""Validate an interactive whiteboard lesson (format v2). Usage: python3 -I validate2.py <lesson.json> [...]
Prints OK or a list of problems. Exit code 1 on any problem."""
import json, os, re, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from validate import normalize, same, QS, MN, ICONS, SECS, GUIDES, S

WB = os.environ.get('WB') or os.path.join(S, 'wb')
PROPS = set()
_pf = os.environ.get('WB_PROPS')
for p in ([os.path.join(WB, x) for x in _pf.split(',')] if _pf else glob.glob(os.path.join(WB, 'props_*.js'))):
    src = open(p).read()
    PROPS |= set(re.findall(r'\bP\.([a-z][a-z0-9_]*)\s*=\s*(?:\{|P\.)', src))
PRIMS = {'label', 'num', 'note', 'stamp', 'box', 'circle', 'check', 'cross', 'line', 'divider', 'arrow', 'bubble', 'ring', 'xout', 'icon'}
REFP = {'arrow', 'line', 'ring', 'xout'}
COLORS = {'ink', 'blue', 'red', 'green', 'orange', 'purple', 'yellow', 'gray', 'brown', 'sky', 'pink', 'teal', 'white', 'paper'}
ANIMS = {'draw', 'pop', 'stamp', 'fade', 'slide-l', 'slide-r', 'drop', 'grow', 'fall', 'write'}
LOOPS = {'flicker', 'bob', 'shake', 'spin', 'pulse', 'wobble', 'float'}
SFX = {'ding', 'buzz', 'pop', 'stamp', 'whoosh', 'click', 'crash', 'tada', 'cash', 'boing'}
CAST = {'dana', 'sam', 'jen', 'tony', 'rosa', 'kid', 'adjuster', 'judge', 'thief', 'worker', 'doctor', 'boss', 'neighbor', 'grandma', 'regulator', 'person'}
POSES = {'stand', 'wave', 'point', 'shrug', 'cheer', 'think', 'hold', 'sad', 'run', 'stop', 'sit', 'walk'}
MOODS = {'happy', 'smirk', 'sad', 'worried', 'angry', 'shocked', 'laugh', 'neutral', 'sleep'}
VOICES = {'narrator': 'af_heart', 'dana': 'af_bella', 'sam': 'am_michael', 'tony': 'am_fenrir', 'rosa': 'bf_emma', 'jen': 'bf_emma',
          'grandma': 'bf_emma', 'regulator': 'bf_emma', 'adjuster': 'am_puck', 'judge': 'am_puck', 'kid': 'am_puck', 'worker': 'am_puck',
          'boss': 'am_puck', 'doctor': 'am_puck', 'neighbor': 'am_puck', 'thief': 'am_puck'}
DIMS = {'full': (160, 72), 'half': (80, 72), 'card': (100, 56), 'title': (90, 72), 'choice': (160, 58)}
TYPES = ['title', 'sketch', 'term', 'bullets', 'steps', 'compare', 'timeline', 'table', 'formula', 'scenario', 'bignum', 'hook', 'recap',
         'quiz', 'swipe', 'sort', 'explore', 'slider', 'choice']
GATES = {'quiz', 'swipe', 'sort', 'explore', 'slider', 'choice'}
DRAW_OK = {'title': 'title', 'sketch': 'full', 'term': 'half', 'explore': 'full', 'bullets': 'half', 'steps': 'half', 'formula': 'half',
           'scenario': 'half', 'bignum': 'half', 'hook': 'half', 'recap': 'half', 'quiz': 'half', 'slider': 'half', 'choice': 'choice'}

def money(n): return '$' + format(round(n), ',')
CALC = {
    'coins': (('value', 'pct', 'loss', 'ded', 'limit'), lambda p: max(0, min((p['loss'] * p['limit'] / (p['value'] * p['pct'] / 100) if p['limit'] < p['value'] * p['pct'] / 100 else p['loss']) - p['ded'], p['limit']))),
    'horc': (('rc', 'loss', 'acv', 'limit'), lambda p: min(p['loss'], p['limit']) if p['limit'] >= 0.8 * p['rc'] else min(max(p['acv'], p['loss'] * p['limit'] / (0.8 * p['rc'])), p['limit'])),
    'deductible': (('ded', 'loss'), lambda p: max(0, min(p['loss'] - p['ded'], p.get('limit') or float('inf')))),
    'prorata': (('a', 'b', 'loss'), lambda p: min(p['a'], p['loss'] * p['a'] / (p['a'] + p['b']))),
    'split': (('pp', 'pa', 'inj1'), lambda p: min(sum(min(v, p['pp']) for v in [p['inj1']] + list(p.get('others', []))), p['pa'])),
    'wcprem': (('rate', 'mod', 'payroll'), lambda p: p['payroll'] / 100 * p['rate'] * p['mod']),
    'lossratio': (('premium', 'losses'), lambda p: p['losses'] / p['premium'] * 100),
    'acv': (('rc', 'life', 'age'), lambda p: p['rc'] - p['rc'] * p['age'] / p['life']),
}
CALC_X = {'coins': 'limit', 'horc': 'limit', 'deductible': 'loss', 'prorata': 'loss', 'split': 'inj1', 'wcprem': 'payroll', 'lossratio': 'losses', 'acv': 'age'}

def check(path):
    P = []
    def err(m): P.append(m)
    try: L = json.load(open(path))
    except Exception as e: return [f'JSON parse error: {e}']
    def lim(v, n, where):
        if not isinstance(v, str) or not v.strip(): err(f'{where}: missing text'); return
        if len(v) > n: err(f'{where}: {len(v)} chars > {n}')
    def num(v, where, lo=None, hi=None):
        if not isinstance(v, (int, float)) or isinstance(v, bool): err(f'{where}: must be a number'); return False
        if (lo is not None and v < lo) or (hi is not None and v > hi): err(f'{where}: {v} outside {lo}..{hi}'); return False
        return True
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
    if not 9 <= len(sc) <= 18: err(f'scenes: {len(sc)} (need 9-18)')
    if sc and sc[0].get('type') != 'title': err('first scene must be type title')
    if sc and sc[-1].get('type') != 'recap': err('last scene must be type recap')
    gates = [s.get('type') for s in sc if s.get('type') in GATES]
    if not 4 <= len(gates) <= 8: err(f'{len(gates)} activity scenes (choice/quiz/swipe/sort/explore/slider): need 4-8')
    if not 2 <= gates.count('choice') <= 4: err(f'{gates.count("choice")} choice scenes: need 2-4 (the choose-what-happens story moments)')
    if not 1 <= gates.count('quiz') <= 3: err('need 1-3 quiz scenes')
    if len(set(gates) - {'quiz', 'choice'}) < 1: err('besides choice and quiz, use at least 1 other activity type (swipe, sort, explore, slider)')
    if sum(1 for s in sc if s.get('type') == 'term') < 2: err('need at least 2 term scenes')
    if sum(1 for s in sc if s.get('draw')) < 5: err('need drawings (draw) in at least 5 scenes')
    words = 0; cast_words = 0
    for si, s in enumerate(sc):
        W = f'scenes[{si}]'
        t = s.get('type')
        if t not in TYPES: err(f'{W}: bad type {t}'); continue
        beats = s.get('beats', []); reveal = s.get('reveal', []) if t in GATES else []
        if s.get('reveal') and t not in GATES: err(f'{W}: reveal only on activity scenes')
        allb = beats + reveal
        if not beats: err(f'{W}: no beats')
        if t in GATES and not 1 <= len(reveal) <= 3: err(f'{W}: 1-3 reveal beats required')
        # titles and sources
        if t in ('title',): lim(s.get('title'), 70, f'{W}.title'); lim(s.get('subtitle'), 110, f'{W}.subtitle')
        elif t == 'quiz':
            if s.get('title'): lim(s['title'], 60, f'{W}.title')
        elif t == 'recap':
            if s.get('title'): lim(s['title'], 60, f'{W}.title')
        else: lim(s.get('title'), 60, f'{W}.title')
        if t not in ('title', 'quiz', 'recap'): lim(s.get('src'), 140, f'{W}.src')
        elif s.get('src'): lim(s['src'], 140, f'{W}.src')
        if s.get('icon') and s['icon'] not in ICONS: err(f'{W}: unknown icon {s["icon"]}')
        # drawings
        if s.get('draw') is not None:
            if t not in DRAW_OK: err(f'{W}: type {t} cannot have a drawing')
            else: check_draw(s['draw'], DIMS[DRAW_OK[t]], allb, f'{W}.draw', err)
        if t in ('sketch', 'term', 'explore', 'choice') and not s.get('draw'): err(f'{W}: {t} scene needs a drawing (draw)')
        items = s.get('items', [])
        n = None
        if t in ('bullets', 'steps'):
            if not 2 <= len(items) <= 5: err(f'{W}: 2-5 items')
            for i, it in enumerate(items):
                lim(it.get('label'), 48, f'{W}.items[{i}].label')
                if it.get('detail') is not None: lim(it['detail'], 110, f'{W}.items[{i}].detail')
                if it.get('icon') and it['icon'] not in ICONS: err(f'{W}.items[{i}]: unknown icon {it["icon"]}')
            n = len(items)
        elif t == 'term':
            lim(s.get('term'), 40, f'{W}.term'); lim(s.get('plain'), 150, f'{W}.plain'); lim(s.get('example'), 170, f'{W}.example')
            if s.get('exam') is not None: lim(s['exam'], 150, f'{W}.exam')
            if s.get('kind') is not None: lim(s['kind'], 20, f'{W}.kind')
            n = 4 if s.get('exam') else 3
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
            if not any(b.get('answer') for b in beats): err(f'{W}: one beat must set "answer": true')
        elif t == 'bignum':
            if not 1 <= len(items) <= 4: err(f'{W}: 1-4 items')
            for i, it in enumerate(items): lim(it.get('value'), 14, f'{W}.items[{i}].value'); lim(it.get('label'), 50, f'{W}.items[{i}].label')
            n = len(items)
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
        elif t == 'quiz':
            lim(s.get('q'), 200, f'{W}.q')
            ch = s.get('choices', [])
            if not 3 <= len(ch) <= 4: err(f'{W}: 3-4 choices')
            for i, c in enumerate(ch): lim(c, 80, f'{W}.choices[{i}]')
            if len({c.strip().lower() for c in ch}) != len(ch): err(f'{W}: duplicate choices')
            if s.get('answer') not in range(len(ch)): err(f'{W}: answer index out of range')
            lim(s.get('why'), 200, f'{W}.why')
        elif t == 'swipe':
            opts = s.get('options', [])
            if not 2 <= len(opts) <= 3: err(f'{W}: 2-3 options')
            for i, o in enumerate(opts): lim(o, 18, f'{W}.options[{i}]')
            cards = s.get('cards', [])
            if not 3 <= len(cards) <= 6: err(f'{W}: 3-6 cards')
            for i, c in enumerate(cards):
                lim(c.get('text'), 110, f'{W}.cards[{i}].text'); lim(c.get('why'), 150, f'{W}.cards[{i}].why')
                if c.get('answer') not in range(len(opts)): err(f'{W}.cards[{i}].answer out of range')
                if c.get('draw'): check_draw(c['draw'], DIMS['card'], None, f'{W}.cards[{i}].draw', err)
            if len({c.get('answer') for c in cards}) < 2: err(f'{W}: cards should not all have the same answer')
        elif t == 'sort':
            bins = s.get('bins', [])
            if not 2 <= len(bins) <= 3: err(f'{W}: 2-3 bins')
            for i, b in enumerate(bins): lim(b.get('name'), 22, f'{W}.bins[{i}].name')
            if not 4 <= len(items) <= 8: err(f'{W}: 4-8 items')
            for i, it in enumerate(items):
                lim(it.get('text'), 60, f'{W}.items[{i}].text'); lim(it.get('why'), 120, f'{W}.items[{i}].why')
                if it.get('bin') not in range(len(bins)): err(f'{W}.items[{i}].bin out of range')
            if len({it.get('bin') for it in items}) < len(bins): err(f'{W}: every bin needs at least one item')
        elif t == 'explore':
            ids = {e.get('id') for e in s.get('draw', []) if e.get('id')}
            spots = s.get('spots', [])
            if not 2 <= len(spots) <= 6: err(f'{W}: 2-6 spots')
            for i, sp in enumerate(spots):
                if sp.get('on') not in ids: err(f'{W}.spots[{i}].on: no element with id {sp.get("on")!r} in draw')
                lim(sp.get('label'), 40, f'{W}.spots[{i}].label'); lim(sp.get('text'), 170, f'{W}.spots[{i}].text')
        elif t == 'choice':
            if s.get('ask') is not None: lim(s['ask'], 40, f'{W}.ask')
            opts = s.get('options', [])
            if not 2 <= len(opts) <= 4: err(f'{W}: 2-4 options')
            if sum(1 for o in opts if o.get('ok') is True) != 1: err(f'{W}: exactly one option must have "ok": true')
            for fa in [s.get('failAt')] + [o.get('failAt') for o in opts]:
                if fa is not None and not (isinstance(fa, list) and len(fa) == 2 and 0 <= fa[0] <= 160 and 0 <= fa[1] <= 58): err(f'{W}: failAt must be [x, y] on the 160 x 58 canvas')
            for oi, o in enumerate(opts):
                OW = f'{W}.options[{oi}]'
                lim(o.get('label'), 44, f'{OW}.label')
                if o.get('ok'): lim(o.get('win'), 150, f'{OW}.win')
                else: lim(o.get('fail'), 150, f'{OW}.fail')
                ob = o.get('beats', [])
                if not 1 <= len(ob) <= 2: err(f'{OW}: 1-2 outcome beats')
                if sum(len((b.get('say') or '').split()) for b in ob) > 40: err(f'{OW}: outcome narration over 40 words')
                if not o.get('draw'): err(f'{OW}: needs its own outcome drawing (draw)')
                else: check_draw(o['draw'], DIMS['choice'], ob, f'{OW}.draw', err)
                for bj, b in enumerate(ob):
                    BW = f'{OW}.beats[{bj}]'
                    lim(b.get('text'), 300, f'{BW}.text'); lim(b.get('say'), 300, f'{BW}.say')
                    say = b.get('say') or ''
                    if re.search(r'[0-9$%§&/+=<>#@]', say): err(f'{BW}.say: digits/symbols not allowed (write numbers as words)')
                    if re.search(r'[/+=<>#@§]', b.get('text') or ''): err(f'{BW}.text: write "and", "or", "per", "plus" instead of / + = < > # @ §')
                    d = same(b.get('text') or '', say)
                    if d: err(f'{BW}: {d}')
                    words += len(say.split())
                    vo = b.get('voice', 'narrator')
                    if vo not in VOICES: err(f'{BW}.voice must be one of {sorted(VOICES)}')
                    elif vo != 'narrator': cast_words += len(say.split())
                    if b.get('speaker') is not None: lim(b['speaker'], 16, f'{BW}.speaker')
                    if 'hl' in b:
                        ids = {e.get('id') for e in o.get('draw') or [] if e.get('id')}
                        for x in ([b['hl']] if isinstance(b['hl'], str) else b['hl'] if isinstance(b['hl'], list) else [None]):
                            if x not in ids: err(f'{BW}.hl: no element with id {x!r} in this option\'s drawing')
        elif t == 'slider':
            cn = s.get('calc')
            if cn not in CALC: err(f'{W}: calc must be one of {sorted(CALC)}')
            else:
                need, f = CALC[cn]; x = CALC_X[cn]
                v = s.get('var', {}); p = dict(s.get('params', {}))
                if v.get('key', x) != x: err(f'{W}.var.key must be {x!r} for calc {cn}')
                lim(v.get('label'), 40, f'{W}.var.label')
                ok = all(num(v.get(k), f'{W}.var.{k}') for k in ('min', 'max', 'step', 'start'))
                for k in need:
                    if k != x and not isinstance(p.get(k), (int, float)): err(f'{W}.params.{k} required (number)')
                if ok and v['min'] < v['max'] and v['step'] > 0 and all(isinstance(p.get(k), (int, float)) for k in need if k != x):
                    if not v['min'] <= v['start'] <= v['max']: err(f'{W}.var.start outside min..max')
                    if (v['max'] - v['min']) / v['step'] > 400: err(f'{W}: slider has more than 400 steps')
                    G = s.get('goal')
                    if G:
                        lim(G.get('text'), 120, f'{W}.goal.text')
                        if G.get('done') is not None: lim(G['done'], 60, f'{W}.goal.done')
                        if G.get('op') not in ('gte', 'lte', 'eq'): err(f'{W}.goal.op must be gte, lte or eq')
                        elif num(G.get('value'), f'{W}.goal.value'):
                            def met(val):
                                q = dict(p); q[x] = val; r = f(q)
                                return abs(r - G['value']) < 0.5 if G['op'] == 'eq' else (r <= G['value'] + 0.5 if G['op'] == 'lte' else r >= G['value'] - 0.5)
                            steps = [v['min'] + k * v['step'] for k in range(int(round((v['max'] - v['min']) / v['step'])) + 1)]
                            if not any(met(val) for val in steps): err(f'{W}.goal cannot be reached with this slider')
                            if met(v['start']): err(f'{W}.goal is already met at the start value')
        # beats
        last = 0
        for bi, b in enumerate(allb):
            BW = f'{W}.beats[{bi}]' if bi < len(beats) else f'{W}.reveal[{bi-len(beats)}]'
            lim(b.get('text'), 300, f'{BW}.text'); lim(b.get('say'), 300, f'{BW}.say')
            say = b.get('say') or ''
            if re.search(r'[0-9$%§&/+=<>#@]', say): err(f'{BW}.say: digits/symbols not allowed (write numbers as words)')
            if re.search(r'\b(e\.g|i\.e|etc)\b', say + ' ' + (b.get('text') or ''), re.I): err(f'{BW}: no e.g./i.e./etc.')
            if re.search(r'[/+=<>#@§]', b.get('text') or ''): err(f'{BW}.text: write "and", "or", "per", "plus" instead of / + = < > # @ §')
            if re.search(r'\b(MCL|U\.?S\.?C|CFR)\b', say): err(f'{BW}.say: do not read citations aloud')
            d = same(b.get('text') or '', say)
            if d: err(f'{BW}: {d}')
            wn = len(say.split()); words += wn
            vo = b.get('voice', 'narrator')
            if vo not in VOICES: err(f'{BW}.voice must be one of {sorted(VOICES)}')
            elif vo != 'narrator': cast_words += wn
            if b.get('speaker') is not None:
                if vo == 'narrator': err(f'{BW}.speaker: only for character voices')
                lim(b['speaker'], 16, f'{BW}.speaker')
            if n is not None and 'show' in b:
                if not isinstance(b['show'], int) or b['show'] < last or b['show'] > n: err(f'{BW}.show must be a non-decreasing int 0..{n}')
                else: last = b['show']
            if 'hl' in b:
                h = b['hl']
                if s.get('draw') and (isinstance(h, str) or isinstance(h, list)):
                    ids = {e.get('id') for e in s['draw'] if e.get('id')}
                    for x in ([h] if isinstance(h, str) else h):
                        if x not in ids: err(f'{BW}.hl: no element with id {x!r}')
                elif n is None or not isinstance(h, int) or not 0 <= h < n: err(f'{BW}.hl out of range')
        if n and t not in ('quiz', 'title') and last != n: err(f'{W}: the last beat must show all {n} items (show: {n})')
    if not 550 <= words <= 1300: err(f'narration is {words} words, counting choice outcomes (need 550-1300; listen-only lessons speak every fact on screen)')
    try:
        import clips as _clips
        for pr in _clips.problems(L): err(pr)
    except Exception as e:
        err(f'activity clips: {e}')
    if cast_words > 0.3 * max(words, 1): err(f'character voices speak {cast_words} of {words} words (keep it under 30%)')
    return P

def check_draw(els, dims, beats, W, err):
    if not isinstance(els, list) or not els: err(f'{W}: must be a non-empty list'); return
    if len(els) > 32: err(f'{W}: {len(els)} elements (max 32)')
    w, h = dims; nb = len(beats) if beats is not None else 1
    ids = [e.get('id') for e in els if isinstance(e, dict) and e.get('id')]
    if len(ids) != len(set(ids)): err(f'{W}: duplicate element ids')
    ids = set(ids)
    for i, e in enumerate(els):
        E = f'{W}[{i}]'
        if not isinstance(e, dict): err(f'{E}: must be an object'); continue
        p = e.get('p')
        if p not in PROPS and p not in PRIMS: err(f'{E}: unknown prop {p!r}'); continue
        if p == 'icon' and e.get('name') not in ICONS: err(f'{E}: unknown icon name {e.get("name")!r}')
        if p in REFP or p == 'bubble':
            for k in (('from', 'to') if p in ('arrow', 'line') else ('on',) if p in ('ring', 'xout') else ()):
                v = e.get(k)
                if isinstance(v, str):
                    if v not in ids: err(f'{E}.{k}: no element with id {v!r}')
                elif not (isinstance(v, list) and len(v) == 2 and all(isinstance(z, (int, float)) for z in v)): err(f'{E}.{k}: id or [x, y] required')
            if p == 'bubble' and e.get('to') is not None:
                v = e['to']
                if isinstance(v, str) and v not in ids: err(f'{E}.to: no element with id {v!r}')
        if p not in REFP:
            for k, lo, hi in (('x', -2, w + 2), ('y', -2, h + 2)):
                v = e.get(k)
                if not isinstance(v, (int, float)) or isinstance(v, bool): err(f'{E}.{k}: number required')
                elif not lo <= v <= hi: err(f'{E}.{k}={v} is off the {w}x{h} canvas')
        for k in ('h', 'w', 'size'):
            if k in e and (not isinstance(e[k], (int, float)) or e[k] <= 0 or e[k] > max(w, h)): err(f'{E}.{k}: bad value')
        if 'size' in e and isinstance(e['size'], (int, float)) and p in ('label', 'bubble', 'note') and e['size'] < 3.4: err(f'{E}.size: text smaller than 3.4 is unreadable')
        for k in ('color', 'fill', 'bg', 'paper', 'ink', 'lcolor'):
            if k in e and e[k] not in COLORS: err(f'{E}.{k}: unknown color {e[k]!r}')
        if 'anim' in e and e['anim'] not in ANIMS: err(f'{E}.anim must be one of {sorted(ANIMS)}')
        if 'loop' in e and e['loop'] not in LOOPS: err(f'{E}.loop must be one of {sorted(LOOPS)}')
        if 'sfx' in e and e['sfx'] not in SFX: err(f'{E}.sfx must be one of {sorted(SFX)}')
        if 'at' in e and (not isinstance(e['at'], int) or not 0 <= e['at'] < nb): err(f'{E}.at must be a beat index 0..{nb-1}')
        if 'out' in e and (not isinstance(e['out'], int) or not e.get('at', 0) < e['out'] < nb): err(f'{E}.out must be a later beat index')
        if 'cue' in e:
            if beats is None: err(f'{E}.cue: not allowed here')
            else:
                bt = (beats[e.get('at', 0)] if isinstance(e.get('at', 0), int) and 0 <= e.get('at', 0) < nb else {}).get('text', '')
                if not re.search(r'\b' + re.escape(str(e['cue']).lower()), bt.lower()): err(f'{E}.cue: word {e["cue"]!r} not in beat {e.get("at", 0)} text')
        if 'move' in e:
            m = e['move']
            if not isinstance(m, dict) or not (isinstance(m.get('to'), list) and len(m['to']) == 2): err(f'{E}.move.to: [x, y] required')
            else:
                if 'at' in m and (not isinstance(m['at'], int) or not e.get('at', 0) <= m['at'] < nb): err(f'{E}.move.at: beat index >= at')
                if 'cue' in m and beats is not None:
                    bt = beats[m.get('at', e.get('at', 0))].get('text', '') if 0 <= m.get('at', e.get('at', 0)) < nb else ''
                    if not re.search(r'\b' + re.escape(str(m['cue']).lower()), bt.lower()): err(f'{E}.move.cue: word not in that beat text')
                if 'sfx' in m and m['sfx'] not in SFX: err(f'{E}.move.sfx unknown')
        lens = {'label': 70, 'num': 14, 'note': 120, 'stamp': 16, 'bubble': 120, 'box': 40, 'circle': 30}
        if p in lens and p not in ('box', 'circle'): lim_t(e.get('text'), lens[p], f'{E}.text', err)
        if p in ('box',) and e.get('title') is not None: lim_t(e['title'], 40, f'{E}.title', err)
        if p == 'circle' and e.get('text') is not None: lim_t(e['text'], 30, f'{E}.text', err)
        if e.get('label') is not None and p in PROPS: lim_t(e['label'], 40, f'{E}.label', err)
        o = e.get('opt', {})
        if o is not None and not isinstance(o, dict): err(f'{E}.opt must be an object')
        elif p == 'person':
            if o.get('who', 'person') not in CAST: err(f'{E}.opt.who must be one of {sorted(CAST)}')
            if o.get('pose', 'stand') not in POSES: err(f'{E}.opt.pose must be one of {sorted(POSES)}')
            if o.get('mood', 'happy') not in MOODS: err(f'{E}.opt.mood must be one of {sorted(MOODS)}')
            if o.get('hold') and o['hold'] not in PROPS: err(f'{E}.opt.hold: unknown prop {o["hold"]!r}')
            if o.get('sign') is not None: lim_t(o['sign'], 16, f'{E}.opt.sign', err)
def lim_t(v, n, where, err):
    if not isinstance(v, str) or not v.strip(): err(f'{where}: missing text')
    elif len(v) > n: err(f'{where}: {len(v)} chars > {n}')

if __name__ == '__main__':
    bad = 0
    for p in sys.argv[1:]:
        r = check(p)
        if r:
            bad += 1; print(f'{p}: {len(r)} problem(s)'); [print('  -', x) for x in r]
        else:
            L = json.load(open(p)); w = sum(len(b['say'].split()) for s in L['scenes'] for b in s['beats'] + s.get('reveal', []) + ([x for o in s['options'] for x in o['beats']] if s.get('type') == 'choice' else []))
            print(f'{p}: OK ({len(L["scenes"])} scenes, {w} words, about {w/147:.1f} min of narration)')
    sys.exit(1 if bad else 0)
