# Skate or Die

Skate or Die is a Battle Bears Gold map. It is a sunny, walled concrete skatepark built under two elevated highway decks. Its walls, piers and floor are covered in Battle Bears graffiti. The main features are:
- dry concrete bowls painted to look like water, one with a painted leaping goldfish;
- plywood kickers and fun-boxes with rust-orange rails, and long black steel ledges;
- a giant grey camera with a glowing blue lens beside an "ABBi" tag;
- a pink bone-limbed Huggable mural beside a pillar tagged "Oops, Killed ya!";
- a "BATTLE BEARS" mural that the wiki says is the Battle Bears TV show.

SkyVu named it as one of "3 New Maps" for the BBG launch in its May 30, 2013 trailer description. The 2026 Steam page does not name it, but it is track 7 on the official 2026 soundtrack. It appears in two official shorts, one from 2025 and one from 2026. Fan footage shows it being played in the July and August 2026 PC playtests.

**What I could reach:**
- **Fan wiki, through its API:**
  - the Skate or Die page and its full edit history (31 revisions, 2013–2015);
  - all 5 gallery images, the map-select icon, and the May 2013 "New map.jpeg" photo the page used before release;
  - the related pages: BBG Maps, Battle Bears Gold, Battle Bears Gold/Versions, Updates, Bearscream Sandwich, Imperial Basket Grande, Health Pack, Shield, Sky View, Shortest Parsec, Toxic Terror, Tillman, Plant the Bomb, King of the Windmill, Pick-Ups, Battle Bears TV and "News: Battle Bears goes to Hollywood";
  - the 2013 trailer's stored YouTube metadata.
- **Steam:** the store API for app 4408320, the soundtrack page for app 5321720, and the news API (all fetched 2026-10-16).
- **Official media:** the local Steam trailer, from which I extracted my own 5 fps frames for 45–48 s, and the five Steam screenshots.
- **YouTube:** oEmbed data and thumbnails for official and fan videos, plus the page for the official short "Dangerous Skate Parks". I watched no videos.
- **battlebears.com (live):** a search for "skate" returns 0 results, and /pages/maps returns 404.

**What I could not reach:**
- **web.archive.org:** every connection was reset, and WebFetch is blocked for that host. archive.org's availability API answered twice before rate-limiting me. It has no snapshot of a SkyVu map page at `battlebears.com/games/battle-bears-royale/maps/skate-or-die/`, the URL pattern of the older SkyVu map pages.
- **YouTube watch pages** (HTTP 429) and the player API (LOGIN_REQUIRED).

Local evidence folder: `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/skate_or_die/` (short names used below are mapped to full paths in "Images viewed").

---

## Official text

- **2013 launch trailer description.** The video is "BATTLE BEARS GOLD Trailer: Award-Winning Multiplayer Shooter Game" (YouTube rfAyqVJrli4, published 2013-05-30 21:04 UTC, 69 s). I read the description from the YouTube metadata the wiki stores (File:BATTLE BEARS GOLD Trailer Award-Winning Multiplayer Shooter Game):
  - "3 New Maps: -Gold Digger -Skate or Die -Sky View" [Canon]
  - "HD Graphics (Only available on higher end devices. App automatically detects what graphic mode to show)" [Canon]
  - "Coming June 2013!" [Canon]
- **BBR 1.4.3 release notes (April 15, 2013), as the wiki quotes them:** "Coming soon to Battle Bears!!<br />★ NEW Character Class- the B-1000! A robot made to kill.<br />★ 3 NEW maps!" [Game text via wiki] (wiki Updates page).
- **2026 Steam store (read live 2026-10-16):**
  - "…compete with friends across 16 wacky maps." [Canon]
  - "Iconic Maps will return so prepare to jump back into classics such as No Bears Land, Gold Digger and Space Oddity." Skate or Die is not named anywhere on the page [Canon].
  - Modes: "-Team Deathmatch (TDM) -Free for All (FFA) -Plant the Bomb (PTB)" [Canon]
- **Official soundtrack** (BATTLE BEARS GOLD Soundtrack, app 5321720, "Nov 4, 2026"): the track listing reads "7 | Skate Or Die | 1:29" [Canon]. The credits are "Original Score: Rob Ruiz, AnDrue Humphreys, and Benjamin Vavak" [Canon]. They are not given per track.
- **Official shorts on the BATTLE BEARS channel** (titles and channel confirmed by oEmbed):
  - **"Dangerous Skate Parks"** (y5ThaIm-MYU), published "May 7, 2025" according to the shorts page [Canon].
    - Its frames read "TOP 3 DEADLIEST SKATE PARKS" (oar1) and "RAMP 1 UNITED KINGDOM" (oar2).
    - Over BBG gameplay of this map they read "SKATE OR DIE" and "BATTLE BEARS GOLD", with a map-pin icon (oar3) [Observed].
  - **"BBG Maps Ranked part 1"** (jkv6FHPghx8) [Canon title]. Its 4×4 grid of 16 map stills includes Skate or Die at row 4, column 1 (crop `jk_sodtile`) [Observed].
