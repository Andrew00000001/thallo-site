"""BBG News auto-poster.

  python bot.py prepare           pick the next post (or the clip sent from Discord), write .pending.json
  python bot.py render-video      turn the pending clip/trailer into a Reel (needs ffmpeg)
  python bot.py publish           host the media, publish to Instagram, update state
  python bot.py preview           render every post type to out/preview/ (nothing is posted)
  python bot.py refresh-token     print a refreshed long-lived Instagram token to stdout
  python bot.py register-command  create the Discord "Send to BBG News" command (one time)
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
import discord_api
from discord_api import DiscordError
from instagram import TRANSIENT_CODES, ContainerError, CopyrightMatch, Instagram, InstagramError

ROOT = Path(__file__).parent
CFG = json.loads((ROOT / "config.json").read_text())
EVERGREEN = json.loads((ROOT / "content/evergreen.json").read_text())
STATE_FILE = ROOT / "state/state.json"
PENDING_FILE = ROOT / ".pending.json"
TOLD_FILE = ROOT / ".told"  # set once the owner's Discord reply has a final answer for this run
PREVIEW = ROOT / "out/preview"
WORK = Path(os.environ.get("RUNNER_TEMP") or tempfile.gettempdir()) / "bbg-work"
TZ = ZoneInfo(CFG["timezone"])
APP = CFG["steam_app_id"]
CAPTION_LIMIT = 2200
MAX_FAILURES = 3
STATE_DEFAULTS = {
    "steam_seeded": False, "steam_seen": [],
    "youtube_seeded": False, "youtube_seen": [],
    "trailers_done": [], "failures": {}, "inflight": {}, "posted": [],
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


def clip_post(clip, launched):
    """A clip the owner sent from Discord with the player's OK (see clips.py)."""
    name = clip["credit"]
    if clip["own"]:
        body = clip["caption"] or "🎥 Fresh Battle Bears Gold gameplay."
        source, tag, credit_line = "BBG News gameplay", "GAMEPLAY", "BBG NEWS GAMEPLAY"
    else:
        intro = f"{clip['caption']}\n\n" if clip["caption"] else ""
        body = (f"{intro}🎥 Community clip by {name}!\n\n"
                "Want your clip featured? Send it to us on the Battle Bears Discord.")
        source, tag = f"Clip by {name}, shared with their permission", "COMMUNITY CLIP"
        credit_line = f"CLIP BY {clips.on_video(name)}"
    return {
        "id": f"clip-{clip['attachment_id']}",
        "kind": "clip",
        "launched": launched,
        "video": {"type": "discord", "url": clip["url"], "filename": clip["filename"]},
        "overlay": {"tag": tag, "credit": credit_line},
        "notify": clip["notify"],
        "caption": caption(body, source, launched),
    }


# ---------- Post selection ----------

def launch_status(today):
    """True once Steam says the game is out. Stops everything if Steam's date no longer matches the
    config, because captions and cards quote that date."""
    launch = date.fromisoformat(CFG["launch_date"])
    release, coming_soon = sources.steam_release(APP)
    if release != launch:
        raise SystemExit(
            f"Steam release date is now {release} but config.json says {launch}. Update launch_date, "
            "launch_line and footer_line in config.json (and dated facts in content/evergreen.json), then re-run."
        )
    if today > launch and coming_soon:
        raise SystemExit("Launch date passed but Steam still says coming soon. Check for a delay.")
    return not coming_soon


def choose(state, t):
    """Returns the next automatic post, or None. May update state (first-run seeding)."""
    today = t.date()
    launch = date.fromisoformat(CFG["launch_date"])
    launched = launch_status(today)

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

    if not auto_room:
        return None

    # 3. Official Steam trailers, only once SkyVu has OK'd reposting (config: official_trailers).
    if CFG["official_trailers"]:
        for tr in sources.steam_trailers(APP):
            if tr["id"] not in state["trailers_done"] and fresh(f"trailer-{tr['id']}"):
                return trailer_post(tr, launched)

    # 4. One scheduled post per day, at/after daily_post_hour: countdown beats fact.
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
    state["failures"].pop(pid, None)
    state["inflight"].pop(pid, None)
    state["posted"].append({
        "id": pid, "kind": kind,
        "date": now().date().isoformat(), "at": now().isoformat(timespec="minutes"),
        "media_id": media_id,
    })


def tell(post_or_notify, message):
    """Updates the owner's private Discord reply for a clip they sent (no-op for other posts).
    Returns False if the reply couldn't be updated (its 15-minute window may have passed)."""
    notify = post_or_notify.get("notify") if isinstance(post_or_notify, dict) else post_or_notify
    if not notify:
        return True
    TOLD_FILE.touch()
    if discord_api.edit_reply(notify, message):
        return True
    log("Couldn't update the Discord reply (its 15-minute window may have passed).")
    return False


