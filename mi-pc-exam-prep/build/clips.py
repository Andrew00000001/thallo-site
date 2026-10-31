"""Spoken activity clips for a v2 lesson.

Everything a learner would otherwise have to read during an activity becomes a short narrated clip: the quiz
question and its choices, the story-choice options, each swipe card and sort item, each explore spot, and the
feedback after an answer (why, FAIL and win texts). The narrator reads them in the lesson voice; the player
plays each clip at its moment. clips(L) returns an ordered list of {id, text, say}:
  text  what the clip says, as written (captions and the transcript check compare against it)
  say   the spoken form for the voice: the lesson's own override in L['clipsay'][id] if there is one,
        else an automatic form (numbers, money and abbreviations spelled out like the narration does)
Usage: python3 clips.py lessons/v2/L08.json [...]   lists each lesson's clips and any spoken form that does not
       match its text (fix those with a "clipsay" override)."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from validate import normalize, same, num_words, ordinal

LETTERS = 'ABCD'
NUMS = ['One', 'Two', 'Three', 'Four']
STOP = set('the a an of to and or in on for is are be it its this that with as at by from your you his her their they he she we our not no do does if so but was were has have had can will just than then there what which who when how all any each one'.split())
# all-caps tokens the narration says as words (mnemonics, emphasis); every other abbreviation is spelled letter by letter
CAPS_WORDS = {'FEMA', 'STARR', 'CLEAN', 'CUP', 'DICE', 'PAPER', 'KABOOM', 'OK', 'ZIP', 'EXCEPT', 'AND', 'NOT', 'ALL', 'ONLY',
              'NO', 'NEVER', 'BOTH', 'ANY', 'MINNE', 'FAIL', 'NOW', 'STOP', 'YES', 'BAM', 'BUMP', 'TAG', 'WOW', 'OUCH', 'MORE', 'LESS',
              'BEFORE', 'AFTER', 'OR', 'IS', 'ARE', 'MUST', 'CAN', 'IF', 'THEN', 'FIRM', 'DID', 'SHOULD', 'LOSS'}
ROMAN = {'II': 'two', 'III': 'three', 'IV': 'four'}

def terminal(s):
    s = s.strip()
    return s if re.search(r'[.!?:]["\')]?$', s) else s + '.'

def words(t):
    return [w for w in normalize(t) if w not in STOP and len(w) > 1]

def covered(text, beats):
    """Share of the text's content words that the given narration beats already say."""
    w = words(text)
    if not w: return 1.0
    sp = set(x for b in beats for x in words(b.get('say') or b['text']))
    return sum(1 for z in w if z in sp) / len(w)

def auto_say(text):
    s = text.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('—', ', ').replace('–', ' to ').replace('…', '...').replace('&', ' and ').replace('§', 'section ')
    s = s.replace('×', ' times ').replace('÷', ' divided by ').replace('→', ', then ').replace('≥', ' at least ').replace('≤', ' at most ')
    s = re.sub(r'\be\.g\.,?', 'for example,', s); s = re.sub(r'\bi\.e\.,?', 'that is,', s); s = re.sub(r'\bvs\.', 'versus', s)
    s = re.sub(r'\$(\d[\d,]*(?:\.\d+)?)\s*(million|billion|thousand)\b', lambda m: num_words(m.group(1), False) + ' ' + m.group(2) + ' dollars', s)
    s = re.sub(r'\$(\d[\d,]*(?:\.\d+)?)', lambda m: num_words(m.group(1).rstrip(','), False) + ' dollars', s)
    s = re.sub(r'(\d[\d,]*(?:\.\d+)?)\s*%', lambda m: num_words(m.group(1), False) + ' percent', s)
    s = re.sub(r'\b(\d+)(st|nd|rd|th)\b', lambda m: ordinal(int(m.group(1))), s)
    s = re.sub(r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2})\b', lambda m: m.group(1) + ' ' + ordinal(int(m.group(2))), s)
    s = re.sub(r'\band/or\b', 'and or', s)
    mins = lambda d: '' if d == '00' else ' oh ' + num_words(d[1], False) if d[0] == '0' else ' ' + num_words(d, False)
    s = re.sub(r'\b(\d{1,2}):(\d{2})\s*([ap])\.?m\.?', lambda m: num_words(m.group(1), False) + mins(m.group(2)) + ' ' + m.group(3).upper() + ' M', s, flags=re.I)
    def caps(m):
        t = m.group(0)
        if t in CAPS_WORDS: return t.lower() if t not in ('FEMA', 'OK', 'ZIP') else t
        if t in ROMAN: return ROMAN[t]
        letters, num = re.match(r'([A-Z]+)-?(\d*)', t).groups()
        return ' '.join(letters) + ((' ' + num_words(num, False)) if num else '')
    s = re.sub(r'\b[A-Z]{2,}(?:-\d+)?\b|\b[A-Z]-\d+\b', caps, s)
    s = re.sub(r'(?<![\d.,:])0(\d)\b', lambda m: 'oh ' + num_words(m.group(1), False), s)   # a code's leading zero: Bulletin 96-02 is "ninety six, oh two"
    s = re.sub(r'(?<=\d),(?=\d{3}\b)', '', s)
    s = re.sub(r'\b\d+(?:\.\d+)?\b', lambda m: num_words(m.group(0), True), s)
    s = re.sub(r'(?<=[a-z])/(?=[a-z])', ' or ', s)
    s = re.sub(r'\s+\(([^()]*)\)', r', \1,', s)   # a spaced aside is said with pauses: the voice drops parentheses ("401(k)" stays)
    s = re.sub(r',\s*([,.;:!?])', r'\1', s)
    s = re.sub(r'\s+', ' ', s).replace(' ,', ',').replace(' .', '.').strip()
    return s

