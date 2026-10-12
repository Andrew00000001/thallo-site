"""Minimal Discord REST client (no Gateway connection needed)."""
import json
import os
import time
from urllib.parse import quote

import requests

API = "https://discord.com/api/v10"


class DiscordError(RuntimeError):
    pass


class Discord:
    def __init__(self, token):
        repo = os.environ.get("GITHUB_REPOSITORY", "bbg-news")
        self.s = requests.Session()
        self.s.headers.update({
            "Authorization": f"Bot {token}",
            "User-Agent": f"DiscordBot (https://github.com/{repo}, 1.0)",
        })

    def _req(self, method, path, **kw):
        for _ in range(4):
            r = self.s.request(method, f"{API}{path}", timeout=30, **kw)
            if r.status_code == 429:
                time.sleep(float(r.json().get("retry_after", 1)) + 0.25)
                continue
            if r.status_code >= 400:
                # Stop on auth errors: repeated 401/403s can get the runner's IP banned.
                raise DiscordError(f"{method} {path.split('?')[0]}: HTTP {r.status_code} {r.text[:200]}")
            return r.json() if r.content else None
        raise DiscordError(f"{method} {path.split('?')[0]}: still rate limited")

    def messages(self, channel, limit=100):
        """Newest `limit` messages, newest first."""
        return self._req("GET", f"/channels/{channel}/messages?limit={limit}")

    def reaction_users(self, channel, message, emoji):
        """IDs of users who reacted with `emoji` (first 100)."""
        try:
            users = self._req("GET", f"/channels/{channel}/messages/{message}/reactions/{quote(emoji)}?limit=100")
        except DiscordError as e:
            if "HTTP 404" in str(e) or "10014" in str(e):  # nobody used this emoji yet
                return set()
            raise
        return {u["id"] for u in users}

    def react(self, channel, message, emoji):
        self._req("PUT", f"/channels/{channel}/messages/{message}/reactions/{quote(emoji)}/@me")

    def reply(self, channel, message, content, ping=None):
        return self._req("POST", f"/channels/{channel}/messages", json={
            "content": content,
            "message_reference": {"message_id": message, "fail_if_not_exists": False},
            "allowed_mentions": {"users": [ping] if ping else [], "replied_user": bool(ping)},
        })

    def send(self, channel, content, file_path=None):
        payload = {"content": content, "allowed_mentions": {"parse": []}}
        if not file_path:
            return self._req("POST", f"/channels/{channel}/messages", json=payload)
        name = os.path.basename(file_path)
        payload["attachments"] = [{"id": 0, "filename": name}]
        with open(file_path, "rb") as f:
            data = f.read()
        return self._req("POST", f"/channels/{channel}/messages", files={
            "payload_json": (None, json.dumps(payload), "application/json"),
            "files[0]": (name, data),
        })

    def download(self, url, dest, max_bytes):
        with requests.get(url, stream=True, timeout=120) as r:
            r.raise_for_status()
            size = 0
            with open(dest, "wb") as f:
                for chunk in r.iter_content(1 << 20):
                    size += len(chunk)
                    if size > max_bytes:
                        raise DiscordError(f"attachment larger than {max_bytes} bytes")
                    f.write(chunk)
        return dest
