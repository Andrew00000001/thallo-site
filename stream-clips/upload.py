#!/usr/bin/env python3
"""Upload a rendered Short to every clips channel in config.json with the YouTube Data API (free).

Needs env vars YT_CLIPS_CLIENT_ID, YT_CLIPS_CLIENT_SECRET (falls back to YT_CLIENT_ID,
YT_CLIENT_SECRET) and one refresh token per channel (each channel's "token_env" in config.json)
with the youtube scope. Before each upload we confirm the token belongs to that exact channel,
so a clip can never land on Scribble Age or the wrong channel. A channel whose token isn't set
yet is skipped with a note; the others still get the Short.
"""
import argparse, datetime, json, os, re, sys
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

HERE = Path(__file__).resolve().parent
CONFIG = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
CHANNELS = CONFIG["channels"]
API = "https://www.googleapis.com/youtube/v3"
CHUNK = 16 * 1024 * 1024
SLUG = re.compile(r"twitch\.tv/[\w-]+/clip/([\w-]+)")


class UploadError(Exception):
    pass


def env(name):
    """YT_CLIPS_<name>, else the Scribble Age project's YT_<name>."""
    return os.environ.get(f"YT_CLIPS_{name}") or os.environ.get(f"YT_{name}")


def has_token(ch):
    return bool(os.environ.get(ch["token_env"]))


def access_token(ch):
    missing = [k for k in ("CLIENT_ID", "CLIENT_SECRET") if not env(k)]
    missing += [ch["token_env"]] if not has_token(ch) else []
    if missing:
        raise UploadError(f"missing env vars: {', '.join(missing)}")
    r = requests.post("https://oauth2.googleapis.com/token", data={
        "client_id": env("CLIENT_ID"), "client_secret": env("CLIENT_SECRET"),
        "refresh_token": os.environ[ch["token_env"]], "grant_type": "refresh_token"}, timeout=30)
    if r.status_code != 200:
        raise UploadError(f"token refresh failed: {r.status_code} {r.text}")
    return {"Authorization": f"Bearer {r.json()['access_token']}"}


def check_channel(ch, auth):
    """The token's uploads playlist; raises unless the token belongs to exactly this channel."""
    r = requests.get(f"{API}/channels", params={"part": "snippet,contentDetails", "mine": "true"},
                     headers=auth, timeout=30)
    if r.status_code != 200:
        raise UploadError(f"channel check failed ({r.status_code}): the token needs the youtube scope. {r.text[:300]}")
    items = r.json().get("items") or []
    if not items:
        raise UploadError("channel check failed: this Google account has no channel for the token")
    got = items[0]
    if got["id"] in CONFIG["forbidden_channel_ids"] or got["id"] != ch["id"]:
        raise UploadError(f"refusing: {ch['token_env']} belongs to {got['snippet']['title']!r} ({got['id']}), "
                          f"not {ch['name']!r} ({ch['id']})")
    return got["contentDetails"]["relatedPlaylists"]["uploads"]


def posted_slugs(max_pages=4):
    """Twitch clip slugs already posted on any channel with a token (read from the newest 200
    video descriptions), so a failed history.json push never causes a repeat."""
    slugs = set()
    for ch in CHANNELS:
        if not has_token(ch):
            continue
        auth = access_token(ch)
        uploads, token = check_channel(ch, auth), None
        for _ in range(max_pages):
            params = {"part": "snippet", "playlistId": uploads, "maxResults": 50}
            if token:
                params["pageToken"] = token
            r = requests.get(f"{API}/playlistItems", params=params, headers=auth, timeout=30)
            if r.status_code == 404:  # a brand-new channel has no uploads playlist yet
                break
            r.raise_for_status()
            data = r.json()
            for it in data.get("items", []):
                slugs.update(SLUG.findall(it["snippet"].get("description", "")))
            token = data.get("nextPageToken")
            if not token:
                break
    return slugs


def setup_channel():
    """Set description and keywords on channels that have them in config.json (brandingSettings
    is replaced whole, so read it first and change only those two fields)."""
    for ch in CHANNELS:
        if "description" not in ch:
            continue  # never overwrite a channel we don't own the branding for
        auth = access_token(ch)
        check_channel(ch, auth)
        r = requests.get(f"{API}/channels", params={"part": "brandingSettings", "id": ch["id"]},
                         headers=auth, timeout=30)
        r.raise_for_status()
        branding = r.json()["items"][0].get("brandingSettings", {})
        branding.setdefault("channel", {}).update(description=ch["description"], keywords=ch["keywords"])
        r = requests.put(f"{API}/channels", params={"part": "brandingSettings"}, headers=auth,
                         json={"id": ch["id"], "brandingSettings": branding}, timeout=30)
        if r.status_code != 200:
            raise UploadError(f"channel setup failed: {r.status_code} {r.text[:500]}")
        print(json.dumps({"channel": ch["name"], "description_set": True}))


