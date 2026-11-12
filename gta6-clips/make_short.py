#!/usr/bin/env python3
"""Turn Twitch clips into a vertical YouTube Short with added spoken commentary, using only free tools.

  prep   URL --out DIR   download the clip, transcribe it (faster-whisper, word timings)
                         and save 4 preview frames, so the agent can watch it before writing.
  frames FILE            save check frames of a rendered Short (the middle of the teaser, each clip, each
                         bridge card and the replay, the setup card and the last second) as jpgs.
  render SHORT.json [--work DIR] --out FILE
                         build the 1080x1920 Short: blurred fill, reframed clip with automatic
                         punch-in zooms on loud moments, headline, streamer credit, setup and take
                         cards, context pop-ups, word-by-word captions and a progress bar, plus
                         the added commentary: a synthetic host voice (tts.py) speaks over a
                         teaser, over title cards between clips and over a slow-motion replay.
                         The voice NEVER plays over the original clip. Writes FILE.json next to
                         the video (narration seconds and share), which upload.py checks.

Timeline of every Short:
  [teaser + hook voice] [clip 1, original audio] ([bridge card + bridge voice] [clip 2, original audio])...
  [replay + take voice]

Short JSON (written by the agent). One clip ("breakdown"):
{"format": "breakdown", "url": "...", "slug": "...", "streamer": "xQc", "clip_created": 1790431388,
 "start": 0, "end": 42.5, "crop": "1:1", "focus_x": 0.5, "focus_y": 0.5, "zoom": 1.0,
 "hook_text": "HOW DID HE SURVIVE THAT?", "setup_text": "Five stars and one flat tyre",
 "take_text": "Luck or skill?", "emphasis": ["five", "no way"],
 "popups": [{"at": 12.4, "text": "Five stars = the army shows up"}],
 "narration": {"hook": "...", "bridges": [], "take": "..."},
 "teaser": {"segment": 0, "from": 20.1, "to": 22.4},
 "replay": {"segment": 0, "from": 20.0, "to": 23.0, "speed": 0.5, "zoom": 1.25, "focus_x": 0.5, "focus_y": 0.5},
 "rating": "9/10 ESCAPE",
 "title": "...", "description": "...", "tags": ["..."]}
format: "breakdown" (one clip), "story" (2-3 clips in order) or "ranked" (2-3 clips counted down to #1).
narration.hook is spoken over the teaser, narration.bridges[i] over the card that introduces clip i+2
(exactly one fewer line than clips), narration.take over the replay. teaser/replay "from"/"to" are in
that clip's own seconds (as in the prep transcript); "segment" is the index into the clips.
rating: optional verdict stamp (16 characters or fewer) shown during the replay.
streamer: whose stream the clip is from (the name find_clips printed). It is shown under the
headline as "XQC ON TWITCH", so every Short credits its source on screen.
A story or ranked Short stitches clips: put the per-clip fields in "segments" (each with its own "work" dir
from prep, "streamer", "start", "end", crop fields, optional "popups" and a chapter "label"), keep the rest top-level.
popups[].at and punch_ins are in the clip's own seconds (as in the prep transcript).
punch_ins: optional list of clip seconds to zoom on; by default the loudest moments are found.
crop: "full" (whole 16:9 frame), "4:3", "1:1" (both on a blurred fill), or "vertical" (full-screen 9:16).
focus_x / focus_y: where to crop (0 = left/top edge, 0.5 = centre, 1 = right/bottom edge).
zoom: 1.0 keeps the full frame height; 1.2 crops 20% tighter, e.g. to cut off a chat box.
cut_top / cut_bottom: fraction of the frame height removed before cropping, to drop a stream's
own overlays such as a viewer counter or burned-in captions (defaults: config.json "crop_defaults").
"""
import argparse, hashlib, json, os, re, shutil, subprocess, sys
from pathlib import Path

import imageio_ffmpeg

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))  # tts.py sits next to this script
FONTS = HERE / "assets" / "fonts"  # libass loads the caption font straight from here
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


