# Shared environment conventions (all BBG maps)

This dossier covers what every Battle Bears Gold arena has in common: team bases and spawns, how red and blue show up in the scenery, pickups, jump pads, the Plant the Bomb hardware, kill zones, skies, prop scale, art direction and map music. With it, a short can drop any character into any real map without breaking the game's own rules.

This is the verified edition. I re-fetched every cited page and re-opened every cited image on 2026-10-18. Every claim that survived is kept. Claims that failed are corrected in place, and new evidence is added where I found it.

**Sources I reached (2026-10-18):**
- The fan wiki through the MediaWiki API:
  - all 16 pages in Category:BBG Maps;
  - BBG Maps, Plant the Bomb, Team Battle, Free-For-All, King of the Windmill, Pick-Ups, Bearscream Sandwich, Imperial Basket Grande, Health Pack, Shield, Joules, Gas and Gas Meter;
  - Updates, Battle Bears Gold/Versions, Battle Bears Gold, Battle Bears Overclock, Sky Pirates and Bearzerker;
  - file metadata, including the stored YouTube metadata.
- The Steam store API for the game (4408320), the Soundtrack (5321720) and the Demo (5225670); the Soundtrack store page (its track list); the game's store page and its looping "extras" video; the Steam News API and its four announcement images.
- battlebears.com and play.battlebears.com, both live.
- YouTube:
  - oEmbed titles and channels for 11 videos;
  - watch pages for the 2.3 and 2.8 map previews, "BBG Maps Ranked part 1", the Sky Pirates reveal and the Playtest Highlights;
  - YouTube's own `next` metadata endpoint for the May 30, 2013 BBG trailer, "The Battle Bears Marecraft Arena" and "Sky Pirates in BBG!";
  - chapter titles of two fan playtest uploads;
  - thumbnails.
- The Steam trailer file (54 s) and its frames.
- The Toxic Terror concept artist's DeviantArt page.

**Sources I could not reach:**
- web.archive.org. curl got a connection reset three times and WebFetch refused the domain. So nothing here is re-verified from archived SkyVu pages (map blurbs, the 2012 BBR maps page, the 2.4 and 2.6 release notes).
- Some YouTube watch pages were rate-limited.
- I watched no video. I saw only frames I extracted from the Steam trailer and the store loop, plus YouTube thumbnails.

**Provenance warning (applies to everything below):**
- The Steam trailer "Battle Bears Gold Premium - Trailer" [Canon] re-uses SkyVu's trailer "BATTLE BEARS GOLD Trailer: Award-Winning Multiplayer Shooter Game" (rfAyqVJrli4, uploaded May 30, 2013) [Canon: title, date].
  - Its thumbnails hq1, hq3, maxresdefault and hqdefault match Steam-trailer frames at 11.9 s (Graham card), 42.8 s (Oliver card) and 29.9 s (Tillman card).
  - The scores are greyscale 160×90 MSE 3.6–6.2. hq2 scores 477. The medians against all 540 frames are 6,490–7,476 [Observed: my pixel comparison against frames at 10 fps].
- The five Steam screenshots are frames of the same trailer: screen_00 ≈ 36.4 s, screen_01 ≈ 30.7 s, screen_02 ≈ 50.6 s, screen_03 ≈ 9.8 s and screen_04 ≈ 26.4 s. Their MSE is 147–1,074 against medians of 6,574–10,812 [Observed]. The copies on the store today are byte-identical to our local copies [Observed].
- Supporting evidence:
  - The trailer's class cards are exactly the 8 classes of May 2013 (B-1000, Graham, Astoria, Wil, Tillman, Huggable, Riggs, Oliver) [Observed].
  - Its gameplay shows only maps that existed in BBG 2.0: Gold Digger, Aztec Attack, Abusement Park, Shortest Parsec, Space Oddity, H.I.P. Test Lab, Marecraft, Skate or Die and Sky View [Observed].
  - It shows none of the maps removed at 2.0 (Desert Airmine, Haunted Castle) and none added later (Toxic Terror, Frozen Pundra, Steam Yard Blues) [Observed; removals and additions per Fan-wiki].
  - The 2013 trailer's description says "Choose from 8 classes" and "3 New Maps: -Gold Digger -Skate or Die -Sky View" [Canon].
  - **So every gameplay frame from the Steam trailer or screenshots shows May 2013 (BBG 2.0) environments, not the 2026 build [Inference, strong].**
- The genuine 2026-build images I saw:
  - SkyVu's final-playtest banner (No Bear's Land) [Observed];
  - the official "Battle Bears Gold launches Nov 4, 2026 - Official Playtest Highlights" thumbnails (build label "3.0.0"). Its description says "Highlights from our first two Discord playtests" [Canon];
  - the Sky Pirates reveal and "Sky Pirates in BBG!" thumbnails;
  - the "BBG Maps Ranked part 1" thumbnails;
  - fan thumbnails from the Oct 15 final playtest (build label "3.0.7…") [Observed].
- SkyVu lists "Lighting improvements" for the final 2026 playtest [Canon], and BBG 3.0 (Nov 15, 2021) already listed "New Map Lighting" [Game text via wiki]. So the 2026 lighting may differ from the 2013 frames [Inference].

**Label note:**
- I use [Game text via wiki] for SkyVu's own update notes as the wiki's Updates page transcribes them. That page says it provides "the official update descriptions"; I could not open the original store notes.
- An "≈ #hex" value is the median of pixels I sampled in an image I opened. It is approximate and varies with the region sampled.

---

## 1. Official text about maps and map design

**Steam game page (app 4408320):**
- "compete with friends across 16 wacky maps. A third-person shooter like no other!" [Canon]
- "Grab your A Salt Rifle, Bearzooka and those Turkish SW Boots and fight it out with friends across beloved Battle Bears locations." [Canon]
- "Iconic Maps will return so prepare to jump back into classics such as No Bears Land, Gold Digger and Space Oddity. You can even make some time for that yearly match on Steamyard Blues, most likely just for the soundtrack." [Canon]
- "Speaking of music, this game has bangers so get ready to enjoy that awesome OST once again." [Canon]
- "Whether you're a Team Battle diehard or prefer the underrated Plant the Bomb, there is plenty of battling to be done." [Canon]
- Modes: "-Team Deathmatch (TDM)", "-Free for All (FFA)", "-Plant the Bomb (PTB)" [Canon]
- "All assets in this game are created by human artists." [Canon]

**Steam Soundtrack page (app 5321720, release "Nov 4, 2026"):**
- "The official BATTLE BEARS GOLD Soundtrack featuring original map and menu music by Rob Ruiz, AnDrue Humphreys, and Benjamin Vavak. Includes bonus vocal tracks by Vivyd, Brian Bell & Leck One." [Canon]
- "features the complete collection of map and menu music from the award-winning 4v4 class shooter" [Canon]

**Steam Demo (app 5225670):** release "October 2026" [Canon]. play.battlebears.com: "Play the demo on Steam from October 19-26" [Canon].

**Steam News:**
- Aug 19, 2026, "3rd Discord Playtest this Friday! A New Map comes to BBG!", lists "Auto matchmaking", "New Map: Sky World" and "Bug fixes" [Canon].
- Oct 14, 2026, "Final Discord Playtest this Thursday Oct 15":
  - "Headline additions: -Custom keybinds -Jukebox -UI controller support -Lighting improvements -Lots of bug fixes" [Canon];
  - "please record some footage, ideally on PC and without the UI (press the H key to hide it)" [Canon];
  - the version is "available on Windows, iOS and Android" [Canon].
- The Oct 14 banner reads "CLOSED TESTING 5", "-MENU JUKEBOX", "-REDEEM CODE SYSTEM", "-ANDROID SUPPORT" and "-LIGHTING, EFFECT & TEXTURE IMPROVEMENTS" [Observed: Steam clan image b7c8f8f1….png].

**battlebears.com (live):**
- "This year we're bringing it back to Steam PC and Mobile, packed with new modes, maps, skins and more! Launches Nov 4" [Canon].
- BB Heroes: "(BBH) is the newest game in the series featuring all the famous characters, weapons, and maps with re-imagined BB-1 Campaigns!" [Canon].

