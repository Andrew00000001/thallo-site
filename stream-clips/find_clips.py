#!/usr/bin/env python3
"""List the streamer's most-viewed Twitch clips that the channel hasn't posted yet.

Twitch viewers clip the best moments themselves, and the clip view count ranks them,
so this is the cheapest way to find highlights: no VOD downloads, no scanning hours of stream.
Prints JSON candidates, best first.
"""
import argparse, json, os, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONFIG = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
SAME_MOMENT = 150  # seconds; clips made this close together are usually the same moment


def list_clips(login, rng, limit=60):
    url = f"https://www.twitch.tv/{login}/clips?filter=clips&range={rng}"
    r = subprocess.run([sys.executable, "-m", "yt_dlp", "--flat-playlist", "--playlist-end", str(limit), "-J", url],
                       capture_output=True, text=True, timeout=300)
    if r.returncode:
        sys.exit(f"yt-dlp failed listing {url}: {r.stderr[-1000:]}")
    return [e for e in json.loads(r.stdout).get("entries", []) if e.get("url")]


def slug_of(url):
    return url.rstrip("/").split("/clip/")[-1].split("?")[0]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--count", type=int, default=8, help="how many candidates to print")
    a = p.parse_args()

    history = json.loads((HERE / "history.json").read_text(encoding="utf-8"))["shorts"]
    posted = {h["slug"] for h in history}
    moments = [h["clip_created"] for h in history if h.get("clip_created")]
    if os.environ.get(CONFIG["token_env"]):
        from upload import posted_slugs  # catches uploads whose history.json push failed
        posted |= posted_slugs()

    login = CONFIG["streamer"]["login"]
    picked, seen = [], set()
    for rng in ("24hr", "7d", "30d"):  # widen the window only when the fresh one runs dry
        for e in list_clips(login, rng):
            slug, ts = slug_of(e["url"]), e.get("timestamp") or 0
            if slug in posted or slug in seen:
                continue
            if (e.get("duration") or 0) < CONFIG["min_seconds"] or (e.get("view_count") or 0) < CONFIG["min_views"]:
                continue
            if any(abs(ts - m) < SAME_MOMENT for m in moments):
                continue
            seen.add(slug)
            moments.append(ts)
            picked.append({"slug": slug, "url": e["url"], "twitch_title": e.get("title"),
                           "views": e.get("view_count"), "seconds": e.get("duration"),
                           "clip_created": ts, "range": rng})
        if len(picked) >= a.count:
            break
    print(json.dumps(picked[:a.count], indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
