"""Minimal client for the Instagram API with Instagram Login (graph.instagram.com)."""
import os
import time

import requests

HOST = "https://graph.instagram.com"
VERSION = os.environ.get("IG_API_VERSION", "v25.0")


# Errors that say nothing about the post itself: outages, rate/publish limits, expired token.
TRANSIENT_CODES = {1, 2, 4, 9, 17, 32, 190, 613}


class InstagramError(RuntimeError):
    def __init__(self, msg, code=None):
        super().__init__(msg)
        self.code = code


class ContainerError(InstagramError):
    """Instagram could not process the media. `fetch_failed` means status ERROR/EXPIRED,
    which is what a URL Instagram can't download produces."""

    def __init__(self, msg, fetch_failed=False):
        super().__init__(msg)
        self.fetch_failed = fetch_failed


class CopyrightMatch(InstagramError):
    """Instagram's copyright check matched the video (often background music)."""


class Instagram:
    def __init__(self, token):
        self.token = token
        self._ig_id = None

    def _call(self, method, path, **params):
        params["access_token"] = self.token
        url = f"{HOST}/{VERSION}/{path}"
        try:
            if method == "GET":
                r = requests.get(url, params=params, timeout=60)
            else:
                r = requests.post(url, data=params, timeout=60)
            body = r.json() if r.content else {}
        except (requests.RequestException, ValueError) as e:
            # requests' messages can include the URL, and GET URLs carry the token: never surface them.
            raise InstagramError(f"{path.split('/')[-1]}: {type(e).__name__}") from None
        if r.status_code >= 400 or "error" in body:
            err = body.get("error", {})
            raise InstagramError(f"{path.split('/')[-1]}: {err.get('message', r.status_code)} (code {err.get('code')})",
                                 err.get("code"))
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

    def _status(self, container, fields):
        """One status poll, retried a few times through transient errors."""
        for attempt in range(3):
            try:
                return self._call("GET", container, fields=fields)
            except (requests.RequestException, ValueError) as e:
                err = e
            except InstagramError as e:
                if e.code is not None and e.code not in TRANSIENT_CODES:
                    raise
                err = e  # network error (code None) or a transient Graph error
            time.sleep(10 * (attempt + 1))
        raise err

    def container_status(self, container):
        return self._status(container, "status_code").get("status_code")

    def _wait(self, container, video):
        """Polls until the container is FINISHED. For video, also waits for the copyright check.

        Meta recommends polling video containers about once a minute, for up to 5 minutes;
        this polls every 30 s for up to 10 minutes.
        """
        interval, tries = (30, 20) if video else (5, 12)
        fields = "status_code,status,copyright_check_status" if video else "status_code,status"
        for _ in range(tries):
            c = self._status(container, fields)
            code = c.get("status_code")
            if code in ("ERROR", "EXPIRED"):
                raise ContainerError(f"container {code}: {c.get('status')}", fetch_failed=True)
            check = c.get("copyright_check_status") or {}
            if check.get("matches_found") is True:
                raise CopyrightMatch("Instagram's copyright check found a match")
            if video and check.get("status") == "error":
                raise ContainerError("Instagram's copyright check errored")
            if code == "FINISHED" and (not video or check.get("status") in ("completed", None)):
                if video and check.get("status") is None:
                    print("Note: no copyright_check_status returned; publishing on FINISHED.")
                return
            time.sleep(interval)
        raise ContainerError(f"container not ready after {interval * tries}s (copyright check: {check.get('status')})")

    def _publish(self, params, video, on_container=None):
        ig_id = self.user_id()
        container = self._call("POST", f"{ig_id}/media", **params)["id"]
        self._wait(container, video)
        if on_container:
            on_container(container)  # recorded first, so an unclear publish result can be checked later
        return self._call("POST", f"{ig_id}/media_publish", creation_id=container)["id"]

    def publish_image(self, image_url, caption, on_container=None):
        return self._publish({"image_url": image_url, "caption": caption}, False, on_container)

    def publish_reel(self, video_url, caption, cover_url=None, on_container=None):
        params = {"media_type": "REELS", "video_url": video_url, "caption": caption, "share_to_feed": "true"}
        if cover_url:
            params["cover_url"] = cover_url
        return self._publish(params, True, on_container)

    def permalink(self, media_id):
        try:
            return self._call("GET", media_id, fields="permalink").get("permalink")
        except InstagramError:
            return None

    def refresh_token(self):
        """Extends a long-lived token by 60 days. Token must be 24h+ old and unexpired."""
        try:
            r = requests.get(
                f"{HOST}/refresh_access_token",
                params={"grant_type": "ig_refresh_token", "access_token": self.token},
                timeout=60,
            )
            body = r.json()
        except (requests.RequestException, ValueError) as e:
            raise InstagramError(f"refresh failed: {type(e).__name__}") from None
        if "access_token" not in body:
            raise InstagramError(f"refresh failed: {body.get('error', {}).get('message', r.status_code)}")
        return body["access_token"]