def fpath(path):
    """A path as an ffmpeg filter option: quoted, forward slashes, a Windows drive colon escaped."""
    return "'" + str(path).replace("\\", "/").replace(":", "\\:") + "'"


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
    model = WhisperModel(os.environ.get("WHISPER_MODEL", "small.en"), device="cpu", compute_type="int8")
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
SETUP_SECONDS = 1.8   # setup card at the start of the first clip
TAKE_SECONDS = 2.5    # take card at the end, over the replay
RED = "&H003C3CFF&"   # emphasised words
AMBER = "&H0000D4FF&"  # the host's current word
BAR = "0xFFD400"      # progress bar (amber, as in the profile picture)

FORMATS = ("breakdown", "story", "ranked")
TEASER_RANGE = (1.0, 3.0)      # seconds of source for the teaser
REPLAY_RANGE = (1.5, 4.0)      # seconds of source for the replay
TEASER_TAIL = 0.25             # the teaser outlasts the hook voice by this much
BRIDGE_TAIL = 0.2              # a bridge card outlasts its voice by this much
REPLAY_TAIL = 0.3              # the replay outlasts the take voice by this much
MAX_SLOWDOWN = 4.0
NARRATION_WORDS = {"hook": (6, 14), "bridge": (4, 12), "take": (12, 26)}  # advice, checked with warnings
NARR_CAPTION_WORDS = 4
BG = (f"scale=270:480:force_original_aspect_ratio=increase,crop=270:480,boxblur=10:2,"
      f"scale={W}:{H},eq=brightness=-0.12,setsar=1")
X264 = ["-c:v", "libx264", "-preset", "ultrafast", "-crf", "14", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "256k", "-ac", "2"]


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


def caption_groups(words, size=CAPTION_WORDS):
    groups, cur = [], []
    for w in words:
        if cur and (len(cur) == size or w["start"] - cur[-1]["end"] > 0.6):
            groups.append(cur)
            cur = []
        cur.append(w)
        if re.search(r"[.?!,;:]$", w["word"]):
            groups.append(cur)
            cur = []
    if cur:
        groups.append(cur)
    return groups


def spread_words(text, start, end):
    """Word timings for a spoken line: the words share [start, end] in proportion to their length,
    with a little extra time after punctuation, where the voice pauses."""
    words = text.split()
    weights = [len(re.sub(r"\W", "", w)) + 1.5 + (4 if re.search(r"[.?!]$", w) else 2.5 if re.search(r"[,;:]$", w) else 0)
               for w in words]
    scale = (end - start) / sum(weights)
    out, t = [], start
    for w, wt in zip(words, weights):
        out.append({"start": t, "end": t + wt * scale, "word": w})
        t += wt * scale
    return out


