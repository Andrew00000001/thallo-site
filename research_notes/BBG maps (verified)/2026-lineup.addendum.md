<!-- gap pass 1 -->
# 2026 lineup addendum: Steam Yard Blues, Desert Airmine, Haunted Castle and Frozen Pundra in 2026 footage, and the "16 wacky maps" count

This addendum covers only the 2026-lineup gap. It moves four maps from [partial] to [Observed] in the 2026 build, using frames from the October 15, 2026 final playtest. It also reconciles Steam's "16 wacky maps".

**The main finding.** Toxic Terror is in the 2026 build. Our gap note said it "never appears", but I observed it in:
- SkyVu's own short "BBG Maps Ranked part 1" (Oct 11, 2026), and
- three separate recordings of the Oct 15 final playtest.

The count therefore closes as **15 legacy BBG maps + Sky Pirates = 16**. Every one of those 16 has been seen in 2026 playtest footage. Some I saw myself; others rest on fan chapter labels, as marked in the table in section 6.

**Sources I reached (2026-10-18):**
- **YouTube storyboard images.** These are YouTube's own seek-preview frames: one every 10 s for the long videos, one every 1 s for the short. They were fetched through an Invidious API mirror, cut into frames, and opened with Read as contact sheets. **I watched no video and heard no audio.**
  - Already on disk: HKbwq7PolNc (InstableGR, 429×180), ZMhLVXWT6OY (SkyVu livestream, 320×180), jkv6FHPghx8 (SkyVu short), and the critic's uNZA3nlABOA and EQwloJnrOko frames.
  - Fetched by me this session: 1MP1rFi4t-Q (JustNubz, "Battle Bears Gold FINAL PLAYTEST"), MS2wiArCiCA (Left4Dead, "Battle Bears Gold FINAL PLAYTEST", streamed Oct 15), dz4iqZE8nQE (Vada Zora Reva Nova, iPad, final playtest) and ejjsoKQ-VXU (SkyVu, "BBG Livestream Sunday", Sep 20).
- **Steam, re-fetched 2026-10-18:** the store API for 4408320, the soundtrack API and store page for 5321720, and the News API.
- **Fan wiki through its API, fetched 2026-10-18:** BBG Maps, Desert Airmine, Haunted Castle, Toxic Terror, Sky Pirates.
- **Video metadata (title, author, date, description):** from saved page data and the Invidious API.

**Not reachable:**
- **web.archive.org.** All about 30 attempts were reset, over curl and WebFetch. The availability API does report store-page captures at 20260227133909 and 20260820195244, but neither could be downloaded.
- **SteamDB** (403) and **archive.ph** (429).
- **The Next Fest demo.** It is not live yet; Steam's appdetails `demos` field is null.
- **SkyVu's "Steam Next Fest Demo Party with BBG Devs" (Sf01OOF_X3Q).** It is a scheduled live event that has not started.

**Resolution caveat.** Storyboard frames are 258–429 px wide JPEGs. Shapes and colours are reliable. Small text, decals and fine props are not. All hex values below are approximate (±10–15%). They were sampled by script from the central frame with the HUD margins cropped off. The scripts are in /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/scripts_lineup_gap/.

---

## 0. Which build these frames show

- **SkyVu's livestream** ZMhLVXWT6OY is titled "BBG Livestream Final Playtest before Steam NextFest Oct 19" [Canon]. Its description reads: "The final BATTLE BEARS GOLD playtest will take place tomorrow, Thursday, October 15th at 3:00 PM PDT … Headline additions: -Custom keybinds -Jukebox -UI controller support -Lighting improvements -Lots of bug fixes. A lot to test this week, including a couple of surprises we didn't think we'd be able to squeeze in!" [Canon].
- **Steam news, Oct 14, 2026**, "Final Discord Playtest this Thursday Oct 15", carries the same headline list [Canon].
- **InstableGR's upload** HKbwq7PolNc is titled "Battle Bears Gold - Final PC Playtest (10/15/26)". The description says: "The fifth and final BBG playtest… an overhauled lighting for all maps, attempting to restore what they looked like back in the day. No Bear's Land, Desert Airmine, and Space Oddity … now look almost just like they did when the game first launched as Battle Bears Royale" [Unverified: fan uploader's claim; description text read from page data].
- **Build tag.** The bottom-right tag in HKbwq7PolNc and MS2wiArCiCA begins "3.0.7". I read the rest as "2026.11.19 b7", but the digits are uncertain at this resolution [Observed: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/lineup_gap/wm_all.jpg].
- **SkyVu livestream overlay.** During the stream, an overlay reads "BATTLE BEARS GOLD – FIVE NIGHTS OF BATTLE BEARS – OCT 19 - 23 LIVE EVERY NIGHT" next to a Steam Next Fest badge [Observed: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/critic/zm_fnob_big.png].

---

## 1. Steam Yard Blues (2026 spelling "Steamyard Blues"): now [Observed] in the 2026 build

### Official text
- "You can even make some time for that yearly match on Steamyard Blues, most likely just for the soundtrack." [Canon] (Steam 4408320, re-fetched 2026-10-18).
- Soundtrack: "15 Steamyard Blues 0:51" [Canon] (Steam 5321720 store page, re-fetched 2026-10-18).
- 2014 preview: "BATTLE BEARS GOLD Update 2.8 "Steam Yard Blues" Map Preview", BATTLE BEARS channel, published 2014-02-21 [Canon title and date: Invidious metadata for RnCV0V5gWCI].

### Era and status
- **Added** in BBG 2.8, February 2014 [Canon title]. The wiki says it launched alongside King of the Windmill [Fan-wiki, from the earlier dossier].
- **2026: in the final playtest build** [Observed]:
  - HKbwq7PolNc, 5:20–9:10. The uploader's chapter is "Match 2 (Free-for-All, Steamyard Blues, Astoria)". The HUD shows the leader's name centred, which is the FFA layout [Observed].
  - HKbwq7PolNc, 13:40–17:30. Chapter "Match 4 (Team Battle…)", with a red/blue team score shield [Observed].
  - HKbwq7PolNc, 43:50–47:50. Chapter "Match 11 (Free-for-All…)" [Observed].
  - 1MP1rFi4t-Q, 28:20–32:40. On-screen: "YOU'RE ON TEAM RED / GET KILLS TO SCORE POINTS FOR YOUR TEAM" [Observed: frame 29:10, jn_kc.jpg].
- **Earlier 2026 playtests.** InstableGR's 2nd-playtest upload (lFr8-yHbbzQ, Jul 29) has a chapter "12:33 - Match 4 (Plant the Bomb, Steamyard Blues, B-1000/Graham)" [Unverified: fan chapter label].
- **SkyVu's own short** "BBG Maps Ranked part 1" (jkv6FHPghx8, Oct 11, 2026) opens its ranking with a Steam Yard Blues clip at 0:11–0:15 (brass decks, the shark-mouth plane) and drops the tile into the "13-16" tier [Observed: jkv_all.jpg, jkv_tiers.jpg].
- **2026 modes seen:**
  - FFA and team kills (TDM/"Team Battle") [Observed].
  - PTB, from a fan chapter only [Unverified].
  - Kill Confirmed: no chapter or frame found for this map [Observed absence].

### Setting
Unchanged from the main dossier: a brass-and-airship yard hanging over a void at dusk [Observed in 2026 frames].

### Layout (2026 frames)
- Multi-level wooden plank and riveted gold-plate decks with open edges over a dark void [Observed].
- Glowing cyan circular jump pads sit inside gold gear-rimmed octagonal housings (HK 8:20, 46:20, 47:40) [Observed].
- Which side is red and which is blue cannot be determined from these frames [Unverified].

### Look (2026 build)
- **Time of day:** dusk.
  - A pale butter-yellow horizon glow, about #E6DF84 (HK 6:30) [Observed].
  - Jagged mauve-black mountain silhouettes, #1E0A13 to #462E35 [Observed].
  - Near-black maroon below the horizon, #1B0107 to #1B020A [Observed].
  - A plum to orange-brown haze higher up, #8B4C23 at HK 15:20 [Observed].
- **Metal:**
  - Lit brass and gold reads saturated: median #CD8739, highlights #F7D941 to #F8C55C, gold-orange #E69438 (HK 14:20, 45:00) [Observed].
  - Deck planks #D09648 [Observed].
  - Shadowed metal #251809 / #7A490F [Observed].
- **Planes:** slate-teal bodies about #1F2C32 [Observed]. Wing paint is slate-teal #2B3F3D [Observed].
- **Blimp:** purple envelope panels about #753A8C [Observed].
- **Compared with older images:** the overall dusk-and-gold look matches the 2014 description and SkyVu's grid tile (r3c2) [Observed]. Whether the brass got brighter in 2026 cannot be measured fairly against 2014 thumbnails [Unverified].
- **Particles:** pink petal-like particles over a wing at HK 5:40 [Observed]. They appear only during combat, so they are probably a weapon or ability effect, not set dressing [Inference]. I saw no steam or smoke [Observed].

### Landmarks seen in the 2026 build
1. **The shark-mouth fighter planes.** A slate body, white teeth on a dark-red mouth, and a tasselled red-and-gold hex anchor at the nose (HK 15:20, 46:40; JN 30:20) [Observed: c_syb_shark.png]. The wing carries a roundel and yellow-green lettering [Observed: c_syb_pink.png].
2. **The purple blimp in a gold lattice cage.** Its panels are stencilled with a round-eared bear head that has a white-ringed (monocle) eye [Observed: c_syb_pink.png, HK 5:40].
3. **Giant brass gears and cog plates** that form the deck edges and pad housings (HK 6:50, 8:40, 46:20) [Observed].
4. **Riveted gold hull plates and wooden plank decks** over the void [Observed].
5. **A round brass porthole or hatch** (HK 13:50) [Observed].
6. **A checker-patterned box with a white sack on top** (HK 5:50) [Observed; identity Unverified].

