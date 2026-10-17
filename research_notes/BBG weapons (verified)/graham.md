# Graham (Engineer): BBG weapons dossier (verified edition)

Graham is BBG's Engineer. The wiki calls the class "a defensive class, due to dependence on static weapons for support on the field" with "relatively slow movement speed" [Fan-wiki: Engineer (BBG)]. The wiki's class template carries this blurb: "Don't be fooled by his bushy gray mustache, this class relies more on brains than brawn or speed. This wise whiskered bear specializes in defending areas of the map and controlling enemy traffic." [Fan-wiki: Template:Class:Engineer (BBG); probably the in-game class text, Unverified]. Class stats on that template: health 120, forward speed 250, price 100 Gas [Fan-wiki]. 2.6 raised "Base speed ... to 250 from 200" [Fan-wiki: Versions/2.6].

His BBG arsenal is **17 weapons**: 6 primaries, 7 secondaries and 4 melees [Fan-wiki: Engineer (BBG) weapon list, re-read Oct 17, 2026]. `weapons_by_class.json` holds only 15. MuskIt and Bind Field are missing because their pages lack Category:BBG Weapons [Fan-wiki; checked]. None of the 5 `_unassigned` pages (Adrenaline Gun, Catastrophe, ClubCobra, Hazard Toy, The Incredible Riggs) is Graham's.

**Sources reached (Oct 17, 2026)**
- **Fan wiki:** reached through the MediaWiki API: all 17 weapon pages, the class page and template, Status Effects, Updates, Versions/2.6, BBR 1.4.2 and 1.4.3, Bundle Deals, Instagraham, Old School, Electric Honey (BBG), Graham (Hero), Graham (BBO), Dragon Slayzer (BBO) and Black Hole Shot. I also read the early revision histories of 14 weapon pages and the file metadata.
- **Steam appdetails (app 4408320):** it names no Engineer weapon. It lists "-ENGINEER: Graham" and "80+ PRIMARY WEAPONS / 60+ SECONDARY WEAPONS / 50+ MELEES". Its only movie is "Battle Bears Gold Premium - Trailer", with release date "Nov 4, 2026" [Canon].
- **battlebears.com/pages/characters:** BBH-era text only [Canon].
- **YouTube:** I used oEmbed titles, the innertube "next" endpoint (titles, descriptions, date text, chapter thumbnails) and static thumbnails. The player endpoint returns LOGIN_REQUIRED. I watched no video. Every video claim comes from one thumbnail or chapter frame that I opened.
- **Not reachable:** web.archive.org reset all 3 curl attempts, and WebFetch refuses archive.org. SkyVu's archived "battle-bears-gold-2-6-change-log" is unverified, so every "2.6 change" below is the wiki's transcription [Fan-wiki].

**Era key**
- BBR v1.4 (Nov 28, 2012): Graham launches "complete with 6 original weapons" [Fan-wiki: Updates, transcribing App Store notes].
- BBR 1.4.2 (Feb 28, 2013): "The game has officially been renamed to simply *Battle Bears*" [Fan-wiki: BBR Version 1.4.2].
- BBG 1.0 (May 24, 2013) [Fan-wiki: Updates]. SkyVu's own description calls BBG "an all new app, featuring a slew of new content with all of the existing BATTLE BEARS content you've come to love" [Canon: rfAyqVJrli4 description]. So it was a new app carrying over BBR content, not a simple rename.
- BBG 2.x updates run to 2.53.3 (Aug 31, 2018). Then come 3.0 (Nov 15, 2021) and 3.0.1 (Dec 18, 2021) [Fan-wiki: Updates].
- BBG re-release on Steam: Nov 4, 2026 [Canon: Steam]. BB Heroes (2024) is a different game.

**Two big caveats**
1. **The Steam trailer mixes 2013 art with gameplay of unsettled date.**
   - The "Graham / ENGINEER" card (10.75–12.0 s) is identical to the card in SkyVu's "BATTLE BEARS GOLD Trailer: Award-Winning Multiplayer Shooter Game" (rfAyqVJrli4, channel "BATTLE BEARS", date text "May 30, 2013") [Observed: https://i.ytimg.com/vi/rfAyqVJrli4/hq1.jpg vs /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/graham-verify/frames/f_11.00.png; Canon: oEmbed and YouTube metadata].
   - The Graham gameplay before the card (7.25–10.5 s) draws thick black toon outlines. No 2012–2015 in-game image I checked has them, while the May 2018 Dragon Slayzer render and the 2026 playtest thumbnails do [Observed: compare sheet /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/graham-verify/sheets/outline_cmp.png]. So the footage is probably a 2018-or-later capture [Inference]. The 2013 card art also uses outlines, though, so a 2013 trailer render cannot be ruled out [Unverified].
   - Either way it is SkyVu's official 2026 marketing [Canon]. The earlier draft's "probably 2013 footage" is withdrawn.
2. **Only the Gamma Ray is confirmed in the 2026 build.** The evidence is a fan closed-playtest chapter thumbnail [Observed].
   - The Gernobyl appears in the official trailer's gameplay, but that footage's date is unsettled [Observed; date Unverified].
   - The other 15 weapons are unconfirmed for 2026 [Unverified].