- **In-map text I read in official 2013 images:**
  - "Oops, Killed ya!" in red on a pillar (wiki `sod4`; trailer t_0094–t_0095) [Observed];
  - "ABBi" in blue-teal letters [Observed];
  - "B-1000" in red on a pillar with a heart (wiki `sod1`, `sod2`) [Observed];
  - "BATTLE BEARS." on a billboard (wiki `sod3`) [Observed];
  - "SKATE OR DIE" in orange-yellow block letters on the map-select icon (`icon`) [Observed].
- **No SkyVu map blurb found.** The older maps have archived SkyVu descriptions. I found no snapshot for a Skate or Die page, and battlebears.com search returns "0 results" for "skate" [Unverified whether one ever existed].

## Era and status

- **Not a BBR (2012) map.** BBR 1.4.3 (April 15, 2013) promised "★ 3 NEW maps!" as coming soon [Game text via wiki]. The trailer later names the three [Canon].
- **Before release:**
  - A photo was uploaded to the wiki on 2013-05-10 as "File:New map.jpeg" (uploader Galli8, no source given) [Fan-wiki file data]. It shows a MacBook running the Unity editor, with this map in both the Scene and Game views. The Game view shows a 1:57 match timer, the "BATTLE BEARS" billboard, wooden ramps and the overpass [Observed: `new_map`, `newmap_screen`].
  - Who took the photo is [Unverified]. A SkyVu social-media teaser is likely [Inference].
  - The wiki page was created 2013-05-25 as "Skate or die is a upcoming map in [[Battle Bears: Gold]]", using that photo [Fan-wiki, revision 38143/38430].
- **Added at the BBG launch, 2013:**
  - The wiki dates BBG 1.0 to May 24, 2013, the "Migration from Battle Bears Royale to Battle Bears Gold" [Fan-wiki].
  - The trailer published May 30, 2013 lists it among "3 New Maps" [Canon].
  - The wiki's gallery screenshots were uploaded June 10, 2013 [Fan-wiki file data].
  - The wiki's Sky View page says the three maps came "on the 2.0 update" [Fan-wiki]. But the wiki's version table runs 1.0 → 1.0.1 → 1.0.2 → 2.1 with no 2.0 [Fan-wiki]. "2.0" probably means the launch build [Inference]; this is unresolved.
- **Name and spelling:**
  - SkyVu writes "Skate or Die" in the trailer, "Skate Or Die" on the soundtrack, and "SKATE OR DIE" on the icon [Canon/Observed].
  - The wiki page moved between those spellings three times in 2013 [Fan-wiki].
- **Modes, 2013–2021:**
  - **Team Battle:** default [Fan-wiki].
  - **Plant the Bomb:** the wiki says PtB "takes place in the same stages as Team Battle" [Fan-wiki]. Where the bombs and tubes sit on this map is [Unverified].
  - **Free-For-All:** added in v2.5 (November 27, 2013) [Fan-wiki]. A fan upload titled "Battle Bears Gold 2.5 Skate or Die B-1000 FFA -- Bearail Gun/Energy Barrier Gameplay" (q77eEbDzOiY, published Dec 8, 2013) shows FFA on this map. Its thumbnails show this map [Observed]; the mode comes from the title [Inference].
  - **King of the Windmill:** "added in version 2.8 and removed in version 2.29" [Fan-wiki]. Whether it ran here is unknown [Unverified].
- **Changes over time:**
  - No map-specific rework is documented [Unverified].
  - v3.0 (November 15, 2021) lists "New Map Lighting" for the whole game [Game text via wiki].
  - The wiki says servers "shut down since March 12, 2024" [Fan-wiki].
  - A June 16, 2013 edit mentioned "an area which looks like a trench where players can hide". It was removed the next day [Fan-wiki, revisions 42808→43031], so it is not evidence of a rework.
- **2026 re-release:**
  - The Steam text does not name the map [Canon].
  - The soundtrack has its own track [Canon].
  - SkyVu's official shorts show it in 2025 ("Dangerous Skate Parks") and 2026 ("BBG Maps Ranked part 1", a 16-map grid matching "16 wacky maps") [Observed; the count match is Inference].
  - Fan footage puts it in the 2026 playtest builds:
    - InstableGR, "Battle Bears Gold - PC Playtest #2 w/ New Mode (7/29/26)" (lFr8-yHbbzQ), has the chapter "Match 7 (Team Battle, Skate or Die, Botch)" at 26:03 [Observed chapter text in YouTube data]. Its chapter thumbnail shows this map: the billboard, concrete walls, a black ledge, the TV mural and a wooden ramp, with Botch in the foreground and a 0–0 score (`lFr8_ch7_3x`) [Observed].
    - JustNubz, "Battle Bears Gold Playtest #3 Part 2" (_R4rvvGlRsM), lists "14:04 Skate or Die FFA" in its description [Observed snippet]. Its hq3 frame shows the painted pool and goldfish, the meadow mural and the billboard under a blue sky (`R4r_hq3_3x`) [Observed].
    - The same video's menu frame shows a "3.0.2" version stamp [Observed].
  - **Conclusion:** the map is in the 2026 build and was played in Team Battle and FFA in playtests [Inference, strong].
  - Steam news (7 posts, Feb–Oct 2026) never mentions it [Canon]. The final playtest (October 15, 2026) lists "Lighting improvements" [Canon], so 2026 lighting may differ in detail from 2013 [Inference].
