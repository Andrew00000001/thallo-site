"""Ep 1 comic: the single source of truth for the layout, lettering, crops and
panel prompts. Run it from anywhere; every path is relative to series/comic_ep1/.

Writes (in series/comic_ep1/):
  pages.json            the Nov 4 carousel, s01-s14 (deliverable)
  teaser_pages.json     the Oct 28 teaser, t01-t02 (deliverable)
  panels.json           one entry per panel: prompt, Elements, references, crop, job IDs
and, in tools/build/ (inputs for build_assets.py, fill_script.py and the face test):
  crops.json            source-pixel boxes of the approved-art crops
  mocks.json            grey mock-up shapes for the new-art panels
  pages_test.json, teaser_pages_test.json
                        the deliverables plus engine-only "faces" boxes. A crop's faces are
                        worked out from its source generation's planned faces through its
                        crop_frac, never placed by hand.
  optional_prompts.json the fallback prompts (O1, F2) for SCRIPT.md

Usage: python3 -I series/comic_ep1/tools/build_layout.py
"""
import json
from pathlib import Path

EP = Path(__file__).resolve().parents[1]
BUILD = EP / "tools" / "build"
BUILD.mkdir(parents=True, exist_ok=True)

# Approved sources (Higgsfield job IDs) and their full-resolution originals, named
# relative to the originals folder that build_assets.py takes as --src.
SOURCES = {
    "C1_still": {"what": "C1 start still", "job_id": "de69723e-8cda-438e-80ef-a21bad97e822",
                 "original": "stills/C1_still.png", "size": [1536, 2752]},
    "clip_7.0": {"what": "C1 clip, take 1, frame at 7.0 s (clean window 0-8.4 s)",
                 "job_id": "e17fe146-2939-4673-8a35-3ded5ae610a4",
                 "original": "clips/C1_take1.mp4", "size": [720, 1280], "time": 7.0},
    "P1": {"what": "plate P1, red wreck, low angle", "job_id": "15321af3-be6a-440a-8178-28ba5c6bea7f",
           "original": "plates/P1.png", "size": [1536, 2752]},
}
P2_JOB = "01ca9909-559a-4225-99f5-ad4a74c517e7"
P3_JOB = "f91003b0-68f5-4484-9963-8dac27a297ff"
P1_JOB = SOURCES["P1"]["job_id"]
P1B = "refs/P1b_blue_hull.png"
P3R = "refs/P3r_field.png"
GFX = "tools/build_assets.py"

# ---------------------------------------------------------------- prompt parts
SAN = "<<<e6122a2f-99de-423a-a310-733554bf48bb>>>"
OLI = "<<<74170e99-a46a-4c7d-857c-d3046b839374>>>"
HUG = "<<<E1>>>"
SAN_ID, OLI_ID = SAN[3:-3], OLI[3:-3]
HUG_ID = "PENDING: huggable-huggable-blue (replace E1 with its UUID once it is in SHEETS.md)"

SAN_LINE = ("A lean teddy-bear cyborg in a dark maroon helmet with rounded bear-ear bumps and an "
            "opaque glowing red visor hiding his eyes, a light tan muzzle with a small dark goatee, a "
            "grey-khaki chest plate over grey-and-white camo, olive-and-tan camo trousers, a dark grey "
            "glove on his left hand and an oversized red-and-black mechanical right arm.")
OLI_SOLO = ("A chestnut-brown robotic teddy-bear soldier, soft plush all over, with a red headband "
            "and a brass-cartridge bandolier,")
OLI_CO = ("a chestnut-brown robotic teddy-bear soldier, soft plush all over, with a red headband and "
          "a brass-cartridge bandolier, as tall as the cyborg,")
CARRY = ("tucked firmly under his mechanical right arm and hugging a softly glowing red basket of "
         "golden fried food,")
HUG_LINE = ("Five identical copies of a small stitched hot-pink plush teddy about two-thirds as tall "
            "as a teddy-bear soldier, with a big round cream-bandaged head, short stubby arms and "
            "legs, a boxy dark olive-green radio with a thin grey red-ball antenna, one glossy red "
            "button eye on its right, one small black bead eye on its left, a huge fixed toothy grin "
            "and a tall, narrow blue banner on a pole rising from its back high above its head,")
LIGHT = ("under a saturated mid-blue sky with big soft white cumulus clouds, the high sun as a "
         "slightly warm key with a soft cool fill from the sky and a gentle rim light on the characters.")
FOOD = ("A sunlit daisy-flecked grass field at high noon, beside a red-and-yellow pyramid parasol "
        "with plain, unmarked panels on a single dark pole over a squat grey cart, a softly glowing "
        "red basket of golden fried food on the grass beside it, " + LIGHT)
# The pad matches the approved art (P1 and the C1 still: a flat glowing square), not the
# package's derived "octagonal pad with a yellow-and-black hazard rim and a glowing icy-cyan
# star centre" (SCRIPT.md open item 12).
PAD = ("a flat, softly glowing pale-cyan square pad with a light-grey rim on top of its hull, "
       "faint stacked cyan rings hovering over it")
WRECK = ("beside a chunky crash-landed dark grey sci-fi transport aircraft with an olive cast, "
         "softly rounded painted-metal panels with gentle dents, {band} bands, stubby wings and three "
         "fat cylindrical engine pods, the fourth snapped off in the grass beside the nose, " + PAD +
         ", the hull clean, intact and quiet in clear, still air, short, soft, stylised yellow-green "
         "turf flecked with tiny white daisies all around, " + LIGHT)
RED = ("A sunlit grassy hilltop at high noon, at the head of a long ploughed furrow of soft "
       "orange-edged earth, " + WRECK.format(band="tomato-red"))
BLUE = "A sunlit grassy hilltop at high noon, " + WRECK.format(band="royal-blue")
FIELD = ("A sunlit open grass field at high noon, short, soft, stylised yellow-green turf flecked "
         "with tiny white daisies, plump curved arcs of tan sandbags and a few chunky black steel "
         "barriers of three thick crossed beams like giant toy jacks on gentle mounds, misty "
         "blue-grey wooded hills on the horizon, " + LIGHT)
