#!/usr/bin/env python3
"""Turn a Twitch clip into a vertical YouTube Short, using only free tools.

  prep   URL --out DIR   download the clip, transcribe it (faster-whisper, word timings)
                         and save 4 preview frames, so the agent can watch it before writing.
  render SHORT.json --work DIR --out FILE
                         build the 1080x1920 Short: blurred fill, reframed clip, hook headline,
                         word-by-word captions and an optional spoken hook (Edge TTS).

Short JSON (written by the agent):
{"url": "...", "slug": "...", "start": 0, "end": 42.5, "crop": "4:3", "focus_x": 0.5, "focus_y": 0.5, "zoom": 1.0,
 "hook_text": "HE WALKED INTO A VOLCANO", "hook_voice": "Kai just walked inside a volcano...",
 "title": "...", "description": "...", "tags": ["..."]}
crop: "full" (whole 16:9 frame), "4:3", "1:1" (both on a blurred fill), or "vertical" (full-screen 9:16).
focus_x / focus_y: where to crop (0 = left/top edge, 0.5 = centre, 1 = right/bottom edge).
zoom: 1.0 keeps the full frame height; 1.2 crops 20% tighter, e.g. to cut off a chat box.
cut_top / cut_bottom: fraction of the frame height removed before cropping, to drop the
stream's own viewer counter and burned-in captions (defaults: config.json "streamer").
"""
import argparse, asyncio, json, os, re, shutil, ssl, subprocess, sys, time
from pathlib import Path

import imageio_ffmpeg

HERE = Path(__file__).resolve().parent
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
W, H = 1080, 1920
VIDEO_TOP = 560  # y where the clip sits on the blurred fill; the hook headline goes above it
FONT = "Anton"
VOICE = "en-US-AndrewNeural"
CAPTION_WORDS = 3
YELLOW, WHITE = "&H0000F0FF&", "&H00FFFFFF&"  # ASS colours are BGR
# Captions stay advertiser-friendly; the audio is the streamer's own and isn't changed.
CENSOR = [("FUCK", "F*CK"), ("SHIT", "SH*T"), ("BITCH", "B*TCH"), ("NIGG", "N*GG"), ("PUSSY", "P*SSY"), ("DICK", "D*CK")]

# The cloud sandbox re-terminates TLS; edge-tts pins certifi, so trust the proxy CA when present.
CA = "/root/.ccr/ca-bundle.crt"


def run(args):
    r = subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", *args], capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"ffmpeg failed: {r.stderr[-2000:]}")


def probe(path):
    r = subprocess.run([FFMPEG, "-hide_banner", "-i", str(path)], capture_output=True, text=True)
    h, m, s = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr).groups()
    size = re.search(r"Video: .*?, (\d{3,5})x(\d{3,5})", r.stderr)
    fps = re.search(r"([\d.]+) fps", r.stderr)
    return {"seconds": int(h) * 3600 + int(m) * 60 + float(s),
            "width": int(size.group(1)), "height": int(size.group(2)), "fps": float(fps.group(1)) if fps else 30.0}


def install_font():
    fonts = Path.home() / ".fonts"
    fonts.mkdir(exist_ok=True)
    dst = fonts / "Anton-Regular.ttf"
    if not dst.exists():
        shutil.copy(HERE / "assets" / "Anton-Regular.ttf", dst)
        subprocess.run(["fc-cache", "-f"], capture_output=True)
    return fonts


# ---------- prep ----------

def download(url, out):
    dst = out / "clip.mp4"
    r = subprocess.run([sys.executable, "-m", "yt_dlp", "-q", "--no-warnings", "-f", "best[ext=mp4]/best",
                        "-o", str(dst), url], capture_output=True, text=True, timeout=600)
    if r.returncode or not dst.exists():
        sys.exit(f"download failed: {r.stderr[-1000:]}")
    return dst


def transcribe(clip):
    from faster_whisper import WhisperModel
    model = WhisperModel("small.en", device="cpu", compute_type="int8")
    segments, _ = model.transcribe(str(clip), language="en", word_timestamps=True, vad_filter=True)
    words = []
    for seg in segments:
        for w in seg.words or []:
            words.append({"start": round(w.start, 2), "end": round(w.end, 2), "word": w.word.strip()})
    return words