- **The Steam trailer is probably 2013 footage.** Earlier work showed the 2026 trailer reuses the 2013 character cards [per Gold Digger draft]. This map's segment has no HUD [Observed], and its overhead camera matches the framing in the 2025 official short [Observed]. Both probably come from the same 2013-era capture [Inference].
- **Battle Bears Heroes (2024):** no evidence it appears there [Unverified].

## Setting

- **What the wiki says:**
  - "It is a skating park below two highways and there is plenty of graffiti and other things from all of the Battle Bears series." [Fan-wiki]
  - "Skate or Die is a map that appears to be based on a skating park (also because of the name), and has a very wide and open area, much like No Bear's Land." [Fan-wiki]
- **What the images show:**
  - An open-air plaza enclosed by tall board-formed concrete walls with rows of tie-holes and panel seams [Observed: `sod1`–`sod4`].
  - Two elevated concrete highway decks cross overhead at different heights. They curve and rest on massive T-shaped (hammerhead) piers that stand inside the play area (`sod2_deck`, `sod3`) [Observed].
  - Above the walls there is only sky, a "BATTLE BEARS." billboard on a pole, and another billboard on posts (`sod3`, `sod1`) [Observed].
- **Where it sits in the Battle Bears world:** not documented [Unverified]. The setting reads as an Earth-like urban underpass skatepark [Inference].
- **The name:** a pun on the skater slogan "skate or die" [Inference].
- **How SkyVu framed it in 2025:** ranked against real parks in "TOP 3 DEADLIEST SKATE PARKS", next to Ramp 1, United Kingdom [Observed]. Its rank is not visible in the thumbnails [Unverified].

## Layout

- **Overall shape:** a large, roughly rectangular walled plaza, mostly at one level, with sunken bowls and raised decks and ramps [Observed: trailer overhead 45.5–47.5 s; `sod1`–`sod4`].
  - The wiki calls it large ("Due to its large size Snipers can be very effective, although cover is very abundant and useful for breaking locks") and "very wide and open" [Fan-wiki].
- **Overhead view in the Steam trailer (≈45.5–47.5 s, clearest 46.0–46.8 s; t_0093/t_0094, `s_05`, `s_09`, `s_11`)** [Observed]:
  - **A long, irregular, river-shaped bowl** runs diagonally down one side. Its floor is painted pale aqua with white foam, and a painted orange goldfish leaps with a white splash. It has steel coping and a wooden-faced bank along its far edge.
  - **A smaller angular bowl**, also painted as water, sits near the camera corner.
  - **A central pier** stands in the middle. At its base is a black steel box with a stepped ramp. A small white box-shaped pickup with an orange glow sits on top (`tr_pickup`).
  - **Street-course props:** a honey-coloured plywood kicker / fun-box with a rust-orange rail, a long black open-topped steel ledge, short orange flat rails, and three short black ledges in a row by the back wall.
  - **The far corner** holds the giant ABBi camera and the "ABBi" tag. The rainbow-and-skull ledge and the "Oops, Killed ya!" pillar are to the right, and the pink Huggable mural is on the right-hand wall.
  - **The opposite corner** has the green meadow mural with wooden-faced banks and a wooden wedge ramp.
- **From the ground (wiki gallery and fan thumbnails)** [Observed]:
  - **A wooden quarter/half-pipe** with orange coping in a corner (`sod3`, `sod3_right`).
  - **A wide raised wooden platform** on chunky wooden box legs that you can walk under (flythrough hq3, `vLNA_hq3_3x`).
  - **Concrete stairs with steel handrails** up to a raised level in front of a wall of pasted posters (`sod2`, flythrough hq3).
  - **Concrete banks, hips and humps**, one with a drain grate (trailer `s_06`).
  - **An octagonal, bolted steel pipe mouth** with a rusty orange interior. It is set into a concrete hump at the edge of the painted bowl (`sod2_hatch`). The wiki mentions "many bridges, tunnels and hills" [Fan-wiki]. This pipe is one such tunnel [Inference].
- **Central high point:** the wiki describes "a large hill near the center of the map containing a health pack on top" [Fan-wiki]. Its pickup list puts a Health Pack "on the large spire directly in the middle of the map, facing the Red team's side" [Fan-wiki], and the Health Pack page says "On top of the central ramp" [Fan-wiki]. The pickup on the black box at the central pier in the trailer is probably that Health Pack [Inference].
- **Verticality:**
  - There are three levels: sunken bowls, the main floor, and raised platforms and the half-pipe [Observed].
  - The highway decks are scenery above the play space. No source shows players on them [Unverified].
  - There are no jump pads: the BBG Maps page lists "Skate or Die, Sky View, and Toxic Terror are the only maps that contain no Jump Pads" [Fan-wiki].
  - The map page contradicts itself, calling it "one of the only two maps without Jump Pads, the other being Sky View" and also "one of the 3 maps" with Toxic Terror [Fan-wiki].
