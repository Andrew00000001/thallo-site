#!/usr/bin/env python3
"""BBG News comic lettering and page-assembly engine.

Renders every page of a pages JSON (see README.md in this folder) into
finished Instagram carousel slides: panels cover-fitted around a focus
point, black panel borders, and comic lettering (speech balloons, shouts,
whispers, thought clouds, captions, B-1000's HUD boxes, SFX, the cover
title and the end card).

Usage:
    python3 letter.py pages.json --out DIR [--root DIR_OF_IMAGES] [--jpg]
                      [--only s01,s02] [--guides] [--sheet] [--strict]

Only Pillow and the standard library are used.
"""

import argparse
import hashlib
import json
import math
import os
import random
import re
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageColor, ImageDraw, ImageFilter, ImageFont

try:
    from PIL import ImageCms
except ImportError:  # Pillow built without littlecms
    ImageCms = None

Image.MAX_IMAGE_PIXELS = 200_000_000

SS = 4                      # supersampling factor for all vector lettering
TAIL_GAP = 0.8              # default gap between a tail tip and its target, x text size
REF_W = 1080.0              # sizes in this file are px at a 1080 px-wide canvas
DIALOGUE_MIN = 30           # smallest dialogue size at 1080 px wide
MARGIN = 40                 # outer margin (px at 1080 wide)
GUTTER = (16, 24)           # allowed gutter range
MAX_SLIDES = 20             # Instagram carousel limit

FONT_DIR = Path(os.environ.get("BBG_FONT_DIR",
                               Path(__file__).resolve().parents[2] / "assets" / "fonts"))

# Font keys -> files in assets/fonts. A missing file falls back along FALLBACK.
FONT_FILES = {
    "comic": "ComicNeue-Bold.ttf",            # dialogue (OFL)
    "comic-italic": "ComicNeue-BoldItalic.ttf",  # **emphasis**, shouts (OFL)
    "comic-light": "ComicNeue-Regular.ttf",   # whispers (OFL)
    "bangers": "Bangers-Regular.ttf",         # SFX and titles (OFL)
    "anton": "Anton-Regular.ttf",             # BBG News display face (OFL)
    "barlow": "Barlow-SemiBold.ttf",          # end card, placeholders (OFL)
    "rounded": "Nunito-VariableFont_wght.ttf",   # B-1000 HUD, ExtraBold 800 (OFL)
    "rounded-black": "Nunito-VariableFont_wght.ttf",  # "LOCAL HAZARDS" sting, Black 900 (OFL)
    "mono": "ShareTechMono-Regular.ttf",      # former HUD face, kept as the rounded fallback (OFL)
}
# Variable fonts: axis name -> value, applied whenever the key is loaded.
FONT_AXES = {"rounded": {"Weight": 800}, "rounded-black": {"Weight": 900}}
FALLBACK = {"comic": "barlow", "comic-italic": "comic", "comic-light": "comic",
            "bangers": "anton", "anton": "barlow", "mono": "barlow",
            "rounded": "mono", "rounded-black": "rounded"}
# Comic Neue draws every capital I with crossbars. Lettering convention keeps
# the crossbar I for the pronoun only, so other capital I's use the plain
# vertical stroke of the font's own lowercase l (same height, same weight).
PLAIN_I_FONTS = {"comic", "comic-italic", "comic-light"}
SYSTEM_FALLBACKS = ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
                    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]

DIALOGUE_TYPES = {"balloon", "shout", "whisper", "thought", "caption", "hud"}
LETTER_TYPES = DIALOGUE_TYPES | {"sfx", "title", "endcard"}

DEFAULTS = {
    "balloon": dict(size=36, font="comic", bold="comic-italic", color="#141414",
                    fill="#ffffff", outline="#141414", outline_width=3.5, upper=True),
    "shout": dict(size=40, font="comic", bold="comic-italic", color="#141414",
                  fill="#ffffff", outline="#141414", outline_width=4, upper=True),
    "whisper": dict(size=33, font="comic-light", bold="comic", color="#2a2a2e",
                    fill="#ffffff", outline="#141414", outline_width=3, upper=True),
    "thought": dict(size=34, font="comic", bold="comic-italic", color="#141414",
                    fill="#ffffff", outline="#141414", outline_width=3.5, upper=True),
    "caption": dict(size=32, font="comic", bold="comic-italic", color="#141414",
                    fill="#fff1a8", outline="#141414", outline_width=3, upper=True),
    "hud": dict(size=32, font="rounded", bold="rounded", color="#62f3ff",
                fill="#05090ecc", outline="#62f3ffb0", outline_width=2, upper=True),
    "sfx": dict(size=None, font="bangers", fill="#ffe14d", fill2="#ff7a1a",
                outline="#141414", angle=8, upper=True),
    "title": dict(size=None, font="bangers", fill="#ffe45c", fill2="#f5a300",
                  outline="#141414", angle=0, upper=True),
    "endcard": dict(size=26, font="barlow", bold="barlow", color="#d9dae0",
                    fill="#0e0f14", outline=None, outline_width=0, upper=False),
}

WARNINGS = []


def warn(msg):
    WARNINGS.append(msg)
    print("  warning: " + msg, file=sys.stderr)


# --------------------------------------------------------------------------
# Small helpers
# --------------------------------------------------------------------------

def rgba(value, default=None):
    """'#rgb', '#rrggbb', '#rrggbbaa', a colour name or [r,g,b(,a)] -> RGBA."""
    if value is None:
        value = default
    if value is None:
        return None
    if isinstance(value, (list, tuple)):
        v = [int(c) for c in value]
        return tuple(v + [255] * (4 - len(v)))[:4]
    s = str(value).strip()
    if s.startswith("#") and len(s) == 9:
        return tuple(int(s[i:i + 2], 16) for i in (1, 3, 5, 7))
    c = ImageColor.getrgb(s)
    return tuple(list(c) + [255] * (4 - len(c)))[:4]


def lerp(a, b, t):
    return a + (b - a) * t


def vlen(x, y):
    return math.hypot(x, y)


def seeded(*parts):
    h = hashlib.sha1("|".join(str(p) for p in parts).encode()).hexdigest()
    return random.Random(int(h[:12], 16))


def bezier(p0, p1, p2, steps):
    out = []
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        out.append((u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0],
                    u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]))
    return out


def rects_overlap(a, b):
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


# --------------------------------------------------------------------------
# Fonts
# --------------------------------------------------------------------------

class FontBook:
    def __init__(self, font_dir, root):
        self.font_dir = Path(font_dir)
        self.root = Path(root)
        self.cache = {}
        self.cover = {}
        self.used = {}
        # glyph fallbacks, tried in order for characters a font lacks
        self.fallback_paths = []
        barlow = self.font_dir / FONT_FILES["barlow"]
        if barlow.exists():
            self.fallback_paths.append(str(barlow))
        system = [p for p in SYSTEM_FALLBACKS if Path(p).exists()]
        if system:                       # the first system font found is enough
            self.fallback_paths.append(system[0])

    def resolve(self, key):
        """Font key or path -> (path, effective key)."""
        seen = []
        k = key
        while k is not None and k not in seen:
            seen.append(k)
            if k in FONT_FILES:
                p = self.font_dir / FONT_FILES[k]
                if p.exists():
                    if k != key:
                        self._note_fallback(key, k)
                    return str(p), k
                k = FALLBACK.get(k)
                continue
            p = Path(k)
            for cand in (p, self.root / p, self.font_dir / p):
                if cand.exists():
                    return str(cand), k
            warn("font %r not found, using barlow" % key)
            k = "barlow"
        raise SystemExit("no usable font for %r (looked in %s)" % (key, self.font_dir))

    def _note_fallback(self, want, got):
        tag = (want, got)
        if tag not in self.used:
            self.used[tag] = True
            warn("font %r missing in %s, fell back to %r" % (want, self.font_dir, got))

    def font(self, key, px):
        path, eff = self.resolve(key)
        px = max(1, int(round(px)))
        axes = FONT_AXES.get(eff)
        ck = (path, px, tuple(sorted(axes.items())) if axes else None)
        if ck not in self.cache:
            f = ImageFont.truetype(path, px)
            if axes:
                set_axes(f, axes, eff)
            self.cache[ck] = f
        return self.cache[ck], eff

    def raw(self, path, px):
        px = max(1, int(round(px)))
        ck = (path, px)
        if ck not in self.cache:
            self.cache[ck] = ImageFont.truetype(path, px)
        return self.cache[ck]

    def covers(self, font, ch):
        """True when the font has a real glyph for ch (not .notdef)."""
        if ord(ch) < 128:
            return True
        ck = (font.path, ch)
        if ck not in self.cover:
            probe = ImageFont.truetype(font.path, 48)
            self.cover[ck] = _glyph_bytes(probe, ch) != _glyph_bytes(probe, "￿")
        return self.cover[ck]


def set_axes(font, axes, key):
    """Set a variable font's axes by name (e.g. {"Weight": 800})."""
    try:
        info = font.get_variation_axes()
        values = []
        for a in info:
            name = a["name"].decode() if isinstance(a["name"], bytes) else str(a["name"])
            v = axes.get(name, a.get("default"))
            values.append(min(max(v, a["minimum"]), a["maximum"]))
        font.set_variation_by_axes(values)
    except (OSError, AttributeError, KeyError) as e:
        warn("font %r: could not set axes %s (%s); using its default instance" % (key, axes, e))


def _glyph_bytes(font, ch):
    im = Image.new("L", (96, 96), 0)
    ImageDraw.Draw(im).text((20, 70), ch, font=font, fill=255, anchor="ls")
    return im.tobytes()


