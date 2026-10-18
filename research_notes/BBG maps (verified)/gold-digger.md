# Gold Digger

Gold Digger is a Battle Bears Gold (BBG) map set in a gold mine at night. The main arena is an oval pit open to a starry sky, walled by tiers of stacked rock blocks. Two black shafts sit in the middle, split by a narrow stone-edged path that the wiki calls "a bridge". Timber-framed tunnel mouths and fenced rail openings ring the edge. Small mine carts hold glowing gold, and a red gem and a blue gem mark the two team sides. SkyVu added the map when BBG launched in 2013. It names Gold Digger among the "Iconic Maps" returning on November 4, 2026, and a fan's recording of the October 15, 2026 final playtest shows it running in the 2026 build.

**Verification pass, 2026-10-18.** I re-fetched every cited source, re-downloaded and opened every image, and added new evidence. The changes from the draft:
- **New 2026 footage.** A fan video of the 2026 final playtest has storyboard frames of Gold Digger, and its timestamp list puts the match in Team Battle.
- **Corrected visual claims.** Moonlight does not light the wall crests. The carts hold a flat glowing load, not visible nuggets.
- **Newly identified details.** The fenced rail openings carry team gems, and the map looks mirror-symmetric. The ledge pickup is probably the Imperial Basket Grande.
- **Better era evidence.** The wiki's "2.0" is now better supported as the May 2013 launch, and the wiki dates King of the Windmill's removal.
- **Palette and labels.** The hex values are re-sampled, and a mislabelled absence check is fixed.

**What I could reach:**
- **Fan wiki (MediaWiki API).** The Gold Digger page with all 28 revisions (May 25, 2013 to September 21, 2026), its 4 gallery images in original format, and the map icon. Also the pages for Sky View, BBG Maps, Battle Bears Gold, Battle Bears Gold/Versions, Battle Bears Gold/Versions/2.6 (with its history), Updates, Imperial Basket Grande, Bearscream Sandwich, Health Pack, Shield, Pick-Ups, Joules, Team Battle, Plant the Bomb, Free-For-All and King of the Windmill, plus the 2013 trailer's stored YouTube metadata.
- **Steam.** The store API for app 4408320 and the soundtrack app 5321720, the soundtrack store page, the news API with its 4 images, and the 5 current screenshots (byte-identical to our local copies).
- **Local files.** The Steam trailer (54.0 s, 1920×1080), from which I extracted my own full-resolution frames.
- **YouTube metadata and images.** oEmbed, the "next" metadata endpoint, thumbnails, and storyboard sprites through an Invidious instance. Storyboards are thumbnail sprite sheets (one frame every 10 s, or every 1 s for the short). I watched no video.
- **Official sites.** battlebears.com (home, games, characters, sitemaps) and play.battlebears.com.

**What I could not reach:**
- **web.archive.org.** Every request was reset by the egress proxy (ws_closed_mid_exchange), and WebFetch was refused. archive.org's availability API still confirms that snapshot 20140108131247 of SkyVu's Gold Digger page exists (status 200).
- **YouTube player API.** It returned "LOGIN_REQUIRED".
- **Other archives.** timetravel.mementoweb.org and webarchive.org were refused by the proxy.

---

## Official text