- **Teams and spawns:**
  - "The two team's spawn points are very large on this map, extending almost the width of the map." [Fan-wiki]
  - **Red side** has "the large 'pool'" (a Shield is in it), a "large raised half-pipe at the corner of the map, on the Red team's left side" (Bearscream Sandwich), and "the large raised platform, closer to the Red team's side" (Imperial Basket Grande) [Fan-wiki].
  - **Blue side** has "a huge column" (a Shield behind it), "a curved ramp" (Imperial Basket Grande), and "a ramp on the left side of the Blue team's side leading up to the large raised platform" (Bearscream Sandwich) [Fan-wiki].
  - The Bearscream page adds that on Skate Or Die the two sandwiches "are placed at opposite ends of the map with a huge open space in between" [Fan-wiki].
  - With both sandwiches on each team's left, the layout is probably rotationally rather than mirror symmetric, and imperfectly so, since the big pool is on Red's side only [Inference].
  - Which landmark (pool, camera corner, half-pipe) faces which team on screen is [Unverified].
- **Full pickup list:** the wiki lists Bearscream Sandwich ×2, Imperial Basket Grande ×2, Health Pack ×2 and Shield ×2 [Fan-wiki]. It calls the pickups "excessive" and the map "one of the two maps that have two Bearscream Sandwiches, along with the Shortest Parsec" [Fan-wiki].

## Look

- **Time of day and sky:**
  - Clear, cloudless daylight [Observed].
  - In the 2013 images the sky runs from cornflower blue at the zenith to a pale peach-lavender haze at the horizon [Observed: `sod2`, `sod3`, flythrough hq1].
  - Sunlit concrete is warm cream-beige, and the overpass decks and piers cast long, hard shadows across the floor [Observed].
  - This reads as late afternoon [Inference].
  - The low-res 2026 playtest thumbnails show the same daylight look with a strong blue sky [Observed]. Finer lighting changes can't be judged at that size [Unverified].
- **The 2013 trailer is warmer and more saturated** than the 640×400 wiki screenshots: brighter orange wood and warmer floor [Observed]. This probably reflects the "HD Graphics" mode or the trailer's grade [Inference].
- **Materials** [Observed]:
  - board-formed concrete walls with tie-holes;
  - large square concrete paving slabs, scuffed and spray-stained;
  - smooth concrete bowls with steel coping, their floors painted as water;
  - light honey plywood ramps with visible grain and steel kick-plates;
  - black-painted steel ledges and boxes with bright steel edges;
  - rust-orange grind rails;
  - a rusty bolted steel pipe ring;
  - dark charcoal overpass concrete.
- **Weather and particles:** none seen. The only clouds are painted ones in murals [Observed].

**Palette.** These are approximate hex values I sampled with a script from the images named in each row. The wiki images are 640×400 WebP re-encodes.

| Element | Hex | Source |
|---|---|---|
| Sky, zenith | #5776B1 (2013 wiki); #76A9D3 (2013 fan flythrough) | `sod2`; `vLNAENqXIf8_hq1` |
| Sky, horizon haze | #EADFDC pale peach; #B7BECF lavender-grey | `sod3`; flythrough hq1 |
| Sunlit concrete wall | #E4C9B1 (highlight #F8E4C6) | `sod2` |
| Shaded concrete wall | #5D555E | `sod1` |
| Sunlit floor / ramp concrete | #806F62 – #9C8879; trailer #92796D | `sod4`, `sod2`, `s_09` |
| Floor in shadow | #363034 – #443D42 | `sod1`, `sod3` |
| Overpass underside, piers | #302B2D – #3A3437 | `sod2`, `sod1` |
| Plywood ramps | #644326 – #6C4C2D (wiki); trailer sunlit #FD994B, highlight #FFD66B | `sod1`, `sod3`, `s_09` |
| Grind rails (rust) | #59311E | `sod3` |
| Black steel ledges / box | #181618 | `sod1` |
| Painted "water" bowls | #B5DADD – #BCEBEF (wiki); trailer #2F5069 with #8EC5D2 highlights | `sod2`; `s_09` |
| Meadow mural grass / sky | #367C04 – #419A02 / #408FA8 | `sod1`, `sod3` |
| Pink Huggable graffiti | #934578 (wiki); #EA7197 (trailer) | `sod4`; `s_11` |
| Rainbow (dominant orange band) | #CD6932; trailer #E97649 | `sod4`; `s_11` |
| Skull outline green | #75C355 | `sod4` |
| "ABBi" letters | #4C808C | `sod4` |
| "Oops, Killed ya!" red | #B1504A | `sod4` |
| ABBi lens | #246280 deep blue around a near-white cyan core | `s_05` |
| TV mural teal / magenta | #3F6E86 / #A13372 | `tvgraffiti` |

