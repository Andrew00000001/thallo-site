"""Discord clip submissions: consent, owner approval, and credits.

Flow in the #submit-clips channel:
  1. Someone posts a video. The bot reacts 👀 and replies with a clip request that states the
     exact credit. Everything is decided by reactions on that reply, which players can't edit.
  2. The player reacts 👍 on the request (their explicit go-ahead to post it).
  3. The owner reacts ✅ on the request to post it, or ❌ to skip it.
  4. The bot posts it as a Reel, replies with the link and reacts 📸 on the clip.
If the clip message is edited after the request was sent, the old request is deleted and a new
one is sent, so nobody's earlier 👍/✅ carries over to changed content. The owner's own clips
only need ✅. An owner reply to the clip starting with "caption:" sets the caption.
"""
import re
import sys
from datetime import datetime

from discord_api import DiscordError

SEEN, CONSENT, APPROVE, REJECT, POSTED = "👀", "👍", "✅", "❌", "📸"
MARKER = "BBG News clip request"
VIDEO_EXT = (".mp4", ".mov", ".m4v", ".webm", ".mkv")
MAX_REFETCH = 20  # pending clips pushed out of the newest-100 window that are fetched one by one

PLAYER_PROMPT = (
    "<@{author}> thanks for the clip! 🎥 ({marker})\n"
    "**Player:** react {consent} on **this message** to confirm it's your own gameplay and that you want "
    "BBG News to post it publicly on Instagram and in this server's feed channel, credited as `{credit}`.\n"
    "Want a different credit? Edit your clip message to add `ig: @yourhandle` and you'll get a new request.\n"
    "**Owner:** react {approve} to post it or {reject} to skip it.\n"
    "Only the first video in a message is used. To get a posted clip taken down, just ask here."
)
OWNER_PROMPT = "{marker}: react {approve} to post this clip or {reject} to skip it."


def log(msg):
    print(msg, file=sys.stderr)


def video_attachment(msg):
    for a in msg.get("attachments", []):
        if (a.get("content_type") or "").startswith("video/") or a["filename"].lower().endswith(VIDEO_EXT):
            return a
    return None


def ig_handle(text):
    """`ig: @name` (or `ig @name`, `IG:@name`) in the message text."""
    m = re.search(r"(?i)\big\s*[:=]?\s*@([a-z0-9._]{1,30})", text or "")
    return m.group(1).rstrip(".") if m else None


def credit_for(msg):
    """Caption credit for a submission: @handle if given, else the Discord display name."""
    handle = ig_handle(msg.get("content"))
    if handle:
        return f"@{handle}"
    author = msg["author"]
    return (author.get("global_name") or author["username"]).replace("`", "").strip() or author["username"]


def on_video(credit):
    """Credit text burned into the Reel (the fonts only cover ASCII)."""
    text = "".join(c for c in credit if c.isascii() and c.isprintable()).strip()
    return (text or "A BBG PLAYER").upper()


def prompt_credit(prompt):
    m = re.search(r"credited as `([^`]*)`", prompt.get("content", ""))
    return m.group(1) if m else None


def _ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def _bot_reacted(msg, emoji):
    return any(r["emoji"]["name"] == emoji and r.get("me") for r in msg.get("reactions", []))


def _others(msg, prefix):
    """Reaction names starting with `prefix` that someone other than the bot added."""
    return [r["emoji"]["name"] for r in msg.get("reactions", [])
            if r["emoji"]["name"].startswith(prefix) and r["count"] - (1 if r.get("me") else 0) > 0]


def _reacted_by(dc, channel, msg, prefix, user):
    """Whether `user` reacted with `prefix` (any skin tone of it) on `msg`."""
    return any(user in dc.reaction_users(channel, msg["id"], name) for name in _others(msg, prefix))


