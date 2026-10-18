<!-- gap pass 1 -->
# Frozen Pundra: gap addendum (spawns, ring track, icicles, 2026 look and modes, 2.7 blog post)

This addendum covers only the gaps left in the [partial] Frozen Pundra dossier at /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/out/drafts/research_frozen-pundra.md. It does not repeat that dossier's other content.

**Sources reached**
- **SkyVu's official 2.7 preview (Ev5WvMIp1_4).** I opened its full YouTube storyboard: 32 frames, one per second, 320×180. The Invidious record gives an interval of 1000 ms, so frame N is at N seconds. I enlarged and cropped the frames myself. The Invidious API record also gives the title, author, publish date and full description. I did not watch the video.
- **2026 fan playtest recordings, through YouTube storyboards only (one frame every 10 s).**
  - InstableGR, PT2 (lFr8-yHbbzQ): I downloaded the L3 sheets M14–M17 today, at 429×180.
  - Nuke_Dukem, PT3 (EQwloJnrOko): I downloaded the L3 sheets M24–M29 today, at 424×180.
  - InstableGR, final playtest (HKbwq7PolNc): frames already on disk, 429×180.
  - The chapter lists come from YouTube page JSON already on disk.
- **Fan wiki (MediaWiki API, re-fetched today):** Frozen Pundra, Plant the Bomb, Team Battle, Shield and Health Pack.
- **Steam (re-fetched 2026-10-18):** the appdetails API and the news API.
- **SkyVu's official livestream ZMhLVXWT6OY:** a colour scan of all 620 storyboard frames. I did not open the frames one by one.
- **Weapons dossiers:** used as a cross-reference for effects (/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/out/verified/combat-vfx.md and 2026.addendum.md).

**Not reached**
- **SkyVu's 2.7 blog post is still unread [Unverified].**
  - The Wayback availability API on archive.org confirms a capture exists: `http://web.archive.org/web/20140623210724/http://battlebears.com:80/battle-bears-gold-update-2-7-now-available-full-release-notes/` (status 200).
  - Every fetch from web.archive.org and wayback.archive.org was reset in the proxy tunnel. That is about 25 HTTPS attempts over roughly 25 minutes, including a background retry loop. The proxy logs them as `ws_closed_mid_exchange`, a relay failure, not a policy block.
  - WebFetch refuses web.archive.org.
  - The live URL now returns battlebears.com's store 404 page (canonical `https://battlebears.com/404`).
  - archive.ph serves a CAPTCHA.
- **InstableGR's PT3 recording (aujTcdFuxdE):** Invidious returned 500, so I have no storyboard for it.

---

## Official text
- **Preview title:** "BATTLE BEARS GOLD Update 2.7 "Frozen Pundra" Map Preview" [Canon]. Author "BATTLE BEARS", length 31 s, published 2014-01-22 (Unix time 1390348800) [Canon metadata, via the Invidious record at /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/critic/inv/inv_Ev5WvMIp1_4.json].
- **Full description:** "Check out this epic fly through of the new map coming to BATTLE BEARS GOLD in Update 2.7! Are you excited? / Get Battle Bears for iPhone iPad iTouch http://bit.ly/XuhF4R / Get Battle Bears for Android http://bit.ly/YZIDw4 / Get Battle Bears for Windows 8 http://bit.ly/170ulih" [Canon].
- **Text inside the preview** [Observed]:
  - 0:01–0:02: "FROZEN PUNDRA" in white block capitals on black.
  - 0:03: the same title laid over gameplay.
  - 0:25: black.
  - 0:26–0:31: an end card reading "FREE TO PLAY", with the gold bear app icon, "Phone / Tablet / PC" device icons and the "BATTLE BEARS GOLD" logo.
- **Steam store text (re-fetched today):**
  - "Whether you're a Team Battle diehard or prefer the underrated Plant the Bomb, there is plenty of battling to be done." [Canon]
  - "Dominate in Competitive Modes: -Team Deathmatch (TDM) -Free for All (FFA) -Plant the Bomb (PTB)" [Canon]
  - Release date "Nov 4, 2026" [Canon].
  - Frozen Pundra is still not named anywhere in the store text [Canon, checked].
