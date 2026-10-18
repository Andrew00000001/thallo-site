# Aztec Attack (originally "Facing Temples")

Aztec Attack is a night-time arena with two temples. Two big stepped sandstone pyramids face each other across a cracked, burnt-orange plateau. The plateau sits like an island in a sea of lava, under a starry crimson-to-indigo sky. A lava pool in the middle splits the field. In it sits a large dark obsidian rock, joined by a line of stepping stones to a ruined pavilion on each side.

The map began in Battle Bears Royale (BBR) v1.3.1 (June 28, 2012) as "Facing Temples". It was renamed "Aztec Attack" when the game relaunched as Battle Bears Gold (BBG) in 2013. Its 2026 presence rests on three things:
- "Aztec Attack" is track 13 of the official 2026 soundtrack.
- A fan video of SkyVu's Aug 21, 2026 playtest has the chapter "Aztec Attack FFA".
- It appears in the trailer on the 2026 Steam page. **That trailer is a re-edit of the May 2013 BBG launch trailer, so its Aztec shots show 2013 footage, not the 2026 build** [Inference, strong; evidence under Era and status].

**Verification pass (2026-10-18).** I re-fetched every wiki page and official page cited, re-downloaded and opened every image, extracted full-resolution trailer frames and pixel-matched them, and found new images:
- File:Download_(16).jpg (April 2013).
- The 2015 So Fly video thumbnail on the wiki.
- The wiki's metadata for the 2013 launch trailer.
- The signed chapter thumbnail of the 2026 playtest video.

Path shorthand: **[V]** = `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/aztec_attack_verify/`.

**Sources reached**
- **Fan wiki (MediaWiki API).** Pages read:
  - Aztec Attack: wikitext, images, the full revision history with content, and the latest diff.
  - BBG Maps, Battle Bears Gold, Battle Bears Royale, Updates, BBR Version 1.3.1, BBR Version 1.4.2.
  - Bearscream Sandwich, Health Pack, Imperial Basket Grande, Shield, Over Clocked Oliver, Astoria, Zombocalypse, Battle Bears: Zombies, Battle Bears Heroes, Sniper (BBG), So Fly.
  - Searches of the File namespace and the text, and the backlinks to Aztec Attack (8 pages).
  - "Facing Temples" does not exist as a page. The article was moved from "Facing Temples" to "Aztec Attack" on 2013-06-04 by Kodokor12 [Observed: revision log].
- **Official sources:**
  - Steam appdetails for 4408320 (BBG) and 5321720 (the soundtrack), plus the soundtrack's store page with its track list and credits.
  - The Steam news API for 4408320: 7 posts, none naming this map.
  - battlebears.com: no map text. /maps and the old map URL return 404.
  - YouTube oEmbed (titles and channels) and thumbnails.
  - The wiki-hosted YouTube metadata of the 2013 BBG trailer.
- **Not reached:**
  - web.archive.org reset every connection (curl with retries and backoff; WebFetch said "unable to fetch"). The proxy status log shows the tunnels closing.
  - The archive.org availability API does confirm a 200 snapshot of SkyVu's page at http://web.archive.org/web/20130815053638/http://battlebears.com:80/games/battle-bears-royale/maps/aztec-attack/ , but its text is unread.
  - YouTube watch pages now redirect to Google's "sorry" page. Fan-video descriptions were read from watch and search pages saved on Oct 16 in `.../maps/dl/aztec_attack/yt/`.
  - **No video was watched.** Every video observation is a thumbnail or a frame of the local Steam trailer file.

---

## Official text

- **BBR v1.3.1 update note (June 28, 2012):** "> Awesome New Map - Facing Temples" [Game text via wiki].
  - The wiki's Updates page says it gives "the official update descriptions for every version" and notes "Pertains to the iOS AppStore only." ([Updates](https://battlebears.fandom.com/wiki/Updates))
- **2026 soundtrack (Steam app 5321720):**
  - The track listing includes "13 Aztec Attack 1:20" [Canon].
  - The page says: "The official soundtrack for Battle Bears Gold features the complete collection of map and menu music from the award-winning 4v4 class shooter, along with select bonus vocal tracks from across the series." Credits: "Original Score: Rob Ruiz, AnDrue Humphreys, and Benjamin Vavak" [Canon].
  - The page's credits block spells it "AnDrue Humprey". Label "SkyVu Inc."; release date "Nov 4, 2026" [Canon].
- **2026 Steam store (app 4408320):**
  - The text does not name Aztec Attack [Observed].
  - It says "compete with friends across 16 wacky maps", "fight it out with friends across beloved Battle Bears locations" and "Iconic Maps will return so prepare to jump back into classics such as No Bears Land, Gold Digger and Space Oddity" [Canon].
  - Modes: "Team Deathmatch (TDM) / Free for All (FFA) / Plant the Bomb (PTB)" [Canon].
  - Its only video is titled "Battle Bears Gold Premium - Trailer" (movie 257411324) [Canon].
- **2013 BBG launch trailer:** "BATTLE BEARS GOLD Trailer: Award-Winning Multiplayer Shooter Game", on the BATTLE BEARS channel (YouTube rfAyqVJrli4) [Canon: oEmbed title and channel].
  - The wiki-hosted YouTube metadata gives a publish date of 1369947857 (2013-05-30) and a duration of 69 s.
  - Its description says "Choose from 8 classes", lists "3 New Maps: -Gold Digger -Skate or Die -Sky View" and "HD Graphics (Only available on higher end devices…)", and ends "Coming June 2013!" [Canon via wiki-hosted metadata].
  - Aztec Attack is not named; it was not new in BBG.