**Signature set dressing** [Observed unless marked]:
- **Graffiti murals and tags** on almost every wall, pier and bank. These are listed under Landmarks and Easter eggs.
- **Floor graffiti:**
  - a blue spray splat;
  - a white cloud with blue drips;
  - a cream bear-head stencil;
  - a purple-and-blue leopard-print arrow tag;
  - pink and orange scribbles (`sod2_floor`, `s_06`).
- **A wall of dense, many-coloured tags** with a large looping black scrawl (flythrough hq2 / maxresdefault).
- **A 3×4 grid of wheat-paste posters** of a pale figure on dark pink-and-black posters (`sod2_posters`, flythrough hq3). The subject is unidentified.
- **An orange kite graffito** with a trailing string (`sod3_right`).

## Landmarks

1. **The overpass.** Two crossing elevated highway decks on hammerhead piers frame the whole park and throw big shadows [Observed: `sod2_deck`, `sod3`; Fan-wiki "below two highways"].
2. **The painted pools.** Dry concrete bowls are painted pale aqua to look like water, one with a leaping orange goldfish and a white splash. Characters run across them, so they are solid floor [Observed: trailer 46.0–46.8 s; `sod1`, `sod2`; 2026 `R4r_hq3_3x`].
3. **ABBi's camera.** A giant grey cylindrical camera body juts from a corner with a big glowing blue lens. Beside it is the tag "ABBi", and a thick dark cable snakes away along the walls [Observed: trailer `s_05`/`tr_lens`; flythrough `vLNA_hq1_3x`; official grid tile `jk_sodtile`; `sod4` shows the cable].
   - It is ABBi's single camera eye [Inference]. The wiki says ABBi "has a single camera for an eye" [Fan-wiki, per our notes].
4. **The "Oops, Killed ya!" pillar and the bone-limbed Huggable.** A large pink Huggable graffito has a stitched body, a gaping mouth, one bulging eye, and one arm and one leg that are bare bones. It is sprayed beside a pier tagged in red "Oops, Killed ya!". This pairing is the map-select icon [Observed: `sod4`, `icon`, trailer t_0094–t_0095, official short oar3].
5. **The "BATTLE BEARS" TV mural.** Distressed black "BATTLE BEARS" lettering sits over teal and magenta spray, with a scowling brown bear, a yellow bear and a goggled bear face [Observed: `tvgraffiti`, `sod3_right`, 2026 `lFr8_ch7_3x`]. The wiki captions it "Battle Bears TV show in the map" [Fan-wiki].
6. **The "BATTLE BEARS." billboard** on a pole above the wall. It shows Oliver, a rainbow and a pink Huggable head [Observed: `sod3_billboard`, `new_map`, 2026 `lFr8_ch7_3x`].
   - Also seen: the green meadow mural with tiny pink Huggables, and the rainbow trail ending in a green-outlined skull and crossbones [Observed].

## Hazards and interactive elements

- **No environmental hazards** are documented [Unverified], and none are visible in any image: no pits, water, traps or moving vehicles [Observed]. The "water" is paint [Observed].
- **No jump pads** [Fan-wiki].
- **Pickups:** two each of Bearscream Sandwich, Imperial Basket Grande, Health Pack and Shield [Fan-wiki]. Positions are under Layout.
  - The trailer and the 2013 flythrough show a small white box-shaped pickup with an orange glow on and near the central black box (`tr_pickup`, `vLNA_hq1_3x`) [Observed]. Which pickup it is: probably the Health Pack [Inference].
- **Skating:** the ramps, rails and ledges are terrain and cover. No skate or grind mechanic is documented [Unverified].
- **Cover and sightlines:** "cover is very abundant and useful for breaking locks", and snipers are strong because of the map's size [Fan-wiki].
- **Plant the Bomb and King of the Windmill:** bomb platform and tube positions, and windmill landing spots, are [Unverified].
- **Unidentified glow:** a white glowing octagonal outline appears on the floor at the bottom of the trailer overhead at 46.0 s (`s_06`) [Observed]. It is probably a weapon or effect ring, not map geometry [Inference; Unverified].

## Easter eggs and references

- **The Battle Bears TV series.** The wiki captions the mural "Battle Bears TV show in the map" [Fan-wiki].
  - SkyVu announced the W!LDBRAIN TV deal on October 4, 2012 [Fan-wiki page "News: Battle Bears goes to Hollywood"; official letter per our franchise notes].
  - The mural repeats the 2012 "THE TELEVISION SERIES / COMING SOON!" poster: the same distressed black "BATTLE BEARS" lettering over a teal glow with pink accents [Observed comparison: `tvgraffiti` vs `bbtv_coming_soon`].
  - The figures are probably Oliver (brown, scowling), Wil (yellow) and Graham (goggles), as on the TV banner [Inference; `bbtv_banner`].
