# Combat VFX and death conventions (Battle Bears Gold)

This dossier covers how combat looks in BBG as a whole, independent of any one weapon. It covers:
- how kills and deaths look for bears, robots and Huggables
- damage feedback, headshots, team colours and status-effect visuals
- pickups, respawn and explosions
- the game's overall effects style

It also settles the Bearzooka colour conflict.

**Sources I could reach today:**
- **Fan wiki:** about 90 pages through the MediaWiki API, plus about 45 wiki images.
- **Official 2026 Steam media:** the five Steam screenshots, the 54 s "Battle Bears Gold Premium - Trailer" (re-sampled at 10 fps around every kill), and a 1.4 s looping video embedded in the Steam store description (`extras/f7ecb9b2e78f0fd754cc7cf8220ad9b0.mp4`, downloaded).
- **Steam store text:** from the cached `appdetails.json`.
- **YouTube thumbnails only:** two 2013–14 fan gameplay videos the wiki embeds ("[Oliver]:Secondary - Bearzooka", AZt_huguhzc, published 2013-04-14; "Gamma Ray Demonstration", 0GuhKiAnNyc, 2014-01-03), and the 2026 JustNubz showcase (-lAtv-j9Sms), whose four thumbnails show only menus.
- **battlebears.com (live):** reachable, but it has no BBG combat or effects text; it is BB Heroes-era.

**Not reachable:**
- web.archive.org: seven curl attempts ended in connection resets, and WebFetch refused the host. No archived SkyVu blog or patch notes were read, so almost nothing here is [Canon] beyond Steam text and item descriptions.
- YouTube video content. I did not watch any video; YouTube claims come from thumbnail frames only.

**Eras:**
- **BBG 2013+:** the same game first shipped as Battle Bears Royale (BBR) in 2012 and was renamed Gold in 2013. The wiki's "BBR v1.x" and "BBG v2.x" version numbers belong to this one game.
- **BBG 2026:** the Steam re-release, out Nov 4, 2026.

Unless a section says otherwise, wiki mechanics describe BBG 2013–2015. Footage in the 2026 trailer and screenshots is official 2026 media; which build it was captured on is [Unverified].

**Path key (used in every "Images viewed" list):**
- `W` = `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons`
- `C` = `W/dl/combat-vfx`
- **Trailer timestamps:** `t_N` frames sit at (N−1)×0.5 s. My own 10 fps extractions are in `C/tr/` with these start times:
  - `rb_` 2.9 s; `bz_` 3.6 s; `gb_` 4.9 s; `gr_` 7.0 s; `tl_` and `tz_` 12.0 s
  - `wl_` 18.0 s; `bm_` 26.0 s; `nk_` 26.7 s (4 fps); `as_` 29.8 s
  - `rg_` 34.5 s; `sh_` 38.3 s; `ov_` 49.6 s
- Contact sheets of these frames are in `C/sheets/`.
- **Colour samples:** hex values are median-cut samples I took from the named image. They are approximate and not official codes [Inference].

## Quick summary of the conventions
- **Normal death:** the victim goes limp and topples as one intact body, with no blood. The corpse stays on screen for at least about 1–2 s [Observed].
- **Explosive or radiation death:** the body breaks into 4–7 large, clean, toy-like chunks (head, torso, limbs, backpack or flag) flung upward through a yellow faceted blast, with no gore visible [Observed]. The wiki says Demo explosives gib and that Tillman shows "pink and red flesh" [Fan-wiki]; I did not see the flesh.
- **Huggable rainbow blood:** this is SkyVu's gag from the earlier PvE games (BB-1, BB Zombies, BB Zero) [Fan-wiki]. In BBG footage, a Huggable breaks into plush pieces with gold sparkles [Observed], and its default bear-trap melee is smeared with rainbow colours [Observed]. No source shows confetti.
- **Effects style:** flat, saturated, semi-transparent faceted shapes, octagonal ground shockwaves, star-shaped hit sparks and 2D cartoon icons above heads [Observed]. 2026 media add a thick black ink outline to characters [Observed].
- **Team colours:** red and blue on character accents, the HUD, the kill feed, team flags and bombs, and on cloak, Peek A Boo and Energy Barrier glows [Observed/Fan-wiki]. Weapon projectiles keep their own colours [Inference from Observed].
- **Bearzooka:** coral-red with orange panels, not green [Observed].

---

## Overall VFX style (all weapons; BBG 2013 vs BBG 2026 media)
- **Official text:**
  - "All assets in this game are created by human artists." [Canon] (Steam store text, app 4408320)
  - "An award-winning 4v4 class shooter with more personality than sense!" [Canon] (Steam short description)
