#!/usr/bin/env python3
"""Upload a built video to the Scribble Age channel with the YouTube Data API (free).

Needs env vars YT_CLIENT_ID, YT_CLIENT_SECRET, YT_REFRESH_TOKEN (scope youtube.upload).
Until Google approves the API audit, YouTube forces API uploads to private.
"""
import argparse, datetime, json, os, sys
from zoneinfo import ZoneInfo
from pathlib import Path

import requests

CHUNK = 16 * 1024 * 1024


def access_token():
    missing = [k for k in ("YT_CLIENT_ID", "YT_CLIENT_SECRET", "YT_REFRESH_TOKEN") if not os.environ.get(k)]
    if missing:
        sys.exit(f"missing env vars: {', '.join(missing)}")
    r = requests.post("https://oauth2.googleapis.com/token", data={
        "client_id": os.environ["YT_CLIENT_ID"], "client_secret": os.environ["YT_CLIENT_SECRET"],
        "refresh_token": os.environ["YT_REFRESH_TOKEN"], "grant_type": "refresh_token"}, timeout=30)
    if r.status_code != 200:
        sys.exit(f"token refresh failed: {r.status_code} {r.text}")
    return r.json()["access_token"]


def publish_time(hhmm):
    """Next occurrence of HH:MM America/Detroit (DST-aware), as UTC ISO 8601."""
    tz = ZoneInfo("America/Detroit")
    now = datetime.datetime.now(tz)
    h, m = map(int, hhmm.split(":"))
    t = now.replace(hour=h, minute=m, second=0, microsecond=0)
    if t <= now + datetime.timedelta(minutes=15):
        t += datetime.timedelta(days=1)
    return t.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def upload(episode, video, thumbnail, privacy, publish_at=None):
    ep = json.loads(Path(episode).read_text(encoding="utf-8"))
    auth = {"Authorization": f"Bearer {access_token()}"}
    body = {
        "snippet": {"title": ep["title"][:100], "description": ep["description"][:5000],
                    "tags": ep.get("tags", [])[:30], "categoryId": "27", "defaultLanguage": "en",
                    "defaultAudioLanguage": "en"},
        "status": {"privacyStatus": privacy, "selfDeclaredMadeForKids": False, "containsSyntheticMedia": True},
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
    thumb_note = "set"
    if thumbnail and os.path.exists(thumbnail):
        with open(thumbnail, "rb") as f:
            t = requests.post(f"https://www.googleapis.com/upload/youtube/v3/thumbnails/set?videoId={vid}",
                              headers={**auth, "Content-Type": "image/jpeg"}, data=f.read(), timeout=120)
        if t.status_code != 200:
            # Custom thumbnails need a phone-verified channel (youtube.com/verify).
            thumb_note = f"failed {t.status_code}: {t.text[:300]}"
    print(json.dumps({"video_id": vid, "url": f"https://youtu.be/{vid}",
                      "channel_id": result.get("snippet", {}).get("channelId"),
                      "privacy": result.get("status", {}).get("privacyStatus"),
                      "publish_at": result.get("status", {}).get("publishAt"), "thumbnail": thumb_note}))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("episode")
    p.add_argument("--video", default="build/video.mp4")
    p.add_argument("--thumbnail", default="build/thumbnail.jpg")
    p.add_argument("--privacy", default="public", choices=["public", "unlisted", "private"])
    p.add_argument("--publish-at", help="HH:MM America/Detroit; schedules the video to go public then")
    a = p.parse_args()
    upload(a.episode, a.video, a.thumbnail, a.privacy, a.publish_at)