- **Official URL slug:** SkyVu's site had `battlebears.com/games/battle-bears-royale/maps/aztec-attack/` by 2013-08-15 [Canon for the slug only; page text unread].
- **Official videos whose thumbnails show the map:** "BATTLE BEARS GOLD Developer Update - Astoria Overhaul" (wUWf9O-YX4A) and "BATTLE BEARS GOLD Developer Update - Tillman Overhaul" (q1Y8Siqfvn4), both by "BATTLE BEARS" [Canon: oEmbed].
  - Neither video date was found. A wiki edit of 2014-06-07 says "Updated Bouncing Betty statistics as of June 6, 2014 (Demo Overhaul)" [Fan-wiki]. That makes about June 2014 likely for the Tillman (Demo) video [Inference].
- **Lead, not re-verified:** our notes quote an archived official BBR maps page (2012-11-30): "Haunted Castle, Abusement Park, Facing Temples, Battlefield Airpad, Desert Airmine, Huggable Factory, Spacecraft." [Unverified this pass; the Wayback Machine was unreachable.]
- **The wiki's own description (not official):** "Aztec Attack, originally titled Facing Temples, is a map added in v1.3.1. It is extremely unpredictable depending on the players. The course features two giant temples on an island-like field surrounded by lava. If a player falls into the lava, it will be counted as a suicide. Each team's base is on the inside of each temple. By going to the back of the temple, players can get on top of it via a series of jump pads." Also: "Next to the lava pool, are ruins. Two smaller buildings, with Pick-Ups in each one and a bomb in the Plant the Bomb mode." [Fan-wiki] ([Aztec Attack](https://battlebears.fandom.com/wiki/Aztec_Attack))

## Era and status

- **BBR v1.3.1, June 28, 2012:** added as "Facing Temples" [Game text via wiki].
  - The wiki's 1.3.1 page says "New map: Aztec Attack, at the time titled Facing Temples." [Fan-wiki]
  - The BBR page's stage table lists it as "Facing Temples" [Fan-wiki].
  - The oldest map image on the wiki is File:IMG_0525.PNG (uploaded 2012-11-22), captioned "Oliver playing the Facing Temples stagein TDM mode" [Fan-wiki caption; Observed].
- **BBR v1.4.2 (released Feb 28, 2013, per the wiki):** the wiki lists a fix for "Mini Me glitches in Battlefield Airpad, Facing Temples and Spacecraft" [Fan-wiki].
- **April 2013 (BBR era):** File:Download_(16).jpg (uploaded 2013-04-21) already shows the lava pool and lava glowing beyond the island [Observed].
- **Rename to Aztec Attack:**
  - Wiki: "Up until version 2.0, Aztec Attack was referred to as the 'Facing Temples'." [Fan-wiki, added 2013-06-04]
  - This is **not** a numbering conflict. The BBR page explains: "The v2.0 installment of Battle Bears Royale saw Battle Bears Gold. This took form as a completely separate app". The new app's own version list starts again at "1.0" (May 24, 2013) [Fan-wiki].
  - The wiki page was moved on 2013-06-04 [Observed]. The "AZTEC ATTACK" map tile was uploaded 2013-06-15 [Observed]. SkyVu's site used the aztec-attack slug by 2013-08-15 [Canon: slug].
- **Modes on this map:**
  - **TDM:** red-vs-blue score HUDs on IMG_0525 (2012) and File:Maxresdefault(100).jpg (2013) [Observed]. The wiki's caption says TDM.
  - **Plant the Bomb:** the mode predates the map, added in BBR 1.3 (May 3, 2012): "NEW Game Mode: 'Plant the Bomb'" [Game text via wiki]. Wiki: "In Plant the Bomb the bombs are in the small buildings to the sides of the map" [Fan-wiki, added 2014]. Fan video KhJEqrNgzo8 ("Facing temples battle bears glitch", about 2013) has thumbnails showing "AUTOMATCHING FOR PLANT THE BOMB" and "YOU'RE ON TEAM RED" with a red/blue counter HUD [Observed fan thumbnails].
  - **FFA:** the mode was added in BBG 2.5, Nov 27, 2013 [Game text via wiki]. Both official overhaul thumbnails show a single-leader HUD ("6 … CARROTS" and "4 … CARROTS") on this map [Observed]. Reading that HUD as FFA is [Inference].
- **Lighting and look changes:**
  - No map-specific rework is documented.
  - The 2012 BBR screenshot is darker and browner. The May 2013 captures and the 2013 launch-trailer footage have the brighter, saturated orange look [Observed]. So the change came with the 2013 BBG relaunch, whose description advertises "HD Graphics" [Inference]. It does not need BBG 3.0.
  - BBG 3.0 (Nov 15, 2021) lists "New Map Lighting" game-wide [Game text via wiki]. No post-2021 image of this map was found to show its effect.