- **Steam post of 2026-10-14:** "The next and final BATTLE BEARS GOLD playtest will take place on Thursday 15th October at 3pm PDT … Headline additions: -Custom keybinds -Jukebox -UI controller support -Lighting improvements -Lots of bug fixes" [Canon].
- **Steam post of 2026-08-19:** "Friday 21st August at 4pm PDT … New Map: Sky World" [Canon].
- **Steam post of 2026-07-28:** "An experimental new gamemode" [Canon].
- **2026 game UI text on this map, seen in fan recordings** [Observed]:
  - "YOU'RE ON TEAM BLUE" over "[D?]E[LIV?]ER THE BOMB TO SCORE POINTS" (HKbwq7PolNc 22:30). The first word is partly hidden; reading it as "DELIVER" is my [Inference].
  - "DEPOSIT ⚡ +225" in the kill feed (HKbwq7PolNc 23:20, 24:00, 25:10, 25:50, 26:40).
  - "BOMB HOLE WARNING" on a sign (25:50).
  - "BLUE TEAM WINS" / "SUBMITTING GAME TO SERVER..." (27:00).
  - "TIGLATHPILESER III WINS!" (EQwloJnrOko 42:40).

## Era and status
- **Added:** v2.7 [Canon: video title]. SkyVu posted the preview on Jan 22, 2014 [Canon metadata]; the wiki dates 2.7 to January 23, 2014 [Fan-wiki]. The Jan 22 date is now verified (see Corrections).
- **2026: played in every playtest build I could sample** [Observed]. No SkyVu text names the map [Canon, checked].

| Playtest | Recording | Mode on Frozen Pundra | Evidence |
|---|---|---|---|
| PT2, Jul 29 2026 | InstableGR, lFr8-yHbbzQ, chapter 21:52–26:03 | Team Battle | Chapter "Match 6 (Team Battle, Frozen Pundra, Saberi/Graham)" [Unverified: fan chapter]. Frames: red-vs-blue score from 0:0 at 22:00 to a "RED TEAM 23 VS 28 BLUE TEAM" scoreboard at 26:00; countdown 2:55 at 23:00, 0:25 at 25:30, 0:05 at 25:50 [Observed]. That fits the wiki's 4-minute Team Battle [Fan-wiki; Inference]. |
| PT3, Aug 21 2026 | InstableGR, aujTcdFuxdE, chapter 16:42 | Team Battle | "Match 5 (Team Battle, Frozen Pundra, B-1000/Botch/Wil)" [Unverified: fan chapter; storyboard unreachable] |
| PT3, Aug 21 2026 | Nuke_Dukem, EQwloJnrOko ("Battle Bears Gold Playtest #3 Full Gameplay", posted Aug 22), about 38:50–42:40 | **Free for All** | The top of the HUD shows one leader's portrait, name and count, not a team score. The countdown falls from 3:00 (≈39:50) to 0:07 (≈42:30). "TIGLATHPILESER III WINS!" at 42:40. Lobby chat at 43:10 reads "VINYLSCRATCH WHY FFA" [Observed]. Not listed in any chapter. |
| Final, Oct 15 2026 | InstableGR, HKbwq7PolNc, chapter 21:52–27:06 | Plant the Bomb | "Match 6 (Plant the Bomb, Frozen Pundra, B-1000/Botch)" [Unverified: fan chapter]. Frames show the bomb prompt, deposits and bomb props; the countdown reads 4:00 at 23:00, 3:00 at 24:00, 2:00 at 25:00, 1:00 at 26:00 and 0:10 at 26:50, then "BLUE TEAM WINS" at 27:00 [Observed]. That fits the wiki's 5-minute Plant the Bomb [Fan-wiki; Inference]. |