# --------------------------------------------------------------------------
# Rich text: **bold** emphasis, \n breaks, word measuring
# --------------------------------------------------------------------------

BREAK = None
PRONOUN_I = re.compile(r"^[\"'“‘(\[.…\-–—]*I(?:['’](?:M|LL|D|VE))?[\"'”’)\].,!?;:…\-–—]*$")


class Word:
    __slots__ = ("runs", "w")

    def __init__(self, runs, w):
        self.runs = runs   # list of (text, style): r body, b emphasis, f0.. fallbacks
        self.w = w         # width in supersampled px


class TextStyle:
    """Fonts and metrics for one letter, all measured at SS scale."""

    def __init__(self, book, size, font_key, bold_key, upper=True, lead=1.17,
                 tracking=0.0):
        self.book = book
        self.size = size
        self.upper = upper
        self.lead = lead
        reg, reg_eff = book.font(font_key, size * SS)
        bold, bold_eff = book.font(bold_key or font_key, size * SS)
        self.fonts = {"r": reg, "b": bold}
        self.fallbacks = []
        for i, path in enumerate(book.fallback_paths):
            key = "f%d" % i
            self.fonts[key] = book.raw(path, size * SS)
            self.fallbacks.append(key)
        self.plain_i = {"r": upper and reg_eff in PLAIN_I_FONTS,
                        "b": upper and bold_eff in PLAIN_I_FONTS}
        self.tracking = tracking * size * SS
        self.space = reg.getlength(" ") + self.tracking
        self.cap = -reg.getbbox("H", anchor="ls")[1]           # cap height, SS px
        self.lp = size * SS * lead                              # line pitch, SS px

    def run_width(self, text, style):
        f = self.fonts[style]
        w = f.getlength(text)
        if self.tracking:
            w += self.tracking * max(0, len(text) - 1)
        return w

    def tokens(self, text):
        if self.upper:
            text = text.upper()
        chars = []
        for i, part in enumerate(str(text).split("**")):
            for ch in part:
                chars.append((ch, "b" if i % 2 else "r"))
        out, cur = [], []
        for ch, st in chars:
            if ch == "\n":
                if cur:
                    out.append(self._word(cur))
                    cur = []
                out.append(BREAK)
            elif ch.isspace():
                if cur:
                    out.append(self._word(cur))
                    cur = []
            else:
                cur.append((ch, st))
        if cur:
            out.append(self._word(cur))
        return out

    def _word(self, chars):
        raw = "".join(c for c, _ in chars)
        keep_i = bool(PRONOUN_I.match(raw))
        runs = []
        for ch, st in chars:
            if ch == "I" and not keep_i and self.plain_i.get(st):
                ch = "l"
            if not self.book.covers(self.fonts[st], ch):
                for fk in self.fallbacks:
                    st = fk
                    if self.book.covers(self.fonts[fk], ch):
                        break
            if runs and runs[-1][1] == st:
                runs[-1] = (runs[-1][0] + ch, st)
            else:
                runs.append((ch, st))
        w = sum(self.run_width(t, s) for t, s in runs)
        return Word(runs, w)


def greedy(tokens, caps, space):
    """Fill lines in order with per-line capacities (SS px). Returns
    [(words, width)] or None when the text does not fit len(caps) lines."""
    lines, cur, curw = [], [], 0.0
    n = len(caps)
    for tok in tokens:
        if tok is BREAK:
            lines.append((cur, curw))
            cur, curw = [], 0.0
            if len(lines) >= n:
                return None
            continue
        if cur and curw + space + tok.w <= caps[len(lines)]:
            cur.append(tok)
            curw += space + tok.w
            continue
        if cur:
            lines.append((cur, curw))
            cur, curw = [], 0.0
            if len(lines) >= n:
                return None
        if tok.w > caps[len(lines)]:
            return None
        cur, curw = [tok], tok.w
    lines.append((cur, curw))
    return lines


def wrap_balanced(tokens, maxw, space):
    """Wrap to at most maxw (SS px) with as few lines as possible, then
    narrow the measure until just before a new line appears, so lines come
    out even instead of one long line and a stub."""
    words = [t for t in tokens if t is not BREAK]
    if not words:
        return [([], 0.0)]
    widest = max(t.w for t in words)
    maxw = max(maxw, widest)
    big = [maxw] * 64
    base = greedy(tokens, big, space)
    n = len(base)
    lo, hi = widest, maxw
    for _ in range(30):
        mid = (lo + hi) / 2
        r = greedy(tokens, [mid] * 64, space)
        if r is not None and len(r) <= n:
            hi = mid
        else:
            lo = mid
    return greedy(tokens, [hi + 0.01] * 64, space)


def block_height(style, nlines):
    return style.cap + (nlines - 1) * style.lp


def draw_lines(mask, style, lines, cx=None, left=None, top=0.0, align="center", embolden=0):
    """Draw wrapped lines into an L mask. cx/left/top are SS px in mask space."""
    d = ImageDraw.Draw(mask)
    for i, (words, w) in enumerate(lines):
        base = top + style.cap + i * style.lp
        if align == "left":
            x = left
        elif align == "right":
            x = left - w
        else:
            x = cx - w / 2
        for j, word in enumerate(words):
            if j:
                x += style.space
            for text, st in word.runs:
                f = style.fonts[st]
                if style.tracking:
                    for ch in text:
                        d.text((x, base), ch, font=f, fill=255, anchor="ls",
                               stroke_width=embolden, stroke_fill=255)
                        x += f.getlength(ch) + style.tracking
                    x -= style.tracking
                else:
                    d.text((x, base), text, font=f, fill=255, anchor="ls",
                           stroke_width=embolden, stroke_fill=255)
                    x += f.getlength(text)


# --------------------------------------------------------------------------
# Sprite: a supersampled RGBA tile placed on the canvas
# --------------------------------------------------------------------------