**YouTube (official BATTLE BEARS channel; titles and channel from oEmbed; dates and descriptions read from YouTube's own page data):**
- "The Battle Bears Marecraft Arena" (Apr 5, 2013): "Have you ever tried to take out a team of highly skilled players INSIDE A GIANT UNICORN??!!!! … New level coming to Battle Bears in update 1.4.3 on iOS and Android in April, 2013" [Canon].
- "BATTLE BEARS GOLD Trailer: Award-Winning Multiplayer Shooter Game" (May 30, 2013): "Choose from 8 classes", "3 New Maps: -Gold Digger -Skate or Die -Sky View" and "HD Graphics (Only available on higher end devices. App automatically detects what graphic mode to show)" [Canon].
- "BATTLE BEARS GOLD Update 2.3 New Map Preview" (Sep 13, 2013): "Check out this epic fly through of the new map coming to BATTLE BEARS GOLD in Update 2.3! Are you excited?" [Canon].
  - The map is Toxic Terror. The wiki embeds this video on its Toxic Terror page [Fan-wiki], and the thumbnails show a dark sewer with green ooze under "NEW LEVEL COMING IN 2.3..." [Observed].
- "BATTLE BEARS GOLD Update 2.8 "Steam Yard Blues" Map Preview" (Feb 21, 2014): "Another new update on the horizon means another awesome new map! Check out this epic fly through of the new map, Steam Yard Blues, coming to BATTLE BEARS GOLD in Update 2.8!" [Canon].
- "Battle Bears Gold launches Nov 4, 2026 - Official Playtest Highlights" (Aug 16, 2026): "Highlights from our first two Discord playtests for Battle Bears Gold." [Canon].
- "Battle Bears Gold 2026 - Sky Pirates Map Reveal" (Aug 31, 2026): "Gameplay highlights from the new Sky Pirates map!" [Canon].
- "Sky Pirates in BBG!" (Sep 7, 2026): "Enjoy the highlights from our Sky World playtest!" [Canon].
  - **So "Sky World" (the Steam post) and "Sky Pirates" (the video titles) are one map** [Inference, strong].
- "BBG Maps Ranked part 1" (Oct 11, 2026): "Maps ranked pt1, do you agree?" [Canon].

**Update notes (BBR 2011–13, BBG 2013–21, BBO 2020):**
- "Spawn Shield - Newly spawned players have a few seconds of invincibility." (BBR 1.2.1, Jan 27, 2012) [Game text via wiki]
- "NEW Game Mode: "Plant the Bomb"" (BBR 1.3, May 3, 2012) [Game text via wiki]
- "Awesome New Map - Facing Temples" (1.3.1, Jun 28, 2012) [Game text via wiki]
- "New Level: Abusement Park" (1.3.2, Aug 24, 2012) [Game text via wiki]
- "NEW Haunted Castle map with interactive features!" (1.3.3, Oct 10, 2012) [Game text via wiki]
- "Fixed Abusement Park Skybox" (1.3.4, Oct 20, 2012) [Game text via wiki]
- "New Space Station map!" (teased in 1.4.1, Jan 10, 2013) [Game text via wiki]
- "NEW- The Shortest Parsec Map!" (1.4.2, Feb 28, 2013) [Game text via wiki]
- "NEW MAP: The Marecraft! Fight or die inside a giant living unicorn! The goriest battlefield ever!" (1.4.3, Apr 15, 2013) [Game text via wiki]
- "3 NEW maps!" (teased in 1.4.3 for BBG) [Game text via wiki]
- "Upgraded Map Lighting, check out how Skyworld has benefitted!" (Battle Bears Overclock 3.0, Jul 3, 2020) [Game text via wiki]. So "Skyworld" is an Overclock map in SkyVu's own notes. The wiki's Overclock map list has "Sky Pirates" and no "Skyworld" [Fan-wiki].
- "New Map Lighting" (BBG 3.0, Nov 15, 2021) [Game text via wiki]

**Map design process.** The only first-hand statement I found is from the Toxic Terror concept artist Deus-Nocte (DeviantArt, "[Battle Bears] Toxic Terror Concepts", Sep 16, 2013, re-read verbatim):
> "Though 2.3 isn't out yet, I was cleared to post these concepts of the new level! The 3D team modeled the basic structure and it was up to me to do something with it. These concepts went through a lot--we tried different color schemes and stuff until we settled on this (They were painted in black and white). I also textured this level, which ended up being my biggest project to date; 89 hours clocked on it for 4 texture sheets. The version in game has some really awesome lighting and I had to add a lot more to the walls in order to fill them up."

It is a personal page, so it is [Unverified] as SkyVu's voice. That the author worked on the SkyVu map is [Inference], from "I was cleared to post".

**Not verified this pass:** our notes cite archived SkyVu map blurbs, for example on Marecraft. I could not reload them because Wayback was unreachable [Unverified].

**Gaps:** none of the 2026 official texts I read describes spawn rooms, team-colour rules, pickups or hazards [Inference: absent from Steam, battlebears.com and the playtest posts and video descriptions].

---

## 2. Roster and lifecycle (eras)

| Map (old name) | Added | Removed / reworked | 2026 evidence |
|---|---|---|---|
| No Bear's Land (Battlefield Airpad until 2.0) | BBR 1.0, Oct 8, 2011 [Fan-wiki; date Game text via wiki] | Reskins: winter 2.26 (Jan 17, 2017), summer 2.27 (May 29, 2017), "Winter Map is back" 2.28 (Dec 20, 2017), spring 2.51 (Apr 13, 2018) [Game text via wiki] | Named on Steam [Canon]; final-playtest banner and Playtest Highlights maxres [Observed]; OST track 2 [Canon] |
| H.I.P. Test Lab (Huggable Factory) | BBR 1.0 [Fan-wiki] | – | OST track 5 "Huggable Factory" [Canon]; 2013 footage only [Observed]; no 2026 sighting found [Unverified] |
| Space Oddity (Spacecraft) | BBR 1.0 [Fan-wiki] | – | Named on Steam [Canon]; OST 6 [Canon]; 2013 footage (30–32.5 s, screen_01) [Observed] |
| Desert Airmine | BBR 1.0 [Fan-wiki] | Removed 2.0 (May 2013), returned 2.7 [Fan-wiki] | OST 12 [Canon]; fan final-playtest thumbnails, build 3.0.7 [Observed: fan upload] |
| Aztec Attack (Facing Temples) | BBR 1.3.1, Jun 28, 2012 [Game text via wiki] | – | OST 13 [Canon]; 2013 footage [Observed] |
| Abusement Park | BBR 1.3.2, Aug 24, 2012 [Game text via wiki] | Skybox fix 1.3.4 [Game text via wiki] | OST 1 [Canon]; 2013 footage [Observed] |
| Haunted Castle | BBR 1.3.3, Oct 10, 2012 [Game text via wiki] | Removed 2.0, returned 2.4 (Oct 24, 2013) [Fan-wiki] | OST 11 [Canon] |
| Shortest Parsec | BBR 1.4.2, Feb 28, 2013 [Game text via wiki] | – | OST 9 [Canon]; 2013 footage [Observed]; a 2026 fan thumbnail of a red-and-white space deck with a jump pad [Observed; identification Inference] |
| Marecraft | BBR 1.4.3, Apr 15, 2013 [Game text via wiki] | – | OST 8 [Canon]; 2013 footage [Observed] |
| Gold Digger, Skate or Die, Sky View | BBG launch, May 24, 2013 (the "2.0 update" in the wiki's map pages; the Versions table labels it 1.0) [Fan-wiki]; "3 New Maps" [Canon: May 30, 2013 trailer description] | – | Gold Digger named on Steam [Canon]; OST 4, 7, 3 [Canon]; 2013 footage of all three [Observed]; a 2026 Playtest Highlights thumbnail on a concrete skatepark [Observed; identification as Skate or Die is Inference] |
| Toxic Terror | 2.3, Sep 27, 2013 [Fan-wiki] | – | OST 14 [Canon]; no 2026 sighting found [Unverified] |
| Frozen Pundra | 2.7, Jan 23, 2014 [Fan-wiki] | – | OST 10 [Canon] |
| Steam Yard Blues | 2.8, Mar 4, 2014 [Fan-wiki] | – | Named on Steam as "Steamyard Blues" [Canon]; OST 15 [Canon]; fan final-playtest thumbnails [Observed: fan upload] |
| Tutorial (single-player) | BBR [Fan-wiki: "The transition from Battle Bears Royale marked several minor changes to the Tutorial"] | – | OST 18 "Tutorial" [Canon] |
| Sky World = Sky Pirates | New in the 3rd BBG playtest, Aug 21, 2026 [Canon]; an Overclock launch map (v1.0, Feb 2016) per the wiki [Fan-wiki]; "Skyworld" in Overclock 3.0 notes [Game text via wiki] | – | Steam post "Sky World"; SkyVu videos titled "Sky Pirates", described as the "Sky World playtest" [Canon] |

**Map count:**
- The wiki lists 15 classic arena maps [Fan-wiki]. The wiki's own Battle Bears Gold page still says "14 different stages", written before Steam Yard Blues [Fan-wiki, stale].
- The 2026 OST has exactly 15 map-named tracks (1–15), plus "Castle Royale" (16), and none for Sky World/Sky Pirates [Canon].
- 15 classic maps + Sky World = Steam's "16 wacky maps" [Inference].
- The ranking short's tier list has rows "1-4", "5-8", "9-12" and "13-16" [Observed: jkv6FHPghx8 hq2]. Its title frame shows a 4×4 grid of 16 map tiles [Observed: jkv6FHPghx8 hq1 and maxresdefault; the tiles are too small to identify all of them]. Both fit 16 [Inference].
- Whether the Tutorial counts, and whether every classic map ships, is [Unverified].
- **2026 playtest sightings (fan chapter titles, read by me on the watch pages; I did not watch):**
  - InstableGR, "Battle Bears Gold - PC Playtest #3 (8/21/26)", 12 chapters: Sky Pirates, No Bear's Land, Steamyard Blues, Frozen Pundra, Sky View, Shortest Parsec, Space Oddity, Aztec Attack and Abusement Park.
  - InstableGR, "Battle Bears Gold - Final PC Playtest (10/15/26)", 17 match chapters: Desert Airmine, Steamyard Blues, Space Oddity, Frozen Pundra, No Bear's Land, Gold Digger, Shortest Parsec, Sky View, Sky Pirates, Marecraft and Haunted Castle.
  - Modes in these chapters: "Team Battle", "Free-for-All", "Plant the Bomb" and "Kill Confirmed" [Unverified: fan titles].
  - Together that is 12 classic maps plus Sky Pirates. **H.I.P. Test Lab, Skate or Die and Toxic Terror do not appear in these chapter titles** [Observed: chapter lists]. Skate or Die probably appears in an official 2026 thumbnail [Inference].

---

## 3. Team colours and team bases (red vs blue)

**Rules:**
- Two teams, Red and Blue, up to 4 players each [Fan-wiki: Team Battle, King of the Windmill].
- Plant the Bomb gives each team "a bomb in each team's color and a bomb tube in each team's color" [Fan-wiki].
- In Free-For-All, "all other players will be viewed as being on the Blue team, with the player in third-person view seeing themself as being on the Red team", and the in-game leaderboard has "a dark green background" [Fan-wiki].
- A fan thumbnail from the 2026 final playtest matches this: in a "GET KILLS TO SCORE POINTS" match, the opponents carry blue triangle markers [Observed: 1MP1rFi4t-Q maxres3, JustNubz upload, build 3.0.7].
- The Tutorial has a "TEAM COLORS" sign over red voxel/lattice bear dummies, one wearing a blue cap [Observed: Mqdefault_(6).jpg, 320×180, low resolution].

**HUD:**
- The red score sits on the left and the blue on the right, with a cog between them, in every era I saw [Observed]:
  - 2012–spring 2013: separate red and blue bars with a grey cog (Oliver-battlefield…png, A_life_upside_down.jpg);
  - from Sep 2013: one tapered red/blue bar with a green cog (Scary_Light.png, Imawe.jpg, Screenshot_(509).png);
  - 2026: the same tapered bar, with a round green radar under it (C7uFxvSZ10c, r91WkR10W2A hq3).
- Sampled colours (A_life_upside_down.jpg, uploaded Apr 27, 2013, BBR era): red ≈ #FD0101, blue ≈ #013CFC [Observed].
- Plant the Bomb swaps the score icons for red and blue checkered bomb icons [Observed: Blue-bomb.png, 2012; Plant_the_bombbbbbb_b.jpeg and Plant_The_Bomb_Mode_Bomb_Explosion.jpeg, spring 2013].
- The Team Battle mode card splits a red-lit team on the left from a blue-lit team on the right with a jagged line [Observed: Team_Battle_Icon.jpg].
- The results room has a red siren lamp on the left and a blue one on the right, with a "1 VS 4" red/blue banner [Observed: PTB_balance_beam.jpg, 2014].

**How team colour shows in the scenery.** It is always an accent and never a repaint [Inference from all of the below].
- **No Bear's Land:**
  - The olive concrete keep wears bright red bands on one end (2012, ≈ #D71D18–#EE1E1A) and blue bands on the other [Observed: Oliver-battlefield-airpad-red-base-front.png; Battlefield.png].
  - The Oct 2026 banner shows the blue-banded keep, still stencilled "PMOC 20-11" [Observed].
  - The two crashed Pelican'ts carry team stripes: red on one, blue on the other [Observed: Battlefield.png]. A blue-banded Pelican't appears in the 2012 capture, and a dark wreck with red markings in the 2026 banner [Observed].
  - Perimeter posts are capped red at one end and blue at the other (≈ #C71512 / #293AA6) [Observed: Battlefield.png].
- **H.I.P. Test Lab:**
  - A white lab with a blue-lit doorframe, a blue crest above it (≈ #4E73E2) and a blue double-arrow pillar (≈ #0129ED) [Observed: trailer 35.0 s / screen_00, 2013].
  - The 2012 overhead shows red-lit trim on one half and blue on the other [Observed: Factory.png].
  - The wiki says the rooms mirror "with the exception of the team colors and each team base" [Fan-wiki].
- **Shortest Parsec:**
  - One base arm is lit red and the other blue, with dashed running lights [Observed: trailer 25.0 s; Shortest_Parsec.jpg]. The overhead puts red markers on the left arm and blue on the right [Observed].
  - Inside, a red-lit door (≈ #FF4D4F) faces a purple-blue-lit door (≈ #9761FD) [Observed: trailer 26.25 s / screen_04].
- **Abusement Park:**
  - "[RED]" is spray-stencilled between big red stars with paint drips on the red base wall [Observed: trailer 18.0 s].
  - On the blue side, "RED" is painted in blue, pocked with bullet holes, beside a big blue ring and a blue bear-head silhouette [Observed: wiki File:Screenshot_(509).png, Mar 2014]. The uploader's caption reads "Fun Fact: It says Red on the Blue Team's side on Abusement Park" [Fan-wiki].
  - The wiki also lists "BBR FOREVER" graffiti next to the blue spawn [Fan-wiki]. The same screenshot shows partial blue lettering "BBR…" below [Observed].
- **Gold Digger:**
  - "mining carts filled with gold and team-coloured jewels to indicate which spawn point the player is in" [Fan-wiki].
  - A blue faceted gem glows by a timber tunnel mouth [Observed: screen_03].
  - Red faceted crystals lie near the pits [Observed: trailer 53.0 s]. That they mark the red side is [Inference].
- **Aztec Attack:**
  - In the 2013 overhead, one temple has red-glowing panels (≈ #BC351C) and the other teal, pink and blue gem inlays [Observed: trailer 43.5 s].
  - The gem temple also has cyan orb lights at its door [Observed: IMG_0525.PNG, 2012].
  - That the red temple is the red base is [Inference]. "Each team's base is on the inside of each temple" [Fan-wiki].
- **Marecraft:**
  - The octagonal ring entrances have a red rim at one end and a blue rim at the other [Observed: Marecraft_Arena.jpg].
  - A red and a blue square socket sit on the central bridge [Observed].
- **Desert Airmine:** the 2012 overhead shows red spawn markers on the upper-right islands and blue markers around the helipad "H" [Observed: Desertmine.png]. The wiki: the blue spawn is "most recognizable by the big helicopter landing pad" [Fan-wiki].
- **Haunted Castle:**
  - Red pennants with a bear-head emblem hang over a portcullis, with orange wall torches [Observed: IMG_0178.PNG, 2012]. A blue-team player sees red pennants too [Observed: Plant_The_Bomb_Mode_Bomb_Explosion.jpeg].
  - Whether the pennants are team-coloured at all is [Unverified].
  - The map icon shows blue-lit windows on a castle structure [Observed: HauntedCastle_Preview1.png]; their meaning is [Unverified].
  - The base gates open and close with levers [Fan-wiki].
- **Spawn glyphs on the overheads:**
  - Crosshair-in-circle marks in team colour. Marecraft's second set renders purple [Observed: Battlefield.png, Marecraft_Arena.jpg, Haunted_Castle.jpeg, Shortest_Parsec.jpg, Abusement_Park.jpg, Desertmine.png].
  - The overheads carry the "BATTLE BEARS" logo as a watermark and were uploaded to the wiki in 2012–13 by wiki users [Fan-wiki upload data]. Whether they are SkyVu renders is [Unverified].

**Player markers:**
- A small inverted triangle in team colour floats over players:
  - 2013 [Observed: Maxresdefault(100).jpg, red and blue];
  - 2014, with the teammate's name "BUTTERCUP" beneath a red triangle [Observed: Screenshot_(509).png];
  - 2026 [Observed: jkv6FHPghx8 hq2, red and blue; C7uFxvSZ10c hq1; final-playtest fan thumbnails, with player names under blue triangles].
- In the Oct 2026 banner a lone blue triangle floats above the blue keep's roof, with no player visible under it [Observed].
- Exactly what the triangles signal (all visible players? teammates only plus targets?) is [Unverified].

**Characters wear team colour too:**
- The default Soldier (Oliver) headband is blue in a 2012 capture and red in the Tutorial, in a 2014 red-team capture and in kill-feed portraits ringed red or blue [Observed: Oliver-battlefield…png; Tutorial_BBG_.jpg; Screenshot_(509).png; Imawe.jpg].
- An eye-patch Oliver wears a white headband in an Apr 2013 capture [Observed: A_life_upside_down.jpg].
- So the headband follows team colour on the default skin [Inference], not on every skin.

---

## 4. Spawn areas and the spawn shield

**General rules:**
- Each team spawns in its own base or spawn area. In symmetrical maps these sit at opposite ends [Fan-wiki: map pages] [Observed: overheads of No Bear's Land, Marecraft, Haunted Castle, Abusement Park, Shortest Parsec and Desert Airmine].
- FFA: "the player will randomly spawn from either team's spawn point during the match" [Fan-wiki].

**Spawn shield:**
- "Spawn Shield - Newly spawned players have a few seconds of invincibility." (BBR 1.2.1, Jan 27, 2012) [Game text via wiki]
- "When the player respawns, they have the shields for 4.5 seconds (to discourage spawn killing)" [Fan-wiki: Shield].
- The effect is translucent pale-green heater shields circling the bear, one showing a faint cross emblem [Observed: Maxresdefault(100).jpg, Aztec Attack, uploaded May 23, 2013]. The wiki captions it "A player with shields" [Fan-wiki]. Whether this frame shows the respawn shield or the Shield pickup is [Unverified]; the wiki gives both the same "four green shields".

**Spawn layouts:**
- **No Bear's Land:** "two towers which makes for the two teams' base"; "Each team's spawnpoint is located near or behind this wall" [Fan-wiki]. The overhead shows markers scattered along each keep end [Observed].
- **H.I.P. Test Lab:** the base is "split into two connected sections": a Huggable-tube room and "the big spawn room". Each base has four entrances, and "a relatively steep incline" leads up to each base [Fan-wiki].
- **Space Oddity:** "Each base has two levels", with "3 Jump Pads in each base". The bomb tubes are at the spawns [Fan-wiki].
- **Aztec Attack:** the bases are inside the temples [Fan-wiki].
- **Abusement Park:** asymmetric; the routes to the two bases differ [Fan-wiki]. Each team's markers sit on wooden decks in opposite corners (red top-left, blue bottom-right in the overhead) [Observed: Abusement_Park.jpg].
- **Desert Airmine:** "The Red team will spawn on the lowest level of the stage, while the Blue team will spawn in a somewhat middle level" [Fan-wiki].
- **Haunted Castle:** a lever in a tower near each team's spawn [Fan-wiki]. The overhead shows about ten red markers in the top-right lobe and about ten blue in the bottom-left lobe, mostly in clusters of four [Observed: Haunted_Castle.jpeg].
- **Marecraft:** a battlement or sniper tower at each base and an intestine-textured room below with a jump pad up [Fan-wiki]; a 5×2 marker grid at each end [Observed].
- **Sky View:** "some spawn points directly face the edge of the map" [Fan-wiki].
- **Skate or Die:** "The two team's spawn points are very large on this map, extending almost the width of the map" [Fan-wiki].
- **Gold Digger:** spawns marked by carts with team jewels [Fan-wiki]; timber tunnel mouths [Observed].
- **Toxic Terror:** "the only map where there is a possibility of a player spawning directly onto a power-up" (the Health Packs) [Fan-wiki].
- **Bug note:** "Arbiter will no longer spawn with Bearscream Sandwich on Gold Digger" (2.6.1, Jan 4, 2014) [Fan-wiki: Versions].

---

## 5. Layout grammar

- **Symmetry is the default:**
  - H.I.P. Test Lab is "symmetrical" [Fan-wiki].
  - Space Oddity is "symmetrical in every way, even with pick-ups" [Fan-wiki].
  - No Bear's Land and Haunted Castle are "symmetrical" [Fan-wiki].
  - The overheads show [Observed]:
    - 180° rotation: No Bear's Land, Marecraft;
    - diagonal point symmetry, with team lobes at opposite corners: Haunted Castle;
    - a left/right mirror: Shortest Parsec, H.I.P. Test Lab.
- **The exceptions:**
  - Desert Airmine is "the very first asymmetrical stage" [Fan-wiki]. The same page also calls it "the second asymmetrical stage" [Fan-wiki, self-contradicting].
  - "The stage is asymmetrical, like Desert Airmine" (Abusement Park) [Fan-wiki].
  - Gold Digger's trivia calls it "the only map where a team has a direct advantage", with an Imperial Basket Grande only on red's side. Its own pickup list puts the Grande and Shield "outside both teams' spawn" [Fan-wiki, self-contradicting].
- **The centre lure:** "Bearscream Sandwiches are mostly found somewhere near the center of the map, possibly to induce a rush by all players towards the Sandwich" [Fan-wiki]. Exceptions are in §6.
- **Verticality:**
  - Most maps have several levels joined by jump pads, ramps, towers and tunnels [Fan-wiki; Observed].
  - Steam Yard Blues has "a total of three levels"; Haunted Castle has "4 levels" [Fan-wiki].
  - Each map "has its own unique geographical features, structures and obstacles" [Fan-wiki: BBG Maps].

---

## 6. Pickups

| Pickup | Effect and respawn | Look | Typical spot |
|---|---|---|---|
| Bearscream Sandwich | "doubles the damage" for 20 s, respawns every 90 s (Sandwich page) vs "Triples" (Pick-Ups page) [Fan-wiki, contradictory] | A bear-head ice-cream sandwich: brown cookie face (≈ #944424), angry red eyes, wide screaming mouth with yellow teeth, white cream edge with dark flecks [Observed: Bearscream_Sandwich.jpg, a render on a green-grid background]. When eaten, a crackling magenta ring circles the bear (≈ #FB6CFB) [Observed: A_life_upside_down.jpg; Scary_Light.png]. In 2013 Aztec footage it stands upright on a small teal disc near the lava [Observed: Maxresdefault(100).jpg crop] | Usually central: "There is always at least one… in every map" [Fan-wiki]. Exceptions: Abusement Park, "inside the small shed near the Blue Team's spawn points"; Sky View, "on the Blue team's side" of the central tarp; Desert Airmine, a hidden island; Shortest Parsec, "Guarded by a laser". Haunted Castle "is the first to have two" and Skate or Die has two (Shortest Parsec is also called a two-Sandwich map) [Fan-wiki, partly contradictory] |
| Imperial Basket Grande | Heals 50% of max health, can overheal to 200%; 60 s respawn [Fan-wiki] | Menu art: a red plastic mesh basket (≈ #C33523) lined with white paper and heaped with golden fried chunks (≈ #D1A35E) [Observed: Imperial-basket-grande.png]. The in-world model is [Unverified] | Beside bases, on crates and ledges [Fan-wiki tables] |
| Health Pack | Up to 35 health, no overheal; 45 s [Fan-wiki] | A small white-grey case with an orange cross on its side and a grey inset front panel [Observed: HealthPack.png, a 67×55 crop] | Near spawns and on towers or Pelican'ts [Fan-wiki table] |
| Shield | Immune to damage for 10 s, but "they can still die by falling off a stage" [Fan-wiki] | The effect: four green shields circling the bear [Fan-wiki; Observed]. In-world model [Unverified]. A green shield-with-plus icon in a cyan glow floats over the No Bear's Land keep roof in the Oct 2026 banner [Observed]. The wiki puts No Bear's Land's Shields "on the top of each base tower" [Fan-wiki], so reading the icon as the Shield pickup is [Inference, fairly strong] | Mid-routes and tower tops, often paired with a Health Pack [Fan-wiki] |
| Joules | Before 2.1: a map pickup worth 150. Since 2.1 ("Kill confirm Joule drops", Jul 15, 2013): three drop where a player dies, 25 each, gone after 10 s [Fan-wiki; 2.1 line Game text via wiki]. The Team Battle page says "3 +50 Joule coins" [Fan-wiki, contradictory] | A blue lightning bolt on a dark hexagon-like badge [Observed: Joule.png]. In 2026, three floating blue lightning bolts hover over a deck [Observed: C7uFxvSZ10c hq2, official]. Blue bolt tokens also appear in a final-playtest thumbnail [Observed: HKbwq7PolNc maxres3, fan]. The HUD uses the bolt ("ASSIST +11", 2013; "+200" and "+25", 2026) [Observed] | Wherever someone dies |

**How pickups sit in the world:**
- In 2013 Gold Digger footage, a small floating food item hovers over a rock ledge beside a yellow glow arc [Observed: trailer 52.5–53.0 s]. Enlarged, it has a white rim, a golden-yellow top and a pink layer beneath, and reads more like an egg-and-ham stack than the basket art [Observed: crops/gd53_pick.png]. Its identity is [Unverified]. The wiki's Gold Digger Grande "On a raised area near the shield pickup" makes the Grande the likeliest match [Inference].
- In the Oct 2026 No Bear's Land banner, an angry brown bear face (the Sandwich design) floats above a concrete post near the middle of the view [Observed]. Its identity as the Sandwich is [Inference]. Beside it sits a red-and-yellow capsule with a round bear-face badge, which I could not identify [Unverified].
- On the overheads, pickups are small white squares at the wiki's listed spots, for example on Marecraft's towers and cross-walkway [Observed; the match is Inference].
- Spin or bob animation is [Unverified].

**Not pickups (correcting the brief's premise):**
- **Gas** is a purchasable currency, and the "Gas Meter" gates matches; neither is an in-match item [Fan-wiki: Gas, Gas Meter, Pick-Ups].
  - The icon is a red jerry can [Observed: Gas.jpg].
  - In 2026 Gas is still a currency: "REFERRAL REWARDS: 650 SIGNS UPS as of Oct 13 🎉 Almost to 25 Gas Cans for All" (Steam News, Oct 2026) [Canon]. The referral banner shows red jerry cans [Observed].
- **Ammo** has no pickup in any wiki pickup list [Fan-wiki].
  - The HUD shows magazine readouts such as 23/50, 4/30, 1/2, 70/70 and 25/60 [Observed: 2012–14 captures], and 27/70 and 32/120 in 2026 [Observed: fan final-playtest thumbnails].
  - So weapons reload rather than collect ammo [Inference].
- The Overclock "Gold" coin and File:Shield.png are **not BBG**. Shield.png is an Overclock "Gear" menu listing "Self Healing Potion", "Shield", "Overclock", "Team Healing Potion" and "Sandbag Drop" [Observed].
- The No Bear's Land page places the bombs "near the pillar with the Bearzerker pickup". The wiki has no Bearzerker pickup page; Bearzerker is a boss character [Fan-wiki]. So it is probably a slip for the Sandwich [Inference].

---

## 7. Jump pads

**Look:**
- An octagonal dark-metal pad with a yellow-and-black hazard ring (≈ #CED01D) [Observed].
- A glowing icy-cyan star core (≈ #42D2E1) [Observed].
- Faint translucent cyan octagon rings stacked above it [Observed].
- Sources: Jump_Pad.jpg (a studio-style render on a green-grid background); 2013 trailer footage of H.I.P. (35.0 s), Space Oddity (screen_01) and Gold Digger (52.5–53.0 s).
- **The same design appears in a 2026 final-playtest thumbnail** on a red-and-white space deck [Observed: 1MP1rFi4t-Q maxres2, fan upload, build 3.0.7].
- Aztec's pads read as small round teal discs around and on the lava-pool rock [Observed: trailer 43.5 s; Maxresdefault(100).jpg]. That they are jump pads is [Inference]; the wiki puts "two jump pads at the largest floating platform" [Fan-wiki].

**Rules (all [Fan-wiki: BBG Maps]):**
- "Launch pads appear in most stages in BBG, apart from Skate or Die, Sky View and Toxic Terror".
- "The Aztec Attack map has 12 jump pads, containing the most jump pads out of any map".
- Walking over one "will launch players either vertically or at an angle"; players "can maneuver to a certain degree".
- A bug stalls players mid-flight on Aztec Attack and Shortest Parsec [Fan-wiki: map trivia].
- The overheads show cyan circle glyphs where pads sit [Observed; Inference].

---

## 8. Plant the Bomb hardware

**Era:**
- Added in BBR 1.3, May 3, 2012 [Game text via wiki].
- "The original duration of PtB was 8 minutes, before being changed to 6 minutes, and finally to 5 minutes" [Fan-wiki]. A 2014 results screen reads "MATCH TIME 8:00" [Observed: PTB_balance_beam.jpg]; that it shows a PtB match is [Inference from the filename].
- Listed for 2026 [Canon]. Fan chapter titles show "Plant the Bomb" matches in the Aug and Oct 2026 playtests on Sky View, Aztec Attack, Frozen Pundra, Marecraft and Haunted Castle [Unverified: fan titles].

**Set-up:**
- "The stages feature a bomb in each team's color and a bomb tube in each team's color… placed evenly so both teams can have a chance of fairness" [Fan-wiki].
- "red players have to carry their red bomb to the blue team's tube and vice versa" [Fan-wiki].
- "Each bomb starts on a bomb platform in the same color as the bomb itself" [Fan-wiki].
- Map pages also say "bomb stands" (No Bear's Land) and "Bomb Inserters" (Desert Airmine) [Fan-wiki].

**Rules (all [Fan-wiki]):**
- Lifting the bomb starts a 2-minute timer. The opposing team sees no number, only "a circle… around the bomb's icon".
- The player is invincible while picking it up.
- The bomb beeps "and the bomb will pulsate with increasing intensity starting thirty seconds before detonation".
- The carrier "cannot attack nor use special equipment" but can use "Jump Pads and power-ups".
- If the carrier falls off the map or into a suicide pit, the bomb explodes at once.
- The blast deals "huge, but survivable, damage", and "These deaths count as suicides".
- A deposit pays 225 Joules and resets the bomb on its platform.

**Look (2012):**
- A glossy round cartoon bomb in saturated team blue with a stubby grey fuse cap, seated in a square team-blue slab with a round socket, in a No Bear's Land trench [Observed: Blue-bomb.png].
- A blue bomb icon floats above it [Observed].

**Look (spring 2013, Haunted Castle):**
- A blue-team Oliver holds a blue polka-dotted cylinder with a wire fuse ending in a small ball, while a huge explosion fills the courtyard [Observed: Plant_The_Bomb_Mode_Bomb_Explosion.jpeg, uploaded Apr 19, 2013].
- That the cylinder is the carried bomb is [Inference].
- A green 3D down-arrow floats at the top of the view; that it is an objective marker is [Unverified].

**Mode art:**
- 2012 card: a red-headbanded bear holds a glossy red checker-highlighted bomb aloft [Observed: PlantTheBomb.png, BBR_PTB.png].
- 2013–14 cards: the same bear runs with a red bomb toward a large glossy blue ribbed tube with a domed end, on a space-station deck [Observed: Plant_the_Bomb.jpg, Jun 2013; Plant_the_Bomb-300x2251.png and PTB_icon.jpg, 2014]. That the blue tube is a bomb tube is [Inference].

**Timer:** in a 2014 No Bear's Land capture captioned "Taunting while holding a bomb" [Fan-wiki], a red "1:54:68" countdown box sits at the top right [Observed: Imawe.jpg]. That it is the bomb timer is [Inference].

**Blast:** a huge pale grey, faceted, low-poly cloud, with "SUICIDE" lines in the kill feed [Observed: Plant_the_bombbbbbb_b.jpeg, Aztec Attack, May 2013; same cloud style in Plant_The_Bomb_Mode_Bomb_Explosion.jpeg].

**On the overheads:**
- Marecraft's bridge holds a red and a blue square slab, each with a round dark socket, matching the 2012 bomb stand [Observed: crops/mc_sockets.png; the match is Inference].
- Abusement Park's central booth holds a small blue and a small red square stand with round dark centres [Observed: crops/ap_booth.png]. This fits the wiki's "bombs, both red and blue in front of the House of Mirrors" [Fan-wiki; Inference].

**Placement per map (all [Fan-wiki]):**
- No Bear's Land: bombs in the central trenches, tubes on top of the keeps.
- H.I.P. Test Lab: both bombs under the main bridge, tubes behind the Huggable containers.
- Space Oddity: both bombs on the central platform, tubes at the spawns.
- Sky View: each bomb on the enemy's side of the "large, light blue tarp".
- Toxic Terror: bombs inside each team's own spawn, tubes by the tree.
- Desert Airmine: red bomb under the windmill, blue on the third level; "The Bomb Inserters are located at each enemy team spawn point".
- Shortest Parsec: both bombs "on the bottommost platform right next to each other".

**Unknown:** the in-game tube model and any 2026 Plant the Bomb visuals [Unverified].

---

## 9. Kill zones, hazards and interactive elements

**Scoring:**
- Environmental deaths count as suicides [Fan-wiki]. The kill feed shows "SUICIDE" [Observed: 2013].
- 2.14 "Fixed Suicide giving players -1 kills" (Nov 29, 2014) and 2.19 "Suicides are penalized in team battle" (Apr 26, 2015) [Game text via wiki].

**Kill zones by map:**
- **Fall-outs:**
  - Sky View: "If you fall into the city, you will suicide" [Fan-wiki]. The trailer shows red steel-girder decks with dark grating and wooden planks, ringed by skyscraper walls, with open gaps between decks [Observed: 48.5 s].
  - Shortest Parsec: "The map has almost no walls" [Fan-wiki]; unrailed decks over open space [Observed: 50.75 s].
  - Desert Airmine: falling off the floating islands [Fan-wiki].
  - Gold Digger: "If you fall off the bridge, and into a black pit, you will suicide" [Fan-wiki]. The trailer shows two pure-black pits (#000000) split by a narrow stone path [Observed: 52.5–53.0 s].
- **Lava (Aztec Attack):** "If a player falls into the lava, it will be counted as a suicide" [Fan-wiki]. Bright orange-yellow (≈ #FFAA11) [Observed].
- **Marecraft canal:** "Any player who falls into the canal will die" [Fan-wiki]. Green "digestive" canals (≈ #3B7A20) beside the bridge [Observed: overhead].
- **H.I.P. Test Lab:** the loading bay "will cause the player to suicide if they attempt to stand on its floor" [Fan-wiki].
- **Shortest Parsec laser:**
  - "The orange laser near the team spawn. It kills any player who stays under its ray, resulting in suicide." [Fan-wiki caption]
  - It is an orange-yellow cone (core ≈ #FFDA70, edges deeper orange) pouring from a blue hex-patterned emitter onto a red-orange floor disc, with ember sparks [Observed: Scary_Light.png].
  - "You actually can run through the laser if you use caffeine boost or shield." [Fan-wiki]
- **Desert Airmine machines:** hitting the oil drill mid-air "will count as a suicide"; "Hitting the windmill itself will kill any player" [Fan-wiki].

**Interactive maps (all [Fan-wiki]):**
- Haunted Castle was first: levers, hit with melee, open and close gates.
- Shortest Parsec was second: a switch moves the central dome floor.
- Frozen Pundra was third: icicles drop when shot.
- Steam Yard Blues "has no interactive features".

**Protection:** the Shield does not save you from falling [Fan-wiki].

---

## 10. Skies and skyboxes

| Map | Sky | Source |
|---|---|---|
| Gold Digger | Deep navy night (≈ #001A2D), stars, a big pale full moon (≈ #B3CCDD) over the rock rim | [Observed: trailer 4.0 s, 2013] |
| Sky View | Dusk: deep blue at the top grading to a pink-orange glow, with distant skyscraper silhouettes [Observed: Sky_View_1.jpg, 2013]. A navy night in a 2026 clip [Observed: jkv6FHPghx8 hq2; identification as Sky View is Inference]. "This map uses the same skybox as Gold Digger" [Fan-wiki]; the 2013 dusk frame does not look like Gold Digger's moonlit night [Observed], so the claim is doubtful | as cited |
| Aztec Attack | Magenta-to-crimson haze (≈ #7B063B) over dark ridges, stars at the top, lava below | [Observed: IMG_0525.PNG 2012; Maxresdefault(100).jpg 2013; trailer 12–16 s] |
| Shortest Parsec | Open space: near-black indigo, dense white stars, a violet band | [Observed: trailer 24–25.5 s, 49.5–51.5 s] |
| No Bear's Land | Clear daytime blue (≈ #4277D7, 2012). Same clear blue in 2026, with pale haze near the horizon [Observed: final-playtest banner; C7uFxvSZ10c maxres]. Infobox "Day, Sunlight" [Fan-wiki] | as cited |
| Haunted Castle | Black starry night, lit by orange torches; a purple glow at the horizon | [Observed: IMG_0178.PNG] |
| Abusement Park | Dark plum dusk with clouds [Observed: trailer 18.0 s; Screenshot_(509).png]; "Fixed Abusement Park Skybox" (1.3.4) [Game text via wiki] | as cited |
| Steam Yard Blues | Pale yellow evening sky over purple-grey hills (2014) [Observed: Steamyard.png; RnCV0V5gWCI hq1]. A pink-purple dusk in a 2026 fan thumbnail [Observed: HKbwq7PolNc maxres2] | as cited |
| Desert Airmine (2026) | Light blue sky with soft clouds over red-orange mesas | [Observed: HKbwq7PolNc maxres1, fan upload, build 3.0.7] |
| Sky Pirates (2026) | Bright day, pale blue sky, sea horizon, autumn-orange trees, pirate ships with black flags | [Observed: r91WkR10W2A hq2, hq3; CwxpBZg6Fi4 hq2] |
| Tutorial | Black void with green "digital rain" and green wireframe geometry (green ≈ #20B010–#31E419) | [Observed: Tutorial_BBG_.jpg, Photo_(2).png] |
| Interiors: H.I.P. Test Lab, Space Oddity, Marecraft, Toxic Terror, Frozen Pundra | The H.I.P. loading bays show "the backdrop of a large ship in space" [Fan-wiki]. Space Oddity: an orange-glass hull with teal lights [Observed: screen_01]. Marecraft: enclosed orange-red flesh [Observed: trailer 40.0 s]. Toxic Terror: a dark sewer with green ooze glow [Observed: HquG87_5Xa0 hq1–2; map icon]. Frozen Pundra: an icy white-blue cave [Observed: map icon] | as cited |

Also: if a player glitches out of Gold Digger, "the background is the same as Sky View, with all of its buildings" [Fan-wiki].

---

## 11. Scale: doors, crates and cover against the bears

All of these are approximate, from single frames; perspective adds error.
- **H.I.P. doorway (35.0 s):** the opening is about 215 px tall and about 200 px wide. A Huggable standing in the doorway is about 145 px tall. So doors are at least about 1.4–1.5× a bear's height and about two bears wide [Observed, approximate].
- **Shortest Parsec interior (26.25 s):** the purple-lit door frame is roughly 400 px tall. The bear I could compare is airborne mid-corridor, so its depth is unknown. **No reliable ratio** [Observed; the draft's 1.9× is withdrawn].
- **Abusement Park (18.0 s):** the bear in the foreground is **Wil** (his "CHUB SCOUT" card follows at 22.5 s), not Tillman. Against the bear at mid-distance (about 200 px tall), the nearby yellow U-rails are about 65 px, roughly a third of a bear: knee-to-thigh height [Observed, approximate].
- **Sky View (48.5 s):** the teal tarp screens on posts stand roughly as tall as, or taller than, a bear: full-body cover [Observed, approximate].
- **Gold Digger (53.0 s):** a mine cart is roughly as long as a bear is tall [Observed, approximate].
- **Rule of thumb for shorts:** doors about 1.5–2× a bear's height; rails and sandbags at knee-to-waist height; tarps and crate stacks as full cover [Inference].

---

## 12. General art direction, materials and lighting

**Official:**
- "All assets in this game are created by human artists." [Canon]
- "Lighting improvements" (final 2026 playtest) [Canon]. The banner says "LIGHTING, EFFECT & TEXTURE IMPROVEMENTS" [Observed].
- "New Map Lighting" (BBG 3.0, 2021) [Game text via wiki]. "Upgraded Map Lighting… Skyworld" (Overclock 3.0, 2020) [Game text via wiki].
- BBG 2.0 offered "HD Graphics (Only available on higher end devices. App automatically detects what graphic mode to show)" [Canon: May 30, 2013 trailer description].

**Common traits I observed (2012–14 captures, 2013 trailer footage, 2026 thumbnails):**
- Chunky, low-poly, hard-edged geometry with hand-painted textures: stone blocks, wood grain, panel lines, cracks, paint drips [Observed].
- Each map is built around one dominant hue plus a contrasting accent [Observed: trailer, overheads, the 14 map icons, preview thumbnails]:
  - Aztec Attack: orange lava and magenta sky;
  - H.I.P. Test Lab: white with magenta and blue;
  - Shortest Parsec: red and white against indigo space;
  - Gold Digger: brown-black rock with gold and gem glows;
  - Marecraft: saturated flesh red (≈ #F04B30) with cream tubes and green canals;
  - No Bear's Land: grass green and olive concrete;
  - Toxic Terror: dark sewer with green ooze glow;
  - Frozen Pundra: icy white-blue;
  - Desert Airmine: sandy-orange mesas;
  - Space Oddity: amber glass with teal light;
  - Steam Yard Blues: brass-gold structures, purple panels, a pale yellow sky;
  - Sky Pirates: white-walled red-roofed buildings, autumn-orange trees, blue sea.
- Strong coloured light sources do the mood work: lava underglow, neon strips, torches, the moon, gem glows, the laser [Observed].
- **Ink outline:**
  - Environments carry no ink outline in any era I saw [Observed].
  - Characters have a thick black outline in the May 2013 trailer footage and in every 2026 in-game capture with HUD that I saw [Observed: C7uFxvSZ10c maxres, build 3.0.0; HKbwq7PolNc maxres1, build 3.0.7; the Steam store loop's flying Huggable].
  - The outline is absent from the 2012–14 phone captures on the wiki [Observed: Oliver-battlefield…png, A_life_upside_down.jpg, Maxresdefault(100).jpg, Imawe.jpg, Screenshot_(509).png].
  - That the outline belonged to the 2013 "HD Graphics" mode is [Inference]. Whether 2026 lets players turn it off is [Unverified].
- Gag set dressing is everywhere [Observed; Fan-wiki]:
  - posters (Abusement Park); graffiti (Skate or Die, including "ABBi"; Abusement Park's blue "RED");
  - H.I.P. emblems on Shortest Parsec floors ("a few logos in the map reading 'H.I.P.'" [Fan-wiki]);
  - black crates with pink Huggable faces (H.I.P. Test Lab and Space Oddity) [Observed: screen_00, screen_01]; the "PMOC 20-11" stencil;
  - carvings and tombstones listed by the wiki (Haunted Castle, Toxic Terror).
- The 14 map-select icons (2013–14) are in-game renders under chunky orange-yellow lettering with a black outline [Observed: icons/*.png].

**Approximate swatches I sampled:**

| Item | Hex | Source |
|---|---|---|
| Lava | ≈ #FFAA11 | trailer 43.5 s |
| Parsec laser | ≈ #FFDA70 core, deeper orange edges | Scary_Light.png |
| Abusement Park planks | ≈ #F38F6E | trailer 18.0 s |
| Abusement Park yellow rails | ≈ #E49109 | trailer 18.0 s |
| H.I.P. walls | ≈ #C7BDB9 | trailer 35.0 s |
| Gold Digger rock | ≈ #140A0B–#2D2324 | trailer 4.0 s, 53.0 s |
| Sky View tarp | dark-to-light teal waves (≈ #075964 to #2D978E) | trailer 48.5 s |
| Tutorial green | ≈ #20B010–#31E419 | Tutorial_BBG_.jpg |
| No Bear's Land red band | ≈ #D71D18 | Oliver-battlefield…png |

All of these are [Observed; median of sampled pixels].

---

## 13. Map music (OST)

**Soundtrack track list** (Steam 5321720, "Nov 4, 2026") [Canon]:
1. Abusement Park 0:54
2. No Bears Land 0:44
3. Sky View 1:03
4. Gold Digger 0:38
5. Huggable Factory 0:54
6. Space Oddity 0:54
7. Skate Or Die 1:29
8. Marecraft 0:57
9. Shortest Parsec 1:13
10. Frozen Pundra 0:54
11. Haunted Castle 1:01
12. Desert Airmine 1:13
13. Aztec Attack 1:20
14. Toxic Terror 1:18
15. Steamyard Blues 0:51
16. Castle Royale 1:56
17. Main Menu (BBG) 1:49
18. Tutorial 0:32
19. After Match 1:04
20. Main Menu (BBR) 1:09
21. Huggable Factory (Full Version) 2:52
22. Abusement Park (Full Version) 3:05
23. I'm a Battle Bear (feat. Vivyd, Brian Bell & Leck One.) 2:44
24. The Right to Bear Arms (feat. Vivyd, Brian Bell & Leck One.) 1:31

**Notes on the list:**
- Every classic arena map has its own track [Canon]. "Each stage consists of its own map layout as well as soundtrack" [Fan-wiki].
- "Huggable Factory" is H.I.P. Test Lab under its BBR name [Fan-wiki rename; Inference].
- "Castle Royale" matches no documented BBG map. It may belong to the 2018 Battle Royale mode (2.50) [Inference; Unverified].
- There is no Sky World/Sky Pirates track, so its music is [Unverified]. The Overclock map would have had its own music [Unverified].
- The map cues run 0:38–1:29, which suggests loops [Inference].

**Credits:**
- Map and menu music is credited jointly to Rob Ruiz, AnDrue Humphreys and Benjamin Vavak, with no per-track credit [Canon].
- "Battle Bears Royale: Huggable Factory Music (FULL VERSION)" was uploaded on the "R Con" channel on Mar 6, 2012 [Observed: oEmbed; the wiki's stored YouTube metadata]. Its description reads "Produced by: Rob "DJ (R)Con" Ruiz and Drue Humphrey for SkyVu Entertainment" [Fan-wiki: stored copy].
- Its duration (172 s = 2:52) equals OST track 21, "Huggable Factory (Full Version) 2:52" [Observed; Inference: same piece].

**Recognition and 2026 features:**
- 2013 Best App Ever awards (Android), "Best Soundtrack": Winner [Fan-wiki, citing bestappever.com].
- 2026 adds a menu "Jukebox" [Canon; banner Observed]. A fan final-playtest upload has a chapter "Early Jukebox Showcase" [Unverified: fan title].
- SkyVu jokes that Steamyard Blues is played "most likely just for the soundtrack" [Canon]. That implies a weak map with loved music [Inference].
- Sound-effect conventions per map are undocumented [Unverified].

---

## 14. Seasonal reskins and removed modes that changed the scenery

- **No Bear's Land reskins:**
  - Christmas/winter (2.26): "a Christmas Tree in the center of the stage, white colored ground, along with snowmen" [Fan-wiki].
  - Summer (2.27): "a sandy ground texture instead of grass, animated water running along the trenches, orange shade umbrellas on the two towers and crashed planes as well as palm trees" [Fan-wiki].
  - Winter returns (2.28: "Winter Map is back") and spring (2.51: "Spring Theme for No Bear's Land Map.") [Game text via wiki].
- **Haunted Castle** returned for Halloween in 2.4 [Fan-wiki; Game text via wiki on Versions].
- **King of the Windmill** "was added in version 2.8 and removed in version 2.29" ("King Of The Windmill is retired", Jan 26, 2018) [Fan-wiki; Game text via wiki].
  - A windmill lands at a random spot "surrounded by a green circle" [Fan-wiki].
  - "chicken leg icons will fly out of the ground and into the air" before it lands [Fan-wiki].
  - The landing can damage heavily "or even kill" [Fan-wiki].
  - Mode art: bears on a green hill under a blue sky with clouds, and a purple-and-white pinwheel windmill blasting off overhead [Observed: BBG_windmill_game_mode-300x225.png].
- **Battle Royale** arrived in 2.50 (Apr 5, 2018); "Bridge to Terabearthia" was added to it in 2.53 (Apr 28, 2018) [Game text via wiki].
- Neither King of the Windmill nor Battle Royale is in SkyVu's 2026 mode list [Canon]. Fan chapter titles show a "Kill Confirmed" mode in the Aug and Oct 2026 playtests [Unverified: fan titles]. A final-playtest fan thumbnail shows the prompt "YOU'RE ON TEAM BLUE / COLLECT ENEMY TAGS TO SCORE POINTS" [Observed: 1MP1rFi4t-Q maxres1].

---

## 15. Images viewed (all opened with Read)

Local paths are under `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/shared_conventions_verify/` unless a full path is given.

**Steam (official):**
- `news/b7c8f8f133ad960899cce9f3d232b42847891d08.png` (final-playtest banner) and crops `crops/pt5_center.png`, `pt5_keep.png`, `pt5_right.png`, `pt5_green.png`, `pt5_bottom.png`.
- `news/60061117627037f3508ed7eb899ff08e7f7720a9.png` (referral banner), `news/3b7f9b97cdb4f799bbc696475d327f4d7c7a9523.png` (first playtest), `news/282237bbf3e28853d621b030f8c6fcc574430b3d.png` (store launch).
- `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/steam_screens/screen_00.jpg`–`screen_04.jpg`. They are byte-identical to fresh downloads in `steamss/`. Crops: `crops/s0_bears.png`, `crops/s1_flames.png`, `crops/s4_robot.png`.
- Trailer contact sheets `sheets/tr1.png`, `tr2.png`, `tr3.png`, covering all of `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/trailer/t_0001.jpg`–`t_0108.jpg`.
- Full-resolution frames: `tfull/f_4.0.jpg`, `f_18.0.jpg`, `f_25.0.jpg`, `f_26.25.jpg`, `f_35.0.jpg`, `f_40.0.jpg`, `f_43.5.jpg`, `f_46.0.jpg`, `f_48.5.jpg`, `f_50.75.jpg`, `f_53.0.jpg`; `crops/gd525.png` (52.5 s), `crops/gd53_pick.png`.
- Store loop video frames `sheets/extra.png`, from `extras/f7ecb9b2e78f0fd754cc7cf8220ad9b0.mp4`.

**Wiki files (via MediaWiki file URLs):**
- `img/`: `Bearscream_Sandwich.jpg`, `Imperial-basket-grande.png`, `A_life_upside_down.jpg`, `Maxresdefault(100).jpg` (+ `crops/mx100_shield.png`, `mx100_center.png`), `Blue-bomb.png`, `Plant_the_bombbbbbb_b.jpeg`, `Imawe.jpg`, `Jump_Pad.jpg`, `Oliver-battlefield-airpad-red-base-front.png`, `IMG_0178.PNG`, `IMG_0525.PNG`, `Battlefield.png`, `Marecraft_Arena.jpg` (+ `crops/mc_sockets.png`), `Haunted_Castle.jpeg`, `Shortest_Parsec.jpg`, `Abusement_Park.jpg` (+ `crops/ap_booth.png`), `Steamyard.png`, `Screenshot_509_rgb.png` (from File:Screenshot_(509).png).
- `sheets/small.png` (HealthPack.png, Joule.png, Gas.jpg, Gas.png); `sheets/ptb_art.png` (Plant_the_Bomb-300x2251.png, BBR_PTB.png, BBG_windmill_game_mode-300x225.png); `sheets/tut.png` (Tutorial_BBG_.jpg, Photo_(2).png, Tutorial_2.jpg); `sheets/mq6.png` (Mqdefault_(6).jpg); `sheets/modes.png` (FFA.jpg, Team_Battle_Icon.jpg); `sheets/misc1.png` (Sky_View_1.jpg, Scary_Light.png, O+A.jpg); `sheets/misc2.png` (Shield.png, Steamyard.png); `sheets/ovh2.png` (Factory.png, Spaceship.png, Desertmine.png).
- `sheets/icons.png`: the 14 map icons in `icons/` (H.I.P._Test_Lab.png through Pundra_map.png).
- `img2/PTB_balance_beam.jpg`, `img2/Plant_The_Bomb_Mode_Bomb_Explosion.jpeg`, `sheets/ptb2.png` (PTB_icon.jpg, PlantTheBomb.png, Plant_the_Bomb.jpg).

**YouTube thumbnails (https://i.ytimg.com/vi/<id>/…):**
- `yt/th_C7uFxvSZ10c_maxresdefault.jpg`, `sheets/c7.png` (hq1–hq3), `crops/c7hq1.png`, `crops/c7hq2.png`.
- `yt/th_jkv6FHPghx8_maxresdefault.jpg`, `sheets/jk.png` (hq1–hq3), `crops/jk_grid.png`, `crops/jk_hq2.png`.
- `sheets/r91.png` (r91WkR10W2A hq1–hq3).
- `sheets/cw.png` (CwxpBZg6Fi4 hq1–hq3; -lAtv-j9Sms hq1–hq2, which are menu screens only).
- `sheets/old.png` (HquG87_5Xa0 hq1–hq2; RnCV0V5gWCI hq1–hq2; SSwlTVbW8Wg hq1).
- `sheets/final_pt.png` (HKbwq7PolNc maxres1–3 and maxresdefault, InstableGR, fan).
- `sheets/jn_final.png` (1MP1rFi4t-Q maxres1–3, JustNubz, fan).
- Pixel matches (computed, not opened as images): `yt/th_rfAyqVJrli4_hq1/hq2/hq3/maxresdefault/hqdefault.jpg` against `tr10/f_*.jpg` (the trailer at 10 fps).

---

## 16. Prompt pack (shared building blocks)

**Modules to append to any map prompt** (environment only, no characters, no readable text or logos):
- **A. Team accent:** team colour only as accents. Options [Observed patterns]:
  - a pair of saturated red (≈ #D71D18) or royal-blue (≈ #0129ED) bands along parapets;
  - a coloured light strip around a base doorway;
  - a glowing team gem beside the spawn exit;
  - a team-coloured running light along one arm of a structure.

  Keep the map's own base materials [Inference].
- **B. Jump pad:** an octagonal dark-steel floor pad with a yellow-and-black hazard ring and a glowing icy-cyan star core; faint stacked cyan octagon rings shimmer above it [Observed, 2013 and 2026].
- **C. Centre pickup:** a bear-head-shaped ice-cream sandwich, standing upright and hovering at chest height above a small post; brown cookie face, angry red eyes, open mouth with yellow teeth, white cream edge with dark flecks [Observed design and 2026 banner placement]. A soft warm glow under it is [BBG News invention].
- **D. Bomb stand (Plant the Bomb):** a glossy round cartoon bomb in team colour with a stubby grey fuse cap, seated in a square team-coloured slab with a round socket [Observed, 2012].
- **E. Health props:** a small white-grey case with an orange cross on its side; a red mesh basket of golden fried chunks [Observed designs; the basket is menu art]. Their in-world pedestals are [BBG News invention].
- **F. Joule drop:** three floating blue lightning-bolt tokens hovering where a bear fell [Observed, 2026].

**Example 9:16 establishing shot (No Bear's Land centre, the best-documented case):**
> Vertical 9:16 high three-quarter view across a mirrored grassy battlefield under a clear mid-blue daytime sky with pale haze near the horizon. Zig-zag dirt trenches with orange soil walls and plank floors cut through bright green grass dotted with white daisies. Sandbag walls and dark cross-shaped tank-trap hedgehogs line the trench lips. In the centre a small concrete pillar rises from the trenches, flanked by two octagonal jump pads with yellow-and-black hazard rings and glowing cyan star cores, and an angry bear-faced ice-cream sandwich hovers above the pillar. In the far distance an olive-drab concrete keep with two bright blue bands along its parapet; a small green shield emblem glows on its roof. A crashed dark-olive dropship with red markings lies on a hill at one flank. Clean hard-edged low-poly shapes, hand-painted textures, bright saturated daylight.

- The elements are [Observed: 2012 capture, Oct 2026 banner, Battlefield.png overhead]. The centre pillar is [Fan-wiki]. Jump pads at the pillar are [Fan-wiki: "use the Jump Pads to jump up the pillar"; Observed overhead glyphs].
- The camera placement, and putting the pillar, pads and keep in one frame, are [BBG News invention].

**Three staging spots that work on every map:**
1. **The spawn exit.** A bear pops out of the team doorway inside four orbiting pale-green shields: the 4.5 s respawn shield [Fan-wiki; Observed effect]. Team-coloured light from the door strip falls on it [Observed on H.I.P. and Shortest Parsec]; using it as a key light is [BBG News invention].
2. **The centre rush.** Both teams sprint for the Sandwich, which the wiki says is placed "to induce a rush" [Fan-wiki]. The winner crackles with a magenta electric ring [Observed]. The specific gag is [BBG News invention]. On Abusement Park, Sky View and Shortest Parsec, move the Sandwich off-centre as the wiki lists [Fan-wiki].
3. **The bomb run.** A carrier who "cannot attack nor use special equipment" carries a beeping, pulsing bomb toward the enemy tube, ideally via a jump pad [Fan-wiki]. The pay-off is the giant pale faceted blast, logged as "SUICIDE" [Observed]. Timing and jokes are [BBG News invention].

---

## 17. Confidence

**Overall: partial.**

| Area | Confidence |
|---|---|
| Team colours | observed (2012–14 frames plus several 2026 images) |
| Spawn shield and spawn layouts | documented, partly observed |
| Pickups | Sandwich, Health Pack and Joule designs observed; Joule drops observed in 2026; in-world Grande and Shield models unknown |
| Jump pads | observed (2013 and 2026) |
| Plant the Bomb | partial (stand and blast observed; tube only in mode art; no 2026 visuals) |
| Hazards | documented, partly observed |
| Skies | partial (2013 for most maps; 2026 for No Bear's Land, Sky Pirates, Desert Airmine and Steam Yard Blues via thumbnails) |
| Scale | partial (single frames, approximate) |
| Music | documented (the 2026 track list is Canon) |
| 2026 status | partial (13 maps seen in 2026 playtest chapter titles or thumbnails; H.I.P. Test Lab and Toxic Terror unseen; Wayback-only sources not re-checked) |

---

## Corrections to our notes

1. **research_notes/Battle Bears character lore/franchise_world.md** (line 276, map count).
   - Current: "[FAN-WIKI] The wiki lists 15 BBG maps across the original run, and Haunted Castle and Desert Airmine were removed at 2.0 and Haunted Castle later returned".
   - Correction: both returned. Haunted Castle came back in v2.4 (Oct 24, 2013) and Desert Airmine in v2.7 (Jan 2014) [Fan-wiki]. The 2026 OST has one track for each of the 15 classic maps [Canon], and 15 plus Sky World makes 16 [Inference].
2. **research_notes/BBG maps (unverified drafts)/research_tutorial.md** (line 283).
   - Current: "Steam app 5321720 lists track 18 "Tutorial" (0:32) after the 16 map tracks and "Main Menu (BBG)"".
   - Correction: tracks 1–15 are the 15 classic maps; track 16 is "Castle Royale" (no documented BBG map); track 17 is "Main Menu (BBG)".
3. **research_notes/BBG maps (unverified drafts)/research_desert-airmine.md** (line 38; same error on line 232).
   - Current: "the OST has 16 map-named tracks including Desert Airmine. But it also has "Castle Royale" and no Sky World track". Line 232: "starting with 16 map themes: … Steamyard Blues, Castle Royale".
   - Correction: 15 map-named tracks (Desert Airmine is track 12) plus "Castle Royale" as track 16; no Sky World/Sky Pirates track.
4. **research_notes/BBG weapons (verified)/combat-vfx.md** (line 601), and the same line in **research_notes/BBG weapons (unverified drafts)/visuals_combat-vfx.md** (line 346).
   - Current: "Orange flame jets rise from floor vents [Observed: screen_01.jpg]. Whether they are a hazard or jump pads is [Unverified]."
   - Correction: small flames rise from short orange-yellow rectangular bits lying on the floor beside a jump pad, not from vents [Observed: screen_01 crop]. They fit the Señor Potato Cannon's "piping hot french fries" [Inference]. No fire hazard is documented on Space Oddity [Fan-wiki]. screen_01 is a frame of the May 2013 trailer at about 30.7 s.
5. **research_notes/BBG weapons (verified)/combat-vfx.md** (lines 74 and 113, ink outline).
   - Current: "2026 media add a thick black ink outline to characters [Observed]. Whether the outline is in-game is [Unverified]." and "In the 2026 Steam screenshots, the trailer gameplay and the Steam loop video, characters have a thick black ink outline".
   - Correction:
     - The Steam screenshots and trailer are May 2013 trailer footage (pixel matches), so the outline was already in SkyVu's 2013 footage, not added in 2026.
     - The outline also appears in 2026 in-game captures with HUD (Playtest Highlights maxres, build "3.0.0"; fan final-playtest thumbnails, build "3.0.7"). So it is rendered in-game in 2026.
     - It is absent in 2012–14 phone captures.
     - SkyVu's 2013 trailer description advertises "HD Graphics (Only available on higher end devices…)"; tying the outline to that mode is [Inference].
6. **research_notes/BBG weapons (verified)/combat-vfx.md** (line 762, pickups).
   - Current: "Which pickups survive into 2026 is [Unverified]."
   - Correction: partly answered.
     - Joule drops survive: three floating blue lightning bolts appear in an official 2026 playtest thumbnail [Observed: C7uFxvSZ10c hq2].
     - The Oct 2026 final-playtest banner, on No Bear's Land, shows a floating angry bear face (the Bearscream Sandwich design) and a green shield-with-plus icon on the keep roof, where the wiki puts the Shield [Observed]. Reading them as the Sandwich and the Shield is [Inference].
7. **bbg-news-repo/content/evergreen.json** (lines 142–145): outdated, not wrong.
   - Current: "Four Discord playtests, July to September 2026" (caption: "SkyVu ran four Battle Bears Gold playtests on the Battle Bears Discord between July and September 2026.…").
   - Correction: add that SkyVu then ran a fifth and "final" playtest on Oct 15, 2026 on Windows, iOS and Android (banner "CLOSED TESTING 5"). The Playtest 3 map is "Sky World" in the Steam post and "Sky Pirates" in SkyVu's video titles; SkyVu's Sep 7 video "Sky Pirates in BBG!" says "Enjoy the highlights from our Sky World playtest!".
8. **research_notes/Battle Bears character lore/franchise_world.md** (line 224, Toxic Terror).
   - Current: "It also has a tree carved with "O+A" in a heart".
   - Refinement: the wiki's File:O+A.jpg (528×427) shows a faint heart outline in bark, but the letters are not legible at that size [Observed]. Keep "O+A" as [Fan-wiki].
9. **research_notes/BBG maps (unverified drafts)/research_aztec-attack.md** (line 54).
   - Current: "The 2026 trailer shows the same layout as the 2012 top-down render [Observed], with brighter, more saturated orange ground than the 2012 screenshot [Observed]. That the 3.0 lighting pass explains the change is [Inference]."
   - Correction: the Steam trailer's gameplay is May 2013 footage. Its class cards pixel-match the May 30, 2013 trailer, and it shows only BBG 2.0 maps and classes. So the brighter look predates the 2021 3.0 "New Map Lighting" and cannot be explained by it.
10. **research_notes/BBG maps (unverified drafts)/research_shortest-parsec.md** (line 3).
    - Current: "The official 2026 Steam trailer shows it, and so do two of the five 2026 Steam screenshots."
    - Correction: say "two of the five screenshots on the 2026 Steam page". They are frames of the May 2013 trailer (screen_02 ≈ 50.6 s, screen_04 ≈ 26.4 s) and show the 2013 build, not 2026.
11. **The brief itself (not a file).** "pickups (Gas, health, ammo)" is wrong for BBG. Gas is a currency and gates matches through the Gas Meter; there is no ammo pickup. The real pickups are the Bearscream Sandwich, Shield, Imperial Basket Grande, Health Pack and Joule drops [Fan-wiki; Observed icons].

## Open questions

1. Does every classic map ship on Nov 4, 2026? H.I.P. Test Lab and Toxic Terror have no 2026 sighting; Skate or Die has only a likely one. Is the 16th map Sky World/Sky Pirates or the Tutorial?
2. How do the maps look after "Lighting improvements"? The Steam demo (Oct 19–26, per play.battlebears.com) is the first chance to capture clean 2026 footage. SkyVu asked testers for UI-free capture with the H key.
3. What is OST track 16 "Castle Royale"? Does Sky World/Sky Pirates have its own music?
4. What does the in-game bomb tube look like? Does the mode art's blue ribbed domed tube match it? What does 2026 Plant the Bomb look like?
5. What are the in-world models and idle motion (pedestal, spin, glow) of the Shield, Health Pack and Imperial Basket Grande? Is the floating egg-and-ham-like item on Gold Digger's ledge (trailer 53.0 s) the Grande?
6. What is the red-and-yellow capsule with a bear-face badge next to the Sandwich in the Oct 2026 banner? And the grey smoke puff with a lime glow behind the keep?
7. Are the team-coloured crosshair spawn glyphs on the overheads SkyVu renders? Does each team always spawn at the same end of a map?
8. Exactly what do the floating inverted triangles mark? Name tags appear under some of them (2014, 2026).
9. Wiki contradictions: is the Sandwich 2× or 3× damage? Is a Joule drop worth 25 or 50 in 2026? Which maps have two Sandwiches (Haunted Castle, Skate or Die, Shortest Parsec)? Does Sky View really share Gold Digger's skybox, given the 2013 frames show dusk vs moonlit night?
10. Is "Kill Confirmed" ("COLLECT ENEMY TAGS TO SCORE POINTS" in fan footage) the "experimental new gamemode" of the 2nd playtest? Will it ship beside TDM, FFA and PTB?
11. Are Haunted Castle's red pennants team markers, with blue ones on the other gate, or decoration?
12. The archived SkyVu map blurbs, the 2012 BBR maps page and the 2.4/2.6 release notes need re-checking when web.archive.org is reachable.
13. Is the thick character outline in 2026 always on, or a graphics setting like 2013's "HD Graphics"?