def publish_time(hhmm):
    """Next occurrence of HH:MM America/Detroit (DST-aware), as UTC ISO 8601."""
    tz = ZoneInfo("America/Detroit")
    now = datetime.datetime.now(tz)
    h, m = map(int, hhmm.split(":"))
    t = now.replace(hour=h, minute=m, second=0, microsecond=0)
    if t <= now + datetime.timedelta(minutes=15):
        t += datetime.timedelta(days=1)
    return t.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def upload_one(ch, sh, video, privacy, publish_at):
    auth = access_token(ch)
    check_channel(ch, auth)
    body = {
        "snippet": {"title": sh["title"][:100], "description": sh["description"][:5000],
                    "tags": sh.get("tags", [])[:30], "categoryId": "24", "defaultLanguage": "en",
                    "defaultAudioLanguage": "en"},
        "status": {"privacyStatus": privacy, "selfDeclaredMadeForKids": False, "containsSyntheticMedia": False},
    }
    if publish_at:
        # YouTube publishes a scheduled video itself; it must be uploaded as private.
        body["status"].update(privacyStatus="private", publishAt=publish_time(publish_at))
    size = os.path.getsize(video)
    r = requests.post(
        "https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status",
        headers={**auth, "Content-Type": "application/json; charset=UTF-8",
                 "X-Upload-Content-Type": "video/mp4", "X-Upload-Content-Length": str(size)},
        data=json.dumps(body), timeout=60)
    if r.status_code != 200:
        raise UploadError(f"upload init failed: {r.status_code} {r.text}")
    url, pos, result = r.headers["Location"], 0, None
    with open(video, "rb") as f:
        while pos < size:
            chunk = f.read(CHUNK)
            end = pos + len(chunk) - 1
            r = requests.put(url, headers={**auth, "Content-Range": f"bytes {pos}-{end}/{size}"},
                             data=chunk, timeout=300)
            if r.status_code in (200, 201):
                result = r.json()
                break
            if r.status_code != 308:
                raise UploadError(f"upload failed at byte {pos}: {r.status_code} {r.text}")
            pos = int(r.headers["Range"].split("-")[1]) + 1 if "Range" in r.headers else 0
            f.seek(pos)
    vid = result["id"]
    return {"channel": ch["name"], "video_id": vid, "url": f"https://youtube.com/shorts/{vid}",
            "channel_id": result.get("snippet", {}).get("channelId"),
            "privacy": result.get("status", {}).get("privacyStatus"),
            "publish_at": result.get("status", {}).get("publishAt")}


def upload(short, video, privacy, publish_at=None):
    """Upload to every channel; one JSON line each. Exit 1 if any channel with a token failed."""
    sh = json.loads(Path(short).read_text(encoding="utf-8"))
    failed = False
    for ch in CHANNELS:
        if not has_token(ch):
            print(json.dumps({"channel": ch["name"], "skipped": f"{ch['token_env']} is not set"}))
            continue
        try:
            print(json.dumps(upload_one(ch, sh, video, privacy, publish_at)), flush=True)
        except (UploadError, requests.RequestException) as e:
            failed = True
            print(json.dumps({"channel": ch["name"], "error": str(e)[:1000]}), flush=True)
    if failed:
        sys.exit(1)


def whoami():
    """Check every channel's token; exit 1 if the primary (first) channel isn't usable."""
    primary_ok = False
    for i, ch in enumerate(CHANNELS):
        try:
            if not has_token(ch):
                raise UploadError(f"{ch['token_env']} is not set")
            check_channel(ch, access_token(ch))
            print(json.dumps({"channel": ch["name"], "channel_id": ch["id"], "ok": True}))
            primary_ok |= i == 0
        except (UploadError, requests.RequestException) as e:
            print(json.dumps({"channel": ch["name"], "ok": False, "error": str(e)[:500]}))
    if not primary_ok:
        sys.exit(1)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("short", nargs="?", help="short JSON written by the agent")
    p.add_argument("--video", default="build/short.mp4")
    p.add_argument("--privacy", default="public", choices=["public", "unlisted", "private"])
    p.add_argument("--publish-at", help="HH:MM America/Detroit; schedules the Short to go public then")
    p.add_argument("--whoami", action="store_true", help="check every channel's token and exit")
    p.add_argument("--setup-channel", action="store_true", help="set channel descriptions and keywords")
    a = p.parse_args()
    try:
        if a.setup_channel:
            setup_channel()
        elif a.whoami:
            whoami()
        elif a.short:
            upload(a.short, a.video, a.privacy, a.publish_at)
        else:
            p.error("give a short JSON file or --whoami")
    except UploadError as e:
        sys.exit(str(e))