- **Shutdown:** "Battle Bears Gold servers have shut down since March 12, 2024" [Fan-wiki].
- **2026 status:**
  - **Soundtrack:** track 13 "Aztec Attack" (1:20) [Canon].
  - **Playtest:** the fan video "Battle Bears Gold Playtest #3 Part 1" (JustNubz, page date "Aug 21, 2026") has the chapters "1:28 Marecraft TDM / 8:05 Sky Pirates KC / 13:50 Aztec Attack FFA" [fan description, read from the saved watch page].
    - SkyVu's Steam post of Aug 19 announced that playtest for "Friday 21st August" with "New Map: Sky World" [Canon].
    - The chapter thumbnail (hqdefault_830900, 13:50.9) shows the 2026 build here: new HUD with "90/90" health, a "FORGINAL DARKLORD" kill banner, a single-leader score, an edge of the lava sea, a brick temple wall and a magenta sky [Observed].
  - **Steam trailer:** it shows the map at ≈12.25–16.4 s and ≈43.1–45.7 s [Observed], but this is 2013 footage [Inference, strong]:
    - its eight class cards (B-1000, Graham, Astoria, Wil, Tillman, Huggable, Riggs, Oliver) are the 2013 trailer's "8 classes";
    - the 2013 trailer's hq/maxres/sd thumbnails match Steam-trailer frames at 11.92 s, 28.89 s and 42.85 s with pixel MSE 11–13, against a median of about 7,000 [Observed: my pixel comparison];
    - Assassin, Combat Tech and Arbiter are absent.
  - **Lighting caution:** SkyVu's Oct 14, 2026 post lists "Lighting improvements" for the final playtest [Canon]. The launch build may not match the 2013 look.
  - **Launch roster:** inclusion in the Nov 4, 2026 launch is a strong [Inference]; the store text does not confirm it. The 2026 modes are TDM, FFA and PTB [Canon]. That FFA ran on this map in the Aug 2026 playtest is from the fan chapter title. Which modes run at launch is [Unverified].
- **BB Heroes (2024):** nothing found. The wiki describes BBH's MOBA mode as "a variety of three-lane maps" and names no maps [Unverified for this map].

## Setting

- **Theme:**
  - Mesoamerican-style temple ruins on a plateau ringed by a lava sea, at night [Observed].
  - The motifs are stepped pyramids, carved mask faces, swirl and scroll reliefs, stepped-fret bands and gem mosaics [Observed].
  - The name says "Aztec" and the art mixes generic Aztec and Maya cues [Inference].
  - The wiki's comparison with Unreal Tournament's Facing Worlds ("both have vague Mayan motifs") is a 2025 fan addition (added 2025-02-03) [Fan-wiki].
- **Island in a lava sea:**
  - The wiki says "island-like field surrounded by lava" [Fan-wiki].
  - The sand plateau's edges drop straight into an open lava sea that fills the background [Observed]. Sources: the trailer aerial (2013 footage); Maxresdefault(100).jpg (May 2013), where lava glows behind the ruins; Download_(16).jpg (Apr 2013); the 2015 So Fly thumbnail; the Astoria Overhaul thumbnail; and the 2026 playtest chapter thumbnail.
  - So the lava sea dates from at least April 2013 and is still there in 2026 [Observed]. IMG_0525 (2012) shows only an orange glow at the left horizon [Observed].
- **Story location:** none documented. No planet, island name or backstory was found [Unverified]. The 2013 official blurb is unread.

## Layout

- **Shape:**
  - A peanut or hourglass-shaped island. The long axis runs temple to temple, and the island narrows at the waist where the lava pool sits [Observed: File:Facingtemples.png top-down; trailer aerial 43.5 and 45.0 s].
  - **The layout is point-symmetric (a 180° rotation), not a mirror image** [Observed: top-down]. The two tilted ruins, the four corner pads, the 16 face cubes and the white markers each map onto their partners under a 180° turn about the centre, but not under a mirror.
  - The top-down (uploaded 2012-11-27) has a transparent background (alpha 0 outside the island), so no lava sea is drawn. It carries a partly visible "BATTLE BEARS" logo watermark. That it is an official render is [Inference]; its provenance is [Unverified].
