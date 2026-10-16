# Abusement Park

Abusement Park is a night-time carnival arena with a horror streak, walled in by cracked stone. A roller coaster ridden by grinning pink Huggables loops the whole perimeter, and the middle is packed with striped tents, booths, joke signs and teaser posters. It was added in Battle Bears Royale (BBR) update 1.3.2 in 2012 and stayed in Battle Bears Gold (BBG). The official 2026 Steam trailer shows its red base, and the official 2026 soundtrack lists "Abusement Park" as track 1.

**Sources I could reach:**
- Fan wiki through the MediaWiki API: the map page and its revision history, every image on the page, three more files found by a File-namespace search, the pickup and update pages, and BBR Version 1.3.2.
- Steam store API for BBG (app 4408320) and the official soundtrack page (app 5321720).
- Steam news API.
- The local Steam screenshots and the frames of the 54 s Steam trailer. I also extracted extra frames at 4 fps for 17.5–22.5 s.
- YouTube thumbnails only: official 2026 videos and fan gameplay uploads. I did not watch any video.
- battlebears.com live. It has no BBG map text.

**Sources I could not reach:** web.archive.org reset every connection. I made more than 25 attempts with backoff, by curl, curl over HTTP/1.1, the `id_` raw URL and wayback.archive.org, and WebFetch refused the host. The official SkyVu Abusement Park blurb, the Nov 2012 BBR maps list and the SkyVu blog therefore come only from our prior notes and are flagged that way. archive.ph returned 429.

---

## Official text

- **SkyVu 1.3.2 announcement banner.** The text reads exactly: "UPDATE 1.3.2" / "COMING SOON" / "- New Level: Abusement Park" / "- New Weapons: Soldier & Heavy Classes" / "- Pro-style HUD/Controls Layout" / "- main menu tips/announcements, store bundle deals, fixed many crashes, fixed skill rating, bug fixes, & more!"
  - [Observed] /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/abusement_park/conv/Update_1_3_2_coming_soon.png (wiki File:Update_1_3_2_coming_soon.jpeg).
  - The layout and art look like a SkyVu in-game or social banner, but the wiki gives no source [Inference].
  - The banner art is an overhead render of the map: the maroon big-top, green tents, striped booths and the coaster [Observed].
