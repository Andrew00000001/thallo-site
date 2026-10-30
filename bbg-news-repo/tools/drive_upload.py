"""Upload finished comics to Bryce's Google Drive.

Every folder under comics_final/ is one finished comic. comics_final/index.json
maps each folder to the Drive folder title it gets inside "BBG News Comics" (in
My Drive). Any file in the comic's folder that is not in Drive yet is uploaded;
files already there (same name) are left alone, so running it again is safe.

Credentials come from the environment, never from the repo or the chat: an OAuth
client of Bryce's own and a refresh token with the drive.file scope (the app can
see and change only the files it creates):
  GDRIVE_CLIENT_ID, GDRIVE_CLIENT_SECRET, GDRIVE_REFRESH_TOKEN

Standard library only.

Usage: python3 -I tools/drive_upload.py [--dry-run]
  --dry-run   list what would be uploaded; with no credentials set, only the
              local side is checked
Exit status: 0 done, 2 credentials missing, 1 an API error.
"""
import json
import mimetypes
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
FINAL = REPO / "comics_final"
ROOT_TITLE = "BBG News Comics"
FOLDER = "application/vnd.google-apps.folder"
API = "https://www.googleapis.com/drive/v3/files"
UPLOAD = "https://www.googleapis.com/upload/drive/v3/files"
TOKEN = "https://oauth2.googleapis.com/token"
VARS = ("GDRIVE_CLIENT_ID", "GDRIVE_CLIENT_SECRET", "GDRIVE_REFRESH_TOKEN")


def request(method, url, token=None, data=None, headers=None):
    req = urllib.request.Request(url, data=data, method=method, headers=dict(headers or {}))
    if token:
        req.add_header("Authorization", "Bearer " + token)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            body = r.read()
            return r.status, dict(r.headers), body
    except urllib.error.HTTPError as e:
        raise SystemExit("Drive API error %s on %s %s: %s"
                         % (e.code, method, url.split("?")[0], e.read().decode("utf-8", "replace")[:400]))


def access_token():
    env = {k: os.environ.get(k, "").strip() for k in VARS}
    missing = [k for k, v in env.items() if not v]
    if missing:
        return None, missing
    body = urllib.parse.urlencode({
        "client_id": env["GDRIVE_CLIENT_ID"], "client_secret": env["GDRIVE_CLIENT_SECRET"],
        "refresh_token": env["GDRIVE_REFRESH_TOKEN"], "grant_type": "refresh_token"}).encode()
    _, _, out = request("POST", TOKEN, data=body,
                        headers={"Content-Type": "application/x-www-form-urlencoded"})
    return json.loads(out)["access_token"], []


def q_escape(s):
    return s.replace("\\", "\\\\").replace("'", "\\'")


def children(token, parent, folders_only=False):
    q = "'%s' in parents and trashed = false" % parent
    if folders_only:
        q += " and mimeType = '%s'" % FOLDER
    names, page = {}, None
    while True:
        params = {"q": q, "fields": "nextPageToken, files(id, name, mimeType)", "pageSize": 1000}
        if page:
            params["pageToken"] = page
        _, _, out = request("GET", API + "?" + urllib.parse.urlencode(params), token)
        d = json.loads(out)
        for f in d.get("files", []):
            names[f["name"]] = f["id"]
        page = d.get("nextPageToken")
        if not page:
            return names


def folder(token, title, parent):
    q = ("name = '%s' and mimeType = '%s' and '%s' in parents and trashed = false"
         % (q_escape(title), FOLDER, parent))
    _, _, out = request("GET", API + "?" + urllib.parse.urlencode({"q": q, "fields": "files(id)"}), token)
    found = json.loads(out).get("files", [])
    if found:
        return found[0]["id"]
    meta = json.dumps({"name": title, "mimeType": FOLDER, "parents": [parent]}).encode()
    _, _, out = request("POST", API + "?fields=id", token, meta, {"Content-Type": "application/json"})
    print("  created folder: %s" % title)
    return json.loads(out)["id"]


def upload(token, path, parent):
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    if path.suffix == ".txt":
        mime = "text/plain"
    meta = json.dumps({"name": path.name, "parents": [parent]}).encode()
    _, h, _ = request("POST", UPLOAD + "?uploadType=resumable&fields=id", token, meta,
                      {"Content-Type": "application/json; charset=UTF-8", "X-Upload-Content-Type": mime})
    session = h.get("Location") or h.get("location")
    data = path.read_bytes()
    _, _, out = request("PUT", session, token, data, {"Content-Type": mime})
    return json.loads(out)["id"]


def main():
    dry = "--dry-run" in sys.argv[1:]
    index = json.loads((FINAL / "index.json").read_text())
    comics = []
    for d in sorted(p for p in FINAL.iterdir() if p.is_dir()):
        if d.name not in index:
            raise SystemExit("comics_final/%s has no title in comics_final/index.json" % d.name)
        files = sorted(f for f in d.iterdir() if f.is_file() and not f.name.startswith("."))
        comics.append((d, index[d.name], files))
    token, missing = access_token()
    if not token:
        print("Credentials missing: %s." % ", ".join(missing))
        for d, title, files in comics:
            print("  would upload %s -> %s/%s (%d files)" % (d.name, ROOT_TITLE, title, len(files)))
        return 0 if dry else 2
    root = folder(token, ROOT_TITLE, "root") if not dry else None
    total = 0
    for d, title, files in comics:
        if dry:
            print("  %s -> %s/%s: %d files" % (d.name, ROOT_TITLE, title, len(files)))
            continue
        fid = folder(token, title, root)
        have = children(token, fid)
        for f in files:
            if f.name in have:
                continue
            upload(token, f, fid)
            total += 1
            print("  uploaded %s/%s/%s" % (ROOT_TITLE, title, f.name))
    print("done: %d new file(s)" % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
