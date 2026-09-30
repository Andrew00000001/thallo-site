#!/usr/bin/env python3
"""Check a Scribble Age episode before building it.

    python3 review.py episodes/YYYY-MM-DD.json --out /tmp/sa_review

Validates the JSON, counts words and shots, and catches mechanical mistakes: text in the caption
zone, text off the frame, overlapping text, near-empty frames, repeated shots, possible spelling
mistakes, and on-screen numbers to verify against sources. Then it renders
contact sheets (16 shots per sheet, numbered) plus the thumbnail at full and phone size.
Look at every sheet it prints. Exit code 1 means there's a problem that has to be fixed.
"""
import argparse, json, re, sys
from pathlib import Path

import cairosvg
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import doodle  # noqa: E402  (installs the Patrick Hand font for cairosvg)
from make_video import shot_svgs  # noqa: E402

TW, TH = 480, 270  # tile size on the contact sheets
CAPTION_TOP = 840


def text_in_caption_zone(svg):
    hits = []
    for m in re.finditer(r"<text\b[^>]*>", svg):
        tag = m.group(0)
        y = re.search(r'\by="([\d.]+)"', tag)
        if y and float(y.group(1)) > CAPTION_TOP and "rotate" not in tag:
            hits.append(float(y.group(1)))
    return hits


TEXT_RE = re.compile(r"<text\b([^>]*)>(.*?)</text>", re.S)


def text_boxes(svg):
    """Bounding boxes of visible text (outline layers are merged with their fill layer)."""
    boxes = {}
    for attrs, body in TEXT_RE.findall(svg):
        if "rotate" in attrs:
            continue
        g = lambda k: re.search(k + r'="([^"]+)"', attrs)
        x, y, size = g(r"\bx"), g(r"\by"), g("font-size")
        if not (x and y and size):
            continue
        x, y, size = float(x.group(1)), float(y.group(1)), float(size.group(1))
        content = re.sub(r"<[^>]+>", "", body).replace("&amp;", "&").replace("&lt;", "<")
        w = doodle.text_width(content, size)
        anchor = g("text-anchor")
        x0 = x - w / 2 if (anchor and anchor.group(1) == "middle") else (x - w if anchor and anchor.group(1) == "end" else x)
        boxes[(round(x), round(y), content)] = (x0, y - size * 0.78, x0 + w, y + size * 0.22, content)
    return list(boxes.values())


def overlap(a, b, pad=6):
    return not (a[2] + pad <= b[0] or b[2] + pad <= a[0] or a[3] + pad <= b[1] or b[3] + pad <= a[1])


def emptiness(png):
    """Share of the frame taken by its single most common color (1.0 = one flat color)."""
    im = Image.open(png).convert("RGB").resize((96, 54)).quantize(8)
    counts = sorted(im.getcolors(), reverse=True)
    return counts[0][0] / (96 * 54)


def speller():
    try:
        from spellchecker import SpellChecker
        return SpellChecker()
    except Exception:
        return None


NUM_RE = re.compile(r"\d[\d,.]*")


