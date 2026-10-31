#!/usr/bin/env python3
"""Narrate v2 (interactive whiteboard) lesson JSON files: Kokoro TTS for the narrator, and for characters either Kokoro
or a chosen take from the cast directory (see CAST_DIR). Every beat is transcribed back with Whisper (word timestamps
also time the drawings' "cue" words). Writes a full-quality Opus master, a small Opus copy for the page, and timing.
Usage: tts/venv/bin/python -I lessons/narrate.py --out lessons/audio lessons/final/L*.json
Writes <out>/<id>.hq.webm, <out>/<id>.webm, <out>/<id>.timing.json, <out>/<id>.verify.json. Skips a lesson whose script hash is unchanged."""
import argparse, collections, hashlib, json, os, subprocess, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from validate import normalize  # same normalizer the validator uses
from validate2 import VOICES, GATES

SR = 24000
VOICE, SPEED = 'af_heart', 1.0
# Character lines can be replaced by chosen takes from another engine (tts3/cast: Chatterbox Turbo cloning the same
# Kokoro voice). chosen.json maps cast_key(kokoro voice, say) -> {"file": wav path relative to the cast dir, ...}.
CAST_DIR = os.environ.get('CAST_DIR') or os.path.join(HERE, '..', 'tts3', 'cast')
def cast_key(kvoice, say): return hashlib.sha256(json.dumps(['cast1', kvoice, say]).encode()).hexdigest()[:16]
def load_cast():
    p = os.path.join(CAST_DIR, 'chosen.json')
    return json.load(open(p)) if os.path.exists(p) else {}
HQ_BITRATE = '32k'
# the small copy (embedded in the page; the offline fallback) is sized so the page with every lesson stays under 16 MB
SMALL_BITRATE, SMALL_FRAME = os.environ.get('SMALL_BITRATE', '10k'), os.environ.get('SMALL_FRAME', '60')
GAP_BEAT, GAP_SCENE, GAP_QUIZ = 0.32, 0.8, 0.5

def trim(a, thr=0.004, keep=0.06):
    idx = np.where(np.abs(a) > thr)[0]
    if not len(idx): return a[:0]
    s = max(0, idx[0] - int(keep * SR)); e = min(len(a), idx[-1] + int(keep * SR))
    return a[s:e]

import re
from validate import roman_sections, expand_neg
LABELS = r'Part|Parts|Coverage|Coverages|Section|Class|Symbol|Form|Schedule|Plan|Tier|Level|Type|Category|Division|Option|Item|Exhibit|Line|Grade|Policy|Policies|Insurer|Insurers|Company|Building|Location|Driver|Car|Vehicle|Choice'
def speak(say):
    """Pronunciation fixes for the TTS engine only; the script text is unchanged."""
    s = expand_neg(roman_sections(say))
    s = re.sub(rf'\b({LABELS})\s+A\b', r'\1 "A"', s)
    s = re.sub(r'\bA(?= (?:C V|M Best)\b)', '"A"', s)
    s = re.sub(r'(?<=[A-Za-z])-(?=[A-Za-z])', ' ', s)
    s = re.sub(r'\bP P I\b', 'P. P. I.', s)
    s = re.sub(r'\b([Aa])leatory\b', r'\1lea-tory', s)
    s = re.sub(r'\b(thir|four|fif|six|seven|eigh|nine)teen\b', r'\1-teen', s, flags=re.I)   # keep "-teen" stressed: sixteen is not sixty
    s = re.sub(r'\b([Ee])xcess of loss(?= [A-Za-z])', r'\1xcess, of loss,', s)
    s = re.sub(r'\b([Ee])xcess of loss\b', r'\1xcess, of loss', s)
    s = re.sub(r'\b([Ee])xcess\b', lambda m: m.group(1) + 'k-sess', s)                          # not "access"
    s = re.sub(r'\b([Dd])id over ([Ss])hould\b(?![,.;:!?])', r'\1id, over \2hould,', s)
    s = re.sub(r'\b([Dd])id over ([Ss])hould\b', r'\1id, over \2hould', s)
    s = re.sub(r'(?<!")\bA\b(?!")(?=,? (?:plus|minus)\b|,? (?:and|or) [A-D]\b)', '"A"', s)   # answer letters: "A and C" says "ay"
    s = re.sub(r'\b(out|picks?|picked|choose|chose|answer|choice) A(?=[,.;:?!]| (?:and|or)\b|$)', r'\1 "A"', s)
    s = re.sub(r'(?<!")\bA\b(?!["\'’])', lambda m: letter_a(s, m), s)
    for a_, b_ in MI_PLACES.items(): s = re.sub(rf'\b{a_}\b', b_, s)   # Michigan pronunciations
    s = re.sub(r'\bfour hundred one ?\(?k\)?(?=\W|$)', 'four-oh-one-K', s, flags=re.I)   # a 401(k) plan is said "four oh one K"
    s = re.sub(r'\b([Mm])onoline\b', r'\1ono line', s)   # "mono-line", not "MAH-noh-leen"
    s = re.sub(r'\b([Cc])oinsur', r'\1o insur', s)        # co-insurance, not "COIN-surance"
    s = re.sub(r'\b([Oo])bligee', r'\1bbligee', s)        # OB-li-jee, not "uh-BLIJ-ee" (heard as obligee)
    s = re.sub(r'\b([Ff])ungi\b', r'\1ungai', s)          # FUN-guy, one word (heard as fungi)
    return s

