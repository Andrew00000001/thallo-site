"""BBG News auto-poster.

  python bot.py prepare        sync Discord clips, pick the next post, write .pending.json
  python bot.py render-video   turn the pending clip/trailer into a Reel (needs ffmpeg)
  python bot.py publish        host the media, publish to Instagram, update Discord and state
  python bot.py preview        render every post type to out/preview/ (nothing is posted)
  python bot.py refresh-token  print a refreshed long-lived Instagram token to stdout
"""
import json
import os
import re
import shutil
import sys
import tempfile
import time
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

import clips
import hosting
import render
import sources
import video
from discord_api import Discord, DiscordError
from instagram import TRANSIENT_CODES, ContainerError, CopyrightMatch, Instagram, InstagramError

ROOT = Path(__file__).parent
CFG = json.loads((ROOT / "config.json").read_text())
EVERGREEN = json.loads((ROOT / "content/evergreen.json").read_text())
STATE_FILE = ROOT / "state/state.json"
PENDING_FILE = ROOT / ".pending.json"
PREVIEW = ROOT / "out/preview"
WORK = Path(os.environ.get("RUNNER_TEMP") or tempfile.gettempdir()) / "bbg-work"
TZ = ZoneInfo(CFG["timezone"])
APP = CFG["steam_app_id"]
CAPTION_LIMIT = 2200
MAX_FAILURES = 3
STATE_DEFAULTS = {
    "steam_seeded": False, "steam_seen": [],
    "youtube_seeded": False, "youtube_seen": [],
    "trailers_done": [], "clips": {}, "failures": {}, "inflight": {}, "posted": [],
}


def log(msg):
    print(msg, file=sys.stderr)


def env(name):
    return (os.environ.get(name) or "").strip()


def now():
    # BBG_NOW=2026-11-04T18:00 lets you simulate a date when testing.
    if env("BBG_NOW"):
        return datetime.fromisoformat(env("BBG_NOW")).replace(tzinfo=TZ)
    return datetime.now(TZ)


def load_state():
    state = json.loads(STATE_FILE.read_text()) if STATE_FILE.exists() else {}
    for k, v in STATE_DEFAULTS.items():
        state.setdefault(k, json.loads(json.dumps(v)))
    return state


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2) + "\n")


def set_output(**kv):
    if env("GITHUB_OUTPUT"):
        with open(env("GITHUB_OUTPUT"), "a") as f:
            for k, v in kv.items():
                f.write(f"{k}={v}\n")


def setting(name):
    """Non-secret setting: environment variable (e.g. a GitHub Actions variable) or config.json."""
    return env(name.upper()) or str(CFG.get(name, "")).strip()


def discord():
    """(client, clips channel, owner id, feed channel) or None if Discord isn't configured."""
    channel, owner = setting("discord_clips_channel_id"), setting("discord_owner_id")
    if not (env("DISCORD_BOT_TOKEN") and channel and owner):
        return None
    return Discord(env("DISCORD_BOT_TOKEN")), channel, owner, setting("discord_feed_channel_id")


# ---------- Text helpers ----------

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


def caption(body, source, launched):
    suffix = CFG["post_launch_line"] if launched else CFG["launch_line"]
    tail = (
        f"\n\nSource: {source}\n\n{suffix}\n"
        f"BBG News is an unofficial fan page, not affiliated with SkyVu.\n.\n.\n{' '.join(CFG['hashtags'])}"
    )
    room = CAPTION_LIMIT - len(tail)
    if len(body) > room:
        body = body[: room - 1].rsplit(" ", 1)[0] + "…"
    return body + tail


def countdown_caption(n):
    if n == 0:
        d = date.fromisoformat(CFG["launch_date"])
        return (
            f"🚨 IT'S LAUNCH DAY. Steam lists Battle Bears Gold for release today, {d:%b} {d.day}.\n\n"
            "Grab your loadout and we'll see you on the battlefield. Who's on first? 👇"
        )
    when = "TOMORROW" if n == 1 else f"in {n} days"
    return (
        f"⏳ Battle Bears Gold drops {when}!\n\n"
        "Wishlist it on Steam to get notified the moment it's live (link in bio).\n\n"
        "Who's playing day one? 👇"
    )