class Sprite:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = int(math.floor(x0)) - 2
        self.y0 = int(math.floor(y0)) - 2
        self.w = int(math.ceil(x1)) + 2 - self.x0
        self.h = int(math.ceil(y1)) + 2 - self.y0
        self.img = Image.new("RGBA", (self.w * SS, self.h * SS), (0, 0, 0, 0))
        self.body = None   # canvas bbox of the balloon body, for checks
        self.target = None

    def p(self, x, y):
        return ((x - self.x0) * SS, (y - self.y0) * SS)

    def pts(self, pts):
        return [self.p(x, y) for x, y in pts]

    def mask(self):
        return Image.new("L", self.img.size, 0)

    def paint(self, color, mask, offset=(0, 0)):
        if color is None:
            return
        r, g, b, a = color
        if a == 0:
            return
        if a < 255:
            mask = mask.point(lambda v: v * a // 255)
        layer = Image.new("RGBA", self.img.size, (r, g, b, 0))
        layer.putalpha(mask)
        if offset != (0, 0):
            shifted = Image.new("RGBA", self.img.size, (r, g, b, 0))
            shifted.paste(layer, (int(offset[0]), int(offset[1])))
            layer = shifted
        self.img.alpha_composite(layer)

    def finish(self):
        return self.img.reduce(SS)


# --------------------------------------------------------------------------
# Balloon geometry
# --------------------------------------------------------------------------

def superellipse(cx, cy, a, b, n, k=720):
    pts = []
    e = 2.0 / n
    for i in range(k):
        t = 2 * math.pi * i / k
        c, s = math.cos(t), math.sin(t)
        pts.append((cx + a * math.copysign(abs(c) ** e, c),
                    cy + b * math.copysign(abs(s) ** e, s)))
    return pts


def fit_ellipse(tokens, style, a, n, padx, pady):
    """Smallest semi-axis b (SS px) for which the wrapped text fits inside a
    superellipse of semi-axis a with the given clearances. Returns
    (b, lines) or None."""
    words = [t for t in tokens if t is not BREAK]
    nb = sum(1 for t in tokens if t is BREAK)
    if not words:
        return (style.cap / 2 + pady, [([], 0.0)])
    best = None
    for L in range(1 + nb, min(len(words) + nb, 18) + 1):
        H = block_height(style, L)
        ey = []
        for i in range(L):
            top = -H / 2 + i * style.lp
            ey.append(max(abs(top), abs(top + style.cap)) + pady)

        def caps(bv):
            out = []
            for e in ey:
                if e >= bv:
                    out.append(-1.0)
                else:
                    out.append(2 * (a * (1 - (e / bv) ** n) ** (1.0 / n) - padx))
            return out

        lo, hi = max(ey), max(ey) + 40 * a
        if greedy(tokens, caps(hi), style.space) is None:
            continue
        for _ in range(36):
            mid = (lo + hi) / 2
            if greedy(tokens, caps(mid), style.space) is None:
                lo = mid
            else:
                hi = mid
        lines = greedy(tokens, caps(hi), style.space)
        if lines is None or len(lines) != L:
            continue
        if best is None or hi < best[0]:
            best = (hi, lines)
    return best


def fit_balloon(tokens, style, a_max, n, padx, pady, snug=True, aspect=1.9, line_cost=0.08):
    """Choose semi-axes (a, b) in SS px for the text. With snug, a may shrink
    below a_max so the balloon hugs the text with a pleasing aspect."""
    words = [t for t in tokens if t is not BREAK]
    widest = max((t.w for t in words), default=0.0)
    a_min = widest / 2 + padx + 1
    cands = [a_max]
    if snug:
        a = a_max
        while True:
            a *= 0.97
            if a < a_min:
                break
            cands.append(a)
    best = None
    for a in cands:
        r = fit_ellipse(tokens, style, a, n, padx, pady)
        if r is None:
            continue
        b, lines = r
        cost = a * b * (1 + 0.9 * math.log((a / b) / aspect) ** 2) * (1 + line_cost * (len(lines) - 1))
        if best is None or cost < best[0]:
            best = (cost, a, b, lines)
    if best is None:
        return None
    return best[1], best[2], best[3]


def tail_geometry(perim, cx, cy, target, size, base_half, gap, curve, min_len):
    """Return (i_left, i_right, side_left, side_right) for a tapered curved
    tail leaving the outline polygon perim (canvas px) toward target."""
    tx, ty = target
    phi = math.atan2(ty - cy, tx - cx)
    k = len(perim)
    best_i, best_d = 0, 9.0
    for i, (x, y) in enumerate(perim):
        d = abs((math.atan2(y - cy, x - cx) - phi + math.pi) % (2 * math.pi) - math.pi)
        if d < best_d:
            best_i, best_d = i, d
    ex, ey = perim[best_i]
    dist = vlen(tx - ex, ty - ey)
    # inside the balloon: no tail
    if vlen(tx - cx, ty - cy) <= vlen(ex - cx, ey - cy) + 2:
        return None
    ux, uy = (tx - ex) / dist, (ty - ey) / dist
    length = max(min_len, dist - gap)
    tip = (ex + ux * length, ey + uy * length)
    base_half = min(base_half, 0.32 * length)

    def walk(step):
        acc, i = 0.0, best_i
        while acc < base_half:
            j = (i + step) % k
            acc += vlen(perim[j][0] - perim[i][0], perim[j][1] - perim[i][1])
            i = j
        return i

    i_r, i_l = walk(1), walk(-1)
    # bend: the control point drifts toward the tip's side, so the tail
    # leaves the balloon steeply and turns into the speaker.
    mx, my = (ex + tip[0]) / 2, (ey + tip[1]) / 2
    px, py = -uy, ux
    sgn = 1.0 if px * (tip[0] - ex) >= 0 else -1.0
    if abs(tip[0] - ex) < 1e-6:
        sgn = 1.0
    bend = curve * length * sgn
    ctrl = (mx + px * bend, my + py * bend)
    A, B = perim[i_l], perim[i_r]
    ca = (ctrl[0] + (A[0] - ex) * 0.45, ctrl[1] + (A[1] - ey) * 0.45)
    cb = (ctrl[0] + (B[0] - ex) * 0.45, ctrl[1] + (B[1] - ey) * 0.45)
    side_l = bezier(A, ca, tip, 28)
    side_r = bezier(tip, cb, B, 28)
    return i_l, i_r, side_l, side_r, tip


def union_outline(perim, tail):
    """Outline polygon of balloon + tail (tail inserted into the perimeter)."""
    if tail is None:
        return list(perim)
    i_l, i_r, side_l, side_r = tail[:4]
    k = len(perim)
    out = []
    i = i_r
    while True:
        out.append(perim[i])
        if i == i_l:
            break
        i = (i + 1) % k
    out.extend(side_l[1:])
    out.extend(side_r[1:-1])
    return out


def stroke_closed(mask, pts, width):
    d = ImageDraw.Draw(mask)
    d.line(pts + pts[:2], fill=255, width=max(1, int(round(width))), joint="curve")


def dashed_closed(mask, pts, width, dash, gap):
    d = ImageDraw.Draw(mask)
    w = max(1, int(round(width)))
    r = w / 2.0
    seq = pts + [pts[0]]
    on, left = True, dash
    cur = [seq[0]]
    for i in range(1, len(seq)):
        x0, y0 = seq[i - 1]
        x1, y1 = seq[i]
        seg = vlen(x1 - x0, y1 - y0)
        pos = 0.0
        while seg - pos > left:
            pos += left
            t = pos / seg
            pt = (lerp(x0, x1, t), lerp(y0, y1, t))
            if on:
                cur.append(pt)
                d.line(cur, fill=255, width=w, joint="curve")
                for cx, cy in (cur[0], cur[-1]):
                    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=255)
            cur = [pt]
            on = not on
            left = dash if on else gap
        left -= seg - pos
        if on:
            cur.append((x1, y1))
    if on and len(cur) > 1:
        d.line(cur, fill=255, width=w, joint="curve")


# --------------------------------------------------------------------------
# Letter renderers. Each returns a Sprite. Geometry is in canvas px.
# --------------------------------------------------------------------------

class Ctx:
    def __init__(self, book, W, H, page_id):
        self.book = book
        self.W, self.H = W, H
        self.k = W / REF_W
        self.page_id = page_id


def opt(spec, key, kind, default=None):
    if key in spec:
        return spec[key]
    return DEFAULTS.get(kind, {}).get(key, default)


def letter_size(spec, kind, ctx):
    size = spec.get("size")
    if size is None:
        base = DEFAULTS[kind]["size"]
        size = None if base is None else base * ctx.k
    if size is not None and kind in DIALOGUE_TYPES and size < DIALOGUE_MIN * ctx.k:
        warn("%s/%s: size %s is below the %d px dialogue minimum; using %d"
             % (ctx.page_id, spec.get("_id"), size, DIALOGUE_MIN, round(DIALOGUE_MIN * ctx.k)))
        size = DIALOGUE_MIN * ctx.k
    return size


def make_style(spec, kind, ctx, size, lead=None):
    return TextStyle(ctx.book, size, opt(spec, "font", kind), opt(spec, "bold", kind),
                     upper=opt(spec, "upper", kind, True),
                     lead=lead or spec.get("lead", 1.17),
                     tracking=spec.get("tracking", 0.0))


def box_of(spec, ctx):
    box = spec.get("box")
    if not box or len(box) < 3:
        raise SystemExit("%s/%s: %s needs \"box\": [x, y, w]"
                         % (ctx.page_id, spec.get("_id"), spec.get("type")))
    return [float(v) for v in box]


def render_balloon(spec, kind, ctx):
    """balloon, whisper and thought share the fit; shout has its own outline."""
    size = letter_size(spec, kind, ctx)
    style = make_style(spec, kind, ctx, size)
    x, y, W = box_of(spec, ctx)[:3]
    sw = float(opt(spec, "outline_width", kind)) * ctx.k
    tokens = style.tokens(spec.get("text", ""))
    padx = spec.get("pad_x", 0.55 if kind != "thought" else 0.45) * size + sw / 2
    pady = spec.get("pad_y", 0.42 if kind != "thought" else 0.36) * size + sw / 2
    n = float(spec.get("roundness", 2.0 if kind == "thought" else 2.3))
    snug = spec.get("fit", "snug") != "box"

    if kind == "shout":
        spike = spec.get("spike", 0.62) * size
        extra = spike + sw / 2
        n = float(spec.get("roundness", 2.0))
    elif kind == "thought":
        bump = spec.get("bump", 0.72) * size
        extra = 1.15 * bump + sw / 2
    else:
        extra = sw / 2

    a_max = (W / 2 - extra) * SS
    aspect = spec.get("aspect", 1.9)
    fit = fit_balloon(tokens, style, a_max, n, padx * SS, pady * SS, snug=snug, aspect=aspect)
    if fit is None:
        widest = max((t.w for t in tokens if t is not BREAK), default=0)
        cap_a = (ctx.W / 2 - extra - 8 * ctx.k) * SS
        a_try = min(max((widest / 2 + padx * SS) * 1.5, a_max), cap_a)
        warn("%s/%s: a word is too long for a %d px wide %s; widened to %d px"
             % (ctx.page_id, spec.get("_id"), W, kind, 2 * (a_try / SS + extra)))
        fit = fit_balloon(tokens, style, a_try, n, padx * SS, pady * SS, snug=True, aspect=aspect)
        if fit is None:
            raise SystemExit("%s/%s: %r cannot fit on the canvas at %d px; shorten the word "
                             "or break it with a hyphen" % (ctx.page_id, spec.get("_id"),
                                                            spec.get("text"), size))
    a, b, lines = fit[0] / SS, fit[1] / SS, fit[2]

    anchor = spec.get("anchor", "center")
    if anchor == "left":
        cx = x + extra + a
    elif anchor == "right":
        cx = x + W - extra - a
    else:
        cx = x + W / 2
    cy = y + extra + b
    # keep the body inside the canvas
    inset = 6 * ctx.k
    ox = min(0.0, ctx.W - inset - (cx + a + extra)) + max(0.0, inset - (cx - a - extra))
    oy = min(0.0, ctx.H - inset - (cy + b + extra)) + max(0.0, inset - (cy - b - extra))
    if ox or oy:
        warn("%s/%s: %s ran off the canvas; moved by (%d, %d)"
             % (ctx.page_id, spec.get("_id"), kind, ox, oy))
        cx += ox
        cy += oy

    tail = spec.get("tail")
    body = (cx - a - extra, cy - b - extra, cx + a + extra, cy + b + extra)
    x0, y0, x1, y1 = body
    if tail:
        x0, y0 = min(x0, tail[0]), min(y0, tail[1])
        x1, y1 = max(x1, tail[0]), max(y1, tail[1])
    sp = Sprite(x0 - sw, y0 - sw, x1 + sw, y1 + sw)
    sp.body = body
    sp.target = tuple(tail) if tail else None

    fill = rgba(opt(spec, "fill", kind))
    line = rgba(opt(spec, "outline", kind))
    gap = spec.get("tail_gap", TAIL_GAP) * size
    curve = spec.get("tail_curve", 0.14)

    if kind == "thought":
        _draw_cloud(sp, spec, ctx, cx, cy, a, b, bump, sw, fill, line, tail, size)
    elif kind == "shout":
        pts = _burst_points(spec, ctx, cx, cy, a, b, spike, size, tail)
        fm, om = sp.mask(), sp.mask()
        ImageDraw.Draw(fm).polygon(sp.pts(pts), fill=255)
        stroke_closed(om, sp.pts(pts), sw * SS)
        sp.paint(fill, fm)
        sp.paint(line, om)
    else:
        perim = superellipse(cx, cy, a, b, n)
        tg = None
        if tail:
            tg = tail_geometry(perim, cx, cy, tail, size,
                               base_half=spec.get("tail_width", 0.78) * size / 2 + sw,
                               gap=gap, curve=curve, min_len=0.9 * size)
            if tg is not None:
                spec["_tip"] = tg[4]
            else:
                warn("%s/%s: tail target is inside the balloon; no tail drawn"
                     % (ctx.page_id, spec.get("_id")))
        pts = union_outline(perim, tg)
        fm, om = sp.mask(), sp.mask()
        ImageDraw.Draw(fm).polygon(sp.pts(pts), fill=255)
        if kind == "whisper":
            dashed_closed(om, sp.pts(pts), sw * SS, spec.get("dash", 0.55) * size * SS,
                          spec.get("dash_gap", 0.34) * size * SS)
        else:
            stroke_closed(om, sp.pts(pts), sw * SS)
        sp.paint(fill, fm)
        sp.paint(line, om)

    tm = sp.mask()
    H = block_height(style, len(lines))
    pcx, pcy = sp.p(cx, cy)
    embolden = int(round(0.022 * size * SS)) if kind == "shout" else 0
    draw_lines(tm, style, lines, cx=pcx, top=pcy - H / 2 + spec.get("nudge_y", 0) * SS,
               embolden=embolden)
    sp.paint(rgba(opt(spec, "color", kind)), tm)
    return sp


