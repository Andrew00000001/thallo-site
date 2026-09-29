#!/usr/bin/env python3
"""Turn a Twitch clip into a vertical YouTube Short, using only free tools.

  prep   URL --out DIR   download the clip, transcribe it (faster-whisper, word timings)
                         and save 4 preview frames, so the agent can watch it before writing.
  render SHORT.json [--work DIR] --out FILE
                         build the 1080x1920 Short: blurred fill, reframed clip with automatic
                         punch-in zooms on loud moments, headline, setup and take cards, context
                         pop-ups, word-by-word captions and a progress bar. No voice-over.

Short JSON (written by the agent). One clip:
{"url": "...", "slug": "...", "clip_created": 1790431388, "start": 0, "end": 42.5,
 "crop": "4:3", "focus_x": 0.5, "focus_y": 0.5, "zoom": 1.0,
 "hook_text": "WHY ONLY 6/10?", "setup_text": "Kai just finished the Wolverine game",
 "take_text": "Too harsh or fair?", "emphasis": ["six", "story"],
 "popups": [{"at": 12.4, "text": "Lucian produced the soundtrack"}],
 "title": "...", "description": "...", "tags": ["..."]}
A story Short stitches clips: put the per-clip fields in "segments" (each with its own "work" dir from
prep, "start", "end", crop fields, optional "popups" and a chapter "label"), keep the rest top-level.
popups[].at and punch_ins are in the clip's own seconds (as in the prep transcript).
punch_ins: optional list of clip seconds to zoom on; by default the loudest moments are found.
crop: "full" (whole 16:9 frame), "4:3", "1:1" (both on a blurred fill), or "vertical" (full-screen 9:16).
focus_x / focus_y: where to crop (0 = left/top edge, 0.5 = centre, 1 = right/bottom edge).
zoom: 1.0 keeps the full frame height; 1.2 crops 20% tighter, e.g. to cut off a chat box.
cut_top / cut_bottom: fraction of the frame height removed before cropping, to drop the
stream's own viewer counter and burned-in captions (defaults: config.json "streamer").
"""
import argparse, json, re, shutil, subprocess, sys
from pathlib import Path

import imageio_ffmpeg

HERE = Path(__file__).resolve().parent
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
W, H = 1080, 1920
VIDEO_TOP = 560  # y where the clip sits on the blurred fill; the hook headline goes above it
FONT = "Anton"
CAPTION_WORDS = 3
YELLOW, WHITE = "&H0000F0FF&", "&H00FFFFFF&"  # ASS colours are BGR
# Captions stay advertiser-friendly; the audio is the streamer's own and isn't changed.
CENSOR = [("FUCK", "F*CK"), ("SHIT", "SH*T"), ("BITCH", "B*TCH"), ("NIGG", "N*GG"), ("PUSSY", "P*SSY"), ("DICK", "D*CK")]


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

PUNCH = 1.15          # punch-in zoom on loud moments
CARD_Y = 470          # setup/take cards sit just under the headline, off the subject's face
SETUP_SECONDS = 1.8   # setup card at the start
TAKE_SECONDS = 2.5    # take card at the end
RED = "&H003C3CFF&"   # emphasised words
BAR = "0xFFD400"      # progress bar (amber, as in the profile picture)


def ass_time(t):
    cs = int(round(max(t, 0) * 100))
    return f"{cs // 360000}:{cs // 6000 % 60:02d}:{cs // 100 % 60:02d}.{cs % 100:02d}"


def clean(word):
    w = word.replace("{", "(").replace("}", ")").upper()
    for bad, ok in CENSOR:
        w = w.replace(bad, ok)
    return w


def norm(word):
    return re.sub(r"[^a-z0-9/']", "", word.lower())


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


