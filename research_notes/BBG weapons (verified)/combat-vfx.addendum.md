<!-- gap pass 1 -->
# Combat VFX addendum: Frozen (S'no Matter, Let It Cold)

**What this covers.** This addendum covers the Frozen status that Tillman's (Demo) two ice weapons inflict:
- **S'no Matter**, primary, added in BBG 2.15 on Dec 20, 2014 [Fan-wiki: Updates; S'no Matter]
- **Let It Cold**, secondary, added in BBG 2.26 on Jan 17, 2017 [Fan-wiki: Updates]

The main new finding: there is now an **in-game image of the freeze**, from a fan-video thumbnail of Oct 24, 2015 (BBG 2.22). It shows a closed, faceted ice chunk, white on top and translucent teal below. The concept art does not show the target "encased", as earlier rows said. In the concept, a jagged ice mound only catches the target's legs and back.

**Path shorthand.** `FZ/` = `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/combat-vfx/frozen/`. Scripts are in `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/scripts_combat_vfx_frozen/`.

**Sources I could reach:**
- **Fan wiki (MediaWiki API):**
  - Pages: S'no Matter rev 76873, Let It Cold rev 77278, Status Effects rev 76616, Freeze Blast rev 76757, Snowtato Launcher rev 76974, Updates.
  - File metadata: Snomatter.jpg (Maniacbird, 2015-02-15); Snomatterconcpetar.jpg (Thecheeselover, 2015-03-29, description "S'no Matter concept Art"); Letitcold.jpeg (Thecheeselover, 2017-01-18).
  - I re-downloaded these images fresh.
- **YouTube thumbnails** (i.ytimg.com):
  - all sizes of the three cited videos
  - seven more candidates from twelve new searches
  - dates and descriptions from the youtubei `next` endpoint
- **Already-saved files:** the Steam screenshots and the Steam trailer frames.

**Sources I could not reach:**
- YouTube playback and storyboards: LOGIN_REQUIRED / "Sign in to confirm you're not a bot" on five clients. Watch pages redirect to google.com/sorry. I watched no video.
- web.archive.org: about 15 connection resets across curl attempts, plus WebFetch refused. So no archived SkyVu 2.15 or 2.26 notes or forum posts.

**Official text.** No SkyVu-authored text that describes the freeze visual was found [Unverified]:
- The Steam appdetails text (app 4408320) has no "freeze", "frozen", "ice", "snow" or "cold" [Observed: API text grep].
- Previously saved battlebears.com pages have no freeze text [Observed: grep].

## Frozen status: what a frozen target looks like (shared by S'no Matter and Let It Cold; BBG 2.15+; 2026 unverified)