def _burst_points(spec, ctx, cx, cy, a, b, spike, size, tail):
    rnd = seeded(ctx.page_id, spec.get("_id"), spec.get("text"))
    per = math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))
    count = max(10, int(round(per / (spec.get("spike_spacing", 1.05) * size))))
    pts, spikes = [], []
    off = rnd.uniform(0, 2 * math.pi / count)
    for i in range(count):
        for half in (0, 1):
            t = off + 2 * math.pi * (i + 0.5 * half) / count
            c, s = math.cos(t), math.sin(t)
            px, py = cx + a * c, cy + b * s
            nx, ny = b * c, a * s
            nl = vlen(nx, ny)
            nx, ny = nx / nl, ny / nl
            if half == 0:     # valley, just outside the text ellipse
                d = 0.08 * spike
            else:             # spike tip
                d = spike * rnd.uniform(0.7, 1.25)
                spikes.append(len(pts))
            pts.append((px + nx * d, py + ny * d))
    if tail:
        phi = math.atan2(tail[1] - cy, tail[0] - cx)
        best = min(spikes, key=lambda j: abs((math.atan2(pts[j][1] - cy, pts[j][0] - cx)
                                              - phi + math.pi) % (2 * math.pi) - math.pi))
        sx, sy = pts[best]
        dx, dy = tail[0] - sx, tail[1] - sy
        dist = vlen(dx, dy)
        gap = spec.get("tail_gap", TAIL_GAP) * size
        if vlen(tail[0] - cx, tail[1] - cy) > vlen(sx - cx, sy - cy):
            L = max(0.0, dist - gap)
            pts[best] = (sx + dx / dist * L, sy + dy / dist * L)
            spec["_tip"] = pts[best]
            # widen the two valleys either side so the tail reads as a wedge
            for j in (best - 1, (best + 1) % len(pts)):
                vx, vy = pts[j]
                pts[j] = (lerp(vx, cx, 0.10), lerp(vy, cy, 0.10))
    return pts


def _draw_cloud(sp, spec, ctx, cx, cy, a, b, bump, sw, fill, line, tail, size):
    rnd = seeded(ctx.page_id, spec.get("_id"), spec.get("text"))
    per = math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))
    count = max(8, int(round(per / (bump * 1.62))))
    # evenly spaced by arc length on the ellipse
    k = 720
    ring = [(cx + a * math.cos(2 * math.pi * i / k), cy + b * math.sin(2 * math.pi * i / k))
            for i in range(k)]
    acc = [0.0]
    for i in range(1, k + 1):
        p0, p1 = ring[i - 1], ring[i % k]
        acc.append(acc[-1] + vlen(p1[0] - p0[0], p1[1] - p0[1]))
    total = acc[-1]
    circles = []
    j = 0
    start = rnd.uniform(0, total / count)
    for i in range(count):
        target = (start + total * i / count) % total
        while not (acc[j] <= target < acc[j + 1]):
            j = (j + 1) % k
        r = bump * rnd.uniform(0.86, 1.14)
        circles.append((ring[j][0], ring[j][1], r))
    om, fm = sp.mask(), sp.mask()
    do, df = ImageDraw.Draw(om), ImageDraw.Draw(fm)

    def disc(d, x, y, r):
        X, Y = sp.p(x, y)
        R = r * SS
        d.ellipse([X - R, Y - R, X + R, Y + R], fill=255)

    def ell(d, grow):
        X0, Y0 = sp.p(cx - a - grow, cy - b - grow)
        X1, Y1 = sp.p(cx + a + grow, cy + b + grow)
        d.ellipse([X0, Y0, X1, Y1], fill=255)

    half = sw / 2
    for x, y, r in circles:
        disc(do, x, y, r + half)
        disc(df, x, y, r - half)
    ell(do, half)
    ell(df, -half)
    # bubble trail toward the thinker
    if tail:
        tx, ty = tail
        phi = math.atan2(ty - cy, tx - cx)
        c, s = math.cos(phi), math.sin(phi)
        # distance from centre to the cloud's outer edge along phi
        rr = 1.0 / math.sqrt((c / a) ** 2 + (s / b) ** 2) + bump
        ex, ey = cx + c * rr, cy + s * rr
        dist = vlen(tx - ex, ty - ey)
        if vlen(tx - cx, ty - cy) > rr + 4:
            gap = spec.get("tail_gap", TAIL_GAP) * size
            radii = [0.40 * size, 0.28 * size, 0.18 * size]
            room = max(dist - gap, 0.0)
            need = sum(2 * r for r in radii)
            space = min(max((room - need) / len(radii), 0.14 * size), 0.42 * size)
            pos = 0.1 * size
            for r in radii:
                pos += r
                if pos > room + r:
                    break
                bx, by = ex + c * pos, ey + s * pos
                spec["_tip"] = (bx + c * r, by + s * r)
                disc(do, bx, by, r + half)
                disc(df, bx, by, r - half)
                pos += r + space
        else:
            warn("%s/%s: thought tail target is inside the cloud" % (ctx.page_id, spec.get("_id")))
    sp.paint(line, om)
    sp.paint(fill, fm)


def render_caption(spec, ctx):
    kind = "caption"
    size = letter_size(spec, kind, ctx)
    style = make_style(spec, kind, ctx, size)
    x, y, W = box_of(spec, ctx)[:3]
    sw = float(opt(spec, "outline_width", kind)) * ctx.k
    padx, pady = spec.get("pad_x", 0.5) * size, spec.get("pad_y", 0.42) * size
    tokens = style.tokens(spec.get("text", ""))
    lines = wrap_balanced(tokens, (W - 2 * padx - sw) * SS, style.space)
    tw = max((w for _, w in lines), default=0) / SS
    snug = spec.get("fit", "snug") != "box"
    bw = (tw + 2 * padx + sw) if snug else W
    if tw + 2 * padx + sw > W + 0.5:
        warn("%s/%s: a word is too long for a %d px caption; widened to %d px"
             % (ctx.page_id, spec.get("_id"), W, tw + 2 * padx + sw))
        bw = max(bw, tw + 2 * padx + sw)
    bh = block_height(style, len(lines)) / SS + 2 * pady + sw
    box4 = spec.get("box")
    if len(box4) > 3:
        bh = max(bh, float(box4[3]))
    anchor = spec.get("anchor", "left")
    bx = x if anchor == "left" else (x + W - bw if anchor == "right" else x + (W - bw) / 2)
    bx, by = _clamp_rect(spec, ctx, bx, y, bw, bh)
    shadow = spec.get("shadow", False)
    sh = (6 * ctx.k, 6 * ctx.k) if shadow is True else (tuple(shadow) if shadow else (0, 0))
    sp = Sprite(bx, by, bx + bw + sh[0], by + bh + sh[1])
    sp.body = (bx, by, bx + bw, by + bh)
    m = sp.mask()
    d = ImageDraw.Draw(m)
    X0, Y0 = sp.p(bx + sw / 2, by + sw / 2)
    X1, Y1 = sp.p(bx + bw - sw / 2, by + bh - sw / 2)
    rad = spec.get("radius", 0) * ctx.k * SS
    if shadow:
        sm = sp.mask()
        ImageDraw.Draw(sm).rounded_rectangle([X0 - sw * SS / 2, Y0 - sw * SS / 2,
                                              X1 + sw * SS / 2, Y1 + sw * SS / 2],
                                             radius=rad, fill=255)
        sp.paint(rgba(spec.get("shadow_color", "#000000a0")), sm,
                 offset=(sh[0] * SS, sh[1] * SS))
    d.rounded_rectangle([X0, Y0, X1, Y1], radius=rad, fill=255)
    sp.paint(rgba(opt(spec, "fill", kind)), m)
    om = sp.mask()
    ImageDraw.Draw(om).rounded_rectangle([X0, Y0, X1, Y1], radius=rad, outline=255,
                                         width=max(1, int(round(sw * SS))))
    sp.paint(rgba(opt(spec, "outline", kind)), om)
    tm = sp.mask()
    align = spec.get("align", "center")
    cx = bx + bw / 2
    top = by + (bh - block_height(style, len(lines)) / SS) / 2
    draw_lines(tm, style, lines, cx=sp.p(cx, 0)[0],
               left=sp.p(bx + sw / 2 + padx, 0)[0] if align == "left" else sp.p(bx + bw - sw / 2 - padx, 0)[0],
               top=sp.p(0, top)[1], align=align)
    sp.paint(rgba(opt(spec, "color", kind)), tm)
    return sp