AVOID = ("Avoid: photorealistic fur, realistic anatomy, real-person likeness, official logos, "
         "text, watermarks.")
SUFFIX = ("Polished feature-film 3D animation, soft rounded shapes, expressive faces, soft plush "
          "fur, soft global illumination, cinematic lighting, snappy cartoon timing with strong "
          "poses and holds.")
CLEAN = "left clear; a clean image with no text."
FRAME = {"4:5": "Vertical 4:5 framing.", "3:2": "Horizontal 3:2 framing.",
         "5:4": "Horizontal 5:4 framing.", "1:1": "Square 1:1 framing."}
# pixel size of a 2k download, by ratio (crop checks only; a 4k download has the same ratio)
RAW = {"4:5": (1856, 2304), "3:2": (2528, 1696), "5:4": (2304, 1856), "1:1": (2048, 2048)}


def prompt(parts, ratio):
    return " ".join(parts + [AVOID, FRAME[ratio], SUFFIX])


def ref(file_or_job, role, source_job=None):
    r = {"job_or_file": file_or_job, "role": role}
    if source_job:
        r["source_job"] = source_job
    return r


GEN = {}
GEN["G01"] = dict(panel="p01", ratio="4:5", res="2k", day="2026-10-27", els=[SAN_ID, OLI_ID],
    refs=[ref(P3R, "location reference: field, sandbags, trench zig-zag and hills (P3's right half "
              "only; the airliner-like nose is cut out). Upload it with media_upload. Run with no "
              "location reference if Bryce rejects P3r.", P3_JOB)],
    prompt=prompt([SAN, SAN_LINE, "With", OLI, OLI_CO, CARRY,
        "he soars across the sky at the top of one huge, high arc in a heroic flying pose, body "
        "stretched out level and turned three-quarters toward the camera, his gloved left fist thrust "
        "forward, chin up, mouth set firm, the glow band inside his visor narrowed, while the soldier "
        "clutches the basket to his chest with wide eyes, both brows shot up and a golden fry clamped "
        "in his mouth, a few golden fries tumbling out behind them and a few wisps of cloud whipping "
        "past them.", FIELD,
        "Medium-wide shot from high in the air, level with the two as they fly from left to right "
        "across the middle third of the frame, slightly right of centre, both faces large and clear; "
        "far below, an S-shaped zig-zag of sunken trenches with honey-gold plank floors and plain "
        "grass-capped lips crosses the field in the bottom third.",
        "The upper third of the frame is open blue sky with only soft clouds, " + CLEAN], "4:5"))
GEN["G02"] = dict(panel="p08", ratio="3:2", res="2k", day="2026-10-27", els=[OLI_ID],
    refs=[ref(P2_JOB, "location reference (P2 food stand), only once Bryce approves P2 as a "
              "reference; otherwise none")],
    prompt=prompt([OLI, OLI_SOLO,
        "sits on the grass right of centre beside the cart, frozen mid-bite with a golden fry in his "
        "mouth and another in his paw, eyes squeezed shut in bliss, cheeks stuffed full, both heavy "
        "brows lifted, the softly glowing red basket of golden fried food on the grass at his side.",
        FOOD,
        "High-angle medium shot looking down at him from above and in front, the edge of the "
        "parasol's red-and-yellow canopy cutting across the top of the frame.",
        "The left third of the frame is plain, open daisy-flecked grass with nothing in it, " + CLEAN],
        "3:2"))
GEN["G03"] = dict(panel="p10", ratio="4:5", res="4k", day="2026-10-29", els=[SAN_ID, OLI_ID],
    refs=[ref("4f2adc91-2485-423b-afdf-96ea76df244b", "continuity: Oliver, basket, stand (G02, approved)"),
          ref(P2_JOB, "location reference (P2), only if approved")],
    prompt=prompt([SAN, SAN_LINE,
        "He has just marched in from the left with both hands empty and stopped in a proud, heroic "
        "stance left of centre, turned three-quarters toward the right of the frame, beside", OLI, OLI_CO,
        "who sits on the grass beside the cart in the lower right foreground, seen from behind and to "
        "the side, frozen mid-bite beside the softly glowing red basket of golden fried food; the "
        "cyborg stands tall with his chin up in his Verdict pose, his gloved left hand flat on his chest "
        "plate and his mechanical right arm raised and pointing at the soldier, the brighter glow band "
        "inside his visor narrowed to a thin slit; his left arm is a plain furry arm in a grey-and-white "
        "camo sleeve ending in the dark grey glove, and only his right arm is the red-and-black mechanical "
        "one.", FOOD,
        "Dramatic low-angle shot from ground level in the grass behind the soldier, looking steeply up "
        "at the cyborg, who towers left of centre against the open sky, his helmet in the upper third of "
        "the frame, the soldier's back and shoulder low in the lower right corner.",
        "The top fifth of the frame above his helmet and the open sky to the right of his head are "
        "clear saturated blue sky with soft clouds and nothing else, " + CLEAN], "4:5"))
GEN["G04"] = dict(panel="p11", ratio="3:2", res="2k", day="2026-10-29", els=[OLI_ID],
    refs=[ref("4f2adc91-2485-423b-afdf-96ea76df244b", "continuity: Oliver, basket, grass")],
    prompt=prompt([OLI, OLI_SOLO,
        "sits on the grass beside the cart and looks up into the camera, cheeks stuffed full and a fry "
        "poking from his mouth, both heavy brows shot up high, flashing a wide, guilty grin that lifts "
        "on his right side, and holds a single golden fry up toward the camera in one paw, the softly "
        "glowing red basket of golden fried food on the grass at his side.", FOOD,
        "High-angle medium close-up looking down at him from a standing height, his face just below "
        "the centre of the frame and the fry raised just below his chin.",
        "The upper third of the frame is plain daisy-flecked grass with nothing in it, " + CLEAN],
        "3:2"))