- **Steam store, re-read 2026-10-18 through the store API:** "Iconic Maps will return so prepare to jump back into classics such as No Bears Land, Gold Digger and Space Oddity. You can even make some time for that yearly match on Steamyard Blues, most likely just for the soundtrack." [Canon] ([Steam app 4408320](https://store.steampowered.com/app/4408320))
- **Same page, on modes:** "Whether you're a Team Battle diehard or prefer the underrated Plant the Bomb, there is plenty of battling to be done." The mode list reads "-Team Deathmatch (TDM) -Free for All (FFA) -Plant the Bomb (PTB)" [Canon].
- **Steam short description:** "…compete with friends across 16 wacky maps." [Canon]
- **2013 launch trailer.**
  - "BATTLE BEARS GOLD Trailer: Award-Winning Multiplayer Shooter Game" on the official BATTLE BEARS channel. Title and channel confirmed by YouTube oEmbed [Canon].
  - Its description includes "3 New Maps:\n-Gold Digger\n-Skate or Die\n-Sky View" and ends "Coming June 2013!" [Canon].
  - Published 1369947857, which is 2013-05-30 21:04 UTC; 69 s long.
  - I read the description from the YouTube metadata stored on the wiki's file page, "File:BATTLE BEARS GOLD Trailer Award-Winning Multiplayer Shooter Game" ([rfAyqVJrli4](https://www.youtube.com/watch?v=rfAyqVJrli4)).
- **Official soundtrack** ("BATTLE BEARS GOLD Soundtrack", SkyVu, coming Nov 4, 2026).
  - Track 4 is "Gold Digger", 0:38 [Canon].
  - Short description: "The official BATTLE BEARS GOLD Soundtrack featuring original map and menu music by Rob Ruiz, AnDrue Humphreys, and Benjamin Vavak." [Canon] ([Steam app 5321720](https://store.steampowered.com/app/5321720))
- **SkyVu's 2013–14 map blurb, as quoted in our notes:** "narrow tunnels deep underground with nothing but rickety old wooden beams between you and a horrible, horrible death… a pit full of gold and several other armed and equally avaricious opponents." [Canon per our notes; Unverified this session] ([archived page](https://web.archive.org/web/20140108131247/http://battlebears.com/games/battle-bears-royale/maps/gold-digger/))
  - The snapshot exists (archive.org availability API, 2026-10-18), but I could not open it.
- **Patch 2.6.1 (January 4, 2014).**
  - The Updates page and the Versions table read: "Arbiter will no longer spawn with Bearscream Sandwich on Gold Digger" [Game text via wiki].
  - The 2.6 sub-page reads "Assault will no longer spawn with Bearscream Sandwich on Gold Digger" [Game text via wiki]. One editor wrote that page between December 28 and 30, 2015, and it also turns "Arbiter's missing taunt icons" into "Assault's" [Fan-wiki: page history].
  - The Updates page says it gives "the official update descriptions" [Fan-wiki].
  - Arbiter was new in 2.6, which fits a missing-taunt-icon bug, so "Arbiter" is the likelier original [Inference].
- **Official 2026 short.** "BBG Maps Ranked part 1", BATTLE BEARS channel, dated Oct 11, 2026. Description: "Maps ranked pt1, do you agree?" [Canon] ([jkv6FHPghx8](https://www.youtube.com/watch?v=jkv6FHPghx8))
- **battlebears.com (live):** "This year we're bringing it back to Steam PC and Mobile, packed with new modes, maps, skins and more!" [Canon]
  - The site's live pages carry no Gold Digger text. I checked the home, games and characters pages and the page and article sitemaps [Unverified: absence check].

## Era and status

- **Battle Bears Royale (BBR, 2012): not a BBR map.**
  - SkyVu's November 2012 BBR map list in our notes has seven maps and no Gold Digger [Canon per our notes; not re-fetched: Wayback unreachable].
  - BBR 1.4.3 (April 15, 2013) promised "★ 3 NEW maps!" under "Coming soon to Battle Bears!!" [Game text via wiki, Updates page].
  - Those three are presumably Gold Digger, Skate or Die and Sky View [Inference].
- **Added at the BBG launch, May–June 2013.**
  - The wiki says BBG was "re-released on the App Store as Battle Bears Gold" on May 24, 2013 [Fan-wiki]. It dates Android to June 3, 2013 and Windows PC to December 20, 2013 [Fan-wiki].
  - The wiki's Gold Digger page was created May 25, 2013: "Gold Digger is a map coming in [[Battle Bears: Gold]]" [Fan-wiki, revision 38145].
  - The May 30 trailer lists it among "3 New Maps" but still says "Coming June 2013!" [Canon]. That "June" may refer to Android or a wider release [Inference].
  - The wiki's gallery screenshots were uploaded June 4, 2013 by Galli8, and the map icon on June 15, 2013 [Fan-wiki file data].
  - The Sky View page says the three maps came "on the 2.0 update" [Fan-wiki]. The version tables jump from 1.0.2 to 2.1 with no 2.0 [Fan-wiki].
  - The wiki's BBG gallery captions settle the meaning. They call the BBG launch loading screen "The first 2.0 loading screen" and the BBR splash "Before 2.0 splash screen", and say BBR's 1.4.2 icon was "discarded as of version 2.0" [Fan-wiki]. So the wiki's "2.0" is the May 2013 BBG launch [Inference, well supported].
- **Modes, 2013–2021.**
  - The wiki lists Team Battle, Plant the Bomb and Free-For-All (added in v2.5, November 27, 2013) [Fan-wiki].
  - King of the Windmill "was added in version 2.8 and removed in version 2.29" [Fan-wiki]; 2.8 is dated March 4, 2014 [Game text via wiki].
  - A "New Battle Royale mode" arrived in 2.50 (April 5, 2018) [Game text via wiki].
  - The Plant the Bomb page says "The game takes place in the same stages as Team Battle" [Fan-wiki]. The Free-For-All page says players "spawn in the same points as they would in a team-based Team Battle or Plant the Bomb game" [Fan-wiki].
  - No source names a mode on Gold Digger specifically [Unverified]. The general wiki statements imply it hosted Team Battle, Plant the Bomb and Free-For-All [Inference].
- **Changes over time.**
  - **Pickups.** The wiki's account changes from edit to edit.
    - Edits from June 20 to August 15, 2013 put an Imperial Basket Grande "outside both teams' spawn" plus "Bonus Joules: Located on the walls next to the main entrance of each team's base" [Fan-wiki, revisions 43509–49689].
    - Map Joule pickups "were removed in 2.1" [Fan-wiki, Joules page], and 2.1 is dated July 15, 2013 [Game text via wiki]. The Bonus Joules line was deleted on August 27, 2013 [Fan-wiki, revision 51142].
    - From November 23, 2013 (revision 57222) until September 2026, the page said the Imperial Basket Grande was only "outside Red teams' spawn". A trivia line was added: Blue "originally had a Joules pickup in place of the Imperial Basket Grande" [Fan-wiki].
    - On September 21, 2026, user Alphabbr changed the line to "Located outside Red teams' and Blue teams' spawn". The edit summary reads "this got updated to have ibgs for both sides some time ago". The Red-advantage trivia was left in place [Fan-wiki, revision 77726].
  - **2.6.1** (January 4, 2014) fixed a class spawning with the Bearscream Sandwich on this map [Game text via wiki].
  - **3.0** (November 15, 2021) lists "New Map Lighting" for the whole game [Game text via wiki].
  - **Servers** "have shut down since March 12, 2024" [Fan-wiki].
- **The 2026 re-release.**
  - Named on Steam as a returning classic [Canon], and it has its own soundtrack track [Canon].
  - **In SkyVu's official short.** Gold Digger is one of 16 map stills in the "BBG Maps Ranked part 1" thumbnail: row 4, column 3 of a 4×4 grid in `oar1.jpg` [Observed]. A second thumbnail (`oar2.jpg`) shows a tier list with rows "1-4", "5-8", "9-12" and "13-16" [Observed], which matches "16 wacky maps" [Inference]. The short's storyboard does not show Gold Digger being ranked in part 1 [Observed: 76 storyboard frames].
  - **In the October 15, 2026 final playtest.**
    - A fan video, "Battle Bears Gold - Final PC Playtest (10/15/26)" by InstableGR (published Oct 17, 2026), lists "31:20 - Match 8 (Team Battle, Gold Digger, Huggable/Riggs/Graham)" [Unverified: fan source] ([HKbwq7PolNc](https://www.youtube.com/watch?v=HKbwq7PolNc)).
    - Its storyboard frames at about 1890–2120 s show Gold Digger in the 2026 build, with a red-vs-blue team score HUD [Observed: storyboard sprites]. So the map is in the 2026 build and ran at least as a team mode [Observed + Inference].
    - Whether FFA or PTB run on it in 2026 is unknown [Unverified].
  - **Lighting.**
    - The final playtest notes list "Lighting improvements" [Canon], and the "CLOSED TESTING 5" banner reads "-LIGHTING, EFFECT & TEXTURE IMPROVEMENTS" [Observed]. The banner image shows No Bear's Land, not Gold Digger [Observed].
    - The fan uploader writes of "an overhauled lighting for all maps, attempting to restore what they looked like back in the day", naming No Bear's Land, Desert Airmine and Space Oddity but not Gold Digger [Unverified: fan claim].
    - In the storyboard frames, Gold Digger keeps its 2013 look: night sky, rock walls, carts and gems. It reads slightly brighter and greyer than the 2013 trailer (see Look) [Observed, low resolution].
  - **The official October 15 livestream** ("BBG Livestream Final Playtest before Steam NextFest Oct 19") shows no Gold Digger match in its 620 storyboard frames [Observed] ([ZMhLVXWT6OY](https://www.youtube.com/watch?v=ZMhLVXWT6OY)).
  - **Steam news.** None of the seven 2026 posts mentions Gold Digger. I checked the text through the news API on 2026-10-18 [Unverified: absence check].
  - **Demo.**
    - play.battlebears.com: "Play the demo on Steam from October 19-26" [Canon].
    - The livestream description says "Steam Next Fest Oct 19-21" [Canon].
    - An official stream, "Steam Next Fest Demo Party with BBG Devs", is scheduled for Oct 19, 2026 [Canon].
    - Whether the demo includes Gold Digger is unknown [Unverified].
- **The Steam trailer is most likely 2013 gameplay that SkyVu re-used on the 2026 Steam page.**
  - Its Graham, Tillman and Oliver cards (frames `t_0023`, `t_0059`, `t_0085`) match the 2013 trailer's auto-thumbnails `rfAyqVJrli4` hq1, hq2, hq3 and maxresdefault exactly [Observed].
  - It opens on the current logo (`t_0002`) [Observed].
  - Its Gold Digger footage is therefore probably 2013-era [Inference].
  - A later check matched the gameplay too, not only the cards, against the 160×90 storyboard of that 2013 trailer. Storyboard frames at 2013 8 s, 12–13 s and 57 s match the Steam trailer at about 4.0 s (B-1000 under the moon), 8.0–9.0 s (Graham) and 53.0 s (the overhead), one in each Gold Digger segment [Observed: match table `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/edit2026_tr/sb_match.txt`, cited in the maps overview, section 0, item 1; side by side in `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/rev_gd/gd_sb_check.jpg`]. So the Gold Digger footage is 2013 footage [Inference, strong].
  - The Graham shot at 7.0–10.0 s is no exception: its frames at about 8.0 and 9.0 s are among those storyboard matches [Observed]. A weapons note had dated it "2018 or later" from Graham's toon outlines, but some 2013 fan captures already show those outlines (Gold Graham, July 2013; the circuit-pattern skins, September–November 2013) [Observed, per `research_notes/BBG weapons (verified)/graham.addendum.md`, Incidental findings 1]. Why this Graham is outlined when December 2013 fan captures of the same Instagraham skin are not stays open [Unverified]. It is not 2026 evidence.
- **Battle Bears Heroes (2024).** battlebears.com says BBH features "all the famous characters, weapons, and maps" [Canon]. No source names Gold Digger in BBH, and the wiki has no BBH map page for it [Unverified].

## Setting

- **The wiki:** "It appears to be a mining cave, hence the name." [Fan-wiki]
- **SkyVu's blurb:** "narrow tunnels deep underground… a pit full of gold" [Canon per our notes; Unverified this session].
- **The main arena is open to the night sky.**
  - **2013 trailer.** A dark navy sky with small white stars and a bright, textured full moon with a soft halo sits above the rock walls (`t_0009` at 4.0 s, `t_0011` at 5.0 s) [Observed].
  - **2026 official short.** The Gold Digger still shows stars above a curved wall of stacked rock [Observed].
  - **2026 playtest.** A frame shows the same navy starry sky above tiered rock walls (fan video storyboard, about 2080 s). No moon is in view there [Observed].
- **The side tunnels are roofed.** They have timber frames, an earthen brown ceiling and hanging lamps (wiki `Gold_Digger_4.jpg`, map icon) [Observed].
- **Best reading:** a night-time open-pit gold mine, with timber-roofed rail tunnels leading off the pit [Inference].
- **Link to Sky View.**
  - The wiki's trivia: "If a player is to glitch their way out of the map, they will see that the background is the same as [[Sky View]], with all of its buildings, suggesting some connection between the two maps." [Fan-wiki]
  - The Sky View page adds: "This map uses the same skybox as Gold Digger." [Fan-wiki]
  - Sky View's gallery shows a navy starry sky with a magenta dusk glow over city towers [Observed]. Gold Digger frames show navy and stars, but I saw no magenta glow in them [Observed]. That is a partial fit with a shared skybox [Inference].
- **Where it sits in the Battle Bears world:** not documented [Unverified].

## Layout

- **Overall shape.** An oval bowl ringed by tall tiers of stacked rock blocks (`Gold_Digger_2.jpg`, `Gold_Digger_3.jpg`; trailer 52.1 s) [Observed].
- **Centre.**
  - Two deep shafts sit on a diagonal, one kidney-shaped and one rounded teardrop. From above they read as a lopsided figure 8 (`Gold_Digger_3.jpg`; trailer 52.0–53.5 s) [Observed].
  - Grey slab stones ring the rims. The shaft walls are sheer, faceted and streaked olive-brown, and they drop into pure black [Observed].
  - A narrow, floor-level dirt path edged with stones runs between the two shafts [Observed, `Gold_Digger_2.jpg`, 52.1 s]. The wiki calls it "a bridge in the middle of the map" [Fan-wiki]. It looks about one to two bears wide [Inference, judged against characters at 52.1 s].
- **Floor.** A ring of packed ochre dirt runs between the shafts and the walls, with big rounded grey boulders at the shaft lips as cover [Observed].
- **Edge of the pit.**
  - Curving stone-curbed paths and ledges run along the foot of the walls [Observed, `Gold_Digger_3.jpg`].
  - Two gold carts sit on opposite ledges, each on a pale stone-paved patch (`Gold_Digger_3.jpg`; trailer 52.1–53.0 s) [Observed].
  - Diagonal timber braces lean against the pit walls (`Gold_Digger_2.jpg`, `Gold_Digger_3.jpg`) [Observed].
- **Openings in the walls.** Four kinds appear in the images:
  - Open timber-framed tunnel mouths with lit, rounded-cobble interiors (`Gold_Digger_1.jpg`, left) [Observed].
  - A timber mouth closed off low by a solid plank board (`Gold_Digger_1.jpg`, right) [Observed].
  - Wide openings closed by a wooden post-and-rail fence, with a mine track running across behind (`Gold_Digger_2.jpg`; trailer 52.1 s) [Observed].
  - A long, straight, roofed rail tunnel with a gold cart at the end of the track (`Gold_Digger_4.jpg`, map icon) [Observed].
- **Team sides and spawns.**
  - The wiki mentions "team-coloured jewels to indicate which spawn point the player is in" [Fan-wiki].
  - A faceted red gem glows on the rock right of a timber tunnel mouth (`Gold_Digger_1.jpg`) [Observed].
  - A red glow sits at the right post of a fenced rail opening, with a gold cart on a ledge to its left (`Gold_Digger_2.jpg`) [Observed].
  - The mirror of that arrangement appears with a blue gem at the fenced opening's right post and a cart to its left (trailer 52.1 s) [Observed].
  - A blue faceted gem sits right of a timber tunnel mouth (Steam `screen_03`; trailer 7.0–10.0 s) [Observed].
  - So each team side has matching gems, openings and carts, and the map looks mirror-symmetric [Inference].
  - Health Packs are "Inside the spawn area near the central cave" [Fan-wiki, Health Pack page], so the spawns are probably the tunnel areas behind the gem-marked openings [Inference].
  - Which side of the pit is red and which is blue is not documented [Unverified].
- **Height and movement.**
  - The map is mostly one level, with deadly shafts below and raised ledges at the walls [Observed].
  - Two jump pads sit in the dirt ring on opposite sides of the shafts (trailer 52.5–53.8 s) [Observed].
  - The wiki: "Launch pads appear in most stages in BBG, apart from Skate or Die, Sky View and Toxic Terror. Walking over one will launch players either vertically or at an angle." [Fan-wiki, BBG Maps page]
  - Where Gold Digger's pads send you is not documented [Unverified].
- **Pickups, according to the wiki:**
  - Bearscream Sandwich: "Located at the middle of the bridge." The Bearscream page adds "In the center of the map, on top of the bridge." [Fan-wiki]
  - Shield: "Located outside both teams' spawn, next to Imperial Basket Grande." [Fan-wiki]
  - Health Pack: "Located inside both teams' spawn." [Fan-wiki]
  - Imperial Basket Grande: "Located outside Red teams' and Blue teams' spawn, next to Shields." The Imperial Basket Grande page gives "On a raised area near the shield pickup", number 2 [Fan-wiki].
  - In the trailer overhead, a floating pickup sits on a raised ledge left of the blue fenced opening (52.1 s, 52.6 s). It reads as golden pieces on white paper in a red base [Observed], which fits the wiki's Imperial Basket Grande icon (a red basket of golden fried pieces) and its "raised area" location [Inference].
- **In 2026 (fan-recorded storyboard, 429×180).** The frames show trench edges over dark pits, gold carts, a timber rail tunnel with large rounded cobbles and rails, the red and blue gems, and tiered walls under stars [Observed]. Nothing at that resolution suggests a changed layout [Inference].

## Look

**Palette.** I sampled raw pixels: 10th-percentile, median and 90th-percentile by luminance, with the file and region cited. The gameplay frames are very dark: `t_0105` averages RGB(33,22,14), `t_0007` RGB(34,27,25) and `t_0009` RGB(37,31,30). For shorts, raise the exposure but keep these hue relationships [Inference].

| Element | Shadow | Mid | Highlight | Source (region, px) |
|---|---|---|---|---|
| Stacked rock walls (warm charcoal, plum cast) | #080100 | #170E0F | #302525 | trailer 52.1 s (1300–1700, 10–150); `t_0009` median #110909 |
| Boulders and slab stones | #33292C | #393032 | #3C3235 | 52.1 s (520–640, 260–380); `t_0007` median #372E31 |
| Pit floor dirt (lit) | #302115 | #3F2A13 | #422B15 | 52.1 s (300–460, 440–500); `t_0007` median #3D2B15; unlit median #251301 |
| Shaft walls (olive-brown) | #090300 | #181008 | #251C0F | 52.1 s (640–760, 420–520) |
| Shaft bottom | | #000000 | | 52.1 s (1060–1220, 700–820) |
| Rail-tunnel floor | #1B1310 | #4E3316 | #613916 | `Gold_Digger_4.jpg` (560–640, 290–330) |
| Rail-tunnel cobble wall | #18100D | #2E231C | #46382D | `Gold_Digger_4.jpg` (560–630, 120–220) |
| Tunnel ceiling (earth) | #0B0A06 | #281A0D | #452A15 | `Gold_Digger_4.jpg` (250–400, 30–60) |
| Timber | #241301 | #331D02 | #533417 | `Gold_Digger_4.jpg` (350–368, 110–250) |
| Gold load in cart | #4C3C17 | #DDA612 | #FFD50E | 52.1 s (668–722, 183–197) |
| Blue team gem | #0000B3 | #0206E7 | #5A67E7 | `screen_03` (1285–1325, 440–480) |
| Red team gem | #2D1312 | #591614 | #921408 | `Gold_Digger_1.jpg` (93–103, 124–134) |
| Jump-pad centre (cyan) | | #2C93A3 | #31BFE1 | 52.6 s (338–362, 346–366) |
| Night sky | #001121 | #00172B | #001A2D | `t_0009` (480–620, 5–110) |
| Moon | #8FACBC | #ACC6D8 | #E5F3FC | `t_0009` (665–715, 150–185) |
| Hanging lamp lens | #787252 | #ECF0AE | | `Gold_Digger_4.jpg` (412–438, 8–20) |

All rows are [Observed].

**2026 comparison.** These come from fan-recorded storyboard sprites (429×180, heavily compressed), so treat them as rough.
- Sky median #0E2B40 (f_2080000) [Observed].
- Walls #211915–#261E1B, floor #31251A–#3A2F28, gold load median #7B7413 (highlight #B09707), tunnel cobble #4F4027 [Observed].
- Blue gem #1006DC and red gem #82131A [Observed].
- The official short's Gold Digger tile: sky #0D2B3D, wall #231D1F [Observed]. Those values sit close to the 2026 playtest frames, so the tile is probably a 2026-build still [Inference].
- Whole-frame means of about RGB(52–55,47–52,37–41) against about RGB(33–37,22–31,14–30) for the 2013 trailer. The 2026 frames read brighter and less orange. HUD, characters and video encoding inflate these numbers, so they are only an indication [Observed numbers; Inference on cause].

- **Lighting and time of day.**
  - It is night [Observed].
  - The key is low and warm. The light comes from the glowing gold loads, the tunnel lamps (with a visible light cone in the map icon) and soft oval pools of light on the dirt (52.1 s) [Observed].
  - The only cool tones are the navy sky and the moon. The rock stays warm dark brown right up to the crests; no moonlight is visible on the walls (`t_0009` crest samples have medians #0E0807 to #161211) [Observed].
  - The 2021 "New Map Lighting" and the 2026 "Lighting improvements" may have changed exposure [Inference]. The 2026 storyboard keeps the same overall scheme [Observed].
- **Materials.**
  - Chunky low-poly shapes with simple painted textures [Observed].
  - The walls are cube-like rock blocks stacked in uneven tiers, with cobblestone-pattern faces and dark grout lines [Observed].
  - The tunnel walls use bigger, lighter, rounded cobbles; the tunnel ceiling is earthen orange-brown; the timber is plain brown wood [Observed].
  - The rails are dark riveted metal on wooden sleepers [Observed].
  - Small yellow flecks of gold are scattered on the tunnel floor (`Gold_Digger_4.jpg`) [Observed].
- **Signature props** [Observed]:
  - Small mine carts: dark plank boxes on little wheels, each filled to the brim with a flat, glowing yellow-gold load. No separate nuggets are visible.
  - Mine rails.
  - Timber post-and-beam tunnel frames, and diagonal timber braces.
  - Wooden post-and-rail fences across the rail openings, and a plank board across one mouth.
  - Squat octagonal ceiling lamps hung from a black cable.
  - Faceted red and blue team gems set into the rock.
  - Big rounded boulders and slab-stone rims.
  - Jump pads: a glowing cyan star-pattern centre in a yellow-and-black striped ring on a dark octagonal plate, matching the wiki's `Jump_Pad.jpg`.
- **Weather and particles:** none seen. The only glows come from the gold, gems, lamps and pads [Observed].

## Landmarks

1. **The twin black shafts and the narrow stone-edged "bridge" between them.** The Bearscream Sandwich spawns at its middle [Observed; Fan-wiki].
2. **The bowl of towering stacked-rock walls under a navy starry sky,** with a full moon in the 2013 trailer [Observed].
3. **Glowing gold carts on opposite stone ledges,** with another at the end of the rail tunnel [Observed].
4. **The straight rail tunnel with timber frames and hanging lamps.** This is the image on the map-select icon [Observed].
5. **The fenced rail openings and timber mouths marked by a red or a blue faceted gem** [Observed; Fan-wiki].
6. **Cyan jump pads with hazard-striped rims** on the dirt ring [Observed].

## Hazards and interactive elements

- **The shafts.** "If you fall off the bridge, and into a black pit, you will suicide." [Fan-wiki] They render as bottomless black [Observed].
  - A Shield pickup will not save you: shielded players "can still die by falling off a stage" [Fan-wiki, Shield page], and "Players can still suicide from natural hazards" [Fan-wiki, Pick-Ups page].
  - In Plant the Bomb, if the carrier "falls into a suicide pit, the bomb will instanly explode" [Fan-wiki, Plant the Bomb page; a general rule, not Gold Digger-specific].
- **Jump pads.** Two were seen [Observed]. They launch players "either vertically or at an angle" [Fan-wiki].
- **Pickups:** as listed under Layout [Fan-wiki].
- **Wooden beams.** SkyVu's blurb mentions "rickety old wooden beams" [Canon per our notes; Unverified this session]. No collapsing beams, moving carts or other interactive set pieces are documented [Unverified].
- **Spawn protection.** A June 20, 2013 wiki revision, removed hours later, said: "Unlike in the [[H.I.P. Test Lab]], the [[Demo]]'s Secondary weapons can hit targets inside the spawn points." [Fan-wiki, revision 43509]
  - Respawning players get shields "for 4.5 seconds (to discourage spawn killing)" [Fan-wiki, Shield page]. The 2026 storyboard shows a respawned Graham flanked by green shield icons [Observed].

## Easter eggs and references

- **Sky View in the background.** If you glitch out of the map, Sky View's city shows behind it, and the Sky View page says the two maps share a skybox [Fan-wiki].
- **Pickup imbalance trivia.** The wiki says: "This is the only map where a team has a direct advantage over another…", because only Red had an Imperial Basket Grande [Fan-wiki]. The September 2026 edit says both sides now have one [Fan-wiki]. June–August 2013 revisions already listed it "outside both teams' spawn" [Fan-wiki], so the wiki's history contradicts itself.
- **The name.** "Gold digger" is an idiom for someone chasing money, and the blurb's "equally avaricious opponents" plays on it [Inference].
- **Nothing else documented.** No hidden graffiti, character cameos or secret rooms are recorded for this map [Unverified].

## Sound and music

- **Its own track.** The official soundtrack's track 4 is "Gold Digger", 0:38 [Canon]. The album credits "Original Score: Rob Ruiz, AnDrue Humphreys, and Benjamin Vavak" [Canon], but not per track, so who composed this cue is unknown [Unverified].
- **Every stage has music.** "Each stage consists of its own map layout as well as soundtrack." [Fan-wiki, Battle Bears Gold page]
- **2026 Jukebox.** The final playtest added a "-Jukebox" [Canon]. A fan says you "can even assign them to maps" [Unverified: fan claim].
- **Ambient sound effects:** not documented [Unverified].

## Images viewed

All paths are absolute.

**Wiki images** (original format, in `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/gold_digger_verify/img/`):
- `orig_gd1.jpg`–`orig_gd4.jpg`, from https://static.wikia.nocookie.net/battlebears/images/6/67/Gold_Digger_1.jpg, …/2/2d/Gold_Digger_2.jpg, …/5/5c/Gold_Digger_3.jpg and …/1/12/Gold_Digger_4.jpg (`&format=original`). Viewed as `gd_gallery.png`.
- Zooms: `z_gd1_mouths.png`, `z_gd2_right.png`, `z_gd3_top.png`, `z_gd4.png`.
- Map icon `orig_icon.png` (…/c/c8/Gold_Digger.png), with `orig_ibg.png`, `Bearscream_Sandwich.png` and `Jump_Pad.png` in `icon_pickups.png`.
- `Battle_Bears_Gold_loading_screen.png` (shows characters, no map).
- Sky View 1–4: `sv1.jpg`–`sv4.jpg`, viewed as `sv_sheet.png`.

**Steam trailer frames.**
- Opened individually from `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/trailer/`: `t_0007.jpg` (3.0 s) and `t_0009.jpg` (4.0 s).
- In `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/gold_digger_verify/frames/`:
  - Contact sheets `tr_02_25.png`, `tr_26_67.png` and `tr_68_108.png`, covering every frame.
  - My own 1920×1080 extractions `v_52.1.png`, plus `v_51.6`, `v_51.9`, `v_52.6`, `v_53.0`, `v_53.4` and `v_53.8` in `v_sheet.png`.
  - Zooms: `z_pickup_cart.png`, `z_fence.png`, `z_pads.png`, `z_crest.png`, `z_shieldspot.png`, `z_ledge526.png`.
  - Sample checks: `sample_sheet1.png`–`sample_sheet3.png`.
- Gold Digger appears at 1.5–5.0 s (B-1000 by a boulder at the trench rim, then the moonlit walls), 7.0–10.0 s (Graham at a timber mouth with the blue gem) and 51.9–54.0 s (overhead of the twin shafts, crossfading in from Shortest Parsec at 51.6–51.9 s).

**Steam screenshots.**
- `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/steam_screens/screen_03.jpg` (opened full size), and all five in `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/gold_digger_verify/steam/steam_sheet.png`.
- Only `screen_03` is Gold Digger. The current store files are byte-identical (MD5) to these.

**Steam news images.** `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/gold_digger_verify/steam/news_b7c8f8f1….png` (Closed Testing 5 banner, No Bear's Land), `news_3b7f9b97….png`, `news_282237bb….png` and `news_60061117….png`. None shows Gold Digger.

**YouTube** (in `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/gold_digger_verify/yt/`):
- `jk_oar1.jpg`, with the tile crop `jk_gdtile_big.png`; `jk_oar23.png` (`oar2` + `oar3`); `jk_mega_00.jpg` and `jk_mega_01.jpg` (all 76 storyboard frames of jkv6FHPghx8).
- `cmp_cards.png`: rfAyqVJrli4 hq1, hq2, hq3 and maxresdefault against `t_0023`, `t_0059`, `t_0085` and `t_0001`.
- `ls_mega_00.jpg`–`ls_mega_05.jpg` and `ls_check.png` (the official livestream ZMhLVXWT6OY storyboard).
- Fan video HKbwq7PolNc storyboard: `sb/HKbwq7PolNc/cs_09.jpg`, `sb/HKbwq7PolNc/cs_10.jpg`, `gd26_a.png`–`gd26_d.png` (frames at 1880–2120 s), `hexgrid.png`, `f2080_big.png` and `build_str.png`.

## Prompt pack

**Establishing shot (vertical 9:16, environment only, style-neutral):**

> High three-quarter view looking down into an oval open-pit gold mine at night. In the centre of the bowl two deep mine shafts sit on a diagonal like a lopsided figure eight, one kidney-shaped and one a rounded teardrop; their rims are ringed with flat grey slab stones and their sheer, faceted olive-brown walls fall into pure black. A narrow floor-level dirt path edged with stones runs between the two shafts like a bridge. Big rounded grey boulders rest at the shaft lips. The floor is packed tan-ochre dirt with soft oval pools of warm light. Curving stone-curbed ledges run along the foot of the walls; on two opposite ledges sit small dark plank mine carts on little wheels, each filled to the brim with a flat, glowing yellow-gold load. Around the bowl rise tall, uneven tiers of chunky stacked rock blocks, warm charcoal with a faint plum cast, every face patterned like cobblestone with dark grout lines; diagonal timber braces lean against the rock. Set into the walls are timber-framed tunnel mouths with heavy posts and lintels, and a wide opening closed by a wooden post-and-rail fence with mine rails running behind it. A faceted gem glows red in the rock beside one opening, and a faceted gem glows blue beside the opposite one. Two round jump pads, glowing cyan star centres inside yellow-and-black striped rings on dark octagonal plates, are set into the dirt on opposite sides of the shafts. Above the rim is a dark navy sky with small white stars and a bright, textured full moon with a soft halo. Low-key night lighting: warm gold and lamp glows below, cool tones only in the sky and moon, and the rock staying warm and dark right to its crest. Chunky simplified low-poly forms, clean painted textures. No characters, no text, no logos.

**What is documented and what is invented in this shot:**
- **Observed somewhere:** the overhead layout, carts, fence, boulders and pads (trailer 52.0–53.8 s; `Gold_Digger_3.jpg`); the braces (`Gold_Digger_2.jpg`, `Gold_Digger_3.jpg`); the moon and sky (trailer 4.0–5.0 s); the gems (`Gold_Digger_1.jpg`, `Gold_Digger_2.jpg`, `screen_03`, 52.1 s).
- **[BBG News invention]:**
  - The vertical framing.
  - Putting the moon in the same frame as the high overhead angle. The moon was only seen from floor level in 2013, and not at all in the 2026 frames I sampled.
  - Showing the red and blue gems together in one shot.
  - The exact placement of the pads relative to the gems.

**Places a short could stage a scene:**
1. **The Bridge.** The path between the shafts, where the Bearscream Sandwich spawns [Fan-wiki]. A fall is instant death [Fan-wiki], and a Shield won't save you [Fan-wiki]. Two bears inch toward the sandwich from opposite ends while a pebble drops into the black and never lands. The pebble gag is [BBG News invention].
2. **The Lamp Tunnel.** The straight rail tunnel: timber frames, octagonal lamps on a black cable, gold flecks on the floor and a glowing cart at the end of the track (`Gold_Digger_4.jpg`, map icon) [Observed]. It suits a spotlight reveal under the lamp cone. Any rolling or runaway cart is [BBG News invention]; moving carts are not documented.
3. **The Gem Gate.** A fenced rail opening with its team gem glowing at the post and a gold cart on the ledge beside it (`Gold_Digger_2.jpg` red; trailer 52.1 s blue) [Observed]. It suits a pre-match huddle. Using the gem as a team-coloured key light on faces is [BBG News invention].
4. **The Moon Rim.** A low angle from the pit floor up the stacked wall to the full moon (trailer 4.0 s) [Observed], for silhouettes or hero shots. Whether the 2026 build keeps the moon is unconfirmed [Unverified].

## Confidence

**observed.** The look and layout rest on official 2013-era frames (the Steam trailer, Steam `screen_03` and the wiki gallery), one official 2026 thumbnail tile, and fan-recorded 2026 storyboard frames that match them. These remain only partly known:
- which side is red and which is blue;
- the modes on Gold Digger in each era;
- where the jump pads send you;
- the exact 2026 lighting values;
- SkyVu's original blurb, which I could not re-check this session.

---

## Corrections to our notes

1. **`research_notes/Battle Bears character lore/franchise_world.md`, line 220.**
   - Current: "**Gold Digger**: a mine. Out-of-bounds, "the background is the same as Sky View"."
   - Correction: The wiki calls it "a mining cave". Out of bounds, "the background is the same as [[Sky View]], with all of its buildings" [FAN-WIKI]. Official frames show the central pit is open to a navy starry night sky, with a full moon in the 2013 trailer; only the side rail tunnels are roofed [OFFICIAL-FRAME].
   - Evidence: Steam trailer frames `t_0009` and `t_0011` (4.0 s and 5.0 s); the Gold Digger tile in `jkv6FHPghx8` `oar1.jpg` (row 4, column 3); wiki `Gold_Digger_4.jpg` (roofed tunnel); Gold Digger page wikitext (API, 2026-10-18).
2. **`research_notes/Battle Bears character lore/animation_reference.md`, Q1 §B "Art style as seen in official frames", the in-game 3D look entry under "In-game 3D and logo" (formerly line 150). Applied: the entry now names the rocky caves as Gold Digger and gives these samples.**
   - Text at the time: "uses chunky, simple low-poly models and highly saturated colour. Interiors are glossy white and red sci-fi, there are lava/orange caverns and rocky caves"
   - Correction: Add that the "rocky caves" are the Gold Digger map (Steam screenshot `screen_03`; trailer 1.5–10 s and 51.9–54 s). Its environment is low-key and desaturated, not highly saturated. Saturation is limited to glowing props (gold load #DDA612–#FFD50E, blue gem #0206E7, jump-pad cyan #31BFE1) and weapon effects.
   - Evidence: Pixel samples. Rock walls median #170E0F (52.1 s) and #0F0708 (`t_0007`); dirt floor median #3D2B15 (`t_0007`); mean RGB(33,22,14) for `t_0105`.
3. **`research_notes/BBG maps (unverified drafts)/research_gold-digger.md`, Look section.**
   - Current: "Cool moonlight catches the wall crests (t_0009) [Observed]."
   - Correction: Remove it. The rock stays warm dark brown up to the crests; the only cool tones are the navy sky and the moon with its halo [Observed].
   - Evidence: `t_0009` crest regions have medians #161413, #0E0807 and #161211 (zoom `z_crest.png`).
4. **Same file, Prompt pack.**
   - Current: "low-key night lighting: warm gold and lamp glows against cool moonlight on the wall crests."
   - Correction: "low-key night lighting: warm gold and lamp glows below, cool tones only in the sky and moon, and the rock staying warm and dark right to its crest."
   - Evidence: As in correction 3.
5. **Same file, Look section.**
   - Current: "Small wooden mine carts heaped with glowing gold nuggets."
   - Correction: "Small dark plank mine carts on little wheels, each filled to the brim with a flat, glowing yellow-gold load. No separate nuggets are visible." [Observed]
   - Evidence: Trailer 52.1 s and 52.6 s zooms (`z_pickup_cart.png`, `z_ledge526.png`); `Gold_Digger_4.jpg`; 2026 storyboard `f_2030000`.
6. **Same file, Era and status.**
   - Current: "Which of these Gold Digger supports is unknown [Unverified]."
   - Correction: Gold Digger is in the 2026 build. A fan's video of the October 15, 2026 final playtest lists "Match 8 (Team Battle, Gold Digger, Huggable/Riggs/Graham)" [Unverified: fan source], and its storyboard frames at about 1890–2120 s show the map with a red-vs-blue score HUD [Observed]. FFA and PTB on Gold Digger in 2026 remain unconfirmed.
   - Evidence: YouTube metadata for HKbwq7PolNc (InstableGR, Oct 17, 2026; title confirmed by oEmbed); storyboard sprites `sb/HKbwq7PolNc/cs_09.jpg` and `cs_10.jpg`.
7. **Same file, Era and status.**
   - Current: "No 2026 Steam news post names Gold Digger [Observed]."
   - Correction: Relabel as a text check: "None of the seven 2026 Steam news posts mentions Gold Digger (checked through the news API) [Unverified: absence check]." [Observed] is reserved for images and frames.
   - Evidence: The news API returned 7 items; a case-insensitive search for "gold digger" found nothing.
8. **Same file, Era and status.**
   - Current: "So the 2026 build may not look like the 2013 images [Inference]."
   - Correction: The 2026 final-playtest storyboard shows the same navy starry sky, stacked-rock walls, glowing gold carts, timber rail tunnel and red and blue gems [Observed]. It reads somewhat brighter and greyer, which could come from the 2026 "Lighting improvements" or from capture and encoding [Inference].
   - Evidence: `gd26_a.png`–`gd26_d.png` and `f2080_big.png`. 2026 sky median #0E2B40 against 2013 #00172B; 2026 frame means about RGB(52–55,47–52,37–41) against about RGB(33–37,22–31,14–30) in 2013.
9. **Same file, Era and status.**
   - Current: "\"2.0\" probably means the launch build [Inference]; this is unresolved."
   - Correction: The wiki's "2.0" is the May 2013 BBG launch. Its BBG gallery captions the launch loading screen "The first 2.0 loading screen" and the BBR splash "Before 2.0 splash screen", and says BBR's 1.4.2 icon was "discarded as of version 2.0" [Fan-wiki].
   - Evidence: Battle Bears Gold page wikitext (API, 2026-10-18).
10. **Same file, Layout section.**
    - Current: "A pickup floats on a rock ledge up the wall, top left of the overhead shot. I could not identify which pickup it is [Observed]."
    - Correction: It reads as golden pieces on white paper in a red base [Observed], which fits the Imperial Basket Grande icon and the wiki's IBG location "On a raised area near the shield pickup" [Inference].
    - Evidence: Zoom `z_pickup_cart.png` (trailer 52.1 s); wiki `Imperial-basket-grande.png`; Imperial Basket Grande page table.

## Open questions

- **SkyVu's blurb.** What is the exact 2013–14 battlebears.com Gold Digger text? Wayback snapshot 20140108131247 exists, but every connection was reset on 2026-10-18.
- **Team sides.** Which side of the pit is red and which is blue? The red and blue gem openings look mirror-symmetric, but their compass orientation and the exact spawn rooms are undocumented.
- **Jump pads.** Two are visible in the trailer overhead. Are there more, and where do they launch players?
- **Modes.** Which ran on Gold Digger in 2013–2021? Where were the Plant the Bomb platforms and tubes, and was King of the Windmill or Battle Royale ever played here? Does Gold Digger support FFA and PTB in 2026, beyond the fan-listed Team Battle?
- **Pickups now.** What is the 2026 layout? Does each side have an Imperial Basket Grande, as the September 21, 2026 wiki edit says?
- **2.6.1 patch.** Did it say Arbiter (Updates and Versions pages; likelier) or Assault (the 2015 sub-page)?
- **2026 look.** Does the 2026 build keep the full moon? What are its true colours under "Lighting improvements"? The storyboard is 429×180. The Steam demo (October 19–26) or the iPad playtest video dz4iqZE8nQE could settle this.
- **2026 effects.** Is the orange-red hexagonal wireframe in the 2026 frames at about 1890–1910 s a weapon or special effect, or a new spawn barrier? Which pickup glows green in a wall recess at about 2080–2090 s?
- **Steam trailer and screenshots.** Are they entirely 2013-era footage? Most likely: the character cards match the 2013 trailer exactly, and the gameplay, the Space Oddity clip included, matches that trailer's 160×90 storyboard, so the maps overview (section 0, item 1) reads all of it as 2013 footage [Inference, strong]. No full-resolution match of the gameplay exists yet.
- **The music.** Who composed the "Gold Digger" track (0:38)?
- **Battle Bears Heroes.** Does Gold Digger or a variant appear there? SkyVu says BBH has "all the famous … maps", but no source names this one.