def _clamp_rect(spec, ctx, x, y, w, h):
    inset = 6 * ctx.k
    nx = min(max(x, inset), ctx.W - inset - w)
    ny = min(max(y, inset), ctx.H - inset - h)
    if abs(nx - x) > 0.5 or abs(ny - y) > 0.5:
        warn("%s/%s: %s ran off the canvas; moved by (%d, %d)"
             % (ctx.page_id, spec.get("_id"), spec.get("type"), nx - x, ny - y))
    return nx, ny


def render_hud(spec, ctx):
    kind = "hud"
    size = letter_size(spec, kind, ctx)
    style = make_style(spec, kind, ctx, size, lead=spec.get("lead", 1.32))
    x, y, W = box_of(spec, ctx)[:3]
    k = ctx.k
    sw = float(opt(spec, "outline_width", kind)) * k
    padx, pady = spec.get("pad_x", 0.62) * size, spec.get("pad_y", 0.5) * size
    tokens = style.tokens(spec.get("text", ""))
    lines = wrap_balanced(tokens, (W - 2 * padx) * SS, style.space)
    tw = max((w for _, w in lines), default=0) / SS
    live = bool(spec.get("live"))
    live_size = size * 0.86
    live_font, _ = ctx.book.font(spec.get("live_font", "rounded"), live_size * SS)
    live_w = (live_size * 0.62 + 0.45 * live_size) + live_font.getlength("LIVE") / SS
    live_h = live_size * 1.25 if live else 0
    content_w = max(tw, live_w if live else 0)
    snug = spec.get("fit", "snug") != "box"
    bw = content_w + 2 * padx if snug else W
    if content_w + 2 * padx > W + 0.5:
        warn("%s/%s: a word is too long for a %d px HUD box; widened to %d px"
             % (ctx.page_id, spec.get("_id"), W, content_w + 2 * padx))
        bw = max(bw, content_w + 2 * padx)
    text_h = block_height(style, len(lines)) / SS
    bh = text_h + 2 * pady + live_h
    box4 = spec.get("box")
    if len(box4) > 3:
        bh = max(bh, float(box4[3]))
    br = spec.get("bracket", 0.17) * min(bw, bh)
    br = min(max(br, 14 * k), 40 * k)
    bo = 5 * k                      # bracket offset outside the box
    bt = 4 * k                      # bracket thickness
    bx, by = _clamp_rect(spec, ctx, x - bo - bt, y - bo - bt, bw + 2 * (bo + bt), bh + 2 * (bo + bt))
    bx, by = bx + bo + bt, by + bo + bt
    tail = spec.get("tail")
    x0, y0, x1, y1 = bx - bo - bt, by - bo - bt, bx + bw + bo + bt, by + bh + bo + bt
    if tail:
        x0, y0 = min(x0, tail[0] - 20 * k), min(y0, tail[1] - 20 * k)
        x1, y1 = max(x1, tail[0] + 20 * k), max(y1, tail[1] + 20 * k)
    pad_glow = 0.4 * size
    sp = Sprite(x0 - pad_glow, y0 - pad_glow, x1 + pad_glow, y1 + pad_glow)
    sp.body = (bx - bo - bt, by - bo - bt, bx + bw + bo + bt, by + bh + bo + bt)
    sp.target = tuple(tail) if tail else None
    cyan = rgba(opt(spec, "accent", kind, "#62f3ff"))
    tcol = spec.get("color", DEFAULTS[kind]["color"])
    tcol = rgba("#f2fbff" if tcol == "white" else ("#62f3ff" if tcol == "cyan" else tcol))
    # box
    m = sp.mask()
    X0, Y0 = sp.p(bx, by)
    X1, Y1 = sp.p(bx + bw, by + bh)
    ImageDraw.Draw(m).rectangle([X0, Y0, X1, Y1], fill=255)
    sp.paint(rgba(opt(spec, "fill", kind)), m)
    if spec.get("scanlines", True):
        sm = sp.mask()
        d = ImageDraw.Draw(sm)
        step = 4 * k * SS
        yy = Y0 + step / 2
        while yy < Y1:
            d.line([(X0, yy), (X1, yy)], fill=255, width=max(1, int(SS * k)))
            yy += step
        sp.paint((255, 255, 255, 12), sm)
    om = sp.mask()
    ImageDraw.Draw(om).rectangle([X0, Y0, X1, Y1], outline=255, width=max(1, int(round(sw * SS))))
    sp.paint(rgba(opt(spec, "outline", kind)), om)
    # corner brackets + leader line, with a soft glow
    gm = sp.mask()
    d = ImageDraw.Draw(gm)
    t = bt * SS
    L = br * SS
    ex0, ey0 = sp.p(bx - bo - bt / 2, by - bo - bt / 2)
    ex1, ey1 = sp.p(bx + bw + bo + bt / 2, by + bh + bo + bt / 2)
    for (cxp, cyp, sx, sy) in ((ex0, ey0, 1, 1), (ex1, ey0, -1, 1), (ex0, ey1, 1, -1), (ex1, ey1, -1, -1)):
        d.line([(cxp + sx * L, cyp), (cxp, cyp), (cxp, cyp + sy * L)], fill=255,
               width=int(round(t)), joint="curve")
    if tail:
        _hud_leader(d, sp, bx, by, bw, bh, bo + bt, tail, size, k, spec)
    glow = gm.filter(ImageFilter.GaussianBlur(5 * k * SS))
    sp.paint((cyan[0], cyan[1], cyan[2], 150), glow)
    sp.paint(cyan, gm)
    # LIVE tag: red dot + LIVE
    ty = by + pady
    if live:
        lm = sp.mask()
        d = ImageDraw.Draw(lm)
        r = live_size * 0.31
        dcx, dcy = bx + padx + r, ty + live_size * 0.5
        X, Y = sp.p(dcx, dcy)
        d.ellipse([X - r * SS, Y - r * SS, X + r * SS, Y + r * SS], fill=255)
        lx, ly = sp.p(dcx + r + 0.45 * live_size, dcy)
        cap = -live_font.getbbox("H", anchor="ls")[1]
        d.text((lx, ly + cap / 2), "LIVE", font=live_font, fill=255, anchor="ls",
               stroke_width=int(round(0.02 * live_size * SS)), stroke_fill=255)
        red = rgba(spec.get("live_color", "#ff3044"))
        sp.paint((red[0], red[1], red[2], 140), lm.filter(ImageFilter.GaussianBlur(4 * k * SS)))
        sp.paint(red, lm)
        ty += live_h
    tm = sp.mask()
    align = spec.get("align", "left")
    draw_lines(tm, style, lines, cx=sp.p(bx + bw / 2, 0)[0], left=sp.p(bx + padx, 0)[0],
               top=sp.p(0, ty)[1], align=align)
    sp.paint((tcol[0], tcol[1], tcol[2], 110), tm.filter(ImageFilter.GaussianBlur(0.12 * size * SS)))
    sp.paint(tcol, tm)
    return sp


def _hud_leader(d, sp, bx, by, bw, bh, out, tail, size, k, spec):
    """Thin leader line from the box edge to a lock ring near the target."""
    tx, ty = tail
    cx, cy = bx + bw / 2, by + bh / 2
    # leave from the side facing the target
    if ty > by + bh:
        sx, sy = min(max(tx, bx + 0.25 * bw), bx + 0.75 * bw), by + bh + out
        knee = (sx, sy + 18 * k)
    elif ty < by:
        sx, sy = min(max(tx, bx + 0.25 * bw), bx + 0.75 * bw), by - out
        knee = (sx, sy - 18 * k)
    elif tx > cx:
        sx, sy = bx + bw + out, min(max(ty, by + 0.3 * bh), by + 0.7 * bh)
        knee = (sx + 18 * k, sy)
    else:
        sx, sy = bx - out, min(max(ty, by + 0.3 * bh), by + 0.7 * bh)
        knee = (sx - 18 * k, sy)
    ring = spec.get("ring", 13) * k
    dx, dy = tx - knee[0], ty - knee[1]
    dist = vlen(dx, dy)
    if dist < ring * 2:
        return
    end = (tx - dx / dist * ring, ty - dy / dist * ring)
    w = int(round(2.6 * k * SS))
    d.line(sp.pts([(sx, sy), knee, end]), fill=255, width=w, joint="curve")
    X, Y = sp.p(tx, ty)
    R = ring * SS
    d.ellipse([X - R, Y - R, X + R, Y + R], outline=255, width=w)
    r2 = 3.2 * k * SS
    d.ellipse([X - r2, Y - r2, X + r2, Y + r2], fill=255)


