#!/usr/bin/env python3
"""Build a Scribble Age video from an episode JSON file, using only free tools.

Episode JSON:
{
  "title": "...", "description": "...", "tags": ["..."],
  "thumbnail_svg": "<svg width='1280' height='720' ...>",
  "scenes": [{"narration": "...", "shots": [{"svg": "<svg width='1920' height='1080' ...>"},
                                             {"add": "<g>...drawn on top of the previous shot...</g>"}]}]
}

Output (in --out): video.mp4, thumbnail.jpg, captions.ass
Voice: Microsoft Edge neural TTS (free, via edge-tts). Pictures: SVG doodles
rendered with cairosvg. Assembly and captions: ffmpeg (imageio-ffmpeg build).
"""
import argparse, asyncio, json, os, re, shutil, ssl, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import cairosvg
import edge_tts
import edge_tts.communicate as ec
import imageio_ffmpeg
from PIL import Image, ImageChops

import sound

HERE = Path(__file__).resolve().parent
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
VOICE = "en-US-AndrewNeural"
FPS = 30
W, H = 1920, 1080
FONT_NAME = "Patrick Hand"
WORDS_PER_CAPTION = 3
SCENE_TAIL = 0.35  # seconds of silence after each scene
POP_IN = 0.22     # seconds for a pop-in element to fade and rise into place
POP_RISE = 36     # pixels (at 2x render scale) a pop-in rises while appearing

# The cloud sandbox re-terminates TLS; edge-tts pins certifi, so trust the proxy CA when present.
CA = "/root/.ccr/ca-bundle.crt"
if os.path.exists(CA):
    ec._SSL_CTX = ssl.create_default_context(cafile=CA)


def install_font():
    fonts = Path.home() / ".fonts"
    fonts.mkdir(exist_ok=True)
    dst = fonts / "PatrickHand-Regular.ttf"
    if not dst.exists():
        shutil.copy(HERE / "assets" / "PatrickHand-Regular.ttf", dst)
        subprocess.run(["fc-cache", "-f"], capture_output=True)
    return fonts


def run(args):
    r = subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", *args], capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"ffmpeg failed: {r.stderr[-2000:]}")


def duration(path):
    r = subprocess.run([FFMPEG, "-hide_banner", "-i", str(path)], capture_output=True, text=True)
    h, m, s = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr).groups()
    return int(h) * 3600 + int(m) * 60 + float(s)


async def tts(text, mp3):
    words = []
    comm = edge_tts.Communicate(text, VOICE, rate="+5%", boundary="WordBoundary")
    with open(mp3, "wb") as f:
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                words.append((chunk["offset"] / 1e7, (chunk["offset"] + chunk["duration"]) / 1e7, chunk["text"]))
    return words


def tts_retry(text, mp3, attempts=4):
    # The free Edge TTS endpoint drops requests now and then; retry before failing the build.
    for i in range(attempts):
        try:
            return asyncio.run(tts(text, mp3))
        except Exception as e:
            if i == attempts - 1:
                raise
            print(f"tts retry {i + 1}: {e}", flush=True)
            time.sleep(2 * (i + 1))


def ass_time(t):
    cs = int(round(t * 100))
    return f"{cs // 360000}:{cs // 6000 % 60:02d}:{cs // 100 % 60:02d}.{cs % 100:02d}"


def write_ass(captions, path, style="Cap", res=(1920, 1080)):
    head = (
        f"[Script Info]\nScriptType: v4.00+\nPlayResX: {res[0]}\nPlayResY: {res[1]}\nWrapStyle: 2\n\n"
        "[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, "
        "Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, "
        "Alignment, MarginL, MarginR, MarginV, Encoding\n"
        # Karaoke: each word turns amber (PrimaryColour, ASS is BGR) as it's spoken, from white (SecondaryColour).
        f"Style: Cap,{FONT_NAME},110,&H001EA2F6,&H00FFFFFF,&H00000000,&H64000000,0,0,0,0,100,100,0,0,1,6,3,2,80,80,60,1\n"
        f"Style: Short,{FONT_NAME},92,&H001EA2F6,&H00FFFFFF,&H00000000,&H64000000,0,0,0,0,100,100,0,0,1,6,3,2,60,60,470,1\n\n"
        "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"
    )
    lines = [f"Dialogue: 0,{ass_time(a)},{ass_time(b)},{style},,0,0,0,,{t}" for a, b, t in captions]
    Path(path).write_text(head + "\n".join(lines) + "\n", encoding="utf-8")


