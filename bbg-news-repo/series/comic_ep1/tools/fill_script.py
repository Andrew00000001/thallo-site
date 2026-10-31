"""Fill tools/SCRIPT.tmpl.md from pages.json, teaser_pages.json, panels.json and
tools/build/optional_prompts.json, so every prompt and every letter in SCRIPT.md is
identical to the JSON deliverables. Run build_layout.py first.

Usage: python3 -I series/comic_ep1/tools/fill_script.py   (writes series/comic_ep1/SCRIPT.md)
"""
import json
import re
from pathlib import Path

EP = Path(__file__).resolve().parents[1]
TOOLS = EP / "tools"
out = EP / "SCRIPT.md"
tmpl = (TOOLS / "SCRIPT.tmpl.md").read_text()
pages = json.loads((EP / "pages.json").read_text())["pages"]
pages += json.loads((EP / "teaser_pages.json").read_text())["pages"]
panels = {p["id"]: p for p in json.loads((EP / "panels.json").read_text())}
opt = json.loads((TOOLS / "build" / "optional_prompts.json").read_text())
PG = {p["id"]: p for p in pages}

ALT = {
 "s01": "Comic cover. High over a sunny field of zig-zag trenches, Sanchez, a teddy-bear cyborg with a glowing red visor and a huge red-and-black robot arm, flies in a superhero pose, fist forward. Tucked under his robot arm, Oliver, a brown teddy-bear soldier in a red headband, hugs a glowing basket of fries with a fry in his mouth as fries tumble out behind them. Gold title: We'll Getcha Home. Cyan screen box: BBG News, live. Local Hazards, episode 1. A target ring on Sanchez reads: Destination: home? Swipe.",
 "s02": "B-1000, a hulking maroon robot bear with glowing cyan eye-slits, a rail-gun arm and cyan claws, stands below a chunky grey crashed dropship with red bands and a glowing pad on its roof. His cyan screen box: \"B-1000. Live. Scanning location.\" Two identical panels of the ship, his head peeking up from below: \"Hazard: crashed dropship.\" \"Status: still crashed.\" He shouts beside a close-up of the roof pad in a target ring: \"Launch pad destination: the other crashed dropship.\"",
 "s03": "Title band: Local Hazards, with a news sting: dun-dunn! Caption: The red food stand. Under a red-and-yellow parasol, Oliver sits in the grass, eyes shut in bliss, biting a fry beside a glowing basket. Screen tag: \"Subject: Oliver. Threat level: fluffy.\" Sound: crunch! Bottom panel: a red-and-black robot arm swings into view, pointing, beside a dark grey gloved hand on a chest plate. Sound: ka-chunk!",
 "s04": "Low angle: Sanchez towers over Oliver, his gloved hand on his chest, pointing his robot arm down at him. Screen tag: \"Subject: Sanchez. Threat level: partial upgrade.\" Sanchez: \"Oliver, we'll getcha...\" \"...home.\"",
 "s05": "Looking down at Oliver, mouth stuffed, grinning guiltily and holding up a single fry, the basket beside him: \"Sanchez! Buddy! You look great!\" Close-up, hopeful: \"...Fry?\" Sanchez's red visor stares back in silence while the fryer sizzles.",
 "s06": "Caption: One scoop later... Low angle up at the red-banded crashed dropship: Sanchez stands on the glowing roof pad, chest out, Oliver tucked under his robot arm and still chewing. Sanchez: \"This arm, I did not ask for.\" Sound: klang!",
 "s07": "Close-up: Sanchez tilts his head toward his robot arm with a small proud smile. Sanchez: \"But look at it.\" Oliver chews, deadpan. Sound: munch. Below, Sanchez's boots and Oliver's dangling bare feet on the pad as it glows brighter. Sound: a rising hum, vmmmm.",
 "s08": "The roof pad, suddenly empty: whump! Below, seen from down in a trench, Sanchez streaks overhead in a heroic flying pose, Oliver under his arm with a fry in his mouth, fries raining down toward us. Caption: heroic brass swells. Sound: fwoooosh!",
 "s09": "They land beside the nose of a crashed dropship with royal-blue bands. Caption: big heroic finish. Sound: thoom! Sanchez, chest out: \"Home.\" Below, a silent close-up of the blue band and the cockpit window, and an off-panel balloon with three dots.",
 "s10": "Oliver stares up, flat-faced: \"...That's their ship.\" The music caption is cut off: heroic bra. Below, Sanchez still holds his proud pose as something off-panel goes: fwap!",
 "s11": "Reverse view: five grinning pink stitched Huggables with bandaged heads, head radios, tall blue banners and black bear-trap jaws on their paws have snapped round toward us, arms wide for a hug, in front of the blue ship. Their radios: kssht. Jaws: clack! Sanchez, off-panel, in a tiny whisper: \"...Mayday.\"",
 "s12": "A ledger card: Scenery 1, Bears 0. Three blue lightning-bolt tokens: plink, plink, plink. Method: delivered to the wrong ship. Stamp: Real map. Fan-made news. Below, B-1000 in a small news window reports in cyan boxes: \"Kill credit: jump pad. Assist: Huggables.\" \"Next location: Steamyard Blues.\" \"Uploading... 99%\", over a progress bar stuck one segment short.",
 "s13": "Pink static with a stitched seam: kssht. Over B-1000, standing by the red ship: \"Rerouting... to: everyone.\" B-1000, in a dead-still glare: \"Tee-hee.\"",
 "s14": "B-1000's screen: \"Next location: Steamyard Blues.\" Guess the next threat level in the comments. A blank tag: \"Subject: question marks. Threat level: question marks.\" Send this to your BBG squad. Follow BBG News for Ep 2. Small print: Unofficial fan comic, not affiliated with SkyVu; characters © SkyVu.",
 "t01": "Comic cover. High over a sunny trench field, Sanchez, a teddy-bear cyborg with a glowing red visor and a huge red-and-black robot arm, flies in a superhero pose with Oliver, a brown teddy-bear soldier, tucked under his arm, hugging a basket of fries with a fry in his mouth. Gold title: We'll Getcha Home. Stamp: Nov 4. Cyan screen box: BBG News, Local Hazards. Swipe.",
 "s11 (if F2 replaces p23)": "Sanchez, with Oliver still tucked under his robot arm, freezes beside the blue ship, his red visor glow wide, as the tops of five tall blue banners, each marked with a white circle, triangle and square, rise into the bottom of the frame behind us. Radio static: kssht. Something clacks: clack! Sanchez whispers: \"...Mayday.\"",
 "t01 (if the teaser fallback is used)": "Comic cover. B-1000, a hulking maroon robot bear with glowing cyan eye-slits, a rail-gun arm and cyan claws, stands below a chunky grey crashed dropship with red bands under a bright blue sky. Title: We'll Getcha Home. Local Hazards, a BBG News fan comic, Nov 4. Swipe.",
 "t02": "B-1000, a hulking maroon robot bear with cyan eye-slits, reports live from below a crashed grey dropship with red bands: \"B-1000. Live. Scanning location.\" \"Hazard: crashed dropship.\" \"Status: still crashed.\" He shouts beside the glowing roof pad in a target ring: \"Launch pad destination: the other crashed dropship.\" Title: Local Hazards, Nov 4. Small print: Unofficial fan comic, not affiliated with SkyVu; characters © SkyVu.",
}