# ---------- Post builders ----------

def news_post(item, launched):
    text = clean_bbcode(item["contents"])
    return {
        "id": f"news-{item['gid']}",
        "kind": "news",
        "launched": launched,
        "card": {"tag": "OFFICIAL NEWS", "headline": item["title"].upper(), "body": [first_sentence(text)]},
        "caption": caption(f"📰 {item['title']}\n\n{text}", "SkyVu announcement on Steam", launched),
    }


def youtube_post(v, launched):
    return {
        "id": f"youtube-{v['id']}",
        "kind": "youtube",
        "launched": launched,
        "card": {"tag": "NEW VIDEO", "headline": v["title"].upper(),
                 "body": ["New on the official Battle Bears YouTube channel"]},
        "caption": caption(
            f"🎬 New official video: {v['title']}\n\nWatch it on the Battle Bears YouTube channel: youtube.com/battlebears",
            "Battle Bears YouTube channel", launched),
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


def trailer_post(t, launched):
    return {
        "id": f"trailer-{t['id']}",
        "kind": "trailer",
        "launched": launched,
        "video": {"type": "hls", "url": t["hls"]},
        "overlay": {"tag": "OFFICIAL TRAILER", "credit": "FOOTAGE: SKYVU"},
        "caption": caption(f"🎬 {t['name']}\n\nOfficial Battle Bears Gold footage from SkyVu.",
                           "Battle Bears Gold Steam page (footage © SkyVu)", launched),
    }


def clip_post(c, launched):
    m, mine, name = c["msg"], c["mine"], c["credit"]
    if mine:
        body = c["caption"] or "🎥 Fresh Battle Bears Gold gameplay."
        source, tag, credit_line = "BBG News gameplay", "GAMEPLAY", "BBG NEWS GAMEPLAY"
    else:
        intro = f"{c['caption']}\n\n" if c["caption"] else ""
        body = f"{intro}🎥 Community clip by {name}!\n\nGot a clip? Submit it in the BBG News Discord (link in bio)."
        source, tag, credit_line = f"Clip by {name}, shared with their permission", "COMMUNITY CLIP", f"CLIP BY {clips.on_video(name)}"
    return {
        "id": f"clip-{m['id']}",
        "kind": "clip",
        "launched": launched,
        "video": {"type": "discord", "url": c["att"]["url"], "filename": c["att"]["filename"]},
        "overlay": {"tag": tag, "credit": credit_line},
        "discord": {"msg": m["id"], "author": m["author"]["id"], "mine": mine},
        "caption": caption(body, source, launched),
    }


# ---------- Post selection ----------

def choose(state, t, ready_clips):
    """Returns the next post dict, or None. May update state (first-run seeding)."""
    today = t.date()
    launch = date.fromisoformat(CFG["launch_date"])

    release, coming_soon = sources.steam_release(APP)
    if release != launch:
        raise SystemExit(
            f"Steam release date is now {release} but config.json says {launch}. Update launch_date, "
            "launch_line and footer_line in config.json (and dated facts in content/evergreen.json), then re-run."
        )
    launched = not coming_soon
    if today > launch and coming_soon:
        raise SystemExit("Launch date passed but Steam still says coming soon. Check for a delay.")

    posted_ids = {p["id"] for p in state["posted"]}
    blocked = {pid for pid, n in state["failures"].items() if n >= MAX_FAILURES}

    def fresh(pid):
        return pid not in posted_ids and pid not in blocked and pid not in state["inflight"]

    today_posts = [p for p in state["posted"] if p["date"] == today.isoformat()]
    auto_today = [p for p in today_posts if p["kind"] != "clip"]
    auto_room = len(auto_today) < CFG["max_posts_per_day"]
    if not auto_room:
        log(f"Daily cap reached for auto posts ({len(auto_today)} today).")

    # 1. New official Steam announcements, any time of day.
    news = sources.steam_news(APP)
    if not state["steam_seeded"]:
        state["steam_seen"] = [n["gid"] for n in news]
        state["steam_seeded"] = True
        log(f"First run: marked {len(news)} existing Steam announcements as already seen.")
    for item in news:
        if auto_room and item["gid"] not in state["steam_seen"] and fresh(f"news-{item['gid']}"):
            return news_post(item, launched)

    # 2. New videos on the official YouTube channel (announced with a card, not reposted).
    try:
        vids = sources.youtube_uploads(env("YOUTUBE_API_KEY")) if env("YOUTUBE_API_KEY") else None
    except (requests.RequestException, KeyError, ValueError) as e:
        log(f"YouTube check skipped this run: {type(e).__name__}")  # optional source; never blocks posting
        vids = None
    if vids is not None:
        if not state["youtube_seeded"]:
            state["youtube_seen"] = [v["id"] for v in vids]
            state["youtube_seeded"] = True
            log(f"First run: marked {len(vids)} existing YouTube uploads as already seen.")
        for v in vids:
            if auto_room and v["id"] not in state["youtube_seen"] and fresh(f"youtube-{v['id']}"):
                return youtube_post(v, launched)

    # 3. Discord clips approved by the owner, any time of day.
    clips_today = [p for p in today_posts if p["kind"] == "clip"]
    if len(clips_today) < CFG["max_clips_per_day"]:
        for c in ready_clips:
            if fresh(f"clip-{c['msg']['id']}"):
                return clip_post(c, launched)

    if not auto_room:
        return None

    # 4. Official Steam trailers, only once SkyVu has OK'd reposting (config: official_trailers).
    if CFG["official_trailers"]:
        for tr in sources.steam_trailers(APP):
            if tr["id"] not in state["trailers_done"] and fresh(f"trailer-{tr['id']}"):
                return trailer_post(tr, launched)

    # 5. One scheduled post per day, at/after daily_post_hour: countdown beats fact.
    if t.hour < CFG["daily_post_hour"]:
        return None
    if any(p["kind"] in ("countdown", "fact") for p in today_posts):
        return None
    days_left = (launch - today).days
    if days_left in CFG["countdown_milestones"] and fresh(f"countdown-{days_left}"):
        return countdown_post(days_left, launched)
    for item in EVERGREEN:
        if not fresh(item["id"]) or (item.get("pre_launch_only") and today >= launch):
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


# ---------- State updates ----------

def mark_done(state, post, media_id):
    kind, pid = post["kind"], post["id"]
    if kind == "news":
        state["steam_seen"].append(pid.removeprefix("news-"))
    elif kind == "youtube":
        state["youtube_seen"].append(pid.removeprefix("youtube-"))
    elif kind == "trailer":
        state["trailers_done"].append(pid.removeprefix("trailer-"))
    elif kind == "clip":
        state["clips"].setdefault(post["discord"]["msg"], {"prompt": None})["status"] = "posted"
    state["failures"].pop(pid, None)
    state["inflight"].pop(pid, None)
    state["posted"].append({
        "id": pid, "kind": kind,
        "date": now().date().isoformat(), "at": now().isoformat(timespec="minutes"),
        "media_id": media_id,
    })


def drop_clip(state, post, reason):
    """Gives up on a clip for good and tells the submitter why."""
    msg = post["discord"]["msg"]
    state["clips"].setdefault(msg, {"prompt": None})["status"] = "rejected"
    state["failures"][post["id"]] = MAX_FAILURES
    dc = discord()
    if dc:
        try:
            ping = None if post["discord"]["mine"] else post["discord"]["author"]
            dc[0].reply(dc[1], msg, f"Sorry, this clip can't be posted: {reason}", ping=ping)
        except DiscordError as e:
            log(f"Discord reply failed: {e}")


def record_failure(state, post, reason="Instagram kept rejecting the video."):
    """Counts a failure caused by the post itself; at MAX_FAILURES the post is given up on."""
    n = state["failures"].get(post["id"], 0) + 1
    state["failures"][post["id"]] = n
    if n >= MAX_FAILURES and post["kind"] == "clip":
        drop_clip(state, post, reason)
    return n


def post_caused(e):
    """True if the error is about this post's media, not an outage, limit or expired token."""
    if isinstance(e, (ContainerError, video.VideoError)):
        return True
    return isinstance(e, InstagramError) and e.code is not None and e.code not in TRANSIENT_CODES


def reconcile(state):
    """Settles posts whose publish result was unclear last run (e.g. a timeout), so they're never doubled."""
    if not state["inflight"] or not env("IG_ACCESS_TOKEN"):
        return
    ig = Instagram(env("IG_ACCESS_TOKEN"))
    for pid, info in list(state["inflight"].items()):
        try:
            status = ig.container_status(info["container"])
        except (InstagramError, requests.RequestException, ValueError) as e:
            log(f"Couldn't check the earlier upload of {pid} yet: {type(e).__name__}")
            continue
        state["inflight"].pop(pid)
        if status != "PUBLISHED":
            continue
        post = {"id": pid, "kind": info["kind"], "discord": {"msg": pid.removeprefix("clip-")}}
        mark_done(state, post, None)
        log(f"{pid} had already been published; recorded it.")
        dc = discord()
        if dc and info["kind"] == "clip":
            try:
                dc[0].react(dc[1], post["discord"]["msg"], clips.POSTED)
            except DiscordError as e:
                log(f"Discord follow-up failed: {e}")


# ---------- Commands ----------

def cmd_prepare():
    PENDING_FILE.unlink(missing_ok=True)  # a leftover from a failed run must never be published later
    if not env("IG_ACCESS_TOKEN"):
        log("Instagram isn't connected yet (no IG_ACCESS_TOKEN secret), so the bot is idle.")
        set_output(has_post="false", needs_ffmpeg="false")
        return
    state = load_state()
    reconcile(state)
    ready, dc = [], discord()
    if dc:
        try:
            ready = clips.sync(dc[0], dc[1], dc[2], state)
        except DiscordError as e:
            log(f"Discord sync skipped: {e}")
        save_state(state)
    post = choose(state, now(), ready)
    save_state(state)
    if not post:
        log("Nothing to post this run.")
        set_output(has_post="false", needs_ffmpeg="false")
        return

    WORK.mkdir(parents=True, exist_ok=True)
    if post["kind"] == "clip":
        src = WORK / ("clip" + (Path(post["video"]["filename"]).suffix.lower() or ".mp4"))
        try:
            dc[0].download(post["video"]["url"], src, CFG["max_clip_mb"] * 1024 * 1024)
        except DiscordError:  # only raised for oversized files
            drop_clip(state, post, f"it's bigger than {CFG['max_clip_mb']} MB.")
            save_state(state)
            set_output(has_post="false", needs_ffmpeg="false")
            return
        except requests.RequestException as e:
            # Never log str(e): it contains the signed attachment URL and the player's filename.
            status = getattr(getattr(e, "response", None), "status_code", None)
            log(f"Clip download failed ({type(e).__name__} {status or ''}); will retry next run.")
            if status and 400 <= status < 500:  # the file itself is gone or forbidden, not an outage
                record_failure(state, post, "the video couldn't be downloaded from Discord. Try posting it again.")
                save_state(state)
            set_output(has_post="false", needs_ffmpeg="false")
            return
        post["video"] = {"type": "file", "path": str(src)}  # don't keep the signed Discord URL
    if not post.get("video"):
        post["image"] = str(render_post(post, WORK))
        log(f"Prepared {post['id']}\n\n{post['caption']}")
    else:
        log(f"Prepared {post['id']} (video)")  # clip captions name players; keep them out of public logs
    PENDING_FILE.write_text(json.dumps(post, indent=2))
    set_output(has_post="true", post_id=post["id"], needs_ffmpeg=str(bool(post.get("video"))).lower())


def cmd_render_video():
    post = json.loads(PENDING_FILE.read_text()) if PENDING_FILE.exists() else {}
    if not post.get("video"):
        log("No pending video to render.")
        return
    v = post["video"]
    cfg = dict(CFG, footer_line=CFG["post_launch_footer"]) if post["launched"] else CFG
    try:
        src = Path(v["path"]) if v["type"] == "file" else video.download_hls(v["url"], WORK / "trailer.mp4")
        overlay = render.render_reel_overlay(cfg, post["overlay"]["tag"], post["overlay"]["credit"], WORK / "overlay.png")
        reel = video.render_reel(src, overlay, WORK / f"{post['id']}.mp4", CFG["max_video_seconds"])
        post["reel"] = str(reel)
        post["cover"] = str(video.cover(reel, WORK / f"{post['id']}.jpg"))
    except video.VideoError as e:
        state = load_state()
        if post["kind"] == "clip":
            short = str(e) if "Instagram needs" in str(e) or str(e) == "no video stream" else "the video file couldn't be processed."
            drop_clip(state, post, short)
        else:
            record_failure(state, post)
        save_state(state)
        PENDING_FILE.unlink()
        raise SystemExit(f"Video render failed for {post['id']}: {e}")
    PENDING_FILE.write_text(json.dumps(post, indent=2))
    log(f"Rendered {post['id']}: {Path(post['reel']).stat().st_size / 1e6:.1f} MB")


def wait_public(url):
    for _ in range(6):
        if requests.head(url, timeout=30).status_code == 200:
            return
        time.sleep(5)
    raise RuntimeError("media not publicly reachable yet")


def publish_media(ig, post, on_container):
    if "reel" in post:
        urls = hosting.push_media([post["reel"], post["cover"]])
        reel_url, cover_url = urls[Path(post["reel"]).name], urls[Path(post["cover"]).name]
        wait_public(reel_url)
        try:
            return ig.publish_reel(reel_url, post["caption"], cover_url, on_container)
        except ContainerError as e:
            if not e.fetch_failed:
                raise
            log(f"Instagram couldn't use the raw.githubusercontent.com video ({e}); retrying via a Release asset.")
        alt = hosting.release_asset(post["reel"])
        try:
            return ig.publish_reel(alt, post["caption"], cover_url, on_container)
        finally:
            hosting.remove_release_asset(post["reel"])
    if "video" in post:
        raise SystemExit("Pending video post was never rendered (run render-video first).")
    url = hosting.push_media([post["image"]])[Path(post["image"]).name]
    wait_public(url)
    return ig.publish_image(url, post["caption"], on_container)


def announce(post, permalink):
    """Discord follow-ups after a successful post. Failures here never undo the post."""
    dc = discord()
    if not dc:
        return
    client, channel, _, feed = dc
    steps = []
    if post["kind"] == "clip":
        d = post["discord"]
        steps.append(lambda: client.react(channel, d["msg"], clips.POSTED))
        if not d["mine"]:
            where = permalink or "the BBG News Instagram"
            steps.append(lambda: client.reply(channel, d["msg"], f"<@{d['author']}> your clip is live on {where} 🙌",
                                              ping=d["author"]))
    if feed:
        first = post["caption"].split("\n", 1)[0]
        steps.append(lambda: client.send(feed, f"**New on BBG News:** {first}\n{permalink or ''}".strip(),
                                         file_path=post.get("cover") or post.get("image")))
    for step in steps:
        try:
            step()
        except DiscordError as e:
            log(f"Discord follow-up failed: {e}")


def cmd_publish():
    if not PENDING_FILE.exists():
        log("Nothing to publish.")
        return
    post = json.loads(PENDING_FILE.read_text())
    if not env("IG_ACCESS_TOKEN"):
        raise SystemExit("IG_ACCESS_TOKEN is not set. Add it as a GitHub Actions secret.")
    ig = Instagram(env("IG_ACCESS_TOKEN"))
    state = load_state()

    def on_container(container):
        state["inflight"][post["id"]] = {"container": container, "kind": post["kind"]}
        save_state(state)

    try:
        media_id = publish_media(ig, post, on_container)
    except CopyrightMatch:
        if post["kind"] == "clip":
            drop_clip(state, post, "Instagram's copyright check flagged it (usually background music). "
                                   "Try a clip without music.")
        else:
            state["failures"][post["id"]] = MAX_FAILURES
        save_state(state)
        PENDING_FILE.unlink()
        log(f"Skipped {post['id']}: Instagram copyright match.")
        return
    except BaseException as e:
        if post_caused(e):
            n = record_failure(state, post)
            log(f"Publish failed for {post['id']} (attempt {n}/{MAX_FAILURES}).")
        else:
            log(f"Publish failed for {post['id']} for a reason unrelated to the post; it will be retried.")
        save_state(state)
        raise

    mark_done(state, post, media_id)
    save_state(state)  # saved before any Discord follow-up, so a failure there can't cause a repost
    PENDING_FILE.unlink()
    permalink = ig.permalink(media_id)
    log(f"Published {post['id']} as Instagram media {media_id} {permalink or ''}")
    announce(post, permalink)


def cmd_preview():
    PREVIEW.mkdir(parents=True, exist_ok=True)
    posts = [countdown_post(n, False) for n in (21, 1, 0)]
    posts += [fact_post(i, False) for i in EVERGREEN]
    posts.append(youtube_post({"id": "example", "title": "Battle Bears Gold: Example Video Title"}, False))
    try:
        posts += [news_post(n, False) for n in sources.steam_news(APP)[-2:]]
    except requests.RequestException as e:
        log(f"Skipping Steam news preview: {e}")
    lines = []
    for p in posts:
        path = render_post(p, PREVIEW)
        lines.append(f"## {p['id']}\n\n![]({path.name})\n\n```\n{p['caption']}\n```\n")

    if shutil.which("ffmpeg"):
        fake_clip = {"msg": {"id": "example", "author": {"id": "1", "username": "player"}},
                     "att": {"url": "", "filename": "clip.mp4"}, "caption": None, "mine": False, "credit": "@your.handle"}
        samples = [trailer_post(t, False) for t in sources.steam_trailers(APP)[:1]]
        samples.append(clip_post(fake_clip, launched=False))
        WORK.mkdir(parents=True, exist_ok=True)
        src = video.download_hls(sources.steam_trailers(APP)[0]["hls"], WORK / "trailer.mp4")
        for p in samples:
            overlay = render.render_reel_overlay(CFG, p["overlay"]["tag"], p["overlay"]["credit"], WORK / "overlay.png")
            reel = video.render_reel(src, overlay, PREVIEW / f"{p['id']}.mp4", 10)
            video.cover(reel, PREVIEW / f"{p['id']}.jpg")
            lines.append(f"## {p['id']} (10s sample)\n\n![]({p['id']}.jpg)\n\n```\n{p['caption']}\n```\n")
    else:
        log("ffmpeg not found: skipping Reel previews.")
    (PREVIEW / "captions.md").write_text("\n".join(lines))
    log(f"Rendered previews to {PREVIEW}")


def cmd_refresh_token():
    if not env("IG_ACCESS_TOKEN"):
        raise SystemExit("IG_ACCESS_TOKEN is not set.")
    print(Instagram(env("IG_ACCESS_TOKEN")).refresh_token())


if __name__ == "__main__":
    commands = {
        "prepare": cmd_prepare,
        "render-video": cmd_render_video,
        "publish": cmd_publish,
        "preview": cmd_preview,
        "refresh-token": cmd_refresh_token,
    }
    if len(sys.argv) != 2 or sys.argv[1] not in commands:
        raise SystemExit(__doc__)
    commands[sys.argv[1]]()
