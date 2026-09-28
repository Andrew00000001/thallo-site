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
from pathlib import Path

import cairosvg
import edge_tts
import edge_tts.communicate as ec
import imageio_ffmpeg
from PIL import Image

HERE = Path(__file__).resolve().parent
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
VOICE = "en-US-AndrewNeural"
FPS = 30
W, H = 1920, 1080
FONT_NAME = "Patrick Hand"
WORDS_PER_CAPTION = 3
SCENE_TAIL = 0.35  # seconds of silence after each scene

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


def write_ass(captions, path):
    head = (
        "[Script Info]\nScriptType: v4.00+\nPlayResX: 1920\nPlayResY: 1080\nWrapStyle: 2\n\n"
        "[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, "
        "Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, "
        "Alignment, MarginL, MarginR, MarginV, Encoding\n"
        f"Style: Cap,{FONT_NAME},110,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,0,0,0,0,100,100,0,0,1,6,3,2,80,80,60,1\n\n"
        "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"
    )
    lines = [f"Dialogue: 0,{ass_time(a)},{ass_time(b)},Cap,,0,0,0,,{t}" for a, b, t in captions]
    Path(path).write_text(head + "\n".join(lines) + "\n", encoding="utf-8")


def svg_to_png(svg, png, w, h):
    cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=str(png), output_width=w, output_height=h,
                     background_color="white")


def shot_svgs(sc):
    """A scene is one picture ("svg") or several ("shots"). A shot is either {"svg": full SVG}
    or {"add": SVG elements}, which draws the elements on top of the previous shot (a cheap reveal)."""
    if "shots" not in sc:
        return [sc["svg"]]
    svgs = []
    for shot in sc["shots"]:
        if "svg" in shot:
            svgs.append(shot["svg"])
        else:
            prev = svgs[-1]
            cut = prev.rindex("</svg>")
            svgs.append(prev[:cut] + shot["add"] + prev[cut:])
    return svgs


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


def build(episode_path, out):
    ep = json.loads(Path(episode_path).read_text(encoding="utf-8"))
    out = Path(out)
    work = out / "work"
    work.mkdir(parents=True, exist_ok=True)
    fonts_dir = install_font()

    clips, captions, t0, shots_total = [], [], 0.0, 0
    for i, sc in enumerate(ep["scenes"]):
        mp3, mp4 = work / f"s{i:03d}.mp3", work / f"s{i:03d}.mp4"
        words = tts_retry(sc["narration"], mp3)
        d = duration(mp3) + SCENE_TAIL
        svgs = shot_svgs(sc)
        cuts = shot_cuts(words, d, len(svgs))
        inputs, chains = [], []
        for k, svg in enumerate(svgs):
            png = work / f"s{i:03d}_{k}.png"
            svg_to_png(svg, png, W, H)
            frames = max(1, int(round((cuts[k + 1] - cuts[k]) * FPS)))
            inputs += ["-i", str(png)]
            chains.append(f"[{k}:v]scale={W*2}:{H*2},{motion(shots_total + k, frames)}"
                          f":d={frames}:s={W}x{H}:fps={FPS},setsar=1[v{k}]")
        n = len(svgs)
        graph = ";".join(chains) + ";" + "".join(f"[v{k}]" for k in range(n)) + \
            f"concat=n={n}:v=1:a=0,format=yuv420p[v];[{n}:a]apad=pad_dur={SCENE_TAIL},aresample=44100[a]"
        run([*inputs, "-i", str(mp3), "-filter_complex", graph,
             "-map", "[v]", "-map", "[a]", "-t", f"{d:.3f}",
             "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-c:a", "aac", "-b:a", "160k", "-ac", "2",
             str(mp4)])
        clips.append(mp4)
        shots_total += n
        for j in range(0, len(words), WORDS_PER_CAPTION):
            grp = words[j:j + WORDS_PER_CAPTION]
            end = words[j + WORDS_PER_CAPTION][0] if j + WORDS_PER_CAPTION < len(words) else grp[-1][1] + 0.2
            text = " ".join(w[2] for w in grp).replace("{", "(").replace("}", ")")
            captions.append((t0 + grp[0][0], t0 + end, text))
        t0 += duration(mp4)
        print(f"scene {i + 1}/{len(ep['scenes'])}: {d:.1f}s, {n} shots", flush=True)

    (work / "list.txt").write_text("".join(f"file '{c.name}'\n" for c in clips))
    run(["-f", "concat", "-safe", "0", "-i", str(work / "list.txt"), "-c", "copy", str(work / "joined.mp4")])
    write_ass(captions, out / "captions.ass")
    run(["-i", str(work / "joined.mp4"),
         "-vf", f"ass={out / 'captions.ass'}:fontsdir={fonts_dir}",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-c:a", "copy", "-movflags", "+faststart",
         str(out / "video.mp4")])

    svg_to_png(ep["thumbnail_svg"], work / "thumb.png", 1280, 720)
    Image.open(work / "thumb.png").convert("RGB").save(out / "thumbnail.jpg", quality=90)  # YouTube limit is 2 MB
    total = duration(out / "video.mp4")
    print(json.dumps({"video": str(out / "video.mp4"), "thumbnail": str(out / "thumbnail.jpg"),
                      "seconds": round(total, 1), "scenes": len(clips), "shots": shots_total,
                      "seconds_per_shot": round(total / max(shots_total, 1), 1)}))
    shutil.rmtree(work)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("episode")
    p.add_argument("--out", default="build")
    a = p.parse_args()
    build(a.episode, a.out)