### Hazards and interactive elements
- The deck edges are open [Observed]. Death by falling is [Inference]: "SUICIDE" kill-feed lines appear (HK 14:10, 15:20) but their cause cannot be seen [Observed].
- No moving hazard was seen [Observed absence].

### Easter eggs and references
Nothing new.

### Sound and music
- The OST track is listed above [Canon].
- InstableGR says the new Jukebox lets players "assign them to maps" [Unverified: fan claim].
- The Jukebox appears as a menu ("JUKEBOX … Menu Theme - BBG / Menu Theme - BBR / Bear With Me …") at HK 75:10 [Observed: hk_hc17.jpg].

### Images viewed
/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/lineup_gap/hk_syb2.jpg, hk_syb4.jpg, hk_syb11.jpg, c_syb_shark.png, c_syb_pink.png, jn_all_1.jpg (28:20–32:40), jn_kc.jpg, jkv_all.jpg, jkv_tiers.jpg, grid_x3.png, plus the HK frames listed on those sheets.

### Prompt pack (9:16, environment only)
- **Shot.** A vertical establishing shot at dusk, taken from a high brass gantry looking across a floating airship yard.
- **Foreground:** a riveted gold deck of hull plates and huge interlocking brass gears. One gear rim cradles a glowing cyan circular launch pad.
- **Midground:** a slate-teal riveted propeller fighter plane, tethered by tan ropes. Its nose is painted as a white-toothed shark mouth on dark red, with a gold hex anchor and a red tassel at the tip.
- **Above:** a purple airship envelope held in a gold lattice-rib cage. Its panels carry a stencilled round-eared bear head with a monocle-ringed eye; the stencil has no letters.
- **Below:** wooden plank walkways cross between platforms. Past the deck edge there is only a deep maroon-black void.
- **Horizon:** a pale butter-yellow glow behind jagged mauve-black mountain silhouettes, with plum haze above.
- **Light:** warm gold key light on the metal and deep plum shadows. No characters, no readable text or logos.
- **Not documented:** soft distant airship lights in the haze [BBG News invention].
- **Staging spots:**
  - (1) On the plane's wing beside the shark mouth, for a "this thing bites" gag [BBG News invention].
  - (2) Inside a gear-rim jump pad, mid-launch [the pads are Observed; the gag is BBG News invention].
  - (3) At the deck edge above the void, silhouetted against the yellow horizon [Observed setting].

### Confidence
**observed** for the 2026 look, landmarks and modes (FFA, team kills). PTB in 2026 is fan-labelled only.

---

## 2. Desert Airmine: now [Observed] in the 2026 build

### Official text
- Soundtrack: "12 Desert Airmine 1:13" [Canon] (Steam 5321720).
- The Steam store page does not name the map [Canon, by absence].

### Era and status
- **History.** The wiki says: "It was released in the initial 1.0 release together with the No Bear's Land, Space Oddity and H.I.P. Test Lab, but was later removed in update 2.0 together with Haunted Castle not only because they were the least popular maps, but to also allow more server space. It was re-released in v2.7." [Fan-wiki; Desert Airmine page fetched 2026-10-18].
- **2026: in the final playtest build** [Observed]:
  - HKbwq7PolNc, 0:10–5:10. Chapter "Match 1 (Team Battle, Desert Airmine, Wil/Riggs)". "YOU'RE ON TEAM BLUE" shows at 0:10 [Observed].
  - HKbwq7PolNc, 9:30–13:30, an FFA chapter [Observed: 12:00 frame].
  - HKbwq7PolNc, 60:30–64:30, a Team Battle chapter [Observed: 60:40 and 62:10].
  - 1MP1rFi4t-Q, 14:00–17:50 [Observed].
  - dz4iqZE8nQE (iPad), 108:00–109:10 [Observed: dz4_tt.jpg].
- **Earlier:** JustNubz's 3rd-playtest chapter "19:59 Desert Airmine FFA" [Unverified: fan chapter label].
- **SkyVu's ranking short** shows a Desert Airmine clip at 0:54–0:59 and places it in the "9-12" tier [Observed: jkv_all.jpg, jkv_tiers.jpg 1:04].
- **2026 modes seen:** team kills and FFA [Observed / chapter labels].

### Setting and layout
- Floating, sand-topped islands with tapered terracotta undersides, over a deep red-rock canyon, on several levels [Observed].
- Metal grating walkways and plank bridges link the islands. Power cables are slung between towers (HK 4:00, 60:40) [Observed].
- A round grey landing pad with a red "H"-shaped marking (HK 12:00) [Observed; the letter is read at low resolution]. This matches the wiki's Blue-team "big helicopter landing pad" [Fan-wiki].
- The wiki's three-level plan and the hidden fourth island were not checkable at this resolution [Unverified].

### Look (2026 build)
- **Lighting:** bright daylight, clear and hazy, with no night or dusk grading [Observed].
  - Sky: powder blue, #9BB9C8 to #AAC6CF [Observed].
  - Sand: golden. The median is #E3AB57; lit tops run #F6CB66 to #F9D874 [Observed].
  - Canyon walls: terracotta, #764936 to #825C42 [Observed].
  - Deep shadow under the islands: #28110E [Observed].
  - Steel and grey metal: #716D5D to #856E63 [Observed].
  - Cactus green: about #4F9724 [Observed].
- **Compared with our draft:**
  - The 2026 sky matches the draft's in-game "powder-blue" range (#95B0C7 to #A1BED6) [Observed comparison].
  - The 2026 sand reads warmer orange-gold than the draft's "saturated golden yellow" fan thumbnails (#F1CE4C to #FCBD32), and closer to the 2012 renders' #E0A045 [Observed comparison]. That fits InstableGR's claim that the lighting was restored toward BBR [Inference; the claim itself is Unverified].

### Landmarks seen in the 2026 build
1. **A blue portable-toilet booth** with a black-and-white bear-face poster and a small red label, next to a spawn (HK 0:10, 62:10) [Observed: da_crops.jpg].
2. **A windmill on a lattice tower** (HK 2:50, 4:10) [Observed].
3. **Saguaro cacti** (HK 2:50, 60:40, 62:10) [Observed].
4. **A satellite dish on a lattice mast**, with a glowing cyan hexagonal ring near its head (HK 60:40) [Observed; what the ring is remains Unverified].
5. **Stacked black-and-white crates printed with bear-face icons** (HK 60:40) [Observed].
6. **A blue-glowing grid launch pad on metal** (HK 1:10) [Observed].
- **The central oil drill with Graham's emblem** was not clearly visible in any storyboard frame I opened [Observed absence]. It cannot be confirmed or ruled out at this resolution.
- A red funnel or horn shape seen from above (HK 2:20) is [Observed; identity Unverified]. It may be the drill's red-rimmed head [Inference].

### Hazards and interactive elements
The wiki's moving drill and windmill kill-zones [Fan-wiki] were not observed in action [Unverified].

### Easter eggs
None new.

### Images viewed
/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/lineup_gap/hk_da1.jpg, da_detail.jpg, da_drill.jpg, da_crops.jpg, jn_all_0.jpg (14:00–17:50), dz4_tt.jpg (108:00–109:10), jkv_all.jpg, grid_x3.png (r1c4).

### Prompt pack (9:16)
- **Shot.** A vertical establishing shot under a clear powder-blue sky with soft haze.
- **Islands:** floating islands with smooth golden sand tops and striated terracotta cliff sides that taper to dark red-brown points underneath, stacked at different heights above a deep red-rock canyon.
- **Foreground:** a metal-grate walkway and a rope-and-plank bridge lead to a sand island with two saguaro cacti and a pale-blue portable toilet booth. The booth's poster shows only a simple bear-face icon, with no text.
- **Midground:**
  - a tall riveted lattice tower carrying a windmill;
  - a second mast with a satellite dish;
  - power cables sagging between them;
  - a stack of black-and-white crates printed with bear-face icons;
  - a round grey landing pad with red markings (shown as an abstract cross-bar shape, no letters).
- **Light:** bright daylight with warm rim light on the rock and deep shadow under each island. No characters.
- **Not documented:** a few loose rock chunks floating in the far sky [BBG News invention; the draft saw them in 2012 renders only].
- **Staging spots:**
  - (1) The toilet booth: a door-slam or hiding gag [the booth is Observed; the gag is BBG News invention].
  - (2) The windmill tower platform: a sniper perch [Fan-wiki use].
  - (3) A plank bridge between two islands over the canyon drop [Observed].

### Confidence
**observed** for the look and props. The drill and the layout details are **partial**.

---

## 3. Haunted Castle: now [Observed] in the 2026 build

### Official text
- Soundtrack: "11 Haunted Castle 1:01" [Canon] (Steam 5321720).
- From our notes, not re-verified (Wayback unreachable): "The Battle Bears Family. Their house is a haunted castle." [Canon per franchise_world.md; Unverified this session].

### Era and status
- **History.** The wiki says: "The Haunted Castle was a map added to Battle Bears Gold in v1.3.3, part of the Halloween-themed update. It was later removed alongside the Desert Airmine map in the 2.0 update … It was re-released in v2.4 as part of the Halloween-themed update." [Fan-wiki; fetched 2026-10-18].
- **2026: in the final playtest build** [Observed]:
  - HKbwq7PolNc, 69:50–74:40. Chapter "Match 17 (Plant the Bomb, Haunted Castle, Graham)". "YOU'RE ON TEAM RED" shows at 69:50 [Observed].
  - **SkyVu's own livestream** ZMhLVXWT6OY, 46:00–50:10 [Observed: zm_hc.jpg]. A dark map tile is chosen on the PICK LEVEL screen at 45:30, just before the match [Observed: zm_create.png; reading the tile as Haunted Castle is Inference].
- **Earlier:** InstableGR's 2nd-playtest chapter "30:14 - Match 8 (Kill Confirmed, Haunted Castle, Tillman/B-1000)" [Unverified fan label]. droid BBG's videos describe "Free-For-All on Haunted Castle" (Sep 25) and "Team Deathmatch on Haunted Castle" (Oct 9) [Unverified fan text].
- **2026 modes:** PTB [Observed chapter plus team HUD]. KC, FFA and TDM [fan labels].