- **"Oops, Killed ya!"** is the wiki's signature kill line for Oliver: "Oops, killed ya!" [Fan-wiki, Template:Class:Soldier_(BBG) per our notes]. Here it is painted as graffiti [Observed].
- **ABBi:** the "ABBi" tag plus the giant camera eye [Observed; identity Inference].
- **"B-1000"** is written in red under a red heart and a blue tag on a pier (`sod1_left`, `sod2_pillar`) [Observed]. The B-1000 was the new class launched with BBG and this map [Canon: trailer description].
- **The wiki's list of characters drawn on the walls:** "Oliver, Wil, Tillman, Riggs, ABBi, and Huggables" [Fan-wiki].
  - I can confirm Oliver (billboard, mural), ABBi and Huggables [Observed].
  - A black-and-white panda-like figure on a wall (`tr_panda`, `sod3_right`) may be Tillman [Inference].
  - A grey boxy robot head with a strap, in front of a yellow-green explosion (`sod1_robot`), is unidentified [Unverified].
  - I did not identify Riggs [Unverified].
- **The rainbow ending in a skull:** possibly a nod to the Huggables' rainbow blood [Inference].
- **Toxic Terror** repeats the idea: "Like Skate or Die, there are many drawings on the walls." [Fan-wiki]

## Sound and music

- The official 2026 soundtrack lists "Skate Or Die", 1:29, as track 7 [Canon].
  - It is the longest of the 15 BBG map loops before track 16. Only "Castle Royale" (1:56) is longer [Inference from the Canon durations].
  - Which of the three composers wrote it is not stated [Unverified].
- Fan uploads exist ("Skate or Die Flythrough and Music Track", CheeseclanBBG, 2013; several soundtrack rips) [Observed titles]. I listened to none, so the track's style is [Unverified].

## Images viewed

Base folder: `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/skate_or_die/`

**Wiki images** (converted from WebP):
- `sod1`–`sod4`: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/skate_or_die/conv/sod1.png, sod2.png, sod3.png, sod4.png (File:Skate or Die 1–4.jpg)
- `tvgraffiti`: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/skate_or_die/conv/tvgraffiti.png (File:BB TV show graffiti on Skate Or Die.jpg)
- `icon`: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/skate_or_die/conv/icon.png (File:Skate Or Die.png, the map-select icon)
- `new_map`: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/skate_or_die/conv/new_map.png (File:New map.jpeg)
- `bbtv_coming_soon`, `bbtv_banner`: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/skate_or_die/conv/bbtv_coming_soon.png, bbtv_banner.png

**Crops**, all in /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/skate_or_die/crops/: sod1_wall.png, sod2_wall.png, sod3_wall.png, sod4_wall.png, sod1_robot.png, sod1_left.png, sod2_posters.png, sod2_pillar.png, sod2_floor.png, sod2_hatch.png, sod2_deck.png, sod3_billboard.png, sod3_right.png, newmap_screen.png, tr_lens.png, tr_pickup.png, tr_panda.png, jk_grid.png, jk_tier.png, jk_sodtile.png, lFr8_ch7_3x.png, R4r_hq3_3x.png, vLNA_hq1_3x.png, vLNA_hq3_3x.png

**Steam trailer:**
- Provided frames: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/trailer/t_0092.jpg, t_0093.jpg, t_0094.jpg, t_0095.jpg, t_0096.jpg (45.5–47.5 s).
- My 5 fps extraction (s_N = 45.0 + (N−1)×0.2 s, about ±0.2 s against the t_ frames): /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/skate_or_die/trailer/s_05.png, s_06.png, s_09.png, s_11.png, s_12.png, s_13.png, plus contact sheet /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/skate_or_die/trailer_sheet.png
- Whole-trailer contact sheets: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/aztec_attack/trailer_sheets/sheet_0.jpg–sheet_3.jpg
- Skate or Die appears only at ≈45.5–47.5 s. It crossfades in from Aztec Attack and out to a construction-site map of wooden planks and teal tarps.

**Steam screenshots:**
- Contact sheet of screen_00–04: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/skate_or_die/steam_sheet.png
- None of the five shows Skate or Die [Observed].

**YouTube thumbnails**, all in /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/skate_or_die/yt/:
- Official "Dangerous Skate Parks": y5ThaIm-MYU_oar1.jpg, y5ThaIm-MYU_oar2.jpg, y5ThaIm-MYU_oar3.jpg; sheet /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/skate_or_die/sheet_y5.png (hq1–3, maxres1–3).
- Official zsfXXbObBQs, _KGqe9GYhiI, 8SVeIeDHuhY and jkv6FHPghx8 oar1–3: sheet /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/skate_or_die/sheet_others.png. Only jkv6FHPghx8 shows this map.
- 2013 trailer rfAyqVJrli4 maxres1–3 and maxresdefault: sheet /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/skate_or_die/sheet_rfAy.png. Character cards only.
- Fan 2013 flythrough vLNAENqXIf8: sheet /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/skate_or_die/sheet_flythrough.png and vLNAENqXIf8_maxresdefault.jpg.
- Fan 2013 FFA q77eEbDzOiY: sheet /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/skate_or_die/sheet_q77.png.
- Fan 2026 playtest #3 _R4rvvGlRsM: sheet /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/skate_or_die/sheet_R4r.png and _R4rvvGlRsM_maxresdefault.jpg.
- Fan 2026 playtest #2 chapter thumbnail lFr8_ch7_signed.jpg (shown via the crop lFr8_ch7_3x.png).