def refuse(post_or_notify, message):
    """Tells the owner a clip wasn't posted. If Discord can't show it any more, fails the run instead,
    so GitHub emails the owner rather than the clip disappearing silently."""
    if not tell(post_or_notify, message):
        raise SystemExit(f"Clip not posted, and the Discord reply had expired: {message}")


def record_failure(state, post):
    """Counts a failure caused by the post itself; at MAX_FAILURES the post is given up on."""
    n = state["failures"].get(post["id"], 0) + 1
    state["failures"][post["id"]] = n
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
        mark_done(state, {"id": pid, "kind": info["kind"]}, None)
        log(f"{pid} had already been published; recorded it.")


# ---------- Commands ----------

def cmd_prepare():
    PENDING_FILE.unlink(missing_ok=True)  # a leftover from a failed run must never be published later
    TOLD_FILE.unlink(missing_ok=True)
    inputs = clips.dispatch_inputs()
    if not env("IG_ACCESS_TOKEN"):
        set_output(has_post="false", needs_ffmpeg="false")
        if inputs.get("clip_url"):
            tell(inputs.get("notify", ""), "❌ Not posted: Instagram isn't connected yet (add the IG_ACCESS_TOKEN secret on GitHub).")
            raise SystemExit("A clip was sent, but the IG_ACCESS_TOKEN secret is missing.")
        log("Instagram isn't connected yet (no IG_ACCESS_TOKEN secret), so the bot is idle.")
        return
    if inputs.get("clip_url"):
        return prepare_clip(inputs)
    state = load_state()
    reconcile(state)
    post = choose(state, now())
    save_state(state)
    if not post:
        log("Nothing to post this run.")
        set_output(has_post="false", needs_ffmpeg="false")
        return
    WORK.mkdir(parents=True, exist_ok=True)
    if not post.get("video"):
        post["image"] = str(render_post(post, WORK))
    log(f"Prepared {post['id']}\n\n{post['caption']}")
    PENDING_FILE.write_text(json.dumps(post, indent=2))
    set_output(has_post="true", post_id=post["id"], needs_ffmpeg=str(bool(post.get("video"))).lower())


def prepare_clip(inputs):
    """A clip the owner sent with the Discord app. Posted right away; the owner hears back in Discord.
    Clip details stay out of the public run log (players' names, signed links, the reply token)."""
    set_output(has_post="false", needs_ffmpeg="false")
    notify = inputs.get("notify", "")
    try:
        clip = clips.parse(inputs)
    except ValueError as e:
        log(f"Clip rejected: {e}")
        refuse(notify, f"❌ Not posted: {e}")
        return
    state = load_state()
    reconcile(state)
    save_state(state)
    pid = f"clip-{clip['attachment_id']}"
    if pid in {p["id"] for p in state["posted"]}:
        log(f"{pid} was already posted.")
        refuse(notify, "ℹ️ That clip is already on BBG News.")
        return
    if pid in state["inflight"]:
        log(f"{pid} is still unconfirmed; not reposting.")
        refuse(notify, "⏳ Still can't confirm whether the earlier attempt went live. Check the BBG News "
                       "Instagram, and send it again in a few minutes if it isn't there.")
        return
    try:
        launched = launch_status(now().date())
    except SystemExit:
        tell(notify, "⏸️ Posting is paused because Steam's release date changed. Check the bot on GitHub.")
        raise
    except Exception as e:  # Steam down or rate-limited: captions quote its date, so don't guess
        tell(notify, f"❌ Not posted: couldn't check Steam right now ({type(e).__name__}). Send it again in a few minutes.")
        raise
    post = clip_post(clip, launched)
    WORK.mkdir(parents=True, exist_ok=True)
    src = WORK / ("clip" + (Path(clip["filename"]).suffix.lower() or ".mp4"))
    try:
        discord_api.download(clip["url"], src, CFG["max_clip_mb"] * 1024 * 1024)
    except DiscordError:  # only raised for oversized files
        log("Clip download refused: file too big.")
        refuse(post, f"❌ Not posted: the file is bigger than {CFG['max_clip_mb']} MB.")
        return
    except requests.RequestException as e:
        # Never log str(e): it contains the signed attachment link.
        status = getattr(getattr(e, "response", None), "status_code", None)
        log(f"Clip download failed ({type(e).__name__} {status or ''}).")
        refuse(post, f"❌ Couldn't download the clip from Discord ({status or type(e).__name__}). Send it again.")
        return
    post["video"] = {"type": "file", "path": str(src)}  # don't keep the signed link
    PENDING_FILE.write_text(json.dumps(post, indent=2))
    log(f"Prepared {pid} (clip sent from Discord)")
    set_output(has_post="true", post_id=pid, needs_ffmpeg="true")