GEN["G05"] = dict(panel="p14", ratio="4:5", res="2k", day="2026-10-29", els=[SAN_ID, OLI_ID],
    refs=[ref(P1_JOB, "location and dropship design reference (approved P1, red-banded wreck)"),
          ref("75d12d6d-6c6a-440f-bfdc-e94c7434ec82", "continuity: the under-arm carry and the basket"),
          ref("panels/p06.png", "the pad's look (a crop of P1, uploaded Oct 27 as media 14a3405a-0f4e-4038-9acc-85376ed7edf1); match it",
              P1_JOB)],
    prompt=prompt([SAN, SAN_LINE, "With", OLI, OLI_CO, CARRY,
        "he stands planted on the glowing pad on top of the hull after a hard stop, feet wide, chest "
        "out, chin up, mouth open on a short line, his boots lit from below by the pad's cyan glow, the "
        "soldier held against his right hip by the red-and-black mechanical arm and his gloved left hand "
        "free, while the soldier chews a fry with a flat, unimpressed look.", RED,
        "Low-angle medium shot from the head of the furrow, right up against the huge hull, looking "
        "steeply up its curved, dented flank to the roof; the hull is enormous, as long as a bus and "
        "many times taller than the bears, so only its upper flank, one fat engine pod and the edge of "
        "its roof are in frame, and the two of them stand large on the pad at the roof's edge right of "
        "centre, rim-lit against the sky, his boots, the soldier's dangling bare feet and the glowing "
        "pad clearly visible.",
        "The upper left third of the frame is open saturated blue sky with soft white clouds and "
        "nothing else, " + CLEAN], "4:5"))
GEN["G06"] = dict(panel="p15", ratio="3:2", res="2k", day="2026-10-30", els=[SAN_ID, OLI_ID],
    refs=[ref("p14 (G05, its job ID once approved)", "continuity: same pad, hull and carry")],
    prompt=prompt([SAN, SAN_LINE, "With", OLI, OLI_CO, CARRY,
        "he stands on the glowing pad on top of the hull and tilts his head toward his mechanical arm "
        "as a small closed-mouth smile lifts his goatee, the glow band inside his visor widening, "
        "while the soldier chews a fry, cheeks full, with a flat, deadpan stare.", RED,
        "Medium close-up at eye level on top of the hull, the cyborg's head right of centre and the "
        "soldier's head lower left, both faces large in frame.",
        "The upper left corner of the frame is open saturated blue sky with nothing in it, " + CLEAN],
        "3:2"))
GEN["G07"] = dict(panel="p19", ratio="5:4", res="4k", day="2026-10-28", els=[SAN_ID, OLI_ID],
    refs=[ref(P1B, "dropship design reference: approved P1 recoloured locally to royal-blue bands, so "
              "the blue wreck stays P1's chunky cartoon dropship (not P3's airliner nose). Upload it "
              "with media_upload", P1_JOB),
          ref("75d12d6d-6c6a-440f-bfdc-e94c7434ec82", "continuity: the carry, the basket, both faces"),
          ref(P3R, "field reference, approved Oct 26 as a reference only; uploaded as media 5cc57baa-2499-4e2e-9447-c353469da317", P3_JOB)],
    prompt=prompt([SAN, SAN_LINE, "With", OLI, OLI_CO, CARRY,
        "he has just landed on the grass beside the hull with a squash on bent knees and snapped up "
        "into a hard hold, chest out, chin up, his gloved left fist on his hip, mouth open on one "
        "word, a small soft puff of dust settling at his boots, while the soldier stares up at the "
        "hull's royal-blue bands, his smirk gone flat and his brows down.", BLUE,
        "Low wide shot from the open grass beside the hull's blunt nose, the nose with its cockpit "
        "window, twin round headlamps and royal-blue bands filling the right half of the frame, the "
        "two of them standing on the grass left of centre with both faces large and clear and "
        "turned three-quarters toward the camera.",
        "The upper left third of the frame and the sky above the hull's nose in the top quarter of "
        "the frame are open saturated blue sky with soft white clouds, " + CLEAN], "5:4"))
GEN["G08"] = dict(panel="p23", ratio="4:5", res="2k", day="2026-10-29", els=[HUG_ID],
    refs=[ref("panels/p20.png", "continuity: the blue hull's nose, turf and light (no characters). "
              "A crop of the approved G07; upload it with media_upload"),
          ref(P1B, "dropship design reference (blue-banded P1 recolour)", P1_JOB)],
    prompt=prompt([HUG, HUG_LINE,
        "have snapped around toward the camera in perfect unison, each with its cream bandage, olive "
        "radio, stitched scar and red button eye on the viewer's left and its bare ear and small black "
        "bead eye on the viewer's right, and lean in on their toes with their arms forward and wide in "
        "a hug pose, oversized black bear-trap jaws on all their paws, the red balls on their antennas "
        "glowing together and their banners whipping above their heads, their grins fixed and their "
        "teeth together.", BLUE,
        "Locked-off medium shot at low eye level, the five in a loose, staggered row on the open turf "
        "in front of the hull's blunt nose, the hull filling the upper middle of the frame behind "
        "them.",
        "The top fifth of the frame is open blue sky above the banner tops and the bottom fifth is "
        "plain, empty turf, " + CLEAN], "4:5"))
