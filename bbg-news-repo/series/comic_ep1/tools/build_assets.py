"""Ep 1 comic: build every free panel, the two local design references and (for
lettering tests) grey mock-ups of the new art. No generation credits.

Every path is relative to series/comic_ep1/. Run build_layout.py first (it writes
tools/build/crops.json and tools/build/mocks.json).

  python3 -I series/comic_ep1/tools/build_assets.py [--src DIR] [--mock DIR] [--teaser-fallback]

What it does:
  - panels/p07, p24, p26, p27, p29.png: the local original-art graphics (always rebuilt).
  - panels/<id>.png for the 13 crops of approved art and refs/P1b_blue_hull.png and
    refs/P3r_field.png: rebuilt only with --src, the folder of full-resolution originals
    (stills/C1_still.png, plates/P1.png, plates/P3.png, clips/C1_take1.mp4; ffmpeg for the
    clip frame). Without --src the committed files are kept. The originals are not in the
    repo; re-download them by the job IDs in panels.json (reuse_source.job_id).
  - panels/<id>.png for every new generation and its crops, once the approved download is
    saved as src/<generation panel id>_raw.png (crop_frac from panels.json).
  - --mock DIR: writes DIR/panels/ with every built panel plus grey mock-ups (planned faces
    drawn in) of the panels still missing, for `letter.py --root DIR` lettering tests.
  - --teaser-fallback: if G01 failed twice, writes panels/t01a.png from the C1 start still
    (crop_px [0, 0, 1536, 1951], exactly 1000:1270) instead of the G01 crop. Needs --src.
"""
import argparse
import json
import math
import random
import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

EP = Path(__file__).resolve().parents[1]
BUILD = EP / "tools" / "build"
PANELS = EP / "panels"
REFS = EP / "refs"
SRC_RAW = EP / "src"

ap = argparse.ArgumentParser()
ap.add_argument("--src", help="folder of full-resolution originals (stills/, plates/, clips/)")
ap.add_argument("--mock", help="write mock-up panels for lettering tests to DIR/panels")
ap.add_argument("--teaser-fallback", action="store_true",
                help="cut t01a from the C1 start still instead of G01 (needs --src)")
args = ap.parse_args()
PANELS.mkdir(exist_ok=True)
REFS.mkdir(exist_ok=True)

# ---------------- crops of approved art (only with --src) ----------------
CROPS = json.loads((BUILD / "crops.json").read_text())
ORIG = {"C1_still": "stills/C1_still.png", "P1": "plates/P1.png", "P3": "plates/P3.png",
        "clip": "clips/C1_take1.mp4"}
built = []
if args.src:
    S = Path(args.src)
    missing = [v for v in ORIG.values() if not (S / v).exists()]
    if missing:
        raise SystemExit("--src %s lacks %s" % (S, ", ".join(missing)))
    c1 = Image.open(S / ORIG["C1_still"]).convert("RGB")
    p1 = Image.open(S / ORIG["P1"]).convert("RGB")
    p3 = Image.open(S / ORIG["P3"]).convert("RGB")
    with tempfile.TemporaryDirectory() as td:
        fp = Path(td) / "f_7.0.png"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "7.0", "-i", str(S / ORIG["clip"]),
                        "-frames:v", "1", str(fp)], check=True)
        f70 = Image.open(fp).convert("RGB")
        f70.load()
    SRC = {"C1_still": c1, "P1": p1, "clip_7.0": f70}
    for pid, c in CROPS.items():
        im = SRC[c["src"]].crop(tuple(c["box"]))
        tw, th = c["rect"]
        assert abs(tw / th - im.width / im.height) / (tw / th) < 0.02, (pid, tw / th, im.size)
        im.save(PANELS / f"{pid}.png")
        built.append(pid)

    # local design references (no generation)
    # P1b: approved P1 with its tomato-red bands hue-shifted to royal blue, hull and hilltop only.
    hsv = p1.crop((0, 0, 1536, 1600)).convert("HSV")
    h_, s_, v_ = hsv.split()
    hp, sp, vp = h_.load(), s_.load(), v_.load()
    for y in range(hsv.height):
        for x in range(hsv.width):
            hh, ss, vv = hp[x, y], sp[x, y], vp[x, y]
            # red/orange-red hues (PIL hue 0-255): <= 14 or >= 238, saturated enough
            if (hh <= 14 or hh >= 238) and ss > 80 and vv > 40:
                hp[x, y] = 160          # royal blue (~226 deg)
                sp[x, y] = min(255, int(ss * 1.05))
    Image.merge("HSV", (h_, s_, v_)).convert("RGB").save(REFS / "P1b_blue_hull.png")
    # P3r: P3's right half only (field, sandbags, trench zig-zag, hills); the airliner-like nose is cut out.
    p3.crop((750, 0, 1536, 2752)).save(REFS / "P3r_field.png")
    if args.teaser_fallback:
        c1.crop((0, 0, 1536, 1951)).save(PANELS / "t01a.png")
        built.append("t01a (fallback: C1 still)")
