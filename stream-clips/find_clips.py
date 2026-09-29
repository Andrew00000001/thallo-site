#!/usr/bin/env python3
"""List the streamer's most-viewed Twitch clips that the channel hasn't posted yet.

Twitch viewers clip the best moments themselves, and the clip view count ranks them,
so this is the cheapest way to find highlights: no VOD downloads, no scanning hours of stream.
Prints JSON candidates, best first.
"""
import argparse, datetime, json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONFIG = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
SAME_MOMENT = 150  # seconds; clips made this close together are usually the same moment


def list_clips(login, rng, limit):
    url = f"https://www.twitch.tv/{login}/clips?filter=clips&range={rng}"
    r = subprocess.run([sys.executable, "-m", "yt_dlp", "--flat-playlist", "--playlist-end", str(limit), "-J", url],
                       capture_output=True, text=True, timeout=300)
    if r.returncode:
        sys.exit(f"yt-dlp failed listing {url}: {r.stderr[-1000:]}")
    return [e for e in json.loads(r.stdout).get("entries", []) if e.get("url")]


def slug_of(url):
    return url.rstrip("/").split("/clip/")[-1].split("?")[0]


def parse_utc(text):
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00")).timestamp()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--count", type=int, default=12, help="how many candidates to print")
    a = p.parse_args()

    history = json.loads((HERE / "history.json").read_text(encoding="utf-8"))["shorts"]
    posted = {h["slug"] for h in history}
    moments = [h["clip_created"] for h in history if h.get("clip_created")]
    from upload import posted as on_channels  # the channels themselves; runs can't push history.json
    slugs, times = on_channels()
    posted |= slugs
    moments += times
    # Whole streams we never clip, e.g. network co-productions (config.json "skip_windows").
    windows = [(parse_utc(w["from"]), parse_utc(w["to"])) for w in CONFIG.get("skip_windows", [])]

    def usable(e):
        ts = e.get("timestamp") or 0
        return (slug_of(e["url"]) not in posted and (e.get("duration") or 0) >= CONFIG["min_seconds"]
                and (e.get("view_count") or 0) >= CONFIG["min_views"]
                and not any(lo <= ts <= hi for lo, hi in windows))

    login = CONFIG["streamer"]["login"]
    # Fresh clips first (last 24 hours, then 7 days). When those run dry (the streamer is offline,
    # or everything fresh was used or rejected), go deep: the 30-day and all-time clip lists,
    # merged and ranked by views, so the channel falls back on the streamer's biggest moments.
    fresh = [(rng, e) for rng in ("24hr", "7d") for e in list_clips(login, rng, 100) if usable(e)]
    deep = []
    if len(fresh) < a.count:
        deep = [(rng, e) for rng, limit in (("30d", 200), ("all", 300)) for e in list_clips(login, rng, limit) if usable(e)]
        deep.sort(key=lambda x: -(x[1].get("view_count") or 0))

    picked, seen = [], set()
    for rng, e in fresh + deep:
        slug, ts = slug_of(e["url"]), e.get("timestamp") or 0
        if slug in seen or any(abs(ts - m) < SAME_MOMENT for m in moments):
            continue
        seen.add(slug)
        moments.append(ts)
        picked.append({"slug": slug, "url": e["url"], "twitch_title": e.get("title"),
                       "views": e.get("view_count"), "seconds": e.get("duration"), "clip_created": ts,
                       "clip_date": datetime.datetime.fromtimestamp(ts, datetime.timezone.utc).strftime("%Y-%m-%d"),
                       "range": rng})
        if len(picked) >= a.count:
            break
    print(json.dumps(picked, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
