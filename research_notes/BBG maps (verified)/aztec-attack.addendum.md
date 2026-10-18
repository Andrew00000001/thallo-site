<!-- gap pass 1 -->
# Aztec Attack: addendum on 2026 playtest modes and temple interiors

This addendum answers two gaps in the Aztec Attack draft:

1. Which modes Aztec Attack ran in during the 2026 playtests.
2. A 2026 frame from inside a temple, to test the wiki's claim of Over Clocked Oliver (OCO) and Astoria symbols at the spawns.

**How I worked**
- I never played a video. I fetched YouTube **storyboard sprite sheets** (the scrub-bar preview thumbnails) through the Invidious API (invidious.f5.si, after 10 retries), sliced them into frames and opened them with Read.
  - Frames are 320–429 px wide and sampled every 10 s, so all times are ±10 s.
  - A file named f_N.jpg is the frame at N milliseconds.
- I also opened storyboards that earlier sessions had already saved: InstableGR playtest #2, the official livestreams, and fan uploads from playtests #4 and #5.
- I wrote a colour scanner (magenta sky plus lava or orange sand) and ran it over 45 playtest-era storyboards to find Aztec segments I had not been pointed to. I checked every hit by eye.

**Sources reached**
- Steam store API and Steam news API for app 4408320, re-fetched 2026-10-18.
- The fan wiki through the MediaWiki API: Aztec Attack with its full revision history, Over Clocked Oliver, Plant the Bomb, and a search for Kill Confirmed (no page exists).
- Invidious metadata and storyboards for aujTcdFuxdE, qt43iTdANbM and uNZA3nlABOA (new), plus storyboards already on disk.
- YouTube thumbnails (i.ytimg.com).

A note on display: some sheets I built would not display at first (the viewer hit a request limit). I re-opened every sheet these findings depend on. Only images that actually displayed are listed under "Images viewed", and no claim rests on any other image.

**Path shorthand.** `$AA` = /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/aztec-attack-gap. Folders of storyboard frames from other sessions are written out in full where they are cited.

---

## 1. The 2026 playtest calendar (official)

- **PT1.** Steam news, 2026-07-06: "The first **BATTLE BEARS GOLD playtest** will take place this **Thursday** at **4pm PDT**" and "There won't be any new features in this build" [Canon]. That Thursday is Jul 9, 2026 [Inference: calendar].
- **PT2.** Steam news, 2026-07-28, "2nd Discord Playtest Tomorrow! Trial a new gamemode!" [Canon].
  - It says the test "will take place this **Wednesday** at **4pm PDT**" and lists "An experimental new gamemode" [Canon].
  - The same post also ends "See you on the Battlefield this Thursday!" [Canon]. The post contradicts itself on the day.
  - Fan uploads date the session Jul 29, 2026, a Wednesday [Fan description; Inference: calendar].
- **PT3.** Steam news, 2026-08-19, "3rd Discord Playtest this Friday! A New Map comes to BBG!" [Canon].
  - Date: "Friday 21st August at 4pm PDT" [Canon].
  - "This version contains:" "Auto matchmaking", "New Map: Sky World", "Bug fixes" [Canon].