def prep(url, out):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    clip = download(url, out)
    info = probe(clip)
    words = transcribe(clip)
    (out / "words.json").write_text(json.dumps(words, ensure_ascii=False), encoding="utf-8")
    frames = []
    for k, frac in enumerate((0.1, 0.35, 0.6, 0.85)):
        f = out / f"frame{k}.jpg"
        run(["-ss", f"{info['seconds'] * frac:.2f}", "-i", str(clip), "-frames:v", "1", "-vf", "scale=960:-2", str(f)])
        frames.append(str(f))
    lines, line = [], []
    for w in words:  # a readable transcript with a timestamp every ~8 words
        if not line:
            line.append(f"[{w['start']:.1f}]")
        line.append(w["word"])
        if len(line) > 8:
            lines.append(" ".join(line))
            line = []
    if line:
        lines.append(" ".join(line))
    print(json.dumps({"clip": str(clip), **info, "frames": frames, "transcript": "\n".join(lines)},
                     indent=1, ensure_ascii=False))


# ---------- render ----------

async def _tts(text, mp3):
    import edge_tts
    import edge_tts.communicate as ec
    if os.path.exists(CA):
        ec._SSL_CTX = ssl.create_default_context(cafile=CA)
    await edge_tts.Communicate(text, VOICE, rate="+12%").save(str(mp3))


def tts(text, mp3, attempts=4):
    # The free Edge TTS endpoint drops requests now and then; retry before failing the build.
    for i in range(attempts):
        try:
            return asyncio.run(_tts(text, mp3))
        except Exception as e:
            if i == attempts - 1:
                raise
            print(f"tts retry {i + 1}: {e}", flush=True)
            time.sleep(2 * (i + 1))


def ass_time(t):
    cs = int(round(max(t, 0) * 100))
    return f"{cs // 360000}:{cs // 6000 % 60:02d}:{cs // 100 % 60:02d}.{cs % 100:02d}"


def clean(word):
    w = word.replace("{", "(").replace("}", ")").upper()
    for bad, ok in CENSOR:
        w = w.replace(bad, ok)
    return w


def caption_groups(words):
    groups, cur = [], []
    for w in words:
        if cur and (len(cur) == CAPTION_WORDS or w["start"] - cur[-1]["end"] > 0.6):
            groups.append(cur)
            cur = []
        cur.append(w)
        if re.search(r"[.?!,]$", w["word"]):
            groups.append(cur)
            cur = []
    if cur:
        groups.append(cur)
    return groups


def write_ass(sh, words, length, streamer, path, cap_margin):
    head = (
        f"[Script Info]\nScriptType: v4.00+\nPlayResX: {W}\nPlayResY: {H}\nWrapStyle: 0\nScaledBorderAndShadow: yes\n\n"
        "[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, "
        "Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, "
        "Alignment, MarginL, MarginR, MarginV, Encoding\n"
        f"Style: Hook,{FONT},112,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,0,0,0,0,100,100,1,0,1,7,4,8,70,70,190,1\n"
        f"Style: Credit,{FONT},44,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,0,0,0,0,100,100,2,0,1,4,2,8,70,70,{VIDEO_TOP - 70},1\n"
        f"Style: Cap,{FONT},104,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,0,0,0,0,100,100,1,0,1,8,4,2,60,60,{cap_margin},1\n\n"
        "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"
    )
    ev = [f"Dialogue: 1,{ass_time(0)},{ass_time(length)},Hook,,0,0,0,,{clean(sh['hook_text'])}",
          f"Dialogue: 1,{ass_time(0)},{ass_time(length)},Credit,,0,0,0,,{streamer.upper()} ON TWITCH"]
    for g in caption_groups(words):
        for k, w in enumerate(g):  # the spoken word lights up yellow
            end = g[k + 1]["start"] if k + 1 < len(g) else w["end"] + 0.25
            text = " ".join(("{\\c" + YELLOW + "}" + clean(x["word"]) + "{\\c" + WHITE + "}") if j == k
                            else clean(x["word"]) for j, x in enumerate(g))
            ev.append(f"Dialogue: 0,{ass_time(w['start'])},{ass_time(min(end, length))},Cap,,0,0,0,,{text}")
    Path(path).write_text(head + "\n".join(ev) + "\n", encoding="utf-8")


ASPECT = {"full": 16 / 9, "4:3": 4 / 3, "1:1": 1.0, "vertical": 9 / 16}


