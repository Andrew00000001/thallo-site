# BBG News: LOCAL HAZARDS · Ep 1 "We'll Getcha Home": production package

*Unofficial BBG News fan short. Package v1, 2026-10-20. Built from the locked slate (`series/season1_slate.md`, §2, §3 Ep 1, §4, §5), the souls `b-1000.md`, `sanchez.md`, `oliver.md` and `huggable.md`, `STYLE.md`, the characters `README.md`, `sheets/SHEETS.md` and `environments/no-bear-s-land.md`. Labels follow the README legend and are never upgraded. Anything not labelled otherwise is [BBG News invention].*

**Status: nothing has been generated. Five things block generation; see §0.** Release: teaser (C1) Wed Oct 28, episode locked Sun Nov 1, posted Wed Nov 4 (launch day).

---

## 0. Before anything is generated (blockers found 2026-10-20)

**Status on 2026-10-22:**
- Blocker 1: the low-poly Elements are gone. New Elements are made from the house-style sheets only after an independent review panel passes them (SHEETS.md). `sanchez-arbiter` is live; B-1000 and Oliver follow their Oct 23 fixes.
- Blocker 2 is done: Sanchez's sheet passed and his Element is live.
- Blocker 3: the Huggable fix is queued for Oct 24, with the blue sheet after it.
- Blocker 4 is done: Bryce approved AI voices and left the casting to BBG News. Cast: Orion (B-1000), Jasper (Sanchez), John (Oliver); see `voice_casting.md`.
- Blocker 5: B-1000 now has no hands. His head (pointed plated ears, jaw plate) is fixed on Oct 23.

The teaser path:
- Oct 23: B-1000's sheet, plate P1 and B-1000's voice lines.
- Oct 24: the C1 start still and clip.
- Oct 25-27: a C1 retake if needed, and the dub and edit.

Higgsfield's 5-a-day generation limit sets this pace.

**Status on 2026-10-24:**
- The C1 start still passed (job de69723e). The C1 clip, take 1, passed its checklist on the 0-8.4 s window (Seedance job e17fe146, 45 credits). From about 8.7 s the claws fan out.
- The draft teaser is in `ep1_edit/teaser_draft_v1.mp4`, waiting on Bryce's review.
- Voices:
  - B-1000: all lines done.
  - Sanchez: 3 of 5 lines done; "But look at it." and "Home." are retaken Oct 25.
  - Oliver: 2 of 3 lines done; C4 is retaken Oct 25.
- The B-1000 Element is live. Oliver's waits for his review panel. The Huggable needs a fresh sheet before C5's blue sheet.

**Status on 2026-10-25:**
- Elements:
  - `oliver-soldier` is live (74170e99); the review panel rated his sheet usable.
  - Live now: Sanchez, B-1000 and Oliver, so every C2-C4 character has an Element.
- The fresh Huggable sheet failed: the radio went to its left, apart from the button eye. Sheet v4 runs Oct 26 with every sided feature in viewer terms. C5 waits on it and then on the blue sheet.
- Voices:
  - B-1000's "Tee-hee" is picked.
  - Sanchez's "But LOOK at it!" now lifts.
  - Jasper failed "Home" a second time and Fraser passed it, so Fraser records the full Sanchez set on Oct 26 for a whole-set comparison.
  - Oliver's C4 came out breathy again; three variants run Oct 26.
- Oct 26 runs P3 (C4 is the riskiest shot) and P2. P4 and the C4 and C2 start stills follow Oct 27.
- Credits: 106.12.


1. **The Higgsfield Elements are still the old low-poly ones.** A read-only listing of the workspace on 2026-10-20 shows `oliver-soldier` (5e079b47…), `huggable-huggable` (e188dc42…) and `riggs-heavy` (1475a232…), all created on Oct 15 from the retired low-poly sheets (their descriptions say "low-poly"). No Element has been made from any SHEETS.md sheet, and there is no `b-1000-assault-signature` Element at all.
   - Create the new Elements from the SHEETS.md jobs (type `image_job`): B-1000 from the fixed sheet once blocker 5 clears (the current sheet is `1f7259ce-23ed-4398-9a91-cdbf429dfeed`; use it only under Bryce's recorded exception), Oliver `909ea0bd-843e-4324-ae88-193c2eeb84cb`; Sanchez and the blue Huggable once their sheets pass QA. Creating an Element cost nothing on Oct 15.
   - Names are unique per workspace, and a clash gets a numeric suffix. **Bryce's call (open item 1):** delete or rename the low-poly Elements in the Higgsfield web UI first (the MCP tool can list and create Elements, not delete or rename them), or accept suffixed names. Either way, write each new Element's UUID into SHEETS.md and attach only by UUID, so a low-poly sheet can never be attached by mistake.
2. **Sanchez's sheet** (`sanchez-arbiter`) is queued for the Oct 21 reset. The queued prompt in `shorts/sheets_v2/element_prompts.json` is the right one: the unarmed Element, with the Oct 19 arm fix ("the heavy red-and-black mechanical right arm hanging slightly forward, the red mechanical right hand empty"). The notes field beside it still quotes the old clause; that's a stale note only, the prompt itself is correct. QA it against sanchez.md's Look before making the Element.
3. **The Huggable fix** (Oct 21 reset), then **the blue main sheet** (jaws on), made as an edit of the fixed sheet at the next reset (slate §4). C5 can't be generated until the blue main sheet passes QA.
4. **Bryce's ruling on tool-generated voices** (slate §4, due this week). Casting and recording wait on it.
5. **The B-1000 sheet breaks his hand rule.** SHEETS.md rates `b-1000-assault-signature` "Minor… usable as it is", but the sheet (`sheets/b-1000.jpg`) shows a dark fist gripping the rail-gun and a black fist behind the cyan claws, with no chest disc and no claw hose. b-1000.md: "he never holds anything in a hand… Neither forearm shows a hand", and no paws or fingers below any weapon [BBG News invention]. Every C1 take conditioned on this Element will tend to copy the fists, so C1 would fail its own checklist (§7) or pass with a look the soul forbids. Recommended: before the Element is made, queue an edit-fix of the sheet (job `1f7259ce-23ed-4398-9a91-cdbf429dfeed`) at the next daily reset, with an edit prompt in `shorts/sheets_v2/fix_prompts.json`: the rail-gun built onto the right forearm with no hand, no fist or fingers behind the claw gauntlet, the small plain unlit chest disc visible (and the looping claw hose, the sheet's other QA gap). QA it against b-1000.md's Look, then make the Element from the fixed sheet. The alternative is Bryce's recorded exception for C1, written into the C1 checklist. Sheet credits belong to the sheet queue, not this budget.

C1's generation needs blocker 1 (the B-1000 Element) and blocker 5 (the sheet fix, or Bryce's recorded exception), and can still happen this week. The teaser cut also needs blocker 4 and B-1000's four recorded and dubbed lines by Mon Oct 26. If no voice is ready by then, the teaser runs C1 with its servo SFX and burned-in captions only, or posts later (Bryce's call).

**Tool check (read-only, Higgsfield `models_explore`, 2026-10-20).** `seedance_2_0`: duration 4–15 s (default 5, so set **10**), resolution 720p (default), mode `std`, `bitrate_mode` standard, `genre` (use `comedy`), `generate_audio` (default on), aspect 9:16. Media roles: `start_image`, `end_image`, `image_references`, `video_references`, `audio_references`. **There is still no negative-prompt field**, so the negative lists are take checklists (§7) and each prompt carries only STYLE.md's short "Avoid:" sentence. Elements are attached by putting `<<<ELEMENT_UUID>>>` in the prompt text through the API (in the web UI, pick the Element; it shows as @name). This is the attachment, not pasted text: put each placeholder immediately before the words that describe that character. So the operator never edits inside a quote by hand, every paste-ready prompt and opening-pose sentence below already carries neutral slots (`<<<E1>>>`, `<<<E2>>>`) in the right places, and each clip has a "Slots" line, not for pasting, that maps them to Elements. Before submitting, replace the slot's `E1` or `E2` with that Element's bare UUID from SHEETS.md, so `<<<E1>>>` becomes `<<<` + UUID + `>>>`. The tokens are neutral, so a token left unreplaced can never put a name into a prompt.

---

## 1. Logline, runtime, cast

