# BBG News: LOCAL HAZARDS · Ep 1 "We'll Getcha Home": comic production script

*Unofficial BBG News fan comic. Production script v1, 2026-10-26. Bryce dropped the animated shorts today ("forget making videos. we are now making exciting comics."). This script adapts the locked Ep 1 package (`series/episode1_package.md`) into a swipeable Instagram carousel. It merges the two Oct 26 drafts (A faithful, B excitement first) and applies the Oct 26 carousel research. Built from `series/season1_slate.md`, `characters/STYLE.md`, `characters/README.md`, the souls `b-1000.md`, `sanchez.md`, `oliver.md` and `huggable.md`, `characters/sheets/SHEETS.md`, `environments/no-bear-s-land.md` and the lettering engine (`series/comic/README.md`, `letter.py`). Labels follow the README legend and are never upgraded. Anything not labelled otherwise is [BBG News invention].*

**Status:** script only; nothing new has been generated. Every free panel (crops of approved art and the local graphics) is already built in the scratchpad, and the whole carousel has been test-lettered with `letter.py`: **zero layout warnings**, and the only warnings are the 17 missing images still to be generated. A second test with mock face boxes (engine-only `faces` key, not in the deliverable) also passes with zero warnings.

**Files in this folder:**
- `SCRIPT.md`: this script.
- `pages.json`: the 14 carousel slides plus the 2 teaser slides, in exactly the shared PAGE SPEC form (base keys only). Every panel image is `panels/<panel id>.png`.
- `panels.json`: one entry per panel (35): its prompt, Elements, references, ratio, resolution, reuse source, day and status.

**Era:** classic, Dec 2013 or later (Sanchez arrived in BBG 2.6 [Canon]). BBG 2013 default skins in the house feature-film 3D style. No Steam-trailer or Steam-screenshot material is used (No Bears Land and Sanchez are in neither [Observed]), so no panel needs its own "classic 2013 look" tag; the caption's Era sentence names the era as "classic 2013 look".

**Bryce's decisions this script follows:** the feature-film 3D house style (every panel a polished animated-movie still built with the existing souls and Elements); an Instagram carousel of portrait slides at 4:5, 1080×1350, at most 20; Ep 1 adapted for Wed Nov 4; the cover doubles as the Wed Oct 28 teaser. "Exciting" is his word, so every slide is built to be punchy and fun to swipe.

---

## 0. How this script was chosen

Both drafts were read in full and scored out of 10 on the five criteria in the brief.

| Criterion | Draft A (faithful) | Draft B (excitement first) | Notes |
|---|---|---|---|
| Story fidelity | 9 | 8 | A keeps every beat in package order and gives "...That's THEIR ship." its own swipe. B adds a SCOOP walk the package keeps in the cut and puts HOME and THEIR on one slide. Both keep every locked line word for word. |
| Excitement and swipe pull | 6.5 | 9 | B: full-page Verdict, "This arm..." and Huggable splashes, the solemn line turning over to "But LOOK at it." on the swipe, a stand-alone slide 2, a 2-slide teaser. A: 29 panels, several small, and many multi-panel slides. |
| Soul and canon fidelity | 9 | 8.5 | Both are clean. B's Huggable prompt lacks the viewer-terms side clause that SHEETS.md's Oct 25 diagnosis says the model needs. |
| Lettering room and readability | 6 | 8.5 | A letters at 30–36 px, under the research's 42 px dialogue target. B uses 42–52 px, at most about 35 words a slide, and keeps out of Instagram's slide counter. |
| Production cost | 9.5 | 5.5 | A: 8 generations, 22 credits. B: 11 (+1 optional), about 30 credits, about 15 with retakes, five of them 4K, and four full-bleed slides that break the shared spec's 40 px margin. |
| **Total (equal weights)** | **40** | **39.5** | |
| **Total (excitement double, as Bryce asked)** | **46.5** | **48.5** | |

**Spine: Draft B.** Its slide order through the launch, its full-page splashes, its stand-alone cold open, its research-sized lettering, its send-and-follow end card, the 2-slide teaser and the five-hashtag caption.

