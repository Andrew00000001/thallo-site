<!-- gap pass 1 -->
# Saberi: BBH weapons addendum (Huggable Splicer, Healing Turret, BBH model recheck)

This addendum covers only Saberi's two Battle Bears Heroes (BBH) abilities and a recheck of her BBH look. In BBH she is the "Medic" [Canon] (battlebears.com/pages/characters). The game soft-launched in 2023 and launched globally on Aug 20, 2024 [Canon, prior notes]. The wiki says Saberi was added in "Summer 2023" [Fan-wiki]. A fan upload dated Sept 26, 2026 shows BBH still running. Neither ability belongs to BBG: the Steam page for the Nov 4, 2026 BBG release (re-fetched today) still lists her as "-COMBAT TECH: Saberi" [Canon] (store.steampowered.com/api/appdetails?appids=4408320).

**Sources I reached today**
- battlebears.com/pages/characters, fetched live [Canon].
- The wiki's "Battle Bears Heroes" page through the MediaWiki API (revid 77677), with its BBH image files [Fan-wiki].
- YouTube titles and descriptions for both target uploads, through oEmbed and the youtubei "next" endpoint.
- All thumbnail variants for both target uploads.
- **YouTube storyboard sprites.** These are the low-resolution preview tiles YouTube shows when you scrub. I found their URLs through the Invidious API and downloaded them from i.ytimg.com:
  - CuptyqnRweM: 390×180, one tile every 10 s.
  - 8C7JH7STmyo: 320×180, one tile every 1 s.
  - The same for four official SkyVu BBH uploads and one fan "All Heroes List" upload.

I did not watch any video. Every "t=" below is a tile's index multiplied by the storyboard interval, so it is accurate only to within one interval.

**The two target uploads**
- "Battle Bears Heroes: Matches with Saberi" by Princess and Nebula. Uploaded May 1, 2025, 987 s long. Description: "More Battle Bears Gameplays…".
- "All Battle Bears Heroes Characters Animation" by S8 KBW_Overwatch. Uploaded Oct 3, 2024, 60 s long. Description: "…For now enjoy these new animations they made. Also congrats to @battlebears for releasing the game."

---

## Huggable Splicer (BBH main Attack; BB Heroes only, 2023/2024 to present; not in BBG)

- **Official text:** "Saberi's "Huggable Splicer" attack unleashes a wide spray of huggable bits in a sweeping motion, ideal for hitting multiple enemies despite its inaccuracy. She's less effective in singular, long-range confrontations." [Canon] (battlebears.com/pages/characters, fetched 2026-10-18).
- **Wiki stats** [Fan-wiki] (Battle Bears Heroes page, character table):
  - Damage "15 x 190"; Range "Normal"; Reload Speed "Very slow".
  - Cost "600 Shards"; release "Summer 2023".
  - Hero bio: "A weapon expert who doesn't take anything from anybody! Saberi is a momma bear who knows how to lay down the law. A specialist in support, teammates love having her in the squad." The wiki does not give a source for this text, so treat it as [Fan-wiki], not game text.