- **Look:**
  - **Explosions** are clusters of hard-edged, semi-transparent faceted volumes, not particle smoke. Their core is near-white to lemon (#FFFFEA, #FFFF6B, #FEF376) [Observed: screen_02.jpg; trailer 26.5–27.8 s; 50.6–51.8 s].
  - **Fire** is flat flame sprites in orange #F47E3E / #FAA751 [Observed: trailer 12.4–13.0 s].
  - **Smoke** is faceted grey-white puffs [Observed: Duo.png; trailer 51.8 s].
  - **Shockwaves** are flat octagonal rings on the ground, white on the space station and orange in the cave [Observed: trailer 50.6–51.8 s, 52.6–53.4 s; screen_02.jpg].
  - **Beams** are long flat ribbons with a white-hot core. Pink beams sample #FF5DFE / #FD51B1; yellow tracers are thin lines [Observed: screen_03.jpg; trailer 7.2–10.5 s, 38.3–41 s].
  - **Electricity** is jagged cyan polylines (#80FFFE) [Observed: screen_03.jpg].
  - **Hit sparks:**
    - Beam hits make 4-point pink stars [Observed: screen_03.jpg; trailer 7.2 s, 35.3 s].
    - Melee hits scatter 5-point yellow cartoon stars [Observed: trailer 35.8–36.3 s; screen_00.jpg].
  - **Status indicators** are flat 2D sprites above heads [Observed: trailer 8.2–8.8 s; Images_(3).png; 0GuhKiAnNyc hq1].
- **Ink outline:**
  - In the 2026 Steam screenshots, the trailer gameplay and the Steam store loop video, characters have a thick black ink outline [Observed: outline_compare.jpg (screen_01 crop); steam_extra.jpg].
  - 2013 captures on the wiki have none [Observed: A_life_upside_down.png (uploaded 2013-04-27); Photo_19-04-13_12_02_26_PM.png].
  - It is [Unverified] whether this is a 2026 engine change or a capture filter. Because it appears in both trailer gameplay and the screenshots, it is probably the 2026 look [Inference].
- **HUD palette (2013 capture):** health bar green #178602, red team #FC0101, blue team #023DF6 [Observed: A_life_upside_down.png].
- **Firing / Projectile / Impact:** see the sections below.
- **Images viewed:** `W/visuals/steam_screens/screen_00.jpg`–`screen_04.jpg`; `C/sheets/trailer_sheet_0.jpg`–`trailer_sheet_8.jpg` (from `W/visuals/trailer/t_0001.jpg`–`t_0108.jpg`); `C/sheets/outline_compare.jpg`; `C/png/A_life_upside_down.png`; `C/sheets/steam_extra.jpg` (frames of `C/steam/extra.mp4`, from https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4408320/extras/f7ecb9b2e78f0fd754cc7cf8220ad9b0.mp4); `C/png/Duo.png`
- **Depiction for shorts:** Build every effect from hard-edged, flat-shaded, semi-transparent shapes in saturated pink, cyan, yellow and orange. Use an ink outline on characters for the 2026 look and none for the 2013 look [Observed]. Effect timings (frame counts and holds) are [BBG News invention].
- **Confidence:** observed

## Ordinary deaths: ragdoll collapse (all classes; BBG 2013 and 2026 media)
- **Official text:** none found [Unverified].
  - The wiki implies a death animation exists. When a Huggable dies using Mini Me it "may occasionally… freeze in its position of death without going through the death animation" [Fan-wiki: Mini Me].
- **Look:** the victim goes limp and topples as one intact body. Four examples:
  1. A white-headed, black-suited bear (skin unidentified) on the Aztec temple map falls backwards and lies face-down. The body is still there at 14.9 s, when the shot ends [Observed: trailer 12.6–14.9 s].
  2. A sniper in blue pyjamas with a green face mask collapses face-down; the pink Huggable that hit her stands over the body. That she is Astoria in a skin is [Inference] [Observed: trailer 31.7–32.7 s; t_0066.jpg].
  3. A blue-team white-and-blue bear holding a round purple-blue shield with a magenta core slumps to the floor after a purple beam hits [Observed: trailer 40.4–41.2 s].
  4. A green Heavy pitches over backwards (2013) [Observed: A_life_upside_down.png]. That it is dying is [Inference] from the file name and the kill feed.
- No blood, darkening or fade-out was seen [Observed]. One corpse was briefly tinted red by the Dead Eye skull glow [Observed: trailer 13.7 s].
- **Firing:** n/a.
- **Projectile:** n/a.
- **Impact / end result:**
  - At the death site, "Three [Joules pickups] are dropped… and disappear after 10 seconds" (since v2.1) [Fan-wiki: Pick-Ups; Joules].
  - How long the corpse stays and how it despawns is [Unverified].
  - Separately, Wil is hurled spinning through a fireball with his limbs splayed, still intact. Whether that blast killed him is [Unverified] [Observed: trailer 19.5–21.5 s].
- **Images viewed:** `C/sheets/seq_tl.jpg`; `C/sheets/tl_zoom.jpg`; `C/sheets/seq_as.jpg`; `C/sheets/seq_sh.jpg`; `C/sheets/seq_wl.jpg`; `W/visuals/trailer/t_0066.jpg`; `C/png/A_life_upside_down.png`
- **Depiction for shorts:** a floppy cartoon pratfall onto the floor, the body staying whole, then a hard cut. Dizzy spirals or orbiting stars on the KO are [BBG News invention]. Never show blood; none appears in the game [Observed].
- **Confidence:** observed

## Explosive and radiation deaths: gibbing into clean chunks (bears, robots, Huggables; BBG)
- **Official text:**
  - "Your enemies won't have a skull or bones after being hit with ice cold rockets!" [Game text via wiki] (Let It Cold)
  - "Just when you thought the huggable could not be any more dangerous, it takes it's head off and tries to kill you... to death." [Game text via wiki] (Losing Your Head)
- **Wiki:**
  - "The Double Hug is one of two of the Demo's weapons that do not gib players, the other is the Reverse Fountain." [Fan-wiki]
  - "Although the Demo has no other indication of being even partly organic, he has pink and red flesh as revealed when he is gibbed in-game." [Fan-wiki: Demo (BBG)]
  - When the Chub Scout "explodes with his suicidal weapons, he explodes into his default skin" whatever skin he wears [Fan-wiki: Headlights].
- **Look:**
  - **Bear:** a Green Oliver-skin Soldier (blue team) is cut down by B-1000 (orange energy streaks, then a cyan jagged blade swipe). His head with its blue headband, his torso with a blue belt band, an arm with a blue cuff and his white-lilac backpack come apart as big clean chunks and fly up and away. No inner surfaces or blood are visible [Observed: trailer 4.9–5.6 s; `C/sheets/gib_green.jpg`]. Which B-1000 weapon did it is [Unverified].
  - **Huggable:** an orange Huggable with a blue flag pops into its head, arms, legs and torso. The pieces are orange plush with blue stitch marks (#F4972D / #FBBB3A), with gold sparkle particles and a yellow-white blocky blast [Observed: trailer 8.9–9.0 s; screen_03.jpg].
  - **Robot / armour:**
    - In the nuke corridor, orange-and-blue armour chunks, a pink chunk and a mottled orange piece are flung up through a translucent yellow faceted blast [Observed: trailer 26.5–27.8 s; nuke_gibs.jpg].
    - Bright-red, armour-like body chunks (a helmet/head piece, two fists, forearms) tumble in mid-air [Observed: screen_04.jpg; trailer 26.2–26.5 s]. That they are B-1000 is [Inference].
  - **Pattern:** about 4–7 large pieces per body, each keeping its colour and texture [Observed]. The "pink and red flesh" on Tillman gibs [Fan-wiki] was not seen [Unverified].
- **Firing:** n/a.
- **Projectile:** n/a.
- **Impact / end result:**
  - Gibbing follows radiation explosions and nuke blasts [Observed] and most Demo explosives [Fan-wiki].
  - Whether every explosive weapon gibs is [Unverified].
- **Images viewed:** `C/sheets/bz_sheet.jpg`; `C/sheets/gib_green.jpg`; `C/sheets/graham_sheet.jpg`; `C/sheets/graham_zoom.jpg`; `W/visuals/steam_screens/screen_03.jpg`; `W/visuals/steam_screens/screen_04.jpg`; `C/sheets/s04_zoom.jpg`; `C/sheets/seq_bm.jpg`; `C/sheets/nuke_gibs.jpg`
- **Depiction for shorts:** The victim pops into a handful of clean toy pieces (head, body, limbs, backpack or flag) that tumble with a puff of faceted smoke. This matches the game [Observed]. Never show insides: use white stuffing or fluff for Huggables, loose bolts and springs for robots and sparks for bears [BBG News invention]. A "reassemble and walk off" gag is [BBG News invention].
- **Confidence:** observed

## Huggable deaths and "rainbow blood" (BB-1 / BB Zombies / BB Zero vs BBG)
- **Official text:**
  - "Remove your head and fire out a cutting death beam of rainbow essence." [Game text via wiki] (Headlights)
  - "By pressing small amounts of rainbow out of their bodies, Huggables can match the color of their surroundings…" [Game text via wiki] (Peek A Boo)
  - "Huggable viscera is pretty!" and "A huggable's rainbow soul can power a laser gun!" are SkyVu YouTube copy for BB-1 shorts [Canon per prior BBG News notes; not re-verified today].
- **Wiki:**
  - "They have rainbow blood that flies out from the body vertically when the Huggable is beheaded" [Fan-wiki: Huggable].
  - Headlights is "based off of the death animation for the Huggable when it is shot in the head in Battle Bears -1, Battle Bears: Zombies and Battle Bears Zero, where the head would fly off far into the distance, leaving behind a trail of rainbows" [Fan-wiki]. That death animation belongs to the PvE games, not BBG.
- **Look in BBG:**
  - Bite Me's bear-trap jaws carry iridescent rainbow smears, which the wiki calls "Huggable blood" [Observed: HuggyBiteMeCR.png; Fan-wiki: Bite Me].
  - The one observed BBG Huggable death is a plush gib with gold sparkles and no rainbow spray [Observed: trailer 8.9 s].
- **The 3.3–3.8 s rainbow fan:**
  - A pink red-team Huggable is clipped by a yellow tracer. A fan of red, yellow, green and blue streaks (#E35254 / #E3B935 / #41A13E) bursts upward from a magenta point at its feet, narrows into a vertical column over about 0.5 s, and the Huggable glows pink-white [Observed].
  - At 3.8 s it is still standing [Observed], so no death is shown.
  - The best match is Peek A Boo: "a short burst of rainbow energy will be emitted above the Huggable" [Fan-wiki] → [Inference].
- **Other rainbow effects:**
  - **Steam store loop:** an orange Huggable flies arm-first, trailing white-core shards of yellow, green, orange, cyan and violet [Observed: steam_extra.jpg]. This matches So Fly ("fly forward a short distance in a stream of rainbows") [Fan-wiki] → [Inference].
  - **Double Rainbow!:** "two spinning rainbows that rotate around the user" [Fan-wiki]. A rainbow ring circles the orange Huggable's waist at trailer 7.2–8.5 s [Observed]; that it is Double Rainbow! is [Inference].
- **Firing / Projectile:** n/a; see the Huggable class dossier for the abilities.
- **Impact / end result:** see Look.
- **Images viewed:** `C/sheets/rainbow_sheet.jpg`; `C/sheets/rainbow_zoom.jpg`; `C/png/HuggyBiteMeCR.png`; `C/sheets/misc3.jpg`; `C/sheets/steam_extra.jpg`; `C/sheets/graham_zoom.jpg`; `C/png/Huggable-suction-pose.png`
- **Depiction for shorts:**
  - A Huggable KO as a short upward rainbow streak fountain plus plush pieces and a puff of white fluff. It honours SkyVu's long-running rainbow gag [Fan-wiki/Canon per prior notes], but in a BBG-set short it is a [BBG News invention], because BBG footage shows plush chunks.
  - "Rainbow confetti" appears in no source; label it [BBG News invention].
- **Confidence:** partial

## Damage feedback (all classes; BBG)
- **Official text:** none found [Unverified].
- **Look:**
  - **Hit flash:** a hit target brightens for a frame or two:
    - the orange Huggable turns bright yellow [Observed: trailer 7.9 s, 8.2 s]
    - the cyan Huggable flashes light cyan under Riggs's pink beam [Observed: trailer 34.8–35.6 s]
  - **Beam contact:** a pink 4-point star spark [Observed: screen_03.jpg; trailer 7.2, 7.4, 8.4, 35.3 s].
  - **Melee contact:** small yellow-white 5-point stars [Observed: trailer 35.8–36.3 s; screen_00.jpg].
  - **HUD health bar:**
    - Top-left, "A green bar… which degrades to red as it is depleted" [Fan-wiki: Health]; green and part-red bars appear in screenshots [Observed: Sonic_wave_glue_bomb.png; Glue_bomb_on_a_wall.png].
    - A later version added numbers to the bar [Fan-wiki].
  - **Damage numbers:** none in any image I examined [Observed absence; Unverified overall].
  - **Pain barks:** e.g. Tillman "You call that PAIN?!" [Fan-wiki: Demo (BBG)].
  - **Enemy markers:** a red triangle and green name text float above an enemy [Observed: 0GuhKiAnNyc hqdefault/hq1 (2014 fan video)]. What the marker colours mean is [Unverified].
- **Firing / Projectile:** n/a.
- **Impact / end result:** see Look.
- **Images viewed:** `C/sheets/graham_zoom.jpg`; `C/sheets/riggs_cupcake.jpg`; `W/visuals/steam_screens/screen_00.jpg`; `W/visuals/steam_screens/screen_03.jpg`; `C/sheets/effects1.jpg`; `C/sheets/yt_0GuhKiAnNyc.jpg`; `C/crops/gamma_hq2_x2.png`
- **Depiction for shorts:** a one-frame white or bright flash on the target plus a star spark (pink for beams, yellow for punches) [Observed]. Floating damage numbers would be [BBG News invention].
- **Confidence:** observed

## Headshots, sniper locks and (no) critical hits (Sniper primaries; BBG v1.4.3+)
- **Official text:**
  - "Got a problem? The Deadeye is your solution. She may not have the biggest clip but she definitely has the biggest kick. If you understand the value of power, this is the rifle for you." [Game text via wiki] (Dead Eye)
- **How a headshot works:**
  - A white-lock shot "is guaranteed to kill the opponent, regardless of his/her remaining health. When an opponent is killed in this way it is a headshot, and shows up on the update feed differently" [Fan-wiki: Dead Eye].
  - **Scoped warning:** "a red crosshair will appear over the player's head" [Fan-wiki: Status Effects].
  - **Kill-feed card:** the killer's portrait (blue outline), the words "HEAD SHOT", and the victim's portrait under a red crosshair [Observed: Sonic_wave_glue_bomb.png; headshot_feed.png].
  - On screen, Demo and Sniper lock-ons show a red bracket reticle around a "!" [Observed: Duo.png; Imagef.png]. That this is the lock reticle is [Inference].
- **Critical hits:** no BBG crit system was found. "Critical Chance / Critical Damage" belong to Battle Bears Overclock weapons [Fan-wiki: Rocket Launcher (BBO)], so BBG probably has no crits [Inference]. Instant kills come only from headshots and radiation [Fan-wiki: Health].
- **Firing:** for the Dead Eye, "a single, red, stream-like bullet that erupts into a flurry of glowing, transparent buffalo skulls" [Fan-wiki].
- **Projectile:** a thin pale zigzag trail runs to the victim [Observed: trailer 12.2 s].
- **Impact / end result:**
  - Cartoon flames burst around the victim, then a large translucent red horned skull (#FE2B35 / #971031) rises and fades while he topples [Observed: trailer 12.4–13.7 s].
  - Identifying this as a Dead Eye kill is [Inference].
  - What happens to the head on a headshot is [Unverified]; no image shows it.
- **Images viewed:** `C/sheets/tl_zoom.jpg`; `C/sheets/seq_tl.jpg`; `C/crops/headshot_feed.png`; `C/sheets/effects1.jpg`
- **Depiction for shorts:**
  - A red crosshair blinking over the target's head, the shot, then a "HEAD SHOT"-style card with original art, not the game's UI [BBG News invention].
  - For a Dead Eye kill, a ghostly red buffalo skull rising [Observed]. The head stays on [BBG News invention].
- **Confidence:** partial

## Kill feed, rewards and announcer text (HUD; BBG 2013–14)
- **Official text:** none.
- **Look:**
  - "[killer portrait] KILLS [victim portrait]", with portraits outlined in team red or blue [Observed: A_life_upside_down.png; AZt_huguhzc hq3].
  - "SUICIDE" lines; bomb deaths count as suicides [Observed: Plant_the_bombbbbbb_b.png; Fan-wiki: Plant the Bomb].
  - "ASSIST +11" with a lightning-bolt icon [Observed: A_life_upside_down.png].
  - Large green "OH BABY" text mid-screen [Observed: A_life_upside_down.png]. Its meaning is [Unverified]; possibly a streak call [Inference].
  - "XP +25" and "⚡+100" under a kill line [Observed: 0GuhKiAnNyc hq3].
  - Stacked "⚡ +25" lines [Observed: Glue_bomb_on_a_wall.png]; that these are Joule pickups is [Inference].
- **Wiki:** "100 Joules automatically for each kill (as of version 2.17)" [Fan-wiki: Joules].
- **Firing / Projectile:** n/a.
- **Impact / end result:** see Look.
- **Images viewed:** `C/png/A_life_upside_down.png`; `C/sheets/yt_AZt_huguhzc.jpg`; `C/sheets/yt_0GuhKiAnNyc.jpg`; `C/sheets/effects1.jpg`
- **Depiction for shorts:** a red-vs-blue portrait strip with "KILLS" or "HEAD SHOT" and a lightning-bolt reward, redrawn in original art with no game UI or logos [BBG News invention].
- **Confidence:** observed

## Team colours, red vs blue (all classes and effects; BBG)
- **Official text:** "compete for dominance across competitive 4v4 multiplayer modes" [Canon] (Steam).
- **Look, characters (accents):**
  - **Soldier:** headband, wristbands and ankle bands are red in menus [Observed: OliverSkin.png; GreenSkin.png; Photo_19-04-13_12_02_26_PM.png] and blue for blue-team players in matches [Observed: trailer 3.9–4.8 s, Green Oliver skin with blue headband, gloves and belt band; AZt_huguhzc thumbnails, brown Oliver in a blue headband].
  - **Huggable:** it "has a flag respective to the team color that only shows up in a match" [Fan-wiki]. Red flag [Observed: trailer 3.3 s]; blue flags [Observed: trailer 7.2–9 s; screen_00.jpg].
  - **Tillman:** black and red armour on the red team [Observed: trailer card t_0058; Ohmagawdyas.png]; white, blue and black on the blue team [Observed: trailer 18–22 s].
  - **B-1000:** maroon on red, "dark blue" on blue [Fan-wiki].
  - **Sniper:** "gloves with the colour of the team colour" [Fan-wiki per astoria.md].
- **Look, HUD:** red score on the left (#FC0101), blue on the right (#023DF6); kill-feed portrait outlines in team colour [Observed: A_life_upside_down.png; headshot_feed.png].
- **Look, effects:**
  - Cloaking's aura "sports the user's team color" (from v1.4.2) [Fan-wiki].
  - Peek A Boo shows "neon red/blue lines (depending on the player's team)" [Fan-wiki].
  - Energy Barrier: "the player will begin to glow their team coloured" [Fan-wiki].
  - Plant the Bomb uses a bomb and tube "in each team's color"; the blue bomb is a round blue cartoon bomb with a fuse [Observed: Blue-bomb.png; Fan-wiki].
- **Projectile:** projectiles are not team-coloured in the footage. Yellow tracers come from both sides, pink beams from red-team Graham and red-skinned Riggs, and a purple beam hits a blue-team bear [Observed]. As a general rule this is [Inference].
- **Firing:** n/a.
- **Impact / end result:** n/a.
- **Images viewed:** `C/sheets/oliver_skins.jpg`; `C/sheets/bz_sheet.jpg`; `C/sheets/yt_AZt_huguhzc.jpg`; `C/sheets/rainbow_zoom.jpg`; `C/sheets/graham_zoom.jpg`; `C/sheets/seq_wl.jpg`; `C/sheets/misc4.jpg`; `C/png/Blue-bomb.png`; `C/png/A_life_upside_down.png`
- **Depiction for shorts:**
  - Team identity goes on accents: headband and cuffs, the Huggable's flag, Tillman's armour panels. Weapon effects keep each weapon's own colours.
  - The BBG News default stays red team.
  - Team-coloured glows only for cloak, Peek A Boo and Energy Barrier [Fan-wiki].
- **Confidence:** observed

## Explosions in general (all explosive weapons; BBG)
- **Official text:**
  - "Phat chance that you'll be dodging this baby. Flies out of sight and, just when you've forgotten about it, hits fast and hard like a liquored up grandpa." [Game text via wiki] (Phat Man)
  - "It's not to be taken lightly WAKKA WAKKA WAKKA!" [Game text via wiki] (Light Matter)
  - "Tillman really likes fireworks, so much so he turns a beautiful fountain into a deadly shower of sparks and fire!" [Game text via wiki] (Reverse Fountain)
- **Look:**
  - **Standard fireball:** an orange-yellow faceted burst with flame tongues and grey faceted smoke [Observed: trailer 19.5–21.5 s (fireballs behind Wil); t_0006 (orange fireball)].
  - **Nuke (Phat Man / Piece Maker):**
    - It rises on a yellow-white flame trail and comes down on one [Observed: Up1.png; Down1.png].
    - A yellow light column marks the drop, with an olive bomb carrying a yellow-black trefoil [Observed: screen_04.jpg; trailer 26.2–26.5 s]. That it is the Phat Man is [Inference].
    - The blast is a translucent yellow faceted dome that fills the room and flings gibs [Observed: trailer 26.5–27.8 s].
    - Then a mushroom cloud of translucent white faceted puffs [Observed: Duo.png].
  - **Radiation self-explosion:** "the same as the Piece Maker and Phat Man explosion animation"; its size "depends on the victim's size" [Fan-wiki: Gamma Ray]. Observed as a yellow-white blocky blast plus gibs [Observed: trailer 8.9–9.0 s] and a full-screen yellow-white flash [Observed: 0GuhKiAnNyc hq3].
  - **Electric (Light Matter):** "notably large, blinding, and electrified" [Fan-wiki]. An opaque white sphere wrapped in jagged cyan lightning [Observed: Photo.png]. The same look appears at trailer 8.7–10.4 s and in screen_03.jpg [Observed]; the identification is [Inference].
  - **Dark Matter:** "a sphere of energy blocks the target's vision" [Fan-wiki].
  - **Plant the Bomb detonation:** a huge white-grey faceted cloud [Observed: Plant_the_bombbbbbb_b.png]. The bomb beeps and pulses during its last 30 s [Fan-wiki].
  - **Shockwave rings:**
    - Expanding white octagonal rings on the space station [Observed: trailer 50.6–51.8 s; screen_02.jpg].
    - An orange cone from the sky followed by orange octagonal rings in the cave map [Observed: trailer 52.6–53.4 s].
    - Which weapons made these is [Unverified].
  - **Other explosive looks:**
    - Fireworks "expode into a flurry of damaging, orange sparks" [Fan-wiki].
    - Losing Your Head makes "a bright blue blast" [Fan-wiki].
- **Firing / Projectile:** see the weapon dossiers.
- **Impact / end result:** many explosives also hurt the user ("easy to kill yourself with"; Phat Man "prone to suicide") [Game text via wiki / Fan-wiki].
- **Images viewed:** `W/visuals/trailer/t_0006.jpg`; `C/sheets/seq_wl.jpg`; `C/sheets/seq_bm.jpg`; `C/sheets/nuke_gibs.jpg`; `C/sheets/effects1.jpg`; `C/sheets/effects2.jpg`; `C/sheets/misc3.jpg`; `C/sheets/seq_ov.jpg`; `W/visuals/steam_screens/screen_02.jpg`; `W/visuals/steam_screens/screen_04.jpg`
- **Depiction for shorts:** flash, then a chunky faceted fireball (yellow core, orange edge), then a flat octagonal ring sliding along the ground, then a faceted grey-white puff. Nukes add a sky beam and a white faceted mushroom cloud [Observed]. A soot-face gag on a survivor is [BBG News invention].
- **Confidence:** observed

## Irradiated (Gamma Ray, Gernobyl, Radiation Rod and others; Engineer; BBG v1.4.3+)
- **Official text:**
  - "Turn your enemies in to walking explosives with this radioactive ray gun. It does very little damage on initial impact, but once you charge them up all the way...BOOM! The radioactive symbol over their head indicates how charged they are. The bigger they are, the longer it takes to blow them up, however yielding a much larger and more aggressive explosion." [Game text via wiki] (Gamma Ray)
  - "Straight from the core of the Ursa Major. Warning may cause spontaneous bear combustion if in contact for long periods of time." [Game text via wiki] (Radiation Rod)
- **Look:**
  - "a yellow circle will appear over the player's head and a noise from a Geiger counter will begin sounding… three portions of the circle will dissolve into the common radioactivity symbol" [Fan-wiki: Status Effects]. The stage icons run from a full ring to a trefoil [Observed: Hazard-3.png, Hazard-0.png].
  - In the 2026 trailer: a yellow trefoil (#FACD21) on a black disc that grows over about 0.6 s [Observed: trailer 8.2–8.8 s].
  - In 2014 fan footage: a large yellow wedge-disc above the target [Observed: 0GuhKiAnNyc hq1, hq2].
- **Firing:**
  - Gamma Ray: "a short-ranged constant yellow beam" [Fan-wiki].
  - Gernobyl: "irradiating globs of light green goo" that leave puddles [Fan-wiki]. The puddle is a big translucent lime blob (#A1D22C / #C2E330) [Observed: Radioactive_puddle.png].
  - Radiation Rod: a placed "glowing radiation field" [Fan-wiki].
- **Projectile:** see Firing.
- **Impact / end result:**
  - At full radiation the target "will die instantly in a relatively large explosion" that also hurts others nearby [Fan-wiki].
  - It gibs [Observed: trailer 8.9 s]. The irradiating weapon in that trailer shot is [Unverified]; the visible beam there is pink.
- **Images viewed:** `C/sheets/graham_zoom.jpg`; `C/sheets/graham_sheet.jpg`; `C/sheets/icons.jpg`; `C/crops/gamma_hq2_x2.png`; `C/sheets/yt_0GuhKiAnNyc.jpg`; `C/sheets/misc3.jpg`
- **Depiction for shorts:** a ticking yellow-black trefoil filling up above the victim with Geiger clicks speeding up [Fan-wiki], then a yellow flash and a toy-piece pop [Observed]. The victim trembling first is [BBG News invention].
- **Confidence:** observed

## Poisoned (Mother of Nature, Chaos Toss, Toxic Rifle, Hazard Toy, Fear Orbit and others; BBG)
- **Official text:**
  - "Shoots poisonous berries at your enemies that drain their health over time." [Game text via wiki] (Mother of Nature)
  - "Spray your enemy with toxins that deal poison damage overtime and can stack with each bullet!" [Game text via wiki] (Toxic Rifle, v2.15)
- **Look:** "a purple/green skull will appear over the player's head" [Fan-wiki: Status Effects]; Mother of Nature uses "a small purple skull" [Fan-wiki].
- **Firing / Projectile:**
  - Mother of Nature: "a large purple berry" fired in an arc [Fan-wiki].
  - Chaos Toss: "a gleaming orb" lobbed from a skeletal hand [Fan-wiki].
  - Fear Orbit: two poison orbs circling Botch [Fan-wiki].
- **Impact / end result:**
  - Mother of Nature: "a large purple plume of poison", 4 damage a second for 10 s [Fan-wiki].
  - Chaos Toss: "a toxic green cloud" [Fan-wiki].
- **Images viewed:** none of the poison effect; no frame found.
- **Depiction for shorts:** a purple (Riggs) or green (Botch) faceted cloud, with a little cartoon skull bobbing over the victim's head [Fan-wiki]. A green tint on the victim's face is [BBG News invention].
- **Confidence:** documented

## Slowed, glued, bound or held (Slow Motion Field, Glue Bomb, Bind Field, Phantom Hug, Freeze Blast; BBG)
- **Official text:**
  - "Slows down all nearby enemies for a limited time." (Slow Motion Field)
  - "Glue plus bomb equals very slow battle bears." (Glue Bomb)
  - "Make your opponents feel as old as you do. All enemies within the field stop and dream about bingo." (Bind Field)
  - "The Huggable's ability to love will make time seem like it comes to a halt. When actually it's just your feet and you're about to die." (Phantom Hug)
  - "Blastin you with FREEEZEEEEE!!!" (Freeze Blast)
  - All [Game text via wiki].
- **Look:**
  - Slowed players get "a yellow Z" over their head [Fan-wiki].
  - Slow Motion Field: "a yellow circle forms around the player" [Fan-wiki].
- **Firing / Projectile:**
  - Glue Bomb: thrown in an arc; it sticks to a surface and explodes after 1 s [Fan-wiki]. A small purple blob stuck in a doorway [Observed: Glue_bomb_on_a_wall.png].
  - Bind Field: "a prickly purple-green ball" [Fan-wiki]. Graham holds a brown ball with purple nodes and green seams [Observed: Slowfield.png].
  - Phantom Hug: "a cluster of pink energy in the shape of a Huggable" [Fan-wiki]. A glowing translucent pink Huggable silhouette [Observed: PH_MenuDisplay.png].
  - Freeze Blast: "small blue projectiles" [Fan-wiki].
- **Impact / end result:**
  - Glue Bomb: blue concentric rings on the ground [Observed: Sonic_wave_glue_bomb.png]; 2 s slow [Fan-wiki].
  - Bind Field: a force field with a 75% slow for 3 s [Fan-wiki].
  - Phantom Hug: cannot move or turn for 2.5 s [Fan-wiki].
  - Freeze Blast: slowing pools on the floor [Fan-wiki].
- **Images viewed:** `C/sheets/effects1.jpg`; `C/sheets/effects2.jpg`; `C/sheets/misc4.jpg`
- **Depiction for shorts:** feet stuck in glue rings or a pink hug-ghost wrapping the victim, with a big yellow "Z" floating up [Fan-wiki]. Snail-speed walk cycles are [BBG News invention] (the Slow Motion Field menu icon pairs a bear with a snail [Observed: SlowMotionField.png]).
- **Confidence:** partial

## Stunned (Sucker Punch; Heavy; BBG)
- **Official text:** "Lobs a projectile that will stun the target for a few seconds." [Game text via wiki]
- **Look:**
  - "a blue Nuggs will appear over the player's head… having them appear dazed" [Fan-wiki].
  - A round blue bird circled by grey swoosh arrows above the target [Observed: Images_(3).png, the wiki's "Stunned Status symbol"].
  - Before a change it was "a green question mark" [Fan-wiki].
- **Firing:** Riggs fires a pink, cube-headed, Huggable-like launcher [Observed: SuckerPunch.png].
- **Projectile:** "a small, pink Huggable-like head" that stays solid after hitting and can push players [Fan-wiki].
- **Impact / end result:** fully immobilised for 2.6 s [Fan-wiki].
- **Images viewed:** `C/crops/stun_x3.png`; `C/png/SuckerPunch.png`
- **Depiction for shorts:** a pink plush head bonks the victim, a little blue Nugg bird circles their head, and they sway dazed [Fan-wiki/Observed]. Tweeting sounds are [BBG News invention].
- **Confidence:** partial

## Frozen (S'no Matter, Let It Cold; Demo; BBG v2.15+)
- **Official text:**
  - "It S'no Matter how fast you can move, I can just freeze you!" [Game text via wiki] (S'no Matter)
  - "Your enemies won't have a skull or bones after being hit with ice cold rockets! These rockets explode on impact and freezes the opponent for a small duration" [Game text via wiki] (Let It Cold)
- **Look:** the frozen-state visual is [Unverified]; no image found.
- **Firing:** S'no Matter fires "a slow moving gray projectile at a straight trajectory" [Fan-wiki].
- **Projectile:** see Firing.
- **Impact / end result:** the S'no Matter blast "freezes anyone in the blast radius for 2 seconds, leaving them unable to move or rotate the camera"; it may also freeze teammates [Fan-wiki].
- **Images viewed:** none.
- **Depiction for shorts:** an ice-block shell or frost tint with a rigid pose is [BBG News invention]. Keep the 2 s hold as the beat [Fan-wiki].
- **Confidence:** documented

## Fire and burning (Flame Thrower, Cosmic Fire; BBG)
- **Official text:**
  - "Burn your enemies with the power of hot morning coffee without the lawsuit!" (Flame Thrower)
  - "Sometimes "killing it with fire" is the only way to deal with something, amirite?" (Cosmic Fire, v2.3)
  - Both [Game text via wiki].
- **Look:**
  - No burning status appears in the wiki's Status Effects list [Fan-wiki]. Flame weapons do contact damage only [Fan-wiki].
  - Orange-yellow flame sprites (#F47E3E / #FAA751) licked around a victim just before his death [Observed: trailer 12.4–13.0 s]. Their source is [Unverified].
  - Orange flame jets rise from floor vents [Observed: screen_01.jpg]. Whether they are a hazard or jump pads is [Unverified].
- **Firing:**
  - Flame Thrower: "red-colored flames" [Fan-wiki].
  - Cosmic Fire: the fire in Botch's palm "begins to burn much more vigorously" for 5 s [Fan-wiki].
- **Projectile:** see Firing.
- **Impact / end result:** see Look.
- **Images viewed:** `C/sheets/tl_zoom.jpg`; `W/visuals/steam_screens/screen_01.jpg`
- **Depiction for shorts:** flat cartoon flames on contact. A smoking bottom or a sooty face afterwards is [BBG News invention]. No lingering burn icon [Fan-wiki].
- **Confidence:** partial

## Controls reversed, blinded and smoke (Sake Bomb, Daydreamer, Dark Matter, Light Matter, Smoke Screen; BBG)
- **Official text:**
  - "A shot from this will make you wine and stumble." (Sake Bomb)
  - "Turn your opponents' daydream into a nightmare…" (Daydreamer)
  - "B1000 has his own version of hide and seek. It is called: Hide in smoke and then kill everyone!" (Smoke Screen, v2.7)
  - All [Game text via wiki].
- **Look:**
  - Controls reversed: "a green question mark will appear over the player's head"; "background music will be disabled and other sounds will feature an mild echo" [Fan-wiki].
  - The armed Daydreamer is "only noticeable by a small white crystal sticking out from the ground" [Fan-wiki].
  - Smoke Screen: "a huge, harmless white cloud" [Fan-wiki].
  - Dark Matter and Light Matter blind with their blasts [Fan-wiki]; the Light Matter blast is a white sphere [Observed: Photo.png].
- **Firing / Projectile / Impact:** as above.
- **Images viewed:** `C/sheets/misc3.jpg`
- **Depiction for shorts:** a green "?" over a stumbling bear with the soundtrack muffled and echoing [Fan-wiki]. That is a strong comedic beat for a short [Inference].
- **Confidence:** documented

## Speed (Caffeine Injection, Speed Field; BBG)
- **Official text:**
  - "Grants the user brief super speed!" (Caffeine Injection)
  - "Gotta go fast! Any player who enters the field gets their speed doubled!" (Speed Field)
  - Both [Game text via wiki].
- **Look:**
  - Caffeine Injection: "the symbol of a coffee cup will appear above the player and there will be a trail of white dust around their feet" [Fan-wiki]. A white coffee mug floats above Graham [Observed: 0GuhKiAnNyc hq1, hq2].
  - Speed Field: "a hazy, light yellow orb" that becomes a dome with a "translucent light yellow haze" [Fan-wiki].
- **Firing / Projectile:** n/a.
- **Impact / end result:** Caffeine Injection lasts 10 s [Fan-wiki].
- **Images viewed:** `C/sheets/yt_0GuhKiAnNyc.jpg`; `C/crops/gamma_hq2_x2.png`
- **Depiction for shorts:** a steaming coffee mug icon bobbing over the head and dust puffs at the feet [Fan-wiki/Observed]. Speed lines are [BBG News invention].
- **Confidence:** partial

## Cloak (Cloaking special, Cloak Field, Peek A Boo; BBG)
- **Official text:**
  - "Become invisible! Activation will make you transparent to all players! Great for avoiding sniper locks! Note: Moving will affect your transparency!" (Cloaking)
  - "Sanchez is really good at hide and seek. Any player who enters the field gains cloaking!" (Cloak Field)
  - Both [Game text via wiki].
- **Look:**
  - Cloaking: 75% transparent while moving and 95% while still; taking damage reveals the user for 0.5 s [Fan-wiki]. The aura is in team colour (from v1.4.2) [Fan-wiki]. The menu icon is a dark silhouette with a glowing green outline [Observed: Cloaking.png].
  - Cloak Field: a dome with a "translucent light purple haze" [Fan-wiki].
  - Peek A Boo: a rainbow burst, then invisibility with neon red/blue team lines [Fan-wiki].
- **Firing / Projectile:** n/a.
- **Impact / end result:** see Look.
- **Images viewed:** `C/png/Cloaking.png`; `C/sheets/rainbow_zoom.jpg` (possible Peek A Boo burst)
- **Depiction for shorts:** a heat-haze see-through character with a faint red or blue rim. Flicker it fully visible when hit [Fan-wiki].
- **Confidence:** partial

## Damage up and damage down (Bearscream Sandwich, Propbearganda, Pain Field, Invulnerable Field, Energy Barrier; BBG)
- **Official text:**
  - "This field speeds projectiles to cause pain faster. Anyone inside takes 50% more hurting from dangerous things flying around…" (Pain Field)
  - "Increases all nearby teammates damage by 25% for a limited time. Stay close to your friends for maximum effect." (Propbearganda)
  - "With great power comes great invulnerability" (Invulnerable Field)
  - "Make those pesky bullets less pesky with this brand new shield! Upon activation all damage recieved is reduced by 50%!" (Energy Barrier)
  - All [Game text via wiki].
- **Look:**
  - **Bearscream Sandwich buff:** a swirling magenta and pink electric ring around the player's body (#E76FE6 / #FCBEFC) [Observed: A_life_upside_down.png, which the wiki captions as showing this pickup]. The wiki contradicts itself on the bonus: "doubles" (Bearscream Sandwich page) vs "Triples" (Pick-Ups page) [Fan-wiki].
  - **Propbearganda:** "speakers will rise from the player's back playing a tune" (the Bearbershop Quartet) plus "a purple fist symbol" [Fan-wiki].
  - **Pain Field:**
    - "a small compact pink orb… grows massively and transforms into a large barrier of compact hexagons"; no overhead icon [Fan-wiki].
    - A magenta faceted cellular sphere (#D457EB / #A758C9) [Observed: Imagef.png].
    - The trailer shows a matching magenta faceted dome (#CD20ED / #F124FC / #9819B2) over the temple stairs, with a sniper stepping out of it [Observed: trailer 14.0–16.0 s]. That it is the Pain Field is [Inference].
  - **Invulnerable Field:** a dome from "a hazy, light blue orb" [Fan-wiki].
  - **Energy Barrier:** a team-colour glow for 2 s [Fan-wiki].
- **Firing / Projectile:** n/a.
- **Impact / end result:** see Look.
- **Images viewed:** `C/png/A_life_upside_down.png`; `C/sheets/effects1.jpg`; `C/sheets/trailer_sheet_2.jpg`; `C/sheets/seq_tl.jpg`
- **Depiction for shorts:** a crackling pink ring around a sandwich-powered bear; a giant translucent magenta honeycomb bubble for the Pain Field [Observed]. A boombox-backpack rising for Propbearganda [Fan-wiki].
- **Confidence:** partial

## Healing and life drain (Health pickups, Healing Tent, Drain Field; BBG)
- **Official text:** "Toss this sucker at the nearest enemy and watch as his life force is drained from him and transferred to you!" [Game text via wiki] (Drain Field, v2.16)
- **Look:**
  - Health is restored only by the Healing Tent or by pickups [Fan-wiki: Health].
  - Drain Field: "a leech-like creature… a dark field will be formed with bats in it", "a projection of a live creature wearing sunglasses" [Fan-wiki]. Not observed; the Drainfield image I opened shows an Arbiter character, not the field [Observed].
  - The visual of the heal itself is [Unverified].
- **Firing / Projectile / Impact:** see Look.
- **Images viewed:** `C/sheets/effects2.jpg`
- **Depiction for shorts:** a green "+" sparkle on healing is [BBG News invention]. A dark bubble full of cartoon bats in sunglasses for the Drain Field [Fan-wiki].
- **Confidence:** documented

## Pickups: Shield, Health Pack, Imperial Basket Grande, Bearscream Sandwich, Joules (and Gas, which is not a pickup) (map items; BBG 2013+)
- **Official text:**
  - The Imperial Basket Grande comes from a BB-1 gag ad: "Ease your hunger with 3 pounds of deep fried pain, pain, pain!…" [Game text via wiki, BB-1].
  - Steam: "Grab your A Salt Rifle, Bearzooka and those Turkish SW Boots" [Canon].
- **Look:**
  - **Shield:** "four green shields will circle around the player, making them immune to damage for 10 seconds" [Fan-wiki]. Translucent green and pale heater-shield shapes around the player, low resolution [Observed: Maxresdefault(100).png].
  - **Health Pack:** a white-grey box with an orange cross [Observed: HealthPack.png]. It heals up to 35 and respawns in 45 s [Fan-wiki].
  - **Imperial Basket Grande:** a red basket of golden fried chunks on white paper [Observed: Imperial-basket-grande.png]. It gives +50% of max health, can overheal to 200%, and respawns in 60 s [Fan-wiki].
  - **Bearscream Sandwich:** an ice-cream sandwich with an angry brown bear face, red eyes and yellow teeth [Observed: Bearscream_Sandwich.png]. It respawns every 90 s and usually sits at the map centre [Fan-wiki].
  - **Joules:** a blue lightning bolt on a dark hexagon [Observed: Joule.png]. Three drop where a player dies (25 each), vanishing after 10 s (from v2.1) [Fan-wiki].
  - **Gas:** a currency, shown as a red jerry-can icon [Observed: Gas.png], also used for the Gas Meter. It is not an in-match pickup [Fan-wiki: Gas; Gas Meter].
- **Barks:**
  - Wil: "Force field, FORCE FIELD!" (Shield) and "Omnomnomnom..." (Health Pack) [Fan-wiki].
  - Tillman: "Gives me chills!" (Shield) [Fan-wiki].
- **Firing / Projectile:** n/a.
- **Impact / end result:** see Look. Which pickups survive into 2026 is [Unverified].
- **Images viewed:** `C/sheets/icons.jpg`; `C/crops/shield_crop.png`; `C/crops/shield_crop2.png`; `C/png/Maxresdefault(100).png`
- **Depiction for shorts:** four green crest-shields orbiting a bear; a sneering ice-cream sandwich that turns its eater pink-electric [Observed/Fan-wiki]. Exact pickup idle spin and bob is [BBG News invention].
- **Confidence:** partial

## Respawn, suicide and hazards (match flow; BBG)
- **Official text:** none found.
- **Look:**
  - Players respawn by tapping "Tap to Respawn", and may switch loadout between lives [Fan-wiki: Loadouts].
  - "When the player respawns, they have the shields for 4.5 seconds (to discourage spawn killing)" [Fan-wiki: Shield]. The 2014 HUD shows a green-shield "SHIELDS" indicator [Observed: 0GuhKiAnNyc hq1]; that it relates to this is [Inference].
  - Any spawn-in flash or teleport effect is [Unverified].
- **Hazards:**
  - "natural hazards which can instantly kill a player… These hazards will cause a suicide and deduct a kill" [Fan-wiki: Health]. Shortest Parsec's laser instead deals damage over time [Fan-wiki].
  - "Suicides are penalized in team battle" [Fan-wiki: Versions].
  - Lava borders the Aztec maps [Observed: trailer 43.5–46 s; Maxresdefault(100).png].
- **Firing / Projectile:** n/a.
- **Impact / end result:** see Look.
- **Images viewed:** `C/sheets/yt_0GuhKiAnNyc.jpg`; `C/sheets/trailer_sheet_7.jpg`; `C/png/Plant_the_bombbbbbb_b.png`
- **Depiction for shorts:** a respawn shown as the bear popping in under orbiting green shields [Fan-wiki]. Any teleport sparkle is [BBG News invention].
- **Confidence:** partial

## Bearzooka (secondary, Soldier/Oliver default; BBG 2013, named in the 2026 Steam text) — colour conflict resolved
- **Official text:**
  - "The basic weapon of any Soldier. Does a good amount of damage, with a decent area of effect (AOE). Useful for all situations." [Game text via wiki]
  - "Grab your A Salt Rifle, Bearzooka and those Turkish SW Boots" [Canon] (Steam)
  - Wiki: "In BBG and BB0, it is a rocket launcher with red and orange lines. In BBZ and BB-1 it is just a dark green rocket launcher." [Fan-wiki: Bearzooka]
- **Look:**
  - **Shape:** an octagonal tube that pinches in the middle and flares at both ends [Observed: Photo_19-04-13_12_02_26_PM.png (2013 menu capture); trailer 3.9–4.8 s].
  - **Body colour:** coral to brick red. Samples: #DE604D / #E16957 in the 2026 trailer [Observed: bz_full_4.3.png]; #A14243 / #B36161 in the 2013 capture [Observed].
  - **Details:**
    - A row of glowing orange chevron and rectangle window panels (#FF941F / #FFAA31, or #F18922 in 2013)
    - two grey metal collars (#7F7D7C)
    - a grey-on-red checkered rear flare
    - a black bore with a grey rim
    - [Observed]
  - **Concept art:** a red tube, grey bands, orange chevrons and a red/grey checkered flare, plus "THROWN MISSILE" sketches of a round bomb and a dynamite bundle [Observed: Bearzooka_Concept.png]. Whether the thrown missiles were ever used in game is [Unverified].
  - **Size:** about 2–2.5× Oliver's head height long [Inference from foreshortened images].
  - **Carry:** shouldered with the muzzle forward [Observed: 2013 capture; trailer 3.9–4.8 s], or held low at the hip from behind [Observed: AZt_huguhzc thumbnails, 2013].
- **Where "green, hazard-striped" came from:**
  - In the trailer shot, the bear holding the coral Bearzooka has green fur. That is the Green Oliver recolour skin [Observed: GreenSkin.png; Fan-wiki: Soldier (BBG)/Skins], here on the blue team with a blue headband.
  - The yellow-and-black diagonal "hazard stripes" are his brass-bullet bandolier (#D9B05D on dark navy) [Observed: bz_full_4.3.png; OliverSkin.png].
  - BBG's only green "Bearzookas" are Tillman's olive Twin Bearzookas (Demo primary, v2.17) [Observed: Ohmagawdyas.png; Fan-wiki].
- **Firing:** two shots before reloading [Fan-wiki]. Planned "incoming stats" listed a 1 second rate of fire, a 3 s reload and 1000 u/s projectiles [Fan-wiki]. The muzzle effect is [Unverified].
- **Projectile:** rocket look [Unverified]; no frame shows one.
- **Impact / end result:**
  - Explosive area damage (AOE) [Game text via wiki]; "The user is very prone to suicide while using the Bearzooka." [Fan-wiki]
  - The explosion look for this weapon specifically is [Unverified]; use the general explosion grammar above [Inference].
- **Images viewed:** `C/png/Photo_19-04-13_12_02_26_PM.png`; `C/crops/bz_grid.png`; `C/png/Bearzooka_Concept.png`; `C/sheets/bz_sheet.jpg`; `C/tr/bz_full_4.3.png`; `C/crops/bz_trailer_grid.png`; `C/sheets/yt_AZt_huguhzc.jpg` (https://i.ytimg.com/vi/AZt_huguhzc/hqdefault.jpg, hq1, hq2, hq3); `C/sheets/oliver_skins.jpg`; `C/sheets/misc4.jpg`
- **Depiction for shorts:** a coral-red tube with glowing orange window chevrons, grey collars and a checkered back flare on Oliver's shoulder [Observed]. The rocket's look and the comic recoil are [BBG News invention].
- **Confidence:** partial (look observed; projectile and impact not)

---

## Corrections for the character file

1. **`oliver.md` line 51.**
   - *Current:* "The Bearzooka is drawn as a green, hazard-striped tube [Observed; Inference]."
   - *Correction:* "In BBG the Bearzooka is a coral-red octagonal tube (~#DE604D in the 2026 trailer, ~#A14243 in a 2013 capture) with a row of glowing orange window panels (~#FF941F), grey metal collars and a grey-checkered flared rear [Observed]. This matches the wiki's 'rocket launcher with red and orange lines' [Fan-wiki]. Green Bearzookas belong to BB Zombies and BB-1 [Fan-wiki]."
   - *Evidence:* `C/png/Photo_19-04-13_12_02_26_PM.png`; trailer 3.9–4.8 s (`C/tr/bz_full_4.3.png`, `C/sheets/bz_sheet.jpg`); `C/png/Bearzooka_Concept.png`. The "green" was the Green Oliver skin's fur and the "hazard stripes" were his bullet bandolier (`C/png/GreenSkin.png`).
2. **`oliver.md` line 75 (character reference prompt).**
   - *Current:* "He holds a chunky assault rifle and carries a green hazard-striped launcher tube on his back."
   - *Correction:* "He holds a chunky assault rifle and carries a coral-red launcher tube with glowing orange window panels, grey metal collars and a grey-checkered flared end."
   - *Evidence:* same as item 1.
3. **`oliver.md` line 50 (and the unsampled "harness green #4E6B35" in line 49). Check before changing.**
   - *Current:* "A green-and-dark-grey harness with grey clips [Observed] and a small green backpack [Inference]."
   - *Correction:* the BBG 2013 in-game default shows a brass-bullet bandolier across the chest and red (team-colour) headband, wristbands and ankle bands with red gem studs [Observed]. The backpack seen in play is pale grey-lilac (~#A88EA4) with team-colour trim [Observed]. If the green harness comes from a specific 2012 card, cite and keep it only for that era.
   - *Evidence:* `C/png/OliverSkin.png` (wiki default-skin render, 2013); `C/tr/bz_full_4.3.png` (backpack on the Green Oliver skin).
4. **`README.md` line 57.**
   - *Current:* "No blood, gore or organs: bears throw sparks, Huggables burst into rainbow confetti, robots shed bolts."
   - *Correction:* Keep the rule but label it, adding the observed baseline: "In BBG, a normal death is an intact ragdoll collapse, and explosive or radiation deaths break the body into a few clean toy-like chunks [Observed]. BBG News dresses the chunks as sparks (bears), rainbow fluff (Huggables) and bolts (robots) [BBG News invention]. No source shows confetti."
   - *Evidence:* trailer 4.9–5.6 s, 8.9–9.0 s, 12.6–14.9 s, 26.5–27.8 s, 31.7–32.7 s; `W/visuals/steam_screens/screen_03.jpg` and `screen_04.jpg`. The prior notes' fact-check also removed "confetti" as unsourced.
5. **`riggs.md` line 72.**
   - *Current:* "Huggable "gore" stays rainbow confetti."
   - *Correction:* "Huggable "gore" stays rainbow fluff or confetti [BBG News invention]. SkyVu's rainbow Huggable blood is from the earlier PvE games [Fan-wiki]; in BBG footage a killed Huggable breaks into plush pieces with gold sparkles [Observed]."
   - *Evidence:* wiki Huggable and Headlights pages; trailer 8.9 s; `C/png/HuggyBiteMeCR.png`.
6. **`README.md` line 53 (addition, low priority).**
   - *Current:* "**Team colour:** red team by default."
   - *Correction:* append "Team colour shows on accents (Soldier headband and cuffs, the Huggable's flag, Tillman's armour panels), on the HUD and kill feed, and on cloak, Peek A Boo and Energy Barrier glows. Weapon projectiles keep their own colours [Observed/Fan-wiki; Inference]."
   - *Evidence:* `C/sheets/oliver_skins.jpg`; trailer 3.9–4.8 s, 18–22 s; `C/png/A_life_upside_down.png`; the wiki's Cloaking, Peek A Boo and Energy Barrier pages.

## Open questions
- Does the 2026 build keep ragdolls and gibbing? Both appear in the official 2026 trailer, but the capture build is unverified. The Oct 19–26 Steam Next Fest demo, or the JustNubz showcase if it can be viewed, could confirm.
- Is the black ink outline in the 2026 Steam screenshots and trailer an in-game rendering change or a marketing filter?
- Does a Huggable spray rainbow when it dies in BBG? The 3.3–3.8 s trailer rainbow fan is most likely Peek A Boo, but this is unconfirmed.
- What do the Bearzooka's rocket, muzzle flash and explosion look like? No frame found; the wiki's demonstration video AZt_huguhzc was only seen as thumbnails.
- Do gibbed bears show the "pink and red flesh" the wiki describes for Tillman?
- How do the Frozen state (S'no Matter, Let It Cold), poison skulls and Drain Field look? No images were found.
- Is there a respawn or spawn-in effect, a death cam, and how long do corpses stay?
- What does the green "OH BABY" HUD text mean? Possibly a killstreak call.
- Which weapon made each trailer effect: the pink beam that irradiated the orange Huggable at 7–9 s, B-1000's kill of the green Soldier at 4.9 s, and the orange cone with ring shockwaves at 52.6 s?
- Does the Bearscream Sandwich double or triple damage? The wiki pages conflict.
- Can archived SkyVu blog and patch notes add [Canon] wording on deaths, gibs or team colours? Wayback was unreachable from this sandbox (connection resets).