**Logline.** Sanchez finally finishes rescuing Oliver, years late. He carries him onto a crashed Pelican't's super jump pad, which delivers them both right next to the enemy's Pelican't. [BBG News invention; the pads and where they land are Fan-wiki.]

**Era.** Classic, Dec 2013 or later (Sanchez arrived in BBG 2.6, Dec 20, 2013 [Canon]). BBG 2013 default skins in the house 3D style. Joule tokens on the ledger are allowed (post-v2.1). No Steam-trailer or Steam-screenshot material is used: No Bears Land and Sanchez are in neither [Observed].

**Runtime: about 48.7 s** (target 40–60).

| Segment | Length |
|---|---|
| C1 cold open | 8.5 s |
| Title sting | 1.5 s |
| C2 | 7.5 s |
| C3 | 6.5 s |
| C4 | 7.5 s |
| C5 | 5.0 s |
| Sign-off | 10.2 s |
| End card | 2.0 s |

**Cast and Elements.**

| Character | Element (SHEETS.md) | Sheet QA | Clips | Per-shot variant the souls require |
|---|---|---|---|---|
| B-1000 | `b-1000-assault-signature` (job 1f7259ce…) | Minor ("usable as it is", SHEETS.md), but its held rail-gun, fists and missing chest disc break the C1 checklist: edit-fix or Bryce's exception first (§0, blocker 5) | C1 on screen; sign-off VO | Solo shot: STYLE.md's sanctioned "glossy painted armour" in the video suffix (b-1000.md, Style strings). Signature kit only: rail-gun right forearm, claw gauntlet left forearm, jump-pack; no Satellite: not in the signature kit, and it would need its own sheet (`b-1000-assault-orb`); BBG 2.7, 2014 [Fan-wiki]. He fires nothing. |
| Sanchez | `sanchez-arbiter` (queued, Oct 21 reset) | not yet made | C2, C3, C4; VO in C5 | The unarmed Element in every shot (sanchez.md: "use this one as his Element in every image and video"). No gun, no blade, so never the armed model sheet or the melee-out variant. Blue team changes no words; he's red here anyway. |
| Oliver | `oliver-soldier` (job 909ea0bd…) | Pass | C2, C3, C4 | The unarmed Element (oliver.md). Red team. He holds only a fry and then the basket, food props described in words; no prop sheet. |
| Huggable ×5 (a wave) | SHEETS.md lists `huggable-huggable` (job 0680a612…, Fix queued) | Fix queued | C5 | huggable.md's paw rule: the arms-wide threat pose takes the **main sheet, jaws on**, and as opponents of a red lead they take the **blue** sheet (STYLE.md, Teams in frame). So C5 uses the **blue main sheet**, an edit of the fixed red sheet that changes only "red cloth team banner" to "blue cloth team banner". It isn't in SHEETS.md yet; proposed Element name `huggable-huggable-blue` (open item 6). Five copies count as one Element (STYLE.md habit 4). |

Every shot has at most two Element characters: C1 one, C2 to C4 two, C5 one.

---

## 2. Map, environment sheet, plates

**Map:** No Bears Land at noon, `environments/no-bear-s-land.md`. Spell it "No Bears Land" in captions (maps overview §5.4). One light rig for the whole episode, the sheet's classic 2013 rig, in every clip word for word: "under a saturated mid-blue sky with big soft white cumulus clouds, the high sun as a slightly warm key with a soft cool fill from the sky and a gentle rim light on the characters." Never use the Oct 2026 lighting-pass variants.

**Layout used** (sheet §2, rotational, never mirrored): Red keep north, its food stand to the north-east; the **red-banded wreck in the west**, the **blue-banded wreck in the east**. Sanchez walks Oliver from the Red food stand to the west wreck, climbs it by the wing ("the port wing" [Fan-wiki]), and the pad drops them "right next to the opposite spacecraft" [Fan-wiki], the blue east wreck. The trench zig-zag runs through the middle, under the arc.

**Map guards** (slate; sheet §5 and §7): the Pelican't stays an original stubby cartoon dropship, never Halo- or Aliens-like, and is prompted as "sci-fi transport aircraft"; the food stand's mascot roundels are blank ("plain, unmarked panels"); the keep stencil is blank (no keep is in frame); the wrecks are empty, clean, with no smoke, fire or crew; no score bar, kill feed, "SUICIDE" wording or player markers.

**Scene lines.** The sheet gives video-environment lines for the trench, the field, the pillar, the tower roof and the food stand, but **none for the wrecks**. C1, C3, C4 and C5 use wreck lines this package derives from the sheet's low-angle plate, in the sheet's own words and with its light clause unchanged. They need approval or a place in the sheet (open item 4).

| Line | Used in | Text (camera sentence per clip in §3) | Source |
|---|---|---|---|
| Food stand | C2 | the sheet's "Food stand" line, word for word | Sheet §6 |
| Red wreck | C1, C3 | "A sunlit grassy hilltop at high noon, at the head of a long ploughed furrow of soft orange-edged earth, beside a chunky crash-landed dark grey sci-fi transport aircraft with an olive cast, softly rounded painted-metal panels with gentle dents, tomato-red bands, stubby wings and three fat cylindrical engine pods, the fourth snapped off in the grass beside the nose, an octagonal pad with a yellow-and-black hazard rim and a glowing icy-cyan star centre on top of its hull, faint stacked cyan rings hovering over it, the hull clean, intact and quiet in clear, still air, short, soft, stylised yellow-green turf flecked with tiny white daisies all around, under a saturated mid-blue sky with big soft white cumulus clouds, the high sun as a slightly warm key with a soft cool fill from the sky and a gentle rim light on the characters." | Derived from the sheet's low-angle plate (the furrow and the three pods plus the snapped-off fourth, in its own words) and pad wording; the rings are the establishing shot's pad wording (stacked cyan rings on jump pads are [Observed], wreck tops included, sheet §4) |
| Blue wreck | C4, C5 | "A sunlit grassy hilltop at high noon, beside a chunky crash-landed dark grey sci-fi transport aircraft with an olive cast, softly rounded painted-metal panels with gentle dents, royal-blue bands, stubby wings and three fat cylindrical engine pods, the fourth snapped off in the grass beside the nose, an octagonal pad with a yellow-and-black hazard rim and a glowing icy-cyan star centre on top of its hull, faint stacked cyan rings hovering over it, the hull clean, intact and quiet in clear, still air, short, soft, stylised yellow-green turf flecked with tiny white daisies all around, under a saturated mid-blue sky with big soft white cumulus clouds, the high sun as a slightly warm key with a soft cool fill from the sky and a gentle rim light on the characters." | Derived, as above, with the sheet's own blue swap ("tomato-red bands" → "royal-blue bands"). The furrow clause is left out on purpose: C4 and C5 look at the nose end from the landing spot, and the east wreck's furrow trails south behind its tail (sheet §2, §4) |