def clips(L):
    """Ordered clip list for lesson L (see the module docstring)."""
    out = [{'id': 'ok', 'text': "That's right."}, {'id': 'no', 'text': 'Not quite.'}]
    add = lambda cid, text: text and out.append({'id': cid, 'text': text.strip()})
    for si, sc in enumerate(L['scenes']):
        t = sc['type']; p = f's{si}'
        if t == 'quiz':
            add(p + '.q', terminal(sc['q']) + ' ' + ' '.join(f'{LETTERS[i]}: {terminal(c)}' for i, c in enumerate(sc['choices'])))
            if sc.get('why') and covered(sc['why'], sc.get('reveal', [])) < 0.75: add(p + '.why', sc['why'])
        elif t == 'swipe':
            opts = sc['options']
            add(p + '.intro', (', '.join(opts[:-1]) + ', or ' + opts[-1] + '?') if len(opts) > 1 else terminal(opts[0]))
            for k, c in enumerate(sc['cards']):
                add(f'{p}.c{k}', terminal(c['text'])); add(f'{p}.c{k}.why', c.get('why'))
        elif t == 'sort':
            names = [b['name'] for b in sc['bins']]
            add(p + '.intro', 'Sort each one: ' + ', '.join(names[:-1]) + ', or ' + names[-1] + '.')
            for k, x in enumerate(sc['items']):
                add(f'{p}.i{k}', terminal(x['text'])); add(f'{p}.i{k}.why', x.get('why') or f"It goes in {names[x['bin']]}.")
        elif t == 'explore':
            for k, x in enumerate(sc['spots']): add(f'{p}.p{k}', terminal(x['label']) + ' ' + x['text'])
        elif t == 'choice':
            add(p + '.ask', terminal(sc.get('ask') or 'What would you do?') + ' ' + ' '.join(f'{NUMS[k]}: {terminal(o["label"])}' for k, o in enumerate(sc['options'])))
            for k, o in enumerate(sc['options']):
                add(f'{p}.o{k}.fail' if not o.get('ok') else f'{p}.o{k}.win', o.get('fail') if not o.get('ok') else o.get('win'))
        elif t == 'slider':
            g = sc.get('goal') or {}
            if g.get('text') and covered(g['text'], sc.get('beats', [])) < 0.75: add(p + '.goal', g['text'])
            if g.get('done') and covered(g['done'], sc.get('reveal', [])) < 0.75: add(p + '.done', g['done'])   # the reveal right after usually says it
    over = L.get('clipsay', {})
    for c in out: c['say'] = over.get(c['id']) or auto_say(c['text'])
    return out

def signature(cl):
    """Fingerprint of a lesson's clips (ids and spoken text): the build refuses clip audio made from other text."""
    import hashlib
    return hashlib.sha256(json.dumps([(c['id'], c['say']) for c in cl]).encode()).hexdigest()[:16]

def same_clip(text, say):
    """same() from the validator, also accepting a possessive on a code ("DP-3's" said "D P three's") and a code's leading zero said "oh"."""
    d = same(text, say)
    if d is None: return None
    m = lambda t: ' '.join(normalize(re.sub(r'(?<![\d.,:])0(\d)\b', r'oh \1', re.sub(r"(\w)['\u2019]s\b", r'\1', re.sub(r'\b([A-Z]+)-(\d+)', r'\1 \2', t)))))
    return None if m(text) == m(say) else d

def problems(L):
    P, ids = [], set()
    for c in clips(L):
        ids.add(c['id'])
        d = same_clip(c['text'], c['say'])
        if d: P.append(f"clip {c['id']}: {d}  | text: {c['text'][:90]} | say: {c['say'][:90]}")
    for k in L.get('clipsay', {}):
        if k not in ids: P.append(f'clipsay {k}: no such clip')
    return P

if __name__ == '__main__':
    tot = 0
    for f in sys.argv[1:]:
        L = json.load(open(f)); C = clips(L); P = problems(L); tot += len(C)
        print(f"{L['id']}: {len(C)} clips, {sum(len(c['say'].split()) for c in C)} words, {len(P)} spoken-form problems")
        for x in P: print('   ', x)
    print('total clips', tot)
