"""Original, royalty-free audio made from scratch in code (no samples, no licenses needed):
a gentle plucked-string music bed and small sound effects for pop-ins and picture changes."""
import wave

import numpy as np

SR = 44100


def _pluck(freq, seconds=1.6, damping=0.996, seed=0):
    """Karplus-Strong plucked string."""
    rng = np.random.default_rng(seed)
    n = int(SR / freq)
    buf = rng.uniform(-1, 1, n)
    out = np.empty(int(SR * seconds))
    idx = 0
    for i in range(len(out)):
        out[i] = buf[idx]
        nxt = (idx + 1) % n
        buf[idx] = damping * 0.5 * (buf[idx] + buf[nxt])
        idx = nxt
    return out * np.linspace(1, 0.6, len(out))


def _note(name):
    names = {"C": -9, "D": -7, "E": -5, "F": -4, "G": -2, "A": 0, "B": 2}
    semis = names[name[0]] + (int(name[-1]) - 4) * 12
    return 440.0 * 2 ** (semis / 12)


# A warm, common progression (C - G - Am - F) played as arpeggios; generic, not any existing song.
CHORDS = [["C3", "E3", "G3", "C4", "E4", "G3"], ["G2", "D3", "G3", "B3", "D4", "G3"],
          ["A2", "E3", "A3", "C4", "E4", "A3"], ["F2", "C3", "F3", "A3", "C4", "F3"]]


def music_bed(seconds, bpm=96):
    """Looping plucked arpeggios plus a soft bass note on each bar, as a float32 stereo array."""
    total = int(SR * (seconds + 2))
    mix = np.zeros(total)
    cache = {}
    step = 60 / bpm / 2  # eighth notes
    t, bar = 0.0, 0
    while t < seconds + 1:
        chord = CHORDS[bar % len(CHORDS)]
        for k in range(8):
            name = chord[k % len(chord)]
            if name not in cache:
                cache[name] = _pluck(_note(name), seed=len(cache))
            s = int((t + k * step) * SR)
            if s >= total:
                continue
            note = cache[name] * (0.55 if k else 0.8)
            end = min(total, s + len(note))
            mix[s:end] += note[:end - s]
        bass = chord[0]
        key = bass + "_bass"
        if key not in cache:
            f = _note(bass) / 2
            tt = np.arange(int(SR * 2.4)) / SR
            cache[key] = np.sin(2 * np.pi * f * tt) * np.exp(-tt * 1.6) * 0.5
        s = int(t * SR)
        if s < total:
            end = min(total, s + len(cache[key]))
            mix[s:end] += cache[key][:end - s]
        t += step * 8
        bar += 1
    mix = mix[:int(SR * seconds)]
    fade = int(SR * 1.5)
    mix[:fade] *= np.linspace(0, 1, fade)
    mix[-fade:] *= np.linspace(1, 0, fade)
    mix /= max(1e-9, np.abs(mix).max())
    # slight stereo width: delay one channel by 12 ms
    right = np.concatenate([np.zeros(int(SR * 0.012)), mix])[:len(mix)]
    return np.stack([mix, right], axis=1).astype(np.float32)


def _pop():
    t = np.arange(int(SR * 0.09)) / SR
    freq = 520 + 900 * (t / t[-1])
    return np.sin(2 * np.pi * np.cumsum(freq) / SR) * np.exp(-t * 38)


def _whoosh(seed=1):
    rng = np.random.default_rng(seed)
    n = int(SR * 0.32)
    noise = rng.uniform(-1, 1, n)
    k = 60  # simple moving-average low-pass for a soft, airy sound
    soft = np.convolve(noise, np.ones(k) / k, mode="same")
    env = np.sin(np.linspace(0, np.pi, n)) ** 2
    return soft * env * 3.0


def effects_track(seconds, pops=(), whooshes=()):
    total = int(SR * (seconds + 1))
    mix = np.zeros(total)
    for times, clip, gain in ((pops, _pop(), 0.55), (whooshes, _whoosh(), 0.45)):
        for t in times:
            s = int(t * SR)
            if 0 <= s < total:
                end = min(total, s + len(clip))
                mix[s:end] += clip[:end - s] * gain
    mix = np.clip(mix[:int(SR * seconds)], -1, 1)
    return np.stack([mix, mix], axis=1).astype(np.float32)


def write_wav(path, stereo):
    data = (np.clip(stereo, -1, 1) * 32767).astype("<i2")
    with wave.open(str(path), "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(data.tobytes())
