<!-- gap pass 1 -->
# Astoria (Sniper): addendum for the gaps (2026-10-17)

This addendum covers only four open gaps in the verified Astoria dossier (/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/out/verified/astoria.md):

1. The two new Astoria weapons from the final 2026 playtest (Oct 15, 2026).
2. The impact looks of the Art of War, the Blow Dart and the charged Crossbow.
3. The impact looks of Capital Pains, Mamba's Boy, Fidget Boomer, Rake and I Lava You.
4. The look of the BB Heroes (BBH) Sniper Rifle and its "Explosive Retreat" Ultimate.

Astoria is the BBG Sniper ("-SNIPER: Astoria" [Canon, Steam store text]).

**Sources I could reach today**
- YouTube's innertube "next" endpoint. It gave titles, channels, dates, descriptions, chapters, comments, and the live-chat replay of SkyVu's official final-playtest stream.
- YouTube's innertube "search" endpoint.
- i.ytimg.com thumbnails, including the full-size auto-frames maxres1, maxres2 and maxres3 (1280×720).
- The Steam ISteamNews API for app 4408320 (re-fetched).
- The official BATTLE BEARS channel RSS feed (re-fetched).
- The fan wiki's MediaWiki API: recent changes and image metadata.
- Material saved by the earlier run of this task: the battlebears.com characters page and the BBH Google Play listing with its 15 store screenshots.

**Sources I could not reach**
- YouTube video, player and storyboards. Every player client returned LOGIN_REQUIRED or ERROR, and storyboard URLs (i.ytimg.com/sb/…) returned 403.
- YouTube transcripts: get_transcript returned FAILED_PRECONDITION, and timedtext returned an empty body.
- Reddit (403) and X syndication (429).
- A web search found nothing about the new weapons.
- I watched no video.

**What counts as [Observed] here.** Every [Observed] claim comes from a still image I opened with the Read tool. Hex values are approximate PIL samples (run with python -I). Crops are in /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/.

**No timestamps for auto-frames.** YouTube's maxres1–3 frames are chosen automatically, and their times are unknown. The JustNubz showcase's "midpoint" frame (maxres2) shows the Heavy, not the Sniper chapter. So I give no timestamp for any auto-frame.

**How I tell Astoria apart in fan footage.** Sniper maximum health differs by era in the HUD [Observed]:
- 70 in Dec 2014;
- 77 in 2017;
- 80 in 2015–Apr 2018;
- 90 from Jun 2018, including build 3.0.7 in Oct 2026;
- 94 when the Rake is equipped: 90 × 1.05, the Rake's "5% Health Increase" [Fan-wiki infobox; the arithmetic is Inference].

---

## Two new Astoria weapons from the final playtest (new · BBG 2026, final playtest Oct 15, 2026; names unverified)

- **Official text** [Canon]:
  - SkyVu's Steam post of Oct 14, 2026 and the description of the official stream "BBG Livestream Final Playtest before Steam NextFest Oct 19" (ZMhLVXWT6OY, BATTLE BEARS) both say: "A lot to test this week, including a couple of surprises we didn't think we'd be able to squeeze in!"
  - The stream's "Headline additions" are "-Custom keybinds / -Jukebox / -UI controller support / -Lighting improvements / -Lots of bug fixes".
  - Neither text names Astoria or any weapon.
- **Fan claim.** InstableGR's description of "Battle Bears Gold - Final PC Playtest (10/15/26)" (HKbwq7PolNc, Oct 17, 2026) says: "We got skins for Riggs, Wil, and Huggable inspired by the classic games and two new weapons for Astoria which is all great" [fan claim].
- **Official live-chat replay.** @bold3703 asked at 18:55: "Did Astoria get two new weapons". No written answer appears in the 203-message replay [Observed chat text]. Ben Vu's spoken answer, if any, could not be reached because the transcript is blocked [Unverified].
- **Status:**
  - The wiki has no page for either weapon. Its recent changes from Oct 10 to Oct 17 are empty [Fan-wiki API].
  - No official 2026 upload after Oct 16 (RSS) and no Steam post after Oct 14 mentions them.
  - Both names are [Unverified].

### Candidate weapon A: seen only as a HUD icon [Observed, one frame]

- **Source frame:** HKbwq7PolNc auto-frame maxres2, time unknown.
  - The HUD build string reads "3.0.7_2026.11.19_b7".
  - The shooter has cream fur and wears a red jacket with white sleeves and a brown backpack, the Assassino-style outfit. Health is 90/90, the Sniper's 2026 maximum, so the shooter is Astoria [Inference].
  - The top banner reads "11 [bear icon] ART". That fits the Free-for-All leader display seen in other 2026 frames, so this is probably Match 2 or 3 (both Free-for-All with Astoria) rather than Match 9 (Team Battle) [Inference].
