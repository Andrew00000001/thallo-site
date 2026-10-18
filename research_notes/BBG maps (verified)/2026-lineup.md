# BBG 2026 map lineup

This dossier covers the map lineup for the Nov 4, 2026 re-release of Battle Bears Gold (BBG):
- which maps are in the game;
- which are new, missing or reworked compared with BBG 2013–2021;
- which modes each map has been seen in;
- what is known about the 2026 look.

It also identifies the map in every gameplay shot of the official Steam trailer and the five Steam screenshots. Only the one new map, Sky Pirates (also called "Sky World"), gets a full map block. The 15 legacy maps have their own dossiers; this one gives a quick reference for each.

**Verification pass, Oct 18, 2026.** Every source below was re-fetched in this pass, and every image marked [Observed] was re-downloaded and opened. Timings are accurate to about ±0.5 s.

**Sources reached and re-checked (Oct 18, 2026):**
- **Steam appdetails** for BBG (4408320), the Soundtrack (5321720) and the Demo (5225670).
  - The five BBG screenshots were re-downloaded. Their md5 hashes are identical to the local `steam_screens/screen_00–04.jpg`.
  - The Soundtrack's two store images were opened: a logo card and a track-list card. Neither shows a map.
- **Steam store HTML** for BBG and the Soundtrack.
- **The live Steam trailer playlist** (`hls_264_0_video.m3u8`): 18 segments, 54.0 s. This matches the local `trailer.mp4` (54.02 s, 1920×1080, 30 fps).
- **The Steam news API** (all 7 posts) and the 4 announcement images.
- **battlebears.com** and **play.battlebears.com**.
- **The Fandom wiki through the MediaWiki API:**
  - all 15 BBG map pages, Tutorial, BBG Maps, Battle Bears Gold, Battle Bears Gold/Versions, Updates and BBR Version 1.0;
  - Plant the Bomb, Free-For-All, Team Battle and King of the Windmill;
  - Sky Pirates, Battle Bears Overclock, Bearscream Sandwich, Pick-Ups and Bearzerker;
  - file metadata and images: Bearscream_Sandwich.jpg, Uumhfc.jpg, Toxic-Terror-Preview.png, Steamyard.png, and the four Sky Pirates images.
  - Pages that do not exist: "Battle Royale", "Castle Royale", "Bridge to Terabearthia" and "Kill Confirmed".
- **YouTube metadata** (titles, dates, channels, descriptions, chapters) from the innertube "next" and "search" endpoints, plus auto-thumbnails (maxres, hqdefault, hq1–3, and Shorts oar1–3). The videos covered are:
  - 15 official uploads;
  - about 40 fan uploads.

**Not reachable:**
- **web.archive.org.** curl gets "connection reset" every time, and the proxy logs "ws_closed_mid_exchange". WebFetch refuses the domain. The archive.org availability API does answer, but no snapshot could be fetched. No archived SkyVu blog post or patch note could be re-read, so the version history below relies on the wiki's transcription of store update notes [Game text via wiki].
- **Video playback and transcripts.** I watched no video. Everything said about a video comes from its title, description, chapter list or auto-thumbnails.

## Bottom line

- **The official count is 16, but no official list exists.** SkyVu says "16 wacky maps" and names only four: No Bears Land, Gold Digger, Space Oddity and Steamyard Blues [Canon]. No SkyVu text, post or video description I found lists all 16 [Unverified].
- **One new map is documented: Sky World / Sky Pirates.**
  - The Aug 19, 2026 playtest post calls it "Sky World", and the Aug 31 reveal video calls it "Sky Pirates" [Canon].
  - The official Short "Sky Pirates in BBG!" carries the description "Enjoy the highlights from our Sky World playtest!" [Canon].
  - Overclock's 2020 update notes also call a map "Skyworld" ("Upgraded Map Lighting, check out how Skyworld has benefitted!", BBO 3.0, Jul 3, 2020 [Game text via wiki]). The wiki's BBO map list has Sky Pirates and no "Skyworld" [Fan-wiki].
  - That the two names mean one map is a strong [Inference].
  - It is a port of the 2014 Battle Bears Ultimate/Overclock launch map [Fan-wiki]. The 2026 frames match the wiki's 2015 BBO render [Observed].
- **The best-supported reading of 16 is the 15 legacy BBG maps plus Sky Pirates** [Inference].
  - Fan playtest chapter lists from July–October 2026 place 14 of the 15 legacy maps, and Sky Pirates, in the 2026 builds [Unverified: fan chapter text; videos not watched].
  - Fan and official thumbnails independently show No Bear's Land, Skate or Die, Frozen Pundra, Space Oddity, H.I.P. Test Lab, Steam Yard Blues, Abusement Park (probable), Desert Airmine and Sky Pirates in 2026 builds [Observed thumbnails; map identity is Inference where noted].
- **Toxic Terror is the only legacy map with no 2026 sighting.** It has a 2026 soundtrack track [Canon]. A fresh YouTube search and about 40 more 2026 fan thumbnails turned up no Toxic Terror gameplay [Unverified absence]. Its 2026 status is unknown.
- **Nothing is confirmed removed in 2026.** The documented removals are older:
  - King of the Windmill was "retired" in v2.29 (Jan 26, 2018) [Game text via wiki].
  - Battle Royale (v2.50, Apr 5, 2018) is not among the 2026 store modes [Canon by absence].
  - The 2026 soundtrack still has a "Castle Royale" track [Canon]. That track is most likely the music of the 2018 Battle Royale castle map [Inference]. No 2026 source shows that map playable [Unverified].
- **The store lists three modes:** TDM, FFA and PTB [Canon].
  - A fourth, Kill Confirmed, was playtested as "An experimental new gamemode" [Canon wording].
  - The name comes from fans. Its HUD lines "YOU'RE ON TEAM BLUE / COLLECT ENEMY TAGS TO SCORE POINTS" and its "SCORED" / "DENIED" badges are visible in fan thumbnails [Observed].
  - It is not on the store list.
- **The official trailer shows 9 maps, and the five screenshots are stills from it** [Observed].
  - The 9 maps are Gold Digger, Aztec Attack, Abusement Park, Shortest Parsec, Space Oddity, H.I.P. Test Lab, Marecraft, Skate or Die and Sky View.
  - The screenshots show H.I.P. Test Lab, Space Oddity, Shortest Parsec ×2 and Gold Digger [Observed pixel match].
- **The trailer is 2013 footage, so it does not show the 2026 look.**
  - Its Graham, Tillman and Oliver class cards are identical to SkyVu's May 30, 2013 BBG trailer [Observed].
  - It shows only the 8 classes the 2013 description advertises ("Choose from 8 classes") [Observed; Canon].
  - It shows no map added after BBG's launch [Observed].
  - The Oct 12, 2026 Q&A thumbnail reuses the trailer's Oliver-on-Marecraft shot [Observed].
- **Official 2026-build imagery:**
  - The Oct 14 "Closed Testing 5" banner, showing No Bear's Land [Observed].
  - The Sky Pirates reveal and Short frames [Observed].
  - The Aug 16 "Official Playtest Highlights" thumbnails and the Aug 25–30 "Playtest Highlights" Shorts. These carry fan playtester name tags, so they are 2026 Discord-playtest footage [Observed; Inference]. They show No Bear's Land, Skate or Die and Frozen Pundra (map identity is Inference).
  - The Sep 20 livestream thumbnails: Sky Pirates art and Skate or Die [Observed].
- **The 2026 build has a new lighting pass.**
  - The final-playtest post says "-Lighting improvements" [Canon]. Its banner says "-LIGHTING, EFFECT & TEXTURE IMPROVEMENTS" [Observed].
  - A fan who played it says the overhaul restores the look of the original Battle Bears Royale [Unverified].
  - Only the Closed Testing 5 banner is likely to show the post-pass look [Inference]. The Sky Pirates reveal footage (build 3.0.3) predates it [Inference from build stamps and dates].

## 1. Official 2026 text [Canon]

**Steam store (app 4408320, fetched Oct 18, 2026):**
- Short description: "An award-winning 4v4 class shooter with more personality than sense! The ORIGINAL Mobile Multiplayer Shooting Game comes to PC! Choose from 11 unique classes, mix hundreds of thousands of loadout combinations, and compete with friends across 16 wacky maps. A third-person shooter like no other!"
- About: "Relive your childhood as this beloved third-person shooter comes to your PC. Grab your A Salt Rifle, Bearzooka and those Turkish SW Boots and fight it out with friends across beloved Battle Bears locations."
- About: "Pick between 11 distinct classes and compete for dominance across competitive 4v4 multiplayer modes. Whether you're a Team Battle diehard or prefer the underrated Plant the Bomb, there is plenty of battling to be done."
- About: "Iconic Maps will return so prepare to jump back into classics such as No Bears Land, Gold Digger and Space Oddity. You can even make some time for that yearly match on Steamyard Blues, most likely just for the soundtrack."
- About: "Speaking of music, this game has bangers so get ready to enjoy that awesome OST once again."
- Mode list, verbatim: "Dominate in Competitive Modes:-Team Deathmatch (TDM)-Free for All (FFA)-Plant the Bomb (PTB)".
- Store details:
  - Release date "Nov 4, 2026". Trailer name "Battle Bears Gold Premium - Trailer".
  - Platform flags: `windows: true, mac: false, linux: false`. The API also returns a Mac requirements block (macOS 11.0 Big Sur minimum).
  - The store HTML has only `data-os="win"`.