**Look**
- **Shape.** A squat round drum like a big revolver cylinder, with the cylinder's face pointing forward [Observed] (thumbs/8C7JH7STmyo_maxres2.jpg; crops/default_splicer_x2.png).
  - The face is a grey disc with an engraved geometric pattern (#565F68 in shadow to #A9B7BC lit).
  - Four round bores with silver rims sit in the face. Each holds a hot-pink Huggable (#E83ACD to #F13CDD) [Observed].
  - One pink Huggable sticks out of the lower bore. It has a stitched "x" eye and a stitched mouth [Observed].
- **Body.** The casing is teal-blue (#35729B to #3F89AF) with a yellow band (#F6E03F). Small white lamps sit on both flanks [Observed].
- **Handle.** A teal strut frame on top carries a handle wrapped in brown (#44332C to #49372C) [Observed].
- **How it is held.** On the hero stage she carries it at hip height by the top handle, with the face pointing forward [Observed] (8C7JH7STmyo maxres2; storyboard t≈30–32 s in crops/sb_8C7_saberi_27_32.png). For the attack pose she heaves it up onto her right shoulder [Observed] (8C7JH7STmyo t≈31 s; KLcjIqjf5sc t=27–28 s in crops/kl_saberi.png).
- **Size.** In the close-up the drum is about 1.2× her head width [Observed]. That makes it about 0.3× her standing height across the face, and roughly 0.35–0.4× her height front to back. On the BBG News chart (Oliver = 1.0×, Saberi 1.0×) that is about 0.3× [Inference from the 2026 skill-screen tiles].
- **Skins change it.** With the long-blonde/gold-tiara skin, the same drum has a gold-yellow frame (#EEDB39), a dark olive body (#7E763C / #403C2D), a silver face (#BDC2C6) and the same pink Huggables (#E446BD) [Observed] (thumbs/CuptyqnRweM_maxres1.jpg). The official "HUGGABLE HUNTER" Medic skin holds a gold gun with pink showing at the front [Observed] (official skins tour o0qNL2DHufw, t=106 s, crops/tour_medic.png). That this gold gun is a Splicer variant is [Inference].

**Firing**
- **Aim cone.** In matches the aim guide is a wide grey wedge (#77849A), roughly 40–50° across [Observed] (CuptyqnRweM t=30 s, crops/cup_a.png). This matches the official "wide spray… sweeping motion" [Canon].
- **Fire rate.** The wiki's "15 x 190" suggests 15 projectiles per attack [Inference from Fan-wiki]. Reload is "Very slow" [Fan-wiki]. The true rate and burst timing are [Unverified].
- **Muzzle flash.** On the 2026 hero screen the drum is raised to the shoulder and a violet-pink starburst flashes at the front (core #D0AAE3), throwing short pink streaks outward [Observed] (KLcjIqjf5sc t=28 s; crops/muzzle_zoom.png). At 8C7JH7STmyo t≈31 s the four bores glow pink at the moment of firing [Observed].
- **Sound.** [Unverified].

**Projectile**
- **What it is.** Officially "huggable bits" [Canon].
- **Hero screen.** One frame shows a whole pink Huggable figure flying up out of the muzzle [Observed, low-res] (KLcjIqjf5sc t=27 s). The 8C7JH7STmyo animation opens on a limp hot-pink Huggable with x-eyes and a stitched mouth lying on the stage before she raises the Splicer [Observed] (t≈27 s). Reading this as the Huggable being loaded as ammo is [Inference].
- **In matches.** The shots read as a fan of magenta/hot-pink streaks and star-shaped puffs mixed with white and pale-yellow sparkles. Through the storyboard blur the magenta samples come out at #A95492 to #BE63A1; the sparkles at #EFF0BF [Observed] (CuptyqnRweM t=20, 40, 70, 90, 160, 620, 630 s; crops/cup_a.png, crops/spray_zoom.png).
- **Reach.** The spray covers roughly 3–4 bear-lengths, consistent with Range "Normal" [Observed estimate; Fan-wiki].
- **Trails.** No individual trail can be resolved at this resolution [Unverified].

**Impact / end result**
- **What a hit looks like.** Pink and orange flecks burst where the spray strikes crates (#BC629C with #C7795A) [Observed] (CuptyqnRweM t=20 s). Pink streaks pile onto loot crates [Observed] (t=40, 70 s).
- **Kills.** The on-screen UI shows "HAS KILLED" banners [Observed] (t=480, 530, 560 s). What a defeated enemy looks like after a Splicer hit could not be resolved [Unverified].
- **Status effects and knockback.** None are documented [Unverified].

**Images viewed**
Downloads are under /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/saberi-bbh-gaps/:
- thumbs/8C7JH7STmyo_maxres2.jpg
- thumbs/CuptyqnRweM_maxres1.jpg
- thumbs/CuptyqnRweM_maxresdefault.jpg
- crops/sheet_two.jpg (all 8 thumbnails of both target uploads)
- crops/default_splicer_x2.png
- crops/muzzle_zoom.png
- crops/sb_8C7_saberi_27_32.png
- crops/kl_saberi.png
- crops/cup_a.png
- crops/spray_zoom.png
- crops/cup_lobby.png
- crops/tour_medic.png
- frames/KLcjIqjf5sc/cs_01.jpg
- frames/o0qNL2DHufw/cs_00–cs_05.jpg

**Depiction for shorts**
Show BBH-default Saberi hefting a teal four-bore drum by its brown-wrapped top handle, with pink Huggables visible in the bores. She swings it onto her shoulder and sweeps it side to side, and a wide fan of hot-pink fluff stars and white sparkles sprays out. Where it hits, targets pop into pink-and-orange confetti puffs. Keep "huggable bits" as plush stuffing and confetti, never torn bodies [BBG News invention].

**Confidence:** observed for the weapon, the muzzle flash and the spray colour; partial for impact and kills.

---

## Healing Turret (BBH Ultimate; BB Heroes only, 2023/2024 to present; not in BBG)

- **Official text:** "Her Ultimate, "Healing Turret," provides a healing radius for her and her teammates, excluding non-player units." [Canon] (battlebears.com/pages/characters).
- **In-game label:** the 2026 hero screen reads "SABERI / Medic … Ultimate / Healing Turret" [Observed] (KLcjIqjf5sc t=27–28 s).
- **Wiki stats** [Fan-wiki]: "Healing per Second 468"; Range "Very long"; "HP of HealBox 3360".

**Look**
- **The healing area.** A translucent green dome or disc sits on the ground [Observed] (CuptyqnRweM t=530, 570, 730, 740 s; crops/cup_d.png, crops/cup_heal_zoom2.png).
  - Colours: fill #4C7335 to #547B3A where it blends with the dark-red ground (#3B2021); rim #76AC5F; brightest #A7E579 [Observed].
  - Size: about 6 bear-widths across, so about 6× Oliver's width on the BBG News chart [Observed estimate].
- **The box (the wiki's "HealBox").** A small object sits at or near the centre of the dome, on a pale-blue ring (#80C8DA). It has its own HP number in a cyan box, "3198" at t=730/740 s. That is below the wiki's 3360 maximum, which fits a damaged box [Observed; Inference].
  - At storyboard resolution the object is only a few pixels: dark brown/olive with green on top (#463D30 / #547B3A) [Observed].
  - Whether it is a crate, a medkit or a turret with a head [Unverified]. No gun barrel is visible [Observed].
- **Do not borrow Graham's turret.** The grey-and-white gun turret with a red sight in the BBH key art is Graham's "Turret Summon" ("deploy a gun turret from scrap") [Canon] (files BBH_KeyArt.png and BBH_Epic_Banner.png). Do not use it as Saberi's turret [Inference].

**Firing**
- **Activation.** How she deploys it (throw or place) and how long it lasts: [Unverified].
- **Shooting.** Nothing is seen firing from it, and the official text describes only a "healing radius" [Canon; Observed].

**Projectile**
- None. The visible effect is pale-green plus-sign sparkles (#BCEC84) drifting up inside the dome [Observed] (t=530, 570, 730 s).

**Impact / end result**
- **Who is healed.** She and her teammates inside the radius, "excluding non-player units" [Canon]. Non-player units presumably means minions such as Piggables, Golems and turrets [Inference]. The rate is 468 per second [Fan-wiki].
- **Destroying it.** The box has HP, so enemies can destroy it [Fan-wiki "HP of HealBox"; Observed HP readout]. How it looks when destroyed: [Unverified].
- **Healed teammates.** I could not see a glow or a rising HP number on healed allies [Unverified].

**Images viewed** (same base folder):
- crops/cup_d.png
- crops/cup_heal_zoom2.png
- crops/healbox_zoom.png
- crops/kl_saberi.png
- crops/small_BBH_KeyArt.jpg
- crops/small_BBH_Epic_Banner.jpg

**Depiction for shorts**
Saberi plants a small box at her feet, which carries a little pale-blue base ring. A see-through green dome about six bears wide swells out of it, and pale-green "+" sparkles float up inside. Teammates inside perk up while enemies outside bounce off nothing. The box's exact design (we suggest a medic crate with a green cross) and any heal glow on allies are [BBG News invention].

**Confidence:** partial. The dome and the box's HP were observed; the object's design is unknown.

---

## Sub-topic: BBH Saberi model recheck (the "blonde, gold headband, white top" question)

- **Default BBH in-game model.** It matches the portrait note (white bandana, navy suit, red backpack). Details [Observed] (thumbs/8C7JH7STmyo_maxres2.jpg; KLcjIqjf5sc t=27–28 s; 8C7JH7STmyo t≈28–32 s):
  - White-grey knotted bandana (#DAD9E3) whose two ends stand up like ears.
  - Blonde side-swept fringe (#B8A582 to #CCB893).
  - Mid tan-brown fur (#726242).
  - Dark eyes with heavy lashes and eyeliner.
  - Near-black navy suit (#2E2F39) with a yellow cross on the chest (#FBFD9E) and yellow sleeves.
  - Teal gloves (#60D1CB to #67EFDE).
  - Yellow tool belt and pouch, and a red backpack.
- **Icon and portrait.** These are the official 2D icon (Saberi_BBH_HeroIcon_1, also the wiki's BBH_Profile_Saberi.png). They show a cream bandana, blonde bangs, one teal eye in a wink, a navy suit with grey harness and a red backpack [Observed]. The teal eye and the wink belong to the icon art. The 3D model's eyes read dark [Observed].
- **The look in "Matches with Saberi" is a skin, not the default** [Inference, strong]: long straight blonde hair, a gold tiara with a red gem, a white sleeveless top with gold shoulder guards and cuffs, a blue skirt (#3E37A0) and green eyes [Observed] (CuptyqnRweM_maxresdefault.jpg, maxres1–3). Reasons:
  - The video is titled "Matches with Saberi".
  - The model carries the Splicer drum, re-coloured gold and olive.
  - The 2026 skill screen and the 2024 hero animation show the white-bandana default.
  - The skin's name is [Unverified]. The six Medic skin icons in SkyVu's skins tour are too blurry to match (crops/tour_medic_icons.png).
- **Other Medic skins** [Observed]:
  - Official skins tour (Feb 23, 2024): "HUGGABLE HUNTER" (gold armoured flying suit with a cyan visor) and "SKULL DRIVER" ("BUY NOW 129") (o0qNL2DHufw t=106, 108 s).
  - SkyVu's official shorts "Top 4 Heroes to take down Huggable" (#1 Saberi) and "Top 5 Heroes To Use In DeathMatch" (Number 4: Saberi) show a pink-hoodie, red-boxing-glove skin with no gun on screen (OQrmLlynY1o t=19–21 s; 0029-TLegLE t=11–14 s).
- **Classic look in official BBH art.** SkyVu's BBH group key art (official skins-tour thumbnail o0qNL2DHufw maxresdefault; trailer end card ihkXJS4Oatk t=60–138 s; full size as the wiki file BBH_Splash.png) shows Saberi in her classic BBG look [Observed]. Sampled colours:
  - Red bandana with white polka dots (#D22E2C / #F7DDDC).
  - Dark brown fur (#572B1E shadow, #865D4F lit).
  - Teal-green eyes (#55A885) and a beauty mark.
  - Red top knotted at the waist (#930D1B).
- **Unidentified gun in that art.** She holds a gun not seen in any gameplay: an orange and dark-grey blocky body (#CE6739 lit, #A5492E) with a black ribbed hose behind a flared grey cone nozzle (#646E7A) [Observed] (crops/splash_saberi.png). Whether it is concept art for the Splicer, a skin weapon or decoration is [Unverified].
- **Images viewed:**
  - official/Saberi_BBH_HeroIcon_1_full.png
  - wiki/BBH_Profile_Saberi.png
  - crops/splash_saberi.png
  - crops/tour_key_left.png and crops/tour_key_right.png
  - crops/sheet_off.jpg
  - frames/OQrmLlynY1o/cs_00–01.jpg
  - frames/0029-TLegLE/cs_00–01.jpg
  - frames/ihkXJS4Oatk/cs_00–03.jpg
  - frames/XiMjGoHPNRY/cs_00–01.jpg (Saberi not identified there)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/completeness-r3/sheets/bbh.jpg
- **Confidence:** observed.

---

## Corrections for the character file (/home/user/thallo-site/bbg-news-repo/characters/saberi.md)

1. **Weapons/props line**
   - Current: "BBH: Huggable Splicer, Healing Turret [Canon] ([characters][chars])."
   - Change to: "BBH: Huggable Splicer (a teal four-bore drum launcher loaded with hot-pink Huggables, carried by a top handle and fired from the shoulder in a wide pink spray [Observed]) and Healing Turret (a small box the wiki calls a 'HealBox' [Fan-wiki], projecting a translucent green healing dome with pale-green '+' sparkles [Observed]) [Canon names] ([characters][chars])."
   - Evidence: 8C7JH7STmyo maxres2 and storyboard t≈27–32 s; KLcjIqjf5sc t=27–28 s; CuptyqnRweM storyboard t=530–740 s.
2. **Look, BBH alternative**
   - Current: "Alternative: the 2024 BBH redesign (light tan fur, blonde bangs, cream bandana, winking teal eyes, navy suit, red backpack) [Observed] ([icon][icon])."
   - Change to: "…[Observed] ([icon][icon]); the in-game 3D default adds a yellow chest cross, yellow sleeves, teal gloves and a yellow tool belt, with mid tan-brown fur (#726242) and dark eyes (the teal wink is icon-only) [Observed]. The long-blonde / gold-tiara / white-top look in fan match videos is a skin, not the default [Inference]."
   - Evidence: 8C7JH7STmyo maxres2; KLcjIqjf5sc t=27–28 s; CuptyqnRweM thumbnails.
3. **Optional BBH colour row for the Look section**
   - Current: "BBH portrait, k-means sampled [Inference]: fur #9C8564 / #796247, light #EEE4C7."
   - Change to: add "in-game 3D: fur #726242, suit #2E2F39, gloves #60D1CB, bandana #DAD9E3, Splicer teal #35729B / yellow #F6E03F / pink #E83ACD [Observed, sampled]."
   - Evidence: thumbs/8C7JH7STmyo_maxres2.jpg samples.

## Open questions

- What does the HealBox itself look like (crate, medkit or a small turret)? How long does it last, does it stay put, and how does it break? The storyboard tiles are too low-resolution to tell.
- What is the gold-tiara Medic skin called, and how is it unlocked? Does each skin re-colour the Splicer?
- What is the orange flared-nozzle gun in SkyVu's BBH key art (BBH_Splash.png): early Splicer concept art, a skin weapon, or decoration?
- How does a Splicer kill or knockback look in BBH? Is there a hit status effect? What do the Splicer and the turret sound like?
- Are whole Huggables fired, or only "bits"? The hero screen shows one whole pink Huggable flying from the muzzle; the gameplay tiles show only magenta puffs.
- Will any BBH element (Medic role, Splicer, Healing Turret) carry over to BBG 2026? Steam lists only "COMBAT TECH: Saberi".