- **Primary-slot icon** [Observed]:
  - a long dark-navy rifle body (≈#2A3C56) with a pale highlight stripe along the barrel (≈#C2CBEA);
  - a black box-shaped muzzle and a small grey rail near the front;
  - a light-blue translucent scope shaped like a capped plastic bottle (≈#96C6E0) on top;
  - a black pistol grip, with a small cream block marked with two dots in front of it;
  - a large dark-red oval at the rear (≈#8E0C1E), placed like a stock or a squeeze bulb.
  - Ammo shows 2/4.
- **Secondary icon:** a bald eagle with a white head, yellow beak, brown body and white tail. That is the Eagle Standard [Inference, matching the Gear Up images in the main dossier].
- **It matches no known Sniper primary** [Observed comparison; conclusion Inference]:
  - I set it beside the 2026 Art of War icon (black and yellow receiver, grey hopper, red barrel, brush tip), and the earlier dossier documents the other six primaries.
  - None of the eight wiki primaries has a navy body, a bottle scope or a red oval stock.
  - So it is probably one of the two new weapons. A 2026 re-skin of an old weapon cannot be ruled out [Unverified].
- **The model in her hands:** a large dark slate-teal block shape (≈#2C4241) sits in front of her right arm. Whether it is part of this weapon is [Unverified].
- **Firing / projectile / impact: not observed.** At the far target there are yellow translucent shards, a blue triangle marker and a green "+" shield. The blue triangle and the green shield appear as generic HUD and spawn markers in other 2026 frames, and none of these can be tied to the weapon [Inference].

### Candidate weapon B: no image [Unverified]

- It appears in no frame I could open.
- It might be a secondary, since the secondary slot in the one frame holds the old Eagle Standard [Inference, weak].
- In a fan livestream of the same session ("Battle Bears Gold FINAL PLAYTEST", MS2wiArCiCA, Left4Dead), the channel owner typed in chat at 22:13: "this secondary is SO op". The class is not stated [fan; unattributed].

### Other final-playtest uploads checked without finding Astoria

I opened the auto-frames of these and found no Astoria [Observed]:
- JustNubz 1MP1rFi4t-Q;
- MS2wiArCiCA;
- dz4iqZE8nQE;
- ORYnnvqn19w;
- s9W6eLXj9qc;
- JustNubz 4N3pXUAYVq0;
- the official ZMhLVXWT6OY and pmE2jKQLSms;
- 12 "[LA]Huggable" final-playtest games.

### Images viewed

Thumbnails:
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/gap1_HKbwq7PolNc_maxres2.jpg (https://i.ytimg.com/vi/HKbwq7PolNc/maxres2.jpg)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/gap1_HKbwq7PolNc_maxres1.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/gap1_HKbwq7PolNc_maxres3.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/gap1_HKbwq7PolNc_maxresdefault.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/sc_-lAtv-j9Sms_maxres2.jpg

Crops:
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/hk_m2_icon.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/hk_m2_held.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/hk_m2_target.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/hk_m2_top.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/icon_compare.jpg

Contact sheets:
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/sheet_gap1_1MP1rFi4t-Q.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/sheet_fp_MS2wiArCiCA.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/sheet_fp_dz4iqZE8nQE.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/sheet_fp_ORYnnvqn19w.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/sheet_fp_s9W6eLXj9qc.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/sheet_off_ZMhLVXWT6OY.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/sheet_off_pmE2jKQLSms.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/sheet_jn_4N3pXUAYVq0.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/la_m0.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/la_m1.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/la_m2.jpg

### Depiction for shorts

Don't feature either weapon until SkyVu names it. If a teaser is needed, show Astoria in silhouette hefting a navy rifle with a pale-blue bottle scope and a red oval stock, with a "NEW" tag. What it fires and how it hits would be [BBG News invention].

### Confidence

Partial for weapon A (one HUD icon). Unknown for weapon B, both names and both mechanics.

---

## Art of War (primary · revealed 2012, released BBG 2.11 Aug 27, 2014; seen in the 2026 beta, build 3.0.0)

- **Official text:** "Paint the battlefield red, or orange, or yellow, or green, or blue, or violet. It doesn't really matter as long as its your enemies pallet." ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Art_of_War).
- **2026 status, now observed** [Observed]:
  - Source: Takishi's "Astoria - The "Art of War" (Battle Bears Gold)" (B-8uQcs1DFA, Aug 2, 2026). Its description reads "12 years after - Here we go again ! (Battle Bears Gold - Beta testing)".
  - The auto-frames show Astoria (cream fur, team-blue backpack, health 94/94) with the Art of War HUD icon: black and yellow receiver, grey oval hopper, red barrel with gold marks, white brush tip with an orange tip.
  - Ammo reads 0/4 (with "RELOAD"), 2/4 and 4/4. The build string reads "3.0.0".
  - The 2026 clip is 4. The infobox says 3 [Fan-wiki], and 2016 HUDs show 2/3 and 1/3 [Observed, rnbGzc0Gm0g].
- **Look:** the icon matches the render described in the main dossier [Observed]. Held two-handed at chest, as all her rifles are [Inference].
- **Firing:** manual aim, with no lock and no headshots [Fan-wiki]. The uploader of rnbGzc0Gm0g writes "Why their no auto-lock" and "It shoot canceric colors" [fan description].
- **Projectile** [Observed, rnbGzc0Gm0g maxres2, Nstrike, Jan 2, 2016]:
  - A long, thin, perfectly straight beam made of parallel rainbow bands with a soft glow.
  - Sampled bands, from one edge to the other: magenta ≈#F122CC, violet ≈#A829F4, blue ≈#305AEA, sky ≈#35AFFF, cyan ≈#39F2ED, green ≈#58F75C, yellow ≈#F8F41F, orange ≈#F8680F, red ≈#DC211C.
  - It is about 40 px wide (at 1280 px) near the camera and thins with distance.
  - The HUD shows the Art of War with ammo just dropped to 2/3, so this is her shot [Inference, strong].
  - In this frame the beam enters from the lower-left edge rather than from her hands. It is probably a trail that lingered while the camera turned [Inference].
  - This fits the wiki's "a single stream-like bullet" [Fan-wiki].
- **Impact / end result** [Observed]:
  - Where the beam ends, by a red-coated enemy: a small white-to-lavender starburst, with a rounded pink blob beside it (rnbGzc0Gm0g maxres2).
  - In Q5A0__2IHSk maxres3 (Epic Domination BBG, Sep 27, 2014; Solid Fisher skin, 2/3 ammo), a distant pink target has small red, green, blue and violet flecks on its chest under a green crosshair. The image is low-resolution; that these are paint flecks is [Inference].
  - The wiki's "erupting into a flurry of paint, however, it is merely cosmetic" [Fan-wiki] is consistent with this. No large paint explosion appears in any frame.
  - The 2026 frames show yellow star sprites near distant enemies and a fireball in the distance. Neither can be attributed to the weapon [Observed; attribution Unverified].
- **Images viewed:**

  Thumbnails:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/aow_rnbGzc0Gm0g_maxres2.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/aow_rnbGzc0Gm0g_maxres3.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/aow_Q5A0__2IHSk_maxres3.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/aow_B-8uQcs1DFA_maxres2.jpg

  Crops:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/aow_rnb_end.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/aow_rnb_beam.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/aow_q5_m3_target.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/aow26_m1_mid.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/aow26_m1_held.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/aow_m2_icon.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/aow_m3_icon.jpg

  Contact sheets:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/sheet_aow_B-8uQcs1DFA.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/aow_mosaic.jpg (rnbGzc0Gm0g, Q5A0__2IHSk, ztbY2F5JdsY, WqpdWnzsGUM)
- **Depiction for shorts:** the brush-tipped rifle fires one thin, glowing rainbow ribbon straight to the target. On contact there is a small white-lavender sparkle pop and a few coloured paint flecks on the target, with no damage shown. A bigger cartoon paint splat would be [BBG News invention].
- **Confidence:** observed (projectile, 2026 presence); partial (impact).

---

## Blow Dart (primary · BBG 2.6, Dec 20, 2013; 2026 status unverified)

- **Official text:** "Just because it is the future does not mean there cannot be old school weaponry. Watch out for exploding darts!" ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Blow_Dart).
- **HUD icon** [Observed, A_1aki1oFTg maxres1, SW, Jan 9, 2022]: a copper tube with a pink chevron and a pink stripe, purple bands, and an angular head with a pink-lipped muzzle. It matches the main dossier's model.
- **Clip sizes in the HUD** [Observed]: 0/6 (Jun 2014), 0/8 (Jun 2014), 2/6 and 0/6 (Jan 2022), 4/8 (May 2023, build 2.53.6). The infobox says 4 [Fan-wiki]. The differences probably come from Ammo+ equipment [Inference].
- **Projectile:**
  - A pale cream-yellow straight streak (bright core ≈#FDFBDF) runs from her hands to a distant enemy, with the Blow Dart in the HUD [Observed, low-res, jNGRojtbvf4 sddefault, Jan 31, 2014; that it is the dart's flight is Inference].
  - The dart itself is not resolved in any frame [Unverified].
- **Impact / end result** [Observed; that these are Blow Dart detonations is Inference, strong, since the Blow Dart is equipped in all three frames and the wiki describes a "blue tinge and large Area of Effect"]:
  - **A_1aki1oFTg maxres2** (ammo 0/6, "RELOAD", so every dart had been fired): a huge translucent pale-cyan dome or burst fills the upper centre (mean ≈#B3E4E1, light ≈#BAFEFC, shading ≈#4EA597). A blue crystal-armoured enemy is caught mid-air inside it, still holding his copper-drum gun. The blast launching him is [Inference].
  - **A_1aki1oFTg maxres1** (2/6): a starburst of long white blade-like shards (≈#EFFAF2) radiates from the crosshair point, with pale-blue streaks behind them.
  - **kaV9iJ0gttc maxres3** (Rumi2004, May 10, 2023; 4/8; Fairy's Dust as secondary): the same kind of white blade-shards radiate around a target.
- **Corrections to the main dossier's leads:**
  - The "large pale-blue triangular shape" in 4u-wBVKu5Kw hq1 is a blue zig-zag lightning-bolt object lying on the ground. The same bolt objects appear loose in unrelated matches: Mamba's Boy in 2018, the Rake video in 2023 and HKbwq7PolNc maxres3 in 2026. It is therefore a dropped pickup, not the Blow Dart blast [Observed; that it is a pickup is Inference].
  - The long bright-green straight streaks (≈#27ED77) and green translucent dice-like cubes in 4u-wBVKu5Kw sddefault have an unclear origin and are not attributable to the Blow Dart [Unverified].
  - The pink-violet faceted blobs in NogKTD5Vsx0 match Fairy's Dust better than a dart blast [Inference].
- **Images viewed:**

  Thumbnails:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/bd_A_1aki1oFTg_maxres1.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/bd_A_1aki1oFTg_maxres2.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/bd_kaV9iJ0gttc_maxres3.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/bd_4u-wBVKu5Kw_sddefault.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/bd_4u-wBVKu5Kw_hq1.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/bd_NogKTD5Vsx0_sddefault.jpg

  Crops:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/bd_a1_icon.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/bd_a1_m2_blast.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/bd_4u_streak.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/bd_jn_sd.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/bd_jn_streak.jpg

  Contact sheets:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/bd_m0.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/bd_m1.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/bd_m2.jpg
- **Depiction for shorts:**
  1. A puff from the copper tube and a thin pale-yellow streak; the dart sticks.
  2. A comic beat: the wiki gives a 6 s fuse [Fan-wiki].
  3. A burst of white spike-shards and a big pale-cyan dome that pops the target harmlessly into the air.
  
  The blinking dart and countdown are [BBG News invention].
- **Confidence:** partial. The impact is observed, and its attribution is a strong inference.

---

## Crossbow / "Unicorn Crossbow 2.0": the charged burst (primary · BBG 2.2, Aug 21, 2013; reworked 2.6)

- **Official text:** "Leave it to Astoria to make a rapid fire weapon that shoots unicorn horns. Even worse is that she can charge up the weapon and release a stronger attack! What's next jackelope weapons?" ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Crossbow_(BBG)).
- **Clip history** [Observed]:
  - The 2.2 Gear Up (nhzRGwyAypA hq3, PrinceofBB, Aug 21, 2013, version label "2.2") lists "VIPERIFLE / CAPITAL PAINS / DEAD EYE / CROSSBOW EQUIPPED". Solid Fisher Astoria holds the white crossbow.
  - The HUD shows 88/100 (hq1) and 100/100 (VziLarZLx0E, RuBTNbSPydc), which confirms the 100-round pre-2.6 clip [Observed + Fan-wiki].
  - 2023–2024 HUDs show 5/15 and 15/15 (build 2.53.6), matching the infobox's 15 [Observed].
- **Charge look** [Observed; meaning Inference]:
  - RuBTNbSPydc maxres2 (progamerr25, Oct 7, 2013): a glittery pink-violet aura surrounds her and the crossbow at the bottom of the screen. That fits the wiki's "shine a bright purple aura" [Fan-wiki].
  - _zEvhEjA_Tg maxres3 (Rumi2004, Aug 26, 2023; crossbow HUD, 5/15): pink-magenta and white four-point star sparkles burst at the crossbow front.
  - F_usCDPV6CM maxres3 (Feb 14, 2024; a gold Astoria skin; 15/15): violet-pink sparkles at the crossbow, and a tall white vapour plume ahead of unclear origin.
- **Projectile:** in VziLarZLx0E (Aug 22, 2013), a thin lavender line leaves the white crossbow [Observed, low-res]. An orange-yellow fireball near a blue-team player in the same frame cannot be attributed [Unverified].
- **Charged burst impact: still not observed** [Unverified]. Documented only: "AOE damage upon a hit"; "first Sniper weapon that could directly cause the player to suicide" [Fan-wiki].
- **Images viewed:**

  Thumbnails:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/xb_RuBTNbSPydc_maxres2.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/xb_dStej-r7jAg_maxres2.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/xb_NPKKs3i6mX4_maxres2.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/xb_F_usCDPV6CM_maxres3.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/rk__zEvhEjA_Tg_maxres3.jpg

  Crops:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/xb_vz_fire.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/xb_vz_line.jpg

  Contact sheets:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/xb_vz.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/xb_m0.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/xb_m1.jpg
- **Depiction for shorts:** while charging, a glittery pink-violet aura wraps the white unicorn crossbow and pink and white star sparkles fizz at its tip [Observed]. The released horn's lavender sparkle-pop on impact is [BBG News invention].
- **Confidence:** partial (the charge look is observed; the burst is unknown).

---

## Capital Pains (primary · BBR 1.3 → BBG; red mode later removed; 2026 status unverified)

- **Official text:** "If the NASDAQ stock index is down the day before, it shoots much faster, has more ammo, but does less damage and locks slower." ~ Official Battle Bears Gold description [Game text via wiki].
- **New frames:**
  - XSJ6TSXQVZI (Paul Mara, Apr 14, 2013, "Tips series #2 RED capital pains"): ammo x/5 (5/5, 4/5, 0/5) in the Solid Fisher skin [Observed]. That fits red mode's "more ammo" [Inference].
  - gDhD-AtDUrk sd1 (Dec 24, 2014, titled "red capital pains"):
    - The HUD icon is still the green €-zig-zag, so the icon does not change colour with the mode [Observed; Inference].
    - Ammo 1/2, health 70/70, with a "HEAD SHOT" entry in the kill feed.
    - A thin vertical red streak flecked with white sits at a pink target [Observed, low-res; that it is her bullet is Inference]. That agrees with the earlier "red dotted streaks".
  - yZY6TO_lmKc maxres2 (SW, Aug 31, 2015, "GREEN", 2.21): ammo 5/6 with no visible shot [Observed]. This conflicts with the infobox ammo of 2 [Fan-wiki]; equipment is unknown.
- **Impact / end result:** still not observed in any frame [Unverified]. J49iiFx_nRE sd3 shows a fire burst, but the shooter is a different class using a Doomstick.
- **Images viewed:**

  Thumbnails:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/cp_gDhD-AtDUrk_sd1.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/cp_J49iiFx_nRE_sd3.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/cp_yZY6TO_lmKc_maxres2.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/cp2_3gCvALnjpKI_maxres1.jpg

  Crops:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/cp_gd_sd1_target.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/cp_gd_sd1_icon.jpg

  Contact sheets:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/cp_m0.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/cpmb_m1.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/more_m.jpg
- **Depiction for shorts:** unchanged from the main dossier. Red day means a thin red, white-flecked streak; green day means green. The coin-confetti hit is [BBG News invention].
- **Confidence:** partial (projectile); unknown (impact).

---

## Mamba's Boy (primary · BBR 1.3.1 → BBG; 2026 status unverified)

- **Official text:** "This gun will send you crying back to your mamba. Trade aim and damage for a faster rate of fire." ~ Official Battle Bears Gold description [Game text via wiki].
- **Projectile** [Observed]:
  - **WlMcJybUywg sddefault** (rockstartanwille, Jun 25, 2013): the HUD shows the lime snake-rifle icon at ammo 5/6. A thin mint-green streak (≈#55CD8D, brighter ≈#16EB7F near the shooter) runs into a black lock reticle on the target.
  - **GTYs6LwzR2c maxres3** (SW, Jun 2, 2018; ammo 0/2, health 93/90):
    - The lime snake-head muzzle is visible at the bottom edge.
    - The shot is a flat, blade-like mint-green tracer (core ≈#00FA64, ≈#1FED6C), wide at the muzzle and tapering into the black lock reticle.
    - A thin straight red line leaves the snake's mouth. It is probably a laser sight [Inference].
- **Impact / end result** [Observed, one frame]: a small lime-green spark puff at the hit point (GTYs6LwzR2c maxres3). The documented effect is that a white-lock hit kills with a headshot [Fan-wiki]. In WlMcJybUywg, a horizontal spray of green, white and red flecks with an orange trail next to the target comes from beside it, not from her shot [Unverified].
- **Correction to the main dossier:** the main dossier's projectile line rests on one official thumbnail with a "thin pale-white streak". Two fan frames with Mamba's Boy confirmed in the HUD show a mint-green tracer instead. The pale streak may belong to another weapon or era [Unverified].
- **Images viewed:**

  Thumbnails:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/mb_WlMcJybUywg_sddefault.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/mb_WlMcJybUywg_sd1.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/mb_GTYs6LwzR2c_maxres3.jpg

  Crops:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/mb_wl_target.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/mb_wl_icon.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/mb_gt_target.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/mb_gt_muzzle.jpg

  Contact sheets:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/mbfb_m2.jpg
- **Depiction for shorts:** the open-mouthed lime snake rifle spits quick mint-green tapering tracers into a lock reticle, and each hit gives a small lime spark puff. Animating the red sight line as a flicking snake tongue is [BBG News invention].
- **Confidence:** observed (projectile); partial (impact).

---

## Fidget Boomer (primary · BBG 2.27, May 29, 2017; 2026 status unverified)

- **Official text:** "Have toy tricks gone too far!? Explosions are safe right?" ~ Official Battle Bears Gold description [Game text via wiki].
- **Look and hold** [Observed]:
  - ca8Zn_DDZ_M maxres2 (SW, Sep 9, 2018; health 11/90): Solid Fisher Astoria holds the dusty-pink chrome three-lobed spinner raised in one hand by a lobe. The HUD icon is the same spinner, with ammo 2/2.
  - ejzYTuB-CfM maxres1 (S8 KBW_Overwatch, "BattleBearsGold 2.27 S3 Ep89", about 2017): the spinner is held raised, with ammo 3/3.
  - These HUD clip sizes differ from the infobox's 4 [Fan-wiki].
- **Not the explosion:**
  - The tall green-yellow glowing column in ca8Zn_DDZ_M maxres2 is a light shaft belonging to the map [Inference].
  - The pink lightning crackles in ejzYTuB-CfM maxres1 sit next to a "POWER UP" kill-feed entry and cannot be attributed.
  - The fire background in ca8Zn_DDZ_M's custom thumbnail is a fan composite, not evidence.
- **Explosion: still not observed** [Unverified]. Documented only: a short delay after contact, then an explosion "akin to the TNT Launcher" [Fan-wiki].
- **Images viewed:**

  Thumbnails:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/fb_ca8Zn_DDZ_M_maxres2.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/fb2_ejzYTuB-CfM_maxres1.jpg

  Contact sheets:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/mbfb_m2.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/more_m.jpg
- **Depiction for shorts:** she holds the chrome-pink spinner overhead by one lobe and flings it. The spin-whistle, the landing wobble and the blast colour are [BBG News invention].
- **Confidence:** observed (look and hold); unknown (blast).

---

## Rake (secondary · in BBG by Jan 2014; seen in the 2026 beta, build 3.0.0)

- **Official text:** "Stop your opponents dead in their tracks with this exciting new gardening tool!" ~ Official Battle Bears Gold description [Game text via wiki].
- **2026 status, now observed:**
  - The secondary icon in Takishi's Aug 2, 2026 beta frames (B-8uQcs1DFA maxres1–3) matches the Rake's HUD icon from Rumi2004's 2023 Rake video pixel-shape for pixel-shape: a dark-grey rake in profile, with a long handle and a head showing a short turquoise tooth [Observed side-by-side comparison].
  - Health in those 2026 frames is 94/94, which equals 90 × 1.05 for the Rake's "5% Health Increase" [Fan-wiki infobox; the arithmetic is Inference].
- **Look in the hand** [Observed, _zEvhEjA_Tg maxresdefault, Rumi2004, Aug 26, 2023, build 2.53.6]:
  - Astoria holds the Rake up one-handed like a sign: a dark-grey square head with five turquoise teeth on a grey handle. That matches the main dossier's Gear Up.
  - Ammo 6/10 matches the infobox's 10 [Observed + Fan-wiki].
  - Health 141/94 is over-healed, with the cause unknown.
- **Spring-up: still not observed** [Unverified]. In _zEvhEjA_Tg maxres1, yellow star sprites lie scattered at a nearby enemy's feet. But the crossbow was in hand (0/15), and identical stars appear in unrelated 2026 frames, so they cannot be tied to the Rake.
- **Images viewed:**

  Thumbnails:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/rk__zEvhEjA_Tg_maxresdefault.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/rk__zEvhEjA_Tg_maxres1.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/rk__zEvhEjA_Tg_maxres3.jpg

  Crops:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/rake_icon_compare.jpg
- **Depiction for shorts:** she plants the turquoise-toothed rake. The step-and-bonk gag with stars and no injury is [BBG News invention], consistent with the wiki's "spring up and damage".
- **Confidence:** observed (look, 2026 presence); unknown (spring-up).

---

## I Lava You / "I Lava U" (secondary · BBG 2.51, Apr 13, 2018; 2026 status unverified)

- **Official text:** none found. The wiki infobox titles it "I Lava U" [Fan-wiki].
- **New frames:**
  - The only weapon-titled video (T3cQQTFP0a4, Apr 15, 2018) mostly shows another class in a yellow hard hat.
  - Its maxres1 shows a dark-headed bear with Sniper-era health 52/80 and ammo 2/4 (I Lava U has 4 [Fan-wiki]) on a green slime map. No mine or blast is visible [Observed].
  - In A_1aki1oFTg (2022) the secondary icon is a long dark lava-textured rifle with a red glow and a grey scope. That is consistent with the wiki's "Sniper with I Lava U" image [Observed; identification Inference].
- **Mines and blasts: still not observed** [Unverified].
- **Images viewed:**

  Thumbnails:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/il_T3cQQTFP0a4_maxres1.jpg

  Crops:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/il_m1.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/ilava_compare.jpg

  Contact sheets:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/sheet_il_T3cQQTFP0a4.jpg
- **Depiction for shorts:** unchanged from the main dossier. The look of the mines and the blast is [BBG News invention].
- **Confidence:** observed (look); unknown (projectile, impact).

---

## BB Heroes Sniper Rifle + "Explosive Retreat" Ultimate (BBH, Astoria added May 2023; not BBG)

- **Official text:**
  - "Astoria wields a sniper rifle for long-distance attacks, dealing more damage from afar. Up close, she's vulnerable but compensates with her "Explosive Retreat" Ultimate, diving away from the action when enemies get too close." [Canon, battlebears.com/pages/characters, saved page]
  - The Google Play listing says "Astoria the Sniper" [Canon, store text].
- **Official visuals** [Observed]:
  - **battlebears.com image** (cdn.shopify.com …/astoria_1_480x480.png), identical to the wiki's File:BBH_Profile_Astoria.png: head only. Cream fur, blue eyes, a light-grey cap with a red brim and a red ear-shaped emblem, and a red collar. No weapon.
  - **Official "BATTLE BEARS HEROES Gameplay & Skins Tour 4K 60fps"** (o0qNL2DHufw, BATTLE BEARS, Feb 23, 2024):
    - maxres3 is the skin screen "ASTORIA EXERCISIST / Sniper": a yellow-skinned Astoria with cracked skin, yellow eyes, a pink headband, a pink crop top and leggings. No weapon is shown.
    - In the roster lineup, a cream bear in black wraparound sunglasses and a black suit holds upright a white unicorn-head weapon with a lavender horn tip, like the BBG Crossbow.
  - **BBH key art** (File:BBH_KeyArt.png, wiki upload 2024-10-16, "15 YEAR ANNIVERSARY"; also Google Play screenshot ss_08): the same suited bear in sunglasses runs carrying a paint-splattered multicolour rifle with a red barrel and a white brush tip, i.e. Art-of-War-style.
- **That suited bear is Astoria's "James Pond" skin** [Inference, strong]. Fan video R8MqgiIcJ8Q (S8 KBW_Overwatch, May 3, 2025) is titled "Battle Bears Heroes: Astoria James Pond - Red Gameplay". Its thumbnail render shows the suited bear in sunglasses with a red tie holding a pink fish-shaped gun with a silver spike barrel [title is fan; image Observed].
- **Gameplay and lobby frames from fans** [Observed]:
  - ugDSh4yIMiI (S8 KBW_Overwatch, May 23, 2023), top-down match frame: a long, thin mint-aqua tracer (≈#89E6D4–#7BF0C4, core ≈#3BF089) runs from the player "KBW_Overwatch 2" to an enemy.
  - Its results screen shows that player and a teammate as Astoria in a Solid-Fisher-like helmet (black with red stripes and three red lamps). Each holds a Viperifle-like rifle: dark body, bright green capsule on top, green snake-head muzzle.
  - sxXRsKt649A (Feb 20, 2025) thumbnail: Astoria in a black cap, orange scarf and black outfit with red piping holds an Art-of-War-style rifle with a paint-splattered receiver and a red barrel bearing gold characters.
  - So the BBH rifle model changes with the skin [Inference].
- **Explosive Retreat: no frame found** [Unverified]. I checked the official tour, the official 4K trailer (ihkXJS4Oatk), the official BBH trailer ISutMIXTUc8, the official sneak peek b6K9Z9mVskU, the 15 store screenshots and four fan Astoria videos. The wiki's "4 x 670" damage hints at four hits [Fan-wiki; Inference].
- **Images viewed:**

  Thumbnails:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/thumbs/bh_sxXRsKt649A_maxresdefault.jpg

  Crops:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/bbh_exer.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/bbh_line_left.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/bbh_key_agent.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/gp01_lineup_mid.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/gp05_mid.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/bh_ug_m3_left.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/bh_ug_m2_mid.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/bh_sx_rifle.jpg

  Contact sheets:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/sheet_bbh_o0qNL2DHufw.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/bbh_m.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/bh_m2.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/sheet_bh_ugDSh4yIMiI.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/sheet_bh_R8MqgiIcJ8Q.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/gp_sheet_0.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops2/gp_sheet_1.jpg

  Official images:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/official/bb/astoria_icon.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops/BBH_Profile_Astoria.png.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-gaps/crops/BBH_KeyArt.png.jpg
- **Depiction for shorts:** keep BBH out of BBG-era shorts. In a BBH-labelled short, her rifle fires a long, thin mint-aqua tracer [Observed]. Any dive, blast or count for Explosive Retreat is [BBG News invention].
- **Confidence:** partial (several rifle looks and one tracer observed); documented, text only (Explosive Retreat).

---

## Corrections for the character file (/home/user/thallo-site/bbg-news-repo/characters/astoria.md)

Flagged only; nothing was edited. These add to the main dossier's corrections 1–12.

1. **Line 56, Weapons/props**
   - Current: "- **Weapons/props:** a sniper rifle [Canon] (BBG default: the Viperifle [Fan-wiki] ([Sniper (BBG)][sniper])); the Tomahawk, …"
   - Correction: after the main dossier's item 8 (add the Dead Eye and Fairy's Dust), append:
     > "2026 build: fan beta footage (Aug 2, 2026, build 3.0.0) shows the Art of War (a brush-tipped paintball rifle that fires a thin rainbow beam) and the Rake equipped [Observed, fan video B-8uQcs1DFA]. The Oct 15, 2026 final playtest added 'two new weapons for Astoria' [fan claim, InstableGR]; SkyVu only promised 'a couple of surprises' [Canon]. One appears only as a HUD icon (a navy rifle with a light-blue bottle-shaped scope and a red oval stock); neither is named [Unverified]."
   - Evidence: crops2/icon_compare.jpg, crops2/rake_icon_compare.jpg, thumbs/aow_B-8uQcs1DFA_maxres2.jpg, thumbs/gap1_HKbwq7PolNc_maxres2.jpg; the ZMhLVXWT6OY description and the Steam post of Oct 14, 2026.
2. **Line 62, Fighting** (Explosive Retreat)
   - Current: ""Up close, she's vulnerable but compensates with her 'Explosive Retreat' Ultimate, diving away from the action" [Canon] ([characters][chars])."
   - Correction: keep the quote and tag it BBH. Add: "Its look is undocumented: no official BBH tour, trailer or store screenshot and no fan BBH frame shows it [Unverified], so any dive or blast design is [BBG News invention]." The main dossier's item 9 still applies to the beats on lines 68 and 76.
   - Evidence: auto-frames of o0qNL2DHufw, ihkXJS4Oatk, ISutMIXTUc8 and b6K9Z9mVskU; the 15 Google Play screenshots; the fan videos ugDSh4yIMiI, R8MqgiIcJ8Q, sxXRsKt649A and E5vWKwOhc8k.
3. **Line 101, open question on the 2026 build**
   - Current: "- What default skin, taunts and audio does the 2026 build use? The [Astoria Overhaul][overhaul] and [2026 showcase][showcase] videos haven't been viewed."
   - Correction: keep it, and add a new open question:
     > "What are the two new Astoria weapons from the Oct 15, 2026 final playtest called, and what do they fire? One is seen only as a HUD icon (navy rifle, light-blue bottle scope, red oval stock, 4-round clip) in InstableGR's HKbwq7PolNc."
   - Evidence: thumbs/gap1_HKbwq7PolNc_maxres2.jpg; the official live-chat question "Did Astoria get two new weapons" (18:55) had no written answer.

## Open questions

- What are the names, slots, firing modes and impacts of the two new Astoria weapons from Oct 15, 2026?
  - Is the navy bottle-scope rifle (HUD ammo x/4) one of them, or a 2026 re-skin?
  - A human viewer could check HKbwq7PolNc Matches 2, 3 and 9 (5:14, 9:24, 35:30) and JustNubz 1MP1rFi4t-Q.
  - The official stream ZMhLVXWT6OY around 18:55 may hold Ben Vu's spoken answer.
- Will the Steam Next Fest demo (Oct 19–21, 2026) or SkyVu's "Steam Next Fest Demo Party with BBG Devs" stream (Sf01OOF_X3Q, scheduled Oct 19) show or name them?
- Which still-unseen impact effects need a human viewer of the fan videos?
  - the charged Crossbow burst;
  - the Fidget Boomer blast;
  - the I Lava U mines and blasts;
  - the Rake spring-up;
  - the Capital Pains hit.
- Are the white blade-shards plus pale-cyan dome definitely the Blow Dart detonation? A frame-accurate look at A_1aki1oFTg or kaV9iJ0gttc would settle it.
- What does BBH's Explosive Retreat look like? And is the BBH rifle model per skin: Viperifle-like with the Solid-Fisher-like helmet, Art-of-War-like with James Pond and the black-cap look, a fish gun with James Pond - Red?
- Why do 2026 HUD clip sizes differ from the pre-2021 infoboxes (Art of War 4 vs 3), given that BBG 3.0 removed the +1 equipment except Speed?
- Is the Assassino jacket the default look in build 3.0.7, or a skin chosen by that player?
