"""The few Discord calls the bot makes. None of them logs URLs or tokens."""
import os
import re

import requests

API = "https://discord.com/api/v10"
COMMAND = {"name": "Send to BBG News", "type": 3, "integration_types": [1], "contexts": [0, 1, 2]}


class DiscordError(RuntimeError):
    pass


def _ua():
    return f"DiscordBot (https://github.com/{os.environ.get('GITHUB_REPOSITORY', 'bbg-news')}, 1.0)"


def download(url, dest, max_bytes):
    """Streams an attachment to `dest`. Raises DiscordError if it's bigger than max_bytes,
    requests exceptions otherwise (callers must not log them: they contain the signed URL)."""
    with requests.get(url, stream=True, timeout=120) as r:
        r.raise_for_status()
        size = 0
        with open(dest, "wb") as f:
            for chunk in r.iter_content(1 << 20):
                size += len(chunk)
                if size > max_bytes:
                    raise DiscordError(f"attachment larger than {max_bytes // (1024 * 1024)} MB")
                f.write(chunk)
    return dest


def edit_reply(notify, content):
    """Updates the owner's private reply from the relay. Best effort: the interaction token
    only works for 15 minutes, and a failure here must never affect posting."""
    if not re.fullmatch(r"\d+/[\w.-]+", notify or ""):
        return False
    try:
        r = requests.patch(f"{API}/webhooks/{notify}/messages/@original", json={"content": content[:2000]},
                           headers={"User-Agent": _ua()}, timeout=30)
        return r.ok
    except requests.RequestException:
        return False


def register_command(app_id, bot_token):
    """Creates (or replaces) the app's "Send to BBG News" message command, installable to users."""
    try:
        r = requests.put(f"{API}/applications/{app_id}/commands", json=[COMMAND],
                         headers={"Authorization": f"Bot {bot_token}", "User-Agent": _ua()}, timeout=30)
    except requests.RequestException as e:
        raise DiscordError(f"couldn't reach Discord ({type(e).__name__})") from None
    if not r.ok:
        raise DiscordError(f"Discord said HTTP {r.status_code}: {r.text[:300]}")
    return r.json()