**Grafted from Draft A:**
- **Its economy.** 8 new generations, not 11–12. B's SCOOP walk (its G05) is cut, its separate arc splash (G08) becomes a crop of the cover, and its optional boots shot (G12) and B-1000 "tee-hee" (G11) become free crops of G05 and the approved C1 still. B's "Admiration" close-up stays (G06 here): the solemn-to-proud turn is Sanchez's soul in one swipe.
- **Its cover.** The flight at the top of the arc is the episode's signature image (C4). It spoils nothing, its upper third is naturally sky for the title, and a level camera keeps both faces big (B's steep low angle foreshortens them). It is reused inside as the arc splash, so one image does the work of B's two (its G01 and G08).
- **Its launch-to-punchline pacing.** The empty pad going WHUMP (free, from approved P1), then the arc; "HOME." and a silent blue band on one slide; "...That's THEIR ship." opening the next, with the music caption cut to "HEROIC BRA--". The research's page-turn rule (suspense at the bottom, reveal at the top of the next swipe) favours A here.
- **Its deadpan cold-open gag.** Two identical "crashed dropship" panels.
- **Its free graphics.** The sting band, the ledger card with three Joule-style tokens, the 99% bar and the pink stitched-seam glitch, all original art drawn by script.
- **P1b.** A local recolour of approved P1 to royal-blue bands, used as the blue wreck's design reference, so it stays P1's chunky cartoon dropship (P3's airliner nose is the failure to avoid). This script's version also recolours the tail and wingtips.
- **The Huggable's viewer-terms clause** and its fallback shot, and the 40 px-margin layout (no full-bleed slides).

**New in this script:** "ONE SCOOP LATER..." as the gutter caption for the hoist the package keeps off screen; the cover HUD "DESTINATION: HOME?", which the cold open answers ("...the other crashed dropship"); the silent visor answering "...Fry?"; the end card's blank THREAT LEVEL tag next to B's send line.

---

## 1. Pitch and counts

The carousel is B-1000's live feed, and it moves at swipe speed. Slide 1 is the hero shot: Sanchez flying high over the trenches with Oliver and the fries under his arm, under WE'LL GETCHA HOME, while B-1000's lock ring asks "DESTINATION: HOME?". Slide 2 answers in four deadpan HUD lines (it works alone when Instagram re-serves the carousel from slide 2): the destination is "the other crashed dropship". Then every swipe lands one beat, and every slide ends on a question the next one answers at the top:
- a red visor and a clunking arm cut into Oliver's lunch (who's that?);
- "Oliver, we'll getcha..." holds its one pause before "...HOME." (Oliver's reaction is held back);
- "...FRY?" gets a silent visor stare (what does a solemn man do with a fry?);
- "ONE SCOOP LATER...": "This arm, I did not ask for." (but?);
- "But LOOK at it." as the pad hums VMMMM under their boots (launch?);
- WHUMP: the pad is suddenly empty, and the cover comes back as the arc splash (where do they land?);
- THOOM. "HOME." Then a silent blue band and an off-panel "..." (what's wrong?);
- "...That's THEIR ship." The music caption dies mid-word; FWAP from off-panel (what flapped?);
- the swipe is the hard cut: five blue Huggables, arms wide, KSSHT, and "...Mayday.";
- the ledger: SCENERY 1 · BEARS 0, METHOD: DELIVERED TO THE WRONG SHIP, upload stuck at 99%;
- KSSHT again (the same SFX as the Huggables: hijacker clue 1), REROUTING... TO: EVERYONE, "TEE-HEE.";
- the end card: the comment game, the send line and the README end card.

**Counts:**
- **14 carousel slides** (s01–s14) plus **2 teaser slides** (t01, t02, posted Oct 28). Research: 8–14 slides perform best; 20 is the cap.
- **35 panels**: 28 in the carousel, 7 in the teaser.
- **8 new Nano Banana Pro generations, the cover included: 22 credits.** With about 30% retakes (3), about 11 generations and about 31 credits. The hard ceiling, with every optional shot, is 14 (§8).
- **Free (0 credits):** 9 crops of the new generations; 13 crops of approved art (the C1 start still, plate P1 and one frame of the C1 clip at 7.0 s, inside its clean 0–8.4 s window); 5 local graphics.
- **The B-1000 Element is not needed:** every B-1000 panel reuses the approved C1 still or clip.
- **The Huggable panel is generated last**, and it **needs the blue Huggable Element** `huggable-huggable-blue` (not yet made).

### Beat map (episode → comic)

| Episode beat (package §3–§4) | Slides | How the timing becomes panels |
|---|---|---|
| C1 cold open, four lines on holds | s02 (and the cover's question) | One line per panel. Lines 2 and 3 sit on two identical panels (the deadpan hold). Line 4 gets B-1000's shout and the lock on the pad |
| Title sting | s03 top band | "LOCAL HAZARDS" over a scan-line band, plus "DUN-DUNN!" |
| C2 food stand, the Verdict, "...Fry?" | s03–s05 | The FLUFFY tag on Oliver mid-bite; the visor cutting in as the swipe hook; a full-page Verdict with the pause as two balloons; "GREAT!", then "...FRY?", then a silent visor |
| C3 up the wreck | s06–s07 | The hoist happens in the gutter ("ONE SCOOP LATER..."). The grand half of the line on a full page, the pride half after the swipe; the pad hum as SFX |
| C4 launch, arc, "Home." / "...That's THEIR ship." | s08–s10 | The empty pad goes WHUMP; the arc splash (the cover paying off); THOOM and "HOME."; a silent band; the punchline opens s10 and cuts the music caption |
| C5 reverse, kssht, "...Mayday." | s10 hook → s11 | FWAP from off-panel ends s10; the wave is a full-page splash; the next swipe is the hard cut |
| Sign-off and end card | s12–s14 | Ledger, plinks, METHOD, stamp, VO and the 99% bar; the pink glitch, KSSHT, REROUTING, "TEE-HEE."; the CTA and the end card |

---

## 2. Format and lettering rules

### 4:5 at 1080×1350 (and why not 3:4)
The research checked 3:4 (1080×1440). Instagram has shown 3:4 photos in single posts and carousels since May 2025 (Mosseri, via PetaPixel and Business Today), and the profile grid crops every post to 3:4. But Meta's Graph API still accepts only 4:5 to 1.91:1 (IG User Media reference), and the repo's own posting path (`instagram.py`) uses the Graph API. Guides also disagree on whether every account gets 3:4 (Krumzi, Sep 2026), and the gain is only about 6.7% more height. **The evidence is not strong, so this script delivers 1080×1350 pages.** 3:4 is worth one manual test post later. The cover keeps its faces and title inside the central 1012 px column that the 3:4 grid keeps, which the 40 px margin already covers.

### Layout
- A 40 px outer margin on every slide. Gutters of 20 px. No full-bleed panels. The cover and the teaser cover have no border; every other panel has a 6 px border.
- Nothing lettered in the top-right ~140×90 px (Instagram's "1/14" slide counter). Nothing important in the bottom-left corner (the tag icon).
- Every panel image is pre-cut to its panel's shape (crop recipes in `panels.json`), so `focus` is [0.5, 0.5]. The exceptions are the raw generations shown whole (p01, p08, p10, p11, p14, p15, p19, p23), whose focus is set from the prompt's composition.
- Balloon and tail positions on new art follow each prompt's intended composition. They get their final values from `letter.py --guides` once each image lands: move a balloon before regenerating a panel.

### Lettering (research §3, for a 1080 px slide read on a 375–440 pt phone)
- **Sizes:** dialogue 44–58 px (floor 34), captions 34–46 px, the whisper 38 px, B-1000's HUD 30–50 px (30–32 only for short labels in small panels, at the engine's floor), SFX and titles fill their boxes (120 px and up for the big ones).
- **Words:** at most 15 words per balloon, at most 3 balloons and about 35 words per slide (only s12, the ledger, reaches 30; s14's end card is small print).
- **Order:** the first speaker top-left, then down and right; tails never cross; tails stop short of faces (the engine's `tail_gap`).
- **Faces:** Comic Neue Bold dialogue in capitals, `**emphasis**` in bold italic, the crossbar I only for the pronoun; Bangers for SFX and titles; Share Tech Mono for B-1000's HUD (cyan box, corner brackets, a leader to a lock ring); Barlow for the end card. No new font is needed.
- **Punctuation:** three-dot ellipses; a double dash for the cut-off music caption ("HEROIC BRA--"), never an em dash (Blambot).
- **Engine extras (optional):** `pages.json` uses only the base PAGE SPEC keys. If the lettering engine supports these documented extras, they are worth adding at render time; a renderer that ignores them still draws valid pages.
  - `"fill": "#ff6fb5", "fill2": "#d6337f", "outline": "#2a0a1a"` on **both** "KSSHT" SFX (s11 and s13). The same pink on both is the hijacker clue.
  - `"live": true` on B-1000's opener (s02, t02), for the red "● LIVE" tag.
  - `"fill": "#d7263d", "outline": "#f4f1e8"` on the "REAL MAP. FAN-MADE NEWS." stamp (s12).

---

## 3. Production plan

### Shared prompt parts (word for word from the sources)
- **Element placeholders** go immediately before the words that describe that character:
  - Sanchez: `<<<e6122a2f-99de-423a-a310-733554bf48bb>>>` (`sanchez-arbiter`, the unarmed Element).
  - Oliver: `<<<74170e99-a46a-4c7d-857c-d3046b839374>>>` (`oliver-soldier`, the current Element; never the deleted 85977ecb).
  - The blue Huggable: the neutral slot `<<<E1>>>`. Replace `E1` with the bare UUID of `huggable-huggable-blue` (main sheet, jaws on) once it is in SHEETS.md. That Element doesn't exist yet: the red sheet v4 (job 321fe5d6) is under review, then the blue edit.
  - `b-1000-assault-signature` (`afb181b2-…`) and `riggs-heavy` are not used: B-1000 is all reused art, and Riggs isn't in Ep 1.
  - At most two Element characters per image (STYLE.md habit 4); the five Huggables count as one.
- **Character lines:** Sanchez's from his soul's video starter; Oliver's from his starter, with the package's co-star words ("as tall as the cyborg") and its carry clause ("tucked firmly under his mechanical right arm and hugging a softly glowing red basket of golden fried food"); the Huggable's from its starter with the blue-team change and the package's "Five identical copies of" prefix.
- **Scene lines:** the package's red-wreck and blue-wreck lines (§2), the environment sheet's "Food stand" line and, for the flight, its "Open field, wide" line. Each carries the episode's one light rig word for word.
- **Closing, in this order:** the camera sentence; a sentence naming the empty space the lettering needs, ending "left clear; a clean image with no text."; STYLE.md's short "Avoid: photorealistic fur, realistic anatomy, real-person likeness, official logos, text, watermarks." (Nano Banana Pro has no negative field); the framing line for the panel's ratio ("Vertical 4:5 framing.", "Horizontal 3:2 framing.", "Horizontal 5:4 framing."), in place of STYLE.md's "Vertical 9:16 framing."; and the video suffix, always last (STYLE.md has no still suffix; the approved C1 still used this one).
- **Never in a prompt:** names, map names, weapon names, hex codes, spoken words, HUD text, tags, SFX, "comic", "dropship", "slow" or "solemn". Every word on a slide is added by `letter.py`.

### Local references (made for free, in the scratchpad)
- **P1b** (`/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/comic/final_work/refs/P1b_blue_hull.png`): approved P1, hull and hilltop only, with its tomato-red bands shifted to royal blue. Design reference for the blue wreck (G07, G08).
- **P3r** (`/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/comic/final_work/refs/P3r_field.png`): plate P3's right half only (field, sandbags, the trench zig-zag, hills). The airliner-like nose is cut out. Field reference for the flight (G01); it needs Bryce's OK (open item 1), and G01 runs with no location reference if he says no.
- **P2** (job 01ca9909): the food-stand reference for G02 and G03, only if Bryce approves it as a reference. Its centred parasol doesn't matter, because each prompt sets its own framing.
- **P3 is not redone and P4 is not made.** The comic needs neither, which saves two generations.
- The builder for every free panel and both references is `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/comic/final_work/build_assets.py`, driven by `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/comic/final_work/build_layout.py` (one source for the layout, the crops and the prompts).

### Generation ledger (8 new generations; the cover counts)

| Gen | Panel id (+ free crops) | Slides | Shot | Elements | Image references | Ratio | Res | Credits | Day |
|---|---|---|---|---|---|---|---|---|---|
| G01 | p01 (+ p18, t01a) | s01, s08, t01 | The cover: the flight at the top of the arc | Sanchez, Oliver | P3r | 4:5 | 2k | 2 | Tue Oct 27, first |
| G02 | p08 | s03 | Oliver mid-bite, high angle | Oliver | P2 (if approved) | 3:2 | 2k | 2 | Tue Oct 27 |
| G03 | p10 (+ p09, p13) | s04, s03, s05 | The Verdict, low angle past Oliver's shoulder | Sanchez, Oliver | G02, P2 (if approved) | 4:5 | 4k | 4 | Tue Oct 27 |
| G04 | p11 (+ p12) | s05 | Oliver's guilty basket offer, Sanchez's point of view | Oliver | G02 | 3:2 | 2k | 2 | Wed Oct 28 |
| G05 | p14 (+ p16) | s06, s07 | Planted on the red wreck's pad, low angle | Sanchez, Oliver | P1, G01 | 4:5 | 4k | 4 | Wed Oct 28 |
| G06 | p15 | s07 | The pride smile, eye level | Sanchez, Oliver | G05 | 3:2 | 2k | 2 | Wed Oct 28 |
| G07 | p19 (+ p20, p21, p22) | s09, s10 | Landed beside the blue wreck's nose | Sanchez, Oliver | P1b, G01, P3r (if approved) | 5:4 | 4k | 4 | Wed Oct 28 |
| G08 | p23 | s11 | The blue Huggable wave (**needs the blue Element**) | blue Huggable ×5 | G07, P1b | 4:5 | 2k | 2 | Fri Oct 30 |

- **Base: 8 runs, 22 credits.** 4K only where the image is cropped again tightly (G03 into the visor panels, G05 into the boots, G07 into three close-ups). G01's crops stay above 1:1 source pixels at 2k.
- Confirm every quote before submitting (on Oct 15, 2k was 2 credits and 4k was 4).
- The research's "draft at 1K, final at 2K" is not used: it doubles the runs, and the 5-a-day cap can't carry it.

### Checklist for every new image (package §7 lists, used as checks, since there is no negative field)
- **Lettering space:** no text, letters, numbers, speech bubbles, logos or watermarks anywhere, and the stated space really is clear.
- **House style:** no ink outlines, no low-poly or flat-2D look, no photoreal fur.
- **Light and set:** noon light unchanged (no dusk, haze or overcast). Wrecks clean, with no smoke, fire or crew, and a chunky stubby cartoon dropship like P1, never Halo-, Aliens- or airliner-like. The food stand blank, with no mascot. No yellow stripes on trench lips.
- **Cast:** no unnamed extra bear; no morphing, extra limbs or melted props; no gear that differs from the Element; nothing the teen rating bans.
- **Sanchez:** opaque visor (no eyes, pupils or brows; only the inner glow band acts). The whole right arm red-and-black, with the red lamp on the outer forearm. Dark grey glove on the left hand. No gun or blade. No sombrero, poncho or any stereotype costume. The pointing is a pose, never a crude gesture.
- **Oliver:** snug red headband with no tails; red wristbands; red knee bands, each with one silver-ringed stud; crossed brass bandolier; the smirk and the cocky brow on his right side. No harness, launcher or rifle.
- **Both:** the same height when standing. **Exactly one basket**, and it is fried food, never a drink.
- **The carry** (G01, G05, G06, G07): no fused, swapped or extra limbs where the bodies touch; the basket stays in Oliver's arms; no jet flames, plumes or wings on Sanchez (the pad threw him).
- **The Huggables** (G08): the package's C5 list (§5 below).

### Retake rules (package §7, adapted to stills)
- Retake only for a flaw that lands inside the panel or one of its crops. Fix a framing problem by moving the crop, the focus or a balloon first.
- A retake changes only the action or camera sentence, **or** the reference image, never both (Higgsfield's own advice), and never a character line, scene line or suffix.
- The one exception is the Huggable wave size (five → three), which needs Bryce's advance approval (package open item 5).

---

## 4. The cover (s01) and the Oct 28 teaser (t01, t02)

### s01 · The cover
**Design.** A full-page hero shot inside the 40 px margin with no border. Sanchez flies left to right across the middle third at the top of the pad's huge arc: gloved fist forward, chin up, visor band narrowed, both faces turned three-quarters to camera. Oliver is clamped under the mechanical arm (flying right puts his right side, the arm and Oliver, toward the camera), hugging the glowing basket with a fry in his mouth while fries tumble out behind. The trench zig-zag crosses the noon field far below. The upper third is open sky for the title. B-1000's HUD frames it as his live feed, and its lock ring on Sanchez asks the question the cold open answers. Nothing about the blue wreck or the Huggables is shown, so nothing is spoiled. The same image comes back inside as the s08 arc splash, so the cover's promise pays off.

**Panel:** p01 [40, 40, 1000, 1270]

**G01 → p01** (4:5, 2k; Elements: Sanchez, Oliver; reference: P3r), paste-ready inside the quotes:
> "<<<e6122a2f-99de-423a-a310-733554bf48bb>>> A lean teddy-bear cyborg in a dark maroon helmet with rounded bear-ear bumps and an opaque glowing red visor hiding his eyes, a light tan muzzle with a small dark goatee, a grey-khaki chest plate over grey-and-white camo, olive-and-tan camo trousers, a dark grey glove on his left hand and an oversized red-and-black mechanical right arm. With <<<74170e99-a46a-4c7d-857c-d3046b839374>>> a chestnut-brown robotic teddy-bear soldier, soft plush all over, with a red headband and a brass-cartridge bandolier, as tall as the cyborg, tucked firmly under his mechanical right arm and hugging a softly glowing red basket of golden fried food, he soars across the sky at the top of one huge, high arc in a heroic flying pose, body stretched out level and turned three-quarters toward the camera, his gloved left fist thrust forward, chin up, mouth set firm, the glow band inside his visor narrowed, while the soldier clutches the basket to his chest with wide eyes, both brows shot up and a golden fry clamped in his mouth, a few golden fries tumbling out behind them and long crisp white streaks of rushing air trailing behind them. A sunlit open grass field at high noon, short, soft, stylised yellow-green turf flecked with tiny white daisies, plump curved arcs of tan sandbags and a few chunky black steel barriers of three thick crossed beams like giant toy jacks on gentle mounds, misty blue-grey wooded hills on the horizon, under a saturated mid-blue sky with big soft white cumulus clouds, the high sun as a slightly warm key with a soft cool fill from the sky and a gentle rim light on the characters. Medium-wide shot from high in the air, level with the two as they fly from left to right across the middle third of the frame, slightly right of centre, both faces large and clear; far below, an S-shaped zig-zag of sunken trenches with honey-gold plank floors and plain grass-capped lips crosses the field in the bottom third. The upper third of the frame is open blue sky with only soft clouds, left clear; a clean image with no text. Avoid: photorealistic fur, realistic anatomy, real-person likeness, official logos, text, watermarks. Vertical 4:5 framing. Polished feature-film 3D animation, soft rounded shapes, expressive faces, soft plush fur, soft global illumination, cinematic lighting, snappy cartoon timing with strong poses and holds."

- Not for pasting. Extra checks: no jet flames, plumes or wings on Sanchez; Oliver stays tucked; the upper third stays empty sky; both faces at least about a tenth of the frame height. If the faces read small, the retake changes only the camera sentence ("Medium shot from high in the air, ...").
- **Teaser fallback:** if G01 fails twice on Oct 27, t01 posts on Oct 28 over the approved C1 still (the t02a crop, refit to 1000×1270) with the same lettering, at 0 credits, and G01 retries on Oct 28 for s01 and s08.

**Lettering:**
  - **hud** "BBG NEWS · LIVE / LOCAL HAZARDS · EP 1" · panel p01 · box [72, 72, 520] · 34 px
  - **title** "WE'LL GETCHA" · panel p01 · box [110, 180, 860]
  - **title** "HOME" · panel p01 · box [340, 318, 400]
  - **hud** "DESTINATION: HOME?" · panel p01 · box [640, 930, 380] · tail → [700, 540] · 34 px
  - **hud** "SWIPE >>" · panel p01 · box [830, 1222, 180] · 30 px

### t01 + t02 · The Oct 28 teaser (a 2-slide carousel, 0 extra credits)
The research says carousels out-reach single photos and that the teaser tile should differ from the Nov 4 cover on the grid, so the teaser is two slides. It rebuilds the old video teaser (C1, then a "Nov 4" super, then the end card) as panels.
- **t01:** the cover art zoomed about 1.12× (crop `t01a`), with the kicker, the title, a "NOV 4" stamp and the swipe cue.
- **t02:** the cold open (all approved art, ready now), with "LOCAL HAZARDS · NOV 4" and the README end card under it, so the post carries the card.
- Render with `letter.py pages.json --only t01,t02 --jpg`. These pages are not part of the Nov 4 carousel.

**t01 panel:** t01a [40, 40, 1000, 1270]
  - **hud** "BBG NEWS · LOCAL HAZARDS" · panel t01a · box [72, 72, 560] · 34 px
  - **title** "WE'LL GETCHA" · panel t01a · box [110, 170, 860]
  - **title** "HOME" · panel t01a · box [340, 306, 400]
  - **sfx** "NOV 4" · panel t01a · box [650, 1010, 330] · angle 8
  - **hud** "SWIPE >>" · panel t01a · box [830, 1222, 180] · 30 px

**t02 panels:** t02a [40, 40, 1000, 560] · t02b [40, 620, 490, 240] · t02c [550, 620, 490, 240] · t02d [40, 880, 330, 250] · t02e [390, 880, 650, 250]
  - **hud** "B-1000. LIVE. / SCANNING LOCATION." · panel t02a · box [64, 60, 420] · tail → [498, 356] · 34 px
  - **hud** "HAZARD: / CRASHED DROPSHIP." · panel t02b · box [56, 632, 360] · tail → [420, 745] · 32 px
  - **hud** "STATUS: / STILL CRASHED." · panel t02c · box [566, 632, 360] · tail → [930, 745] · 32 px
  - **hud** "LAUNCH PAD DESTINATION: / THE OTHER CRASHED DROPSHIP." · panel t02e · box [404, 892, 620] · tail → [763, 1040] · 32 px
  - **title** "LOCAL HAZARDS · NOV 4" · box [60, 1150, 960]
  - **endcard** "Unofficial fan comic, not affiliated with SkyVu; characters © SkyVu." · default placement (bottom margin)

---

## 5. Slide by slide

Coordinates are canvas pixels on 1080×1350. "Crop of Gnn" panels are cut from that generation's full approved download (saved as `src/<panel id>_raw.png`) at the fractions given in `panels.json`, then saved as `panels/<panel id>.png` at the panel's shape. Crops of approved art give their source-pixel boxes in `panels.json`.

### s02 · LIVE (the cold open; it must also work alone)
- **Why the reader swipes:** a deadpan robot is "live" at a crashed ship, the same shot twice is the joke, and the last line answers the cover's question: the destination is "the other crashed dropship". Who's going to use that pad?
- **Panels:** p02 [40, 40, 1000, 640] · p03 [40, 700, 490, 280] · p04 [550, 700, 490, 280] · p05 [40, 1000, 330, 310] · p06 [390, 1000, 650, 310]
  - **p02:** the approved C1 start still (job de69723e): B-1000 below the red-banded wreck, the glowing pad on its roof.
  - **p03 and p04 (the same image on purpose):** the C1 still cropped to the hull, B-1000's head peeking up from the bottom edge, staring at it.
  - **p05:** the C1 clip at 7.0 s (inside the clean 0–8.4 s window): B-1000 mid-shout, jaw plate dropped.
  - **p06:** approved P1 (job 15321af3), close on the glowing pad: B-1000's point of view of the target (slate §2 POV habit).
- **Lettering** (B-1000's four locked lines, 17 words):
  - **hud** "B-1000. LIVE. / SCANNING LOCATION." · panel p02 · box [64, 64, 420] · tail → [498, 396] · 36 px
  - **hud** "HAZARD: / CRASHED DROPSHIP." · panel p03 · box [56, 714, 360] · tail → [430, 846] · 32 px
  - **hud** "STATUS: / STILL CRASHED." · panel p04 · box [566, 714, 360] · tail → [940, 846] · 32 px
  - **hud** "LAUNCH PAD DESTINATION: / THE OTHER CRASHED DROPSHIP." · panel p06 · box [404, 1014, 620] · tail → [774, 1200] · 32 px

### s03 · Sting, Oliver, and a red visor arriving
- **Why the reader swipes:** the show's title lands, Oliver is caught mid-snack with a FLUFFY rating, and a red visor and a clunking arm cut in at the bottom. Who's that?
- **Panels:** p07 [40, 40, 1000, 200] · p08 [40, 260, 1000, 700] · p09 [40, 980, 1000, 330]
  - **p07:** the local sting band (navy HUD grid, scan line). Original art, no text.
  - **p08 = G02** (3:2, 2k; Element: Oliver; reference: P2 if approved). A high angle makes him small: the panel is the FLUFFY tag in picture form.
> "<<<74170e99-a46a-4c7d-857c-d3046b839374>>> A chestnut-brown robotic teddy-bear soldier, soft plush all over, with a red headband and a brass-cartridge bandolier, sits on the grass right of centre beside the cart, frozen mid-bite with a golden fry in his mouth and another in his paw, eyes squeezed shut in bliss, cheeks stuffed full, both heavy brows lifted, the softly glowing red basket of golden fried food on the grass at his side. A sunlit daisy-flecked grass field at high noon, beside a red-and-yellow pyramid parasol with plain, unmarked panels on a single dark pole over a squat grey cart, a softly glowing red basket of golden fried food on the grass beside it, under a saturated mid-blue sky with big soft white cumulus clouds, the high sun as a slightly warm key with a soft cool fill from the sky and a gentle rim light on the characters. High-angle medium shot looking down at him from above and in front, the edge of the parasol's red-and-yellow canopy cutting across the top of the frame. The left third of the frame is plain, open daisy-flecked grass with nothing in it, left clear; a clean image with no text. Avoid: photorealistic fur, realistic anatomy, real-person likeness, official logos, text, watermarks. Horizontal 3:2 framing. Polished feature-film 3D animation, soft rounded shapes, expressive faces, soft plush fur, soft global illumination, cinematic lighting, snappy cartoon timing with strong poses and holds."
  - **p09 = crop of G03:** the glowing visor at left and the raised red-and-black arm reaching right, a 1000:330 strip from the 4k Verdict.
- **Lettering:**
  - **title** "LOCAL HAZARDS" · panel p07 · box [70, 70, 700]
  - **sfx** "DUN-DUNN!" · panel p07 · box [790, 130, 220] · angle 6
  - **caption** "The red food stand." · panel p08 · box [64, 282, 560] · 34 px
  - **hud** "SUBJECT: OLIVER / THREAT LEVEL: FLUFFY" · panel p08 · box [64, 350, 450] · tail → [640, 500] · 34 px
  - **sfx** "CRUNCH!" · panel p08 · box [90, 740, 360] · angle 8
  - **sfx** "KA-CHUNK!" · panel p09 · box [610, 1150, 400] · angle -6

### s04 · The Verdict (full page)
- **Why the reader swipes:** the reveal answers s03. The line is split across two balloons, so the reader takes Sanchez's one allowed pause before "...HOME.". Oliver's reaction is held for the next swipe.
- **Panel:** p10 [40, 40, 1000, 1270]
  - **p10 = G03** (4:5, 4k; Elements: Sanchez, Oliver; references: the approved G02, and P2 if approved). Sanchez towers left of centre, turned three-quarters to frame right so the mechanical right arm is on the near side and points down at Oliver in the lower-right foreground. The top fifth and the sky right of his head are open for the tag and balloons.
> "<<<e6122a2f-99de-423a-a310-733554bf48bb>>> A lean teddy-bear cyborg in a dark maroon helmet with rounded bear-ear bumps and an opaque glowing red visor hiding his eyes, a light tan muzzle with a small dark goatee, a grey-khaki chest plate over grey-and-white camo, olive-and-tan camo trousers, a dark grey glove on his left hand and an oversized red-and-black mechanical right arm. He has just strode in from the left with both hands empty and snapped into a hard hold left of centre, turned three-quarters toward the right of the frame, beside <<<74170e99-a46a-4c7d-857c-d3046b839374>>> a chestnut-brown robotic teddy-bear soldier, soft plush all over, with a red headband and a brass-cartridge bandolier, as tall as the cyborg, who sits on the grass in the lower right foreground with his back half-turned to the camera, frozen mid-bite beside the softly glowing red basket of golden fried food; the cyborg's feet are planted wide, chest out, chin up, his gloved left hand flat on his chest plate and his mechanical right arm raised and pointing down at the soldier, the brighter glow band inside his visor narrowed to a thin slit, his mouth open on a short line. A sunlit daisy-flecked grass field at high noon, beside a red-and-yellow pyramid parasol with plain, unmarked panels on a single dark pole over a squat grey cart, a softly glowing red basket of golden fried food on the grass beside it, under a saturated mid-blue sky with big soft white cumulus clouds, the high sun as a slightly warm key with a soft cool fill from the sky and a gentle rim light on the characters. Low-angle shot from the grass just behind the soldier's shoulder, looking up at the cyborg, who towers left of centre against the open sky, his helmet in the upper third of the frame. The top fifth of the frame above his helmet and the open sky to the right of his head are clear saturated blue sky with soft clouds and nothing else, left clear; a clean image with no text. Avoid: photorealistic fur, realistic anatomy, real-person likeness, official logos, text, watermarks. Vertical 4:5 framing. Polished feature-film 3D animation, soft rounded shapes, expressive faces, soft plush fur, soft global illumination, cinematic lighting, snappy cartoon timing with strong poses and holds."
  - Not for pasting: "holds" and "snapped", never "slow" or "solemn" (sanchez.md, Timing). Reject a take with two baskets. 4k, because p09 and p13 are tight crops of it.
- **Lettering:**
  - **hud** "SUBJECT: SANCHEZ / THREAT LEVEL: / PARTIAL UPGRADE" · panel p10 · box [64, 64, 340] · tail → [420, 304] · 32 px
  - **balloon** "Oliver, we'll getcha..." · panel p10 · box [440, 70, 470] · tail → [512, 418] · 44 px
  - **balloon** "...**home.**" · panel p10 · box [660, 270, 300] · tail → [516, 446] · 56 px

### s05 · "GREAT!" / "...FRY?" / the silent visor
- **Why the reader swipes:** Oliver's guilty over-friendliness, the hopeful "...FRY?", and Sanchez's only answer is a silent visor while the fryer sizzles. What does a solemn man do with a fry?
- **Panels:** p11 [40, 40, 1000, 640] · p12 [40, 700, 490, 570] · p13 [550, 700, 490, 570]
  - **p11 = G04** (3:2, 2k; Element: Oliver; reference: the approved G02). Sanchez's point of view, looking down.
> "<<<74170e99-a46a-4c7d-857c-d3046b839374>>> A chestnut-brown robotic teddy-bear soldier, soft plush all over, with a red headband and a brass-cartridge bandolier, sits on the grass beside the cart and looks up into the camera, cheeks stuffed full and a fry poking from his mouth, both heavy brows shot up high, flashing a wide, guilty grin that lifts on his right side, and holds the softly glowing red basket of golden fried food up toward the camera in both paws, the one basket, freshly scooped up off the grass. A sunlit daisy-flecked grass field at high noon, beside a red-and-yellow pyramid parasol with plain, unmarked panels on a single dark pole over a squat grey cart, a softly glowing red basket of golden fried food on the grass beside it, under a saturated mid-blue sky with big soft white cumulus clouds, the high sun as a slightly warm key with a soft cool fill from the sky and a gentle rim light on the characters. High-angle medium close-up looking down at him from a standing height, his face just below the centre of the frame and the basket raised in the lower left. The upper third of the frame is plain daisy-flecked grass with nothing in it, left clear; a clean image with no text. Avoid: photorealistic fur, realistic anatomy, real-person likeness, official logos, text, watermarks. Horizontal 3:2 framing. Polished feature-film 3D animation, soft rounded shapes, expressive faces, soft plush fur, soft global illumination, cinematic lighting, snappy cartoon timing with strong poses and holds."
  - Not for pasting: the scene line still says the basket is "on the grass" (as in the package's C2), while the action calls it "the one basket": reject any take with two.
  - **p12 = crop of G04:** his face and the raised basket (the package's "half-beat of silence, then '...Fry?' on the hold").
  - **p13 = crop of G03:** tight on the helmet and the glowing visor, the glow band narrowed, cut above the mouth (he is speaking in G03), so the panel reads as a silent stare.
- **Lettering:**
  - **balloon** "Sanchez! Buddy! You look **GREAT!**" · panel p11 · box [64, 56, 440] · tail → [458, 470] · 44 px
  - **balloon** "...**FRY?**" · panel p12 · box [64, 718, 280] · tail → [166, 866] · 52 px
  - **sfx** "SSSSZZZ..." · panel p13 · box [700, 1200, 320] · angle 4

### s06 · Up the wreck: "This arm, I did not ask for." (full page)
- **Why the reader swipes:** the hoist happened in the gutter ("ONE SCOOP LATER..."), they're on the pad from the cold open, and the grand line stops at "...I did not ask for." But?
- **Panel:** p14 [40, 40, 1000, 1270]
  - **p14 = G05** (4:5, 4k; Elements: Sanchez, Oliver; references: P1 for the wreck, furrow and palette; the approved G01 for the carry).
> "<<<e6122a2f-99de-423a-a310-733554bf48bb>>> A lean teddy-bear cyborg in a dark maroon helmet with rounded bear-ear bumps and an opaque glowing red visor hiding his eyes, a light tan muzzle with a small dark goatee, a grey-khaki chest plate over grey-and-white camo, olive-and-tan camo trousers, a dark grey glove on his left hand and an oversized red-and-black mechanical right arm. With <<<74170e99-a46a-4c7d-857c-d3046b839374>>> a chestnut-brown robotic teddy-bear soldier, soft plush all over, with a red headband and a brass-cartridge bandolier, as tall as the cyborg, tucked firmly under his mechanical right arm and hugging a softly glowing red basket of golden fried food, he stands planted on the glowing pad on top of the hull after a hard stop, feet wide, chest out, chin up, mouth open on a short line, his boots lit from below by the pad's cyan glow, while the soldier chews a fry with a flat, unimpressed look. A sunlit grassy hilltop at high noon, at the head of a long ploughed furrow of soft orange-edged earth, beside a chunky crash-landed dark grey sci-fi transport aircraft with an olive cast, softly rounded painted-metal panels with gentle dents, tomato-red bands, stubby wings and three fat cylindrical engine pods, the fourth snapped off in the grass beside the nose, an octagonal pad with a yellow-and-black hazard rim and a glowing icy-cyan star centre on top of its hull, faint stacked cyan rings hovering over it, the hull clean, intact and quiet in clear, still air, short, soft, stylised yellow-green turf flecked with tiny white daisies all around, under a saturated mid-blue sky with big soft white cumulus clouds, the high sun as a slightly warm key with a soft cool fill from the sky and a gentle rim light on the characters. Low-angle medium shot from the head of the furrow, close to the hull, looking up past the stubby wing at the top of the hull, the two of them standing on the pad right of centre and large in frame, rim-lit against the sky, their boots and the pad's glowing rim clearly visible. The upper left third of the frame is open saturated blue sky with soft white clouds and nothing else, left clear; a clean image with no text. Avoid: photorealistic fur, realistic anatomy, real-person likeness, official logos, text, watermarks. Vertical 4:5 framing. Polished feature-film 3D animation, soft rounded shapes, expressive faces, soft plush fur, soft global illumination, cinematic lighting, snappy cartoon timing with strong poses and holds."
  - Not for pasting: he stands on the pad (octagon, yellow-and-black rim, cyan star core), reached by the wing, not a ladder or ramp; tomato-red bands; no smoke; both faces at least about a tenth of the frame height; the carry checks. P1 draws the pad as a flat glowing square: either reading is fine, as long as G05 and G06 agree. 4k, because p16 is a tight crop of the boots.
  - **Fallback if the carry fails twice:** two solo shots on the same pad, one Element each (Sanchez chest out; Oliver munching on the hull), at one extra run.
- **Lettering:**
  - **caption** "One scoop later..." · panel p14 · box [64, 64, 400] · 38 px
  - **balloon** "This arm, I did not ask for." · panel p14 · box [64, 150, 470] · tail → [574, 470] · 46 px
  - **sfx** "KLANG!" · panel p14 · box [640, 880, 360] · angle -8

### s07 · "But LOOK at it."
- **Why the reader swipes:** the pride leaks through (his soul's contradiction: he did not ask for the arm, but he thinks it is really, really cool), and the pad starts to hum under their boots. Next: the launch.
- **Panels:** p15 [40, 40, 1000, 680] · p16 [40, 740, 1000, 570]
  - **p15 = G06** (3:2, 2k; Elements: Sanchez, Oliver; reference: the approved G05). The package's C3 hold: he tilts his head toward the arm with a small closed-mouth smile; he can't lift the arm, because Oliver is under it.
> "<<<e6122a2f-99de-423a-a310-733554bf48bb>>> A lean teddy-bear cyborg in a dark maroon helmet with rounded bear-ear bumps and an opaque glowing red visor hiding his eyes, a light tan muzzle with a small dark goatee, a grey-khaki chest plate over grey-and-white camo, olive-and-tan camo trousers, a dark grey glove on his left hand and an oversized red-and-black mechanical right arm. With <<<74170e99-a46a-4c7d-857c-d3046b839374>>> a chestnut-brown robotic teddy-bear soldier, soft plush all over, with a red headband and a brass-cartridge bandolier, as tall as the cyborg, tucked firmly under his mechanical right arm and hugging a softly glowing red basket of golden fried food, he stands on the glowing pad on top of the hull and tilts his head toward his mechanical arm as a small closed-mouth smile lifts his goatee, the glow band inside his visor widening, while the soldier chews a fry, cheeks full, with a flat, deadpan stare. A sunlit grassy hilltop at high noon, at the head of a long ploughed furrow of soft orange-edged earth, beside a chunky crash-landed dark grey sci-fi transport aircraft with an olive cast, softly rounded painted-metal panels with gentle dents, tomato-red bands, stubby wings and three fat cylindrical engine pods, the fourth snapped off in the grass beside the nose, an octagonal pad with a yellow-and-black hazard rim and a glowing icy-cyan star centre on top of its hull, faint stacked cyan rings hovering over it, the hull clean, intact and quiet in clear, still air, short, soft, stylised yellow-green turf flecked with tiny white daisies all around, under a saturated mid-blue sky with big soft white cumulus clouds, the high sun as a slightly warm key with a soft cool fill from the sky and a gentle rim light on the characters. Medium close-up at eye level on top of the hull, the cyborg's head right of centre and the soldier's head lower left, both faces large in frame. The upper left corner of the frame is open saturated blue sky with nothing in it, left clear; a clean image with no text. Avoid: photorealistic fur, realistic anatomy, real-person likeness, official logos, text, watermarks. Horizontal 3:2 framing. Polished feature-film 3D animation, soft rounded shapes, expressive faces, soft plush fur, soft global illumination, cinematic lighting, snappy cartoon timing with strong poses and holds."
  - Not for pasting: the smile is small and closed-mouthed; the visor stays opaque and only its inner band widens; the carry checks.
  - **p16 = crop of G05:** their boots and Oliver's dangling feet on the glowing pad.
- **Lettering** (the bold italic on LOOK is the package's "tiny lift on 'look'"; the words are unchanged):
  - **balloon** "But **LOOK** at it." · panel p15 · box [64, 60, 400] · tail → [564, 330] · 50 px
  - **sfx** "MUNCH" · panel p15 · box [430, 600, 240] · angle -10
  - **sfx** "VMMMMMMMMM" · panel p16 · box [64, 1100, 940] · angle 4

### s08 · Launch: WHUMP, then the arc
- **Why the reader swipes:** the pad from the cold open fires, and they're already gone; then the cover comes back, tighter, as the arc splash. Where do they land?
- **Panels:** p17 [40, 40, 1000, 300] · p18 [40, 360, 1000, 950]
  - **p17:** approved P1, cropped to the hull top: the same pad B-1000 locked onto, glowing and **empty**.
  - **p18 = crop of G01:** about 80% of the cover's width, centred on the pair, so it doesn't read as a repeat.
- **Lettering** (the mock-heroic brass-and-strings cue becomes a caption):
  - **sfx** "WHUMP!" · panel p17 · box [84, 92, 340] · angle 8
  - **caption** "~ Heroic brass swells ~" · panel p18 · box [64, 384, 480] · 36 px
  - **sfx** "FWOOOOOSH!" · panel p18 · box [64, 1100, 620] · angle 8

### s09 · THOOM. "HOME."
- **Why the reader swipes:** a proud landing, then a silent panel on the band's colour and an off-panel "..." from Oliver. The sharp reader notices before he says it.
- **Panels:** p19 [40, 40, 1000, 800] · p20 [40, 860, 1000, 450]
  - **p19 = G07** (5:4, 4k; Elements: Sanchez, Oliver; references: P1b for the dropship's design, the approved G01 for the carry, P3r for the field if approved). They land **beside** the hull, never on top ("right next to the opposite spacecraft" [Fan-wiki]).
> "<<<e6122a2f-99de-423a-a310-733554bf48bb>>> A lean teddy-bear cyborg in a dark maroon helmet with rounded bear-ear bumps and an opaque glowing red visor hiding his eyes, a light tan muzzle with a small dark goatee, a grey-khaki chest plate over grey-and-white camo, olive-and-tan camo trousers, a dark grey glove on his left hand and an oversized red-and-black mechanical right arm. With <<<74170e99-a46a-4c7d-857c-d3046b839374>>> a chestnut-brown robotic teddy-bear soldier, soft plush all over, with a red headband and a brass-cartridge bandolier, as tall as the cyborg, tucked firmly under his mechanical right arm and hugging a softly glowing red basket of golden fried food, he has just landed on the grass beside the hull with a squash on bent knees and snapped up into a hard hold, chest out, chin up, his gloved left fist on his hip, mouth open on one word, a small soft puff of dust settling at his boots, while the soldier stares up at the hull's royal-blue bands, his smirk gone flat and his brows down. A sunlit grassy hilltop at high noon, beside a chunky crash-landed dark grey sci-fi transport aircraft with an olive cast, softly rounded painted-metal panels with gentle dents, royal-blue bands, stubby wings and three fat cylindrical engine pods, the fourth snapped off in the grass beside the nose, an octagonal pad with a yellow-and-black hazard rim and a glowing icy-cyan star centre on top of its hull, faint stacked cyan rings hovering over it, the hull clean, intact and quiet in clear, still air, short, soft, stylised yellow-green turf flecked with tiny white daisies all around, under a saturated mid-blue sky with big soft white cumulus clouds, the high sun as a slightly warm key with a soft cool fill from the sky and a gentle rim light on the characters. Low wide shot from the open grass beside the hull's blunt nose, the nose with its cockpit window, twin round headlamps and royal-blue bands filling the right half of the frame, the two of them standing on the grass left of centre with both faces large and clear and turned three-quarters toward the camera. The upper left third of the frame is open saturated blue sky with soft white clouds, left clear; a clean image with no text. Avoid: photorealistic fur, realistic anatomy, real-person likeness, official logos, text, watermarks. Horizontal 5:4 framing. Polished feature-film 3D animation, soft rounded shapes, expressive faces, soft plush fur, soft global illumination, cinematic lighting, snappy cartoon timing with strong poses and holds."
  - Not for pasting: the bands are royal blue (no red bleeding in from P1); the dropship is chunky and stubby like P1, not an airliner; no jets or wings; no Huggables or anyone else. 4k, because three more panels are cut from it.
  - **p20 = crop of G07:** the nose, one royal-blue band and the cockpit window like an eye. No faces.
- **Lettering** (the cue peaks over the arc and lands on the touchdown):
  - **caption** "~ Big heroic finish ~" · panel p19 · box [64, 64, 480] · 34 px
  - **balloon** "**HOME.**" · panel p19 · box [590, 100, 250] · tail → [478, 290] · 58 px
  - **sfx** "THOOM!" · panel p19 · box [64, 650, 400] · angle -6
  - **balloon** "..." · panel p20 · box [470, 900, 150] · tail → [190, 1296] · 48 px

### s10 · "...That's THEIR ship."
- **Why the reader swipes:** the punchline opens the slide, the music caption dies mid-word ("HEROIC BRA--", where the package cuts the music dead on "THEIR"), and then something goes FWAP off-panel right: the five banners turning as one.
- **Panels:** p21 [40, 40, 1000, 800] · p22 [40, 860, 1000, 450]
  - **p21 = crop of G07:** Oliver's head and shoulders with the basket, a blue band behind him. If the 4k crop is soft, use **O1** (§9).
  - **p22 = crop of G07:** Sanchez chest-up, still in his proud hold. He hasn't noticed a thing.
- **Lettering** (his bravado cracks on THEIR):
  - **balloon** "...That's **THEIR** ship." · panel p21 · box [64, 64, 440] · tail → [514, 420] · 48 px
  - **caption** "~ Heroic bra--" · panel p21 · box [640, 110, 340] · 34 px
  - **sfx** "FWAP!" · panel p22 · box [780, 1150, 210] · angle -10

### s11 · The reverse (full page; generated last)
- **Why the reader swipes:** the swipe is the reveal, and the next swipe is the hard cut, before the hug lands. No contact is ever shown.
- **Panel:** p23 [40, 40, 1000, 1270]
  - **p23 = G08** (4:5, 2k; **needs the blue Huggable Element** `huggable-huggable-blue`, the main sheet with jaws on, by huggable.md's paw rule, because this is the arms-wide threat pose; references: the approved G07 and P1b). The true reverse from the landing spot at low eye level: five blue Huggables in a loose, staggered row in front of the blue nose, snapped round in unison into the hug pose. Sanchez and Oliver are behind the camera.
> "<<<E1>>> Five identical copies of a small stitched hot-pink plush teddy about two-thirds as tall as a teddy-bear soldier, with a big round cream-bandaged head, short stubby arms and legs, a boxy dark olive-green radio with a thin grey red-ball antenna, one glossy red button eye on its right, one small black bead eye on its left, a huge fixed toothy grin and a tall, narrow blue banner on a pole rising from its back high above its head, have snapped around toward the camera in perfect unison, each with its bandage, radio and red button eye on the viewer's left, and lean in on their toes with their arms forward and wide in a hug pose, oversized black bear-trap jaws on all their paws, the red balls on their antennas glowing together and their banners whipping above their heads, their grins fixed and their teeth together. A sunlit grassy hilltop at high noon, beside a chunky crash-landed dark grey sci-fi transport aircraft with an olive cast, softly rounded painted-metal panels with gentle dents, royal-blue bands, stubby wings and three fat cylindrical engine pods, the fourth snapped off in the grass beside the nose, an octagonal pad with a yellow-and-black hazard rim and a glowing icy-cyan star centre on top of its hull, faint stacked cyan rings hovering over it, the hull clean, intact and quiet in clear, still air, short, soft, stylised yellow-green turf flecked with tiny white daisies all around, under a saturated mid-blue sky with big soft white cumulus clouds, the high sun as a slightly warm key with a soft cool fill from the sky and a gentle rim light on the characters. Locked-off medium shot at low eye level, the five in a loose, staggered row on the open turf in front of the hull's blunt nose, the hull filling the upper middle of the frame behind them. The bottom fifth of the frame is plain, empty turf, left clear; a clean image with no text. Avoid: photorealistic fur, realistic anatomy, real-person likeness, official logos, text, watermarks. Vertical 4:5 framing. Polished feature-film 3D animation, soft rounded shapes, expressive faces, soft plush fur, soft global illumination, cinematic lighting, snappy cartoon timing with strong poses and holds."
  - Not for pasting: the character line is huggable.md's word for word, with its blue-team change and the package's prefix. The viewer-terms clause ("on the viewer's left") sits in the action, after SHEETS.md's Oct 25 diagnosis that the model reads a bare "right" as image-right. Checks (package C5):
    - exactly five, identical, never merging;
    - hot-pink plush paws inside black bear-trap jaws on both paws;
    - the red button eye, scar, cream bandage and olive radio on each teddy's own right (the viewer's left); a red-ball antenna;
    - blue banners with a white circle, triangle and square stacked top to bottom, and no letters;
    - grins fixed, teeth together, no thumbs;
    - the hug pose (leaning in on its toes, arms forward), not the T pose;
    - no bear in frame, no contact;
    - none of the Huggable negatives (greeting-card cuteness, tummy emblem, pastel colours, chrome, blue gems, knee brace, neon outlines, guns).
  - No THREAT LEVEL tag here: the Huggable's "HUG" tag is saved for Ep 5 (package C5).
  - If the blue Element isn't live by Sat Oct 31, use **F2** (§9).
- **Lettering** (in the episode's sound order; KSSHT is the radios' shared static, hijacker clue 1):
  - **sfx** "KSSHT" · panel p23 · box [130, 120, 580] · angle 4
  - **sfx** "CLACK!" · panel p23 · box [64, 880, 330] · angle -8
  - **whisper** "...Mayday." · panel p23 · box [560, 1150, 400] · tail → [800, 1304] · 38 px

### s12 · The ledger and the upload
- **Why the reader swipes:** the season's scoreboard, the METHOD punchline, and B-1000's report sticking at 99%. Will it upload?
- **Panels:** p24 [40, 40, 1000, 560] · p25 [40, 620, 420, 690] · p26 [480, 620, 560, 690]
  - **p24:** the local ledger card: dark slate, a gold rule and three Joule-style tokens (dark hexagons with a blue bolt over a violet halo). Original art, no text. Labels: the tokens [Observed]; their identity as Joules [Fan-wiki; identification Inference]; their use as the ledger's point marker [BBG News invention]. Never the kill feed, never "SUICIDE".
  - **p25:** the C1 clip at 7.0 s, as a picture-in-picture news window (the sign-off is voice-over in the package; showing his face attributes it). Never a picture from s11, so the hug stays unseen.
  - **p26:** the local upload screen: navy HUD grid and a segmented bar frozen one sliver short of full.
- **Lettering:**
  - **title** "SCENERY 1 · BEARS 0" · panel p24 · box [80, 66, 920]
  - **sfx** "PLINK! PLINK! PLINK!" · panel p24 · box [80, 226, 600] · angle 3
  - **caption** "Method: delivered to the **wrong ship**" · panel p24 · box [80, 372, 920] · 38 px
  - **sfx** "REAL MAP. FAN-MADE NEWS." · panel p24 · box [300, 462, 680] · angle -5
  - **hud** "KILL CREDIT: JUMP PAD. / ASSIST: HUGGABLES." · panel p26 · box [500, 642, 520] · tail → [248, 760] · 34 px
  - **hud** "NEXT LOCATION: / STEAMYARD BLUES." · panel p26 · box [500, 800, 520] · 34 px
  - **hud** "UPLOADING... 99%" · panel p26 · box [500, 1080, 420] · 36 px

### s13 · Rerouting... "TEE-HEE."
- **Why the reader swipes:** pink static with the Huggable's stitched seam hijacks the upload, with the same "KSSHT" as the Huggables (the clue connects), the report goes to everyone, and the robot giggles. Then the end card.
- **Panels:** p27 [40, 40, 1000, 300] · p28 [40, 360, 1000, 950]
  - **p27:** the local pink glitch: static with a jagged pale-grey seam and dark spiky ticks (the Huggable's chest seam).
  - **p28:** the approved C1 still, B-1000 waist-up: a dead-still glare under "TEE-HEE." plays his contradiction. Optional upgrade: **U1** (§9).
- **Lettering** ("Tee-hee." is his one per short):
  - **sfx** "KSSHT" · panel p27 · box [270, 96, 540] · angle -4
  - **hud** "REROUTING... / TO: EVERYONE" · panel p28 · box [64, 384, 420] · 40 px
  - **hud** "TEE-HEE." · panel p28 · box [700, 560, 300] · tail → [612, 640] · 48 px

---

## 6. End card and call to action (s14)
- **Why it's there:** it turns the swipe into comments and sends. The slate's weekly "guess the next label" game gets a blank tag; the research's top signal for reaching non-followers is sends, so the send line is explicit. It teases next week and carries the README end card. No wishlist or buy lines.
- **Panel:** p29 [40, 40, 1000, 1160] (the local HUD screen, with room for the end card on the bottom margin).
- **Lettering:**
  - **hud** "NEXT LOCATION: / STEAMYARD BLUES." · panel p29 · box [90, 100, 900] · 50 px
  - **caption** "Guess the next **THREAT LEVEL** in the comments." · panel p29 · box [90, 360, 900] · 46 px
  - **hud** "SUBJECT: ??? / THREAT LEVEL: ???" · panel p29 · box [260, 610, 560] · 46 px
  - **caption** "Send this to your BBG squad. / Follow BBG News for Ep 2." · panel p29 · box [90, 870, 900] · 44 px
  - **endcard** "Unofficial fan comic, not affiliated with SkyVu; characters © SkyVu." · default placement (bottom margin)
- **End card**, word for word, adapted from "fan film" to "fan comic": "Unofficial fan comic, not affiliated with SkyVu; characters © SkyVu." It spans the margins on the bottom margin, with no logos, wordmarks or app icons. Whether the card also says "AI" stays [Open] (README); the caption and Instagram's AI label carry the disclosure.
- **Text added for the comic** (all [BBG News invention], lettering only; no locked line is changed): the cover kicker, "DESTINATION: HOME?" and the swipe cue; the location caption and "ONE SCOOP LATER..."; every SFX; the three music captions; Oliver's off-panel "..."; the "99%" on the upload label; the teaser's "NOV 4"; the CTA lines and the blank tag.
- **Locked lines, word for word:** B-1000's 17 cold-open words, his 11 sign-off words and "Tee-hee."; Sanchez's "Oliver, we'll getcha... home." (his one pause is the gap between two balloons), "This arm, I did not ask for. But look at it." (split across the swipe), "Home." and "...Mayday."; Oliver's "Sanchez! Buddy! You look GREAT! ...Fry?" (split across two panels) and "...That's THEIR ship.". Capitals follow the package ("GREAT", "THEIR"), plus LOOK for C3's lift; `letter.py` sets dialogue in capitals anyway.

---

## 7. Generation schedule (Oct 27 – Nov 3)

Higgsfield allows about 5 generations a day, shared with the Huggable sheet queue (the red-sheet fix if v4 fails, then the blue main-sheet edit: about 2–3 runs). Comics need no voices, plates or clips, so the rest of each day's queue is free for panels. That gives 40 slots across the eight days; this plan uses at most about 17.

| Day | Slots (in order) | Also |
|---|---|---|
| **Tue Oct 27** | 1. **G01 cover** (first thing; QA by midday). 2. G01 retake if it failed, else **G02**. 3. **G02**, or **G03** once G02 passes (G03 uses it as a reference). 4. **Huggable:** the blue main-sheet edit if v4 (job 321fe5d6) passed review, else the v5 fix. 5. **G03**, or G04 if G03 already ran | Cut t01a from G01; render t01 and t02 (`--only t01,t02 --jpg`); send to Bryce that evening. If G01 failed twice, render t01 over the C1 still (teaser fallback) |
| **Wed Oct 28** | 1. **G04**. 2. **G05** (4k). 3. **G06** (after G05 passes). 4. **G07** (4k). 5. A retake (G02–G04), or the Huggable blue edit if slot 4 on Oct 27 went to the v5 fix | **Post the teaser at about 12:00** (Buffer's top Wednesday slot), AI label on |
| **Thu Oct 29** | 1. Huggable: a retake of the blue sheet if needed. 2–4. Retakes for G05–G07 (the carry), or **O1** if p21 is soft. 5. Spare | Create the blue Element (free) as soon as the blue sheet passes QA, and write its UUID into SHEETS.md and into G08's `<<<E1>>>` |
| **Fri Oct 30** | 1. **G08** (needs the blue Element). 2. A G08 retake if needed. 3–5. Spare | Cut every crop; letter the whole carousel with `--guides` |
| **Sat Oct 31** | **F2** only if there is still no blue Element; otherwise spare | Deadline for the s11 decision |
| **Sun Nov 1** | **U1** only if credits and a retake slot are left over | **Lock:** every panel approved, `letter.py pages.json --only s01,...,s14 --strict --guides --jpg`, Bryce's review |
| **Mon Nov 2 – Tue Nov 3** | Buffer only | Phone check: the slide counter, the 3:4 grid crop of s01, the in-app alt-text limit; final caption |
| **Wed Nov 4** | — | **Post at about 12:00**, AI label on |

---

## 8. Budget

- **Base:** 8 generations, 22 credits (G01 2, G02 2, G03 4, G04 2, G05 4, G06 2, G07 4, G08 2).
- **Retakes (about 30%):** 3 generations, about 8–10 credits. They are kept for G01 (it gates the teaser), the carry shots (G05–G07) and G08 (five identical copies).
- **Optional, only from unused retake slots:** O1 (2), F2 (2), U1 (2). The hard ceiling is **14 panel generations**, the cover included.
- **Huggable sheets** (not this budget, but the same daily slots): 2–3 runs, about 8–12 credits at 4k.
- **Expected total:** about 11 panel runs and about 31 credits; with the sheets, about 39–43 of the ~95 credits. **About 50 credits stay** for Ep 2 and later. Worst case, with every option: about 49 credits, leaving about 46.

---

## 9. Fallbacks and optional upgrades (prompts paste-ready)

**O1 · Oliver close-up beside the blue hull** (replaces the p21 crop only if it is soft; 5:4, 2k; Elements: Oliver, Sanchez; reference: the approved G07):
> "<<<74170e99-a46a-4c7d-857c-d3046b839374>>> A chestnut-brown robotic teddy-bear soldier, soft plush all over, with a red headband and a brass-cartridge bandolier, held under the oversized red-and-black mechanical right arm of <<<e6122a2f-99de-423a-a310-733554bf48bb>>> a lean teddy-bear cyborg in a dark maroon helmet with rounded bear-ear bumps and an opaque glowing red visor hiding his eyes, a light tan muzzle with a small dark goatee, a grey-khaki chest plate over grey-and-white camo, olive-and-tan camo trousers, a dark grey glove on his left hand and an oversized red-and-black mechanical right arm, whose head is out of frame, hugs a softly glowing red basket of golden fried food and stares flatly up toward the right of the frame, his smirk gone flat, brows down, eyes half-lidded in deadpan realisation. A sunlit grassy hilltop at high noon, beside a chunky crash-landed dark grey sci-fi transport aircraft with an olive cast, softly rounded painted-metal panels with gentle dents, royal-blue bands, stubby wings and three fat cylindrical engine pods, the fourth snapped off in the grass beside the nose, an octagonal pad with a yellow-and-black hazard rim and a glowing icy-cyan star centre on top of its hull, faint stacked cyan rings hovering over it, the hull clean, intact and quiet in clear, still air, short, soft, stylised yellow-green turf flecked with tiny white daisies all around, under a saturated mid-blue sky with big soft white cumulus clouds, the high sun as a slightly warm key with a soft cool fill from the sky and a gentle rim light on the characters. Low-angle close-up of the soldier's head and shoulders right of centre, behind him the hull's olive-cast dark grey painted side with one broad royal-blue band running across it. The upper left third of the frame is the hull's plain painted side, left clear; a clean image with no text. Avoid: photorealistic fur, realistic anatomy, real-person likeness, official logos, text, watermarks. Horizontal 5:4 framing. Polished feature-film 3D animation, soft rounded shapes, expressive faces, soft plush fur, soft global illumination, cinematic lighting, snappy cartoon timing with strong poses and holds."

**F2 · The shadow reveal** (replaces p23 only if no blue Huggable Element is live by Sat Oct 31; 4:5, 2k; Elements: Sanchez, Oliver; reference: the approved G07). It keeps the beat with the two live Elements and keeps the hug off-panel, but costs the reveal of the wave itself. With F2, "...Mayday." becomes a whisper on-panel, its tail to Sanchez's mouth.
> "<<<e6122a2f-99de-423a-a310-733554bf48bb>>> A lean teddy-bear cyborg in a dark maroon helmet with rounded bear-ear bumps and an opaque glowing red visor hiding his eyes, a light tan muzzle with a small dark goatee, a grey-khaki chest plate over grey-and-white camo, olive-and-tan camo trousers, a dark grey glove on his left hand and an oversized red-and-black mechanical right arm. With <<<74170e99-a46a-4c7d-857c-d3046b839374>>> a chestnut-brown robotic teddy-bear soldier, soft plush all over, with a red headband and a brass-cartridge bandolier, as tall as the cyborg, tucked firmly under his mechanical right arm and hugging a softly glowing red basket of golden fried food, he freezes in his hard hold beside the hull, the glow band inside his visor widened to fill the visor, his mouth a small flat line, while the soldier's brows shoot up, as five short, round shadows with arms spread wide and five tall, thin banner-pole shadows fall across them both from behind the camera. A sunlit grassy hilltop at high noon, beside a chunky crash-landed dark grey sci-fi transport aircraft with an olive cast, softly rounded painted-metal panels with gentle dents, royal-blue bands, stubby wings and three fat cylindrical engine pods, the fourth snapped off in the grass beside the nose, an octagonal pad with a yellow-and-black hazard rim and a glowing icy-cyan star centre on top of its hull, faint stacked cyan rings hovering over it, the hull clean, intact and quiet in clear, still air, short, soft, stylised yellow-green turf flecked with tiny white daisies all around, under a saturated mid-blue sky with big soft white cumulus clouds, the high sun as a slightly warm key with a soft cool fill from the sky and a gentle rim light on the characters. Locked-off medium shot at low eye level, facing the two with the hull's blunt nose behind them. The bottom fifth of the frame is plain, empty turf, left clear; a clean image with no text. Avoid: photorealistic fur, realistic anatomy, real-person likeness, official logos, text, watermarks. Vertical 4:5 framing. Polished feature-film 3D animation, soft rounded shapes, expressive faces, soft plush fur, soft global illumination, cinematic lighting, snappy cartoon timing with strong poses and holds."

**U1 · B-1000's "tee-hee"** (replaces the p28 crop, spare slot only, Nov 1; 1:1, 2k; Element: `b-1000-assault-signature` `<<<afb181b2-d8e7-47d3-8426-df01bf99e80c>>>`; reference: the C1 start still, job de69723e). A solo shot, so it uses STYLE.md's glossy-armour suffix and the package C1's Avoid sentence without its video-only terms. Check it against the package's C1 list (no hands; rail-gun on his own right forearm, the viewer's left; a small plain unlit chest disc; maroon, no fur; the eye-slits narrow, never curve).
> "<<<afb181b2-d8e7-47d3-8426-df01bf99e80c>>> A hulking, top-heavy robot bear built entirely of glossy maroon painted-metal armour, with pointed plated ears, a black-tipped snout over a hinged jaw plate, two narrow glowing cyan eye-slits under a heavy brow plate, a long orange-and-black slab rail-gun built onto his right forearm, a three-blade cyan claw gauntlet on his left forearm and a white winged jump-pack on his back, stands planted in front of the crashed aircraft with his clawed feet set wide, his head cocked to one side, his heavy brow plate lifted and tilted, his eye-slits squeezed to thin, extra-bright lines and his hinged jaw plate dropped a little, looking far too pleased with himself. A sunlit grassy hilltop at high noon, at the head of a long ploughed furrow of soft orange-edged earth, beside a chunky crash-landed dark grey sci-fi transport aircraft with an olive cast, softly rounded painted-metal panels with gentle dents, tomato-red bands, stubby wings and three fat cylindrical engine pods, the fourth snapped off in the grass beside the nose, an octagonal pad with a yellow-and-black hazard rim and a glowing icy-cyan star centre on top of its hull, faint stacked cyan rings hovering over it, the hull clean, intact and quiet in clear, still air, short, soft, stylised yellow-green turf flecked with tiny white daisies all around, under a saturated mid-blue sky with big soft white cumulus clouds, the high sun as a slightly warm key with a soft cool fill from the sky and a gentle rim light on the characters. Locked-off low-angle medium close-up, his head and shoulders in the middle of the frame, the glowing pad on top of the hull visible behind him. The upper left of the frame is open saturated blue sky above the top of the hull, left clear; a clean image with no text. Avoid: photorealism, real-person likeness, official logos, text, watermarks. Square 1:1 framing. Polished feature-film 3D animation, soft rounded shapes, expressive faces, glossy painted armour, soft global illumination, cinematic lighting, snappy cartoon timing with strong poses and holds."

**Teaser fallback (0 credits):** see §4.

---

## 10. Instagram

### Caption, Wed Nov 4 (the slate's template, adapted to a comic; the hook first, since the feed shows about 125 characters)
> Sanchez is finally finishing Oliver's rescue. The jump pad has other plans. Swipe ▸
>
> LOCAL HAZARDS Ep 1: No Bears Land. Era: classic 2013 look (BBG's 2013 default skins, set after Sanchez joined in Dec 2013). In the game: the two crashed dropships with jump pads on top (seen in game footage; the fan wiki calls them Pelican'ts), which fling you across the field to land right next to the other ship (per the fan wiki), and the food stand's glowing basket of fried food (seen in game footage). Fan-made: everything that happens; fan take: Sanchez's unfinished rescue is a BBG News invention; the BB Zombies crash is the fan wiki's account. No Bears Land returns Nov 4.
>
> Guess the next THREAT LEVEL in the comments, and send this to your BBG squad. Next location: Steamyard Blues.
>
> Unofficial AI fan comic. Not affiliated with SkyVu.
>
> #BBGNews #LocalHazards #BattleBearsGold #NoBearsLand #FanComic

### Caption, Wed Oct 28 teaser
> A robot files field reports from real BBG maps. The scenery has never lost. LOCAL HAZARDS, a fan comic, Wed Nov 4. Swipe ▸
>
> Ep 1: No Bears Land. Era: classic 2013 look (BBG's 2013 default skins, set after Sanchez joined in Dec 2013). In the game: two crashed dropships with jump pads on top (seen in game footage) that land you right next to the other ship (per the fan wiki). Fan-made: everything that happens. Unofficial AI fan comic. Not affiliated with SkyVu.
>
> #BBGNews #LocalHazards #BattleBearsGold #NoBearsLand #FanComic

**Notes:**
- **Five hashtags:** Instagram has capped posts at five since its Dec 2025 rollout (research §1). Swap #LocalHazards for #BattleBears if reach matters more than the show tag.
- **AI disclosure, three layers:** switch on Instagram's AI label on both posts (or set `is_ai_generated` on the carousel container if posting by API; children can't take it); the caption line; the end card on s14 and t02. Never the "AI-generated profile" label: this page has no AI person.
- **Labels:** the wrecks and pads [Observed]; "Pelican't" for these wrecks [Fan-wiki], attributed; the pad behaviour [Fan-wiki], attributed; "returns Nov 4" [Canon: Steam]; the teaser's "the other crashed dropship" line is [Fan-wiki] and its caption carries the attribution (slate §4). Nothing is captioned as SkyVu canon that isn't.
- No #SkyVu tag and no mention of SkyVu's approval (package open item 8).
- Post at about 12:00 local time on both Wednesdays (Buffer, Sep 2026). Turn on "Upload at highest quality". Export with `--jpg` (JPEG q92, sRGB, 4:4:4).

### Alt text (one per slide; each under 600 characters, inside the API's 1,000. If the in-app box proves shorter, post the full set as the first comment.)
- **s01:** Comic cover. High over a sunny field of zig-zag trenches, Sanchez, a teddy-bear cyborg with a glowing red visor and a huge red-and-black robot arm, flies in a superhero pose, fist forward. Tucked under his robot arm, Oliver, a brown teddy-bear soldier in a red headband, hugs a glowing basket of fries with a fry in his mouth as fries tumble out behind them. Gold title: We'll Getcha Home. Cyan screen box: BBG News, live. Local Hazards, episode 1. A target ring on Sanchez reads: Destination: home? Swipe.
- **s02:** B-1000, a hulking maroon robot bear with glowing cyan eye-slits, a rail-gun arm and cyan claws, stands below a chunky grey crashed dropship with red bands and a glowing pad on its roof. His cyan screen box: "B-1000. Live. Scanning location." Two identical panels of the ship, his head peeking up from below: "Hazard: crashed dropship." "Status: still crashed." He shouts beside a close-up of the roof pad in a target ring: "Launch pad destination: the other crashed dropship."
- **s03:** Title band: Local Hazards, with a news sting: dun-dunn! Caption: The red food stand. Under a red-and-yellow parasol, Oliver sits in the grass, eyes shut in bliss, biting a fry beside a glowing basket. Screen tag: "Subject: Oliver. Threat level: fluffy." Sound: crunch! Bottom panel: a glowing red visor and a red-and-black robot arm swing into view. Sound: ka-chunk!
- **s04:** Low angle: Sanchez towers over Oliver, his gloved hand on his chest, pointing his robot arm down at him. Screen tag: "Subject: Sanchez. Threat level: partial upgrade." Sanchez: "Oliver, we'll getcha..." "...home."
- **s05:** Looking down at Oliver, mouth stuffed, grinning guiltily and holding the basket up: "Sanchez! Buddy! You look great!" Close-up, hopeful: "...Fry?" Sanchez's red visor stares back in silence while the fryer sizzles.
- **s06:** Caption: One scoop later... Low angle up at the red-banded crashed dropship: Sanchez stands on the glowing roof pad, chest out, Oliver tucked under his robot arm and still chewing. Sanchez: "This arm, I did not ask for." Sound: klang!
- **s07:** Close-up: Sanchez tilts his head toward his robot arm with a small proud smile. Sanchez: "But look at it." Oliver chews, deadpan. Sound: munch. Below, their boots on the pad as it glows brighter. Sound: a rising hum, vmmmm.
- **s08:** The roof pad, suddenly empty: whump! Below, Sanchez flies in a heroic pose high over the trench field, Oliver under his arm with a fry in his mouth. Caption: heroic brass swells. Sound: fwoooosh!
- **s09:** They land beside the nose of a crashed dropship with royal-blue bands. Caption: big heroic finish. Sound: thoom! Sanchez, chest out: "Home." Below, a silent close-up of the blue band and the cockpit window, and an off-panel balloon with three dots.
- **s10:** Oliver stares up, flat-faced: "...That's their ship." The music caption is cut off: heroic bra. Below, Sanchez still holds his proud pose as something off-panel goes: fwap!
- **s11:** Reverse view: five grinning pink stitched Huggables with bandaged heads, head radios, tall blue banners and black bear-trap jaws on their paws have snapped round toward us, arms wide for a hug, in front of the blue ship. Their radios: kssht. Jaws: clack! Sanchez, off-panel, in a tiny whisper: "...Mayday."
- **s12:** A ledger card: Scenery 1, Bears 0. Three blue lightning-bolt tokens: plink, plink, plink. Method: delivered to the wrong ship. Stamp: Real map. Fan-made news. Below, B-1000 in a small news window reports in cyan boxes: "Kill credit: jump pad. Assist: Huggables." "Next location: Steamyard Blues." "Uploading... 99%", over a progress bar stuck one notch short.
- **s13:** Pink static with a stitched seam: kssht. Over B-1000, standing by the red ship: "Rerouting... to: everyone." B-1000, in a dead-still glare: "Tee-hee."
- **s14:** B-1000's screen: "Next location: Steamyard Blues." Guess the next threat level in the comments. A blank tag: "Subject: question marks. Threat level: question marks." Send this to your BBG squad. Follow BBG News for Ep 2. Small print: Unofficial fan comic, not affiliated with SkyVu; characters © SkyVu.
- **t01:** Comic cover. High over a sunny trench field, Sanchez, a teddy-bear cyborg with a glowing red visor and a huge red-and-black robot arm, flies in a superhero pose with Oliver, a brown teddy-bear soldier, tucked under his arm, hugging a basket of fries with a fry in his mouth. Gold title: We'll Getcha Home. Stamp: Nov 4. Cyan screen box: BBG News, Local Hazards. Swipe.
- **t02:** B-1000, a hulking maroon robot bear with cyan eye-slits, reports live from below a crashed grey dropship with red bands: "B-1000. Live. Scanning location." "Hazard: crashed dropship." "Status: still crashed." He shouts beside the glowing roof pad in a target ring: "Launch pad destination: the other crashed dropship." Title: Local Hazards, Nov 4. Small print: Unofficial fan comic, not affiliated with SkyVu; characters © SkyVu.

---

## 11. Pages JSON and panels JSON

- **`pages.json`** is in exactly the shared PAGE SPEC form: `canvas` [1080, 1350], `background` "#0d0d10", and per page `panels` (`id`, `rect`, `image`, `focus`, `border`) and `letters` (`type`, `text`, `panel`, `box` [x, y, w], `tail`, `size`, `angle`), with optional keys left out. Two letters have no `panel`: the end cards and t02's title band, which sit on the background.
- **Render:** from this folder, `python3 ../comic/letter.py pages.json --out out --guides --sheet` (add `--only s01,s02,s03,s04,s05,s06,s07,s08,s09,s10,s11,s12,s13,s14` for the Nov 4 carousel, `--only t01,t02` for the teaser, `--jpg` for posting, `--strict` at lock).
- **Image files:** every panel is `panels/<panel id>.png`. Raw downloads of new generations go in `src/<panel id>_raw.png` (`src/p01_raw.png` for G01, and so on). Each crop's `reuse_source` names its source, frame time and crop: source-pixel boxes (`crop_px`) for approved art, fractions of the raw image (`crop_frac`) for new art. Fractions are the intended framing; nudge them with `--guides` once the art lands.
- **`panels.json`** has one entry per panel (35): the 8 generations carry their paste-ready prompt, Element UUIDs and references; the 27 free panels carry `prompt: null` and their `reuse_source`. G08's Element is listed as pending until the blue Huggable exists. Set `status` to `generated`, `approved` or `cut` as work lands.
- **Test results (Oct 26):** all 16 pages render; zero layout, margin, gutter, overlap or off-canvas warnings; 17 missing-image warnings (8 new generations and 9 crops of them). With mock face boxes added (engine-only `faces`, not in the deliverable), zero face or tail warnings. The test renders are in `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/comic/final_work/out_real/` (the deliverable JSON with the free art) and `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/comic/final_work/out_mock/` (with grey mock-ups of the new art and face boxes).

---

## 12. Open items for Bryce

1. **References:** approve **P3r** (P3's right half) as G01's field reference by the morning of Oct 27 (otherwise G01 runs with no location reference), and **P2** as a location reference for G02 and G03. **P3 is not redone and P4 is not made**: the blue wreck comes from P1b, the local blue recolour of approved P1.
2. **Framing lines for comic panels:** "Vertical 4:5 framing.", "Horizontal 3:2 framing." and "Horizontal 5:4 framing." replace STYLE.md's "Vertical 9:16 framing.", and the video suffix stays last on stills. STYLE.md's Frame rule (9:16, Reels safe zone) needs a comic note: 4:5 slides, a 40 px margin, the lettering space named in every prompt.
3. **End card:** "Unofficial fan comic, not affiliated with SkyVu; characters © SkyVu." Add "AI"? (README [Open]; the default leaves it out.)
4. **The teaser:** the 2-slide carousel (t01 cover + t02 cold open, the default), or the cover alone. Both cost 0 extra credits.
5. **New comic-only words** ([BBG News invention]; spoken lines unchanged). Approve as a set: "DESTINATION: HOME?", "ONE SCOOP LATER...", "THE RED FOOD STAND.", the music captions ("~ HEROIC BRASS SWELLS ~", "~ BIG HEROIC FINISH ~", "~ HEROIC BRA--"), Oliver's off-panel "...", the "99%" on the upload label, "NOV 4", the SFX, the CTA lines and the caption hooks.
6. **The Huggables:** five copies (default) or three if takes merge (package open item 5); F2 if the blue Element isn't live by Sat Oct 31.
7. **Hashtags:** #LocalHazards or #BattleBears in the fifth slot.
8. **Local original-art graphics** (sting band, ledger card with tokens, 99% screen, pink seam glitch, end-card screen): drafts are built. Approve them, or ask for a designed set.
9. **Carried over from the package:** item 15, the catchphrase reading ("we'll getcha... home" and "...Mayday." as one known line); item 12, a corner bug (none by default; the cover kicker names the show).
10. **No longer needed for Ep 1:** the dub, the music, the Seedance clips, plate P4 and the C2/C4 start stills. The C1 clip stays as the source of p05, p25 and t02d.
11. **3:4 test:** one manual in-app test post before any future switch from 4:5 (§2).