def write_ass(sh, words, popups, chapters, length, streamer, path):
    head = (
        f"[Script Info]\nScriptType: v4.00+\nPlayResX: {W}\nPlayResY: {H}\nWrapStyle: 0\nScaledBorderAndShadow: yes\n\n"
        "[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, "
        "Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, "
        "Alignment, MarginL, MarginR, MarginV, Encoding\n"
        f"Style: Hook,{FONT},112,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,0,0,0,0,100,100,1,0,1,7,4,8,70,70,190,1\n"
        f"Style: Credit,{FONT},44,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,0,0,0,0,100,100,2,0,1,4,2,8,70,70,110,1\n"
        f"Style: Cap,{FONT},104,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,0,0,0,0,100,100,1,0,1,8,4,2,60,60,440,1\n"
        # BorderStyle 3 draws an opaque box in OutlineColour behind the text.
        f"Style: Setup,{FONT},80,&H00FFFFFF,&H00FFFFFF,&H28000000,&H00000000,0,0,0,0,100,100,1,0,3,20,0,8,90,90,{CARD_Y},1\n"
        f"Style: Take,{FONT},84,&H00000000,&H00000000,&H0000D4FF,&H00000000,0,0,0,0,100,100,1,0,3,22,0,8,90,90,{CARD_Y},1\n"
        f"Style: Pop,{FONT},58,&H00000000,&H00000000,&H00FFFFFF,&H00000000,0,0,0,0,100,100,1,0,3,14,0,8,90,90,{VIDEO_TOP + 100},1\n"
        f"Style: Chap,{FONT},50,&H00000000,&H00000000,&H0000D4FF,&H00000000,0,0,0,0,100,100,1,0,3,10,0,7,50,50,{VIDEO_TOP + 24},1\n\n"
        "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"
    )
    pop_in = "{\\fad(80,120)\\fscx82\\fscy82\\t(0,140,\\fscx100\\fscy100)}"
    ev = [f"Dialogue: 1,{ass_time(0)},{ass_time(length)},Hook,,0,0,0,,{clean(sh['hook_text'])}",
          f"Dialogue: 1,{ass_time(0)},{ass_time(length)},Credit,,0,0,0,,{streamer.upper()} ON TWITCH"]
    if sh.get("setup_text"):
        ev.append(f"Dialogue: 3,{ass_time(0)},{ass_time(min(SETUP_SECONDS, length))},Setup,,0,0,0,,"
                  f"{{\\fad(0,150)}}{clean(sh['setup_text'])}")
    if sh.get("take_text") and length > TAKE_SECONDS + SETUP_SECONDS + 2:
        ev.append(f"Dialogue: 3,{ass_time(length - TAKE_SECONDS)},{ass_time(length)},Take,,0,0,0,,"
                  f"{pop_in}{clean(sh['take_text'])}")
    for a, b, label in chapters:
        ev.append(f"Dialogue: 2,{ass_time(a)},{ass_time(b)},Chap,,0,0,0,,{clean(label)}")
    for p in popups:
        ev.append(f"Dialogue: 2,{ass_time(p['at'])},{ass_time(min(p['at'] + p.get('dur', 2.5), length))},Pop,,0,0,0,,"
                  f"{pop_in}{clean(p['text'])}")
    emphasis = {norm(x) for e in sh.get("emphasis", []) for x in e.split()}
    for g in caption_groups(words):
        for k, w in enumerate(g):  # the spoken word lights up; emphasised words are red and bigger
            end = g[k + 1]["start"] if k + 1 < len(g) else w["end"] + 0.25
            parts = []
            for j, x in enumerate(g):
                hot = norm(x["word"]) in emphasis
                colour = RED if hot else (YELLOW if j == k else WHITE)
                size = "\\fscx125\\fscy125" if hot and j == k else ""
                parts.append("{\\c" + colour + size + "}" + clean(x["word"]) + "{\\c" + WHITE + "\\fscx100\\fscy100}")
            ev.append(f"Dialogue: 0,{ass_time(w['start'])},{ass_time(min(end, length))},Cap,,0,0,{g[0]['mv']},,"
                      + " ".join(parts))
    Path(path).write_text(head + "\n".join(ev) + "\n", encoding="utf-8")


ASPECT = {"full": 16 / 9, "4:3": 4 / 3, "1:1": 1.0, "vertical": 9 / 16}
FRAME_H = {"full": 608, "4:3": 810, "1:1": 1080, "vertical": H}  # clip height in the Short, at 1080 wide