_GRAIN = {}


def paper_grain(w, h):
    """Soft paper texture, multiplied over every picture so frames feel drawn on paper."""
    if (w, h) not in _GRAIN:
        g = Image.effect_noise((w // 4, h // 4), 28).resize((w, h), Image.BICUBIC)
        grain = g.point(lambda v: 235 + v * 20 // 255)
        # Storybook vignette: corners fall off gently toward warm shadow.
        vig = Image.radial_gradient("L").resize((w, h)).point(lambda v: 255 - max(0, v - 150) * 70 // 105)
        tone = ImageChops.multiply(grain, vig)
        _GRAIN[(w, h)] = Image.merge("RGB", [tone, tone, tone.point(lambda v: v * 245 // 255)])
    return _GRAIN[(w, h)]


def svg_to_png(svg, png, w, h, grain=True):
    cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=str(png), output_width=w, output_height=h,
                     background_color="white")
    if grain:
        img = Image.open(png).convert("RGB")
        ImageChops.multiply(img, paper_grain(w, h)).save(png)


def shot_svgs(sc):
    """Final picture of each shot (including its pops), for review. A scene is one picture ("svg") or
    several ("shots"). A shot is {"svg": full SVG} or {"add": SVG elements} (drawn on top of the previous
    shot), and either kind may carry "pops": elements that animate in one after another."""
    if "shots" not in sc:
        return [sc["svg"]]
    svgs = []
    for shot in sc["shots"]:
        base = shot["svg"] if "svg" in shot else _inject(svgs[-1], shot["add"])
        for frag in shot.get("pops", []):
            base = _inject(base, frag)
        svgs.append(base)
    return svgs


def _inject(svg, fragment):
    cut = svg.rindex("</svg>")
    return svg[:cut] + fragment + svg[cut:]


def plan_segments(sc):
    """Group a scene's shots into segments: each full "svg" starts a segment (a new picture and camera
    move); "add" shots and "pops" become animated pop-ins inside the current segment."""
    shots = sc.get("shots") or [{"svg": sc["svg"]}]
    segs = []
    for si, shot in enumerate(shots):
        if "svg" in shot:
            segs.append({"base": shot["svg"], "first_shot": si, "pops": []})
        else:
            segs[-1]["pops"].append({"frag": shot["add"], "shot": si, "j": -1, "n": 0})
        pops = shot.get("pops", [])
        for j, frag in enumerate(pops):
            segs[-1]["pops"].append({"frag": frag, "shot": si, "j": j, "n": len(pops)})
    return segs


def pop_times(seg_pops, cuts, words):
    """When each pop appears: an "add" lands on its cut; pops spread evenly across their shot,
    snapped to the start of a spoken word."""
    starts = [w[0] for w in words]
    out = []
    for p in seg_pops:
        a, b = cuts[p["shot"]], cuts[p["shot"] + 1]
        if p["j"] < 0:
            t = a
        else:
            # The first pop lands fast (so a backdrop never sits empty); the rest spread across the shot.
            lead = 0.35 if any(q["j"] < 0 and q["shot"] == p["shot"] for q in seg_pops) else 0.0
            first = a + lead + min(0.6, (b - a) * 0.15)
            t = first if p["j"] == 0 else first + (b - 0.5 - first) * p["j"] / p["n"]
            near = [w for w in starts if a < w < b - 0.4]
            if near:
                t = min(near, key=lambda w: abs(w - t))
        out.append(t)
    return out


def render_pop(fragment, png, w, h):
    """Render SVG elements alone on a transparent canvas, crop to their bounds, return the offset."""
    doc = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{fragment}</svg>'
    cairosvg.svg2png(bytestring=doc.encode("utf-8"), write_to=str(png), output_width=w, output_height=h)
    img = Image.open(png).convert("RGBA")
    box = img.getchannel("A").getbbox()
    if not box:
        return None
    x0, y0 = max(0, box[0] - 8), max(0, box[1] - 8)
    crop = img.crop((x0, y0, min(w, box[2] + 8), min(h, box[3] + 8)))
    rgb = ImageChops.multiply(crop.convert("RGB"), paper_grain(w, h).crop((x0, y0, x0 + crop.width, y0 + crop.height)))
    rgb.putalpha(crop.getchannel("A"))
    rgb.save(png)
    return x0, y0


def shot_cuts(words, total, n):
    """Split a scene into n shots at word boundaries, so each picture changes on a spoken word."""
    even = [total * k / n for k in range(n + 1)]
    if n == 1 or len(words) < n:
        return even
    cuts = [0.0] + [words[round(k * len(words) / n)][0] for k in range(1, n)] + [total]
    if any(b - a < 0.8 for a, b in zip(cuts, cuts[1:])):
        return even
    return cuts


MOTIONS = [  # zoompan expressions; cycling them keeps each new picture moving differently
    "zoompan=z='1+0.08*on/{f}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'",
    "zoompan=z='1.08-0.08*on/{f}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'",
    "zoompan=z='1.08':x='(iw-iw/zoom)*on/{f}':y='ih/2-(ih/zoom/2)'",
    "zoompan=z='1.08':x='(iw-iw/zoom)*(1-on/{f})':y='ih/2-(ih/zoom/2)'",
]


def motion(idx, frames):
    return MOTIONS[idx % len(MOTIONS)].format(f=frames)


OUTRO = 4.0  # seconds of end card after the last scene
# Narration on top; music ducks under the voice (sidechain) and swells in pauses; effects sit between.
AUDIO_MIX = ("[0:a]asplit=2[n1][n2];[1:a]volume=0.20[m];"
             "[m][n1]sidechaincompress=threshold=0.02:ratio=9:attack=20:release=450[md];"
             "[2:a]volume=0.55[fx];[n2][md][fx]amix=inputs=3:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=44100[a]")


def build_outro(work):
    """End card: the mascot waves and a subscribe button pops in (no narration, the music plays out)."""
    import doodle as d
    d.seed(99)
    base = d.scene(d.speed_lines(960, 460, "#FFD37A", d.AMBER), d.mascot(1350, 930, 1.25, expression="happy", pose="wave"))
    card = d.fit_text(640, 330, "NEW STORY", 1000, 170, outline="#fff", outline_width=20) + \
        d.fit_text(640, 500, "EVERY DAY", 1000, 170, fill="#B5482A", outline="#fff", outline_width=20)
    button = d.rect(360, 590, 560, 140, "#E4572E", width=9) + d.text(640, 690, "SUBSCRIBE", 100, fill="#fff")
    png, frames = work / "outro.png", int(OUTRO * FPS)
    svg_to_png(base, png, W * 2, H * 2)
    inputs = ["-loop", "1", "-framerate", str(FPS), "-t", f"{OUTRO}", "-i", str(png)]
    chain, last = [], "0:v"
    for k, (frag, lt) in enumerate(((card, 0.5), (button, 1.3)), start=1):
        pp = work / f"outro_p{k}.png"
        off = render_pop(frag, pp, W * 2, H * 2)
        inputs += ["-loop", "1", "-framerate", str(FPS), "-t", f"{OUTRO}", "-i", str(pp)]
        chain.append(f"[{k}:v]format=rgba,fade=in:st={lt}:d={POP_IN}:alpha=1[p{k}]")
        chain.append(f"[{last}][p{k}]overlay=x={off[0]}:y='{off[1]}+{POP_RISE}*max(0\\,1-(t-{lt})/{POP_IN})':eval=frame:format=yuv420[b{k}]")
        last = f"b{k}"
    chain.append(f"[{last}]{motion(1, frames)}:d=1:s={W}x{H}:fps={FPS},setsar=1,format=yuv420p[v]")
    mp4 = work / "outro.mp4"
    run([*inputs, "-f", "lavfi", "-t", f"{OUTRO}", "-i", "anullsrc=r=44100:cl=stereo", "-filter_complex", ";".join(chain),
         "-map", "[v]", "-map", f"{len(inputs) // 8}:a", "-frames:v", str(frames), "-c:v", "libx264", "-preset", "ultrafast",
         "-crf", "16", "-c:a", "aac", "-b:a", "160k", "-ac", "2", str(mp4)])
    return mp4


SHORT_MAX = 58.0


def build_short(ep, work, out, scenes_meta, captions, fonts_dir, pop_at, whoosh_at):
    """Vertical 1080x1920 YouTube Short from the video's opening scenes (the hook), ending on a card that
    points to the full story. Returns its length, or 0 if the opening is too short."""
    import doodle as d
    t, n = 0.0, 0
    for _, _, dur, _, _ in scenes_meta:
        if t + dur > SHORT_MAX - 3:
            break
        t += dur
        n += 1
    if t < 20:
        return 0
    end_card = 3.0
    total = t + end_card
    title = ep.get("short_title") or ep["title"]
    top = (f'<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">'
           f'<rect width="1080" height="1920" fill="{d.CREAM}"/>' + d.speed_lines(540, 1900, "#FBE3B0", d.CREAM) +
           d.rect(40, 150, 1000, 330, "#fff", width=9) + d.fit_text(540, 290, title.upper()[:40], 920, 96) +
           (d.fit_text(540, 410, title.upper()[40:80], 920, 96) if len(title) > 40 else "") +
           d.text(540, 1830, "SCRIBBLE AGE", 70, fill="#B5482A") + "</svg>")
    bg = work / "short_bg.png"
    cairosvg.svg2png(bytestring=top.encode(), write_to=str(bg), output_width=1080, output_height=1920)
    card = d.thumbnail(d.speed_lines(960, 540, "#FFD37A", d.AMBER), d.mascot(1450, 1000, 1.2, expression="happy", pose="point"),
                       d.fit_text(640, 430, "FULL STORY", 1100, 190, outline="#fff", outline_width=20),
                       d.fit_text(640, 640, "ON THE CHANNEL", 1100, 150, fill="#B5482A", outline="#fff", outline_width=20))
    cardpng = work / "short_card.png"
    cairosvg.svg2png(bytestring=card.encode(), write_to=str(cardpng), output_width=1920, output_height=1080)
    write_ass([c for c in captions if c[0] < t], work / "short.ass", style="Short", res=(1080, 1920))
    sound.write_wav(work / "short_music.wav", sound.music_bed(total))
    sound.write_wav(work / "short_sfx.wav", sound.effects_track(total, [p for p in pop_at if p < t] + [t + 0.3],
                                                              [w for w in whoosh_at if w < t] + [t - 0.08]))
    norm = f"scale=1080:608,setsar=1,fps={FPS},format=yuv420p"
    graph = (f"[0:v]trim=0:{t:.3f},setpts=PTS-STARTPTS,{norm}[main];"
             f"[3:v]{norm},trim=0:{end_card},setpts=PTS-STARTPTS[endv];[main][endv]concat=n=2:v=1:a=0[clip];"
             f"[1:v]setsar=1,format=yuv420p[bg];[bg][clip]overlay=0:620:shortest=1,ass={work / 'short.ass'}:fontsdir={fonts_dir},format=yuv420p[v];"
             f"[0:a]atrim=0:{t:.3f},asetpts=PTS-STARTPTS,apad=pad_dur={end_card}[nar];"
             "[nar]asplit=2[n1][n2];[4:a]volume=0.20[m];[m][n1]sidechaincompress=threshold=0.02:ratio=9:attack=20:release=450[md];"
             "[5:a]volume=0.55[fx];[n2][md][fx]amix=inputs=3:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=44100[a]")
    run(["-i", str(work / "joined.mp4"), "-loop", "1", "-framerate", str(FPS), "-t", f"{total:.3f}", "-i", str(bg),
         "-f", "lavfi", "-t", "1", "-i", "anullsrc", "-loop", "1", "-framerate", str(FPS), "-t", f"{end_card}", "-i", str(cardpng),
         "-i", str(work / "short_music.wav"), "-i", str(work / "short_sfx.wav"),
         "-filter_complex", graph, "-map", "[v]", "-map", "[a]", "-t", f"{total:.3f}", "-r", str(FPS),
         "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart",
         str(out / "short.mp4")])
    return round(total, 1)


def build(episode_path, out):
    ep = json.loads(Path(episode_path).read_text(encoding="utf-8"))
    out = Path(out)
    work = out / "work"
    work.mkdir(parents=True, exist_ok=True)
    fonts_dir = install_font()

    # Pass 1 (sequential): voice every scene and render every picture; queue the video work.
    scenes_meta, seg_jobs, shots_total, beats_total = [], [], 0, 0
    scene_t0, pop_at, whoosh_at, chapters = 0.0, [], [], []
    for i, sc in enumerate(ep["scenes"]):
        mp3, mp4 = work / f"s{i:03d}.mp3", work / f"s{i:03d}.mp4"
        words = tts_retry(sc["narration"], mp3)
        d = duration(mp3) + SCENE_TAIL
        segs = plan_segments(sc)
        n_shots = len(sc.get("shots") or [1])
        cuts = shot_cuts(words, d, n_shots)
        bounds = [cuts[g["first_shot"]] for g in segs] + [d]
        seg_files = []
        for g, seg in enumerate(segs):
            seg_d = bounds[g + 1] - bounds[g]
            frames = max(1, int(round(seg_d * FPS)))
            base = work / f"s{i:03d}_{g}.png"
            svg_to_png(seg["base"], base, W * 2, H * 2)
            inputs = ["-loop", "1", "-framerate", str(FPS), "-t", f"{seg_d:.3f}", "-i", str(base)]
            chain, last, k = [], "0:v", 0
            if scene_t0 + bounds[g] > 0.05:
                whoosh_at.append(scene_t0 + bounds[g] - 0.08)
            for p, t in zip(seg["pops"], pop_times(seg["pops"], cuts, words)):
                png = work / f"s{i:03d}_{g}_p{k}.png"
                off = render_pop(p["frag"], png, W * 2, H * 2)
                if off is None:
                    continue
                k += 1
                lt = max(0.0, t - bounds[g])
                pop_at.append(scene_t0 + bounds[g] + lt)
                inputs += ["-loop", "1", "-framerate", str(FPS), "-t", f"{seg_d:.3f}", "-i", str(png)]
                chain.append(f"[{k}:v]format=rgba,fade=in:st={lt:.3f}:d={POP_IN}:alpha=1[p{k}]")
                chain.append(f"[{last}][p{k}]overlay=x={off[0]}:y='{off[1]}+{POP_RISE}*max(0\\,1-(t-{lt:.3f})/{POP_IN})'"
                             f":eval=frame:format=yuv420[b{k}]")
                last = f"b{k}"
            chain.append(f"[{last}]{motion(shots_total + g, frames)}:d=1:s={W}x{H}:fps={FPS},setsar=1,format=yuv420p[v]")
            seg_mp4 = work / f"s{i:03d}_{g}.mp4"
            seg_jobs.append([*inputs, "-filter_complex", ";".join(chain), "-map", "[v]", "-frames:v", str(frames),
                             "-c:v", "libx264", "-preset", "ultrafast", "-crf", "16", str(seg_mp4)])
            seg_files.append(seg_mp4)
            beats_total += 1 + k
        shots_total += len(segs)
        if sc.get("chapter"):
            chapters.append((scene_t0, sc["chapter"]))
        scene_t0 += d
        scenes_meta.append((mp3, mp4, d, words, seg_files))
        print(f"scene {i + 1}/{len(ep['scenes'])}: {d:.1f}s, {len(segs)} pictures", flush=True)

    # Pass 2 (parallel): animate every segment, then join each scene with its voice.
    with ThreadPoolExecutor(max_workers=max(1, min(4, os.cpu_count() or 1) - 1)) as pool:
        list(pool.map(run, seg_jobs))
        joins = []
        for mp3, mp4, d, _, seg_files in scenes_meta:
            n = len(seg_files)
            graph = "".join(f"[{k}:v]" for k in range(n)) + \
                f"concat=n={n}:v=1:a=0[v];[{n}:a]apad=pad_dur={SCENE_TAIL},aresample=44100[a]"
            joins.append([*sum((["-i", str(f)] for f in seg_files), []), "-i", str(mp3), "-filter_complex", graph,
                          "-map", "[v]", "-map", "[a]", "-t", f"{d:.3f}", "-c:v", "libx264", "-preset", "ultrafast",
                          "-crf", "16", "-c:a", "aac", "-b:a", "160k", "-ac", "2", str(mp4)])
        list(pool.map(run, joins))

    clips, captions, t0 = [], [], 0.0
    for mp3, mp4, d, words, _ in scenes_meta:
        clips.append(mp4)
        for j in range(0, len(words), WORDS_PER_CAPTION):
            grp = words[j:j + WORDS_PER_CAPTION]
            end = words[j + WORDS_PER_CAPTION][0] if j + WORDS_PER_CAPTION < len(words) else grp[-1][1] + 0.2
            parts = []
            for q, w in enumerate(grp):
                nxt = grp[q + 1][0] if q + 1 < len(grp) else w[1]
                parts.append("{\\k%d}%s" % (max(1, round((nxt - w[0]) * 100)), w[2].replace("{", "(").replace("}", ")")))
            captions.append((t0 + grp[0][0], t0 + end, " ".join(parts)))
        t0 += duration(mp4)

    outro = build_outro(work)
    whoosh_at.append(t0 - 0.08)
    pop_at += [t0 + 0.5, t0 + 1.3]
    clips.append(outro)
    total_len = t0 + OUTRO

    (work / "list.txt").write_text("".join(f"file '{c.name}'\n" for c in clips))
    run(["-f", "concat", "-safe", "0", "-i", str(work / "list.txt"), "-c", "copy", str(work / "joined.mp4")])
    write_ass(captions, out / "captions.ass")
    sound.write_wav(work / "music.wav", sound.music_bed(total_len))
    sound.write_wav(work / "sfx.wav", sound.effects_track(total_len, pop_at, whoosh_at))
    run(["-i", str(work / "joined.mp4"), "-i", str(work / "music.wav"), "-i", str(work / "sfx.wav"),
         "-filter_complex", f"[0:v]ass={out / 'captions.ass'}:fontsdir={fonts_dir}[v];" + AUDIO_MIX,
         "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
         "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(out / "video.mp4")])
    if chapters:
        if chapters[0][0] > 0.5:
            chapters.insert(0, (0.0, "Intro"))
        (out / "chapters.json").write_text(json.dumps([[round(a, 1), b] for a, b in chapters]))
    short_len = build_short(ep, work, out, scenes_meta, captions, fonts_dir, pop_at, whoosh_at)

    svg_to_png(ep["thumbnail_svg"], work / "thumb.png", 1280, 720)
    Image.open(work / "thumb.png").convert("RGB").save(out / "thumbnail.jpg", quality=90)  # YouTube limit is 2 MB
    total = duration(out / "video.mp4")
    print(json.dumps({"video": str(out / "video.mp4"), "thumbnail": str(out / "thumbnail.jpg"),
                      "seconds": round(total, 1), "scenes": len(clips), "pictures": shots_total,
                      "visual_beats": beats_total, "seconds_per_beat": round(total / max(beats_total, 1), 1),
                      "chapters": len(chapters), "short": str(out / "short.mp4") if short_len else None,
                      "short_seconds": short_len}))
    shutil.rmtree(work)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("episode")
    p.add_argument("--out", default="build")
    a = p.parse_args()
    build(a.episode, a.out)