def _send_prompt(dc, channel, clip, mine):
    if mine:
        text = OWNER_PROMPT.format(marker=MARKER, approve=APPROVE, reject=REJECT)
        ping, emojis = None, (APPROVE, REJECT)
    else:
        text = PLAYER_PROMPT.format(author=clip["author"]["id"], marker=MARKER, consent=CONSENT,
                                    credit=credit_for(clip), approve=APPROVE, reject=REJECT)
        ping, emojis = clip["author"]["id"], (CONSENT, APPROVE, REJECT)
    prompt = dc.reply(channel, clip["id"], text, ping=ping)
    for e in emojis:  # one tap for the player/owner, and the exact 👍 the bot checks for
        dc.react(channel, prompt["id"], e)
    return prompt


def _process(dc, channel, owner, rec, m, by_id):
    """Returns True when the clip is consented to and approved."""
    if not _bot_reacted(m, SEEN):
        try:
            dc.react(channel, m["id"], SEEN)
        except DiscordError as e:
            log(f"Couldn't mark clip {m['id']} as seen: {e}")
    mine = m["author"]["id"] == owner
    prompt = None
    if rec["prompt"]:
        prompt = by_id.get(rec["prompt"]) or dc.message(channel, rec["prompt"])
    if prompt and m.get("edited_timestamp") and _ts(m["edited_timestamp"]) > _ts(prompt["timestamp"]):
        try:
            dc.delete(channel, prompt["id"])
        except DiscordError as e:
            log(f"Couldn't delete outdated request {prompt['id']}: {e}")
        prompt = None
    if prompt is None:
        rec["prompt"] = _send_prompt(dc, channel, m, mine)["id"]
        return False  # a fresh request has no reactions yet
    if _reacted_by(dc, channel, prompt, REJECT, owner):
        return False
    if not _reacted_by(dc, channel, prompt, APPROVE, owner):
        return False
    return mine or _reacted_by(dc, channel, prompt, CONSENT, m["author"]["id"])


def sync(dc, channel, owner, state):
    """Processes submissions and returns approved clips ready to post, oldest first.

    Every run re-checks every pending clip, so approvals given at any time are picked up.
    Only bare message IDs are kept in state (the repo is public).
    """
    by_id = {m["id"]: m for m in dc.messages(channel)}
    clips = state["clips"]
    refetched = 0
    for mid, rec in list(clips.items()):
        if mid in by_id:
            continue
        if rec["status"] != "pending" or refetched >= MAX_REFETCH:
            del clips[mid]
            continue
        refetched += 1  # pending but pushed out of the window by newer messages
        for pid in (mid, rec.get("prompt")):
            if pid and pid not in by_id and (m := dc.message(channel, pid)):
                by_id[pid] = m
        if mid not in by_id:
            del clips[mid]  # deleted by its author
    msgs = sorted(by_id.values(), key=lambda m: int(m["id"]))  # IDs are time-ordered

    captions, prompts = {}, {}
    for m in msgs:
        ref = (m.get("message_reference") or {}).get("message_id")
        if not ref:
            continue
        if m["author"]["id"] == owner and m.get("content", "").lower().startswith("caption:"):
            captions[ref] = m["content"][len("caption:"):].strip()
        if m["author"].get("bot") and MARKER in m.get("content", ""):
            prompts[ref] = m["id"]  # newest request wins; recovers prompts if state was lost

    ready = []
    for m in msgs:
        if m["author"].get("bot") or not (att := video_attachment(m)):
            continue
        rec = clips.setdefault(m["id"], {"status": "pending", "prompt": prompts.get(m["id"])})
        if _bot_reacted(m, POSTED):
            rec["status"] = "posted"
        if rec["status"] != "pending":
            continue
        try:
            if not _process(dc, channel, owner, rec, m, by_id):
                continue
            prompt = by_id.get(rec["prompt"]) or dc.message(channel, rec["prompt"])
        except DiscordError as e:
            log(f"Skipping clip {m['id']} this run: {e}")
            continue
        mine = m["author"]["id"] == owner
        ready.append({
            "msg": m, "att": att, "mine": mine, "caption": captions.get(m["id"]),
            "credit": None if mine else prompt_credit(prompt) or credit_for(m),
        })
    return ready
