# Combat VFX and death conventions (Battle Bears Gold)

This dossier covers how combat looks in BBG as a whole, independent of any one weapon:
- how kills and deaths look for bears, robots and Huggables
- damage feedback, headshots, the kill feed, team colours and status-effect visuals
- pickups, respawn, hazards and explosions
- the game's overall effects style

It also settles the Bearzooka colour conflict.

This is the edited version of the draft. I applied the source check and the image check, and re-checked every point where a report and the draft disagreed against the wiki text and the image files. Corrections from those checks are folded in. Claims that did not survive were removed or relabelled.

**Sources reachable:**
- **Fan wiki (MediaWiki API):**
  - about 110 pages, re-fetched for the source check
  - about 135 wiki images (the draft's 45, re-downloaded byte-identical, plus 90 more)
  - upload dates from `imageinfo`
- **Official Steam media (on the 2026 store page):**
  - the five Steam screenshots
  - the 54 s "Battle Bears Gold Premium - Trailer"
  - the 1.4 s loop video in the store description (`extras/f7ecb9b2e78f0fd754cc7cf8220ad9b0.mp4`)
  - the live `appdetails` text and store page
- **battlebears.com (live):**
  - BB Heroes-era site
  - its Shopify product JSON for the "Huggable Rainbow Explosion T-shirt Black", which I re-fetched today
- **YouTube:**
  - thumbnails and oEmbed titles only
  - "[Oliver]:Secondary - Bearzooka" (AZt_huguhzc, uploader Dban1)
  - "Gamma Ray Demonstration" (0GuhKiAnNyc, uploader ApplerGamers)
  - "BBG All Classes Showcase [Skins, Taunts, Weapons, and Melee] (from Closed Playtest #4)" (-lAtv-j9Sms, JustNubz)
  - two "BB-1 Riggs" shorts on the channel "BattleBearsGame"

**Not reachable:**
- web.archive.org reset the connection on every try, in the draft (7 tries) and the source check (3 tries). No archived SkyVu blog or patch notes were read.
- YouTube video content is blocked. Nobody watched any video. YouTube claims come from thumbnail frames only.

**Eras:**
- **BBR:** the wiki dates Battle Bears Royale to "October 8th, 2011 in the US and December 5th, 2011 worldwide" [Fan-wiki: Battle Bears Gold]. The BBG News era key calls this era "BBR (2012)". BBR versions run 1.0 to 1.4.x.
- **BBG:** the wiki's BBG version list starts "1.0 | Migration from Battle Bears Royale to Battle Bears Gold | May 24th, 2013". It then runs 2.1 (July 15, 2013) to 2.31 [Fan-wiki: Battle Bears Gold/Versions].
- **Wiki captures:** any wiki image uploaded before May 24, 2013 is a BBR capture. An upload date is only the latest possible capture date.
- **BBG 2026:** the Steam re-release, "Nov 4, 2026" [Canon: Steam]. The Steam trailer and screenshots were not captured on a 2026 build: they re-use SkyVu's May 2013 trailer footage [Inference, strong; see Overall VFX style, Ink outline]. The class cards are pixel-identical to the 2013 trailer at full size, and the gameplay is matched to it at storyboard size (160×90), the Space Oddity shot (screen_01) and the Graham segment included [Observed; the gameplay at storyboard size: 2026.md, "The Steam trailer is 2013 footage"].

**Path key** (used in every "Images viewed" list):
- `W` = `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons`
- `C` = `W/dl/combat-vfx` (draft downloads)
- `C2` = `W/dl/combat-vfx-check` (check downloads)
- `E` = `W/dl/combat-vfx-edit` (this edit; holds today's re-fetch of the shirt JSON)
- `M` = `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl` (maps-research downloads)
- `MC` = `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps_corr/cvfx_chk` (contact sheets and wiki copies made while applying the maps-research corrections)
- **Trailer frames:** `t_N` frames sit at (N−1)×0.5 s. The draft's and the image check's own extractions differ by about 0.2 s, so treat every trailer time as ±0.2 s.
- **"Images viewed" lists** have three groups: "draft" (opened by the drafter), "check" (opened by the image checker) and "edit" (re-opened by me during this edit). Sections changed by the maps-research corrections add a fourth group, "maps check" (opened for those corrections).

**Colour samples:** hex values are approximate median samples from the named image, not official codes [Inference]. Where two samplers disagree, I give the range.

## Quick summary of the conventions
- **Intact deaths:** many victims go limp and topple as one intact body, with no blood. In one trailer shot the corpse vanished in a single frame about 3 s later, with no fade [Observed].
- **Break-apart deaths:** some kills break the body into a few (about 4–7) large, clean, toy-like pieces, with no insides visible [Observed]:
  - bodies under a Phat Man blast
  - an irradiated Huggable
  - the Green Oliver after a B-1000 close-range attack (B-1000 is the Assault robot)

  What decides intact versus pieces is [Unverified]. The wiki says most Demo explosives "gib" [Fan-wiki].
- **Huggable "rainbow death":**
  - **Official merch:** SkyVu's 2023 merch art shows a headless pink Huggable with white stuffing and a vertical rainbow column [Canon: official merch art, not gameplay].
  - **Earlier games:** the wiki gives Huggables "rainbow blood" in the earlier games [Fan-wiki].
  - **BBG footage:** a Huggable breaks into plush pieces with gold sparkles [Observed].
  - No source shows confetti.
- **Effects style:** a mix of looks [Observed]:
  - soft, billowing particle fire and smoke
  - painterly cartoon flames
  - hard-edged faceted blasts and shards
  - flat octagonal ground rings
  - star-shaped hit sparks
  - 2D icons above heads

  Characters have a thick black ink outline in SkyVu's May 2013 trailer footage and in 2026 in-game captures with HUD, but not in the 2012–14 player captures on the wiki [Observed]. Some 2013 fan videos of Graham do have it [Observed: graham.addendum.md, Incidental findings 1]. So the outline was not added in 2026. Tying it to the 2013 trailer's advertised "HD Graphics" mode is [Inference].
- **Team colours:**
  - **Where they show:** character accents, the HUD, the kill feed and Plant the Bomb gear [Observed / Fan-wiki].
  - **Effects:** the only team-coloured effect the wiki documents for later BBG is the Energy Barrier glow (v2.3+). The Cloaking aura (BBR v1.4.2 only) and the Peek A Boo neon lines (v1.4.2 to v2.6) were removed [Fan-wiki].
  - **Exception:** some Huggables in the Steam trailer and screenshots (2013 footage [Inference, strong]) carry a white flag with rainbow dots, not a team flag [Observed].
- **Bearzooka:** coral-red with glowing orange panels in both an April 2013 BBR capture and the Steam trailer (2013 footage [Inference, strong]) [Observed]. For 2026, the 2026 dossier sees the same tube in tutorial and item-overview thumbnails [Observed, low-res: 2026.md, Bearzooka]. The green, hazard-striped Bearzooka is the BB Zombies one [Observed: wiki "Bearzooka in BBZ"].

---

## Overall VFX style (all weapons; BBR/BBG 2013 captures, the Steam media's 2013 footage and 2026 playtest captures)
- **Official text:**
  - "All assets in this game are created by human artists." [Canon] (Steam store text, app 4408320)
  - "An award-winning 4v4 class shooter with more personality than sense!" [Canon] (Steam short description)
- **Look:**
  - **Faceted, hard-edged volumes** are used for specific blasts, not as a general rule. Cores run near-white to lemon (#FFFFEA, #FFFF6B, #FEF376) [Observed: screen_02.jpg; trailer 26.5–27.8 s, 50.6–51.8 s]. Examples:
    - the nuke dome (26.6–27.8 s)
    - the burst on the irradiated Huggable (9.0–10.4 s)
    - the Shortest Parsec blast (50.5–51.7 s)
    - magenta and yellow shard bursts with white cores (30.8–32.2 s, screen_01)
  - **Fire comes in two looks:**
    1. Soft, blurred, billowing particle fire with dark orange-brown smoke. Examples: the plume off B-1000 at about 2.5–2.9 s, and the fire behind Wil at about 20–22 s [Observed: t_0006.jpg; C2/sheets2/t67.jpg, wf.jpg, ro.jpg].
    2. Painterly, semi-transparent cartoon flame shapes in orange (#F47E3E / #FAA751), as around the victim at 12.4–13.0 s [Observed: C/sheets/tl_zoom.jpg].
  - **Smoke:** faceted white and grey puffs after big blasts [Observed: Duo.png; trailer 51.3–51.7 s]. Soft dark smoke goes with the particle fire [Observed: wf.jpg].
  - **Shockwaves:** flat octagonal rings on the floor [Observed: screen_02.jpg; C2/sheets2/ta6.jpg, ta7.jpg, th2.jpg]:
    - white on Shortest Parsec (50.5–51.1 s)
    - white and grey by a Gold Digger tunnel mouth (9.0–10.4 s)
    - an orange cone from the sky, then orange and white rings together, over Gold Digger's open pit (52.5–53.5 s)
  - **Beams:** long flat ribbons with a white-hot core [Observed: screen_03.jpg; trailer 7.2–10.5 s, 38.3–41 s; C2/sheets2/tf3.jpg, tf4.jpg; rk30.jpg]:
    - pink beams (#FF5DFE / #FD51B1)
    - a thick yellow ribbon with pale concentric arc rings at the muzzle (38.5–39.4 s)
    - thin yellow tracers (2.8–3.0 s)
    - a thin purple beam (40.4–40.8 s)
  - **Electricity:** jagged cyan polylines (#80FFFE) [Observed: screen_03.jpg; ta6.jpg].
  - **Hit sparks:**
    - Beam hits make 4-point pink stars [Observed: screen_03.jpg; trailer 7.2, 7.4, 8.4, 35.3 s].
    - Melee hits scatter 5-point yellow cartoon stars [Observed: trailer 35.8–36.3 s; screen_00.jpg].
  - **Status indicators:** flat 2D sprites above heads [Observed: trailer 8.2–8.8 s; Images_(3).png; 0GuhKiAnNyc hq1/hq2].
  - **Hearts:** a stream of pink cartoon hearts trails a Huggable at 26.0 s [Observed: C2/crops2/hearts.png]. The wiki says Tough Love leaves the Huggable "trailed by a stream of hearts" [Fan-wiki], so it is probably Tough Love [Inference].
- **Ink outline:**
  - **The Steam media are 2013 footage:** the Steam trailer's class cards are pixel-identical to SkyVu's May 30, 2013 "BATTLE BEARS GOLD Trailer: Award-Winning Multiplayer Shooter Game" (rfAyqVJrli4, channel BATTLE BEARS) [Observed: greyscale MSE about 1–6 against medians of about 5,700–7,500]. The Steam screenshots are frames of the trailer [Observed: screen_02 matches trailer ≈50.6 s]. The trailer gameplay matches the 2013 video's 160×90 YouTube storyboard at an offset of about 4 s (45 of 55 frames from 2013 5–59 s) [Observed, storyboard size: 2026.md, "The Steam trailer is 2013 footage"]. So the trailer gameplay and the screenshots are May 2013 footage [Inference, strong]. The Space Oddity shot (about 30.0–32.8 s) and its frame screen_01 are no exception: the same moment, bloom included, is in the 2013 storyboard (2013 35–36 s = Steam 30.85–31.95 s) [Observed], so they are 2013 footage too [Inference, strong]. Only why the shot's pillar top blooms more than fan captures is [Unverified] (see Fire and burning).
  - In the Steam screenshots, the trailer gameplay and the Steam loop video, characters have a thick black ink outline [Observed: C/sheets/outline_compare.jpg; C/sheets/steam_extra.jpg]. The 2013 trailer's own class cards show it too [Observed: rfAyqVJrli4 maxres1–3]. So the outline was already in SkyVu's 2013 footage, not added in 2026.
  - It also appears in 2026 in-game captures with HUD [Observed: C7uFxvSZ10c maxresdefault, SkyVu's "Official Playtest Highlights", build "3.0.0"; HKbwq7PolNc maxres1, InstableGR's "Final PC Playtest (10/15/26)", build "3.0.7_2026.11.19_b7"]. So it is rendered in-game in 2026 [Observed].
  - 2012–14 player captures on the wiki have none (Oliver-battlefield-airpad-red-base-front.png, uploaded 2012-11-22; A_life_upside_down.png, uploaded 2013-04-27; Photo_19-04-13_12_02_26_PM.png, uploaded 2013-04-19; Screenshot_(509).png, uploaded 2014-03-16; Imawe.jpg, uploaded 2014-05-05) [Observed].
  - Some 2013 fan videos do show it: Gold Graham in the July 2013 2.0 beta and the circuit-pattern Graham skins in Sept–Nov 2013. Dec 2013 fan captures of Instagraham do not [Observed in the weapons research: graham.addendum.md, Incidental findings 1]. So the outline does not date the Steam trailer's Graham segment (about 7.25–10.5 s) to a later build, and the "2018 or later" reading is withdrawn [graham.md, Verifier's corrections, item 1]. The segment is in the 2013 storyboard (2013 12–13 s = Steam 7.95–8.95 s) [Observed, storyboard size], so it is 2013 footage [Inference, strong]. Why that segment's Graham is outlined when the Dec 2013 Instagraham captures are not is [Unverified].
  - The JustNubz "Closed Playtest #4" thumbnail shows the Gear Up menu (build text "3.0.5_2026.11.19_B1") with no thick outline on the menu model [Observed: C2/yt/lAtv_maxresdefault.jpg, C2/crops/lAtv_build.png].
  - The 2013 trailer description advertises "HD Graphics (Only available on higher end devices. App automatically detects what graphic mode to show)" [Canon: YouTube description of rfAyqVJrli4, May 30, 2013]. Tying the outline to that mode is [Inference]. Whether 2026 always shows it or makes it a setting is [Unverified].
- **HUD palette (BBR v1.4.x capture, April 2013):** health bar green ~#178602–#178702, red team ~#FC0101–#FD0101, blue team ~#003CFC–#023DF6 [Observed: A_life_upside_down.png].
  - A later BBG health bar "tells how much health a character has with numbers" [Fan-wiki: Health, Newhealthbar.png caption].
- **Firing / Projectile / Impact:** see the sections below.
- **Images viewed:**
  - draft: `W/visuals/steam_screens/screen_00.jpg`–`screen_04.jpg`; `C/sheets/trailer_sheet_0.jpg`–`trailer_sheet_8.jpg` (from `W/visuals/trailer/t_0001.jpg`–`t_0108.jpg`); `C/sheets/outline_compare.jpg`; `C/png/A_life_upside_down.png`; `C/sheets/steam_extra.jpg` (frames of https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4408320/extras/f7ecb9b2e78f0fd754cc7cf8220ad9b0.mp4); `C/png/Duo.png`
  - check: `C2/sheets2/t67.jpg`, `wf.jpg`, `te1.jpg`, `ta6.jpg`, `ta7.jpg`, `th2.jpg`
  - edit: `C/sheets/outline_compare.jpg`; `C/sheets/tl_zoom.jpg`; `C2/sheets2/t67.jpg`, `wf.jpg`, `ro.jpg`, `ta6.jpg`, `ta7.jpg`, `th2.jpg`, `te1.jpg`, `tf3.jpg`, `tf4.jpg`; `C2/crops2/hearts.png`; `C2/yt/lAtv_maxresdefault.jpg`; `C2/crops/lAtv_build.png`; `C2/png/A_life_upside_down.png`
  - maps check: `M/shortest_parsec_verify/frames/f_49.50.jpg`–`f_51.75.jpg` and `MC/sp_sheet.png` (Shortest Parsec); `MC/rf_sheet.png` (rfAyqVJrli4 maxres1–3 and maxresdefault); `M/shared_conventions/yt/th_C7uFxvSZ10c_maxresdefault.jpg`; `M/desert_airmine_verify/yt/th/HKbwq7PolNc_maxres1.jpg` and `MC/hk_crop.png`; `MC/wiki/s509.jpg` (File:Screenshot_(509).png); `MC/wiki/Imawe.jpg`; `M/shared_conventions/conv/Oliver-battlefield-airpad-red-base-front.png`; `C2/sheets2/ta6.jpg`, `ta7.jpg`, `th2.jpg` (Gold Digger)
- **Depiction for shorts:**
  - Use the effect type that matches the source:
    - soft billowing fire with dark smoke for flames and fireballs
    - hard-edged, flat-shaded, semi-transparent faceted shapes for nukes, radiation bursts and energy shards
    - flat octagonal rings sliding along the floor for shockwaves
    - star sparks on hits [Observed]
  - Ink outline on characters for the 2026 look and for SkyVu's 2013 trailer look; none for the look of the 2012–14 player captures on the wiki [Observed] (some 2013 fan videos of Graham do have it; graham.addendum.md, Incidental findings 1).
  - Exact frame counts and holds are [BBG News invention].
- **Confidence:** observed

## Ordinary deaths: intact collapse (all classes; BBR/BBG and the Steam trailer's 2013 footage)
- **Official text:** none found [Unverified].
  - The wiki implies a death animation exists. A Huggable using Mini Me "may occasionally… freeze in its position of death without going through the death animation" [Fan-wiki: Mini Me].
- **Look:** the victim goes limp and topples as one intact body. Four examples, all from the Steam trailer (2013 footage [Inference, strong], example 2's Space Oddity shot included; see Overall VFX style, Ink outline):
  1. **Temple victim (12.6–16.0 s):**
     - A white-headed, black-suited bear (skin unidentified) holding a red-and-black patterned long gun falls face-down after flames and a red skull, at 12.6–13.0 s [Observed: C/sheets/tl_zoom.jpg].
     - The body stays until about 15.9 s. At about 16.0 s it vanishes in one frame, with no fade, about 3 s after the fall [Observed: C2/sheets2/fz.jpg, tb3.jpg].
     - The image check measured almost no change in the rest of the frame (mean difference 2 vs 43 at the corpse), so it is not a cut. A trailer edit still can't be ruled out [Inference].
     - A sniper then steps out of the magenta dome at 16.1–16.2 s [Observed: tb3.jpg].
  2. **Sniper (31.7–32.7 s):** a sniper in blue pyjamas with a green face mask collapses face-down amid magenta and yellow shard bursts. The pink Huggable that hit her stands over the body [Observed: C2/sheets2/te1.jpg; t_0066.jpg]. That she is Astoria in a skin is [Inference].
  3. **Engineer (about 40.1 s):** a hard-hat Engineer collapses face-down, his gun on the floor [Observed: C2/sheets2/tf4.jpg].
  4. **Shield bear (40.4–41.4 s):**
     - A bear with a round purple-blue shield (magenta core) is hit by a thin purple beam at 40.4–40.8 s. He slumps and lies on the floor at 41.1–41.4 s [Observed: tf4.jpg].
     - His colour flickers between white-with-blue and dark slate blue throughout 39.6–41.4 s, and he lies dark as a corpse [Observed: tf4.jpg]. Which state is his base colour is [Unverified].
- **Removed:** the draft's fourth example, the "dying" green Heavy in A_life_upside_down.png, was wrong.
  - In that kill feed the green, red-outlined Heavy is the killer. The victim is a blue-outlined white Heavy with a red X over his portrait [Observed: C2/crops2/alu_kf.png].
  - Nothing in the image shows the green Heavy dying.
- **Blood:** no blood or darkening was seen. One corpse was briefly tinted red by the Dead Eye skull glow [Observed: trailer 13.7 s].
- **Firing:** n/a.
- **Projectile:** n/a.
- **Impact / end result:**
  - At the death site, "Three [Joules pickups] are dropped… and disappear after 10 seconds" [Fan-wiki: Pick-Ups; Joules]. This arrived as "Kill confirm Joule drops" in BBG v2.1, July 15, 2013 [Fan-wiki: Versions].
  - How long corpses stay in general is [Unverified]; one trailer corpse lasted about 3 s.
  - Separately, Wil moves through fire with his limbs splayed and his feet often off the floor, still intact [Observed: trailer 19.5–21.5 s; C2/sheets2/wf.jpg]. Whether he runs or is hurled is unclear: frames at 0.1 s steps show him just after eating a Batterito, so the fire may be his own (2026.md, trailer table; tillman.md, Big Shot) [Observed; Inference]. Whether it killed him is [Unverified]. (Oct 18 review: this replaced "Wil is hurled through fire … screaming".)
- **Images viewed:**
  - draft: `C/sheets/seq_tl.jpg`; `C/sheets/tl_zoom.jpg`; `C/sheets/seq_as.jpg`; `C/sheets/seq_sh.jpg`; `C/sheets/seq_wl.jpg`; `W/visuals/trailer/t_0066.jpg`; `C/png/A_life_upside_down.png`
  - check: `C2/sheets2/fz.jpg`, `tb3.jpg`, `tf4.jpg`, `te1.jpg`; `C2/crops2/alu_kf.png`, `alu_h.png`
  - edit: `C/sheets/tl_zoom.jpg`; `C2/sheets2/fz.jpg`, `tb3.jpg`, `te1.jpg`, `tf4.jpg`, `wf.jpg`; `C2/crops2/alu_kf.png`; `C2/png/A_life_upside_down.png`
- **Depiction for shorts:** a floppy cartoon pratfall onto the floor, with the body staying whole [Observed]. Then the body pops out of existence or there is a hard cut [Observed once]. Dizzy spirals or orbiting stars on the KO are [BBG News invention]. Never show blood; none appears in the game [Observed].
- **Confidence:** observed

## Break-apart deaths: clean chunks (bears, robots, Huggables; BBR/BBG and the Steam trailer's 2013 footage)
- **Official text** (joke item text; neither describes how a gib looks):
  - "Your enemies won't have a skull or bones after being hit with ice cold rockets!" [Game text via wiki] (Let It Cold)
  - "Just when you thought the huggable could not be any more dangerous, it takes it's head off and tries to kill you... to death." [Game text via wiki] (Losing Your Head)
- **Wiki:**
  - "The Double Hug is one of two of the Demo's weapons that do not gib players, the other is the Reverse Fountain." [Fan-wiki]
  - "Although the Demo has no other indication of being even partly organic, he has pink and red flesh as revealed when he is gibbed in-game." [Fan-wiki: Demo (BBG)]
  - When the Chub Scout "explodes with his suicidal weapons, he explodes into his default skin" whatever skin he wears [Fan-wiki: Headlights trivia].
  - Huggables are "full-on-fleshy in almost all of the games (except in Gold, where they are modified)" [Fan-wiki: Huggable].
- **Look:**
  - **Bear: the Green Oliver (4.6–5.6 s), in this order:**
    - 4.6 s: B-1000's cyan claw-blade swipe
    - 4.7 s: a yellow-orange flash
    - 4.8 s: orange speed streaks fill the background
    - 4.9 s: the Soldier's body comes apart
    - 5.4–5.5 s: a second cyan swipe, after the break-up

    [Observed: C2/sheets2/ta2.jpg, ta3.jpg, gib_check.jpg]

    The pieces fly up as big clean chunks: the head with its blue headband, the torso and legs with a blue belt band and bandolier, and his white-lilac backpack. No fireball sits on the body, and no inner surfaces or blood show [Observed].

    The orange streaks run until the "B-1000 / ASSAULT" intro card at 5.8 s, so they may be a trailer graphic rather than a weapon effect [Inference]. Which B-1000 weapon did it is [Unverified]. The source check's candidates from the Assault (BBG) page are Primus Sword, Metal Crush, Last Resort and Shock N Claw.
  - **Huggable: the orange Huggable (8.27–9.9 s):**
    - A final-stage radiation trefoil sits over it from about 8.27 to 8.9 s.
    - At 9.0 s it pops into its head, arms, legs and torso: orange plush with blue stitch marks (#F4972D / #FBBB3A). The pieces scatter until about 9.9 s.
    - The burst is a yellow-white blocky blast with white octagonal floor rings. Gold sparkles surround it just before [Observed: C2/sheets2/ta6.jpg, ta7.jpg; screen_03.jpg].
    - A white sphere wrapped in cyan lightning (a Light Matter-type blast) also bursts nearby from 8.7 s [Observed: ta6.jpg].
    - A radiation detonation is the most likely cause [Inference].
  - **Phat Man blast (26.2–27.8 s):**
    - At 26.2 s an orange-and-blue armoured bear and a pink Huggable stand in the corridor.
    - After the Phat Man lands at about 26.6 s, orange-and-blue armour pieces (a helmeted head among them) and pink pieces fly up through the translucent yellow faceted dome at 26.8–27.8 s [Observed: C2/sheets2/td1.jpg; C/sheets/nuke_gibs.jpg].
  - **Red armour chunks:**
    - Bright-red, armour-like chunks (a helmet or head piece, fists, forearms) are already in the air at 26.2 s, before the nuke lands [Observed: td1.jpg; screen_04.jpg]. So the nuke did not make them [Observed].
    - In screen_04 a red Huggable carrying a white rainbow-dot flag is airborne among them [Observed: screen_04.jpg; C2/sheets2/flags.jpg].
    - Who they belong to and what broke them is [Unverified]. The draft's "B-1000" is only a guess.
  - **Pattern:** about 4–7 large pieces per body, each keeping its colour and texture [Observed]. The "pink and red flesh" on Tillman gibs [Fan-wiki] was not seen [Unverified].
- **What decides it:**
  - Observed kills that broke bodies apart [Observed]:
    - a nuke blast
    - an irradiated target bursting
    - one B-1000 close-range attack
  - Observed kills that left bodies intact [Observed]:
    - flames plus a red skull
    - shard bursts
    - a purple beam
  - The rule behind it is [Unverified]. "Explosions and radiation gib" is only [Inference], supported by the wiki's Demo remarks.
- **Firing:** n/a.
- **Projectile:** n/a.
- **Impact / end result:** see Look.
- **Images viewed:**
  - draft: `C/sheets/bz_sheet.jpg`; `C/sheets/gib_green.jpg`; `C/sheets/graham_sheet.jpg`; `C/sheets/graham_zoom.jpg`; `W/visuals/steam_screens/screen_03.jpg`; `W/visuals/steam_screens/screen_04.jpg`; `C/sheets/s04_zoom.jpg`; `C/sheets/seq_bm.jpg`; `C/sheets/nuke_gibs.jpg`
  - check: `C2/sheets2/ta2.jpg`, `ta3.jpg`, `gib_check.jpg`, `td1.jpg`, `ta6.jpg`, `ta7.jpg`; `C2/tr/f_5.0.jpg`, `f_5.3.jpg`, `f_5.6.jpg`
  - edit: `C2/sheets2/ta2.jpg`, `ta3.jpg`, `gib_check.jpg`, `ta6.jpg`, `ta7.jpg`, `td1.jpg`, `flags.jpg`; `W/visuals/steam_screens/screen_04.jpg`
- **Depiction for shorts:** the victim pops into a handful of clean toy pieces (head, body, limbs, backpack or flag) that tumble with a puff of faceted smoke [Observed]. Never show insides:
  - For Huggables, white stuffing puffs out [Canon: SkyVu's official "Huggable Rainbow Explosion" merch art; not BBG gameplay].
  - For robots, loose bolts and springs [BBG News invention].
  - For bears, sparks [BBG News invention].

  A "reassemble and walk off" gag is [BBG News invention].
- **Confidence:** observed (what triggers it is unknown)

## Huggable deaths and "rainbow blood" (BB-1 / BB Zombies / BB Zero vs BBG; official 2023 merch)
- **Official text:**
  - "Remove your head and fire out a cutting death beam of rainbow essence." [Game text via wiki] (Headlights)
  - "By pressing small amounts of rainbow out of their bodies, Huggables can match the color of their surroundings…" [Game text via wiki] (Peek A Boo)
  - battlebears.com product "Huggable Rainbow Explosion T-shirt Black": "Official Huggable Rainbow Explosion T-shirt in Black." [Canon] (battlebears.com Shopify JSON, vendor "Battle Bears", published 2023-05-05; re-fetched live today)
    - The art shows a headless pink Huggable with a white belly patch.
    - White stuffing bursts from its neck, and a vertical rainbow column (red, orange, yellow, green, blue, lavender) shoots up from it [Observed: C2/web/rainbow_shirt_cu_view.jpg].
    - This is official SkyVu art, not BBG gameplay.
  - **BB-1 YouTube copy:** "Huggable viscera is pretty!" and "A huggable's rainbow soul can power a laser gun!" [Canon?, channel unconfirmed; description text not verified].
    - oEmbed confirms the titles "BB-1 Riggs 2/10: Firin' the Laser!" and "BB-1 Riggs 3/10: Massacre of the innocents" on the channel "BattleBearsGame".
    - Watch pages are blocked, so the description wording is unverified.
- **Wiki:**
  - "They have rainbow blood that flies out from the body vertically when the Huggable is beheaded" [Fan-wiki: Huggable].
  - "This weapon is seemingly based off of the death animation for the Huggable when it is shot in the head in Battle Bears -1, Battle Bears: Zombies and Battle Bears Zero, where the head would fly off far into the distance, leaving behind a trail of rainbows." [Fan-wiki: Headlights trivia]. That death animation belongs to the PvE games, and the link to Headlights is hedged.
  - "Dying while performing So Fly would cause the Huggable to arc and continue its stream of damaging rainbows. Double Rainbow would continue to rotate and the Headlights continue to fire in a straight line" [Fan-wiki: Huggable (BBG)]. It is worded in the past tense ("had the ability"), so this was probably fixed [Inference].
- **Pre-BBG art:** Scared_Oliver.PNG (Colbear page, uploaded 2012-03-27) shows a 2D dead pink Huggable lying on rainbow splatter [Observed: C2/crops2/scared.png]. It is pre-BBG evidence only.
- **Look in BBG:**
  - Bite Me's bear-trap jaws carry iridescent rainbow smears, which the wiki calls "Huggable blood" [Observed: HuggyBiteMeCR.png; Fan-wiki: Bite Me].
  - The one observed BBG Huggable death is a plush break-apart with gold sparkles and no rainbow spray [Observed: trailer 9.0 s].
- **The 3.3–3.8 s rainbow fan:**
  - A pink red-team Huggable is clipped by a yellow tracer. A fan of red, yellow, green and blue streaks (#E35254 / #E3B935 / #41A13E) bursts upward from a magenta point at its feet. It narrows into a vertical column over about 0.5 s, and the Huggable glows pink-white [Observed: C2/sheets2/ta2.jpg].
  - At 3.8 s it is still standing [Observed], so no death is shown.
  - The best match is Peek A Boo: "a short burst of rainbow energy will be emitted above the Huggable" [Fan-wiki] → [Inference].
- **Other rainbow effects:**
  - **So Fly:** in the Steam loop an orange Huggable flies arm-first, trailing white-core shards of yellow, green, orange, cyan and violet [Observed: steam_extra.jpg].
    - The So Fly menu art (Photo_27-04-13_11_29_45_AM.png) shows a rainbow wave trail with a white burst [Observed: C2/sheets2/x_6.jpg].
    - The wiki says it flies "forward a short distance in a stream of rainbows" [Fan-wiki]. So the loop is So Fly [Inference, strong].
  - **Double Rainbow!:** "two spinning rainbows that rotate around the user" [Fan-wiki].
    - A rainbow ring circles the orange Huggable's waist at trailer 7.2–8.5 s [Observed: C2/sheets2/ggz.jpg].
    - The Double Rainbow! menu art (Photo_27-04-13_11_29_40_AM.png) shows rainbow rings around a Huggable's waist [Observed by the image check].
- **Firing / Projectile:** n/a; see the Huggable class dossier for the abilities.
- **Impact / end result:** see Look.
- **Images viewed:**
  - draft: `C/sheets/rainbow_sheet.jpg`; `C/sheets/rainbow_zoom.jpg`; `C/png/HuggyBiteMeCR.png`; `C/sheets/misc3.jpg`; `C/sheets/steam_extra.jpg`; `C/sheets/graham_zoom.jpg`; `C/png/Huggable-suction-pose.png`
  - check: `C2/web/rainbow_shirt_cu_view.jpg`; `C2/crops2/scared.png`; `C2/sheets2/x_6.jpg`; `C2/png2/Photo_27-04-13_11_29_40_AM.png`
  - edit: `C2/web/rainbow_shirt_cu_view.jpg` (product JSON re-fetched to `E/web/shirt.json` from https://battlebears.com/products/huggable-rainbow-explosion-t-shirt-black.json); `C2/crops2/scared.png`; `C2/sheets2/x_6.jpg`, `ggz.jpg`, `ta2.jpg`
- **Depiction for shorts:**
  - For a Huggable KO, use SkyVu's own merch look: the head pops off, white stuffing puffs from the neck, and a straight vertical rainbow column shoots up [Canon: official merch art].
  - In a BBG-match setting, note that gameplay shows plush chunks with gold sparkles instead [Observed].
  - "Rainbow confetti" appears in no source; label it [BBG News invention].
- **Confidence:** partial

## Damage feedback (all classes; BBR/BBG and the Steam trailer's 2013 footage)
- **Official text:** none found [Unverified].
- **Look:**
  - **Hit flash:** the clearest one is the gold bear turning flat lemon yellow under the yellow beam at 38.3 s [Observed: C2/sheets2/tf3.jpg]. The orange Huggable turns bright yellow at 7.9 s and 8.2 s [Observed].
  - **Two-state flicker (not a confirmed hit flash):**
    - The cyan Huggable switches between bright #05E4FC and dark teal #447A96 at about 34.8–35.6 s, including frames with no visible hit [Observed: C2/sheets2/cy.jpg].
    - The shield bear switches between white-with-blue and dark slate (39.6–41.4 s) [Observed: tf4.jpg].
    - Which state is the base colour is [Unverified].
  - **Beam contact:** a pink 4-point star spark [Observed: screen_03.jpg; trailer 7.2, 7.4, 8.4, 35.3 s].
  - **Melee contact:** small yellow-white 5-point stars [Observed: trailer 35.8–36.3 s; screen_00.jpg].
  - **HUD health bar:**
    - Top-left, "A green bar indicates how much health is remaining, which degrades to red as it is depleted." [Fan-wiki: Health]
    - Green and part-red bars appear in screenshots [Observed: Sonic_wave_glue_bomb.png; Glue_bomb_on_a_wall.png].
    - A later version added numbers to the bar [Fan-wiki].
  - **Damage numbers:** none in any image examined [Observed absence; Unverified overall].
  - **Pain barks:** e.g. Tillman "You call that PAIN?!" [Fan-wiki: Demo (BBG)].
  - **Enemy markers:** a red triangle and green name text float above an enemy [Observed: 0GuhKiAnNyc maxresdefault/hq1 (fan video, wiki file created 2014-01-03, so BBG era)]. What the marker colours mean is [Unverified].
  - **Lock-on reticle:** a red "( ! )" bracket reticle appears in an Assassin view (Imagef.png, Pain Field page) and in an Engineer view (Radioactive_puddle.png) [Observed]. So it is not specific to Demo or Sniper, and its meaning is [Unverified]. The draft's "Demo and Sniper lock-on" reading was wrong.
- **Firing / Projectile:** n/a.
- **Impact / end result:** see Look.
- **Images viewed:**
  - draft: `C/sheets/graham_zoom.jpg`; `C/sheets/riggs_cupcake.jpg`; `W/visuals/steam_screens/screen_00.jpg`; `W/visuals/steam_screens/screen_03.jpg`; `C/sheets/effects1.jpg`; `C/sheets/yt_0GuhKiAnNyc.jpg`; `C/crops/gamma_hq2_x2.png`
  - check: `C2/sheets2/gb.jpg`, `cy.jpg`, `tf4.jpg`; `C2/crops/imagef_ret.png`
  - edit: `C2/sheets2/tf3.jpg`, `cy.jpg`, `tf4.jpg`, `yt_gr.jpg`; `C2/sheets/icons_check.jpg` (Radioactive_puddle reticle)
- **Depiction for shorts:** a one-frame flat bright flash on the target plus a star spark: pink for beams, yellow for punches [Observed]. Floating damage numbers would be [BBG News invention].
- **Confidence:** observed

## Headshots, sniper locks and (no) critical hits (Sniper primaries Viperifle, Capital Pains, Mamba's Boy, Dead Eye; Dead Eye from BBR v1.4.3, nerfed BBG v2.20)
- **Official text:**
  - "Got a problem? The Deadeye is your solution. She may not have the biggest clip but she definitely has the biggest kick. If you understand the value of power, this is the rifle for you." [Game text via wiki] (Dead Eye)
  - The wiki cites a SkyVu blog post for the Dead Eye (battlebears.com/blog/item/138-the-weekend-update). It could not be read [Unverified].
- **How a headshot works:**
  - **Scoped warning:** "When a player is locked onto by an opponent's sniper rifle (reticule turns green), a red crosshair will appear over the player's head, indicating a headshot is in the process of being targeted." [Fan-wiki: Status Effects]
  - **White lock:**
    - A white-lock shot "is guaranteed to kill the opponent, regardless of his/her remaining health. When an opponent is killed in this way it is a headshot, and shows up on the update feed differently" [Fan-wiki: Dead Eye].
    - For the Dead Eye it takes 9 s to green-lock and "a further 2" to white-lock [Fan-wiki].
  - **Kill-feed card:** the killer's portrait (Astoria, blue outline), the words "HEAD SHOT", and the victim's portrait (Tillman) under a red crosshair [Observed: C2/sheets2/misc_z.jpg (hs3 crop); Sonic_wave_glue_bomb.png].
- **Critical hits:**
  - No BBG crit system was found. "Critical Chance / Critical Damage" columns are on the wiki's "Rocket Launcher" page, a Battle Bears Overclock weapon (Tillman (BBO)) [Fan-wiki]. So BBG probably has no crits [Inference].
  - Instant kills [Fan-wiki: Health]: "The only weapons which can instantly kill regardless of any health remaining include the Viperifle, Capital Pains, Mamba's Boy, Dead Eye through the process of a headshot and Gamma Ray, Gernobyl, Radiation Rod, Gamma Burst, Solar Wind Scar, MuskIt through radiation".
  - Natural hazards also kill instantly [Fan-wiki: Health].
- **Firing:** for the Dead Eye, "a single, red, stream-like bullet that erupts into a flurry of glowing, transparent buffalo skulls" [Fan-wiki].
- **Projectile:**
  - A thin, pale white zigzag trail runs to the victim at 12.2 s [Observed: C/sheets/tl_zoom.jpg].
  - It does not match the wiki's "red, stream-like bullet". So the Dead Eye identification is only [Inference].
- **Impact / end result:**
  - Painterly cartoon flames burst around the victim. Then a large translucent red horned skull (core ~#FC2034–#FE2B35, shadow ~#800E33–#971031) rises and fades while he topples face-down [Observed: trailer 12.4–13.7 s; tl_zoom.jpg].
  - What happens to the head on a headshot is [Unverified]; no image shows it.
- **Images viewed:**
  - draft: `C/sheets/tl_zoom.jpg`; `C/sheets/seq_tl.jpg`; `C/crops/headshot_feed.png`; `C/sheets/effects1.jpg`
  - check: `C2/crops/hs_feed_x4.png`; `C2/sheets2/hs_j.jpg`
  - edit: `C/sheets/tl_zoom.jpg`; `C2/sheets2/misc_z.jpg`
- **Depiction for shorts:**
  - A red crosshair blinking over the target's head, the shot, then a "HEAD SHOT"-style card in original art, not the game's UI [BBG News invention].
  - For a Dead Eye kill, a ghostly red horned skull rising over a whole, toppling body [Observed]. The head stays on [BBG News invention].
- **Confidence:** partial

## Kill feed, rewards and announcer text (HUD; BBR v1.4.x Apr–May 2013 and BBG 2013–14)
- **Official text:** none.
- **Look:**
  - "[killer portrait] KILLS [victim portrait]", with portraits outlined in team red or blue and a red X over the victim's portrait [Observed: C2/crops2/alu_kf.png (BBR capture, April 2013); AZt_huguhzc hq3].
  - "HEAD SHOT" card (see above).
  - "SUICIDE" lines; bomb deaths count as suicides [Observed: Plant_the_bombbbbbb_b.png (uploaded 2013-05-20, BBR era); Fan-wiki: Plant the Bomb].
  - "ASSIST +11" with a lightning-bolt icon on a dark maroon hexagon [Observed: alu_kf.png].
  - Large green "OH BABY" text mid-screen [Observed: A_life_upside_down.png]. Its meaning is [Unverified]; possibly a streak call [Inference].
  - "XP +25" and "⚡+100" under a kill line [Observed: 0GuhKiAnNyc hq3, BBG era].
  - Stacked "⚡ +25" lines [Observed: Glue_bomb_on_a_wall.png, uploaded 2013-12-22]. That these are Joule pickups is [Inference].
  - End-of-match results screens: "RED TEAM WINS", team kill/death columns and "TOTAL DAMAGE" [Observed: wiki 001.png and 002.png via C2/sheets2/x_1.jpg; capture date unknown].
- **Wiki:** "100 Joules automatically for each kill (as of version 2.17)" [Fan-wiki: Joules].
- **Firing / Projectile:** n/a.
- **Impact / end result:** see Look.
- **Images viewed:**
  - draft: `C/png/A_life_upside_down.png`; `C/sheets/yt_AZt_huguhzc.jpg`; `C/sheets/yt_0GuhKiAnNyc.jpg`; `C/sheets/effects1.jpg`
  - check: `C2/crops2/alu_kf.png`, `az_feed.png`
  - edit: `C2/crops2/alu_kf.png`; `C2/png/A_life_upside_down.png`; `C2/sheets2/yt_gr.jpg`, `yt_az.jpg`, `x_1.jpg`
- **Depiction for shorts:** a red-vs-blue portrait strip with "KILLS" (red X on the loser) or "HEAD SHOT" and a lightning-bolt reward, redrawn in original art with no game UI or logos [BBG News invention].
- **Confidence:** observed

## Team colours, red vs blue (all classes and effects; BBR/BBG and the Steam media's 2013 footage)
- **Official text:** "compete for dominance across competitive 4v4 multiplayer modes" [Canon] (Steam).
- **Look, characters (accents):**
  - **Soldier:**
    - The default skin is "featuring a bandana, arm and leg bands, and ammo straps, all coloured to the team. As with all characters, also a unique backpack." [Fan-wiki: Soldier (BBG)/Skins]
    - The bands are red in menus and on red-team players [Observed: OliverSkin.png; Photo_19-04-13_12_02_26_PM.png; A_life_upside_down.png].
    - They are blue on blue-team players [Observed: trailer 3.9–4.8 s, Green Oliver skin with blue headband, cuffs and belt band; AZt_huguhzc thumbnails, brown Oliver in a blue headband].
  - **Huggable flag:**
    - The Huggable "has a flag respective to the team color that only shows up in a match" [Fan-wiki: Huggable (BBG)].
    - Team flags are observed: red at trailer 3.3 s; blue at 7.2–9 s, in screen_00.jpg and on the pink Huggable in screen_04.jpg [Observed].
    - The Steam trailer and screenshots also show Huggables with a white flag carrying rainbow-coloured dots: the cyan Huggable at about 34.8–35.6 s, and a red Huggable in screen_04.jpg [Observed: C2/sheets2/flags.jpg, cy.jpg].
    - That footage is from 2013 [Inference, strong], so the flag is not a 2026 change [Inference]. Whether it is a skin flag or a change to team flags is [Unverified].
  - **Tillman:**
    - Red and black on the red team, in the 3D shot at about 27.9–28.3 s that leads into his intro card, and on the card itself [Observed: C2/sheets2/te1.jpg, td1.jpg]. The menu render Ohmagawdyas.png is red and black too.
    - White, blue and black on the blue team [Observed: trailer 18–22 s; wf.jpg].
  - **B-1000:** maroon on red, "dark blue" on blue [Fan-wiki: B-1000 (Skin)].
  - **Sniper:** "gloves with the colour of the team colour" [Fan-wiki: Astoria (Skin)].
- **Look, HUD:** red score on the left (~#FC0101), blue on the right (~#023DF6), and kill-feed portrait outlines in team colour [Observed: A_life_upside_down.png; HEAD SHOT crop].
- **Look, effects:**
  - **Cloaking aura:** after BBR v1.4.2 Cloaking emitted an aura "which sports the user's team color". In v1.4.3 "Cloaking was improved to give the user complete transparency when standing still", and Peek A Boo trivia says "In v1.4.3, the neon outline was removed only for Cloaking" [Fan-wiki: Cloaking; Peek A Boo]. So the team-coloured cloak aura existed only in BBR v1.4.2.
  - **Peek A Boo neon lines:** "As of v1.4.2, neon red/blue lines (depending on the player's team) will highlight the player's most prominant features"; "In v2.6, the neon outline was removed from Peek A Boo and their overall visibility reduced." [Fan-wiki: Peek A Boo]
  - **Energy Barrier (Assault, v2.3+):** "the player will begin to glow their team coloured" [Fan-wiki]. This is the only team-coloured effect documented for later BBG.
  - **Plant the Bomb:** uses a bomb and tube "in each team's color". The blue bomb is a round blue cartoon bomb with a fuse [Observed: Blue-bomb.png, uploaded 2012-07-04, BBR era; Fan-wiki].
- **Projectile:** projectiles are not team-coloured in the footage [Observed]:
  - Yellow tracers come from both sides.
  - Pink beams come from a red, rock-skinned Riggs (34–36 s) and from off-screen shooters (8.2 s, 9.1–9.8 s).
  - The red-bodied, rainbow-helmeted Graham at 7.3–7.6 s throws lime-green goo, not a pink beam.
  - A purple beam hits a blue-team bear.

  As a general rule this is [Inference].
- **Firing:** n/a.
- **Impact / end result:** n/a.
- **Images viewed:**
  - draft: `C/sheets/oliver_skins.jpg`; `C/sheets/bz_sheet.jpg`; `C/sheets/yt_AZt_huguhzc.jpg`; `C/sheets/rainbow_zoom.jpg`; `C/sheets/graham_zoom.jpg`; `C/sheets/seq_wl.jpg`; `C/sheets/misc4.jpg`; `C/png/Blue-bomb.png`; `C/png/A_life_upside_down.png`
  - check: `C2/sheets2/ggz.jpg`, `te1.jpg`, `flags.jpg`
  - edit: `C2/png/OliverSkin.png`, `Photo_19-04-13_12_02_26_PM.png`, `Ohmagawdyas.png`; `C2/sheets2/ggz.jpg`, `flags.jpg`, `cy.jpg`, `te1.jpg`, `td1.jpg`, `wf.jpg`, `yt_az.jpg`; `C2/sheets/icons_check.jpg` (Blue-bomb); `W/visuals/steam_screens/screen_04.jpg`
- **Depiction for shorts:**
  - Team identity goes on accents: the Soldier's headband, cuffs and ammo straps, the Huggable's flag and Tillman's armour panels. Weapon effects keep each weapon's own colours [Observed/Inference].
  - The BBG News default stays red team.
  - A team-coloured glow is accurate only for the Energy Barrier in a 2014+ setting. A red or blue cloak rim is accurate only for a BBR v1.4.2 setting (cloak) or a v1.4.2–v2.6 setting (Peek A Boo) [Fan-wiki].
- **Confidence:** observed

## Explosions in general (all explosive weapons; BBR/BBG and the Steam trailer's 2013 footage)
- **Official text:**
  - "Phat chance that you'll be dodging this baby. Flies out of sight and, just when you've forgotten about it, hits fast and hard like a liquored up grandpa." [Game text via wiki] (Phat Man)
  - "It's not to be taken lightly WAKKA WAKKA WAKKA!" [Game text via wiki] (Light Matter)
  - "Tillman really likes fireworks, so much so he turns a beautiful fountain into a deadly shower of sparks and fire!" [Game text via wiki] (Reverse Fountain)
- **Look:**
  - **Fire and fireballs:** soft, blurred, billowing orange-yellow fire with dark orange-brown smoke [Observed: t_0006.jpg; C2/sheets2/t67.jpg, ro.jpg, wf.jpg]. The draft's "faceted fireball with grey faceted smoke" was wrong for both cited shots.
  - **Phat Man (Demo secondary):**
    - The bomb in the 26.0 s shot has a yellow nose with an X-eyed smiley. That matches the wiki's Phat Man render (Tillman_Phat_Man_copy.png, uploaded 2012-07-22): an olive bomb with a yellow-black trefoil and an X-eyed smiley nose [Observed: C2/sheets2/td1.jpg, extra_z.jpg]. So the identification no longer rests on inference.
    - It rises on a yellow-white flame trail and comes down on one [Observed: Up1.png, Down1.png; wiki captions "Phat Man rising into the air" and "Phat Man descending"; both uploaded 2013-05-20, BBR era].
    - The yellow column above the bomb in screen_04 and at 26.2–26.5 s is that falling flame trail, not a separate light beam [Observed: screen_04.jpg; td1.jpg].
    - The blast is a translucent yellow faceted dome that fills the corridor and flings bodies apart [Observed: trailer 26.6–27.8 s].
    - Then comes a mushroom cloud of translucent white faceted puffs [Observed: Duo.png; wiki caption "Phat Man's mushroom cloud in comparison to Piece Maker's"; BBR-era upload].
    - "As with most explosive weapons, players are prone to suicide when using the Phat Man." [Fan-wiki]
  - **Piece Maker:** the wiki render (PeaceMaker.png) shows a rainbow-striped bomb on Tillman's back [Observed: C2/sheets2/extra_z.jpg].
  - **Radiation self-explosion:** "same as the Piece Maker and Phat Man explosion animation", and "The size of the explosion depends on the victim's size" [Fan-wiki: Gamma Ray]. The blast radius is "between 150-200 units" [Fan-wiki: Status Effects]. It was observed as a yellow-white blocky blast plus white floor rings and plush pieces (trailer 9.0 s), and as a full-screen yellow-white flash in 2014 fan footage [Observed: ta6.jpg; 0GuhKiAnNyc hq3].
  - **Light Matter (Demo primary, BBR v1.3.1+):**
    - It "releases a single, slow moving blue orb"; the explosion is "notably large, blinding, and electrified" [Fan-wiki].
    - The orb is blue with cyan lightning (wiki caption "Light Matter projectile") [Observed: Light_Matter_Orb.jpeg via C2/sheets2/extra_z.jpg].
    - The blast is an opaque white sphere wrapped in jagged cyan lightning [Observed: Photo.png, wiki caption "Light Matter explosion", uploaded 2012-06-30, BBR era].
    - The same look appears at trailer 8.7–10.4 s and in screen_03.jpg [Observed]. That identification is [Inference].
  - **Dark Matter (Demo primary):**
    - It "fires purple orbs that travel in straight lines and explode on impact"; on detonation "a sphere of energy blocks the target's vision" [Fan-wiki].
    - The projectiles are pink-magenta swirling orbs with cyan lightning (wiki caption "Dark Matter projectiles") [Observed: Dearly_matter_close_up.jpeg via extra_z.jpg].
  - **Plant the Bomb:** the detonation is a huge white-grey faceted cloud [Observed: Plant_the_bombbbbbb_b.png, BBR era]. The bomb beeps and pulses during its last 30 s [Fan-wiki].
  - **Shockwave rings:**
    - Expanding white octagonal rings, with a yellow faceted blast and white faceted puffs, on Shortest Parsec (50.5–51.7 s) [Observed: th2.jpg].
    - White and grey rings by a Gold Digger tunnel mouth (9.0–10.4 s) [Observed: ta6.jpg, ta7.jpg].
    - An orange cone from the sky, then orange and white rings together, over Gold Digger's open pit (52.5–53.5 s) [Observed: th2.jpg].
    - Thin yellow vertical streaks come down from the sky at about 49.6–50.3 s (reported by the source check) and 51.3–51.5 s [Observed: th2.jpg]. Both they and the 52.5 s cone resemble a falling nuke [Inference]. Which weapons made these effects is [Unverified].
  - **Other explosive looks:**
    - Fireworks "expode into a flurry of damaging, orange sparks" [Fan-wiki]. The menu render shows Tillman with red rockets [Observed: C2/sheets2/x_3.jpg].
    - Losing Your Head makes "a bright blue blast" [Fan-wiki].
- **Firing / Projectile:** see the weapon dossiers.
- **Impact / end result:**
  - Many explosives also hurt the user:
    - Bearzooka: "The user is very prone to suicide while using the Bearzooka." [Fan-wiki]
    - The Soldier class template: "Use his starting Bearzooka carefully as it is easy to kill yourself with it!" [Fan-wiki: Template:Class:Soldier (BBG); not marked as official game text]. This line is about the Bearzooka only.
    - Phat Man: "prone to suicide" [Fan-wiki].
  - With a Shield, "Players can still suicide from natural hazards, but not from their own weapons." [Fan-wiki: Pick-Ups]
- **Images viewed:**
  - draft: `W/visuals/trailer/t_0006.jpg`; `C/sheets/seq_wl.jpg`; `C/sheets/seq_bm.jpg`; `C/sheets/nuke_gibs.jpg`; `C/sheets/effects1.jpg`; `C/sheets/effects2.jpg`; `C/sheets/misc3.jpg`; `C/sheets/seq_ov.jpg`; `W/visuals/steam_screens/screen_02.jpg`; `W/visuals/steam_screens/screen_04.jpg`
  - check: `C2/sheets2/t67.jpg`, `wf.jpg`, `td1.jpg`, `th2.jpg`, `extra_z.jpg`
  - edit: `C2/sheets2/t67.jpg`, `wf.jpg`, `ro.jpg`, `td1.jpg`, `th2.jpg`, `ta6.jpg`, `ta7.jpg`, `extra_z.jpg`, `x_3.jpg`; `W/visuals/steam_screens/screen_04.jpg`
  - maps check: `MC/sp_sheet.png` (Shortest Parsec); `C2/sheets2/th2.jpg`, `ta6.jpg`, `ta7.jpg` (Gold Digger)
- **Depiction for shorts:**
  - **Ordinary fireball:** a soft, billowing orange fireball with dark smoke [Observed].
  - **Nuke:** the smiley-nosed bomb dives on its flame trail. Then a hard-edged translucent yellow faceted dome, flat octagonal rings sliding along the floor, and white faceted mushroom puffs [Observed].
  - **Light Matter:** a white sphere crackling with cyan lightning [Observed].
  - A soot-face gag on a survivor is [BBG News invention].
- **Confidence:** observed

## Irradiated (Gamma Ray, Gernobyl, Radiation Rod, MuskIt for the Engineer; Plasma Shotgun and Gamma Burst for the Combat Tech; Solar Wind Scar for the Soldier; BBR v1.4.3 to BBG v2.9+; seen in the Steam trailer's 2013 footage)
- **Official text:**
  - "Turn your enemies in to walking explosives with this radioactive ray gun. It does very little damage on initial impact, but once you charge them up all the way...BOOM! The radioactive symbol over their head indicates how charged they are. The bigger they are, the longer it takes to blow them up, however yielding a much larger and more aggressive explosion." [Game text via wiki] (Gamma Ray)
  - "Straight from the core of the Ursa Major. Warning may cause spontaneous bear combustion if in contact for long periods of time." [Game text via wiki] (Radiation Rod, v2.5)
  - "Saberi Smash! Creates a deadly radiation area around the player." [Game text via wiki] (Gamma Burst, v2.9)
  - "You know a great way to exfoliate your skin, white hot plasma! *Caution may cause severe salt*" [Game text via wiki] (Plasma Shotgun, v2.9)
  - "Cut a star in half and imbued it with power. It's said that even standing in it wake will singe the flesh." [Game text via wiki] (Solar Wind Scar)
  - "The musk of the Gyrnobal has been known to turn people into mutants, but most blow up." [Game text via wiki] (MuskIt)
- **Look:**
  - "a yellow circle will appear over the player's head and a noise from a Geiger counter will begin sounding… three portions of the circle will dissolve into the common radioactivity symbol" [Fan-wiki: Status Effects].
  - The wiki's four stage icons cut progressively more wedges out of a disc (1–24, 25–49, 50–74 and 75–99 radiation points; 100 points means explosion) [Fan-wiki; Observed: Hazard-3.png, Hazard-0.png].
  - The clicking speeds up as radiation rises, and "the radioactivity symbol will gradually deform and the effect will wear off" when exposure stops [Fan-wiki].
  - **Steam trailer (2013 footage):** a final-stage trefoil (yellow ~#FACD21–#FCCD25 on a black disc) at full size from its first frame (about 8.27 s) until the burst (about 8.9 s) [Observed: C2/sheets2/tz.jpg]. No ring-to-trefoil progression is shown. The draft's "grows over about 0.6 s" was not supported.
  - **2014 fan footage (BBG):** a large yellow wedge-disc, an intermediate stage, above the target [Observed: 0GuhKiAnNyc hq2 via C2/sheets2/yt_gr.jpg].
- **Firing:**
  - **Gamma Ray:**
    - "a short-ranged constant yellow beam"; "The end of the projectile emits a type of smoke-like vapour." [Fan-wiki]
    - The best visual candidate is in the trailer at 38.5–39.4 s: an Engineer's orange gun fires a thick yellow ribbon beam with pale concentric arc rings at the muzzle [Observed: C2/sheets2/tf3.jpg]. The 2014 "Gamma Ray Demonstration" thumbnails show the same muzzle rings [Observed: yt_gr.jpg].
    - No trefoil was seen over that trailer target, so the identification is [Inference].
  - **Gernobyl (BBR v1.4.3):**
    - "irradiating globs of light green goo" that leave puddles [Fan-wiki].
    - In the trailer, Graham (red body, rainbow-striped helmet, brown backpack) throws lime-green goo blobs with glowing green trails at the orange Huggable at about 7.3–7.6 s. Glowing green splats land on the floor [Observed: C2/sheets2/ggz.jpg].
    - A lime faceted chunk (#B0E030 / #D0F050) stays beside the blast at 9.0–10.4 s and in screen_03 [Observed: ta6.jpg, ta7.jpg].
    - The puddle is a big translucent lime blob (#A1D22C / #C2E330) [Observed: Radioactive_puddle.png, uploaded 2013-05-10, BBR era].
    - The weapon itself is a goo-dripping creature in a carry cage [Observed: Gernobil.png and Gernobyl.png via C2/sheets2/x_3.jpg].
    - So the irradiating weapon in the 7–9 s trailer shot is most likely the Gernobyl [Inference]. The draft's "the visible beam there is pink" was a misreading: the pink beam comes from off-screen.
  - **Radiation Rod (v2.5):** a placed "glowing radiation field" [Fan-wiki].
  - **MuskIt:** a shotgun cone that "shoots green stuff of what appears to look like bug spray" [Fan-wiki].
  - **Plasma Shotgun:** radiation 25 per hit (infobox) [Fan-wiki]. Its look is [Unverified].
  - **Gamma Burst:** "a purple disk-like structure will emerge from the Combat Tech's backpack", then "a yellow dome-like structure around the user" [Fan-wiki].
  - **Solar Wind Scar:** "an orange slash, that travels in a straight direction. It will travel through walls, and when it hits someone, a dark, circular radiation belt will spawn" [Fan-wiki].
- **Projectile:** see Firing.
- **Impact / end result:**
  - At full radiation the target "will die instantly in a relatively large explosion. The player and other enemies within the blast radius will also receive damage upon explosion." [Fan-wiki: Gamma Ray]
  - It breaks the body into pieces [Observed: trailer 9.0 s].
- **Images viewed:**
  - draft: `C/sheets/graham_zoom.jpg`; `C/sheets/graham_sheet.jpg`; `C/sheets/icons.jpg`; `C/crops/gamma_hq2_x2.png`; `C/sheets/yt_0GuhKiAnNyc.jpg`; `C/sheets/misc3.jpg`
  - check: `C2/sheets2/ggz.jpg`, `tz.jpg`, `tf3.jpg`, `yt_gr.jpg`; `C2/sheets/hazard_alpha.png`
  - edit: `C2/sheets2/ggz.jpg`, `tz.jpg`, `ta6.jpg`, `ta7.jpg`, `tf3.jpg`, `yt_gr.jpg`, `x_3.jpg`; `C2/sheets/icons_check.jpg` (Hazard-3, Hazard-0, Radioactive_puddle)
- **Depiction for shorts:**
  - A yellow-black trefoil sprite over the victim, with Geiger clicks speeding up [Fan-wiki]. The stages can fill in as the gag builds [Fan-wiki], although the trailer jumps straight to the full trefoil [Observed].
  - Then a yellow-white blocky flash, floor rings and a toy-piece pop [Observed].
  - Gernobyl goo is lime-green globs with glowing trails [Observed].
  - The victim trembling first is [BBG News invention].
- **Confidence:** observed

## Poisoned (Mother of Nature for the Heavy; Chaos Toss, Fear Orbit, Hazard Toy, Toxic Plague for the Assassin; Toxic Rifle for the Combat Tech; Kelowna for the Arbiter; BBG, Toxic Rifle v2.15, Toxic Plague v2.17, Kelowna v2.31)
- **Official text:**
  - "Shoots poisonous berries at your enemies that drain their health over time." [Game text via wiki] (Mother of Nature)
  - "Spray your enemy with toxins that deal poison damage overtime and can stack with each bullet!" [Game text via wiki] (Toxic Rifle, v2.15)
  - "Pop one of these babies out onto the field and watch the neon gas show!" [Game text via wiki] (Toxic Plague, v2.17)
  - "Banned from elementary schools world wide, this weapon is as dangerous as it looks!" [Game text via wiki] (Hazard Toy)
  - The Kelowna is "the only Arbiter primary to lack a description" [Fan-wiki].
- **Look:**
  - "a purple/green skull will appear over the player's head" [Fan-wiki: Status Effects].
  - Mother of Nature uses "a small purple skull" [Fan-wiki].
- **Firing / Projectile:**
  - **Mother of Nature:** "a large purple berry" fired in an arc [Fan-wiki].
  - **Chaos Toss:** "a gleaming orb" lobbed from a skeletal hand [Fan-wiki]. The menu render shows a lime-green crystal hand [Observed: ChaosTossCR.png via C2/sheets2/x_1.jpg].
  - **Fear Orbit:** two poison orbs circling Botch [Fan-wiki]. The render shows lime-green geodesic orbs with green glow trails [Observed: FearOrbitCR.png via extra_z.jpg, x_3.jpg].
  - **Hazard Toy:** a projectile that "explodes upon contact and poisons" [Fan-wiki]. The render shows a translucent green radiation-symbol fan toy in Botch's hand [Observed: HazardToy.png via C2/sheets2/x_4.jpg].
  - **Toxic Plague:** a bouncing ball; "As it moves, the ball leaves a green gas trail behind it" [Fan-wiki].
  - **Kelowna:** "a small projectile that explodes once it comes in contact with a surface"; it produces "a clone of Arbiter doing the Creepin taunt among clouds of poison" [Fan-wiki].
- **Impact / end result:**
  - Mother of Nature: "a large purple plume of poison", 4 damage a second for 10 s [Fan-wiki].
  - Chaos Toss: "a toxic green cloud" [Fan-wiki].
  - Toxic Plague: poison stacks if the target keeps moving in the trail [Fan-wiki].
  - Kelowna: 8 damage a second for 2 s. The wiki says a licensed pop song plays on a Kelowna kill [Fan-wiki]; BBG News should not reproduce that music.
- **Images viewed:**
  - draft: none of the poison effect in play.
  - check: `C2/sheets2/x_1.jpg`, `x_3.jpg`, `x_4.jpg`
  - edit: `C2/sheets2/x_1.jpg`, `x_3.jpg`, `x_4.jpg`, `extra_z.jpg`
- **Depiction for shorts:**
  - A faceted gas cloud in the weapon's own colour (purple for Riggs's berry, lime-green for Botch's weapons), with a little cartoon skull bobbing over the victim's head [Fan-wiki/Observed renders].
  - The Combat Tech and Arbiter poison colours are [Unverified].
  - A green tint on the victim's face is [BBG News invention].
- **Confidence:** documented

## Slowed, glued, bound or held (Slow Motion Field special; Glue Bomb, Arbiter primary; Bind Field, aka "Slow Field", Engineer secondary v2.6; Phantom Hug, Huggable secondary v2.2; Freeze Blast, Heavy secondary; BBG)
- **Official text:**
  - "Slows down all nearby enemies for a limited time." (Slow Motion Field)
  - "Glue plus bomb equals very slow battle bears." (Glue Bomb)
  - "Make your opponents feel as old as you do. All enemies within the field stop and dream about bingo." (Bind Field)
  - "The Huggable's ability to love will make time seem like it comes to a halt. When actually it's just your feet and you're about to die." (Phantom Hug)
  - "Blastin you with FREEEZEEEEE!!!" (Freeze Blast)
  - All [Game text via wiki].
- **Look:**
  - Slowed players get "a yellow Z" over their head [Fan-wiki].
  - Slow Motion Field: "a yellow circle forms around the player" [Fan-wiki]. The menu icon pairs a bear with a snail [Observed: SlowMotionField.png].
  - **Wiki contradiction:** Status Effects lists "Bind Gun" as a slowing weapon, but that page now redirects to the Adrenaline Gun, which speeds enemies up (see Speed) [Fan-wiki].
- **Firing / Projectile:**
  - **Glue Bomb:**
    - Thrown in an arc; it sticks to a surface and explodes after 1 s [Fan-wiki].
    - On a doorway wall it is a dark sphere with a glowing magenta four-point star [Observed: C2/sheets2/misc_z.jpg, glue_wall crop]. The draft's "purple blob" was imprecise.
    - It matches the render of Sanchez holding a dark orb with a magenta glow [Observed: Glue_Bomb.png via x_3.jpg].
  - **Bind Field:** "a prickly purple-green ball" [Fan-wiki]. Graham holds a brown ball with purple nodes and green seams [Observed: Slowfield.png].
  - **Phantom Hug:** "a cluster of pink energy in the shape of a Huggable" [Fan-wiki]. A glowing translucent pink Huggable silhouette [Observed: PH_MenuDisplay.png].
  - **Freeze Blast:** "small blue projectiles" [Fan-wiki]. The render shows Riggs with a pale cyan-white blaster [Observed: Freeze.png via x_3.jpg].
- **Impact / end result:**
  - Glue Bomb: blue concentric rings on the ground [Observed: Sonic_wave_glue_bomb.png]; 2 s slow [Fan-wiki].
  - Bind Field: a force field with a 75% slow for 3 s [Fan-wiki].
  - Phantom Hug: the target cannot move or turn for 2.5 s [Fan-wiki].
  - Freeze Blast: slowing pools on the floor [Fan-wiki].
- **Images viewed:**
  - draft: `C/sheets/effects1.jpg`; `C/sheets/effects2.jpg`; `C/sheets/misc4.jpg`
  - check: `C2/sheets2/misc_z.jpg`; `C2/png2/Glue_Bomb.png`
  - edit: `C2/sheets2/misc_z.jpg`, `x_3.jpg`; `C2/sheets/icons_check.jpg` (SlowMotionField)
- **Depiction for shorts:** feet stuck in glue rings, or a pink hug-ghost wrapping the victim, with a big yellow "Z" floating up [Fan-wiki/Observed]. Snail-speed walk cycles are [BBG News invention].
- **Confidence:** partial

## Stunned (Sucker Punch; Heavy secondary; BBG)
- **Official text:** "Lobs a projectile that will stun the target for a few seconds." [Game text via wiki]
- **Look:**
  - "a blue Nuggs will appear over the player's head… having them appear dazed until recovered from the effect" [Fan-wiki: Status Effects].
  - A round blue bird circled by grey swoosh arrows above the target [Observed: Images_(3).png, wiki caption "Stunned Status symbol", uploaded 2013-04-09, BBR era].
  - The wiki's Blue Nugg image is a cyan-blue bird with a white crest [Observed: Blue_Nugg.png via C2/sheets2/x_1.jpg].
  - Before a change the stun icon was "a green question mark" [Fan-wiki].
- **Firing:** SuckerPunch.png is a Gear Up menu render of a rock-skinned Riggs holding the pink, cube-headed, Huggable-like launcher, not firing it [Observed].
- **Projectile:**
  - "a small, pink Huggable-like head" that stays solid after hitting and can push players [Fan-wiki].
  - A blurred pink, fuzzy, head-like object flies past with pink star sparks near the irradiated Huggable at about 8.2–8.4 s [Observed: C2/sheets2/pinkhead.jpg]. Whether it is a Sucker Punch head is [Unverified].
- **Impact / end result:** fully immobilised for 2.6 s [Fan-wiki].
- **Images viewed:**
  - draft: `C/crops/stun_x3.png`; `C/png/SuckerPunch.png`
  - check: `C2/png/SuckerPunch.png`
  - edit: `C2/sheets/icons_check.jpg` (Images_(3)); `C2/sheets2/x_1.jpg`, `pinkhead.jpg`
- **Depiction for shorts:** a pink plush head bonks the victim, a little blue Nugg bird circles their head, and they sway dazed [Fan-wiki/Observed]. Tweeting sounds are [BBG News invention].
- **Confidence:** partial

## Frozen (S'no Matter, Demo primary; Let It Cold, Demo secondary; BBG v2.15+)
- **Official text:**
  - "It S'no Matter how fast you can move, I can just freeze you!" [Game text via wiki] (S'no Matter)
  - "Your enemies won't have a skull or bones after being hit with ice cold rockets! These rockets explode on impact and freezes the opponent for a small duration" [Game text via wiki] (Let It Cold)
- **Look:**
  - SkyVu-style concept art titled "Tillmans S'no Matter" (wiki file Snomatterconcpetar.jpg, uploaded 2015-03-29) [Observed: C2/png2/Snomatterconcpetar.png]:
    - two launcher designs with snowflakes, cyan hex gems and a red tartan wrap
    - a silhouetted Demo lobbing a shot in an arc
    - the target encased in jagged cyan and white ice crystals
  - It is concept art, not in-game.
  - Let It Cold's render shows blue rockets with cartoon eyes on Tillman's arms [Observed: Letitcold.png via C2/sheets2/x_4.jpg].
  - The in-game frozen-state visual is [Unverified].
- **Firing:**
  - S'no Matter fires "a slow moving gray projectile at a straight trajectory" [Fan-wiki].
  - The concept art shows a lobbed arc instead, a conflict [Observed vs Fan-wiki].
- **Projectile:** see Firing.
- **Impact / end result:** the S'no Matter blast "freezes anyone in the blast radius for 2 seconds, leaving them unable to move or rotate the camera"; it may also freeze teammates [Fan-wiki].
- **Images viewed:**
  - draft: none.
  - check: `C2/crops2/sno_bottom.png`; `C2/png2/Snomatter.png`; `C2/png2/Letitcold.png`
  - edit: `C2/png2/Snomatterconcpetar.png`; `C2/sheets2/x_4.jpg`
- **Depiction for shorts:** encase the victim in jagged cyan-and-white ice crystals, as in the concept art [Observed: concept art; in-game look Unverified], and hold for the 2 s beat [Fan-wiki].
- **Confidence:** partial

## Fire and burning (Flame Thrower, Heavy primary v2.14; Cosmic Fire, Assassin primary v2.3; Batterito and Killdoba, Chub Scout secondaries; BBG)
- **Official text:**
  - "Burn your enemies with the power of hot morning coffee without the lawsuit!" (Flame Thrower)
  - "Sometimes "killing it with fire" is the only way to deal with something, amirite?" (Cosmic Fire, v2.3)
  - "Set you mouth and you opponent's faces ablaze with fiery power of the batterito. Once consumed, fire will spew from your mouth and movement speed is increased until the inferno dies down." (Batterito, Wil's default secondary per the Batterito (BBG) page)
  - All [Game text via wiki].
- **Look:**
  - No burning status appears in the wiki's Status Effects list [Fan-wiki]. Flame weapons do contact damage only [Fan-wiki].
  - Painterly orange-yellow flame shapes (#F47E3E / #FAA751) lick around a victim just before his death [Observed: trailer 12.4–13.0 s; C/sheets/tl_zoom.jpg]. Their source is [Unverified].
  - In screen_01 small flames rise from short orange-yellow sticks lying on the floor beside a jump pad, not from vents [Observed: screen_01.jpg; s1_flames.png crop]. screen_01 is a frame of the Steam trailer's Space Oddity shot at about 30.7 s [Observed]. That shot is 2013 footage like the rest of the trailer [Inference, strong]: the same moment, bloom included, is in the storyboard of SkyVu's May 2013 trailer (2013 35–36 s = Steam 30.85–31.95 s) [Observed: 2026.md, "The Steam trailer is 2013 footage"], and the maps research's Space Oddity dossier now dates it to 2013 too. Its pillar top blooms to near-white, unlike 2013 and 2021 fan captures [Observed in the maps research: space-oddity.md]; why it blooms more is [Unverified].
    - The flames fit the Señor Potato Cannon's "piping hot french fries", which "do damage over time" [Fan-wiki transcription of SkyVu's 1.4.3.1 notes], so they are weapon VFX, not a map feature [Inference]. The Wil dossier's addendum covers the fries.
    - No fire hazard is documented on Space Oddity [Fan-wiki: Space Oddity].
  - Flame Thrower render: Riggs with a red fuel can and a black barrel [Observed: Flamethrower_.png via C2/sheets2/x_3.jpg].
  - Cosmic Fire render: a green-white flame in Botch's palm [Observed: CosmicFire.png via extra_z.jpg].
- **Firing:**
  - Flame Thrower: "red-colored flames" [Fan-wiki].
  - Cosmic Fire: the fire in Botch's palm "begins to burn much more vigorously" for 5 s [Fan-wiki].
  - Batterito: the user "breathes damage-dealing fire from their mouth for 6 seconds" with a speed boost [Fan-wiki].
  - The Killdoba "is a reskin of the Batterito" [Fan-wiki].
- **Projectile:** see Firing.
- **Impact / end result:** see Look.
- **Images viewed:**
  - draft: `C/sheets/tl_zoom.jpg`; `W/visuals/steam_screens/screen_01.jpg`
  - check: `C2/sheets2/fire_check.jpg`, `wilfire.jpg`
  - edit: `C/sheets/tl_zoom.jpg`; `C2/sheets2/x_3.jpg`, `extra_z.jpg`, `wf.jpg`
  - maps check: `W/visuals/steam_screens/screen_01.jpg`; `M/shared_conventions_verify/crops/s1_flames.png` (screen_01 crop)
- **Depiction for shorts:** cartoon flames on contact; Wil breathing fire after a Batterito is documented [Game text via wiki]. A smoking bottom or a sooty face afterwards is [BBG News invention]. No lingering burn icon [Fan-wiki].
- **Confidence:** partial

## Controls reversed, blinded and smoke (Sake Bomb, Soldier secondary; Daydreamer, Sniper secondary; Spin Baby Spin, Arbiter primary; Dark Matter and Light Matter, Demo; Smoke Screen, Assault secondary v2.7; BBR/BBG)
- **Official text:**
  - "A shot from this will make you wine and stumble." (Sake Bomb)
  - "Turn your opponents' daydream into a nightmare…" (Daydreamer)
  - "When I spin you spin!" (Spin Baby Spin)
  - "B1000 has his own version of hide and seek. It is called: Hide in smoke and then kill everyone!" (Smoke Screen, v2.7)
  - All [Game text via wiki].
- **Look:**
  - **Controls reversed:** "a green question mark will appear over the player's head"; "background music will be disabled and other sounds will feature an mild echo" [Fan-wiki: Status Effects]. The items capable are Sake Bomb, Daydreamer and Spin Baby Spin [Fan-wiki].
  - **Spin Baby Spin:** "a projectile weapon that explodes on contact"; "based off of the Fidget Spinner" [Fan-wiki].
  - **Sake Bomb:** the render is a round bottle with a Daruma-style face [Observed: SAKEBOMB.png via C2/sheets2/x_6.jpg].
  - **Daydreamer:** the armed Daydreamer is "only noticeable by a small white crystal sticking out from the ground" [Fan-wiki].
  - **Smoke Screen:** "a huge, harmless white cloud" [Fan-wiki].
  - **Dark Matter and Light Matter:** both blind with their blasts [Fan-wiki]. The Light Matter blast is a white sphere with cyan lightning [Observed: Photo.png].
- **Firing / Projectile / Impact:** as above.
- **Images viewed:**
  - draft: `C/sheets/misc3.jpg`
  - edit: `C2/sheets2/x_6.jpg`, `extra_z.jpg`
- **Depiction for shorts:** a green "?" over a stumbling bear, with the soundtrack muffled and echoing [Fan-wiki]. It is a strong comedic beat for a short [Inference].
- **Confidence:** documented

## Speed (Caffeine Injection special; Speed Field, Arbiter primary; Adrenaline Gun, Arbiter default primary; Batterito; BBG)
- **Official text:**
  - "Grants the user brief super speed!" (Caffeine Injection)
  - "Gotta go fast! Any player who enters the field gets their speed doubled!" (Speed Field)
  - "The only bad thing about being faster than light is that you always live in darkness" (Adrenaline Gun). The wiki notes it was "submitted by community member Wilpower784".
  - All [Game text via wiki].
- **Look:**
  - **Caffeine Injection:**
    - "the symbol of a coffee cup will appear above the player and there will be a trail of white dust around their feet" [Fan-wiki].
    - A white coffee mug floats above an Engineer [Observed: 0GuhKiAnNyc hq1, hq2 via C2/sheets2/yt_gr.jpg].
    - The menu art shows a bear sprinting with a mug [Observed: CaffeineInjection.png via x_1.jpg].
  - **Speed Field:** "a hazy, light yellow orb" that becomes a dome with a "translucent light yellow haze" [Fan-wiki].
  - **Adrenaline Gun (the old "Bind Gun" page redirects here):**
    - It "shoots a purple beam. It is not completely accurate as the beam tends to move in an oval-like wave. When an enemy is hit by the beam, they will be drastically sped up for a brief amount of time." Its Speed Effect is "50% per hit" for 0.5 s [Fan-wiki].
    - A thin purple beam hits the shield bear at 40.4–40.8 s [Observed: C2/sheets2/tf4.jpg]. That it is the Adrenaline Gun is a weak [Inference].
- **Firing / Projectile:** see Look.
- **Impact / end result:** Caffeine Injection lasts 10 s [Fan-wiki].
- **Images viewed:**
  - draft: `C/sheets/yt_0GuhKiAnNyc.jpg`; `C/crops/gamma_hq2_x2.png`
  - edit: `C2/sheets2/yt_gr.jpg`, `x_1.jpg`, `tf4.jpg`
- **Depiction for shorts:** a steaming coffee-mug icon bobbing over the head and dust puffs at the feet [Fan-wiki/Observed]. Speed lines are [BBG News invention].
- **Confidence:** partial

## Cloak (Cloaking special; Cloak Field, Arbiter primary; Peek A Boo, Huggable; BBR v1.4.2 to BBG v2.14)
- **Official text:**
  - "Become invisible! Activation will make you transparent to all players! Great for avoiding sniper locks! Note: Moving will affect your transparency!" (Cloaking)
  - "Sanchez is really good at hide and seek. Any player who enters the field gains cloaking!" (Cloak Field)
  - Both [Game text via wiki].
- **Look:**
  - **Cloaking:**
    - Mechanism: "When moving, the player will be 75% transparent, and when standing still, the transparency will be 95%. If damage is taken, the player will be completely revealed for 0.5 seconds" [Fan-wiki].
    - History [Fan-wiki]:
      - BBR v1.4.2 added a team-coloured aura.
      - v1.4.3 gave "complete transparency when standing still" and removed the outline.
      - "After Update 2.14, Cloaking was changed once again to be less effective, with visibility increased when both moving and standing still."
    - Whether the 75%/95% figures predate 2.14 is [Unverified].
    - The menu icon is a dark silhouette with a glowing green outline [Observed: Cloaking.png, uploaded 2013-01-13, BBR era].
  - **Cloak Field:** a dome with a "translucent light purple haze" [Fan-wiki].
  - **Peek A Boo:**
    - A short rainbow burst, then invisibility [Fan-wiki].
    - "Prior to v1.4.2, the neon lines were absent but the Huggable was instead marked by a light greyish shape"; from v1.4.2 to v2.6 it had neon team lines; v2.6 removed them and reduced visibility [Fan-wiki].
    - The menu art shows a green-outlined empty Huggable silhouette in white cloud puffs [Observed: Photo_27-04-13_11_29_57_AM.png via C2/sheets2/x_6.jpg].
- **Firing / Projectile:** n/a.
- **Impact / end result:** see Look.
- **Images viewed:**
  - draft: `C/png/Cloaking.png`; `C/sheets/rainbow_zoom.jpg` (possible Peek A Boo burst)
  - edit: `C2/sheets/icons_check.jpg` (Cloaking); `C2/sheets2/x_6.jpg`, `ta2.jpg`
- **Depiction for shorts:**
  - A heat-haze, see-through character that flickers fully visible when hit [Fan-wiki].
  - Add a faint red or blue rim only for a BBR v1.4.2 cloak, or a v1.4.2–v2.6 Peek A Boo [Fan-wiki]. A later-BBG cloak has no team rim.
- **Confidence:** partial

## Damage up and damage down (Bearscream Sandwich pickup; Propbearganda special; Pain Field, Assassin secondary; Tough Love, Huggable; Invulnerable Field, Arbiter secondary; Energy Barrier, Assault secondary v2.3; BBR/BBG)
- **Official text:**
  - "This field speeds projectiles to cause pain faster. Anyone inside takes 50% more hurting from dangerous things flying around…" (Pain Field)
  - "Increases all nearby teammates damage by 25% for a limited time. Stay close to your friends for maximum effect." (Propbearganda)
  - "With great power comes great invulnerability" (Invulnerable Field)
  - "Make those pesky bullets less pesky with this brand new shield! Upon activation all damage recieved is reduced by 50%!" (Energy Barrier)
  - All [Game text via wiki].
- **Look:**
  - **Bearscream Sandwich buff:**
    - A swirling magenta and pink electric ring around the player's body (~#E76FE6–#F060F0, light #FCBEFC) [Observed: A_life_upside_down.png, wiki caption "Soldier with the Bearscream Sandwich pick-up"; BBR capture, April 2013].
    - The wiki contradicts itself on the bonus: "doubles the damage of all the player's weapons for 20 seconds" (Bearscream Sandwich page) vs "Triples the amount of damage" (Pick-Ups page) [Fan-wiki].
  - **Propbearganda:**
    - "speakers will rise from the player's back playing a tune" (the Bearbershop Quartet) plus "a purple fist symbol" [Fan-wiki].
    - The menu art shows a speaker pole with a purple glow and a purple fist icon [Observed: Propbearganda.png via C2/sheets2/x_6.jpg].
  - **Pain Field:**
    - "a small compact pink orb… grows massively and transforms into a large barrier of compact hexagons"; no overhead icon [Fan-wiki].
    - A magenta faceted cellular sphere (#D457EB / #A758C9) [Observed: Imagef.png].
    - The trailer shows a matching magenta faceted dome (~#CD20ED–#D621F9, light ~#F124FC–#FD28FE, shadow #9819B2) over the temple stairs, with a sniper stepping out of it [Observed: trailer 14.0–16.2 s; C2/sheets2/tb3.jpg]. That it is the Pain Field is [Inference], backed by the wiki's pink hex-orb render PainFieldCR.png (image check).
  - **Tough Love:** "the Huggable is trailed by a stream of hearts and all melee damage inflicted to enemies in its duration will be boosted in damage by 50%" [Fan-wiki]. A stream of pink cartoon hearts at trailer 26.0 s [Observed: C2/crops2/hearts.png].
  - **Invulnerable Field:** a dome from "a hazy, light blue orb" [Fan-wiki]. Damage Resistance has "No overhead icon shown" [Fan-wiki: Status Effects].
  - **Energy Barrier:** a team-colour glow for 2 s [Fan-wiki].
- **Firing / Projectile:** n/a.
- **Impact / end result:** see Look.
- **Images viewed:**
  - draft: `C/png/A_life_upside_down.png`; `C/sheets/effects1.jpg`; `C/sheets/trailer_sheet_2.jpg`; `C/sheets/seq_tl.jpg`
  - check: `C2/sheets2/pf.jpg`; `C2/png2/PainFieldCR.png`
  - edit: `C2/png/A_life_upside_down.png`; `C2/sheets2/tb3.jpg`, `fz.jpg`, `x_6.jpg`; `C2/crops2/hearts.png`
- **Depiction for shorts:**
  - A crackling pink ring around a sandwich-powered bear [Observed].
  - A giant translucent magenta honeycomb bubble for the Pain Field [Observed].
  - A trail of pink hearts behind a Tough Love Huggable [Observed/Fan-wiki].
  - Speakers rising from the back for Propbearganda [Fan-wiki].
- **Confidence:** partial

## Healing and life drain (Health pickups, Healing Tent; Drain Field, Arbiter secondary v2.16; BBG)
- **Official text:** "Toss this sucker at the nearest enemy and watch as his life force is drained from him and transferred to you!" [Game text via wiki] (Drain Field, v2.16)
- **Look:**
  - "Health can only be restored on field using the Healing Tent or health pickups such as Health Packs and Imperial Basket Grandes." [Fan-wiki: Health]
  - **Drain Field:**
    - In play: "the Arbiter will toss the leech-like creature that flies in an arc. When it makes contact with any solid surface, a dark field will be formed with bats in it"; "The field formed appears to be a projection of a live creature wearing sunglasses." [Fan-wiki]
    - Concept art (wiki caption "Concept Art for Drain Field", titled "Sanchez drain field") shows a red-striped, horned, leech-like blob with a dark band over one eye (possibly the sunglasses) wrapped in white swirl rings [Observed: C2/png2/Drainfield.png]. It also shows a grey dome with a cross and syringe and cross-shaped health icons [Observed].
    - The infobox image Drainfield.jpg (caption "Arbiter with the Drain Field") shows Sanchez holding an orange, fleshy, slit-eyed creature (source check crop `C2/crops/drain_arm.png`). That this is the thrown leech is [Inference].
  - The visual of a heal itself is [Unverified].
- **Firing / Projectile / Impact:** see Look.
- **Images viewed:**
  - draft: `C/sheets/effects2.jpg`
  - check: `C2/crops2/drain_top.png`; `C2/crops/drain_arm.png`
  - edit: `C2/png2/Drainfield.png`
- **Depiction for shorts:** a lobbed leech creature that splats into a dark bubble full of cartoon bats, with a sunglasses-wearing creature projected in it [Fan-wiki; concept art Observed]. A green "+" sparkle on healing is [BBG News invention].
- **Confidence:** partial

## Pickups: Shield, Health Pack, Imperial Basket Grande, Bearscream Sandwich, Joules (and Gas, which is not a pickup) (map items; BBR/BBG 2013+)
- **Official text:**
  - The Imperial Basket Grande comes from a BB-1 gag ad: "Ease your hunger with 3 pounds of deep fried pain, pain, pain!…" [Game text via wiki, BB-1].
  - Steam: "Grab your A Salt Rifle, Bearzooka and those Turkish SW Boots" [Canon].
- **Look:**
  - **Shield:**
    - "four green shields will circle around the player, making them immune to damage for 10 seconds (they can still die by falling off a stage)" [Fan-wiki].
    - Translucent green heater-shield shapes around the player, low resolution [Observed: Maxresdefault(100).png, wiki caption "A player with shields", uploaded 2013-05-23, BBR era].
    - A clearer view: a translucent pale yellow-green heater shield with a cross emblem in front of an Engineer who shows the "SHIELDS" HUD tag [Observed: 0GuhKiAnNyc maxresdefault via C2/sheets2/yt_gr.jpg, BBG era].
  - **Health Pack:** a white-grey box with an orange cross [Observed: HealthPack.png]. It heals up to 35 and respawns in 45 s [Fan-wiki].
  - **Imperial Basket Grande:** a red basket of golden fried chunks on white paper [Observed: Imperial-basket-grande.png]. It gives +50% of max health, can overheal to 200%, and respawns in 60 s [Fan-wiki].
  - **Bearscream Sandwich:** an ice-cream sandwich with an angry brown bear face, red eyes and yellow teeth [Observed: Bearscream_Sandwich.png]. It respawns every 90 s and is "usually found at the center of maps" [Fan-wiki].
  - **Joules:**
    - A blue lightning bolt (~#1090D0) on a dark maroon hexagon (~#300000) [Observed: Joule.png, sampled; uploaded 2012-02-04, BBR icon].
    - Three drop where a player dies (25 each) and vanish after 10 s, since BBG v2.1 [Fan-wiki].
  - **Gas:** a currency, shown as a red jerry-can icon [Observed: Gas.png], also used for the Gas Meter. It is not an in-match pickup [Fan-wiki: Gas; Gas Meter].
- **Barks:**
  - Wil (Chub Scout): "Force field, FORCE FIELD!" (Shield) and "Omnomnomnom..." (Health Pack) [Fan-wiki: Chub Scout (BBG)].
  - Tillman: "Gives me chills!" (Shield) [Fan-wiki: Demo (BBG)].
- **Firing / Projectile:** n/a.
- **Impact / end result:** see Look.
- **2026 status (partly answered):**
  - Three floating blue lightning bolts appear in a frame thumbnail of SkyVu's "Official Playtest Highlights" video [Observed: C7uFxvSZ10c hq2]. They match the Joule icon and the three-per-death drop, so Joule drops survive into 2026 [Inference, strong].
  - The Oct 14, 2026 Steam banner for the final playtest, set on No Bear's Land, shows a floating angry bear face (the Bearscream Sandwich design) and a green shield-with-plus icon on the keep roof [Observed: Steam news image b7c8f8f133ad960899cce9f3d232b42847891d08.png]. The wiki puts the Shield "on the top of each base tower" [Fan-wiki: No Bear's Land]. Reading the two icons as the Sandwich and the Shield is [Inference].
  - Whether the Health Pack and Imperial Basket Grande survive is [Unverified].
- **Images viewed:**
  - draft: `C/sheets/icons.jpg`; `C/crops/shield_crop.png`; `C/crops/shield_crop2.png`; `C/png/Maxresdefault(100).png`
  - check: `C2/yt2/0GuhKiAnNyc_maxresdefault.jpg`; `C2/crops2/joule2.png`
  - edit: `C2/sheets/icons_check.jpg` (HealthPack, Imperial-basket-grande, Bearscream_Sandwich, Joule, Gas); `C2/sheets2/yt_gr.jpg`, `misc_z.jpg` (shield2 crop); `C2/png/Joule.png` (sampled)
  - maps check: `M/shared_conventions_verify/crops/c7hq2.png` (C7uFxvSZ10c hq2); `M/shared_conventions/news/b7c8f8f133ad960899cce9f3d232b42847891d08.png` (the banner); `M/shared_conventions_verify/crops/pt5_center.png`, `pt5_keep.png`
- **Depiction for shorts:** four green crest-shields orbiting a bear, and a sneering ice-cream sandwich that turns its eater pink-electric [Observed/Fan-wiki]. Exact pickup idle spin and bob is [BBG News invention].
- **Confidence:** partial

## Respawn, suicide and hazards (match flow; BBR/BBG)
- **Official text:** none found.
- **Look:**
  - "To change loadouts, tap the "Loadouts" button, above the "Tap to Respawn" button" [Fan-wiki: Loadouts]. The Loadouts feature arrived in BBG v2.2 (August 21, 2013) [Fan-wiki: Versions].
  - "When the player respawns, they have the shields for 4.5 seconds (to discourage spawn killing)" [Fan-wiki: Shield]. The 2014 HUD shows a green-shield "SHIELDS" tag [Observed: 0GuhKiAnNyc hq1, hq2]. That it relates to spawn shields is [Inference].
  - Any spawn-in flash or teleport effect is [Unverified].
- **Hazards:**
  - "There are also natural hazards which can instantly kill a player regardless of any other factors, with the exception of Shortest Parsec's laser, which does damage quickly over time. These hazards will cause a suicide and deduct a kill in addition to causing a death." [Fan-wiki: Health]
  - "Suicides are penalized in team battle" arrived in BBG v2.19, April 26, 2015 [Fan-wiki: Versions].
  - Lava surrounds the Aztec Attack map, which is the only Aztec map [Observed: trailer ≈43.1–45.7 s; File:Maxresdefault(100).jpg; Fan-wiki: Category:BBG Maps]. That trailer shot is 2013 footage [Inference, strong].
- **Firing / Projectile:** n/a.
- **Impact / end result:** see Look.
- **Images viewed:**
  - draft: `C/sheets/yt_0GuhKiAnNyc.jpg`; `C/sheets/trailer_sheet_7.jpg`; `C/png/Plant_the_bombbbbbb_b.png`
  - edit: `C2/sheets2/yt_gr.jpg`
  - maps check: `MC/aztec_sheet.png` (trailer 43.05–46.7 s); `M/aztec_attack_verify/img/Maxres100.jpg` (File:Maxresdefault(100).jpg)
- **Depiction for shorts:** the bear pops in under orbiting green shields [Fan-wiki]. Any teleport sparkle is [BBG News invention].
- **Confidence:** partial

## Bearzooka (Soldier/Oliver default secondary; BBR v1.0 onward through BBG; named in the 2026 Steam text) — colour conflict resolved
- **Official text:**
  - "The basic weapon of any Soldier. Does a good amount of damage, with a decent area of effect (AOE). Useful for all situations." [Game text via wiki]
  - "Grab your A Salt Rifle, Bearzooka and those Turkish SW Boots" [Canon] (Steam)
  - Wiki: "In BBG and BB0, it is a rocket launcher with red and orange lines. In BBZ and BB-1 it is just a dark green rocket launcher." [Fan-wiki: Bearzooka]
  - The Soldier class has `addedgame = BBR`, `addedversion = 1.0` [Fan-wiki: Template:Class:Soldier (BBG)].
- **Look:**
  - **Shape:** an octagonal tube that pinches in the middle and flares at both ends [Observed: Photo_19-04-13_12_02_26_PM.png (BBR v1.4.x capture, uploaded 2013-04-19); trailer 3.9–4.8 s].
  - **Body colour:** coral to brick red [Observed]:
    - ~#D35550–#E16957 in the Steam trailer's 2013 footage (my sample #E05F4F from `C/tr/bz_full_4.3.png`)
    - ~#A14243–#B36161 in the April 2013 BBR capture (my sample #A24D4E)
  - **Details** [Observed]:
    - a row of glowing orange chevron and rectangle window panels (~#F08020–#FFAA31 in the trailer, ~#F18922–#F48D20 in the April 2013 capture)
    - two grey metal collars (#7F7D7C)
    - a grey-on-red checkered rear flare
    - a black bore with a grey rim
  - **Concept art:** a red tube, grey bands, orange chevrons and a red/grey checkered flare, plus "THROWN MISSILE" sketches of a round bomb and a dynamite bundle [Observed: Bearzooka_Concept.png, uploaded 2012-11-26]. Whether the thrown missiles were ever used in game is [Unverified].
  - **Size:** about 2–2.5× Oliver's head height long [Inference from foreshortened images].
  - **Carry:** shouldered with the muzzle forward [Observed: 2013 capture; trailer 3.9–4.8 s], or held low at the hip from behind [Observed: AZt_huguhzc thumbnails, BBR era].
- **Where "green, hazard-striped" came from:**
  - BB Zombies' Bearzooka is literally that. Bear.jpg (wiki caption "Bearzooka in BBZ", uploaded 2013-01-01) shows a weapon-select screen with a dark green tube, yellow-and-black hazard stripes and a "BEARZOOKA" stencil [Observed: C2/png2/Bear.png].
  - Separately, the Steam trailer's coral Bearzooka is held by a green-furred bear (the Green Oliver recolour skin, here on the blue team) whose brass-bullet bandolier reads as yellow-and-black stripes [Observed: C2/sheets2/ta2.jpg; GreenSkin.png].
  - Which of these misled the character file is [Unverified]. Either way, green with hazard stripes is not the BBR/BBG Bearzooka.
  - BBG's other green "Bearzookas" are Tillman's yellow-green Twin Bearzookas (Demo primary, v2.17, March 8, 2015) [Observed: Ohmagawdyas.png; Fan-wiki]. That they are the only green ones in BBG is [Inference].
- **Firing:**
  - The current infobox says Ammo 1, Rate of Fire 1.5 seconds, Reload 2.5 seconds, Projectile Speed 1,000 u/s and Explosives 40–60. The body text says it "has two shots without additional ammo" [Fan-wiki].
  - The BBR-era AZt_huguhzc thumbnails show the HUD at "0/1" with a RELOAD prompt and at "1/1" with the Bearzooka equipped [Observed: C2/sheets2/yt_az.jpg]. That suggests one rocket loaded plus one in reserve, two in total [Inference].
  - Planned "Incoming stats" were Ammo 3, a 1 second rate of fire, a 3 second reload and 1000 u/s [Fan-wiki].
  - Close up, the muzzle effect is [Unverified]. At a distance the Steam trailer shows the launch as a white smoke burst with an orange core (see Projectile) [Observed].
- **Projectile:**
  - The launch is at 1.92 s, from the distant green-furred Soldier himself: a white smoke burst with an orange core at his shoulder. The white puff at about 2.8 s is the rocket's trailing smoke. The camera is static and does not follow the rocket. The rocket passes under the airborne B-1000 at 2.82 s and in front of the distant pink bear at 2.89–2.95 s, then leaves the frame at 3.05 s without detonating [Observed: exact-frame trace in shared.addendum.md, round 3; its sheets re-opened in an Oct 18 edit]. (This replaces "At about 2.8–3.0 s a rocket launches with a small white puff from beside the distant green-furred Soldier and flies right, past the pink Huggable, while the camera follows it" [C2/sheets2/ro.jpg, rk30.jpg].)
  - It has a grey hex-stepped nose cone, glowing yellow-orange checker panels (#FCD22C / #F08000), grey collars and fins, a dark rear section with red squares, and a spiky orange flame exhaust [Observed].
  - The frame then washes orange (3.02–3.15 s). The wash centres on the B-1000's jet flame [Observed]; that the jet is its source is [Inference]. No rocket detonation is on screen [Observed].
  - That this is the Bearzooka's rocket is [Inference, high] (raised in the Oct 18 edit on the round-3 trace: it is fired by the green Soldier who shoulders the coral Bearzooka at 3.89 s) from where it launches and its panel pattern. The object at about 4.3 s is B-1000's arm cannon, not a rocket (source check).
- **Impact / end result:**
  - Explosive area damage (AOE) [Game text via wiki]; "The user is very prone to suicide while using the Bearzooka." [Fan-wiki]
  - The explosion look for this weapon in official media is [Unverified]; the Steam trailer does not show it [Observed]. Use the general explosion grammar above [Inference].
  - Fan footage from 2014–15 shows a faceted yellow polygon blast with a grey or dark-grey smoke ball (7WSXU2LaxYo, Mar 10, 2014; 0ZbJ0-Za5Ws, Jul 25, 2015; low-res storyboard frames) [Observed, per oliver.addendum.md; Bearzooka link Inference, high]. No 2026 frame shows the blast [Unverified for 2026].
- **Images viewed:**
  - draft: `C/png/Photo_19-04-13_12_02_26_PM.png`; `C/crops/bz_grid.png`; `C/png/Bearzooka_Concept.png`; `C/sheets/bz_sheet.jpg`; `C/tr/bz_full_4.3.png`; `C/crops/bz_trailer_grid.png`; `C/sheets/yt_AZt_huguhzc.jpg` (https://i.ytimg.com/vi/AZt_huguhzc/hqdefault.jpg, hq1, hq2, hq3); `C/sheets/oliver_skins.jpg`; `C/sheets/misc4.jpg`
  - check: `C2/sheets2/x_1.jpg` (Bear.jpg), `yt_az.jpg`, `ro.jpg`, `rk30.jpg`, `bzcmp.jpg`; `C2/crops2/rocket_z.png`; `C2/tr/rk/topright.jpg`
  - edit: `C2/png/Photo_19-04-13_12_02_26_PM.png` (sampled), `OliverSkin.png`, `Ohmagawdyas.png`; `C2/png2/Bear.png`; `C2/sheets2/ta2.jpg`, `ta3.jpg`, `yt_az.jpg`, `ro.jpg`, `rk30.jpg`, `x_1.jpg`; `C/tr/bz_full_4.3.png` (sampled only)
  - Oct 18 edit (round-3 corrections from shared.addendum.md): `W/dl/shared-r3/sheets/green_launch.jpg`, `green45_71.jpg`, `rocket_track.jpg`, `s74_85.jpg`, `s86_97.jpg`; `W/dl/oliver/gaps_r2/z/bz7W_a.jpg`, `bz0Z_38.jpg` (the 2014–15 blasts)
- **Depiction for shorts:**
  - A coral-red octagonal tube with glowing orange window chevrons, grey collars and a checkered back flare, on Oliver's shoulder [Observed].
  - The rocket is grey-nosed with glowing yellow-orange checker panels and a spiky orange flame [Observed; identification Inference, high].
  - The explosion follows the 2014–15 fan footage: a faceted yellow polygon blast with grey smoke [Observed, low-res; Bearzooka link Inference, high]. The comic recoil is [BBG News invention]; no recoil is documented.
- **Confidence:** partial (look observed; rocket probable, Inference, high; impact seen only in low-res 2014–15 fan footage, not in official media)

---

## Corrections for the character file

All paths are under `/home/user/thallo-site/bbg-news-repo/characters/`. The README cited here is `characters/README.md`, not the repo-root README.

1. **`oliver.md` line 51.**
   - *Current:* "The Bearzooka is drawn as a green, hazard-striped tube [Observed; Inference]."
   - *Correction:* "In BBR/BBG the Bearzooka is a coral-red octagonal tube (~#E05F4F in the Steam trailer (2013 footage [Inference, strong]), ~#A24D4E in an April 2013 BBR capture). It has a row of glowing orange window panels (~#F48D20–#FF931F), grey metal collars and a grey-checkered flared rear [Observed]. This matches the wiki's 'rocket launcher with red and orange lines' [Fan-wiki]. The dark green, hazard-striped Bearzooka is the BB Zombies one [Observed: wiki 'Bearzooka in BBZ']."
   - *Evidence:* Photo_19-04-13_12_02_26_PM.png (Bearzooka (BBG) infobox, uploaded 2013-04-19); Steam trailer (2013 footage) 3.9–4.8 s (`C/tr/bz_full_4.3.png`, `C2/sheets2/ta2.jpg`); Bearzooka_Concept.png; Bear.jpg (caption "Bearzooka in BBZ", `C2/png2/Bear.png`).
2. **`oliver.md` line 75 (character reference prompt), launcher.**
   - *Current:* "He holds a chunky assault rifle and carries a green hazard-striped launcher tube on his back."
   - *Correction:* "He holds a chunky assault rifle and carries a coral-red octagonal launcher tube with glowing orange window panels, grey metal collars and a grey-checkered flared end."
   - *Evidence:* same as item 1.
3. **`oliver.md` line 75 (character reference prompt), gear.**
   - *Current:* "Green-and-dark-grey shoulder harness, small green backpack, no clothing."
   - *Correction:* "Red headband, red arm bands and red ankle bands with red gem studs, a brass-bullet bandolier across the chest, a small pale grey-white backpack with red trim, no clothing."
   - *Evidence:*
     - Soldier (BBG)/Skins: "The default skin maintains the official appearence, featuring a bandana, arm and leg bands, and ammo straps, all coloured to the team. As with all characters, also a unique backpack." [Fan-wiki]
     - OliverSkin.png and Photo_19-04-13_12_02_26_PM.png [Observed].
     - The backpack is white with blue trim on a blue-team Oliver (AZt_huguhzc thumbnails) and pale grey-lilac (~#A88EA4) with blue trim on the Green Oliver skin (trailer 4.3 s) [Observed].
     - The file itself sets the default as the BBG 2013 "Oliver" skin.
4. **`oliver.md` line 50 (and the unsampled "harness green #4E6B35" in line 49).**
   - *Current:* "A green-and-dark-grey harness with grey clips [Observed] and a small green backpack [Inference]."
   - *Correction:* "In-game default skin (BBR/BBG): a brass-bullet bandolier ('ammo straps') across the chest, and a red (team-colour) headband, arm bands and ankle bands with red gem studs [Observed; Fan-wiki]. A small pale grey-white backpack with team-colour trim [Observed]. If the green harness was observed on the 2013 redesign card (File:Oliver.jpg), keep it only for card-era art and say so. Drop 'harness green #4E6B35' from the default palette."
   - *Evidence:* as item 3. File:Oliver.jpg was not opened in this check.
5. **`oliver.md` line 76 (video prompt starter).**
   - *Current:* "Oliver, a chunky low-poly brown teddy-bear soldier in a green-and-grey harness, swaggers in…"
   - *Correction:* "Oliver, a chunky low-poly brown teddy-bear soldier in a red headband and a brass-bullet bandolier, swaggers in…"
   - *Evidence:* as item 3.
6. **`oliver.md` line 57 (label).**
   - *Current:* "whose Bearzooka is "easy to kill yourself with" [Game text via wiki] ([Template](…Template:Class:Soldier_(BBG)))"
   - *Correction:* "…whose Bearzooka is 'easy to kill yourself with' [Fan-wiki template text; not marked as official game text]. The Bearzooka page adds: 'The user is very prone to suicide while using the Bearzooka.' [Fan-wiki]"
   - *Evidence:* the Template:Class:Soldier (BBG) `description` field reads "Use his starting Bearzooka carefully as it is easy to kill yourself with it!" with no "Official … description" marker. The quoted official Bearzooka description is different text.
7. **`README.md` line 57.**
   - *Current:* "No blood, gore or organs: bears throw sparks, Huggables burst into rainbow confetti, robots shed bolts."
   - *Correction:* keep the rule, but label it and add the observed baseline:
     - "In BBG footage many deaths are an intact ragdoll collapse. Some kills (a nuke blast, an irradiated target, one B-1000 close-range kill) break the body into a few clean toy-like chunks [Observed]. What decides which is unknown."
     - "SkyVu's own merch art shows a headless Huggable with white stuffing and a vertical rainbow column [Canon: official 2023 merch art, not gameplay]."
     - "BBG News dresses the chunks as sparks (bears), white fluff plus a rainbow column (Huggables) and bolts (robots) [BBG News invention, except the Huggable look above]. No source shows confetti."
   - *Evidence:* trailer 4.6–5.6 s, 9.0 s, 12.6–16.0 s, 26.6–27.8 s, 31.7–32.7 s, 40.1 s, 41.1–41.4 s; battlebears.com "Huggable Rainbow Explosion T-shirt Black" (`C2/web/rainbow_shirt_cu_view.jpg`; JSON re-fetched live to `E/web/shirt.json`).
8. **`riggs.md` line 72.**
   - *Current:* "Huggable "gore" stays rainbow confetti."
   - *Correction:* "Huggable 'gore' stays white stuffing plus a rainbow column, as on SkyVu's official 'Huggable Rainbow Explosion' merch art [Canon: merch art], or rainbow confetti [BBG News invention]. Rainbow Huggable blood is from the earlier PvE games [Fan-wiki]. In BBG footage a killed Huggable breaks into plush pieces with gold sparkles [Observed]."
   - *Evidence:* wiki Huggable and Headlights pages; trailer 9.0 s; `C2/web/rainbow_shirt_cu_view.jpg`.
9. **`riggs.md` line 17.**
   - *Current:* "calm amid rainbow confetti (canon, channel unconfirmed: "good, clean fun"; [Fan-wiki] "Thank you, may I have another?")."
   - *Correction:* "calm amid rainbow confetti [BBG News invention] (canon, channel unconfirmed: 'good, clean fun'; [Fan-wiki] 'Thank you, may I have another?')." The confetti sits inside a "canon" clause, but no source shows confetti.
   - *Evidence:* no source in the wiki, Steam, the trailer or battlebears.com shows confetti.
10. **`README.md` line 53 (optional addition).**
    - *Current:* "**Team colour:** red team by default."
    - *Correction:* append:
      - "Team colour shows on accents (the Soldier's headband, cuffs and ammo straps; the Huggable's flag; Tillman's armour panels), on the HUD and kill feed, and on Plant the Bomb gear [Observed/Fan-wiki]."
      - "Among effects, only the Energy Barrier glow (v2.3+) is team-coloured in later BBG. The cloak aura (BBR v1.4.2 only) and the Peek A Boo neon lines (v1.4.2–v2.6) were removed [Fan-wiki]."
      - "Weapon projectiles keep their own colours [Inference from Observed]."
      - "Some Huggables in the Steam trailer (2013 footage [Inference, strong]) carry a white rainbow-dot flag [Observed]."
    - *Evidence:* wiki Cloaking, Peek A Boo, Energy Barrier and Soldier (BBG)/Skins pages; trailer 3.9–4.8 s, 18–22 s; `C2/sheets2/flags.jpg`.

## Open questions
1. **Deaths in the 2026 build:**
   - Does it keep intact collapses, break-apart deaths and instant corpse removal? All appear in the Steam trailer, but that is SkyVu's May 2013 footage [Inference, strong], so it says nothing about the 2026 build.
   - No Next Fest demo is listed on today's Steam page; the only event is "Final Discord Playtest this Thursday Oct 15".
   - The JustNubz "Closed Playtest #4" showcase or the Nov 4 launch build could confirm.
2. **Gibs:** what decides whether a kill breaks the body apart or leaves it intact? And is the Green Oliver break-up at 4.9 s gameplay, or trailer staging (orange streak background leading into the B-1000 intro card)?
3. **Ink outline:** partly answered. The outline is in SkyVu's May 2013 trailer footage and in 2026 in-game captures (builds 3.0.0 and 3.0.7), but not in the 2012–14 player captures on the wiki [Observed]. Some 2013 fan videos of Graham have it too [Observed: graham.addendum.md]. Was it the 2013 "HD Graphics" mode [Inference]? Is it always on in 2026, or a graphics setting? The 2026 playtest menu thumbnail shows none on the Gear Up model.
4. **Huggable flags:** is the white rainbow-dot Huggable flag in the Steam trailer and screenshots (2013 footage) a skin flag or a change to team flags?
5. **Huggable death spray:** does a BBG Huggable spray rainbow when it dies? Official merch art says rainbow column and stuffing; BBG footage shows plush chunks. The 3.3–3.8 s rainbow fan is most likely Peek A Boo.
6. **Bearzooka:**
   - What do its explosion and muzzle flash look like in official and 2026 media? (2014–15 fan footage shows a faceted yellow blast with grey smoke; the Steam trailer shows a white launch burst with an orange core at 1.92 s.) Is the 1.92–3.05 s rocket really a Bearzooka rocket? (Inference, high, per shared.addendum.md, round 3.)
   - Is it one rocket loaded plus one in reserve (HUD "0/1" and "1/1"), or two shots, as the body text says?
7. **Tillman gibs:** do gibbed bears show the "pink and red flesh" the wiki describes for Tillman?
8. **Status visuals with no images:** how do the in-game Frozen state, the poison skull icons, the Combat Tech and Arbiter poison clouds, and the Drain Field in play look?
9. **Respawn:** is there a respawn or spawn-in effect or a death cam? How long do corpses normally stay (one trailer corpse lasted about 3 s and vanished in one frame)?
10. **"OH BABY":** what does the green "OH BABY" HUD text mean? Possibly a killstreak call.
11. **Unidentified trailer effects:**
    - the pink beams at 8.2 s and 9.1–9.8 s
    - B-1000's weapon at 4.6 s
    - the red armour chunks already airborne at 26.2 s
    - the magenta and yellow shard bursts at 30.8–32.2 s
    - the pink fuzzy head-like object at 8.2–8.4 s
    - the yellow sky streaks at about 49.6–51.5 s
    - the orange sky cone with ring shockwaves at 52.5 s
    - the purple beam at 40.4 s (Adrenaline Gun?)
12. **Two-state flicker:** is the flicker on the cyan Huggable and the shield bear a hit flash, a skin effect or something else?
13. **Bearscream Sandwich:** does it double or triple damage? The wiki pages conflict.
14. **"Bind Gun":** the Status Effects page lists "Bind Gun" as slowing, but it redirects to the Adrenaline Gun, which speeds enemies up. Which is right, and did it change?
15. **Archived SkyVu sources:** could archived SkyVu blog and patch notes (e.g. the Dead Eye post battlebears.com/blog/item/138-the-weekend-update) add [Canon] wording on deaths, gibs or team colours? Wayback was unreachable from this sandbox.
16. **Build string:** what does the build text "3.0.5_2026.11.19_B1" in the September 2026 playtest thumbnail mean? Its date-like part is later than the video.
