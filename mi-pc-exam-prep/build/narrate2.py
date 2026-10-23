#!/usr/bin/env python3
"""Narrate v2 (interactive whiteboard) lesson JSON files with Kokoro TTS: a narrator plus character voices.
Every beat is transcribed back with Whisper (word timestamps also time the drawings' "cue" words). Writes MP3 + timing.
Usage: tts/venv/bin/python -I lessons/narrate.py --out lessons/audio lessons/final/L*.json
Writes <out>/<id>.mp3, <out>/<id>.timing.json, <out>/<id>.verify.json. Skips a lesson whose script hash is unchanged."""
import argparse, hashlib, json, os, subprocess, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from validate import normalize  # same normalizer the validator uses
from validate2 import VOICES, GATES

SR = 24000
VOICE, SPEED = 'af_heart', 1.0
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
    s = re.sub(r'\bDid over Should\b(?![,.;:!?])', 'Did, over Should,', s)
    s = re.sub(r'\bDid over Should\b', 'Did, over Should', s)
    s = re.sub(r'(?<!")\bA\b(?!")(?=,? (?:plus|minus)\b|,? (?:and|or) [A-D]\b)', '"A"', s)   # answer letters: "A and C" says "ay"
    s = re.sub(r'\b(out|picks?|picked|choose|chose|answer|choice) A(?=[,.;:?!]| (?:and|or)\b|$)', r'\1 "A"', s)
    s = re.sub(r'(?<!")\bA\b(?!["\'’])', lambda m: letter_a(s, m), s)
    for a_, b_ in MI_PLACES.items(): s = re.sub(rf'\b{a_}\b', b_, s)   # Michigan pronunciations
    return s

def letter_a(s, m):
    """A capital A inside a sentence is a letter ("ten percent of A", "M A I P F"); at a sentence start it is
    the article unless the letter is plainly meant ("A is the Abode", "A to D")."""
    pre, nxt = s[:m.start()], s[m.end():]
    if not pre.strip() or re.search(r'[.!?:;]\s*$', pre):
        return '"A"' if re.match(r' (?:is\b|to [A-Z]\b)', nxt) else 'A'
    return '"A"'
MI_PLACES = {'Houghton': 'Hoeton', 'Mackinac': 'Mackinaw', 'Saginaw': 'Sagginaw', 'Coney': 'Koney'}

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
    mdir = os.environ.get('TTS_MODEL') or os.path.join(HERE, '..', 'tts', 'model')  # Kokoro-82M ONNX: model.onnx + voices.npz
    tts = Kokoro(os.path.join(mdir, 'model.onnx'), os.path.join(mdir, 'voices.npz'))
    asr = WhisperModel('small.en', device='cpu', compute_type='int8')
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
        h = hashlib.sha256(json.dumps([VOICE, SPEED, GAP_BEAT, GAP_SCENE, GAP_QUIZ, [speak(x) for x in says], vo, sorted((k[0], str(k[1]), sorted(v)) for k, v in cuew.items())]).encode()).hexdigest()[:16]
        tp = os.path.join(a.out, f'{lid}.timing.json')
        if not a.force and os.path.exists(tp) and json.load(open(tp)).get('hash') == h and os.path.exists(os.path.join(a.out, f'{lid}.mp3')):
            print(lid, 'unchanged, skipped'); continue
        chunks, t, scenes, checks = [], 0.0, [], []
        def add(x):
            nonlocal t
            chunks.append(x); t += len(x) / SR
        def gap(sec): add(np.zeros(int(sec * SR), np.float32))
        def beat(si, key, b, where):
            """Speak one beat; transcribe it back; return (start, end, {cueword: offset})."""
            audio, sr = tts.create(speak(b['say']), voice=VOICES[b.get('voice', 'narrator')], speed=SPEED, lang='en-us')
            assert sr == SR
            audio = trim(np.asarray(audio, np.float32))
            rms = float(np.sqrt(np.mean(audio ** 2))) if len(audio) else 0.0
            if rms > 1e-4: audio = np.clip(audio * min(4.0, 0.075 / rms), -1, 1).astype(np.float32)   # even loudness across voices
            start = t; add(audio); end = t
            want = cuew.get((si, key))
            segs, _ = asr.transcribe(to16k(audio), beam_size=5, language='en', condition_on_previous_text=False, word_timestamps=bool(want))
            segs = list(segs); heard = ' '.join(x.text.strip() for x in segs); got = {}
            if want:
                ws = [(re.sub(r"[^a-z0-9']", '', w.word.lower()), w.start) for x in segs for w in (x.words or [])]
                for cw in want:
                    hit = next((st for wd, st in ws if wd.startswith(cw.replace("'", '')[:6]) or cw.startswith(wd) and len(wd) > 2), None)
                    if hit is not None: got[cw] = round(max(0.0, hit - 0.05), 3)
            e = wer(normalize(b['say']), heard_norm(heard))
            checks.append({'scene': si, 'beat': where, 'say': b['say'], 'heard': heard, 'wer': round(e, 3), 'voice': b.get('voice', 'narrator')})
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
        wav = np.concatenate(chunks)
        mp3 = os.path.join(a.out, f'{lid}.mp3')
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-',
                        '-af', 'loudnorm=I=-18:TP=-1.5:LRA=11', '-ar', str(SR), '-ac', '1',
                        '-c:a', 'libmp3lame', '-b:a', '48k', '-write_xing', '1', mp3], input=wav.tobytes(), check=True)
        webm = os.path.join(a.out, f'{lid}.webm')   # small Opus copy embedded in the single-file page
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', mp3, '-ac', '1', '-c:a', 'libopus', '-b:a', '10k', '-vbr', 'on',
                        '-application', 'voip', '-frame_duration', '60', '-compression_level', '10', webm], check=True)
        json.dump({'from': os.path.basename(mp3), 'sha256': hashlib.sha256(open(mp3, 'rb').read()).hexdigest(), 'bitrate': '10k'}, open(webm + '.json', 'w'))
        dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', mp3],
                                   capture_output=True, text=True, check=True).stdout.strip())
        shash = hashlib.sha256(json.dumps(says).encode()).hexdigest()[:16]
        json.dump({'id': lid, 'hash': h, 'shash': shash, 'voice': VOICE, 'dur': round(dur, 3), 'scenes': scenes}, open(tp, 'w'))
        bad = [c for c in checks if c['wer'] > 0]
        json.dump({'id': lid, 'beats': len(checks), 'mismatches': bad}, open(os.path.join(a.out, f'{lid}.verify.json'), 'w'), indent=1)
        line = f'{lid}: {dur/60:.1f} min, {len(checks)} beats, {len(bad)} transcript mismatches, {os.path.getsize(mp3)//1024} KB'
        print(line, flush=True); summary.append(line)
    print('\n'.join(summary))

if __name__ == '__main__':
    main()
