#!/usr/bin/env python3
"""Offline text-to-speech for the Shorts' host commentary, on CPU, free.

Engine: Kokoro-82M (Apache-2.0) run by kokoro-onnx (onnxruntime + espeak-ng, all pip packages).
The model and the voice's style file come from a Hugging Face repo (config.json -> narrator.repo)
the first time they are needed and stay in the Hugging Face cache (HF_HOME, default
~/.cache/huggingface); nothing is installed outside pip.

  speak(text, out_wav) -> seconds      48 kHz mono wav, loudness matched to the clips (-14 LUFS)

Anything that stops speech from being made raises TTSError; make_short.py then refuses to render,
so a Short is never produced without its narration.

  python3 tts.py "Some words to say." out.wav      try it
"""
import json, os, re, subprocess, sys, tempfile, wave
from pathlib import Path

HERE = Path(__file__).resolve().parent
RATE = 48000          # output sample rate, as in the clips
LEAD = 0.1            # silence before the first word, so the Short's opening fade-in never clips it
LOUDNESS = "I=-14:TP=-1.5:LRA=11"   # the same target make_short.py gives the clips
ENGINES = ("kokoro",)

_engine = None


class TTSError(RuntimeError):
    pass


def narrator():
    """config.json -> narrator, with defaults."""
    cfg = json.loads((HERE / "config.json").read_text(encoding="utf-8")).get("narrator", {})
    return {"engine": "kokoro", "voice": "af_heart", "speed": 1.0,
            "repo": "onnx-community/Kokoro-82M-v1.0-ONNX", "model_file": "onnx/model_quantized.onnx", **cfg}


def describe():
    """What the sidecar records about the voice."""
    n = narrator()
    return {k: n[k] for k in ("engine", "repo", "model_file", "voice", "speed")}


def _cache_dir():
    base = os.environ.get("HF_HOME") or str(Path.home() / ".cache" / "huggingface")
    d = Path(base) / "gta6-kokoro"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _voices_file(repo, voice):
    """kokoro-onnx wants one .npz of style vectors. The repo ships each voice as a raw float32 file
    (510 x 1 x 256), so fetch the one we need and wrap it, once."""
    from huggingface_hub import hf_hub_download
    import numpy as np
    dst = _cache_dir() / f"{repo.replace('/', '--')}--{voice}.npz"
    if not dst.exists():
        raw = Path(hf_hub_download(repo, f"voices/{voice}.bin"))
        style = np.fromfile(raw, dtype=np.float32)
        if style.size % 256:
            raise TTSError(f"voice file voices/{voice}.bin in {repo} has an unexpected size")
        tmp = dst.with_name(dst.stem + ".tmp.npz")
        np.savez(tmp, **{voice: style.reshape(-1, 1, 256)})
        os.replace(tmp, dst)
    return dst


def _load():
    global _engine
    if _engine is None:
        n = narrator()
        if n["engine"] not in ENGINES:
            raise TTSError(f"config.json narrator.engine {n['engine']!r} is not supported (use one of {ENGINES})")
        os.environ.setdefault("HF_HUB_DISABLE_PROGRESS_BARS", "1")
        try:
            from huggingface_hub import hf_hub_download
            from kokoro_onnx import Kokoro
            model = hf_hub_download(n["repo"], n["model_file"])
            _engine = Kokoro(str(model), str(_voices_file(n["repo"], n["voice"])))
        except TTSError:
            raise
        except Exception as e:
            raise TTSError(f"could not load the {n['engine']} voice model {n['repo']}/{n['model_file']} "
                           f"(needs the kokoro-onnx package and a Hugging Face download): {type(e).__name__}: {e}") from e
    return _engine


def _ffmpeg(args):
    import imageio_ffmpeg
    return subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), "-hide_banner", "-y", *args], capture_output=True, text=True)


def _normalise(src, dst):
    """Two-pass loudnorm (measure, then apply linearly) to the clips' level, resampled to 48 kHz."""
    r = _ffmpeg(["-i", str(src), "-af", f"loudnorm={LOUDNESS}:print_format=json", "-f", "null", "-"])
    m = re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", r.stderr)
    af = f"loudnorm={LOUDNESS}"
    if m:
        s = json.loads(m.group(0))
        try:
            af += (f":measured_I={float(s['input_i'])}:measured_TP={float(s['input_tp'])}"
                   f":measured_LRA={float(s['input_lra'])}:measured_thresh={float(s['input_thresh'])}"
                   f":offset={float(s['target_offset'])}:linear=true")
        except (KeyError, ValueError):  # "-inf" for silence: the check below reports it
            pass
    r = _ffmpeg(["-i", str(src), "-af", af + f",aresample={RATE}", "-ac", "1", "-c:a", "pcm_s16le", str(dst)])
    if r.returncode:
        raise TTSError(f"ffmpeg could not process the speech: {r.stderr[-500:]}")


def speak(text, out_wav):
    """Say `text` and write it to out_wav (48 kHz mono). Returns the length in seconds, which
    includes LEAD seconds of silence at the start."""
    import numpy as np
    text = " ".join(str(text).split())
    if not text:
        raise TTSError("nothing to say: the narration line is empty")
    n = narrator()
    tts = _load()
    try:
        audio, rate = tts.create(text, voice=n["voice"], speed=min(max(float(n["speed"]), 0.5), 2.0), lang="en-us")
    except Exception as e:
        raise TTSError(f"speech synthesis failed for {text!r}: {type(e).__name__}: {e}") from e
    audio = np.concatenate([np.zeros(int(LEAD * rate), dtype=np.float32), np.asarray(audio, dtype=np.float32)])
    if len(audio) / rate < 0.3 or float(np.abs(audio).max()) < 0.01:
        raise TTSError(f"the voice produced silence for {text!r}")
    out_wav = Path(out_wav)
    out_wav.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        raw = Path(tmp) / "raw.wav"
        with wave.open(str(raw), "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(rate)
            w.writeframes((np.clip(audio, -1, 1) * 32767).astype("<i2").tobytes())
        _normalise(raw, out_wav)
    with wave.open(str(out_wav), "rb") as w:
        seconds = w.getnframes() / w.getframerate()
    if seconds < 0.3:
        raise TTSError(f"the speech for {text!r} came out empty")
    return seconds


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit('usage: python3 tts.py "text to say" out.wav')
    try:
        print(f"{speak(sys.argv[1], sys.argv[2]):.2f} s -> {sys.argv[2]}")
    except TTSError as e:
        sys.exit(f"error: {e}")
