"""Public URLs for Instagram to fetch media from (it never accepts direct uploads on Instagram Login).

Primary: each publish force-pushes a single parentless commit holding only that post's files to
the `bbg-media` branch and serves it from raw.githubusercontent.com pinned to the commit. Old
media drops out of the branch on the next publish, so clones don't grow with every video, but
GitHub keeps serving a replaced commit by its SHA until GitHub itself garbage-collects it.
Fallback: a GitHub Release asset, deleted after use (used if Instagram can't fetch a raw video URL).
"""
import os
import subprocess
from pathlib import Path

BRANCH = "bbg-media"
RELEASE_TAG = "bbg-media"
ROOT = Path(__file__).parent


def _git(*args, stdin=None):
    p = subprocess.run(["git", *args], cwd=ROOT, input=stdin, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"git {args[0]} failed: {p.stderr.strip()}")
    return p.stdout.strip()


def push_media(paths):
    """Publishes files to the media branch. Returns {filename: raw URL}."""
    entries = [f"100644 blob {_git('hash-object', '-w', str(p))}\t{Path(p).name}" for p in paths]
    tree = _git("mktree", stdin="\n".join(entries) + "\n")
    commit = _git("commit-tree", tree, "-m", "BBG News media")
    _git("push", "--force", "origin", f"{commit}:refs/heads/{BRANCH}")
    repo = os.environ["GITHUB_REPOSITORY"]
    return {Path(p).name: f"https://raw.githubusercontent.com/{repo}/{commit}/{Path(p).name}" for p in paths}


def _gh(*args):
    return subprocess.run(["gh", *args], cwd=ROOT, capture_output=True, text=True)


def release_asset(path):
    """Uploads to a pre-release used only as a media bucket. Returns the download URL."""
    if _gh("release", "view", RELEASE_TAG).returncode != 0:
        p = _gh("release", "create", RELEASE_TAG, "--prerelease", "--latest=false",
                "--title", "BBG News media (temporary)", "--notes", "Temporary files for Instagram posts.")
        if p.returncode != 0:
            raise RuntimeError(f"gh release create failed: {p.stderr.strip()}")
    p = _gh("release", "upload", RELEASE_TAG, str(path), "--clobber")
    if p.returncode != 0:
        raise RuntimeError(f"gh release upload failed: {p.stderr.strip()}")
    repo = os.environ["GITHUB_REPOSITORY"]
    return f"https://github.com/{repo}/releases/download/{RELEASE_TAG}/{Path(path).name}"


def remove_release_asset(path):
    p = _gh("release", "delete-asset", RELEASE_TAG, Path(path).name, "--yes")
    if p.returncode != 0:
        print(f"Warning: couldn't delete release asset {Path(path).name}: {p.stderr.strip()}")