## Prompt pack

**Establishing shot (9:16, environment only)**

> Vertical 9:16 wide establishing shot from a low angle at the lip of a dry concrete skate bowl.
>
> **Foreground:** the bowl's floor is painted pale aqua (#B5DADD) with white foam swirls to look like rippling water, and a painted orange goldfish leaps with a white splash. Steel coping runs along the rim.
>
> **Midground:** a sunlit concrete skate plaza of large square slabs. There is a honey-coloured plywood kicker and fun-box with a rust-orange grind rail, a long black open-topped steel ledge with bright steel edges, and short orange flat rails. A black steel box with a stepped ramp sits at the foot of a massive concrete hammerhead pier, with a small white pickup crate glowing orange on top.
>
> **Upper third:** the dark charcoal undersides of two elevated highway decks cross at different heights and curve away. They cut across a clear cornflower-blue sky (#5776B1) that fades to pale peach haze at the horizon.
>
> **Background:** tall board-formed concrete walls with rows of tie-holes, covered in bright spray-paint murals:
> - a green meadow with white clouds and tiny pink cartoon bears;
> - a rainbow trail ending in a green-outlined cartoon skull;
> - a large pink cartoon bear with bone limbs;
> - dense abstract multicolour tags.
>
> In one corner a giant grey cylindrical camera juts out with a glowing blue lens, a thick black cable snaking along the wall. A billboard on a pole rises above the wall.
>
> Warm, low sun with hard, long shadows from the decks. No people, no characters, no readable text, no logos.

Every element above is observed in official 2013 footage or the wiki screenshots [Observed]. The following details are inventions or inferences:
- The specific camera position and composition [BBG News invention].
- Making all graffiti letter-free, and leaving the billboard and the "ABBi" and "Oops" tags unreadable or blank, so a house style can add text later. In the game these are readable [BBG News invention].
- Late-afternoon sun [Inference].

**Staging spots for shorts**

1. **The Painted Pool.** The river-shaped bowl painted as water, with its goldfish. In the official footage characters run straight across it [Observed]. A bear "diving in" and face-planting on painted concrete is a natural gag [BBG News invention].
2. **ABBi's Eye corner.** The giant blue-lens camera and "ABBi" tag [Observed]. Stage it as surveillance: ABBi "watching" a sneaky play, or the lens glinting at the punchline [BBG News invention]. The camera turning or zooming is not documented [BBG News invention].
3. **"Oops, Killed ya!" pillar.** The pier tag next to the bone-limbed pink Huggable mural [Observed]. This is a natural spot for an Oliver kill or taunt beat, since the phrase is Oliver's line per the wiki [Fan-wiki; Inference]. Add the text in post if wanted.
4. **Under the overpass, King of the Box.** The central pier's black box and stepped ramp with the glowing pickup on top (the wiki's central Health Pack) [Observed; Inference]. Good for a scramble or standoff in the deck's shadow [BBG News invention].

## Confidence

**observed.** The look, materials, signature graffiti and main props come from official 2013 footage: the Steam trailer, the 2025 official short and the official 2026 grid. They are cross-checked against the 2013 wiki screenshots and the fan flythrough and gameplay thumbnails. Several things are only partly known:
- the full top-down layout and which side is Red or Blue;
- the 2026 lighting details;
- the identity of some graffiti figures;
- whether SkyVu ever wrote a map blurb.

---

## Corrections to our notes

1. **`research_notes/BBG weapons (unverified drafts)/visuals_2026.md`, line 105**
   - **Current text:** "| 43–53.5 s, aerial shots | Yellow tracer dots, a golden half-dome blast (47.0 s), pink laser lines, a yellow-orange cube blast with a white shock ring (50.5 s), a vertical yellow-orange cone, then orange octagonal ring shockwaves and white smoke (52.5–53.5 s). | none named |"
   - **Correction:** name the maps.
     - 43.0–45.5 s is Aztec Attack.
     - ≈45.5–47.5 s is Skate or Die: an overhead of the painted-water bowl, the wooden kicker, the black box at an overpass pier and the giant ABBi camera. The yellow tracer dots and the golden blasts at ≈46.0 s (kicker base) and ≈47.0–47.2 s (the large yellow half-dome at the pool edge) happen on Skate or Die.
     - From ≈47.5 s the construction-site map of wooden planks and teal tarps follows (probably Sky View, Inference).
     - Gold Digger is ≈51.9–54 s.
   - **Evidence:** trailer t_0093–t_0096 and my frames s_06 (46.0 s), s_12 (47.2 s) and s_13 (47.4 s crossfade).