def write_ass(sh, words, popups, chapters, credits, length, path, extra):
    """extra: setup (start, end) of the setup card; narration [(start, end, text)] spoken by the host;
    bridges [(start, end, label)]; replay (start, end, rating)."""
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
        f"Style: Chap,{FONT},50,&H00000000,&H00000000,&H0000D4FF,&H00000000,0,0,0,0,100,100,1,0,3,10,0,7,50,50,{VIDEO_TOP + 24},1\n"
        # The host's added commentary: a dark box with white text and an amber current word, nothing
        # like the clip's own captions (big outlined text, yellow current word), plus a COMMENTARY tag.
        f"Style: NCap,{FONT},72,&H00FFFFFF,&H00FFFFFF,&H30301A10,&H00000000,0,0,0,0,100,100,1,0,3,18,0,2,90,90,400,1\n"
        f"Style: NTag,{FONT},36,&H00000000,&H00000000,&H0000D4FF,&H00000000,0,0,0,0,100,100,3,0,3,8,0,2,90,90,326,1\n"
        f"Style: Bridge,{FONT},150,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,0,0,0,0,100,100,2,0,1,9,4,5,80,80,0,1\n"
        f"Style: BridgeTag,{FONT},54,&H0000D4FF,&H0000D4FF,&H00000000,&H96000000,0,0,0,0,100,100,6,0,1,5,2,5,80,80,0,1\n"
        f"Style: Replay,{FONT},50,&H00FFFFFF,&H00FFFFFF,{RED},&H00000000,0,0,0,0,100,100,3,0,3,10,0,7,50,50,{VIDEO_TOP + 24},1\n"
        f"Style: Stamp,{FONT},64,&H00000000,&H00000000,&H0000D4FF,&H00000000,0,0,0,0,100,100,1,0,3,14,0,9,50,50,{VIDEO_TOP + 30},1\n\n"
        "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"
    )
    pop_in = "{\\fad(80,120)\\fscx82\\fscy82\\t(0,140,\\fscx100\\fscy100)}"
    ev = [f"Dialogue: 1,{ass_time(0)},{ass_time(length)},Hook,,0,0,0,,{clean(sh['hook_text'])}"]
    for a, b, name in credits:  # whose stream is on screen; it changes with the clip in a story Short
        ev.append(f"Dialogue: 1,{ass_time(a)},{ass_time(b)},Credit,,0,0,0,,{clean(name)} ON TWITCH")
    if sh.get("setup_text"):
        a, b = extra["setup"]
        ev.append(f"Dialogue: 3,{ass_time(a)},{ass_time(b)},Setup,,0,0,0,,{{\\fad(0,150)}}{clean(sh['setup_text'])}")
    a, b, rating = extra["replay"]
    ev.append(f"Dialogue: 2,{ass_time(a)},{ass_time(b)},Replay,,0,0,0,,REPLAY")
    if rating:
        ev.append(f"Dialogue: 2,{ass_time(a + 0.3)},{ass_time(b)},Stamp,,0,0,0,,"
                  f"{{\\fad(80,0)\\frz-4\\fscx140\\fscy140\\t(0,160,\\fscx100\\fscy100)}}{clean(rating)}")
    ta = max(b - TAKE_SECONDS, a)
    if sh.get("take_text") and b - ta >= 1.0:
        ev.append(f"Dialogue: 3,{ass_time(ta)},{ass_time(b)},Take,,0,0,0,,{pop_in}{clean(sh['take_text'])}")
    for a, b, label in extra["bridges"]:
        ev.append(f"Dialogue: 2,{ass_time(a)},{ass_time(b)},BridgeTag,,0,0,0,,{{\\an5\\pos({W // 2},{H // 2 - 130})}}UP NEXT")
        ev.append(f"Dialogue: 2,{ass_time(a)},{ass_time(b)},Bridge,,0,0,0,,"
                  f"{{\\an5\\pos({W // 2},{H // 2 + 20})\\fad(120,0)}}{clean(label)}")
    for a, b, label in chapters:
        ev.append(f"Dialogue: 2,{ass_time(a)},{ass_time(b)},Chap,,0,0,0,,{clean(label)}")
    for p in popups:
        ev.append(f"Dialogue: 2,{ass_time(p['at'])},{ass_time(min(p['at'] + p.get('dur', 2.5), length))},Pop,,0,0,0,,"
                  f"{pop_in}{clean(p['text'])}")
    emphasis = {norm(x) for e in sh.get("emphasis", []) for x in e.split()}
    groups = caption_groups(words)
    for n, g in enumerate(groups):
        # A line stays up briefly after its last word, but never into the next line (they'd stack).
        next_start = groups[n + 1][0]["start"] if n + 1 < len(groups) else length
        for k, w in enumerate(g):  # the spoken word lights up; emphasised words are red and bigger
            end = g[k + 1]["start"] if k + 1 < len(g) else min(w["end"] + 0.25, next_start)
            parts = []
            for j, x in enumerate(g):
                hot = norm(x["word"]) in emphasis
                colour = RED if hot else (YELLOW if j == k else WHITE)
                size = "\\fscx125\\fscy125" if hot and j == k else ""
                parts.append("{\\c" + colour + size + "}" + clean(x["word"]) + "{\\c" + WHITE + "\\fscx100\\fscy100}")
            ev.append(f"Dialogue: 0,{ass_time(w['start'])},{ass_time(min(end, length))},Cap,,0,0,{g[0]['mv']},,"
                      + " ".join(parts))
    for a, b, text in extra["narration"]:  # the host's lines, captioned in their own style
        ev.append(f"Dialogue: 4,{ass_time(a)},{ass_time(b)},NTag,,0,0,0,,COMMENTARY")
        ngroups = caption_groups(spread_words(text, a, b), NARR_CAPTION_WORDS)
        for n, g in enumerate(ngroups):
            group_end = ngroups[n + 1][0]["start"] if n + 1 < len(ngroups) else b
            for k, w in enumerate(g):
                end = g[k + 1]["start"] if k + 1 < len(g) else group_end
                parts = ["{\\c" + (AMBER if j == k else WHITE) + "}" + clean(x["word"]) for j, x in enumerate(g)]
                ev.append(f"Dialogue: 4,{ass_time(w['start'])},{ass_time(end)},NCap,,0,0,0,," + " ".join(parts))
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


