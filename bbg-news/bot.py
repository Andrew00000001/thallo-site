"""BBG News auto-poster.

  python bot.py preview   render every post type to out/preview/ (no Instagram calls)
  python bot.py prepare   pick the next post, render it, write .pending.json
  python bot.py publish   publish .pending.json to Instagram and record it in state
  python bot.py refresh-token   print a refreshed long-lived token to stdout
"""
import json
import os
import re
import sys
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

import render
from instagram import Instagram

ROOT = Path(__file__).parent
CFG = json.loads((ROOT / "config.json").read_text())
EVERGREEN = json.loads((ROOT / "content/evergreen.json").read_text())
STATE_FILE = ROOT / "state/state.json"
PENDING_FILE = ROOT / ".pending.json"
OUT = ROOT / "out"
TZ = ZoneInfo(CFG["timezone"])
APP = CFG["steam_app_id"]
CAPTION_LIMIT = 2200


def log(msg):
    print(msg, file=sys.stderr)


def now():
    # BBG_NOW=2026-11-04T18:00 lets you simulate a date when testing.
    if os.environ.get("BBG_NOW"):
        return datetime.fromisoformat(os.environ["BBG_NOW"]).replace(tzinfo=TZ)
    return datetime.now(TZ)


def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"steam_seeded": False, "steam_seen": [], "posted": []}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2) + "\n")


def set_output(**kv):
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            for k, v in kv.items():
                f.write(f"{k}={v}\n")


# ---------- Steam ----------

def steam_release():
    """Returns (release date or None, coming_soon) from the Steam store."""
    r = requests.get(
        "https://store.steampowered.com/api/appdetails",
        params={"appids": APP, "filters": "release_date"},
        timeout=30,
    )
    rd = r.json()[str(APP)]["data"]["release_date"]
    try:
        return datetime.strptime(rd["date"], "%b %d, %Y").date(), rd["coming_soon"]
    except ValueError:
        return None, rd["coming_soon"]


def steam_news(count=10):
    """Official SkyVu announcements only (not third-party press feeds), oldest first."""
    r = requests.get(
        "https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/",
        params={"appid": APP, "count": count, "feeds": "steam_community_announcements"},
        timeout=30,
    )
    items = r.json()["appnews"]["newsitems"]
    return sorted(items, key=lambda n: n["date"])