**Steam Soundtrack (app 5321720):**
- Short description: "The official BATTLE BEARS GOLD Soundtrack featuring original map and menu music by Rob Ruiz, AnDrue Humphreys, and Benjamin Vavak. Includes bonus vocal tracks by Vivyd, Brian Bell & Leck One."
- About: "the complete collection of map and menu music from the award-winning 4v4 class shooter".
- Track list, verbatim, with durations:
  1 Abusement Park 0:54 · 2 No Bears Land 0:44 · 3 Sky View 1:03 · 4 Gold Digger 0:38 · 5 Huggable Factory 0:54 · 6 Space Oddity 0:54 · 7 Skate Or Die 1:29 · 8 Marecraft 0:57 · 9 Shortest Parsec 1:13 · 10 Frozen Pundra 0:54 · 11 Haunted Castle 1:01 · 12 Desert Airmine 1:13 · 13 Aztec Attack 1:20 · 14 Toxic Terror 1:18 · 15 Steamyard Blues 0:51 · 16 Castle Royale 1:56 · 17 Main Menu (BBG) 1:49 · 18 Tutorial 0:32 · 19 After Match 1:04 · 20 Main Menu (BBR) 1:09 · 21 Huggable Factory (Full Version) 2:52 · 22 Abusement Park (Full Version) 3:05 · 23 I'm a Battle Bear (feat. Vivyd, Brian Bell & Leck One.) 2:44 · 24 The Right to Bear Arms (feat. Vivyd, Brian Bell & Leck One.) 1:31
- Tracks 1–16 carry map names [Observed]. The list has no "Sky Pirates" or "Sky World" track, and it includes "Castle Royale". So the soundtrack is not the 2026 map rotation [Inference].
- The two store images are a logo card and a track-list card in the same order. Neither shows any map [Observed: `img/ost_ss0.jpg`, `img/ost_ss1.jpg`].

**Steam Demo (app 5225670):**
- "BATTLE BEARS GOLD Demo", release "October 2026", Windows only.
- play.battlebears.com says: "Play the demo on Steam from October 19-26".
- A fan says the demo is "part of Steam Next Fest" [Unverified: InstableGR, HKbwq7PolNc description].

**battlebears.com home:**
- "BBG LAUNCHES NOV 4 … Your childhood is back! The award-winning Battle Bears Gold launches this November 4 on Steam PC, iOS and Google Play!"
- "This year we're bringing it back to Steam PC and Mobile, packed with new modes, maps, skins and more! Launches Nov 4"
- The site also says BB Heroes features "all the famous characters, weapons, and maps with re-imagined BB-1 Campaigns!" [Canon]. This is not about BBG's lineup.

**Steam announcements (all 7 posts in the news API):**
- **Feb 24, 2026:** "The BB Gold store page is officially live on Steam!"
- **Jul 6, 2026, playtest 1** ("this Thursday", 4pm PDT, Windows-only): "There won't be any new features in this build and any progress made will not carry over to launch."
- **Jul 28, 2026, "2nd Discord Playtest Tomorrow! Trial a new gamemode!"** ("this Wednesday at 4pm PDT", Windows-only): "Testing Server Capacity improvements and bug fixes. Controller Support (gameplay only for now) An experimental new gamemode". The post also says "See you on the Battlefield this Thursday!" [sic].
- **Aug 19, 2026, "3rd Discord Playtest this Friday! A New Map comes to BBG!":** "Friday 21st August at 4pm PDT", "still Windows only". "This version contains: Auto matchmaking New Map: Sky World Bug fixes".
- **Sep 19, 2026, "4rd Discord Playtest this Sunday Sep 20" (sic):** "Sunday 20th September at 1pm PDT".
- **Oct 14, 2026, "Final Discord Playtest this Thursday Oct 15":**
  - "The next and final BATTLE BEARS GOLD playtest will take place on Thursday 15th October at 3pm PDT … available on Windows, iOS and Android".
  - "Headline additions: -Custom keybinds -Jukebox -UI controller support -Lighting improvements -Lots of bug fixes".
  - "We'd also love to grab some screenshots for our Steam and store pages. If you're able, please record some footage, ideally on PC and without the UI (press the H key to hide it)."
- **Oct 14, 2026, "REFERRAL REWARDS: 650 SIGNS UPS as of Oct 13 🎉 Almost to 25 Gas Cans for All":** a single image. Its backdrop is described in section 7.

**Official YouTube (channel "BATTLE BEARS"):**
- "Battle Bears Gold launches Nov 4, 2026 - Official Playtest Highlights" (C7uFxvSZ10c, Aug 16, 2026): "Highlights from our first two Discord playtests for Battle Bears Gold."
- "Playtest Highlights Part 1" (oDZdTN7M0-E, Aug 25). "Playtest Highlights Part 2 #battlebears #battlebearsgold" (SZZ38et45Xs, Aug 26). "Battle Bears Gold Highlights Pt 3 #wishlist #steam" (NnjUom5NFC4, Aug 30): "Enjoy the highlights from our Discord playtest!"
- "Battle Bears Gold 2026 - Sky Pirates Map Reveal" (r91WkR10W2A, Aug 31): "BBG LAUNCHES NOV 4 on Steam & Mobile. Gameplay highlights from the new Sky Pirates map!"
- "Sky Pirates in BBG!  #battlebears #wishlist #steam" (CwxpBZg6Fi4, Sep 7): "Enjoy the highlights from our Sky World playtest!"
- "BBG Livestream Sunday" (ejjsoKQ-VXU, streamed Sep 20): "Join Ben and Gold44 as they test the latest build."
  - Its chapters include "Custom matches and map tour", "Free-for-all match and Q&A" and "Bomb plant mode and legacy skin" [Observed chapter text].
  - The description has no timestamps, so these chapters are probably YouTube's automatic ones, not SkyVu's [Inference].
- "TEASER TRAILER - Battle Bears Gold Returns November 4th 2026" (d2ByJWrsoec, Oct 2).
- "BBG Maps Ranked part 1" (jkv6FHPghx8, Oct 11): "Maps ranked pt1, do you agree?"
- "Battle Bears Gold - Q&A with the Creator" (pmE2jKQLSms, Oct 12): "CEO Ben Vu answers the most-asked BBG questions!"

## 2. Reconciling "16 wacky maps"

### 2.1 Candidate pool

- **15 legacy BBG maps** [Fan-wiki]:
  - No Bear's Land, H.I.P. Test Lab, Space Oddity, Aztec Attack, Abusement Park, Shortest Parsec, Marecraft, Sky View, Gold Digger, Skate or Die, Toxic Terror, Desert Airmine, Haunted Castle, Frozen Pundra and Steam Yard Blues.
  - Sources: the BBG Maps page list and Category:BBG Maps. The category also files Tutorial.
  - The wiki's BBG Maps list links "Marecraft Carrier". The map page itself is titled "Marecraft (Map)" and calls the map "Marecraft Arena" [Fan-wiki].
  - The wiki's Battle Bears Gold page says "14 different stages", because its picture grid omits Steam Yard Blues [Fan-wiki].
- **Sky Pirates / Sky World:** new to BBG in 2026 [Canon].
- **Castle Royale:** a soundtrack track only [Canon].
  - SkyVu's Mar 28, 2018 video "Battle Bears Gold Battle Royale Map!" (bOEK6skhDKU) says "New Battle Royale Mode and Map coming in update v2.32! See you on the battlefield." [Canon].
  - Its four auto-thumbnails show a large crenellated stone castle with teal- and red-capped round towers, on a floating green island with hedges, fences and small grave-like markers, above pink-white clouds [Observed].
  - That this castle is "Castle Royale" is [Inference].
- **Tutorial:** a single-player arena [Fan-wiki].
  - Mika_do's upload "【Battle Bears Gold】Tutorial" (lgd9Gqw6ahA, Sep 20, 2026) shows the green wireframe "matrix-rain" tutorial arena. Signs read "MOVING", "MOVE", "WEAPON / MELEE" and "TEAM BLUE", and a mobile touch HUD is visible [Observed].
  - I do not count it as a competitive map. The soundtrack lists "Tutorial" with the menu tracks [Inference].

**Arithmetic:** 15 legacy maps + Sky Pirates = 16, which matches Steam's number [Inference]. The alternatives cannot be ruled out [Unverified]:
- Toxic Terror is out, and Castle Royale or another map fills the 16th slot.
- More than one new map exists. battlebears.com says "new modes, maps" in the plural [Canon], but only Sky Pirates is documented.

### 2.2 Evidence matrix

Abbreviations for the fan playtest column (all are fan text; I watched none of the videos) [Unverified]:
- **PT2** = Jul 29, 2026: InstableGR, "Battle Bears Gold - PC Playtest #2 w/ New Mode (7/29/26)" (lFr8-yHbbzQ).
- **PT3** = Aug 21, 2026: JustNubz, "Battle Bears Gold Playtest #3 Part 1/2/3" (qt43iTdANbM, _R4rvvGlRsM, VHo1O41RNJE).
- **PT5** = Oct 15, 2026: InstableGR, "Battle Bears Gold - Final PC Playtest (10/15/26)" (HKbwq7PolNc).
- **dBBG** = droid BBG uploads.
- **TB** means "Team Battle", the game's and the fans' name for TDM. JustNubz writes "TDM".

The "Other 2026 image" column lists official and fan 2026 thumbnails I opened [Observed; map identity is Inference unless it is unmistakable].