def geometry(seg, defaults):
    """A clip's framing: (mode, zoom, (focus_x, focus_y), (cut_top, cut_bottom))."""
    return (seg.get("crop", "4:3"), float(seg.get("zoom", 1.0)),
            (seg.get("focus_x", 0.5), seg.get("focus_y", 0.5)),
            (seg.get("cut_top", defaults.get("cut_top", 0)), seg.get("cut_bottom", defaults.get("cut_bottom", 0))))


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


def render_segment(seg, defaults, dst, fps):
    """One clip → a 1080x1920 piece with reframing and punch-ins, no text yet, with the clip's own
    audio at full level. Returns (start, length)."""
    clip = Path(seg["work"]) / "clip.mp4"
    info = probe(clip)
    start = float(seg.get("start", 0))
    length = min(float(seg.get("end", info["seconds"])), info["seconds"]) - start
    if length < 1:
        sys.exit(f"{seg['work']}: end must be at least 1 s after start (clip is {info['seconds']:.1f} s)")
    mode, zoom, where, cuts = geometry(seg, defaults)
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
        graph += f";[b]{BG}[bg];[bg][fg]overlay=(W-w)/2:{VIDEO_TOP}[v]"
    else:
        graph += ";[fg]null[v]"
    graph += ";[0:a]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]"
    run(["-ss", f"{start:.3f}", "-t", f"{length:.3f}", "-i", str(clip), "-filter_complex", graph,
         "-map", "[v]", "-map", "[a]", "-t", f"{length:.3f}", *X264, str(dst)])
    return start, length


def render_host(seg, defaults, fps, dst, voice, dur, src_from, src_to, stretch=1.0, zoom_mult=1.0,
                focus=None, still=False):
    """A host piece: footage from a clip with NO clip audio, the narration wav `voice` under it.
    The footage runs from src_from to src_to (clip seconds) stretched `stretch` times (2 = half
    speed), then its last frame is held, or it is cut, so the piece lasts exactly `dur`.
    `still` freezes the frame at src_from, darkened and blurred, for a bridge card."""
    clip = Path(seg["work"]) / "clip.mp4"
    mode, zoom, where, cuts = geometry(seg, defaults)
    where = focus or where
    zoom *= zoom_mult
    if mode != "vertical":
        layout = (f"[s]split=2[f][b];[f]{crop_filter(mode, *where, zoom, *cuts)}[fg];[b]{BG}[bg];"
                  f"[bg][fg]overlay=(W-w)/2:{VIDEO_TOP}[v0];")
    else:
        layout = f"[s]{crop_filter(mode, *where, zoom, *cuts)}[v0];"
    audio = f"[1:a]aformat=sample_rates=48000:channel_layouts=stereo,apad=whole_dur={dur:.3f},atrim=duration={dur:.3f}[a]"
    if still:  # one frame is composed, then repeated: filtering 100 identical frames would be slow
        png = Path(str(dst) + ".png")
        run(["-ss", f"{src_from:.3f}", "-t", "0.5", "-i", str(clip), "-filter_complex",
             "[0:v]trim=end_frame=1,setpts=PTS-STARTPTS[s];" + layout + "[v0]normalize=strength=0.6,boxblur=14:3,eq=gamma=1.5:brightness=-0.05:saturation=0.9[v]",
             "-map", "[v]", "-frames:v", "1", str(png)])
        run(["-loop", "1", "-framerate", str(fps), "-i", str(png), "-i", str(voice), "-filter_complex", audio,
             "-map", "0:v", "-map", "[a]", "-t", f"{dur:.3f}", *X264, str(dst)])
        png.unlink()
        return
    graph = (f"[0:v]setpts=PTS-STARTPTS,setpts={stretch:.5f}*PTS,fps={fps},"  # fps= repeats frames: no blended ghosts
             f"tpad=stop_mode=clone:stop_duration={dur:.3f},trim=duration={dur:.3f},setpts=PTS-STARTPTS[s];"
             + layout + "[v0]null[v];" + audio)
    run(["-ss", f"{src_from:.3f}", "-t", f"{src_to - src_from:.3f}", "-i", str(clip), "-i", str(voice),
         "-filter_complex", graph, "-map", "[v]", "-map", "[a]", "-t", f"{dur:.3f}", *X264, str(dst)])