- **PT4.** Steam news, 2026-09-19, "4rd Discord Playtest this Sunday Sep 20" [Canon; "4rd" is SkyVu's spelling].
- **PT5.** Steam news, 2026-10-14, "Final Discord Playtest this Thursday Oct 15" [Canon]. Its headline additions include "-Lighting improvements" [Canon].
- **Store mode list.** The Steam store text, re-fetched 2026-10-18, lists "Dominate in Competitive Modes: -Team Deathmatch (TDM) -Free for All (FFA) -Plant the Bomb (PTB)" [Canon].
  - It does **not** name Kill Confirmed [Observed: appdetails JSON].
  - The same text says "Whether you're a Team Battle diehard or prefer the underrated Plant the Bomb" [Canon]. So SkyVu's store copy uses "Team Battle" and "Team Deathmatch" for the same mode [Inference, strong].
- **Kill Confirmed's name** is not in any SkyVu text I found [Unverified as an official name].
  - Fan chapter titles call the PT2 "experimental new gamemode" "Kill Confirmed" [Fan description].
  - The in-game prompt reads "COLLECT ENEMY TAGS TO SCORE POINTS" under "YOU'RE ON TEAM BLUE" [Observed: https://i.ytimg.com/vi/1MP1rFi4t-Q/maxres1.jpg, JustNubz's final playtest, not on Aztec; build stamp "3.0.7_…"].
  - The wiki has no Kill Confirmed page (API: "missingtitle") [Observed].

## 2. Which modes Aztec Attack ran in during the 2026 playtests

### How I identified the mode from frames
- **Kill Confirmed (KC).**
  - The kill feed shows **SCORED** and **DENIED** entries with tag-shaped icons [Observed in the chaptered KC match].
  - The red/blue team score does not equal the team's kill total [Observed numbers]. Reading that as "points come from tags" is [Inference].
- **Plant the Bomb (PTB).**
  - The wiki says "Matches in this mode last 5 minutes instead of 4 minutes as in Team Battle" and "The stages feature a bomb in each team's color and a bomb tube in each team's color" [Fan-wiki: Plant the Bomb].
  - In every Aztec match I clocked, 5-minute rounds go with bomb props. 4-minute rounds do not [Observed].
- **Free-for-All (FFA).** The top HUD shows one leader's score, avatar and name instead of red/blue team scores [Observed]. A "<NAME> WINS!" banner confirms it [Observed in M1kaa717's video].
- **Team Battle (TDM).** Red/blue score, a 4-minute clock, "RED TEAM WINS", and a feed with only KILLS, SUICIDE and ASSIST entries [Observed]. Calling that Team Battle rather than KC is [Inference].

### Aztec Attack matches found in 2026 playtest footage

| Playtest | Source (channel, video ID) | Time in video | Mode | Evidence and label |
|---|---|---|---|---|
| PT1 or PT2 | **Official**: "Battle Bears Gold launches Nov 4, 2026 - Official Playtest Highlights" (BATTLE BEARS, C7uFxvSZ10c, published Aug 16, 2026; description: "Highlights from our first two Discord playtests") [Canon: title and description] | ≈1:48–1:54 | Team mode, exact mode unknown | Sandstone ruins, lava pool, cyan jump pad and magenta sky with a 2–2 red/blue score [Observed] |
| **PT2, Jul 29** | InstableGR, "Battle Bears Gold - PC Playtest #2 w/ New Mode (7/29/26)" (lFr8-yHbbzQ). Chapter: "00:00 - Match 1 (Kill Confirmed, Aztec Attack, Oliver)" [Fan description] | 0:00–4:14 | **Kill Confirmed** | **Documented and observed.** Details below the table. |
| PT2, Jul 29 | M1kaa717, "Battle Bears Gold CLOSED BETA 2026 Testing #2 Clipdump" (g_Qbis4xaLY, Jul 29) | ≈15:50–17:20 | Unresolved | Aztec clips with red/blue scores. The montage cuts between clips, so the mode cannot be read [Observed; mode Unverified] |
| **PT3, Aug 21** | InstableGR, "Battle Bears Gold - PC Playtest #3 (8/21/26)" (aujTcdFuxdE). Chapter: "42:39 - Match 11 (Plant the Bomb, Aztec Attack, Tillman/Wil" (unclosed bracket in the original) [Fan description] | 42:39–47:49 | **Plant the Bomb** | **Documented and observed.** Details below the table. |
| **PT3, Aug 21** | JustNubz, "Battle Bears Gold Playtest #3 Part 1" (qt43iTdANbM). Chapter: "13:50 Aztec Attack FFA" [Fan description] | 13:50–≈17:40 | **Free-for-All** | **Documented and observed.** Details below the table. |
| PT4, Sep 20 | **Official livestream**: "BBG Livestream Sunday" (BATTLE BEARS, ejjsoKQ-VXU, Sep 20). Description: "Join Ben and Gold44 as they test the latest build." [Canon] | ≈25:50–30:10 | Team Battle (likely) | "YOU'RE ON TEAM BLUE"; 2:59 at 27:00 and 1:59 at 28:00, so 4 minutes; "RED TEAM WINS"; final board 19 vs 15; 12 feed crops show only KILLS and Joule rewards [Observed; mode Inference] |
| PT4, Sep 20 | Same official livestream | ≈52:20–57:30 | **Plant the Bomb** (likely) | Details below the table. |
| PT4, Sep 20 | Left4Dead, "Battle Bears Gold Playtest" (BLcbfgDhjvs), and JustNubz, "Battle Bears Gold Playtest #4 (Raw 3 Hours of Goodness)" (uNZA3nlABOA, 20:00–24:00). Same lobby: both show GUBZANDER, LEFT4DEAD, KUBEARNIKUS, BEAR4553, NYCO, JUSTNUBZ, TOBBSAUCE and HOLYCHICKEN01 [Observed] | L4D ≈23:40–28:00 | Team Battle (likely) | "YOU'RE ON TEAM RED"; 2:58 at 24:50 and 0:08 at 27:40, so 4 minutes; "RED TEAM WINS"; feed shows KILLS, SUICIDE, ASSIST and +500, with no SCORED or DENIED [Observed; mode Inference] |
| PT4, Sep 20 | Left4Dead (BLcbfgDhjvs) | ≈94:00–98:00 | Team Battle (likely) | "YOU'RE ON TEAM BLUE"; 2:59 at 95:00 and 0:59 at 97:00, so 4 minutes; "RED TEAM WINS" [Observed; mode Inference] |
| PT4, Sep 20 | JustNubz (uNZA3nlABOA) | ≈13:20–17:30 | **FFA** (likely) | Single-leader HUD ("JUSTNUBZ", "GUBZANDER", "KAZPURE"); 3:00 at 14:20 and 1:00 at 16:20, so 4 minutes [Observed; mode Inference] |
| PT4 window | Slinkster, "Battle Bears Gold Beta Test #4" (tNcHwpk5UuY). Description: "recorded on September 2-20th 2026" [Fan description] | ≈1:00–5:30 | **Plant the Bomb** (likely) | Details below the table. |
| **PT5, Oct 15** | Left4Dead, "Battle Bears Gold FINAL PLAYTEST" (MS2wiArCiCA, streamed Oct 15) | ≈39:00–41:20 | **Kill Confirmed** (likely) | "YOU'RE ON TEAM BLUE"; 3:58 at 39:00, so 4 minutes; feed reads "DENIED" and "SCORED", each with a pink or blue tag icon [Observed; mode Inference, from the same feed vocabulary as the chaptered KC match] |
| PT5, Oct 15 | Vada Zora Reva Nova, "Battle Bears Gold: The Final Playtest Session Before Release! (iPad Gameplay!)" (dz4iqZE8nQE, uploaded Oct 16) | ≈74:40–78:40 | **FFA** (likely) | Single-leader HUD ("2 … ACEARTS", "5 … NOONASLAYER"); 2:53 at 75:40 and 0:03 at 78:30, so 4 minutes [Observed; mode Inference] |
| PT5 | M1kaa717, "BATTLE BEARS GOLD 2026 FINAL BETA HIGHLIGHTS" (s9W6eLXj9qc, Oct 16) | ≈0:45–2:30 | Unresolved | A montage of Aztec clips with team scores [Observed; mode Unverified] |
| PT5 | InstableGR, "Battle Bears Gold - Final PC Playtest (10/15/26)" (HKbwq7PolNc) | — | — | Its 17 chaptered matches include **no** Aztec Attack [Fan description] |

**Evidence for the four key matches**
- **PT2 Kill Confirmed (lFr8-yHbbzQ, 0:00–4:14):**
  - The feed shows "SCORED" and "DENIED" at f_0050000, f_0100000, f_0170000, f_0200000 and f_0210000 [Observed].
  - The team score does not track kills [Observed numbers]:
    - At f_0040000 the board reads **0 vs 0** while players already have kills (DOCCRPLS 2, INSTABLEGR 2, and others).
    - At f_0090000 it reads **4 vs 3** while each team's kill column sums to 7.
    - At f_0230000 it reads **9 vs 15** while the kill columns sum to 16 and 20.
  - "YOU'RE ON TEAM BLUE" at 0:10 [Observed].
  - The clock reads 3:58 at 0:10 and 0:28 at 3:40, so the round is 4 minutes [Observed].
- **PT3 Plant the Bomb (aujTcdFuxdE, 42:39–47:49):**
  - The clock reads 3:52 at 43:50, 2:52 at 44:50, 1:52 at 45:50, 0:52 at 46:50 and 0:02 at 47:40. That is a **5-minute** round [Observed], which matches the wiki's PTB length [Fan-wiki].
  - At 46:30 a dark angular device with a red and a green light stands on a red square plinth beside a yellow-and-black striped post, inside a temple room [Observed]. That it is the red team's "bomb tube" is [Inference].
  - The feed shows KILLS, ASSIST, SUICIDE, SAYS and SHIELDS, and never SCORED or DENIED [Observed].
- **PT3 Free-for-All (qt43iTdANbM, from 13:50):**
  - The HUD shows a single leader instead of team scores; the clock reads 2:52 at 15:00 and 0:22 at 17:30 [Observed].
  - M1kaa717's video "BATTLE BEARS GOLD *2026* Closed BETA Test Experience..." (MhJakRqd9ew, Aug 22) shows the same lobby. Both show SUPERBEAR, JUSTNUBZ, GUBZANDER, DARKLORD, FORGINAL, DOODLES and RANDYDECK. At 4:44 it shows "**M1KAA717 WINS!**" [Observed]. An individual winner confirms FFA.
- **PT4 official livestream, second match (ejjsoKQ-VXU, ≈52:20–57:30):**
  - "YOU'RE ON TEAM RED" [Observed].
  - The clock reads 3:59 at 53:30, 2:59 at 54:30 and 0:29 at 57:00, so the round is **5 minutes** [Observed].
  - A red digital countdown appears top right ("0:23:48" at 55:00) and a pink-red light beam at 55:20 [Observed]. That these are bomb cues is [Inference].
  - The lobby's mode tile has different art from the first match's tile, but its label cannot be read at this resolution [Observed].
- **Slinkster PT4 window (tNcHwpk5UuY, ≈1:00–5:30):**
  - At 1:10 a player carries a large blue sphere on a handle up a temple stair, with the same red digital countdown ("0:24:48") [Observed].
  - At 4:30 a red sphere sits on a red square platform under a red light beam [Observed].
  - The clock reads 3:56 at 1:30 and 0:06 at 5:20, so the round is **5 minutes** [Observed].
  - The wiki says each team's bomb is "in the same color" and "starts on a bomb platform in the same color as the bomb itself" [Fan-wiki]. Reading the spheres as the blue and red bombs is [Inference].

### Answer
- Aztec Attack ran in **all four** 2026 playtest modes [Documented + Observed + Inference, per the table]:
  - **Kill Confirmed:** PT2, documented and observed; PT5, inferred.
  - **Plant the Bomb:** PT3, documented and observed; PT4, inferred twice.
  - **Free-for-All:** PT3, documented and observed; PT4 and PT5, inferred.
  - **Team Battle:** PT4, inferred three times.
- Kill Confirmed, which the store page does not list, ran on Aztec in the very playtest that introduced it [Fan description + Observed].
- Which modes Aztec will rotate through at the Nov 4 launch is still [Unverified]. No SkyVu text names Aztec Attack's modes.
- **Official SkyVu material containing 2026 Aztec footage:**
  - the Official Playtest Highlights video (C7uFxvSZ10c, ≈1:48–1:54);
  - the Sep 20 livestream (ejjsoKQ-VXU);
  - "BBG Maps Ranked part 1" (BATTLE BEARS, jkv6FHPghx8, Oct 11, 2026; description "Maps ranked pt1, do you agree?"). Its Aztec gameplay at ≈0:59–1:04 is lava and sandstone under a magenta sky [Canon: titles and descriptions; Observed: frames]. The tier Aztec was given cannot be read in the storyboard [Unverified].
  - Together these support (but do not prove) Aztec's inclusion at launch [Inference].

## 3. Inside the temples in the 2026 build

### Frames that show the interiors
1. **Best frame: `$AA/frames/aujTcdFuxdE/f_2790000.jpg`** (PT3, Aug 21, PTB, 46:30; enlarged at `$AA/seg/pt3_2790_x4.jpg`) [Observed].
   - An enclosed room of cool grey carved stone.
   - Two tall wall panels each carry a large carved **grimacing mask face** with heavy brows and bared teeth, framed by scroll and spiral borders.
   - Brick courses run along the base.
   - The device on the red plinth with the yellow-and-black post stands in front.
2. **`$AA/frames/aujTcdFuxdE/f_2560000.jpg`** (42:40, enlarged at `$AA/seg/pt3_2560_x4.jpg`): the **blue-team spawn** ("YOU'RE ON TEAM BLUE") [Observed].
   - A grey-stone room with a huge **concentric spiral relief** on the back wall and a low brick altar block.
   - Doorways open onto glowing lava and a magenta sky.
   - A white box with a red cross (probably a Health Pack) sits outside one doorway [Observed; identification Inference].
3. **`$AA/frames/aujTcdFuxdE/f_2630000.jpg`** (43:50, enlarged at `$AA/seg/pt3_2630_x4.jpg`) and **`f_2840000.jpg`** (47:20) [Observed].
   - A large **pale silver floor disc** set into the grey flagstones.
   - It is engraved with five-pointed stars, curling cloud swirls and an outer ring of clock-like tick marks.
   - It is brightly lit while the rest of the room is dim.
4. **`/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/toxic-terror-gap/frames/BLcbfgDhjvs/f_1430000.jpg`** (PT4, Sep 20, 23:50): the **red-team spawn** ("YOU'RE ON TEAM RED") [Observed].
   - Beside the doorway are carved panels inlaid with red gem mosaics.
   - The same match shows a **gold floor disc** at f_1500000, f_1510000 and f_1560000. At f_1560000 the gold disc is visible at the red-team respawn [Observed].
   - The grey wall at f_1500000 carries a large spiral relief [Observed].
5. **`$AA/frames/uNZA3nlABOA/f_1390000.jpg`** (PT4, 23:10): "YOU'RE ON TEAM BLUE" with the player standing on the **pale silver disc** [Observed].
6. **`$AA/frames/aujTcdFuxdE/f_2590000.jpg`** (PT3, 43:10): a **gold disc** engraved with sun rays [Observed]. It is crossed by blue-bolt Joule tokens.
7. **`/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/environment-conventions/frames/sb_lFr8-yHbbzQ/f_0200000.jpg`** (PT2, Jul 29, KC, 3:20; enlarged at `$AA/pt2/f200_x4.jpg`) [Observed].
   - The view looks out of a temple doorway: dark stone walls with a big spiral relief on the left, a rectangular opening onto lava, and a magenta sky.
   - **Correction to the gap brief:** no carved *face* can be made out in this frame, only the spiral.
8. **`/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/toxic-terror-gap/frames/MS2wiArCiCA/f_2410000.jpg`** (PT5, Oct 15, 40:10): the **gold disc** seen from above [Observed].
   - The surrounding floor reads warm brown-sandstone (≈#9B6E3F), not grey.
   - This may be PT5's "Lighting improvements" [Canon: news text] or a difference in capture [Inference; Unverified].
9. **The giant glowing gold mask face** [Observed]:
   - `$AA/frames/uNZA3nlABOA/f_0890000.jpg` (PT4, 14:50);
   - `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/toxic-terror-gap/frames/BLcbfgDhjvs/f_5710000.jpg` (PT4, 95:10).
   - It is a wall-sized carved mask face glowing orange-gold (≈#E0A323), framed by grey carved stone.
   - Where it sits on the map is [Unverified]: inside a temple, at the summit shrine, or on a facade.

A comparison board of frames 1, 2, 3, 4, 5 (the f_1500000 room), 7, 8 and 9 is at `$AA/seg/interior_board.jpg`.

### What the interiors look like
- **Material contrast.** The temple **exteriors** are warm orange sandstone; the **spawn rooms** are cool slate-grey carved stone (PT2–PT4 frames) [Observed]. Use this contrast in shorts.
- **Lighting** [Observed]:
  - The floor discs read brightly lit, as if from above, while the walls stay dim.
  - Doorways glow orange from the lava outside and frame the magenta night sky.
  - No torches, braziers or visible lamps appear in any interior frame.
  - What lights the discs is [Unverified]. A skylight is [Inference].
- **Palette.** Approximate hex values: medians of sampled boxes from compressed 320–429 px storyboard frames [Observed].
  - Grey floor: #2C2A36 in shade, #3C3A4A where lit.
  - Grey wall: #383634.
  - Silver disc: #878EA9 to #ADAFC9.
  - Gold disc: #DFB96D (PT3) and #F6B862 (PT5).
  - Giant gold face: #E0A323.
  - Glowing red gems on the red temple: #EB1B26 (JustNubz PT3 f_0860000, two big glowing red oval gems in a carved wall).
  - Red plinth: #86273A. Red bomb: #CE0205. Blue bomb: #0B01CD (both Slinkster).
  - Sky through doorways: #6B0139 (PT2), #71013C (PT5), #4A012A (PT4 phone capture).
  - Lava: #DD780F (PT3), #F6BC22 (PT5).
- **Which temple is which colour (stronger than the draft's inference):**
  - The red spawn has red gem panels and the gold disc. The blue spawn has the silver disc [Observed in two spawn frames each side; the general rule is Inference].
  - In PT2, blue-team Oliver attacks the temple whose facade has glowing red panels (f_0030000) [Observed].
  - In the 2012 top-down render, the summit panel glows **orange** on the red-marked temple and **pale lavender-white** on the blue-marked one [Observed in the draft]. That matches the gold and silver disc colours of each team [Inference].
  - So: **red team = red-gem, gold-disc temple; blue team = silver-disc temple** [Inference, now well supported].

### Over Clocked Oliver and Astoria symbols: result
- **Wiki claims** [Fan-wiki, Unverified]:
  - Aztec Attack page: "One temple has a symbol representing [[Over Clocked Oliver]], while the other has a symbol representing [[Astoria]]."
  - OCO page: "there seems to be a carving of Over Clocked Oliver, along with [[Astoria]]. Both are located at each team's spawn points."
  - The Aztec Attack line was first added on **2013-07-06** by user "Cheese Ausar" (revision 44951) and has stayed in every revision since [Observed: revision history]. It describes the 2013 BBG build, not 2026.
- **What the 2026 spawn-room frames show:**
  - The carvings are mask faces, spirals, scroll borders, red gem mosaics and the two floor discs [Observed].
  - **No carving identifiable as OCO or Astoria** is visible at storyboard resolution [Observed absence; low resolution].
  - The centre of each disc cannot be resolved. An 8× crop of the gold disc (`$AA/seg/medallion_centres_x8.jpg`) shows a small central figure that cannot be identified [Observed].
- **Lead.** Each spawn has its own team-specific disc, and the wiki puts the symbols "at each team's spawn points". The discs are therefore the best candidates for the wiki's "symbols" [Inference; Unverified]. Possible readings, all speculation, never to be presented as fact:
  - stars on the silver disc as "Astoria" (astra, stars);
  - the clock-like ring as "Over Clocked".
- **Status:** still unconfirmed. Keep "[Fan-wiki, Unverified]" on every use.

## Images viewed (opened with Read, all displayed)

**Sheets and crops I built**
- `$AA/seg/interior_board.jpg`
- `$AA/seg/pt3_a.jpg`, `$AA/seg/pt3_b.jpg`, `$AA/seg/pt3_2790_x4.jpg`, `$AA/seg/pt3_2630_x4.jpg`, `$AA/seg/pt3_2560_x4.jpg`
- `$AA/seg/medallions_x5.jpg`, `$AA/seg/medallion_centres_x8.jpg`, `$AA/seg/discs.jpg`
- `$AA/pt2/sheet_000_050.jpg`, `$AA/pt2/sheet_060_110.jpg`, `$AA/pt2/sheet_180_230.jpg`, `$AA/pt2/f200_x4.jpg`, `$AA/seg/pt2_feed.jpg`
- `$AA/seg/jn_ffa.jpg`, `$AA/seg/jn_int_x3.jpg`, `$AA/seg/mhj.jpg`
- `$AA/seg/ejj_a.jpg`, `$AA/seg/ejj_feed_a.jpg`, `$AA/seg/ejj_b.jpg`, `$AA/seg/ejj_1560_x5.jpg`, `$AA/seg/ejj_ptb_x3.jpg`
- `$AA/seg/blc_a.jpg`, `$AA/seg/blc_feed.jpg`, `$AA/seg/blc_int_x3.jpg`, `$AA/seg/blc_1430_panel_x6.jpg`, `$AA/seg/blc_1500_wall_x5.jpg`, `$AA/seg/blc_b.jpg`, `$AA/seg/blc_b_x3.jpg`
- `$AA/seg/unz_a.jpg`, `$AA/seg/unz_b.jpg`, `$AA/seg/unz_x3.jpg`
- `$AA/seg/tnc.jpg`, `$AA/seg/tnc_ptb_x3.jpg`, `$AA/seg/tnc_b_x3.jpg`
- `$AA/seg/ms2.jpg`, `$AA/seg/ms2_x3.jpg`, `$AA/seg/ms2_feed.jpg`, `$AA/seg/hud_tops.jpg`
- `$AA/seg/dz4.jpg`, `$AA/seg/s9w.jpg`, `$AA/seg/g_Q2.jpg`, `$AA/seg/g_Q_feed.jpg`
- `$AA/seg/c7u.jpg`, `$AA/seg/jkv6.jpg`
- `$AA/seg/mode_tiles.jpg`, `$AA/seg/mode_labels.jpg`
- `$AA/scan/cand2.jpg`, `$AA/scan/cand3.jpg` (scanner false positives, rejected)

**Thumbnails**
- `$AA/thumbs/1MP1_maxres1.jpg`, from https://i.ytimg.com/vi/1MP1rFi4t-Q/maxres1.jpg (the KC prompt)
- `$AA/thumbs/lFr8_maxresdefault.jpg`, from https://i.ytimg.com/vi/lFr8-yHbbzQ/maxresdefault.jpg (fan cover art, no map)

**Frame sources**
- `$AA/frames/aujTcdFuxdE/`, `$AA/frames/qt43iTdANbM/`, `$AA/frames/uNZA3nlABOA/`
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/environment-conventions/frames/sb_lFr8-yHbbzQ/ and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/environment-conventions/frames/sb_C7uFxvSZ10c/
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/toxic-terror-gap/frames/ (ejjsoKQ-VXU, BLcbfgDhjvs, tNcHwpk5UuY, MS2wiArCiCA, dz4iqZE8nQE, s9W6eLXj9qc, g_Qbis4xaLY, MhJakRqd9ew)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/gold_digger_verify/yt/sb/jkv6FHPghx8/

**Built but never displayed; no claims rest on them**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/critic2/pt2_aa_check.jpg
- `$AA/pt2/sheet_120_170.jpg`, `$AA/pt2/sheet_240_260.jpg`
- `$AA/scan/runs_0.jpg` to `runs_3.jpg`
- `$AA/seg/g_Q.jpg`, `$AA/seg/ejj_1540_x5.jpg`

## Prompt pack (temple interior)

**Base 9:16 establishing shot, environment only**

> Vertical 9:16 interior of a squat stone temple chamber at night. Floor of large irregular slate-grey flagstones with dark grout lines. In the foreground, set flush into the floor, a large circular medallion of polished pale silver engraved with five-pointed stars, curling cloud swirls and an outer ring of clock-like tick marks, brightly lit from above so it glows against the dim floor. Walls of cool grey carved stone blocks: on the back wall a huge concentric spiral relief above a low brick altar block; on the side walls tall panels carved with grimacing mask faces with heavy brows and bared teeth, framed by scroll borders; brick courses along the wall bases. Two rectangular doorways in the back wall open onto the outside, showing glowing orange-yellow lava and a starry magenta-to-crimson night sky, with warm orange light spilling across the sills. Dim, cool stone interior; a bright pale pool of light on the medallion; warm lava glow only at the doorways; no torches or lamps. Chunky low-poly game-world forms with hand-painted textures and dark outlines. No characters, no text, no logos.

- **Documented** [Observed in 2026 frames 1–7]: the grey stone, spiral relief, mask-face panels, brick altar, silver disc motifs, doorways onto lava and magenta sky, the bright disc and dim walls, and no torches.
- **[BBG News invention]:** the exact layout (which wall holds which carving), the "from above" light source, and the camera position.
- **Red-team variant** [Observed: gold disc and red gem mosaics; team mapping is Inference]: swap in a gold disc engraved with sun rays (≈#DFB96D–#F6B862) and add carved door panels inlaid with red gem mosaics (≈#EB1B26 where lit).

**Spots where a short could stage a scene**
1. **The spawn disc.** A character "beams in" on the glowing silver or gold medallion, as players respawn here [Observed: "YOU'RE ON TEAM BLUE/RED" over the disc rooms; staging is BBG News invention].
2. **The doorway threshold.** A silhouette against lava and the magenta sky, looking out across the arena; PT2's 3:20 frame is this exact view [Observed; staging is BBG News invention].
3. **The carved-mask room with the red plinth.** A Plant-the-Bomb heist or defuse beat under the grimacing stone faces [Observed: room and device; that it is the bomb tube is Inference; staging is BBG News invention].
4. **The giant glowing gold mask face.** A "the temple is watching you" reaction shot [Observed: face; location Unverified; staging is BBG News invention].

## Confidence
- **Modes:**
  - Documented and observed: KC (PT2), PTB (PT3), FFA (PT3).
  - Partial (inferred from frames): Team Battle (PT4), PTB (PT4), KC (PT5), FFA (PT4, PT5).
  - Unknown: the launch rotation.
- **Interiors:** observed, but low resolution (storyboards of 320–429 px).
- **Team colour mapping:** partial; well supported.
- **OCO and Astoria symbols:** unknown. They have not been seen, and the floor discs are only a candidate.

---

## Corrections to our notes

1. **/home/user/thallo-site/research_notes/BBG maps (unverified drafts)/research_aztec-attack.md, line 61** (identical scratchpad copy at /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/out/drafts/research_aztec-attack.md).
   - Current text: "  - The 2026 modes are TDM, FFA and PTB [Canon]. Which of them run on Aztec Attack at launch is [Unverified]."
   - Correction:
     - The store lists TDM, FFA and PTB [Canon].
     - In the 2026 playtests Aztec Attack ran in Kill Confirmed (PT2, Jul 29: fan chapter plus SCORED/DENIED feed observed; PT5, Oct 15: inferred), Plant the Bomb (PT3, Aug 21: chapter plus 5-minute clock and bomb plinth observed; PT4: inferred twice), Free-for-All (PT3: chapter plus "M1KAA717 WINS!" observed; PT4 and PT5: inferred) and Team Battle (PT4: inferred three times).
     - Kill Confirmed is not on the store page.
     - The launch rotation is still [Unverified].
   - Evidence: section 2 table; storyboard frames lFr8-yHbbzQ f_0040000, f_0090000 and f_0230000; aujTcdFuxdE f_2630000 to f_2860000; MhJakRqd9ew f_0284000; MS2wiArCiCA f_2360000 to f_2380000; Steam appdetails re-fetched 2026-10-18.
2. **Same file, line 59** ("…lists the chapter "13:50 Aztec Attack FFA"… [fan description; thumbnail Observed; video not watched]").
   - Add: storyboard frames from 13:50 to 17:40 show a single-leader FFA HUD, and M1kaa717's view of the same lobby (MhJakRqd9ew) ends "M1KAA717 WINS!" [Observed]. The video is still unwatched; only storyboards were viewed.
   - Evidence: `$AA/seg/jn_ffa.jpg`, `$AA/seg/mhj.jpg`.
3. **Same file, lines 89–90** ("Reading them as spawn markers is [Inference]." / "That the red temple is the red base is [Inference].").
   - Strengthen with 2026 evidence:
     - The "YOU'RE ON TEAM RED" spawn has red gem mosaic panels and a gold floor disc (BLcbfgDhjvs f_1430000 and f_1560000).
     - The "YOU'RE ON TEAM BLUE" spawn has a silver disc (uNZA3nlABOA f_1390000; aujTcdFuxdE f_2560000 to f_2640000).
     - Blue-team Oliver attacks the red-panel temple (lFr8-yHbbzQ f_0030000).
     - The 2012 summit-panel colours (orange and pale) match the gold and silver discs.
   - The label stays [Inference], now well supported.
4. **Same file, line 180** ("The claimed spot (spawns inside the temples) is not clearly shown in any image.").
   - Replace with: 2026 storyboard frames show both spawn rooms. They are enclosed grey carved-stone chambers with mask-face panels, spiral reliefs, a brick altar, red gem mosaics (red side) and team-specific floor discs: gold with sun rays for red, silver with stars and swirls for blue.
   - No OCO or Astoria likeness can be identified at this resolution [Observed]. The discs are the likeliest candidates for the wiki's "symbols" [Inference, Unverified].
   - Also note that the wiki line dates from 2013-07-06 (revision 44951).
5. **Same file, lines 81–86 ("Temples in-game").**
   - Add: the interiors are cool slate-grey stone (≈#2C2A36–#3C3A4A floor, ≈#383634 wall), in contrast to the warm sandstone exterior. There is also a giant glowing gold mask face (≈#E0A323), location unconfirmed [Observed].
   - Evidence: `$AA/seg/interior_board.jpg`.
6. **Same file, lines 284 and 288 (open questions).**
   - Interior frames now exist (section 3). The symbols are still unconfirmed.
   - 2026 playtest modes are answered (section 2). The launch rotation stays open.
7. **/home/user/thallo-site/research_notes/BBG weapons (verified)/2026.addendum.md, "Blue lightning-bolt tokens (sub-topic; the gap's "Joule tokens")" (formerly line 303).** Applied: that sub-topic and its open question 7 now say the bolt tokens are not KC tags and are probably Joule drops.
   - Current text: "  - Whether the tokens are Joule drops, Kill Confirmed tags or both is [Unverified]."
   - Correction: the blue-bolt hex tokens also appear in non-KC Aztec matches:
     - the chaptered PTB match (aujTcdFuxdE f_2590000, 43:10, and f_2760000, 46:00);
     - the FFA match (MhJakRqd9ew, ≈3:56).
   - KC "SCORED/DENIED" feed entries use a different, tag-shaped icon (1MP1rFi4t-Q maxres1; MS2wiArCiCA f_2360000). So the bolt tokens are not KC tags. That they are Joule drops is [Inference, likely].
   - The same applies to open question 7 in that file's first "Open questions" list (formerly line 359).
8. **/home/user/thallo-site/research_notes/Battle Bears character lore/franchise_world.md, Q2 §E "Settings and maps (wiki)", the Aztec Attack entry under "Map details" (formerly line 225)** ("**Aztec Attack**: temple carvings of O.C.O. and Astoria."). Applied: the entry now carries the hedged wiki wording, the 2013-07-06 date and the 2026 spawn-room note.
   - In addition to the earlier draft's fix (use the hedged wiki wording), append: "2026 playtest frames of both spawn rooms show no identifiable OCO or Astoria carving; the wiki line dates from 2013-07-06."
   - The labels in the lore report and in characters/oliver.md and characters/astoria.md ("[Fan-wiki, Unverified]") remain correct.

## Open questions
- Which modes will Aztec Attack run in at the Nov 4, 2026 launch? No SkyVu text names its modes.
- **The fastest way to settle the symbols and identify the disc centres:** the Steam Next Fest demo (Oct 19–21, per InstableGR's and SkyVu's descriptions [Fan description; Canon]) or launch footage, captured at full resolution in each spawn room. A frame at 1080p or better of each disc centre, plus the mask panels, would answer whether the wiki's OCO and Astoria symbols exist.
- Where is the giant glowing gold mask face: inside a temple, at the summit shrine, or on a facade?
- Is the dark device on the red plinth (PT3, 46:30) the red team's PTB "bomb tube"? And is the red digital countdown seen in the PT4 bomb matches the bomb-carry timer?
- Was PT4 livestream match 1 Team Battle rather than KC? The lobby mode tiles cannot be read at storyboard resolution.
- Which modes were the Aztec clips in M1kaa717's PT2 clipdump (g_Qbis4xaLY) and PT5 highlights (s9W6eLXj9qc)?
- Did PT1 (Jul 9) include Aztec Attack? The official highlights reel mixes PT1 and PT2, and I scanned no PT1-only footage with Aztec.
- Is PT5's warmer sandstone floor around the gold disc a result of SkyVu's "Lighting improvements" or of capture differences?
- Where did Aztec Attack land in the official "BBG Maps Ranked part 1" tier list?