GEN["G09"] = dict(panel="p18", ratio="1:1", res="2k", day="2026-10-29", els=[SAN_ID, OLI_ID],
    refs=[ref("75d12d6d-6c6a-440f-bfdc-e94c7434ec82", "continuity: the under-arm carry, the basket, "
              "both faces"),
          ref(P3R, "field reference, approved Oct 26 as a reference only; uploaded as media 5cc57baa-2499-4e2e-9447-c353469da317", P3_JOB)],
    prompt=prompt([SAN, SAN_LINE, "With", OLI, OLI_CO, CARRY,
        "he flies across the sky in one huge, high arc in a heroic flying pose, body stretched out "
        "level, his gloved left fist thrust forward, chin up, mouth set firm, the glow band inside his "
        "visor narrowed, while the soldier clutches the basket to his chest with wide eyes, both brows "
        "shot up and a golden fry clamped in his mouth.", FIELD,
        "Low-angle shot from inside a sunken trench with honey-gold plank floors and plain grass-capped lips, looking up as the "
        "two streak overhead from left to right, faces turned down toward the camera, fries raining "
        "toward the lens.",
        "The top-left quarter of the frame is open blue sky, " + CLEAN], "1:1"))

# ---------------------------------------------------------------- fallbacks (SCRIPT.md only)
OPTIONAL = {
 "O1": prompt([OLI, OLI_SOLO,
    "hugs a softly glowing red basket of golden fried food and stares flatly up toward the right of "
    "the frame, his smirk gone flat, brows down, eyes half-lidded in deadpan realisation, tucked "
    "under the arm of", SAN, "a" + SAN_LINE[1:-1] + ", his head above the top of the frame.", BLUE,
    "Low-angle close-up of the soldier's head and shoulders right of centre, behind him the hull's "
    "olive-cast dark grey painted side with one broad royal-blue band running across it.",
    "The upper left third of the frame is the hull's plain painted side, " + CLEAN], "5:4"),
 "F2": prompt([SAN, SAN_LINE, "With", OLI, OLI_CO, CARRY,
    "he freezes in his hard hold beside the hull, the glow band inside his visor widened to fill the "
    "visor, his mouth a small flat line, while the soldier's brows shoot up, as the tops of five "
    "tall, narrow blue cloth banners on thin dark grey poles, each marked with a white circle, a "
    "triangle and a square stacked top to bottom, rise into the bottom edge of the frame in the "
    "soft-focus foreground.", BLUE,
    "Locked-off medium shot at low eye level, facing the two with the hull's blunt nose behind them.",
    "The upper left third of the frame is open saturated blue sky, " + CLEAN], "4:5"),
}

# ---------------------------------------------------------------- layout
# panel kinds: 'gen' (Gxx shown whole) | 'crop' (of Gxx, crop_frac) | 'reuse' (approved art,
# crop_px) | 'gfx' (local original art). Faces on 'gen' panels are planned positions in canvas
# px (from each prompt's composition); faces on 'crop' panels are derived, never hand-placed.
PAGES = []


def page(pid, panels, letters, teaser=False):
    PAGES.append({"id": pid, "panels": panels, "letters": letters, "teaser": teaser})


def P(pid, rect, focus=(0.5, 0.5), border=6, **meta):
    return {"id": pid, "rect": list(rect), "image": f"panels/{pid}.png", "focus": list(focus),
            "border": border, "_meta": meta}


def L(type_, text, panel=None, box=None, tail=None, size=None, angle=None, **extra):
    d = {"type": type_, "text": text}
    if panel:
        d["panel"] = panel
    if box:
        d["box"] = list(box)
    if tail:
        d["tail"] = list(tail)
    if size:
        d["size"] = size
    if angle is not None:
        d["angle"] = angle
    d.update(extra)
    return d


# engine extras (documented keys of series/comic/letter.py)
PINK = dict(fill="#ff6fb5", fill2="#d6337f", outline="#2a0a1a")     # both KSSHTs: hijacker clue
STAMP = dict(fill="#d7263d", outline="#f4f1e8")                       # REAL MAP. FAN-MADE NEWS.
STING = dict(font="rounded-black")                                    # slate: original rounded lettering

# s01 cover
page("s01", [P("p01", (40, 40, 1000, 1270), border=0, kind="gen", gen="G01",
               faces=[(560, 250, 200, 200, "S"), (400, 410, 175, 185, "O")])],
     [L("hud", "BBG NEWS · LIVE\nLOCAL HAZARDS · EP 1", "p01", (64, 58, 470), size=34),
      L("hud", "DESTINATION: HOME?", "p01", (64, 790, 420), (520, 640), size=34),
      L("title", "WE'LL GETCHA", "p01", (90, 955, 900)),
      L("title", "HOME", "p01", (330, 1092, 420)),
      L("hud", "SWIPE >>", "p01", (810, 1240, 200), size=30)])

# s02 cold open (stands alone if Instagram re-serves the carousel from slide 2)
page("s02", [P("p02", (40, 40, 1000, 640), kind="reuse", src="C1_still", box=(0, 740, 1536, 1723),
               faces=[(440, 352, 116, 136, "B")]),
             P("p03", (40, 700, 490, 280), kind="reuse", src="C1_still", box=(280, 820, 1336, 1423)),
             P("p04", (550, 700, 490, 280), kind="reuse", src="C1_still", box=(280, 820, 1336, 1423)),
             P("p05", (40, 1000, 330, 310), kind="reuse", src="clip_7.0", box=(170, 320, 550, 677),
               faces=[(120, 1070, 140, 150, "B")]),
             P("p06", (390, 1000, 650, 310), kind="reuse", src="P1", box=(280, 800, 1070, 1177))],
     [L("hud", "B-1000. LIVE.\nSCANNING LOCATION.", "p02", (64, 64, 450), (498, 396), size=36,
        live=True),
      L("hud", "HAZARD:\nCRASHED DROPSHIP.", "p03", (56, 714, 400), (430, 846), size=32),
      L("hud", "STATUS:\nSTILL CRASHED.", "p04", (566, 714, 400), (940, 846), size=32),
      L("hud", "LAUNCH PAD DESTINATION:\nTHE OTHER CRASHED DROPSHIP.", "p06", (404, 1014, 620),
        (774, 1200), size=32)])

