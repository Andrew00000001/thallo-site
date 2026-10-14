"""Official content sources: Steam (release date, announcements, trailers) and YouTube."""
from datetime import datetime

import requests

APP = 4408320
# Official "BATTLE BEARS" YouTube channel (youtube.com/@battlebears).
YT_CHANNEL = "UCwPClz0LJVpdkRjoidDZjEg"


def steam_release(app=APP):
    """Returns (release date or None, coming_soon) from the Steam store."""
    r = requests.get(
        "https://store.steampowered.com/api/appdetails",
        params={"appids": app, "filters": "release_date"},
        timeout=30,
    )
    r.raise_for_status()
    rd = r.json()[str(app)]["data"]["release_date"]
    try:
        return datetime.strptime(rd["date"], "%b %d, %Y").date(), rd["coming_soon"]
    except ValueError:
        return None, rd["coming_soon"]


def steam_news(app=APP, count=10):
    """Official SkyVu announcements only (not third-party press feeds), oldest first."""
    r = requests.get(
        "https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/",
        params={"appid": app, "count": count, "feeds": "steam_community_announcements"},
        timeout=30,
    )
    return sorted(r.json()["appnews"]["newsitems"], key=lambda n: n["date"])


def steam_trailers(app=APP):
    """Trailers on the Steam store page: [{id, name, hls}]. Steam serves HLS/DASH only."""
    r = requests.get(
        "https://store.steampowered.com/api/appdetails",
        params={"appids": app, "filters": "movies"},
        timeout=30,
    )
    movies = r.json()[str(app)]["data"].get("movies", [])
    return [{"id": str(m["id"]), "name": m["name"], "hls": m["hls_h264"]} for m in movies if m.get("hls_h264")]


def youtube_uploads(api_key, channel=YT_CHANNEL, count=10):
    """Latest uploads via the YouTube Data API (1 quota unit per call), oldest first.

    The public RSS feed is disallowed by YouTube's robots.txt, so the API is used instead.
    """
    r = requests.get(
        "https://www.googleapis.com/youtube/v3/playlistItems",
        params={
            "part": "snippet",
            "playlistId": "UU" + channel[2:],  # a channel's uploads playlist
            "maxResults": count,
            "key": api_key,
        },
        timeout=30,
    )
    r.raise_for_status()
    items = [
        {
            "id": i["snippet"]["resourceId"]["videoId"],
            "title": i["snippet"]["title"],
            "published": i["snippet"]["publishedAt"],
        }
        for i in r.json().get("items", [])
    ]
    return sorted(items, key=lambda v: v["published"])