- **Deposit reward:** the 2026 "DEPOSIT +225" matches the wiki's "The player making the deposit will be awarded with an extra 225 Joules" [Observed + Fan-wiki].
- **Kill Confirmed:** this mode appears in the 2026 playtests but is not on Steam's list. None of the three chapter lists shows it on Frozen Pundra [Unverified: fan chapters].
- **SkyVu's own 2026 footage:** the colour scan of the official Oct 14–15 livestream (ZMhLVXWT6OY) found no ice-cave frames [Inference: automated scan only]. The tile in "BBG Maps Ranked part 1" is still the only SkyVu-made 2026 image of the map [Observed in the main dossier].
- **"Lighting improvements":** the final build (Oct 15) lists them [Canon]. Its frames use the same cobalt-and-cyan scheme as the July and August builds, and no layout change shows at storyboard resolution [Observed]. What the lighting change did to this map cannot be isolated [Inference].
- **Launch on Nov 4:** inclusion is very likely but undocumented [Inference].

## Setting
- It is still a fully enclosed ice cave in 2026. None of the roughly 60 Frozen Pundra frames I viewed from 2026 shows sky, sun or a horizon [Observed].

## Layout
**SkyVu's preview, one frame per second** [Observed; storyboard frames f_0003000–f_0024000]:
- **0:03:** a high angle over snow with a round, bowl-shaped dip. Three blue lightning-bolt tokens sit at the left; a fight around a pale cyan disc is at the right.
- **0:04–0:06:** the camera sweeps over a broad, banked snow path. Its inner half is lit lavender-pink and its outer half cyan, with a rock wall on the outer side.
  - A rounded raised snow lip runs along the path.
  - A Health Pack (white box, red cross, orange-glowing base) and a blue-glowing base with a white post sit on a higher ledge (0:06).
  - A jump pad (cyan centre, gold rim) is visible at 0:05.
- **0:07:** a narrow, winding snow path between dark rock walls, with two lightning-bolt tokens hovering.
- **0:08–0:10:** a deep-blue-lit stretch. Raised snow ledges with slot-shaped grooves run under banded indigo and cobalt rock and an icicle fringe.
- **0:11–0:13:** a wide snow ramp climbs to a round, snow-capped rock top holding a Health Pack. A **thin snow bridge** runs off from it. Pointed ice stalagmites stand in front, and glassy white crystal masses sit at the right. At 0:13 a large near-white icicle with a blue mark hangs over the bridge.
- **0:15–0:16:** dense blue icicles hang almost to the floor. One tip meets a dark post set in a ring-shaped snow mound, forming the "hourglass" column.
- **0:17–0:18:** floor level, in a snow passage between dark rock supports, **under a raised snow slab**. A jump pad with a yellow-and-black hazard ring, a glowing cyan centre and concentric cyan rings sits in the foreground.
- **0:19:** a white flash. The slab's rounded edge crosses the frame, resting on a squat, snow-capped support.
- **0:20–0:23:** a purple-indigo rock wall over pink-lit snow, where a blast and smoke take place (see Look).
- **0:24:** a large, dark, faceted rock mass under a thick snow cap, partly veiled by smoke, with a thin snow track behind it to the right and a jump pad on the floor. This is the central dome [Observed; that it is the dome is an Inference from the wiki tile].
- The frame rate is too low to tell which shots are continuous camera moves and which are cuts [Observed]. The sequence reads as a pass along the outer ring that ends at the dome [Inference]. The gap note's "fly-through of the whole … ring" overstates what the frames show.

**Ring-track synthesis**
- **Form:** a broad, flat-topped snow "highway" with rounded edges, carried on squat, snow-capped dark-rock supports with open gaps beneath (0:18–0:19) [Observed]. The wiki says "raised above the ground by rocks" [Fan-wiki].
- **Width varies:** wide, banked sweeps (0:04–0:06), plus thin snow bridges between snow-capped rock tops (0:11–0:13; in 2026, HKbwq7PolNc 25:40 and 26:00) [Observed].
- **Perches:** a ramp climbs to a round rock top holding a Health Pack (0:11–0:12) [Observed]. This matches the wiki's "large snow-covered rocks on opposite sides of the map" [Fan-wiki]. The same kind of Health Pack perch appears in 2026 (HKbwq7PolNc 25:40; EQwloJnrOko 41:50) [Observed].
- **Under the ring:** snow passages run at floor level between the supports, with jump pads on the floor (0:17–0:18) [Observed]. In 2026 the pads appear as a gold ring with a teal centre on the snow (lFr8-yHbbzQ 24:10; EQwloJnrOko 40:10; HKbwq7PolNc 24:50) [Observed].
- **Floor:** round, bowl-shaped dips (0:03, 0:13) and pointed ice stalagmite cones (0:11; in 2026, EQwloJnrOko 39:10 and HKbwq7PolNc 25:40) [Observed].
- **Plan:** a ring around a central dome, with pickups mirrored on "opposite sides" [Fan-wiki], so the map is probably a two-sided, symmetric layout [Inference]. The ring's diameter and the number of bridges and ramps are [Unverified].