# s03 sting, Oliver, the red visor arriving
page("s03", [P("p07", (40, 40, 1000, 200), kind="gfx", gfx="sting band: navy HUD grid, scan line"),
             P("p08", (40, 260, 1000, 700), focus=(0.55, 0.5), kind="gen", gen="G02",
               faces=[(590, 490, 200, 200, "O")]),
             P("p09", (40, 980, 1000, 330), kind="crop", gen="G03", crop=(0.16, 0.16, 0.92, 0.36),
               note="the glowing visor (left third) and the raised red-and-black arm reaching right; "
                    "crop at 1000:330")],
     [L("title", "LOCAL HAZARDS", "p07", (70, 70, 700), **STING),
      L("sfx", "DUN-DUNN!", "p07", (790, 130, 220), angle=6),
      L("caption", "The red food stand.", "p08", (64, 282, 560), size=34),
      L("hud", "SUBJECT: OLIVER\nTHREAT LEVEL: FLUFFY", "p08", (64, 350, 450), (640, 500), size=34),
      L("sfx", "CRUNCH!", "p08", (90, 740, 360), angle=8),
      L("sfx", "KA-CHUNK!", "p09", (610, 1150, 400), angle=-6)])

# s04 the Verdict
page("s04", [P("p10", (40, 40, 1000, 1270), kind="gen", gen="G03",
               faces=[(340, 300, 165, 170, "S"), (700, 1000, 190, 180, "O-back")])],
     [L("hud", "SUBJECT: SANCHEZ\nTHREAT LEVEL:\nPARTIAL UPGRADE", "p10", (64, 64, 380), (420, 304),
        size=34),
      L("balloon", "Oliver, we'll getcha...", "p10", (440, 70, 470), (512, 418), size=44),
      L("balloon", "...**home.**", "p10", (660, 270, 300), (516, 446), size=56)])

# s05 the fry offer, "...Fry?", the silent visor
page("s05", [P("p11", (40, 40, 1000, 640), focus=(0.5, 0.55), kind="gen", gen="G04",
               faces=[(465, 330, 190, 190, "O")]),
             P("p12", (40, 700, 490, 610), kind="crop", gen="G04", crop=(0.284, 0.12, 0.757, 0.998),
               note="his face and the raised fry, crop at 490:610"),
             P("p13", (550, 700, 490, 610), kind="crop", gen="G03", crop=(0.31, 0.14, 0.46, 0.29),
               note="tight on the helmet and the glowing visor (glow band narrowed), cut above the "
                    "mouth so the panel reads silent; crop at 490:610")],
     [L("balloon", "Sanchez! Buddy! You look **GREAT!**", "p11", (64, 56, 440), (458, 470), size=44),
      L("balloon", "...**FRY?**", "p12", (64, 718, 280), (250, 940), size=52),
      L("sfx", "SSSSZZZ...", "p13", (690, 722, 330), angle=4)])

# s06 up the wreck: the solemn half of the line
page("s06", [P("p14", (40, 40, 1000, 1270), kind="gen", gen="G05",
               faces=[(580, 380, 160, 160, "S"), (470, 510, 140, 140, "O")])],
     [L("caption", "One scoop later...", "p14", (64, 64, 400), size=38),
      L("balloon", "This arm, I did not ask for.", "p14", (64, 150, 470), (574, 470), size=46),
      L("sfx", "KLANG!", "p14", (640, 880, 360), angle=-8)])

# s07 "But LOOK at it." and the pad starting to hum
page("s07", [P("p15", (40, 40, 1000, 680), kind="gen", gen="G06",
               faces=[(570, 212, 200, 200, "S"), (210, 455, 180, 180, "O")]),
             P("p16", (40, 740, 1000, 570), kind="crop", gen="G05", crop=(0.20, 0.49, 0.95, 0.834),
               note="Sanchez's boots and Oliver's dangling bare feet on the glowing pad, crop at "
                    "1000:570")],
     [L("balloon", "But **LOOK** at it.", "p15", (64, 60, 400), (564, 330), size=50),
      L("sfx", "MUNCH", "p15", (430, 600, 240), angle=-10),
      L("sfx", "VMMMMMMMMM", "p16", (64, 1100, 940), angle=4)])

# s08 the launch: empty pad, then the arc seen from the trench (G09)
page("s08", [P("p17", (40, 40, 1000, 300), kind="reuse", src="P1", box=(0, 830, 1536, 1291)),
             P("p18", (40, 360, 1000, 950), kind="gen", gen="G09",
               faces=[(560, 600, 160, 160, "S"), (410, 720, 150, 150, "O")])],
     [L("sfx", "WHUMP!", "p17", (84, 92, 340), angle=8),
      L("caption", "~ Heroic brass swells ~", "p18", (64, 384, 480), size=36),
      L("sfx", "FWOOOOOSH!", "p18", (64, 1100, 620), angle=8)])

# s09 the landing: "HOME." and a silent blue band
page("s09", [P("p19", (40, 40, 1000, 800), kind="gen", gen="G07",
               faces=[(126, 293, 154, 145, "S"), (335, 428, 150, 118, "O")]),
             P("p20", (40, 860, 1000, 450), kind="crop", gen="G07", crop=(0.56, 0.35, 1.00, 0.596),
               note="the nose: one royal-blue band and the cockpit window, no faces, crop at 1000:450")],
     [L("caption", "~ Big heroic finish ~", "p19", (64, 64, 480), size=34),
      L("balloon", "**HOME.**", "p19", (310, 214, 270), (262, 405), size=58),
      L("sfx", "THOOM!", "p19", (330, 742, 360), angle=-6),
      L("balloon", "...", "p20", (80, 1110, 150), (20, 1215), size=48)])

# s10 the punchline, and something flaps
page("s10", [P("p21", (40, 40, 1000, 800), kind="crop", gen="G07", crop=(0.255, 0.38, 0.555, 0.678),
               note="Oliver's head and shoulders under open sky, staring flat at the hull; crop at 1000:800"),
             P("p22", (40, 860, 1000, 450), kind="crop", gen="G07", crop=(0.00, 0.30, 0.40, 0.5234),
               note="Sanchez chest-up, still in his proud hold; crop at 1000:450")],
     [L("balloon", "...That's **THEIR** ship.", "p21", (64, 64, 440), (560, 560), size=48),
      L("caption", "~ Heroic bra--", "p21", (64, 744, 320), size=34),
      L("sfx", "FWAP!", "p22", (780, 1150, 210), angle=-10)])