**Scale, colours and image key**
- **H** means Graham's height. On the BBG News chart, Graham = 1.0× Oliver [BBG News invention, per the character file]. Sizes are eyeballed or measured in pixels on the 2012–2015 store and loadout renders, and perspective inflates items held toward the camera [Observed, approximate].
- **Hex values** are medians sampled by script from the images. They are approximate, not official [Observed].
- **Wiki images** are cited as `File:<name>` (https://battlebears.fandom.com/wiki/File:<name>). I re-downloaded each one, for example /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/graham-verify/img/Power_Glove.jpg (originals in that `img` folder, PNG conversions in the sibling `png` and `png2` folders).
- **Trailer frames:** I extracted my own frames from /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/trailer.mp4. Each is named for its time, e.g. /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/graham-verify/frames/f_08.25.png is at 8.25 s.
- **YouTube thumbnails:** /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/graham-verify/yt/.
- **Contact sheets:** /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/graham-verify/sheets/.

## Shared visual systems

### The in-game Graham who holds these weapons (2012–2015 BBG model)
- **Model** [Observed: File:Power_glove.png, File:Gamma_ray.png, File:Hand_Cannon.png, File:Slowfield.png, File:Turret.jpg]:
  - orange hard hat with three dark grooves
  - blue-framed goggles with glowing cyan lenses
  - white handlebar moustache
  - dark-grey fur with a light-grey belly
  - boxy radio-style backpack with an antenna and a side speaker grille
  - red gloves on **both** hands, a red sash, and a red-and-yellow tool belt with a silver buckle
  - white stripe bands on the upper arms
- **Team colour:** the backpack is red by default and teal-blue on the blue team [Observed: https://i.ytimg.com/vi/U3XDJXo1Ej4/hq2.jpg; File:GIgramhambundle.png, where the backpack and gloves are teal]. The skin concept File:InstaGraham.jpg shows the same skin in a brown/red version and a teal version [Observed]. That the colour follows the team is [Inference].
- **Weapon hand:** one-handed weapons sit in his right hand, the viewer's left in front-facing renders [Observed].
- **Outlines:** 2012–2015 in-game images have none [Observed: U3XDJXo1Ej4 maxres; 0GuhKiAnNyc maxres; File:So_many_mines.jpg]. The May 2018 render, the Steam trailer gameplay and the 2026 playtest thumbnails all have thick black outlines [Observed].
- **Skins seen with weapons:**
  - **Instagraham** in the Steam trailer: brown cap with a rainbow stripe, dark-rimmed goggles with camera-lens lenses, red-brown fur and a brown radio backpack. It matches File:Instagrahamrl.png, which also holds the Gamma Ray [Observed]. The wiki notes the "stripe of colours on his helmet and camera lens on his goggles" [Fan-wiki: Instagraham].
  - **Old School** in all 2026 playtest thumbnails: red cap with a "G", red overalls, white shirt and a green warp-pipe backpack [Observed]. The wiki calls it a Mario reference ("It's a me!", a warp-pipe backpack) [Fan-wiki: Old School].

### Radiation status and detonation (Gamma Ray, Gernobyl, MuskIt, Radiation Rod)
- **Wiki description:** "a yellow circle will appear over the player's head and a noise from a Geiger counter will begin sounding ... As the intake increases, three portions of the circle will dissolve into the common radioactivity symbol, where further exposure will result in death." [Fan-wiki: Status Effects]. All four Engineer radiation weapons are on that page's "Irradiated" list [Fan-wiki].
- **Icon stages:** the wiki's icons step from a full 6-wedge disc (Hazard-3, 0–24%) to 5 wedges (Hazard-2) to 4 (Hazard-1) to the 3-blade trefoil (Hazard-0, 75–99%) [Observed: File:Hazard-3.png to File:Hazard-0.png; percentage bands Fan-wiki: Gamma Ray]. The wiki's icons are black silhouettes on transparency, not game colours [Observed].
- **In-game icon colours** [Observed]:
  - **Early stage:** a bright yellow disc (#FBFE13) split into wedges by thin dark lines, with a dark hub. One wedge is already gone and shows dark, not "whited out" as the wiki words it [Observed: https://i.ytimg.com/vi/0GuhKiAnNyc/hq2.jpg, Jan 3, 2014 fan Everyplay clip].
  - **Late stage:** three yellow-orange blades (#FFC20B) on a black disc (#150E09) with a black hub. This is the trefoil shape with its colours inverted from the usual black-on-yellow sign [Observed: f_08.25.png, f_08.50.png, f_08.75.png; zoom sheet trefoil.png].
  - The 2013 HUD also shows a yellow-and-black trefoil at the screen edge while Graham stands in goo [Observed: File:Radioactive_puddle.jpeg].
- **Sound:** a Geiger-counter tick that grows "faster and faster - this sound is audible to all players nearby" [Fan-wiki: Gamma Ray].
- **Decay:** about 3–5 RP/s once exposure stops, and the icon steps back [Fan-wiki].
- **Detonation:**
  - At full radiation the target "will die instantly in a relatively large explosion". The blast radius is 150–200 units and hurts nearby players, so suicide is possible [Fan-wiki: Gamma Ray].
  - "the explosion animation is the same as the Piece Maker and Phat Man explosion animation". Its size "depends on the victim's size" but "does not surpass the size of Piece Maker or Phat Man" [Fan-wiki: Gamma Ray trivia].
  - **The wiki conflicts:** Status Effects says the maximum is "100 radiation points" with the Gamma Ray at "5" per hit; the Gamma Ray and Radiation Rod pages say "Maximum radiation is equal to the individual players maximum health", with "4.5 radiation points" per Gamma Ray shot [Fan-wiki].
- **What a detonation looks like in the Steam trailer** [Observed: f_09.00.png to f_10.00.png; sheet tr_c.png]:
  - The target pops into toy-like orange body pieces (head, limbs).
  - They fly out of a blocky white-hot cloud with yellow (#FFE83C / #FFF5AA) and orange edges.
  - A white hexagonal ring spreads across the floor.
  - A large white flash edged with cyan lightning also sweeps across the upper right at 8.75–10.25 s; it also appears in Steam screenshot screen_03.jpg [Observed]. Its source, an in-game effect or a trailer graphic, is [Unverified]. Don't treat it as part of the radiation blast.
  - That this burst is the radiation kill is [Inference]: the trefoil was showing and Graham was firing the Gamma Ray.
- **Other detonation sightings:**
  - 2012 beta: with the Gamma Ray in hand and a fresh kill in the feed, a puffy, blocky pale-yellow/white cloud with translucent grey smoke hangs over the field [Observed: https://i.ytimg.com/vi/U3XDJXo1Ej4/maxresdefault.jpg]. That this is a detonation is [Inference].
  - Jan 2014 fan clip: the kill frame is washed yellow-white, with "RELOAD" and 0/120 on the HUD [Observed: https://i.ytimg.com/vi/0GuhKiAnNyc/hq3.jpg].
- **Turret immunity:** the Turret is immune to status effects [Fan-wiki: Turret].

### Slowed status (Bind Field)
- "a yellow Z will appear over the player's head, indicating a reduction in speed" [Fan-wiki: Status Effects].
- The list names "Slow Field" (the Bind Field's original name). Black Hole is not listed [Fan-wiki].

---

## Power Glove (primary; default; BBR v1.4, Nov 28, 2012, through BBG; 2026 unconfirmed)
- **Official text:** "The precursor to the O.C.O. Glove, this weapon can rapidly fire small orbs of energy. When charged up, it delivers a larger and more destructive orb that explodes on impact. This weapon can HANDle any situation." [Game text via wiki] (https://battlebears.fandom.com/wiki/Power_Glove)
- **Era / status:**
  - It is the default primary [Fan-wiki infobox] and one of the v1.4 launch six [Fan-wiki: Updates].
  - The 2012 primary list shows "GAMMA RAY" and "POWER GLOVE / EQUIPPED" [Observed: File:Power_glove.png, uploaded 2012-11-29].
  - BBR 1.4.2 (Feb 28, 2013): "Charge time changed from 1.8 to 1.5 seconds". The page now says 2.25 s [Fan-wiki], so the stats have drifted.
  - It is in the "Groundhog Day" bundle and in an Oct 12–14, 2013 Graham bundle [Fan-wiki: Bundle Deals].
  - 2026: not seen [Unverified].
- **Look:**
  - An oversized robotic glove worn over his right hand, with three chunky fingers and a thumb. The pale-grey shell reads #7C8684 in the render's lighting, and the knuckle joints are dark [Observed: File:Power_Glove.jpg, File:Power_glove.png].
  - A glowing cyan hexagonal core sits on the back of the hand (#19C5CA median, brightest centre about #27E5E9), with cyan circuit traces and a cyan dot on each fingertip [Observed].
  - Size: about 0.45 H from fingertip to cuff, palm as wide as his head. It is held up toward the camera, so it reads bigger [Observed, approximate]. His other hand keeps its red glove [Observed].
  - A 2013 in-match screenshot shows a Graham with a brown radio backpack raising the same white glove with cyan lights [Observed: File:4_mines_one_is_hidden.jpg].
  - **Design link to his "mechanical hand":** the concept "Graham's Self-Enhanced Hand" is a silver mechanical hand with cyan lights [Observed: File:Graham_glove.png], and the class gallery captions it "Power Glove Concept" [Fan-wiki]. The art File:Engineer-Graham.png (uploaded 2012-11-02) gives Graham a matching silver hand with cyan circuits on his **right** arm [Observed]. So the in-game Power Glove looks like the playable form of that hand [Inference]. SkyVu provenance for both art files is [Unverified].
- **Firing:**
  - "Semi-automatic". It "can be charged", and "When building up a charge, the weapon can still be fired" [Fan-wiki]. That you tap to shoot and hold to charge is [Inference].
  - Full charge is "indicated by the appearance of a small energy ring formed around the Glove" [Fan-wiki].
  - "Using a charged shot will be considered using a full magazine of ammo" [Fan-wiki].
  - Cooldown 0.1 s uncharged and 1.0 s charged; 100 ammo; 3.5 s reload. The trivia says it was the first BBG weapon with charged shots and "the ability to regenerate ammo" [Fan-wiki].
  - The 2012 stat panel shows DAMAGE / EXPLOSIVES / RELOAD / AOE bars [Observed: File:Power_glove.png].
  - Sound: [Unverified].
- **Projectile:** "small orbs of energy", or when charged "a larger and more destructive orb" [Game text via wiki], at 1,400 u/s [Fan-wiki]. No image of an orb exists, so its colour and trail are [Unverified]. Cyan is only a lead, taken from the glove's lights [Inference].
- **Impact / end result:**
  - An uncharged or partly charged hit does 20 with no splash [Fan-wiki].
  - A charged orb "explodes on impact" [Game text via wiki]: 50 on a direct hit, plus 60 within 150 units and 30 at 150–300 units [Fan-wiki].
  - What the explosion looks like is [Unverified].
- **Images viewed:** File:Power_Glove.jpg, File:Power_glove.png, File:Graham_glove.png, File:Engineer-Graham.png, File:4_mines_one_is_hidden.jpg. Sheets: pg.png, pg_zoom.png, 4m_zoom.png, eg_zoom.png.
- **Depiction for shorts:** Graham raises the big white robo-glove and its cyan core pulses. Quick shots spit small glowing orbs. Holding grows a thin ring of light around the glove [Fan-wiki], then a big orb bursts into a ring of sparks. The cyan-white orb colour and the spark style are [BBG News invention].
- **Confidence:** partial (look observed; projectile and impact undocumented).

## Gamma Ray (primary; BBR v1.4, Nov 28, 2012, through BBG; confirmed in the 2026 closed playtest)
- **Official text:** "Turn your enemies in to walking explosives with this radioactive ray gun. It does very little damage on initial impact, but once you charge them up all the way...BOOM! The radioactive symbol over their head indicates how charged they are. The bigger they are, the longer it takes to blow them up, however yielding a much larger and more aggressive explosion." [Game text via wiki] (https://battlebears.fandom.com/wiki/Gamma_Ray)
- **Era / status:**
  - A v1.4 launch weapon costing 150,000 Joules [Fan-wiki].
  - SkyVu's video "BATTLE BEARS ROYALE Update 1.4 Beta - Engineer Class (Graham)" (U3XDJXo1Ej4, channel "BATTLE BEARS", 170 s, date text "Oct 31, 2012"; 23:37 UTC per wiki file metadata) carries the description "Battle Bears Royale (BBR) Update 1.4 is in beta testing now! Get a sneak peak at the all new class being added, the Engineer (aka Graham)." [Canon]
  - Its beta loadout reads PRIMARY GAMMA RAY / SECONDARY TURRET / MELEE T SQUARE [Observed: File:Graham-gamma-ray.png].
  - BBR 1.4.2: reload 4.0 to 3.6 s [Fan-wiki].
  - BBG 2.6 (Dec 20, 2013): "Damage increased from 1 to 2" and "Clip size decreased from 120 to 80" [Fan-wiki transcription]. The infobox now says damage 1, ammo 100, reload 3.5 s [Fan-wiki], which conflicts.
  - **Ammo counters seen** [Observed]:
    - 164/250 and 250/250 in the 2012 beta (U3XDJXo1Ej4 maxres, hq3)
    - x/120 in the Jan 3, 2014 fan clip (0GuhKiAnNyc)
    - 100/100 and 0/100 in 2026 playtest #3 ("Battle Bears Gold Playtest #3 Part 1" qt43iTdANbM chapter frame at 8:11; "Part 3" VHo1O41RNJE chapter frame at 29:05; JustNubz)
  - That those 2026 HUDs belong to the Gamma Ray is [Inference]: Old School Graham at 120/120 health holds an orange gun, and the clip is 100. The Power Glove also has 100 ammo but is white.
  - **2026:** the Engineer chapter thumbnail of JustNubz's "BBG All Classes Showcase [Skins, Taunts, Weapons, and Melee] (from Closed Playtest #4)" (Sep 20, 2026; chapter at 34:42; frame at 34:52) shows the loadout screen reading CHARACTER ENGINEER / SKIN OLD SCHOOL. Graham holds the Gamma Ray: orange clamp frame, dark ring, green lens [Observed: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/graham-verify/yt/jn_ch_34m42_3x.png]. The same skin-and-gun pairing appears in File:Old_school2cool.png from 2013 [Observed].
  - It is in the "Groundhog Day" bundle [Fan-wiki].
- **Look:**
  - **2012 render:** a dark round drum or emitter with a bright green octagonal lens (#66FF08), framed by orange clamp-like brackets (#B8630A in shade). A small white cylinder with a yellow radiation sticker sits on top, and the housing has vent slots [Observed: File:Graham_default.png, File:Gamma_ray.png, File:Graham-gamma-ray.png; the cylinder is clearest in Graham-gamma-ray.png].
  - **Card (2013 art, reused in the 2026 trailer):** a bright orange blocky housing (#FF7700 lit, #A14F13 in shade) with black vent slots, a dark panel with small lime LEDs, a glowing green core visible behind a big black octagonal ring, and orange prongs gripping the ring [Observed: frames/card_gun.png at 11.5 s and card_gun_1075.png].
  - From behind, a grey hexagon sits on the rear block [Observed: f_08.25.png; 0GuhKiAnNyc maxres].
  - Held two-handed at the hip, about head-sized and roughly 0.3 H long [Observed, approximate].
  - HUD/nav icon: an orange gun with green tube segments [Observed: File:Gamma-ray-navi-icon.png].
- **Firing:**
  - Automatic: "a short-ranged constant yellow beam". Range 1,000 units, cooldown 0.08 s [Fan-wiki].
  - "The end of the projectile emits a type of smoke-like vapour." [Fan-wiki]
  - On screen, pale-gold to white concentric arcs (about #FAE8A4 to #FFFBE4) ripple out around the muzzle like sound waves [Observed: f_08.25.png, f_08.50.png; https://i.ytimg.com/vi/0GuhKiAnNyc/maxresdefault.jpg and hq1.jpg, where the arcs carry a yellow-green glow].
  - The card's muzzle flash is yellow-white [Observed: f_11.50.png].
  - The 2012 stat panel shows RADIATION / AMMO / COOLDOWN / RELOAD bars [Observed: File:Gamma_ray.png].
  - Sound: the Geiger ticking on the target [Fan-wiki].
- **Projectile:** no bullet is visible. The "beam" reads on screen as the rippling ring arcs [Observed + Fan-wiki].
  - In a 2026 playtest frame at 0/100 ammo, pale-cyan concentric hexagonal outlines float in front of an enemy [Observed: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/graham-verify/yt/ch_VHo1O41RNJE_hqdefault_1745866.jpg]. Whether that is the 2026 Gamma Ray beam or another player's effect is [Unverified].
- **Impact / end result:**
  - Each hit adds radiation for "very little damage" [Game text via wiki].
  - In the trailer [Observed: f_08.00.png to f_09.00.png]:
    - 8.0 s: the target glows yellow and white sparkles fizz off it.
    - 8.25–8.75 s: a yellow-on-black trefoil appears over its head.
    - 9.0 s: the target bursts as described in the shared radiation section.
  - That the burst is the radiation kill is [Inference].
- **Images viewed:**
  - Wiki: File:Graham_default.png, File:Gamma_ray.png, File:Graham-gamma-ray.png, File:Gamma-ray-navi-icon.png, File:Old_school2cool.png, File:Instagrahamrl.png, File:Hazard-0.png to File:Hazard-3.png.
  - Trailer frames f_06.00 to f_13.25 (sheets tr_a, tr_b, tr_c, tr_d, tr_e).
  - YouTube: U3XDJXo1Ej4 hqdefault, hq1, hq2, hq3 and maxres; 0GuhKiAnNyc maxres, hq1, hq2 and hq3; rfAyqVJrli4 hqdefault, hq1, hq2, hq3 and maxres; the JustNubz -lAtv-j9Sms chapter thumbnails; playtest #3 chapter thumbnails (qt43iTdANbM, VHo1O41RNJE, _R4rvvGlRsM).
  - Steam screenshots screen_00.jpg to screen_04.jpg.
- **Depiction for shorts:**
  - Graham braces the orange ray gun at his hip, and pale-gold rings pulse out of the muzzle [Observed].
  - The target glows yellow and fizzes with sparkles. A yellow disc over its head loses wedges until three yellow blades remain on black, while the Geiger ticks speed up [Observed + Fan-wiki].
  - Then a blocky white-yellow flash and a white hex ring on the floor [Observed].
  - The game shows the victim flying apart into toy-like pieces; for 13+, show stuffing puffs, bolts and confetti instead [BBG News invention].
- **Confidence:** observed.

## Rivet Gun (primary; BBG 2.1, Jul 15, 2013, per its page)
- **Official text:** "Not just for fixing. This weapon shoots electrified rivets that stick into walls and create a ball of death!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Rivet_Gun)
- **Era / status:**
  - The wiki's 1.4.3 preview lists it as an Engineer primary [Fan-wiki: BBR Version 1.4.3]. It appears in the "BB 1.4.3 COMING SOON" promo art [Observed: File:1.4.3Weapons_B.png, uploaded 2013-04-09; SkyVu authorship Inference].
  - "The Rivet Gun's original function was for the rivets to stick to the ground and then connect to each other using beams to form a kind of damage-dealing barrier. It was originally meant to be released in v.1.4.3, but its release was delayed" [Fan-wiki].
  - The page says "released in v2.1", but the Updates row for 2.1 (Jul 15, 2013) does not list it [Fan-wiki]. On 2013-07-17 the page changed from "It will come in in v2.1" to "released in Update 2.1" [Fan-wiki revision history, checked]. So 2.1 is likely [Inference].
  - That July 2013 revision said its "light purple force fields" "last for about 20 seconds", the rivets "can only stick to the ground", and "It has a base ammo clip of 3" [Fan-wiki, early].
  - 2.6: "Reload speed decreased from 6 to 4" and "Time to Live decreased from 10 to 7" [Fan-wiki].
  - Costs 50,000 Joules; in the Groundhog Day bundle [Fan-wiki].
- **Look:**
  - **Turnaround (File:Rosie.png):** a long boxy gun with a dark brown-black body (#2E211A) and orange-brown bands (about #9E6D40 lit) [Observed]. It also has:
    - a ribbed rail along the top
    - a black carry handle on silver posts
    - a short silver tube muzzle
    - a grey-tan underslung canister banded in orange with an orange emblem
    - a dark hose looping from the rear grip down to the canister
  - Two loose canisters with silver nozzle caps sit beside the gun [Observed]. They are probably rivet magazines [Inference]. The emblem is too small to identify as a hazard symbol [Observed].
  - **Promo art:** near-black gunmetal with orange bands, a silver muzzle, and a black carry handle on silver posts [Observed: File:1.4.3Weapons_B.png].
  - **In hand:** seen from the front, a silver hexagonal-nut muzzle in a dark olive-brown housing with an orange band, aimed at the camera at waist height [Observed: File:Rivet_Gun.jpg].
  - Length: roughly 0.35–0.45 H. This is an inference from the turnaround proportions; no side-on in-hand image exists [Inference].
- **Firing:** 4 per clip, 1 s rate, 4 s reload, 1,600 u/s [Fan-wiki]. The muzzle effect is [Unverified].
- **Projectile:** "electrified rivets" [Game text via wiki]. What they look like in flight is [Unverified].
- **Impact / end result:**
  - Rivets "land on the ground or any wall and immediately form light purple energy fields around their landing area, which last for 7 seconds. The rivets themselves cannot directly damage players." [Fan-wiki]
  - Damage is higher toward the centre, 30 DPS [Fan-wiki].
  - The fields "are in fact square when viewed from above" despite the "ball of death" text [Fan-wiki].
  - No image of a field was found [Unverified].
- **Images viewed:** File:Rivet_Gun.jpg, File:Rosie.png, File:1.4.3Weapons_B.png, File:Generalstoread2.png (no Rivet Gun in it) (sheets rivet.png, rosie3.png).
- **Depiction for shorts:** a rivet thunks into the floor or a wall, crackles, and blooms into a light-purple, box-shaped electric field [Fan-wiki colour and shape]. Anyone inside gets zapped with harmless sparks until it fizzles out after about 7 s. The spark style is [BBG News invention].
- **Confidence:** partial.

## Hand Cannon (primary; BBG 2.5, Nov 27, 2013)
- **Official text:** "Slow and steady, just like Graham himself. This slow moving missile causes a massive explosion on contact." [Game text via wiki] (https://battlebears.fandom.com/wiki/Hand_Cannon)
- **Era / status:**
  - 2.5 lists "Engineer primary – Hand Cannon" [Fan-wiki: Updates].
  - Costs 60 Gas; it was the "first Engineer primary weapon to cost Gas" [Fan-wiki].
  - 2.6: "Projectile Speed increased from 400 to 750"; the infobox now says 800 u/s [Fan-wiki].
  - It is in the "GI GRAHAM" bundle with the Buzzsaw for 120 Gas [Fan-wiki: Bundle Deals].
- **Look:**
  - A short, fat orange-gold cylinder (#D5811B median; #EA9C3E lit) with dark bands and a cream rim [Observed: File:Hand_Cannon.png].
  - A glowing bright-green octagonal front face (#43E641), plus green light strips on top [Observed].
  - Held at mid-chest: his right hand grips the rear and his left hand supports it. About 0.25 H long, with a face about 0.15 H across [Observed, approximate].
  - On the GI GRAHAM banner, a blue-team Graham (teal backpack and gloves) holds it low, green face forward [Observed: File:GIgramhambundle.png].
- **Firing:** one slow missile per shot: "This slow moving missile" [Game text via wiki]. 2 per clip, 1 s cooldown, 3 s reload [Fan-wiki].
- **Projectile:** "a comically large green-black missile" [Fan-wiki]. No image was found [Unverified].
- **Impact / end result:**
  - It "causes a massive explosion on contact" [Game text via wiki].
  - It explodes on contact with "a player or surface": 20–40 damage, AoE max 100 / min 300 units, with a high suicide risk [Fan-wiki].
  - What the explosion looks like is [Unverified].
- **Images viewed:** File:Hand_Cannon.png, File:GIgramhambundle.png (sheets hc_bz_mk.png, bundles.png).
- **Depiction for shorts:** a huge green-and-black cartoon missile drifts out so slowly the target has time to stare at it [Fan-wiki basis]. Then a big orange-white boom with Graham at its edge and his hat smoking [BBG News invention].
- **Confidence:** partial.

## Buzzsaw (primary; BBG 2.6, Dec 20, 2013)
- **Official text:** "Gun that shoots spinning saw blades: Check! Spinning saw blades that explode on impact: Check!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Buzzsaw)
- **Era / status:** "New: Buzzsaw Primary / 80 Gas" in 2.6 [Fan-wiki: Versions/2.6]. It now costs 60 Gas with no level lock [Fan-wiki]. It is in the GI GRAHAM bundle [Fan-wiki].
- **Look:**
  - A boxy dark-grey/black launcher (#1B1F1D) with a silver-grey side panel and a glowing green vertical slot (#47C562).
  - A large white/silver toothed circular blade (#CCCCCC) stands upright at the front, blurred as if spinning.
  - Held two-handed at chest height. The blade is about 0.4 H across [Observed, approximate: File:BuzzSaw.jpg].
  - The GI GRAHAM banner shows it beside the Hand Cannon, with a huge grey saw blade in the background [Observed: File:GIgramhambundle.png].
- **Firing:** 3 per clip, 1 s rate, 3 s reload [Fan-wiki].
- **Projectile:**
  - "spinning saw blades" [Game text via wiki].
  - "It can dig into surfaces and then track the closest opponent". The homing is "very weak, slow and unreliable" with "rather limited range" [Fan-wiki].
  - "After travelling for a short amount of time the buzz saws will sink below the ground and cease any effect. It may hover at a spot for several seconds occasionally" [Fan-wiki].
  - It is "one of only two projectiles that can penetrate the Iron Curtain" (the other is the Sucker Punch) [Fan-wiki].
- **Impact / end result:**
  - The blades "explode on impact" [Game text via wiki]: 70 damage, plus explosives 35–70 over AoE 150/275, and "consistent damage regardless of the distance" [Fan-wiki].
  - What the explosion looks like is [Unverified].
- **Images viewed:** File:BuzzSaw.jpg, File:GIgramhambundle.png (sheets hc_bz_mk.png, bundles.png).
- **Depiction for shorts:** a whirring blade shoots out, bites into the floor and burrows toward the nearest enemy like a shark fin, then pops up and bursts into sparks and spinning bolts. The behaviour is per the [Fan-wiki]; the look is [BBG News invention].
- **Confidence:** partial.

## MuskIt (primary; BBG 2.12, Oct 2, 2014)
- **Official text:** "The musk of the Gyrnobal has been known to turn people into mutants, but most blow up." [Game text via wiki; spelling "Gyrnobal" as quoted] (https://battlebears.fandom.com/wiki/MuskIt)
- **Era / status:**
  - 2.12 adds MuskIt and Double Wrench [Fan-wiki: Updates]. Level 10, 60 Gas [Fan-wiki].
  - The first revision (2014-10-03) listed radiation 40–60, damage 35, AoE 125/175, ammo 2 and −5% speed. The page now lists radiation 35.5–55.5, damage 30, radiation range 100/150, ammo 3 and no modifier [Fan-wiki, revisions checked].
  - Its page is in Category:Shotgun but lacks Category:BBG Weapons [Fan-wiki].
- **Look:**
  - A long dark-maroon barrel (#663634) with white curved bands.
  - A salmon-pink bulbous rear chamber (#BC6C5C) with a grey emblem, and a yellow ribbed collar.
  - A yellow tank (#CBA41B) with a black-and-white marking hangs below the rear down to knee height.
  - Held diagonally across the hips with the barrel pointing forward and down. The barrel is about 0.35 H [Observed, approximate: File:Musket.jpg; zoom musk_zoom.png].
  - It reads as an old pump bug-sprayer [Inference, matching the wiki's "bug spray"].
- **Firing:** "used like a shotgun, dealing damage and irradiating enemies in a small cone". 1.5 s rate, 3 ammo, 4.5 s reload [Fan-wiki].
- **Projectile:** "When fired, it shoots green stuff of what appears to look like bug spray" [Fan-wiki]. No image was found [Unverified].
- **Impact / end result:** damage plus radiation within 100–150 units [Fan-wiki]. It uses the shared radiation status and detonation (it is on the Irradiated list) [Fan-wiki: Status Effects].
- **Images viewed:** File:Musket.jpg (sheets hc_bz_mk.png, musk_zoom.png).
- **Depiction for shorts:** Graham pumps it like a garden sprayer, and a short cone of green mist puffs out. Targets in the cone get the yellow disc and start ticking. The mist shape is [BBG News invention]; the colour and status are per the [Fan-wiki].
- **Confidence:** partial.

## Turret (secondary; default; BBR v1.4 through BBG)
- **Official text:** "Place this device on the ground while facing the enemy and it will do all the killing for you. Use it wisely, you only get one at a time. If you wish to reposition, you can use the self-destruct to destroy your existing turret." [Game text via wiki] (https://battlebears.fandom.com/wiki/Turret)
- **Era / status:**
  - Default secondary and a v1.4 launch weapon [Fan-wiki]. It is in the 2012 secondary list [Observed: File:Turret.png] and the beta loadout [Observed: File:Graham-gamma-ray.png].
  - The wiki's first revision (Nov 2, 2012, pre-release) said: "Graham lays the turret on the ground as the turret rises up. It shoots the same bullets as the Electric Honey." [Fan-wiki, early, checked]
  - BBR 1.4.2: damage 2.5 to 3.5, dispersion 0.04 to 0.03, health 100 to 135 [Fan-wiki].
  - BBG 2.6: "Damage increased from 3.5 to 7" and "Range decreased from 2000 to 1000" [Fan-wiki].
  - The current page (damage 3.5, dispersion 0.02, health 180, reload 4.0 s, range 1,800 in the text) conflicts with both logs [Fan-wiki].
  - It is in the Groundhog Day bundle [Fan-wiki].
- **Look:**
  - **Carried:** a light-grey/white boxy device with vent slots, red stripes, a red light knob on top and a dark round port. He holds it low in front with both hands on its top, and it looms large near the camera [Observed: File:Turret.jpg].
  - **Deployed** [Observed: File:Turretdeploy.png]:
    - a white/light-grey boxy gun body with vent grilles and a ribbed grey drum on its side
    - blue diagonal stripes and a blue handle bar on top (#06247C in shade)
    - a white barrel stepping down to a dark section with a white sleeve tip
    - a dark angled (Z-shaped) neck on an X-shaped base with four light square feet
  - **Weapon icon** (the wiki captions File:Turret_2.png "Turret's weapon icon"): a grey gun with a red stripe and red handle on a bent leg [Observed: File:Turret_2.png, File:Graham-gamma-ray.png]. Whether the stripe colour follows the team is [Inference].
  - **Deployed height:** undocumented [Unverified]. An unsourced sketch shows Graham leaning against a turret of this shape (long barrel, Z-leg, X-base), legs crossed, holding a "#1" mug [Observed: File:Graham_relaxing_on_turret.png; provenance Unverified].
  - **Concepts:** a domed grey turret with glowing red or blue stripes and an ammo dispenser with a glass hopper (File:Engineer2.png), plus "turrets 1 2 3" sketches (File:Engineer1.png) [Observed; SkyVu provenance Unverified]. The released shape differs [Observed].
- **Firing:**
  - It takes "approximately 2-3 seconds to set up". It "cannot turn", and its fixed cone is 100° [Fan-wiki].
  - Unlimited bullets at 0.25 s per shot. It targets one enemy at a time, "is not 100% accurate", and its range is 1,800 units per the page text [Fan-wiki].
  - One turret at a time, two with Ammo +2. "Player's can destroy their own Turret for repositioning by tapping the reload button." [Fan-wiki]
  - The 2012 beta HUD shows the turret icon with a red button beside "0/1" [Observed: https://i.ytimg.com/vi/U3XDJXo1Ej4/hq1.jpg].
- **Projectile:** undocumented for BBG [Unverified]. The only lead is the early-wiki claim that it fires Electric Honey bullets. Electric Honey's official text is "Electrically charged bees are slightly smaller* allowing for a higher bees-per-hive ratio and thus longer continuous fire!" [Game text via wiki: Electric Honey (BBG)], so bee-bullets are implied [Inference; Unverified].
- **Impact / end result:**
  - Small repeated hits on one target [Fan-wiki].
  - When destroyed, "after two seconds of smoking, it will vanish" [Fan-wiki].
  - It cannot detect players in Cloaking, Peek A Boo or Flawless Disguise. It cannot be locked onto by a Sniper or the Demo, and it is immune to status effects [Fan-wiki].
- **Images viewed:** File:Turret.jpg, File:Turret.png, File:Turretdeploy.png, File:Turret_2.png, File:Engineer1.png, File:Engineer2.png, File:Graham_relaxing_on_turret.png, File:Graham-gamma-ray.png, U3XDJXo1Ej4 hq1 (sheets tur1.png, tur2.png, eng12.png, u3_hud.png).
- **Depiction for shorts:**
  - Graham sets the white case down, and it "rises up" onto its X-legs [Fan-wiki, early].
  - It fires rapid small shots straight ahead within a fixed cone; it does not swivel [Fan-wiki].
  - The shots' look is undocumented. Use small yellow tracer bolts or, as a nod to the early wiki, tiny electric bees [BBG News invention].
  - When destroyed, it smokes for 2 s and blinks out [Fan-wiki].
- **Confidence:** partial.

## Proximity Mine (secondary; BBR v1.4 through BBG)
- **Official text:** "Useful in high traffic or choke areas, this placable explosive can attach itself to any surface. Once an enemy gets close, it will explode. This weapon can also be remote detonated by tapping the red button by the ammo count." [Game text via wiki] (https://battlebears.fandom.com/wiki/Proximity_Mine)
- **Era / status:**
  - A v1.4 launch weapon costing 100,000 Joules [Fan-wiki].
  - The 2012 list shows "PROXIMITY MINE / EQUIPPED" with EXPLOSIVES and AOE stat bars [Observed: File:Proximity_mines.png].
  - BBR 1.4.2: reload 3.5 to 3.2 s, cooldown 3.0 to 2.8 s, priming 2.5 to 2.2 s [Fan-wiki].
  - BBG 2.6: "Maximum Damage increased from 100 to 150" and "Minimum Damage increased from 200 to 300". These read as AoE radii [Fan-wiki; interpretation Inference].
  - The red button "has since been removed and its function added to the reload button" [Fan-wiki].
  - The infobox's 0.01 s priming conflicts with the logs. It also lists a trigger radius of 14.9 [Fan-wiki].
- **Look:**
  - **Held:** an olive-khaki four-pronged claw-star with dark-grey prongs and a tan rim, held out low at his right side. It is about 0.35–0.4 H across and close to the camera [Observed: File:Proximity_Mine.jpg, File:Proximity_mines.png].
  - **List/HUD icon:** a dark four-pointed X-star with a green centre dot [Observed: File:Proximity_mines.png, File:Engineers_setup.jpg; U3XDJXo1Ej4 hq2 under "RELOAD"].
  - **Placed:** flat dark-olive stars lie on floors or stick to walls. Each has a small glowing green centre and a thin red line sticking straight out of it: vertical on floors, horizontal from walls [Observed: File:So_many_mines.jpg, File:Dat_Engineer.jpg, File:4_mines_one_is_hidden.jpg].
  - The wiki says "In a later update, a small red line will display above the mine" [Fan-wiki]. The lines are already there in screenshots uploaded 2013-05-11 and 2013-07-25 [Observed; upload dates Fan-wiki file metadata].
- **Firing:** thrown. It sticks to any surface, and "If a player toss a mine directly at an opposing player, it will rebound off the player's body". 4 ammo; 2 s cooldown and reload per the infobox [Fan-wiki].
- **Projectile:** the tossed mine itself [Fan-wiki]. Its arc and spin are [Unverified].
- **Impact / end result:**
  - It explodes when an enemy steps on or near it, or on remote detonation, but "it will not cause an explosion if it is detonated before reaching a solid surface" [Fan-wiki].
  - Explosives 20–110, AoE 140/300. Enemy explosives can set it off, and suicide is possible [Fan-wiki].
  - SkyVu's beta thumbnail shows a giant flat white starburst with long cream/yellow rays and a chunky yellow puff at its centre, with "RELOAD" over the mine icon, a red detonate button and "0/1" on the HUD [Observed: https://i.ytimg.com/vi/U3XDJXo1Ej4/hq2.jpg; zoom u3_hq2.png]. That this is a mine blast is [Inference].
- **Images viewed:** File:Proximity_Mine.jpg, File:Proximity_mines.png, File:So_many_mines.jpg, File:Dat_Engineer.jpg, File:4_mines_one_is_hidden.jpg, File:Engineers_setup.jpg, U3XDJXo1Ej4 hq2 (sheets pm1.png, pm2.png, u3_hq2.png, u3_hud.png).
- **Depiction for shorts:** mines clack onto the floor and walls, each with its little red line sticking out [Observed]. An enemy steps close and a white-and-yellow starburst flashes [Observed basis, low-res]. Confetti and bolts replace damage [BBG News invention].
- **Confidence:** partial.

## Gernobyl (secondary; BBR 1.4.3, Apr 2013, through BBG; in the Steam trailer's gameplay of unsettled date)
- **Official text:**
  - In-game: "Radioactive goo never hurt anyone, unless of course it came from the contaminated mouth of an adorable little mutated mammal. The longer your exposure the greater your chance of death!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Gernobyl)
  - Patch note, 1.4.3 row (Apr 15, 2013): "Gernobyl: Engineer's radioactive launcher.This mid-sized rodent shoots irradiated goop: a hit will cause radiation damage and slight physical damage, if you miss an opponent it creates a radioactive puddle- any player who steps in it will receive radiation damage."
  - The 1.4.3.1 row (Apr 23, 2013) reads "...radioactive launcher. This mid-sized rodent shoots irradiated goop; a hit..." [Fan-wiki: Updates, which presents these as App Store notes; not checked against the store].
- **Era / status:**
  - The wiki's 1.4.3 page says "This update has been released, but as 1.4.3.1" [Fan-wiki]. Costs 90 Gas [Fan-wiki].
  - Its 2013 stat panel shows RADIATION / RELOAD / DURATION / DAMAGE bars and "SPEED +5%" [Observed: File:Dmimage.jpg, uploaded 2013-04-30].
  - 2.6 [Fan-wiki]:
    - AoE "Maximum damage" 100 to 150 and "Minimum damage" 200 to 300
    - "Clip size increased from 1 to 3"
    - fire rate 1.5 to 1.25
    - radiation minimum 45 to 55
    - "Puddle Radiation increased from 2 to 10"
  - The current infobox: damage "5-10 (75 radiation per second from puddles)", cooldown 1.5 [Fan-wiki].
  - It is in the Groundhog Day bundle [Fan-wiki].
- **Look** [Observed: File:Gernobyl.jpg, File:Gernobil.jpg, File:1.4.3Weapons_B.png, File:Dmimage.jpg]:
  - A fat tan/cream gerbil (#D9BC74) with a brown stripe down its head and back and a brown curled tail.
  - Glowing yellow eyes, and an open red mouth with buck teeth, dripping green goo.
  - A black harness with a yellow-and-black hazard band, and a silver-and-black carry-handle frame on its back.
  - Lime-green goo patches (#BFDB3C) drip off its body.
  - Graham carries it by the handle like a lantern, mouth forward, at hip height. It is about 0.35 H long [Observed, approximate].
- **Concepts:** a tube launcher with the gerbil at its muzzle, a gerbil-with-handle sketch, and alternatives A–D (a generator, a lamp and canister, an axe with a radiation barrel, and a big goo-dripping gun) [Observed: File:Screen_Shot_2013-01-24_at_4.42.10_PM.png, File:Screen_Shot_2013-01-23_at_4.51.03_PM.png, File:Screen_Shot_2013-01-23_at_4.57.25_PM.png; SkyVu provenance Unverified].
- **Firing:**
  - It lobs goo at 1,000 u/s, with 3 ammo and a 4.5 s reload [Fan-wiki].
  - The illustrated in-game "Groundhog Day" banner shows the gerbil spewing a thick lime stream, with a lime splat on the left [Observed: File:Groundhogbundle.png].
- **Projectile:**
  - "irradiating globs of light green goo", and "The goo will split into 2 to 3 droplets" [Fan-wiki].
  - The wiki's caption image shows a line of small glowing yellow-green droplets (#B3DC36) with glowing tails, captioned "Radioactive goop before contact with any surface, with trail of glowing goo effects" [Observed: File:Radioactive_goo.jpeg; caption Fan-wiki].
  - **Steam trailer** [Observed: frames g_7.20.png to g_7.90.png; sheet gern_tr.png]:
    - 7.2–7.7 s: Graham's right hand holds a tan furry body with lime goo patches; a silver handle bar shows at 7.6–7.7 s.
    - By 7.9 s he has switched to the orange Gamma Ray.
    - That the object is the Gernobyl is [Inference, strong].
    - 7.4 s: a chunky, faceted lime glob about the size of his head launches toward the target.
    - 7.5–7.75 s: soft glowing green ovals dot the area.
- **Impact / end result:**
  - A hit causes "radiation damage and slight physical damage", and a miss "creates a radioactive puddle" [patch note via Fan-wiki].
  - Each puddle "lasts 4.5 seconds" and irradiates anyone who steps in it [Fan-wiki].
  - The wiki's "Radioactive puddle" image shows a huge, opaque, lumpy lime goo mass (#B1DA2D) filling the view in front of Graham, with a yellow-and-black trefoil at the HUD edge [Observed: File:Radioactive_puddle.jpeg]. Whether it lies on the floor or a wall can't be told from this angle [Observed].
  - In the trailer at 7.5 s the lime glob splashes over the target's body [Observed: f_07.50.png]. Radiation status and detonation then follow, as in the shared section.
- **Images viewed:** File:Gernobyl.jpg, File:Gernobil.jpg, File:Dmimage.jpg, File:Radioactive_goo.jpeg, File:Radioactive_puddle.jpeg, File:1.4.3Weapons_B.png, File:Generalstoread2.png, the three Screen_Shot_2013-01 concept files, File:Groundhogbundle.png, trailer frames f_07.25 to f_08.00 and g_7.20 to g_7.90 (sheets gern1.png, gern2.png, gconc.png, bundles.png, gern_tr.png, tr_b.png).
- **Depiction for shorts:**
  - Graham swings the grumpy gerbil like a lantern, and it hacks up a lime glob [Observed basis].
  - The glob splats into a bubbling lime puddle [Observed]. Anyone who steps in gets the yellow disc and the ticking [Fan-wiki].
  - The gerbil's expressions and coughing are [BBG News invention].
- **Confidence:** observed.

## Black Hole (secondary; between BBG 2.12 and Oct 31, 2014, most likely 2.13)
- **Official text:** "A star that has collapsed in on itself, creating a gravitational force so strong not even light can escape. But Graham is an engineer so don't worry about it." [Game text via wiki] (https://battlebears.fandom.com/wiki/Black_Hole)
- **Era / status:**
  - Level 15 lock, 150,000 Joules. The first revision (Nov 4, 2014) listed 300,000 Joules, a 5.0 s duration and a 3.5 s reload [Fan-wiki, checked].
  - No update log names it. The fan Everyplay clip "Black Hole BBG" (7gdfSoWC2ZI) was published 2014-10-31 17:39 UTC [Fan-wiki file metadata], the release date of BBG 2.13 [Fan-wiki: Updates]. So it is no later than Oct 31, 2014, and 2.13 is likely [Inference].
- **Look:**
  - A glossy magenta-purple sphere (#A734AE median; #92219B in shade) with a lighter spiral swirl and a white highlight.
  - Held out on his right palm like a bowling ball, about 0.25 H across [Observed: File:BlackHole.jpg].
  - The fan clip's HUD icon is the same purple orb [Observed: https://i.ytimg.com/vi/7gdfSoWC2ZI/maxresdefault.jpg, hq1.jpg, hq2.jpg].
- **Firing:** an early revision says "The user throws the projectile" [Fan-wiki, Nov 5, 2014]. 1,000 u/s; 1 ammo, 2.5 s rate, 3 s reload [Fan-wiki]. The fan HUD shows 1/1, then 0/1 with "RELOAD" [Observed].
- **Projectile:** the orb [Fan-wiki]. In the fan maxres thumbnail, a small yellow-green dot with a translucent purple blob trails through the sky [Observed]. Whether that is the orb is [Unverified].
- **Impact / end result:**
  - "When deployed, it slows down all the opponents within its Area of Effect, while dealing moderate damage": 65% slow for 4.0 s at about 30 DPS ("Based on tested values"). "Players are at risk of suicide" [Fan-wiki].
  - What the field looks like is [Unverified].
  - A fan kill thumbnail shows the victim breaking into dark chunks inside a teal/cyan glow, with "KILLS" and "+150" on the HUD [Observed: https://i.ytimg.com/vi/7gdfSoWC2ZI/hq3.jpg]. Whether that glow is the Black Hole field is [Unverified].
- **Not a Graham concept:** File:Black_Hole_Shot.png (four sphere options, the purple swirl circled) was uploaded 2012-11-22 and captioned "Black Hole Shot Concepts" on the page for BB Zero's Black Hole Shot, a weapon of Wil's [Fan-wiki: Black Hole Shot; file metadata]. That is two years before the BBG Black Hole. The BBG orb resembles the circled option [Observed], so the design may have been reused [Inference].
- **Images viewed:** File:BlackHole.jpg, File:Black_Hole_Shot.png, 7gdfSoWC2ZI maxres, hq1, hq2 and hq3 (sheets bh.png, gen2.png, bhyt.png).
- **Depiction for shorts:** the swirling purple ball lobs out, lands and opens into a vortex. Everyone in it moves in slow motion while sparks nip at them. The vortex look is [BBG News invention]; the orb look is [Observed].
- **Confidence:** partial.

## Bind Field, formerly Slow Field (secondary; added BBG 2.6, Dec 20, 2013; renamed and reworked around 2.12, Oct 2014)
- **Official text (current):** "Make your opponents feel as old as you do. All enemies within the field stop and dream about bingo." [Game text via wiki] (https://battlebears.fandom.com/wiki/Bind_Field)
- **Official text (2013, as Slow Field):** "Make your enemies feel as old as you do. All enemies within the field will be slowed by 50%." [Game text via wiki, Dec 22, 2013 revision]
- **Era / status:**
  - "New: Slow Field Secondary / 50,000 Joules" in 2.6 [Fan-wiki: Versions/2.6].
  - The wiki moved "Slow Field" to "Bind Field" on 2014-10-02, the 2.12 release day, with the new description [Fan-wiki revision history]. So the rename probably shipped in 2.12 [Inference].
  - The wiki's stats drift [Fan-wiki revisions]:
    - 2013: 50% slow for 5 s, 2 ammo
    - Oct 2014: 95%
    - 2015: 50% for 2.5 s
    - Nov 2020 to now: 75% for 3 s, 1 ammo
  - The new text's "stop" fits a stronger, binding effect [Inference].
  - "The Bind Field was originally named the Slow Field, most likely renamed to prevent confusion with the Special ability Slow Motion Field." [Fan-wiki]
  - It is in the "Grahamzilla" bundle (listed as Slow Field) with the Radiation Rod for 85,000 Joules [Fan-wiki: Bundle Deals]. Its page lacks Category:BBG Weapons [Fan-wiki].
  - Which name it carries in 2026 is [Unverified].
- **Look:**
  - A dark-brown sphere (#2D170C) netted with glowing lime-green lines (#33F247) that form pentagon/hexagon cells.
  - Purple spiky knobs (#801C7D) sit at the nodes. It reads like a sea mine or a buckyball.
  - Held up in his right hand, about 0.27 H across [Observed: File:Slowfield.png].
  - On the Grahamzilla banner he holds it raised, wrapped in a pink-magenta glow [Observed: File:Grahamzillabundle.png].
- **Firing:** "firing a prickly purple-green ball in an arc at where the user is aiming". 1 ammo, 2.5 s rate, 3 s reload [Fan-wiki].
- **Projectile:** the prickly ball [Fan-wiki].
- **Impact / end result:**
  - "Upon impact with a solid surface (players excluded), it detonates and forms a medium-sized force field which slows all opponents caught in its radius by 75% for 3 seconds." "this weapon deals no damage" [Fan-wiki].
  - Slowed players show a yellow Z [Fan-wiki: Status Effects].
  - The field's colour and shape are [Unverified].
- **Images viewed:** File:Slowfield.png, File:Grahamzillabundle.png (sheets bh.png, bundles.png).
- **Depiction for shorts:** the spiky ball bounces and pops into a bubble laced with a green lattice. Enemies inside shuffle like grandpas with yellow "Z"s over their heads [Fan-wiki], dreaming of bingo [Game text joke]. The bubble look is [BBG News invention].
- **Confidence:** partial.

## Radiation Rod (secondary; BBG 2.5, Nov 27, 2013)
- **Official text:** "Straight from the core of the Ursa Major. Warning may cause spontaneous bear combustion if in contact for long periods of time." [Game text via wiki] (https://battlebears.fandom.com/wiki/Radiation_Rod)
- **Era / status:** 2.5 lists "Engineer secondary – Radiation Rod" [Fan-wiki: Updates]. It costs 75,000 Joules and is in the Grahamzilla bundle [Fan-wiki].
- **Look:**
  - A purple cylindrical fuel-rod canister (#65286E median; #7B337E lit) with a lime-green chevron stripe (#79F447) and a small green trefoil decal.
  - An end cap with a cluster of glowing green hexagonal vents.
  - Held level at the waist in both hands like a log, about 0.4 H long [Observed: File:Radiation_Rod.png].
  - The Grahamzilla banner shows the vent cap facing the camera [Observed: File:Grahamzillabundle.png].
- **Firing:** placed, not fired: "a placeable nuclear fuel rod". 5 rods, 1 s between placements, 3 s reload, 10 s duration [Fan-wiki].
- **Projectile:** none [Fan-wiki].
- **Impact / end result:**
  - It "creates a glowing radiation field when placed", irradiating at 60/s, "far faster than any other radiation-based weapons". It also blocks the lock-ons of the Sniper's primaries [Fan-wiki].
  - "the player is not affected by their own radiation", but the resulting blast can still hurt him [Fan-wiki]. Detonation works as in the shared section.
  - The field's colour and radius are [Unverified].
- **Images viewed:** File:Radiation_Rod.png, File:Grahamzillabundle.png (sheets bh.png, bundles.png).
- **Depiction for shorts:** Graham plants the purple rod upright. Its green vents glow, and a humming green haze dome surrounds it [BBG News invention]. Enemies who wander in get the trefoil almost at once [Fan-wiki].
- **Confidence:** partial.

## Dragon Slayzer (BBG) (secondary; BBG 2.51, Apr 13, 2018)
- **Official text:** none found. The page is a stub with no quoted description [Unverified].
- **Era / status:**
  - 2.51 reads "New weapon for Engineer (BBG) - the Dragon Slayzer (BBG)" [Fan-wiki: Updates]. It costs 400,000 Joules with no level lock [Fan-wiki].
  - The page was created 2020-05-28 [Fan-wiki revision, checked]. Its only image, File:Huggable-suction-pose.png (a pink Huggable from 2012), is an unrelated template leftover [Observed].
- **Look:**
  - A red dragon head (#CA0101 median) with green eyes, white teeth, small horns and spikes, and little red wings.
  - A long silver double-edged blade juts from its mouth.
  - Held at the hip, pointed down and forward. It is about 0.6 H long [Observed: File:DragonSlayzer(BBG).jpeg, uploaded 2018-05-12; zoom ds_full.png].
  - This 2018 render draws black outlines on Graham [Observed].
- **Firing / projectile:**
  - BBG infobox: explosives 10–20, damage 35, 1 s cooldown, 4 ammo, 4 s reload, projectile 800 u/s, and "Duration 4 seconds" for an unnamed effect [Fan-wiki].
  - What it fires in BBG is [Unverified].
  - In BBO (a different game, where it is Oliver's weapon): "The laser, which the dragon fires, is an orange blast", and it "fires a straight-moving laser that explodes on contact" [Fan-wiki: Dragon Slayzer].
  - That BBO page says "The dragon's color is red", but its "Default look ... as shown on the Gear Up menu" image shows a grey dragon head with grey wings, a green eye, a wrapped tan grip and a blade [Observed: File:DSNew.jpg]. The page conflicts with its own image.
  - A concept labelled "THE DRAGON SLAYZER" shows a winged dragon-head sword with a glowing tip [Observed: File:Image-1.jpg].
- **Impact / end result:** unknown [Unverified].
- **Images viewed:** File:DragonSlayzer(BBG).jpeg, File:DSNew.jpg, File:Image-1.jpg, File:Huggable-suction-pose.png (sheets ds.png, ds_full.png).
- **Depiction for shorts:** show it posed or as a sword-like prop. Any orange laser bolt is a [BBG News invention] borrowed from BBO.
- **Confidence:** partial (look observed; function unknown).

## T Square (melee; default; BBR v1.4 through BBG)
- **Official text:** "Tee off on your opponents with this classic tool. Ouch." [Game text via wiki] (https://battlebears.fandom.com/wiki/T_Square)
- **Era / status:** default melee and a v1.4 launch weapon [Fan-wiki]. It is the beta loadout's melee [Observed: File:Graham-gamma-ray.png]. 2.6: "Melee +1 decreased from 8 to 5" [Fan-wiki]. It is in the Groundhog Day bundle [Fan-wiki].
- **Look:**
  - A silver-grey ruler blade (#8B9292) with black tick marks, and a dark-brown/black, slightly curved crossbar head [Observed: File:T_Square.jpg].
  - He grips the end of the blade like a club, so the crossbar is the striking head [Observed: File:T_square.png (2012 melee list) and File:T_Square.jpg]:
    - In the 2012 list render it is raised over his right shoulder, crossbar above his hat.
    - In the 2013 render it is held upright in front of his chest, crossbar across his goggles.
  - Measured on the 2013 render, the blade is about 0.55 H long and the crossbar at least 0.55 H wide (it runs off the frame edge, perspective-inflated) [Observed, approximate].
  - HUD icon: a T-shaped ruler with tick marks [Observed: File:Graham-gamma-ray.png; U3XDJXo1Ej4 hq1 and hq3].
  - **Other art:**
    - File:Engineer-Graham.png shows a T-square with a silver ruled blade and a dark crossbar held in his left hand [Observed; provenance Unverified].
    - The card File:Graham_description.jpg has him leaning on a T-square with a tan blade and a dark crossbar [Observed].
    - The sketch File:Engineer1.png shows a dark crossbar with ticks on a light ruled blade [Observed].
- **Firing:** a melee swing for 55 damage with no stat modifier [Fan-wiki]. Engineer melees have "fast draw times" [Fan-wiki: Engineer (BBG)]. Class melee-swing barks: "Whippersnapper!" and "Delinquent!" [Fan-wiki].
- **Impact / end result:** the hit visual is undocumented [Unverified]. Class melee-kill barks include "Shouldn't you be in school?" and "Stay off of my lawn!" [Fan-wiki].
- **Images viewed:** File:T_Square.jpg, File:T_square.png, File:Graham-gamma-ray.png, File:Engineer-Graham.png, File:Graham_description.jpg, File:Engineer1.png, U3XDJXo1Ej4 hq1 and hq3 (sheets mel1.png, tsq_grid.png, tsq2012.png, eg_zoom.png, u3_hud.png).
- **Depiction for shorts:** a golf-swing "tee off" with the crossbar as the club head [Game text pun + Observed grip], then a THWACK with a star-burst and bouncing bolts [BBG News invention].
- **Confidence:** observed.

## Wrench (melee; BBR v1.4 through BBG)
- **Official text:** "Just a trusty monkey wrench. This will fix your enemies real good." [Game text via wiki] (https://battlebears.fandom.com/wiki/Wrench)
- **Era / status:**
  - A v1.4 launch weapon costing 45,000 Joules [Fan-wiki].
  - The 2012 melee list shows "WRENCH / EQUIPPED" [Observed: File:Wrench.png, File:Images_(5).jpg].
  - The HUD melee icon in SkyVu's beta thumbnails is this wrench [Observed: U3XDJXo1Ej4 maxres and hq2].
  - 2.6: "Speed Modifier increased from 0 to 10%", and Melee +1 dropped from 7 to 5 [Fan-wiki].
  - It is in the Groundhog Day bundle [Fan-wiki].
- **Look:**
  - A big orange pipe wrench (#E7720B lit, #B3601B in shade) with a dark-grey adjustable hook jaw (#63615D).
  - Held upright against his right shoulder, jaw beside his hat. About 0.75–0.8 H long [Observed, measured: File:Screen_Shot_2012-12-09_at_10.11.21_AM.png; File:Images_(5).jpg].
  - The Old School skin holds the same wrench [Observed: File:GRAHAM_ER.jpg, uploaded 2013-05-07].
  - The wiki notes "While the description calls Wrench a monkey wrench, it is actually a pipe wrench" [Fan-wiki]. The images agree [Observed].
- **Firing:** a melee swing for 30 damage, +10% speed. "It makes metal noises when used." [Fan-wiki]
- **Impact / end result:** the visual is undocumented [Unverified].
- **Images viewed:** File:Screen_Shot_2012-12-09_at_10.11.21_AM.png, File:Images_(5).jpg, File:Wrench.png, File:GRAHAM_ER.jpg, File:Radioactive_puddle.jpeg and File:Engineers_setup.jpg (HUD icons), U3XDJXo1Ej4 maxres and hq2 (sheets mel1.png, mel2.png, wr_cb_grid.png, u3_max_melee.png).
- **Depiction for shorts:** a big orange pipe wrench with a metallic CLANK [Fan-wiki sound]. The sparks are [BBG News invention].
- **Confidence:** observed.

## Double Wrench (melee; BBG 2.12, Oct 2, 2014)
- **Official text:** "Prepare for trouble and make it double... wrench." [Game text via wiki] (https://battlebears.fandom.com/wiki/Double_Wrench)
- **Era / status:** added in 2.12 [Fan-wiki: Updates]. Costs 140,000 Joules with a level 10 lock [Fan-wiki]. The first revision (2014-10-03) listed 37 damage, +20% special speed and −10% speed. The page now lists 30 damage and +30% special speed [Fan-wiki, checked].
- **Look:** "The wrench depicted in game is an open end wrench. An open wrench has two wrenches of different size on both ends." [Fan-wiki] No image exists on the wiki [checked: the page lists no images, and no file name starting "Double" or "Wrench" matches it]. The JustNubz Engineer chapter (34:42–39:57) could not be viewed [Unverified].
- **Firing:** a melee swing for 30 damage, +30% special (cooldown) speed [Fan-wiki].
- **Impact / end result:** undocumented [Unverified].
- **Images viewed:** none exist on the wiki.
- **Depiction for shorts:** a double-ended open spanner. Its colour and size are [BBG News invention]; its shape is per the [Fan-wiki].
- **Confidence:** documented.

## Crowbar (melee; BBG 2.21, Jul 3, 2015)
- **Official text:** "One of Graham's many unusual tools. A crow infused with a steel bar after radiation testing." [Game text via wiki] (https://battlebears.fandom.com/wiki/Crowbar)
- **Era / status:** added in 2.21 with five other melees [Fan-wiki: Updates]. Costs 150,000 Joules [Fan-wiki]. It does 55 damage with +15% health. The trivia calls it "the highest damaging melee out of all the Engineer's melees", but the T Square also does 55 [Fan-wiki, conflict].
- **Look:**
  - A purple crowbar (#693A59) whose hooked end is a crow's head with spiky dark-purple feathers, a tan beak and a pale yellowish eye.
  - Held diagonally in front of his body, the crow head above his hat. About 0.8–0.85 H long [Observed, measured].
  - The only image shows it with the White Graham skin [Observed: File:Image9.PNG].
- **Firing:** a melee swing [Fan-wiki].
- **Impact / end result:** undocumented [Unverified].
- **Images viewed:** File:Image9.PNG (sheets mel1.png, wr_cb_grid.png).
- **Depiction for shorts:** the crow head squawks on impact, and a puff of purple feathers comes off [BBG News invention].
- **Confidence:** observed.

---

## Other eras (brief)
- **BBF:** "He has the ability to deploy temporary Turrets which disappear after twenty seconds." [Fan-wiki: Graham (Hero)]
- **BBO** [Fan-wiki: Graham (BBO)]:
  - "Graham builds a big blue turret, shooting yellow plasma projectiles", which shuts down after 15 s.
  - A healing turret: "a big white/red machine" with a short heal beam.
  - Thunderdome: "a big dome" that slows opponents by 60% and blocks projectiles for 4.5 s.
  - "Graham Overclock" is a yellow-tone forcefield buff.
  - BBO's Dragon Slayzer belongs to Oliver.
- **BBH:** "Graham's "Photon Refractor" bounces between nearby enemies, inflicting progressively less damage with each jump. His Ultimate, "Turret Summon," allows him to deploy a gun turret from scrap, which auto-targets and fires at enemies within its vicinity." [Canon: battlebears.com/pages/characters]
- **BBG 3.0 (Nov 15, 2021):** "Speed 2 Equipment has been moved to default movement", "All +1 Equipment has been removed except Speed +1" and "Equipment Slot 2 has been removed" [Fan-wiki: Updates]. These change numbers, not visuals.
- **BBG 3.0.1 (Dec 18, 2021):** "Scale down weapon Graham in Home Menu" [Fan-wiki: Updates].

## Verifier's corrections to the draft and to the arsenal inventory
1. **Steam trailer dating.** The card (10.75–12.0 s) is the May 30, 2013 card [Observed]. The gameplay at 7.25–10.5 s is not "probably 2013 footage". Its black outlines match the 2018+ and 2026 renders, not the 2012–2015 in-game images, so its date is unsettled [Observed; Inference]. It is still the only official 2026 depiction of Graham's weapons; the playtest images are fan footage.
2. **The trailer skin is Instagraham**, matched to File:Instagrahamrl.png, which also holds the Gamma Ray [Observed]. This upgrades the earlier [Inference].
3. **File:Black_Hole_Shot.png is not a Graham concept.** It was uploaded 2012-11-22 as "Black Hole Shot Concepts" for BB Zero's Black Hole Shot, a weapon of Wil's [Fan-wiki].
4. **Bind Field.** It was renamed from Slow Field on the wiki on 2014-10-02 (the 2.12 release day). Its official text changed from "...will be slowed by 50%" to "...stop and dream about bingo", and its slow values changed several times [Fan-wiki revisions].
5. **Era fixes:**
   - BBG launched May 24, 2013 as "an all new app" [Canon: rfAyqVJrli4 description], not as a rename. BBR's own Feb 2013 rename was to "Battle Bears" [Fan-wiki].
   - BBG 2.x ran to 2.53.3 (Aug 31, 2018), not 2.51.
   - BBR 1.4.2 is Feb 28, 2013 [Fan-wiki: Updates and BBR Version 1.4.2]. The beta video is Oct 31, 2012 [YouTube date text; wiki metadata].
6. **Turret.** File:Turret_2.png is the wiki's "Turret's weapon icon", not a deployed view. The 1,800 range is in the page text, not the infobox. In File:Turret.jpg he carries the turret in front of him with both hands, not at his side. The relaxing sketch shows him leaning on the turret, not sitting on it.
7. **T Square.** It is gripped by the blade with the crossbar as the head, and about 0.55 H, not 0.75 H [Observed, measured].
8. **Power Glove.** "Taps fire / holding charges" is [Inference], not game text. Its design matches Graham's silver-and-cyan "Self-Enhanced Hand" art [Observed; link Inference].
9. **Radioactive puddle.** "Flat" is unsupported. The image shows a lumpy goo mass whose orientation can't be read [Observed].
10. **Kept from the draft, after checking:** the Gernobyl in the trailer [Observed; ID Inference, strong]; the radiation icon colours (the early disc #FBFE13; the late three yellow blades on black) [Observed]; the Rivet Gun emblem and canisters [Observed]; the Proximity Mine red lines [Observed]; the Crowbar damage conflict [Fan-wiki]; the Gernobyl patch note being a wiki transcription, not in-game text [Fan-wiki].

## Corrections for the character file
File: /home/user/thallo-site/bbg-news-repo/characters/graham.md
1. **The trailer look and its "orange drill-gun".**
   - Current: "Exception: the 2013 BBG trailer card shows a different look (rainbow-striped cap, black-rimmed glasses, red track jacket, orange drill-gun) [Observed] ([trailer][trailer13]), probably the "Instagraham" skin [Inference], so the card look stays the default; keep the trailer look for skin gags."
   - Correction: the skin *is* Instagraham. It matches File:Instagrahamrl.png: brown cap with a rainbow stripe, dark-rimmed goggles with camera-lens lenses (not glasses), red-brown fur, brown radio backpack [Observed]. The wiki calls it a "brown-coloured theme with a stripe of colours on his helmet and camera lens on his goggles" [Fan-wiki: Instagraham].
   - The "orange drill-gun" is the **Gamma Ray**, which Instagrahamrl.png also holds [Observed].
   - The "red track jacket" is probably the skin's red-brown fur plus the model's standard white arm stripes [Inference].
   - The same card is reused at 10.75–12.0 s of the 2026 Steam trailer, and the gameplay at 7.25–10.5 s shows this skin firing the Gernobyl, then the Gamma Ray [Observed].
2. **The Weapons bullet is incomplete.**
   - Current: "**Weapons:** BBG defaults [Fan-wiki] Power Glove (...), Turret (...) and T Square (...) ... BBH turret "from scrap" [Canon]".
   - Correction: list all 17 BBG weapons with eras [Fan-wiki]:
     - **Primaries:** Power Glove and Gamma Ray (v1.4, Nov 2012), Rivet Gun (2.1, Jul 2013), Hand Cannon (2.5, Nov 2013), Buzzsaw (2.6, Dec 2013), MuskIt (2.12, Oct 2014).
     - **Secondaries:** Turret and Proximity Mine (v1.4), Gernobyl (1.4.3, Apr 2013), Radiation Rod (2.5), Bind Field, formerly Slow Field (2.6), Black Hole (by Oct 31, 2014), Dragon Slayzer (2.51, Apr 2018).
     - **Melees:** T Square and Wrench (v1.4), Double Wrench (2.12), Crowbar (2.21, Jul 2015).
   - Note that only the Gamma Ray is confirmed in the 2026 build [Observed].
3. **The Gernobyl quote is truncated and mislabelled.**
   - Current: "Gernobyl, per the BBR v1.4.3 patch notes: "This mid-sized rodent shoots irradiated goop." [Game text via wiki] ([Updates][wup])".
   - Correction: the transcribed note reads "...This mid-sized rodent shoots irradiated goop: a hit will cause radiation damage and slight physical damage, if you miss an opponent it creates a radioactive puddle- any player who steps in it will receive radiation damage." The original has no full stop after "goop".
   - Label it [Fan-wiki transcription of App Store notes; Unverified against the store]; patch notes are not in-game item text.
   - Add the in-game text: "Radioactive goo never hurt anyone, unless of course it came from the contaminated mouth of an adorable little mutated mammal. The longer your exposure the greater your chance of death!" [Game text via wiki].
4. **Mechanical hand: side and in-game form.**
   - Current: "a dark blue-grey mechanical gauntlet hand (side unrecorded; BBG News: right [BBG News invention])".
   - Correction: File:Engineer-Graham.png (uploaded 2012-11-02) puts a silver mechanical hand with cyan circuit lights on his **right** arm [Observed; SkyVu provenance Unverified]. "Right" is now observed, not invented.
   - The in-game BBG model shows two red-gloved hands [Observed: File:Rivet_Gun.jpg, File:Slowfield.png, File:Turret.jpg]. In game, the hand's silver-and-cyan design appears only as the Power Glove weapon [Inference: the concept "Graham's Self-Enhanced Hand" is captioned "Power Glove Concept" by the wiki].
   - Keep the dark blue-grey version for card-era shorts only [Observed: File:Graham_description.jpg].
5. **Backpack era.**
   - Current: "olive-green backpack with twin exhaust pipes and a side vent".
   - Correction: that is the card look [Observed: File:Graham_description.jpg, File:Engineer-Graham.png]. Every in-game weapon render shows a boxy radio backpack with an antenna and a speaker grille: red by default, teal on the blue team, brown for Instagraham, a green warp pipe for Old School [Observed]. When a short shows in-game weapons, match the era, or mix them knowingly.
6. **T-square in the Prompt pack.**
   - Current: "holding a T-square".
   - Correction: the in-game T Square is a silver-grey ruler blade with black tick marks and a dark curved crossbar, gripped by the blade like a club, about 0.55 H [Observed: File:T_Square.jpg, File:T_square.png]. The card's T-square has a tan blade [Observed: File:Graham_description.jpg], while File:Engineer-Graham.png's is silver-bladed [Observed]. Say which era you want.
7. **Turret gag.**
   - Current: "(1) his back cracks like a ratchet and the turret swivels with each click".
   - Correction: the BBG Turret "cannot turn" and fires in a fixed 100° cone [Fan-wiki: Turret]. Keep the swivel as a knowing [BBG News invention], or have the turret ratchet up a notch per click as it "rises up" [Fan-wiki, early revision].
8. **2026 status (Open questions).**
   - Current: "2026 changes (Oct 19–26 demo; unviewed [fan showcase][showcase])".
   - Correction: the closed-playtest #4 Engineer chapter thumbnail (34:52 of -lAtv-j9Sms) shows Graham in the Old School skin holding the Gamma Ray. Playtest #3 HUDs show an orange gun at 100/100 and 0/100 with 120 max health [Observed]. The other weapons are unconfirmed.
9. **Skins line.**
   - Current: "Gold Graham, Old Timey, Graham Cracker, Holograham, Instagraham".
   - Correction: the class page also lists the specials Invisible Graham, Spider Graham and Old School, plus the generic default Graham and five colour variants (Brown, Cyan, Green, Purple, White) [Fan-wiki: Engineer (BBG)].
   - Old School is the skin in all 2026 playtest footage [Observed]. It is a Mario reference ("It's a me!", a warp-pipe backpack) [Fan-wiki: Old School], so it is risky to feature in shorts [Inference].

## Open questions
- Power Glove: what colour are its orbs, its charge ring and its charged-orb explosion?
- Rivet Gun: what do the rivets in flight and the "light purple", square damage fields look like on screen?
- Hand Cannon: what do the "green-black missile" and its explosion look like?
- Buzzsaw: what do the blade's flight, burrowing and explosion look like?
- MuskIt: what does its "bug spray" cone look like?
- Turret:
  - What are its bullets? Electric Honey bee-bullets, per the 2012 wiki, are unconfirmed.
  - How tall is it when deployed?
  - What are its real damage and range in the 2026 build?
- Black Hole:
  - What do the field's colour and shape look like? Is the teal glow in the fan kill frame the field?
  - Does it show the yellow "Z"?
  - Which update added it: 2.12, 2.13, or an unlogged patch?
- Bind Field:
  - What does its force field look like?
  - Is it called Bind Field or Slow Field in 2026, and what are its current slow values?
  - Did the rename ship in 2.12?
- Radiation Rod: what colour and radius does its field have?
- Dragon Slayzer (BBG): what does it fire, and what is its 4-second "Duration" effect?
- Double Wrench: what does it look like?
- 2026 roster: which of the 17 Engineer weapons are in the build? The JustNubz Engineer chapter (34:42–39:57) would answer this, but YouTube playback is blocked from this sandbox.
- 2026 Gamma Ray beam: are the pale-cyan hexagonal outlines in the VHo1O41RNJE 29:05 frame the beam?
- Steam trailer:
  - When was the Graham gameplay (7.25–10.5 s) captured: 2013, 2018 or later, or the 2026 build?
  - What makes the white flash edged with cyan lightning at 8.75–10.25 s?
- SkyVu's archived 2.6 change log is still unreachable (web.archive.org resets connections). All 2.6 numbers are unverified against SkyVu.
- Radiation threshold: is it 100 RP (Status Effects) or the target's maximum health (the Gamma Ray and Radiation Rod pages)? Is it 4.5 or 5 RP per Gamma Ray hit?
- Rivet Gun release: was it 2.1? The page says so, but the Updates log omits it.
- Art provenance: are File:Engineer-Graham.png, File:Graham_glove.png, File:Engineer1.png and File:Engineer2.png SkyVu art? The wiki gives no source.
