# Unassigned, shared and special weapons

This dossier covers the BBG weapons that fall outside the per-class files:

- the five Category:BBG Weapons pages that no class page links to;
- four real BBG weapon pages that are missing from that category;
- weapons supposedly shared between classes, and what classes really share (Specials);
- retextures (Sci-Fi ASR, Sci-Fi HASR);
- the Bearzooka colour conflict;
- BBR-era carryovers;
- removed and reworked weapons;
- seasonal and promotional drops.

**Sources I could reach on 2026-10-16:**
- **Wiki:** the fan wiki through its MediaWiki API (wikitext, categories, revision histories, images).
- **Official sites:** battlebears.com (live), the Steam appdetails API and the Steam news API.
- **Videos:** i.ytimg.com thumbnails only. I extracted frames from the official Steam trailer (t_N is at (N-1)×0.5 s).

**Sources I could not reach:**
- **web.archive.org.** About ten curl attempts were reset by the proxy, and WebFetch refuses the domain. So I did **not** re-check any archived SkyVu blog post or patch note (BBR 1.3.1, BBG 2.6, 2.20, 2.27). Version dates below come from the wiki's Updates table [Fan-wiki].
- **The JustNubz 2026 showcase.** I did not watch it, only its thumbnails.

All local paths start with `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/`. Every path below is written out in full.

**Scale reference:** BBG News chart, Oliver = 1.0×, Riggs ~1.2×, Sanchez, Saberi, Botch, Graham and Astoria 1.0×, Wil and Tillman ~0.9× [BBG News invention, from /home/user/thallo-site/bbg-news-repo/characters/README.md]. Weapon sizes below are my measurements on the images I viewed [Observed], converted with that chart [Inference].

## Key findings

1. **Why the five pages were "unassigned."** It is a link and categorisation problem, not a sign of special weapons [Fan-wiki, checked against the class-page wikitext]:
   - **Adrenaline Gun:** the Arbiter (BBG) page still links the old name "Bind Gun", which redirects.
   - **Catastrophe:** the Heavy (BBG) page links the in-game misspelling "Catastophe", which redirects.
   - **ClubCobra:** the Combat Tech (BBG) page links "Clubcobra", which redirects.
   - **Hazard Toy:** it is missing from the Assassin (BBG) page entirely.
   - **The Incredible Riggs:** it is a Heavy **skin** that was miscategorised as a weapon.
2. **The 185-page list undercounts BBG weapons.** Four real BBG weapon pages are linked from class pages but are not in Category:BBG Weapons:
   - MuskIt (Engineer)
   - Bind Field, formerly Slow Field (Engineer)
   - Traffic Light (Chub Scout)
   - Social Butterfly (BBG) (Combat Tech)

   [Fan-wiki]. Steam's 2026 copy promises "80+ PRIMARY WEAPONS 60+ SECONDARY WEAPONS 50+ MELEES 10 SPECIAL EQUIPMENT" [Canon] ([Steam appdetails](https://store.steampowered.com/api/appdetails?appids=4408320)). The wiki, including these orphans, has about 77 primaries, 64 secondaries and 46 melees, removed weapons included. The 2026 build may contain weapons the wiki never documented [Inference].
3. **No BBG weapon is shared between classes.**
   - Every weapon page carries exactly one class category [Fan-wiki].
   - In `weapons_by_class.json`, A Salt Rifle, Heavy A Salt Rifle, Soaker, Spreadshot, Steamshot, B.E.A.R. Club and Krikkit Bat also appear under Riggs and Huggable. That overlap comes from a copy-pasted Soldier changelog: the "Version 1.0 … Weapons (WIP)" block on the Heavy (BBG) and Huggable (BBG) pages even links Soldier skins such as "Grey Oliver" [Fan-wiki; Inference].
   - What every class really shares is the **10 Specials** (Turkish SW Boots and so on) and the map pick-ups.
4. **Bearzooka colour conflict resolved.**
   - The BBG Bearzooka is **coral-red with orange windows**, in a 2013 in-game screenshot, the SkyVu concept sheet and the 2026 Steam trailer [Observed].
   - The green launchers are Tillman's **Twin Bearzookas** (olive) and the old BB Zombies / BB-1 Bearzooka [Observed; Fan-wiki].
   - The "hazard stripes" in the trailer frame are the bear's gold-and-black bullet bandolier, not the weapon [Observed].
5. **2026 status of almost everything here is unconfirmed.** The only item in this dossier I could see in a 2026 source is **The Incredible Riggs** skin. It appears in the loadout menu of the September 2026 playtest showcase thumbnail [Observed].

---

## PART A: The five unassigned pages

