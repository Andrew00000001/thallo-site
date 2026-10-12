"""Discord clip submissions: consent prompts, owner approval, and credits.

Flow in the #submit-clips channel:
  1. A player posts a video. The bot reacts 👀 and replies with a consent prompt.
  2. The player reacts 👍 on that prompt (their explicit go-ahead to post it on Instagram).
  3. The owner reacts ✅ on the clip to approve it, or ❌ to reject it.
  4. The bot posts it as a Reel, replies with the link, and reacts 📸.
The owner's own clips skip step 2. An owner reply starting with "caption:" sets the caption.
"""
import re

SEEN, CONSENT, APPROVE, REJECT, POSTED = "👀", "👍", "✅", "❌", "📸"
VIDEO_EXT = (".mp4", ".mov", ".m4v", ".webm", ".mkv")

CONSENT_TEXT = (
    "<@{author}> thanks for the clip! 🎥\n"
    "To let **BBG News** post it on Instagram, react {consent} to **this message**. By reacting you confirm:\n"
    "• it's your own gameplay recording, and\n"
    "• you want BBG News to post it publicly on Instagram, credited to your Discord name "
    "(or your Instagram handle if you add `ig: @yourhandle` to your clip message).\n"
    "The BBG News owner reviews every clip before it's posted. To get a posted clip taken down, just ask here."
)


def video_attachment(msg):
    for a in msg.get("attachments", []):
        if (a.get("content_type") or "").startswith("video/") or a["filename"].lower().endswith(VIDEO_EXT):
            return a
    return None


def ig_handle(text):
    """`ig: @name` (or `ig @name`, `IG:@name`) in the message text."""
    m = re.search(r"(?i)\big\s*[:=]?\s*@([a-z0-9._]{1,30})", text or "")
    return m.group(1).rstrip(".") if m else None


def credit(msg):
    """(caption credit, on-video credit) for a submission."""
    handle = ig_handle(msg.get("content"))
    if handle:
        return f"@{handle}", f"@{handle}".upper()
    author = msg["author"]
    name = author.get("global_name") or author["username"]
    ascii_name = "".join(c for c in name if c.isascii() and c.isprintable()).strip()
    return name, (ascii_name or "A BBG PLAYER").upper()


def _reacted(msg, emoji):
    return any(r["emoji"]["name"] == emoji for r in msg.get("reactions", []))


def _bot_reacted(msg, emoji):
    return any(r["emoji"]["name"] == emoji and r.get("me") for r in msg.get("reactions", []))


def sync(dc, channel, owner, state):
    """Processes the newest 100 messages. Returns approved clips ready to post, oldest first.

    Every run re-checks all pending clips in the window, so approvals given at any
    time are picked up. Only bare message IDs are kept in state (the repo is public).
    """
    msgs = list(reversed(dc.messages(channel)))  # oldest first
    clips = state["clips"]
    in_window = {m["id"] for m in msgs}
    for mid in list(clips):
        if mid not in in_window:
            del clips[mid]

    captions, prompts = {}, {}
    for m in msgs:
        ref = (m.get("message_reference") or {}).get("message_id")
        if not ref:
            continue
        if m["author"]["id"] == owner and m.get("content", "").lower().startswith("caption:"):
            captions[ref] = m["content"][len("caption:"):].strip()
        if m["author"].get("bot") and "thanks for the clip" in m.get("content", ""):
            prompts[ref] = m["id"]

    ready = []
    for m in msgs:
        if m["author"].get("bot"):
            continue
        att = video_attachment(m)
        if not att:
            continue
        author = m["author"]["id"]
        rec = clips.get(m["id"])
        if rec is None:
            rec = clips[m["id"]] = {"status": "pending", "prompt": prompts.get(m["id"])}
        if _bot_reacted(m, POSTED):
            rec["status"] = "posted"
        if rec["status"] != "pending":
            continue
        if not _bot_reacted(m, SEEN):
            dc.react(channel, m["id"], SEEN)
        if author != owner and not rec["prompt"]:
            rec["prompt"] = dc.reply(
                channel, m["id"], CONSENT_TEXT.format(author=author, consent=CONSENT), ping=author
            )["id"]

        if _reacted(m, REJECT) and owner in dc.reaction_users(channel, m["id"], REJECT):
            rec["status"] = "rejected"
            continue
        if not (_reacted(m, APPROVE) and owner in dc.reaction_users(channel, m["id"], APPROVE)):
            continue
        if author != owner and author not in dc.reaction_users(channel, rec["prompt"], CONSENT):
            continue
        ready.append({"msg": m, "att": att, "caption": captions.get(m["id"])})
    return ready
