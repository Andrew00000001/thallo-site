#!/usr/bin/env python3
"""Check a Scribble Age episode before building it.

    python3 review.py episodes/YYYY-MM-DD.json --out /tmp/sa_review

Validates the JSON, counts words and shots, flags text inside the caption zone, and renders
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

    tiles, adds = [], 0
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
            try:
                png = out / f"shot_{i + 1:02d}_{k + 1}.png"
                cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=str(png), output_width=TW * 2, output_height=TH * 2,
                                 background_color="white")
                tiles.append((label, png))
            except Exception as e:
                problems.append(f"shot {label} does not render: {e}")

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
