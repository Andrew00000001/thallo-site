<!-- gap pass 1 -->
# Environment conventions addendum: mode and pickup hardware, and the October 2026 lighting pass

This addendum covers only the five open items on the "environment-conventions" gap list:
1. the Kill Confirmed tags (2026);
2. the joule-drop bolts;
3. the King of the Windmill windmill (2014–2018);
4. the 2018 Battle Royale props and screens;
5. before/after evidence for the October 2026 lighting pass.

**Sources reached this session**
- **Fan wiki (MediaWiki API): reached.**
  - Pages read: Updates, Battle Bears Gold/Versions (and /2.1), Joules, Pick-Ups, Team Battle, King of the Windmill, Free-For-All, Plant the Bomb, Battle Bears Gold, Battle Bears Royale, Battle Bears Heroes, Gold, Killstreaks, Imperial Basket Grande, Gold Digger, Haunted Castle, Kelowna, EZ Chee-Z and Provolowned.
  - These titles return `missingtitle`: Kill Confirmed, Battle Royale, Castle Royale, Bridge to Terabearthia, Team Deathmatch, Battle Bears Royale 2018, Lighting, Tags, Dog Tags and Sky World.
- **Steam: reached.** Store API for app 4408320, and the ISteamNews API (7 posts, Feb 24 to Oct 14, 2026), including the Oct 14 banner image.
- **battlebears.com (live): reached.** It mentions no modes by name.
- **YouTube:** I could read metadata, chapters and descriptions through `youtubei/v1/next`, plus oEmbed and thumbnails. The player endpoint returns `LOGIN_REQUIRED`. After 12 retries, Invidious (invidious.f5.si) returned storyboard specs for 7 more videos. I downloaded and sliced those storyboards myself. **I did not watch any video.** Every frame cited below is a storyboard tile (160–429 px wide) or a thumbnail.
- **Wayback Machine: unreachable.** CDX queries through curl got "connection reset", and WebFetch said "unable to fetch". No archived SkyVu blog or patch-note text was reached.
- **A note on honesty:** many image reads early in this session returned "media removed: request limit". I re-opened every image cited below until it actually displayed. Images that never displayed are not cited as [Observed].

Unless a full path is given, storyboard frames are named `f_<milliseconds>.jpg`.

---

## 1. Kill Confirmed tags (2026 playtests)

**Official text**
- SkyVu's Jul 28, 2026 Steam post ("2nd Discord Playtest Tomorrow! Trial a new gamemode!") lists, as a session focus: "An experimental new gamemode" [Canon] (Steam news gid 1839041357038714). It does not name the mode [Canon, by absence].
- The Steam store lists only "-Team Deathmatch (TDM) -Free for All (FFA) -Plant the Bomb (PTB)" [Canon] (store API, app 4408320). Kill Confirmed is not listed [Canon, by absence].
- The in-game start banner, on screen at each spawn:
  - "YOU'RE ON TEAM RED" / "COLLECT ENEMY TAGS TO SCORE POINTS" [Observed: HKbwq7PolNc storyboard at 56:20, 58:50 and 60:00].
  - For comparison, Team Battle reads "YOU'RE ON TEAM RED" / "[G]ET KILLS TO SCORE POINTS FOR YOUR TEAM" [Observed: HK 52:10, first letter clipped].
  - Plant the Bomb reads "YOU'RE ON TEAM BLUE" / "[illegible] THE BOMB TO SCORE POINTS" [Observed: HK 22:30].
- Kill-feed words "SCORED" and "DENIED" appear only in Kill Confirmed matches [Observed: HK 56:40–60:10; lFr8-yHbbzQ 9:00–12:30 and 17:50–21:40; VHo1O41RNJE 3:00–5:10; EQwloJnrOko 9:30–11:00].

**Era and status**
- **Lineage of the name.** BBG 2.1 (July 15, 2013) lists "Kill confirm Joule drops" [Game text via wiki] (Updates; Battle Bears Gold/Versions). The 2026 mode re-uses "kill confirm" as a mode name [Inference]. The 2013 feature was the joule drops in section 2, not a mode [Game text via wiki].
- **First footage.** InstableGR, "Battle Bears Gold - PC Playtest #2 w/ New Mode (7/29/26)": "This includes some of the first footage of a new mode: Kill Confirmed." [fan claim]. Its chapters list Kill Confirmed on:
  - Aztec Attack (00:00);
  - Marecraft (04:14, 42:44);
  - No Bear's Land (08:23, 17:42);
  - Haunted Castle (30:14) [fan chapter text].
- **Aug 21 playtest.** JustNubz's "Playtest #3 Part 3" lists "2:44 Sky Pirates KC" and "36:07 Sky Pirates KC" [fan description]. The VHo1O41RNJE storyboard at 2:50–7:10 shows SCORED and DENIED in the feed and a blue tag on the grass at 5:00 [Observed].
- **Oct 15 final playtest.** InstableGR's "56:16 - Match 14 (Kill Confirmed, Sky Pirates, Huggable/Tillman/Botch)" [fan chapter]. The storyboard confirms the banner, the tags and the feed [Observed]. The build label reads "3.0.7_2026.11.19_b7" [Observed, HK frames].
- **Possible fourth case.** Nuke_Dukem's No Bear's Land segment in EQwloJnrOko (9:00–12:40) also shows SCORED and DENIED. It is probably a Kill Confirmed match rather than Team Battle [Observed feed; Inference on the mode].
- **Launch status** on Nov 4: [Unverified]. Kill Confirmed is not in the store's mode list [Canon], but it was still running at the last playtest on Oct 15 [Observed].

**The tag, as seen**
- **Shape:** a flat, elongated rounded-rectangle plaque, about 1:2.5, like a dog tag or ID card. It has a thick dark rim and a round eyelet near one end. The face carries a faint embossed emblem I cannot read [Observed: lFr8 storyboard 9:50, 10:50, 11:30, 12:10 (blue) and 18:30 (red), crops `l_590/650/690/730.jpg` and `l_1110.jpg`].
- **Team colour** (Python-sampled from those crops):
  - Blue tag: face pale periwinkle #95A5D6–#98A6D7, rim dark ultramarine #252A86–#2D3888 [Observed].
  - Red tag: face dusty pink #CC8A94, rim oxblood #600709–#713131 (median #671112) [Observed].
- **Which colour drops.** At HK 58:40 a red tag lies next to the dead pink Huggable played by the uploader, who is on Team Red. At 58:30 a blue tag sits over an enemy marker [Observed]. So the tag takes the colour of the player who died [Inference]. Taking an enemy tag reads "SCORED" and taking your own team's tag reads "DENIED" [Inference from the banner text and feed words].
- **Placement:**
  - The tag floats about waist-to-chest high over the death spot. It is roughly as long as a bear's torso [Observed: l_650, where it overlaps a running player].
  - It is tilted at different angles in different frames [Observed].
  - A soft pale-green/white ring of light sits on the ground under it [Observed: l_690].
  - Whether it spins or bobs, and how long it lasts: [Unverified; storyboards are 10 s apart].
- **Scoring:** the HK Kill Confirmed match ends "BLUE TEAM WINS" at 20–25 with the clock near 0:09 [Observed: 60:10–60:20]. A score limit, if any: [Unverified].

**Hazards and interaction**
- Tags are picked up by moving through them. Joule drops (section 2) are also picked up on contact [Inference by analogy; no pickup animation seen].
- No tag-specific hazard is documented [Unverified].

**Easter eggs and references**
- The mode name and its "confirm the kill by collecting a tag" loop echo the common shooter convention [Inference].
- The 2013 patch line "Kill confirm Joule drops" is the in-house precedent [Game text via wiki].

**Images viewed** (all displayed this session)
- `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/environment-conventions/sheets/hk_kc_a.jpg` (HK storyboard 56:20–58:10) and `.../sheets/hk_kc_b.jpg` (58:20–60:20). Source frames: `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/toxic-terror-gap/frames/HKbwq7PolNc/f_3380000.jpg`–`f_3620000.jpg`.
- `.../environment-conventions/sheets/lfr8_m1.jpg` (Aztec Attack Kill Confirmed 0:00–4:10), `lfr8_m3.jpg` (No Bear's Land Kill Confirmed 8:30–12:30), `lfr8_m5.jpg` (No Bear's Land Kill Confirmed 17:50–21:50).
- `.../environment-conventions/sheets/l_tags.jpg` (crops `.../frames/l_590.jpg`, `l_650.jpg`, `l_690.jpg`, `l_730.jpg`), `l_red.jpg` (`.../frames/l_1110.jpg`, `l_1130.jpg`) and `l_zoom1.jpg` (`.../frames/l_080.jpg`, `l_120.jpg`). Source frames are in `.../environment-conventions/frames/sb_lFr8-yHbbzQ/`.
- `.../environment-conventions/sheets/vho_kc.jpg` (VHo1O41RNJE 2:50–9:20) and `eq_nbl.jpg` (EQwloJnrOko 9:00–12:40).
- `.../environment-conventions/sheets/prompts2.jpg` and `prompts3.jpg` (banner crops).