def main(path, out):
    ep = json.loads(Path(path).read_text(encoding="utf-8"))
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    problems, warnings = [], []
    for key in ("title", "description", "tags", "thumbnail_svg", "scenes"):
        if key not in ep:
            problems.append(f"missing '{key}'")
    if problems:
        print("\n".join("PROBLEM: " + p for p in problems))
        return 1
    if len(ep["title"]) > 70:
        warnings.append(f"title is {len(ep['title'])} characters (aim for under 70)")
    if not 10 <= len(ep["tags"]) <= 15:
        warnings.append(f"{len(ep['tags'])} tags (aim for 10 to 15)")
    words = sum(len(sc["narration"].split()) for sc in ep["scenes"])
    if not 850 <= words <= 1100:
        problems.append(f"script is {words} words (must be 850 to 1100)")

    tiles, adds, screen_text = [], 0, []
    for i, sc in enumerate(ep["scenes"]):
        shots = sc.get("shots", [])
        if len(shots) != 2:
            problems.append(f"scene {i + 1} has {len(shots)} shots (must be 2)")
        if shots and "svg" not in shots[0]:
            problems.append(f"scene {i + 1}: the first shot must be a full 'svg'")
        adds += sum(1 for s in shots if "add" in s)
        try:
            svgs = shot_svgs(sc)
        except Exception as e:
            problems.append(f"scene {i + 1}: {e}")
            continue
        for k, svg in enumerate(svgs):
            label = f"{i + 1}.{k + 1}"
            low = text_in_caption_zone(svg)
            if low:
                problems.append(f"shot {label}: text at y={low[0]:.0f}, inside the caption zone (keep text above y={CAPTION_TOP})")
            boxes = text_boxes(svg)
            for bx in boxes:
                if bx[0] < 12 or bx[2] > 1908 or bx[1] < 6:
                    problems.append(f"shot {label}: text '{bx[4][:30]}' runs off the edge of the frame")
            for a_i in range(len(boxes)):
                for b_i in range(a_i + 1, len(boxes)):
                    if overlap(boxes[a_i], boxes[b_i]):
                        problems.append(f"shot {label}: texts '{boxes[a_i][4][:24]}' and '{boxes[b_i][4][:24]}' overlap")
            if k > 0 and svg == svgs[k - 1]:
                problems.append(f"shot {label} is identical to the shot before it")
            screen_text.append((i, " ".join(b[4] for b in boxes)))
            try:
                png = out / f"shot_{i + 1:02d}_{k + 1}.png"
                cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=str(png), output_width=TW * 2, output_height=TH * 2,
                                 background_color="white")
                tiles.append((label, png))
                if emptiness(png) > 0.82:
                    problems.append(f"shot {label} is mostly one flat color (looks empty). Add a setting and details")
            except Exception as e:
                problems.append(f"shot {label} does not render: {e}")

    sp = speller()
    narration_all = " ".join(sc["narration"] for sc in ep["scenes"]).lower()
    to_verify = []
    for i, txt in screen_text:
        narr = ep["scenes"][i]["narration"]
        for num in set(NUM_RE.findall(txt)):
            n = num.strip(",.")
            if n and n.replace(",", "") not in narr.replace(",", ""):
                to_verify.append(f"scene {i + 1}: on-screen '{n}' (narration: \"{narr[:90]}...\")")
        if sp:
            words = [w for w in re.findall(r"[A-Za-z']{3,}", txt) if w.lower() not in narration_all]
            bad = sp.unknown([w.lower() for w in words])
            if bad:
                warnings.append(f"scene {i + 1}: possible on-screen spelling mistakes: {', '.join(sorted(bad))}")
    if sp:
        narr_words = [w for w in re.findall(r"\b[a-z][a-z']{2,}\b", " ".join(sc["narration"] for sc in ep["scenes"]))]
        bad = sp.unknown(narr_words)
        if bad:
            warnings.append(f"narration words to double-check spelling: {', '.join(sorted(bad)[:25])}")

    total_shots = sum(len(sc.get("shots", [])) for sc in ep["scenes"])
    if total_shots and not 0.25 <= adds / total_shots * 2 <= 0.75:
        warnings.append(f"{adds} of {total_shots // 2} second shots are 'add' reveals (aim for about half)")

    sheets = []
    for n in range(0, len(tiles), 16):
        sheet = Image.new("RGB", (TW * 4, TH * 4), "white")
        draw = ImageDraw.Draw(sheet)
        for j, (label, png) in enumerate(tiles[n:n + 16]):
            x, y = (j % 4) * TW, (j // 4) * TH
            sheet.paste(Image.open(png).convert("RGB").resize((TW, TH)), (x, y))
            draw.rectangle([x + TW - 60, y + TH - 26, x + TW, y + TH], fill="black")
            draw.text((x + TW - 54, y + TH - 20), label, fill="white")
            draw.line([(x, y + TH * CAPTION_TOP / 1080), (x + TW, y + TH * CAPTION_TOP / 1080)], fill=(255, 0, 0), width=1)
        path_ = out / f"sheet_{n // 16 + 1}.png"
        sheet.save(path_)
        sheets.append(str(path_))

    try:
        thumb = out / "thumbnail.png"
        cairosvg.svg2png(bytestring=ep["thumbnail_svg"].encode("utf-8"), write_to=str(thumb), output_width=1280, output_height=720,
                         background_color="white")
        Image.open(thumb).resize((320, 180)).save(out / "thumbnail_phone.png")
    except Exception as e:
        problems.append(f"thumbnail does not render: {e}")

    print(json.dumps({"words": words, "scenes": len(ep["scenes"]), "shots": total_shots, "add_reveals": adds,
                      "contact_sheets": sheets, "thumbnail": str(out / "thumbnail.png"),
                      "thumbnail_phone": str(out / "thumbnail_phone.png")}, indent=1))
    if to_verify:
        print("VERIFY each on-screen number against your sources (it isn't written the same way in the narration):")
        for v in to_verify:
            print("  -", v)
    for w in warnings:
        print("WARNING:", w)
    for p in problems:
        print("PROBLEM:", p)
    print("red line on each tile = top of the caption zone")
    return 1 if problems else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("episode")
    ap.add_argument("--out", default="/tmp/sa_review")
    a = ap.parse_args()
    sys.exit(main(a.episode, a.out))