# s11 the reverse (the swipe is the hard cut)
page("s11", [P("p23", (40, 40, 1000, 1270), kind="gen", gen="G08",
               faces=[(85, 580, 150, 150, "H"), (265, 560, 150, 150, "H"), (465, 600, 150, 150, "H"),
                      (665, 560, 150, 150, "H"), (845, 580, 150, 150, "H")])],
     [L("sfx", "KSSHT", "p23", (190, 84, 440), angle=4, **PINK),
      L("sfx", "CLACK!", "p23", (64, 1110, 330), angle=-8),
      L("whisper", "...Mayday.", "p23", (560, 1150, 400), (800, 1304), size=38)])

# s12 the ledger and the upload
page("s12", [P("p24", (40, 40, 1000, 560), kind="gfx", gfx="ledger card: slate, gold rule, three "
               "Joule-style tokens at right"),
             P("p25", (40, 620, 420, 690), kind="reuse", src="clip_7.0", box=(100, 280, 580, 1068),
               faces=[(175, 715, 145, 150, "B")]),
             P("p26", (480, 620, 560, 690), kind="gfx", gfx="upload screen: navy HUD grid, "
               "segmented bar frozen one segment short (the last segment hollow)")],
     [L("title", "SCENERY 1 · BEARS 0", "p24", (110, 66, 830)),
      L("sfx", "PLINK! PLINK! PLINK!", "p24", (80, 226, 600), angle=3),
      L("caption", "Method: delivered to the **wrong ship**", "p24", (80, 372, 920), size=38),
      L("sfx", "REAL MAP. FAN-MADE NEWS.", "p24", (300, 474, 680), angle=-5, **STAMP),
      L("hud", "KILL CREDIT: JUMP PAD.\nASSIST: HUGGABLES.", "p26", (500, 642, 520), (248, 760),
        size=34),
      L("hud", "NEXT LOCATION:\nSTEAMYARD BLUES.", "p26", (500, 800, 520), size=34),
      L("hud", "UPLOADING... 99%", "p26", (500, 1080, 420), size=36)])

# s13 rerouting, tee-hee
page("s13", [P("p27", (40, 40, 1000, 300), kind="gfx", gfx="pink static with the Huggable's "
               "stitched chest seam"),
             P("p28", (40, 360, 1000, 950), kind="reuse", src="C1_still", box=(290, 1080, 1090, 1840),
               faces=[(462, 545, 195, 250, "B")])],
     [L("sfx", "KSSHT", "p27", (270, 96, 540), angle=-4, **PINK),
      L("hud", "REROUTING...\nTO: EVERYONE", "p28", (64, 384, 420), size=40),
      L("hud", "TEE-HEE.", "p28", (700, 560, 300), (612, 640), size=48)])

# s14 end card and call to action
page("s14", [P("p29", (40, 40, 1000, 1160), kind="gfx", gfx="B-1000's HUD screen: navy grid, "
               "scan line")],
     [L("hud", "NEXT LOCATION:\nSTEAMYARD BLUES.", "p29", (90, 100, 900), size=50),
      L("caption", "Guess the next **THREAT LEVEL** in the comments.", "p29", (90, 360, 900),
        size=46),
      L("hud", "SUBJECT: ???\nTHREAT LEVEL: ???", "p29", (260, 610, 560), size=46),
      L("caption", "Send this to your BBG squad.\nFollow BBG News for Ep 2.", "p29", (90, 870, 900),
        size=44),
      L("endcard", "Unofficial fan comic, not affiliated with SkyVu; characters © SkyVu.")])

# t01, t02: the Oct 28 teaser (a 2-slide carousel, teaser_pages.json)
page("t01", [P("t01a", (40, 40, 1000, 1270), border=0, kind="crop", gen="G01",
               crop=(0.060, 0.100, 0.940, 1.000),
               note="the cover zoomed about 1.14x, anchored at the bottom so the title sits on the field "
                    "below the pair and the Oct 28 and Nov 4 grid tiles differ; crop at 1000:1270")],
     [L("hud", "BBG NEWS · LOCAL HAZARDS", "t01a", (64, 64, 430), size=32),
      L("title", "WE'LL GETCHA", "t01a", (90, 930, 900)),
      L("title", "HOME", "t01a", (330, 1067, 420)),
      L("sfx", "NOV 4", "t01a", (700, 770, 300), angle=8),
      L("hud", "SWIPE >>", "t01a", (810, 1240, 200), size=30)], teaser=True)
page("t02", [P("t02a", (40, 40, 1000, 560), kind="reuse", src="C1_still", box=(0, 800, 1536, 1660),
               faces=[(440, 315, 116, 136, "B")]),
             P("t02b", (40, 620, 490, 240), kind="reuse", src="C1_still", box=(280, 880, 1336, 1398)),
             P("t02c", (550, 620, 490, 240), kind="reuse", src="C1_still", box=(280, 880, 1336, 1398)),
             P("t02d", (40, 880, 330, 250), kind="reuse", src="clip_7.0", box=(150, 330, 570, 648),
               faces=[(125, 930, 125, 130, "B")]),
             P("t02e", (390, 880, 650, 250), kind="reuse", src="P1", box=(230, 830, 1130, 1176))],
     [L("hud", "B-1000. LIVE.\nSCANNING LOCATION.", "t02a", (64, 60, 440), (498, 356), size=34,
        live=True),
      L("hud", "HAZARD:\nCRASHED DROPSHIP.", "t02b", (56, 632, 400), (420, 745), size=32),
      L("hud", "STATUS:\nSTILL CRASHED.", "t02c", (566, 632, 400), (930, 745), size=32),
      L("hud", "LAUNCH PAD DESTINATION:\nTHE OTHER CRASHED DROPSHIP.", "t02e", (404, 892, 620),
        (763, 1040), size=32),
      L("title", "LOCAL HAZARDS · NOV 4", None, (60, 1150, 960), **STING),
      L("endcard", "Unofficial fan comic, not affiliated with SkyVu; characters © SkyVu.")],
     teaser=True)