def fail(msg):
    sys.exit(f"error: {msg}")


def check_plan(sh, segments, lengths):
    """Validate the narration plan (format, narration, teaser, replay) before any work is done.
    Returns (format, narration, teaser, replay)."""
    fmt = sh.get("format")
    if fmt not in FORMATS:
        fail(f'"format" must be one of {", ".join(FORMATS)} (got {fmt!r})')
    n = len(segments)
    if fmt == "breakdown" and n != 1:
        fail('format "breakdown" is one clip; use "story" or "ranked" for several')
    if fmt != "breakdown" and not 2 <= n <= 3:
        fail(f'format "{fmt}" needs 2-3 clips in "segments" (got {n}); use "breakdown" for one clip')
    nar = sh.get("narration")
    if not isinstance(nar, dict):
        fail('"narration" is missing: every Short needs {"hook": ..., "bridges": [...], "take": ...}')
    for key in ("hook", "take"):
        if not str(nar.get(key) or "").strip():
            fail(f"narration.{key} is missing or empty: every Short is rendered with spoken commentary")
    bridges = nar.get("bridges") or []
    if not isinstance(bridges, list) or len(bridges) != n - 1 or not all(str(b).strip() for b in bridges):
        fail(f"narration.bridges needs exactly {n - 1} non-empty line(s) for {n} clip(s), one per card between clips")
    if n > 1 and any(not str(s.get("label") or "").strip() for s in segments):
        fail('every clip of a story/ranked Short needs a "label" (it is shown large on the card before the clip)')
    spans = {}
    for name, rng in (("teaser", TEASER_RANGE), ("replay", REPLAY_RANGE)):
        sp = sh.get(name)
        if not isinstance(sp, dict):
            fail(f'"{name}" is missing: {{"segment": 0, "from": s, "to": s}}')
        try:
            idx, a, b = int(sp.get("segment", 0)), float(sp["from"]), float(sp["to"])
        except (KeyError, TypeError, ValueError):
            fail(f'"{name}" needs "segment", "from" and "to" (numbers; seconds in that clip)')
        if not 0 <= idx < n:
            fail(f"{name}.segment is {idx}, but there are {n} clip(s) (0-based)")
        if not 0 <= a < b <= lengths[idx] + 0.05:
            fail(f"{name}: from/to must satisfy 0 <= from < to <= {lengths[idx]:.1f} (the clip's length)")
        if not rng[0] - 0.05 <= b - a <= rng[1] + 0.05:
            fail(f"{name} must cover {rng[0]}-{rng[1]} s of the clip (got {b - a:.2f} s)")
        spans[name] = {**sp, "segment": idx, "from": a, "to": b}
    rp = spans["replay"]
    rp["speed"] = min(max(float(rp.get("speed", 0.5)), 0.25), 1.0)
    rp["zoom"] = min(max(float(rp.get("zoom", 1.25)), 1.0), 2.0)
    if len(str(sh.get("rating") or "")) > 16:
        fail('"rating" must be 16 characters or fewer')
    for key, text in [("hook", nar["hook"]), ("take", nar["take"])] + [("bridge", b) for b in bridges]:
        lo, hi = NARRATION_WORDS[key]
        if not lo <= len(str(text).split()) <= hi:
            print(f"warning: narration {key} has {len(str(text).split())} words (aim for {lo}-{hi}): {text!r}",
                  file=sys.stderr)
    return fmt, nar, spans["teaser"], rp


def synthesize(nar, folder):
    """Speak every narration line. Fails the whole render when speech can't be made: a Short is
    never rendered silently. Returns {key: (wav, seconds, text)} for hook, bridge0.., take."""
    try:
        import tts
        jobs = [("hook", nar["hook"])] + [(f"bridge{i}", b) for i, b in enumerate(nar.get("bridges") or [])] \
            + [("take", nar["take"])]
        out = {}
        for key, text in jobs:
            wav = folder / f"voice_{key}.wav"
            out[key] = (wav, tts.speak(str(text), wav), str(text).strip())
        return out
    except Exception as e:  # TTSError, a missing package, a failed download: all the same to the caller
        shutil.rmtree(folder, ignore_errors=True)
        sys.exit(f"error: cannot make the narration voice, so no Short is rendered ({type(e).__name__}: {e})")