def render_endcard(spec, ctx):
    kind = "endcard"
    size = letter_size(spec, kind, ctx)
    style = make_style(spec, kind, ctx, size, lead=spec.get("lead", 1.32))
    box = spec.get("box")
    m = MARGIN * ctx.k
    if box:
        x, y, W = [float(v) for v in box[:3]]
    else:
        x, W, y = m, ctx.W - 2 * m, None
    padx, pady = spec.get("pad_x", 0.9) * size, spec.get("pad_y", 0.7) * size
    tokens = style.tokens(spec.get("text", ""))
    lines = wrap_balanced(tokens, (W - 2 * padx) * SS, style.space)
    tw = max((w for _, w in lines), default=0) / SS
    if tw + 2 * padx > W + 0.5:
        warn("%s/%s: a word is too long for a %d px end card; widened to %d px"
             % (ctx.page_id, spec.get("_id"), W, tw + 2 * padx))
        W = tw + 2 * padx
    rule = spec.get("rule", "#f5b700")
    rule_h = 4 * ctx.k if rule else 0
    bh = block_height(style, len(lines)) / SS + 2 * pady + rule_h
    if box and len(box) > 3:
        bh = max(bh, float(box[3]))
    if y is None:
        y = ctx.H - m - bh
    x, y = _clamp_rect(spec, ctx, x, y, W, bh)
    sp = Sprite(x, y, x + W, y + bh)
    sp.body = (x, y, x + W, y + bh)
    fm = sp.mask()
    X0, Y0 = sp.p(x, y)
    X1, Y1 = sp.p(x + W, y + bh)
    ImageDraw.Draw(fm).rectangle([X0, Y0, X1 - 1, Y1 - 1], fill=255)
    sp.paint(rgba(opt(spec, "fill", kind)), fm)
    if opt(spec, "outline", kind):
        om = sp.mask()
        ImageDraw.Draw(om).rectangle([X0, Y0, X1 - 1, Y1 - 1], outline=255,
                                     width=max(1, int(round(float(spec.get("outline_width", 2)) * ctx.k * SS))))
        sp.paint(rgba(spec["outline"]), om)
    if rule:
        rm = sp.mask()
        ImageDraw.Draw(rm).rectangle([X0, Y0, X1 - 1, Y0 + rule_h * SS], fill=255)
        sp.paint(rgba(rule), rm)
    tm = sp.mask()
    top = y + rule_h + pady
    draw_lines(tm, style, lines, cx=sp.p(x + W / 2, 0)[0], top=sp.p(0, top)[1])
    sp.paint(rgba(opt(spec, "color", kind)), tm)
    return sp