# generations already made (job IDs and status; Oct 27)
DONE = {
    "G01": {"job_id": "75d12d6d-6c6a-440f-bfdc-e94c7434ec82",
            "status": "approved: Oct 28 edit of take 1 (9daa8018) mirrored locally, smoke removed and barriers black",
            "rejected": ["1f7dc7cd-f277-4d3e-9cfd-d77abced45af (take 2: pair still high, Oliver under the wrong arm)"]},
    "G02": {"job_id": "4f2adc91-2485-423b-afdf-96ea76df244b", "status": "approved"},
    "G03": {"job_id": None, "status": "todo (Oct 27 try 4a6cf631 flagged by the filter, refunded; Oct 28 take rejected; v3 Oct 29)",
            "rejected": ["4a6cf631-2ef6-4d23-96e0-5b3920f1ceef (Oct 27, content filter, refunded)",
                         "1e4697a7-6c79-49b0-b0b4-4dbe9c83e144 (Oct 28: both arms drawn mechanical; eye-level, not the low-angle Verdict)"]},
    "G05": {"job_id": None, "status": "todo (Oct 28 take rejected; v2 Oct 29)",
            "rejected": ["d85aeea7-b5f3-4b5a-9b1b-5f8195936da7 (Oct 28: the wreck drawn toy-sized under the bears; Oliver under the gloved arm)"]},
    "G07": {"job_id": "56882afc-79c0-44c9-97a0-0d00b9c0aee7",
            "status": "approved (Oliver lands standing beside Sanchez, not carried; crops p20-p22 re-fit Oct 28)"},
}


# ---------------------------------------------------------------- checks and derived faces
RECT = {pn["id"]: pn["rect"] for pg in PAGES for pn in pg["panels"]}
META = {pn["id"]: pn for pg in PAGES for pn in pg["panels"]}


def cover_view(rw, rh, rect, focus):
    """The source window (left, top, scale) that letter.py's cover-fit shows in rect."""
    _, _, w, h = rect
    s = max(w / rw, h / rh)
    vw, vh = w / s, h / s
    left = min(max(focus[0] * rw - vw / 2, 0), rw - vw)
    top = min(max(focus[1] * rh - vh / 2, 0), rh - vh)
    return left, top, s


def faces_in_source(gen_id):
    """Planned faces of a generation as source fractions (x0, y0, x1, y1, label)."""
    g = GEN[gen_id]
    pn = META[g["panel"]]
    rw, rh = RAW[g["ratio"]]
    left, top, s = cover_view(rw, rh, pn["rect"], pn["focus"])
    rx, ry = pn["rect"][:2]
    out = []
    for x, y, w, h, lab in pn["_meta"].get("faces", []):
        out.append(((left + (x - rx) / s) / rw, (top + (y - ry) / s) / rh,
                    (left + (x + w - rx) / s) / rw, (top + (y + h - ry) / s) / rh, lab))
    return out


def derived_faces(pn):
    """A crop panel's faces: its source generation's faces mapped through crop_frac."""
    m = pn["_meta"]
    cx0, cy0, cx1, cy1 = m["crop"]
    rx, ry, w, h = pn["rect"]
    out = []
    for x0, y0, x1, y1, lab in faces_in_source(m["gen"]):
        X0 = rx + (x0 - cx0) / (cx1 - cx0) * w
        X1 = rx + (x1 - cx0) / (cx1 - cx0) * w
        Y0 = ry + (y0 - cy0) / (cy1 - cy0) * h
        Y1 = ry + (y1 - cy0) / (cy1 - cy0) * h
        X0, X1 = max(X0, rx), min(X1, rx + w)
        Y0, Y1 = max(Y0, ry), min(Y1, ry + h)
        if X1 - X0 > 12 and Y1 - Y0 > 12:
            out.append((round(X0), round(Y0), round(X1 - X0), round(Y1 - Y0), lab))
    return out


for pg in PAGES:
    for pn in pg["panels"]:
        m = pn["_meta"]
        if m["kind"] == "crop":
            g = GEN[m["gen"]]
            rw, rh = RAW[g["ratio"]]
            x0, y0, x1, y1 = m["crop"]
            assert 0 <= x0 < x1 <= 1 and 0 <= y0 < y1 <= 1, pn["id"]
            r = (x1 - x0) * rw / ((y1 - y0) * rh)
            rr = pn["rect"][2] / pn["rect"][3]
            assert abs(r - rr) / rr < 0.02, (pn["id"], r, rr)
            m["faces"] = derived_faces(pn)

# ---------------------------------------------------------------- outputs
crops, mocks, panels = {}, {}, []

