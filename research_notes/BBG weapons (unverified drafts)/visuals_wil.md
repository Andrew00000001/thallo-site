# Wil (Chub Scout): weapons bible

**What this covers.** Wil is BBG's **Chub Scout**. The class blurb, as the wiki quotes it from the game: "The masticator of mayhem, a Chub Scout is always prepared to even the odds for his team. His appetite for destruction is perfect for those simply wishing to wreak sweet havoc on their enemy." [Game text via wiki]. SkyVu's Steam page for the 2026 re-release lists "-CHUB SCOUT: Wil" and "80+ PRIMARY WEAPONS 60+ SECONDARY WEAPONS 50+ MELEES 10 SPECIAL EQUIPMENT" [Canon] (store API, appid 4408320, re-fetched today).

**How complete the list is.** The wiki's Category:Chub Scout (39 pages, re-listed today) has exactly 20 Chub Scout weapons: 9 primaries, 6 secondaries and 5 melees. That matches the previous inventory. Traffic Light is in the class category but missing from Category:BBG Weapons [Observed: API]. One BBH-only ability (Sarcastic Air Strike) is logged at the end.

**Era key.** BBR = Battle Bears Royale (2012). BBG = Battle Bears Gold (2013 to about 2018; fan titles from about v2.53 say "Battle Bears Royale" again). BBG 2026 = the re-release on Nov 4, 2026. BBH = Battle Bears Heroes (2023–24).

**Sources reached today**
- Fan-wiki MediaWiki API: weapon pages, Versions and 2.6 tables, Updates, the class page, skin pages.
- Steam store API.
- Official Steam trailer "Battle Bears Gold Premium - Trailer" (local mp4 frames).
- The 5 Steam screenshots. None of them clearly shows Wil [Observed].
- YouTube thumbnails (hq1, hq2, hq3, hqdefault, maxres) of:
  - SkyVu's own videos: "BATTLE BEARS GOLD Update 2.2 Weapon Recap" (BcEeAzXFChI); "Battle Bears Royale 1.3 Update Trailer" (wNpM1woYv7k); "Official Playtest Highlights" (C7uFxvSZ10c); the 2026 teaser; "Q&A with the Creator".
  - Many fan gameplay uploads, 2012–2026.
- YouTube search-result titles and description snippets.

I never watched a video. Every [Observed] tag on a YouTube source means a still thumbnail I opened. YouTube watch pages return LOGIN_REQUIRED or a 302 to google.com/sorry.

**Not reached.** web.archive.org reset every connection again today (curl tries plus WebFetch "unable to fetch"). The archive availability API now returns no snapshot for the 2.6 change-log URL. So SkyVu's BBG 2.6 change log and the archived blog stay unverified, and every patch number below comes from the wiki's tables [Fan-wiki].

