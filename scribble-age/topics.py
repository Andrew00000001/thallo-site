#!/usr/bin/env python3
"""Pick today's Scribble Age topic. No saved state is needed: every date maps to a fixed slot in
an era-interleaved calendar, and any topic already on the channel (checked against the channel's
RSS feed, which lists the latest 15 videos) is skipped.

    python3 topics.py            # today's topic plus recent channel titles
    python3 topics.py --date 2026-10-05
"""
import argparse, datetime, json, re, sys, urllib.request
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
CHANNEL_ID = "UC1q7Zvv9PeoL5smeMvAvwDQ"
FEED = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"


def calendar(data):
    eras = list(data["eras"].values())
    order, i = [], 0
    while any(i < len(e) for e in eras):
        order += [e[i] for e in eras if i < len(e)]
        i += 1
    return order


def recent_videos():
    try:
        xml = urllib.request.urlopen(FEED, timeout=30).read().decode("utf-8", "ignore")
    except Exception as e:  # the pick still works without the feed; it just can't double-check
        print(f"warning: channel feed unavailable ({e})", file=sys.stderr)
        return []
    out = []
    for entry in re.findall(r"<entry>(.*?)</entry>", xml, re.S):
        title = re.search(r"<title>(.*?)</title>", entry, re.S).group(1)
        desc = re.search(r"<media:description>(.*?)</media:description>", entry, re.S)
        out.append((title, desc.group(1) if desc else ""))
    return out


def used(topic, videos, history):
    text = " ".join(t + " " + d for t, d in videos).lower() + " " + " ".join(history).lower()
    return any(re.search(r"\b" + re.escape(k.lower()) + r"\b", text) for k in topic["k"])


def pick(date):
    data = json.loads((HERE / "topics.json").read_text(encoding="utf-8"))
    order = calendar(data)
    start = datetime.date.fromisoformat(data["start_date"])
    slot = max(0, (date - start).days)
    videos = recent_videos()
    history = [e.get("topic", "") + " " + e.get("title", "") for e in
               json.loads((HERE / "history.json").read_text()).get("episodes", [])]
    history += [t["t"] for t in data.get("done", [])]
    for step in range(len(order)):
        topic = order[(slot + step) % len(order)]
        if not used(topic, videos, history):
            return topic, slot, step, videos, len(order)
    return None, slot, len(order), videos, len(order)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--date", help="YYYY-MM-DD (default: today, America/Detroit)")
    a = p.parse_args()
    date = datetime.date.fromisoformat(a.date) if a.date else datetime.datetime.now(ZoneInfo("America/Detroit")).date()
    topic, slot, skipped, videos, total = pick(date)
    print(json.dumps({"date": str(date), "topic": topic["t"] if topic else None, "slot": slot,
                      "skipped_as_already_posted": skipped, "calendar_size": total,
                      "slots_left_before_repeat": total - slot % total,
                      "recent_channel_titles": [t for t, _ in videos]}, ensure_ascii=False, indent=1))
