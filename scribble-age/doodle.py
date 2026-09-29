"""Scribble Age drawing kit: hand-drawn-looking SVG pieces in the channel's house style.

Every function returns an SVG fragment (a string). Compose them into a scene with scene():

    from doodle import *
    svg = scene(sky("day"), sun(1600, 180), hills(700), ground(800, "grass"),
                hut(400, 800), person(900, 820, expression="shocked", pose="arms_up"),
                mascot(1400, 820, expression="happy", pose="point"),
                banner("FRANCE, 5000 BC"))

Coordinates are on a 1920x1080 canvas; (x, y) for figures and buildings is the point where
they touch the ground. Lines wobble slightly (seeded), so drawings feel hand-made but render
the same way every time.
"""
import math
import os
import random
import shutil
import subprocess

# Make Patrick Hand available to cairosvg for review renders, not just for make_video.py.
_font = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "PatrickHand-Regular.ttf")
_dst = os.path.expanduser("~/.fonts/PatrickHand-Regular.ttf")
if os.path.exists(_font) and not os.path.exists(_dst):
    os.makedirs(os.path.dirname(_dst), exist_ok=True)
    shutil.copy(_font, _dst)
    subprocess.run(["fc-cache", "-f"], capture_output=True)

INK = "#111"
CREAM = "#FFF8EC"
AMBER = "#F6A21E"
SKIN = "#FFD9B0"
SKIN_SHADE = "#F2BE8E"
W, H = 1920, 1080

SKINS = ["#FFD9B0", "#E8B58A", "#C98E5E", "#9A6440", "#6E4529"]
HAIR = {"black": "#1E1A18", "brown": "#5A3A22", "blond": "#E8C45A", "red": "#B5482A", "grey": "#B8B4AE", "white": "#F2F0EA"}

_rng = random.Random(7)


def seed(n):
    """Reset the wobble generator (call once per scene for repeatable drawings)."""
    _rng.seed(n)


def _j(amount):
    return _rng.uniform(-amount, amount)


def _f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