**Paths.** `$W` = `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-dossier`. `$T` = `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/trailer`. Frame t_N is at (N−1)×0.5 s.
- Wiki images are PNG copies at `$W/png/<File>_<ext>.png`.
- YouTube thumbnails are at `$W/yt/thumbs/<id>_<size>.jpg` and `$W/r2/thumbs/` (URL form: https://i.ytimg.com/vi/<id>/<size>.jpg).
- Zooms and contact sheets are in `$W/frames/` and `$W/r2/`.
- Hex values are medians of image crops: approximate, and affected by lighting and JPEG compression.

**Scale.** Oliver = 1.0×; Wil ≈ 0.9× and pear-shaped [BBG News invention, house chart]. Weapon sizes below are fractions of Wil's height, measured from the wiki's 3D loadout renders [Observed, approximate].

**Wil's BBG default look, for every short.** Sources: File:Wil_default.png, Arrow.jpg, Bbooww.jpg, Bowandarrow.jpg, EZ_Chee-Z.jpg, Whipped_Pain.jpg, Pie_Bomb.png, Wils_backpack.png [Observed].
- Red padded helmet with round vent holes and a black chin strap. Sampled about #970913 to #A31116 in shadow. In-match thumbnails show a blue helmet on blue-team Wils, so the helmet is team-coloured [Observed: wNpM1woYv7k hq1, evq-fk6i8Eo hq1–3; Inference].
- White ribbed tank top (#E2E2E1) with a red ice-pop print (#D00613) that has a drip and a wooden stick.
- Black elbow pads, and black knee bands with red-glowing pads.
- A grey ABBi backpack with a big camera lens.
- Fur samples #A36B21 (shaded forehead) to #B88336 (muzzle). The lit muzzle in the 2026 trailer reads about #E09444.
- In 2026: a playtest thumbnail shows the same red padded helmet (i.ytimg.com/vi/OqSi3rfMdl8/hq1.jpg, `$W/r2/z_oq1.png`). A loadout screen reads "SKIN: CLASSIC WIL" (i.ytimg.com/vi/MS2wiArCiCA/hq2.jpg, `$W/r2/z_ms2_skin.png`; low-res, faint text) [Observed].

---

## Boomstick (primary; default; BBR v1.3 May 2012 → BBG → 2026)
- **Official text:** "Trusty Boomstick McShootington. This guy does more damage if your enemy has a higher K/D ratio and less damage if they have a lower K/D ratio." [Game text via wiki] (wiki: Boomstick). The trivia says "The boomstick used to be affected by Kill/Death ratio." No date is given [Fan-wiki].
- **Different game:** BBH's Boomstick "launches explosive pellets that burst on impact, covering a wide area." [Canon, BBH only] (battlebears.com/pages/characters, saved copy `$W/live_characters_today.html`).
- **Look:** A compact, near-black pump shotgun (#21211F–#343B35) on a Franchi SPAS-12 model [Fan-wiki trivia].
  - A boxy top rail with round lightening holes, and a ribbed pump fore-end.
  - A small **red two-digit LED readout ("00")** on the receiver side [Observed: zoom `$W/r2/z_boomgun.png`]. The previous inventory called it "a small red mark"; it is a digital counter.
  - About 0.4× Wil's height. He holds it two-handed, across the belly, muzzle down-right [Observed: File:BoomBoom.png, held in the Gift Wrapped skin].
  - BB-1 (2010) 2D cutscene version: a grey-green shotgun lit by his lighter [Observed: File:Boomstick_McShootinton.png]. That is not BBG.
- **Firing:** Hitscan; "a powerful, short ranged wave of bullets"; "the Chub Scout uses it like a pump action shotgun." [Fan-wiki]
  - Infobox: 55 damage, 1 s rate of fire, ammo 1, 1.5 s reload, +5% speed [Fan-wiki].
  - BBG 2.6 (Dec 20, 2013): damage 22→50, kill-difference bonus 7→2, fire rate .75→1 [Fan-wiki table; SkyVu's source log unreached].
  - Fan HUDs in two 2013–14 "Boom Stick" videos read 0/3–3/3 (8HtBU9imRzo, zt6DqETrDM4), but another reads 1/1 (-gRmjscGzQs) [Observed]. Either an older clip size or mislabelled Doomstick footage [Unverified].
  - The muzzle flash is not visible in any frame I opened [Unverified].
- **Projectile:** No travelling projectile in BBG (hitscan) [Fan-wiki].
- **Impact / end result:**
  - In "HERE'S MY BOOMSTICK!!!" (2.25), the target is surrounded by many small glowing yellow-orange spark dots [Observed: i.ytimg.com/vi/D_t7M6WwYPg/maxresdefault.jpg, `$W/r2/z_dt7_mid.png`]. Probably the pellet hits [Inference].
  - The same frame has a magenta zig-zag streak whose source is unclear [Unverified].
  - A 2013 upload shows orange "+"-shaped glints near an enemy [Observed: -gRmjscGzQs hqdefault/hq2]. These could be pickups rather than hits [Unverified].
  - No splash or status effect in BBG [Fan-wiki]. Do not show BBH's exploding pellets in a BBG-era short [Inference].
- **Images viewed:** `$W/frames/sheet_prim1.jpg` (File:BoomBoom.png), `$W/r2/z_boomgun.png`, `$W/frames/sheet_prim2.jpg` (File:Boomstick_McShootinton.png), `$W/frames/yt_boom.jpg` (8HtBU9imRzo, zt6DqETrDM4, D_t7M6WwYPg, -gRmjscGzQs), `$W/r2/z_dt7_mid.png`.
- **Depiction for shorts:** A pump, a short fan of yellow pellet sparks peppering the target, and a sparks-and-recoil reaction; no explosion. The muzzle puff is [BBG News invention].
- **Confidence:** partial (model observed; hit sparks seen only in thumbnails).

## Doomstick (primary; BBR 1.3/1.3.1 2012 → BBG)
- **Official text:** "We give Wil a hard time but, the truth is, he is a far braver man than I for even touching this thing... 0__0" [Game text via wiki] (wiki: Doomstick).
- **Look:** "a firey, more hellish version [of the Boomstick] with an eye in the middle" [Fan-wiki]. What the images show [Observed: File:TbwrU.png "THE DOOMSTICK" graphic; File:Wil_doomstickers.png; File:Doomstick.jpg]:
  - A black, slate-blue body (#2A232B–#383C4C) crazed with glowing lava cracks: red #BD2821 through orange #B05B22 to yellow #C8A323.
  - A row of yellow-orange flame spikes along the top.
  - A bloodshot eyeball with a yellow-orange iris set in the side.
  - Fleshy pink double barrels (#B5756E, pale ends #EDDED9) with red veins, and a flesh-pink grip.
  - About 0.45× Wil's height.
  - Seen in SkyVu banners [Observed: File:Paqueta.png, File:Chubby_bundle.jpg] and held by the Booty Duty and Fatman skins [Observed: File:Booty_duty.png, File:Fatman.PNG].
- **Firing:** Same hitscan short-range "wave of bullets" as the Boomstick, pump-style [Fan-wiki].
  - Infobox: 55 damage, 0.75 s rate of fire, ammo 2, 2.5 s reload, +5% speed. The intro claims "three times the ammo", which conflicts [Fan-wiki].
  - 2.6: fire rate 1→.25, clip 2→3, kill-difference bonus 4→2 [Fan-wiki].
  - The +7% speed buff was removed in 1.4.2 (Feb 28, 2013) [Fan-wiki]. Its code name is "KingSlayer" [Fan-wiki].
- **Projectile:** None visible (hitscan) [Fan-wiki].
- **Impact / end result:** I saw no in-game hit frame [Unverified]. Use the Boomstick's sparks [Inference].
- **Images viewed:** `$W/png/TbwrU_png.png`, `$W/frames/sheet_prim1.jpg`, `$W/frames/sheet_prim2.jpg` (Doomstick.jpg), `$W/r2/misc2.jpg` (Paqueta.png, Chubby_bundle.jpg, Fatman.PNG), `$W/r2/booty.jpg` (Booty_duty.png).
- **Depiction for shorts:** Wil holds it at arm's length. The eyeball swivels toward the target, then the gun fires the same yellow pellet sparks. The swivelling eye is a [BBG News invention] gag.
- **Confidence:** partial.

## Balance Beam (primary; level 15; BBR v1.3 May 2012 → BBG)
- **Official text:** "The worse your team is doing than the other team, the more powerful this weapon is." [Game text via wiki]
- **Look:** Like a barbell or a balance scale [Observed: File:Balance_Beam.jpg, File:Balancebeam.png]:
  - A white, silver gun body.
  - A gold rod (#C99B2E) carrying two hexagonal gold weights, with a blue tip on one end and a red tip (#D90613) on the other.
  - A white pentagonal emitter (#FDFAFE) glowing violet (#D697FE) at its centre.
  - About 0.5× Wil's height across; held level at the waist.
- **Firing:** A hitscan automatic "firing beams in quick succession"; it "fires slightly below the crosshairs" [Fan-wiki].
  - Stats: range 3000 units, 0.15 s rate of fire, 50 ammo, 4 s reload, −10% health [Fan-wiki].
  - Damage is 7.0, ±0.25 per kill (or bomb) that his team trails or leads by, minimum 1 [Fan-wiki].
  - 2.6: scaling 1→.25 [Fan-wiki].
- **Projectile / beam:** In a fan 2.22 video, a magenta-violet glow sits at the emitter (#941D73, deep violet #43294C), and a faint thin pinkish line runs forward from it [Observed, low-res: i.ytimg.com/vi/o4FJDPNxyuA/hq1.jpg, `$W/r2/z_o4f_hq1.png`]. Read it as thin magenta-violet beam pulses [Inference].
- **Impact / end result:** Not visible [Unverified].
- **Images viewed:** `$W/frames/sheet_prim1.jpg`, `$W/frames/sheet_prim2.jpg`, `$W/r2/z_o4f_hq1.png`, `$W/r2/z_o4f_hq2.png`.
- **Depiction for shorts:** Rapid thin magenta-violet beam ticks from the pentagon, with small violet sparks on hit. The sparks are a [BBG News invention]. Gag: the beam gets fatter as the scoreboard turns against his team, which reflects the [Game text via wiki].
- **Confidence:** partial.

## Señor Potato (primary; BBR 1.4.3 Apr 15, 2013 → BBG)
- **Official text:** "You couldn't find a kinder gun if you tried! Not only does it fire a high velocity spud at your enemies, it also leaves piping hot fries behind to blister their feet." [Game text via wiki]
- **Update-note text:** The wiki's Updates page transcribes the 1.4.3 notes as: "-Señor Potato Cannon: Wil shoots flaming spuds that explode on contact and leave piping hot french fries behind; Caution, fries do damage over time." [Fan-wiki transcription of SkyVu notes; Unverified as Canon]
- **Look:** A speckled tan potato (#E09A42 with red-orange spots #DA5B3F) with a red Mr.-Potato-Head nose (#C6201C) [Observed: File:Senor_Potato.jpg]:
  - A white paper coffee cup on top.
  - Silver bicycle handlebars through the middle.
  - A pink-brown cardboard-tube barrel (#C89364).
  - Held at the hip, barrel forward; about 0.5× Wil's height long.
  - Concept sheet: four grey variants A–D [Observed: File:Señor_Potato_Concept.jpg].
- **Firing:** A lobbed spud on an "extreme arc"; 1 s rate of fire, 3 ammo, 3.5 s reload [Fan-wiki].
- **Projectile:** A potato [Game text via wiki]; "flaming" per the update transcription [Fan-wiki]. I saw no in-flight frame [Unverified].
- **Impact / end result:** The spud "bursts into fries when it hits a player or surface" [Fan-wiki].
  - Impact 65 damage; explosive 35–50; AoE radii 125/250. The fries then damage over time, even to players "a large depth below" [Fan-wiki].
  - In one fan thumbnail an enemy stands in orange-yellow flame chunks with a column of grey smoke [Observed, low-res: i.ytimg.com/vi/XxEAr8mP4nE/hq3.jpg, `$W/r2/z_xxe3.png`]. Consistent with burning fries; their shape is not readable [Inference].
  - A glowing red box I first suspected was the spud is a pickup crate [Observed: `$W/r2/z_efn2.png`; excluded].
- **Images viewed:** `$W/frames/sheet_prim1.jpg`, `$W/r2/misc2.jpg` (concept), `$W/frames/yt_potato1.jpg` (EfndjtWhm-0, XxEAr8mP4nE, IbC1S6CArrI, 1PPkt0_HQZQ), `$W/r2/z_xxe3.png`, `$W/r2/z_efn2.png`, `$W/r2/z_efn_hq3.png`, `$W/r2/z_rxo_fries.png`.
- **Depiction for shorts:** A high, smoking lob. The spud splits into a starburst of glowing golden fries that stick upright in the floor like birthday candles, smoking for a beat; bears hop on hot feet. The fry visuals are a [BBG News invention].
- **Confidence:** partial.

## Pie Bomb (primary; BBG 2.2 Aug 21, 2013)
- **Official text:** "This explosive weapon will make you enjoy your last supper. It'll clean your plate. Prepare to pie...I mean...die! Okay, okay, you get the idea. It's a pie with a bomb in it." [Game text via wiki]
- **SkyVu's own video:** The on-screen caption reads "Pie Bomb" / "Wil Primary Weapon" [Canon: caption in the official thumbnail i.ytimg.com/vi/BcEeAzXFChI/hqdefault.jpg and maxresdefault]. The search snippet says: "Duc and Trang introduce all 5 new weapons found in BATTLE BEARS GOLD Update 2.2, including the fully customizable ..." [Canon, truncated].
- **Look:** A golden-crust pie (#A58663–#B9A679) in a crimped foil tin (#C5C4C3). A round black cartoon bomb sits in it with a short lit fuse that throws a white-yellow star spark [Observed: File:Pie_Bomb.png; official first-person views BcEeAzXFChI hq2/hq3 and `$W/r2/z22_pie.png`].
  - Carried flat on one palm like a waiter's plate (third person); in first person the black bomb dome is at the bottom of the screen [Observed].
  - Pie about 0.3× Wil's height wide.
- **Firing:** A fast (1,100 u/s) large projectile; direct hits advised [Fan-wiki].
  - 0.45 s rate of fire, 3.5 s reload; derived from the Rockette Launcher [Fan-wiki].
  - The HUD in SkyVu's 2.2 recap reads 2/2 [Observed]. Later fan HUDs read 4/4 [Observed: 3X0gxm8IVGY]. The infobox says 4 [Fan-wiki]. The wiki's Ammo +2 adds +2, so 4/4 may be base 2 plus equipment [Inference].
- **Projectile:** The pie-with-bomb itself [Game text via wiki]. No in-flight frame seen [Unverified].
- **Impact / end result:** A bright white-yellow-orange fireball fills a corridor ahead, with grey smoke, at 0/2 ammo [Observed: i.ytimg.com/vi/a9pZW9OJI-8/hq3.jpg, `$W/frames/z_pie_a9_hq3.png`].
  - Explosive 25–50; AoE 150/300 (2.6: 75→100 and 150→200) [Fan-wiki].
  - It formerly did more damage when the user was losing [Fan-wiki].
  - File:Imagefdv.jpg, captioned as the Pie Bomb, actually shows a MOGA controller [Observed earlier; do not use].
- **Images viewed:** `$W/frames/sheet_prim1.jpg`, `$W/frames/yt_22recap.jpg`, `$W/r2/z22_pie.png`, `$W/frames/yt_piebomb.jpg` (BdQM3oz6wrk, 2prPRhZBjGg, 3X0gxm8IVGY, a9pZW9OJI-8), `$W/frames/z_pie_a9_hq3.png`.
- **Depiction for shorts:** He flicks the pie like a frisbee, fuse sparking. It hits in a white-orange fireball and a harmless rain of crust flakes and filling dollops. The splatter is a [BBG News invention].
- **Confidence:** observed (model, held pose and blast; in-flight look unknown).

## Chainsaw Shotgun (primary; BBG 2.2 Aug 21, 2013)
- **Official text:** "Chainsaws are cool. Shotguns that shoot chainsaws are cooler. Thanks BRJ." [Game text via wiki]
- **Look:** A boxy purple-violet twin-tube launcher (#584393–#614296) with cyan light strips (#30A9C2). A grey chainsaw bar with teeth runs along it; the muzzle glows white-hot (#FEFFF2).
  - About 0.4× Wil's height; held two-handed at the chest.
  - Sources [Observed]: File:Chainsaw_Shotgun.png; SkyVu's in-game "Boom Bundle" banner (File:Boombundle.png); SkyVu's official 2.2 promo art (i.ytimg.com/vi/BcEeAzXFChI/hq1.jpg, `$W/r2/z22_art.png`), where Wil aims it with dark saw teeth along the top and bottom and a lavender-white glow in the mouth.
- **Firing:** "fires a chainsaw that sticks to all surfaces including players" [Fan-wiki].
  - 0.75 s rate of fire, 3 ammo, 4.5 s reload; derived from the TNT Launcher [Fan-wiki].
  - In-game, a bright yellow-white starburst flash bursts at the muzzle [Observed: KsddBonDY88 hq3 in `$W/frames/yt_chainsaw2.jpg`]. A soft white glow at the muzzle shows in ohJnpHcMabY hq1 (`$W/r2/z_ohj1.png`) [Observed].
- **Projectile:** A chainsaw [Fan-wiki]. No in-flight frame seen [Unverified].
- **Impact / end result:** It sticks, then detonates "a second or two after impact with a rather large AoE" [Fan-wiki].
  - Infobox delay 0.75 s; 2.6 cut it .5→.25. The delay figures conflict [Fan-wiki].
  - Explosive 35–70; AoE 100/200.
  - Known bug: the saw can hang in mid-air at the impact point [Fan-wiki].
  - A small yellow-orange blast at distance shows in a fan 2.23 thumbnail [Observed, low-res: ohJnpHcMabY hq3].
- **Images viewed:** `$W/frames/sheet_prim1.jpg`, `$W/png/Boombundle_png.png`, `$W/frames/yt_22recap.jpg`, `$W/r2/z22_art.png`, `$W/frames/yt_chainsaw1.jpg`, `$W/frames/yt_chainsaw2.jpg`, `$W/r2/z_kfj.png`, `$W/r2/z_ohj1.png`, `$W/r2/z_ksdd.png`, `$W/r2/more.jpg` (du9-TFHf6Lg fan title art).
- **Depiction for shorts:** A muzzle flash, then a spinning saw blade thunks into a wall or bear, revs and rattles for a beat (comic tension), and pops in a yellow-orange blast with bolts and sawdust. The rev beat and debris are a [BBG News invention].
- **Confidence:** partial.

## Bubble Gun (primary; BBG 2.12 Oct 2, 2014)
- **Official text:** "Bubble bubble pop, BUBBLE POP!" [Game text via wiki]
- **Look:** A green sphere tank (#38A323) with yellow piping on top, a yellow body (#E6CD0F), and a light-blue barrel (#33BEE1) ending in a yellow square-frame "wand" muzzle. About 0.5× Wil's height [Observed: File:Bubble.jpg].
- **BB Zero version (2012, not BBG):** BB Zero's (2012) Bubble Gun is a different weapon: it "does no damage and deflects projectiles" [Fan-wiki]. Its 2D art [Observed: File:Bubble_Gun.jpg]:
  - A green sphere, then an orange sphere, then a blue tube, then a yellow trumpet bell.
  - It blows a big iridescent violet-blue soap bubble.
  - Brass steampunk concept with a pink porthole [Observed: File:Bubble_Gun.png].
- **Firing:** "fire[s] a blue projectile" at 800 u/s; 0.75 s rate of fire, 4 ammo, 3.5 s reload [Fan-wiki].
- **Projectile:** A blue glob [Fan-wiki]. Not seen [Unverified]. No usable gameplay thumbnail found.
- **Impact / end result:** "a big bubble [appears] in the area where it was shot. After a second or two, this bubble will explode" [Fan-wiki]. Explosive 25–50; AoE 125/250; self-kill possible [Fan-wiki].
- **Images viewed:** `$W/frames/sheet_prim2.jpg`, `$W/r2/misc2.jpg` (BB0 2D and concept).
- **Depiction for shorts:** A blue glob splats, swells into a wobbling translucent rainbow-sheened bubble (the sheen borrowed from the BB0 art), then pops in a burst of suds and confetti. The BBG bubble look is a [BBG News invention].
- **Confidence:** partial (model only).

## Buster Cannon (primary; BBG 2.14 Nov 29, 2014)
- **Official text:** "Don't be a busta. Charge up your cannon and blow your enemies away with a powerful energy ball" [Game text via wiki]
- **Look:** A chunky arm-worn gauntlet cannon. About 0.45× Wil's height; it covers most of his torso [Observed: File:Bustercannon.jpg]:
  - Gun-metal grey body (#404547) with a mesh grille, two cone spikes and blue-grey trim (#42576A).
  - An orange concentric-ring decal on the side.
  - A glowing pale-blue cube emitter at the front (#DDE8EB).
  - BB Zero's ancestor "Blaster Cannon" is kitchen junk: a blue blender body, an orange spiral and salt shakers [Observed: File:STORY_WEAPON.png; not BBG].
- **Firing:** Semi-automatic energy orbs [Fan-wiki].
  - Uncharged: 20 damage, no AoE, 1400 u/s.
  - Full 2.5 s charge: 50–80 direct plus an AoE burst (150/300) at 1500 u/s, and it spends the whole magazine. 100 ammo [Fan-wiki]. HUDs read 100/100 and 0/100 [Observed].
  - Charge cue per the wiki: "a pulsating purple energy ring formed around the glove" [Fan-wiki]. In-game it reads as **swirling pink-magenta to violet rings (#C53BB2, #EE5AF6) with white cores** wrapped around the gauntlet, plus a pink fringe glow on the arm [Observed: i.ytimg.com/vi/evq-fk6i8Eo/hq1.jpg and hq3.jpg, `$W/frames/re_buster.jpg`].
- **Projectile:** The orb's exact colour is not isolated in any frame. Pink-violet energy at the hand and a pink burst on a hit target are visible [Observed: icEIszkRrsA hq3; 86mjqmdx708 hq1–2 shows magenta electric crackle at the floor].
- **Impact / end result:** At full charge, an AoE burst around the orb [Fan-wiki]. A pink-magenta flash shows on the enemy [Observed, low-res].
- **Images viewed:** `$W/frames/sheet_prim2.jpg`, `$W/r2/misc2.jpg` (STORY_WEAPON), `$W/frames/yt_buster1.jpg`, `$W/frames/re_buster.jpg`, `$W/frames/yt_buster2.jpg`.
- **Depiction for shorts:** Rings of pink-violet energy spin up around the glove (with a rising whine) and fire a pink-white plasma ball that bursts in a magenta shock-ring. The ball's look is [Inference from the observed charge colour].
- **Confidence:** partial.

## Snowtato Launcher (primary; BBG 2.26 Jan 17, 2017)
- **Official text:** "A makeshift potato launcher convertor to weapon of frosty devastation. Shoot snowballs that explode and turn them into flakes!" [Game text via wiki]
- **Look:** The Señor Potato build in ice tones. About 0.45× Wil's height [Observed: File:Snowtato.jpeg]:
  - A lavender-blue frozen potato body (#95A3CD).
  - An ice-blue cup on top (#C1DBE2).
  - Flat grey handlebars and a fat grey metal barrel (#6C6D70).
  - At launch it had no menu model [Fan-wiki].
- **Firing:** Exploding snowballs; cooldown 2.2, 6 ammo, 4.5 s reload [Fan-wiki]. One fan HUD reads 5/5 [Observed: _7wmOHdRMs4 hq1]. Minor conflict.
- **Projectile:** A snowball [Game text via wiki]. Not seen in flight [Unverified].
- **Impact / end result:** "snow will remain present in the air in the Snowtato's area of effect for several seconds and block any explosives" [Fan-wiki]. Explosive 35–65; AoE 150/300 [Fan-wiki].
  - In a fan Snowtato video (title "BattleBearsRoyale 2.53.2 … Snowtato Launcher Gameplay"), a dense cluster of **violet-indigo puffs** (#4B217B, #3D3A70) hangs across the corridor in front of the player [Observed: i.ytimg.com/vi/_7wmOHdRMs4/hq1.jpg, `$W/frames/z_snow_hq1.png`]. Probably the lingering snow cloud [Inference]. Why it is purple and not white (team tint or lighting) is [Unverified].
  - Fan title art in that video's thumbnail shows a white snowball with snowflakes [Observed; fan art, not game].
- **Images viewed:** `$W/frames/sheet_prim2.jpg`, `$W/frames/yt_snow_kd.jpg`, `$W/frames/z_snow_hq1.png`, `$W/frames/z_snow_hq2.png`, `$W/frames/z_snow_icon.png`.
- **Depiction for shorts:** A thunk, then a snowball bursts into a hanging cloud of chunky flakes that lingers. A second shot "clinks" off the cloud, per the wiki's blocking note. Hold flake colour white-lavender until gameplay is checked; that is a [BBG News invention].
- **Confidence:** partial.

## Batterito (secondary; default; BBR v1.3 May 2012 → BBG → 2026 trailer)
- **Official text:** "Set you mouth and you opponent's faces ablaze with fiery power of the batterito. Once consumed, fire will spew from your mouth and movement speed is increased until the inferno dies down." [Game text via wiki]
- **Look:** A bullet-shaped wrapped burrito about 0.3× Wil's height, hugged against the belly [Observed: Steam trailer frame at 17.8 s, `$W/frames/crop_batterito.png`; File:Wil.png]:
  - A dark grey wrapper (#524A4E).
  - A label band fading green, to yellow, to orange (#83C32A to #FBE324 to #A97226) with "BATTERITO" lettering.
  - A rounded yellow end cap.
  - BLAST 2D version (not BBG): a black wrapper with orange and yellow stripes, "BATTERITO", and "NUT FACT PEANUTS ARE NOT NUTS" [Observed: File:Batterup.jpg].
- **Firing (activation):** He eats it. Damage starts "a second or two" later. Primary, melee and Specials are locked until it ends [Fan-wiki]. 70 DPS, +200 u/s speed [Fan-wiki]. Duration is 8 s in the infobox but 6 s and 7 s in the text [Fan-wiki conflict].
- **Official 2026 trailer** ("Battle Bears Gold Premium - Trailer", 54 s) [Observed: `$T/t_0037.jpg`–`t_0048.jpg`]:
  - **18.0–19.0 s:** Wil (Booty Duty skin) hugs the Batterito. His eyes stream blue tears, his teeth clench, then his mouth gapes.
  - **19.5–20.0 s:** Arms up, head back. An orange-yellow glow (#FF9934 / #FFEB4A) floods the frame.
  - **20.5–21.0 s:** He runs off, seen from behind. Orange flame plumes billow past.
  - **22.0 s:** The panda-skinned bear he charges at is lit pure white (#FFFFFF with an orange rim, #F59E65). Orange smoke clouds (#D86829, dark red-brown #66231D) roll overhead.
  - **22.5–23.5 s:** The "Wil / CHUB SCOUT" title card shows a thick flame jet from his crying, open mouth. Yellow core #FDDB44, orange #E2973D, red edge #CC4F35.
- **Projectile:** No projectile; a short continuous flame cone or jet from the mouth [Game text via wiki; Observed].
  - Fan thumbnails show the same big orange-yellow fire cloud right in front of Wil's face. BBR 1.3.1: rzGuh5Qga1Y hq1. BBG 2.27: -VwccFy5cuc hqdefault [Observed: `$W/frames/yt_batt.jpg`].
  - A 2026 playtest thumbnail shows default-helmet Wil with a tear-filled eye [Observed: OqSi3rfMdl8 hq1]. That suggests the same crying "too hot" acting in 2026 [Inference].
- **Impact / end result:** The target is engulfed and glows white-hot. There is no knockback cue [Observed: trailer 22.0 s].
  - With the Not-So-Slenderman skin, eyes and a mouth appear when he breathes fire [Fan-wiki].
  - 2.6: damage 30→35, duration 10→6.5, reload 12→5 [Fan-wiki].
- **Images viewed:** `$W/r2/tsheet.jpg` (`$T/t_0036`–`t_0051`), `$W/r2/t45_47.jpg`, `$W/frames/crop_batterito.png`, `$W/frames/sheet_sec1.jpg` (Wil.png, Batterito_(BBR).jpg, Batterup.jpg), `$W/frames/yt_batt.jpg`, `$W/r2/z_oq1.png`, `$W/r2/booty.jpg`.
- **Depiction for shorts:** Copy the trailer beat for beat: chomp, tears, red cheeks, a gaping mouth, then a yellow-core, orange-edged flame jet with rolling orange smoke. Wil sprints while breathing fire, and the target flashes white and fades to a sooty, blinking bear (no burns).
- **Confidence:** observed.

## Killdoba (secondary; BBR v1.3.1 2012 → BBG)
- **Official text:** "\"Muy caliente\" is what you might say if you weren't so busy spewing fire and running faster than a burning, headless chicken. This mega-bean packs a punch but burns coming out twice, if you know what I mean." [Game text via wiki]
- **Look:** A large burrito in crinkled silver foil (#E5E5E4 / #A3A3A3) with a tan tortilla end, hugged to the chest. About 0.3× Wil's height [Observed: File:Killdoba.jpg].
  - SkyVu banners show a white-wrapped burrito with red-brown chili filling bulging out [Observed: File:Paqueta.png; File:HungryScoutBundle.png, where Wil in a scout uniform holds two].
  - The BBR menu shows "HEALTH -5%" [Observed: File:Killdoba.png].
  - The infobox says "Primary"; the category is Secondary [Fan-wiki error].
- **Firing (activation):** A Batterito reskin: eat it, breathe fire, +200 u/s speed. 70 DPS, 4 s duration, 3 s reload [Fan-wiki]. 2.6: damage 37→45, reload 13→7, health −5%→0 [Fan-wiki].
- **Projectile:** Mouth fire [Game text via wiki]. Not seen for this item. File:180px-Ci0oml.jpg shows a fire burst in a corridor, but nothing ties it to the Killdoba [Unverified]. A fan "Killdoba fire lasting forever" glitch video's thumbnails show no fire [Observed: LOa3e4GyrCk].
- **Impact / end result:** As for the Batterito [Inference].
- **Images viewed:** `$W/frames/sheet_sec1.jpg`, `$W/r2/misc2.jpg`, `$W/r2/melee_etc.jpg`, `$W/r2/more.jpg`.
- **Depiction for shorts:** Same flame breath as the Batterito, bigger and redder, with a comic after-burp puff. The colour shift is a [BBG News invention]. Skip the official text's toilet joke for 13+ tone.
- **Confidence:** partial.

## EZ Chee-Z (secondary; level 15; BBR v1.3 May 2012 → BBG)
- **Official text:** "Chugging this can of cheese will cause you to swell up and explode, killing yourself and anyone unlucky enough to be caught in the blast." [Game text via wiki]
- **Look:** A spray-cheese aerosol can about 0.3× Wil's height, held up in one hand [Observed: File:EZ_Chee-Z.jpg, File:E-Z_Chee-Z.png]:
  - A white and royal-blue body (#0376C1).
  - Orange label marks.
  - An orange-yellow nozzle cap (#FDC020).
- **Firing (activation):** He shakes the can, eats the contents and bloats "to the point where the player will not be able to enter certain roofed areas". For 2 s he moves at −50 u/s, then explodes [Fan-wiki]. Explosive 150–225; AoE 150/400. Shields do not stop the self-kill [Fan-wiki].
- **What I saw:** A fan BBR clip shows Wil from behind holding a can, with a hugely swollen body [Observed: iSgdJ1qHmMA hq2, `$W/frames/z_cz_isg_hq2.png`; greyscale fan video].
  - "KAMICHEEZE WIL!!!" (2.24): Wil's back and shoulders fill most of the frame [Observed: `$W/frames/z_cz_7fq.png`].
  - **Correction to the previous inventory:** SkyVu's BBR 1.3 "SECONDARY EDIBILITIES" thumbnail shows two clips of Wil from behind; the right one is a blue team helmet. Nothing in them proves bloating [Observed: `$W/r2/z_wnpm_hq2.png`]. Downgrade that claim to [Unverified].
- **Projectile:** None; he is the bomb [Fan-wiki].
- **Impact / end result:** A big self-centred blast that kills him and anyone in range. The explosion's look was not seen [Unverified].
- **Images viewed:** `$W/frames/sheet_sec2.jpg`, `$W/frames/yt_cheez.jpg`, `$W/frames/z_cz_7fq.png`, `$W/frames/z_cz_isg_hq2.png`, `$W/r2/bbr13.jpg`, `$W/r2/z_wnpm_hq2.png`.
- **Depiction for shorts:** Shake, a can-to-mouth glug, then Wil inflates into a beach ball and waddles slowly, then BOOM: an orange-yellow cheese-cloud blast that leaves a cheese-dusted crater. Wil respawns sheepish. Show it as cartoon, not gore; the blast look is a [BBG News invention].
- **Confidence:** partial.

## Whipped Pain (secondary; BBR v1.3.1 2012 → BBG)
- **Official text:** "This hillarious party stunt is about to go all over the faces of your enemies. It may take a bit longer than the E-Z Chee-Z but the pay off packs a larger punch." [Game text via wiki]
- **Look:** A red (#EF0F10) and white whipped-cream aerosol can with a red cap, about 0.3× Wil's height [Observed: File:Whipped_Pain.jpg].
  - In-match, Wil holds the can up with a white glove-like hand. In two 2012 BBR clips he wears a black suit (Dia De Los Muertos skin) with a hugely swollen head and body [Observed: oA22vOD9KBI and gMz53R_72UI thumbnails; File:Images(2).jpg captioned "Wil bloating up after using the Whipped Pain."].
- **Firing (activation):** As the EZ Chee-Z, but he explodes after 5 s, with a wider blast. Explosive 225–400; AoE 250/600; −10% health [Fan-wiki].
- **Impact / end result:**
  - In a 2024 fan short titled for Whipped Pain, **large flat white splats cover the screen** [Observed: i.ytimg.com/vi/3Z65fUow2UQ/hq1.jpg, `$W/r2/z_3z_hq1.png`]. Reads as cream on the camera [Inference].
  - Its hq3 shows Wil bloated in the Gift Wrapped skin [Observed].
  - A 2.30 fan video shows white puff clouds bursting near a distant enemy [Observed, low-res: o8rEXLT4n_0 hq3, `$W/r2/z_o8_hq3.png`].
- **Images viewed:** `$W/frames/sheet_sec2.jpg`, `$W/frames/yt_cheez.jpg`, `$W/r2/z_3z_hq1.png`, `$W/r2/z_o8_hq3.png`, `$W/r2/misc2.jpg` (Purple Pain banner, no weapon shown).
- **Depiction for shorts:** A long, tense 5-second swell (ticking), then a huge white whipped-cream blast that plasters every nearby bear's face, with a cherry landing on top as the button. The cream-splat look is backed by the observed white splats and the "all over the faces" text; the cherry is a [BBG News invention].
- **Confidence:** partial.

## Sole's Bane (secondary; BBR 1.4.3 Apr 15, 2013 → BBG)
- **Official text:** "Wil doesn't want to share his toys but he's more than happy to share the pain of stepping on one of the buggers." [Game text via wiki]
- **Update-note text:** "-Sole's Bane: Wil leaves a trail of pain with colorful mines that sure to give any opponent a sore foot." [Fan-wiki transcription of SkyVu 1.4.3 notes; Unverified as Canon]
- **Look:** An armful heap of interlocking toy bricks: red #C32019, green #75B530, yellow, blue #288AC3, orange, white and black. About 0.35× Wil's height wide, held at the belly [Observed: File:SolesBane.jpeg].
  - It is held the same way mid-match in a 2.23 fan video (light-blue skin, brick heap in his arms) [Observed: i.ytimg.com/vi/RukIckwnibs/hq2.jpg, `$W/r2/z_ruk_hq2.png`].
  - The HUD weapon icon is an orange 2×4 brick [Observed: RukIckwnibs hq1–3].
- **Firing (activation):** "a pile of Lego bricks that Wil throws in the air when activated … The throwing effect keeps going on even if the player dies" [Fan-wiki].
  - 50 damage, 4.5 s duration, 3 ammo, 2 s rate of fire, 3 s reload, +5% speed [Fan-wiki].
  - The "throws" (wiki) and "trail of mines" (update text) accounts differ. The duration stat fits bricks lying on the floor as timed caltrops [Inference].
- **Projectile / impact:** The scatter and the triggering were not seen [Unverified]. Small AoE, high damage [Fan-wiki].
- **Images viewed:** `$W/frames/sheet_sec2.jpg`, `$W/r2/sb_v6.jpg` (V6FLnB_c_fk; its hq3 shows a pink-violet lightning burst from another weapon), `$W/r2/more.jpg`, `$W/r2/z_ruk_hq2.png`.
- **Depiction for shorts:** Wil tosses the heap overhead and bricks rain into a colourful carpet behind him. A chasing bear steps on one, hops clutching its foot, and a small pop of sparks follows. The pop and hop are a [BBG News invention].
- **Confidence:** partial.

## Pop Tart Shuriken (secondary; BBG 2.25 Mar 21, 2016)
- **Official text:** "Breakfast just got deadly." [Game text via wiki]
- **Look:** A six-pointed star-shaped toaster pastry, about 0.2× Wil's height across, held up in one hand [Observed: File:218426BB-3EEC-43E7-B36F-4EA0806BD23A_1.png]:
  - A tan crust rim (#9E7036–#DBB032).
  - Pink and white frosting (#EF7AAA, #F9F0ED).
  - Green, pink and yellow sprinkles (#4EB840).
  - A hole in the centre.
- **Firing:** Each press flings two shurikens in a straight, gravity-free line at 1,600 u/s. 3 ammo (6 shurikens), 0.5 s rate of fire, 3 s reload [Fan-wiki].
  - It originally had a "shining" sound per throw; this was changed to one sound per press [Fan-wiki].
- **Projectile:** **A rainbow-stripe trail** (red, orange, yellow, green, blue, violet bands) with white star sparkles behind each pastry, like Nyan Cat [Observed: i.ytimg.com/vi/uAtfV_9vEYc/hq1.jpg, `$W/frames/z_pt_uatf_hq1.png`; q8a8noCNVcg hqdefault, `$W/frames/z_pt_q8.png`]. The wiki's Nyan Cat note [Fan-wiki] is now confirmed visually.
- **Impact / end result:** A small explosion (explosive 10–30; AoE 50/150). It cannot hurt the user or blow up bodies [Fan-wiki].
  - In a 2.25 fan thumbnail, pink-red puff chunks scatter around the hit target [Observed: v9yFp06dn00 hqdefault, `$W/frames/z_pt_v9.png`]. Probably the hit and explosion puffs [Inference].
- **Images viewed:** `$W/frames/sheet_sec2.jpg`, `$W/frames/yt_poptart1.jpg`, `$W/frames/z_pt_uatf_hq1.png`, `$W/frames/z_pt_q8.png`, `$W/frames/z_pt_v9.png`.
- **Depiction for shorts:** A ninja double-throw. Two frosted stars streak in on rainbow trails with sparkle stars, then pop into pink frosting puffs and sprinkles on contact. The sprinkle confetti is a [BBG News invention]; the trail is observed.
- **Confidence:** observed.

## Bow (melee; default; BBR v1.3 May 2012 → BBG)
- **Official text:** "Last time Wil got Bow and Arrow together certain words were exchanged and hearts were broken. They haven't spoken in weeks. Wil doesn't want to talk about it." [Game text via wiki]
- **Look:** A plain wooden longbow (about #875B23) with a taut pale string and a cream striped grip wrap. About 0.8–0.9× Wil's height, held upright at his side [Observed: File:Bbooww.jpg].
- **Firing:** None; a melee swing with the bow (there is no arrow) [Inference from the official text]. 70 damage. Same range as the Arrow despite its length [Fan-wiki]. 2.6 changed the Melee+ equipment values only [Fan-wiki].
- **Projectile:** None.
- **Impact / end result:** Undocumented [Unverified].
- **Images viewed:** `$W/r2/melee_etc.jpg` (Bbooww.jpg), `$W/r2/misc2.jpg` (Chubby bundle shows a bow icon).
- **Depiction for shorts:** He swings it like a club. "THWANG": the string twangs on the hit and the target sees stars. [BBG News invention]
- **Confidence:** partial.

## Arrow (melee; BBR v1.3 May 2012 → BBG; wiki page "Arrow (BBG)")
- **Official text:** "Trusty old arrow. What say we get it stuck in someone else's leg this time?" [Game text via wiki]
- **Look:** A single wooden-shaft arrow about 0.6× Wil's height, gripped near the fletching and held upright like a short spear [Observed: File:Arrow.jpg]:
  - A pointed silver-grey head.
  - Pale white to blue fletching.
- **Origin:** BB-1 (2010): the arrow a Huggable shot into his leg [Fan-wiki; earlier notes cite 2010 press].
- **Firing:** None; a hand-held stab or jab [Inference]. Now 45 damage, +15% health. 2.6 raised damage 45→55 and added +10% health, so a later nerf is implied [Fan-wiki].
- **Impact / end result:** Undocumented [Unverified].
- **Images viewed:** `$W/r2/melee_etc.jpg` (Arrow.jpg).
- **Depiction for shorts:** A comic poke to the backside, a yelp, and sparks. Keep it a poke, never a wound. [BBG News invention]
- **Confidence:** partial.

## Bow and Arrow (melee; BBG 2.13 Oct 31, 2014 or 2.16 Jan 30, 2015)
- **Official text:** "Wil's bow and arrow has made up and joined forces to fight against evil! Too bad Wil doesn't know how to use it still. Maybe next time.." [Game text via wiki]
- **Look:** The wooden bow with the arrow (grey head, white fletching) held along it in one hand. The bow is about 0.8× Wil's height [Observed: File:Bowandarrow.jpg].
- **Firing:** None; per the official joke he cannot shoot it, so it is a club [Inference]. 45 damage, −10% speed, +20% health. It was 65 damage, −10% speed, +15% health when the page was created [Fan-wiki].
- **Release conflict:** The wiki's Versions table lists it under both 2.13 and 2.16 [Fan-wiki conflict].
- **Impact / end result:** Undocumented [Unverified].
- **Images viewed:** `$W/r2/melee_etc.jpg`.
- **Depiction for shorts:** He nocks the arrow, aims, then whacks the bear with the whole bundle. [BBG News invention]
- **Confidence:** partial.

## Traffic Light (melee; no release version listed; page created Nov 1, 2014)
- **Official text:** "Why is there no yellow light you ask? Wil only travels in two modes. He stops and sometimes he has to go." [Game text via wiki]
- **Look:** A yellow pole (#F1C810) with black bands at the grip, topped by a dark grey signal head with a **red lamp above a green lamp and no amber**. About 0.8× Wil's height, shouldered like a mace [Observed: File:Trafficlight.png].
  - **Correction:** Wil in that icon wears the **Fatman** skin, the Batman-parody one: a red cowl with ears, a grey suit, a gold bear chest emblem and a yellow-black belt. It matches File:Fatman.PNG [Observed]. The previous inventory called it an unidentified "red-masked superhero-style skin". The wiki says Fatman "is a reference to Batman" [Fan-wiki].
- **Firing:** None; a melee club [Inference]. 45 damage, +10% speed; it was 12% speed and 200,000 Joules at page creation [Fan-wiki].
- **Impact / end result:** Undocumented [Unverified].
- **Images viewed:** `$W/r2/melee_etc.jpg`, `$W/r2/misc2.jpg` (Fatman.PNG).
- **Depiction for shorts:** The lamp flips red ("STOP") as he bonks someone, then green ("GO") as he waddles off. [BBG News invention, from the official joke]
- **Confidence:** partial.

## Selfie Stick (melee; BBG 2.21 Jul 3, 2015)
- **Official text:** "But first, let me hit you with this!" [Game text via wiki]
- **Look:** A yellow pole (#CFA10E) with a black-and-yellow banded grip, topped by a **smiling yellow bear-face head**, perhaps a phone in a bear case [Inference]. About 0.7× Wil's height [Observed: File:Image7.PNG, low-res].
  - Wil wears the **Lunchador** skin: a red luchador mask with gold trim, red trunks and a bare furry chest [Observed; matches the wiki's Lunchador skin name].
- **Firing:** None; a melee club [Inference]. 45 damage, −20% health, +20% speed [Fan-wiki].
- **Impact / end result:** Undocumented [Unverified].
- **Images viewed:** `$W/r2/melee_etc.jpg`.
- **Depiction for shorts:** A selfie flash pops in the target's face, then the bonk. [BBG News invention]
- **Confidence:** partial.

## Sarcastic Air Strike (BBH ultimate only; not in BBG)
- **Official text:** "His Ultimate, \"Sarcastic Air Strike,\" features A.B.B.I., his mocking robot backpack, executing a devastating airstrike, raining destruction across the battlefield." [Canon] (battlebears.com/pages/characters, re-read from `$W/live_characters_today.html`).
- **Status:** BBH reworked Wil's attack and ultimate on June 20, 2023 [Fan-wiki: Updates]. There is no BBG or BBG 2026 equivalent [Unverified].
- **Look, firing, impact:** No visual opened [Unverified]. ABBi in BBG is a grey shell with a large camera lens [Observed: File:Wils_backpack.png].
- **Depiction for shorts:** Only in BBH-labelled content: ABBi's lens flashes, she sighs a sarcastic line, and a cartoon bombing run pounds the area. [BBG News invention]
- **Confidence:** documented (text only).

---

## Corrections to the previous inventory
1. **Boomstick "small red mark":** it is a red two-digit LED readout ("00") on the receiver [Observed: `$W/r2/z_boomgun.png`].
2. **EZ Chee-Z in the BBR 1.3 trailer:** the "SECONDARY EDIBILITIES" clips do not clearly show bloating; the blue dome is the blue team helmet. Mark it [Unverified].
3. **The skin in the 2026 trailer is Booty Duty, red-team version** [Observed match: trailer `$T/t_0037`–`t_0043` vs File:Booty_duty.png and File:Booty.png concept]: a red headband, a pink-white tank, red shorts, striped wristbands, and a black backpack covered in snacks (cookie, candy, lollipop). The wiki describes "exercise clothes … cookies, chips, candy bars, and lollipop on his team-coloured and black backpack" [Fan-wiki].
4. **Traffic Light icon skin = Fatman** [Observed].
5. **Pie Bomb:** SkyVu's own 2.2 video captions it "Wil Primary Weapon", and its HUD shows a 2-round clip [Observed; Canon caption].
6. **Visuals that were "undocumented" and are now observed:**
   - Pop Tart rainbow trail.
   - Buster Cannon pink-violet charge rings.
   - Balance Beam magenta-violet emitter glow (low-res).
   - Chainsaw Shotgun official promo art and muzzle flash.
   - Pie Bomb fireball.
   - Whipped Pain white splats.
   - A violet puff cloud in a Snowtato video (tentative).
7. **Sole's Bane:** RukIckwnibs hq2 shows the bricks held, not scattered.
8. **Killdoba:** the "fire lasting forever" glitch video's thumbnails show no Killdoba fire.

## Corrections for the character file (`/home/user/thallo-site/bbg-news-repo/characters/wil.md`)
1. **Look, line 49.** Current: "Exception: no researcher has described his BBG 2013 in-game default, so until it is checked the model uses the closest observed proxies." … "outfit from the March 2012 BBR animation-test frame, "a brown bear in a red cap, white shirt and a grey backpack" [Observed, low-res]". Replace with the observed BBG default:
   - A red padded helmet with vent holes and a black chin strap, team-coloured (blue on blue team).
   - A white ribbed tank top with a red ice-pop print.
   - Black elbow pads, and black knee bands with red-glowing pads.
   - A grey ABBi camera backpack.
   - Evidence: File:Wil_default.png, Arrow.jpg, Bbooww.jpg, Bowandarrow.jpg, EZ_Chee-Z.jpg [Observed].
   - In the 2026 playtest the default still has the red padded helmet (OqSi3rfMdl8 hq1), and the loadout names it "CLASSIC WIL" (MS2wiArCiCA hq2) [Observed, low-res].
2. **Line 49.** Current: "The research never describes his BBG trailer card ([Steam][steam]) or the 2026 playtest showcase". Replace with: the Steam trailer card ("Wil / CHUB SCOUT", 22.5–23.5 s) shows him in the **Booty Duty** skin breathing a Batterito flame jet [Observed]. The JustNubz showcase is still unwatched.
3. **Colours, line 51.** Current: "Unsampled picks [BBG News invention]: cap #C8352E, shirt #F2EFE6, ABBi grey #8B9299, eyes #141414, ice pop #3FA7E0." Replace with sampled values:
   - Helmet about #A31116 (shadow #970913).
   - Shirt #E2E2E1.
   - Ice-pop print red #D00613. It is a shirt graphic, not a blue prop.
4. **Colours, line 51.** Current: "fur #D8AC57, mid #B88A46, shadow #754F26, light #DFCA95" (from the BBH portrait). Add the BBG samples: menu-render fur #A36B21 (shaded) to #B88336 (muzzle); 2026 trailer lit muzzle about #E09444. The BBG model is a deeper orange-brown than the BBH portrait.
5. **Weapons & props, line 54.** Current: "Senor Potato, Pie Bomb, Traffic Light [Fan-wiki]; blue ice pop [Observed]." Replace with:
   - The full BBG kit: 9 primaries, 6 secondaries, 5 melees, listed above.
   - Default loadout Boomstick, Batterito, Bow.
   - Pie Bomb is captioned "Wil Primary Weapon" in SkyVu's 2.2 video [Canon].
   - The "blue ice pop" should go. The BBG ice pop is a red print on his shirt [Observed].
   - Note that BBH's Boomstick fires "explosive pellets that burst on impact" [Canon, BBH], while BBG's is a hitscan shotgun with no splash [Fan-wiki].
6. **Fighting, line 61.** Current: "ABBi's "Sarcastic Air Strike" [Canon]". Mark it BBH only. BBG Wil's signature moves are edible secondaries: Batterito fire breath (official 2026 trailer [Observed]) and the EZ Chee-Z / Whipped Pain self-inflate-and-explode [Game text via wiki].
7. **Prompt pack, line 76.** Current: "red cap, white shirt; compact grey robot backpack with one camera-eye lens; chunky cartoon shotgun; alternate pose with a dripping blue ice pop;". Replace with: "red padded sports helmet with chin strap, white ribbed tank top with a red ice-pop print; compact grey robot backpack with one camera-eye lens; dark grey pump shotgun with a red digital readout; alternate pose hugging a grey-wrapped neon-striped burrito".
8. **Video prompt, line 77.** Current: "A round golden-tan teddy-bear soldier in a red cap". Change to "in a red padded helmet". An optional fire-breathing beat can follow the trailer.
9. **Canon vs invention ledger, line 84.** Current: "the red-cap look as default [Observed + Inference]". Change to "red padded helmet default [Observed: BBG renders]".
10. **Open questions, line 88.** Current: "what his BBG card and 2026 default skin show (red cap? ABBi?)". Partly answered: the 2026 default keeps the red padded helmet ("CLASSIC WIL"). The trailer uses Booty Duty, whose backpack is black and covered in snacks rather than ABBi [Observed; Fan-wiki says only the default and Gift Wrapped skins carry ABBi].
11. **Signature skins, line 55** (optional). Add Booty Duty (2026 trailer), Fatman (Traffic Light icon) and Dia De Los Muertos (EZ Chee-Z and Killdoba menu shots) as observed.

## Open questions
- What the Bubble Gun's blue glob and bubble, and the chainsaw in flight, look like in BBG. No gameplay frame was found.
- The Buster Cannon orb colour (pink-violet like the charge ring?), and the exact Balance Beam beam colour at full resolution.
- Whether the Snowtato's lingering cloud is really violet, or white tinted by lighting or team.
- The Señor Potato fries' shape and colour on the ground, and whether the spud visibly burns in flight ("flaming spuds" comes from the wiki transcription only).
- Sole's Bane: thrown-and-scattered, or a trail of floor mines? Neither has been seen.
- The EZ Chee-Z and Whipped Pain explosion looks, and the bloat silhouette in BBG (only BBR and fan footage seen).
- Boomstick clip size (3 in two 2013–14 fan HUDs vs 1 in the infobox), and when the K/D scaling was removed.
- Which 2.x patch added Bow and Arrow (2.13 or 2.16), and when Traffic Light was released.
- Whether any Chub Scout weapon changed, was renamed or was removed for the 2026 re-release. Check the JustNubz showcase from the 28:11 Chub Scout chapter, and SkyVu's patch notes at launch.
- SkyVu's original BBG 2.6 change log (battlebears.com/battle-bears-gold-2-6-change-log/) is still unreached; web.archive.org resets connections.
