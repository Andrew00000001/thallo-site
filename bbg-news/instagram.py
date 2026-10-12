"""Minimal client for the Instagram API with Instagram Login (graph.instagram.com)."""
import os
import time

import requests

HOST = "https://graph.instagram.com"
VERSION = os.environ.get("IG_API_VERSION", "v25.0")


class InstagramError(RuntimeError):
    pass


class Instagram:
    def __init__(self, token):
        self.token = token

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
        if os.environ.get("IG_USER_ID"):
            return os.environ["IG_USER_ID"]
        me = self._call("GET", "me", fields="user_id,username")
        if "data" in me:  # Meta's docs show the fields wrapped in a data list
            me = me["data"][0]
        return me["user_id"]

    def publish_image(self, image_url, caption):
        """Create a media container, wait for it, publish it. Returns the media ID."""
        ig_id = self.user_id()
        container = self._call("POST", f"{ig_id}/media", image_url=image_url, caption=caption)["id"]
        for _ in range(12):
            status = self._call("GET", container, fields="status_code").get("status_code")
            if status == "FINISHED":
                break
            if status in ("ERROR", "EXPIRED"):
                raise InstagramError(f"container {container} status {status}")
            time.sleep(5)
        else:
            raise InstagramError(f"container {container} not ready after 60s")
        return self._call("POST", f"{ig_id}/media_publish", creation_id=container)["id"]

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