def _smooth(points, closed=False):
    """Catmull-Rom spline through points -> SVG path data."""
    pts = list(points)
    if closed:
        pts = [pts[-1]] + pts + [pts[0], pts[1]]
    else:
        pts = [pts[0]] + pts + [pts[-1]]
    d = f"M{_f(pts[1][0])},{_f(pts[1][1])}"
    for i in range(1, len(pts) - 2):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[i + 1], pts[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C{_f(c1[0])},{_f(c1[1])} {_f(c2[0])},{_f(c2[1])} {_f(p2[0])},{_f(p2[1])}"
    return d + (" Z" if closed else "")


def _style(fill="none", stroke=INK, width=8, extra=""):
    return (f'fill="{fill}" stroke="{stroke}" stroke-width="{_f(width)}" '
            f'stroke-linecap="round" stroke-linejoin="round"{(" " + extra) if extra else ""}')


# ---------- primitives with a hand-drawn wobble ----------

def blob(cx, cy, rx, ry, fill="none", stroke=INK, width=8, wobble=0.035, n=14, rot=0):
    """Wobbly ellipse."""
    pts = []
    for i in range(n):
        a = 2 * math.pi * i / n + rot
        k = 1 + _j(wobble)
        pts.append((cx + rx * k * math.cos(a), cy + ry * k * math.sin(a)))
    return f'<path d="{_smooth(pts, True)}" {_style(fill, stroke, width)}/>'


def line(points, stroke=INK, width=8, wobble=2.5, fill="none"):
    """Wobbly line through points (list of (x, y)); a hand-drawn stroke."""
    pts = []
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        steps = max(1, int(math.hypot(x1 - x0, y1 - y0) / 90))
        for s in range(steps):
            t = s / steps
            jit = _j(wobble) if 0 < s else 0
            pts.append((x0 + (x1 - x0) * t + jit, y0 + (y1 - y0) * t + jit))
    pts.append(points[-1])
    return f'<path d="{_smooth(pts)}" {_style(fill, stroke, width)}/>'


def poly(points, fill="none", stroke=INK, width=8, wobble=2.0):
    """Wobbly closed polygon with straight-ish sides."""
    pts = []
    for (x0, y0), (x1, y1) in zip(points, points[1:] + points[:1]):
        pts.append((x0 + _j(wobble), y0 + _j(wobble)))
        steps = max(1, int(math.hypot(x1 - x0, y1 - y0) / 120))
        for s in range(1, steps):
            t = s / steps
            pts.append((x0 + (x1 - x0) * t + _j(wobble), y0 + (y1 - y0) * t + _j(wobble)))
    d = "M" + " L".join(f"{_f(x)},{_f(y)}" for x, y in pts) + " Z"
    return f'<path d="{d}" {_style(fill, stroke, width)}/>'


def rect(x, y, w, h, fill="none", stroke=INK, width=8, wobble=2.0):
    return poly([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], fill, stroke, width, wobble)


def group(*parts, transform=""):
    t = f' transform="{transform}"' if transform else ""
    return f"<g{t}>" + "".join(parts) + "</g>"


def shadow(x, y, w, alpha=0.18):
    return f'<ellipse cx="{_f(x)}" cy="{_f(y)}" rx="{_f(w / 2)}" ry="{_f(w / 9)}" fill="#000" opacity="{alpha}"/>'


# ---------- text ----------

def text(x, y, s, size=90, fill=INK, anchor="middle", outline=None, outline_width=14, rotate=0):
    """Patrick Hand text. outline="#fff" (or any color) draws a thick outline behind the fill
    (two layers, because cairosvg ignores paint-order)."""
    s = s.replace("&", "&amp;").replace("<", "&lt;")
    rot = f' transform="rotate({rotate} {_f(x)} {_f(y)})"' if rotate else ""
    base = f'x="{_f(x)}" y="{_f(y)}" font-family="Patrick Hand" font-size="{size}" text-anchor="{anchor}"{rot}'
    out = ""
    if outline:
        out += (f'<text {base} fill="{outline}" stroke="{outline}" stroke-width="{outline_width}" '
                f'stroke-linejoin="round">{s}</text>')
    return out + f'<text {base} fill="{fill}">{s}</text>'


def banner(s, x=60, y=60, size=64, fill=AMBER):
    """Place/date tag in the top-left corner, like a taped-on paper label."""
    w = len(s) * size * 0.52 + 70
    return group(poly([(x, y), (x + w, y + 6), (x + w - 8, y + size + 34), (x + 4, y + size + 28)],
                      fill=fill, width=7),
                 text(x + w / 2, y + size + 6, s, size=size))


def big_number(s, x=960, y=460, size=260, fill=INK, outline="#fff"):
    return text(x, y, s, size=size, fill=fill, outline=outline, outline_width=22)


def label(x, y, s, size=64, fill=INK, bg="#fff"):
    """Boxed label with a slight tilt."""
    w = len(s) * size * 0.5 + 50
    return group(rect(x - w / 2, y - size * 0.95, w, size * 1.35, fill=bg, width=6),
                 text(x, y + size * 0.12, s, size=size, fill=fill),
                 transform=f"rotate({_f(_j(2.5))} {_f(x)} {_f(y)})")


def speech(x, y, s, size=58, w=None, tail="left", fill="#fff"):
    """Speech bubble centered at (x, y); tail points down-left or down-right toward the speaker."""
    lines = s.split("\n")
    w = w or max(len(t) for t in lines) * size * 0.5 + 80
    h = len(lines) * size * 1.15 + 50
    tx = x - w * 0.25 if tail == "left" else x + w * 0.25
    out = blob(x, y, w / 2, h / 2, fill=fill, width=7, wobble=0.02)
    out += poly([(tx - 25, y + h / 2 - 12), (tx + 25, y + h / 2 - 12),
                 (tx + (-60 if tail == "left" else 60), y + h / 2 + 70)], fill=fill, width=7)
    out += f'<rect x="{_f(tx - 22)}" y="{_f(y + h / 2 - 30)}" width="44" height="22" fill="{fill}"/>'
    for i, t in enumerate(lines):
        out += text(x, y - h / 2 + 25 + size * (i + 0.95) * 1.1, t, size=size)
    return out


def arrow(x1, y1, x2, y2, stroke=INK, width=10, bend=0.2):
    mx, my = (x1 + x2) / 2 - (y2 - y1) * bend, (y1 + y2) / 2 + (x2 - x1) * bend
    a = math.atan2(y2 - my, x2 - mx)
    head = [(x2 - 45 * math.cos(a - 0.5), y2 - 45 * math.sin(a - 0.5)), (x2, y2),
            (x2 - 45 * math.cos(a + 0.5), y2 - 45 * math.sin(a + 0.5))]
    return line([(x1, y1), (mx, my), (x2, y2)], stroke, width, 1) + line(head, stroke, width, 0.5)


# ---------- effects ----------

def motion_lines(x, y, length=120, n=3, direction=-1, gap=34):
    return "".join(line([(x, y + i * gap), (x + direction * length, y + i * gap + _j(6))], width=6, wobble=1)
                   for i in range(n))


def shock_marks(x, y, s=1.0):
    out = ""
    for a in (-60, -30, 0, 30, 60):
        r = math.radians(a - 90)
        out += line([(x + 70 * s * math.cos(r), y + 70 * s * math.sin(r)),
                     (x + 115 * s * math.cos(r), y + 115 * s * math.sin(r))], width=7, wobble=0.5)
    return out


def sweat(x, y, s=1.0):
    return f'<path d="M{_f(x)},{_f(y)} q{_f(-18*s)},{_f(34*s)} 0,{_f(44*s)} q{_f(18*s)},{_f(-10*s)} 0,{_f(-44*s)} z" {_style("#8ED0F0", INK, 5)}/>'


def sparkle(x, y, s=1.0, fill=AMBER):
    p = [(x, y - 40 * s), (x + 10 * s, y - 10 * s), (x + 40 * s, y), (x + 10 * s, y + 10 * s), (x, y + 40 * s),
         (x - 10 * s, y + 10 * s), (x - 40 * s, y), (x - 10 * s, y - 10 * s)]
    return poly(p, fill=fill, width=5, wobble=0.5)


def question(x, y, size=140):
    return text(x, y, "?", size=size, fill=AMBER, outline=INK, outline_width=10, rotate=_j(12))


def exclaim(x, y, size=150):
    return text(x, y, "!", size=size, fill="#E4572E", outline=INK, outline_width=10, rotate=_j(10))


def fire(x, y, s=1.0):
    outer = [(x - 70 * s, y), (x - 80 * s, y - 70 * s), (x - 40 * s, y - 120 * s), (x - 30 * s, y - 70 * s),
             (x, y - 170 * s), (x + 30 * s, y - 90 * s), (x + 55 * s, y - 130 * s), (x + 80 * s, y - 60 * s),
             (x + 70 * s, y)]
    inner = [(x - 35 * s, y), (x - 30 * s, y - 50 * s), (x, y - 100 * s), (x + 30 * s, y - 50 * s), (x + 35 * s, y)]
    logs = line([(x - 90 * s, y + 10 * s), (x + 90 * s, y - 10 * s)], "#6B3E1F", 22 * s, 1) + \
        line([(x - 90 * s, y - 10 * s), (x + 90 * s, y + 10 * s)], "#7A4A26", 22 * s, 1)
    return logs + f'<path d="{_smooth(outer, True)}" {_style("#E4572E", INK, 7)}/>' + \
        f'<path d="{_smooth(inner, True)}" {_style("#FFC83D", "none", 0)}/>'


# ---------- sky and land ----------

SKY = {"day": "#CFEAF5", "dusk": "#F7C59F", "night": "#27324A", "storm": "#9AA5AE", "paper": CREAM}


def sky(kind="day", horizon=H):
    return f'<rect x="0" y="0" width="{W}" height="{horizon}" fill="{SKY.get(kind, kind)}"/>' + (
        "".join(f'<circle cx="{_rng.randint(20, W - 20)}" cy="{_rng.randint(20, 600)}" r="{_rng.choice([3, 4, 5])}" fill="#FFF6D8"/>'
                for _ in range(60)) if kind == "night" else "")


def sun(x, y, r=90, fill="#FFD23F"):
    rays = "".join(line([(x + (r + 25) * math.cos(a), y + (r + 25) * math.sin(a)),
                         (x + (r + 65) * math.cos(a), y + (r + 65) * math.sin(a))], width=7, wobble=0.5)
                   for a in [i * math.pi / 6 for i in range(12)])
    return rays + blob(x, y, r, r, fill=fill, width=8, wobble=0.02)


def moon(x, y, r=80):
    return blob(x, y, r, r, fill="#FFF3C4", width=7, wobble=0.02) + \
        f'<circle cx="{_f(x + r * 0.35)}" cy="{_f(y - r * 0.2)}" r="{_f(r * 0.18)}" fill="#E9DDA8"/>'


def cloud(x, y, s=1.0, fill="#fff"):
    parts = [(-90, 10, 70, 50), (-20, -25, 85, 65), (70, 0, 75, 55), (10, 25, 110, 45)]
    body = "".join(blob(x + dx * s, y + dy * s, rx * s, ry * s, fill=fill, width=0, stroke="none") for dx, dy, rx, ry in parts)
    outline = "".join(blob(x + dx * s, y + dy * s, rx * s, ry * s, width=7) for dx, dy, rx, ry in parts[:3])
    return f'<g>{outline}{body}</g>'


def hills(y=700, fill="#A9CF7A", shade="#93BC63", n=4):
    pts = [(-50, y + 80)]
    for i in range(n * 2 + 1):
        pts.append((i * W / (n * 2), y - (70 if i % 2 else 0) + _j(25)))
    pts += [(W + 50, y + 80)]
    d = _smooth(pts) + f" L{W + 50},{H} L-50,{H} Z"
    return f'<path d="{d}" {_style(fill, INK, 7)}/>' + \
        f'<path d="{_smooth([(-50, y + 60)] + [(x, yy + 45) for x, yy in pts[1:-1]] + [(W + 50, y + 60)])} L{W + 50},{H} L-50,{H} Z" fill="{shade}" opacity="0.55"/>'


def mountains(y=720, fill="#9DA7B5", snow="#fff", peaks=((300, 330), (720, 260), (1180, 350), (1620, 290))):
    out = ""
    for px, ph in peaks:
        base = 330
        out += poly([(px - base, y), (px, ph), (px + base, y)], fill=fill, width=8, wobble=3)
        out += poly([(px - base * 0.28, ph + (y - ph) * 0.28), (px, ph),
                     (px + base * 0.28, ph + (y - ph) * 0.28), (px + 30, ph + (y - ph) * 0.22),
                     (px - 10, ph + (y - ph) * 0.3)], fill=snow, width=6, wobble=2)
        out += f'<path d="M{px},{ph} L{px + base},{y} L{px + base * 0.35},{y} Z" fill="#000" opacity="0.08"/>'
    return out


GROUND = {"grass": ("#B7D98A", "#8FB85F"), "sand": ("#F2D7A0", "#D9B777"), "snow": ("#F4F7FA", "#C9D6E0"),
          "dirt": ("#C9A77C", "#A9855A"), "stone": ("#C7C2B8", "#A39E93"), "floor": ("#D9B98F", "#B99570")}


def ground(y=820, kind="grass"):
    fill, dark = GROUND.get(kind, (kind, kind))
    pts = [(-40, y)] + [(x, y + _j(10)) for x in range(160, W, 320)] + [(W + 40, y)]
    out = f'<path d="{_smooth(pts)} L{W + 40},{H + 40} L-40,{H + 40} Z" {_style(fill, INK, 8)}/>'
    for _ in range(26):
        gx, gy = _rng.randint(40, W - 40), _rng.randint(y + 40, H - 30)
        if kind == "grass":
            for dx, h, lean in ((-10, 20, -8), (0, 30, 2), (10, 22, 9)):
                out += line([(gx + dx, gy), (gx + dx + lean, gy - h - _rng.randint(0, 8))], dark, 5, 0.3)
        elif kind in ("sand", "snow"):
            out += line([(gx - 26, gy), (gx, gy - 8), (gx + 26, gy)], dark, 5, 0.5)
        else:
            if _rng.random() < 0.5:
                out += blob(gx, gy, _rng.randint(6, 12), _rng.randint(4, 8), fill=dark, width=3)
    return out


def water(y=820, fill="#7EC4E0"):
    out = f'<rect x="0" y="{y}" width="{W}" height="{H - y}" fill="{fill}"/>' + line([(-20, y), (W + 20, y)], width=8)
    for row in range(3):
        for x in range(60 + row * 90, W, 300):
            yy = y + 60 + row * 70
            out += line([(x, yy), (x + 30, yy - 14), (x + 60, yy), (x + 90, yy - 14)], "#fff", 6, 0.5)
    return out


# ---------- nature and buildings ----------

def tree(x, y, s=1.0, kind="round", leaf="#6FB35A", leaf_shade="#56984A"):
    trunk = poly([(x - 22 * s, y), (x - 14 * s, y - 170 * s), (x + 14 * s, y - 170 * s), (x + 22 * s, y)], "#8A5A34", width=7)
    if kind == "pine":
        tiers = "".join(poly([(x - (140 - i * 30) * s, y - (120 + i * 95) * s), (x, y - (290 + i * 95) * s),
                              (x + (140 - i * 30) * s, y - (120 + i * 95) * s)], "#3F8F55", width=7) for i in range(3))
        return shadow(x, y, 220 * s) + trunk + tiers
    if kind == "palm":
        trunk = line([(x, y), (x - 25 * s, y - 160 * s), (x - 10 * s, y - 320 * s)], "#8A5A34", 30 * s, 2) + \
            line([(x, y), (x - 25 * s, y - 160 * s), (x - 10 * s, y - 320 * s)], INK, 4, 2)
        fronds = "".join(f'<path d="M{_f(x - 10 * s)},{_f(y - 320 * s)} q{_f(dx * 0.5 * s)},{_f(-90 * s)} {_f(dx * s)},{_f(40 * s)} q{_f(-dx * 0.4 * s)},{_f(-50 * s)} {_f(-dx * s)},{_f(-40 * s)}z" {_style("#4FA35A", INK, 6)}/>'
                         for dx in (-190, -120, 120, 190))
        return shadow(x, y, 200 * s) + trunk + fronds
    crown = blob(x, y - 250 * s, 150 * s, 130 * s, fill=leaf, width=8, wobble=0.06, n=18)
    shade = f'<path d="M{_f(x - 20 * s)},{_f(y - 140 * s)} q{_f(150 * s)},{_f(10 * s)} {_f(165 * s)},{_f(-110 * s)} q{_f(-20 * s)},{_f(90 * s)} {_f(-165 * s)},{_f(110 * s)}z" fill="{leaf_shade}"/>'
    dots = "".join(line([(x + dx * s, y - dy * s), (x + (dx + 18) * s, y - (dy + 6) * s)], leaf_shade, 6, 0.5)
                   for dx, dy in ((-80, 280), (40, 320), (-30, 210), (70, 230)))
    return shadow(x, y, 260 * s) + trunk + crown + shade + dots


def rock(x, y, s=1.0, fill="#A8A29A"):
    return poly([(x - 70 * s, y), (x - 55 * s, y - 55 * s), (x - 5 * s, y - 80 * s), (x + 60 * s, y - 50 * s), (x + 75 * s, y)],
                fill, width=7, wobble=3) + line([(x - 10 * s, y - 60 * s), (x + 15 * s, y - 25 * s)], "#8A857E", 6, 1)


def hut(x, y, s=1.0):
    wall = poly([(x - 150 * s, y), (x - 140 * s, y - 150 * s), (x + 140 * s, y - 150 * s), (x + 150 * s, y)], "#C99A62", width=8)
    roof = poly([(x - 200 * s, y - 130 * s), (x, y - 330 * s), (x + 200 * s, y - 130 * s)], "#D8B25E", width=8)
    straw = "".join(line([(x + dx * s, y - (310 - abs(dx) * 0.9) * s), (x + dx * 1.25 * s, y - 145 * s)], "#B8913F", 5, 1)
                    for dx in (-120, -60, 0, 60, 120))
    door = poly([(x - 40 * s, y), (x - 40 * s, y - 100 * s), (x + 40 * s, y - 100 * s), (x + 40 * s, y)], "#5A3A22", width=7)
    return shadow(x, y, 380 * s) + wall + roof + straw + door


def house(x, y, s=1.0, wall="#F0D9B5", roof="#B5482A"):
    body = rect(x - 170 * s, y - 220 * s, 340 * s, 220 * s, wall, width=8)
    rf = poly([(x - 200 * s, y - 215 * s), (x, y - 380 * s), (x + 200 * s, y - 215 * s)], roof, width=8)
    win = rect(x - 130 * s, y - 170 * s, 80 * s, 70 * s, "#BFE3F0", width=6) + line([(x - 90 * s, y - 170 * s), (x - 90 * s, y - 100 * s)], width=5)
    door = rect(x + 30 * s, y - 130 * s, 80 * s, 130 * s, "#7A4A26", width=7)
    beams = "".join(line([(x - 170 * s, y - yy * s), (x + 170 * s, y - yy * s)], "#C9A77C", 5, 1) for yy in (60, 110))
    return shadow(x, y, 420 * s) + body + beams + rf + win + door


def castle(x, y, s=1.0, stone="#C7C2B8"):
    out = shadow(x, y, 700 * s)
    for tx in (-260, 260):
        out += rect(x + (tx - 70) * s, y - 420 * s, 140 * s, 420 * s, stone, width=8)
        out += "".join(rect(x + (tx - 70 + i * 50) * s, y - 460 * s, 40 * s, 40 * s, stone, width=7) for i in range(3))
    out += rect(x - 190 * s, y - 300 * s, 380 * s, 300 * s, stone, width=8)
    out += "".join(rect(x + (-190 + i * 65) * s, y - 340 * s, 45 * s, 40 * s, stone, width=7) for i in range(6))
    out += f'<path d="M{_f(x - 65 * s)},{_f(y)} v{_f(-120 * s)} a{_f(65 * s)},{_f(65 * s)} 0 0 1 {_f(130 * s)},0 v{_f(120 * s)} z" {_style("#5A3A22", INK, 8)}/>'
    for bx, by in ((-120, 90), (60, 200), (150, 60), (-250, 220), (250, 300)):
        out += line([(x + bx * s, y - by * s), (x + (bx + 50) * s, y - by * s)], "#9C968B", 5, 1)
    out += line([(x + 260 * s, y - 460 * s), (x + 260 * s, y - 580 * s)], width=6) + \
        poly([(x + 262 * s, y - 580 * s), (x + 360 * s, y - 555 * s), (x + 262 * s, y - 530 * s)], "#E4572E", width=6)
    return out


def temple(x, y, s=1.0, stone="#EDE6D6"):
    out = shadow(x, y, 760 * s) + rect(x - 360 * s, y - 50 * s, 720 * s, 50 * s, stone, width=8)
    for i in range(6):
        cx = x + (-300 + i * 120) * s
        out += rect(cx - 30 * s, y - 330 * s, 60 * s, 280 * s, stone, width=7)
        out += line([(cx, y - 320 * s), (cx, y - 60 * s)], "#CFC6B2", 5, 1)
    out += rect(x - 360 * s, y - 380 * s, 720 * s, 50 * s, stone, width=8)
    out += poly([(x - 380 * s, y - 380 * s), (x, y - 520 * s), (x + 380 * s, y - 380 * s)], stone, width=8)
    return out


def pyramid(x, y, s=1.0):
    out = shadow(x, y, 900 * s) + poly([(x - 450 * s, y), (x, y - 480 * s), (x + 450 * s, y)], "#E8C98A", width=8, wobble=3)
    out += f'<path d="M{_f(x)},{_f(y - 480 * s)} L{_f(x + 450 * s)},{_f(y)} L{_f(x + 120 * s)},{_f(y)} Z" fill="#000" opacity="0.1"/>'
    for i in range(1, 6):
        yy = y - i * 80 * s
        half = 450 * s * (1 - i * 80 / 480)
        out += line([(x - half, yy), (x + half, yy)], "#C9A76A", 5, 1.5)
    return out


# ---------- objects ----------

def spear(x, y, length=300, angle=-75):
    a = math.radians(angle)
    ex, ey = x + length * math.cos(a), y + length * math.sin(a)
    tip = [(ex + 40 * math.cos(a), ey + 40 * math.sin(a)), (ex + 16 * math.cos(a + 1.6), ey + 16 * math.sin(a + 1.6)),
           (ex + 16 * math.cos(a - 1.6), ey + 16 * math.sin(a - 1.6))]
    return line([(x, y), (ex, ey)], "#8A5A34", 14, 0.5) + line([(x, y), (ex, ey)], INK, 3, 0.5) + poly(tip, "#9DA7B5", width=5, wobble=0.5)


def sword(x, y, length=240, angle=-60):
    a = math.radians(angle)
    ex, ey = x + length * math.cos(a), y + length * math.sin(a)
    guard = line([(x + 30 * math.cos(a + 1.57), y + 30 * math.sin(a + 1.57)),
                  (x + 30 * math.cos(a - 1.57), y + 30 * math.sin(a - 1.57))], "#B8913F", 14, 0.5)
    return line([(x, y), (ex, ey)], "#D5DCE3", 22, 0.3) + line([(x, y), (ex, ey)], INK, 3, 0.3) + guard


def shield(x, y, s=1.0, fill="#B5482A", emblem=AMBER):
    return poly([(x - 60 * s, y - 70 * s), (x + 60 * s, y - 70 * s), (x + 55 * s, y + 10 * s), (x, y + 80 * s), (x - 55 * s, y + 10 * s)],
                fill, width=7) + blob(x, y - 5 * s, 22 * s, 22 * s, fill=emblem, width=5)


def scroll(x, y, s=1.0, lines=4):
    out = rect(x - 130 * s, y - 90 * s, 260 * s, 180 * s, "#F6E7C1", width=7)
    out += blob(x - 130 * s, y, 22 * s, 95 * s, fill="#E8D39F", width=7) + blob(x + 130 * s, y, 22 * s, 95 * s, fill="#E8D39F", width=7)
    out += "".join(line([(x - 90 * s, y + (-50 + i * 32) * s), (x + (60 - _rng.randint(0, 40)) * s, y + (-50 + i * 32) * s)], "#8A7A5A", 5, 1)
                   for i in range(lines))
    return out


def coin(x, y, s=1.0):
    return blob(x, y, 40 * s, 40 * s, fill="#F5C84C", width=6, wobble=0.02) + text(x, y + 18 * s, "$", size=int(50 * s), fill="#B8913F")


def crown(x, y, s=1.0):
    return poly([(x - 70 * s, y), (x - 80 * s, y - 80 * s), (x - 35 * s, y - 40 * s), (x, y - 95 * s),
                 (x + 35 * s, y - 40 * s), (x + 80 * s, y - 80 * s), (x + 70 * s, y)], "#F5C84C", width=7) + \
        blob(x, y - 25 * s, 12 * s, 12 * s, fill="#E4572E", width=4)


def boat(x, y, s=1.0, sail="#fff"):
    hull = f'<path d="M{_f(x - 260 * s)},{_f(y - 60 * s)} L{_f(x + 260 * s)},{_f(y - 60 * s)} Q{_f(x + 220 * s)},{_f(y + 30 * s)} {_f(x)},{_f(y + 30 * s)} Q{_f(x - 220 * s)},{_f(y + 30 * s)} {_f(x - 260 * s)},{_f(y - 60 * s)} Z" {_style("#8A5A34", INK, 8)}/>'
    mast = line([(x, y - 60 * s), (x, y - 420 * s)], "#6B3E1F", 14, 0.5)
    sl = poly([(x + 10 * s, y - 400 * s), (x + 200 * s, y - 120 * s), (x + 10 * s, y - 110 * s)], sail, width=7)
    planks = line([(x - 230 * s, y - 25 * s), (x + 230 * s, y - 25 * s)], "#6B3E1F", 5, 1)
    return mast + sl + hull + planks


def animal(x, y, s=1.0, kind="dog", fill="#C98E5E", facing=1):
    """Simple doodle quadruped: dog, horse, cow, sheep or cat."""
    L = {"dog": (130, 60, 55), "cat": (110, 50, 50), "horse": (220, 90, 150), "cow": (230, 100, 120),
         "sheep": (170, 90, 90)}[kind]
    bl, bh, leg = L[0] * s, L[1] * s, L[2] * s
    cx, cy = x, y - leg - bh * 0.5
    out = shadow(x, y, bl * 1.6)
    for lx in (-0.35, -0.2, 0.25, 0.38):
        out += line([(cx + lx * bl * facing, cy + bh * 0.3), (cx + lx * bl * facing, y)], fill, 16 * s, 0.5) + \
            line([(cx + lx * bl * facing, cy + bh * 0.3), (cx + lx * bl * facing, y)], INK, 3, 0.5)
    body_fill = "#F4F1EA" if kind == "sheep" else fill
    out += blob(cx, cy, bl * 0.55, bh * 0.6, fill=body_fill, width=8, wobble=0.08 if kind == "sheep" else 0.03)
    if kind == "cow":
        out += blob(cx - bl * 0.15, cy - bh * 0.1, bl * 0.14, bh * 0.22, fill="#111", width=0, stroke="none")
    hx, hy = cx + facing * bl * 0.6, cy - bh * (0.9 if kind == "horse" else 0.45)
    if kind == "horse":
        out += line([(cx + facing * bl * 0.4, cy - bh * 0.2), (hx, hy)], fill, 40 * s, 0.5)
    out += blob(hx, hy, bh * 0.42, bh * 0.36, fill=body_fill if kind != "sheep" else "#3B3330", width=7)
    out += f'<circle cx="{_f(hx + facing * bh * 0.15)}" cy="{_f(hy - bh * 0.08)}" r="{_f(6 * s + 2)}" fill="{INK}"/>'
    if kind in ("dog", "cat"):
        ear = [(hx - facing * bh * 0.1, hy - bh * 0.25), (hx - facing * bh * 0.2, hy - bh * 0.7), (hx + facing * bh * 0.12, hy - bh * 0.3)]
        out += poly(ear, fill, width=6, wobble=0.5)
    tail_x = cx - facing * bl * 0.55
    out += line([(tail_x, cy - bh * 0.1), (tail_x - facing * 40 * s, cy - bh * 0.6)], INK, 8, 1)
    return out


def bird(x, y, s=1.0, fill="#6E7B8B", big=False):
    """Standing bird. big=True gives a long-necked emu/ostrich shape."""
    if big:
        out = shadow(x, y, 180 * s)
        out += line([(x - 25 * s, y - 120 * s), (x - 35 * s, y)], INK, 8, 1) + line([(x + 20 * s, y - 120 * s), (x + 30 * s, y)], INK, 8, 1)
        out += blob(x, y - 170 * s, 110 * s, 75 * s, fill=fill, width=8, wobble=0.09, n=18)
        out += line([(x + 70 * s, y - 200 * s), (x + 95 * s, y - 330 * s)], fill, 26 * s, 1) + \
            line([(x + 70 * s, y - 200 * s), (x + 95 * s, y - 330 * s)], INK, 3, 1)
        out += blob(x + 105 * s, y - 350 * s, 34 * s, 26 * s, fill=fill, width=7)
        out += poly([(x + 135 * s, y - 356 * s), (x + 175 * s, y - 348 * s), (x + 135 * s, y - 340 * s)], AMBER, width=5, wobble=0.5)
        out += f'<circle cx="{_f(x + 115 * s)}" cy="{_f(y - 356 * s)}" r="{_f(6 * s)}" fill="{INK}"/>'
        for fx in (-60, -20, 25):
            out += line([(x + fx * s, y - 150 * s), (x + (fx - 25) * s, y - 125 * s)], "#4E5967", 5, 1)
        return out
    out = blob(x, y - 45 * s, 50 * s, 35 * s, fill=fill, width=6) + blob(x + 40 * s, y - 80 * s, 24 * s, 22 * s, fill=fill, width=6)
    out += poly([(x + 60 * s, y - 84 * s), (x + 85 * s, y - 78 * s), (x + 60 * s, y - 72 * s)], AMBER, width=4, wobble=0.3)
    out += line([(x - 10 * s, y - 12 * s), (x - 12 * s, y)], INK, 5, 0.3) + line([(x + 10 * s, y - 12 * s), (x + 12 * s, y)], INK, 5, 0.3)
    return out + f'<circle cx="{_f(x + 46 * s)}" cy="{_f(y - 86 * s)}" r="{_f(4 * s)}" fill="{INK}"/>'


# ---------- people ----------

def _face(cx, cy, r, expression, facing):
    """Eyes, brows and mouth. expression: neutral, happy, sad, shocked, angry, scared, smug, thinking, laughing."""
    ex = r * 0.34
    fx = r * 0.12 * facing
    out = ""
    eye_r = r * 0.085
    if expression == "laughing":
        for sx in (-1, 1):
            out += line([(cx + fx + sx * ex - 10, cy - r * 0.08), (cx + fx + sx * ex, cy - r * 0.18), (cx + fx + sx * ex + 10, cy - r * 0.08)], width=5, wobble=0.3)
    elif expression == "shocked" or expression == "scared":
        for sx in (-1, 1):
            out += f'<circle cx="{_f(cx + fx + sx * ex)}" cy="{_f(cy - r * 0.12)}" r="{_f(eye_r * 1.7)}" fill="#fff" stroke="{INK}" stroke-width="4"/>'
            out += f'<circle cx="{_f(cx + fx + sx * ex)}" cy="{_f(cy - r * 0.12)}" r="{_f(eye_r * 0.8)}" fill="{INK}"/>'
    else:
        for sx in (-1, 1):
            out += f'<circle cx="{_f(cx + fx + sx * ex)}" cy="{_f(cy - r * 0.12)}" r="{_f(eye_r)}" fill="{INK}"/>'
    brow_y = cy - r * 0.36
    tilt = {"angry": 12, "sad": -10, "scared": -12, "thinking": 6, "smug": 5}.get(expression, 0)
    if tilt or expression in ("shocked",):
        lift = -10 if expression == "shocked" else 0
        for sx in (-1, 1):
            out += line([(cx + fx + sx * (ex + 16), brow_y + lift - (tilt if sx == 1 else 0) * 0.5 * sx * -1 + (tilt * 0.5 if sx == -1 else 0)),
                         (cx + fx + sx * (ex - 14), brow_y + lift + (tilt * 0.5 if sx == 1 else -tilt * 0.5) * (1 if sx == 1 else -1))], width=5, wobble=0.3)
    my = cy + r * 0.32
    mx = cx + fx
    if expression in ("happy", "smug"):
        out += f'<path d="M{_f(mx - r * 0.3)},{_f(my - 4)} Q{_f(mx)},{_f(my + r * 0.28)} {_f(mx + r * 0.3)},{_f(my - 4)}" {_style("none", INK, 5)}/>'
        if expression == "smug":
            out = out.replace(f'M{_f(mx - r * 0.3)}', f'M{_f(mx - r * 0.1)}')
    elif expression == "laughing":
        out += f'<path d="M{_f(mx - r * 0.32)},{_f(my - 8)} Q{_f(mx)},{_f(my + r * 0.4)} {_f(mx + r * 0.32)},{_f(my - 8)} Z" {_style("#7A2E2E", INK, 5)}/>'
    elif expression in ("sad",):
        out += f'<path d="M{_f(mx - r * 0.25)},{_f(my + 10)} Q{_f(mx)},{_f(my - r * 0.18)} {_f(mx + r * 0.25)},{_f(my + 10)}" {_style("none", INK, 5)}/>'
    elif expression in ("shocked", "scared"):
        out += blob(mx, my + 4, r * 0.14, r * 0.19, fill="#7A2E2E", width=5, wobble=0.02)
    elif expression == "angry":
        out += line([(mx - r * 0.25, my + 6), (mx, my - 4), (mx + r * 0.25, my + 6)], width=5, wobble=0.3)
    elif expression == "thinking":
        out += line([(mx - r * 0.2, my), (mx + r * 0.2, my + 8)], width=5, wobble=0.3)
    else:
        out += line([(mx - r * 0.2, my + 2), (mx + r * 0.2, my + 2)], width=5, wobble=0.3)
    if expression in ("happy", "laughing", "smug"):
        for sx in (-1, 1):
            out += f'<ellipse cx="{_f(cx + fx + sx * r * 0.55)}" cy="{_f(cy + r * 0.18)}" rx="{_f(r * 0.13)}" ry="{_f(r * 0.08)}" fill="#F29C9C" opacity="0.7"/>'
    return out


def _hair(cx, cy, r, style, color):
    c = HAIR.get(color, color)
    if style == "bald":
        return f'<path d="M{_f(cx - r * 0.5)},{_f(cy - r * 0.75)} q{_f(r * 0.3)},{_f(-r * 0.2)} {_f(r * 0.5)},{_f(-r * 0.1)}" {_style("none", "#fff", 6)} opacity="0.6"/>'
    if style == "messy":
        pts = []
        for i in range(15):
            a = math.pi + math.pi * i / 14
            k = 1.18 + (0.22 if i % 2 else 0) + _j(0.05)
            pts.append((cx + r * k * math.cos(a), cy - r * 0.05 + r * k * math.sin(a)))
        return f'<path d="{_smooth(pts)} Q{_f(cx)},{_f(cy - r * 0.55)} {_f(pts[0][0])},{_f(pts[0][1])} Z" {_style(c, INK, 7)}/>'
    if style == "long":
        return f'<path d="M{_f(cx - r * 1.08)},{_f(cy + r * 0.9)} Q{_f(cx - r * 1.25)},{_f(cy - r * 1.25)} {_f(cx)},{_f(cy - r * 1.08)} Q{_f(cx + r * 1.25)},{_f(cy - r * 1.25)} {_f(cx + r * 1.08)},{_f(cy + r * 0.9)} L{_f(cx + r * 0.8)},{_f(cy + r * 0.2)} Q{_f(cx)},{_f(cy - r * 0.75)} {_f(cx - r * 0.8)},{_f(cy + r * 0.2)} Z" {_style(c, INK, 7)}/>'
    if style == "bun":
        return blob(cx, cy - r * 1.05, r * 0.35, r * 0.3, fill=c, width=7) + \
            f'<path d="M{_f(cx - r)},{_f(cy - r * 0.1)} Q{_f(cx)},{_f(cy - r * 1.35)} {_f(cx + r)},{_f(cy - r * 0.1)} Q{_f(cx)},{_f(cy - r * 0.65)} {_f(cx - r)},{_f(cy - r * 0.1)} Z" {_style(c, INK, 7)}/>'
    return f'<path d="M{_f(cx - r * 1.02)},{_f(cy - r * 0.05)} Q{_f(cx - r * 0.9)},{_f(cy - r * 1.3)} {_f(cx + r * 0.2)},{_f(cy - r * 1.08)} Q{_f(cx + r * 1.1)},{_f(cy - r * 0.95)} {_f(cx + r * 1.02)},{_f(cy - r * 0.05)} Q{_f(cx + r * 0.4)},{_f(cy - r * 0.6)} {_f(cx - r * 1.02)},{_f(cy - r * 0.05)} Z" {_style(c, INK, 7)}/>'


def _hat(cx, cy, r, hat):
    if hat == "helmet":
        return f'<path d="M{_f(cx - r * 1.1)},{_f(cy - r * 0.2)} Q{_f(cx)},{_f(cy - r * 1.6)} {_f(cx + r * 1.1)},{_f(cy - r * 0.2)} Z" {_style("#9DA7B5", INK, 7)}/>' + \
            line([(cx, cy - r * 1.05), (cx, cy - r * 0.2)], "#7D8794", 5, 0.3)
    if hat == "crown":
        return crown(cx, cy - r * 0.75, r / 90)
    if hat == "wide":
        return blob(cx, cy - r * 0.62, r * 1.5, r * 0.22, fill="#8A5A34", width=7) + \
            f'<path d="M{_f(cx - r * 0.75)},{_f(cy - r * 0.62)} Q{_f(cx)},{_f(cy - r * 1.6)} {_f(cx + r * 0.75)},{_f(cy - r * 0.62)} Z" {_style("#8A5A34", INK, 7)}/>'
    if hat == "hood":
        return f'<path d="M{_f(cx - r * 1.2)},{_f(cy + r * 0.8)} Q{_f(cx - r * 1.35)},{_f(cy - r * 1.5)} {_f(cx)},{_f(cy - r * 1.3)} Q{_f(cx + r * 1.35)},{_f(cy - r * 1.5)} {_f(cx + r * 1.2)},{_f(cy + r * 0.8)} L{_f(cx + r * 0.9)},{_f(cy + r * 0.4)} Q{_f(cx)},{_f(cy - r * 1.1)} {_f(cx - r * 0.9)},{_f(cy + r * 0.4)} Z" {_style("#7A6A58", INK, 7)}/>'
    if hat == "top":
        return rect(cx - r * 0.55, cy - r * 1.9, r * 1.1, r * 1.05, "#222", width=6) + rect(cx - r * 0.9, cy - r * 0.9, r * 1.8, r * 0.15, "#222", width=6)
    return ""


def person(x, y, s=1.0, skin=SKIN, shirt="#4E7FB0", pants="#3B3B4F", hair="brown", hair_style="short",
           expression="neutral", pose="stand", facing=1, hat=None, outfit="shirt", prop=None):
    """A Scribble Age character standing on (x, y).
    pose: stand, wave, arms_up, point, hold, walk, run, shrug, cheer
    expression: neutral, happy, sad, shocked, angry, scared, smug, thinking, laughing
    outfit: shirt, robe, armor, fur, dress
    prop: None, spear, sword, shield, torch, scroll, coin
    hat: None, helmet, crown, wide, hood, top
    """
    r = 58 * s
    hip_y = y - 150 * s
    neck_y = hip_y - 150 * s
    head_cy = neck_y - r * 0.95
    sx = facing
    out = shadow(x, y, 170 * s)
    # legs
    stride = {"walk": 35, "run": 60}.get(pose, 0) * s
    for side, off in ((-1, -stride), (1, stride)):
        foot_x = x + side * 30 * s + off * sx
        out += line([(x + side * 22 * s, hip_y), (foot_x, y - 8 * s)], pants if outfit not in ("robe", "dress") else INK, 26 * s, 1)
        out += line([(x + side * 22 * s, hip_y), (foot_x, y - 8 * s)], INK, 4, 1)
        out += blob(foot_x + 14 * s * sx, y - 8 * s, 26 * s, 12 * s, fill="#3A2A20", width=5)
    # torso
    body_fill = {"robe": "#8C6BB1", "armor": "#9DA7B5", "fur": "#8A5A34", "dress": "#D96C8A"}.get(outfit, shirt)
    if outfit in ("robe", "dress"):
        torso = [(x - 55 * s, neck_y + 10 * s), (x + 55 * s, neck_y + 10 * s), (x + 90 * s, y - 30 * s), (x - 90 * s, y - 30 * s)]
    else:
        torso = [(x - 55 * s, neck_y + 10 * s), (x + 55 * s, neck_y + 10 * s), (x + 62 * s, hip_y + 8 * s), (x - 62 * s, hip_y + 8 * s)]
    out += poly(torso, body_fill, width=8, wobble=1.5)
    out += f'<path d="M{_f(x + 10 * s)},{_f(neck_y + 14 * s)} L{_f(torso[1][0])},{_f(torso[1][1] + 4)} L{_f(torso[2][0])},{_f(torso[2][1])} L{_f(x + 20 * s)},{_f(torso[2][1])} Z" fill="#000" opacity="0.1"/>'
    if outfit == "armor":
        out += "".join(line([(x - 50 * s, neck_y + dy * s), (x + 50 * s, neck_y + dy * s)], "#7D8794", 5, 1) for dy in (50, 95, 140))
    if outfit == "fur":
        out += "".join(line([(x + dx * s, neck_y + dy * s), (x + (dx + 10) * s, neck_y + (dy + 18) * s)], "#5E3A1E", 5, 0.5)
                       for dx, dy in ((-30, 40), (15, 60), (-10, 100), (30, 120), (-40, 130)))
    if outfit == "shirt":
        out += line([(x - 55 * s, hip_y - 10 * s), (x + 55 * s, hip_y - 10 * s)], "#2E2E3E", 8, 1)
    # arms: (shoulder -> elbow -> hand) per side
    sh_y = neck_y + 30 * s
    arms = {
        "stand": [(-1, (-85, 90), (-80, 170)), (1, (85, 90), (80, 170))],
        "wave": [(-1, (-85, 90), (-80, 170)), (1, (110, -10), (130, -110))],
        "arms_up": [(-1, (-100, -20), (-130, -130)), (1, (100, -20), (130, -130))],
        "point": [(-1, (-85, 90), (-80, 170)), (1, (110, 10), (210, -20))],
        "hold": [(-1, (-70, 70), (30, 90)), (1, (80, 70), (60, 90))],
        "walk": [(-1, (-70, 80), (-40, 160)), (1, (70, 80), (95, 150))],
        "run": [(-1, (-90, 40), (-60, -30)), (1, (80, 90), (150, 120))],
        "shrug": [(-1, (-110, 40), (-150, -20)), (1, (110, 40), (150, -20))],
        "cheer": [(-1, (-85, 90), (-80, 170)), (1, (100, -20), (120, -140))],
    }.get(pose, [])
    hands = {}
    for side, (ex_, ey_), (hx, hy) in arms:
        shx = x + side * 52 * s
        pts = [(shx, sh_y), (x + ex_ * s * (sx if side == 1 or pose in ("point",) else 1), sh_y + ey_ * s),
               (x + hx * s * (sx if pose in ("point", "run") else 1), sh_y + hy * s)]
        out += line(pts, body_fill, 24 * s, 1) + line(pts, INK, 4, 1)
        out += blob(pts[-1][0], pts[-1][1], 17 * s, 17 * s, fill=skin, width=5)
        hands[side] = pts[-1]
    # head
    out += line([(x, neck_y + 12 * s), (x, head_cy + r * 0.8)], skin, 26 * s, 0.3)
    out += _hair(x, head_cy, r, "long", hair) if hair_style == "long" else ""
    out += blob(x, head_cy, r, r * 1.02, fill=skin, width=8, wobble=0.025)
    out += f'<path d="M{_f(x + r * 0.35 * sx)},{_f(head_cy - r * 0.85)} A{_f(r)},{_f(r)} 0 0 {1 if sx > 0 else 0} {_f(x + r * 0.35 * sx)},{_f(head_cy + r * 0.88)} Q{_f(x + r * 0.7 * sx)},{_f(head_cy)} {_f(x + r * 0.35 * sx)},{_f(head_cy - r * 0.85)} Z" fill="{SKIN_SHADE if skin == SKIN else "#000"}" opacity="{0.6 if skin == SKIN else 0.12}"/>'
    out += blob(x - r * 0.98 * sx, head_cy + r * 0.05, r * 0.16, r * 0.22, fill=skin, width=5)
    if hair_style != "long":
        out += _hair(x, head_cy, r, hair_style, hair)
    out += _face(x, head_cy, r, expression, sx)
    if hat:
        out += _hat(x, head_cy, r, hat)
    if prop and 1 in hands:
        hx, hy = hands[1]
        out += {"spear": lambda: spear(hx, hy + 120 * s, 330 * s, -88),
                "sword": lambda: sword(hx, hy, 230 * s, -70),
                "shield": lambda: shield(hands[-1][0], hands[-1][1], s),
                "torch": lambda: line([(hx, hy + 60 * s), (hx + 20 * s, hy - 80 * s)], "#8A5A34", 16 * s, 0.5) + fire(hx + 22 * s, hy - 70 * s, 0.45 * s),
                "scroll": lambda: scroll(hx, hy, 0.5 * s),
                "coin": lambda: coin(hx, hy - 30 * s, s)}.get(prop, lambda: "")()
    if expression in ("scared", "shocked") and pose not in ("run",):
        out += sweat(x + r * 1.1 * sx, head_cy - r * 0.6, s)
    return out


def mascot(x, y, s=1.0, expression="happy", pose="stand", facing=1):
    """The channel mascot: a caveman with messy dark hair, a fur tunic and a giant pencil."""
    out = person(x, y, s, shirt="#8A5A34", pants="#8A5A34", hair="black", hair_style="messy",
                 expression=expression, pose=pose, facing=facing, outfit="fur")
    px = x + (140 if pose in ("stand", "walk") else -150) * s * facing
    if pose in ("stand", "walk", "point", "wave", "cheer"):
        px = x - 130 * s * facing
        pencil_bottom, pencil_top = (px, y - 30 * s), (px + 40 * s * facing, y - 420 * s)
        out += line([pencil_bottom, pencil_top], AMBER, 34 * s, 0.3) + line([pencil_bottom, pencil_top], INK, 4, 0.3)
        tx, ty = pencil_top
        out += poly([(tx - 17 * s, ty), (tx + 17 * s, ty + 4 * s), (tx + 2 * s, ty - 55 * s)], "#F4DDB0", width=5, wobble=0.3)
        out += blob(pencil_bottom[0], pencil_bottom[1], 18 * s, 14 * s, fill="#F29C9C", width=5)
    return out


def crowd(x, y, n=7, s=0.7, spread=900, expression="neutral", pose="stand", seed_=3, **kw):
    """A row of varied people centered on x."""
    r = random.Random(seed_)
    shirts = ["#4E7FB0", "#B5482A", "#6FB35A", "#8C6BB1", "#E8A33D", "#3F8F85", "#C75B7A"]
    out = ""
    for i in range(n):
        px = x - spread / 2 + spread * (i + 0.5) / n + r.uniform(-20, 20)
        out += person(px, y + r.uniform(-8, 8), s * r.uniform(0.9, 1.08), skin=r.choice(SKINS), shirt=r.choice(shirts),
                      hair=r.choice(list(HAIR)), hair_style=r.choice(["short", "short", "bun", "long", "bald", "messy"]),
                      expression=expression, pose=pose, facing=r.choice([1, -1]), **kw)
    return out


# ---------- composition ----------

def scene(*parts, bg=CREAM, w=W, h=H, scene_seed=None):
    """Wrap fragments into a full SVG document."""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<rect width="{w}" height="{h}" fill="{bg}"/>' + "".join(parts) + "</svg>")


def paper_frame():
    """Subtle inner border that makes a frame feel like a page in a sketchbook."""
    return rect(18, 18, W - 36, H - 36, "none", "#000", 4, 1.5).replace('stroke="#000"', 'stroke="#000" stroke-opacity="0.12"')
