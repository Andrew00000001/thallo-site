#!/usr/bin/env python3
"""Pick today's Scribble Age topic. No saved state is needed: every date maps to a fixed slot in
an era-interleaved calendar, and any topic already on the channel is skipped. The channel is the
only record of past topics. Its uploads are read with the YouTube Data API when YT_REFRESH_TOKEN
has a read scope (youtube.readonly); otherwise from the public RSS feed (the latest 15 videos).

    python3 topics.py            # today's topic plus recent channel titles
    python3 topics.py --date 2026-10-05
"""
import argparse, datetime, json, os, re, sys, urllib.parse, urllib.request
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
CHANNEL_ID = "UC1q7Zvv9PeoL5smeMvAvwDQ"
FEED = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"
API = "https://www.googleapis.com/youtube/v3"


def calendar(data):
    eras = list(data["eras"].values())
    order, i = [], 0
    while any(i < len(e) for e in eras):
        order += [e[i] for e in eras if i < len(e)]
        i += 1
    return order


def get_json(url, params=None, data=None, headers=None):
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, urllib.parse.urlencode(data).encode() if data else None, headers or {})
    return json.load(urllib.request.urlopen(req, timeout=30))


def api_videos():
    """Every upload, newest first: channels.list mine -> uploads playlist -> playlistItems.
    None if the token can't read the channel (an upload-only token gets a 403)."""
    if not all(os.environ.get(k) for k in ("YT_CLIENT_ID", "YT_CLIENT_SECRET", "YT_REFRESH_TOKEN")):
        return None
    try:
        tok = get_json("https://oauth2.googleapis.com/token", data={
            "client_id": os.environ["YT_CLIENT_ID"], "client_secret": os.environ["YT_CLIENT_SECRET"],
            "refresh_token": os.environ["YT_REFRESH_TOKEN"], "grant_type": "refresh_token"})
        auth = {"Authorization": f"Bearer {tok['access_token']}"}
        items = get_json(f"{API}/channels", {"part": "contentDetails", "mine": "true"}, headers=auth).get("items") or []
        if not items or items[0]["id"] != CHANNEL_ID:
            raise ValueError(f"token belongs to {items[0]['id'] if items else 'no channel'}, not {CHANNEL_ID}")
        params = {"part": "snippet", "maxResults": 50,
                  "playlistId": items[0]["contentDetails"]["relatedPlaylists"]["uploads"]}
        out = []
        while True:
            page = get_json(f"{API}/playlistItems", params, headers=auth)
            out += [(it["snippet"]["title"], it["snippet"].get("description", "")) for it in page.get("items", [])]
            if not page.get("nextPageToken"):
                return out
            params["pageToken"] = page["nextPageToken"]
    except Exception as e:
        print(f"note: YouTube Data API unavailable ({e}); using the RSS feed", file=sys.stderr)
        return None


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


def used(topic, videos, done):
    text = " ".join(t + " " + d for t, d in videos).lower() + " " + " ".join(done).lower()
    return any(re.search(r"\b" + re.escape(k.lower()) + r"\b", text) for k in topic["k"])


def pick(date):
    data = json.loads((HERE / "topics.json").read_text(encoding="utf-8"))
    order = calendar(data)
    start = datetime.date.fromisoformat(data["start_date"])
    slot = max(0, (date - start).days)
    videos = api_videos()
    source = "youtube_api" if videos is not None else "rss_feed"
    if videos is None:
        videos = recent_videos()
    done = [t["t"] for t in data.get("done", [])]
    for step in range(len(order)):
        topic = order[(slot + step) % len(order)]
        if not used(topic, videos, done):
            return topic, slot, step, videos, len(order), source
    return None, slot, len(order), videos, len(order), source


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--date", help="YYYY-MM-DD (default: today, America/Detroit)")
    a = p.parse_args()
    date = datetime.date.fromisoformat(a.date) if a.date else datetime.datetime.now(ZoneInfo("America/Detroit")).date()
    topic, slot, skipped, videos, total, source = pick(date)
    print(json.dumps({"date": str(date), "topic": topic["t"] if topic else None, "slot": slot,
                      "skipped_as_already_posted": skipped, "calendar_size": total,
                      "slots_left_before_repeat": total - slot % total, "channel_source": source,
                      "recent_channel_titles": [t for t, _ in videos]}, ensure_ascii=False, indent=1))