## Adrenaline Gun, formerly the Bind Gun (Primary, Arbiter / Sanchez default; Bind Gun BBG 2.6, Dec 20 2013; reworked June 2021; 2026 version unconfirmed)
- **Official text:**
  - Current: "The only bad thing about being faster than light is that you always live in darkness" [Game text via wiki], tagged "~Official Battle Bears Gold description, submitted by community member Wilpower784" ([Adrenaline Gun](https://battlebears.fandom.com/wiki/Adrenaline_Gun)).
  - Old Bind Gun text: "One weapon to slow them all!" [Game text via wiki].
  - 2.6 class blurb as the wiki transcribes it: "Back from the brink of death, Sanchez has been rebuilt from the arm up! Use his unique weaponry to slow down opponents and finish them off with his devastating melee attacks." [Game text via wiki] ([BBG/Versions/2.6](https://battlebears.fandom.com/wiki/Battle_Bears_Gold/Versions/2.6)).
  - BBH only, not BBG: "Sanchez's "Adrenaline Gun" rapidly fires four staggered projectiles with a fast reload time." [Canon, BBH] ([characters](https://battlebears.com/pages/characters)).
- **Rework history:**
  - The wiki says the Bind Gun "was changed into the adrenaline gun on the 19th of June 2021" [Fan-wiki].
  - The page history shows the stats edited at 2021-06-18 23:32 UTC and the page moved "Bind Gun → Adrenaline Gun: New name for the weapon" on 2021-07-17 [Fan-wiki, revision log].
  - Slow and damage values: in the 2020 version the effect was "Slow Effect 20% per hit" for 1.25 s with damage 5 (earlier 10% and damage 6). The 2021 version is "Speed Effect 50% per hit" for 0.5 s with damage 7, rate of fire 0.15 s, ammo 55, reload 4 s, "+2% Speed" [Fan-wiki].
  - The wiki still illustrates the page with the 2013 Bind Gun image. So whether the model changed is [Unverified].
- **Look:**
  - The SkyVu-style "New Character: Sanchez" weapon card labels the weapon "BIND GUN" with an arrow [Observed, Sanchez_weapons.png]. The card is 900×691 and was uploaded to the wiki on the 2.6 release day. That matches the archived battlebears.com file `sanchez_weapon_ad2-900x691.jpg` cited in our lore notes, so it is probably the official card [Inference].
  - Shape: a long, chunky, angular sci-fi rifle with stepped armour panels and an open slot along the top, held two-handed across the chest. It is about **0.7× Sanchez's height**, so ≈0.7× Oliver.
  - Colours: glossy azure **#0991D4**, lit faces **#1CB5F3**, highlights **#6CCFF4** on the card. In the dim shop screenshot it reads darker steel-cyan, **#367494** (bright edges #69B3C6, shadow #15364D).
  - The muzzle is a round **glowing white-cyan disc, #EBF0F5**, ringed in near-black (#0F2D3D) [Observed].
- **Firing:**
  - "an automatic weapon that shoots a purple beam. It is not completely accurate as the beam tends to move in an oval-like wave" [Fan-wiki].
  - I found no image or frame of the beam [Unverified].
- **Projectile:**
  - A continuous purple beam that wobbles in an oval wave [Fan-wiki].
  - BBH's version fires "four staggered projectiles" [Canon, BBH], but do not port that to BBG [Inference].
- **Impact / end result:**
  - **Bind Gun era (2013–2021):** hits slowed the target. The Status Effects page lists the Bind Gun under **Slowed**: "a yellow Z will appear over the player's head" [Fan-wiki].
  - **Adrenaline era (2021+):** targets "will be drastically sped up for a brief amount of time." The wiki suggests using it to make enemies "fall off the map, run into a Sanchez melee or barely miss their intended destination such as a powerup or safe area" [Fan-wiki].
  - Shields: "If the target has a Shield, the speed up effect will be applied, but damage is not inflicted." A known glitch lets the wobbling beam hit the shooter when backing up [Fan-wiki].
  - No overhead icon is documented for "sped up". The only speed-up icon on the wiki, a coffee mug, belongs to the Caffeine Injection Special [Fan-wiki; Unverified for the gun].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Sanchez_weapons.png ([File:Sanchez_weapons.jpg](https://battlebears.fandom.com/wiki/File:Sanchez_weapons.jpg))
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Bind_Gun.png ([File:Bind_Gun.png](https://battlebears.fandom.com/wiki/File:Bind_Gun.png))
- **Depiction for shorts:**
  - Sanchez braces the big azure gun and sprays a wobbling purple ribbon beam.
  - In the 2013 setting, the target slows and a cartoon yellow "Z" pops over its head.
  - In the 2021+ setting, the target's legs blur [BBG News invention: speed lines] and it overshoots a ledge or misses a pick-up (the wiki's own usage note).
  - Pick one era per short and say which.
- **Confidence:** partial. The look is observed. The beam and the speed visuals come from the fan wiki only, and the 2026 version is unknown.

## Catastrophe (Melee, Heavy / Riggs; BBR v1.3.1, released over four weeks from June 28 2012; carried into BBG; 2026 unconfirmed)
- **Official text:** "Let Riggs bring the kitten cuddlin' to you! You may not like how he does it, though, and living through it isn't likely... but hey, kittens!" [Game text via wiki] ([Catastrophe](https://battlebears.fandom.com/wiki/Catastrophe)).
  - The in-game name is misspelled "CATASTOPHE". I read it on the Oct 2012 shop screenshot [Observed], and the wiki notes the same [Fan-wiki].
- **Look:**
  - A **pair of calico cat-head gloves**, one over each fist [Observed, Catastrophe.png].
  - Each head is low-poly: brown back (#441D17–#5B3D23), rust-orange patches (#924920–#A35525) and white muzzle and cheeks (#D1C6C1–#F3F2F0).
  - One huge glossy **blue cartoon eye** (#0072CF, white highlight) on each side, small pointed ears and a red open mouth (#7F0A0D) at the front.
  - Each glove is about head-sized for Riggs, about 0.35× Riggs's height ≈ 0.4× Oliver [Observed; Inference].
  - The SkyVu-style promo graphic "BBR 1.3.1 and BEYOND!" shows the same cat head among the 1.3.1 weapons [Observed, BBRWEAPONS.png; official provenance Inference].
- **Firing:**
  - A melee punch. "It deals 40 damage which can be doubled due to the second glove used in the attack" [Fan-wiki].
  - Current BBG modifiers are a 20% speed reduction and a 10% health boost. The 2012 shop screenshot shows "HEALTH -5%" and "SPEED +15%", which matches the wiki's "Previous Stats" [Observed; Fan-wiki].
  - No swing animation or sound is documented.
- **Projectile:** none (melee).
- **Impact / end result:** undocumented beyond damage [Unverified].
- **Era notes:**
  - "Like all v1.3.1 weapons and skins, the Catastrophe was offered to those who took part in the Forum Appreciation promotion, free of charge and before the official release date/week" [Fan-wiki].
  - The original price was 20 Gas [Fan-wiki].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Catastrophe.png ([File:Catastrophe.png](https://battlebears.fandom.com/wiki/File:Catastrophe.png), Oct 2012 shop screenshot with Riggs in the Teen Wolf skin)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Catastrophe_1.png ([File:Catastrophe_1.png](https://battlebears.fandom.com/wiki/File:Catastrophe_1.png))
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/BBRWEAPONS.png ([File:BBRWEAPONS.png](https://battlebears.fandom.com/wiki/File:BBRWEAPONS.png))
- **Depiction for shorts:** Riggs throws a one-two of cat-head punches. Each glove's big blue eye blinks on contact with a "mrrp!" and a burst of yellow sparks and floating hearts [BBG News invention: sound and hit FX]. Keep the calico colours and the single big eye per side.
- **Confidence:** partial. The look is observed. The hit effects are unknown.

## ClubCobra (Melee, Combat Tech / Saberi; BBG 2.20, May 29 2015; 2026 unconfirmed)
- **Official text:** "A powerful melee made of jade and gold." [Game text via wiki] ([ClubCobra](https://battlebears.fandom.com/wiki/ClubCobra)).
- **Stats and sale:**
  - 50 damage, 150,000 Joules, level 10 lock [Fan-wiki].
  - The health modifier conflicts: the ClubCobra page says "+15% Health", but the wiki's Health page says "+10% health". The shop screenshot I viewed shows "HEALTH +10%" [Observed], so +10% is better supported.
  - It was sold in the 2.20 "Sandkind" bundle with the Sandchez skin, Toxic Plague and Toxic Rifle [Fan-wiki, Bundle Deals].
- **Look:**
  - A **golden cobra-head club** [Observed, Clubcobra.png]. A straight gold shaft carved with zig-zag and glyph patterns ends in a hooded cobra head curling forward, with an open mouth.
  - A green jade eye (#29C74E) is set in a dark-violet socket.
  - The grip is wrapped in dark brown leather (#2D1912) and ends in a gold pommel hook.
  - Gold tones: #F9C10A lit, #DF9B0C mid, #A37B02 shadow, #FFD823 highlights. Most of the "jade" is the eye; the club reads almost entirely gold [Observed; Inference].
  - Saberi holds it one-handed, raised; the club is about 0.6× her height ≈ 0.6× Oliver.
- **Firing:** melee swing, undocumented [Unverified].
- **Projectile:** none.
- **Impact / end result:** undocumented [Unverified].
- **Images viewed:** /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Clubcobra.png ([File:Clubcobra.jpg](https://battlebears.fandom.com/wiki/File:Clubcobra.jpg))
- **Depiction for shorts:** Saberi swings the gold cobra overhead. On impact the cobra's mouth snaps shut with a gold flash and green sparkle chips [BBG News invention: hit FX]. Keep it gold with a single jade-green eye.
- **Confidence:** partial. The look is observed and the swing is unknown.

## Hazard Toy (Primary, explosive and poison; Assassin / Botch; BBG 2.27, May 29 2017; not listed on the wiki's Assassin page; 2026 unconfirmed)
- **Official text:** "Banned from elementary schools world wide, this weapon is as dangerous as it looks!" [Game text via wiki] ([Hazard Toy](https://battlebears.fandom.com/wiki/Hazard_Toy)).
- **Era:**
  - Released in 2.27 alongside Fidget Boomer (Sniper) and Spin Baby Spin (Arbiter), with a summer-themed No Bear's Land [Fan-wiki, Updates].
  - "It is based off of the Fidget Spinner" [Fan-wiki].
  - Price 60 Gas, level 1 [Fan-wiki].
- **Look:**
  - A **translucent green three-bladed fidget spinner** [Observed, HazardToy.png]. The blades are wedge-shaped like the three arms of a radiation trefoil, which is probably the "hazard" pun [Inference].
  - Blades are glassy green (#206321–#207C1E, edges #43883A), with a round hub of concentric dark and light green rings.
  - It floats beside Botch's raised paw, edge-on to camera. Its diameter is about 0.5× Botch's height, roughly his head width.
  - Botch's eyes glow lime #B7FA20 in the same shot [Observed].
- **Firing:**
  - "a projectile weapon which explodes upon contact" with "a straight trajectory compared to the curve of Chaos Toss, and a faster projectile speed than Toxic Plague" [Fan-wiki].
  - Stats: rate of fire 1.5 s, ammo 3, reload 3.5 s, projectile 1,100 u/s, explosive 25–50 [Fan-wiki].
- **Projectile:** what visibly flies (the spinner itself, or a pellet) is not documented [Unverified].
- **Impact / end result:**
  - It explodes and "poisons enemies caught in the radius". The poison stacks across multiple clouds and does about 4 damage per tick over 5 s [Fan-wiki].
  - Poisoned status: "a purple/green skull will appear over the player's head" [Fan-wiki, Status Effects].
  - The cloud colour is not documented. Botch's Chaos Toss cloud is described as "toxic green" [Fan-wiki], so green is likely [Inference].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/HazardToy.png ([File:HazardToy.jpeg](https://battlebears.fandom.com/wiki/File:HazardToy.jpeg))
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/fidget_group.png (side-by-side of the 2017 trio)
- **Depiction for shorts:** Botch flicks the green trefoil spinner and it whizzes straight out [BBG News invention: the spinner itself flies]. It pops in a puff of green gas, and a little purple-green cartoon skull bobs over each target's head while their health ticks down.
- **Confidence:** partial. The held look is observed. The flying object and the cloud colour are unknown.

## The Incredible Riggs (Skin, not a weapon; Heavy / Riggs; BBG 2.15, Dec 20 2014; present in the 2026 playtest)
- **Official text:** "You won't like me when I'm green! " [Game text via wiki] ([The Incredible Riggs](https://battlebears.fandom.com/wiki/The_Incredible_Riggs)). Price 400,000 Joules [Fan-wiki]. "It is a reference to the Incredible Hulk" [Fan-wiki].
- **Status:** this is a skin. Its page is miscategorised in Category:BBG Weapons [Fan-wiki]. The September 2026 playtest showcase thumbnail shows the loadout menu reading "CHARACTER HEAVY / SKIN THE INCREDIBLE RIGGS" with green Riggs on the pedestal, and a build string read as "3.0.5_2026.11.19_B1 8218727" [Observed].
- **Look:**
  - A green-skinned, hugely muscled Riggs with a bulldog-like snarl and bared teeth [Observed]. Skin green is #448B2F in 2015 and #449C2E in 2026, with highlights #88C773.
  - Torn maroon shorts: #75292E in 2015, #6B2331 in 2026.
  - A segmented grey-beige shell backpack with a blade stuck in it [Observed]. The concept art shows two backpack options: a rock shell and a tech shell with a green spiral [Observed].
- **Weapon in the 2015 shot:** the **Beebeegun**, Riggs's default primary [Inference from shape; Fan-wiki default]. It has a dark gunmetal riveted body with pink and blue striped vents, a glossy pink octagonal "hive" canister (#DB4ACF–#FC83FE) with a cartoon bee peeking out, small yellow-and-black bees around it, a glowing magenta spiral coil around the barrel and a black muzzle [Observed].
- **Firing (for this skin's default gun):**
  - In the 2026 Steam screenshot, a rock-skinned Riggs fires it: the magenta coil flares, thin pink tracer streaks fly out, and pale-yellow stars burst at the target's feet [Observed, screen_00 zoom].
  - The official description says "Artificially accelerated and naturally angry bees. Also the bees are fired backwards." [Game text via wiki].
- **Impact / end result:** see the Beebeegun in the Riggs dossier. The skin changes nothing mechanically [Fan-wiki: skins are cosmetic; Inference].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Theincredibleriggs.png ([File:Theincredibleriggs.jpg](https://battlebears.fandom.com/wiki/File:Theincredibleriggs.jpg))
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/irigg_gun_zoom.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Incredibleriggsconceptart.png ([File:Incredibleriggsconceptart.jpg](https://battlebears.fandom.com/wiki/File:Incredibleriggsconceptart.jpg))
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/web/showcase_maxresdefault.jpg (https://i.ytimg.com/vi/-lAtv-j9Sms/maxresdefault.jpg)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/web/ver_crop.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/s00_beebee_zoom.png (crop of /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/steam_screens/screen_00.jpg)
- **Depiction for shorts:**
  - Use the in-game skin exactly: green skin, torn **maroon** shorts and the shell backpack.
  - Do not add Hulk trademarks such as purple trousers or Marvel lettering [Inference: IP caution].
  - He can fire the Beebeegun with pink tracers and yellow star hits. The angry-bee swarm is a [BBG News invention] built on the official "angry bees" line.
- **Confidence:** observed (skin and gun look); documented (2026 presence).

---

## PART B: BBG weapon pages missing from Category:BBG Weapons

## MuskIt (Primary, radiation shotgun; Engineer / Graham; BBG 2.12, Oct 2 2014)
- **Official text:** "The musk of the Gyrnobal has been known to turn people into mutants, but most blow up." [Game text via wiki] ([MuskIt](https://battlebears.fandom.com/wiki/MuskIt)).
- **Look:**
  - A musket-style long gun [Observed, Musket.png]: dark brown barrel with white bands and a gold ring, a salmon-pink breech block (#AF5649–#C06C5B) with a grey emblem, and a yellow stock (#CEA218).
  - Held at hip level; about 0.8× Graham's height.
- **Firing:**
  - "used like a shotgun, dealing damage and irradiating enemies in a small cone. When fired, it shoots green stuff of what appears to look like bug spray" [Fan-wiki].
  - Stats: damage 30, radiation 35.5–55.5, rate of fire 1.5 s, ammo 3 [Fan-wiki].
- **Projectile:** a short green spray cone [Fan-wiki].
- **Impact / end result:** the Irradiated status [Fan-wiki, Status Effects]:
  - "a yellow circle will appear over the player's head and a noise from a Geiger counter will begin sounding"; the circle dissolves into the radiation symbol as exposure grows.
  - At 100 radiation points the target explodes, with a 150–200 unit blast.
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Musket.png ([File:Musket.jpg](https://battlebears.fandom.com/wiki/File:Musket.jpg))
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/musket_zoom.png
- **Depiction for shorts:** a green bug-spray puff, a ticking yellow radiation badge over the target, then a cartoon "pop" of confetti [BBG News invention: confetti in place of the explosion].
- **Confidence:** partial.

## Bind Field, formerly Slow Field (Secondary, arc-thrown field; Engineer / Graham; BBG 2.6, Dec 20 2013)
- **Official text:** "Make your opponents feel as old as you do. All enemies within the field stop and dream about bingo." [Game text via wiki] ([Bind Field](https://battlebears.fandom.com/wiki/Bind_Field)).
- **Rename:** "originally named the Slow Field, most likely renamed to prevent confusion with the Special ability Slow Motion Field" [Fan-wiki]. The 2.6 list says "Slow Field" [Fan-wiki].
- **Look:**
  - A head-sized **dark-brown sphere with neon-green seams (#2AF944) and purple knob studs (#841783)**, in a buckyball pattern, held in Graham's hand [Observed, Slowfield.png].
  - About 0.35× Graham's height.
- **Firing:** "firing a prickly purple-green ball in an arc" [Fan-wiki].
- **Projectile:** the studded ball, lobbed [Fan-wiki; Observed held look].
- **Impact / end result:**
  - It "detonates and forms a medium-sized force field which slows all opponents caught in its radius by 75% for 3 seconds" and deals no damage [Fan-wiki].
  - Slowed targets show a yellow "Z" [Fan-wiki, Status Effects].
  - The field's colour is undocumented [Unverified].
- **Images viewed:** /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Slowfield.png ([File:Slowfield.png](https://battlebears.fandom.com/wiki/File:Slowfield.png))
- **Depiction for shorts:** the ball lands, a dome pops up [BBG News invention: dome colour], and enemies inside slow to a crawl with dozing "Z"s, matching the "bingo" joke.
- **Confidence:** partial.

## Traffic Light (Melee, Chub Scout / Wil; release version not on the wiki, image uploaded May 2015)
- **Official text:** "Why is there no yellow light you ask? Wil only travels in two modes. He stops and sometimes he has to go." [Game text via wiki] ([Traffic Light](https://battlebears.fandom.com/wiki/Traffic_Light)).
- **Stats:** 45 damage, +10% speed, 150,000 Joules [Fan-wiki].
- **Look:**
  - A **yellow pole (#FED100) with black bands**, topped by a spiky grey traffic-signal head with **only a red and a green lamp** [Observed, Trafficlight.png].
  - Wil swings it like a mace. It is about 0.8× his height. In that shot he wears a red cowl and a grey bear-emblem shirt; the skin name is unknown.
- **Firing / Projectile / Impact:** melee; the hit look is undocumented [Unverified].
- **Images viewed:** /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Trafficlight.png ([File:Trafficlight.png](https://battlebears.fandom.com/wiki/File:Trafficlight.png))
- **Depiction for shorts:** the lamp flips red as he winds up, then green as he swings [BBG News invention]. The "no yellow" joke is canon text.
- **Confidence:** partial.

## Social Butterfly (BBG) (Primary, "Saboteur" type; Combat Tech / Saberi; BBG 2.53, Apr 28 2018)
- **Official text:** none on the wiki stub.
- **Stats:** "Primary - Saboteur", damage 0, rate of fire 2 s, ammo 5, reload 5 s, gravity 1000 units (so it arcs), projectile 1000 u/s, duration 0.5 s, 40 Gas [Fan-wiki] ([Social Butterfly (BBG)](https://battlebears.fandom.com/wiki/Social_Butterfly_(BBG))).
- **Look / Projectile / Impact:** no image and no effect description. Entirely [Unverified].
- **Images viewed:** none exist on the wiki. Searches for "Social" and "Butterfly" found no files.
- **Depiction for shorts:** do not depict until a 2026 frame shows it.
- **Confidence:** unknown.

---

## PART C: "Shared" weapons

## Finding: no BBG weapon is shared between classes (all eras)
- All 185 pages, plus the four orphans, carry exactly one class category [Fan-wiki].
- The "shared" set in `weapons_by_class.json` (A Salt Rifle, Heavy A Salt Rifle, Soaker, Spreadshot, Steamshot, B.E.A.R. Club, Krikkit Bat under Riggs and Huggable) comes only from the "Changelog" scroll box on the Heavy (BBG) and Huggable (BBG) pages. That box is a copy of the Soldier list headed "Weapons (WIP)"; it also lists "Bearzooka" and links Soldier skins such as "Grey Oliver" and "O.C.O." [Fan-wiki; Inference: copy-paste].
- The Heavy page's real weapon lists are Beebeegun, Provolowned, Field Medic, Big Iron, Electric Honey, Zombee Gun, Bounce Lazer and Flame Thrower; Hivey League, Plasma Orb, Mother of Nature, Freeze Blast, Buzz Kill and Sucker Punch; and Barbed Gloves, Catastophe, Blood Spurt, Sword and Stone, Huggable Gloves and Zombee Gloves [Fan-wiki].
- **Name-sharing look-alikes, which are not shared weapons:**
  - **Minigun (Soldier)** is an 80-round automatic primary: "Mini refers to your enemies after its done with them." It is a dark gunmetal four-barrel minigun held at the hip [Observed, Mini.png; Game text via wiki]. **Minigun (Combat Tech)** is Saberi's backpack secondary [Fan-wiki].
  - **Bearzooka** (Soldier secondary) versus **Twin Bearzookas** (Demo primary). See Part E.
  - The **2017 fidget-spinner trio**: Hazard Toy (Assassin), Fidget Boomer (Sniper) and Spin Baby Spin (Arbiter) share a concept but not a weapon. See Part G.
  - **Huggable Gloves** is a Heavy melee themed on the Huggable, not a Huggable-class item [Fan-wiki].
- **Confidence:** documented.

## Specials (all 11 classes; BBR → BBG; "10 SPECIAL EQUIPMENT" in 2026)
- **Official text:**
  - Steam 2026: "Grab your A Salt Rifle, Bearzooka and those Turkish SW Boots" and "10 SPECIAL EQUIPMENT" [Canon] ([Steam](https://store.steampowered.com/app/4408320)).
  - Wiki: "All characters are able to use all Specials. If you purchase a Special for one class, you don't have to buy it for another class." [Fan-wiki] ([Specials](https://battlebears.fandom.com/wiki/Specials)).
- **Per Special.** Visuals are taken from the in-game description diagrams, which are 2D comic illustrations on a dark grid with a green glow outline [Observed]. Quotes are [Game text via wiki], mechanics are [Fan-wiki].

| Special | Official text | Observed diagram | Effect visuals |
|---|---|---|---|
| Turkish SW Boots | "You want to jump? These allow it!" | Oliver mid-leap in red-and-black boots with white jet puffs | Big jump, usable mid-air, 4.5 s cooldown |
| Tesla Shield | "Detonates enemy projectiles on impact." | Orange-red wireframe geodesic cage of glowing nodes; a red rocket bounces off | "gigantic orb of red light"; bullets still pass |
| Slow Motion Field | "Slows down all nearby enemies for a limited time." | Astoria with a snail and yellow zig-zags at her feet | Yellow circle around the user; slowed enemies show a yellow "Z" |
| Iron Curtain | (none on wiki) | Slanted green armoured wall with yellow lights in front of Oliver; a rocket hits it | Blocks frontal bullets; explosives stop but still blast |
| Caffeine Injection | "Grants the user brief super speed!" | Wil sprinting with a coffee cup and red motion blur | Coffee-cup icon overhead and a white dust trail, 10 s |
| Healing Tent | "Activating the healing tent prevents you from moving but gives you health…" | Beige canvas tent with a green cross on grass | Beeping, "Zzzzzzz" signs; 2021 re-upload |
| Propbearganda | "Increases all nearby teammates damage by 25%…" | Oliver with a loudspeaker mast blasting magenta; an ally with a purple fist icon | Speakers rise from the back playing the Bearbershop Quartet tune; purple fist icon |
| Cloaking | "Become invisible!…" | Translucent green outline of a big bear | Transparency; flickers when hit |
| Sixth Sense Goggles | "Discloses all enemy positions - even behind walls!…" | Oliver in purple and yellow goggles; red and blue outlines behind a wall | Team-coloured brackets |
| Flawless Disguise | "Neither team will be able to see who you are, trust no one!" | A cardboard box marked "THE ORANGE" over a crouching bear | Friend/foe hidden; blocks lock-ons |

- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/specials1.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/specials2.png
  - These are built from /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png_sp/*.png, which are the wiki files TurkishSWBoots.jpg, Tesla_sheild.png, SlowMotionField.jpg, IronCurtain.jpg, CaffeineInjection.jpg, NewHealingTent.jpeg, Propbearganda.png, Cloaking.png, Sixth_sense_goggles.png, FlawlessDisguise.jpg and Special.jpg.
- **Depiction for shorts:** any bear can use any Special, so these are ideal cross-cast gags (Riggs in the cardboard box, Wil on caffeine). Keep the icons: coffee cup, yellow Z, purple fist.
- **Confidence:** documented (text), observed (diagram art). The 2026 roster of Specials beyond the count and the SW Boots is unconfirmed.

---

## PART D: Retextures and variants

## Sci-Fi ASR (Primary, automatic; Soldier / Oliver; BBR v1.3.1, second week, summer 2012; in BBG)
- **Official text:** "In the future, lasers will be the seasoning of choice among the elite while the common rabble shall continue to put analog salt-dust into their primitive bodies." [Game text via wiki] ([Sci-Fi ASR](https://battlebears.fandom.com/wiki/Sci-Fi_ASR)).
- **Status:** "a retexture of the standard A Salt Rifle". Stats: 105,000 Joules, level 10, damage 5, rate of fire 0.15 s, ammo 25 ("the lowest ammo of all automatics"), +5% speed. It was a Forum Appreciation freebie in 2012 [Fan-wiki]. The 2.6 rebalance changed its damage from 5 to 5.5 and its clip from 30 to 20 [Fan-wiki].
- **Look:**
  - Compare the base A Salt Rifle: pale sage green (#93BBA8–#B4DEC2) with dusty salmon-rose panels (#7C5B5C shadow, about #CB9A90 lit), a **clear salt-shaker canister** (#FDFFFF) on a ribbed hose on top, and a slate grip (#536270). It is about 0.65× Oliver's height [Observed, Oliver3d.png; concept "AR3" in ASRconcept.png].
  - The Sci-Fi ASR swaps this for **chrome and gunmetal** (#4D4A54 to #E0E0E0). The salt shaker becomes a hexagonal energy cell with **red-orange diagonal stripes (#F94C14)** and a **glowing orange hex cap (#FEA11F)**. It has four dark dots on the side and a dark-teal blade tip (#195457) [Observed, Oliver_SciFi_Asalt.png and the shop icon in Sci-Fi_HASR.png].
- **Firing / Projectile:** automatic [Fan-wiki]. The 2013 fan demo thumbnail is too low-resolution to show the tracers; it shows a yellow-white flash at the target [Observed, P5EsIBxZS-k hq2; weak]. The "lasers" are only in the joke text [Game text via wiki]; the actual tracer look is [Unverified].
- **Impact / end result:** bullet damage, no status effect [Fan-wiki].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/asr_group.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/asr_zoom.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/asr_concepts.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Sci-Fi_HASR.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/web/P5EsIBxZS-k_strip.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/sfasr_hq2_zoom.png
- **Depiction for shorts:** Oliver's rifle with the salt shaker replaced by a glowing orange hex cell. If he fires it, use orange-yellow energy tracers [BBG News invention].
- **Confidence:** partial.

## Sci-Fi HASR (Primary, automatic; Soldier / Oliver; BBR v1.3.1, second week; in BBG)
- **Official text:** "Look no further for reasons for people to get out of your way, you're holding the only one you need. Should a chump still refuse to step aside, this puppy has a convenient little button to change their mind." [Game text via wiki].
- **Status:** "a retexture of the standard Heavy A Salt Rifle". Stats: 60 Gas, level 15, damage 7, rate of fire 0.125 s, ammo 50, reload 5 s, −10% speed; the 2.6 notes show −15% [Fan-wiki].
- **Look:**
  - Base HASR: an AK-style rifle in the same sage-and-salmon scheme with a **large ring-shaped drum** wrapped around the grip [Observed; concept "AR5"].
  - The Sci-Fi version is silver-grey with a dark gunmetal ring [Observed, Photo_19-04-13_12_01_58_PM.png, Sci-Fi_HASR.png].
  - The Oct 2012 shop shot shows Oliver in the gore-styled "Skinless" skin; **do not use that skin in shorts**.
- **Firing / Projectile / Impact:** automatic bullets, no status effect [Fan-wiki]. The tracer look is [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Photo_19-04-13_12_01_58_PM.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Photo_19-04-13_12_02_04_PM.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Sci-Fi_HASR.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/web/ICIsRtcYckY_strip.jpg
- **Depiction for shorts:** a chrome HASR with a black drum ring, and fast muzzle flashes [BBG News invention].
- **Confidence:** partial.

---

## PART E: Cross-game carryovers

## Bearzooka (Secondary, explosive; Soldier / Oliver default; a franchise weapon since BB Zombies, in BBG from BBR 1.0 in 2011; named on Steam in 2026)
- **Official text:**
  - "The basic weapon of any Soldier. Does a good amount of damage, with a decent area of effect (AOE). Useful for all situations." [Game text via wiki] ([Bearzooka (BBG)](https://battlebears.fandom.com/wiki/Bearzooka_(BBG))).
  - "Grab your A Salt Rifle, Bearzooka…" [Canon, Steam 2026].
  - BBH: "his powerful 'Bearzooka' Ultimate which deals massive damage and destroys obstacles" [Canon, BBH].
- **The wiki on colour:** "In BBG and BB0, it is a rocket launcher with red and orange lines. In BBZ and BB-1 it is just a dark green rocket launcher." [Fan-wiki] ([Bearzooka](https://battlebears.fandom.com/wiki/Bearzooka)).
- **Look (resolved):**
  - A shoulder-carried **coral-red tube**: #A54447 in the 2013 screenshot, #D05655 under 2026 trailer lighting.
  - **Glowing orange chevron and hex windows** (#EB7921–#FF8F25), grey metal bands and a black bore.
  - One end flares into a **grey-and-red checkered cone**, matching the SkyVu concept sheet labelled "ROCKET" with yellow-orange chevrons and a checkered flare [Observed].
  - Length about 0.8× Oliver.
  - In 2026 trailer frame t_0009 (4.0 s), a **green-skinned** Soldier carries it. Only the Soldier can carry a Bearzooka, so this is an Oliver skin [Inference]. The bear wears a **gold-and-black bullet bandolier**; that is the green and the "hazard stripes", not the launcher [Observed].
  - **Green launchers** are Tillman's Twin Bearzookas: two olive tubes (#868F43) with black hexagonal muzzles, one on each shoulder [Observed, Ohmagawdyas.png].
- **Firing:** one rocket per shot (2 per clip in the stats), projectile 1,000 u/s, explosive 40–60 within 125/250 units [Fan-wiki]. In t_0010 (4.5 s) a broad yellow-orange blast fills the frame at the muzzle [Observed].
- **Impact / end result:** explosion with splash; "The user is very prone to suicide while using the Bearzooka" [Fan-wiki].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Photo_19-04-13_12_02_26_PM.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Bearzooka_Concept.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Ohmagawdyas.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/trailer/t_0009.jpg (4.0 s)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/bz_t9_t10.jpg (t_0009 at 4.0 s and t_0010 at 4.5 s)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/web/AZt_huguhzc_strip.jpg (2013 fan demo thumbnail: coral launcher on Oliver's right shoulder and a coral HUD icon)
- **Depiction for shorts:** a coral-red tube with glowing orange windows on Oliver's right shoulder, a fat yellow-orange blast, and comic soot when it backfires. Never draw it green unless the gag is about Tillman's twins or a BB-1 flashback.
- **Confidence:** observed.

## BBR-era weapons still in BBG (BBR 2011–Apr 2013 → BBG relaunch May 24 2013)
Release versions below are as the wiki pages state them [Fan-wiki]. Looks belong in the class dossiers.
- **BBR 1.0, Oct 8 2011.** The "original three" sets:
  - Soldier primaries: A Salt Rifle, Heavy A Salt Rifle, Soaker.
  - Soldier secondaries: Bearzooka, Spreadshot, TNT Launcher.
  - Soldier melees: B.E.A.R. Club, Krikkit Bat, Queensbury Rules.
  - Heavy primaries: Electric Honey, Zombee Gun, plus Beebeegun as default.
  - Heavy secondaries: Buzz Kill, Hivey League.
  - Heavy melees: Huggable Gloves, Zombee Gloves, Barbed Gloves.
  - Demo melees: Double Hug, Good Morning.
- **BBR 1.1 (Nov 23 2011):** Sniper with the Viperifle.
- **BBR 1.3 (May 3 2012):** Chub Scout; Doomstick, Tomahawk.
- **BBR 1.3.1** (from June 28 2012, released over four weeks): Doomstick, Killdoba, Steamshot, Plasma Orb, Provolowned, **Catastrophe**, Disciplinarian, Mamba's Boy, Eagle Standard, Golden Dragon, **Sci-Fi ASR**, Punk Bands, **Sci-Fi HASR**, Light Matter, Phat Man, Urine Trouble, Whipped Pain, Field Medic, Rockette Launcher, Presidentures, Beaver Fever.
- **BBR 1.3.2 (Aug 24 2012):** Mother of Nature, Big Iron, Blood Spurt, Sake Bomb, O.C.O. Gauntlet, Kumakiri.
- **BBR 1.4 (Nov 28 2012):** Engineer with Power Glove, Turret, Wrench, Gamma Ray and others.
- **BBR 1.4.3 (Apr 15 2013):** Dead Eye, Fairy's Dust (the 1.4.3.1 text says "Fairy's Sparkle"), Static Shuffle, Señor Potato Cannon (now "Senor Potato"), Sole's Bane, Gernobyl.

Story-game names reused in BBG are noted on the wiki [Fan-wiki]: Bearzooka (BBZ, BB-1, BB0), Spreadshot (BB-1), Crossbow 2.0 (named after BBZ's Unicorn Crossbow), Arrow (the BB-1 arrow in Wil's leg), Batterito (BLAST food), Dragon Slayzer (BB Overclock, added to BBG in 2.51) and Twin Bearzookas (Tillman in BB Zero).

## BBG → BBH (2024) name carryovers
These are not BBG behaviour [Canon, battlebears.com/pages/characters]:
- Acreambo Pistols and the Bearzooka Ultimate (Oliver)
- So Fly (Huggy)
- "Beebee gun" (Riggs)
- Boomstick (Wil)
- Blast-o-Mole and "Firework Flurry" (Tillman)
- "Turret Summon" (Graham)
- Doom Cloud (Botch)
- Adrenaline Gun and Speed Field (Sanchez)

**Do not port BBH mechanics, such as the four staggered Adrenaline Gun shots, into BBG shorts** [Inference].

---

## PART F: Removed and reworked weapons

| Item | Owner | Era in | Change | When | Source |
|---|---|---|---|---|---|
| Bind Gun → Adrenaline Gun | Arbiter | BBG 2.6 (Dec 20 2013) | Slowing beam became a speeding beam; renamed | Wiki edit 2021-06-18 UTC ("19th of June 2021"); page moved 2021-07-17 | [Fan-wiki] |
| Slow Field → Bind Field | Engineer | 2.6 | Renamed | Unknown | [Fan-wiki] |
| Bouncing Betty | Demo | 2.2 (Aug 21 2013) | "removed later" | Unknown; page put in the past tense 2020-05-22 | [Fan-wiki] |
| Greased Lightning | Arbiter | Page created Jun 2014 | "THIS WEAPON IS REMOVED!" | Note added 2020-11-10; removal date unknown | [Fan-wiki] |
| Last Resort | Assault (default secondary) | BBG 1.0 (2013) | "THIS WEAPON IS REMOVED" | Note on page by 2020-11-09 | [Fan-wiki] |
| Capital Pains (red mode) | Sniper | — | "Red Capital Pains is currently removed" | Unknown | [Fan-wiki] |
| Hivey League stat modifier | Heavy | — | Removed | v2.6 | [Fan-wiki] |
| Equipment | All | — | "All +1 Equipment has been removed except Speed +1"; "Equipment Slot 2 has been removed" | 3.0, Nov 15 2021 | [Fan-wiki, Updates] |

Notes:
- Sanchez, Tillman and B-1000 are 1.0× on the BBG News chart, Tillman ~0.9×.
- None of the removals appears in any official 2026 text I could read. Whether these weapons return in 2026 is [Unverified].

## Bouncing Betty (Primary, explosive; Demo / Tillman; BBG 2.2, Aug 21 2013; removed, date unknown)
- **Official text:** "The master of explosions has a lovely friend named Betty. Tillman and her go way back, bouncing around exploding everywhere. Oh, to be young and explosively in love!" [Game text via wiki].
- **Look:** a big shoulder-held **white and silver launcher with a wide black bore**, red and black fittings and a round hazard-target decal on the side, braced on Tillman's shoulder. Its bore is about head-sized [Observed, Bouncing_Betty.png].
- **Firing / Projectile:** it "lobbed a large, black bomb with a lit fuse" [Fan-wiki].
- **Impact:** the bomb explodes on each surface contact and bounces three times, with 30–50 damage and a large area of effect; it cannot hit players directly [Fan-wiki].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Bouncing_Betty.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/removed_group.png
- **Depiction for shorts:** a black cartoon bomb with a fizzing fuse boing-boing-booms down a corridor in three puffs of smoke and confetti [BBG News invention: confetti]. Mark it "classic 2013".
- **Confidence:** partial.

## Greased Lightning (Primary, automatic; Arbiter / Sanchez; about mid-2014; removed)
- **Official text:** "It's automatic! It's systematic! Hydromatic!? Why it's Greased Lightning!!??" [Game text via wiki].
- **Look:** a **glossy red rifle (#990608) with white lightning-crack decals**, a grey toothed top rail and a tan cylinder at the rear [Observed, Greased_Lightning.png].
- **Firing / Projectile:** "fires red-violetish lasers at a rapid rate"; rate of fire 0.13 s, ammo 30 [Fan-wiki].
- **Impact:** damage only. A "slight AOE … deals no damage" [Fan-wiki].
- **Images viewed:** /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Greased_Lightning.png
- **Depiction for shorts:** red-violet laser darts; leave out the song lyrics and music [Inference: rights].
- **Confidence:** partial.

## Last Resort (Secondary, self-destruct; Assault / B-1000 default; BBG 1.0, 2013; removed)
- **Official text:** "Winning takes sacrifice, and in this case that means blowing yourself up. Press and hold the fire button initiate a self-destruct sequence, wait 3 seconds and then boom!" [Game text via wiki].
- **Look:**
  - The wiki image shows B-1000 from behind, wearing an **orange-gold (#BE5904–#E89901) and black backpack of two hexagonal modules with circular vents** [Observed, Last_Resort.png]. That this pack is the Last Resort device is [Inference].
  - The same shot shows the orange and white gun-arm and a grey axe blade with orange teeth.
- **Firing / Impact:** hold for about 3–4 s, then self-explode for 200–400 damage, "the highest damage of any explosive weapon" [Fan-wiki].
- **Images viewed:** /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Last_Resort.png
- **Depiction for shorts:** a beeping countdown on the backpack, then a giant cartoon "BOOM" cloud with B-1000's head bouncing out intact [BBG News invention]. No gore.
- **Confidence:** partial.

---

## PART G: Seasonal, promotional and limited drops
The wiki marks **no BBG weapon as limited-time**. The items below were themed drops or promotions [Fan-wiki]. For 2026, the only limited item in official text is a skin: "Sign Up & Wishlist for an Iconic Zombie Skin!" [Canon] ([play.battlebears.com](https://play.battlebears.com/)). The Steam playtest posts list no weapon changes. The first post says "There won't be any new features in this build" [Canon] ([Steam news](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=4408320)).

**Promotions:**
- **BBR 1.3.1 Forum Appreciation (2012):** "Players who joined the forums could get the weapons and skins of v1.3.1 free and earlier than other people" [Fan-wiki].
- **The "BBR 1.3.1 and BEYOND!" graphic** has a red, white and blue starburst with a bald eagle above a pile of the 1.3.1 weapons: Eagle Standard, Presidentures dentures, Golden Dragon, Mamba's Boy snake, the Catastrophe cat head and a Phat Man radiation bomb [Observed, BBRWEAPONS.png]. A Fourth-of-July theme is [Inference].
- **Bundle Deals** ran "in selected periods", for example Oct 20–22 2012. The 2015 "Sandkind" bundle included ClubCobra [Fan-wiki].

## Winter drops: S'no Matter (Demo primary, 2.15, Dec 20 2014); Let It Cold (Demo secondary) and Snowtato Launcher (Chub Scout primary), both 2.26, Jan 17 2017, with a winter No Bear's Land
- **Official text:**
  - S'no Matter: "It S'no Matter how fast you can move, I can just freeze you! "
  - Let It Cold: "Your enemies won't have a skull or bones after being hit with ice cold rockets! These rockets explode on impact and freezes the opponent for a small duration"
  - Snowtato: "A makeshift potato launcher convertor to weapon of frosty devastation. Shoot snowballs that explode and turn them into flakes!"
  - All three are [Game text via wiki].
- **Look:**
  - **S'no Matter:** a glowing icy crystal device held two-handed, cyan to white (#5FC4DB → #9BFEFD).
  - **Let It Cold:** two black shoulder racks, each with **two blue rockets (#2062DA)** carrying grinning cartoon-face decals, striped sticks and icy tips.
  - **Snowtato Launcher:** a silver barrel, a lavender-blue body and fins (#6D7DA9) and a white snow-heap hopper.
  - All [Observed].
- **Projectile and impact:**
  - S'no Matter: a slow grey projectile that freezes everyone in the blast for 2 s, teammates included.
  - Let It Cold: rockets "rain down", explode and freeze for 3 s.
  - Snowtato: exploding snowballs, with lingering snow that blocks explosives.
  - All [Fan-wiki]. The frozen-target look is undocumented [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/winter_group.png
  - Sources: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Letitcold.png, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Snowtato.png, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Snomatter.png, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Mini.png
- **Depiction for shorts:** targets frozen in a cartoon ice block with chattering teeth [BBG News invention].
- **Confidence:** partial.

## Summer 2017 fidget trio: Fidget Boomer (Sniper primary), Spin Baby Spin (Arbiter primary), Hazard Toy (Assassin primary), all 2.27, May 29 2017
- **Official text:**
  - Fidget Boomer: "Have toy tricks gone too far!? Explosions are safe right?"
  - Spin Baby Spin: "When I spin you spin!"
  - Both [Game text via wiki].
- **Look:**
  - **Fidget Boomer:** a **rose-chrome three-lobed spinner** (#8B5160, highlights #DC8297) raised in Astoria's hand, about 0.45× her height.
  - **Spin Baby Spin:** a **gunmetal translucent spinner with a glass hub**, held in Sanchez's mechanical right hand.
  - **Hazard Toy:** green trefoil, as in Part A.
  - All [Observed].
- **Projectile and impact:**
  - Fidget Boomer: "the fastest projectile speed in the game" (3000 u/s); explodes after a short delay on surface contact; 40–70 damage, no status effect.
  - Spin Baby Spin: explodes and causes **Controls Reversed** for 8 s, shown as "a green question mark" overhead, with music disabled and sounds echoing.
  - Both [Fan-wiki].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/fidget_group.png
  - Sources: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/FidgetBoomer.png, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/SpinBabySpin.png, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/HazardToy.png, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Kelowna.png
- **Depiction for shorts:** a "fidget craze" short with three bears and three spinners: a pink pop, a green question mark and a green poison skull.
- **Confidence:** partial.

## Late-era drops, 2018
- **Kelowna** (Arbiter primary, 2.31, Mar 8 2018). No description: "the only Arbiter primary to lack a description" [Fan-wiki].
  - Look: a black gun with a **glowing violet canister (#5E2CFC)**, a purple-lens scope and a white crystal-spike muzzle crown [Observed, Kelowna.png].
  - Impact: a small projectile bursts into poison clouds containing "a clone of Arbiter doing the Creepin taunt", and kills play "Thriller" [Fan-wiki]. **Do not use that song** [Inference: rights].
- **I Lava You / "I Lava U"** (Sniper secondary, 2.51, Apr 13 2018): proximity mines fired in a straight line, 1 s priming, 100-unit trigger, 25–60 damage [Fan-wiki]. No image, so the look is [Unverified].
- **Dragon Slayzer (BBG)** (Engineer secondary, 2.51): a stub with no image [Fan-wiki]. The BB Overclock version is "a dragon with a sword coming out of its head… The laser… is an orange blast. The dragon's color is red" [Fan-wiki]. Whether BBG's version matches is [Unverified].
- **Social Butterfly (BBG)** (2.53): see Part B.
- **Confidence:** partial / unknown.

---

## Corrections for the character file
1. **oliver.md**
   - Current text: "The Bearzooka is drawn as a green, hazard-striped tube [Observed; Inference]."
   - Correction: the BBG Bearzooka is a coral-red tube (#A54447; #D05655 under 2026 trailer light) with glowing orange chevron windows (#EB7921–#FF8F25), grey bands, a black bore and a grey-and-red checkered flared end, carried on the right shoulder. Green launchers are Tillman's Twin Bearzookas (olive #868F43) or the BBZ / BB-1 Bearzooka.
   - Evidence: Photo_19-04-13_12_02_26_PM.png, Bearzooka_Concept.png, trailer t_0009 at 4.0 s (a green-skinned Soldier with a gold-and-black bullet bandolier carrying the coral launcher), Ohmagawdyas.png, and the wiki's "red and orange lines".
2. **sanchez.md** (colours line)
   - Current text: "Bind Gun #1E6FD9"
   - Correction: "Bind Gun #0991D4 (lit #1CB5F3, highlight #6CCFF4; reads #367494 in dim in-game light), glowing white-cyan muzzle disc #EBF0F5."
   - Evidence: sampled from Sanchez_weapons.png and Bind_Gun.png.
3. **sanchez.md** (reference prompt)
   - Current text: "Holds a large glossy blue sci-fi gun (#1E6FD9)."
   - Correction: "Holds a large, angular, glossy azure sci-fi rifle (#0991D4 with #1CB5F3 highlights) with a glowing white-cyan round muzzle, about 0.7× his height, two-handed across the chest."
4. **sanchez.md** (open questions)
   - Current text: "'Adrenaline Gun' (site) versus 'Adrenaline Burst' (wiki)."
   - Correction: both names are on the wiki, for different games. "Adrenaline Gun" is the BBG page (the Bind Gun, with stats edited 2021-06-18 UTC and the page moved 2021-07-17). "Adrenaline Burst" appears only in the wiki's BBH roster table, while SkyVu's own BBH page says "Adrenaline Gun".
5. **riggs.md**
   - Current text: "Their look is undocumented, so designs, like the toothbrush prop, are [BBG News invention]."
   - Correction: the Beebeegun's look is documented in images. It has a dark gunmetal riveted body with pink and blue striped vents, a glossy pink octagonal hive canister (#DB4ACF–#FC83FE) with a cartoon bee, small yellow-and-black bees and a glowing magenta spiral coil; it fires pink tracer streaks with pale-yellow star hits.
   - Evidence: Theincredibleriggs.png (2015), the Steam screenshot screen_00, and trailer t_0070–t_0073 at 34.5–36.0 s.
6. **riggs.md** (skins list)
   - Current text: "The Incredible Riggs" (listed without status).
   - Correction: add "seen in the Sept 2026 playtest loadout menu [Observed]". Also add the Catastrophe cat-head gloves (BBR 1.3.1) to his extra melees.
7. **b-1000.md**
   - Current text: "Defaults: Grenader (…), Last Resort (…), Axecutioner (…)"
   - Correction: mark Last Resort as removed. The wiki page carries "THIS WEAPON IS REMOVED" (on the page by Nov 2020). It was the default secondary in the 2013–2020 era; the current and 2026 default is unknown.
8. **saberi.md**
   - Current text: "Energy Rifle, Plasma Machine Gun, Missiles, Minigun, Mallet, Sledgehammer; later Plasma Shotgun and Gamma Burst [Canon]"
   - Correction: the list is incomplete. Add Toxic Rifle (2.15), Land Mine (2.19), ClubCobra (2.20; "A powerful melee made of jade and gold."; a gold cobra-head club) and Social Butterfly (2.53) [Fan-wiki].
9. **botch.md**
   - Current text: "extras include Orbs, Fear Orbit, Cosmic Bomb, Gravity Well and Toxic Plague"
   - Correction: add Hazard Toy (2.27, May 29 2017), a green trefoil fidget spinner that fires a straight poison-burst shot. It is missing from the wiki's Assassin page.
10. **graham.md**
    - Current text: the weapons line names only Power Glove, Turret, T Square and Gernobyl.
    - Correction: add MuskIt (2.12; a musket that sprays an irradiating green cone) and Bind Field (2.6, formerly Slow Field; a studded brown, green and purple ball that makes a 75% slow field). Neither page is in Category:BBG Weapons.
11. **wil.md**
    - Current text: "Senor Potato, Pie Bomb, Traffic Light [Fan-wiki]"
    - Correction: the Traffic Light has official item text [Game text via wiki] and a documented look: a yellow and black pole with a red and green two-lamp head.
12. **Mapping file** (weapons_by_class.json, not a character file)
    - Remove A Salt Rifle, Heavy A Salt Rifle, Soaker, Spreadshot (BBG), Steamshot, B.E.A.R. Club and Krikkit Bat from Riggs and Huggable. They come from a copy-pasted changelog.
    - Assign Adrenaline Gun → Sanchez, Catastrophe → Riggs, ClubCobra → Saberi, Hazard Toy → Botch, MuskIt and Bind Field → Graham, Traffic Light → Wil, Social Butterfly (BBG) → Saberi.
    - Drop The Incredible Riggs, which is a skin.

## Open questions
- Does the 2026 build's Arbiter default fire the slowing Bind Gun or the speeding Adrenaline Gun, and did the model change?
- What colour is the beam, and what does a "sped-up" target look like? No image found.
- Hazard Toy: does the spinner itself fly, and what colour is its poison cloud?
- Catastrophe, ClubCobra and Traffic Light swing animations and hit effects are undocumented.
- Social Butterfly has no image or effect description at all.
- When were Bouncing Betty, Greased Lightning and Last Resort removed, and are they in the 2026 build?
- ClubCobra's health modifier: +10% (screenshot and Health page) or +15% (its own page)?
- Steam claims "80+ primaries / 60+ secondaries / 50+ melees" against about 77/64/46 on the wiki. Are there new or undocumented 2026 weapons?
- The Sept 20 2026 showcase thumbnail shows the build string "3.0.5_2026.11.19_B1". What does the date field mean?
- Archived SkyVu sources (BBR 1.3.1 blog, BBG 2.6, 2.20, 2.27 notes) were unreachable through web.archive.org this run. Re-verify the version dates and official wording.
- Which Oliver skin is the green bear in trailer t_0009?
- Were the seasonal weapons ever time-limited? Do frozen targets have a visual?