def crop_filter(mode, fx, fy, zoom, cut_top, cut_bottom):
    """Drop the stream's top and bottom overlay bands, crop to the mode's aspect ratio zoomed in
    `zoom` times around (fx, fy), then scale."""
    fx, fy = (min(max(float(v), 0.0), 1.0) for v in (fx, fy))
    ct, cb = (min(max(float(v), 0.0), 0.3) for v in (cut_top, cut_bottom))
    band = f"crop=iw:ih*{1 - ct - cb:.3f}:0:ih*{ct:.3f}"
    ch = f"ih/{max(float(zoom), 1.0):.3f}"
    cw = f"{ch}*{ASPECT[mode]:.5f}"
    scale = f"scale={W}:{H}" if mode == "vertical" else "scale=1080:-2"
    return f"{band},crop={cw}:{ch}:(iw-{cw})*{fx}:(ih-{ch})*{fy},{scale}"


def render(short, work, out):
    sh = json.loads(Path(short).read_text(encoding="utf-8"))
    work = Path(work)
    clip = work / "clip.mp4"
    info = probe(clip)
    start = float(sh.get("start", 0))
    end = min(float(sh.get("end", info["seconds"])), info["seconds"])
    length = end - start
    if length > 180:
        sys.exit("a Short must be 3 minutes or less")
    words = [{**w, "start": w["start"] - start, "end": w["end"] - start}
             for w in json.loads((work / "words.json").read_text(encoding="utf-8"))
             if start <= w["start"] < end]
    config = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
    fonts = install_font()
    ass = work / "short.ass"
    mode, fps = sh.get("crop", "4:3"), min(round(info["fps"]), 60)
    # Full-screen footage: keep captions low, off the face. Framed footage: just under the clip.
    write_ass(sh, words, length, config["streamer"]["name"], ass, 330 if mode == "vertical" else 440)
    streamer = config["streamer"]
    fg = crop_filter(mode, sh.get("focus_x", 0.5), sh.get("focus_y", 0.5), sh.get("zoom", 1.0),
                     sh.get("cut_top", streamer.get("cut_top", 0)), sh.get("cut_bottom", streamer.get("cut_bottom", 0)))
    if mode == "vertical":
        video = f"[0:v]{fg},setsar=1[base]"
    else:
        video = (f"[0:v]split[a][b];[a]scale=270:480:force_original_aspect_ratio=increase,crop=270:480,"
                 f"boxblur=10:2,scale={W}:{H},eq=brightness=-0.12[bg];[b]{fg}[fg];"
                 f"[bg][fg]overlay=(W-w)/2:{VIDEO_TOP},setsar=1[base]")
    video += f";[base]ass={ass}:fontsdir={fonts},fps={fps},format=yuv420p[v]"

    inputs = ["-ss", f"{start:.3f}", "-t", f"{length:.3f}", "-i", str(clip)]
    if sh.get("hook_voice"):
        mp3 = work / "hook.mp3"
        tts(sh["hook_voice"], mp3)
        hook_end = probe_audio(mp3) + 0.3
        inputs += ["-i", str(mp3)]
        audio = (f"[0:a]volume='if(lt(t,{hook_end:.2f}),0.22,1)':eval=frame[orig];"
                 f"[1:a]adelay=150|150,volume=1.6[vo];[orig][vo]amix=inputs=2:duration=first:normalize=0,"
                 f"loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]")
    else:
        audio = "[0:a]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]"
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    run([*inputs, "-filter_complex", video + ";" + audio, "-map", "[v]", "-map", "[a]", "-t", f"{length:.3f}",
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-c:a", "aac", "-b:a", "192k", "-ac", "2",
         "-movflags", "+faststart", str(out)])
    final = probe(out)
    print(json.dumps({"short": str(out), "seconds": round(final["seconds"], 1),
                      "size": f"{final['width']}x{final['height']}", "fps": fps, "caption_words": len(words)}))


def probe_audio(path):
    r = subprocess.run([FFMPEG, "-hide_banner", "-i", str(path)], capture_output=True, text=True)
    h, m, s = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr).groups()
    return int(h) * 3600 + int(m) * 60 + float(s)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    a1 = sub.add_parser("prep")
    a1.add_argument("url")
    a1.add_argument("--out", required=True)
    a2 = sub.add_parser("render")
    a2.add_argument("short")
    a2.add_argument("--work", required=True)
    a2.add_argument("--out", required=True)
    a = p.parse_args()
    prep(a.url, a.out) if a.cmd == "prep" else render(a.short, a.work, a.out)