**Spawn sides: still undocumented** [Unverified]
- **Red, 2014:** in the fan frame 1HxwjhH-Qao hq1 ("YOU'RE ON TEAM RED"), the player is at floor level and the raised track crosses the view at about head height, with the snow-capped dome beyond [Observed]. So the red spawn is on the floor outside the ring, facing inward [Inference].
- **Blue, 2026:** the "YOU'RE ON TEAM BLUE" frames (HKbwq7PolNc 22:30; lFr8-yHbbzQ 23:30) are both at floor level among cobalt rock and cyan snow. Neither shows a landmark that fixes the spawn's position [Observed].
- **Withdrawn:** the main dossier's "blue-glowing figures … probably the opposing spawn groups" (iy_MND-ch1s hq1, which is the preview's 0:03 frame). They are **three blue lightning-bolt tokens on dark hexagonal bases**, not figures [Observed: crop c_iy_tokens.png]. That frame says nothing about spawns.
- Which compass side is red and which is blue remains [Unverified]. Mirrored pickups suggest the two spawns sit on opposite sides of the ring [Inference].

## Look
- **2014 palette** (sampled from the preview's storyboard frames) [Observed]:
  - pink-lit snow #92667F to #A7738A
  - cyan snow #61B2D0 to #7AC7E5
  - slate-indigo rock #1F2B55 (lit faces #4E4D75)
  - highlights on the pale icicles up to #C1F8FF
  - jump-pad cyan #0AD5CF to #66E5D0
- **2026 palette** (all three playtests): brighter and more saturated [Observed; sampled]:
  - snow floor #49DFFA (range #43C5F7 to #54F2FB)
  - rock walls and pillars a deep cobalt, #16317E / #1B3679 (shadows #0A173A, lit faces #2C57BF to #3578BC), with horizontal banding
  - icicles #1171BE to #2085DE in shade, up to #47E1FD
  - A **mauve-plum zone persists** (EQwloJnrOko 40:30: #4A3757, #46507C, #271821).
  - The 2026 rock reads cobalt blue rather than 2014's slate-indigo and purple [Observed]. The lavender snow in the Maps Ranked tile is therefore probably that mauve zone or video grading, not a map-wide relight [Inference].
- **Lighting and weather:** flat, bright and without a visible source. There is no sky, and no falling snow or weather particles in any frame I viewed from 2014 or 2026 [Observed].
- **Things that are not set dressing** (keep them out of establishing shots):
  - **Pale-yellow translucent faceted shapes** (2014 at 0:20–0:22; 2026 at lFr8-yHbbzQ 24:00 and 25:00, EQwloJnrOko 40:20 and 42:20–42:30) [Observed]. They match the 2026 blast style, which I confirmed on https://i.ytimg.com/vi/EQwloJnrOko/maxres3.jpg (a Skate or Die frame) [Observed]. So they are explosions [Inference].
  - **The grey translucent faceted cloud** at 0:22–0:24 is faceted smoke after that blast [Inference; combat-vfx.md records "faceted white and grey puffs after big blasts"].
  - **Blue lightning-bolt badges on dark hexagons** (0:03, 0:07; 2026 at lFr8-yHbbzQ 24:50 and EQwloJnrOko 42:00 and 42:40) are match tokens [Observed]. Their function is [Unverified].
  - **Green "+" shields around a player** are pickup or respawn protection: "four green shields", "When the player respawns, they have the shields for 4.5 seconds" [Fan-wiki].
- **2026 Plant the Bomb props on this map** [Observed, HKbwq7PolNc]:
  - **The blue bomb:** a round, saturated-blue cartoon bomb (core about #0800E9) with a grey fuse cap. It is carried overhead with the fuse spitting orange sparks (22:40, 24:10, 25:20, 26:00).
  - **The bomb device:** a round pedestal under a near-white light column (about #FEF8F8), framed by two hinged, dark green-black armour panels (#0E1714 to #24564B) studded with small yellow-green lights that open like a clamshell (24:20, 25:00, 26:20, 26:30). The blue bomb hovers in the beam (24:20).
    - Whether this is the blue team's bomb platform or the red team's tube is [Unverified]. The wiki says "Each bomb starts on a bomb platform in the same color as the bomb itself" [Fan-wiki], so I read it as the blue bomb's platform [Inference].
  - **The sign:** a white rectangle with a red border and a round bomb pictogram, lettered "BOMB HOLE WARNING". It stands on a post on a red square base beside a red upright pipe (22:40; 25:50).
  - **HUD only, not a prop:** a red digital countdown box appears top right while the bomb is carried, probably the bomb timer [Inference].

## Landmarks (additions to the main dossier)
1. **The snow-capped central dome**, now seen in SkyVu's own preview (0:24) [Observed].
2. **The raised snow "highway"** on rock supports, with thin snow bridges and a ramp up to a Health Pack perch [Observed + Fan-wiki].
3. **The under-track floor passages** with jump pads [Observed: 0:17–0:18; 2026].
4. **Icicle fringes plus larger near-white icicles** with a blue mark (0:13, 0:22–0:24) [Observed].
5. **2026 Plant the Bomb only:** the clamshell bomb hatch with its light column, and the red-based "warning" sign beside a red pipe [Observed].

## Hazards and interactive elements: icicle behaviour
- **The wiki is still the only source:**
  - "some large lightly-coloured icicles can drop from the ceiling and deal damage to players below if they are dealt enough damage. However, due to the fact that they can take several seconds to drop, do not deal significant damage and each have a small area of effect, using these icicles in direct combat is not a recommended strategy." [Fan-wiki]
  - "Firing at the icicles causes them to fall off and disappear on contact with the floor." [Fan-wiki]
- **What the droppable icicles probably look like:** the larger near-white icicles with a blue mark (0:13; 0:22 top centre; 0:23 right edge) [Observed look]. That these are the droppable ones is [Inference].
- **No falling icicle seen.** No frame in the 1-per-second preview or the 10-second 2026 storyboards shows an icicle detaching, falling or breaking [Observed]. That sampling is too coarse to rule it out.
- **Correction to the gap note:** the "shattering burst at 0:22–0:24" is a pale-yellow faceted blast (0:20–0:22) followed by grey faceted smoke. The near-white icicles above it are still attached in both frames [Observed: c22.png, ev_20_23.jpg]. It is not evidence of an icicle falling [Inference].
- **Still unknown:** how many icicles there are, whether they respawn, their damage values, and whether the mechanic survives in 2026 [Unverified].
- **Other interactive elements:**
  - Jump pads [Observed].
  - A jump pad leads to the Bearscream Sandwich inside the dome [Fan-wiki].
  - In 2026, the Plant the Bomb deposit gives +225 [Observed].
  - No suicide pit is visible in any frame [Observed]. Whether the map has one is [Unverified].

## Easter eggs and references
- **The snowman:** the wiki has "There is a small snowman outside of the circular track." [Fan-wiki].
  - The preview shows a small, white, rounded figure at the outer edge of the snow against the rock wall (0:04 top centre, 0:05 top left, 0:06 left; hq1) [Observed].
  - At 320 px I cannot tell a snowman from a small character, so calling it the snowman is a low-to-medium [Inference].
- **A fish-shaped object:** a dark-teal object with a black scale-tile pattern and a tail-fin outline lies on the snow (0:06 / hq1), and a similar dark shape appears on the snow at 0:05 [Observed].
  - Reading it as a frozen-fish prop is a low [Inference]. Nothing documents it [Unverified].

## Sound and music
- The 2026 final build adds a Jukebox [Canon].
- In the Jukebox frames of HKbwq7PolNc (75:10–76:40), the visible track names are "Menu Theme - BBG", "Menu Theme - BBR", "Bear With Me", "The Right to Bear Arms", "Tentacles!", "I'm a Battle Bear (Sleepy Mix)" and "Jungle Theme" [Observed]. The other rows show challenge names (e.g. "Get 50 Kills with Huggable") with "?" icons instead of tracks; reading those as locked tracks is my [Inference].
- None of the visible names is a Frozen Pundra track [Observed]. The map track's Jukebox title is [Unverified].

## Images viewed
Every file below was opened with the Read tool.
- SkyVu's 2.7 preview storyboard:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/critic/fp_prev.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/critic/sb/Ev5WvMIp1_4/cs_00.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/critic/sb/Ev5WvMIp1_4/cs_01.jpg
- Enlargements of storyboard frames f_0003000 to f_0024000:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/ev_03_06.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/ev_07_10.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/ev_11_14.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/ev_15_18.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/ev_19_24.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/ev_20_23.jpg
- Crops:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/c21.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/c22.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/c24.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/c05_fig.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/c06_fig.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/c_hq1_items.png (from /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra/yt/Ev5_hq1.jpg)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/c_iy_tokens.png (from /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra/yt3/iy_MND-ch1s_hq1.jpg)
- 2014 references:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra/yt3/z2_iy_MND-ch1s_hq1.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra/yt3/z2_1HxwjhH-Qao_hq1.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra/Pundra_map_x4.png
- PT3, Nuke_Dukem (EQwloJnrOko):
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/critic/eq_fp_syb2.jpg
  - Contact sheets of frames split from https://i.ytimg.com/sb/EQwloJnrOko/storyboard3_L3/M24.jpg to M29.jpg:
    - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/eq_l3/g_a.png
    - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/eq_l3/g_b.png
    - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/eq_l3/g_c.png
    - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/eq_l3/g_d.png
  - Enlargements:
    - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/eq_chat_4310.png
    - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/eq_win_4240.png
    - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/eq_more.jpg
    - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/ice26.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/thumbs/EQ_maxres3.jpg (https://i.ytimg.com/vi/EQwloJnrOko/maxres3.jpg, a Skate or Die frame used only for the blast style)
- Final playtest, InstableGR (HKbwq7PolNc): frames from /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/gold_digger_verify/yt/sb/HKbwq7PolNc/f_1260000.jpg to f_1680000.jpg and f_4490000.jpg to f_4640000.jpg, viewed as:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/hk_a.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/hk_b.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/hk_c.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/hk_d.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/hk_2200_2230.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/hk_2230_txt.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/hk_2240.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/hk_2550.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/hk_ptb_props.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/hk_jukebox.png
- PT2, InstableGR (lFr8-yHbbzQ), from https://i.ytimg.com/sb/lFr8-yHbbzQ/storyboard3_L3/M14.jpg to M17.jpg:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/pt2/pt2_a.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/pt2/pt2_b.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/frozen_pundra_gap/pt2_spawn.jpg
- Scanned by colour but not opened: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/gold_digger_verify/yt/sb/ZMhLVXWT6OY/f_*.jpg (620 frames).

## Prompt pack (updated)
**Establishing shot, 2026 look, 9:16, environment only** (style-neutral; append the house-style suffix):
Vertical 9:16 establishing shot inside a fully enclosed ice cave, from a raised three-quarter angle [BBG News invention: camera].
- **Centre:** a squat block of dark faceted rock under a thick, rounded, overhanging snow cap.
- **Track:** a broad, flat-topped snow highway with rounded edges circles it at about head height. It rests on squat, snow-capped rock supports with open gaps beneath. On one side it narrows into a thin snow bridge that runs to a round, snow-capped rock perch.
- **Under the track, at floor level:** a round launch pad with a yellow-and-black striped rim and a glowing cyan centre.
- **Walls:** deep cobalt-blue faceted rock with horizontal banding (about #16317E; shadows #0A173A; lit faces #2C57BF).
- **Ceiling:** rippled ice hung with dense fringes of translucent blue icicles (about #1171BE to #47E1FD). Some reach almost to the floor and meet dark posts set in ring-shaped snow mounds. A few larger near-white icicles each carry a small blue mark.
- **Floor:** smooth, bright, saturated cyan snow (about #49DFFA, highlights #54F2FB) with round bowl-shaped dips and pointed ice stalagmite cones. One side of the cave is washed in dim mauve-plum light (about #4A3757).
- **Lighting:** flat, bright and sourceless. No sky, no sun, no falling snow.
- No characters, no text, no logos, no UI, no explosions.
- Everything above is [Observed], except the camera and the exact composition [BBG News invention].

**2014 variant:**
- Slate-indigo rock (about #1F2B55, lit #4E4D75).
- Softer cyan snow (#61B2D0 to #7AC7E5) with lavender-pink lit patches (#92667F to #A7738A).
- Pale icicle highlights up to #C1F8FF [Observed].

**Staging spots**
1. **Under-track launch.** At floor level between two rock supports under the snow highway, a bear steps on the striped jump pad and is flung up past the slab edge. The pad's position is [Observed: 0:17–0:18]; the action is [BBG News invention].
2. **Bridge to the medkit.** A chase or standoff on the thin snow bridge to the round rock perch with the Health Pack, under icicles. The bridge and perch are [Observed: 0:11–0:13; HKbwq7PolNc 25:40]; the blocking is [BBG News invention].
3. **Plant the Bomb heist (2026).** The clamshell hatch opens and a blue cartoon bomb rises on a white light column. A bear grabs it, fuse sparking overhead, and runs for the red-based warning sign by the red pipe; render the sign blank, with no readable text. The props are [Observed]; the route and gag are [BBG News invention].
4. **Slow icicle gag.** Someone shoots a near-white icicle with a blue mark. Seconds later it drops on a passer-by for a small bonk and vanishes on the floor. The delay, low damage and vanishing are [Fan-wiki]; any shatter effect is [BBG News invention].

Use the pale-yellow faceted blasts, grey faceted smoke and bolt tokens only as action effects, never as set dressing.

## Confidence
**partial** (up from the main dossier).
- **Observed:** the ring and track structure, the 2026 look and three 2026 modes, all at low resolution.
- **Documented only by the fan wiki:** the icicle behaviour.
- **Unknown:** the spawn compass sides, the Plant the Bomb device roles, and the 2.7 blog text.

---

## Corrections to our notes
1. **/home/user/thallo-site/research_notes/Battle Bears character lore/animation_reference.md, Q1 §A, "Map fly-throughs" (line 81). Applied: the entry now reads as the correction below.**
   - Text at the time: `  - "2.7 'Frozen Pundra'" (Jan 22, 2014) — [Ev5WvMIp1_4](https://www.youtube.com/watch?v=Ev5WvMIp1_4)`
   - Correction: `  - "BATTLE BEARS GOLD Update 2.7 "Frozen Pundra" Map Preview" (Jan 22, 2014, 0:31): "Check out this epic fly through of the new map coming to BATTLE BEARS GOLD in Update 2.7! Are you excited?" — [Ev5WvMIp1_4](...)`. The Jan 22 date is now verified. This replaces the main dossier's advice to mark it "not re-verified".
   - Evidence: the Invidious record at /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/critic/inv/inv_Ev5WvMIp1_4.json (author "BATTLE BEARS", published 1390348800 = 2014-01-22, lengthSeconds 31, full description).
2. **/home/user/thallo-site/research_notes/Battle Bears character lore/franchise_world.md, line 216.**
   - Current: `Desert Airmine, Frozen Pundra, plus Steam Yard Blues (v2.8)`
   - Correction: `Desert Airmine, Frozen Pundra (v2.7; SkyVu preview Jan 22, 2014; wiki date Jan 23, 2014), plus Steam Yard Blues (v2.8)`. Optionally add that it was played in the 2026 playtests (Team Battle in PT2, Free for All in PT3, Plant the Bomb in the final playtest).
   - Evidence: the official video title and date above; wiki Updates 2.7 row; the frames listed in this addendum.
3. **Main dossier, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/out/drafts/research_frozen-pundra.md, line 31.**
   - Current: "Our notes date the video upload to Jan 22, 2014, which I could not re-check; YouTube shows "12y ago" [Unverified]."
   - Correction: "SkyVu posted the preview on Jan 22, 2014 [Canon metadata]."
   - Evidence: the same Invidious record.
4. **Main dossier, line 43** (and line 46).
   - Current: "**2026 status:** probably in the 16-map roster, but no SkyVu text confirms it." and "Which of them run on Frozen Pundra is [Unverified]."
   - Correction: "It was played in the 2026 playtest builds: Team Battle (PT2, Jul 29), Free for All (PT3, Aug 21) and Plant the Bomb (final playtest, Oct 15) [Observed in fan recordings]. No SkyVu text names it."
   - Evidence: lFr8-yHbbzQ 22:00–26:00; EQwloJnrOko 39:00–43:10; HKbwq7PolNc 22:00–27:00.
5. **Main dossier, line 77.**
   - Current: "a high-angle frame shows blue-glowing figures at the left and red-armoured figures around a pale cyan disc at the right [Observed, iy_MND-ch1s hq1]. These are probably the opposing spawn groups [Inference]."
   - Correction: "The blue items at the left are three blue lightning-bolt tokens on dark hexagonal bases, not figures (this is the preview's 0:03 frame). Drop the spawn-group inference."
   - Evidence: the crop c_iy_tokens.png and the preview's 0:03 storyboard frame.
6. **Main dossier, line 47.**
   - Current: "The 2026 tile shows lavender snow and a plum-brown rock block … That could be new lighting, a different camera area or video grading [Inference]."
   - Correction: "2026 gameplay shows saturated cyan snow (about #49DFFA) and cobalt rock (about #16317E) across the map, with a mauve-lit zone (about #4A3757) still present. The tile's lavender is probably that zone or grading, not a map-wide relight."
   - Evidence: colours sampled from HKbwq7PolNc 22:00 and 25:40 and EQwloJnrOko 39:10 and 40:30.
7. **Main dossier, line 114.**
   - Current: "a dark-teal faceted chunk with black outlines lying on the snow (Ev5WvMIp1_4 hq1)"
   - Correction: "a dark-teal, fish-shaped object with a black scale-tile pattern and a tail-fin outline (hq1 = storyboard 0:06). Identity unverified; a frozen-fish prop is one possible reading."
   - Evidence: c_hq1_items.png.
8. **Gap note for frozen-pundra (a workflow note, not a file).**
   - Current: "a fly-through of the whole snow ring track … a shattering burst at 0:22-0:24"
   - Correction: "a fly-through of several stretches of the outer ring (cuts cannot be ruled out at 1 frame per second) ending at the snow-capped dome (0:24). 0:20–0:24 shows a pale-yellow faceted blast and then grey faceted smoke; the near-white icicles above it stay attached, so it is not an icicle falling."
   - Evidence: ev_20_23.jpg, c21.png, c22.png, c24.png.

## Open questions
- What does SkyVu's 2.7 blog post say? A capture exists at https://web.archive.org/web/20140623210724/http://battlebears.com:80/battle-bears-gold-update-2-7-now-available-full-release-notes/; retry when web.archive.org is reachable through the proxy.
- Where are the red and blue spawns, by compass side? A minimap, a top-down image or a full-speed video is needed.
- Do the droppable icicles still exist in 2026, how many are there, and do they respawn?
- In 2026 Plant the Bomb, is the clamshell hatch the blue bomb platform or the red tube? Is the red pipe by the "BOMB HOLE WARNING" sign the bomb hole, and where does each sit relative to the spawns?
- Is the small white figure in the preview the wiki's snowman? What is the fish-shaped object?
- Which modes will the map run at the Nov 4 launch? Is Kill Confirmed among them?
- What is the Frozen Pundra track called in the 2026 Jukebox?