**Prompt pack**
- **Prop insert, 9:16, environment only:**
  > Low close-up at grass level on a bright, daisy-flecked lawn in midday sun. A single flat metal tag about as long as a forearm hovers at waist height, tipped about 30 degrees. It is a rounded rectangle with a thick dark-ultramarine rim (#2D3888), a pale periwinkle face (#95A5D6) and a round eyelet hole near its top end. Its face has a blank, softly embossed panel [BBG News invention: emblem left blank]. A faint pale-green ring of light glows on the turf under it. A few metres behind it, out of focus, a second tag of the same shape with an oxblood rim (#671112) and dusty-pink face (#CC8A94) floats over a trampled patch. No characters, no readable text.
- **Staging spots:**
  1. **The No Bear's Land trench lip.** A blue and a red tag hover a step apart beside the plank-floored trench. Two rivals race to "score" or "deny" [Observed setting: lFr8 9:50–12:10; the race is BBG News invention].
  2. **The Sky Pirates village green.** A tag floats among the white paving stones, birches and red-roofed cottages [Observed: HK 57:20–58:40; the comedy beat is BBG News invention].
  3. **The respawn banner moment.** The team-coloured "COLLECT ENEMY TAGS TO SCORE POINTS" banner is a recognisable beat. Shorts should paraphrase it, not reproduce the UI [BBG News invention].

**Confidence:** observed (low resolution). The look and the scoring words are seen. The tag's emblem, motion, lifetime and launch status are unknown.

---

## 2. Joule drops (the floating bolt tokens)

**Official text**
- BBG 2.1, July 15, 2013: "New character class - Assassin: Botch / Kill confirm Joule drops / New Skins / Balance Adjustment" [Game text via wiki] (Updates; Battle Bears Gold/Versions).
- Joules page: "These Joule pickups were removed in 2.1 and was replaced with three Joule Pickups which appear when someone has died. These Pick-Ups can be grabbed by anyone. Each gives you 25 Joules and lasts for a limited amount of time before disappearing. If a person manages to kill someone and collect all three Pick-Ups, which is not always the case, he will receive 175 Joules in total." [Fan-wiki]
- Pick-Ups page: "Joules pick-up: Gives 25 Joules per pick-up to the player. Three are dropped from the site of a player's death and disappear after 10 seconds." [Fan-wiki]
- Team Battle page: "When a player dies, 3 +50 Joule coins come out of the body, which can be collected by any member in the game." [Fan-wiki] This contradicts the 25 on the other two pages [Fan-wiki, internal conflict].

**Era and status**
- **Battle Bears Royale (BBR) and BBG before 2.1.** A static "Joules Pickup" of 150 Joules "was on all maps" [Fan-wiki: Joules]. The Gold Digger page says Blue's Imperial Basket Grande slot "originally had a Joules pickup … which was later removed from the game completely" [Fan-wiki: Gold Digger].
- **BBG 2.1 to 2021.** Three tokens drop at each death [Fan-wiki]. A 2014 King of the Windmill thumbnail shows three consecutive "+25" feed lines with bolt icons [Observed: GiHV3XmBT8w hq3]. The SrGGNd7V7Xs storyboard shows bolt tokens on the floor of Frozen Pundra at 1:24–1:26 [Observed].
- **2026: still in the game** [Observed].
  - SkyVu's own videos show them:
    - "Official Playtest Highlights" (C7uFxvSZ10c, Desert Airmine, 1:06), a July build [Observed; Canon video];
    - the Sep 20 livestream ejjsoKQ-VXU (No Bear's Land Team Battle, 35:50–36:10) [Observed];
    - the "Sky Pirates Map Reveal" (r91WkR10W2A, 0:34 and 0:40) [Observed].
  - InstableGR's Oct 15 footage shows them in Team Battle on Sky Pirates (HK 51:30–54:10) and in Free-for-All on Space Oddity (HK 19:30) [Observed].
  - [LA]Huggable's Oct 17 upload shows three of them in high resolution on Space Oddity [Observed: boAnKP4zIlg maxres2].
  - I did not see any in the Kill Confirmed frames I opened [Observed, by absence; not conclusive].
- **2026 payout.** The feed shows "XP +25 ⚡+200" on a kill, then three "⚡+500" lines [Observed: C7 0:42 (official, July); HK 2:50 (Oct 15)]. So each token appears to give 500 Joules in 2026, up from the wiki's 25 [Inference].

**Look**
- **Wiki icon** (File:Joule.png, 50×56, uploaded 2012-02-04): a sky-blue lightning bolt (#1090D0–#50B0E0) with a white outline (#F0F0F0) on a near-black maroon hexagon (#300000) [Observed].
- **In-game 2026 token:**
  - A thick, flat hexagonal slab whose body is dark maroon-brown, sampled #402224 (range #382924–#472E32).
  - One face carries a pale-blue bolt (#468BD6) with a white outline (#D1CECC).
  - It floats on edge, tilted, about knee-to-waist high, over a soft violet-blue halo ring (#6D65B9–#7E7AD3) on the ground.
  - Three appear per death, spread about a body-width apart [Observed: boAnKP4zIlg maxres2 at 1280×720, build label "3.0.7_2026.11.19_b7 411483"; storyboards above].
  - So the 2026 token is the 2012 icon turned into a 3D slab [Inference].
- **Lighting.** Tokens are unlit-looking and keep their colours in both daylight and dark maps [Observed: No Bear's Land, Desert Airmine, Space Oddity, Sky Pirates].

**Hazards and interaction**
- Anyone can grab them, and they disappear after a short time; the wiki gives "10 seconds" [Fan-wiki].
- I have not observed the 2026 lifetime [Unverified].

**Easter eggs and references**
- The Joule is a real energy unit, "1 Joule is equal to 1 newton metre" [Fan-wiki trivia].

**Images viewed**
- `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/environment-conventions/conv/Joule_x8.png` (upscaled from `.../img/Joule.png`).
- `.../environment-conventions/yt/th/boAnKP4zIlg_maxres2.jpg`.
- `.../environment-conventions/sheets/hk_5120.jpg` (HK 51:20–54:10) and `so_steam_vs_hk.jpg` (includes HK `f_1170000.jpg`, 19:30).
- `.../environment-conventions/sheets/ej_bolts.jpg` (`.../frames/ej_2150.jpg`, `ej_2170.jpg`), `ej_nbl.jpg`, `c7.jpg`, `c7_da.jpg` and `c7_da2.jpg`.
- `.../environment-conventions/frames/r91_034_x5.jpg` and `.../sheets/r91_32_54.jpg`.
- `.../environment-conventions/sheets/kotw_det2.jpg` (GiHV3XmBT8w hq3 "+25" lines) and `srgg_mill.jpg`.

**Prompt pack**
- **Prop insert, 9:16:**
  > Overhead three-quarter view of a sunlit grass clearing. Three thick hexagonal tokens hover in a loose triangle about knee-to-waist height, each tilted at a different angle. Each token is a dark maroon-brown slab (#402224) with a bold pale-blue lightning bolt (#468BD6) outlined in white on its face. Each casts a soft violet-blue glow ring (#7E7AD3) on the grass below. A faint dust scuff marks the ground at the centre of the triangle. No characters, no text.
  - The tokens' slow spin and bob are [BBG News invention].
- **Staging spots:**
  1. A "loot goblin" beat: three tokens left behind after a knockout, with a rival darting in to grab all three [BBG News invention; the drop count is Fan-wiki and Observed].
  2. The Space Oddity hall: tokens glowing against the amber window light, as in boAnKP4zIlg [Observed setting].

**Confidence:** observed. The look is observed in 2014 and 2026. The 2026 values are an inference from the HUD.

---

## 3. King of the Windmill windmill (BBG 2.8–2.29, March 2014 to January 2018)

**Official text**
- BBG 2.8, March 4, 2014, as quoted on the wiki [Game text via wiki]:
  - "New Map: Steam Yard Blues"
  - "New Gamemode: King of the Windmill"
  - "A single Windmill spawns on the map"
  - "Remain in the radius of the Windmill when it launches with one or more team mates to score a point"
  - "The team with the most points in the end on the game wins"
  - "If tied, the team with the most damage dealt wins"
- BBG 2.29, January 26, 2018: "King Of The Windmill is retired" [Game text via wiki].
- **In-game loading screen** (wiki File:IMG_0913.PNG, 960×640, uploaded 2014-03-24, captioned "released in honor of the latest map and game mode") [Observed]:
  - logo "KING OF THE [purple pinwheel] WINDMILL";
  - "NEW MAP / STEAM YARD BLUES / LOADING . . .";
  - the characters stand on a gold star-shaped platform stamped "MADE IN THE USA".
- **Wiki mode art** (File:BBG_windmill_game_mode-300x225.png) and the wordmark "KING OF THE WINDMILL" (black letters with a gold rim; File:King_of_windmill_text_small.png) [Observed].
  - Both were uploaded 2014-03-20 by a wiki user [Fan-wiki metadata]. Their SkyVu origin is [Unverified].

**Fan-wiki description**
- "A windmill will land in a random place on the map, surrounded by a green circle. The player must stand inside the circle until the windmill blasts off. When windmill blasts off, the point is given to the team, even if one player of the each team was in the circle, regardless of how many players were in the circle." [Fan-wiki]
- "When the windmill is about to land, chicken leg icons will fly out of the ground and into the air. These icons were also used for the Imperial Basket Grande in Royale." [Fan-wiki]
- "Players who are in the receiving end at the landing of the Windmill, the player will be heavily damaged or even killed." [Fan-wiki]

**The windmill, as seen** (2014–2018 fan footage)
- **A rocket windmill**, not a farm windmill.
  - A tall grey steel lattice mast (lit #C2CEDA, shade #5B655E) stands on four splayed, angular grey legs like landing struts.
  - White capsule booster pods (#A8A995) with lavender-purple panel bands (#645C6F) and orange-trimmed feet sit at the base.
  - A tan-orange pole runs up the mast.
  - On top is a purple-and-white pinwheel rotor of about 10–12 trapezoid purple blades with lavender borders around a white hub.
  - Sources [Observed]:
    - iEize4ke3lQ hq3 (base close-up on a round, ring-marked concrete pad);
    - ba1BWXTi8Mk maxresdefault (rotor close-up);
    - SrGGNd7V7Xs storyboard 0:58–1:22 and 3vBGASwuXEE maxresdefault (mast inside the ring);
    - kotw_zoom crops.
- **Landing and launch:**
  - SrGGNd7V7Xs (2014) shows a bright yellow streak arriving (0:56), the tower standing (1:00 and 1:22), then a lift-off with yellow-orange exhaust from the base pods over a translucent green disc (1:24). At 1:26 the tower is gone [Observed].
  - The 2.8 loading screen shows the same lattice tower with white-and-purple rocket pods belching white smoke clouds under a butter-yellow dusk sky (#E8D781) [Observed].
- **Scoring zone:** a translucent green cylinder wall rising from a ground ring. Sampled lit #21920F–#38C51F (Abusement Park) and #40790E–#428E12 in shade (No Bear's Land) [Observed: cjohaXBbOaw hq1, GiHV3XmBT8w hq3].
- **Chicken-leg icons:** not visible in any frame I opened [Unverified visually; Fan-wiki only].

**Maps it ran on** (fan videos titled King of the Windmill; map identified from set dressing) [Observed]
- **Frozen Pundra:** ice cave, SrGGNd7V7Xs "Battle Bears Gold 2.8 King of the Windmill gameplay", storyboard.
- **No Bear's Land:** iEize4ke3lQ and GiHV3XmBT8w. The ring stands on a grass knoll among tank traps, with a crashed dropship behind.
- **A snowy No Bear's Land** with ice-cyan sandbags and the dropship: ba1BWXTi8Mk (about 2018). This is probably the winter reskin, which returned Dec 20, 2017 in 2.28 [Observed thumbnail; Inference on the variant and date].
- **Abusement Park:** cjohaXBbOaw, with carnival booths and posters [Observed; map ID by set dressing, Inference].
- **Steam Yard Blues:** 3vBGASwuXEE.
- 6GHbBirr5qA, "BBG gameplay King of The Windmill", has Desert Airmine thumbnails but no windmill in frame [Observed; that King of the Windmill ran on Desert Airmine is Unverified].

**Mode art scene** (the wiki image; setting only)
- A grassy hilltop under a deep blue sky with big white clouds. The purple-and-white pinwheel windmill stands on a lattice mast behind a crowned bear holding two drumsticks [Observed].
- The crown plus drumsticks ties to the "king" and "chicken leg icons" ideas [Inference].

**2026 status**
- Not in the store's mode list [Canon, by absence]. Not seen in any 2026 playtest frame or chapter list I opened [Observed, by absence]. So it is probably not returning [Inference].

**Images viewed**
- `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/environment-conventions/img/IMG_0913.PNG`
- `.../environment-conventions/conv/BBG_windmill_game_mode-300x225_x3.png` and `.../conv/King_of_windmill_text_small_x2.png`
- `.../environment-conventions/sheets/kotw_6G.jpg`, `kotw_det2.jpg`, `kotw_zoom.jpg` (crops `.../frames/kotw_ba1_mill.jpg`, `kotw_GiHV_ring.jpg`, `kotw_iEize_base.jpg`, `kotw_SrGG_launch.jpg`), `srgg_a.jpg` and `srgg_mill.jpg`.
- Thumbnails in `.../environment-conventions/yt/kotw/`. The storyboard is in `.../frames/sb_SrGGNd7V7Xs/`.

**Prompt pack**
- **Establishing shot, 9:16:**
  > A sunny grassy plateau with a plank-floored trench. In the centre stands a tall grey steel lattice tower on four splayed angular landing legs. White capsule rocket pods with lavender-purple bands cluster at its base. A purple-and-white pinwheel windmill rotor turns at the top. A translucent green cylinder of light, about three bear-heights across, rises from a glowing ring on the ground around it. Thin white smoke curls from the pods. Deep blue sky with big white clouds. No characters, no text.
  - The pinwheel turning and the smoke at idle are [BBG News invention].
- **Staging spots:**
  1. **"The landing."** The windmill drops out of the sky into the ring and flattens someone who stood where it lands [Fan-wiki hazard; the comedy staging is BBG News invention].
  2. **"Lift-off."** A crowd crams inside the green ring as yellow rocket flame lights the pods [Observed launch; the crowd gag is BBG News invention].
  3. A **nostalgia post** pairing the 2.8 loading screen's dusk palette with "retired January 26, 2018" [Game text via wiki].

**Confidence:** observed (2014–2018 fan footage) plus documented (patch text). Exact landing rules per map are partial.

---

## 4. Battle Royale (BBG 2.50–2.53, April 2018) props and screens

**Official text**
- SkyVu video "Battle Bears Gold Battle Royale Map!" (bOEK6skhDKU, published Mar 28, 2018, 20 s), description: "New Battle Royale Mode and Map coming in update v2.32! See you on the battlefield." [Canon]
- Updates table [Game text via wiki]:
  - 2.50 (April 5, 2018): "Chat updated" / "New Battle Royale mode implented.Winners in gas" [sic];
  - 2.53 (April 28, 2018): "Bridge to Terabearthia added to the Battle Royale mode."
  - The video says "v2.32" while the patch table says 2.50 [conflict; Unverified which is right].
- Battle Bears Gold wiki page [Fan-wiki]:
  - "Gas which is obtained by winning Battle Royale with Cheese";
  - gallery caption "The splash screen for the Battle Royale update in 2.50";
  - icon caption "BBG: Battle Bears Royale 2018 … New version of the 2011 logo for the new update of BBG 2.50 or AKA Battle Bears Royale."
  - Whether "Battle Royale with Cheese" names this 2018 mode is [Unverified].
- A Spanish fan description (Chocoindustries, oHIZFR1tHxI, Apr 5, 2018) says the update rebranded BBG back to "BBRoyale" under "Screenzilla" [fan claim]. The wiki's Kelowna trivia mentions "the city that Screenzilla resides in" [Fan-wiki].
- No wiki page exists for the mode or its maps [Fan-wiki: missingtitle].

**The map, as seen**
- **Official preview (bOEK6skhDKU storyboard, 0:00–0:19):** a big stone castle on a floating grass island with a dirt underside [Observed]. It has:
  - grey-pink stone curtain walls and round towers;
  - teal-capped crenellations on one side and red-capped ones on the other;
  - a tall central round keep;
  - boxy dark-green hedges, dirt paths, and a graveyard with tombstones behind an iron fence;
  - a bright blue sky over a white cloud sea.
  - Its name is [Unverified]. It looks like a daytime, enlarged take on Haunted Castle's team-coloured castle [Inference].
- **2.50 splash** (wiki File:Battle_Bears_Royale_Battle_Royale_Update.png, 2048×1536) [Observed]:
  - the "BATTLE BEARS ROYALE" logo on a stone-and-steel plaque;
  - a castle with a blue-capped tower at left and red-capped walls and tower at right;
  - lime grass, a graveyard and iron fence, orange explosions, a cyan sky;
  - a robot panda firing a bazooka in the foreground.
- **Fan gameplay** (storyboards aeEtor1v-0E "battle bears royale 2.50 battle royale", Apr 5, 2018, build label "2.50"; and oHIZFR1tHxI) [Observed]:
  - **Queue:**
    - an "AUTOMATCHING..." panel with a "ROYALE" mode tile, "AVERAGE WAIT TIME", "MATCHMAKING USERS" and a red "CANCEL" button;
    - a starfield transition;
    - black screens counting down "WAITING FOR PLAYERS..." → "WAITING FOR 9 PLAYERS" → "5" → "3" → "WAITING FOR 1 PLAYER" (ae 0:00–0:38).
    - The automatch panel is the BBR-era layout (a 2012 wiki screenshot reads "AUTOMATCHING FOR / PLANT THE BOMB / AVERAGE WAIT TIME / MATCHMAKING USERS / TIME WAITED 1:11 … CANCEL") [Observed: 2012-11-29_19.25.08.png].
  - **Props on the castle grounds:**
    - solid royal-blue cubes about waist high (lit #160ED1, shade #0A0D73);
    - red rectangular blocks;
    - large plank crates (#AF8540);
    - stacked barrels, pumpkins, tombstones and hedges.
    - The grass reads as clipped lime (#C2FE14) in this phone capture [Observed: ae 1:02, 1:06, 2:04, 2:16–2:20, 2:30; oHIZ 3:40, 7:10].
    - What the blue cubes and red blocks do, for example loot crates: [Unverified]. That they are loot or supply boxes is an [Inference] from the mode.
  - **Sky beams:** vertical pink-magenta and cyan light pillars rise into the sky [Observed: oHIZ 2:25–3:15 and 7:00; ae 2:46]. Their function (drop markers or zone) is [Unverified].
  - **End screens:** "#1 WINNER!" / "SUBMITTING GAME TO SERVER..." and "GET READY FOR THE NEXT BATTLE" [Observed: ae 2:58–3:02; oHIZ 3:55–4:00, 7:45].
- **2026:** Battle Royale is not among the store's modes [Canon, by absence]. Do not confuse it with Battle Bears Heroes' Battle Royale (2024), which the wiki quotes as "Mini MOBA, Brick Battle, Death Match and Battle Royale" [Fan-wiki].

**Images viewed**
- `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/environment-conventions/img/Battle_Bears_Royale_Battle_Royale_Update.png` and `.../img/Screenshot_20180407-085431_2.jpg` (the 2018 robot-panda icon).
- `.../environment-conventions/sheets/bOEK.jpg`, `ae_a.jpg`, `ae_b.jpg`, `ae_crates.jpg`, `oHIZ_all.jpg` and `bbr_refs.jpg` (includes the 2012 automatch screen).
- Storyboards: `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/critic/sb/aeEtor1v-0E/`, `.../critic/sb/bOEK6skhDKU/` and `.../dl/new_maps/yt/sb/oHIZFR1tHxI/`.

**Prompt pack**
- **Establishing shot, 9:16:**
  > A floating grass island seen from a high three-quarter angle against a bright blue sky over a white cloud sea. A sprawling grey-pink stone castle covers the island, with round towers and curtain walls. One half's crenellations are capped teal, the other half's red, and a tall round keep rises in the centre. Boxy dark-green hedges line dirt paths. A small graveyard of tombstones sits behind a black iron fence. A few waist-high solid royal-blue cubes and red blocks are scattered on the lawns beside plank crates and pumpkins. A thin magenta light pillar rises from one courtyard into the sky. No characters, no text.
  - The cloud-sea framing below the island is [Observed]. The pillar's placement is [BBG News invention].
- **Staging spots:**
  1. **"Waiting for 1 player."** A lone bear in a black void, staring at the counter [Observed screen; the gag is BBG News invention; paraphrase, do not copy the UI].
  2. **"#1 Winner"** in the graveyard, among the tombstones [Observed props; BBG News invention].

**Confidence:** partial. The props and screens are observed in low-resolution fan footage. Names and functions are undocumented.

---

## 5. October 2026 lighting pass: before and after

**Official text**
- Steam post "Final Discord Playtest this Thursday Oct 15" (Gold44, 2026-10-14 12:07 UTC): "Headline additions: -Custom keybinds -Jukebox -UI controller support -Lighting improvements -Lots of bug fixes" [Canon].
  - The same post asks testers to "record some footage, ideally on PC and without the UI (press the H key to hide it)" for "our Steam and store pages" [Canon].
- Its banner image reads [Canon; Observed]:
  - "-CUSTOM KEYBINDS -MENU JUKEBOX -UI CONTROLLER SUPPORT -REDEEM CODE SYSTEM -ANDROID SUPPORT -LOTS OF BUG FIXES -LIGHTING, EFFECT & TEXTURE IMPROVEMENTS";
  - "CLOSED TESTING 5"; "THURSDAY, 3PM PDT".
  - The banner shows No Bear's Land in clear midday light: a deep blue sky, crisp shadows, a blue-banded keep stencilled "…MOC 20-11", sandbags and tank traps.
- The description of SkyVu's ZMhLVXWT6OY livestream ("Streamed live on Oct 15, 2026") repeats the list [Canon].
- **Earlier pass:** BBG 3.0 (November 15, 2021) lists "New Map Lighting" [Game text via wiki]. So the July–September 2026 builds presumably carried the 2021 lighting [Inference].
  - Do not confuse it with Battle Bears Overclock 3.0 (July 3, 2020): "Upgraded Map Lighting, check out how Skyworld has benefitted!" [Game text via wiki, Overclock section].
- **Fan claim** (InstableGR, HKbwq7PolNc description, Oct 17): "first is an overhauled lighting for all maps, attempting to restore what they looked like back in the day. No Bear's Land, Desert Airmine, and Space Oddity - all shown in this video - now look almost just like they did when the game first launched as Battle Bears Royale, a huge treat for longtime fans and for the eyes." [fan claim]
- **Build labels on screen** [Observed]:
  - Jul 29: "3.0.0 / 11502154" (g_Qbis4xaLY maxres2);
  - Aug 31 reveal: "3.0.2 / 12127020" (r91WkR10W2A maxres1);
  - Oct 15: "3.0.7_2026.11.19_b7" (HK frames; boAnKP4zIlg maxres2).
  - Why an Oct 15 build carries "2026.11.19" is [Unverified].

**Method**
- I measured matched gameplay storyboard frames with Python, cropping out the HUD edges.
  - For No Bear's Land I kept only frames with at least 20% grass.
  - For Desert Airmine I took the median of sand pixels (hue 25–55°, saturation above 0.3, value above 0.55).
- **Best comparison:** InstableGR captured both July 29 and October 15 on the same ultrawide setup (both storyboards are 429×180) [Observed]. That is the cleanest same-pipeline before/after.
- All numbers come from YouTube-compressed, low-resolution tiles. Camera positions differ from frame to frame. Read them as direction of change, not exact values [Inference].

**No Bear's Land**

| Capture | Frames kept | Mean luma | Luma SD | Mean sat. | Near-black share | Sky | Grass |
|---|---|---|---|---|---|---|---|
| BBR-era in-game, wiki Oliver-battlefield-airpad-red-base-front.png (about 2012) | 1 | 92 | 45 | 0.66 | 28.1% | #4176D6 | #6E8519 |
| InstableGR, Jul 29 (lFr8 storyboard, five No Bear's Land matches) | 88 | 131 | 45 | 0.58 | 3.9% | #7392DB | #779626 |
| Nuke_Dukem, Aug 21 (EQ 9:00–12:40) | 22 | 129 | 51 | 0.56 | 7.1% | #7492DB | #7A9626 |
| SkyVu stream, Sep 20 (ejj 33:20–38:20, iPad capture with webcam overlay) | 18 | 107 | 62 | 0.46 | 20.1% | #6482D0 | #6D8A32 |
| **InstableGR, Oct 15 (HK 27:10–31:10)** | 20 | 125 | 58 | 0.48 | 15.6% | #859DE5 | #829E30 |
| SkyVu stream, Oct 15 (ZM 58:10–62:10, PC window with stream overlays) | 14 | 100 | 64 | 0.54 | 28.1% | #85A0E7 | #809B2D |

- **Same channel, July to October:** contrast rose (luma SD 45 → 58). The near-black share quadrupled (3.9% → 15.6%), mostly the shadow sides of the keeps and dropships. Saturation fell (0.58 → 0.48). The sky got lighter and slightly more lavender (#7392DB → #859DE5). Grass barely moved [Observed, Python-sampled].
- **Visually:** the October frames show darker, crisper shadow faces on the keeps and the crashed dropship, under a paler sky with more cloud. The July frames are flatter and brighter [Observed: nbl_same_channel.jpg pairs lFr8 10:00/11:00/11:50/20:10 against HK 28:10/29:30/29:50/30:30].
- **Toward the BBR look?**
  - Partly. The darker shadows and the near-black share move toward the one BBR-era in-game screenshot (28%).
  - The sky moves away from it: BBR has a deep, saturated #4176D6, while October is a paler #859DE5 [Observed metrics; Inference].
  - The SkyVu banner's sky reads deep and saturated (#7399EB in its left third), between the two [Observed].
  - InstableGR's "almost just like" claim is only partly supported here [Inference].
- **SkyVu's own streams**, Sep 20 to Oct 15, move the same way (near-black 20% → 28%, sky lighter). But the two captures used different devices and overlays, so this is weak evidence [Inference].

**Desert Airmine** (sand and canyon medians)

| Capture | Sand median | Sand hue / sat / val | Canyon median |
|---|---|---|---|
| BBR "Desert Level" renders (kevinsalki.com portfolio, 2012–13; not in-game) | #D49147 | 32.7° / 0.67 / 0.83 | #B2683F |
| BBG 2014 fan thumbnails (6GHbBirr5qA hq1–3) | #FBA12F | 36.1° / 0.81 / 0.98 | #713E28 |
| SkyVu "Official Playtest Highlights" (July builds; C7 0:42, 0:44, 1:04, 1:08) | #D68B33 | 32.2° / 0.77 / 0.84 | — |
| JustNubz, Aug 21 (_R4rvvGlRsM 20:00–24:00) | #D58E39 | 32.0° / 0.74 / 0.84 | #714734 |
| **InstableGR, Oct 15, match 1 (HK 0:10–4:50)** | #E1AB5C | 37.0° / 0.60 / 0.88 | #754A35 |
| **InstableGR, Oct 15, match 15 (HK 60:30–64:10)** | #F2B762 | 36.8° / 0.59 / 0.95 | #714732 |

- **The change:** the October sand is clearly paler, brighter and yellower, and less saturated. It reads butter-yellow where July and August read deep orange-amber. The canyon walls did not change [Observed: r4_da.jpg vs hk_da.jpg; c7_da.jpg; Python-sampled].
- **Toward the old look?** The hue moved toward the 2014 in-game yellow (36°), but saturation is far below 2014. It is no closer to the BBR renders, which are not in-game captures anyway [Inference].

**Space Oddity**
- **Before:** Steam screenshot `screen_01`, a frame of the Steam trailer's Space Oddity clip (about 30.0–32.8 s).
  - My local copy was saved Oct 15, 20:52 (container clock), before the 3 PM PDT (22:00 UTC) playtest. It is byte-identical to today's store file (md5 d36d6af6…) [Observed].
  - So it predates the Oct 15 build [Inference]. It is not a 2026 "before" either: the same moment, bloom included, is in the storyboard of SkyVu's May 30, 2013 trailer (rfAyqVJrli4 35–36 s = Steam 30.85–31.95 s) [Observed: so_clip_2013_vs_steam.jpg; 00_OVERVIEW.md, section 0, item 1], so it is 2013 footage [Inference, strong]. space-oddity.md had left its date open and allowed a newer or relit capture [Inference].
  - A real 2026 "before" is in space-oddity.addendum.md: InstableGR's Aug 21 capture (build 3.0.2, aujTcdFuxdE) and Sep 20–21 fan captures (build 3.0.5) show cooler grey-teal metal (#3D4E44) with orange angular panels [Observed there; I re-opened its era_compare.jpg].
- **After:** HK 17:50–21:30 (Oct 15).
- **Warm surfaces** (windows and floor):
  - Steam screenshot screen_01: #AB6425, hue 28.5°, saturation 0.79, warm share 20%.
  - October: #A27635, hue 34.3°, saturation 0.68, warm share 10%.
  - Cyan share about the same (1.6% vs 1.3%) [Observed, Python-sampled].
- **Visually:** in October the window walls read amber-ochre and the bulkheads olive-grey, with soft amber light shafts. screen_01 is vivid red-orange with hot cyan neon [Observed: so_steam_vs_hk.jpg].
- **Caveat:** I found no July–September 2026 Space Oddity capture myself, so my numbers compare against screen_01 (2013 footage [Inference, strong]), not against a 2026 build. space-oddity.addendum.md has the same-channel pair (InstableGR, 3.0.2 on Aug 21 vs 3.0.7 on Oct 15) and measures warm share rising from 14% to 45% on its own method [Observed there].

**Frozen Pundra** (incidental)
- InstableGR Jul 29 (Team Battle) vs Oct 15 (Plant the Bomb): both captures show saturated cyan-blue ice [Observed: fp_pair.jpg]. No clear change is visible at storyboard resolution [Inference].

**Bottom line for depiction**
- For 2026-accurate shorts, use the October look [Inference]:
  - No Bear's Land: a paler sky (about #859DE5), deeper shadow faces, a slightly less saturated field.
  - Desert Airmine: butter-yellow sand (#E1AB5C–#F2B762) over unchanged terracotta canyons.
  - Space Oddity: amber-ochre glass and olive-grey bulkheads, warmer than the grey-teal Aug–Sep builds and less red-orange than screen_01.
- The Steam trailer and store screenshots are not proof of the launch lighting [Inference].
- The Next Fest demo (from Oct 19) should settle this at full resolution [Inference].

**Images viewed**
- `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/environment-conventions/steam/oct14_banner_half.jpg` (from `.../steam/oct14_banner.png`)
- `.../environment-conventions/sheets/nbl_same_channel.jpg`, `official_nbl_pair.jpg`, `eq_nbl.jpg`, `ej_nbl.jpg` and `bbr_refs.jpg`
- `.../environment-conventions/sheets/hk_da.jpg`, `r4_da.jpg`, `c7_da.jpg` and `c7_da2.jpg`
- `.../environment-conventions/sheets/so_steam_vs_hk.jpg` (with `.../steam/ss_1.jpg`) and `fp_pair.jpg`
- `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/astoria_trailer_check/so_clip_2013_vs_steam.jpg` (the Space Oddity clip, 2013 storyboard against Steam; review pass)
- `.../environment-conventions/sheets/labels.jpg` and `labels2.jpg`; `.../yt/th/boAnKP4zIlg_maxres2.jpg`
- Frame sources:
  - `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/toxic-terror-gap/frames/HKbwq7PolNc/`
  - `.../toxic-terror-gap/frames/ZMhLVXWT6OY/`
  - `.../toxic-terror-gap/frames/ejjsoKQ-VXU/`
  - `.../environment-conventions/frames/EQ424/`
  - `.../environment-conventions/frames/sb_lFr8-yHbbzQ/`
  - `.../environment-conventions/frames/sb__R4rvvGlRsM/`
  - `.../environment-conventions/frames/sb_C7uFxvSZ10c/`
- Scripts: `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/scripts_envconv/light.py` and `light2.py`.

**Prompt pack** (a lighting note to append to any 2026 map establishing shot)
- No Bear's Land: "high midday sun, pale periwinkle sky (#859DE5) with soft white cumulus, crisp near-black shadow faces on concrete, slightly muted green turf (#829E30)".
- Desert Airmine: "pale butter-yellow sand tops (#E1AB5C–#F2B762) under a hazy powder-blue sky, unchanged terracotta canyon walls (#754A35)".
- Space Oddity: "amber-ochre star windows (#A27635), olive-grey bulkheads, soft amber light shafts, restrained cyan accents".
- Each is a 2026-build reading [Observed, low-res]. The exact hexes are approximations [Inference].

**Confidence:** partial. The pass is official. The change is visible for No Bear's Land and Desert Airmine. The "BBR look" claim is only partly supported, and my Space Oddity numbers lack a matched 2026 "before" (screen_01 is 2013 footage [Inference, strong]; space-oddity.addendum.md supplies the Aug 21 one).

---

## Corrections to our notes

1. **research_desert-airmine.md** (repo drafts): "The 2026 build's lighting is unobserved; the Oct 14, 2026 Steam post lists "Lighting improvements" [Canon]."
   - → The 2026 look has now been observed in storyboards.
   - July/August builds: orange sand #D58E39 (hue 32°).
   - Oct 15 build: paler, yellower sand #E1AB5C–#F2B762 (hue 37°); canyon unchanged (#714734 → #754A35) [Observed, low-res].
   - Evidence: C7uFxvSZ10c 0:42–1:08; _R4rvvGlRsM 20:00–24:00; HKbwq7PolNc 0:10–4:50 and 60:30–64:10.
2. **research_desert-airmine.md:** "the 2026 build's look is unobserved."
   - → Same fix as item 1. Also, joule bolt tokens are visible on the map in SkyVu's own July footage (C7 1:06) [Observed].
3. **research_no-bear-s-land.md:** "King of the Windmill and Battle Royale: no record of them on this map [Unknown]."
   - → King of the Windmill ran on No Bear's Land: 2014 fan videos iEize4ke3lQ and GiHV3XmBT8w show the windmill and its green ring there, and ba1BWXTi8Mk shows it on the snowy reskin [Observed thumbnails].
   - Battle Royale: still no record.
   - In 2026 the map also hosted Kill Confirmed (Jul 29; probably Aug 21) [Observed].
4. **research_frozen-pundra.md:** "2014 modes: not documented for this map [Unverified]."
   - → King of the Windmill is observed on Frozen Pundra in the 2014 fan video SrGGNd7V7Xs. Its storyboard shows landing, ring and lift-off at 0:56–1:26 [Observed].
5. **research_frozen-pundra.md:** "2026 modes listed on Steam are TDM, FFA and Plant the Bomb [Canon]. Which of them run on Frozen Pundra is [Unverified]."
   - → In 2026 playtests it ran Team Battle (Jul 29, lFr8 match 6) and Plant the Bomb (Oct 15, HK match 6) [fan chapters; Observed banner "…THE BOMB TO SCORE POINTS" at HK 22:30].
   - Launch rotation still unverified.
6. **research_haunted-castle.md:** "Not named on the Steam store [Canon, by absence]. The "16 wacky maps" list is not public [Unverified]."
   - → Add: Haunted Castle appears in SkyVu's own "Official Playtest Highlights" (C7uFxvSZ10c, 1:44–1:46). The frames show a night castle wall, jack-o'-lanterns and a blue banner [Observed].
   - It also hosted Kill Confirmed (Jul 29) and Plant the Bomb (Oct 15) in fan playtest chapters [fan chapter text].
7. **research_abusement-park.md:** "Team battle and Plant the Bomb are documented [Fan-wiki]."
   - → Add: King of the Windmill ran on Abusement Park. cjohaXBbOaw (2014) shows the green ring and windmill among the carnival booths [Observed; map ID by set dressing].
8. **research_marecraft-map.md:** "No source lists modes for Marecraft specifically [Inference: it would have run all of them]."
   - → 2026 playtests list Marecraft with:
     - Kill Confirmed (lFr8 04:14, 42:44);
     - Team Battle (lFr8 34:24; _R4rvvGlRsM "1:08 Marecraft TDM");
     - Plant the Bomb (HK 1:04:35) [fan chapter text].
9. **research_aztec-attack.md:** "The 2026 modes are TDM, FFA and PTB [Canon]. Which of them run on Aztec Attack at launch is [Unverified]."
   - → Add: Aztec Attack hosted Kill Confirmed in the Jul 29 playtest. lFr8 match 1 shows a blue tag at 1:20 and SCORED/DENIED in the feed [Observed]. Launch rotation still unverified.
10. **research_space-oddity.md:** "The 2026 look may differ from the frames below [Inference]."
    - → Observed Oct 15 (HK 17:50–21:30): same geometry. Warm surfaces read amber-ochre (#A27635, hue 34°) rather than the red-orange of Steam screenshot screen_01 (#AB6425, hue 28.5°), at half the warm-pixel share. screen_01 is 2013 footage [Inference, strong], not the 2026 pre-pass look; for that, use the Aug–Sep 2026 builds in space-oddity.addendum.md. Joule tokens appear in Free-for-All [Observed, low-res].
11. **franchise_world.md** (lore notes, "What changed or is new in the 2026 BBG"): '"An experimental new gamemode" ([Jul 28 post](...))'
    - → Add: on-screen banners and fan chapters identify the playtest mode as Kill Confirmed ("COLLECT ENEMY TAGS TO SCORE POINTS") [Observed]. SkyVu's Steam posts never name it [Canon, by absence].
    - Also add the Oct 14 post's "Lighting improvements" and "Jukebox" [Canon].
12. **This workflow's gap brief** (environment-conventions):
    - **"the HKbwq7PolNc storyboard at about 58:50 shows the prompt".** → It first appears at 56:20, at match start, and repeats on each respawn (58:50, 60:00) [Observed].
    - **"Large floating blue lightning-bolt pickups … in Team Battle".** → They are dark maroon hexagonal tokens bearing a blue bolt, three per death. They also appear in Free-for-All (HK 19:30, Space Oddity) and on Desert Airmine in SkyVu's July footage [Observed].
    - **EQwloJnrOko No Bear's Land at 9:00–12:40.** The feed shows SCORED and DENIED, so this is probably a Kill Confirmed match, not Team Battle [Observed; Inference].
    - **Battle Royale "red and blue crates".** What is observed is solid blue cubes and red blocks; that they are crates is [Inference].

## Open questions

- Does Kill Confirmed ship on Nov 4? The store lists only TDM, FFA and PTB.
- What emblem is on the tag face? Do tags spin or bob, and how long do they last? Is there a score limit?
- What is the 2026 joule-token value? The HUD suggests +500 per token, versus the wiki's 25. How long do tokens last, and do they also drop in Kill Confirmed and Plant the Bomb?
- What do the King of the Windmill "chicken leg icons" look like? Did the windmill land on every map, including Desert Airmine, Sky View and Toxic Terror?
- 2018 Battle Royale:
  - What is the castle map called, and is it a reworked Haunted Castle?
  - What does Bridge to Terabearthia look like?
  - What were the blue cubes, red blocks and pink and cyan sky pillars for?
  - Was the version 2.32 (SkyVu video) or 2.50 (patch table)?
- Did the October pass change other maps (Gold Digger, Haunted Castle, Sky View and so on)? A full-resolution Next Fest demo capture is needed to confirm the No Bear's Land, Desert Airmine and Space Oddity readings.
- Will the Steam store screenshots be replaced with October-build captures? The Oct 14 post asked testers for UI-free footage "for our Steam and store pages".
- Why does the Oct 15 build label read "3.0.7_2026.11.19_b7"?


---

<!-- gap pass 2 -->
# Main Menu and GEAR UP room (our "hangar")

Addendum to the environment-conventions dossier. It covers the 3D room behind BBG's front-end screens: the main menu, the GEAR UP loadout view, the matchmaking and lobby views, the after-match boards and the 2026 space-window transition. These are the screens where the selected bear stands in a dark green steel bay full of hazard-striped crates and signs.

**Naming.** SkyVu calls this space the "Main Menu" (Steam soundtrack track titles) and the "main menu" (1.3.2 banner) [Canon; Observed]. The wiki's copy of the 3.0.1 patch notes says "Home Menu" [Fan-wiki]. The button reads "GEAR UP" [Observed], and the wiki calls that screen the "Gear Up menu" [Fan-wiki]. No source calls the room a hangar, so "hangar" is our own label [BBG News invention]. For captions, use "the BBG main menu" or "the Gear Up bay" [Inference].

**What I could reach and what I could not**
- Reached: the fan wiki through its API (wikitext of Battle Bears Gold, Battle Bears Royale, Updates, BBR Version 1.4.2 / 1.3.2, Loadouts, Disconnection, Machine Gun, Charged Run, Losing Your Head, Soldier (BBG), Soldier (BBG)/Skins, Sam-Are-I, Kumakiri, Bundle Deals, Ursa Major and BB Heroes); the wiki image list (2,914 files) and about 45 images, which I opened.
- Reached: YouTube metadata through the youtubei "next" endpoint and oEmbed, plus thumbnails. Storyboards came through Invidious for two videos: SkyVu's "BBG Livestream" of Aug 21, 2026 and JustNubz's Playtest #4 showcase. The Sep 20, 2026 SkyVu livestream storyboard was already on disk.
- Reached: the Steam API and store pages for apps 4408320 (BBG), 5321720 (BBG Soundtrack) and 1482340 (BB-1); battlebears.com (home, characters, about, news).
- Not reached: web.archive.org failed with a connection reset six times through curl, and WebFetch refused it. So no archived SkyVu blog or patch-note page was checked. Invidious storyboards for SkyVu's other videos also failed ("Companion is starting"). battlebears.com/pages/battle-bears-gold now returns 404.
- I did not play or watch any video. Everything I say about a video comes from its storyboard frames (320×180, one every 10 s) or its thumbnails.

## Official text
- Steam soundtrack track list (app 5321720, release "Nov 4, 2026"): "17 Main Menu (BBG) 1:49", "19 After Match 1:04" and "20 Main Menu (BBR) 1:09" [Canon]. Album text: "The official soundtrack for Battle Bears Gold features the complete collection of map and menu music from the award-winning 4v4 class shooter, along with select bonus vocal tracks from across the series." Credits: "Original Score: Rob Ruiz, AnDrue Humphreys, and Benjamin Vavak". No track has its own credit [Canon].
- SkyVu "UPDATE 1.3.2 / COMING SOON" banner: "- main menu tips/announcements, store bundle deals, fixed many crashes, fixed skill rating, bug fixes, & more!" [Observed: SkyVu banner, as re-hosted on the wiki at File:Update_1_3_2_coming_soon.jpeg, uploaded 2012-11-23].
- Marecraft teaser description: "Gear up, it's time to Battle Bears." [Canon] (BATTLE BEARS channel, "The Battle Bears Marecraft Arena", Apr 5, 2013, SSwlTVbW8Wg).
- "BBG Livestream Sunday" (BATTLE BEARS, "Streamed live on Sep 20, 2026", ejjsoKQ-VXU): "We're bringing BBG back on Mobile + Steam! Join Ben and Gold44 as they test the latest build." [Canon]. Its chapter markers ("Welcome and project intro" 0:00, "Gameplay and character skins" 2:01, "Custom matches and map tour" 5:58…) look like YouTube auto-chapters, so I do not treat them as SkyVu's words [Unverified]. "BBG Livestream" (BATTLE BEARS, "Streamed live on Aug 21, 2026", xP27fWSCSKs) has the same description wording [Canon].
- Steam store copy (4408320): "Try thousands of unique LOADOUT combos" [Canon]. This is the Gear Up's job.
- Text read off in-game screens [Observed]:
  - 1.4.2 ticker: "EXPERIENCING PROBLEMS WITH BB, SEND AN EMAIL TO SUPPORT@BATTLEBEARS.COM."
  - Pop-up plaques: "GAME CANCELLED / ALL PLAYERS HAVE LEFT BEFORE THE GAME COULD BEGIN / BOOURNS" and "DISCONNECTED! / YOU HAVE BEEN DISCONNECTED FROM THE GAME. CHECK YOUR CONNECTION. / THAT SUCKS".
  - Matchmaking: "AUTOMATCHING FOR / TEAM BATTLE / AVERAGE WAIT TIME / MATCHMAKING USERS / TIME WAITED / PICK UP YOUR VISUAL SCANNING!".
  - 2026 builds: "TAP TO CHAT", "CREATE MATCH" (Jul–Aug), "CUSTOM MATCH" and "QUESTS" (Sep), "PRO-MODE FEATURES / AVAILABLE NOW", "MATCHING", "WAITING FOR 7 PLAYERS", "RED TEAM WINS" / "BLUE TEAM WINS", "SUBMITTING GAME TO SERVER...", "PLAYER STATS", "TAP TO CLAIM" [Observed; low-res for 2026].
- In-game text quoted by the wiki [Game text via wiki]:
  - Loadouts: "Take multiple bears with you into battle! Using this loadout slot you can customize a specific set of equipment and switch between 3 different ones during a match!"
  - Sam-Are-I, the skin on the 2013 menu bear: "Honor your ancestors and bring shame upon your foes in the most feudal way possible. You are rich in discipline, it is mercy that you lack."
- Fan-wiki lines:
  - Gallery captions: "Battle Bears Royale main menu", "The old Battle Bears Gold home screen", "The new BBG home screen".
  - "The Machine Gun's outline is seen on the Gear Up button in the main menu of Battle Bears Gold."
  - Huggable: "The flag does not appear in the Gear Ups and Main Menu."
  - "The loadout that is first taken into a match is chosen in the Gear Up menu."
  - The lone player is "returned to the Gear Up menu with a special 'Game Cancelled' screen."
  - BBR 1.4.2: "to change you nickname, you simply need to press a single button on the main menu" (sic).
  - Charged Run: "Its stance in the Gear Up menu is identical to that which the Huggable takes on when equipped with Phantom Hug."
  - Losing Your Head is "the only Huggable primary weapon not to have a menu display slide".

## Era and status
- **Aug 31, 2011, pre-launch BBR.** The official "BATTLE BEARS ROYALE Sneak Peek" thumbnail (IucMFqzR_Qw) already shows hazard-striped yellow GEAR UP and PLAY crates, a "MAIN MENU" sign, hanging cables and a green monitor mode carousel ("TUTORIAL / TEAM BATTLE / CAPTURE THE FLAG", the last marked coming soon) [Observed]. I have no frame with a bear standing in a 3D room from 2011 [Unverified].
- **BBR 1.3.1 (Jun 28, 2012).** File:Oliver-main-menu.png, which carries a "1.3.1" stamp and was uploaded 2012-07-30, shows the 3D room [Observed].
  - Default Oliver (red headband, bullet bandolier) stands centre, holding a silver gun.
  - Signs: a "BATTLE BEARS / ROYALE" metal sign and a cyan neon "PLAY" sign, both hanging; a "LIKE US ON FACEBOOK" monitor; a blue "BATTLEBEARS.COM / EARN FREE GAS" crate; a back-wall monitor showing a sunlit desert scene.
- **BBR 1.3.2 (Aug 24, 2012).** The wiki's copy of the update notes says "Store Bundle Deals in Promos in Main Menu" [Fan-wiki]. The banner announces "main menu tips/announcements" [Observed].
- **BBR 1.3.4 (Oct 20, 2012).** "Fixed lower body Animations In Menus" [Fan-wiki]. This implies the menu bear is an animated 3D model [Inference].
- **BBR 1.4.2 (Feb 28, 2013).** The game was renamed simply "Battle Bears" in this update [Fan-wiki]. File:Old_home_screen.jpg carries a "1.4.2" stamp [Observed]. Two things on the wiki point the wrong way:
  - The wiki caption calls it "The old Battle Bears Gold home screen" [Fan-wiki], but the sign reads "BATTLE BEARS" and the stamp is a BBR version, so it is the pre-Gold home screen [Inference].
  - The stamps ("1.3.1", "1.4.2", "2.1", "2.7") sit in the same corner and typeface across uploads by different people, and the 2026 builds print their build string in that corner ("3.0.0 / 11976788", "3.0.5_…"). So they are probably in-game version stamps, not uploader labels [Inference].
- **BBG 2.0 (May 24, 2013) and 2.1 (Jul 15, 2013).** File:The_New_Home_Screen_BBG.jpg ("2.1") shows the BBG layout [Observed]:
  - a "BATTLE BEARS GOLD" truss plate under a "BUNDLE DEALS" lightbox;
  - a pink-Huggable "STORE" monitor;
  - a round glossy blue PLAY button on a hazard-striped crate;
  - a GEAR UP sign with a gun silhouette, where 1.4.2 showed the bear's face.
- **2.2 (Aug 21, 2013).** Loadouts were added and are picked in the Gear Up menu [Fan-wiki]. In 2.7 (Jan 2014) the BUNDLE DEALS sign wears a holly sprig with a red bow [Observed: Smoke_screen.jpg]. A Feb 2015 Gear Up shows the LOADOUTS / CHARACTER / SKIN / TAUNT list and a "PRO-MODE FEATURES" monitor, the same layout as 2026 [Observed: Image-1423989888.jpg].
- **2017–2021 menu changes** [Fan-wiki, Updates table]:
  - 2.28 (Dec 20, 2017): "Menu button promoting the BBR2 Facebook Beta Testing Group is added".
  - 2.30 (Feb 12, 2018): "Chat is introduced; only players level 5 and up can chat" and "Seperate Quickplay and private matchmaking buttons are introduced".
  - 2.30.1: "Fixed bundle deal hover over the chat".
  - 2.51: "New team battle button added".
  - 3.0 (Nov 15, 2021): "New Map Lighting". Whether it touched the menu room is [Unverified].
  - 3.0.1 (Dec 18, 2021): "Updated menu buttons" and "Scale down weapon Graham in Home Menu".
- **Servers.** BBG servers shut down on Mar 12, 2024 [Fan-wiki].
- **2026 playtests.** The room returns with the 2013 layout and new buttons [Observed]:
  - Build 3.0.0, recorded Jul 30, 2026 (fan video, Rt0mWn6rk0c), and the official Aug 21 livestream: "TAP TO CHAT" bar, blue "CREATE MATCH", a "BATTLEBEARS.COM" merch monitor where STORE was, "GET GAS" / "GET JOULES".
  - Sep 20 official livestream and the JustNubz Playtest #4 video (build stamp "3.0.5_…"): orange "CUSTOM MATCH" and a green "QUESTS" monitor.
  - The final layout for the Nov 4, 2026 launch is [Unverified].
- **Not in the Steam trailer or screenshots.** The menu does not appear in the official Steam trailer contact sheets (all 108 frames) or the five Steam screenshots [Observed].
- **BB Heroes (2024).** Not checked [Unverified]. BBH has its own quests ("Complete a wide variety of fun quests to earn Bear Points") [Fan-wiki], but nothing shows it uses this room.

## Setting
- **What the room is.** A compact, dimly lit industrial steel bay. The front-end UI is built into it as physical props: crates, hanging signs, wall monitors and plaques hung on cables [Observed].
- **The UI is part of the set.** In the transition frames (Sep 20 livestream 49:00; Aug 21 livestream 22:20) the MAIN MENU sign, the PRO-MODE monitor and the PLAY button swing in perspective as the camera moves, so they are objects in the scene [Observed; Inference that the whole UI is in-world].
- **Where it is.** No source says where the room is or names it [Unverified]. In 2026 the bear stands at a wide window onto deep space before matches (Sep 20 livestream 10:40, 25:50, 44:00; Slinkster "Beta Test #4" thumbnail hq3) [Observed]. That points to a spacecraft or station [Inference].
- **Is it the Ursa Major?** Canon names the Ursa Major the bears' "flagship" ("Defend the flagship Ursa Major…", Steam BB-1) [Canon]. Nothing ties the menu room to it [Unverified]. BB-1's Ursa Major art (a grey hull with green thrusters, and a white-grey landing bay) does not match the room's teal-green steel [Observed: Ursa_Major.jpg, Battle_bears_neg1_2a.jpg].

## Layout
The game only ever shows fixed camera set-ups, so the room's full 3D shape is unknown [Inference]. Per view:
- **Main menu (2012–2026).** Frontal camera at bear height; the bear stands centre-low on a floor traced with thin dark octagonal inlay lines [Observed].
  - Left wall: a stack of green monitors (OPTIONS / LEVEL-RANK / EXTRAS / STORE, later BATTLEBEARS.COM) over a shelf edged in hazard stripes. In BBR the shelf holds a beige box-shaped electronic unit with red buttons. Below it, a big yellow-orange GEAR UP crate [Observed].
  - Centre top: hanging signs. In BBR, a metal "BATTLE BEARS" sign on a chain and S-hook above a cyan neon PLAY sign on a pink rubber hook; in BBG, the BUNDLE DEALS lightbox above the BATTLE BEARS GOLD truss plate [Observed].
  - Right: an icon monitor, then a yellow currency board fed by thick black ribbed cables, then the PLAY crate (BBG) or the BUNDLE DEALS crate (BBR) [Observed].
  - Back wall: steel panels, diagonal struts and pipes; in BBR, a "GET FREE GAS" monitor, a small yellow "GEAR UP" plate with a bear icon, and a framed screen showing a desert scene with a tall grey machine [Observed].
- **GEAR UP view.** The camera moves in on a round, white-lit floor pad where the bear stands [Observed: 2013, 2014, 2015, 2026].
  - Left: a tall green list board (PRIMARY / SECONDARY / MELEE / SPECIAL / EQUIPMENT 1–2 in 2013; LOADOUTS / CHARACTER / SKIN / TAUNT / PRIMARY… from 2015).
  - Top: the BUNDLE DEALS lightbox.
  - Right: a yellow MAIN MENU sign (red CANCEL while browsing), the currency board, the PRO-MODE monitor, a "TAP FOR DESCRIPTION" stats monitor with an EQUIP / BUY NOW plate, and the PLAY crate at bottom right [Observed].
  - Background: a corridor-like back bay with pipes, a red conduit and small yellow triangle markers (2015); in 2026, a thick pale curved pipe or lit frame arching down the left [Observed; whether it is a pipe or a door frame is unclear at 320 px].
  - In 2013 a "CLASS / SOLDIER" box with the bear's face sits top centre. It matches the small yellow face plate on the back wall of the BBR main menu, so the Gear Up station is probably that back corner of the same room [Inference].
- **Matchmaking (2013).** The camera faces a large recessed back panel with a bevelled frame, a T-shaped ceiling fixture with vents, and a cyan light bar at right. A tall monitor at left shows the mode and a map preview (an Aztec Attack pyramid) [Observed: Screenshot_2013-04-14…]. In 2026 a "MATCHING" monitor sits beside the chat log, and custom-match and lobby screens are flat 2D panels ("ARENA NAME / PASSWORD / PICK GAME TYPE / PICK LEVEL / CREATE") [Observed, low-res].
- **After match.** Two hazard-striped steel boards stand at left and right with a "28 VS 30"-style score plaque at top centre. A red dome beacon sits on the left board and a blue one on the right, washing the ceiling beams red and blue. TEAM STATS / gas / GEAR UP crates line the bottom [Observed: Old_result_screen.jpg; Aug 21 livestream 7:50]. In 2026 the scoreboard step adds a neon "RED TEAM WINS" or "BLUE TEAM WINS" header and PLAYER STATS / TAP TO CLAIM / GEAR UP crates [Observed].
- **Team sides.** Red is on the left and blue on the right on the results boards and on the 2013 loadout bar ("RED TEAM 0 VS 1 BLUE TEAM") [Observed]. The menu shows Sam-Are-I in orange armour; the wiki says the skin is "orange or blue armour (depending on the player's team)" [Observed; Fan-wiki].
- **2026 window.** A wide rounded window with a dark green steel sill looks onto a starfield. The camera sits behind the bear. This shot shows up between lobby and match before three different maps [Observed]. That makes it a shared transition, not part of any map [Inference]. In 2013 the matchmaking back wall is a closed recessed panel, and whether the 2026 window replaced it is [Unverified].
- **Verticality.** None seen: one floor, low ceiling, nothing to climb [Observed].

## Look
- **Sampled palette.** Approximate values from JPEG/WebP, checked against sample-box overlays [Observed, sampled]. The 2026 values come from stream and thumbnail captures and may carry colour shifts.

| Element | 2012–2015 | 2026 builds |
|---|---|---|
| Steel walls | #24332B mid, #2E4337 light, #1B251D shadow (2.1) | #2E4035 / #2A493B / #32513F (Jul 30 thumbnail); #314738 (Aug 21 stream); #1B251C in dim transition shots |
| Ceiling | #141E17 | — |
| Floor | pale sage-grey #6A7970–#748078 in the 2.1 main menu; #4C6148 (2013 Gear Up); #425340 (2.7) | warm tan-brown #725A3A–#7E6446 (thumbnail), #5D442B–#70573C (Aug stream); inlay lines about #251A20 |
| Hazard stripes | yellow #D4BA3E, black #242113 (2.1); lime-tinted #D6E829 under green monitor spill (1.4.2) | — |
| Monitors | green #226421 body, #132F12 dark, text glow #91CA90 | — |
| PLAY | BBR neon PLAY cyan #48F8FC core, #11BBD4, deep #015F76; BBG PLAY button sky blue #56A1B8, highlight #E3FBFE | — |
| BBG logo plate | red-orange #B82C04, yellow #FDFE70 | — |
| Results room | walls #10231D–#22453A; red beacon #621D1E; blue beacon #305361 / #233A57; red-washed beam #491918; blue-washed beam #4F5C82 | — |
| Window and highlights | — | space #0F000B–#160814, crimson nebula band #6C1220, mauve #5A3E4C, warm star-dust #A08A79–#DED2BF; pale pipe/frame highlight #FAFAEA |

- **Lighting.**
  - 2012–2015: dim, cool teal ambient light from above, with green spill from the monitors and cyan glows from the neon and PLAY signs. In Gear Up a white uplight disc sits under the bear [Observed].
  - 2026: the same teal walls over a warm tan floor, with cyan light bars on angled struts (Sep 20 livestream 52:20) [Observed].
  - Results: lit by the red and blue beacons [Observed].
  - There is no time of day; the room is interior and artificially lit [Observed].
- **Sky.** None in the main menu. The 2026 window shows deep space: dense white stars, a violet nebula, a warm golden-pink galactic band and dark drifting rock silhouettes at the right edge [Observed].
- **Materials.** Painted steel panels with seams; diagonal struts; thick ribbed black cable conduit; chains, S-hooks and a pink rubber hook; worn yellow-and-black hazard stripes; phosphor-green monitors; a backlit lightbox; a metal truss plate; a beige retro electronic box; metal plaques hung on coiled cables with frayed blue cable ends [Observed].
- **Particles.** Cyan four-point sparkle glints around PLAY, the currency board and GEAR UP (1.4.2, 2.1, 2026), and white star sparkles on the EQUIP / BUY NOW plates [Observed]. No weather [Observed].
- **The bear.**
  - 1.4.2 and 2.1 menus: Oliver (Soldier) in the Sam-Are-I samurai skin holding a katana [Observed]. The katana is very likely the Kumakiri, the Soldier's katana melee (BBR 1.3.2) [Fan-wiki; Inference].
  - BBR 1.3.1: default Oliver [Observed].
  - 2026 playtest menus: default Botch with the lime Doom Cloud (fan thumbnail), default Oliver (Aug stream) and a charcoal-grey bear (Sep stream) [Observed].
  - Whether the menu bear always shows its primary weapon or the last item viewed is [Unverified].

## Landmarks
1. The round white-lit floor pad where the selected bear stands in GEAR UP [Observed].
2. The big yellow-orange GEAR UP crate (bear face in BBR, then a machine-gun silhouette) and the black hazard-striped crate with the glossy round blue PLAY button [Observed; Fan-wiki for the Machine Gun outline].
3. The hanging signs: the BUNDLE DEALS lightbox and the red-and-gold BATTLE BEARS GOLD truss plate. In BBR, a metal "BATTLE BEARS" sign and a cyan neon PLAY sign on hooks [Observed].
4. The wall of green monitors at left and the yellow currency board fed by thick black cables at right [Observed].
5. The after-match boards with the red (left) and blue (right) dome beacons [Observed].
6. The 2026 starfield window with its green steel sill [Observed].

## Hazards and interactive elements
- No hazards: the room has no combat [Observed].
- **Interactive.** Every button is a prop [Observed; Inference that they are in-world]. The bear holds equipped items in class-specific stances, and some weapons have their own Gear Up stance or "menu display slide" [Fan-wiki; Observed: 2013–2015 Gear Ups].
- **Pop-ups.** Error and description pop-ups are metal plaques hung by coiled cables over the dimmed room ("GAME CANCELLED", "DISCONNECTED!", the 2026 class blurbs) [Observed].
- **2026 additions.** A green "TAP TO CHAT" bar at top centre; chat itself dates from 2.30 (2018) [Observed; Fan-wiki]. The chat log can overlay the main menu [Observed: Sep 20 livestream 23:30–24:10].

## Easter eggs and references
- "BOOURNS" on the Game Cancelled button [Observed: Game_Cancelled.jpg, 2013]. It is probably a nod to *The Simpsons*' "Boo-urns" [Inference]. "THAT SUCKS" on the Disconnected button [Observed].
- Main-menu tips: the 1.4.2 support ticker and "PICK UP YOUR VISUAL SCANNING!" on the automatching screen [Observed]. These match the 1.3.2 "main menu tips/announcements" feature [Inference].
- **Seasonal dressing.** A holly sprig and red bow on the BUNDLE DEALS sign in 2.7, Jan 2014 [Observed]. Other holidays [Unverified].
- **A mode that never shipped.** "CAPTURE THE FLAG", marked coming soon, in the 2011 sneak-peek carousel [Observed]. BBG shipped Team Battle, Plant the Bomb and Free-For-All, plus the later King of the Windmill and Battle Royale modes [Fan-wiki].
- **Back-wall pictures.** The BBR back-wall screen shows a desert with a tall grey machine, perhaps a map preview [Observed; which map is Unverified]. The beige retro electronic box on the left shelf is [Observed; what it is is Unverified].
- **Do not borrow from other games.** On the wiki's Updates page, "New Nostalgic Menu Music" belongs to Battle Bears Overclock 3.0 (2020) and "Tip/Jokes during Matchmaking menu" to BB Heroes 1.0.27 (2023), not to BBG [Fan-wiki].

## Sound and music
- The official soundtrack has "Main Menu (BBG)" (1:49), "After Match" (1:04) and "Main Menu (BBR)" (1:09) [Canon]. They are credited only as a group to Rob Ruiz, AnDrue Humphreys and Benjamin Vavak [Canon].
- The wiki hosts "BBG title music.ogg" (9:30) and "BBR title music.ogg" (6:29), uploaded Jun 16, 2013, with no description and used on no page [Fan-wiki upload]. I did not listen to them; whether they are the menu tracks is [Unverified].
- "Bears With Guns (Main Menu)" is a 2009 Battle Bears soundtrack track, not BBG [Canon, per our notes].

## Images viewed
All paths below are under /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/
- **Home screens (from frozen_pundra/bbgimgs/conv/):** hangar/img/Old_home_screen_sm.jpg (Old_home_screen.png); hangar/img/The_New_Home_Screen_BBG_sm.jpg (The_New_Home_Screen_BBG.png); hangar/view/old142_poster.jpg, hangar/sheets/old142_details.jpg and hangar/view/new21_center.jpg (crops of those two); hangar/img/2.1_sm.jpg; hangar/img/IMG_0913_sm.jpg; hangar/img/Screenshot_20180407-085431_2_sm.jpg.
- **BBR main menu:** hangar/img/Oliver-main-menu_960.jpg (File:Oliver-main-menu.png, https://static.wikia.nocookie.net/battlebears/images/3/34/Oliver-main-menu.png/revision/latest).
- **Other wiki images** (static.wikia.nocookie.net URLs in hangar/wiki/allimages.json), opened as hangar/view/*.jpg: Screenshot_2013-05-01-06-09-29, Screenshot_2013-04-14-14-36-54 (and am13_bright.jpg), Smoke_screen (and 27_sign.jpg), New_Loadout_System, Game_Cancelled, Disconnection, Flawless_Disguise, Weapon_selected-_crossbow (a different, 2D game screen), Old_result_screen, Update_1_3_2, gu2015 (Image-1423989888.jpg).
- **Wiki triage sheets:** hangar/sheets/triage1.jpg and triage2.jpg (OF-main-menu, Nick, 1.4.2, Screen_Shot_2013-*, Screenshot_(509), Yo_Mambas_Bundle_REAL, Rainbow_booster_bundle, Chubby_bundle, AstoriaStarter, GrahamBundle, OCOBundle, BBG_Lobbys, PH_MenuDisplay, DCNew, OliverNew, Untitle, Custom-matches…, Botch23Preview2, HomeNavBBR); hangar/sheets/later_triage.jpg (Image-0, IMG_0156/0157, Image-1428969087, Image103/104, BBG_splash_1280_800, Image-0/1.jpeg, IMG_0402, Image.png); hangar/sheets/ursa.jpg (Ursa_Major, Battle_bears_neg1_2a, Battlebears-1_screen1/2).
- **Sep 20, 2026 SkyVu livestream** (ejjsoKQ-VXU; storyboard frames from lineup_gap/sb/ejjsoKQ-VXU/): hangar/sheets/ej_000_110.jpg, ej_120_230.jpg, ej_240_350.jpg, ej_360_470.jpg, ej_480_1190.jpg, ej_1200_1910.jpg, ej_1920_2630.jpg, ej_2640_3570.jpg, ej_pick_room.jpg (49:00, 52:20, 10:40, 25:50, 32:30, 33:10, 30:30, 38:50), ej_space.jpg (10:40, 44:00, 17:20, 22:40), zoom_floor.jpg, rightcol_sep_vs_aug.jpg; hangar/view/sb_0130.jpg, sb_1550.jpg, sb_2940.jpg, sb_3140.jpg.
- **Aug 21, 2026 SkyVu livestream** (xP27fWSCSKs; storyboard in hangar/sb_xP27/): hangar/sheets/xp_0000_0950.jpg, xp_0960_1880.jpg, xp_pick.jpg (22:20, 7:50, 7:40, 0:00); hangar/pal/ov_xp0.jpg, ov_xp0b.jpg.
- **JustNubz Playtest #4 showcase** (-lAtv-j9Sms, fan; storyboard in hangar/sb_showcase/): hangar/sheets/sc_0000_1030.jpg, sc_1040_2070.jpg, sc_2080_3080.jpg, sc_pick.jpg, gu_2015_vs_2026.jpg, signs.jpg; hangar/view/sc_thumb_corner.jpg.
- **Thumbnails** (https://i.ytimg.com/vi/<id>/…): hangar/sheets/yt_thumbs.jpg (ejjsoKQ-VXU, -lAtv-j9Sms); yt_thumbs2.jpg (Rt0mWn6rk0c, tNcHwpk5UuY); hangar/yt/th_Rt0mWn6rk0c_maxresdefault.jpg; hangar/view/slink_hq3.jpg (tNcHwpk5UuY hq3); hangar/sheets/official_thumbs.jpg (C7uFxvSZ10c, d2ByJWrsoec, pmE2jKQLSms, BcEeAzXFChI, U3XDJXo1Ej4, wNpM1woYv7k, 0gYEZCMQfmA, IucMFqzR_Qw, rfAyqVJrli4, r91WkR10W2A, xP27fWSCSKs); bbr_thumbs.jpg; bbr_trailer_thumbs.jpg.
- **Steam trailer and screenshots:** hangar/sheets/trailer_a.jpg, trailer_b.jpg and trailer_even.jpg (all 108 frames of weapons/visuals/trailer/); hangar/sheets/steam_screens.jpg (weapons/visuals/steam_screens/screen_00–04).
- **Palette sample overlays:** hangar/pal/ov_21.jpg; hangar/sheets/pal_overlays.jpg; hangar/sheets/res_lamps.jpg.

## Prompt pack
**Establishing shot (9:16, environment only, style-neutral; append the house-style suffix):**
"Vertical 9:16 establishing shot of a compact, dimly lit sci-fi equipment bay built from dark teal-green painted steel panels with visible seams and diagonal support struts, seen from a low camera at small-character height looking straight in. In the centre of the floor sits a round, softly glowing white floor pad set into a warm tan steel floor traced with thin dark octagonal inlay lines. On the left wall, a tall stack of wall-mounted monitors glows phosphor green with blank screens above a shelf edged in worn yellow-and-black hazard stripes, which holds a boxy beige retro electronic unit with small red buttons. Below them stands a big glowing yellow-orange crate panel showing only a dark machine-gun silhouette. On the right, a black crate with yellow-and-black hazard-striped edges carries one large glossy round sky-blue button ringed with cyan sparkle glints, under a yellow wall panel fed by thick ribbed black cables. Overhead, a backlit lightbox sign glowing icy cyan-white and a red-and-gold metal truss plate hang from chains and hooks, both blank. The back wall has steel panels, pipes, a red conduit and small yellow triangle markers, and a wide rounded window onto deep space: dense white stars, a violet nebula, a warm golden galactic band and dark drifting rock silhouettes. Cool teal ambient light, green monitor spill, cyan glows. No characters, no readable text or logos."
- **Documented vs invented.** The props, colours and space view are documented [Observed]. Four things are [BBG News invention]: the vertical framing (the game is landscape); putting the space window in the same shot as the main-menu props (they never appear together); blanking every sign; and the red conduit and triangle markers on the main-menu back wall (they are seen only behind the Gear Up).
- **Era toggle.** For a 2013 look, swap the floor to "pale sage-grey steel" and the window to "a large closed, recessed steel panel" [Observed: 2.1 home screen, 2013 automatching shot]. For a BBR look, swap the blue button for "a hanging cyan neon tube sign" and the lightbox for "a weathered metal sign hung on a chain and S-hook" [Observed: 1.3.1 and 1.4.2].

**Staging spots**
1. **The Gear Up pad.** In the game, the selected bear stands on the lit disc holding its equipped item, and the list board changes items beside it [Observed]. Short idea: a bear tries skins and weapons in fast cuts while a teammate waits impatiently. The flash on each swap and the waiting teammate are [BBG News invention].
2. **The space window before a match.** In 2026 the camera sits behind the bear at the window just before the match loads [Observed]. Short idea: a nervous bear waits for "MATCHING" and fogs the glass. The fogged glass and the dialogue are [BBG News invention]; any "MATCHING" text gets added in post.
3. **The after-match boards.** Red beacon on the left board, blue on the right; the soundtrack's "After Match" track exists [Observed; Canon]. Short idea: winners gloat under one beacon while the losers sulk under the other. The action is [BBG News invention].
- **Bonus gag.** The "GAME CANCELLED" plaque drops on its coiled cables and the only button says "BOOURNS" [Observed: text and plaque design]. The plaque dropping is [BBG News invention], and the text goes in in post.

## Confidence
**observed** for the look, props and palette across BBR 1.3.1 (2012), 1.4.2, BBG 2.1, 2.7 and 2015, and the 2026 builds. **partial** for the room's 3D layout and for how the views connect. **unknown** for any in-story location.

## Corrections to our notes
- **No wrong statements found.** I checked the lore report, the character-lore research notes, the 11 character files, the map drafts, the short scripts and the final souls. Nothing they say about the menu room or Gear Up is wrong. The JustNubz "build 3.0.5" in wil.md matches the build stamp in the showcase thumbnail, and the Aug 9, 2026 date in botch.md matches the video, which says it was recorded 30/7/2026.
- **Alignment note, not an error.** bbg-news-repo/characters/riggs.md, logline 4 [BBG News invention]: "Riggs sticks a Buzz Kill queen bee beside the hangar door". If it is staged in the BBG menu room, no door has been seen there. The documented openings are the 2013 recessed back panel, the 2026 space window and a pale curved frame behind the Gear Up pad.
- **Precision on the gap brief.** In the Sep 20 livestream, 0:00–2:00 is the main menu and 2:10–7:50 is GEAR UP (character, skin and weapon browsing); the main menu returns at 10:00–10:10 and 23:30–24:10. The 2012 BBR 1.3.1 screenshot, the 2014 (2.7) and 2015 Gear Ups and the Aug 21, 2026 livestream also show the room, besides 1.4.2, 2.1 and Sep 2026. The Aug 21 build reads "CREATE MATCH" and has no QUESTS button; "CUSTOM MATCH" and "QUESTS" appear by Sep 20.

## Open questions
- Is the room meant to be a real place in the story (the Ursa Major, another ship, a station)? No source says.
- Where do the Gear Up pad, the matchmaking wall, the results boards and the 2026 window sit relative to the main-menu camera?
- When did the floor turn warm tan: BBG 3.0's "New Map Lighting" (Nov 2021) or the 2026 work?
- Will the Nov 4, 2026 release keep CUSTOM MATCH, QUESTS and the space-window transition?
- What does the BBR back-wall screen show (desert scene with a tall grey machine)? What is the beige box on the shelf?
- Does the menu bear hold its primary or the last item viewed?
- Is there seasonal dressing in 2026, and did other holidays dress the room (only 2.7's holly is documented)?
- Are the wiki's "BBG title music.ogg" and "BBR title music.ogg" the soundtrack's "Main Menu (BBG)" and "Main Menu (BBR)"?
- Do archived SkyVu blog posts on BBG 2.0 or 3.0 describe the menu? Wayback was unreachable in this session.
- The Playtest #4 corner stamp reads "3.0.5_2026.11.19_B1" at thumbnail size, which is after the video's Sep 20, 2026 date. Is the date misread?
- Does BB Heroes (2024) reuse this room?
