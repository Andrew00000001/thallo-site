"""Clips sent from Discord with the "Send to BBG News" app (see relay/worker.js).

The owner long-presses a clip in any server they're in, confirms the player's OK and the
credit in a form, and the relay starts this repo's workflow with these inputs:
  clip_url  the Discord attachment link (signed, expires; downloaded right away)
  credit    shown on the Reel and in the caption; "BBG News" means the owner's own clip
  caption   optional text for the caption
  notify    "<application id>/<interaction token>" to update the owner's private Discord reply
"""
import json
import os
import re

CLIP_URL = re.compile(
    r"^https://(?:cdn\.discordapp\.com|media\.discordapp\.net)/attachments/(\d+)/(\d+)/([^\s/?#]+)(?:\?\S*)?$"
)
OWN_CREDIT = "bbg news"


def dispatch_inputs():
    """Inputs of a manual/relay-started run, read from the event file so they never hit the log."""
    if os.environ.get("GITHUB_EVENT_NAME") != "workflow_dispatch" or not os.environ.get("GITHUB_EVENT_PATH"):
        return {}
    with open(os.environ["GITHUB_EVENT_PATH"]) as f:
        return json.load(f).get("inputs") or {}


def parse(inputs):
    """Validated clip details, or raises ValueError with a message for the owner."""
    url = (inputs.get("clip_url") or "").strip()
    m = CLIP_URL.match(url)
    if not m:
        raise ValueError("that isn't a Discord attachment link.")
    credit = " ".join((inputs.get("credit") or "").split())[:60]
    if not credit:
        raise ValueError("the credit is empty.")
    return {
        "url": url,
        "attachment_id": m.group(2),
        "filename": m.group(3),
        "credit": credit,
        "own": credit.lower() == OWN_CREDIT,
        "caption": (inputs.get("caption") or "").strip()[:1000],
        "notify": (inputs.get("notify") or "").strip(),
    }


def on_video(credit):
    """Credit text burned into the Reel (the fonts only cover ASCII)."""
    text = "".join(c for c in credit if c.isascii() and c.isprintable()).strip()
    return (text or "A BBG PLAYER").upper()