### Look (2026 build)
- **Time of day:** night.
  - A black sky (#060D07) with a dark purple horizon band (HK 69:50–70:10) [Observed].
  - A pale grey full moon, #B3B3B3, high in the sky (HK 72:30; ZM 49:30) [Observed]. Our draft had a moon only in a 2021 fan thumbnail; 2026 confirms one in-game.
- **Overall darkness:** 57–81% of each sampled HK frame falls in the dark class (value below 25%) [Observed by script].
  - Stone walls read charcoal, #131616 to #151718; lit stone is grey-brown, #615046 to #6A6660 [Observed].
  - Courtyard dirt is deep umber, #4A2E1A to #4D2A1B, rising to #9F5719 near lanterns [Observed].
  - Red-team banners are crimson, #661315 to #880617 [Observed].
  - Jack-o'-lantern glow is orange with a yellow core of about #DFCD35 [Observed].
- **Compared with 2013 (our draft's numbers):** the 2013 sources show a lit terracotta courtyard (#B5503D) and teal-slate walls (#1B3541). The 2026 build is much darker and browner [Observed comparison of sampled values]. That fits SkyVu's "Lighting improvements" [Canon], but the direction of the change is my reading [Inference].

### Landmarks seen in the 2026 build
1. **Red swallowtail banners with a dark emblem** flanking an arched portcullis gate with a wooden lattice (HK 70:50, 73:30, 74:00; ZM 48:40) [Observed]. A blue banner hangs on a wall at ZM 48:10 [Observed].
2. **Jack-o'-lanterns** on the ground and along the wall tops (HK 70:50, 71:30, 72:10) [Observed].
3. **Cobwebs** across tower corners (HK 71:20; ZM 46:30, 46:50) [Observed].
4. **A graveyard of rounded headstones**, with a red slab or coffin-like box (HK 73:10; ZM 46:30, 49:30) [Observed; reading it as a coffin is Inference].
5. **Crenellated charcoal stone walls and towers, plus barrels** (HK 70:40) [Observed].
6. **Jump pads:** cyan pads with yellow-black hazard rims on metal grating (HK 74:30), and an octagonal pad on dirt (HK 70:30) [Observed].

### Hazards and interactive elements
The wiki says: "There are two levers on the map … When hit with a melee attack, there are gates in a passageway underneath that will open or close." [Fan-wiki]. The levers were not visible in any 2026 frame I opened [Unverified for 2026].

### Easter eggs
- The wiki's gravestone of names: "MK, Lt. Action, Rob, Trang, An, Jackson, Grimes, 1nachoboy5, and Apothecy" [Fan-wiki].
- Headstones are present in 2026 [Observed], but their text is unreadable [Unverified].

### Images viewed
/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/lineup_gap/hk_hc17.jpg, zm_hc.jpg; /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/critic/zm_create.png; grid_x3.png (r2c3).

### Prompt pack (9:16)
- **Shot.** A vertical establishing shot at night inside a castle courtyard.
- **Sky:** a black sky with a faint violet band at the horizon and a pale grey full moon high in the frame.
- **Foreground:** packed deep-umber dirt lit in warm orange pools by jack-o'-lanterns set on the ground.
- **Midground:**
  - an arched gate of dark wooden lattice in a crenellated charcoal stone wall, flanked by two long crimson swallowtail banners with a dark, wordless emblem;
  - jack-o'-lanterns lining the wall top;
  - a cobweb stretched across a tower corner.
- **Side:** a small graveyard of rounded headstones (blank faces) behind a low stone fence, with barrels against the wall.
- **Light:** cool, near-black stone with warm lantern light; no fog.
- **Not documented:** faint drifting dust in the lantern light [BBG News invention].
- **Staging spots:**
  - (1) Under the portcullis between the red banners: a team "gate" entrance [Observed].
  - (2) The headstone row under the moon: a spooky gag beat [Observed setting].
  - (3) A wall-top walkway lined with jack-o'-lanterns [Observed].

### Confidence
**observed** for the look and props. The levers and gates are **unverified** in 2026.

---

## 4. Frozen Pundra: now [Observed] in the 2026 build

### Official text
- Soundtrack: "10 Frozen Pundra 0:54" [Canon].
- 2014 preview: "BATTLE BEARS GOLD Update 2.7 "Frozen Pundra" Map Preview", published 2014-01-22 [Canon title and date: Invidious metadata for Ev5WvMIp1_4].

### Era and status
- **Added** in BBG 2.7, January 2014 [Canon title].
- **2026: in the final playtest build** [Observed]:
  - HKbwq7PolNc, 22:00–26:50. Chapter "Match 6 (Plant the Bomb, Frozen Pundra, B-1000/Botch)". On-screen at 22:30: "YOU'RE ON TEAM BLUE / … THE BOMB TO SCORE POINTS". The kill feed shows "DEPOSIT +225" lines [Observed: hk_fp6.jpg].
  - 1MP1rFi4t-Q, 18:20–22:10, 33:00–36:50 and 52:40–56:30 [Observed].
- **Earlier:** InstableGR's 2nd-playtest chapter "Team Battle, Frozen Pundra" [Unverified fan label]. Nuke_Dukem's 3rd playtest at 39:00–42:20 [Observed: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/critic/eq_fp_syb2.jpg].
- **SkyVu's ranking short:** a clip at 0:16–0:22, carrying a "JUSTNUBZ" corner tag, so it is community playtest footage. The tile goes into the "13-16" tier [Observed].
- **2026 modes:** PTB [Observed]. Team Battle [fan label].

### Look (2026 build)
- **No lavender.** The lavender and mauve tint seen in SkyVu's grid tile and in 2014 images is absent:
  - Pixels in the purple hue band average 0.5–2.6% per recording, measured over 31 HK frames and 73 JN frames.
  - The single highest frame reaches 22%, and that is a weapon effect [Observed by script].
- **Palette:**
  - cyan ice floors, #3ED7F9 to #4DCAF8;
  - mid blue, #2264C7 to #2F75DD;
  - cobalt walls, #183DC4;
  - deep navy rock, #111B76;
  - near-black crevices, #060B0F to #0A0E1F;
  - frost highlights, #E6FDFB.
- **Lighting:** bright, even and cool, with no visible source [Observed].

### Landmarks seen in the 2026 build
1. **Dense icicle fringes on the ceiling**, over faceted cobalt rock walls (HK 24:10, 25:20) [Observed].
2. **Curving ice ramps and slides**, plus tall ice columns (HK 22:00, 24:40) [Observed].
3. **"BOMB HOLE WARNING" signs.** White boards with a red border and a no-bomb symbol, on a red square base (HK 22:40, 25:50) [Observed: fp_signs.jpg]. The same sign text appears on Gold Digger in SkyVu's Sep 20 stream (EJ 20:30) [Observed: other_maps.jpg]. These are PTB "bomb hole" markers [Inference].
4. **A dark-green angular structure with lights** where the blue bomb is placed, under a beam of light (HK 25:00, 26:20) [Observed]. That it is the bomb-delivery point is [Inference] from the "DEPOSIT" feed.
5. **Small cyan ring pads, and a white health box with a red cross** (HK 24:50, 26:00) [Observed].

### Hazards
- None seen [Observed absence].
- The wiki's droppable icicles [Fan-wiki, per the main dossier] are unverified in 2026 [Unverified].

### Images viewed
/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/lineup_gap/hk_fp6.jpg, fp_detail.jpg, fp_signs.jpg, jn_all_0.jpg, jn_all_1.jpg, jn_all_2.jpg, jkv_all.jpg; /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/critic/eq_fp_syb.jpg, eq_fp_syb2.jpg.

### Prompt pack (9:16)
- **Shot.** A vertical establishing shot inside a vast ice cave.
- **Floor:** a curving road of smooth, glowing cyan ice that runs downhill between faceted cobalt-blue rock walls.
- **Ceiling:** thick with fringes of translucent icicles, with a few tall ice columns joining floor to ceiling. Deep navy shadows sit in the crevices.
- **Midground:** a squat, dark-green angular metal platform with small lights, catching a pale vertical light beam.
- **Foreground:** a small warning sign on a red square base, showing only a red-ringed bomb pictogram and no words.
- **Light:** cool, even, sourceless light, saturated cyan and cobalt, with frosty white highlights. No warm or pink tint. No characters.
- **Not documented:** a faint cold mist hugging the floor [BBG News invention].
- **Staging spots:**
  - (1) Sliding down the ice ramp [Observed ramp; action is BBG News invention].
  - (2) Beside the bomb-hole sign, for a PTB gag [Observed].
  - (3) Under the icicle fringe, for a "what's above you" beat [Observed icicles; the drop is Fan-wiki].

### Confidence
**observed** for the look and the PTB props. Hazards are **unverified**.

---

## 5. Toxic Terror: present in 2026 (this changes the count)

### Evidence [Observed]
- **SkyVu's short "BBG Maps Ranked part 1"** (jkv6FHPghx8; presenter's lower third "GOLD44 (JOE) HEAD OF PRODUCT").
  - A gameplay clip at 0:30–0:40 shows a big brown-barked tree trunk, a lime-green glowing pipe and grate, amber wall lamps and railings.
  - The tile is then placed in the "13-16" tier.
  - Sources: jkv_all.jpg, jkv_tt.jpg, jkv_tiers.jpg.
- **MS2wiArCiCA (Left4Dead, final playtest stream)**, 46:40–50:30 and 52:40–56:20 (l4d_tt_a.jpg, l4d_tt_b.jpg).
  - The PICK LEVEL icon at 51:00 is a dark room with a lime-green puddle, the same composition as Toxic Terror tile r4c4 in SkyVu's grid (l4d_pick.jpg, icon_cmp.jpg).
  - In the matches: green glowing grid grates, red pipes, amber lamps, deep indigo walls, a "DANGER" sign and a red STOP sign.
- **1MP1rFi4t-Q (JustNubz, final playtest)**, 37:20–42:10 (jn_tt.jpg).
  - Green grid grates, a STOP sign, a brown tree trunk and branches, and a large blue banner with a white round emblem (40:10).
  - "YOU'RE ON TEAM RED / DELIVER THE BOMB TO SCORE POINTS" at 41:20, which is PTB.
- **dz4iqZE8nQE (iPad, final playtest)**, 110:10–114:10 (dz4_tt.jpg).
  - Green grid floor with red laser lines (112:30).
  - "HUR HUR HUR WINS!" at 114:10, an FFA result.
- **The match to 2013 sources.** The 2013 wiki preview (Toxic-Terror-Preview.png: green grid grate, amber lamps) and Slinkster's tile match these 2026 frames (tt_compare2.jpg) [Observed].

### What was not seen
Toxic Terror does not appear in the playtest 3 and 4 samples I checked (uNZA3nlABOA and EQwloJnrOko green-frame candidates: pt34_green.jpg) [Observed absence; not exhaustive]. It may be one of the "couple of surprises" in the final build [Inference from the Canon quote].

### 2026 look (sampled)
- green grate glow #279D12 to #2DA417, with a pale glow core #D3F7CA;
- dark ground #131A05 to #18150D;
- red pipes #630E0D to #69090A;
- indigo walls about #130A57 (L4D 47:00);
- amber lamps #967F20 to #D1B329.

All [Observed by script].

### Modes seen
PTB and FFA [Observed].

---

## 6. Reconciling "16 wacky maps"

### Official text
- "compete with friends across 16 wacky maps" [Canon] (Steam 4408320 short description, re-fetched 2026-10-18).
- "packed with new modes, maps, skins and more!" [Canon] (battlebears.com home, fetched 2026-10-18).

### Maps seen in 2026 builds
"Mine" means I saw it in frames this session. "Fan label" means a chapter or title text I read but did not verify visually.

| # | Map | 2026 evidence |
|---|---|---|
| 1 | No Bear's Land | Mine: HK 27:20–30:50; SkyVu EJ 33:20–38:30 |
| 2 | H.I.P. Test Lab | Fan labels: PT2 46:53, PT3 15:02 |
| 3 | Space Oddity | Mine: SkyVu ZM 22:10–23:40; HK 18:30 |
| 4 | Aztec Attack | Mine: SkyVu EJ 26:30–28:00 (lava and temple); fan labels |
| 5 | Abusement Park | Fan label: PT3 43:08 |
| 6 | Shortest Parsec | Mine: JN 5:00–13:00, 57:00–61:00; fan label HK 35:30 |
| 7 | Marecraft | Mine: HK 64:40–69:30; JN 48:20–51:10, 70:50–71:20 |
| 8 | Sky View | Mine: JN 0:40–4:30 (crane, crates); critic EQ sheet |
| 9 | Gold Digger | Mine: SkyVu EJ 18:20–20:30 (rock pit, bomb-hole sign); JN 23:10–25:00; fan label HK 31:20 |
| 10 | Skate or Die | Mine: SkyVu EJ 11:00–12:20 (half-pipes), 45:30 (graffiti) |
| 11 | Toxic Terror | Mine: section 5 above |
| 12 | Desert Airmine | Mine: section 2 |
| 13 | Haunted Castle | Mine: section 3 |
| 14 | Frozen Pundra | Mine: section 4 |
| 15 | Steam Yard Blues | Mine: section 1 |
| 16 | Sky Pirates (new for BBG; a BB Overclock launch map per the wiki) | Mine: HK 48:00–60:10. Also SkyVu's "Battle Bears Gold 2026 - Sky Pirates Map Reveal" (Aug 31, 2026; "Gameplay highlights from the new Sky Pirates map!") [Canon] |

The Tutorial was not counted. It is single-player and not a PvP arena; HK's end screen offers "PLAY TUTORIAL" [Observed, hk_hc17.jpg 75:00].

**Result:** 15 legacy BBG maps (exactly the wiki's BBG Maps list: "No Bear's Land … Steam Yard Blues", fetched 2026-10-18 [Fan-wiki]) + Sky Pirates = **16** [Inference, strong]. Every one has been seen in 2026 footage.

### Sky World and Sky Pirates
- Steam news, Aug 19: "New Map: Sky World" [Canon].
- SkyVu's short "Sky Pirates in BBG!" (CwxpBZg6Fi4, Sep 7) has the description "Enjoy the highlights from our Sky World playtest!" [Canon].
- So Sky World and Sky Pirates are the same new map [Inference, strong].

### Why the earlier complications don't break the count
- **SkyVu's 4×4 ranking grid.** It holds 15 *distinct* legacy maps and no Sky Pirates tile.
  - Space Oddity appears twice. Tile r1c3 matches the 2012 "Spaceship Level" render Spacecraft2.jpg: big angled orange windows, a cyan ceiling disc and a yellow-edged floor opening. Tile r3c3 is the Space Oddity map-select tile [Observed: r1c3_cmp.jpg].
  - So the grid ranks only the classic maps [Inference]. It is not a list of the 2026 sixteen.
  - Its part 1 fills the "13-16" tier with Steam Yard Blues, Frozen Pundra, Sky View and Toxic Terror, and the "9-12" tier with Skate or Die, No Bear's Land, Desert Airmine and Aztec Attack, in clip order 0:11–1:04 [Observed: jkv_all.jpg, jkv_tiers.jpg; tile-to-row assignment read from low-res frames].
  - My YouTube search on Oct 18 found no part 2 [Observed: s2_BBG_Maps_Ranked_part_2.json].
- **The OST's 16 map-named tracks** include "16 Castle Royale 1:56" but no Sky Pirates track [Canon].
  - "Castle Royale" is presumably the theme of the 2018 Battle Royale map. SkyVu's video "Battle Bears Gold Battle Royale Map!" (bOEK6skhDKU, 2018-03-28) says: "New Battle Royale Mode and Map coming in update v2.32!" [Canon]. Its thumbnails show a sunny castle with cyan- and red-capped towers on a floating grass island [Observed: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/critic/br2018.jpg].
  - No 2026 frame I opened shows that island or a Battle Royale mode, and Steam lists no BR mode [Observed absence; Canon absence].
  - So the soundtrack's 16 is a music count, not the map count [Inference].
- **One alternative reading survives.** If the "16 wacky maps" line was already on the store page in February 2026, before any Sky Pirates announcement, it could have meant 15 + Castle Royale [Unverified]. The Wayback captures of 2026-02-27 and 2026-08-20 exist but could not be downloaded. Our earliest local copy is from 2026-10-12.

### What would settle it
- A full scroll through PICK LEVEL in the 2026 private-match screen.
- SkyVu's stream shows PICK GAME TYPE / PICK LEVEL at 11:20, 11:40, 12:00, 19:40, 20:00, 28:00, 28:20, 45:20, 45:30, 57:00, 57:10, 77:00 and 91:20, one icon at a time [Observed: zm_create.png]. Left4Dead's stream shows two more icons, at 51:00 (Toxic Terror) and 52:00 (green hills) [Observed].
- The Next Fest demo (from Oct 19) and SkyVu's "Five Nights of Battle Bears" streams (Oct 19–23) are the next chances to see the full list.

---

## 7. 2026 modes per map

### On-screen mode prompts seen [Observed, game text]
- "GET KILLS TO SCORE POINTS FOR YOUR TEAM" (team kills: TDM, also called "Team Battle");
- "GET KILLS TO SCORE POINTS" (FFA);
- "DELIVER THE BOMB TO SCORE POINTS" (PTB);
- "COLLECT ENEMY TAGS TO SCORE POINTS" (Kill Confirmed).

### Kill Confirmed
- It was still in the final build. Observed on:
  - Shortest Parsec: JN 57:00–60:10 [Observed: jn_kc.jpg];
  - Sky View: JN 3:00 [Observed: jn_open.jpg];
  - Sky Pirates: HK 56:16 chapter; "COLLECT ENEMY TAGS" at HK 58:50 [Observed: critic hk_kc.jpg].
- SkyVu's 2nd-playtest post promised "An experimental new gamemode" [Canon]. The name "Kill Confirmed" comes from fan descriptions [Unverified label]. The on-screen tag prompt matches it [Observed].

### Naming and the Steam list
- Steam uses both "Team Battle diehard" and "Team Deathmatch (TDM)" [Canon].
- Steam's three-mode list ("-Team Deathmatch (TDM)-Free for All (FFA)-Plant the Bomb (PTB)") [Canon] therefore leaves out a mode that was still being played on Oct 15 [Inference]. Whether KC ships on Nov 4 is [Unverified].

### Modes per map in 2026
- **Steam Yard Blues:** FFA and team kills [Observed]. PTB [fan label].
- **Desert Airmine:** team kills [Observed]. FFA [fan label plus frames].
- **Haunted Castle:** PTB [fan label plus team HUD]. KC, FFA and TDM [fan labels].
- **Frozen Pundra:** PTB [Observed]. Team Battle [fan label].
- **Toxic Terror:** PTB and FFA [Observed].

---

## Corrections to our notes

1. **Critic gap note for 2026-lineup (this task's brief).**
   - Current text: "Toxic Terror never appears, and the Tutorial appears separately. So 15 legacy maps plus Sky Pirates = 16 fits only if Toxic Terror ships."
   - Correction: Toxic Terror appears in SkyVu's own short (jkv6FHPghx8, 0:30–0:40) and in three final-playtest recordings (MS2wiArCiCA 46:40–56:20; 1MP1rFi4t-Q 37:20–42:10; dz4iqZE8nQE 110:10–114:10). The count closes as 15 + Sky Pirates = 16.
   - Evidence: section 5 sheets.
2. **The critic's sheet /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/critic/eq_fp_syb.jpg / eq_fp_syb2.jpg.**
   - Current: the filename implies Frozen Pundra and Steam Yard Blues.
   - Correction: the non-ice frames (0:40–3:20 and 25:00–30:00) are Sky View, not Steam Yard Blues. They show a yellow tower crane, wooden crate decks and teal tarps under a dusk sky.
   - Evidence: eq_fp_syb2.jpg.
3. **research_notes/Battle Bears character lore/franchise_world.md, line 276.**
   - Current: "[FAN-WIKI] The wiki lists 15 BBG maps across the original run, and Haunted Castle and Desert Airmine were removed at 2.0 and Haunted Castle later returned".
   - Correction: Desert Airmine also returned: "It was re-released in v2.7" [Fan-wiki]. Add that all 15, plus Sky Pirates, appear in 2026 playtest footage, which accounts for "16 wacky maps" [Inference, strong].
4. **research_notes/Battle Bears character lore/franchise_world.md, line 404 (open question).**
   - Current: "Sky Pirates as a BBO map that returns in BBG 2026."
   - Correction: answered. Sky Pirates is playable in 2026 playtests 3–5 [Observed], and SkyVu calls it "the new Sky Pirates map" [Canon].
5. **research_notes/Battle Bears character lore/oliver_riggs_wil.md, lines 252 and 554.**
   - Current: "Whether these are the same map is my [INFERENCE]; no source says so."
   - Correction: SkyVu's "Sky Pirates in BBG!" short (CwxpBZg6Fi4) is described as "Enjoy the highlights from our Sky World playtest!" [Canon]. That ties the two names (animation_reference.md already records it: the Fact-check log's "Added (sourced)" list, and the Q1 section A list of 2026 Shorts).
6. **bbg-news-repo/content/evergreen.json, fact-playtests.**
   - Current: "Four Discord playtests, July to September 2026".
   - Correction: five. Steam news Oct 14: "The next and final BATTLE BEARS GOLD playtest will take place on Thursday 15th October" [Canon].
7. **research_toxic-terror.md, 2026 status.**
   - Current: "The 16-tile grid and the "16 wacky maps" store claim make it likely that Toxic Terror is in the 2026 roster [Inference]. That is not confirmed by SkyVu text."
   - Correction: Toxic Terror is [Observed] in SkyVu's own Oct 11 short and in the Oct 15 build, in PTB and FFA.
8. **research_steam-yard-blues.md, Confidence section.**
   - Current: "Missing: no top-down view, no team-side information, no audio heard, no 2026-build footage."
   - Correction: 2026-build footage now observed (HK 5:20–9:10, 13:40–17:30, 43:50–47:50; JN 28:20–32:40).
   - Also in "Corrections to our notes": current "The other is a crane-and-water map I did not identify." Correction: it is Sky View (grid r4c2; yellow tower crane, teal tarps).
9. **research_frozen-pundra.md, 2026 status.**
   - Current: "The 2026 tile shows lavender snow and a plum-brown rock block where the 2014 tile shows cyan snow and a slate-blue block".
   - Correction: the grid tile is not proven to be 2026 footage, and the actual 2026 build has no lavender. Purple-hue pixels average 0.5–2.6% per recording; the build is cyan and cobalt, #3ED7F9 / #183DC4.
10. **research_haunted-castle.md, Confidence section.**
    - Current: "**2026 status:** unknown."
    - Correction: observed in the Oct 15 build (HK 69:50–74:40 PTB; SkyVu ZM 46:00–50:10). It is darker than 2013 and has an in-game full moon.
11. **research_desert-airmine.md, Look section.**
    - Current: "The 2026 build's lighting is unobserved".
    - Correction: observed as bright daylight, with a powder-blue sky (#9BB9C8 to #AAC6CF), orange-gold sand (#E3AB57) and terracotta canyon walls (#764936 to #825C42).
12. **research_space-oddity.md, open question.**
    - Current: "In "BBG Maps Ranked part 1", is tile row 1, column 3 … a second Space Oddity view or a different map?"
    - Correction: it is Space Oddity. It matches the Spacecraft2.jpg base-deck render (r1c3_cmp.jpg).

## Open questions

1. Does the Nov 4 launch PICK LEVEL list hold exactly these 16 (15 legacy + Sky Pirates)? Is Castle Royale or Battle Royale absent? The Next Fest demo (Oct 19) and SkyVu's Oct 19–23 streams should show a full scroll.
2. Did the store's "16 wacky maps" line exist in the 2026-02-27 Wayback capture, before Sky Pirates was announced? The capture exists but could not be downloaded.
3. Does Kill Confirmed ship at launch, and on which maps? Steam lists only TDM, FFA and PTB.
4. Haunted Castle: are the melee levers and gates still in the 2026 build? Are the gravestone names unchanged?
5. Desert Airmine: does the central drill with Graham's emblem still rise and fall in 2026? It could not be identified at storyboard resolution.
6. Frozen Pundra: are the droppable icicles still in the game? What is the dark-green lit structure: the bomb hole, or a set piece?
7. Toxic Terror: was it absent from playtests 1–4 and added for the final test, as one of SkyVu's "couple of surprises"? My checks of playtests 3 and 4 were sample-based, not exhaustive.
8. What is the full build tag after "3.0.7"? It needs a full-resolution frame.
9. Where does SkyVu's ranking place the other eight classic maps? Part 2 has not been published as of Oct 18.


---

<!-- gap pass 2 -->
# 2026 lineup addendum: the Next Fest demo, the PICK LEVEL carousel, Toxic Terror, Tutorial, Castle Royale and the 2026 display names

This addendum answers one gap: which levels are in the 2026 build, and what are they called in game? The short answers:

- **The Steam Next Fest demo's level list is still unknown.** The demo is not public yet. I checked on 2026-10-18 at 09:09 UTC, one day before it opens.
- **Toxic Terror is in the 2026 build.** This is new, observed evidence:
  - SkyVu's own thumbnail for the final-playtest livestream is a Toxic Terror scene. It carries the 2026 build string.
  - Its tile appears in the custom-match PICK LEVEL carousel in SkyVu's Sep 20 stream and in a fan's Oct 15 stream.
  - That fan then played two Toxic Terror custom matches.
- **All 16 maps are now accounted for in the 2026 builds.** The 15 legacy BBG maps plus Sky Pirates/Sky World have each been seen in 2026 builds, which matches "16 wacky maps" [Inference, strong]. No SkyVu text lists all 16.
- **"Castle Royale" is not a 2026 map in any evidence.** It most plausibly names the music of the 2018 Battle Royale castle map [Inference].
- **The 2026 in-game display names are still unconfirmed.** In the frames I could open, the level tiles carry no name text.

## Sources: what I could reach and what I could not

**Reachable:**
- **Steam:** the store API for the demo (5225670), the game (4408320) and the soundtrack (5321720), re-fetched 2026-10-18 09:09 UTC. Also the Steam News API, the soundtrack's store HTML with its track list, and the image of the final-playtest Steam post.
- **SkyVu's own sites:** battlebears.com and the sign-up page play.battlebears.com, via the battlebears.com/signupyt redirect.
- **SkyVu's YouTube channel:** the RSS feed, the channel tabs, and the innertube player metadata for scheduling.
- **YouTube images:** thumbnails (maxres*) and **storyboard stills**. Storyboards are 320×180 YouTube-generated frames, one every 10 s. They were downloaded by earlier sessions, and I opened them as contact sheets and zooms. **I did not watch any video.** Every "Observed" video claim below comes from a storyboard still or a thumbnail at the timestamp given.
- **Fan wiki:** through its MediaWiki API (search, parse, imageinfo).

**Not reachable:**
- the demo's store text and screenshots, which are not published yet;
- YouTube watch pages, which return Google "sorry" bot-walls;
- the innertube player storyboards, which say LOGIN_REQUIRED or UNPLAYABLE;
- Invidious: the f5.si instance returned "Error while communicating with Invidious companion", and the other instances returned 403, 401 or "disabled".

So no new storyboard sets could be downloaded this session. I used the sets that earlier sessions saved.

**Frame keys used below.** All are YouTube storyboard stills, 10 s apart. The full paths are in "Images viewed".
- **ZM**: SkyVu, "BBG Livestream Final Playtest before Steam NextFest Oct 19" (ZMhLVXWT6OY). It streamed 2026-10-15 22:19 to 2026-10-16 00:02 UTC, per the player API. 620 stills.
- **EJ**: SkyVu, "BBG Livestream Sunday" (ejjsoKQ-VXU), 2026-09-20. 358 stills.
- **L4D**: fan Left4Dead, "Battle Bears Gold FINAL PLAYTEST" (MS2wiArCiCA), streamed 2026-10-15. 384 stills.
- **HK**: fan InstableGR, "Battle Bears Gold - Final PC Playtest (10/15/26)" (HKbwq7PolNc). 465 stills.
- **JN**: fan JustNubz, "Battle Bears Gold FINAL PLAYTEST" (1MP1rFi4t-Q). 596 stills.
- **IPAD**: fan Vada Zora Reva Nova, "…Final Playtest Session Before Release! (iPad Gameplay!)" (dz4iqZE8nQE). 760 stills.
- **BR18**: SkyVu, "Battle Bears Gold Battle Royale Map!" (bOEK6skhDKU), 2018. 21 stills, 1 s apart.

---

## 1. The Steam Next Fest demo (Steam app 5225670)

**Official text and status:**
- The store API, fetched 2026-10-18 09:09 UTC, gives:
  - name "BATTLE BEARS GOLD Demo", type "demo", "is_free": true;
  - "release_date": {"coming_soon": true, "date": "October 2026"};
  - empty "detailed_description", "about_the_game" and "short_description";
  - no screenshots and no movies;
  - platforms windows true, mac false, linux false;
  - categories including "Game demo", "Cross-Platform Multiplayer" and "Partial Controller Support" [Canon]. Saved at /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/steam/app_5225670.json.
  - The JSON is byte-identical to the Oct 16 snapshot [Observed: cmp].
- The demo's Steam News feed is empty ("newsitems": []) [Canon by absence].
- https://store.steampowered.com/app/5225670 redirects (1 hop) to https://store.steampowered.com/app/4408320, the full game's page, so the demo page is not public yet [Observed: curl effective URL].
- The demo header art shows the BATTLE BEARS GOLD logo and the eleven-bear lineup in front of fire, with Steam's demo badge. **No map is shown** [Observed: demo_header.jpg].
- Sign-up page (battlebears.com/signupyt → play.battlebears.com): "Play the demo on Steam from October 19-26" [Canon].
- SkyVu's ZMhLVXWT6OY description: "conduct the final playtest ahead of Steam Next Fest Oct 19-21" [Canon].
- On-screen overlay in that stream: "FIVE NIGHTS OF BATTLE BEARS / OCT 19 - 23 LIVE EVERY NIGHT / 6PM ET BATTLE HOUR / WATCH LIVE ON STEAM / BattleBears.com/Steam" [Observed: ZMhLVXWT6OY_maxres1.jpg and maxres2.jpg].
- The scheduled stream "Steam Next Fest Demo Party with BBG Devs" (Sf01OOF_X3Q) is described as "Join Ben and Gold44 in BATTLE BEARS GOLD Demo as they kick off Steam Next Fest with the BB community!" [Canon]. Player API: "isUpcoming": true, "startTimestamp": "2026-10-19T21:00:00+00:00" [Observed metadata].
- Fan InstableGR (HKbwq7PolNc description): "a public demo will be available on Steam for a few days starting October 19th as part of Steam Next Fest" [Unverified: fan text].

**Date conflict:** SkyVu gives three windows: "Oct 19-21" (stream description), "Oct 19 - 23" (nightly streams overlay) and "October 19-26" (sign-up page) [Canon]. The likeliest reading is that the demo runs Oct 19–26, the nightly streams run Oct 19–23, and "Oct 19-21" is a slip or refers only to the Next Fest kickoff [Inference]. This is not settled.

**Demo level list: unknown.** Nothing published names the demo's levels [Unverified]. Re-check on or after 2026-10-19 21:00 UTC, when the store text, the demo screenshots and the "Demo Party" storyboard should exist.

## 2. The custom-match PICK LEVEL carousel in the 2026 build

**The UI** [Observed: ZM 11:20–11:40, 19:40–20:00, 27:40–28:20, 45:20–45:40, 56:50–57:10, 1:17:00–1:17:10, 1:31:20–1:31:30; EJ 8:10–8:40; L4D 45:50–46:10, 51:00]:
- The CUSTOM MATCH panel has the fields "ARENA NAME:", "PASSWORD: (OPTIONAL)", "PICK GAME TYPE:" and "PICK LEVEL:", with "CREATE" and "CANCEL" buttons. A separate panel offers "SEARCH" and "JOIN".
- Each picker is one square image tile between two large green arrow buttons.
- After CREATE, the room panel shows the mode tile above the level tile, beside the player list, with "PLAY" and "CANCEL".
- The SkyVu build string on the main menu reads "3.0.7 2026.11.19 b7" [Observed: ZMhLVXWT6OY_maxres1.jpg]. The official thumbnail reads "3.0.7_2026.11.19_b7" [Observed: ZMhLVXWT6OY_maxresdefault.jpg].

**The tiles carry no visible name.** At storyboard resolution, the level tiles show no text [Observed]. The tile images match the text-free stills of SkyVu's "BBG Maps Ranked part 1" grid (see below), so the 2026 tiles are probably unlabelled art [Inference]. The 2013 wiki tiles, by contrast, had names baked in (e.g. "SPACE ODDITY", "HAUNTED CASTLE") [Observed: wiki File:Space_Oddity.png, File:HauntedCastle_Preview1.png].

**Tiles identified.** I compared each carousel tile crop with the 16 tiles of the "BBG Maps Ranked part 1" grid. The method: 20×20 blurred RGB vectors, ±5 px jitter, correlation computed by script, using /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/scripts_2026lineup/tilematch.py. I then checked every crop by eye.

| Carousel still | Video | Best grid match (r) | Runner-up r | What it is |
|---|---|---|---|---|
| ZM 11:20, 19:40, 28:10, 56:50, 57:10, 1:17:00, 1:31:20; EJ 8:10–8:30; L4D 45:50 | SkyVu / fan | r1c1, 0.94–0.98 | ≤0.59 | **No Bear's Land** (green hills, bunkers). This is the tile shown whenever the dialog opens [Observed; "default" is Inference] |
| ZM 11:30, 20:00; L4D 46:00 | SkyVu / fan | r1c3, 0.96–0.98 | ≤0.61 | **Space Oddity** (amber windows, cyan ceiling disc). After the tile at ZM 20:00, the room at 20:10 shows this tile and the match at 21:10–25:00 is Space Oddity (amber starfield windows, cyan lights, octagonal pillar) [Observed; ID Inference]. The same interior appears in HK 18:00–20:40, which InstableGR labels "Space Oddity" [Observed] |
| ZM 19:50 | SkyVu | r2c4, 0.88 | 0.53 | **Shortest Parsec** (station in a starfield) |
| ZM 28:20 | SkyVu | r1c2, 0.82 | 0.45 | **H.I.P. Test Lab** (pink-lit wall, tubes). The match at 29:20–33:20 is the white-and-pink lab [Observed; ID Inference] |
| ZM 45:20, 1:17:10 | SkyVu | r2c2, 0.92–0.93 | ≤0.70 | **Abusement Park** (striped storefront). The match at 1:17:40–1:21:40 is the carnival: striped tents, wood floors, a "PEEPER" sign at 1:19:50, "NO ENTRY" at 1:21:40 [Observed] |
| ZM 45:30 | SkyVu | r4c3, 0.85 | 0.63 | **Gold Digger** (rock wall under stars) |
| ZM 45:40 | SkyVu | r2c3, 0.93 | 0.49 | **Haunted Castle**. The match at 46:00–50:10 is a dark night map with a moon (49:30) and red banners (48:40) [Observed; ID Inference] |
| EJ 8:40; L4D 46:10, 51:00 | **SkyVu** (Sep 20) / fan (Oct 15) | r4c4, 0.87–0.91 | ≤0.69 | **Toxic Terror** (dark room, amber lamps, glowing green floor pool) |
| ZM 11:40, 57:00, 1:31:30; EJ room panel 8:50 | SkyVu | no grid tile (score falls back to r1c1 at 0.76–0.82, driven by the green) | — | **Sky Pirates/Sky World**: red-orange autumn trees, a white tower, pale sky [Observed]. The match at 12:30–16:30 and 1:32:10–1:36:20 is the autumn island village with ships [Observed] |

- **Seen in the carousel:** 9 distinct level tiles.
- **Not seen in any sampled carousel still:**
  - Aztec Attack, Desert Airmine, Marecraft, Steamyard Blues, Frozen Pundra, Skate or Die and Sky View [Observed absence, sampled only]. All seven were played in 2026 builds (§3).
  - the Tutorial (§5) and anything castle-island-like (§6).
- **Order and count:** the 10-s spacing means several arrow clicks can fall between stills. The order cannot be read off. For example, NBL→Space Oddity→Sky Pirates at ZM 11:20–11:40, but NBL→Shortest Parsec→Space Oddity at ZM 19:40–20:00 [Observed; order Unverified].

**What the "BBG Maps Ranked part 1" grid really is.** SkyVu's short jkv6FHPghx8 (Oct 11, 2026) has a 4×4 grid [Observed: jk_grid_big.png].
- Eight of its tiles are the same images as the 2026 PICK LEVEL tiles (r 0.82–0.98, table above). So the grid is the game's level-select tile art, wherever the grid was first assembled [Inference, strong].
- The grid does **not** contain Sky Pirates.
- It contains **Space Oddity twice**:
  - r1c3 is the 2026 carousel tile;
  - r3c3 is the 2013 render, the same picture as wiki File:Space_Oddity.png minus the name text [Observed: wiki_vs_ranked.jpg].
- So the grid shows 15 unique legacy maps, with Space Oddity as both the 1st-row and 3rd-row tile [Inference]. It is not evidence for "15 legacy + 1 new = 16".

**Other things in the custom-match area** [Observed: EJ chat, ej_chat.jpg; JN 1:25:30]:
- Chat lines read "GOLD44 JOIN MY ROOM: SKY WORLD" (EJ 8:20–8:40) and "Aar_venom: Join my room: sky pirates" (JN 1:25:30).
- These are free-text arena names announced to chat. Others in the same chat are "BBU", "AAR", "YERRR" and "BEST GAME!". They are **not** level display names, though they show that SkyVu's co-host says "Sky World" and fans say "Sky Pirates" [Inference].

## 3. Every 2026 map, with the strongest evidence for each (16 = 15 legacy + Sky Pirates)

Fan chapter titles are the fans' own labels [Unverified as to naming]. I read them from the video descriptions.

| Map (spelling as in the store/soundtrack) | Strongest 2026-build evidence |
|---|---|
| No Bears Land | Store text [Canon]. Carousel tile; SkyVu stream match ZM 57:40–1:02:50 [Observed]. Shown in the "CLOSED TESTING 5" Steam post image: bunkers stencilled "PMOC 20-11", sandbags, green hills [Observed: news_final.jpg]. Fan #2, #3 and final chapters |
| Gold Digger | Store text [Canon]. Carousel tile ZM 45:30 [Observed]. Final, Match 8 |
| Space Oddity | Store text [Canon]. Carousel tile; SkyVu match ZM 21:10–25:00 [Observed]. #3 and final |
| Steamyard Blues | Store text [Canon]. #2 (PTB), #3 (Kill Confirmed), final (FFA, Team Battle, FFA) |
| Huggable Factory (soundtrack) / H.I.P. Test Lab (wiki) | Carousel tile; SkyVu match ZM 29:20–33:20 [Observed]. #2, Match 12 "H.I.P. Test Lab" |
| Abusement Park | Carousel tile; SkyVu match ZM 1:17:40–1:21:40 [Observed]. #3, Match 12 |
| Haunted Castle | Carousel tile; SkyVu match ZM 46:00–50:10 [Observed]. #2 and final, Match 17 |
| Shortest Parsec | Carousel tile ZM 19:50 [Observed]. #3, final; JustNubz _R4rvvGlRsM "7:55 Shortest Parsec TDM" |
| **Toxic Terror** | SkyVu's official thumbnail [Observed]. Carousel tile in SkyVu's EJ 8:40 and in L4D [Observed]. Two L4D custom matches (§4) [Observed] |
| Sky Pirates / Sky World (new) | Steam news "New Map: Sky World" [Canon]. Carousel tile; SkyVu matches [Observed]. #3, final |
| Aztec Attack | #2 Match 1 (Kill Confirmed); #3 Match 11 (PTB) |
| Marecraft | #2 Matches 2, 9, 11; final Match 16; _R4rvvGlRsM "1:08 Marecraft TDM" |
| Frozen Pundra | #2, #3, final (PTB) |
| Skate or Die | #2 Match 7; _R4rvvGlRsM "14:04 Skate or Die FFA". SkyVu's own EJ thumbnails maxres2/maxres3 show a skate park with ramps and graffiti [Observed; ID Inference] |
| Sky View | #3 Match 6 (PTB); final Match 10 |
| Desert Airmine | Final Matches 1, 3, 15; _R4rvvGlRsM "19:59 Desert Airmine FFA" |

**Conclusion:**
- All 15 legacy BBG maps plus Sky Pirates/Sky World have been seen in 2026 builds, matching "compete with friends across 16 wacky maps" [Canon text; count match Inference, strong].
- No SkyVu text lists the 16.
- The store names only No Bears Land, Gold Digger, Space Oddity and Steamyard Blues [Canon].
- **Modes:** the store lists "Team Deathmatch (TDM)", "Free for All (FFA)" and "Plant the Bomb (PTB)" [Canon]. The playtests also ran "Kill Confirmed" [Unverified fan chapter labels]. The HUD text "YOU'RE ON TEAM RED / COLLECT ENEMY TAGS TO SCORE POINTS" (ZM 12:30) and the "DENIED" tag callouts (ZMhLVXWT6OY_maxres3.jpg) back this up [Observed].

## 4. Toxic Terror in 2026 (new evidence and the 2026 look)

### Official text
- 2026 soundtrack, track 14: "Toxic Terror", 1:18 [Canon] (Steam 5321720 store HTML, re-read 2026-10-18).
- No 2026 store copy, Steam post or SkyVu video title names the map [Canon by absence].

### Era and status
- Added in BBG 2.3, September 2013 [Fan-wiki].
- **In the 2026 build** [Observed]:
  - SkyVu's final-playtest thumbnail (ZMhLVXWT6OY maxresdefault) is a Toxic Terror view, overlaid with "FINAL PLAYTEST LIVESTREAM / THURSDAY, OCT 15 / 3PM PDT / 6PM EDT". It carries the build string "3.0.7_2026.11.19_b7".
  - Its tile is in the PICK LEVEL carousel in SkyVu's own Sep 20 stream (EJ 8:40, r 0.87) and in L4D's Oct 15 stream (46:10, 51:00).
  - L4D played Toxic Terror at L4D 46:40–50:30 and 52:40–56:30. The red/blue scoreboard (L4D 54:00) shows a team mode; which one is unreadable.
- **Why the fan chapters missed it:** sampling. No InstableGR or JustNubz upload happens to include a Toxic Terror match [Inference]. A colour scan of the HK and JN storyboards found no Toxic Terror-like runs [Observed by script; the JN candidates turned out to be a dark cave map, jn_cand.jpg].
- **Demo inclusion:** unknown [Unverified].

### Look in the 2026 build
The main source is SkyVu's 1280×720 thumbnail. It is a marketing image, so its grade may differ from live play. The fan values come from 320×180 JPEG storyboards. Treat all hex values as ±10%.
- **Floor grate:** a large square-grid grate glowing yellow-green from below. Grid lines are #2D760D, brightest #449924; on the far grate #165508 [Observed, sampled].
  - This is a deeper, more yellow-green than the 2013 mint and lime glows in our Toxic Terror dossier (#4BFE82, #53FC23) [Observed comparison].
  - The final playtest lists "LIGHTING, EFFECT & TEXTURE IMPROVEMENTS" [Canon: news_final.jpg]. A fan says lighting was "overhauled… for all maps, attempting to restore what they looked like back in the day" [Unverified: HK description].
- **Shell:**
  - walls #091203
  - floor #172D04
  - ceiling #193305 to #3C5D0C [Observed, sampled]
- **Lamps:**
  - caged amber wall lamps: core #FED913 / #FEFC1B, rim #CD820A
  - a red capsule warning lamp on the left pillar: #CB0502 to #ED140D [Observed]
- **Signs and poster:**
  - a red octagonal "STOP" sign, readable in the thumbnail, dimmed to #420F02–#653A0C by the green light;
  - a tall round-topped poster on a pillar with a circular emblem and four short text lines (illegible), under green light (#203606–#2D530C);
  - a small orange, smiling, bear-like face to the left of the poster [Observed: zm_thumb_poster.jpg, zm_thumb_right.jpg].
- **Fan stills** [Observed: l4d_tt_full.jpg]:
  - an oval "DANGER" sign above an amber lamp beside the glowing grid (48:10);
  - a tilted "CAUTION" sign (49:10);
  - a "STOP" sign over the grid (52:50);
  - walls washed deep blue-violet, about #10085C, brightest #1908C9 (46:50–47:30);
  - red-lit zones, about #580809, brightest #B81119, beside green chain-link-like grids (53:10–53:20);
  - a glowing green grated pool, about #18740B, brightest #5CDA51 (53:30).
- **Not seen in any 2026 still:** the central tree, the "O+A" carving, the Ninja Turtle weapon rack and the chalk drawings [Unverified for 2026].

### Hazards, easter eggs, sound
- Nothing new for 2026 [Unverified].
- The 2026 menu jukebox lets players play songs and, per a fan, "assign them to maps" [Unverified: HK description]. The jukebox itself is shown in §7.

### Prompt pack: Toxic Terror, 2026 look (environment only, 9:16)

"Vertical 9:16 low-angle establishing shot inside a dark underground sewer junction.
- **Foreground:** a wide square-grid floor grate glowing saturated yellow-green from below. Lines run #2D760D to #449924, and their light spills up onto dark olive concrete (#172D04).
- **Midground:**
  - curved near-black walls (#091203);
  - caged amber wall lamps with hot yellow cores (#FED913) at head height;
  - a red octagonal stop sign with no readable lettering, dimmed brown by the green light;
  - a tall round-topped poster with a pale circular emblem on a pillar;
  - a red capsule warning lamp (#CB0502) on the near-left pillar.
- **Background:** overhead pipes and beams fading into darkness. One far wall is washed deep blue-violet (#10085C) and another dull red (#580809).
- No characters, no readable text or logos."

Marked details:
- The overall composition follows the official thumbnail [Observed].
- The blue-violet and red washes come from fan stills [Observed].
- The "damp sheen" on the concrete and any haze in the air are [BBG News invention].

**Staging spots:**
1. **The glowing grate under the STOP sign.** This is the official thumbnail's own framing [Observed]. Use it for a "character steps into the light" reveal.
2. **The DANGER-sign lamp corner by the grid edge** [Observed: L4D 48:10]. Use it for a whispered ambush or a team huddle.
3. **The blue-violet corridor** [Observed: L4D 46:50–47:30]. Use it for a chase. A "colour shift from blue to green as the hero enters the junction" is [BBG News invention].

### Confidence
- Observed for 2026 presence and for the palette of the thumbnail view.
- Partial for layout.

## 5. Tutorial in 2026

- **Still in the final-playtest build** [Observed]:
  - The Options panel has a "TUTORIAL" button, beside "SIGN OUT", "FULL SCREEN", "WINDOWED MODE" and "CHANGE NICKNAME" (ZM 34:00; JN 1:25:20).
  - SkyVu plays the course at ZM 34:10–34:30 and 1:25:00–1:28:40.
  - Fan HK 1:15:00 shows an end-of-test notification: "THANKS FOR TESTING, WE WILL SEE YOU ON THE NEXT TEST! 3D 14:50:41 PLAY TUTORIAL".
  - The Tutorial was **not** seen as a PICK LEVEL tile [Observed absence, sampled]. So it is reached from Options and that prompt, not from the level carousel [Inference].
- **2026 signage uses PC key prompts** [Observed: zm_tutorial.jpg]:
  - "MOVE W A S D / JUMP SPACE"
  - "SHOOTING" with a mouse icon
  - "TEAM COLORS"
  - "JUMP PADS"
  - "OPTIONS ESC"
  - "POWER UP" beside a purple vertical beam (#A13CA6) at 1:27:40.
  - The run ends at a green wireframe ship (1:28:40).
- **Palette:** neon green #41D02C, dim green #0B5406, near-black void #031602, amber sign #C98941 [Observed, sampled from ZM stills].
- **Soundtrack:** track 18 "Tutorial", 0:32 [Canon].

## 6. "Castle Royale" (soundtrack track 16)

- **Official text:** soundtrack track list "16 Castle Royale 1:56", placed between the 15 map themes and "17 Main Menu (BBG)" [Canon] (Steam 5321720 store HTML, re-read 2026-10-18). The fan wiki has no page or text hit for "Castle Royale" [Observed: API search].
- **Best lead: the 2018 Battle Royale castle map.**
  - SkyVu's video "Battle Bears Gold Battle Royale Map!" (Mar 28, 2018) has the description "New Battle Royale Mode and Map coming in update v2.32! See you on the battlefield." [Canon].
  - Its storyboard (BR18 0:00–0:20) shows the map [Observed: br2018.jpg]:
    - a floating grassy island above clouds;
    - a large brick-stone castle whose towers have teal crenellation caps on one side and red caps on the other;
    - hedge rows, picket fences, a graveyard with headstones, and dirt paths.
  - The wiki's 2.50 splash ("The splash screen for the Battle Royale update in 2.50") shows blue- and red-topped castle towers and a graveyard fence behind a robot panda [Observed: br_splash.jpg; caption Fan-wiki].
  - The wiki's Updates table has 2.50 (April 5, 2018), "New Battle Royale mode implented. Winners in gas", and 2.53, "Bridge to Terabearthia added to the Battle Royale mode." [Fan-wiki].
- **So:** "Castle Royale" is most plausibly that castle map's music [Inference; Unverified].
- **2026 status:**
  - No Battle Royale mode is in the 2026 store mode list [Canon by absence].
  - No castle-island tile appears in any carousel still [Observed absence, sampled].
  - So the track is a legacy cue, not evidence of a 2026 level [Inference].
- **Palette of the 2018 map** (from 160×90 stills, so rough): sky #396F9E, grass #78AB54, hedges #3B5A1F, stone #A19A9F, teal caps #4F819A, red caps #A31D49, dirt path #A7725C [Observed, sampled].

## 7. The 2026 display names: what is known

| Map | Official 2026 spellings | In-game 2026 evidence | Status |
|---|---|---|---|
| H.I.P. Test Lab | Soundtrack: "Huggable Factory" (track 5) and "Huggable Factory (Full Version)" (track 21) [Canon] | The main-menu jukebox panel reads "NOW PLAYING: Huggable Factor…", cut off [Observed: HK 1:16:50, hk_nowplaying.jpg]. That is the **music** name. The level tile shows no name [Observed] | Map display name unconfirmed |
| Sky Pirates / Sky World | Steam news Aug 19: "New Map: Sky World". YouTube: "Sky Pirates Map Reveal" and "Sky Pirates in BBG!" ("highlights from our Sky World playtest") [Canon] | The tile shows no name. Co-host Gold44's room is named "SKY WORLD"; fans name rooms "sky pirates" [Observed, free text]. No soundtrack track [Canon by absence] | Unconfirmed |
| Steamyard Blues | Store and soundtrack: "Steamyard Blues" [Canon]; 2014 video title: "Steam Yard Blues" [Canon] | None visible | Unconfirmed |
| No Bears Land | Store and soundtrack: "No Bears Land" (no apostrophe) [Canon] | None visible | Unconfirmed |

- The jukebox labels differ from the soundtrack titles. The jukebox shows "Menu Theme - BBG" and "Menu Theme - BBR", where the soundtrack has "Main Menu (BBG)" and "Main Menu (BBR)" [Observed: ZMhLVXWT6OY_maxres1.jpg and maxres2.jpg; HK 1:15:10]. So soundtrack titles are **not** reliable proxies for in-game strings [Inference].
- Other jukebox entries [Observed: hk_jukebox.jpg, HK 1:15:10–1:16:40]:
  - "RANDOM", "Bear With Me", "The Right to Bear Arms", "Tentacles!", "I'm a Battle Bear (Sleepy Mix)" and "Jungle Theme";
  - locked entries gated by quests such as "Get 50 Kills with Huggable 34/50" and "Win 100 Matches 12/100".

## Images viewed

All local paths are absolute. The storyboard stills were saved by earlier sessions; I opened them through the contact sheets and zooms below.

**Official (SkyVu and Steam):**
- https://i.ytimg.com/vi/ZMhLVXWT6OY/maxresdefault.jpg → /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/yt/th/ZMhLVXWT6OY_maxresdefault.jpg
- Crops of it: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/zm_thumb_poster.jpg and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/zm_thumb_right.jpg
- https://i.ytimg.com/vi/ZMhLVXWT6OY/maxres1.jpg → /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/yt/th/ZMhLVXWT6OY_maxres1.jpg
- ZMhLVXWT6OY maxres2 and maxres3, and ejjsoKQ-VXU maxresdefault, maxres1, maxres2 and maxres3, viewed together as /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/stream_maxres.jpg
- ZM storyboard contact sheets (all 620 stills, source folder /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/gold_digger_verify/yt/sb/ZMhLVXWT6OY/):
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/sheets/zm_00.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/sheets/zm_01.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/sheets/zm_02.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/sheets/zm_03.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/sheets/zm_04.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/sheets/zm_05.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/sheets/zm_06.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/sheets/zm_07.jpg
- ZM zooms:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/pick_tiles.jpg (also holds the L4D and EJ tile crops)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/zm_pick2.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/zm_rooms.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/zm_so.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/zm_tutorial.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/zm_3400.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/zm_steam.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/zm_steam2.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/zm57_check.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/tilecrops_check.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/tiles_compare2.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/tt_tile_compare.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/loading.jpg
- EJ (stills in /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/lineup_gap/sb/ejjsoKQ-VXU/):
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/ej_after.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/ej_chat.jpg
- SkyVu "BBG Maps Ranked part 1" grid (crop of https://i.ytimg.com/vi/jkv6FHPghx8/oar1.jpg made by an earlier session): /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/gold_digger_verify/yt/jk_grid_big.png
- BR18 storyboard (stills in /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/critic/sb/bOEK6skhDKU/): /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/br2018.jpg
- Steam demo header: https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/5225670/15df8f256915d48c4b0bd9370514a9334309f866/header.jpg → /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/steam/demo_header.jpg
- Final-playtest Steam post image: https://clan.akamai.steamstatic.com/images/46006015/b7c8f8f133ad960899cce9f3d232b42847891d08.png → /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/steam/news_final.jpg

**Fan wiki:**
- Battle Royale update splash, local file /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/environment-conventions/img/Battle_Bears_Royale_Battle_Royale_Update.png, viewed as /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/br_splash.jpg
- Space_Oddity.png, Shortest_Parsec.png, Gold_Digger.png and HauntedCastle_Preview1.png (static.wikia.nocookie.net URLs from imageinfo), viewed against the grid as /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/wiki_vs_ranked.jpg

**Fan videos (storyboards):**
- L4D (stills in /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/lineup_gap/sb/MS2wiArCiCA/):
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/sheets/L4D_02.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/l4d_tt_full.jpg
- HK (stills in /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/gold_digger_verify/yt/sb/HKbwq7PolNc/):
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/hk_ref.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/hk_so.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/hk_jukebox.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/hk_nowplaying.jpg
- JN: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/jn_cand.jpg
- IPAD: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/ipad_part.jpg

**Not viewed (the image request limit blocked them; nothing above relies on them):**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/environment-conventions/sheets/ej_custom.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/lineup_gap/l4d_pick.jpg, l4d_tt_a.jpg, l4d_tt_b.jpg and l4d_all_0.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/zoom/l4d_mm.jpg, l4d_create.jpg and tt_vs_l4d.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/gold_digger_verify/yt/jk_oar1.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/2026-lineup/sheets/JN_00.jpg to JN_04.jpg, IPAD_00.jpg to IPAD_06.jpg, L4D_01.jpg and L4D_03.jpg

**Analysed by script only:**
- the tile correlations (/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/scripts_2026lineup/tilematch.py);
- the Toxic Terror colour scan (/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/scripts_2026lineup/ttscan.py);
- the palette samples (/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/scripts_2026lineup/samp.py and inline numpy).

## Confidence

| Item | Confidence | Why |
|---|---|---|
| Demo level list | Unknown | Not published as of 2026-10-18 09:09 UTC |
| Toxic Terror in the 2026 build | Observed | Official thumbnail, SkyVu stream carousel and fan matches. Map identification is Inference, but strong |
| PICK LEVEL carousel contents | Partial | 9 tiles seen; order and total not seen |
| The 16-map roster | Partial, strong | Every map seen in a 2026 build; no official list |
| Display names | Unknown | No in-game name strings visible |
| Castle Royale | Partial | The Battle Royale castle link is Inference |

## Corrections to our notes

1. **Toxic Terror is in the 2026 build.** research_toxic-terror.md (repo and scratch copies) line 64 currently says the grid and the "16 wacky maps" claim make it "likely", unconfirmed by SkyVu. The correction: SkyVu's own final-playtest thumbnail shows the map; its tile is in SkyVu's Sep 20 PICK LEVEL carousel; and a fan played it on Oct 15. Only a SkyVu text naming it is still missing.
2. **The tile is not an old capture.** research_toxic-terror.md line 65 suggests the tile "may be an old capture". The same image is the 2026 in-game PICK LEVEL tile (r 0.87–0.91).
3. **Space Oddity's open question is answered.** research_space-oddity.md line 346: r1c3 is Space Oddity's 2026 PICK LEVEL tile. So the Maps Ranked grid holds Space Oddity twice.
4. **"15 + 1 new" does not hold for the grid.** research_frozen-pundra.md line 220, research_gold-digger.md line 56 and research_skate-or-die.md line 84 read the 16 grid tiles as "15 legacy + 1 new" or as "16 wacky maps". The grid holds 15 unique legacy maps and no Sky Pirates. The 16 count rests instead on 2026 build evidence.
5. **The grid is the level-select art.** research_marecraft-map.md line 46 calls the grid a possible "older community collage". Its tiles are the 2026 level-select art.
6. **H.I.P. Test Lab naming.** research_h-i-p-test-lab.md line 56: add the jukebox "Huggable Factor…" music label and the absence of any tile name.
7. **Castle Royale lead.** research_haunted-castle.md line 187: add the 2018 Battle Royale castle map as the "Castle Royale" lead.
8. **Tutorial status.** research_tutorial.md line 85: it is present in the Oct 15 build too.
9. **Map count.** franchise_world.md line 276: add the 2026-build roster evidence.
10. **Platforms (outside map scope).** The lore report line 29 says "Steam (Windows and Mac)". Steam lists Windows only.

Exact text, corrections and evidence are in the corrections list.

## Open questions

See the open-questions list. The main ones:
- Which levels are in the Oct 19–26 demo?
- What is the full order and count of the carousel?
- What are the in-game display names?
- Is Castle Royale the Battle Royale castle, and does any Battle Royale content ship?
- Do the Toxic Terror tree, the "O+A" carving and the weapon rack survive the 2026 lighting and texture pass?