def render_display(spec, kind, ctx):
    """sfx and title: big outlined display lettering with extrusion or shadow."""
    k = ctx.k
    box = box_of(spec, ctx)
    x, y, W = box[:3]
    Hmax = float(box[3]) if len(box) > 3 else None
    text = str(spec.get("text", "")).replace("**", "")
    if opt(spec, "upper", kind, True):
        text = text.upper()
    lines = text.split("\n")
    fkey = opt(spec, "font", kind)
    size = spec.get("size")
    is_sfx = kind == "sfx"
    grow = float(spec.get("grow", 0.0))         # last letter is (1+grow) x the first
    bounce = float(spec.get("bounce", 0.05 if is_sfx else 0.0))
    ow_f = float(spec.get("outline_width", 0.075 if is_sfx else 0.06))
    ow2_f = float(spec.get("outline2_width", 0.05)) if spec.get("outline2") else 0.0
    lead = float(spec.get("lead", 0.98))
    fit_lines = spec.get("fit") == "lines"
    rnd = seeded(ctx.page_id, spec.get("_id"), text)

    def layout(sz_line):
        """Glyph placements for each line at the given sizes (SS px)."""
        rows = []
        for li, line in enumerate(lines):
            sz = sz_line[li]
            glyphs, xpos = [], 0.0
            n = max(1, len(line) - 1)
            for ci, ch in enumerate(line):
                gs = sz * (1 + grow * ci / n)
                f, _ = ctx.book.font(fkey, gs)
                fbase, _ = ctx.book.font(fkey, sz)
                if ci:
                    # advance with the base font's kerning, scaled by growth
                    pair = fbase.getlength(line[ci - 1:ci + 1]) - fbase.getlength(line[ci])
                    xpos += pair * (1 + grow * (ci - 1) / n)
                dy = 0.0
                if bounce and not ch.isspace():
                    dy = (1 if ci % 2 else -1) * bounce * sz * rnd.uniform(0.5, 1.0)
                glyphs.append((ch, f, xpos, dy, gs))
            last = glyphs[-1] if glyphs else None
            width = (last[2] + last[1].getlength(last[0])) if last else 0
            fb, _ = ctx.book.font(fkey, sz)
            cap = -fb.getbbox("H", anchor="ls")[1] * (1 + grow)
            rows.append((glyphs, width, cap, sz))
        return rows

    pad_f = ow_f + ow2_f
    if size is None:
        probe = 100.0 * SS
        rows = layout([probe] * len(lines))
        if fit_lines:
            sizes = []
            for (g, w, cap, sz) in rows:
                s = probe * (W * SS) / (w + 2 * pad_f * probe) if w else probe
                sizes.append(s)
            cap_ratio = float(spec.get("max_ratio", 1.45))
            smallest = min(sizes)
            sizes = [min(sz, smallest * cap_ratio) for sz in sizes]
        else:
            widest = max(w for (_, w, _, _) in rows) or 1
            s = probe * (W * SS) / (widest + 2 * pad_f * probe)
            sizes = [s] * len(lines)
        if Hmax:
            total = sum(sz * lead for sz in sizes) + 2 * pad_f * max(sizes)
            if total > Hmax * SS:
                f = Hmax * SS / total
                sizes = [sz * f for sz in sizes]
    else:
        sizes = [float(size) * SS] * len(lines)
    rows = layout(sizes)
    big = max(sizes)
    ow = ow_f * big
    ow2 = ow2_f * big
    ext = float(spec.get("extrude", 0.07 if is_sfx else 0.0)) * big
    shadow = spec.get("shadow", None if is_sfx else True)
    if shadow is True:
        shadow = [0.045, 0.06]
    sh = (shadow[0] * big, shadow[1] * big) if shadow else (0.0, 0.0)
    shadow_blur = float(spec.get("shadow_blur", 0.02)) * big

    # block geometry (SS px, local)
    block_h = 0.0
    row_tops = []
    for (glyphs, w, cap, sz) in rows:
        row_tops.append(block_h)
        block_h += sz * lead
    block_h = block_h - rows[-1][3] * lead + rows[-1][2]
    block_w = max(w for (_, w, _, _) in rows)
    margin = ow + ow2 + ext + max(abs(sh[0]), abs(sh[1])) + shadow_blur * 3 + bounce * big + 8
    LW = int(block_w + 2 * margin)
    LH = int(block_h + 2 * margin)
    fill_m = Image.new("L", (LW, LH), 0)
    out_m = Image.new("L", (LW, LH), 0)
    out2_m = Image.new("L", (LW, LH), 0) if ow2 else None
    df, do = ImageDraw.Draw(fill_m), ImageDraw.Draw(out_m)
    do2 = ImageDraw.Draw(out2_m) if out2_m else None
    align = spec.get("align", "center")
    for (glyphs, w, cap, sz), top in zip(rows, row_tops):
        if align == "left":
            x0 = margin
        elif align == "right":
            x0 = margin + block_w - w
        else:
            x0 = margin + (block_w - w) / 2
        base = margin + top + cap
        for ch, f, gx, dy, gs in glyphs:
            if ch.isspace():
                continue
            pos = (x0 + gx, base + dy)
            if do2:
                do2.text(pos, ch, font=f, fill=255, anchor="ls",
                         stroke_width=int(round(ow + ow2)), stroke_fill=255)
            do.text(pos, ch, font=f, fill=255, anchor="ls",
                    stroke_width=int(round(ow)), stroke_fill=255)
            df.text(pos, ch, font=f, fill=255, anchor="ls")
    layer = Image.new("RGBA", (LW, LH), (0, 0, 0, 0))

    def put(color, mask, off=(0, 0)):
        if color is None:
            return
        c = rgba(color)
        if c[3] < 255:
            mask = mask.point(lambda v: v * c[3] // 255)
        lay = Image.new("RGBA", (LW, LH), c[:3] + (0,))
        lay.putalpha(mask)
        if off != (0, 0):
            moved = Image.new("RGBA", (LW, LH), c[:3] + (0,))
            moved.paste(lay, (int(round(off[0])), int(round(off[1]))))
            lay = moved
        layer.alpha_composite(lay)

    outer = out2_m if out2_m else out_m
    if shadow:
        sm = outer.filter(ImageFilter.GaussianBlur(shadow_blur)) if shadow_blur > 0.5 else outer
        put(spec.get("shadow_color", "#000000c8"), sm, sh)
    if ext > 0:
        ang = math.radians(float(spec.get("extrude_angle", 60)))
        ux, uy = math.cos(ang), math.sin(ang)
        em = Image.new("L", (LW, LH), 0)
        steps = max(1, int(ext / 2))
        for i in range(1, steps + 1):
            d = ext * i / steps
            moved = Image.new("L", (LW, LH), 0)
            moved.paste(outer, (int(round(ux * d)), int(round(uy * d))))
            em = ImageChops.lighter(em, moved)
        put(spec.get("extrude_color", spec.get("outline", DEFAULTS[kind]["outline"])), em)
    if out2_m:
        put(spec.get("outline2"), out2_m)
    put(opt(spec, "outline", kind), out_m)
    user_fill = spec.get("fill", spec.get("color"))
    c1 = rgba(user_fill, DEFAULTS[kind]["fill"])
    c2 = rgba(spec.get("fill2", DEFAULTS[kind]["fill2"] if user_fill is None else None))
    if c2 and c2 != c1:
        grad = Image.new("RGBA", (LW, LH))
        gd = ImageDraw.Draw(grad)
        bands = [(int(margin + top - bounce * big), int(margin + top + cap + bounce * big))
                 for (glyphs, w, cap, sz), top in zip(rows, row_tops)]
        for yy in range(LH):
            # glyph parts above or below a row's cap band (Bangers ascenders, descenders)
            # keep that row's end colour; between rows the split is halfway
            for k, (y0, y1) in enumerate(bands):
                nxt = bands[k + 1][0] if k + 1 < len(bands) else None
                if yy <= y1 or nxt is None or yy < (y1 + nxt) / 2:
                    t = min(1.0, max(0.0, (yy - y0) / max(1, y1 - y0)))
                    break
            gd.line([(0, yy), (LW, yy)], fill=tuple(int(lerp(c1[i], c2[i], t)) for i in range(4)))
        grad.putalpha(fill_m)
        layer.alpha_composite(grad)
    else:
        put(c1, fill_m)
    angle = float(opt(spec, "angle", kind, 0) or 0)
    if angle:
        layer = layer.rotate(angle, resample=Image.BICUBIC, expand=True)
    # downsample to canvas scale, keeping the centre where the box says
    small_w = max(1, int(round(layer.width / SS)))
    small_h = max(1, int(round(layer.height / SS)))
    small = layer.resize((small_w, small_h), Image.LANCZOS)
    cx = x + W / 2
    cy = y + (block_h + 2 * margin) / SS / 2 - margin / SS
    px, py = cx - small_w / 2, cy - small_h / 2
    bb = small.getbbox()
    if bb and not spec.get("bleed"):
        inset = 4 * k
        dx = min(0.0, ctx.W - inset - (px + bb[2])) + max(0.0, inset - (px + bb[0]))
        dy = min(0.0, ctx.H - inset - (py + bb[3])) + max(0.0, inset - (py + bb[1]))
        if dx or dy:
            warn("%s/%s: %s ran off the canvas; moved by (%d, %d)"
                 % (ctx.page_id, spec.get("_id"), kind, dx, dy))
            px, py = px + dx, py + dy
    sp = Sprite.__new__(Sprite)
    sp.x0, sp.y0 = int(round(px)), int(round(py))
    sp.w, sp.h = small_w, small_h
    sp.img = small
    sp.body = (sp.x0 + bb[0], sp.y0 + bb[1], sp.x0 + bb[2], sp.y0 + bb[3]) if bb else None
    sp.target = None
    sp.finish = lambda: small
    return sp


def render_letter(spec, ctx):
    kind = spec.get("type", "balloon")
    if kind not in LETTER_TYPES:
        raise SystemExit("%s/%s: unknown letter type %r" % (ctx.page_id, spec.get("_id"), kind))
    if kind in ("balloon", "shout", "whisper", "thought"):
        return render_balloon(spec, kind, ctx)
    if kind == "caption":
        return render_caption(spec, ctx)
    if kind == "hud":
        return render_hud(spec, ctx)
    if kind == "endcard":
        return render_endcard(spec, ctx)
    return render_display(spec, kind, ctx)


# --------------------------------------------------------------------------
# Panels
# --------------------------------------------------------------------------

_IMG_CACHE = {}
_SRGB = None


def srgb_profile_bytes():
    global _SRGB
    if _SRGB is None and ImageCms is not None:
        try:
            _SRGB = ImageCms.ImageCmsProfile(ImageCms.createProfile("sRGB")).tobytes()
        except Exception:
            _SRGB = b""
    return _SRGB or None


def load_image(path):
    key = str(path)
    if key in _IMG_CACHE:
        return _IMG_CACHE[key]
    im = Image.open(path)
    im.load()
    icc = im.info.get("icc_profile")
    if icc and ImageCms is not None:
        try:
            import io
            src = ImageCms.ImageCmsProfile(io.BytesIO(icc))
            dst = ImageCms.createProfile("sRGB")
            if im.mode not in ("RGB", "RGBA"):
                im = im.convert("RGBA" if "A" in im.mode else "RGB")
            im = ImageCms.profileToProfile(im, src, dst, outputMode=im.mode)
        except Exception as e:  # keep going with the raw pixels
            warn("could not convert %s to sRGB (%s)" % (path, e))
    if im.mode in ("RGBA", "LA", "PA") or (im.mode == "P" and "transparency" in im.info):
        im = im.convert("RGBA")
        bg = Image.new("RGBA", im.size, (0, 0, 0, 255))
        bg.alpha_composite(im)
        im = bg.convert("RGB")
    elif im.mode != "RGB":
        im = im.convert("RGB")
    _IMG_CACHE[key] = im
    return im


def cover_fit(im, tw, th, focus=(0.5, 0.5), zoom=1.0):
    iw, ih = im.size
    scale = max(tw / iw, th / ih) * max(1.0, float(zoom))
    cw, ch = tw / scale, th / scale
    fx, fy = focus[0] * iw, focus[1] * ih
    left = min(max(fx - cw / 2, 0), iw - cw)
    top = min(max(fy - ch / 2, 0), ih - ch)
    return im.resize((tw, th), Image.LANCZOS, box=(left, top, left + cw, top + ch),
                     reducing_gap=3.0)


def placeholder(tw, th, label, sub, book, k):
    im = Image.new("RGB", (tw, th), (128, 132, 140))
    d = ImageDraw.Draw(im)
    step = int(36 * k) or 1
    for xx in range(-th, tw, step):
        d.line([(xx, th), (xx + th, 0)], fill=(120, 124, 132), width=max(1, int(10 * k)))
    d.line([(0, 0), (tw, th)], fill=(150, 154, 162), width=max(1, int(3 * k)))
    d.line([(0, th), (tw, 0)], fill=(150, 154, 162), width=max(1, int(3 * k)))
    f1, _ = book.font("anton", max(18, min(64 * k, th / 5)))
    f2, _ = book.font("barlow", max(14, min(26 * k, th / 9)))
    d.rectangle([tw / 2 - tw * 0.4, th / 2 - th * 0.17, tw / 2 + tw * 0.4, th / 2 + th * 0.17],
                fill=(96, 100, 108))
    d.text((tw / 2, th / 2 - 4 * k), label, font=f1, fill=(240, 240, 244), anchor="md")
    d.text((tw / 2, th / 2 + 10 * k), sub, font=f2, fill=(220, 222, 228), anchor="ma")
    return im


def panel_shape(panel, ctx):
    if "poly" in panel:
        pts = [(float(a), float(b)) for a, b in panel["poly"]]
    else:
        x, y, w, h = [float(v) for v in panel["rect"]]
        pts = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    bbox = (int(round(min(xs))), int(round(min(ys))), int(round(max(xs))), int(round(max(ys))))
    return pts, bbox


def draw_panel(page, panel, root, ctx):
    pts, (x0, y0, x1, y1) = panel_shape(panel, ctx)
    tw, th = max(1, x1 - x0), max(1, y1 - y0)
    src = panel.get("image")
    tile = None
    if src:
        p = Path(src)
        if not p.is_absolute():
            p = Path(root) / p
        if p.exists():
            tile = cover_fit(load_image(p), tw, th, panel.get("focus", (0.5, 0.5)),
                             panel.get("zoom", 1.0))
        else:
            warn("%s/%s: image %s not found; placeholder drawn" % (ctx.page_id, panel.get("id"), src))
    if tile is None:
        tile = placeholder(tw, th, panel.get("id", "panel"),
                           "%s  |  %dx%d" % (Path(src).name if src else "no image", tw, th),
                           ctx.book, ctx.k)
    border = float(panel.get("border", 6)) * 1.0
    bcol = rgba(panel.get("border_color", "#000000"))
    if "poly" not in panel:
        page.paste(tile, (x0, y0))
        if border > 0:
            d = ImageDraw.Draw(page)
            b = int(round(border))
            d.rectangle([x0, y0, x1 - 1, y1 - 1], outline=bcol[:3], width=b)
        return
    # polygon panel: antialiased mask and an inside border
    big = Image.new("L", (tw * SS, th * SS), 0)
    lp = [((px - x0) * SS, (py - y0) * SS) for px, py in pts]
    ImageDraw.Draw(big).polygon(lp, fill=255)
    mask = big.reduce(SS)
    page.paste(tile, (x0, y0), mask)
    if border > 0:
        bm = Image.new("L", (tw * SS, th * SS), 0)
        ImageDraw.Draw(bm).line(lp + lp[:2], fill=255, width=int(round(2 * border * SS)), joint="curve")
        bm = ImageChops.multiply(bm, big).reduce(SS)
        page.paste(Image.new("RGB", (tw, th), bcol[:3]), (x0, y0), bm)


def panel_mask(panel, ctx):
    pts, _ = panel_shape(panel, ctx)
    m = Image.new("L", (ctx.W, ctx.H), 0)
    ImageDraw.Draw(m).polygon(pts, fill=255)
    return m


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------

def check_layout(page, ctx):
    pid = ctx.page_id
    m = MARGIN * ctx.k
    shapes = []
    for p in page.get("panels", []):
        if "rect" not in p and "poly" not in p:
            raise SystemExit("%s/%s: panel needs \"rect\" or \"poly\"" % (pid, p.get("id")))
        pts, bb = panel_shape(p, ctx)
        shapes.append((p, bb))
        if p.get("bleed"):
            continue
        if bb[0] < m - 0.5 or bb[1] < m - 0.5 or bb[2] > ctx.W - m + 0.5 or bb[3] > ctx.H - m + 0.5:
            warn("%s/%s: panel crosses the %d px outer margin (add \"bleed\": true if meant)"
                 % (pid, p.get("id"), MARGIN))
    lo, hi = GUTTER[0] * ctx.k, GUTTER[1] * ctx.k
    for i in range(len(shapes)):
        for j in range(i + 1, len(shapes)):
            (pa, a), (pb, b) = shapes[i], shapes[j]
            if pa.get("bleed") or pb.get("bleed") or "poly" in pa or "poly" in pb:
                continue
            if rects_overlap(a, b):
                warn("%s: panels %s and %s overlap" % (pid, pa.get("id"), pb.get("id")))
                continue
            xo = min(a[2], b[2]) - max(a[0], b[0])
            yo = min(a[3], b[3]) - max(a[1], b[1])
            gap = None
            if xo > 0:
                gap = max(b[1] - a[3], a[1] - b[3])
            elif yo > 0:
                gap = max(b[0] - a[2], a[0] - b[2])
            if gap is not None and gap < 3 * hi and not (lo - 0.5 <= gap <= hi + 0.5):
                warn("%s: gutter between %s and %s is %d px (want %d-%d)"
                     % (pid, pa.get("id"), pb.get("id"), gap, GUTTER[0], GUTTER[1]))


def check_letters(page, sprites, ctx):
    pid = ctx.page_id
    avoid = [tuple(r) for r in page.get("avoid", [])]
    for p in page.get("panels", []):
        avoid += [tuple(r) for r in p.get("faces", [])]
    bodies = []
    m = MARGIN * ctx.k
    for spec, sp in sprites:
        if sp.body is None:
            continue
        x0, y0, x1, y1 = sp.body
        if not spec.get("bleed") and (x0 < m - 0.5 or y0 < m - 0.5 or x1 > ctx.W - m + 0.5
                                      or y1 > ctx.H - m + 0.5):
            warn("%s/%s: %s crosses the %d px outer margin (add \"bleed\": true if meant)"
                 % (pid, spec.get("_id"), spec.get("type"), MARGIN))
        for r in avoid:
            fx, fy, fw, fh = r
            if rects_overlap((x0, y0, x1, y1), (fx, fy, fx + fw, fy + fh)):
                warn("%s/%s: %s covers a face/avoid box %s" % (pid, spec.get("_id"), spec.get("type"), list(r)))
        if spec.get("type") in ("balloon", "shout", "whisper", "thought", "caption", "hud"):
            for other_spec, ob in bodies:
                if rects_overlap(sp.body, ob):
                    warn("%s: %s and %s overlap" % (pid, other_spec.get("_id"), spec.get("_id")))
            bodies.append((spec, sp.body))
        tip = spec.get("_tip")
        if tip:
            for r in avoid:
                fx, fy, fw, fh = r
                if fx < tip[0] < fx + fw and fy < tip[1] < fy + fh:
                    warn("%s/%s: tail tip %s ends inside face/avoid box %s; raise tail_gap"
                         % (pid, spec.get("_id"), [round(v) for v in tip], list(r)))
        t = sp.target
        if t and not (0 <= t[0] <= ctx.W and 0 <= t[1] <= ctx.H):
            warn("%s/%s: tail target %s is off the canvas" % (pid, spec.get("_id"), list(t)))


# --------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------

def render_page(page, spec, root, book, guides=False):
    W, H = [int(v) for v in spec.get("canvas", [1080, 1350])]
    ctx = Ctx(book, W, H, page.get("id", "page"))
    bg = rgba(page.get("background", spec.get("background", "#0d0d10")))
    img = Image.new("RGB", (W, H), bg[:3])
    check_layout(page, ctx)
    panels = {}
    for panel in page.get("panels", []):
        draw_panel(img, panel, root, ctx)
        panels[panel.get("id")] = panel
    img = img.convert("RGBA")
    sprites = []
    for i, letter in enumerate(page.get("letters", [])):
        letter = dict(letter)
        letter.setdefault("_id", letter.get("id", "%s#%d" % (letter.get("type", "balloon"), i + 1)))
        ref = letter.get("panel")
        if ref is not None and ref not in panels:
            warn("%s/%s: panel %r does not exist" % (ctx.page_id, letter["_id"], ref))
        sp = render_letter(letter, ctx)
        tile = sp.finish()
        if letter.get("clip") and ref in panels:
            m = panel_mask(panels[ref], ctx).crop((sp.x0, sp.y0, sp.x0 + tile.width, sp.y0 + tile.height))
            tile.putalpha(ImageChops.multiply(tile.getchannel("A"), m))
        layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
        layer.paste(tile, (sp.x0, sp.y0))
        img = Image.alpha_composite(img, layer)
        sprites.append((letter, sp))
    check_letters(page, sprites, ctx)
    out = img.convert("RGB")
    guide = draw_guides(out, page, sprites, ctx) if guides else None
    return out, guide


def draw_guides(img, page, sprites, ctx):
    g = img.convert("RGBA")
    ov = Image.new("RGBA", g.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    m = MARGIN * ctx.k
    d.rectangle([m, m, ctx.W - m, ctx.H - m], outline=(80, 255, 120, 220), width=2)
    crop = (ctx.W - ctx.H * 3 / 4) / 2           # Instagram 3:4 profile-grid crop
    if crop > 0:
        for xx in (crop, ctx.W - crop):
            for yy in range(0, ctx.H, 24):
                d.line([(xx, yy), (xx, yy + 12)], fill=(255, 60, 220, 230), width=2)
    f, _ = ctx.book.font("barlow", 22 * ctx.k)
    for p in page.get("panels", []):
        pts, bb = panel_shape(p, ctx)
        d.polygon(pts, outline=(255, 210, 0, 220))
        d.text((bb[0] + 10, bb[1] + 8), "%s %dx%d" % (p.get("id"), bb[2] - bb[0], bb[3] - bb[1]),
               font=f, fill=(255, 210, 0, 255), stroke_width=2, stroke_fill=(0, 0, 0, 255))
        for r in p.get("faces", []):
            d.rectangle([r[0], r[1], r[0] + r[2], r[1] + r[3]], fill=(255, 0, 0, 50),
                        outline=(255, 40, 40, 230), width=2)
    for r in page.get("avoid", []):
        d.rectangle([r[0], r[1], r[0] + r[2], r[1] + r[3]], fill=(255, 0, 0, 50),
                    outline=(255, 40, 40, 230), width=2)
    for spec, sp in sprites:
        if sp.body:
            d.rectangle(sp.body, outline=(0, 230, 255, 200), width=1)
            d.text((sp.body[0] + 4, sp.body[1] - 24 * ctx.k), str(spec.get("_id")), font=f,
                   fill=(0, 230, 255, 255), stroke_width=2, stroke_fill=(0, 0, 0, 255))
        if sp.target:
            tx, ty = sp.target
            d.line([(tx - 12, ty), (tx + 12, ty)], fill=(255, 40, 40, 255), width=2)
            d.line([(tx, ty - 12), (tx, ty + 12)], fill=(255, 40, 40, 255), width=2)
    return Image.alpha_composite(g, ov).convert("RGB")


def save(img, path, jpg=False):
    icc = srgb_profile_bytes()
    kw = {"icc_profile": icc} if icc else {}
    img.save(path, "PNG", optimize=False, compress_level=6, **kw)
    if jpg:
        img.save(path.with_suffix(".jpg"), "JPEG", quality=92, subsampling=0,
                 optimize=True, **kw)


def contact_sheet(paths, out):
    ims = [Image.open(p) for p in paths]
    if not ims:
        return
    tw = 360
    th = int(ims[0].height * tw / ims[0].width)
    cols = min(5, len(ims))
    rows = (len(ims) + cols - 1) // cols
    gap = 16
    sheet = Image.new("RGB", (cols * tw + (cols + 1) * gap, rows * th + (rows + 1) * gap), (40, 40, 46))
    for i, im in enumerate(ims):
        r, c = divmod(i, cols)
        sheet.paste(im.convert("RGB").resize((tw, th), Image.LANCZOS),
                    (gap + c * (tw + gap), gap + r * (th + gap)))
    sheet.save(out, quality=88)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Letter and assemble BBG News comic pages.")
    ap.add_argument("pages", help="pages JSON file")
    ap.add_argument("--out", required=True, help="output directory")
    ap.add_argument("--root", help="directory that panel image paths are relative to "
                                   "(default: the JSON file's directory)")
    ap.add_argument("--jpg", action="store_true", help="also write JPG at quality 92")
    ap.add_argument("--only", help="comma-separated page ids to render")
    ap.add_argument("--guides", action="store_true",
                    help="also write guides/<id>.png with margins, crops, boxes and tail targets")
    ap.add_argument("--sheet", action="store_true", help="also write a contact sheet of all pages")
    ap.add_argument("--strict", action="store_true", help="exit with status 2 on any warning")
    ap.add_argument("--fonts", help="font directory (default: repo assets/fonts)")
    args = ap.parse_args(argv)

    src = Path(args.pages)
    spec = json.loads(src.read_text(encoding="utf-8"))
    root = Path(args.root) if args.root else src.resolve().parent
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    book = FontBook(args.fonts or FONT_DIR, root)
    W, H = [int(v) for v in spec.get("canvas", [1080, 1350])]
    pages = spec.get("pages", [])
    if len(pages) > MAX_SLIDES:
        warn("%d pages: an Instagram carousel holds at most %d slides" % (len(pages), MAX_SLIDES))
    only = set(args.only.split(",")) if args.only else None
    ids = [p.get("id") for p in pages]
    if len(set(ids)) != len(ids):
        warn("page ids are not unique: %s" % ids)
    written = []
    for page in pages:
        pid = page.get("id", "page")
        if only and pid not in only:
            continue
        print("page %s" % pid)
        img, guide = render_page(page, spec, root, book, guides=args.guides)
        assert img.size == (W, H)
        path = out / ("%s.png" % pid)
        save(img, path, args.jpg)
        written.append(path)
        if guide is not None:
            (out / "guides").mkdir(exist_ok=True)
            guide.save(out / "guides" / ("%s.png" % pid))
    if args.sheet and written:
        contact_sheet(written, out / "contact_sheet.jpg")
    print("wrote %d page(s) to %s%s" % (len(written), out,
                                        " (%d warning(s))" % len(WARNINGS) if WARNINGS else ""))
    if args.strict and WARNINGS:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