**Background plates** (Nano Banana Pro, 9:16, 2k; each plate becomes the image reference for that scene's start still):

| Plate | Clips | Prompt | Status |
|---|---|---|---|
| **P1** red wreck, low angle | C1, C3 | The sheet's "Background plate: low angle (the crash furrow and the wreck)", word for word (it is already the red-banded wreck) | Sheet plate, ready |
| **P2** food stand, medium | C2 | Derived from the sheet's food-stand line (below) | Needs approval |
| **P3** blue wreck, wide, looking back across the field | C4 | Derived (below) | Needs approval |
| **P4** blue wreck, medium, from the landing spot looking east at the nose | C5 | Derived (below). Not the sheet's low-angle plate: that camera sits low in the furrow behind the tail, and the east wreck's furrow trails south (sheet §2), so it can't be the reverse from C4's landing spot beside the nose | Needs approval |

P2, derived (paste-ready inside the quotes):
> "Medium background plate at high noon, at eye level beside a red-and-yellow pyramid parasol with plain, unmarked panels on a single dark pole over a squat grey cart, a softly glowing red basket of golden fried food on short, soft, stylised yellow-green turf flecked with tiny white daisies beside it, plump curved arcs of tan sandbags behind, under a saturated mid-blue sky with big soft white cumulus clouds. A high noon sun as a slightly warm key with crisp, short shadows, a soft cool fill from the sky, a gentle rim light along the parasol and cart silhouettes. Uncluttered, no characters, no text, no logos. Vertical 9:16 framing. Polished stylized feature-film 3D animation, soft rounded shapes, bold readable silhouettes, soft global illumination, cinematic lighting, cinematic depth of field."

Not for pasting: the parasol and cart sit right of centre; the left third is open grass for Sanchez's entrance; the bottom fifth is plain turf. One basket only.

P3, derived (paste-ready inside the quotes):
> "Wide background plate at high noon from low on a grassy hilltop beside the blunt nose of a chunky crash-landed dark grey sci-fi transport aircraft with an olive cast, softly rounded painted-metal panels with gentle dents and royal-blue bands, its nose and one fat cylindrical engine pod filling the left edge of the frame, looking back across a wide sunlit field: short, soft, stylised yellow-green turf flecked with tiny white daisies, plump curved arcs of tan sandbags and an S-shaped zig-zag of sunken trenches with honey-gold plank floors and plain grass-capped lips crossing the middle distance, misty blue-grey wooded hills on the far horizon, and a big open sky above taking up the upper half of the frame, saturated mid-blue with big soft white cumulus clouds. A high noon sun as a slightly warm key with crisp, short shadows, a soft cool fill from the sky, a gentle rim light along the hull silhouette. The hull sits clean, intact and quiet in clear, still air. Uncluttered, no characters, no text, no logos. Vertical 9:16 framing. Polished stylized feature-film 3D animation, soft rounded shapes, bold readable silhouettes, soft global illumination, cinematic lighting, deep focus."

Not for pasting: the empty upper half is the arc's runway; the landing spot is open grass at centre-left, a little above the bottom third. The far red wreck is left out (one landmark per shot, maps overview §5.3).

P4, derived (paste-ready inside the quotes):
> "Medium background plate at high noon at low eye level on a sunlit grassy hilltop, a few steps from the blunt nose of a chunky crash-landed dark grey sci-fi transport aircraft with an olive cast, seen at a three-quarter angle, its cockpit window and twin round headlamps turned partly toward the camera, softly rounded painted-metal panels with gentle dents and royal-blue bands, stubby wings and three fat cylindrical engine pods; the fourth pod lies snapped off in the daisy-flecked grass beside the nose, below a glowing icy-cyan pad on top of the hull. The hull fills the upper middle of the frame, with a broad stretch of open, short, soft, stylised yellow-green turf flecked with tiny white daisies in front of it, under a saturated mid-blue sky with big soft white cumulus clouds. A high noon sun as a slightly warm key with crisp, short shadows, a soft cool fill from the sky, a gentle rim light along the hull silhouette. The hull sits clean, intact and quiet in clear, still air. Uncluttered, no characters, no text, no logos. Vertical 9:16 framing. Polished stylized feature-film 3D animation, soft rounded shapes, bold readable silhouettes, soft global illumination, cinematic lighting, cinematic depth of field."

Not for pasting: the camera stands on C4's landing spot (P3's centre-left grass), looking east back at the nose, so C5 is a true reverse of C4. The nose, pod and pad wording is the sheet's low-angle plate's own; the furrow trails south behind the tail and stays out of frame. The open turf in the lower half holds the staggered row of Huggables; the bottom fifth is plain turf.

Habit-5 check for every plate: the sheet's Negative line (§6), and no yellow stripes on trench lips.

---

## 3. Shot list