2. **`bbg-news-repo/characters/wil.md`, line 53**
   - **Current text:** "- **ABBi:** a single camera eye [Fan-wiki] ([ABBi][wabbi]); probably the Zero teaser's one-eyed, minigun-armed unit [Observed; Inference]."
   - **Correction:** add an in-game BBG reference. Skate or Die has a giant grey cylindrical camera with a glowing blue lens and a trailing black cable, beside a graffiti tag reading "ABBi" [Observed]. Read as ABBi's eye [Inference]. It gives the colour (deep blue #246280 around a near-white cyan core) and the shape (round lens in a thick dark bezel on a grey cylinder).
   - **Evidence:** Steam trailer t_0093–t_0094 and s_05 (crop tr_lens.png); 2013 flythrough vLNAENqXIf8 hq1; official "BBG Maps Ranked part 1" grid tile (jk_sodtile.png); wiki Skate_or_Die_4.jpg.
3. **`bbg-news-repo/characters/oliver.md`, line 21**
   - **Current text:** "\"Oops, killed ya!\" · \"What's dead and eats my bullets? You! Ha ha ha!\""
   - **Correction:** note that SkyVu itself used the phrase in BBG. It is painted as graffiti, "Oops, Killed ya!", on a pier in Skate or Die, and it appears on the map-select icon [Observed]. The phrase is therefore SkyVu-authored in-game text. Its attribution as Oliver's voice line remains [Fan-wiki].
   - **Evidence:** wiki File:Skate_or_Die_4.jpg; File:Skate_Or_Die.png; Steam trailer t_0094–t_0095; official short y5ThaIm-MYU oar3.
4. **`research_notes/Battle Bears character lore/franchise_world.md`, line 216**
   - **Current text:** "- [FAN-WIKI] BBG stages: H.I.P. Test Lab, Space Oddity, No Bear's Land, Aztec Attack, Abusement Park, Marecraft, Shortest Parsec, Sky View, Gold Digger, Haunted Castle, Toxic Terror, Skate or Die, Desert Airmine, Frozen Pundra, plus Steam Yard Blues (v2.8)."
   - **Correction:** add era and status for Skate or Die:
     - one of three launch maps named in SkyVu's 2013 trailer description ("3 New Maps: -Gold Digger -Skate or Die -Sky View", published 2013-05-30) [Canon];
     - track 7 "Skate Or Die" (1:29) on the 2026 official soundtrack [Canon];
     - shown in the official shorts "Dangerous Skate Parks" (May 7, 2025) and "BBG Maps Ranked part 1" [Observed];
     - in the 2026 playtests per fan footage: Team Battle on 7/29/26 and FFA in Playtest #3 [Observed metadata and frames].
   - **Evidence:** the wiki-stored YouTube metadata for rfAyqVJrli4; the Steam app 5321720 track listing; the oEmbed-verified official shorts; lFr8-yHbbzQ chapter "Match 7 (Team Battle, Skate or Die, Botch)"; _R4rvvGlRsM description "14:04 Skate or Die FFA".
5. **`research_notes/Battle Bears character lore/oliver_riggs_wil.md`, line 224**
   - **Current text:** "- [WIKI] Battle Bears TV: a cartoon planned with WildBrain Entertainment for 2014, featuring Astoria, Oliver, Riggs, Graham, Wil and Tillman, set after BB Zero. It was \"presumably cancelled.\" It \"replaced the Battle Bears Movie.\""
   - **Correction:** add that the series left a trace in BBG. A Skate or Die mural reproduces the 2012 "THE TELEVISION SERIES / COMING SOON!" key-art lettering (distressed black "BATTLE BEARS" on a teal glow), with a brown, a yellow and a goggled bear [Observed]. The wiki captions it "Battle Bears TV show in the map" [Fan-wiki].
   - **Evidence:** wiki File:BB TV show graffiti on Skate Or Die.jpg compared with File:Battle-bears-tv-series-coming-soon.jpg and File:BBTV.jpg.

## Open questions

- Which team (Red or Blue) spawns on the painted-pool side versus the ABBi-camera side? The wiki's pickup list implies the pool is on Red's side, but no image ties a team colour to a landmark.
- Did SkyVu ever publish a battlebears.com map page or blurb for Skate or Die, as it did for the BBR maps? web.archive.org was unreachable, and availability lookups found no snapshot for the expected slug.
- What does the full top-down layout look like? Where are the half-pipe, the large raised platform, the "huge column" and the spawns relative to the trailer's overhead? A flythrough or the 2026 build would answer this.
- Who are the figures in the TV mural (Wil? Graham?) and in the grey robot-head graffito? Is the black-and-white figure Tillman? What is on the wheat-paste posters?
- Where are the Plant the Bomb platforms and tubes on this map, and is the map in the 2026 PTB rotation? 2026 fan evidence shows only Team Battle and FFA.
- How different is the 2026 lighting after v3.0's "New Map Lighting" and the October 2026 "Lighting improvements"?
- Who took the May 2013 "New map.jpeg" Unity photo (a SkyVu teaser?), and when was it first posted?
- Which composer wrote the "Skate Or Die" track, and what does it sound like? Not listened to.
- Did "Dangerous Skate Parks" rank Skate or Die #1? Only its title card, the Ramp 1 entry and the Skate or Die entry are visible in the thumbnails.
- Is the white box pickup on the central black box the Health Pack? What was the white glowing octagon on the floor at 46.0 s in the trailer?
- Is Skate or Die in Battle Bears Heroes (2024)? No evidence found.