def cmd_render_video():
    post = json.loads(PENDING_FILE.read_text()) if PENDING_FILE.exists() else {}
    if not post.get("video"):
        log("No pending video to render.")
        return
    v = post["video"]
    cfg = dict(CFG, footer_line=CFG["post_launch_footer"]) if post["launched"] else CFG
    try:
        src = Path(v["path"]) if v["type"] == "file" else video.download_hls(v["url"], WORK / "trailer.mp4")
        post["trimmed"] = video.probe(src)[0] > CFG["max_video_seconds"]
        overlay = render.render_reel_overlay(cfg, post["overlay"]["tag"], post["overlay"]["credit"], WORK / "overlay.png")
        reel = video.render_reel(src, overlay, WORK / f"{post['id']}.mp4", CFG["max_video_seconds"])
        post["reel"] = str(reel)
        post["cover"] = str(video.cover(reel, WORK / f"{post['id']}.jpg"))
    except video.VideoError as e:
        PENDING_FILE.unlink()
        if post["kind"] == "clip":
            short = str(e) if "Instagram needs" in str(e) or str(e) == "no video stream" else "the video file couldn't be processed"
            log(f"Clip not usable: {short}")
            refuse(post, f"❌ Not posted: {short}.")
            return
        state = load_state()
        record_failure(state, post)
        save_state(state)
        raise SystemExit(f"Video render failed for {post['id']}: {e}")
    except Exception as e:
        PENDING_FILE.unlink()
        tell(post, f"❌ Not posted: making the Reel failed ({type(e).__name__}). Send it again in a few minutes.")
        raise
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
        if post["kind"] != "clip":
            state["failures"][post["id"]] = MAX_FAILURES
        save_state(state)
        PENDING_FILE.unlink()
        log(f"Skipped {post['id']}: Instagram copyright match.")
        if post["kind"] == "clip":
            refuse(post, "❌ Not posted: Instagram's copyright check flagged it (usually background music).")
        return
    except BaseException as e:
        if post["kind"] == "clip" and post["id"] in state["inflight"]:
            tell(post, "⚠️ Instagram didn't confirm the post. Check the BBG News Instagram before sending it "
                       "again; the bot records it automatically if it went through.")
        elif post["kind"] == "clip":  # the owner re-sends it; no automatic retries
            reason = str(e) if isinstance(e, InstagramError) else type(e).__name__
            tell(post, f"❌ Couldn't post it ({reason}). Try sending it again in a few minutes.")
        elif post_caused(e):
            n = record_failure(state, post)
            log(f"Publish failed for {post['id']} (attempt {n}/{MAX_FAILURES}).")
        else:
            log(f"Publish failed for {post['id']} for a reason unrelated to the post; it will be retried.")
        save_state(state)
        raise

    mark_done(state, post, media_id)
    save_state(state)  # saved before the Discord update, so a failure there can't cause a repost
    PENDING_FILE.unlink()
    permalink = ig.permalink(media_id)
    log(f"Published {post['id']} as Instagram media {media_id} {permalink or ''}")
    note = f" (only the first {CFG['max_video_seconds']} seconds were used)" if post.get("trimmed") else ""
    tell(post, (f"✅ Posted to Instagram: {permalink}" if permalink else "✅ Posted to Instagram.") + note)


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
        fake_clip = {"url": "", "attachment_id": "example", "filename": "clip.mp4", "credit": "@your.handle",
                     "own": False, "caption": "", "notify": ""}
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


def cmd_clip_failed():
    """Last workflow step when a clip run fails: make sure the owner isn't left on "Sent"."""
    notify = clips.dispatch_inputs().get("notify", "")
    if notify and not TOLD_FILE.exists():
        tell(notify, "❌ Not posted: something went wrong on GitHub. Send it again in a few minutes.")


def cmd_register_command():
    app_id = str(CFG.get("discord_app_id", "")).strip()
    if not (app_id and env("DISCORD_BOT_TOKEN")):
        raise SystemExit("Set discord_app_id in config.json and the DISCORD_BOT_TOKEN secret first.")
    try:
        commands = discord_api.register_command(app_id, env("DISCORD_BOT_TOKEN"))
    except DiscordError as e:
        raise SystemExit(f"Couldn't register the command: {e}")
    log("Registered: " + ", ".join(c["name"] for c in commands))


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
        "register-command": cmd_register_command,
        "clip-failed": cmd_clip_failed,
    }
    if len(sys.argv) != 2 or sys.argv[1] not in commands:
        raise SystemExit(__doc__)
    commands[sys.argv[1]]()