def render(short, work, out):
    sh = json.loads(Path(short).read_text(encoding="utf-8"))
    config = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
    defaults = config.get("crop_defaults", {})
    segments = sh.get("segments") or [{**sh, "work": work}]
    if any(not s.get("work") for s in segments):
        sys.exit("every clip needs its prep folder: --work for one clip, or \"work\" in each segment")
    for seg in segments:
        seg.setdefault("streamer", sh.get("streamer"))
    if any(not str(s.get("streamer") or "").strip() for s in segments):
        sys.exit('every clip needs "streamer" (the name find_clips printed), so the Short credits its source')
    infos = [probe(Path(s["work"]) / "clip.mp4") for s in segments]
    fmt, nar, teaser, replay = check_plan(sh, segments, [i["seconds"] for i in infos])
    fps = min(min(round(i["fps"]) for i in infos), 60)
    out = Path(out)
    parts_dir = Path(str(out) + ".parts")
    parts_dir.mkdir(parents=True, exist_ok=True)
    voice = synthesize(nar, parts_dir)  # first, so a missing voice costs nothing else
    vsec = lambda key: voice[key][1]

    t0, words, popups, chapters, credits, parts = 0.0, [], [], [], [], []
    host, bridge_cards, timeline = [], [], []  # host: (start, end, text) of each spoken line

    def add(kind, path, dur, name, speech=None):
        """Append a piece to the timeline at t0; `speech` is the voice key it carries, if any."""
        nonlocal t0
        if credits and credits[-1][2] == name and abs(credits[-1][1] - t0) < 1e-6:  # same streamer: one credit
            credits[-1] = (credits[-1][0], t0 + dur, name)
        else:
            credits.append((t0, t0 + dur, name))
        if speech:
            host.append((t0, t0 + vsec(speech), voice[speech][2]))
        timeline.append({"kind": kind, "start": round(t0, 3), "end": round(t0 + dur, 3),
                         "narration": bool(speech), "streamer": name})
        parts.append(path)
        t0 += dur

    # 1. teaser, with the hook voice
    seg = segments[teaser["segment"]]
    dur = vsec("hook") + TEASER_TAIL
    part = parts_dir / "teaser.mp4"
    render_host(seg, defaults, fps, part, voice["hook"][0], dur, teaser["from"], teaser["to"],
                stretch=min(max(dur / (teaser["to"] - teaser["from"]), 1.0), MAX_SLOWDOWN))
    add("teaser", part, dur, seg["streamer"], "hook")

    # 2. the clips, each after a bridge card (except the first), with their own audio untouched
    setup = None
    for k, seg in enumerate(segments):
        if k:
            key = f"bridge{k - 1}"
            dur = vsec(key) + BRIDGE_TAIL
            part = parts_dir / f"bridge{k}.mp4"
            first = float(seg.get("start", 0))
            render_host(seg, defaults, fps, part, voice[key][0], dur, first, first, still=True)
            bridge_cards.append((t0, t0 + dur, seg["label"]))
            add("bridge", part, dur, seg["streamer"], key)
        part = parts_dir / f"seg{k}.mp4"
        start, length = render_segment(seg, defaults, part, fps)
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
        if setup is None:
            setup = (t0, t0 + min(SETUP_SECONDS, length))
        add("clip", part, length, seg["streamer"])

    # 3. replay, with the take voice
    seg = segments[replay["segment"]]
    dur = vsec("take") + REPLAY_TAIL
    shown = (replay["to"] - replay["from"]) / replay["speed"]
    if shown > dur + 0.75:
        print(f"warning: the slowed replay lasts {shown:.1f} s but the take voice only {dur:.1f} s, so the end of "
              f"the replay is cut off; shorten the replay range or lengthen narration.take", file=sys.stderr)
    focus = (replay.get("focus_x", seg.get("focus_x", 0.5)), replay.get("focus_y", seg.get("focus_y", 0.5)))
    part = parts_dir / "replay.mp4"
    render_host(seg, defaults, fps, part, voice["take"][0], dur, replay["from"], replay["to"],
                stretch=1 / replay["speed"], zoom_mult=replay["zoom"], focus=focus)
    replay_at = t0
    add("replay", part, dur, seg["streamer"], "take")

    total = t0
    if total > 180:
        sys.exit("a Short must be 3 minutes or less")

    ass = parts_dir / "short.ass"
    write_ass(sh, words, popups, chapters, credits, total, ass,
              {"setup": setup, "narration": host, "bridges": bridge_cards,
               "replay": (replay_at, total, str(sh.get("rating") or "").strip())})
    inputs = [x for p in parts for x in ("-i", str(p))]
    n = len(parts)
    graph = ("".join(f"[{k}:v][{k}:a]" for k in range(n)) + f"concat=n={n}:v=1:a=1[cv][ca];"
             f"[cv]ass={fpath(ass)}:fontsdir={fpath(FONTS)}[tx];color=c={BAR}:s={W}x12:r={fps}[bar];"
             f"[tx][bar]overlay=x='-w+w*t/{total:.3f}':y=0:shortest=1,format=yuv420p[v];"
             # Short fades so the loop back to the start doesn't click.
             f"[ca]afade=t=in:d=0.08,afade=t=out:st={max(total - 0.15, 0):.3f}:d=0.15[a]")
    out.parent.mkdir(parents=True, exist_ok=True)
    run([*inputs, "-filter_complex", graph, "-map", "[v]", "-map", "[a]", "-t", f"{total:.3f}",
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-c:a", "aac", "-b:a", "192k", "-ac", "2",
         "-movflags", "+faststart", str(out)])
    shutil.rmtree(parts_dir)
    final = probe(out)
    spoken = sum(v[1] for v in voice.values())
    import tts
    from upload import narration_hash
    side = {"video": out.name, "video_bytes": out.stat().st_size, "format": fmt, "clips": len(segments),
            "total_seconds": round(final["seconds"], 2), "narration_seconds": round(spoken, 2),
            "narration_share": round(spoken / final["seconds"], 3),
            "narration": nar, "narration_hash": narration_hash(sh["narration"]),
            "voice": tts.describe(), "timeline": timeline}
    Path(str(out) + ".json").write_text(json.dumps(side, indent=1, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"short": str(out), "seconds": round(final["seconds"], 1), "format": fmt, "clips": len(segments),
                      "size": f"{final['width']}x{final['height']}", "fps": fps, "caption_words": len(words),
                      "narration_seconds": side["narration_seconds"], "narration_share": side["narration_share"],
                      "punch_ins": "auto" if not any("punch_ins" in s for s in segments) else "set"}))