- **Temples (one per lobe):**
  - **Top-down** [Observed]:
    - a front staircase facing the centre;
    - two side stair wings, giving a cross-shaped footprint;
    - concentric grey terraces with swirl reliefs;
    - a column of four cyan pad markers climbing the back terraces;
    - a square summit platform with a glowing square panel: orange (≈#EFA354) on the red-marked temple, pale grey-lavender (≈#A79B9D) on the blue-marked one.
  - **In game** [Observed: IMG_0525; Maxresdefault(100).jpg; map tile; trailer 12.5–14 s and 45.0 s]:
    - a broad lower staircase rises from the sand to a mid-level landing;
    - at that landing a dark doorway passage is flanked by gem-mosaic panels;
    - above it the upper tier is a steep truncated pyramid, with a second central staircase running up its face to the summit;
    - stepped-fret bands edge the stair rails and slopes;
    - cobblestone faces cover the side-stair wings.
    - Seen from a corner (IMG_0525), the upper tier reads as a pyramidal cap.
  - **Pillars:** free-standing square sandstone pillars with block capitals stand in loose rows in front of and behind each temple [Observed: IMG_0525; trailer 12.5 s; aerial]. The wiki's glitch notes mention "the pillars at the back of the temple" [Fan-wiki].
- **Bases and spawns:**
  - "Each team's base is on the inside of each temple." [Fan-wiki]
  - The top-down marks red circled-cross markers around the top temple and blue ones around the bottom temple, at the side-stair ends, the stair landings and the front stairs [Observed]. Reading them as spawn markers is [Inference].
  - In the trailer aerial (2013 footage), one temple has red-glowing gem panels and corner lights (≈#D74925–#EB4220). The other has teal, pink and blue gem panels, glowing teal corner gems, and pale teal caps on its nearby pillars [Observed: [V]crops/a43_left.png, a43_right.png, a45_botleft.png].
  - That red = red team and teal = blue team is [Inference], consistent with the top-down's red and blue markers.
- **Centre:**
  - A lava pool fills the waist: roughly round in the 2012 top-down, a rounded octagon in the 2013 footage [Observed].
  - In it sits a large faceted near-black obsidian rock with dark-red marbling, carrying two cyan jump pads (one facing each temple) and a small white pickup [Observed: trailer 43.5 s].
  - A line of smaller dark stones, about two on each side, runs across the pool through the big rock and joins the two ruins [Observed: Maxresdefault(100).jpg; trailer 43.5–45.0 s].
  - Wiki: "floating platforms of rock, with a Bearscream Sandwich and two jump pads at the largest floating platform. The jump pads bring players across the lava pool to the pyramid." and "Connected by the floating rocks platform across the lava pool." [Fan-wiki]
- **Ruins:** two small pavilions flank the pool on the island's flanks, each slightly rotated [Observed: top-down]. Each has [Observed: Maxresdefault(100).jpg; trailer aerial; Tillman Overhaul maxresdefault]:
  - sandstone walls and square pillars under a carved meander frieze;
  - a dark grey carved roof slab with mask and scroll relief;
  - a grey cobblestone plinth with ramps and a sandstone retaining wall;
  - a crumbled hole in one wall.
  - A green shield pickup is visible inside the right ruin in the Tillman Overhaul thumbnail [Observed]. This matches the wiki: Shield "Located under the two structures next to the lava pool". The roofs are "usually only accessible by using So Fly or Metal Crush" [Fan-wiki].
- **Routes** [Observed top-down, with Inference]:
  1. The left flank past the left ruin.
  2. The right flank past the right ruin.
  3. Four corner pads at the pool's corners, whose white lines in the top-down run lengthwise (temple direction) past the pool's left and right edges.
  4. The stepping-stone causeway from ruin to ruin over the central rock. Its two pads launch toward the temples (white lines in the top-down; wiki).
  5. The vertical route: the pad chain up the back of each temple to the summit, a perch overlooking the whole island. The Astoria Overhaul hq3 thumbnail and Download_(16).jpg both show a sniper on a high grey stone platform looking across the pool [Observed]. That this is the summit is [Inference].
- **Jump-pad count:** the wiki says the map "has 12 jump pads, containing the most jump pads out of any map" [Fan-wiki: BBG Maps]. I count 14 cyan markers on the top-down [Observed]: 4 up the back of each temple, 4 at the pool corners and 2 on the rock. The trailer aerial confirms the 4 corner pads and 2 rock pads [Observed]. Unresolved.
- **Pickups** [Fan-wiki]:
  - **Bearscream Sandwich:** "Located on the largest floating platform at the center of the lava pool." (Bearscream page: "In the center of the map, on the rocks in the lava pool.")
  - **Imperial Basket Grande:** "Located on the sides of the pyramids next to a rectangular block"; the IBG page says "In front of a block to the right of each temple" (2).
  - **Health Pack:** "Located at the entrance/exit of temples facing lava pool"; the Health Pack page says "At the front entrance of each temple" (2). IMG_0525 shows a small white box with an orange cross, glowing orange, on a temple ledge [Observed]. That it is the Health Pack is [Inference].
  - **Shield:** "Located under the two structures next to the lava pool."
  - The top-down's white diamond markers sit beside a face cube to the temple's right (from the temple's view), near each ruin, and on the rock [Observed]. Reading them as pickup spawns (IBG, Shield, Sandwich) is [Inference].
- **Scatter:** 16 stone cubes with carved grimacing mask faces on their sides and tops, cracks across the sand, and the free-standing pillars [Observed: top-down count; trailer aerial].

## Look

**Palette.** Approximate hex values: medians of sampled boxes from compressed frames.

| Element | Steam trailer (2013 BBG footage) | 2012 BBR / 2013 captures | 2026 playtest thumbnail |
|---|---|---|---|
| Sky zenith (white stars) | #010123–#05032B | #080039 (2012) | — |
| Upper sky | plum #41082F–#450930 | #4A0039 (2012); #7B0539 (2013) | magenta #790246 |
| Mid sky | crimson #7D0E36 | #730039 (2012) | — |
| Horizon glow | raspberry #9E1138 | #7B0042–#84084A (2012) | — |
| Far hills | maroon #410602 | #422821 (2012); #32210D (2013) | — |
| Sand, lit | burnt orange #D85C2D; near the pool #EA612C | #7B4521 (2012); #C8681E (2013) | — |
| Sand, shade | #8D3E19–#B44A1C | top-down #5A2F15–#693918 | #4F1A0D |
| Temple stairs and walls | #A85936–#BA633A; relief wall #CD7D51 | #5A4531–#7B5531 (2012); stairs #83532D (2013) | shaded brick #442118 |
| Grey terrace and roof stone | ruin roof slab #3E2E28 | top-down roofs #453A33–#473B31 | — |
| Doorway interior | #3B2219 | — | — |
| Pillars | #8C5737 | #7B5531 (2012) | — |
| Lava sea | #FFAC10–#FFAE10 with red marbling | #F68601 (2013) | #F29E16 |
| Lava pool | #FF9D23 | #FBB503 (2013); #FFA800–#FFDE00 (2012 top-down) | — |
| Obsidian rock | #280402, dark-red veins | #2C0D06 (2013) | — |
| Jump pads | cyan #42C7CC | — | — |
| Gems | teal #3C715F, deep teal #044F47, rose #ED625B, pink #AA4847, violet #884956 | cyan gem eyes #29799C (2012) | — |
| Red-temple panels | #D74925–#EB4220 | — | — |
| Summit panels | — | orange #EFA354 / pale #A79B9D (2012 top-down) | — |

- **Lighting and time of day:**
  - It is night in every image: a starry sky (stars visible in 2012, 2013 and the trailer), with no sun or moon [Observed].
  - The light reads as coming from the lava: the lava is the brightest element and the sand and walls glow saturated orange [Observed].
  - The only cool accents are the cyan pads, teal and blue gems, and the teal temple accents [Observed].
  - Shading is soft, with low contrast [Observed].
  - 2012 BBR is darker and browner; the 2013 BBG look is bright orange [Observed]. The 2026 thumbnail's sky and lava match the old palette [Observed]; the full 2026 look is [Unverified].
- **Materials and set dressing** [Observed]:
  - Warm sandstone on vertical faces, with incised swirl and scroll reliefs.
  - Horizontal surfaces (terrace tops, summit, ruin roofs) are grey carved stone with dark swirl relief. This explains the grey temples in the top-down.
  - Carved mask faces with fangs and ear-spools.
  - IMG_0525 shows two large glowing cyan gems in carved frames at a temple's base, which read as a giant mask's eyes [Inference].
  - Rounded cabochon gem mosaics (teal, blue, rose, violet) in scroll frames.
  - Stepped-fret (meander) bands on stair rails, slope edges and ruin friezes.
  - Grey cobblestone on the side-stair wings and ruin plinths.
  - Faceted dark obsidian with red veining.
- **Development render** (File:Facing_Temples_Development.png, uploaded 2012-11-27 by Hackey5) [Observed]:
  - a grey stone stepped tier with carved masks, red and orange gem mosaics and red pillar inlays;
  - a glowing gold mask at the top and a mask with glowing red eyes below;
  - a reddish glow on the lower tier;
  - some faces still untextured white, against a sky-blue gradient;
  - a grey-brick staircase with fret rails, and a distant structure with blue gems.
  - Its stage and provenance are [Unverified]. The shipped temples are warm sandstone with grey horizontal surfaces [Observed].
- **Weather and particles:** none in any still: no rain, smoke or embers [Observed absence; frames, not motion].
- **Style:** chunky low-poly geometry, hand-painted cartoon textures with dark linework, high saturation [Observed].

## Landmarks

1. **The twin stepped temples facing each other across the field.** This is the original "Facing Temples" idea [Observed; name: Game text via wiki].
2. **The grand front staircase:** a lower flight to a dark doorway framed by gem-mosaic panels, then a steep upper flight up the truncated-pyramid top [Observed: trailer 12.5–14 s; Maxresdefault(100).jpg; map tile].
3. **The central lava pool** with its faceted obsidian rock and line of stepping stones [Observed].
4. **The lava sea** surrounding the island [Observed: trailer 43.1–45.7 s; Apr 2013–2026 images].
5. **The two ruined pavilions** with dark grey carved roof slabs, flanking the pool [Observed].
6. **Carved mask-face stone cubes** scattered on cracked orange sand, with rows of free-standing square pillars [Observed].

## Hazards and interactive elements

- **Lava:** "If a player falls into the lava, it will be counted as a suicide." [Fan-wiki] Both the central pool and the outer sea are lava [Observed]. That the outer sea also kills is [Inference, likely].
- **Jump pads:** "If the user moves while in the air after being launched by the Jump Pads, it affects the landing point." [Fan-wiki: BBG Maps]
  - The pad model (File:Jump_Pad.jpg) is an octagon with a yellow-and-black hazard rim, a cyan crystalline centre and stacked cyan octagonal hologram rings [Observed].
  - On this map the pads read as glowing cyan discs from a distance [Observed].
- **No switches, traps or moving parts** are documented [Unverified].
- **Glitches** [Fan-wiki]:
  - "There used to be a glitch where players can go under the pyramids by squeezing through the pillars at the back of the temple with Mini Me."
  - Entering a pyramid's sides through "the gap between the roofs at the third level, third jump pad counting from ground level".
  - "an invisible barrier on the right steps of the temples … This has not been fixed."
  - A mid-air stall near "the Jump Pad at the edge of each team's base" that gives access to the ruin roofs.
- **Caution:** a 2013 BBG fan thumbnail (LOa3e4GyrCk, "…Killdoba fire lasting forever, facing temples") shows flames on a temple top. The fire is a weapon glitch, not set dressing [Inference from the title]. Do not add braziers on that basis.

## Easter eggs and references

- **Temple symbols:**
  - "One temple has a symbol representing Over Clocked Oliver, while the other has a symbol representing Astoria. This may show that Oliver has a crush on Astoria." [Fan-wiki; added 2013-07-06; Unverified]
  - The Over Clocked Oliver page: "In the Battle Bears Gold map Aztec Attack, there seems to be a carving of Over Clocked Oliver, along with Astoria. Both are located at each team's spawn points." [Fan-wiki; Unverified]
  - No image opened (2012–2026) shows such a symbol. The visible carvings are generic masks, scrolls and gem panels [Observed]. The temple interiors (the claimed spot) are never clearly shown.
- **Name:** "Facing Temples" "may have been a reference to the map Facing Worlds from the Unreal Tournament video game series" [Fan-wiki speculation, added 2025-02-03].
- **Zombocalypse pyramid:** "The Aztec Attack's pyramids resembles the pyramid where Zombocalypse stood." [Fan-wiki, added 2013-05-21]
  - File:Uumhfc.jpg, captioned "The pyramid where the Zombocalypse stood", shows a "BATTLE BEARS."-logo drawing of a stepped grey pyramid with green spiral glyphs, a green meander band at the top and a staircase up one face [Observed].
  - The shared feature is the stepped-pyramid form [Inference].

## Sound and music

- **Official track:** "Aztec Attack", 1:20, track 13 of the BATTLE BEARS GOLD Soundtrack (Steam 5321720, Nov 4, 2026) [Canon].
  - Composers are credited only collectively: "Rob Ruiz, AnDrue Humphreys, and Benjamin Vavak" [Canon].
  - The composer of this track is [Unverified].
- **Wiki:** "Each stage consists of its own map layout as well as soundtrack." [Fan-wiki]
- **Fan uploads** (titles from oEmbed; durations and ages from the saved search page; not heard):
  - "Aztec Attack - Battle Bears Gold OST" (mYPnsh-bYb0, 1:24). The quote "Plays in the Aztec Attack map." from the earlier draft could not be re-verified [Unverified].
  - "Aztec Attack soundtrack HQ | Battle Bears Gold Soundtrack" (uvPIiPYpg-s, 3:43).
  - "Battle Bears Gold Soundtrack: Aztec Attack" (EsfIfrzhSFk, 4:03).
  - "Aztec attack (battle bears)" (-1zFjh2VMK8, 4:04).
- The track's musical character and the map's sound effects are [Unverified].

## Images viewed

[V] = `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/aztec_attack_verify/`

**Wiki files** (original format via `&format=original`):
- [V]img/Facingtemples.png (https://static.wikia.nocookie.net/battlebears/images/5/5c/Facingtemples.png/revision/latest?cb=20121127114134). Crops: [V]crops/td_top.png, td_mid.png, td_bot.png.
- [V]img/Facing_Temples_Development.png (https://static.wikia.nocookie.net/battlebears/images/d/d7/Facing_Temples_Development.png/revision/latest?cb=20121127092536).
- [V]img/IMG_0525.png (https://static.wikia.nocookie.net/battlebears/images/8/87/IMG_0525.PNG/revision/latest?cb=20121122154016). Crops: [V]crops/img0525_hp.png, img0525_top.png, img0525_base.png.
- [V]img/Maxres100.jpg (File:Maxresdefault(100).jpg, https://static.wikia.nocookie.net/battlebears/images/b/be/Maxresdefault%28100%29.jpg/revision/latest?cb=20130523030728; on the Shield page). Crops: [V]crops/mx_temple.png, mx_left.png, mx_right.png.
- [V]img/Aztec_Attack_tile.png (File:Aztec_Attack.png, 2013-06-15). Enlarged: [V]crops/tile_big.png.
- [V]img/Jump_Pad.jpg; [V]img/Uumhfc.jpg (enlarged: [V]crops/uumhfc_big.png).
- New: [V]img/Download16.jpg (File:Download_(16).jpg, 2013-04-21; enlarged: [V]crops/download16_big.png).
- New: [V]img/sofly_vid.img (2015 thumbnail of the wiki's "Battle Bears Huggable Gameplay So Fly" video) and [V]img/photo270413.png (not this map). Sheet: [V]crops/sofly_sheet.jpg.

**Steam trailer** (`/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/trailer.mp4`):
- Contact sheets of all 108 stored frames: [V]trailer/all_a.jpg, all_b.jpg.
- Full-resolution frames: [V]trailer/f_12.5.jpg, f_13.0.jpg, f_14.0.jpg, f_15.0.jpg, f_15.5.jpg, f_16.0.jpg, f_16.25.jpg, f_16.5.jpg, f_43.5.jpg, f_44.5.jpg, f_45.0.jpg, f_45.5.jpg.
- Sheets: [V]trailer/ground_mid.jpg, edges.jpg.
- Crops: [V]crops/a45_temple.png, a45_botleft.png, a43_left.png, a43_right.png, g125_gems.png.
- Not Aztec: [V]trailer/interior.jpg (f_39.0, f_39.6, f_40.6: a flesh interior).
- Timing check: the stored frames t_N show ≈(N−1)×0.5 + 0.23 s (pixel-matched). The Aztec cuts are at ≈12.25 s (in), ≈16.39 s (out to the Astoria card), ≈43.12 s (aerial in), and a crossfade out from ≈45.5 s.

**Steam screenshots:** [V]crops/steam_screens.jpg (screen_00–04). None shows Aztec Attack.

**YouTube thumbnails** (i.ytimg.com):
- Official overhauls: [V]crops/yt_official.jpg, [V]yt/q1Y8Siqfvn4_maxresdefault.jpg, [V]crops/astoria_hq3_big.png.
- 2013 launch trailer (rfAyqVJrli4): [V]crops/bbg2013_trailer.jpg.
- Fan, 2012–14: [V]crops/yt_fan.jpg (KhJEqrNgzo8, _b0dKkg0OPQ, oRG574AFi0o, LOa3e4GyrCk).
- 2026 playtests: [V]crops/yt_2026.jpg (no Aztec) and the chapter thumbnail [V]yt/qt43_ch_830900b.jpg (enlarged: [V]crops/qt43_ch_big.png).

## Prompt pack

**Base establishing shot (9:16, environment only)**

> Vertical 9:16 establishing shot of a night-time arena on a narrow plateau island in a sea of molten lava. Foreground: cracked, packed burnt-orange sand with a few grey-brown stone cubes carved with grimacing mask faces, and a loose row of free-standing square sandstone pillars with block capitals. Middle ground: a rounded-octagon pool of glowing lava, yellow-hot at its core and orange-red at the edges, holding one large faceted near-black boulder veined with dark red, with a glowing cyan circular pad on top; a line of smaller dark faceted stepping stones crosses the pool sideways through the boulder. Cyan circular pads glow on the sand at the pool's corners. On the left and right banks stand two small ruined sandstone pavilions: square pillars under a carved meander frieze, a heavy dark-grey carved roof slab, grey cobblestone plinths with ramps, and a crumbled hole in one wall. Background, filling the upper half: a massive stepped temple facing the camera. A broad lower staircase rises to a dark doorway framed by panels of rounded teal, rose and violet gemstones and big swirl reliefs; a steep upper staircase climbs a truncated-pyramid top to a small square summit. Warm sandstone walls, grey carved stone on every flat ledge, stepped-fret bands along the stair rails. Beyond the island's edges the lava sea glows to the horizon under low black-maroon hills. Sky: deep indigo at the top with small white stars, grading through plum and crimson to a raspberry glow at the horizon. Lighting: warm, saturated light thrown up from the lava, soft shadows; cyan pads and teal gems are the only cool accents. Chunky low-poly game-world forms with hand-painted textures and dark linework. No characters, no text, no logos.

- **Documented elements** [Observed: trailer 12.5 s, 43.5 s, 45.0 s; Maxresdefault(100).jpg; IMG_0525; map tile]: the island in a lava sea, the pool, rock and stepping stones, cyan pads, both ruins, the temple's two staircases, gem panels, swirls, fret bands, grey ledges, pillars, face cubes, and the starry gradient sky with hills.
- **Composition choices** [BBG News invention]: standing near one temple and looking across the pool at the other, much like the 2013 capture; placing the temple in the upper half.
- **Optional additions** [BBG News invention]: faint heat shimmer over the lava, or a few slow embers. No embers appear in any still.
- **Twin temple:** if the second temple is shown, it is a twin. One temple's gem panels glow red, the other's are teal and multicolour [Observed, 2013 footage]. Team mapping is [Inference].

**Spots where a short can stage a scene**

1. **The Grand Staircase.**
   - Lower stairs lead to the gem-framed dark doorway; steep upper stairs climb above it [Observed].
   - In the official trailer (2013 footage, ≈12.25–16.4 s), Astoria (the Sniper card follows) stands on the upper stairs below the doorway. A white-headed bear in black burns and collapses at the foot of the stairs, a magenta faceted cloud fills the stairs, and Astoria steps out of it [Observed].
   - Suits standoffs, dramatic descents or a "summoned to the temple" gag [BBG News invention].
2. **The obsidian rock in the lava pool.**
   - Reached by hopping the stepping stones; the Bearscream Sandwich spawns there and its two pads fling players toward a temple [Fan-wiki; pads Observed].
   - Suits a "floor is lava" race for the sandwich, or a duel on narrow footing [BBG News invention].
3. **The summit perch.**
   - Reached by the pad chain up the temple's back [Fan-wiki; Observed top-down]. A grey stone platform looks over the pool, the far temple and the lava sea [Observed: Astoria Overhaul hq3; Download_(16).jpg].
   - Suits overwatch scenes or a pad-chain launch gag [BBG News invention].
4. **Bonus: the ruined pavilions.**
   - Cover beside the pool, with a Shield inside (seen in the Tillman Overhaul thumbnail) [Observed; Fan-wiki].
   - Suits ambushes or a "who's behind the pillar" beat [BBG News invention].

## Confidence

**Observed** for look and layout. Eleven sources agree: the 2012 top-down, the 2012 BBR screenshot, the April 2013 BBR screenshot, the May 2013 capture, the 2013 map tile, the 2013 launch-trailer footage on Steam, two official overhaul thumbnails (about 2014), the 2015 thumbnail and the 2026 playtest thumbnail.
- **Documented:** history and name (the wiki's transcription of the update note, the wiki move log, SkyVu's 2013 URL slug, the 2026 OST track title).
- **Partial:**
  - the full look of the 2026 build (one thumbnail only, and a "Lighting improvements" note);
  - the official blurb (unread);
  - the temple symbols (wiki only, never seen);
  - the team-side mapping (inference);
  - the jump-pad count (12 per the wiki vs 14 markers);
  - the music's character and composer;
  - the launch roster.

---

## Corrections to our notes

1. **`/home/user/thallo-site/research_notes/Battle Bears character lore/animation_reference.md`, Q1 §B "Art style as seen in official frames", the in-game 3D look entry under "In-game 3D and logo" (formerly line 150). Applied: that entry now names the Aztec Attack lava and the Marecraft flesh interior.**
   - Text at the time: "(Steam screenshots and the Steam trailer; the lava caverns are from the trailer) … there are lava/orange caverns and rocky caves".
   - Correction: the trailer has no lava cavern.
     - Its lava is the open-air Aztec Attack map: a plateau island in a lava sea under a starry crimson-to-indigo sky (≈12.25–16.4 s and ≈43.1–45.7 s).
     - The enclosed red-orange space at ≈38.5–41 s is a flesh interior with vein-lined walls and rib columns, probably Marecraft [Inference].
     - The Steam trailer re-edits the May 2013 launch trailer, so it shows the 2013 look, not the 2026 build [Inference, strong].
2. **Same file, Fact-check log, "Corrected" item 17 (formerly line 667)** ("The lava caverns are attributed to the trailer, not the screenshots."). Same fix. Applied: that sub-bullet now says the lava-caverns fix was superseded on 2026-10-18.
3. **`franchise_world.md`, line 225** ("**Aztec Attack**: temple carvings of O.C.O. and Astoria.").
   - Use the wiki's hedged wording: "One temple has a symbol representing Over Clocked Oliver, while the other has a symbol representing Astoria" (Aztec page, added 2013-07-06), and "there seems to be a carving of Over Clocked Oliver, along with Astoria. Both are located at each team's spawn points" (OCO page).
   - Add that no image from 2012–2026 shows them.
4. **`research_notes/BBG weapons (verified)/combat-vfx.md`, line 779**, plus the same line in combat-vfx.meta.json (line 228), the unverified draft visuals_combat-vfx.md (line 463) and the scratchpad weapons draft.
   - "Lava borders the Aztec maps [Observed: trailer 43.5–46 s; Maxresdefault(100).png]" → "Lava surrounds the Aztec Attack map (one map) [Observed: trailer ≈43.1–45.7 s, 2013 footage; File:Maxresdefault(100).jpg]".
5. **`research_notes/BBG weapons (verified)/oliver.md`, line 240** ("On the lava map (about 38.0–41.5 s)"), and the unverified visuals_oliver.md, line 186.
   - That shot is the flesh interior (probably Marecraft), not a lava map.
6. **`research_notes/BBG weapons (verified)/2026.md`, line 138** ("38.6–41.0 s, lava cave").
   - Change to: "38.5–41 s, Marecraft-style flesh interior (not lava) [ID Inference]".
7. **Unverified weapons draft `visuals_combat-vfx.md`, line 77** (repo and scratchpad copies): "The body is still there at 14.9 s, when the shot ends".
   - The Aztec shot runs to ≈16.4 s, and the body is visible at 15.5 s. The verified combat-vfx.md already has the fix.
8. **This dossier's earlier draft** (`research_notes/BBG maps (unverified drafts)/research_aztec-attack.md`, identical to the scratchpad draft) needs four fixes:
   - Line 72: "mirror-symmetric" becomes point-symmetric.
   - Line 54 and the other "2026 trailer" mentions: the footage is from 2013, and the brighter look dates from the 2013 relaunch, not the 3.0 lighting pass.
   - Line 46: there is no numbering conflict.
   - Line 84: "summit shrine with a pyramidal roof cap" becomes a truncated-pyramid upper tier with stairs up to a square summit.

The lore report (lines 53 and 91) and characters/oliver.md (line 35) and astoria.md (line 32) label the temple symbols correctly as wiki claims; no change is needed. astoria_graham_tillman.md (line 153) quotes the wiki exactly.

## Open questions

- What does SkyVu's 2013 page (Wayback snapshot 20130815053638 of battlebears.com/games/battle-bears-royale/maps/aztec-attack/) say? The snapshot exists but web.archive.org is unreachable.
- Do the wiki-claimed Over Clocked Oliver and Astoria symbols exist at the spawns inside the temples? No interior image has been found.
- Is red = the red-glowing temple and blue = the teal temple, in BBG and in 2026?
- Is the jump-pad count 12 (wiki) or 14 (markers on the 2012 top-down)?
- What is the glowing square on each temple summit in the top-down?
- How does the 2026 build look after BBG 3.0's "New Map Lighting" and the Oct 2026 "Lighting improvements"? Which modes run on Aztec Attack at launch?
- Which composer wrote "Aztec Attack", and what does it sound like?
- What are the dates and contents of the "Astoria Overhaul" and "Tillman Overhaul" videos? The Tillman (Demo) one is probably about June 2014.
- Does Aztec Attack appear in BB Heroes (2024)?
- Lead for the bible: the 2026 OST lists 15 BBG map tracks (including "Huggable Factory") plus "Castle Royale". Compare that with "16 wacky maps" and the new Sky World / "Sky Pirates" map.