elif args.teaser_fallback:
    raise SystemExit("--teaser-fallback needs --src")

# ---------------- new generations and their crops (once downloaded) ----------------
PANELS_JSON = json.loads((EP / "panels.json").read_text())
for e in PANELS_JSON:
    if e.get("gen"):
        raw = EP / e["raw_download"]
        if raw.exists():
            shutil.copy(raw, PANELS / f"{e['id']}.png")
            built.append(e["id"])
    rs = e.get("reuse_source") or {}
    if "crop_frac" in rs:
        if e["id"] == "t01a" and args.teaser_fallback:
            continue
        raw = EP / rs["file"]
        if raw.exists():
            im = Image.open(raw).convert("RGB")
            x0, y0, x1, y1 = rs["crop_frac"]
            im.crop((round(x0 * im.width), round(y0 * im.height),
                     round(x1 * im.width), round(y1 * im.height))).save(PANELS / f"{e['id']}.png")
            built.append(e["id"])

# ---------------- local original-art graphics (no text, no logos) ----------------
NAVY = (11, 18, 32)
CYAN = (56, 214, 215)


def scanlines(im, step=6, alpha=22):
    ov = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    for y in range(0, im.size[1], step):
        d.line([(0, y), (im.size[0], y)], fill=(255, 255, 255, alpha), width=1)
    return Image.alpha_composite(im.convert("RGBA"), ov)


def g_scan(w, h, line_at, name):
    im = Image.new("RGBA", (w, h), NAVY + (255,))
    d = ImageDraw.Draw(im)
    for x in range(0, w, 80):
        d.line([(x, 0), (x, h)], fill=(40, 70, 90, 255), width=1)
    for y in range(0, h, 80):
        d.line([(0, y), (w, y)], fill=(40, 70, 90, 255), width=1)
    im = scanlines(im)
    glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    y = int(h * line_at)
    ImageDraw.Draw(glow).rectangle([0, y - 10, w, y + 10], fill=CYAN + (160,))
    im = Image.alpha_composite(im, glow.filter(ImageFilter.GaussianBlur(18)))
    ImageDraw.Draw(im).line([(0, y), (w, y)], fill=(200, 255, 255, 255), width=4)
    im.convert("RGB").save(PANELS / name)


def hexagon(cx, cy, r, rot=30):
    return [(cx + r * math.cos(math.radians(rot + 60 * i)),
             cy + r * math.sin(math.radians(rot + 60 * i))) for i in range(6)]


def token(im, cx, cy, r):
    """A Joule-style token: dark hexagon, blue bolt, violet halo (original art)."""
    halo = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).ellipse([cx - r * 1.5, cy - r * 1.5, cx + r * 1.5, cy + r * 1.5],
                                 fill=(123, 75, 214, 150))
    im.alpha_composite(halo.filter(ImageFilter.GaussianBlur(r * 0.35)))
    d = ImageDraw.Draw(im)
    d.polygon(hexagon(cx, cy, r), fill=(29, 32, 48, 255))
    d.line(hexagon(cx, cy, r) + [hexagon(cx, cy, r)[0]], fill=(120, 130, 170, 255), width=6)
    s = r / 60
    bolt = [(cx + 8 * s, cy - 42 * s), (cx - 22 * s, cy + 6 * s), (cx - 2 * s, cy + 6 * s),
            (cx - 10 * s, cy + 42 * s), (cx + 22 * s, cy - 8 * s), (cx + 2 * s, cy - 8 * s)]
    d.polygon(bolt, fill=(63, 169, 245, 255))


def g_ledger(w, h, name):
    im = Image.new("RGBA", (w, h), (20, 22, 29, 255))
    rnd = random.Random(7)
    d = ImageDraw.Draw(im)
    for _ in range(9000):
        x, y = rnd.randrange(w), rnd.randrange(h)
        g = rnd.randrange(24, 40)
        d.point((x, y), fill=(g, g, g + 6, 255))
    d.rectangle([0, 0, w, 12], fill=(212, 160, 23, 255))
    d.rectangle([60, int(h * 0.555), w - 60, int(h * 0.555) + 4], fill=(212, 160, 23, 140))
    for i in range(3):
        token(im, int(w * 0.70) + i * 190, int(h * 0.47), 66)
    im.convert("RGB").save(PANELS / name)


