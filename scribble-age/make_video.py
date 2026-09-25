#!/usr/bin/env python3
"""Build a Scribble Age video from an episode JSON file, using only free tools.

Episode JSON:
{
  "title": "...", "description": "...", "tags": ["..."],
  "thumbnail_svg": "<svg width='1280' height='720' ...>",
  "scenes": [{"narration": "...", "svg": "<svg width='1920' height='1080' ...>"}]
}

Output (in --out): video.mp4, thumbnail.jpg, captions.ass
Voice: Microsoft Edge neural TTS (free, via edge-tts). Pictures: SVG doodles
rendered with cairosvg. Assembly and captions: ffmpeg (imageio-ffmpeg build).
"""
import argparse, asyncio, json, os, re, shutil, ssl, subprocess, sys
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


def build(episode_path, out):
    ep = json.loads(Path(episode_path).read_text(encoding="utf-8"))
    out = Path(out)
    work = out / "work"
    work.mkdir(parents=True, exist_ok=True)
    fonts_dir = install_font()

    clips, captions, t0 = [], [], 0.0
    for i, sc in enumerate(ep["scenes"]):
        mp3, png, mp4 = work / f"s{i:03d}.mp3", work / f"s{i:03d}.png", work / f"s{i:03d}.mp4"
        words = asyncio.run(tts(sc["narration"], mp3))
        svg_to_png(sc["svg"], png, W, H)
        d = duration(mp3) + SCENE_TAIL
        frames = max(1, int(round(d * FPS)))
        # Slow push-in keeps a still drawing alive; alternate direction per scene.
        zoom = "min(1+0.06*on/%d,1.06)" % frames if i % 2 == 0 else "max(1.06-0.06*on/%d,1)" % frames
        run(["-i", str(png), "-i", str(mp3),
             "-filter_complex",
             f"[0:v]scale={W*2}:{H*2},zoompan=z='{zoom}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
             f":d={frames}:s={W}x{H}:fps={FPS},format=yuv420p[v];[1:a]apad=pad_dur={SCENE_TAIL},aresample=44100[a]",
             "-map", "[v]", "-map", "[a]", "-t", f"{d:.3f}",
             "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-c:a", "aac", "-b:a", "160k", "-ac", "2",
             str(mp4)])
        clips.append(mp4)
        for j in range(0, len(words), WORDS_PER_CAPTION):
            grp = words[j:j + WORDS_PER_CAPTION]
            end = words[j + WORDS_PER_CAPTION][0] if j + WORDS_PER_CAPTION < len(words) else grp[-1][1] + 0.2
            text = " ".join(w[2] for w in grp).replace("{", "(").replace("}", ")")
            captions.append((t0 + grp[0][0], t0 + end, text))
        t0 += duration(mp4)
        print(f"scene {i + 1}/{len(ep['scenes'])}: {d:.1f}s", flush=True)

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
                      "seconds": round(total, 1), "scenes": len(clips)}))
    shutil.rmtree(work)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("episode")
    p.add_argument("--out", default="build")
    a = p.parse_args()
    build(a.episode, a.out)
