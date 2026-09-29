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
TZ = ZoneInfo("America/Detroit")
MIN_GAP = datetime.timedelta(hours=2)  # auto-scheduled Shorts go live at least this far apart
# Go-live times this run already booked. A fresh upload can take a while to show up in the
# channel's uploads list, so without this two uploads in a row could land on the same slot.
BOOKED = HERE / ".booked.json"


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


def recent_videos(auth, uploads, max_pages=4):
    """The channel's newest uploads (up to 200) with snippet, status and recordingDetails."""
    videos, token = [], None
    for _ in range(max_pages):
        params = {"part": "snippet", "playlistId": uploads, "maxResults": 50}
        if token:
            params["pageToken"] = token
        r = requests.get(f"{API}/playlistItems", params=params, headers=auth, timeout=30)
        if r.status_code == 404:  # a brand-new channel has no uploads playlist yet
            break
        r.raise_for_status()
        data = r.json()
        ids = [it["snippet"]["resourceId"]["videoId"] for it in data.get("items", [])]
        if ids:
            v = requests.get(f"{API}/videos", params={"part": "snippet,status,recordingDetails", "id": ",".join(ids)},
                             headers=auth, timeout=30)
            v.raise_for_status()
            videos += v.json().get("items", [])
        token = data.get("nextPageToken")
        if not token:
            break
    return videos


def posted():
    """Twitch clip slugs already on the channels, read from each description's "Clip:" lines, so no
    state has to live in git. (YouTube keeps only the date of recordingDate, so find_clips gets
    each posted clip's exact time from the Twitch clip lists instead.)"""
    slugs = set()
    for ch in CHANNELS:
        if not has_token(ch):
            continue
        auth = access_token(ch)
        for v in recent_videos(auth, check_channel(ch, auth)):
            slugs.update(SLUG.findall(v["snippet"].get("description", "")))
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


def utc(t):
    return t.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def publish_time(hhmm):
    """Next occurrence of HH:MM America/Detroit (DST-aware), as UTC ISO 8601."""
    now = datetime.datetime.now(TZ)
    h, m = map(int, hhmm.split(":"))
    t = now.replace(hour=h, minute=m, second=0, microsecond=0)
    if t <= now + datetime.timedelta(minutes=15):
        t += datetime.timedelta(days=1)
    return utc(t)


def auto_slot(auth, uploads):
    """The first config.json publish time that is 20+ minutes away and MIN_GAP after the latest
    Short already live or scheduled on the channel, so runs at any hour never pile Shorts up."""
    now = datetime.datetime.now(TZ)
    latest = now - MIN_GAP
    for when in booked():
        latest = max(latest, datetime.datetime.fromisoformat(when.replace("Z", "+00:00")).astimezone(TZ))
    for v in recent_videos(auth, uploads, max_pages=1):
        st, sn = v["status"], v["snippet"]
        when = st.get("publishAt") if st.get("privacyStatus") == "private" else (
            sn.get("publishedAt") if st.get("privacyStatus") == "public" else None)
        if when:
            latest = max(latest, datetime.datetime.fromisoformat(when.replace("Z", "+00:00")).astimezone(TZ))
    earliest = max(now + datetime.timedelta(minutes=20), latest + MIN_GAP)
    for day in range(0, 30):
        for hhmm in CONFIG["publish_times"]:
            h, m = map(int, hhmm.split(":"))
            t = (now + datetime.timedelta(days=day)).replace(hour=h, minute=m, second=0, microsecond=0)
            if t >= earliest:
                return utc(t)
    raise UploadError("no free publish slot in the next 30 days")


def booked():
    try:
        return json.loads(BOOKED.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []


def upload_one(ch, sh, video, privacy, publish_at):
    auth = access_token(ch)
    uploads = check_channel(ch, auth)
    body = {
        "snippet": {"title": sh["title"][:100], "description": sh["description"][:5000],
                    "tags": sh.get("tags", [])[:30], "categoryId": "24", "defaultLanguage": "en",
                    "defaultAudioLanguage": "en"},
        "status": {"privacyStatus": privacy, "selfDeclaredMadeForKids": False, "containsSyntheticMedia": False},
    }
    if publish_at:
        # YouTube publishes a scheduled video itself; it must be uploaded as private.
        when = auto_slot(auth, uploads) if publish_at == "auto" else publish_time(publish_at)
        body["status"].update(privacyStatus="private", publishAt=when)
    if sh.get("clip_created"):
        # When the moment happened; later runs read it back to skip other clips of the same moment.
        body["recordingDetails"] = {"recordingDate": datetime.datetime.fromtimestamp(
            sh["clip_created"], datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
    size = os.path.getsize(video)

    def init():
        parts = "snippet,status" + (",recordingDetails" if "recordingDetails" in body else "")
        return requests.post(
            f"https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part={parts}",
            headers={**auth, "Content-Type": "application/json; charset=UTF-8",
                     "X-Upload-Content-Type": "video/mp4", "X-Upload-Content-Length": str(size)},
            data=json.dumps(body), timeout=60)

    r = init()
    if r.status_code == 400 and body.pop("recordingDetails", None):
        r = init()  # the recording date is only a dedupe hint; never let it block an upload
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
    live = result.get("status", {}).get("publishAt")
    if live:
        BOOKED.write_text(json.dumps(booked() + [live]), encoding="utf-8")
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
    p.add_argument("--publish-at", help='"auto" (next free slot from config.json) or HH:MM America/Detroit')
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