def clean_bbcode(text):
    text = re.sub(r"\{STEAM_CLAN_IMAGE\}\S*", "", text)
    text = re.sub(r"\[\*\]\s*(\[p\])?", "\n• ", text)
    text = re.sub(r"\[/?(p|list|olist)\]", "\n", text)
    text = re.sub(r"\[url=([^\]]+)\](.*?)\[/url\]", r"\2", text)
    text = re.sub(r"\[/?[^\]]+\]", "", text)
    text = "\n".join(" ".join(line.split()) for line in text.splitlines())
    text = re.sub(r"\n+(?=• )", "\n", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def first_sentence(text, limit=170):
    flat = " ".join(text.split())
    m = re.match(r"(.+?[.!?])(\s|$)", flat)
    s = m.group(1) if m else flat
    return s if len(s) <= limit else s[: limit - 1].rsplit(" ", 1)[0] + "…"


# ---------- Captions ----------

def caption(body, source, launched):
    suffix = CFG["post_launch_line"] if launched else CFG["launch_line"]
    tail = f"\n\nSource: {source}\n\n{suffix}\n.\n.\n{' '.join(CFG['hashtags'])}"
    room = CAPTION_LIMIT - len(tail)
    if len(body) > room:
        body = body[: room - 1].rsplit(" ", 1)[0] + "…"
    return body + tail


def countdown_caption(n):
    if n == 0:
        return (
            "🚨 IT'S LAUNCH DAY. Steam lists Battle Bears Gold for release today, Nov 4.\n\n"
            "Grab your loadout and we'll see you on the battlefield. Who's on first? 👇"
        )
    when = "TOMORROW" if n == 1 else f"in {n} days"
    return (
        f"⏳ Battle Bears Gold drops {when}!\n\n"
        "Wishlist it on Steam to get notified the moment it's live (link in bio).\n\n"
        "Who's playing day one? 👇"
    )


# ---------- Post selection ----------

def news_post(item, launched):
    text = clean_bbcode(item["contents"])
    return {
        "id": f"news-{item['gid']}",
        "kind": "news",
        "launched": launched,
        "card": {"tag": "OFFICIAL NEWS", "headline": item["title"].upper(), "body": [first_sentence(text)]},
        "caption": caption(f"📰 {item['title']}\n\n{text}", "SkyVu announcement on Steam", launched),
    }


def countdown_post(n, launched):
    return {
        "id": f"countdown-{n}",
        "kind": "countdown",
        "launched": launched,
        "days_left": n,
        "caption": caption(countdown_caption(n), "Battle Bears Gold Steam page", launched),
    }


def fact_post(item, launched):
    return {
        "id": item["id"],
        "kind": "fact",
        "launched": launched,
        "card": {"tag": item["tag"], "headline": item["headline"], "body": item["body"]},
        "caption": caption(item["caption"], item["source"], launched),
    }


def choose(state, t):
    """Returns the next post dict, or None. May update state (Steam seeding)."""
    today = t.date()
    launch = date.fromisoformat(CFG["launch_date"])

    release, coming_soon = steam_release()
    if release != launch:
        raise SystemExit(
            f"Steam release date is now {release} but config.json says {launch}. "
            "Update launch_date, launch_line and footer_line in config.json, then re-run."
        )
    launched = not coming_soon
    if today > launch and coming_soon:
        raise SystemExit("Launch date passed but Steam still says coming soon. Check for a delay.")

    posted_ids = {p["id"] for p in state["posted"]}
    today_posts = [p for p in state["posted"] if p["date"] == today.isoformat()]
    if len(today_posts) >= CFG["max_posts_per_day"]:
        log(f"Daily cap reached ({len(today_posts)} posts today).")
        return None

    # 1. New official news, any time of day.
    news = steam_news()
    if not state["steam_seeded"]:
        state["steam_seen"] = [n["gid"] for n in news]
        state["steam_seeded"] = True
        log(f"First run: marked {len(news)} existing Steam announcements as already seen.")
    for item in news:
        if item["gid"] not in state["steam_seen"]:
            return news_post(item, launched)

    # 2. One scheduled post per day, at/after daily_post_hour: countdown beats fact.
    if t.hour < CFG["daily_post_hour"]:
        return None
    if any(p["kind"] in ("countdown", "fact") for p in today_posts):
        return None
    days_left = (launch - today).days
    if days_left in CFG["countdown_milestones"] and f"countdown-{days_left}" not in posted_ids:
        return countdown_post(days_left, launched)
    for item in EVERGREEN:
        if item["id"] in posted_ids or (item.get("pre_launch_only") and today >= launch):
            continue
        return fact_post(item, launched)
    log("Fact bank used up. Add more entries to content/evergreen.json.")
    return None


def render_post(post, out_dir):
    cfg = dict(CFG, footer_line=CFG["post_launch_footer"]) if post["launched"] else CFG
    path = out_dir / f"{post['id']}.jpg"
    if post["kind"] == "countdown":
        render.render_countdown(cfg, post["days_left"], path)
    else:
        c = post["card"]
        render.render_card(cfg, c["tag"], c["headline"], c["body"], path)
    return path


# ---------- Commands ----------

def cmd_prepare():
    state = load_state()
    post = choose(state, now())
    save_state(state)
    if not post:
        log("Nothing to post this run.")
        set_output(has_post="false")
        return
    OUT.mkdir(exist_ok=True)
    image = render_post(post, OUT)
    PENDING_FILE.write_text(json.dumps({**post, "image": str(image)}, indent=2))
    log(f"Prepared {post['id']} -> {image}\n\n{post['caption']}")
    set_output(has_post="true", post_id=post["id"])


def image_url(image_path):
    if os.environ.get("IMAGE_BASE_URL"):
        return f"{os.environ['IMAGE_BASE_URL'].rstrip('/')}/{Path(image_path).name}"
    repo_root = Path(os.environ.get("GITHUB_WORKSPACE", ROOT.parent))
    rel = Path(image_path).resolve().relative_to(repo_root.resolve()).as_posix()
    return f"https://raw.githubusercontent.com/{os.environ['GITHUB_REPOSITORY']}/{os.environ['IMAGE_COMMIT']}/{rel}"


def cmd_publish():
    pending = json.loads(PENDING_FILE.read_text())
    token = os.environ.get("IG_ACCESS_TOKEN")
    if not token:
        raise SystemExit("IG_ACCESS_TOKEN is not set. Add it as a GitHub Actions secret.")
    url = image_url(pending["image"])
    head = requests.head(url, timeout=30)
    if head.status_code != 200:
        raise SystemExit(f"Image not publicly reachable ({head.status_code}): {url}")
    media_id = Instagram(token).publish_image(url, pending["caption"])

    state = load_state()
    if pending["kind"] == "news":
        state["steam_seen"].append(pending["id"].removeprefix("news-"))
    state["posted"].append({
        "id": pending["id"],
        "kind": pending["kind"],
        "date": now().date().isoformat(),
        "at": now().isoformat(timespec="minutes"),
        "media_id": media_id,
    })
    save_state(state)
    PENDING_FILE.unlink()
    log(f"Published {pending['id']} as Instagram media {media_id}")


def cmd_preview():
    out = OUT / "preview"
    out.mkdir(parents=True, exist_ok=True)
    posts = [countdown_post(n, False) for n in (21, 1, 0)]
    posts += [fact_post(i, False) for i in EVERGREEN]
    try:
        posts += [news_post(n, False) for n in steam_news()[-2:]]
    except requests.RequestException as e:
        log(f"Skipping Steam news preview: {e}")
    lines = []
    for p in posts:
        path = render_post(p, out)
        lines.append(f"## {p['id']}\n\n![]({path.name})\n\n```\n{p['caption']}\n```\n")
    (out / "captions.md").write_text("\n".join(lines))
    log(f"Rendered {len(posts)} previews to {out}")


def cmd_refresh_token():
    token = os.environ.get("IG_ACCESS_TOKEN")
    if not token:
        raise SystemExit("IG_ACCESS_TOKEN is not set.")
    print(Instagram(token).refresh_token())


if __name__ == "__main__":
    commands = {
        "prepare": cmd_prepare,
        "publish": cmd_publish,
        "preview": cmd_preview,
        "refresh-token": cmd_refresh_token,
    }
    if len(sys.argv) != 2 or sys.argv[1] not in commands:
        raise SystemExit(__doc__)
    commands[sys.argv[1]]()