def letter_a(s, m):
    """A capital A inside a sentence is a letter ("ten percent of A", "M A I P F"); at a sentence start it is
    the article unless the letter is plainly meant ("A is the Abode", "A to D")."""
    pre, nxt = s[:m.start()], s[m.end():]
    if not pre.strip() or re.search(r'[.!?:;]\s*$', pre):
        return '"A"' if re.match(r' (?:is\b|to [A-Z]\b)|:', nxt) else 'A'
    return '"A"'
MI_PLACES = {'Houghton': 'Hoeton', 'Mackinac': 'Mackinaw', 'Saginaw': 'Sagginaw', 'Coney': 'Koney', 'Traverse': 'Travers'}

HOMOPHONES = {'bailey': 'bailee', 'baileys': 'bailees', 'lesser': 'lessor', 'lessers': 'lessors'}
def heard_norm(heard):
    h = re.sub(r'\b([A-Za-z])-?0(\d)', r'\1O\2', heard)
    return [HOMOPHONES.get(w, w) for w in normalize(h)]

def to16k(a):
    p = subprocess.run(['ffmpeg', '-v', 'error', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', '-ar', '16000', '-f', 'f32le', '-'],
                       input=a.astype(np.float32).tobytes(), capture_output=True, check=True)
    return np.frombuffer(p.stdout, dtype=np.float32)

def wer(ref, hyp):
    d = list(range(len(hyp) + 1))
    for i in range(1, len(ref) + 1):
        prev, d[0] = d[0], i
        for j in range(1, len(hyp) + 1):
            cur = min(d[j] + 1, d[j - 1] + 1, prev + (ref[i - 1] != hyp[j - 1]))
            prev, d[j] = d[j], cur
    return d[len(hyp)] / max(1, len(ref))

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--out', required=True); ap.add_argument('--force', action='store_true')
    ap.add_argument('files', nargs='+'); a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    from kokoro_onnx import Kokoro
    from faster_whisper import WhisperModel
    import soundfile as sf
    import clips as clipmod
    cast = load_cast()
    mdir = os.environ.get('TTS_MODEL') or os.path.join(HERE, '..', 'tts', 'model')  # Kokoro-82M ONNX: model.onnx + voices.npz
    tts = Kokoro(os.path.join(mdir, 'model.onnx'), os.path.join(mdir, 'voices.npz'))
    asr = [None]
    def get_asr():
        if asr[0] is None: asr[0] = WhisperModel('small.en', device='cpu', compute_type='int8')
        return asr[0]
    cdir = os.path.join(a.out, 'checks'); os.makedirs(cdir, exist_ok=True)   # transcript cache: one file per spoken line
    tdir = os.path.join(a.out, 'tts'); os.makedirs(tdir, exist_ok=True)   # synthesis cache: the voice model is deterministic, so a line said before is not synthesized again
    tfp = [os.path.getsize(os.path.join(mdir, x)) for x in ('model.onnx', 'voices.npz')]
    summary = []
    for f in a.files:
        L = json.load(open(f)); lid = L['id']
        allb = lambda s: s['beats'] + ([b for o in s['options'] for b in o['beats']] if s.get('type') == 'choice' else []) + s.get('reveal', [])
        says = [b['say'] for s in L['scenes'] for b in allb(s)]
        vo = [VOICES[b.get('voice', 'narrator')] for s in L['scenes'] for b in allb(s)]
        cuew = {}   # (scene, beat key) -> words whose time we need; option beats are keyed 'o<k>:<j>'
        for si, s in enumerate(L['scenes']):
            def scan(els, key):
                for e in els or []:
                    if e.get('cue'): cuew.setdefault((si, key(e.get('at', 0))), set()).add(str(e['cue']).lower())
                    m = e.get('move')
                    if isinstance(m, dict) and m.get('cue'): cuew.setdefault((si, key(m.get('at', e.get('at', 0)))), set()).add(str(m['cue']).lower())
            scan(s.get('draw'), lambda a: a)
            for k, o in enumerate(s['options'] if s.get('type') == 'choice' else []): scan(o.get('draw'), lambda a, k=k: f'o{k}:{a}')
        vs = [b.get('voice', 'narrator') for s in L['scenes'] for b in allb(s)]
        used = sorted({cast_key(VOICES[v], x) for v, x in zip(vs, says) if v != 'narrator'} & set(cast))
        castsig = [(k, cast[k].get('sha256', cast[k]['file'])) for k in used]
        CL = clipmod.clips(L)   # spoken activity text, read by the narrator after the main narration (full-quality file only)
        h = hashlib.sha256(json.dumps([VOICE, SPEED, GAP_BEAT, GAP_SCENE, GAP_QUIZ, [speak(x) for x in says], vo, sorted((k[0], str(k[1]), sorted(v)) for k, v in cuew.items()), castsig, HQ_BITRATE, [(c['id'], speak(c['say'])) for c in CL]]).encode()).hexdigest()[:16]
        tp = os.path.join(a.out, f'{lid}.timing.json')
        if not a.force and os.path.exists(tp) and json.load(open(tp)).get('hash') == h and os.path.exists(os.path.join(a.out, f'{lid}.hq.webm')):
            print(lid, 'unchanged, skipped'); continue
        chunks, t, scenes, checks = [], 0.0, [], []
        engines = collections.Counter(); fresh = [0]
        def add(x):
            nonlocal t
            chunks.append(x); t += len(x) / SR
        def gap(sec): add(np.zeros(int(sec * SR), np.float32))
        def line(say, v, want):
            """Synthesize one spoken line; return (audio, engine tag)."""
            ck = cast_key(VOICES[v], say)
            if v != 'narrator' and ck in cast:
                audio, sr = sf.read(os.path.join(CAST_DIR, cast[ck]['file']), dtype='float32'); tag = 'cast:' + cast[ck].get('sha256', '')
                engines[cast[ck].get('engine', 'cast')] += 1
            else:
                tk = os.path.join(tdir, hashlib.sha256(json.dumps(['tts1', tfp, VOICES[v], SPEED, speak(say)]).encode()).hexdigest()[:24] + '.npy')
                audio = None
                if os.path.exists(tk):
                    try: audio, sr = np.load(tk), SR
                    except Exception: audio = None
                if audio is None:
                    audio, sr = tts.create(speak(say), voice=VOICES[v], speed=SPEED, lang='en-us')
                    tmp = tk + f'.{os.getpid()}.tmp.npy'; np.save(tmp, np.asarray(audio, np.float32)); os.replace(tmp, tk)
                tag = 'kokoro:' + VOICES[v]; engines['kokoro'] += 1
            assert sr == SR
            audio = trim(np.asarray(audio, np.float32))
            rms = float(np.sqrt(np.mean(audio ** 2))) if len(audio) else 0.0
            if rms > 1e-4: audio = np.clip(audio * min(4.0, 0.075 / rms), -1, 1).astype(np.float32)   # even loudness across voices
            return audio, tag
        def check(audio, tag, say, ref_text, want):
            """Transcribe a line back (cached by engine, voice, spoken text and cue words); return (heard, wer, cue offsets)."""
            key = hashlib.sha256(json.dumps(['chk1', tag, speak(say), sorted(want or [])]).encode()).hexdigest()[:20]
            cp = os.path.join(cdir, key + '.json')
            c = None
            if os.path.exists(cp):
                try: c = json.load(open(cp))
                except ValueError: c = None
                if c and 'n' in c and c['n'] != len(audio): c = None   # the voice gave different audio this time: check it again
            if c is None:
                segs, _ = get_asr().transcribe(to16k(audio), beam_size=5, language='en', condition_on_previous_text=False, word_timestamps=bool(want))
                segs = list(segs); heard = ' '.join(x.text.strip() for x in segs); got = {}
                if want:
                    ws = [(re.sub(r"[^a-z0-9']", '', w.word.lower()), w.start) for x in segs for w in (x.words or [])]
                    for cw in want:
                        hit = next((st for wd, st in ws if wd.startswith(cw.replace("'", '')[:6]) or cw.startswith(wd) and len(wd) > 2), None)
                        if hit is not None: got[cw] = round(max(0.0, hit - 0.05), 3)
                c = {'heard': heard, 'got': got, 'n': len(audio)}
                tmp = cp + f'.{os.getpid()}.tmp'; json.dump(c, open(tmp, 'w')); os.replace(tmp, cp); fresh[0] += 1   # atomic: other runs share the cache
            return c['heard'], wer(normalize(ref_text), heard_norm(c['heard'])), c['got']
        def beat(si, key, b, where):
            """Speak one beat; transcribe it back; return (start, end, {cueword: offset})."""
            v = b.get('voice', 'narrator'); want = cuew.get((si, key))
            audio, tag = line(b['say'], v, want)
            start = t; add(audio); end = t
            heard, e, got = check(audio, tag, b['say'], b['say'], want)
            checks.append({'scene': si, 'beat': where, 'say': b['say'], 'heard': heard, 'wer': round(e, 3), 'voice': v})
            return round(start, 3), round(end, 3), got
        for si, s in enumerate(L['scenes']):
            sc = {'t0': round(t, 3), 'beats': []}; cues = {}
            seq = [('b', b) for b in s['beats']] + [('r', b) for b in s.get('reveal', [])]
            for k, (kind, b) in enumerate(seq):
                if kind == 'r' and 'q' not in sc:
                    sc['q'] = round(t, 3); gap(GAP_QUIZ)
                    if s.get('type') == 'choice':   # each option's outcome, played only when the learner picks it
                        sc['ob'] = []; oc = {}
                        for oi, o in enumerate(s['options']):
                            seg = []
                            for j, ob in enumerate(o['beats']):
                                b0, b1, got = beat(si, f'o{oi}:{j}', ob, f'o{oi}:{j}')
                                seg.append([b0, b1])
                                if got: oc.setdefault(str(oi), {})[str(j)] = got
                                gap(GAP_BEAT)
                            sc['ob'].append(seg); gap(GAP_QUIZ)
                        if oc: sc['ocues'] = oc
                    sc['r'] = round(t, 3)
                b0, b1, got = beat(si, k, b, k)
                sc['beats'].append([b0, b1])
                if got: cues[str(k)] = got
                if k < len(seq) - 1: gap(GAP_BEAT)
            if s.get('type') in GATES and 'q' not in sc:
                sc['q'] = round(t, 3); sc['r'] = round(t, 3)
            if cues: sc['cues'] = cues
            sc['t1'] = round(t, 3)
            scenes.append(sc)
            gap(GAP_SCENE)
        main_n = sum(len(x) for x in chunks)   # the main narration ends here; the activity clips follow
        clipt = {}
        gap(1.0)
        for c in CL:
            audio, tag = line(c['say'], 'narrator', None)
            start = t; add(audio); clipt[c['id']] = [round(start, 3), round(t, 3)]; gap(0.35)
            heard, e, _ = check(audio, tag, c['say'], c['text'], None)
            checks.append({'clip': c['id'], 'say': c['say'], 'text': c['text'], 'heard': heard, 'wer': round(e, 3), 'voice': 'narrator'})
        gap(0.5)
        wav = np.concatenate(chunks)
        p = subprocess.run(['ffmpeg', '-v', 'error', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-',
                            '-af', 'loudnorm=I=-18:TP=-1.5:LRA=11', '-ar', str(SR), '-ac', '1', '-f', 'f32le', '-'],
                           input=wav.tobytes(), capture_output=True, check=True)
        mix = p.stdout   # loudness-normalized lesson mix, 24 kHz mono float: main narration, then the clips
        hq = os.path.join(a.out, f'{lid}.hq.webm')   # full quality, with the clips: the master, published next to the page
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', '-c:a', 'libopus', '-b:a', HQ_BITRATE,
                        '-vbr', 'on', '-application', 'audio', '-compression_level', '10', hq], input=mix, check=True)
        hq_sha = hashlib.sha256(open(hq, 'rb').read()).hexdigest()
        json.dump({'from': os.path.basename(hq), 'sha256': hq_sha, 'bitrate': HQ_BITRATE}, open(hq + '.json', 'w'))
        webm = os.path.join(a.out, f'{lid}.webm')   # small Opus copy of the main narration only, embedded in the single-file page
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', '-c:a', 'libopus', '-b:a', SMALL_BITRATE, '-vbr', 'on',
                        '-application', 'voip', '-frame_duration', SMALL_FRAME, '-compression_level', '10', webm], input=mix[:main_n * 4], check=True)
        json.dump({'from': os.path.basename(hq), 'sha256': hq_sha, 'bitrate': SMALL_BITRATE, 'frame_ms': SMALL_FRAME}, open(webm + '.json', 'w'))
        probe = lambda x: float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', x], capture_output=True, text=True, check=True).stdout.strip())
        dur = round(main_n / SR, 3)
        shash = hashlib.sha256(json.dumps(says).encode()).hexdigest()[:16]
        json.dump({'id': lid, 'hash': h, 'shash': shash, 'voice': VOICE, 'master': os.path.basename(hq), 'engines': dict(engines),
                   'dur': dur, 'dur_full': round(probe(hq), 3), 'scenes': scenes, 'clips': clipt,
                   'clipsig': clipmod.signature(CL)}, open(tp, 'w'))
        vp = os.path.join(a.out, f'{lid}.verify.json')
        bad = [c for c in checks if c['wer'] > 0]
        json.dump({'id': lid, 'beats': sum(1 for c in checks if 'clip' not in c), 'clips': len(clipt), 'mismatches': bad}, open(vp, 'w'), indent=1)
        line_ = f"{lid}: {dur/60:.1f} min + {len(clipt)} clips ({(probe(hq)-dur)/60:.1f} min), {len(checks)} lines checked ({fresh[0]} new), {len(bad)} transcript mismatches, {os.path.getsize(hq)//1024} KB full, {os.path.getsize(webm)//1024} KB small"
        print(line_, flush=True); summary.append(line_)
    print('\n'.join(summary))

if __name__ == '__main__':
    main()