def fmt_letter(l):
    t = l["text"].replace("\n", " / ")
    bits = [f'**{l["type"]}** "{t}"']
    if "panel" in l:
        bits.append(f'panel {l["panel"]}')
    bits.append(f'box {l["box"]}' if "box" in l else "default placement (bottom margin)")
    if "tail" in l:
        bits.append(f'tail → {l["tail"]}')
    if "size" in l:
        bits.append(f'{l["size"]} px')
    if "angle" in l:
        bits.append(f'angle {l["angle"]}')
    if l.get("live"):
        bits.append("`live: true` (red ● LIVE tag)")
    if "font" in l:
        bits.append(f'font `{l["font"]}`')
    if "fill" in l:
        bits.append("fill `%s`%s%s" % (l["fill"], f' → `{l["fill2"]}`' if "fill2" in l else "",
                                        f', outline `{l["outline"]}`' if "outline" in l else ""))
    return "  - " + " · ".join(bits)


def fill(m):
    key = m.group(1)
    if key.startswith("PROMPT:"):
        return panels[key[7:]]["prompt"]
    if key.startswith("LETTERS:"):
        return "\n".join(fmt_letter(l) for l in PG[key[8:]]["letters"])
    if key.startswith("PANELS:"):
        return " · ".join(f'{p["id"]} {p["rect"]}' for p in PG[key[7:]]["panels"])
    if key in opt:
        return opt[key]
    if key == "ALT":
        return "\n".join(f"- **{k}:** {v}" for k, v in ALT.items())
    if key in ("P1B", "P3R", "BUILD", "LAYOUT"):
        return {"P1B": "refs/P1b_blue_hull.png", "P3R": "refs/P3r_field.png",
                "BUILD": "tools/build_assets.py", "LAYOUT": "tools/build_layout.py"}[key]
    raise KeyError(key)


text = re.sub(r"\{\{([A-Za-z0-9_:]+)\}\}", fill, tmpl)
assert "{{" not in text
for k, v in ALT.items():
    assert len(v) < 600, (k, len(v))
out.write_text(text)
print("ok", out, len(text))