- **iOS 1.3.2 update notes**, as quoted on the wiki's Updates page: ">> iPhone 5 compatible! >> New Level: Abusement Park >> New weapons for Soldier and Heavy classes >> New HUD Layout with Ability to Revert >> Skill Rating Improved! >> Store Bundle Deals in Promos in Main Menu >> Many Bug & Crash Fixes", dated "August 24, 2012" [Game text via wiki] ([Updates](https://battlebears.fandom.com/wiki/Updates)).
- **iOS 1.3.4 update notes:** "Fixed Abusement Park Skybox / Fixed lower body Animations In Menus", dated "October 20, 2012" [Game text via wiki] (same page).
- **SkyVu map blurb**, as quoted in our notes: "child friendly games like 'Pump-A-Chump (Fulla' Lead)'… Fried Stick, now served on stick!… no less than 400,000 tickets will buy your freedom and ONLY ONE CAN LEAVE."
  - Label: [Canon per prior notes; not re-opened this session, so Unverified] ([archived 2013-06-21](https://web.archive.org/web/20130621012649/http://battlebears.com/games/battle-bears-royale/maps/abusement-park/)).
  - The quote is elided. The full text is still needed.
  - Every quoted phrase matches signage I saw in the map: "ONLY ONE CAN LEAVE", "PUMP-A-CHUMP / FULLA' LEAD", "Fried Stick on a Stick", and "EXIT / Only 400,000 Tix" (see Landmarks) [Observed].
- **BBR maps list, Nov 2012**, as quoted in our notes: "Haunted Castle, Abusement Park, Facing Temples, Battlefield Airpad, Desert Airmine, Huggable Factory, Spacecraft." [Canon per prior notes; Unverified this session] ([archived](https://web.archive.org/web/20121130022926/http://www.battlebears.com/games/battle-bears-royale/maps)).
- **2026 Steam OST** "BATTLE BEARS GOLD Soundtrack" (app 5321720, release "Nov 4, 2026"):
  - Track 1 is "Abusement Park 0:54" and track 22 is "Abusement Park (Full Version) 3:05" [Canon].
  - "The official BATTLE BEARS GOLD Soundtrack featuring original map and menu music by Rob Ruiz, AnDrue Humphreys, and Benjamin Vavak." No per-track credit is given [Canon] ([Steam](https://store.steampowered.com/app/5321720)).
- **2026 Steam BBG page:** "compete with friends across 16 wacky maps" and "Iconic Maps will return so prepare to jump back into classics such as No Bears Land, Gold Digger and Space Oddity." It does not name Abusement Park [Canon] ([Steam](https://store.steampowered.com/app/4408320)).

## Era and status

- **Pre-release, July 2012.**
  - File:NewLevelLights.png was uploaded to the wiki on 2012-07-21. It is a two-panel Unity-editor capture: a "Lightmap Display" panel with "Use Lightmaps / Shadow Distance / Show Probes / Show Cells" and a "Persp" view gizmo. One panel is an overhead of the map and the other is the "Jeepers Peepers" corridor [Observed].
  - So the map was being lit (lightmaps and light probes) about a month before release [Inference].
  - Where the image first appeared is unknown. A SkyVu blog post is likely [Unverified].
- **Added: BBR v1.3.2.**
  - The iOS notes are dated August 24, 2012 [Game text via wiki].
  - The wiki page was created at 2012-08-24T01:39Z as "A new stage added in the new update." [Fan-wiki] (page history).
  - Date caveat: those same notes say "iPhone 5 compatible!", but the iPhone 5 was only announced on September 12, 2012. Either the date or the notes may be conflated [Inference].
- **October 20, 2012:** the 1.3.4 update fixed the map's skybox [Game text via wiki].
- **BBG (relaunched May 24, 2013 per the wiki):** the map stayed in.
  - The wiki's BBG Maps list includes it [Fan-wiki].
  - A BBG-style map tile reads "ABUSEMENT PARK" (File:Abusement park.png, uploaded 2013-06-15, used on the wiki's BBG page) [Observed].
  - Screenshots with the BBG HUD were uploaded in Sep 2013 (HuggableCart) and Mar 2014 (Screenshot (509)) [Observed].
- **Modes:**
  - Team battle and Plant the Bomb are documented [Fan-wiki].
  - Free for All is backed only by fan video titles such as "Battle Bears Gold 2.5 Abusement Park Graham FFA" [Unverified].
- **Removed or reworked:** nothing is documented.
  - A Mini Me glitch that let players leave the map or pass through walls "has since been patched", although players "could still climb over the map" [Fan-wiki].
  - Pickup locations differ between wiki pages (see Hazards). That may reflect changes over time [Inference].
- **2026:**
  - The Steam text does not name the map [Canon].
  - The official Steam trailer shows its red base from about 17.75 s to 22.0 s (t_0037–t_0045 and my 4 fps frames ap_02–ap_19). Visible are the "[RED]" stencil wall, the salmon plank deck, yellow U-rails, the maroon-and-white striped tent, the coaster rail overhead, bunting and the twin blue posters [Observed]. The trailer does not say which build the footage came from [Unverified].
  - The 2026 OST opens with the map's theme [Canon].
  - In the 2026 teaser thumbnail, the "SAME" panel shows a red stencil and star on a grey stone wall above wood, which matches the red base [Observed] (https://i.ytimg.com/vi/d2ByJWrsoec/hq1.jpg). That it is this map is [Inference].
  - The Oct 15, 2026 final-playtest post lists "Lighting improvements" and "Jukebox" [Canon] ([Steam news](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1846651706674102)). The 2026 lighting may therefore differ from the 2012–14 captures below [Inference].
  - Overall, the map is very likely in the 2026 rotation [Inference]. No text confirms it.

## Setting

- The wiki describes it as "a horror-themed carnival" with "many circus tents in the middle", "the House of Mirrors, and a giant crate which reads 'CONDEMNED', and many advertisement posters" [Fan-wiki].
- The name is a pun on "Amusement Park" [Fan-wiki].
- What I saw: a run-down carnival at dusk or night, sealed inside tall cracked grey stone-block walls with no visible way out [Observed]. Its signs read "ONLY ONE CAN LEAVE", "[NO ENTRY]" and "CONDEMNED", and the only "EXIT" costs 400,000 tickets [Observed]. That fits the official joke that the park is a trap you cannot afford to leave [Canon per prior notes, Unverified] [Inference].
- No source gives a real-world or in-universe location [Unverified].

## Layout

- **Overall shape:** a roughly square arena enclosed by stone walls. An irregular closed roller-coaster loop runs around the whole perimeter on red-and-white striped pylons, above the play space [Observed] (top-down File:Abusement_Park.jpg; overview File:Abusement_Park.png).
- **Asymmetry:** "The stage is asymmetrical, like Desert Airmine" [Fan-wiki]. The earliest wiki revision says "the abusment park has no even spawns" [Fan-wiki].
- **Team bases:**
  - The top-down image has red spawn crosshairs on wooden decks in one corner (NW in that image) and blue crosshairs on a wooden deck in the diagonally opposite corner (SE) [Observed]. The image's compass orientation is arbitrary.
  - The red corner is lit warm salmon-orange and the blue corner cool blue-grey [Observed].
  - Each base also has a square marker in the opposite team's colour (a red pad with a blue dot, a blue pad with a red dot) [Observed]. These may be Plant the Bomb targets [Inference].
- **Red base:**
  - A raised plank deck edged with chunky yellow U-shaped railings, below cracked stone walls stencilled "[RED]" with red stars and paint drips [Observed] (trailer t_0037/t_0044; fan thumbnails 0n34M2VxJDE hq3, Fbm3TY_D5HE hq1).
  - The wiki says Blue can go "through the tunnel under the Red Team's base", where the "Not Wil's Candy Stash" sign is [Fan-wiki] (2012 revision).
- **Blue base:**
  - A paler, cool-lit plank deck with blue spray graffiti on the stone walls, next to wooden stairs and a blue-and-white tent with white sawtooth trim [Observed] (Screenshot (509); fan thumbnails 0n34M2VxJDE hq1, KsddBonDY88 hq3).
  - Red can go "around and go through the back side of the Blue Team's base or go straight and walk through/jump through the platform" [Fan-wiki].
- **Centre:**
  - The largest roof is a big square maroon-and-white striped tent next to the red side.
  - Beside it are three peaked pale-green striped tents.
  - Orange/yellow striped booths include the Mirrored House and the Pump-A-Chump shooting gallery.
  - An octagonal yellow-and-brown striped tent stands near the blue side [Observed]. This is probably the "gazebo-like structure" holding the Bearscream Sandwich, "right next to" Blue's spawn [Fan-wiki] [Inference].
- **Plant the Bomb:** "a player… will automatically see the bombs, both red and blue in front of the House of Mirrors" [Fan-wiki]. The top-down image shows a small red and a small blue icon side by side on the edge of a central yellow booth [Observed], probably the bomb spawn [Inference].
- **Routes and other features:**
  - "a narrow corridor between the Red and Blue Teams' spawn points" [Fan-wiki]. The top-down image shows a dark corridor through the south-centre with a rainbow-striped floor section [Observed].
  - "The narrow alley next to [the Bearscream gazebo] is a very good place to send explosive projectiles" [Fan-wiki].
  - Also mentioned: "the raised walkway opposite the Red team's spawn points", "the hole at the corner of the arena", "the bridge" near Blue's base, and "the 'exit' above a flight of steps" [Fan-wiki]. The exit is the yellow-and-black "EXIT" sign over a staircase [Observed] (NewLevelLights; c6qGpQ4zxVA hq1).
- **Verticality:**
  - Raised decks and walkways, a tunnel under the red base, stairs and jump pads [Fan-wiki][Observed].
  - The coaster runs overhead at roughly roof height. Players are seen standing on the track or walls only in glitch-style screenshots [Observed] (HuggableCart.png; 6PU2KP9ayN8 hq3). It is probably not normal play space [Inference].

Schematic traced from the top-down image. Orientation is arbitrary and positions are approximate [Observed]:
```
 +--------------------------- coaster loop on striped pylons ---------------------------+
 | RED SPAWN decks (warm)   [ MAROON/WHITE BIG SQUARE TENT ]        [orange pit/rubble] |
 | [RED] walls, U-rails                                                                |
 | [ long wooden deck/walkway ][ 3 green peaked tents ]   [ octagon striped "gazebo" ] |
 |  [orange/yellow   ]  [ yellow booth: red+blue icons on its edge ]          [crates] |
 |  [ striped tent   ]                                                                 |
 | [hazard-striped shutter]   [box]  | dark corridor |   [lane-marked    BLUE SPAWN    |
 | [ ramp -> pink-lit room]          | rainbow strip |    concrete]      deck (cool)   |
 +-------------------------------------------------------------------------------------+
```

## Look

- **Time of day and sky:**
  - Dusk turning to night. A deep plum sky sits over a band of dark blue-violet cumulus, with a dull maroon-red glow low on the horizon [Observed] (File:Abusement_Park.png; HuggableCart.png; IMG_0667).
  - SkyVu patched the skybox in 1.3.4 [Game text via wiki].
- **Lighting:**
  - Theatrical pools of light: warm salmon-orange on the red deck and cool blue-grey on the blue deck.
  - Lit marquees with round bulbs, a backlit lightning-bolt sign box, and a glowing yellow doorway.
  - Teal-glowing jump pads [Observed].
  - The lighting is baked (Unity lightmaps and probes) [Observed editor panel → Inference].
- **Materials:**
  - Cracked grey-mauve stone-block perimeter walls.
  - Wooden plank decks with bolt holes and orange-red paint or blood splats.
  - Grimy grey-olive asphalt.
  - Striped canvas tents.
  - Riveted metal arch signs.
  - Yellow-and-black hazard-striped pillars, shutters and barriers [Observed].
- **Set dressing:**
  - Red-and-teal triangular pennant bunting everywhere, yellow U-railings and striped poles.
  - A giant peppermint-swirl lollipop and a rainbow "…Be This High / To Ride" height chart [Observed] (Abusement_Park.png; text only partly legible).
  - A red-and-white bullseye drum.
  - A kabuki-style angry panda-face panel.
  - Movie and teaser posters [Observed].
- **Weather and particles:** none seen [Observed].

**Approximate palette.** These are median or quantised samples [Observed], made with a sampling script under /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/scripts_abusement/. The 2026 build may differ.

| Element | Hex | Sampled from |
|---|---|---|
| Night sky | #221127 / #241027 | Abusement_Park.png, HuggableCart.png |
| Cloud band | #1c1739 – #2a1b37 | HuggableCart.png, Abusement_Park.png |
| Horizon glow | #462939 – #643e45 | same |
| Stone walls | #786a71 (light #a99889) | Abusement_Park.png |
| Asphalt ground | #3b3939 / #514a37 | Abusement_Park.png, IMG_0667 |
| Red-base deck, lit | #fea47e / #fb8f6a (shadow #cd6a4b) | trailer t_0044 / t_0037 |
| Blue-base deck | #9e8565 – #bab9a0 | Screenshot (509) |
| "[RED]" stencil | #fd1b13 | trailer t_0044 |
| Blue graffiti | #074977 / #224571 | Screenshot (509) |
| Maroon tent stripe | #5f0903 / #7a1e28 (+ off-white) | trailer t_0044 |
| Red-and-white tents | #9c1004 + near-white | IMG_0667 |
| Orange/yellow tents | #df6422 / #fecc54 / #fdfe78 | IMG_0667 |
| Green tents | #709342 (highlight #b2d489) | Abusement_Park.png |
| Mirrored House awning / marquee | #e88c06, #d9520b / teal #296073 | map tile |
| Yellow U-rails | #feb625 / #e9c65a | trailer t_0044 / t_0037 |
| Bunting | red #a11104, teal #2f8c9e | trailer t_0037 |
| Hazard yellow | #eecd10 + black | IMG_0667 |
| Coaster rail | dark #3d0800, cream edge #e7d9af, red stripe | HuggableCart.png, Abusement_Park.png |
| Coaster car | lime #4ebe01 | HuggableCart.png |
| Huggable rider | magenta-pink #d7019d | HuggableCart.png |
| Tent interior | yellow-green #8ca93c | IMG_0632 |
| "SLOWBURN II" poster | #f8f414 | IMG_0668 |

## Landmarks

1. **Perimeter roller coaster.**
   - The coaster rail is dark oxblood with cream edge rails and a red stripe, carried on red-and-white candy-striped pylons around the whole arena.
   - Boxy lime-green cars with a red-orange starburst or flame decal and two headlights each carry a grinning pink Huggable with raised arms [Observed] (HuggableCart.png, File:Abusement_Park.jpg, 6PU2KP9ayN8 hq3).
   - Wiki caption: "This is what the Huggable in a cart looks like in the roller-coaster in Abusement Park, for those who didn't know the look of it." [Fan-wiki].
2. **The red base.** A salmon-lit plank deck with yellow U-rails in front of stone walls sprayed "[RED]" between big red stars with drips. A maroon-and-white striped tent wall stands alongside [Observed] (trailer about 18–22 s).
3. **The Mirrored House.**
   - An orange-and-yellow striped booth with a teal, bulb-studded marquee whose "THE MIRRORED HOUSE" lettering appears mirror-reversed.
   - A white sign reads "LIKE A HOUSE BUT BACKWARDS".
   - Orange double doors have bubble-shaped mirror windows [Observed] (map tile; etzDXojqUKc hqdefault).
   - The wiki calls it the "House of Mirrors" / "Mirror House" [Fan-wiki].
4. **Pump-A-Chump.** A lit marquee reads "…MP-A-CHUMP / FULLA' LEAD". Behind it is a shooting-gallery window with round targets, a big yellow bullet-character cutout and a pink grinning creature face [Observed] (c6qGpQ4zxVA hq2; KsddBonDY88 hqdefault).
5. **Centre skyline.** The big square maroon-and-white tent, three pale-green peaked tents and the octagonal striped gazebo [Observed].
6. **EXIT stairs and the arch.** A yellow-and-black "EXIT" sign reading "Only 400,000 Tix" hangs over a flight of steps. Elsewhere a riveted metal arch is daubed in red "ONLY ONE CAN LEAVE" [Observed] (NewLevelLights; c6qGpQ4zxVA hq1; IMG_0667).

## Hazards and interactive elements

- **Hazards:** no environmental hazard or kill zone is documented anywhere [Unverified]. The map is fully walled [Observed].
- **Jump pads:** present. The wiki's BBG Maps page excludes only Skate or Die, Sky View and Toxic Terror, and the map page mentions jumping "through the jump pads" [Fan-wiki]. I saw a teal glowing ring pad in the "Jeepers Peepers / [NO ENTRY]" corridor and a blue swirl pad near the hazard pillars [Observed].
- **Pickups** [Fan-wiki]:
  - **Bearscream Sandwich:** "inside the small shed near the Blue Team's spawn points". The pickup page says "In a tent on a tiny podium near the Blue Team's base".
  - **Imperial Basket Grande:** the map page says "on the raised walkway opposite the Red team's spawn points" and "near the small shed". The pickup page instead says "Beside the ramp leading out of red's spawn point" and "At the 'exit' above a flight of steps". The two pages conflict.
  - **Health Pack:** "in the narrow corridor between the Red and Blue Teams' spawn points" and "inside the Red Team's base".
  - **Shield:** "in the hole at the corner of the arena" and "near the Blue Team's base next to the bridge".
- **Coaster:** no source says whether the cars move or whether the coaster can be ridden [Unverified]. It is probably set dressing [Inference].
- **Glitches:**
  - The patched Mini Me escape [Fan-wiki].
  - Fan video titles mention a "tent-glitch" (cIa1fCSszKE) and "Out of the map" (XqiPkFluvII) [Unverified].

## Easter eggs and references

- **Battle Bears Fortress teaser posters.**
  - "concept art of the Bombspitter… labelled as the 'Waste Chewer'" and "supposed concept art of the Wizard Hat… labelled as 'Robowizardhat'" [Fan-wiki] ([Bomb Spitter](https://battlebears.fandom.com/wiki/Bomb_Spitter), [Wizard Hat](https://battlebears.fandom.com/wiki/Wizard_Hat)).
  - I saw green posters of a grey robot in a purple star-spotted wizard hat, and a red-framed white poster headed "Waste…" / "Waste Chewer" [Observed] (NewLevelLights crop; Abusement_Park.png; cIa1fCSszKE hq3).
  - The wiki says "Some of these posters are references to new games/updates/maps which SkyVu are developing." [Fan-wiki].
- **Unreleased skin.** "2 duplicate posters of a Soldier skin that never made it in the game", which the wiki places near the exit [Fan-wiki]. I saw two identical blue posters of a spiky, rock- or ice-armoured figure beside the [RED] wall [Observed] (trailer t_0037; Abusement_Park.png). Whether these are the posters the wiki means is [Unverified].
- **Mos Delish.** A poster "near the Red team's base featuring a character named Mos Delish, which is seen in Battle Bears BLAST" [Fan-wiki, Unverified]. Not identified in any image.
- **"2010's" poster.** A poster "near the exit of the park, that says a new game is coming out somewhere in the 2010's" [Fan-wiki]. Not seen.
- **"Not Wil's CANDY STASH".**
  - Red scrawl over a scorched hole in green tent canvas [Observed] (IMG_0632-1-.png).
  - It is in the tunnel under the Red base [Fan-wiki].
  - A joke about Wil, the Chub Scout, who was added three months earlier in 1.3 [Inference].
- **"Jeepers Peepers!"** banner.
  - Five cartoon kids' faces with empty black eye-holes, plus "LOOK INSIDE!" and "WHAT'S IN THE BOX? WHAT'S IN THE BOX?" [Observed] (AP1.png, NewLevelLights).
  - It plays on the film *Jeepers Creepers* and quotes the line from *Se7en* [Inference].
  - It hangs in a corridor under a "[NO ENTRY]" banner, with red curtains [Observed].
- **"SLOWBURN II / You're toast. / Now playing in a theater near you."** A movie poster of an evil chrome toaster [Observed] (IMG_0668). A toaster cutout stands in a glowing yellow doorway [Observed] (6PU2KP9ayN8 hqdefault). No source explains the joke [Unverified].
- **"BBR FOREVER"** graffiti next to Blue's spawn, kept after the 2013 rename to BBG [Fan-wiki]. The blue graffiti beside the blue-side stairs reads "BBR #1" in a low-res thumbnail [Observed] (KsddBonDY88 hq3). The exact wording is unresolved.
- **"RED" painted in blue on the Blue side.** The uploader of Screenshot (509) notes "It says Red on the Blue Team's side" [Fan-wiki]. I saw a big blue ring, "RED" in blue paint pocked with bullet holes, and a blue bear-head silhouette [Observed] (Screenshot (509)).
- **"[RATE US …]?"** A red stencil on the red side, with an arrow curving to a row of stencilled stars [Observed; the rest of the text is illegible] (trailer t_0044). It reads as an app-rating gag [Inference].
- **"Fried Stick on a Stick".** A booth sign with "ULTRA STICK" and "NEW!" [Observed] (c6qGpQ4zxVA hq3; NRvvHAgjkTw hq1). It matches the official "Fried Stick, now served on stick!" [Canon per prior notes, Unverified].
- **"CONDEMNED"** is stencilled on an orange-striped crate or tent [Observed][Fan-wiki].

## Sound and music

- The map has its own theme. The 2026 OST lists "Abusement Park" (0:54) and "Abusement Park (Full Version)" (3:05), scored by "Rob Ruiz, AnDrue Humphreys, and Benjamin Vavak" with no per-track credit [Canon].
- A 2012 wiki revision says "the background music is great" [Fan-wiki].
- Several fan uploads are titled as the map's theme, for example "Battle Bears Gold Soundtrack: Abusement Park" by Slinkster [Unverified]. Not listened to.
- The 2026 build adds a "Jukebox" [Canon]. What it does is undocumented.
- No ambient sound effects are documented [Unverified].

## Images viewed

All local paths are under /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/abusement_park/. Wiki originals are WebP and were converted to PNG.

**Wiki files** (URLs from the imageinfo API on static.wikia.nocookie.net):
- conv/Abusement_Park_jpg.png = File:Abusement_Park.jpg, the top-down editor view with a BATTLE BEARS logo watermark (2012-10-29). Crops: crops/top_nw.png, top_ne.png, top_sw.png, top_se.png.
- conv/Abusement_Park_png.png = File:Abusement_Park.png, the overview (2013-02-08). Crops: crops/ap_png_2x.png, appng_left.png, appng_right.png.
- conv/NewLevelLights.png (2012-07-21). Crops: crops/nll_top.png, nll_bluewall.png, nll_booths.png, nll_leftposter.png.
- conv/AP1.png.
- conv/IMG_0632-1-.png.
- conv/IMG_0667-1-.png.
- conv/IMG_0668-1-.png.
- conv/HuggableCart.png.
- conv/Abusement_park_lc_jpg.png = File:Abusement park.jpg, a small copy of the NewLevelLights composite (2012-08-29).
- conv/Abusement_park_lc_png.png = File:Abusement park.png, the map tile. Crop: crops/icon_4x.png.
- conv/Screenshot_509_png.png = File:Screenshot (509).png. Crop: crops/ss509_wall.png.
- conv/Update_1_3_2_coming_soon.png.

**Steam trailer** (/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/trailer/):
- All 108 frames, viewed as contact sheets sheets/sheet_01–06.png.
- t_0037.jpg (18.0 s), t_0044.jpg (21.5 s) and t_0045.jpg (22.0 s) in full. Crops: crops/t44_rateus.png, crops/t37_posters.png.
- My 4 fps extraction trailer_ap/ap_01–ap_20.jpg (17.5–22.25 s), viewed via sheets/ap_trailer_1.png.
- This is the only Abusement Park shot in the trailer.

**Steam screenshots:** screen_00–04.jpg, viewed via sheets/steam.png. None shows Abusement Park [Observed].

**YouTube thumbnails** (https://i.ytimg.com/vi/<id>/{hqdefault,hq1,hq2,hq3}.jpg):
- Official 2026: -lAtv-j9Sms (menus only), d2ByJWrsoec (hq1 crop: crops/d2By_hq1_2x.png), jkv6FHPghx8, C7uFxvSZ10c, xP27fWSCSKs, ejjsoKQ-VXU, pmE2jKQLSms, qp5cFGLojyw, r91WkR10W2A.
- Fan gameplay: 0n34M2VxJDE, c6qGpQ4zxVA, 573-tJPVPxA, Fbm3TY_D5HE, KsddBonDY88, NRvvHAgjkTw, XqiPkFluvII, 6PU2KP9ayN8, cIa1fCSszKE, etzDXojqUKc. Viewed via sheets/fanA.png, fanB.png, zoom1.png, zoom2.png.

## Prompt pack

**Establishing shot (9:16, environment only, style-neutral; append the house-style suffix):**

> Vertical 9:16 establishing shot from a high three-quarter angle over a walled carnival arena at dusk. The top third is a deep plum-purple sky with a band of dark blue-violet clouds and a dull maroon-red glow along the horizon. A roller-coaster track loops around the entire arena at rooftop height: a dark oxblood rail with cream-white edge rails and a red stripe, held up on red-and-white candy-striped pylons, with a few empty boxy lime-green coaster cars that have red-orange flame decals and twin headlights. Tall cracked grey-mauve stone-block walls enclose everything. On one corner's walls are huge red spray-stencil stars and dripping red paint; the opposite corner's walls have blue spray-paint graffiti and a blue bear-head silhouette. Inside the walls: a large square maroon-and-white striped tent, three peaked pale-green striped tents, orange-and-yellow striped carnival booths with bulb-studded teal marquees, an octagonal yellow-and-brown striped gazebo, a blue-and-white tent with white sawtooth trim, a shooting-gallery booth with round targets, a striped crate stencilled in red, a giant peppermint-swirl lollipop, a rainbow height-chart board and a yellow-and-black hazard-striped shutter over a ramp. Raised wooden plank decks edged with chunky yellow U-shaped railings; red-and-teal triangular pennant bunting strung between striped poles; grimy grey asphalt with orange paint splats. Lighting: warm salmon-orange light pooling on one corner's deck, cool blue-grey light on the opposite corner's deck, glowing marquee bulbs, a backlit lightning-bolt sign box and a teal-glowing jump-pad ring in the foreground. No characters, no readable text, no logos.

- Leaving the coaster cars empty is a [BBG News invention]. In the game every car carries a pink Huggable [Observed], so add the riders back for any shot that allows characters.
- Showing both bases in one frame is a composition choice [BBG News invention]. The official overview renders do show the whole arena from above [Observed].
- Signs and posters are left blank on purpose, so no text is reproduced.

**Staging spots:**
1. **Red base deck at the "[RED]" wall.** Flat salmon planks, yellow U-rails, striped tent on one side, coaster rail overhead. This is documented: the official trailer stages a Wil vs Tillman explosion here [Observed, about 18–22 s]. Good for a stand-off or an explosive punchline. The specific gag is a [BBG News invention].
2. **The EXIT stairs under "Only 400,000 Tix".** The official joke is that 400,000 tickets buy your freedom and "ONLY ONE CAN LEAVE" [Canon per prior notes, Unverified; signage Observed]. A bear counting a pathetic strip of tickets at the foot of the steps is a [BBG News invention].
3. **The Mirrored House doorway ("LIKE A HOUSE BUT BACKWARDS")** [Observed]. A mirror or doppelgänger gag. The interior and any reflections inside are undocumented [BBG News invention].
4. Alternative: **the "Jeepers Peepers" corridor** under the "[NO ENTRY]" banner, with red curtains and a glowing jump pad [Observed]. Something peers through the eye-holes, then someone gets launched off the pad [BBG News invention].

## Confidence

- **Look and landmarks: observed.** Many official and in-game images and trailer frames were opened.
- **Era: documented.** The wiki's store notes, the update banner and the 2026 OST agree. The exact 1.3.2 date is in slight doubt.
- **Layout: partial.** It is traced from one editor top-down image plus wiki prose, and the compass orientation is unknown.
- **2026 status: partial.** The map appears in the trailer and the OST but is not named in the store text.
- **Official blurb: unknown this session.** Wayback was unreachable.

---

## Corrections to our notes

I found no incorrect statement about Abusement Park. I checked:
- /home/user/thallo-site/reports/Battle Bears character lore.md
- /home/user/thallo-site/research_notes/Battle Bears character lore/*.md
- /home/user/thallo-site/bbg-news-repo/characters/*.md
- /home/user/thallo-site/bbg-news-repo/content/evergreen.json

Only franchise_world.md mentions the map, at lines 98 and 104.

Two things to note:
- Line 104's elided blurb quote ("child friendly games like 'Pump-A-Chump (Fulla' Lead)'… Fried Stick, now served on stick!… no less than 400,000 tickets will buy your freedom and ONLY ONE CAN LEAVE.") could not be re-opened this session. In-map signage corroborates every phrase, but the full, unelided text should be captured when Wayback responds.
- A gap rather than an error: none of the notes record that the 2026 OST has a dedicated "Abusement Park" track (track 1) and "Abusement Park (Full Version)", or that the official 2026 Steam trailer shows this map. The evergreen MAPS caption lists only the four maps named on the store page, which is accurate.

## Open questions

See the open_questions field.