def crop_filter(mode, fx, fy, zoom, cut_top, cut_bottom):
    """Drop the stream's top and bottom overlay bands, crop to the mode's aspect ratio zoomed in
    `zoom` times around (fx, fy), then scale."""
    fx, fy = (min(max(float(v), 0.0), 1.0) for v in (fx, fy))
    ct, cb = (min(max(float(v), 0.0), 0.3) for v in (cut_top, cut_bottom))
    band = f"crop=iw:ih*{1 - ct - cb:.3f}:0:ih*{ct:.3f}"
    z, a = max(float(zoom), 1.0), ASPECT[mode]
    # Largest box of the mode's aspect that fits (so a vertical Twitch clip works too), zoomed in z times.
    ch = f"'min(ih,iw/{a:.5f})/{z:.3f}'"
    cw = f"'min(ih,iw/{a:.5f})/{z:.3f}*{a:.5f}'"
    # Exact output size, so zoomed and normal pieces always match when they're joined.
    return f"{band},crop=w={cw}:h={ch}:x='(iw-ow)*{fx}':y='(ih-oh)*{fy}',scale={W}:{FRAME_H[mode]},setsar=1"


def loud_moments(clip, start, length, fixed=None):
    """Seconds (from the segment start) of the loudest spikes: shouts, laughs, hype. At most one
    every 7 s, never in the first or last second. `fixed` (clip seconds) overrides detection."""
    if fixed is not None:
        return sorted(t - start for t in fixed if start + 1 <= t <= start + length - 1.2)
    r = subprocess.run([FFMPEG, "-hide_banner", "-nostats", "-ss", f"{start:.3f}", "-t", f"{length:.3f}",
                        "-i", str(clip), "-af", "ebur128=metadata=1,ametadata=mode=print:key=lavfi.r128.M:file=-",
                        "-f", "null", "-"], capture_output=True, text=True)
    times = [float(x) for x in re.findall(r"pts_time:([\d.]+)", r.stdout)]
    levels = [float(x) for x in re.findall(r"lavfi\.r128\.M=(-?[\d.]+)", r.stdout)]
    pts = [(t - 0.2, m) for t, m in zip(times, levels) if m > -70]  # M is a 0.4 s window ending at t
    if len(pts) < 20:
        return []
    ranked = sorted(m for _, m in pts)
    bar = max(ranked[len(ranked) // 2] + 5, ranked[int(len(ranked) * 0.9)])
    picked = []
    for t, m in sorted(pts, key=lambda p: -p[1]):
        if m < bar or len(picked) >= max(1, int(length // 7)):
            break
        if 1.0 <= t <= length - 1.2 and all(abs(t - q) >= 6 for q in picked):
            picked.append(t)
    return sorted(picked)


def render_segment(seg, streamer, dst, fps):
    """One clip → a 1080x1920 piece with reframing and punch-ins, no text yet. Returns (start, length)."""
    clip = Path(seg["work"]) / "clip.mp4"
    info = probe(clip)
    start = float(seg.get("start", 0))
    length = min(float(seg.get("end", info["seconds"])), info["seconds"]) - start
    if length < 1:
        sys.exit(f"{seg['work']}: end must be at least 1 s after start (clip is {info['seconds']:.1f} s)")
    mode, zoom = seg.get("crop", "4:3"), float(seg.get("zoom", 1.0))
    where = (seg.get("focus_x", 0.5), seg.get("focus_y", 0.5))
    cuts = (seg.get("cut_top", streamer.get("cut_top", 0)), seg.get("cut_bottom", streamer.get("cut_bottom", 0)))
    pieces, t = [], 0.0  # (from, to, zoom): normal framing, with a quick punch-in around each loud moment
    for peak in loud_moments(clip, start, length, seg.get("punch_ins")):
        a, b = max(t, peak - 0.3), min(length, peak + 0.6)
        if a > t:
            pieces.append((t, a, zoom))
        pieces.append((a, b, zoom * PUNCH))
        t = b
    if t < length:
        pieces.append((t, length, zoom))
    n, framed = len(pieces), mode != "vertical"
    graph = f"[0:v]fps={fps},split={n + framed}" + "".join(f"[f{k}]" for k in range(n)) + ("[b]" if framed else "")
    for k, (a, b, z) in enumerate(pieces):
        graph += f";[f{k}]trim=start={a:.3f}:end={b:.3f},setpts=PTS-STARTPTS,{crop_filter(mode, *where, z, *cuts)}[p{k}]"
    graph += ";" + "".join(f"[p{k}]" for k in range(n)) + f"concat=n={n}:v=1:a=0[fg]"
    if framed:
        graph += (f";[b]scale=270:480:force_original_aspect_ratio=increase,crop=270:480,boxblur=10:2,"
                  f"scale={W}:{H},eq=brightness=-0.12,setsar=1[bg];[bg][fg]overlay=(W-w)/2:{VIDEO_TOP}[v]")
    else:
        graph += ";[fg]null[v]"
    graph += ";[0:a]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]"
    run(["-ss", f"{start:.3f}", "-t", f"{length:.3f}", "-i", str(clip), "-filter_complex", graph,
         "-map", "[v]", "-map", "[a]", "-t", f"{length:.3f}", "-c:v", "libx264", "-preset", "ultrafast", "-crf", "14",
         "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "256k", "-ac", "2", str(dst)])
    return start, length


def render(short, work, out):
    sh = json.loads(Path(short).read_text(encoding="utf-8"))
    config = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
    streamer = config["streamer"]
    segments = sh.get("segments") or [{**sh, "work": work}]
    if any(not s.get("work") for s in segments):
        sys.exit("every clip needs its prep folder: --work for one clip, or \"work\" in each segment")
    fps = min(min(round(probe(Path(s["work"]) / "clip.mp4")["fps"]) for s in segments), 60)
    fonts = install_font()
    parts_dir = Path(str(out) + ".parts")
    parts_dir.mkdir(parents=True, exist_ok=True)

    t0, words, popups, chapters, parts = 0.0, [], [], [], []
    for k, seg in enumerate(segments):
        part = parts_dir / f"seg{k}.mp4"
        start, length = render_segment(seg, streamer, part, fps)
        # Full-screen footage: keep captions low, off the face. Framed footage: just under the clip.
        mv = 330 if seg.get("crop", "4:3") == "vertical" else 440
        for w in json.loads((Path(seg["work"]) / "words.json").read_text(encoding="utf-8")):
            if start <= w["start"] < start + length:
                words.append({**w, "start": w["start"] - start + t0, "end": w["end"] - start + t0, "mv": mv})
        for p in seg.get("popups", []):
            if start <= p["at"] < start + length:
                popups.append({**p, "at": p["at"] - start + t0})
        if seg.get("label"):
            chapters.append((t0, t0 + length, seg["label"]))
        parts.append(part)
        t0 += length
    total = t0
    if total > 180:
        sys.exit("a Short must be 3 minutes or less")

    ass = parts_dir / "short.ass"
    write_ass(sh, words, popups, chapters, total, streamer["name"], ass)
    inputs = [x for p in parts for x in ("-i", str(p))]
    n = len(parts)
    graph = ("".join(f"[{k}:v][{k}:a]" for k in range(n)) + f"concat=n={n}:v=1:a=1[cv][ca];"
             f"[cv]ass={ass}:fontsdir={fonts}[tx];color=c={BAR}:s={W}x12:r={fps}[bar];"
             f"[tx][bar]overlay=x='-w+w*t/{total:.3f}':y=0:shortest=1,format=yuv420p[v];"
             # Short fades so the loop back to the start doesn't click.
             f"[ca]afade=t=in:d=0.08,afade=t=out:st={max(total - 0.15, 0):.3f}:d=0.15[a]")
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    run([*inputs, "-filter_complex", graph, "-map", "[v]", "-map", "[a]", "-t", f"{total:.3f}",
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-c:a", "aac", "-b:a", "192k", "-ac", "2",
         "-movflags", "+faststart", str(out)])
    shutil.rmtree(parts_dir)
    final = probe(out)
    print(json.dumps({"short": str(out), "seconds": round(final["seconds"], 1), "clips": n,
                      "size": f"{final['width']}x{final['height']}", "fps": fps, "caption_words": len(words),
                      "punch_ins": "auto" if not any("punch_ins" in s for s in segments) else "set"}))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    a1 = sub.add_parser("prep")
    a1.add_argument("url")
    a1.add_argument("--out", required=True)
    a2 = sub.add_parser("render")
    a2.add_argument("short")
    a2.add_argument("--work", help="prep folder of a one-clip Short")
    a2.add_argument("--out", required=True)
    a = p.parse_args()
    prep(a.url, a.out) if a.cmd == "prep" else render(a.short, a.work, a.out)
