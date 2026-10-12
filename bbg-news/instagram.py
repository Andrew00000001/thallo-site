"""Minimal client for the Instagram API with Instagram Login (graph.instagram.com)."""
import os
import time

import requests

HOST = "https://graph.instagram.com"
VERSION = os.environ.get("IG_API_VERSION", "v25.0")


class InstagramError(RuntimeError):
    pass


class ContainerError(InstagramError):
    """Instagram could not process the media (bad URL, format, etc.)."""


class CopyrightMatch(InstagramError):
    """Instagram's copyright check matched the video (often background music)."""


class Instagram:
    def __init__(self, token):
        self.token = token
        self._ig_id = None

    def _call(self, method, path, **params):
        params["access_token"] = self.token
        url = f"{HOST}/{VERSION}/{path}"
        if method == "GET":
            r = requests.get(url, params=params, timeout=60)
        else:
            r = requests.post(url, data=params, timeout=60)
        body = r.json() if r.content else {}
        if r.status_code >= 400 or "error" in body:
            err = body.get("error", {})
            raise InstagramError(f"{path}: {err.get('message', r.text)} (code {err.get('code')})")
        return body

    def user_id(self):
        if self._ig_id:
            return self._ig_id
        if os.environ.get("IG_USER_ID"):
            self._ig_id = os.environ["IG_USER_ID"]
            return self._ig_id
        me = self._call("GET", "me", fields="user_id,username")
        if "data" in me:  # Meta's docs show the fields wrapped in a data list
            me = me["data"][0]
        self._ig_id = me["user_id"]
        return self._ig_id

    def _wait(self, container, video):
        """Polls until the container is FINISHED. For video, also waits for the copyright check.

        Meta recommends polling video containers about once a minute, for up to 5 minutes.
        """
        interval, tries = (30, 20) if video else (5, 12)
        fields = "status_code,status,copyright_check_status" if video else "status_code,status"
        for _ in range(tries):
            c = self._call("GET", container, fields=fields)
            code = c.get("status_code")
            if code in ("ERROR", "EXPIRED"):
                raise ContainerError(f"container {code}: {c.get('status')}")
            check = c.get("copyright_check_status") or {}
            if check.get("matches_found") is True:
                raise CopyrightMatch("Instagram's copyright check found a match")
            if code == "FINISHED" and (not video or check.get("status") in ("completed", None)):
                if video and check.get("status") is None:
                    print("Note: no copyright_check_status returned; publishing on FINISHED.")
                return
            if video and check.get("status") == "error":
                raise ContainerError("copyright check errored")
            time.sleep(interval)
        raise ContainerError(f"container {container} not ready after {interval * tries}s")

    def _publish(self, params, video):
        ig_id = self.user_id()
        container = self._call("POST", f"{ig_id}/media", **params)["id"]
        self._wait(container, video)
        return self._call("POST", f"{ig_id}/media_publish", creation_id=container)["id"]

    def publish_image(self, image_url, caption):
        return self._publish({"image_url": image_url, "caption": caption}, video=False)

    def publish_reel(self, video_url, caption, cover_url=None):
        params = {"media_type": "REELS", "video_url": video_url, "caption": caption, "share_to_feed": "true"}
        if cover_url:
            params["cover_url"] = cover_url
        return self._publish(params, video=True)

    def permalink(self, media_id):
        try:
            return self._call("GET", media_id, fields="permalink").get("permalink")
        except InstagramError:
            return None

    def refresh_token(self):
        """Extends a long-lived token by 60 days. Token must be 24h+ old and unexpired."""
        r = requests.get(
            f"{HOST}/refresh_access_token",
            params={"grant_type": "ig_refresh_token", "access_token": self.token},
            timeout=60,
        )
        body = r.json()
        if "access_token" not in body:
            raise InstagramError(f"refresh failed: {body.get('error', {}).get('message', r.text)}")
        return body["access_token"]
