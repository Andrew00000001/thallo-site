#!/usr/bin/env python3
"""List the most-viewed Twitch clips of the game that the channel hasn't posted yet.

Twitch viewers clip the best moments themselves, and the clip view count ranks them, so this
finds highlights across every streamer playing the game without downloading a single stream.
Prints JSON candidates, best first.

The lists come from Twitch's public web API (the one twitch.tv itself and yt-dlp use). Without
signing in it only serves the first page of a list, so each list stops at 100 clips.
"""
import argparse, datetime, json, re, sys, time
from pathlib import Path

import requests

HERE = Path(__file__).resolve().parent
CONFIG = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
GQL = "https://gql.twitch.tv/gql"
WEB_CLIENT_ID = "kimne78kx3ncx6brgo4mv6wki5h1ko"  # twitch.tv's own public web client id
SAME_MOMENT = 150  # seconds; one streamer's clips this close together are usually the same moment
PERIODS = {"24hr": "LAST_DAY", "7d": "LAST_WEEK", "30d": "LAST_MONTH", "all": "ALL_TIME"}
LIST_SIZE = 100
NODE = ("slug title viewCount durationSeconds createdAt language videoOffsetSeconds "
        "video{ id } broadcaster{ login displayName }")


def gql(query, variables):
    """One read-only query. Twitch answers "service error" now and then, so try a few times."""
    last = "no response"
    for attempt in range(4):
        try:
            r = requests.post(GQL, json={"query": query, "variables": variables},
                              headers={"Client-ID": WEB_CLIENT_ID}, timeout=40)
            body = r.json()
            if r.status_code == 200 and not body.get("errors"):
                return body.get("data") or {}
            last = f"{r.status_code} {json.dumps(body.get('errors'))[:300]}"
        except (requests.RequestException, ValueError) as e:
            last = str(e)[:300]
        time.sleep(2 * (attempt + 1))
    raise RuntimeError(last)


def parse_utc(text):
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00")).timestamp()


def list_clips(game, rng):
    """The category's top clips for one time range, most viewed first. None if Twitch wouldn't say."""
    langs = [l for l in CONFIG.get("languages", []) if re.fullmatch(r"[A-Z_]{2,10}", l)]
    criteria = f"period:{PERIODS[rng]}" + (f", languages:[{','.join(langs)}]" if langs else "")
    query = ("query($name:String!){ game(name:$name){ id clips(first:%d, criteria:{%s}){ edges{ node{ %s } } } } }"
             % (LIST_SIZE, criteria, NODE))
    try:
        data = gql(query, {"name": game})
    except RuntimeError as e:  # one list failing shouldn't sink the run; the others still count
        print(f"warning: couldn't list the {rng} clips: {e}", file=sys.stderr)
        return None
    if data.get("game") is None:
        sys.exit(f"Twitch has no category named {game!r}; check config.json -> game.twitch_name")
    clips = []
    for edge in (data["game"].get("clips") or {}).get("edges") or []:
        n = edge.get("node") or {}
        b = n.get("broadcaster") or {}
        if not n.get("slug") or not b.get("login"):  # the streamer's account is gone
            continue
        name = b.get("displayName") or b["login"]
        clips.append({
            "slug": n["slug"], "url": f"https://www.twitch.tv/{b['login']}/clip/{n['slug']}",
            "title": n.get("title"), "views": n.get("viewCount") or 0, "seconds": n.get("durationSeconds") or 0,
            "ts": int(parse_utc(n["createdAt"])), "login": b["login"].lower(),
            # The caption font only has Latin letters, so fall back to the login for other scripts.
            "streamer": name if name.isascii() else b["login"],
            "vod": (n.get("video") or {}).get("id"), "offset": n.get("videoOffsetSeconds")})
    return clips


def same_moment(a, b):
    """Two clips of the same streamer cut from the same few minutes of the same stream."""
    if a["login"] != b["login"]:
        return False
    if a["vod"] and a["vod"] == b["vod"] and a["offset"] is not None and b["offset"] is not None:
        return abs(a["offset"] - b["offset"]) < SAME_MOMENT
    return abs(a["ts"] - b["ts"]) < SAME_MOMENT


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--count", type=int, default=12, help="how many candidates to print")
    p.add_argument("--game", help="list another Twitch category instead (for testing); ignores clips_from")
    a = p.parse_args()

    game = a.game or CONFIG["game"]["twitch_name"]
    # Clips from before the game came out are countdown and trailer-reaction streams, never gameplay.
    since = 0 if a.game or not CONFIG["game"].get("clips_from") else parse_utc(CONFIG["game"]["clips_from"])
    skip = {s.lower() for s in CONFIG.get("skip_streamers", [])}

    from upload import posted as on_channels  # the channel is the record; routine runs can't push to git
    posted = on_channels()

    lists = {rng: list_clips(game, rng) for rng in PERIODS}
    if all(v is None for v in lists.values()):
        sys.exit("couldn't list any Twitch clips; check the network, or Twitch changed its web API (see README)")
    lists = {rng: v or [] for rng, v in lists.items()}

    def usable(c):
        return (c["slug"] not in posted and c["login"] not in skip and c["ts"] >= since
                and c["seconds"] >= CONFIG["min_seconds"] and c["views"] >= CONFIG["min_views"])

    # Clips we already posted, so other viewers' clips of the same moment are skipped too.
    moments = [c for lst in lists.values() for c in lst if c["slug"] in posted]
    # Fresh clips first (last 24 hours, then 7 days). When those run dry, go deep: the 30-day and
    # all-time lists, merged and ranked by views, so the channel falls back on the biggest moments.
    fresh = [(rng, c) for rng in ("24hr", "7d") for c in lists[rng] if usable(c)]
    deep = []
    if len(fresh) < a.count:
        deep = [(rng, c) for rng in ("30d", "all") for c in lists[rng] if usable(c)]
        deep.sort(key=lambda x: -x[1]["views"])

    picked, seen, per_streamer = [], set(), {}
    cap = CONFIG.get("max_per_streamer", 3)  # keeps one streamer from filling the whole list
    for rng, c in fresh + deep:
        if c["slug"] in seen or per_streamer.get(c["login"], 0) >= cap or any(same_moment(c, m) for m in moments):
            continue
        seen.add(c["slug"])
        moments.append(c)
        per_streamer[c["login"]] = per_streamer.get(c["login"], 0) + 1
        picked.append({"slug": c["slug"], "url": c["url"], "twitch_title": c["title"],
                       "streamer": c["streamer"], "streamer_login": c["login"],
                       "views": c["views"], "seconds": c["seconds"], "clip_created": c["ts"],
                       "clip_date": datetime.datetime.fromtimestamp(c["ts"], datetime.timezone.utc).strftime("%Y-%m-%d"),
                       "range": rng})
        if len(picked) >= a.count:
            break
    listed = sum(len(v) for v in lists.values())
    print(f"{len(picked)} candidates from {listed} listed clips of {game}", file=sys.stderr)
    print(json.dumps(picked, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
