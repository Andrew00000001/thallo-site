"""ffmpeg pipeline: any clip -> 1080x1920 branded Reel that meets Instagram's specs.

Spec points handled (Instagram Reels reference): H.264 + AAC 48 kHz, 30 fps, moov atom
first, no edit lists, 3 s minimum. Settings were tested with ffmpeg 6.1 (Ubuntu 24.04).
"""
import json
import subprocess

MIN_SECONDS = 3


class VideoError(RuntimeError):
    pass


def _run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        raise VideoError(f"{cmd[0]} failed: {p.stderr.strip()[-600:]}")
    return p.stdout


def probe(src):
    """(duration seconds, has_audio). Raises VideoError if there is no video stream."""
    info = json.loads(_run([
        "ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_type",
        "-of", "json", str(src),
    ]))
    kinds = {s["codec_type"] for s in info.get("streams", [])}
    if "video" not in kinds:
        raise VideoError("no video stream")
    return float(info["format"].get("duration") or 0), "audio" in kinds


def download_hls(url, dest):
    _run(["ffmpeg", "-hide_banner", "-nostdin", "-y", "-loglevel", "error", "-i", url, "-c", "copy", str(dest)])
    return dest


def render_reel(src, overlay_png, out, max_seconds):
    """Blurred 9:16 fill behind the centered original, plus the branding overlay."""
    duration, has_audio = probe(src)
    if duration < MIN_SECONDS:
        raise VideoError(f"clip is {duration:.1f}s; Instagram needs at least {MIN_SECONDS}s")
    dur = min(duration, max_seconds)
    fade_at = max(0.0, dur - 0.5)
    audio_in = [] if has_audio else ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo"]
    audio_src = "[0:a]" if has_audio else "[2:a]"
    graph = (
        "[0:v]fps=30,split=2[bgsrc][fgsrc];"
        "[bgsrc]scale=270:480:force_original_aspect_ratio=increase,crop=270:480,gblur=sigma=12,"
        "lutyuv=y='(val-minval)*0.45+minval':u='(val-128)*0.85+128':v='(val-128)*0.85+128',scale=1080:1920[bg];"
        "[fgsrc]scale=1080:1920:force_original_aspect_ratio=decrease:force_divisible_by=2[fg];"
        "[bg][fg]overlay=x=(W-w)/2:y=(H-h)/2[base];"
        "[1:v]scale=out_color_matrix=bt709:out_range=tv,format=yuva420p[brand];"
        "[base][brand]overlay=x=0:y=0,setsar=1,format=yuv420p[v];"
        f"{audio_src}loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000,"
        f"afade=t=in:d=0.15,afade=t=out:st={fade_at:.3f}:d=0.5[a]"
    )
    _run([
        "ffmpeg", "-hide_banner", "-nostdin", "-y", "-loglevel", "error",
        "-t", f"{dur:.3f}", "-i", str(src),
        "-i", str(overlay_png),
        *audio_in,
        "-filter_complex", graph, "-map", "[v]", "-map", "[a]", "-t", f"{dur:.3f}",
        "-c:v", "libx264", "-preset", "medium", "-profile:v", "high", "-crf", "20",
        "-maxrate", "6M", "-bufsize", "12M", "-pix_fmt", "yuv420p", "-r", "30",
        "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv",
        "-c:a", "aac", "-b:a", "128k", "-ar", "48000", "-ac", "2",
        "-use_editlist", "0", "-movflags", "+faststart",
        str(out),
    ])
    return out


def cover(reel, out):
    """Representative frame as a JPEG for cover_url (explicit BT.709 -> JPEG color conversion)."""
    _run([
        "ffmpeg", "-hide_banner", "-nostdin", "-y", "-loglevel", "error", "-ss", "1", "-t", "4", "-i", str(reel),
        "-an", "-vf",
        "thumbnail=120,scale=in_color_matrix=bt709:in_range=tv:out_color_matrix=bt601:out_range=pc,format=yuvj420p",
        "-frames:v", "1", "-fps_mode", "passthrough", "-update", "1", "-q:v", "2", str(out),
    ])
    return out