- **Official text:**
  - "It S'no Matter how fast you can move, I can just freeze you! " [Game text via wiki] (S'no Matter, rev 76873)
  - "Your enemies won't have a skull or bones after being hit with ice cold rockets! These rockets explode on impact and freezes the opponent for a small duration" [Game text via wiki] (Let It Cold, rev 77278)
  - Neither quote describes the look.

- **Look, in game: one low-res still.** Source: SW, "EVERYBODY FREEZE!!!(SNO-MATTER GAMEPLAY) - Battle Bears Gold 2.22" (uBXgVYop_-0), uploaded Oct 24, 2015, 4:11 [Observed: youtubei metadata].
  - **The ice chunk:** in its maxresdefault (1152×720), a single irregular, faceted ice chunk stands on the concrete floor [Observed: FZ/yt/uBXgVYop_-0_maxresdefault.jpg; zooms FZ/crops/uBX_max_ice.png, FZ/crops/uBX_720_floor.png].
  - **Upper half:** opaque, crumpled white facets with pale lavender-grey shading. Sampled: highlight #F8F6FB / #F9F7FC, mid-tone #C0BBC6 / #C1BBC7 [Observed: sampled from maxres and hq720; video compression makes these approximate].
  - **Lower half:** translucent teal glass with sharp triangular facets. Sampled: mid-tone #287D7B (#287976 in hq720), lighter facets #52949D–#60B2A9, highlights #8DB2BE / #88AFBB, deepest shadow #0F4B54 [Observed: sampled].
  - **Inside:** a dim bluish-white vertical shape and a short horizontal green bar show through the lower ice [Observed].
    - That the shape is the frozen player is [Inference]. Support: the video title, the S'no Matter icon in the shooter's HUD, and the wiki's freeze mechanic.
    - That the green bar is that player's health or name bar is [Inference].
  - **Overhead icon:** none is visible above the chunk at this resolution [Observed].
  - **Shape and size:** the chunk is about as wide as it is tall (about 145 × 140 px in the 1152×720 frame) [Observed measurement]. That it is sized to swallow one bear is [Inference].
  - **Setting:** the Skate or Die map, with the giant blue ABBi camera lens at the left and the rainbow-and-skull ledge behind [Observed; map identification is Inference from our Skate or Die map notes].
  - **Floor glows nearby:** four small upright dark shards, each with a white or blue edge highlight, stand in glowing blue-violet floor halos (bright #6C6FE3, body #3F374C) [Observed]. What they are is [Unverified]. Possibilities include freeze or explosion debris, gibs, or pickups [Inference].
  - **Which frame this is:**
    - The hqdefault (and the same frame in hq2 and hq720) matches the maxres frame. hqdefault vs hq2 mean pixel difference is 4.7/255, against 43 for hq1 [Observed: computed].
    - So the cover image is YouTube's automatic mid-video frame, about 2:05 [Inference: hq2 is normally the ~50% frame]. Exact timestamp [Unverified].
  - **Not the freeze in this video:**
    - hq1 and hq3 show Tillman holding the red Rocket Propelled Lance with its black-and-white checker band [Observed: FZ/crops/sheet_uBX.png; identified from our Tillman RPL row].
    - The "large pale-cyan glassy mass" in hq1 that an earlier pass flagged is the map's dry concrete bowl painted as pale-aqua water with white foam and pink cartoon decals [Observed: FZ/crops/uBX_hq1_mass.png]. It is not ice [Inference from our Skate or Die notes ("dry concrete bowls painted to look like water") and the trailer's Skate or Die overhead at 46.0–47.0 s, FZ/crops/tr_g2.png].

- **Look, concept** (SkyVu provenance unverified; uploaded by a fan wiki user with no source):
  - At the bottom of "Tillmans S'no Matter", a silhouetted Demo lobs a shot in a long low arc [Observed: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/tillman-verify/img/png_Snomatterconcpetar.png; FZ/img/Snomatterconcpetar_v.png].
  - Where it lands, a jagged ice mound bursts up from the ground, leaning toward the target [Observed: FZ/crops/concept_ice.png]:
    - white, snow-capped peaks (#C5C6C8 to #FBFCFA)
    - a translucent teal body (mid-tone #83C5C9, darkest shadow #0C6970)
    - white speed streaks and snow flecks
  - The silhouetted target bear stands at the mound's right edge, arms flung out, legs and back caught in the ice. Its upper body is outside the ice, so it is **not fully encased** [Observed].
  - **Concept vs in game:** both use the same two-tone scheme, a white cap over a teal body [Observed]. In game, the ice is a closed chunk around the victim; in the concept, it is an erupting mound [Observed].

- **Firing:** see the weapon sections below.
- **Projectile:** see the weapon sections below.

- **Impact / end result:**
  - **S'no Matter:** "The explosion freezes anyone in the blast radius for 2 seconds, leaving them unable to move or rotate the camera. If someone is reloading and gets hit by one of the projectiles, the reload will be restarted after the user is able to move again." [Fan-wiki]
  - Trivia: "This weapon also freezes your teammates. It is unknown whether this is intentional." [Fan-wiki]
  - **Let It Cold:** freeze duration 3 seconds (infobox) [Fan-wiki].
  - The Status Effects page (rev 76616) has **no Frozen entry**, so no overhead icon is documented for it [Fan-wiki, by absence]. It does list Stunned, Slowed and others.
  - How the ice ends (shatter, melt, pop) and any freeze sound: no image or text [Unverified].

- **Images viewed:**
  - **uBXgVYop_-0:**
    - FZ/yt/uBXgVYop_-0_maxresdefault.jpg
    - FZ/yt/uBXgVYop_-0_hq720.jpg
    - FZ/crops/sheet_uBX.png (hqdefault, hq1, hq2, hq3)
    - FZ/crops/uBX_max_ice.png
    - FZ/crops/uBX_720_floor.png
    - FZ/crops/uBX_max_hudicon.png
    - FZ/crops/uBX_max_held.png
    - FZ/crops/uBX_hq1_mass.png
    - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/completeness/frames/yt_uBXgVYop_-0.jpg (a 2×2 composite of the same four thumbnails)
  - **Concept:**
    - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/tillman-verify/img/png_Snomatterconcpetar.png
    - FZ/img/Snomatterconcpetar_v.png
    - FZ/crops/concept_ice.png
  - **Trailer grids:** FZ/crops/tr_g1.png and FZ/crops/tr_g2.png (all 108 frames t_0001–t_0108 at 320×180; no ice chunk is visible at this size [Observed]).
  - **Steam:** FZ/crops/steam_sheet.png (screen_00–04; no ice [Observed]).

- **Depiction for shorts:**
  - On the hit, a faceted ice chunk snaps shut around the victim: a frosted white-lavender cap (#F8F6FB / #C0BBC6) over a clear teal lower half (#287D7B, highlights #8DB2BE), with the victim dimly visible inside, mid-pose [Observed in-game still].
  - Hold it for a two-count after S'no Matter, or three after Let It Cold [Fan-wiki durations]. The victim cannot turn, so sell it with eyes darting inside the ice [BBG News invention built on the Fan-wiki "unable to move or rotate the camera"].
  - Make the thaw a crack into white and teal shards and a puff of snow, with no gore [BBG News invention].
  - A teammate can get frozen too, which is a ready-made gag [Fan-wiki trivia].
- **Confidence:** observed (one low-res 2015 fan-video still; that it shows a frozen player is Inference). The thaw is unknown.

## S'no Matter (Demo primary; added BBG 2.15, Dec 20, 2014; footage Oct 2015; 2026 status unverified)

- **Official text:** "It S'no Matter how fast you can move, I can just freeze you! " [Game text via wiki] (rev 76873)

- **Look:**
  - **Menu render:** Tillman holds, at belly height, a crystalline, ice-encrusted mass so bright that only its shape reads [Observed: FZ/img/Snomatter_v.png from wiki Snomatter.jpg, uploaded 2015-02-15].
    - A dark round muzzle opening faces the viewer at its centre [Observed].
    - Glow: core #FDFEFE, edge #CCFCFD, falloff to #5C9B98 [Observed: sampled].
  - **In-game HUD icon:** a grey metal body with a crest of pale ice shards along the top, round glossy cyan gems (one large orb on top, smaller ones in hexagonal mounts on the side), and a red cloth wrap at the rear [Observed: FZ/crops/wyh_max_hud.png from wyhDD9PVKyY maxres, Jan 2017; also FZ/crops/uBX_max_hudicon.png, Oct 2015].
    - Mirrored, this icon matches the concept sheet's **second (grey, studded, plain red wrap) variant**, not the red-tartan first variant [Observed side-by-side: FZ/crops/cmp_conceptB_vs_hud.png]. That the in-game model follows variant B is [Inference from a low-res icon].
  - **First person:** the held launcher shows as a white-and-cyan shape with a cyan-white bloom at the muzzle [Observed: FZ/crops/uBX_max_held.png; FZ/crops/wyh_max_held.png; FZ/crops/kRB_max_held.png]. Whether the bloom is constant or a firing flash is [Unverified].
  - **Size:** carried two-handed at belly height, about as wide as Tillman's torso (Tillman ≈ 0.9× Oliver on the BBG News chart) [Inference from the render].

- **Firing:**
  - "fires a slow moving gray projectile at a straight trajectory"; projectile speed 800 u/s; rate of fire 2 s; ammo 3; reload 4.5 s; −10% movement speed [Fan-wiki].
  - The concept sketch lobs the shot in an arc instead [Observed concept]. This conflicts with the wiki.
  - The wiki says it "pairs well with... Rocket Propelled Lance" [Fan-wiki]. Uploader Gim Ho Games says "Sno matter is a fun weapon to use, especially how you can combine it with the rpg and shoot your own teammates" [fan comment, kRBhGYrQQ2U, Oct 10, 2015]. Two fan videos show the RPL as the paired secondary [Observed: kRBhGYrQQ2U hq3; uBXgVYop_-0 hq1/hq3].
  - Sound: undocumented [Unverified].

- **Projectile:**
  - In kRBhGYrQQ2U's maxresdefault, a small, soft-edged white glowing orb (#F0F2F5, edge #FAFBFB) flies over a grassy map, with no visible trail [Observed: FZ/crops/kRB_max_proj.png, FZ/crops/kRB_orb_tight.png].
  - At that moment the HUD ammo reads 2, against 3/3 in hq1 [Observed]. That the orb is a just-fired S'no Matter shot is [Inference].
  - The wiki calls it "gray" [Fan-wiki]. In this still it reads near-white [Observed].

- **Impact / end result:**
  - It "explodes on contact with any surface, players included", freezing everyone in the blast for 2 s, teammates included [Fan-wiki].
  - Explosives 25–40; AoE "Max Dmg 100.0, Min Dmg 200.0", probably inner and outer radii [Fan-wiki; radius reading is Inference].
  - The frozen result is the white-and-teal ice chunk above [Observed]. The look of the explosion itself is [Unverified].

- **Images viewed:**
  - FZ/img/Snomatter_v.png
  - FZ/crops/wyh_max_hud.png
  - FZ/crops/uBX_max_hudicon.png
  - FZ/crops/cmp_conceptB_vs_hud.png
  - FZ/crops/sheet_kRB.png
  - FZ/crops/kRB_max_proj.png
  - FZ/crops/kRB_orb_tight.png
  - FZ/crops/kRB_max_held.png
  - FZ/crops/kRB_max_hud.png (too blurry to read)
  - FZ/crops/kRB_hq1_box.png: a green translucent box with lightning around a player. It is not ice; unidentified [Observed].
  - FZ/crops/uBX_max_held.png
  - FZ/crops/wyh_max_held.png

- **Depiction for shorts:**
  - Tillman hefts a grey, ice-crested launcher with a red rear wrap and cyan gems [Observed HUD icon]. It fires a slow white orb that flies straight [Fan-wiki: straight; Observed: white orb].
  - The orb bursts into the white-and-teal ice chunk [Observed].
  - Use the lobbed arc only if the short is explicitly a concept-art homage [Observed concept].
- **Confidence:** partial. The look and the freeze are observed. The projectile's identity is Inference. The burst and sound are unknown.

## Let It Cold (Demo secondary; added BBG 2.26, Jan 17, 2017; footage Jan 22, 2017; 2026 status unverified)

- **Official text:** "Your enemies won't have a skull or bones after being hit with ice cold rockets! These rockets explode on impact and freezes the opponent for a small duration" [Game text via wiki] (rev 77278)

- **Look:**
  - A black, horizontally striped bar runs across Tillman's shoulders out to each upper arm. Each end carries two upright blue rockets [Observed: FZ/img/Letitcold_v.png]:
    - body #2663D9
    - deep-blue cone tips #2A2ADB
    - pale mint-green grinning cartoon-face decals with black eyes
    - straw-gold twisted fuse sticks (#ABA660–#F3ECA5) ending in cyan-white ice sparkles (#6EB7BF)
  - **HUD icon:** a single blue rocket with black tail fins [Observed: FZ/crops/wyh_hq3_hud.png, HUD reading 0/4].
  - **Size:** each rocket is about Tillman's head height (≈ 0.25× his body height) [Inference from the render].

- **Firing:**
  - "launchable missiles that rain down on enemies"; rate of fire 0.5 s; ammo 4; reload 4.0 s [Fan-wiki].
  - No image or sound of the launch [Unverified].

- **Projectile:** presumably the blue grinning rockets themselves [Inference]. No in-flight image [Unverified].

- **Impact / end result:**
  - Explosives 20–40; AoE "Max Dmg 150.0, Min Dmg 300.0", larger than S'no Matter's [Fan-wiki].
  - Freeze 3 s [Fan-wiki infobox].
  - No image of its freeze or explosion [Unverified]. That it uses the same ice chunk as S'no Matter is [Inference: same status, same class].
  - The "no skull or bones" line is a joke and must not be drawn literally for 13+ [BBG News rule].

- **Images viewed:**
  - FZ/img/Letitcold_v.png
  - FZ/crops/sheet_wyh.png (maxres and hq1–hq3: "YOU'RE ON TEAM BLUE" spawn shots, no freeze)
  - FZ/crops/wyh_hq3_hud.png
  - FZ/crops/wyh_max_hud.png
  - FZ/crops/wyh_hq3_held.png

- **Depiction for shorts:**
  - The four grinning blue rockets pop off the shoulder bar on gold fuse sticks and rain down [Observed look; Fan-wiki behaviour].
  - Each impact leaves the same white-and-teal ice chunk, held for a three-count. Reusing the chunk is [Inference], and the snowy burst is [BBG News invention].
- **Confidence:** partial. The look is observed. The flight, explosion and freeze are unknown.

## Look-alikes that are not the Frozen ice (do not reuse the ice chunk for these)

- **Freeze Blast** (Heavy/Riggs secondary, BBG 2.12, Oct 2, 2014):
  - Official text: "Blastin you with FREEEZEEEEE!!!" [Game text via wiki].
  - It fires "small blue projectiles in an arc" that "split and form damaging pools on the floor", and enemies in the pools are "slowed down severely" [Fan-wiki].
  - It slows; it does not freeze [Fan-wiki].
- **Snowtato Launcher** (Chub Scout/Wil primary, BBG 2.26):
  - Official text: "A makeshift potato launcher convertor to weapon of frosty devastation. Shoot snowballs that explode and turn them into flakes!" [Game text via wiki].
  - Snow lingers in its area "for several seconds and block[s] any explosives" [Fan-wiki]. No freeze duration is listed [Fan-wiki].
- **Big white domes with cyan lightning arcs:**
  - Seen in SW Tillman videos: 0i1TEJqDxt4 hq3 (Dec 31, 2015, BBG 2.23) and Rjxp848LabU hq2 (Dec 31, 2017, BBG 2.28) [Observed: FZ/crops/s_0i1TEJqDxt4.png, FZ/crops/Rjx_hq2_c.png].
  - A similar dome appears in the Steam trailer at 9.0–10.0 s [Observed: FZ/crops/tr_g1.png].
  - These are explosions, not ice. Which weapon makes them is [Unverified].
- **Painted-water bowls on Skate or Die:** pale aqua with white foam. They can pass for ice in low-res stills (uBXgVYop_-0 hq1) [Observed; Inference].

## Era and status summary

- **S'no Matter:** added BBG 2.15, Dec 20, 2014 [Fan-wiki: Updates]. In fan footage on Oct 7, 10 and 24, 2015 [Observed: titles and dates of dWqxlt0LHjs, kRBhGYrQQ2U, uBXgVYop_-0].
- **Let It Cold:** added BBG 2.26, Jan 17, 2017, alongside Snowtato Launcher and a winter No Bear's Land [Fan-wiki]. In fan footage on Jan 22, 2017 [Observed: wyhDD9PVKyY].
- **Rework or removal:** none recorded [Fan-wiki, by absence].
- **2026 re-release:** no evidence either weapon is in it [Unverified]:
  - absent from the Steam text [Observed]
  - not in the 5 Steam screenshots or the trailer grids either [Observed], but those re-use SkyVu's 2013 footage [Inference, strong; the Space Oddity clip and screen_01 are undated], older than both weapons, so they say nothing about 2026 [Inference]
  - absent from the Oct 16, 2026 Tillman frag movie thumbnails, whose primary icon is a different white launcher [Observed: FZ/crops/s_Pd0VvQ1TBRM.png, FZ/crops/Pd0_hq2_hud.png]
  - absent from the official Aug 16, 2026 playtest-highlights thumbnails [Observed: FZ/crops/s_C7uFxvSZ10c.png]
- **Other candidates checked, no freeze visible:**
  - dWqxlt0LHjs "very annoying snow matter" (Oct 7, 2015): FZ/crops/s_dWqxlt0LHjs.png, FZ/crops/dWq_hq2_c.png
  - E1qNZtzS4IU "Bugs for Battle Bears Gold 2.26 Update" (Jan 19, 2017): FZ/crops/s_E1qNZtzS4IU.png
  - hBN6w4_I1Ng, YFapn1lKcRw, GpvYdh2M0sM, OPqn8iD3nwY (sheets in FZ/crops/; GpvYdh2M0sM is from Dec 2, 2013, before S'no Matter)

## Corrections for the character file

The Tillman character file (/home/user/thallo-site/bbg-news-repo/characters/tillman.md) does not mention S'no Matter, Let It Cold or freezing. Its Weapons bullet (line 54) and Prompt pack (lines 74–78) contain nothing to correct for this topic [Observed: grep]. Adding the two weapons there is optional, not a correction.

The errors are in the weapons-bible rows:

1. **combat-vfx.md, line 576:**
   - Current: "    - the target encased in jagged cyan and white ice crystals"
   - Correction: "    - a jagged ice mound (white caps, translucent teal body) bursting up where the lobbed shot lands; the silhouetted target stands at its right edge with legs and back caught, not fully encased [Observed: concept art; SkyVu provenance unverified]"
   - Evidence: FZ/crops/concept_ice.png.
2. **combat-vfx.md, line 579:**
   - Current: "  - The in-game frozen-state visual is [Unverified]."
   - Correction: "  - In game, the frozen target sits inside a closed, faceted ice chunk with an opaque white-lavender top (#F8F6FB / #C0BBC6) and a translucent teal lower half (#287D7B, highlights #8DB2BE), with a dim figure and a green bar visible inside [Observed: SW, uBXgVYop_-0 maxresdefault, Oct 24 2015, BBG 2.22, low-res; frozen-player identity is Inference]. Let It Cold's freeze has no image [Unverified]."
3. **combat-vfx.md, line 589 (depiction):**
   - Current: "...encase the victim in jagged cyan-and-white ice crystals, as in the concept art [Observed: concept art; in-game look Unverified]..."
   - Correction: show the in-game chunk (white cap, teal body), held 2 s or 3 s [Observed; Fan-wiki]; the thaw is [BBG News invention].
4. **combat-vfx.md, line 906 (open question 8):**
   - Change "the in-game Frozen state" to "how the Frozen ice ends (shatter or melt) and Let It Cold's freeze".
5. **tillman.md (verified):**
   - Line 206 "The concept shows the target encased in a jagged cyan ice block [Observed concept]." → the concept's mound catches only the target's legs and back.
   - Line 207 "No in-game freeze image exists [Unverified]." → cite the uBXgVYop_-0 still.
   - Line 198 → add that the in-game HUD icon matches the grey second variant, not the tartan one [Observed; Inference].
   - Line 402 → "No image of the Let It Cold freeze; the S'no Matter freeze is the white-and-teal chunk [Observed]."
   - Line 404 → reuse the in-game chunk, not the "concept ice block".
   - Line 516 → drop "S'no Matter" from the list of undocumented freezes.
6. **shared.md:**
   - Line 665 "two variants of a launcher wrapped in red tartan cloth" → only the first variant is tartan; the second is grey and studded with a plain red wrap and ice shards, and it matches the in-game HUD icon.
   - Line 672 → add the in-game chunk.
   - Line 842 → partly answered: in game the freeze is a closed chunk, not the concept's mound.
7. **The quick-reference rows in combat-vfx.meta.json, tillman.meta.json and shared.meta.json:** fix the same statements. See soul_corrections.
8. **Completeness gap note:** "hq1 shows a large pale-cyan glassy mass on the ground" → that is the Skate or Die painted-water bowl, not ice [Observed FZ/crops/uBX_hq1_mass.png; Inference from our map notes and trailer 46–47 s].

## Open questions

1. How does the frozen ice end: shatter, melt or pop? Is there a freeze or thaw sound? Answering needs playback of uBXgVYop_-0 (about 2:05) or kRBhGYrQQ2U.
2. Does Let It Cold's 3 s freeze use the same ice chunk? Does the rocket burst look icy?
3. What are the four upright shards in blue-violet floor halos next to the ice in uBXgVYop_-0: freeze debris, gibs or pickups?
4. Is the green bar inside the ice the frozen player's health bar, and does a teammate freeze look different?
5. Is the S'no Matter shot grey (wiki) or near-white (2015 still)? Straight (wiki) or lobbed (concept)?
6. Are S'no Matter and Let It Cold in the Nov 4, 2026 re-release? The JustNubz showcase Demolition chapter (17:44) would answer this but can't be played here.
7. Is "Tillmans S'no Matter" really SkyVu art? It was uploaded by a wiki user with no source.
8. What did the official 2.15 and 2.26 patch notes or forum posts say? Wayback was unreachable today.


---

<!-- gap pass 2 -->
# Combat VFX addendum: Drain Field in play

This addendum fixes one gap in the combat-vfx dossier: the Drain Field part of the "Healing and life drain" section and quickref row 20 ("Drain Field (healing / life drain)"). That row says the impact was "Not seen in play" and describes it as "a dark field". The Drain Field is Sanchez's (Arbiter's) life-drain secondary. The Health pickup and Healing Tent bullets in that section are unchanged.

**Sources reached today (2026-10-18)**
- **Fan wiki (MediaWiki API):**
  - the Drain Field page and all 21 of its revisions (Jan 31, 2015 to Mar 2, 2025)
  - file info for File:Drainfield.jpg and File:Drainfield.png, and both images (WebP, converted to PNG)
  - the Updates page
  - the Speed Field, Cloak Field and Invulnerable Field pages
- **YouTube thumbnails, downloaded fresh:** hqdefault, hq1, hq2, hq3 and maxresdefault for the two videos the sanchez topic cited, xAp9gFMriAU and 5twbNI7iakw.
  - Titles and channel came from oEmbed today.
  - Upload dates came from the watch pages saved on Oct 16 at `dl/sanchez-dossier/yt/watch/`. Today's fresh fetch returned 302/429 (Google "sorry" page).
- **Steam trailer and Steam screenshots:** an automated red-pixel scan of all 108 trailer frames and the 5 Steam screenshots. I viewed the 6 reddest frames.

**What I did not do**
- **I watched no video.** Every YouTube [Observed] tag below means a still thumbnail I opened. hq1, hq2 and hq3 are YouTube's automatic frames from about 25%, 50% and 75% of the runtime [Inference]. hqdefault and maxresdefault of both videos are custom thumbnails made by the uploader: a game frame with title text, the BBG app icon and a Unity logo laid over it [Observed].
- **Not reached: web.archive.org.** A CDX query for 2.16 release-note URLs failed 3 times with backoff ("Connection reset by peer"; proxy: ws_closed_mid_exchange). No SkyVu text about the Drain Field's look was found.
- **Web search:** one search for Drain Field gameplay videos returned only unrelated BB Heroes guides.

**Era:** the Drain Field was added in BBG v2.16 [Fan-wiki: Updates]. Both in-play frames come from videos the uploader titled "Battle Bears Gold 2.25" (Mar and Apr 2016) [oEmbed title]. Whether the Drain Field is in the 2026 re-release is [Unverified].

## Drain Field (secondary, unlock at level 20, 55 Gas; BBG v2.16, Jan 30, 2015; seen in play in 2.25, 2016; 2026 unverified)

- **Official text:** "Toss this sucker at the nearest enemy and watch as his life force is drained from him and transferred to you!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Drain_Field). The page labels it "~Official Battle Bears Gold Description".
  - The quote has been on the page since rev 69093 (Jan 31, 2015). The first revision, rev 69086 ten minutes earlier, carried the Carpet Bomb's text by mistake ("This carpet has been through years of training to prepare for war!") [Fan-wiki revision history].
- **Status:**
  - Added in v2.16 on Jan 30, 2015, alongside Chub Scout's Bow and Arrow [Fan-wiki: Updates].
  - Current infobox: level 20, 55 Gas, damage 25.0/s, healing 25.0 per 1 s, ammo 1, reload 4.5 s, projectile speed 800 u/s [Fan-wiki].
  - From page creation (Jan 31, 2015) the infobox read 35.0/s and 20.0 per 1.5 s. Rev 77118 (Nov 11, 2020, Alphabbr) changed it to 25.0/s and 25.0 per 1 s [Fan-wiki revision history]. The in-game patch behind that change is [Unverified].
  - The 2026 re-release: Steam lists "-ARBITER: Sanchez" and "60+ SECONDARY WEAPONS" [Canon, Steam appdetails 4408320, per the sanchez topic], but names no Drain Field. Its presence in 2026 is [Unverified].
- **Look**
  - **Held (thrown) creature:**
    - The wiki infobox image File:Drainfield.jpg (uploaded 2015-02-15 by Maniacbird, caption "Arbiter with the Drain Field") shows Sanchez in his default camo outfit and red-visored helmet [Observed].
    - In his dark red-black prosthetic hand he holds a glossy orange-brown slug- or fish-shaped creature: mid #B36B44, shadow #A5532B, dark rim #6D2919 [Observed, sampled].
    - It is bulbous at the front, tapers to a tail and has a small dark double-slit mark, like a closed eye or a gill [Observed].
    - It runs off the left edge of the image, and his boots are cut off at the bottom. It is roughly 0.35× his height, and Sanchez is 1.0× on the BBG News scale chart [Inference].
    - The wiki's wording: "the fish-like creature that holds in it's hand" from Feb 1, 2015 (rev 69128). It has said "the leech-like creature" since rev 77698 (Mar 2, 2025) [Fan-wiki revision history].
  - **Concept art:**
    - File:Drainfield.png was uploaded 2015-02-16 by Thecheeselover with the comment "This is concept art for the drain field". It is hand-lettered "Sanchez drain field". SkyVu provenance is [Unverified].
    - The creature is drop-shaped and red-orange (centre #E65D49, light #C67D5E, dark base #511A17) with a hooked, dark-striped tip (#6F241D) [Observed, sampled].
    - It has one white half-lidded eye and a black patch with a strap line across the face, which may be the sunglasses [Observed; the link to the sunglasses is Inference].
    - It is wrapped in white wind rings with up-arrows, next to small black silhouettes of bears holding guns [Observed].
    - The rest of the sheet is greyscale: a dome with a cross and a syringe, a dripping syringe and four health crosses [Observed].
- **Firing**
  - "the Arbiter will toss the leech-like creature that flies in an arc" [Fan-wiki]. It is ammo 1, reload 4.5 s, 800 u/s [Fan-wiki].
  - The HUD ammo box reads "1 / 1" in xAp9gFMriAU hq2 and hq3 [Observed]. The box uses a generic bullet-cluster icon, not a weapon icon. That the 1-ammo weapon shown is the Drain Field is [Inference].
  - Launch effect and sound are [Unverified].
- **Projectile**
  - The leech creature [Fan-wiki]. It was not seen in flight in any image [Unverified].
  - 5twbNI7iakw hq3 shows a brown, open-mouthed creature with red eyes and white fangs next to Sanchez [Observed]. The HUD reads "15 / 15", the primary, so it cannot be attributed to the Drain Field [Unverified].
- **Impact / end result**
  - **Wiki wording (Fan-wiki):**
    - "When it makes contact with any solid surface, a dark field will be formed with bats in it. Any opponent that is in its range will take damage, and their lost health will be transferred to the user. The user will not receive overheal from the Drain Field."
    - Trivia: "the other fields are formed around the user while the Drain Field won't"; "The field formed appears to be a projection of a live creature wearing sunglasses"; "It is possible to gain health when drain field affects an opponent who has a shield. However, the opponent will not take damage."
    - "Dark field" and "bats" date from rev 69128 (Feb 1, 2015, two days after release). "Sunglasses" and "projection" were added in rev 74450 (Feb 27, 2016, Du Poisson) [Fan-wiki revision history].
  - **Observed in play, Mar 24, 2016** (https://i.ytimg.com/vi/xAp9gFMriAU/hq1.jpg, an automatic frame; "THE LIFE STEALER(SANCHEZ DRAIN FIELD GAMEPLAY)- Battle Bears Gold 2.25", SW):
    - **The creature:** a giant deep-red creature head fills most of the frame (#7B2825 below the glasses, lit lower lip #9C3225, mouth gap #512A1C) [Observed, sampled].
    - **Sunglasses:** it wears wide dark-grey sunglasses (lenses #4C4455 and #48444B) with bright white glints (#EEE3F3) [Observed, sampled].
    - **Teeth:** a wide mouth is lined with a ring of white triangular fangs (#F7ECEA) [Observed, sampled].
    - **Size:** a slowed enemy ("PLAYER 11003264", yellow Z icon) stands in front of its mouth. The mouth alone is about 5× that bear's height on screen [Observed]. Perspective makes the real size [Inference], and the field radius is [Unverified].
    - **The bat-like figures:** two small black figures with pointed ears, each with two glowing red eyes (#F50012, #EC002D), sit at the creature's left edge. One is high up and one is low, near Sanchez's gun [Observed, sampled].
      - That these are the wiki's "bats" is [Inference]. Wings are not resolvable at 480×360, and whether they fly is [Unverified].
    - **HUD and holder:** the Bind Gun reads "35 / 40" and Sanchez's magenta-white beam is hitting the slowed target [Observed]. So the field stays up after he switches back to his primary [Inference]. The holder is a black Sanchez skin with glowing red-orange lines holding the cyan Bind Gun [Observed].
    - A "KILL STREAK" banner is on screen [Observed]. Which kill caused it is [Unverified].
  - **Observed in play, Apr 27, 2016** (https://i.ytimg.com/vi/5twbNI7iakw/maxresdefault.jpg; the same frame is in hqdefault; an uploader-made thumbnail over a game frame; "BLINDNESS OF DRAINING ENERGY(DRAIN FIELD & PARASHOOT SANCHEZ GAMEPLAY)- Battle Bears Gold 2.25", SW):
    - The camera is right up against the same red creature (#972A0D, #942D19, lower jaw #9E3621) [Observed, sampled].
    - White triangular teeth (#CDC9B0) line the lower lip [Observed].
    - A grey lens with a white glint (#37423D) sits under two straight dark bars. These are probably the sunglasses' frame and arms seen close up [Observed; reading is Inference].
    - A pale-pink smoky haze (#E77A6D, top #B7786E) rises from the middle of the mouth [Observed]. Whether this is the drain stream is [Unverified].
    - A few small green specks sit near the mouth on the right [Observed]; their meaning is [Unverified].
    - In the upper red, lighter block shapes show faintly, so the projection may be partly see-through [Observed faint]. Translucency is not firmly established [Unverified]: in the Mar 2016 frame the body reads as solid red.
    - The holder is a navy-black armoured bear with a yellow helmet chevron, holding a white-and-grey launcher with a violet glowing cylinder [Observed]. That this is the Parashoot is [Inference, from the title].
  - **Wiki vs frames:** the frames confirm the wiki's sunglasses-wearing creature projection and its bats. They do not support "dark field": in 2.25 the field is red [Observed vs Fan-wiki].
    - "Dark field" was written for the Feb 2015 v2.16 build, and both frames are from 2.25 (2016). A colour change between those builds is undocumented, but it cannot be ruled out [Unverified].
  - **Unseen:** how health visibly moves to Sanchez, any effect on the victims, and how a Drain Field kill looks [Unverified].
  - **Trailer:** the 6 reddest frames of the Steam trailer (2013 footage [Inference, strong]) (t_0001, t_0027, t_0078, t_0080, t_0081, t_0083) show the logo fire, Aztec Attack's red sky with a translucent red horned skull (t_0027) and Marecraft's red flesh interior (t_0078–t_0083), not a Drain Field [Observed]. No official image of the field in play was found.
- **Images viewed** (all under `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/combat-vfx/drain-gap/`):
  - `yt/xAp9gFMriAU_hq1.jpg` (https://i.ytimg.com/vi/xAp9gFMriAU/hq1.jpg)
  - `yt/5twbNI7iakw_maxresdefault.jpg` (https://i.ytimg.com/vi/5twbNI7iakw/maxresdefault.jpg)
  - `crops/sheet_all.png`: hqdefault, hq1, hq2, hq3 and maxresdefault of both xAp9gFMriAU and 5twbNI7iakw
  - crops of xAp9gFMriAU hq1:
    - `crops/xap_hq1_creature_x4.png`
    - `crops/xap_hq1_contrast_x3.png`
    - `crops/xap_hq1_bats_x6.png`
    - `crops/xap_hq1_bat2_x6.png`
    - `crops/xap_hq1_lowerleft_x6.png` (missed the target)
  - `crops/xap_hud_hq2_hq3_hq1_x6.png`
  - crops of 5twbNI7iakw maxresdefault:
    - `crops/5tw_max_inside_x2.png`
    - `crops/5tw_max_rightjaw_x3.png`
    - `crops/5tw_max_top_contrast_x2.png`
  - `img/Drainfield_jpg.png` (https://static.wikia.nocookie.net/battlebears/images/0/07/Drainfield.jpg/revision/latest?cb=20150215092508) and `crops/held_leech_x2.png`
  - `img/Drainfield_png.png` (https://static.wikia.nocookie.net/battlebears/images/d/d3/Drainfield.png/revision/latest?cb=20150216172257) and `crops/concept_creature_x4.png`
  - `crops/trailer_red_candidates.png`: `visuals/trailer/t_0001`, `t_0027`, `t_0078`, `t_0080`, `t_0081` and `t_0083.jpg`
- **Depiction for shorts:**
  - Sanchez lobs the glossy orange-brown leech in a high arc [Fan-wiki arc; Observed look]. It lands and a huge deep-red creature head balloons up out of the floor [BBG News invention for the "balloons up" staging]. The head wears dark-grey shades with white glints and has a ring of white triangular fangs, a pale-pink haze rises from its mouth, and two little black red-eyed bat critters hover at its edges [Observed].
  - Enemies inside give off red-pink sparkle ribbons that stream into Sanchez as he smugly tops up. A splat on landing, flapping bats and the field popping like a soap bubble at the end are all [BBG News invention]. Never show blood.
- **Confidence:** observed (field look, 2016 build); partial overall (throw, flight, heal transfer, kill and duration are unseen).

## Corrections to the combat-vfx dossier itself (out/verified/combat-vfx.md and .meta.json)

1. **Quickref row 20, "look"**
   - Current: "Concept art: a red-striped, horned leech blob (possibly in sunglasses) wrapped in white swirls; a grey dome with cross and syringe icons."
   - Replace with: "Held: a glossy orange-brown leech (#B36B44) in the prosthetic hand [Observed: Drainfield.jpg]. Field in play (2.25, 2016): a giant deep-red creature head (#7B2825–#9E3621) in dark-grey sunglasses (#4C4455) with white glints and a ring of white triangular fangs, with small black red-eyed bat-like figures at its edge [Observed: xAp9gFMriAU hq1; 5twbNI7iakw maxres]. Concept art: a red-orange hooked blob with an eye patch or lens, in white swirl rings [Observed]."
   - Evidence: the frames and samples above.
2. **Quickref row 20, "impact_end_result"**
   - Current: "'a dark field will be formed with bats in it'; the victim's lost health transfers to the user [Fan-wiki]. Not seen in play."
   - Replace with: "Forms where the leech lands. Enemies in range take damage and the user gets their lost health, with no overheal [Fan-wiki]. In play (Mar and Apr 2016) the field is a red, sunglasses-wearing, fanged creature projection with a pale-pink haze in its mouth and black red-eyed bats; it is red, not the wiki's 'dark' [Observed]. Heal and kill visuals are unseen [Unverified]."
3. **Section "Healing and life drain", Drain Field "In play" bullet**
   - Current: "In play: "the Arbiter will toss the leech-like creature that flies in an arc. When it makes contact with any solid surface, a dark field will be formed with bats in it"; "The field formed appears to be a projection of a live creature wearing sunglasses." [Fan-wiki]"
   - Relabel it as the wiki's wording, not "In play", and add the two observed frames as above.
   - Drop "dark field" from any description written in our own voice.
4. **Same section, depiction line**
   - Current: "a lobbed leech creature that splats into a dark bubble full of cartoon bats, with a sunglasses-wearing creature projected in it [Fan-wiki; concept art Observed]."
   - Replace with the depiction above. The field is a red creature projection, not a dark bubble. The bats sit at its edges in the only frame that shows them, so "full of bats" overstates it.
5. **Open question 8 (meta open_questions[7])**
   - Current: "How do the in-game Frozen state, the poison skull icons, the Combat Tech and Arbiter poison clouds, and the Drain Field in play look? Only concept art and menu renders were found."
   - Remove "and the Drain Field in play". The field is now observed, and the remaining unknowns move to the open questions below.
6. **Calibration note.** The gap brief called the projection "translucent". In my viewing it reads as solid red in the Mar 2016 frame and only faintly see-through in the Apr 2016 frame. Keep "translucent" out of firm claims [Unverified].

## Corrections for the character file (bbg-news-repo/characters/sanchez.md)

1. **Weapons/props line**
   - Current: "Fields come from "a command gauntlet on his arm" [Fan-wiki] ([Speed Field][speed])."
   - Correction: narrow this to the Speed, Cloak and Invulnerable Fields. Each of those pages says the orb "appears from a command gauntlet on his arm" (rechecked today). The Drain Field is not an orb from the arm: Sanchez throws a leech that "flies in an arc", and the field forms where it lands ("the other fields are formed around the user while the Drain Field won't") [Fan-wiki].
   - This duplicates sanchez-topic correction 4.
2. **Fighting line**
   - Current: "fields fire from a button on his arm [Fan-wiki] ([Speed Field][speed])."
   - Correction: only the Speed Field page says "To activate it, Sanchez hits a button on his arm" (rechecked today). The Drain Field is thrown [Fan-wiki].
   - This duplicates sanchez-topic correction 5.
3. **Optional addition, not an error.** The Weapons/props line does not mention the Drain Field. If shorts use it, the line could add: "Drain Field: a thrown orange-brown leech that becomes a giant red sunglasses-wearing fanged creature projection with red-eyed bats [Observed, 2016 build]."

## Open questions

See the open_questions field.