| Map | Legacy origin | 2026 OST | Named on Steam | Official Steam trailer / screenshot (2013 footage) | Other 2026 image | Fan playtest chapters, 2026 (modes) | 2026 verdict |
|---|---|---|---|---|---|---|---|
| No Bear's Land | BBR 1.0 (Oct 8, 2011) as "Battlefield Airpad" | #2 | Yes ("No Bears Land") | Not shown | Closed Testing 5 banner; C7uFxvSZ10c maxres; "Playtest Highlights Part 1" oar1; fan KkDhuNbHn3I (Sep 20) | PT2 KC ×2, TB ×3; PT5 TB | **In** [Canon + Observed] |
| Gold Digger | BBG launch, May 24, 2013 per wiki ("Coming June 2013!" per the 2013 trailer) | #4 | Yes | 1.5–5.0 s, 7.0–10.0 s, 52.0–54.0 s; screen_03 | None found | PT5 TB | **In** [Canon] |
| Space Oddity | BBR 1.0 as "Spacecraft" | #6 | Yes | 30.0–32.5 s; screen_01 | Fan final-playtest thumbnails 3rLYgfa9OR8, 6sEv1l_IwOs, bK5fDjBfv9c, mkJ2OEiNpFI, q-vHN73-aE4 | PT5 FFA | **In** [Canon] |
| Steam Yard Blues | BBG 2.8 (Mar 4, 2014) | #15 ("Steamyard Blues") | Yes ("Steamyard Blues") | Not shown | Fan final-playtest ORYnnvqn19w hq1–2 (brass gear platforms); Maps Ranked tier tile | PT2 PTB; PT5 FFA ×2, TB | **In** [Canon] |
| H.I.P. Test Lab | BBR 1.0 as "Huggable Factory" | #5, #21 ("Huggable Factory") | No | 34.5–36.5 s; screen_00 | Fan final-playtest ORYnnvqn19w hq3 (white lab, black crates, pink Huggable) | PT2 TB; PT3 TDM | Very likely |
| Aztec Attack | BBR 1.3.1 (Jun 28, 2012) as "Facing Temples" | #13 | No | 12.2–16.3 s, 43.1–45.5 s | Fan PT2 lFr8-yHbbzQ hq1 (sandstone columns under a crimson sky) | PT2 KC; PT3 FFA | Very likely |
| Abusement Park | BBR 1.3.2 (Aug 24, 2012) | #1, #22 | No | 18.0–22.0 s | Teaser hq1 "SAME" panel; fan mobile 5szTpCKfl-c (Sep 20) carnival booth and "[RED]"-style wall | PT3 TDM | Very likely |
| Shortest Parsec | BBR 1.4.2 (Feb 28, 2013) | #9 | No | 24.0–28.0 s, 50.0–51.0 s; screen_02, screen_04 | None identified with confidence (C7uFxvSZ10c hq2 starfield is unidentified) | PT3 TDM; PT5 TB | Very likely |
| Marecraft | BBR 1.4.3 (Apr 15, 2013) / 1.4.3.1 (Apr 23) | #8 | No | 38.5–41.5 s | None. The Q&A thumbnail reuses the 2013 trailer shot | PT2 KC ×2, TB; PT3 TDM ×2; PT5 PTB | Very likely |
| Sky View | BBG launch, 2013 | #3 | No | 48.0–49.0 s | Maps Ranked oar2 background clip (night deck, probably 2026) | PT5 TB | Very likely |
| Skate or Die | BBG launch, 2013 | #7 | No | 46.0–47.0 s | Livestream hq2–3; C7uFxvSZ10c hq1; "Playtest Highlights Part 1" oar2; fan final-playtest ECARJ0b3T-0 | PT2 TB; PT3 FFA | **In** (seen in official 2026 playtest footage) [Observed; map Inference] |
| Desert Airmine | BBR 1.0; cut at the BBG relaunch; back in 2.7 (Jan 23, 2014) | #12 | No | Not shown | Fan HKbwq7PolNc hq1 (derrick, red mesa) | PT3 FFA; PT5 TB ×2, FFA | Likely |
| Haunted Castle | BBR 1.3.3 (Oct 10, 2012); cut at the relaunch; back in 2.4 (Oct 24, 2013) | #11 | No | Not shown | Fan 2iJozU8jTJI hq1 (night, low-res) | PT2 KC; PT5 PTB; dBBG "Haunted Castle FFA" (Sep 25) and TDM (Oct 9) | Likely |
| Frozen Pundra | BBG 2.7 (Jan 23, 2014) | #10 | No | Not shown | "Playtest Highlights Part 2" oar1 (icy blue cave); fan pR3AHrKj3ng (Aug 21); fan MS2wiArCiCA (final) | PT2 TB; PT5 PTB | Very likely |
| Toxic Terror | BBG 2.3 (Sep 27, 2013) | #14 | No | Not shown | Legacy collage tile only | None found | **Unknown** |
| Sky Pirates / Sky World | BB Ultimate (Jun 25, 2014) / Overclock launch map [Fan-wiki] | None | No | Not shown | Reveal and Short frames; teaser "NEW MAP!"; livestream art; fans pR3AHrKj3ng (Aug 21), uNZA3nlABOA (Sep 20), dz4iqZE8nQE and Pd0VvQ1TBRM (final) | PT3 KC ×3, TDM ×2, FFA; PT5 TB ×2, KC; dBBG FFA (Oct 2) | **In (new)** [Canon] |
| Castle Royale | 2018 Battle Royale map [Inference] | #16 | No | Not shown | None | None | Unknown. Battle Royale is not a listed 2026 mode [Canon by absence] |

### 2.3 The "BBG Maps Ranked part 1" grid is not a 2026 roster

The official Short's frame `oar1` shows a presenter with a 4×4 collage of 16 map stills [Observed]. I identified the tiles by matching them against trailer frames, wiki tiles and fan footage:

| Row | Col 1 | Col 2 | Col 3 | Col 4 |
|---|---|---|---|---|
| 1 | No Bear's Land | H.I.P. Test Lab (pink-lit wall, ceiling claw arms, tubes) | **Unidentified**: amber room with a cyan ceiling disc and a sunken floor, probably a second Space Oddity view | Desert Airmine (derrick, sunset, red mesa) |
| 2 | Aztec Attack (temple stairs) | Abusement Park (striped carnival booth with a lit marquee; text illegible) | Haunted Castle (night, dark column, terracotta floor) | Shortest Parsec (station in a starfield with teal asteroids) |
| 3 | Marecraft (fleshy rib arches, dark towers) | Steam Yard Blues (brass and dark-blue glass) | Space Oddity | Frozen Pundra (snow cave, snow-capped rock block) |
| 4 | Skate or Die (lens-eye, mural) | Sky View (yellow crane, teal tarps, night sky) | Gold Digger (stacked rock wall, stars) | Toxic Terror (dark sewer, green puddle, hazard stripes) |

Tile identities are [Observed match]. Tiles 1-3 and 2-3 are [Inference].

The collage cannot stand as a 2026 roster:
- **It has no Sky Pirates tile** [Observed].
- **The same collage is the thumbnail and video frame of a fan's soundtrack uploads** [Observed]. Slinkster's "Battle Bears Gold Soundtrack: No Bears Land" (vzMlV_kGfnU) and "Battle Bears Gold Soundtrack: Toxic Terror" (zQ0g4GLGs5A), both dated Sep 4, 2026, predate the Oct 11 Short.

It is a legacy-map collage [Inference]. Who made it first is unknown.

Frame `oar2` shows a tier list with rows "1-4 / 5-8 / 9-12 / 13-16" [Observed]:
- So far, Sky View, Frozen Pundra and Steam Yard Blues sit in "13-16", with one slot empty.
- The clip behind the tier list is a night-time deck match: wooden planks, a lit building, a dark navy sky, HUD "0 – 0", and player tags "グラハムユウキ" and "SEAL".
- The map is probably Sky View [Inference]. That the clip is 2026 footage is [Inference].

Frame `oar3` is an end card: "COMING NOVEMBER 4" [Observed].

## 3. What changed versus 2013–2021

### 3.1 Map history (added, removed, reworked)