for pg in PAGES:
    for pn in pg["panels"]:
        m, pid, (x, y, w, h) = pn["_meta"], pn["id"], pn["rect"]
        ar = f"{w}:{h}"
        if m["kind"] == "reuse":
            src = SOURCES[m["src"]]
            crops[pid] = {"src": m["src"], "box": list(m["box"]), "rect": [w, h]}
            rs = {"source": src["what"], "job_id": src["job_id"], "original": src["original"],
                  "original_size": src["size"]}
            if "time" in src:
                rs["time"] = src["time"]
            rs["crop_px"] = list(m["box"])
            panels.append({"id": pid, "slide": pg["id"], "aspect_ratio": ar,
                           "resolution": "reuse, 0 credits", "prompt": None, "elements": [],
                           "references": [], "reuse_source": rs, "day": "2026-10-26",
                           "status": "cut"})
        elif m["kind"] == "gfx":
            panels.append({"id": pid, "slide": pg["id"], "aspect_ratio": ar,
                           "resolution": "local original-art graphic, 0 credits", "prompt": None,
                           "elements": [], "references": [],
                           "reuse_source": {"file": GFX, "graphic": m["gfx"]},
                           "day": "2026-10-26", "status": "built"})
        elif m["kind"] == "gen":
            g = GEN[m["gen"]]
            panels.append({"id": pid, "slide": pg["id"], "gen": m["gen"], "aspect_ratio": g["ratio"],
                           "resolution": g["res"], "prompt": g["prompt"], "elements": g["els"],
                           "references": g["refs"], "reuse_source": None,
                           "raw_download": f"src/{pid}_raw.png",
                           "job_id": DONE.get(m["gen"], {}).get("job_id"), "day": g["day"],
                           "status": DONE.get(m["gen"], {}).get("status", "todo"),
                           **({"rejected": DONE[m["gen"]]["rejected"]} if "rejected" in DONE.get(m["gen"], {}) else {})})
        elif m["kind"] == "crop":
            g = GEN[m["gen"]]
            panels.append({"id": pid, "slide": pg["id"], "aspect_ratio": ar,
                           "resolution": f"crop of {m['gen']} ({g['res']}), 0 credits",
                           "prompt": None, "elements": [], "references": [],
                           "reuse_source": {"file": f"src/{g['panel']}_raw.png",
                                            "crop_frac": list(m["crop"]),
                                            "from": f"{m['gen']}: the full approved download of "
                                                    f"{g['panel']}'s generation",
                                            "note": m["note"]},
                           "day": g["day"], "status": "todo"})
        if m["kind"] in ("gen", "crop"):
            mocks[pid] = {"rect": [x, y, w, h], "note": f"{m['kind']} {m['gen']}",
                          "shapes": [list(f) for f in m.get("faces", [])]}


def pages_doc(teaser, faces=False):
    doc = {"canvas": [1080, 1350], "background": "#0d0d10", "pages": []}
    for pg in PAGES:
        if pg["teaser"] != teaser:
            continue
        pans = []
        for pn in pg["panels"]:
            d = {k: v for k, v in pn.items() if k != "_meta"}
            if faces and pn["_meta"].get("faces"):
                d["faces"] = [list(b[:4]) for b in pn["_meta"]["faces"]]
            pans.append(d)
        doc["pages"].append({"id": pg["id"], "panels": pans, "letters": pg["letters"]})
    return doc


J = lambda o: json.dumps(o, ensure_ascii=False, separators=(", ", ": "))


def write_pages(doc, path):
    """Compact, diff-friendly: one panel or letter per line."""
    out = ['{"canvas": %s, "background": %s,' % (J(doc["canvas"]), J(doc["background"])), ' "pages": [']
    for i, pg in enumerate(doc["pages"]):
        out.append('  {"id": %s,' % J(pg["id"]))
        out.append('   "panels": [')
        out += ['    ' + J(p) + (',' if k < len(pg["panels"]) - 1 else '') for k, p in enumerate(pg["panels"])]
        out.append('   ],')
        out.append('   "letters": [')
        out += ['    ' + J(l) + (',' if k < len(pg["letters"]) - 1 else '') for k, l in enumerate(pg["letters"])]
        out.append('   ]}' + (',' if i < len(doc["pages"]) - 1 else ''))
    out.append(' ]}')
    path.write_text("\n".join(out) + "\n")
    assert json.loads(path.read_text()) == doc


def write_panels(lst, path):
    """One key per line, arrays and objects inline."""
    out = ["["]
    for i, e in enumerate(lst):
        keys = list(e)
        out.append(" {")
        for k_i, k in enumerate(keys):
            out.append("  %s: %s%s" % (J(k), J(e[k]), "," if k_i < len(keys) - 1 else ""))
        out.append(" }" + ("," if i < len(lst) - 1 else ""))
    out.append("]")
    path.write_text("\n".join(out) + "\n")
    assert json.loads(path.read_text()) == lst


def dump(obj, path):
    path.write_text(json.dumps(obj, indent=1, ensure_ascii=False) + "\n")


write_pages(pages_doc(False), EP / "pages.json")
write_pages(pages_doc(True), EP / "teaser_pages.json")
write_panels(panels, EP / "panels.json")
dump(pages_doc(False, faces=True), BUILD / "pages_test.json")
dump(pages_doc(True, faces=True), BUILD / "teaser_pages_test.json")
dump(crops, BUILD / "crops.json")
dump(mocks, BUILD / "mocks.json")
dump(OPTIONAL, BUILD / "optional_prompts.json")

# counts
gens = [p for p in panels if p["prompt"]]
cred = sum(4 if p["resolution"] == "4k" else 2 for p in gens)
carousel = [pg for pg in PAGES if not pg["teaser"]]
teaser = [pg for pg in PAGES if pg["teaser"]]
print("slides", len(carousel), "+ teaser", len(teaser), "| panels", len(panels),
      "(carousel", sum(len(pg["panels"]) for pg in carousel), "teaser",
      sum(len(pg["panels"]) for pg in teaser), ") | new generations", len(gens), "credits", cred)
print("free: crops of new art", sum(1 for pg in PAGES for pn in pg["panels"] if pn["_meta"]["kind"] == "crop"),
      "| crops of approved art", len(crops),
      "| local graphics", sum(1 for pg in PAGES for pn in pg["panels"] if pn["_meta"]["kind"] == "gfx"))
for pg in PAGES:
    words = sum(len(l["text"].replace("\n", " ").replace("**", "").split()) for l in pg["letters"]
                if l["type"] != "endcard")
    print(pg["id"], "panels", len(pg["panels"]), "words", words,
          "| derived faces:", {pn["id"]: pn["_meta"]["faces"] for pn in pg["panels"]
                               if pn["_meta"]["kind"] == "crop"} or "-")