How every prompt is built (STYLE.md, Shot formula; each soul's "How to use"): attach the Elements of everyone in frame, then the acting character's character line from its soul's video starter, then one action, then the scene line with that clip's camera sentence, then the short "Avoid:" sentence (no negative field), then "Vertical 9:16 framing.", then the video suffix, always last. Co-stars are described in their own soul's words. No names, weapon names, hex codes, spoken words or notes go inside the quotes. Seedance settings for every clip: `seedance_2_0`, 10 s, 9:16, 720p, `mode` std, `genre` comedy, `generate_audio` on (but see open item 9).

**Start frames (applies to all clips).**
- Make each start still with Nano Banana Pro (9:16, 2k): attach the clip's plate as `image_references` and the clip's Elements as placeholders, and use the clip's own prompt with the action replaced by the opening-pose sentence given per clip. Still and clip then share every word except the action. Gate each still: on-model, framing and expression match the clip's first beat, safe zone respected.
- Pass the approved still as Seedance's `start_image`, with the same Elements as placeholders.
- **Test this on C1 first.** The Oct 15 package avoided mixing a start image with Element placeholders (a possible refusal or start-frame jump), and its take fa2d2ca7 drifted from the start still at frame 0. If C1 refuses or jumps, drop the placeholders from the video call and run on `start_image` plus the full character lines (the Oct 15 method), keeping the Elements in the stills. Either way, treat the start image as a strong hint, not a lock, and trim to the window that holds.
- **End stills for that fallback (C2 and C4).** Without placeholders, C4 (which starts on the empty P3 plate) would carry no reference for either bear, and C2 (whose still shows Oliver only) none for Sanchez, which breaks STYLE.md habit 1. So if the fallback is used, make an end still for each with Nano Banana Pro (9:16, 2k): P2 or P3 as `image_references` plus both Elements in their slots, posed on the clip's final hold (C2: the Verdict, with Oliver holding the basket up; C4: the landing hold beside the hull). Gate it like a start still, then pass it to Seedance as `end_image` (a listed media role) and run those clips on `start_image` + `end_image` + the full character lines. Budget: 2 more stills (§7).

### C1 · Cold open "LIVE" (also the Oct 28 teaser) · used 8.5 s

- **Beat.** B-1000, live, in front of the red-banded crashed Pelican't. HUD brackets lock onto the jump pad on its roof while he files his hazard report.
- **Camera and staging.** The weekly lock-off: B-1000 slightly left of centre in the upper two-thirds, the hull behind him on its hill, the glowing pad on top of the hull visible right of centre (not at the right edge, where the brackets must land). Low angle, so the half-ton robot looms. No camera move. Faces out of the bottom fifth and the right edge.
- **Elements:** `b-1000-assault-signature` (solo), made from the fixed sheet, or from the current one only under Bryce's recorded exception (§0, blocker 5).
- **Slots** (not for pasting): E1 = `b-1000-assault-signature`.
- **Start frame.** P1 plus the Element. Opening-pose sentence (it replaces the action for the still): "stands planted in front of the crashed aircraft, slightly left of centre in the upper two-thirds of the frame, his clawed feet set wide and his weight low, his head turned three-quarters toward camera, eye-slits narrowed, the glowing pad on top of the hull clear behind him."
- **Prompt** (paste-ready inside the quotes):
> "<<<E1>>> A hulking, top-heavy robot bear built entirely of glossy maroon painted-metal armour, with pointed plated ears, a black-tipped snout over a hinged jaw plate, two narrow glowing cyan eye-slits under a heavy brow plate, a long orange-and-black slab rail-gun built onto his right forearm, a three-blade cyan claw gauntlet on his left forearm and a white winged jump-pack on his back, stands planted in front of the crashed aircraft with his clawed feet set wide and his weight low, snaps his head toward camera and holds a dead-still stare while his eye-slits narrow, then says four short clipped lines, each ending on a dead-still hold; he emotes with his brow plate and eye-slits, and his hinged jaw plate drops a little when he shouts. A sunlit grassy hilltop at high noon, at the head of a long ploughed furrow of soft orange-edged earth, beside a chunky crash-landed dark grey sci-fi transport aircraft with an olive cast, softly rounded painted-metal panels with gentle dents, tomato-red bands, stubby wings and three fat cylindrical engine pods, the fourth snapped off in the grass beside the nose, an octagonal pad with a yellow-and-black hazard rim and a glowing icy-cyan star centre on top of its hull, faint stacked cyan rings hovering over it, the hull clean, intact and quiet in clear, still air, short, soft, stylised yellow-green turf flecked with tiny white daisies all around, under a saturated mid-blue sky with big soft white cumulus clouds, the high sun as a slightly warm key with a soft cool fill from the sky and a gentle rim light on the characters. Locked-off low-angle medium shot. Avoid: photorealism, real-person likeness, official logos, text, watermarks, scene cuts, slow motion. Vertical 9:16 framing. Polished feature-film 3D animation, soft rounded shapes, expressive faces, glossy painted armour, soft global illumination, cinematic lighting, snappy cartoon timing with strong poses and holds."
  - Not for pasting: solo shot, so the suffix uses "glossy painted armour" (STYLE.md sanctioned variant), and the Avoid line leaves out "photorealistic fur, realistic anatomy" so no fur is named. Keep the camera sentence "Locked-off low-angle medium shot." for every episode's C1, so the cold open frames the same way each week.
- **Dialogue (B-1000, on camera; dubbed).** "B-1000. Live. Scanning location." / "Hazard: crashed dropship." / "Status: still crashed." / "Launch pad destination: the other crashed dropship." (17 words, slate §2.)
  - Voice: mid-low, evenly clipped synthetic deadpan with light digital grit, slightly too loud; error-log cadence, each line landing on a dead-still hold with about half a second of silence before the next. Say "B-1000" as "B one thousand". No giggle here (his one "tee-hee" is the sign-off's). Bitcrush in post. Original voice only; never a famous film robot (b-1000.md, Casting).
  - Lip-sync: his jaw plate drops a little and he never moves much, so land each line on a hold and let the slips fall where they fall.
- **Sound.** Servo whine on the head-snap; a light noon breeze over grass; a soft electronic hum from the pad. All SFX are [BBG News invention].
- **On-screen text (edit only).** A small "● LIVE" HUD label top-left in B-1000's cyan, original rounded typeface. HUD per b-1000.md: thin cyan corner brackets, one 6-frame scan line sweeping down, then the brackets lock onto the pad on the hull top on "Launch pad destination". Burned-in captions (see §5).

### Title sting · 1.5 s (edit only)
After the hazard report: a 6-frame scan-line wipe, then "LOCAL HAZARDS" stamped in original rounded lettering, over the original two-note news sting. Built once and reused every week (slate §2).

### C2 · The food stand · used 7.5 s

- **Beat.** At the Red keep's food stand, Oliver is mid-bite from the glowing basket. Sanchez strides in and holds his Verdict pose, visor glowing, and announces the rescue. Oliver, mouth full, guilty and far too friendly, offers him the basket.
- **Camera and staging.** Locked-off medium, eye level. Oliver sits on the grass beside the cart, right of centre, a fry in his paw and the basket on the grass at his side (P2's one basket, where the sheet puts it). Sanchez enters from frame left and plants left of centre, pointing his mechanical arm at Oliver. Leave headroom above both for the THREAT LEVEL tags. One action: Sanchez's entrance into the Verdict. Oliver's reaction on the hold is his blurted line and the basket offer: he scoops it up off the grass and holds it up.
- **Elements:** `sanchez-arbiter`, `oliver-soldier`.
- **Slots** (not for pasting): E1 = `sanchez-arbiter`, E2 = `oliver-soldier`. The start still uses E2 only.
- **Start frame.** P2 plus the Oliver Element only (Sanchez isn't in the opening frame). Opening-pose sentence: "<<<E2>>> a chestnut-brown robotic teddy-bear soldier, soft plush all over, with a red headband and a brass-cartridge bandolier, sits on the grass right of centre beside the cart, frozen mid-bite with a golden fry in his paw, the softly glowing red basket of golden fried food on the grass at his side, the left third of the frame empty grass." (In this still, Oliver's words become the subject line, because Sanchez isn't in frame.)
- **Prompt** (paste-ready inside the quotes):
> "<<<E1>>> A lean teddy-bear cyborg in a dark maroon helmet with rounded bear-ear bumps and an opaque glowing red visor hiding his eyes, a light tan muzzle with a small dark goatee, a grey-khaki chest plate over grey-and-white camo, olive-and-tan camo trousers, a dark grey glove on his left hand and an oversized red-and-black mechanical right arm. He strides in from the left with both hands empty and snaps into a hard hold beside <<<E2>>> a chestnut-brown robotic teddy-bear soldier, soft plush all over, with a red headband and a brass-cartridge bandolier, as tall as the cyborg, who sits on the grass frozen mid-bite beside the softly glowing red basket of golden fried food, a golden fry in his paw; the cyborg plants his feet wide, chest out, chin up, his gloved left hand flat on his chest plate and his mechanical right arm raised and pointing at the soldier, the brighter glow band inside his visor narrowing as he says a short line, and the soldier, cheeks full, raises both brows, flashes a wide guilty grin, blurts a short line through a full mouth, scoops the basket up off the grass and holds it up toward him, and both hold the pose. A sunlit daisy-flecked grass field at high noon, beside a red-and-yellow pyramid parasol with plain, unmarked panels on a single dark pole over a squat grey cart, a softly glowing red basket of golden fried food on the grass beside it, under a saturated mid-blue sky with big soft white cumulus clouds, the high sun as a slightly warm key with a soft cool fill from the sky and a gentle rim light on the characters. Locked-off medium shot. Avoid: photorealistic fur, realistic anatomy, real-person likeness, official logos, text, watermarks, scene cuts, slow motion. Vertical 9:16 framing. Polished feature-film 3D animation, soft rounded shapes, expressive faces, soft plush fur, soft global illumination, cinematic lighting, snappy cartoon timing with strong poses and holds."
  - Not for pasting: one basket. The action puts it on the grass beside Oliver, where the scene line and P2 put it ("on the grass beside it"), in the same words, so both placements agree and the tool draws one; he lifts it only on the offer, and carries it into C3 and C4. "Holds still" wording for Sanchez, never "slow" or "solemn" (sanchez.md, Timing).
- **Dialogue (dubbed).**
  - SANCHEZ: "Oliver, we'll getcha... home." Voice: an original warm, slightly gravelly baritone with operatic gravitas; solemn words over a snappy body; one half-second pause, before "home" (his one allowed pause, before the last word); under 3 s. Any accent is fluent and never a caricature (open item 13). This echoes his BB Zombies radio line [Fan-wiki].
  - OLIVER: "Sanchez! Buddy! You look GREAT! ...Fry?" Voice: a bright, mid-range young-adult male voice with a grin in it, here muffled by a full mouth and pitched too high from guilt; a quick setup, a half-beat of silence, then "...Fry?" on the hold (oliver.md cadence). Original voice only.
- **Sound.** A crunchy bite at the top; servo clunk as the mechanical arm snaps up; a faint fryer sizzle from the cart (maps dossier `no-bear-s-land.md`: steam or sizzle from the cart is [BBG News invention]); breeze. No music yet.
- **On-screen text (edit only).** THREAT LEVEL tags, original HUD style, never over a face, out of the bottom fifth and the right edge: "SUBJECT: OLIVER · THREAT LEVEL: FLUFFY" as the clip opens, then "SUBJECT: SANCHEZ · THREAT LEVEL: PARTIAL UPGRADE" when he lands the Verdict. Captions.

### C3 · Up the wreck · used 6.5 s

- **Beat.** Sanchez carries Oliver to the red-banded wreck and marches up its wing to the glowing star pad: "This arm, I did not ask for. But look at it." Oliver still holds the basket.
- **Camera and staging.** Locked-off low-angle medium from the head of the furrow, looking up at the stubby wing and the top of the hull. P1 stays the still's image reference, but the camera comes in closer than P1's far-down-the-trough view, so the two 1.0× bears (and the small smile) read in a 720p frame; the stacked rings over the pad give the pad a cue that reads from below. The hoist happens in the cut: C3 opens with Oliver already tucked under the mechanical right arm, which keeps one action per clip. The under-arm carry is chosen for reliability and keeps both faces readable (open item 11). He climbs the wing, plants on the pad, and on the hold tips his head toward the arm with the pride smile.
- **Elements:** `sanchez-arbiter`, `oliver-soldier`.
- **Slots** (not for pasting): E1 = `sanchez-arbiter`, E2 = `oliver-soldier`.
- **Start frame.** P1 plus both Elements. Opening-pose sentence: "stands at the foot of the stubby wing, chest out, <<<E2>>> a chestnut-brown robotic teddy-bear soldier, soft plush all over, with a red headband and a brass-cartridge bandolier, as tall as the cyborg, tucked firmly under his mechanical right arm and hugging a softly glowing red basket of golden fried food." Extra gate for this still: both faces at least about a tenth of the frame height.
- **Prompt** (paste-ready inside the quotes):
> "<<<E1>>> A lean teddy-bear cyborg in a dark maroon helmet with rounded bear-ear bumps and an opaque glowing red visor hiding his eyes, a light tan muzzle with a small dark goatee, a grey-khaki chest plate over grey-and-white camo, olive-and-tan camo trousers, a dark grey glove on his left hand and an oversized red-and-black mechanical right arm. With <<<E2>>> a chestnut-brown robotic teddy-bear soldier, soft plush all over, with a red headband and a brass-cartridge bandolier, as tall as the cyborg, tucked firmly under his mechanical right arm and hugging a softly glowing red basket of golden fried food, he marches up the stubby wing onto the top of the hull and plants his boots on the glowing pad with a hard stop, then holds still, chest out, chin up, and says a short line, then tilts his head toward his mechanical arm as a small closed-mouth smile lifts his goatee. A sunlit grassy hilltop at high noon, at the head of a long ploughed furrow of soft orange-edged earth, beside a chunky crash-landed dark grey sci-fi transport aircraft with an olive cast, softly rounded painted-metal panels with gentle dents, tomato-red bands, stubby wings and three fat cylindrical engine pods, the fourth snapped off in the grass beside the nose, an octagonal pad with a yellow-and-black hazard rim and a glowing icy-cyan star centre on top of its hull, faint stacked cyan rings hovering over it, the hull clean, intact and quiet in clear, still air, short, soft, stylised yellow-green turf flecked with tiny white daisies all around, under a saturated mid-blue sky with big soft white cumulus clouds, the high sun as a slightly warm key with a soft cool fill from the sky and a gentle rim light on the characters. Locked-off low-angle medium shot from the head of the furrow, looking up at the stubby wing and the top of the hull. Avoid: photorealistic fur, realistic anatomy, real-person likeness, official logos, text, watermarks, scene cuts, slow motion. Vertical 9:16 framing. Polished feature-film 3D animation, soft rounded shapes, expressive faces, soft plush fur, soft global illumination, cinematic lighting, snappy cartoon timing with strong poses and holds."
- **Dialogue (dubbed).** SANCHEZ: "This arm, I did not ask for. But look at it." (sanchez.md new line 1, trimmed per the slate). Voice: grand inverted syntax, then the pride leaking through on "look at it"; two short lines, each under 3 s; a tiny lift on "look". Oliver is silent and munches.
- **Sound.** Boot clanks on the metal wing; servo whir on the arm; one crunch from Oliver; the pad hum swelling as he plants. **Music in:** an original mock-heroic cue (brass and strings, solemn, swelling) starts on the plant (sanchez.md: solemn setup, swelling music, slapstick deflation).
- **On-screen text.** Captions only.

### C4 · The launch · used 7.5 s (the riskiest shot; generate it first among C2–C5)

- **Beat.** A huge, high arc over the trench zig-zag, Sanchez in a heroic pose and Oliver hugging his lunch. They land beside the blue-banded Pelican't. Sanchez: "Home." Oliver: "...That's THEIR ship."
- **Camera and staging.** Locked-off wide from low beside the blue hull's nose (P3), looking back west across the trenches. The launch itself happens in the cut, covered by a pad "whump" pre-lapped over the end of C3. They enter mid-arc high in the upper left, cross the open upper half of the 9:16 frame, drop and land with a squash at centre-left, then hold for the two lines. One continuous action that ends on a hold. Land them above the bottom third so the faces clear the bottom fifth. No Huggables in this shot.
- **Elements:** `sanchez-arbiter`, `oliver-soldier`.
- **Slots** (not for pasting): E1 = `sanchez-arbiter`, E2 = `oliver-soldier`.
- **Start frame.** P3 itself, empty (the characters fly in). No start still. In the no-placeholder fallback only, add the end still from the start-frames note above as `end_image`.
- **Prompt** (paste-ready inside the quotes):
> "<<<E1>>> A lean teddy-bear cyborg in a dark maroon helmet with rounded bear-ear bumps and an opaque glowing red visor hiding his eyes, a light tan muzzle with a small dark goatee, a grey-khaki chest plate over grey-and-white camo, olive-and-tan camo trousers, a dark grey glove on his left hand and an oversized red-and-black mechanical right arm. With <<<E2>>> a chestnut-brown robotic teddy-bear soldier, soft plush all over, with a red headband and a brass-cartridge bandolier, as tall as the cyborg, tucked firmly under his mechanical right arm and hugging a softly glowing red basket of golden fried food, he sails in from high in the upper left of the sky in one huge, high arc, his gloved left fist thrust forward in a heroic flying pose, drops down and lands beside the hull with a squash on bent knees, then snaps into a hard hold, chest out, chin up, as he says one word, while the soldier stares up at the hull's royal-blue bands, his smirk gone flat and his brows down. A sunlit grassy hilltop at high noon, beside a chunky crash-landed dark grey sci-fi transport aircraft with an olive cast, softly rounded painted-metal panels with gentle dents, royal-blue bands, stubby wings and three fat cylindrical engine pods, the fourth snapped off in the grass beside the nose, an octagonal pad with a yellow-and-black hazard rim and a glowing icy-cyan star centre on top of its hull, faint stacked cyan rings hovering over it, the hull clean, intact and quiet in clear, still air, short, soft, stylised yellow-green turf flecked with tiny white daisies all around, under a saturated mid-blue sky with big soft white cumulus clouds, the high sun as a slightly warm key with a soft cool fill from the sky and a gentle rim light on the characters. Locked-off wide shot from beside the hull's nose, looking back across a zig-zag of sunken trenches with honey-gold plank floors. Avoid: photorealistic fur, realistic anatomy, real-person likeness, official logos, text, watermarks, scene cuts, slow motion. Vertical 9:16 framing. Polished feature-film 3D animation, soft rounded shapes, expressive faces, soft plush fur, soft global illumination, cinematic lighting, snappy cartoon timing with strong poses and holds."
- **Fallback** (slate §5: only if C4 fails after 3 retakes): restage as an edit match-cut. C4a is the end of C3 plus a launch: "…crouches on the glowing pad and is flung straight up by it, shooting out of the top of the frame." (Never "rockets": it invites the jet flames the C4 checklist rejects.) C4b is the P3 plate with "…drops in from the top of the frame and lands beside the hull with a squash…", same character lines and scene lines. A whoosh and a 2-frame sky wipe join them. Cost in §7.
- **Dialogue (dubbed).**
  - SANCHEZ: "Home." Voice: one word, proud and final, chest-voice resonance, on the hold.
  - OLIVER: "...That's THEIR ship." Voice: a half-beat of silence, then flat deadpan realisation, his bravado cracking a little on "THEIR" (oliver.md: deadpan register, yelp crack).
- **Sound.** A pad "whump" and launch whoosh pre-lapped from C3; wind rush across the arc; a heavy landing thud with a small dust puff (the only dust); the basket's fries rattle. **Music:** the mock-heroic cue peaks over the arc and lands on the touchdown, then **cuts dead** on "THEIR".
- **On-screen text.** Captions only.

### C5 · The reverse · used 5.0 s, hard cut

- **Beat.** Reverse shot: a blue Huggable wave turns toward camera as one, arms opening. Their head radios crackle "kssht" in unison (hijacker clue 1). Sanchez, off screen: "...Mayday." Hard cut before the hug lands.
- **Camera and staging.** Locked-off medium at low eye level, from where Sanchez and Oliver landed, looking east at the blue hull's nose (P4, the derived landing-spot plate in §2). Five Huggables in a loose, staggered row on the open turf in front of the hull with their backs to camera, five blue banners filling the frame (staggered so five fit a 9:16 medium). They snap round together into the leaning hug pose (not the stiff T pose), antenna balls blink once together, and they hold. Cut on the held hug pose, before any step toward camera: no contact is ever shown.
- **Elements:** the blue main sheet (proposed `huggable-huggable-blue`), once for all five.
- **Slots** (not for pasting): E1 = `huggable-huggable-blue` (once its UUID is in SHEETS.md).
- **Start frame.** P4 plus the blue main Element. Opening-pose sentence: "stand in a loose, staggered row with their backs to camera in front of the hull, their five blue banners rising high above their heads."
- **Prompt** (paste-ready inside the quotes):
> "<<<E1>>> Five identical copies of a small stitched hot-pink plush teddy about two-thirds as tall as a teddy-bear soldier, with a big round cream-bandaged head, short stubby arms and legs, a boxy dark olive-green radio with a thin grey red-ball antenna, one glossy red button eye on its right, one small black bead eye on its left, a huge fixed toothy grin and a tall, narrow blue banner on a pole rising from its back high above its head, stand in a loose, staggered row with their backs to camera, then snap around toward camera in perfect unison and lean in on their toes with their arms forward and wide in a hug pose, oversized black bear-trap jaws snapping on all their paws, the red balls on their antennas blinking once together and their banners whipping above their heads, and hold, their grins never moving and their teeth never parting. A sunlit grassy hilltop at high noon, beside a chunky crash-landed dark grey sci-fi transport aircraft with an olive cast, softly rounded painted-metal panels with gentle dents, royal-blue bands, stubby wings and three fat cylindrical engine pods, the fourth snapped off in the grass beside the nose, an octagonal pad with a yellow-and-black hazard rim and a glowing icy-cyan star centre on top of its hull, faint stacked cyan rings hovering over it, the hull clean, intact and quiet in clear, still air, short, soft, stylised yellow-green turf flecked with tiny white daisies all around, under a saturated mid-blue sky with big soft white cumulus clouds, the high sun as a slightly warm key with a soft cool fill from the sky and a gentle rim light on the characters. Locked-off medium shot at low eye level. Avoid: photorealistic fur, realistic anatomy, real-person likeness, official logos, text, watermarks, scene cuts, slow motion. Vertical 9:16 framing. Polished feature-film 3D animation, soft rounded shapes, expressive faces, soft plush fur, soft global illumination, cinematic lighting, snappy cartoon timing with strong poses and holds."
  - Not for pasting: the huggable.md character line is word for word with its blue-team change ("a tall, narrow blue banner"); the only addition is the "Five identical copies of" prefix, with the soul's "A" lowercased after it. Its action follows the soul's starter action (lean in on its toes, arms forward and wide, jaws snapping, banner whipping) and the talking-beat face rule (grin never moves, antenna ball blinks).
- **Dialogue (dubbed).**
  - HUGGABLES (through their radios, no lip-sync): a single shared "kssht", with no words.
  - SANCHEZ (off screen): "...Mayday." Voice: the operatic baritone collapsing to a small, resigned murmur; the half-second pause sits before the word. From his BB Zombies line [Fan-wiki].
- **Sound.** Dead silence after the music cut, then five banners flap at once on the turn, the jaws clack as one (huggable.md: a crunchy metallic clack), then the "kssht" (an original radio-static burst; use **the exact same sample** in the sign-off glitch, so the clue connects), then "...Mayday." Hard cut to silence.
- **On-screen text.** No tag here; the Huggable's "HUG" tag is saved for its first focused appearance (Ep 5). Captions: "kssht" and "...Mayday."

---

## 4. Signature pieces, as built for Ep 1

**Cold open "LIVE"** (C1, above). The locked-off low-angle medium, B-1000 slightly left of centre in the upper two-thirds, one landmark behind him. The `b-1000-assault-signature` Element with the glossy solo suffix. "B-1000. Live. Scanning location." plus three hazard lines, 17 words, each on a hold. Edit HUD: "● LIVE" label, thin cyan corner brackets, a 6-frame scan line, brackets locking onto the pad. Original art only, no game UI.

**Sting.** A 6-frame scan-line wipe, "LOCAL HAZARDS" in original rounded lettering, the original two-note news sting, about 1.5 s. Plus the THREAT LEVEL tags in C2 (FLUFFY, PARTIAL UPGRADE), which seed the weekly "guess the next label" comment game.

**Sign-off** (about 10.2 s, edit only; then the end card). The slate's nominal is ~6 s, but Ep 1's VO is 11 words in four lines: at C1's pace (about 3 words a second, with about half a second of hold after each line) it needs about 5.2 s, so the sign-off is timed for it. It plays on the ledger's own original-art background, never over picture from C5, so the hug stays off screen.

| Time in sign-off | Picture | Sound |
|---|---|---|
| 0.0–0.4 | The ledger card slams up: **SCENERY 1 · BEARS 0** (original layout and typeface; never the kill feed, never "SUICIDE") | Slam thump |
| 0.4–1.2 | Three blue-bolt Joule tokens plink onto the card, the ledger's point marker, card only | Plink ×3 |
| 1.2–1.8 | **METHOD: DELIVERED TO THE WRONG SHIP** | Type clack |
| 1.8–2.3 | The stamp lands: **REAL MAP. FAN-MADE NEWS.** | Stamp thunk |
| 2.3–8.5 | The card holds through the VO; the upload bar appears on "Uploading..." (about 7.0) and fills to 99% by 8.5, then freezes | B-1000 VO, 2.3–7.5: "Kill credit: jump pad. Assist: Huggables. Next location: Steamyard Blues. Uploading..." Delivery: clipped error-log cadence, each line on a short hold, a small proud lift on "Kill credit" |
| 8.5–8.65 | A 3-frame pink static glitch with a stitched-seam texture (hijacker clue) | The **same** "kssht" sample as C5 |
| 8.65–9.6 | The bar reads **REROUTING... TO: EVERYONE** | Two descending error bleeps |
| 9.6–10.2 | Hold | B-1000: "Tee-hee." Bright, quick, a little too pleased: his one per short. **Hard cut.** |

If the episode must run shorter, the alternative is to cut "Assist: Huggables." and keep the old 8.0 s timing, which changes the slate's locked VO (Bryce's call).

Ledger labels (slate §2): the tokens [Observed]; their identity as Joules [Fan-wiki; identification Inference]; their use as the ledger's point marker [BBG News invention].

**End card**, word for word, held 2.0 s inside the safe area, silent, no logos, wordmarks or app icons:
> Unofficial fan film, not affiliated with SkyVu; characters © SkyVu.

(Whether it should also say "AI" is [Open], open item 7.)

**Teaser cut (Wed Oct 28, 0 extra credits):** C1 (8.5 s), then a "LOCAL HAZARDS · Nov 4" super in the sting lettering (1.5 s, with the sting), then the end card (2 s). About 12 s. Caption in §6. It carries B-1000's four dubbed lines and their burned-in captions, so it needs the voice ruling (blocker 4) and his recorded lines by Mon Oct 26; the no-voice fallback is in §0.

---

## 5. Edit plan

1. **Order:** C1 → sting → C2 → C3 → C4 → C5 → sign-off → end card. Hard cuts, except the sting's 6-frame scan-line wipe (and the 2-frame sky wipe if the C4 fallback split is used).
2. **Trims.** Pick from each 10 s take the window that passes §7. Targets: C1 8.5 s (all four line holds), C2 7.5 s, C3 6.5 s, C4 7.5 s, C5 5.0 s, cut on the held hug pose before any forward step. Skip any opening frames that drift from the start still. Never use a frame outside the passed window.
3. **Picture finish:** upscale 720p to 1080×1920 (ffmpeg, free); one colour grade for the whole episode (warm noon, saturated but natural); light film grain; hand-timed holds. Anything carrying text stays inside the Reels safe zone: nothing in the bottom fifth, nothing hard against the right edge.
4. **Overlays** (original art, never prompted, no game UI or logos):
   - C1: "● LIVE" label, cyan corner brackets, scan line, the bracket lock on the pad.
   - C2: the two THREAT LEVEL tags.
   - Sting and sign-off: ledger card, Joule tokens, METHOD line, stamp, upload bar, pink stitched-seam glitch, REROUTING line.
   - **Status sprites: none.** No status effect happens in Ep 1 (nobody is slowed, stunned, poisoned, irradiated or reversed), so STYLE.md's sprite kit isn't used this week. No reticles, crosshairs or kill-feed cards.
   - Optional: a small "BBG NEWS · FAN FILM" corner bug from frame 1 (open item 12).
5. **Captions:** burned in for every spoken line, the "kssht" and the "Tee-hee", in an original rounded typeface. B-1000's lines in his HUD cyan, everyone else's in white with a dark outline. Place them just above the bottom fifth and clear of the right edge. Switch off Instagram's auto-captions so they don't double.
6. **Voices:** every line is a separate dubbed track from cast original voices (tool-generated voices only if Bryce rules them in). Never an imitation. Sanchez is under 3 s per line with one pause, Oliver uses a quick setup then the punchline on the hold, B-1000 lands each line on a hold, and the Huggables never lip-sync.
7. **Music (original only; no licensed tracks, library tracks or lyrics):** the two-note news sting (C1 tail into the sting); the mock-heroic brass-and-strings cue from C3's plant to C4's touchdown, cut dead on "THEIR"; silence through C5; then the ledger/upload sound design. Who makes the original music is open item 10.
8. **SFX (original, all [BBG News invention]):** servo whine and clunks, breeze, fryer sizzle, crunch, boot clanks, pad hum and "whump", wind rush, landing thud, banner flap, jaw clack, the "kssht" (one sample, used twice), slam, plink ×3, stamp, bleeps.
9. **Generated audio:** use the Seedance audio as a timing guide only. Strip all generated speech and any generated music. Keep generated ambience only if it's clean and Bryce's tool-sound ruling allows it (open item 9).
10. **Mix:** dialogue forward; loudness about −14 LUFS for Instagram; 48 kHz AAC.
11. **Cover frame:** C2's Verdict hold, with Sanchez pointing and Oliver, cheeks full, holding the one basket up. No text in the bottom fifth, no logos.

---

## 6. Instagram post

**Caption** (template from slate §2):

> LOCAL HAZARDS Ep 1: No Bears Land. Era: classic look (BBG's 2013 default skins, set after Sanchez joined in Dec 2013). In the game: the two crashed dropships with jump pads on top (seen in game footage; the fan wiki calls them Pelican'ts), which fling you across the field to land right next to the other ship (per the fan wiki). Fan-made: everything that happens; fan take: Sanchez's unfinished rescue is a BBG News invention; the BB Zombies crash is the fan wiki's account. No Bears Land returns Nov 4.
>
> Guess the next THREAT LEVEL in the comments. Next location: Steamyard Blues.
>
> Unofficial AI fan film. Not affiliated with SkyVu.
>
> #BBGNews #LocalHazards #BattleBears #BattleBearsGold #NoBearsLand #FanFilm #FanAnimation #AIAnimation

- **AI-content label:** switch on Instagram's AI label when posting, every post, teaser included. The caption's "Unofficial AI fan film." stays as well.
- **Era caption:** the "Era:" sentence above is required (README, Era). No Steam-trailer or Steam-screenshot material is used, so "classic 2013 look" isn't needed. If any Steam frame is ever added (a cover, a comparison), caption it "classic 2013 look", never "2026".
- "Returns Nov 4" is allowed: SkyVu named No Bears Land first among the returning classics [Canon: Steam]. There are no wishlist or buy lines in the film.
- "Pelican't" is SkyVu's spelling [Canon: BB-1 soundtrack, track 11, "Get To the Pelican'ts!"]; SkyVu's comic spells it "Pelicant" [Canon, comic page via wiki]. Calling these No Bears Land wrecks Pelican'ts is [Fan-wiki], so the caption says so; the wrecks themselves are [Observed]. The jump-pad behaviour is [Fan-wiki] and is attributed as such. Nothing is captioned as SkyVu canon that isn't.
- No #SkyVu tag by default, so the tags don't imply affiliation (open item 8).

**Teaser caption (Oct 28):**
> LOCAL HAZARDS · Nov 4. A robot files field reports from real BBG maps. The scenery has never lost. Ep 1: No Bears Land. Era: classic look (BBG's 2013 default skins). In the game: two crashed dropships with jump pads on top (seen in game footage) that land you right next to the other ship (per the fan wiki). Fan-made: everything that happens. Unofficial AI fan film. Not affiliated with SkyVu.
>
> #BBGNews #LocalHazards #BattleBears #BattleBearsGold #FanFilm #AIAnimation

(The teaser's last line, "Launch pad destination: the other crashed dropship.", is [Fan-wiki], so its caption carries the standard template's attribution, as slate §4 asks: "posted with the standard caption".)

---

## 7. Credits and take checklists

**Clip credits** (Seedance 2.0, 10 s, 9:16, 720p, audio, about 45 each; confirm every quote before submitting, and stop and re-plan if a clip quotes more than 45):

| Item | Clips | Credits |
|---|---|---|
| Base: C1–C5 | 5 | 225 |
| Retake allowance: C4 up to 3 (slate §5) | 3 | 135 |
| Retake allowance: one each for C1, C2, C3, C5 | 4 | 180 |
| **Planned ceiling** | 12 | **540** |
| Contingency: the C4 fallback split (C4a + C4b), only after 3 failed C4 retakes | 2 | 90 |
| Contingency: the C2 split (C2a + C2b), only after both C2 takes fail | 2 | 90 (45 if a passing entrance-and-Verdict window is reused as C2a) |
| Contingency: the C5 three-wave take, only after five copies morph in both C5 takes | 1 | 45 |
| **Absolute ceiling** | 17 | **765** |

- Expected spend on the slate's 1.5× rule: about 340.
- Every retake comes from the season-wide pool (about 970), which Ep 1 draws on first. If Ep 1 used its whole planned allowance plus every contingency (540), about 430 would be left for Eps 2–8.
- **Image credits (not in the clip total):** 4 plates (P1–P4) and 4 start stills (C1, C2, C3, C5; C4 starts on P3), plus 2 end stills (C2, C4) only if the no-placeholder fallback is used. On Oct 15, Nano Banana Pro billed 2 credits per 2k image, so about 16 credits (20 with the end stills), or about 24–28 with rerolls; confirm the quote.
- The Sanchez sheet, the Huggable fix and the blue main sheet belong to the sheet queue, not this budget.
- The teaser costs 0 credits.

**Retake rules.**
- Keep a take if a usable window of the target length passes its checklist; never retake for a flaw outside the window.
- A retake may change only the action sentence's wording, never a character line, scene line or suffix. The one exception is the C5 wave-size change ("Five identical copies of" to "Three identical copies of", and "their five blue banners" to "their three" in the still), which changes the subject prefix and needs Bryce's approval in advance (open item 5).
- Fix stills by rerolling the still (2 credits), never the clip.

**Checklist for every clip** (STYLE.md habit 5; the full negative lists applied as a checklist):
- No morphing, extra limbs, melted props, or gear that changes within the take or differs from the Element.
- No broken face rule.
- Nothing the teen rating bans: blood, gore, organs, slurs, sexual content or innuendo, crude gestures, tobacco, alcohol, drugs.
- No text, lettering, logos or watermarks anywhere; no ink outlines; no low-poly or flat-2D look; no photoreal fur.
- No scene cut and no slow-motion float inside the take.
- Noon light unchanged: no dusk, haze, fog or overcast.
- Wrecks clean, with no smoke, fire, scorch or crew; a stubby cartoon dropship, never Halo- or Aliens-like.
- No yellow stripes on trench lips; no mascot or lettering on the food stand.
- Faces and landing spots clear of the bottom fifth and the right edge.
- No unnamed extra bear.
- **Shared negative, kept once:** photorealistic fur, realistic anatomy, blood, gore, sexual content, real-person likeness, official logos, text, watermarks, morphing, extra limbs, low-poly, flat 2D.
- **Map line (sheet §6):** photorealistic textures, realistic grass blades, ink outlines, night, dusk, sunset, golden hour, overcast sky, heavy haze, rain, snow, ground fog, lava, water in trenches, mud, puddles, barbed wire, shell craters, dead trees, ruined buildings, burning wreckage, smoke columns, medieval castle, crenellations, palm trees, sandy beach ground, sand dunes, snowmen, holiday decorations, floating island, empty void beyond the edge, lettering on signs, mascot emblem.

**C1 (B-1000, solo):**
- The rail-gun is on his own right forearm (the viewer's left in a front view), the cyan claw gauntlet on his left, the white winged jump-pack on his back. No paws or fingers below either weapon. Nothing held in a hand. No orb or drone. No Satellite.
- **Known sheet flaw** (SHEETS.md QA, Minor; `sheets/b-1000.jpg`): the current sheet shows a dark fist gripping the rail-gun, a black fist behind the claws, and no chest disc or claw hose, and takes conditioned on it will tend to copy that. Reject a take with a fist on the rail-gun, a fist behind the claws or no chest disc, unless Bryce has recorded a deliberate exception for C1 (§0, blocker 5); with the fixed sheet, this check should simply pass.
- Two narrow cyan eye-slits; the brow plate and eye-slits act; the jaw plate drops only a little.
- A small, plain, unlit chest disc: no glowing reactor, no emblem, no numbers or lettering on the armour.
- Glossy maroon armour, not gold, bright pink, chrome or liquid metal. No fur or plush.
- Robot staccato: snaps into dead-still holds, with enough held frames for four lines (8.5 s).
- The pad on the hull top is visible and clear of the right edge, for the HUD lock. The hull has tomato-red bands.
- B-1000 negatives, kept as checks: photorealism, flesh, organs, oil-blood or red liquid, human or skull face, liquid-metal or chrome humanoid, slim android, cute anime eyes, free-flying drone, eye lasers, bubble or dome shield, glowing chest reactor, numbers or lettering on the armour, Transformers or Terminator likeness, melting or changing weapon parts, mirrored weapon layout, labels, callouts, name title, colour swatches, hex codes; solo-only: fur, plush texture, hand-held weapons, paws, fingers, gold armour, bright pink armour; signature kit: electric arcs, lightning, red or pink beam.
- **Also test here:** did Seedance accept `start_image` with the Element placeholder, and did frame 0 hold? Record the result in SHEETS.md before C2–C5.

**C2 (Sanchez and Oliver, food stand):**
- **Sanchez:**
  - The visor stays opaque, with no eyes, pupils or brows; only its inner glow band moves.
  - The whole right arm is red-and-black, forearm and fist included, not grey or silver (the SHEETS-prompt gap noted in `element_prompts.json`).
  - The red lamp is on the outer forearm and the dark grey glove on the left hand. No gun, rifle, blaster or blade.
  - The Verdict reads clearly: feet wide, chest out, chin up, left hand flat on the chest plate, right arm pointing.
  - None of: human face, blue or green visor, sombrero, poncho or any stereotype costume, real military insignia, third-party costume.
- **Oliver:**
  - A snug red headband with no tails; red wristbands (plain) and red knee bands, each knee band with one silver-ringed red stud at the front; the crossed brass bandolier; the pale grey-lavender hex plate set high.
  - The smirk lifts on his right side and the brows act. No green harness, launcher or rifle, clothes, gold skin or blue circuitry.
- **Both:** the same height when standing; exactly one basket, on the grass beside Oliver until he scoops it up for the offer; food reads as fried food, never a drink; the pointing is a pose, not a crude gesture.
- Dropped for co-stars (STYLE.md, Co-stars in frame): Oliver's "pants or shirts" and "red glowing eyes" (Sanchez's camo and visor); Sanchez's solo-only line.
- **If the basket offer muddles the entrance in both allowed takes,** split it: C2a (the entrance and Verdict) and C2b (Oliver's offer, a start still from C2a's last frame). Both are new clips, so +90 from the pool, or +45 if a passing entrance-and-Verdict window from an existing take is reused as C2a (in the ceiling; open item 14).

**C3 (up the wreck):**
- Oliver stays tucked under the mechanical arm the whole take. Check the contact point closely: no limbs fused, swapped or added where the two bodies touch.
- The basket stays in Oliver's arms.
- He climbs the wing, not a ladder or ramp. The boots plant on the octagonal pad (yellow-and-black rim, cyan star core).
- Tomato-red bands; no smoke.
- The pride smile is small and closed-mouthed, and lands after his line, on the hold.
- Both faces stay readable: at least about a tenth of the frame height.
- Plus every C2 character check.

**C4 (the launch):**
- One continuous arc readable against the sky. They land **beside** the hull, never on top of it ("right next to the opposite spacecraft" [Fan-wiki]).
- No jet flames, jetpack plumes or wings on Sanchez: the pad threw him.
- Oliver stays tucked; the basket stays. A squash on landing, then a hard hold.
- Royal-blue bands on the hull. No Huggables, nor any other character, in this shot.
- No floaty slow drift (STYLE.md habit 3). The landing sits above the bottom third.
- Plus every C2 character check.
- After 3 failed retakes, switch to the fallback split.

**C5 (the Huggable wave):**
- Exactly five, identical, never merging or multiplying.
- Hot-pink plush paws inside the jaws, not peach skin (the SHEETS fix). Black bear-trap jaws on both paws of each.
- The red button eye, scar, cream bandage and olive radio on each teddy's own right (the viewer's left); a red-ball antenna.
- Blue banners showing a white circle, triangle and square stacked top to bottom: no letters or logos.
- Grins never move and teeth never part. No thumbs.
- The hug pose leans in on toes with arms forward; not the T pose.
- No bear in frame (the character line mentions "a teddy-bear soldier" for scale only).
- No step toward camera inside the used window. No contact.
- Huggable negatives, kept as checks: greeting-card cuteness, tummy emblem, pastel colours, washed-out colours, thumbs, organs, readable profanity, chrome, blue gems, knee brace, exposed metal plating (judged on the teddies, not the hull), neon green outlines, crystal pillar, handheld gun, launcher, muzzle flash, gum box; solo add: brown fur, realistic animal.
- If five copies morph in both allowed takes, retake as three: a third C5 clip (+45, in the ceiling) that changes the subject prefix, which the retake rule allows only with Bryce's advance approval (open item 5).

---

## 8. Open items for Bryce

1. **Old low-poly Elements in Higgsfield** (§0): delete or rename `oliver-soldier`, `huggable-huggable` and `riggs-heavy` in the web UI before the new ones are made, or accept suffixed names. Recommended: retire them, so nobody can attach a low-poly sheet.
2. **Tool-generated voices:** are they "original performers"? This is due this week: B-1000's four C1 lines must be cast, recorded and dubbed by Mon Oct 26 for the Oct 28 teaser, and the rest of Ep 1's voices before the Nov 1 lock. If no voice is ready by Oct 26, the teaser runs with servo SFX and captions only, or posts later (§0).
3. **Sanchez's sheet and the Huggable fix** after the Oct 21 reset; then **the blue main sheet**. Approve each after QA. C4 goes first once Sanchez passes; C5 waits for the blue sheet.
4. **Derived scene lines and plates:** the red and blue wreck lines (now with the sheet's three pods plus the snapped-off fourth, the establishing shot's stacked cyan rings over the pad, and, in the red line only, the sheet's furrow), P2 (food stand), P3 (blue wreck wide) and P4 (blue wreck from the landing spot) aren't in `environments/no-bear-s-land.md`. Approve them as written, or have them added to the sheet first. Later episodes will reuse the wreck lines.
5. **Wave size in C5:** five Huggables (proposed), or three if takes morph. The switch to three is a third C5 clip (+45, in §7's ceiling) and changes the subject prefix, so approve it in advance as the one exception to the retake rule.
6. **Element name for the blue main sheet:** `huggable-huggable-blue` (proposed; SHEETS.md has no blue rows yet). Add it and the UUID to SHEETS.md.
7. **End card "AI" wording** ([Open] in the README). The default is the README card word for word. The AI disclosure is carried by the caption and the platform label.
8. **SkyVu wording in the post:** BBG News is SkyVu-approved, but the README's end card and caption say "not affiliated". Should the post mention approval at all? Default: no mention, unless SkyVu supplies the wording. Also, no #SkyVu tag by default (the Oct 15 package used one).
9. **Generated audio:** keep `generate_audio` on (the 45-credit figure assumes it), or get a quote with it off, since every voice and most sound gets replaced? And may clean tool-generated ambience stay in the mix?
10. **Who makes the original music:** the news sting and the mock-heroic cue. Human-composed, or tool-generated (the same question as item 2)?
11. **The carry:** under-arm (proposed, for reliability), or Oliver seated on the raised mechanical forearm (funnier, but riskier for morphing).
12. **A "BBG NEWS · FAN FILM" corner bug** on every episode from frame 1: yes or no.
13. **Sanchez's accent:** the wiki gives him a Spanish accent [Fan-wiki]; sanchez.md allows any fluent accent, never a caricature, and keeps Spanish to short phrases. Ep 1's lines have no Spanish. Cast with or without an accent?
14. **C2 split:** approve +90 from the pool if needed, or +45 if a passing entrance-and-Verdict window is reused as C2a (§7, C2).
15. **Catchphrase rule reading:** C2 ("we'll getcha... home") and C5 ("...Mayday.") both quote fragments of his one BB Zombies radio line [Fan-wiki]. This package counts them as one known line (sanchez.md: at most one known line plus one deflation; no deflation is used). Confirm.
16. **B-1000 sheet (§0, blocker 5):** queue the edit-fix of `b-1000-assault-signature` before its Element is made (recommended), or record a deliberate exception for C1 in the checklist.