def g_upload(w, h, name):
    """B-1000's upload screen: navy HUD with a segmented bar frozen one segment short.
    The last segment is drawn hollow (outline only), so the gap reads on a phone
    (about 37 px wide on the 1080 px slide)."""
    im = Image.new("RGBA", (w, h), NAVY + (255,))
    d = ImageDraw.Draw(im)
    for x in range(0, w, 80):
        d.line([(x, 0), (x, h)], fill=(30, 52, 70, 255), width=1)
    for y in range(0, h, 80):
        d.line([(0, y), (w, y)], fill=(30, 52, 70, 255), width=1)
    im = scanlines(im)
    d = ImageDraw.Draw(im)
    x0, x1 = 50, w - 50
    y0, y1 = int(h * 0.83), int(h * 0.93)
    d.rectangle([x0, y0, x1, y1], outline=CYAN + (255,), width=6)
    n = 12
    seg = (x1 - x0 - 24) / n
    for i in range(n):
        sx = x0 + 12 + i * seg
        box = [sx + 4, y0 + 14, sx + seg - 4, y1 - 14]
        if i < n - 1:
            d.rectangle(box, fill=CYAN + (255,))
        else:
            d.rectangle(box, fill=(16, 30, 44, 255), outline=CYAN + (255,), width=4)
    im.convert("RGB").save(PANELS / name)


def g_glitch(w, h, name):
    """Pink static with the Huggable's stitched chest seam (hijacker clue)."""
    rnd = random.Random(42)
    im = Image.new("RGB", (w, h), (255, 111, 181))
    px = im.load()
    for y in range(h):
        band = rnd.random() < 0.08
        shift = rnd.randrange(-60, 60) if band else 0
        for x in range(w):
            n = rnd.randrange(-70, 70)
            r, g, b = 255, 111 + n // 2, 181 + n // 3
            if band:
                r, g, b = 255, 200, 230
            px[(x + shift) % w, y] = (max(0, min(255, r + n // 3)), max(0, min(255, g)),
                                      max(0, min(255, b)))
    im = im.filter(ImageFilter.GaussianBlur(0.6))
    d = ImageDraw.Draw(im)
    cy = h * 0.62
    pts = [(i, cy + (10 if (i // 36) % 2 else -10)) for i in range(0, w + 1, 36)]
    for x0, y0 in pts:
        d.polygon([(x0 - 5, y0 - 10), (x0 + 5, y0 - 10), (x0, y0 - 34)], fill=(52, 22, 40))
        d.polygon([(x0 - 5, y0 + 10), (x0 + 5, y0 + 10), (x0, y0 + 34)], fill=(52, 22, 40))
    d.line(pts, fill=(205, 200, 210), width=14)
    im.save(PANELS / name)


g_scan(2000, 400, 0.80, "p07.png")      # s03 sting band, 1000x200
g_ledger(2000, 1120, "p24.png")         # s12 ledger card, 1000x560
g_upload(1120, 1380, "p26.png")         # s12 upload screen, 560x690
g_glitch(2000, 600, "p27.png")          # s13 pink glitch, 1000x300
g_scan(2000, 2320, 0.215, "p29.png")    # s14 end-card screen, 1000x1160
built += ["p07", "p24", "p26", "p27", "p29"]

# ---------------- mock-ups of new art, for lettering tests only ----------------
if args.mock:
    MOCK = Path(args.mock) / "panels"
    MOCK.mkdir(parents=True, exist_ok=True)
    for f in PANELS.glob("*.png"):
        shutil.copy(f, MOCK / f.name)
    MOCKS = json.loads((BUILD / "mocks.json").read_text())
    n_mock = 0
    for pid, m in MOCKS.items():
        if (PANELS / f"{pid}.png").exists():
            continue
        rx, ry, rw, rh = m["rect"]
        im = Image.new("RGB", (rw, rh), (120, 128, 138))
        d = ImageDraw.Draw(im)
        for x, y, w, h, label in m.get("shapes", []):
            d.ellipse([x - rx, y - ry, x - rx + w, y - ry + h], fill=(200, 160, 120), outline=(0, 0, 0),
                      width=3)
            d.text((x - rx + 8, y - ry + h // 2 - 6), label, fill=(0, 0, 0))
        d.text((10, 10), f"{pid} MOCK: {m['note']}", fill=(255, 255, 255))
        im.save(MOCK / f"{pid}.png")
        n_mock += 1
    print("mock panels in", MOCK, "(%d mock-ups)" % n_mock)
print("built:", ", ".join(built))
print("panels/ now holds", len(list(PANELS.glob("*.png"))), "files")