| Date | Version | Event | Label |
|---|---|---|---|
| Oct 8, 2011 | BBR 1.0 | Launch maps: Battlefield Airpad (later No Bear's Land), Huggable Factory (later H.I.P. Test Lab), Spacecraft (later Space Oddity), Desert Airmine | [Fan-wiki] (BBR Version 1.0 page) |
| May 3, 2012 | BBR 1.3 | "NEW Game Mode: "Plant the Bomb"" | [Game text via wiki] |
| Jun 28, 2012 | BBR 1.3.1 | "Awesome New Map - Facing Temples" | [Game text via wiki] |
| Aug 24, 2012 | BBR 1.3.2 | "New Level: Abusement Park" | [Game text via wiki] |
| Oct 10, 2012 | BBR 1.3.3 | "NEW Haunted Castle map with interactive features!" | [Game text via wiki] |
| Oct 20, 2012 | BBR 1.3.4 | "Fixed Abusement Park Skybox" | [Game text via wiki] |
| Feb 28, 2013 | BBR 1.4.2 | "NEW- The Shortest Parsec Map!" | [Game text via wiki] |
| Apr 15 / Apr 23, 2013 | BBR 1.4.3 / 1.4.3.1 | "NEW MAP: The Marecraft! Fight or die inside a giant living unicorn! The goriest battlefield ever!" | [Game text via wiki] |
| May 24, 2013 (iOS) | BBG 1.0 (the wiki's "2.0" relaunch) | See the notes below the table | See notes |
| Sep 27, 2013 | BBG 2.3 | "New Map: Toxic Terror" | [Game text via wiki] |
| Oct 24, 2013 | BBG 2.4 | "Haunted Castle returns as a playable stage" | [Game text via wiki] |
| Nov 27, 2013 | BBG 2.5 | "New Mode: Free-For-All" | [Game text via wiki] |
| Jan 23, 2014 | BBG 2.7 | "New Map: Frozen Pundra". Desert Airmine "re-released in v2.7" | [Game text via wiki]; [Fan-wiki] |
| Mar 4, 2014 | BBG 2.8 | "New Map: Steam Yard Blues"; "New Gamemode: King of the Windmill" | [Game text via wiki] |
| Jan 17, 2017 | BBG 2.26 | "Winter themed map of No Bear's Land" | [Game text via wiki] |
| May 29, 2017 | BBG 2.27 | "Summer themed map of No Bear's Land" | [Game text via wiki] |
| Dec 20, 2017 | BBG 2.28 | "Winter Map is back" | [Game text via wiki] |
| Jan 26, 2018 | BBG 2.29 | "King Of The Windmill is retired" | [Game text via wiki] |
| Mar 28, 2018 | (video) | "New Battle Royale Mode and Map coming in update v2.32!" | [Canon] (bOEK6skhDKU) |
| Apr 5, 2018 | BBG 2.50 | "New Battle Royale mode implented.Winners in gas" [sic] | [Game text via wiki] |
| Apr 13, 2018 | BBG 2.51 | "Spring Theme for No Bear's Land Map." | [Game text via wiki] |
| Apr 28, 2018 | BBG 2.53 | "Bridge to Terabearthia added to the Battle Royale mode." | [Game text via wiki] |
| Nov 15, 2021 | BBG 3.0 | "64-bit engine upgrade that future proofs BBG" … "New Map Lighting" | [Game text via wiki] |
| Mar 12, 2024 | — | "Battle Bears Gold servers have shut down since March 12, 2024" | [Fan-wiki] |
| Aug 21, 2026 | 2026 playtest 3 | "New Map: Sky World" | [Canon] |
| Oct 15, 2026 | 2026 final playtest | "-Lighting improvements" | [Canon] |

Notes on the May 24, 2013 relaunch:
- **Release dates.** The wiki dates the iOS relaunch to May 24, 2013, Android to June 3, 2013 and Windows PC to Dec 20, 2013 [Fan-wiki]. SkyVu's May 30, 2013 trailer description says "Coming June 2013!" [Canon].
- **New maps.** The 2013 trailer says: "3 New Maps: -Gold Digger -Skate or Die -Sky View" [Canon] (rfAyqVJrli4, May 30, 2013).
- **Renames.** Battlefield Airpad became No Bear's Land, Spacecraft became Space Oddity, Facing Temples became Aztec Attack, and Huggable Factory became H.I.P. Test Lab [Fan-wiki].
- **Removals.** Desert Airmine and Haunted Castle were removed "not only because they were the least popular maps, but to also allow more server space" [Fan-wiki] (Desert Airmine and Haunted Castle pages). This quote is not in the 2013 trailer description.

The SkyVu video says Battle Royale was "coming in update v2.32" [Canon]. The wiki log jumps from 2.31 (Mar 8, 2018) to 2.50 (Apr 5, 2018) [Game text via wiki]. A renumbering is plausible [Inference], but I could not check the archived notes [Unverified].

### 3.2 Net change for 2026

- **New: Sky Pirates / Sky World**, ported from BB Ultimate/Overclock [Canon that it is new to BBG; Fan-wiki for the BBO origin].
  - The 2026 frames closely match the wiki's BBO render "SkyPiratesnewlightmappedversion2.2.png", uploaded Sep 9, 2015 [Observed]. Shared features:
    - the clock tower on four stone legs with a red skirt roof;
    - a yellow-trimmed galleon flying a black Jolly Roger;
    - orange-canopy birch trees and white flagstones.
  - BBO was "a first-person multiplayer shooter" with "a completely new art style" [Fan-wiki]. The 2026 map is played in BBG's third person [Observed].
- **Legacy maps:** 14 of 15 are seen in 2026 playtest builds [Unverified: fan chapters]. For 9 of them, the 2026 build is also shown in thumbnails I opened [Observed]. Toxic Terror is unaccounted for [Unverified].
- **Not in the 2026 mode list:** King of the Windmill (already retired in 2018) and Battle Royale [Canon by absence]. Whether Castle Royale or "Bridge to Terabearthia" exist in 2026 is unknown [Unverified].
- **Seasonal No Bear's Land reskins (winter, summer, spring):** no 2026 evidence either way [Unverified].
- **Names:**
  - The store uses "No Bears Land" (no apostrophe) and "Steamyard Blues" (one word) [Canon]. The wiki uses "No Bear's Land" and "Steam Yard Blues" [Fan-wiki].
  - The soundtrack still titles the H.I.P. Test Lab music "Huggable Factory" [Canon].
  - The soundtrack says "Marecraft". The wiki's map page title is "Marecraft (Map)", and its text calls it "Marecraft Arena" [Fan-wiki].
  - Fans in 2026 chapter lists write "H.I.P. Test Lab" / "HIP Lab" and "Steamyard Blues" [Unverified].
- **Build labels seen in 2026 footage** [Observed]:
  - "3.0.0 / 1154576…" on the official Playtest Highlights thumbnail, from playtests 1–2.
  - "3.0.2 / 11545762" in Slinkster's Aug 21 footage (pR3AHrKj3ng).
  - "3.0.3 / 5946270" on the Sky Pirates reveal thumbnail.
  - "3.0.7_2026.11.19_b7 / 12195250" in final-playtest fan footage (dz4iqZE8nQE).
  - The second line repeats across builds (1154576… under both 3.0.0 and 3.0.2), so it is not a per-build hash [Inference].

## 4. Modes

- **2026 store list:** "Team Deathmatch (TDM)", "Free for All (FFA)", "Plant the Bomb (PTB)" [Canon].
  - The same page calls TDM "Team Battle" ("a Team Battle diehard") [Canon].
  - That matches the wiki's legacy name, "Team Death Match(Team Battle)" [Fan-wiki].
- **Kill Confirmed (playtest only so far):**
  - Steam called it "An experimental new gamemode" for the Jul 29 test [Canon].
  - A fan wrote: "This includes some of the first footage of a new mode: Kill Confirmed." [Unverified] (lFr8-yHbbzQ).
  - HUD evidence [Observed]:
    - 1MP1rFi4t-Q hq1 (JustNubz, final playtest) reads "YOU'RE ON TEAM BLUE / COLLECT ENEMY TAGS TO SCORE POINTS".
    - "SCORED" badges appear in the kill feed on Sky Pirates (qt43iTdANbM hq2, Pd0VvQ1TBRM hq1) and on No Bear's Land (lFr8-yHbbzQ hq2).
    - dz4iqZE8nQE hq1 adds a "DENIED" badge.
  - Other matches show "GET KILLS TO SCORE POINTS" [Observed: MS2wiArCiCA hq1, 1MP1rFi4t-Q hq3]. That this is the Team Battle intro line is [Inference].
  - Fans report Kill Confirmed on Aztec Attack, Marecraft, No Bear's Land, Haunted Castle and Sky Pirates [Unverified].
  - It is not on the Steam mode list, so its launch status is unknown [Canon by absence].
  - BBG 2.1 (Jul 15, 2013) listed "Kill confirm Joule drops" [Game text via wiki]. That is a 2013 Joule-drop feature, not this mode [Inference].
- **Which maps support which modes (legacy):**
  - PTB "takes place in the same stages as Team Battle" [Fan-wiki].
  - In FFA, players "spawn in the same points as they would in a team-based Team Battle or Plant the Bomb game" [Fan-wiki].
  - Wiki map pages give Plant the Bomb bomb and tube positions for nine maps: No Bear's Land, H.I.P. Test Lab, Space Oddity, Aztec Attack, Abusement Park, Shortest Parsec, Sky View, Toxic Terror and Desert Airmine [Fan-wiki].
  - They give none for Gold Digger, Skate or Die, Marecraft, Haunted Castle, Frozen Pundra or Steam Yard Blues. That is a gap in the wiki, not proof of absence [Inference].
  - Fan chapters show PTB being played on Steam Yard Blues, Frozen Pundra, Marecraft and Haunted Castle in 2026 [Unverified].
- **Per-map modes seen in 2026:** see the evidence matrix. Every map seen in 2026 appears in TB, FFA, PTB or KC in at least one fan chapter. No source says any map is excluded from any mode [Unverified].
- **Retired modes:**
  - **King of the Windmill** (2.8–2.29): "A single Windmill spawns on the map … Remain in the radius of the Windmill when it launches with one or more team mates to score a point" [Game text via wiki].
  - **Battle Royale** (2.50, Apr 5, 2018): "Winners in gas" [Game text via wiki].

## 5. Visual changes in 2026

- **2021 lighting pass:** BBG 3.0 (Nov 15, 2021) listed "New Map Lighting" [Game text via wiki].
- **2026 lighting pass:**
  - The final-playtest post (Oct 15, 2026) lists "-Lighting improvements" [Canon].
  - Its banner reads "-CUSTOM KEYBINDS", "-MENU JUKEBOX", "-UI CONTROLLER SUPPORT", "-REDEEM CODE SYSTEM", "-ANDROID SUPPORT", "-LOTS OF BUG FIXES", "-LIGHTING, EFFECT & TEXTURE IMPROVEMENTS", and "CLOSED TESTING 5 · THURSDAY, 3PM PDT" [Observed: `img/clan_b7c8f8f1…png`].
  - A fan who played it wrote: "an overhauled lighting for all maps, attempting to restore what they looked like back in the day. No Bear's Land, Desert Airmine, and Space Oddity - all shown in this video - now look almost just like they did when the game first launched as Battle Bears Royale" [Unverified: fan description, HKbwq7PolNc].
- **What the 2026 lighting looks like on No Bear's Land** (Closed Testing 5 banner, probably the final build [Inference]) [Observed; hex values sampled, approximate]:
  - Bright high-noon daylight under a saturated blue sky, about #6391E1 at the top fading to #8FABE9 near the horizon.
  - Lime-olive grass, about #809526, with white daisy specks.
  - Trench lips of orange earth, about #A06923.
  - An olive concrete keep, about #5A5735, with saturated royal-blue team stripes (about #4541E9; not the sky-like #6B94E9 an earlier sample gave), a vertical "PMOC 20-11" stencil, and a shield pickup on the roof.
  - The central pillar holds the angry brown bear-face Bearscream Sandwich. It matches the wiki model image `Bearscream_Sandwich.jpg` [Observed match]. The wiki places the sandwich on this pillar [Fan-wiki].
  - Sandbags, steel hedgehogs, and a dark crashed craft with a red stripe sit to the right. The wiki calls the craft a crashed Pelican't [Fan-wiki].
- **The trailer and screenshots are not 2026 renders:**
  - The trailer's Graham (~11 s), Tillman (~29 s) and Oliver (~42 s) cards are identical to the auto-thumbnails hq1/hq2/hq3/maxres of the official May 30, 2013 trailer "BATTLE BEARS GOLD Trailer: Award-Winning Multiplayer Shooter Game" [Observed: `sheets/tr2013.jpg`].
  - Its eight class cards match the 2013 description's "Choose from 8 classes" [Observed; Canon].
  - It shows no map added after BBG's launch: no Toxic Terror, Frozen Pundra, Steam Yard Blues or Haunted Castle [Observed].
  - It has no card for Botch, Saberi or Sanchez, who were added Jul–Dec 2013 [Observed; Game text via wiki dates].
  - The Q&A thumbnail (pmE2jKQLSms, Oct 12, 2026) is the same gold Oliver in the same pose, over the trailer's Marecraft plate [Observed: `sheets/qa_vs_trailer.jpg`].
  - So the trailer and screenshots are 2013 BBG capture [Inference]. The Oct 14 request for UI-free footage "for our Steam and store pages" suggests they will be replaced [Inference].
- **Jukebox:** a fan says songs "you can even assign … to maps" [Unverified]. So a map's in-game music may not be fixed in 2026 [Inference].

## 6. Frame by frame: the official Steam trailer and screenshots

**Source.** "Battle Bears Gold Premium - Trailer", 54.0 s [Canon title].
- I opened contact sheets of all 108 frames `t_0001`–`t_0108` (nominally t_N = (N−1)×0.5 s) and 13 full-resolution frames.
- Scene detection puts the real cuts up to ~0.25 s after the nominal times. Examples: Aztec Attack starts at 12.22 s, Abusement Park at 17.85 s, the Shortest Parsec exterior at ~23.9 s, Space Oddity at 30.02 s, H.I.P. Test Lab at 34.25 s, Marecraft at 38.32 s, the Aztec aerial at 43.09 s.
- So treat all times as ±0.5 s.

| Time (s) | Frames | Content | Map identification and visible landmarks |
|---|---|---|---|
| 0.0–1.0 | t_0001–0003 | Title card "BATTLE BEARS GOLD" over flames | — |
| 1.5–5.0 | t_0004–0011 | B-1000 in a rock-walled bowl; full moon and stars from ~4 s | **Gold Digger**: stacked charcoal rock walls, timber railings, dirt floor, large boulder, moon [Observed] |
| 5.5 | t_0012 | White flash | — |
| 6.0–6.5 | t_0013–0014 | Card "B-1000 / ASSAULT" | — |
| 7.0–10.0 | t_0015–0021 | Graham fires toward a timber-shored tunnel mouth; blue gem in the wall; big white burst with lightning | **Gold Digger** tunnel [Observed]. The wiki says the map has "mining carts filled with gold and team-coloured jewels to indicate which spawn point the player is in" [Fan-wiki]. **screen_03** = 9.8 s |
| 10.5 | t_0022 | White flash | — |
| 11.0–11.5 | t_0023–0024 | Card "Graham / ENGINEER" | — |
| 12.2–16.0 | t_0025–0033 | Low angle up a temple's grand staircase; small figure at the top; a player knocked down; magenta cloud from ~14 s; Astoria in the cloud ~16 s | **Aztec Attack**: carved sandstone stairs, gem-mosaic panels, colonnades, starry crimson-to-indigo sky [Observed] |
| 16.5–17.5 | t_0034–0036 | Card "ASTORIA / SNIPER" | — |
| 18.0–22.0 | t_0037–0045 | Wil (holding a "BATTERITO" snack) panics and is blown up; panda-faced bomber; pan along the base | **Abusement Park** red base [Observed]: salmon plank deck; yellow U-rails; red-and-teal pennant bunting; two blue posters of a spiky ice-or-rock-armoured figure; cracked grey stone wall stencilled "[RED]" with red stars; maroon-and-white striped tent; overhead cable. The wiki mentions "2 duplicate posters of a Soldier skin that never made it in the game" [Fan-wiki]; that these are those posters is [Inference] |
| 22.5–23.5 | t_0046–0048 | Card "Wil / CHUB SCOUT" | — |
| 24.0–25.5 | t_0049–0052 | Camera rides in on a **yellow bomb marked with a black radiation trefoil, with an olive tail**, toward a white-and-red space station; teal asteroids with hexagonal holes float nearby | **Shortest Parsec** exterior: modular white-red station with red roundel emblems, cyan-teal asteroids, purple-blue starfield [Observed: `tf/f_24.0.jpg`, `tf/f_25.5.jpg`]. The foreground object is not an asteroid [Observed] |
| 26.0–28.0 | t_0053–0057 | Interior firefight; huge yellow blast; Tillman close-up under blue-white arches | **Shortest Parsec** interior: red angled ceiling panels, pinkish-white walls, red-lit door on the left and violet-lit door on the right, a yellow radiation bomb [Observed]. **screen_04** = 26.4 s |
| 28.5–29.5 | t_0058–0060 | Card "TILLMAN / DEMO" | — |
| 30.0–32.5 | t_0061–0066 | Huggable ambushes a sniper by the central podium | **Space Oddity**: octagonal dark podium with a glowing top under a cyan ceiling emitter, amber windows onto space, teal neon pipe frames, Huggable-face crates, flame-jet jump pad [Observed]. **screen_01** = 30.7 s |
| 33.0–34.0 | t_0067–0069 | Card "Huggable / HUGGABLE" | — |
| 34.5–36.5 | t_0070–0074 | Rock-skinned Riggs fires down a white corridor, then punches a gold bear | **H.I.P. Test Lab**: white walls and floor; magenta-lit upper room with stacked Huggable-face speakers; vertical rainbow banner; pink Huggable figurines; blue-lit doorframe; pillar with two blue up-arrows; dark ceiling claw arm; cyan jump pad [Observed]. **screen_00** = 36.4 s |
| 37.0–38.0 | t_0075–0077 | Card "RIGGS / HEAVY" | — |
| 38.5–41.5 | t_0078–0083 | Firefight on a dark ledge | **Marecraft**: huge orange-red rib arches with veins, red flesh floor, dark battlements, a dark tower topped with a satellite dish, a grey segmented piston column [Observed: `tf/f_40.5.jpg`] |
| 41.5–42.5 | t_0084–0086 | Card "Oliver / SOLDIER" (gold swirl Oliver) | — |
| 43.1–45.0 | t_0087–0091 | High aerial | **Aztec Attack**: island plateau in a lava sea; central lava pool with a stacked obsidian rock; two temples with red-glowing panels; carved face cubes; stubby pillars; cyan jump pads [Observed] |
| 45.5 | t_0092 | Crossfade | Aztec Attack → Skate or Die |
| 46.0–47.0 | t_0093–0095 | Aerial | **Skate or Die** [Observed: `tf/f_46.5.jpg`]: concrete plaza with massive dark concrete pillars; giant blue camera-lens "eye" beside blue "ABBi" graffiti; rainbow graffiti; red "Oops, Killed ya!" graffiti on a pillar; painted water channel with an orange goldfish; green-meadow mural with pink Huggables; wooden ramps and grind rails |
| 47.5 | t_0096 | Crossfade | → Sky View |
| 48.0–49.0 | t_0097–0099 | Aerial | **Sky View**: rooftop deck of red I-beams and black grating; wooden plank walkways; teal tarp panels; surrounded by tall building facades with lit windows; white smoke puffs [Observed: `tf/f_48.5.jpg`]. **No sky is visible in this shot.** Night is seen only in the Maps Ranked tile (yellow crane under a dark navy sky) and the oar2 clip [Observed] |
| 49.5 | t_0100 | Crossfade | → Shortest Parsec |
| 50.0–51.0 | t_0101–0103 | Aerial over the station; big white-yellow blast | **Shortest Parsec** [Observed]. **screen_02** = 50.6 s |
| 51.5 | t_0104 | Crossfade | → Gold Digger |
| 52.0–54.0 | t_0105–0108 | Aerial | **Gold Digger** [Observed: `tf/f_53.0.jpg`]: twin black pits split by a narrow stone ridge (the wiki: "a bridge in the middle … If you fall off the bridge, and into a black pit, you will suicide" [Fan-wiki]); ring of dirt; gold-filled mine cart; boulders; timber railings; cyan jump pads ringed in yellow-black hazard stripes; a glowing amber box; an expanding orange octagonal ring effect (cause unidentified) |

**Map count:** 9 maps [Observed]:
- Gold Digger (3 shots)
- Aztec Attack (2)
- Shortest Parsec (3: exterior, interior and aerial)
- Abusement Park, Space Oddity, H.I.P. Test Lab, Marecraft, Skate or Die and Sky View (1 each)

The trailer never shows No Bear's Land, Desert Airmine, Haunted Castle, Toxic Terror, Frozen Pundra, Steam Yard Blues or Sky Pirates [Observed].

**Steam screenshots (all 1920×1080).** Each matches a trailer frame. I checked this with a greyscale mean absolute difference at 192×108 against 540 trailer frames at 10 fps; for every screenshot the next-best frame scores 3–4× worse. I also compared them by eye.
- **screen_00:** H.I.P. Test Lab, matches 36.4 s (difference 3.9).
- **screen_01:** Space Oddity, matches 30.7 s (6.1).
- **screen_02:** Shortest Parsec aerial, matches 50.6 s (13.5).
- **screen_03:** Gold Digger tunnel, matches 9.8 s (13.0).
- **screen_04:** Shortest Parsec interior, matches 26.4 s (12.9).

All five are [Observed]. No screenshot shows No Bears Land or Steamyard Blues, even though the store names both [Observed].

## 7. Other official 2026 images, identified

- **Steam clan image b7c8f8f1…png ("Closed Testing 5", Oct 14):** No Bear's Land in the 2026 build. Details in section 5 [Observed].
- **Steam clan image 3b7f9b97…png ("Closed Testing", Jul 6):** class line-up on a fire background, "THURSDAY, 4PM PDT". No map [Observed].
- **Steam clan image 282237bb…png (Feb 24):** logo and icon only [Observed].
- **Steam clan image 60061117…png (referral rewards, Oct 14):**
  - It shows a dark stepped pyramid with a central staircase, glowing green outlines, green square-spiral glyph panels and two glowing eyes at the top, under a smoky sky [Observed].
  - It closely matches the wiki image Uumhfc.jpg, a stepped pyramid with green square-spiral glyphs [Observed comparison]. The Aztec Attack page captions that image "The pyramid where the Zombocalypse stood" and adds "The Aztec Attack's pyramids resembles the pyramid where Zombocalypse stood" [Fan-wiki].
  - The 2013-era Aztec Attack temples in the trailer have gem-mosaic panels, not green spirals [Observed].
  - It is not identifiable as a BBG map. Whether it is a 2026 Aztec Attack temple is [Unverified].
- **Official Playtest Highlights (C7uFxvSZ10c, footage from playtests 1–2):**
  - maxres: gold Oliver on a round concrete tower top above green fields and olive keeps. HUD "10 – 10", tag "Dued", stamp "3.0.0" [Observed]. The map is No Bear's Land [Inference].
  - hq1: concrete plaza with wooden skate ramps and a large pillar, tag "Cinnamon" [Observed]. Probably Skate or Die [Inference].
  - hq2: Wil in a starfield beside an orange-and-slate panelled block with a magenta-red top, tag "CiedC4" [Observed]. Map unidentified; Shortest Parsec is possible [Unverified].
  - hq3: Ben Vu talking. No map.
- **Teaser (d2ByJWrsoec, Oct 2):**
  - hq1: three panels captioned "SAME / ICONIC / GAMEPLAY". The "SAME" panel shows red stencil lettering and a red star on grey stone above a tan deck with a railing [Observed]. That matches the Abusement Park red base [Inference].
  - hq2: "NEW MAP!" over gold swirl Oliver. The backdrop has rust-orange low-poly canopies, a white cottage with a red-brown roof, a wooden fence on a grassy slope and soft clouds [Observed]. That this is Sky Pirates is [Inference].
  - hq3 and maxres: end card and title card. No map [Observed].
- **Sky Pirates reveal (r91WkR10W2A):** maxres and hq1–3 all show Sky Pirates. Player tags "INSTABLEGR" and "JUSTIN BER…" show it is playtest match footage [Observed]. Details in section 8.
- **"Sky Pirates in BBG!" Short (CwxpBZg6Fi4):**
  - hq1: a steep yellow-trimmed galleon hull with a rope, a player standing on it, tag "M1KAA717" [Observed].
  - hq2: the island village with red roofs, orange trees and a white rock outcrop [Observed].
  - maxres: "NEW MAP?" over the clock tower [Observed].
  - hq3: an end card.
- **Official livestream, Sep 20 (ejjsoKQ-VXU):**
  - maxres: "LIVESTREAM" art over a Sky Pirates village backdrop (orange birch trees, red-roofed cottages, white tower) [Observed].
  - hq1: the mobile main menu [Observed].
  - hq2: Skate or Die, with the giant lens-eye and a "…TLE BEARS" billboard [Observed].
  - hq3: Skate or Die wooden ramps and concrete [Observed].
  - The HUD is the mobile touch layout [Observed].
- **"Playtest Highlights" Shorts:** fan playtester name tags (DUED, CINNAMON, INSTABLEGR, M1KAA717, HUBBLE) mark these as 2026 Discord-playtest footage [Observed; Inference].
  - oDZdTN7M0-E (Part 1):
    - oar1: green field with daisies, an olive structure and a crashed craft. Probably No Bear's Land [Inference].
    - oar2: concrete overpass, skate rail and a "BATTLE BEARS" sign. Probably Skate or Die [Inference].
  - SZZ38et45Xs (Part 2):
    - oar1: icy blue cave with a 1:57 timer. Frozen Pundra [Inference].
    - oar2: green corrugated container walls. Unidentified.
  - NnjUom5NFC4 (Pt 3): oar1 and oar2 are unidentified [Unverified].
- **"BBG Maps Ranked part 1" (jkv6FHPghx8):** see section 2.3.
- **"Q&A with the Creator" (pmE2jKQLSms):** the maxres is the 2013 trailer's Oliver-on-Marecraft shot with question captions [Observed]. It is not 2026 footage.

## 8. New map: Sky Pirates ("Sky World")

### Official text
- "3rd Discord Playtest this Friday! A New Map comes to BBG!" … "This version contains: Auto matchmaking New Map: Sky World Bug fixes" [Canon] (Steam news, Aug 19, 2026).
- "Battle Bears Gold 2026 - Sky Pirates Map Reveal": "BBG LAUNCHES NOV 4 on Steam & Mobile. Gameplay highlights from the new Sky Pirates map!" [Canon] (YouTube r91WkR10W2A, Aug 31, 2026).
- "Sky Pirates in BBG!  #battlebears #wishlist #steam": "Enjoy the highlights from our Sky World playtest!" [Canon] (YouTube CwxpBZg6Fi4, Sep 7, 2026).
- On-screen text: "NEW MAP?" on the reveal thumbnail, and "NEW MAP!" in the teaser [Observed].
- BBO-era game text: "Upgraded Map Lighting, check out how Skyworld has benefitted!" (BBO 3.0, Jul 3, 2020) [Game text via wiki].
- BBO-era wiki text: "Sky Pirates is one of the six launch maps in Battle Bears Overclock." "It is an Island/Autumn themed map." Trivia: "Pirate ships fly around the map" [Fan-wiki].

### Era and status
- **Origin: a v1.0 launch map of Battle Bears Ultimate / Overclock** [Fan-wiki].
  - The wiki dates BBU's launch to June 25, 2014 and Overclock's App Store release to February 10, 2016.
  - It says "As of version 2.2, the Sporest, Sky Pirates, Neo-Omaha and Cupcake Coliseum maps were all redesigned from their original versions" [Fan-wiki].
- **Wiki images:** the three concept-art files were uploaded on Jul 13, 2014. "SkyPiratesnewlightmappedversion2.2.png" was uploaded on Sep 9, 2015 [Observed: wiki file timestamps].
- **Never in BBG 2013–2021:** it is in no BBG update entry and not in Category:BBG Maps [Fan-wiki, by absence].
- **Added to BBG** for playtest 3, Aug 21, 2026 [Canon].
  - Fan footage shows it in the Aug 21 build (pR3AHrKj3ng hq3, stamp "3.0.2"), the Sep 20 build (uNZA3nlABOA hq1) and the final Oct 15 build (dz4iqZE8nQE, Pd0VvQ1TBRM) [Observed thumbnails].
- **Modes seen in 2026:** Team Battle/TDM, Kill Confirmed and FFA [Unverified: fan chapters PT3, PT5, dBBG]. Kill Confirmed is also visible as "SCORED" / "DENIED" badges over Sky Pirates scenery [Observed]. PTB is not documented [Unverified].
- **2026 status:** in the game [Canon]. It is not named in the store text [Canon by absence] and has no soundtrack track [Canon by absence].

### Setting
- A floating autumn island in the sky [Observed: r91 maxres and hq3; CwxpBZg6Fi4 hq1–2]. It holds:
  - a small storybook village;
  - a central stilted clock tower;
  - wooden sailing galleons moored or hovering alongside.
- The BBO wiki calls it "Island/Autumn themed" [Fan-wiki].
- The BBO concept art shows a floating rock island with dangling roots and a rope ladder. Its notes read "roots, maybe same branches with leaves" and "small waterfall?" [Observed handwriting on wiki concept art; partly legible].
- A blue, water-like expanse shows beyond the island edge (about #4B93B2) [Observed: r91 maxres, VHo1O41RNJE maxres]. Whether it is sea or sky is [Unverified].

### Layout
- **Overall shape:** an open, grassy, gently rolling island top with scattered white flagstone paving [Observed].
- **Centre:**
  - A white stone clock tower stands on four short stone legs, with open space beneath it and a red skirt roof below the clock [Observed: r91 maxres; BBO render].
  - The Bearscream Sandwich (angry brown bear-face ice-cream sandwich) floats at the tower's foot [Observed: matches the wiki model image]. The sandwich "doubles the damage of all the player's weapons for 20 seconds" [Fan-wiki: Bearscream Sandwich page; the Pick-Ups page says "Triples"].
- **Around the centre:** half-timbered cottages with white walls and red roofs, orange-and-white striped market awnings, and a white rock outcrop with a flat grassy top [Observed: r91 hq2, CwxpBZg6Fi4 hq2].
- **Edges:**
  - Galleons sit beside the island at deck height, and wooden docks and fences run along the edge [Observed].
  - A player stands on a steep yellow-trimmed hull with rope rigging [Observed: CwxpBZg6Fi4 hq1]. That the ships add a walkable raised level is [Inference].
- **Bases and spawns:** red/blue sides and spawn locations are not documented [Unverified].
- **BBO comparison:**
  - The BBO ship sheet notes "animate flag, and also maybe these four?", "As billowy as possible! a looping animation of flapping in the wind would be ideal" and "cannons facing main island" [Observed handwriting; partly legible].
  - Whether the 2026 ships move, as the wiki says BBO's did, is [Unverified].

### Look
- **Palette:** hue-filtered medians from r91WkR10W2A maxres, approximate [Observed]:

  | Element | Hex |
  |---|---|
  | Lit autumn canopies | #F55B14 |
  | Canopies in shade | #7D2D0B |
  | Red clay roofs | #B03134 |
  | Grass (olive, low saturation) | #868132 |
  | Sky | #D4EBF6 |
  | Sea or sky below | #4B93B2 |
  | White stone and plaster | #E7EEEB |
  | Hull wood | #4D301D |
  | Hull trim (yellow) | #E0C04B |

- **Lighting:** bright, high-key, hazy daylight. The sun bloom sits at the right of the reveal thumbnail and shadows are soft [Observed]. This is pre-Oct-15 footage (build 3.0.3), so the final lighting may differ [Inference]. The exact time of day is not documented [Unverified].
- **Materials and props** [Observed]:
  - white birch trunks topped with round, faceted, low-poly foliage clumps;
  - galleon hulls with yellow trim and cannon ports, masts with furled off-white sails, a crow's nest and rope rigging;
  - small wooden rowboats;
  - striped awnings.
- **Weather and particles:** none documented [Unverified].

### Landmarks
1. **The stilted clock tower:** white stone, steep red roof, red skirt roof, round grey-white clock face with black hands [Observed].
2. **The pirate galleons:** yellow-trimmed hulls, cannon ports, furled sails, moored at the island edge [Observed].
3. **The Jolly Roger:** a tattered black flag with a white, angry-eyed bear head (like the BBG icon) over crossed cutlasses [Observed: `img/sp_flag.png`].
4. **Orange-canopy trees** on white birch trunks across the lawn [Observed].
5. **The village:** red-roofed, half-timbered cottages and striped stalls [Observed].
6. **The white rock outcrop** with a grassy cap [Observed].

### Hazards and interactive elements
- None are documented for 2026 [Unverified].
- Falling off the edge is plausibly a "suicide", as on Sky View ("If you fall into the city, you will suicide") and Shortest Parsec [Fan-wiki for those maps]. For Sky Pirates this is [Inference] only.

### Easter eggs and references
- The bear-head Jolly Roger [Observed].
- The name continues the 2014 BBO map [Fan-wiki].
- Nothing else is documented [Unverified].

### Sound and music
- The 2026 soundtrack lists no Sky Pirates track [Canon by absence]. Which music plays on it is [Unverified].
- BBO 1.2 had "New map music for forest", but nothing names Sky Pirates music [Game text via wiki].
- The 2026 Jukebox reportedly lets players assign songs to maps [Unverified: fan].

### Images viewed
All paths are under `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/lineup_verify/`:
- `th/r91WkR10W2A_maxresdefault.jpg`, crop `img/sp_flag.png`, crop `img/stamps2.png`.
- `sheets/r91_cwx.jpg`: r91 hq1–3 and hqdefault; CwxpBZg6Fi4 hq1–3 and maxres.
- `sheets/teaser_c7.jpg` and `sheets/c7_zoom.jpg` (teaser hq2).
- `sheets/live.jpg` (livestream maxres).
- `sheets/sp_bbo.jpg`: the three Concept_art_of_Sky_Pirates images and SkyPiratesnewlightmappedversion2.2.png.
- Fan frames: `sheets/fanA.jpg` (pR3AHrKj3ng), `sheets/fanB.jpg` (DEDQ517trWM, 0TAvVT52u1E, pIMGF9eDjCw, VHo1O41RNJE, qt43iTdANbM), `sheets/fanC.jpg` (uNZA3nlABOA), `sheets/fanD2.jpg` (Pd0VvQ1TBRM, dz4iqZE8nQE), and `img/final_stamp2.png`.
- `wimg/Bearscream_Sandwich_v.jpg`.

### Prompt pack

**Establishing shot (9:16, environment only, style-neutral):**

> Vertical 9:16 high three-quarter establishing shot of a small floating grassy island in a pale, hazy sky. Centre frame: a slim white-stone clock tower with a steep red clay roof, a red skirt roof below a round grey-white clock face with black hands, raised on four short stone legs above a lawn scattered with white flagstones. Around it: half-timbered cottages with white walls and red roofs, a striped orange-and-white market awning, a white rock outcrop with a grassy flat top, and clumps of round, faceted burnt-orange autumn canopies on thin white birch trunks. At the island edge, a wooden sailing galleon with a yellow-trimmed hull, cannon ports, furled off-white sails, a crow's nest and rope rigging sits beside a plank dock with a small rowboat. A tattered black flag with a white bear head and crossed cutlasses flies from its mast. Below and beyond, a blue expanse fades into haze. Bright soft daylight, chunky low-poly geometry, saturated colour. No characters, no readable text or logos.

- The camera height, the single-galleon framing and the rowboat placement are [BBG News invention].
- Everything else is [Observed].
- The flag's bear head is in-game iconography and reads as an emblem, not text. Keep it.

**Staging spots:**
1. **Under the clock tower's stilts.** The Bearscream Sandwich spawns here [Observed]. Stage a standoff or a "grab the sandwich" race [staging: BBG News invention].
2. **The steep galleon hull.** A boarding-party gag or a chase up the slope [Observed: a player on the hull; staging: BBG News invention].
3. **The dock at the island edge.** A "walk the plank" bit with a drop into the blue haze [the drop and the gag are BBG News invention].

### Confidence
- Look and landmarks: observed.
- Layout, spawns and hazards: unknown.
- Overall: partial.

## 9. Quick palettes for the rest of the lineup (approximate)

Method: medians of hue-filtered pixels in the cited image. Values I re-sampled in this pass are marked; the rest are earlier samples, spot-checked against my own runs and found close. Read all values as approximate.

| Map | Source and era | Key colours |
|---|---|---|
| No Bear's Land | CT5 banner, **2026** (re-sampled) | sky #6391E1→#8FABE9, grass #809526, trench earth #A06923, olive keep #5A5735, royal-blue team trim #4541E9 |
| Gold Digger | trailer 4.0 s and 53.0 s, 2013 footage (re-sampled) | night sky #001A2E, moon #BFD6E5, rock #302B2A (deep shadow ~#130C0C), dirt #3D2A14, gold #FFD85D, cyan jump pads #26C0E1 |
| Space Oddity | screen_01, 2013 footage (re-sampled) | amber windows #B7742D, teal neon #29E1C5, khaki floor #89773D |
| H.I.P. Test Lab | screen_00, 2013 footage (re-sampled) | white walls #C8BFC0, dark magenta upper room #34012A, electric-blue trim #032CE3 |
| Aztec Attack | trailer 13.0 s and 44.0 s, 2013 footage (re-sampled) | sky #35072F→#6D0C34, lava #FFAF13, sand #7F3918, obsidian #2B130B |
| Abusement Park | trailer 18.0 s, 2013 footage (re-sampled) | plank deck #FC9473, "[RED]" stencil #FA1A11, U-rails #FFC625; tent maroon ~#530700, night sky ~#180519 (earlier sample) |
| Shortest Parsec | screen_02, 2013 footage (re-sampled) | space #1A113B, red panels #E91D25, white panels #FFFFFF |
| Marecraft | trailer 40.5 s, 2013 footage (re-sampled) | flesh walls #ED551C, flesh floor #FF402D, battlements #331D19 |
| Skate or Die | trailer 46.5 s, 2013 footage (re-sampled) | concrete #494247, water #345265, ramp wood #F4904D, mural green #2A8510 |
| Sky View | trailer 48.5 s, 2013 footage (re-sampled) | girders #6A1B18, planks #9A613C, tarps #07666C, facades #A28172 |
| Steam Yard Blues | wiki Steamyard.png (uploaded Apr 6, 2014; re-sampled) | brass #AF8637, slate-blue biplane #2E4959, wood #79481D, dusky violet sky #3E2430. A 2026 fan frame gives brass #CC9B33 |
| Frozen Pundra | fan pR3AHrKj3ng maxres (Aug 21, 2026; re-sampled) | ice #419FD4, deep ice #193D62, snow #F5FCFC |
| Desert Airmine | fan HKbwq7PolNc hq1 (final playtest, low-res; re-sampled) | sky #9BB8C7, mesa #835E4A |
| Haunted Castle | fan 2iJozU8jTJI hq1 (2026, low-res; re-sampled, small sample) | night #121526, walls #212119, terracotta #43241D |
| Toxic Terror | wiki Toxic-Terror-Preview.png (uploaded Nov 19, 2013; re-sampled) | glowing ooze green #1F9D36, dark sewer #1A261A |
| Sky Pirates | official reveal, **2026** | see section 8 |

Caution: everything marked "2013 footage" predates the 2021 and 2026 lighting passes [Game text via wiki; Canon]. Treat those values as the classic look, not verified 2026 values [Inference].

## 10. Images viewed (exact files)

All relative paths are under `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/lineup_verify/`.

**Official (Steam), opened with Read:**
- Store screenshots `img/ss_0.jpg`–`img/ss_4.jpg`; Soundtrack store images `img/ost_ss0.jpg`, `img/ost_ss1.jpg`.
- Trailer contact sheets `sheets/tr_0.jpg`–`tr_5.jpg`, covering all 108 frames of `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/trailer/t_0001.jpg`–`t_0108.jpg`.
- Full-resolution trailer frames `tf/f_12.0.jpg`, `f_18.0.jpg`, `f_21.0.jpg`, `f_24.0.jpg`, `f_25.5.jpg`, `f_39.5.jpg`, `f_40.5.jpg`, `f_44.0.jpg`, `f_46.5.jpg`, `f_48.5.jpg`, `f_53.0.jpg`.
- Announcement images `img/clan_b7c8f8f133ad960899cce9f3d232b42847891d08.png` (plus crop `img/ct5_keep_crop.png`), `img/clan_60061117627037f3508ed7eb899ff08e7f7720a9.png`, `img/clan_3b7f9b97cdb4f799bbc696475d327f4d7c7a9523.png`, `img/clan_282237bbf3e28853d621b030f8c6fcc574430b3d.png`.

**Official (YouTube), opened with Read:**
- `sheets/tr2013.jpg`: rfAyqVJrli4 maxres and hq1–3 against t_0001, t_0024, t_0059, t_0086.
- `th/r91WkR10W2A_maxresdefault.jpg`; `sheets/r91_cwx.jpg`; `sheets/teaser_c7.jpg`; `sheets/c7_zoom.jpg`; `img/c7_stamp.png`; `img/teaser_same.png`.
- `sheets/live.jpg` (ejjsoKQ-VXU and pmE2jKQLSms); `th/pmE2jKQLSms_maxresdefault.jpg`; `sheets/qa_vs_trailer.jpg`.
- `th/jkv6FHPghx8_oar1.jpg`; `img/jkv6_grid.jpg`; `sheets/jkv6_oar23.jpg`.
- `sheets/shorts_oar.jpg` (oDZdTN7M0-E, SZZ38et45Xs, NnjUom5NFC4 oar1–3).
- bOEK6skhDKU maxres and hq1–3 (in `sheets/fanC.jpg`).

**Wiki, opened with Read:**
- `wimg/Bearscream_Sandwich_v.jpg`, `wimg/A_life_upside_down_v.jpg`, `wimg/Uumhfc_v.jpg`.
- `sheets/sp_bbo.jpg` and `sheets/tt_syb.jpg` (Toxic-Terror-Preview.png, Steamyard.png, plus fan ORYnnvqn19w hq1).

**Fan (2026), opened with Read:**
- `sheets/slink.jpg` (vzMlV_kGfnU, zQ0g4GLGs5A).
- `sheets/fanA.jpg` (1MP1rFi4t-Q, HKbwq7PolNc, pR3AHrKj3ng); `sheets/fanB.jpg`; `sheets/fanC.jpg` (-lAtv-j9Sms, uNZA3nlABOA, lFr8-yHbbzQ, _R4rvvGlRsM); `sheets/fanD1.jpg`; `sheets/fanD2.jpg`; `sheets/tut.jpg` (lgd9Gqw6ahA).
- Crops `img/bka_ap.png`, `img/stamps.png`, `img/stamps2.png`, `img/kc_hq3_text.png`, `img/final_stamp.png`, `img/final_stamp2.png`.
- The JustNubz showcase (-lAtv-j9Sms) thumbnails show only loadout and menu screens, with no map [Observed].

## Confidence

- **Partial overall.**
- The new map and the four store-named maps are documented [Canon].
- Trailer and screenshot identifications are observed.
- The 2026 presence of the other legacy maps rests on fan chapter text, plus 2026 thumbnails for most of them.
- Toxic Terror and Castle Royale are unknown.
- Only No Bear's Land and Sky Pirates have official 2026 images good enough to describe the 2026 look in detail.

## Corrections to our notes

1. **bbg-news-repo/content/evergreen.json (fact-playtests):** "4 PLAYTESTS DOWN" / "Four Discord playtests, July to September 2026" / "SkyVu ran four … playtests … between July and September 2026" → there were five; the final one ran Thursday, Oct 15, 2026, on Windows, iOS and Android (Steam news, Oct 14, 2026).
2. **Same file:** "Playtest 3 added a new map: Sky World" → add that SkyVu's reveal calls it "Sky Pirates" (reveal video Aug 31, 2026; Short "Sky Pirates in BBG!": "Enjoy the highlights from our Sky World playtest!").
3. **animation_reference.md:150:** "lava/orange caverns and rocky caves" → the lava is open-air Aztec Attack; the orange-red interior is Marecraft; the rock is Gold Digger, a moonlit open-roofed mine with timber tunnels. The footage is 2013, not 2026.
4. **franchise_world.md:227:** "It returns in the 2026 BBG as …" → Sky Pirates is new to BBG in 2026; it was a BBU/BBO map (2014–2016, also BBO 3.0 in 2020), never in BBG 2013–2021, and entered BBG at playtest 3 (Aug 21, 2026).
5. **oliver_riggs_wil.md:252:** "Whether these are the same map is my [INFERENCE]; no source says so." → SkyVu's own Short pairs the two names, BBO 2020 notes use "Skyworld", and fan chapters for the Aug 21 test say "Sky Pirates"; a strong [Inference].
6. **Lore report, line 29 (teaser frames):** add that hq2's "NEW MAP!" backdrop is probably Sky Pirates and hq1's "SAME" panel matches the Abusement Park red base [both Inference]; cite hq2 alongside hq1.
7. **Lore report, line 29 ("Steam (Windows and Mac)"):** Steam lists Windows only (`mac: false`); a Mac requirements block exists but Mac is not a supported platform.
8. **research_gold-digger.md:56:** the 16-tile Maps Ranked collage is a legacy collage, not the 2026 roster; use the Steam text naming Gold Digger.
9. **research_frozen-pundra.md:42 and 223:** the collage is not roster evidence; cite the fan PT2/PT5 chapters and the official "Playtest Highlights Part 2" Short (SZZ38et45Xs oar1, icy cave, 2026 playtest footage).
10. **research_marecraft-map.md:48:** fan chapters put Marecraft in PT2, PT3 and PT5; also, the Q&A thumbnail reuses the 2013 trailer shot.
11. **research_haunted-castle.md:239:** "unknown" → likely in (fan PT2/PT5 chapters; droid BBG uploads).
12. **research_desert-airmine.md:35–37:** add the PT5 chapters and InstableGR's lighting note; the PT3 Part 2 upload is dated Aug 21, 2026, not "about Sep 2026".
13. **research_abusement-park.md:62:** add the PT3 chapter, the Sep 20 mobile thumbnails (5szTpCKfl-c) and the teaser "SAME" panel.
14. **research_aztec-attack.md:54:** the "2026 trailer" is 2013 footage, so the 2021 lighting pass cannot explain its look.
15. **research_shortest-parsec.md:168 (and the line-400 open question):** the "2026 trailer" is 2013 footage.
16. **research_skate-or-die.md:84:** replace the collage with the official 2026 playtest-footage images.
17. **research_sky-view.md:63:** collage note; add the PT5 chapter.
18. **research_toxic-terror.md:64:** the collage is not roster evidence; no 2026 sighting; status unknown.

## Open questions

1. What is SkyVu's actual list of the "16 wacky maps"? Is Toxic Terror in it? Is the 16th slot Sky Pirates, or could Castle Royale or another map count?
2. Does the Oct 19–26 Steam demo ship with a fixed map pool, and which maps are in it?
3. Is Kill Confirmed a launch mode?
4. Does Sky Pirates support Plant the Bomb? Where are its team spawns and pickups? Do its galleons move, as in BBO?
5. Which music plays on Sky Pirates? Can the Jukebox reassign map music at launch?
6. Do the seasonal No Bear's Land reskins return in 2026?
7. Is "Castle Royale" the 2018 Battle Royale castle map? Does Battle Royale or "Bridge to Terabearthia" survive in any form?
8. What does the Oct 15 lighting pass change on each map?
9. Will SkyVu replace the 2013-footage Steam trailer and screenshots with 2026 captures?
10. What is tile row 1, column 3 of the Maps Ranked collage? Who made the collage, and what is the final ranking?
11. What did the Sep 20 livestream "map tour" and the Oct 12 "Q&A with the Creator" say about maps?
12. Will Steam add Mac support?
13. Are the Oct 14 referral pyramid and the 2026 Aztec Attack temples related?
14. What do the second-line numbers in the 2026 build stamps mean?
