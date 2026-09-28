#!/usr/bin/env python3
"""Upload a rendered Short to the clips channel with the YouTube Data API (free).

Needs env vars YT_CLIPS_CLIENT_ID, YT_CLIPS_CLIENT_SECRET (falls back to YT_CLIENT_ID,
YT_CLIENT_SECRET) and the channel's refresh token (config.json "token_env", default
YT_CLIPS_REFRESH_TOKEN) with the youtube scope. Before uploading we confirm which channel the
token belongs to, so a clip can never land on Scribble Age by mistake.
"""
import argparse, datetime, json, os, re, sys
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

HERE = Path(__file__).resolve().parent
CONFIG = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
API = "https://www.googleapis.com/youtube/v3"
CHUNK = 16 * 1024 * 1024
SLUG = re.compile(r"twitch\.tv/[\w-]+/clip/([\w-]+)")


def env(name):
    """YT_CLIPS_<name>, else the Scribble Age project's YT_<name>."""
    return os.environ.get(f"YT_CLIPS_{name}") or os.environ.get(f"YT_{name}")


def access_token():
    missing = [k for k in ("CLIENT_ID", "CLIENT_SECRET") if not env(k)]
    missing += [CONFIG["token_env"]] if not os.environ.get(CONFIG["token_env"]) else []
    if missing:
        sys.exit(f"missing env vars: {', '.join(missing)}")
    r = requests.post("https://oauth2.googleapis.com/token", data={
        "client_id": env("CLIENT_ID"), "client_secret": env("CLIENT_SECRET"),
        "refresh_token": os.environ[CONFIG["token_env"]], "grant_type": "refresh_token"}, timeout=30)
    if r.status_code != 200:
        sys.exit(f"token refresh failed: {r.status_code} {r.text}")
    return r.json()["access_token"]


def my_channel(auth):
    """(channel_id, title, uploads_playlist) for the token's channel; exits if it's the wrong one."""
    r = requests.get(f"{API}/channels", params={"part": "snippet,contentDetails", "mine": "true"},
                     headers=auth, timeout=30)
    if r.status_code != 200:
        sys.exit(f"channel check failed ({r.status_code}): the token needs the youtube scope. {r.text[:300]}")
    items = r.json().get("items") or []
    if not items:
        sys.exit("channel check failed: this Google account has no channel for the token")
    ch = items[0]
    cid = ch["id"]
    if cid in CONFIG["forbidden_channel_ids"]:
        sys.exit(f"refusing to upload: token belongs to {ch['snippet']['title']} ({cid}), not the clips channel")
    if CONFIG.get("channel_id") and cid != CONFIG["channel_id"]:
        sys.exit(f"refusing to upload: token belongs to {cid}, config.json expects {CONFIG['channel_id']}")
    if not CONFIG.get("channel_id") and ch["snippet"]["title"] != CONFIG["channel_name"]:
        sys.exit(f"refusing to upload: token belongs to {ch['snippet']['title']!r}, expected {CONFIG['channel_name']!r}")
    return cid, ch["snippet"]["title"], ch["contentDetails"]["relatedPlaylists"]["uploads"]


def posted_slugs(max_pages=4):
    """Twitch clip slugs already on the channel (read from video descriptions), newest 200 uploads."""
    auth = {"Authorization": f"Bearer {access_token()}"}
    _, _, uploads = my_channel(auth)
    slugs, token = set(), None
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
    """Set the channel description and keywords from config.json (brandingSettings is replaced
    whole, so read it first and change only those two fields)."""
    auth = {"Authorization": f"Bearer {access_token()}"}
    cid, title, _ = my_channel(auth)
    r = requests.get(f"{API}/channels", params={"part": "brandingSettings", "id": cid}, headers=auth, timeout=30)
    r.raise_for_status()
    branding = r.json()["items"][0].get("brandingSettings", {})
    branding.setdefault("channel", {}).update(description=CONFIG["channel_description"],
                                             keywords=CONFIG["channel_keywords"])
    r = requests.put(f"{API}/channels", params={"part": "brandingSettings"}, headers=auth,
                     json={"id": cid, "brandingSettings": branding}, timeout=30)
    if r.status_code != 200:
        sys.exit(f"channel setup failed: {r.status_code} {r.text[:500]}")
    print(json.dumps({"channel_id": cid, "channel_title": title, "description_set": True}))


def publish_time(hhmm):
    """Next occurrence of HH:MM America/Detroit (DST-aware), as UTC ISO 8601."""
    tz = ZoneInfo("America/Detroit")
    now = datetime.datetime.now(tz)
    h, m = map(int, hhmm.split(":"))
    t = now.replace(hour=h, minute=m, second=0, microsecond=0)
    if t <= now + datetime.timedelta(minutes=15):
        t += datetime.timedelta(days=1)
    return t.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def upload(short, video, privacy, publish_at=None):
    sh = json.loads(Path(short).read_text(encoding="utf-8"))
    auth = {"Authorization": f"Bearer {access_token()}"}
    cid, ctitle, _ = my_channel(auth)
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
        f"https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status",
        headers={**auth, "Content-Type": "application/json; charset=UTF-8",
                 "X-Upload-Content-Type": "video/mp4", "X-Upload-Content-Length": str(size)},
        data=json.dumps(body), timeout=60)
    if r.status_code != 200:
        sys.exit(f"upload init failed: {r.status_code} {r.text}")
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
                sys.exit(f"upload failed at byte {pos}: {r.status_code} {r.text}")
            pos = int(r.headers["Range"].split("-")[1]) + 1 if "Range" in r.headers else 0
            f.seek(pos)
    vid = result["id"]
    print(json.dumps({"video_id": vid, "url": f"https://youtube.com/shorts/{vid}",
                      "channel_id": result.get("snippet", {}).get("channelId", cid), "channel_title": ctitle,
                      "privacy": result.get("status", {}).get("privacyStatus"),
                      "publish_at": result.get("status", {}).get("publishAt")}))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("short", nargs="?", help="short JSON written by the agent")
    p.add_argument("--video", default="build/short.mp4")
    p.add_argument("--privacy", default="public", choices=["public", "unlisted", "private"])
    p.add_argument("--publish-at", help="HH:MM America/Detroit; schedules the Short to go public then")
    p.add_argument("--whoami", action="store_true", help="print the token's channel and exit")
    p.add_argument("--setup-channel", action="store_true", help="set the channel description and keywords")
    a = p.parse_args()
    if a.setup_channel:
        setup_channel()
    elif a.whoami:
        cid, title, _ = my_channel({"Authorization": f"Bearer {access_token()}"})
        print(json.dumps({"channel_id": cid, "channel_title": title}))
    elif a.short:
        upload(a.short, a.video, a.privacy, a.publish_at)
    else:
        p.error("give a short JSON file or --whoami")