def frames(video, out=None):
    """Check frames for a rendered Short, from the sidecar's timeline: the middle of every piece
    (teaser, clips, bridge cards, replay), 0.8 s into the first clip (the setup card) and 1 s before
    the end (the take card). Prints the jpg paths, one per line."""
    video = Path(video)
    side = json.loads(Path(str(video) + ".json").read_text(encoding="utf-8"))
    out = Path(out) if out else video.with_name(video.name + ".frames")
    out.mkdir(parents=True, exist_ok=True)
    picks, firsts = [], True
    for k, item in enumerate(side["timeline"]):
        picks.append((f"{k}-{item['kind']}", (item["start"] + item["end"]) / 2))
        if item["kind"] == "clip" and firsts:
            picks.append((f"{k}-setup", item["start"] + 0.8))
            firsts = False
    picks.append(("end", side["total_seconds"] - 1.0))
    for name, t in picks:
        f = out / f"{name}.jpg"
        run(["-ss", f"{t:.2f}", "-i", str(video), "-frames:v", "1", "-vf", "scale=540:-2", str(f)])
        print(f"{t:6.1f}s  {f}")


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
    a3 = sub.add_parser("frames")
    a3.add_argument("video")
    a3.add_argument("--out", help="folder for the jpgs (default: VIDEO.frames)")
    a = p.parse_args()
    if a.cmd == "prep":
        prep(a.url, a.out)
    elif a.cmd == "render":
        render(a.short, a.work, a.out)
    else:
        frames(a.video, a.out)
