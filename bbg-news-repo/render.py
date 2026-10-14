"""Renders 1080x1350 (4:5) JPEG post cards for Instagram."""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent
FONT_HEAD = str(ROOT / "assets/fonts/Anton-Regular.ttf")
FONT_BODY = str(ROOT / "assets/fonts/Barlow-SemiBold.ttf")

W, H = 1080, 1350
PAD = 80
BG = (14, 15, 20)
STRIPE = (24, 25, 32)
GOLD = (245, 183, 0)
WHITE = (255, 255, 255)
GREY = (190, 192, 200)
DIM = (120, 122, 132)


def _font(path, size):
    return ImageFont.truetype(path, size)


def _wrap(draw, text, font, max_w):
    lines, line = [], ""
    for word in text.split():
        trial = f"{line} {word}".strip()
        if draw.textlength(trial, font=font) <= max_w or not line:
            line = trial
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def _fit(draw, paragraphs, path, max_w, max_h, start, smallest, spacing):
    """Largest font size where all wrapped paragraphs fit in the box."""
    for size in range(start, smallest - 1, -2):
        font = _font(path, size)
        lines = [_wrap(draw, p, font, max_w) for p in paragraphs]
        line_h = int(size * spacing)
        total = sum(len(l) for l in lines) * line_h + (len(lines) - 1) * int(size * 0.45)
        if total <= max_h:
            return font, lines, line_h
    font = _font(path, smallest)
    return font, [_wrap(draw, p, font, max_w) for p in paragraphs], int(smallest * spacing)


def _frame(cfg, tag):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    for x in range(-H, W, 90):
        d.line([(x, H), (x + H, 0)], fill=STRIPE, width=28)
    d.rectangle([0, 0, W, 14], fill=GOLD)

    d.text((PAD, 70), cfg["brand_name"], font=_font(FONT_HEAD, 64), fill=GOLD)
    tag_font = _font(FONT_BODY, 30)
    tw = d.textlength(tag, font=tag_font)
    x1 = W - PAD
    d.rounded_rectangle([x1 - tw - 40, 82, x1, 138], radius=28, outline=GOLD, width=3)
    d.text((x1 - tw - 20, 110), tag, font=tag_font, fill=GOLD, anchor="lm")
    d.line([(PAD, 180), (W - PAD, 180)], fill=(45, 47, 58), width=3)

    d.rectangle([0, H - 170, W, H], fill=(10, 10, 14))
    d.rectangle([0, H - 170, W, H - 164], fill=GOLD)
    d.text((W // 2, H - 112), cfg["footer_line"], font=_font(FONT_BODY, 34), fill=WHITE, anchor="mm")
    d.text((W // 2, H - 60), cfg["disclaimer"], font=_font(FONT_BODY, 26), fill=DIM, anchor="mm")
    return img, d


def render_card(cfg, tag, headline, body, out_path):
    """Headline + body lines. Used for news and fact posts."""
    img, d = _frame(cfg, tag)
    max_w = W - 2 * PAD
    top, bottom = 230, H - 210

    hfont, hlines, hlh = _fit(d, [headline], FONT_HEAD, max_w, 430, 150, 64, 1.12)
    head_h = len(hlines[0]) * hlh + 90
    if body:
        bfont, blines, blh = _fit(d, body, FONT_BODY, max_w - 40, bottom - top - head_h, 58, 28, 1.3)
        gap = int(bfont.size * 0.45)
        body_h = sum(len(p) for p in blines) * blh + (len(blines) - 1) * gap
    else:
        body_h = 0

    # Center the block, nudged slightly above the middle.
    y = top + max(0, (bottom - top - head_h - body_h) * 2 // 5)
    for line in hlines[0]:
        d.text((PAD, y), line, font=hfont, fill=WHITE)
        y += hlh
    y += 30
    d.rectangle([PAD, y, PAD + 140, y + 10], fill=GOLD)
    y += 60

    if body:
        for para in blines:
            d.rectangle([PAD, y + 12, PAD + 12, y + bfont.size - 6], fill=GOLD)
            for line in para:
                d.text((PAD + 40, y), line, font=bfont, fill=GREY)
                y += blh
            y += gap

    img.save(out_path, "JPEG", quality=92)
    return out_path


def render_countdown(cfg, days_left, out_path):
    """Big-number countdown card. days_left == 0 is launch day."""
    img, d = _frame(cfg, "COUNTDOWN" if days_left else "LAUNCH DAY")
    if days_left:
        d.text((W // 2, 560), str(days_left), font=_font(FONT_HEAD, 460), fill=GOLD, anchor="mm")
        d.text((W // 2, 850), "DAY" if days_left == 1 else "DAYS", font=_font(FONT_HEAD, 120), fill=WHITE, anchor="mm")
        d.text((W // 2, 990), "UNTIL BATTLE BEARS GOLD", font=_font(FONT_BODY, 56), fill=GREY, anchor="mm")
    else:
        d.text((W // 2, 470), "IT'S", font=_font(FONT_HEAD, 140), fill=WHITE, anchor="mm")
        d.text((W // 2, 660), "LAUNCH", font=_font(FONT_HEAD, 260), fill=GOLD, anchor="mm")
        d.text((W // 2, 920), "DAY", font=_font(FONT_HEAD, 260), fill=GOLD, anchor="mm")
        d.text((W // 2, 1085), "BATTLE BEARS GOLD", font=_font(FONT_BODY, 56), fill=GREY, anchor="mm")
    img.save(out_path, "JPEG", quality=92)
    return out_path


def render_reel_overlay(cfg, tag, credit, out_path):
    """Transparent 1080x1920 PNG laid over Reels: brand header plus a credit plate.

    The credit plate sits above the bottom ~400px that Instagram covers with its caption UI.
    """
    rw, rh = 1080, 1920
    img = Image.new("RGBA", (rw, rh), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, rw, 250], fill=(12, 12, 16, 235))
    d.rectangle([0, 242, rw, 250], fill=GOLD + (255,))
    d.text((PAD, 150), cfg["brand_name"], font=_font(FONT_HEAD, 92), fill=GOLD + (255,), anchor="lm")
    tag_font = _font(FONT_BODY, 34)
    tw = d.textlength(tag, font=tag_font)
    x1 = rw - PAD
    d.rounded_rectangle([x1 - tw - 44, 120, x1, 182], radius=31, outline=GOLD + (255,), width=3)
    d.text((x1 - tw - 22, 151), tag, font=tag_font, fill=GOLD + (255,), anchor="lm")

    credit_font = _font(FONT_HEAD, 64)
    while d.textlength(credit, font=credit_font) > rw - 2 * PAD - 60 and credit_font.size > 32:
        credit_font = _font(FONT_HEAD, credit_font.size - 4)
    cw = d.textlength(credit, font=credit_font)
    d.rounded_rectangle([(rw - cw) / 2 - 30, 1330, (rw + cw) / 2 + 30, 1430], radius=18, fill=(12, 12, 16, 215))
    d.rectangle([(rw - cw) / 2 - 30, 1424, (rw + cw) / 2 + 30, 1430], fill=GOLD + (255,))
    d.text((rw / 2, 1378), credit, font=credit_font, fill=WHITE + (255,), anchor="mm")
    d.text((rw / 2, 1468), cfg["disclaimer"], font=_font(FONT_BODY, 30), fill=GREY + (255,), anchor="mm",
           stroke_width=2, stroke_fill=(0, 0, 0, 200))
    img.save(out_path)
    return out_path
