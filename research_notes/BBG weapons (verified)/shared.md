# Unassigned, shared and special weapons

This dossier covers the BBG weapons that fall outside the per-class files:
- the five Category:BBG Weapons pages that no class page links to;
- four real BBG weapon pages missing from that category;
- the "shared weapons" question, and what classes really share (the Specials);
- retextures (Sci-Fi ASR, Sci-Fi HASR);
- the Bearzooka colour conflict;
- BBR-era carryovers and BBH name carryovers;
- removed and reworked weapons;
- seasonal and promotional drops.

**How this version was built**
- The draft was researched on 2026-10-16.
- A source check and an image check ran on 2026-10-17.
- In this edit (2026-10-17) I re-fetched every disputed wiki page live through the MediaWiki API. The copies are in `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/shared-edit/wiki/`.
- I also fetched the YouTube oEmbed titles of the cited demo videos and re-opened the key images and trailer frames.
- "Images viewed" lists files opened by the draft author or the image check. "(re-opened)" marks the files I opened again in this edit.
- In an Oct 18 2026 edit I applied the round-3 Bearzooka corrections from shared.addendum.md ("Shared addendum (round 3)": the trailer rocket, its timing and the open question), after re-opening its trailer frames and re-matching t_0008–t_0010 to exact frames of trailer.mp4. I also brought the trailer dating below in line with the storyboard match.
- In a later Oct 18 2026 edit I added the Bearzooka blast that oliver.addendum.md (Bearzooka, Impact) records in 2014–15 fan footage, after opening its two storyboard crops (bz7W_a.jpg, bz0Z_38.jpg) and the two videos' Invidious metadata (titles and upload dates). What the Steam trailer shows, and that no 2026 frame shows the blast, are unchanged.

**Sources reachable**
- **Wiki:** the fan wiki through its MediaWiki API (wikitext, categories, revisions, image info).
- **Official sites:** battlebears.com, play.battlebears.com, the Steam appdetails API and the Steam news API.
- **Video:** i.ytimg.com thumbnails and YouTube oEmbed titles.
- **Local:** the official Steam screenshots and the official Steam trailer (t_N is nominally at (N-1)×0.5 s).
  - Matched against exact frames, t_N is really about 0.22 s later: t_0008, t_0009 and t_0010 are at 3.72, 4.22 and 4.72 s [Observed: shared.addendum.md, round 3, "Important timing finding" (t_0005–t_0008); t_0008–t_0010 re-matched in the Oct 18 edit]. So trailer times read off the t_ series below are about 0.22 s early unless re-timed.
  - The trailer and the screenshots are SkyVu's 2013 launch footage re-used on the 2026 Steam page (2013 footage [Inference, strong]). The class cards are pixel-identical to SkyVu's May 30 2013 trailer rfAyqVJrli4 at full size, and the gameplay matches that trailer's 160×90 YouTube storyboard at an offset of about 4 s (45 of 55 frames from 5 to 59 s) [Observed, storyboard size] (/home/user/thallo-site/research_notes/BBG weapons (verified)/2026.md, "The Steam trailer is 2013 footage"; /home/user/thallo-site/research_notes/BBG maps (verified)/00_OVERVIEW.md, section 0, item 1). So they show the 2013 look, not the 2026 build.
  - That includes the Space Oddity clip (about 30.0–32.8 s) and screen_01, a frame of it: the same moment, bloom included, is in the 2013 storyboard (2013 35–36 s = Steam 30.85–31.95 s) [Observed], so it is 2013 footage too [Inference, strong]. Only why its pillar top blooms more than fan captures is [Unverified]. This dossier cites neither.
  - In this edit I also compared the gameplay shots cited below with the storyboard of rfAyqVJrli4 (160×90, one frame per second): the B-1000 and Bearzooka shots (1.5–5 s), the Graham segment (7.25–10.5 s) and the Electric Honey shot (34.5–36 s) are all in it [Observed, low-res: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/shared_trailer_rule/steam_vs_2013_sb.jpg].

**Sources not reachable**
- **web.archive.org.** The connection is reset on every attempt, including three more retries in this edit. So no archived SkyVu blog post or patch note (BBR 1.3.1, BBG 2.6, 2.20, 2.27) was re-checked. Version dates below come from the wiki's Updates table [Fan-wiki].
- **The JustNubz 2026 showcase.** Thumbnails only; the video was not watched.

**Era terms**
- BBR = Battle Bears Royale, Oct 2011 to April 2013.
- BBG = Battle Bears Gold, relaunched May 24 2013, updates to 3.0.1 (Dec 2021).
- BBG 2026 = the re-release on Nov 4 2026.
- BBH = Battle Bears Heroes, 2024.

The wiki's `Photo_19-04-13_*` shop shots (uploaded 2013-04-19) and Dban1's demo videos (published 2013-04-14/15) are **BBR v1.4.3, April 2013**, from before the BBG relaunch [Fan-wiki dates; Inference].

**Scale reference** (BBG News chart, head height, Oliver = 1.0×; [BBG News invention], from /home/user/thallo-site/bbg-news-repo/characters/README.md line 54):
- B-1000 ~1.5×
- Riggs ~1.2×
- Oliver, Astoria, Graham, Saberi, Sanchez and Botch 1.0×
- Wil ~0.9× and Tillman ~0.9×
- Huggable ~0.65×

Weapon sizes below are measured on the images [Observed] and converted with that chart [Inference].

## Key findings

1. **Why the five pages were "unassigned."** It is a link and categorisation problem, not a sign of special weapons [Fan-wiki, checked against the class-page wikitext]:
   - **Adrenaline Gun:** the Arbiter (BBG) page still links the old name "Bind Gun", which redirects.
   - **Catastrophe:** the Heavy (BBG) page links the in-game misspelling "Catastophe", which redirects.
   - **ClubCobra:** the Combat Tech (BBG) page links "Clubcobra", which redirects.
   - **Hazard Toy:** it is missing from the Assassin (BBG) page.
   - **The Incredible Riggs:** it is a Heavy **skin**, miscategorised as a weapon.

2. **The 185-page category is not a clean weapon list.**
   - It also holds a skin (The Incredible Riggs) and a list page, "Soldier (BBG)/Weapons" (categories Soldier and BBG Weapons) [Fan-wiki].
   - Four real BBG weapon pages are linked from class pages but missing from the category [Fan-wiki]:
     - MuskIt (Engineer)
     - Bind Field, formerly Slow Field (Engineer)
     - Traffic Light (Chub Scout)
     - Social Butterfly (BBG) (Combat Tech)
   - That gives 183 + 4 = 187 weapon pages: 77 primaries, 64 secondaries and 46 melees, removed weapons included [Fan-wiki; Inference: arithmetic].
   - Steam's 2026 copy promises "80+ PRIMARY WEAPONS 60+ SECONDARY WEAPONS 50+ MELEES 10 SPECIAL EQUIPMENT" [Canon] ([Steam appdetails](https://store.steampowered.com/api/appdetails?appids=4408320)). The 2026 build may hold weapons the wiki never documented [Inference].

3. **No BBG weapon is shared between classes.**
   - No weapon page carries two class categories. The 186 weapon links on the 11 class pages resolve to 186 different pages [Fan-wiki; category scan re-run in this edit].
   - The tagging is not uniform [Fan-wiki]:
     - Bounce Lazer has no class category, although the Heavy page lists it and Updates 2.19 says "Heavy's Bounce Lazer".
     - Dragon Slayzer (BBG) is tagged "Graham", not "Engineer".
     - 18 Huggable pages use "Huggable (class)".
   - In `weapons_by_class.json`, seven Soldier weapons also appear under Riggs and Huggable: A Salt Rifle, Heavy A Salt Rifle, Soaker, Spreadshot, Steamshot, B.E.A.R. Club and Krikkit Bat. That comes from a copy-pasted Soldier changelog on the Heavy (BBG) and Huggable (BBG) pages [Fan-wiki; Inference].
   - What every class really shares is the **10 Specials** [Fan-wiki].

4. **Bearzooka colour conflict resolved.**
   - The BBG Bearzooka is **coral-red with glowing orange window panels** in all three images [Observed]:
     - the BBR April 2013 in-game shop shot;
     - the wiki's concept image (official provenance unverified);
     - the Steam trailer (2013 footage [Inference, strong]).
   - It is still coral-red in 2026: SkyVu's own Jul 6 2026 "Classic Oliver" short (byri_kQBUS4) shows it with orange panels and a grey-checkered flared end, and a 2026 playtest loadout render shows the same tube [Observed, re-opened; 2026.addendum.md and oliver.addendum.md].
   - The green, hazard-striped launcher is the **BB: Zombies** Bearzooka (wiki image Bear.jpg, captioned "Bearzooka in BBZ"). That is the likely origin of oliver.md's description [Observed; Inference].
   - The other green launchers are Tillman's yellow-olive **Twin Bearzookas** [Observed].

5. **What in this dossier is visible or named in a 2026 source:**
   - the Bearzooka (Steam text [Canon]; SkyVu's Jul 6 2026 "Classic Oliver" short and a 2026 playtest loadout render [Observed]);
   - the Turkish SW Boots and the "10 SPECIAL EQUIPMENT" count (Steam text) [Canon];
   - the **Electric Honey**, the gun this dossier shows with The Incredible Riggs (Oct 2026 playtest frames: a white-furred Riggs carries it in droid BBG's CmYil-JJdC0, HUD 93/120 [Observed, re-opened]; that it is the Electric Honey is [Inference, strong], riggs.addendum.md);
   - the Irradiated status icon: SkyVu's Aug 16 2026 "Official Playtest Highlights" thumbnail (C7uFxvSZ10c, HUD build 3.0.0) shows the yellow disc with black radiation wedges, stacked with a Slowed Z, over the target of a gold Graham's yellow beam [Observed, per 2026.addendum.md; crop c7u_icon.jpg re-opened];
   - **The Incredible Riggs** skin and a "BUNDLE DEALS" menu banner (thumbnail of a fan's Sept 2026 playtest showcase) [Observed].

   **Not 2026 evidence:** the Bearzooka at trailer 3.89–4.59 s and its rocket at 1.92–3.05 s (the rocket's Bearzooka link is [Inference, high]), the Electric Honey in Steam screenshot screen_00 and at trailer 34.5–36 s, and the Irradiated status icon at trailer about 8.5 s (the Graham segment) are 2013 footage [Inference, strong]. They show the 2013 look.

   Everything else here is unconfirmed for 2026 [Unverified].

6. **Correction to the draft.** The coil gun seen with The Incredible Riggs, in Steam screen_00 and in the trailer is the **Electric Honey**, not the Beebeegun. The wiki's infobox captions and images settle it [Fan-wiki; Observed].

---

## PART A: The five unassigned pages

## Adrenaline Gun, formerly the Bind Gun (Primary, Arbiter / Sanchez default; Bind Gun from BBG 2.6, Dec 20 2013; reworked June 2021; 2026 version unconfirmed)
- **Official text:**
  - **Current:** "The only bad thing about being faster than light is that you always live in darkness" [Game text via wiki]. The wiki tags it "~Official Battle Bears Gold description, submitted by community member Wilpower784" ([Adrenaline Gun](https://battlebears.fandom.com/wiki/Adrenaline_Gun)).
  - **Old Bind Gun text:** "One weapon to slow them all!" [Game text via wiki].
  - **2.6 class blurb:** "Back from the brink of death, Sanchez has been rebuilt from the arm up! Use his unique weaponry to slow down opponents and finish them off with his devastating melee attacks." [Game text via wiki] ([BBG/Versions/2.6](https://battlebears.fandom.com/wiki/Battle_Bears_Gold/Versions/2.6)).
  - **BBH only, not BBG:** "Sanchez's "Adrenaline Gun" rapidly fires four staggered projectiles with a fast reload time." [Canon, BBH] ([characters](https://battlebears.com/pages/characters)).
- **Rework history** [Fan-wiki, page and revision log]:
  - The trivia says the weapon "used to be called Bind Gun with a speedMultiplier of 0.8, but it was changed into the adrenaline gun on the 19th of June 2021".
  - In the revision log, the stats were edited on 2021-06-18 at 23:32 UTC (rev 77348). The page was moved "Bind Gun → Adrenaline Gun: New name for the weapon" on 2021-07-17.
  - **2018 revision (75784):** "Slow 0.9", damage 6.0, 1 s duration, ammo 45. The text says targets are "slowed down for a brief amount of time by 90 u/s. The longer the target is under the effect, the slower they will become, up to the point of becoming immobile." Reading "Slow 0.9" as a 10% slow is [Inference].
  - **2020-11-10 revision:** 20% per hit for 1.25 s, damage 5.0, ammo 55.
  - **Current infobox:** damage 7.0, "Speed Effect 50% per hit" for 0.5 s, rate of fire 0.15 s, ammo 55, reload 4 s, stat modifier "2% Speed".
  - The page still uses the 2013 Bind Gun image ("Sanchez with the Bind Gun"), so whether the model changed is [Unverified].
- **Look:**
  - The weapon card "New Character: Sanchez" labels the gun "BIND GUN" with an arrow, next to Blade Augment, Cloak Field, Harvester, Speed Field and Glue Bomb [Observed, Sanchez_weapons.png, re-opened].
  - The card is 900×691 and was uploaded to the wiki on 2013-12-20 at 00:46 UTC, the 2.6 release day. sanchez.md cites the same file name from battlebears.com via the Wayback Machine (`/wp-content/uploads/2013/12/sanchez_weapon_ad2-900x691.jpg`). So it is probably SkyVu's official card [Inference; the archive copy was not reachable].
  - **Shape:** a long, chunky, angular sci-fi rifle with stepped armour panels and an open slot along the top. It is held two-handed across the chest, with the red mechanical right arm under it. It is about **0.7–0.75× Sanchez's height**, so ≈0.7× Oliver [Observed; Inference].
  - **Colours on the card** (two independent samplings): glossy azure **#0991D4–#138CC0**, lit faces #1CB5F3–#29B7EE, highlights #6CCFF4–#6BE4F7.
  - **Colours in the dim shop shot:** steel-cyan **#2D6D8F–#367494**, bright edges #61CDE6–#69B3C6, shadow #133248–#15364D.
  - **Muzzle:** a round **glowing white-cyan disc** (#DCE9F5–#EBF0F5) ringed in near-black (#07131C–#0F2D3D) [Observed].
- **Firing:**
  - "an automatic weapon that shoots a purple beam. It is not completely accurate as the beam tends to move in an oval-like wave" [Fan-wiki].
  - No image or frame of the beam was found [Unverified].
- **Projectile:**
  - A continuous purple beam that wobbles in an oval wave [Fan-wiki].
  - BBH's "four staggered projectiles" are BBH only [Canon, BBH]; do not port them to BBG [Inference].
- **Impact / end result:**
  - **Bind Gun era (2013–2021):** targets are slowed, and the slow builds toward immobility. The Status Effects page lists the Bind Gun under **Slowed**: "a yellow Z will appear over the player's head" [Fan-wiki].
  - **Adrenaline era (2021 on):** targets "will be drastically sped up for a brief amount of time". The wiki suggests using this to make them "fall off the map, run into a Sanchez melee or barely miss their intended destination such as a powerup or safe area" [Fan-wiki].
  - **Shields:** "If the target has a Shield, the speed up effect will be applied, but damage is not inflicted." [Fan-wiki]. A glitch lets the wobbling beam hit the shooter when backing up [Fan-wiki].
  - **No "sped-up" icon is documented.** The only speed icon on the Status Effects page is the coffee mug ("Caffeinated"), which lists only Caffeine Injection [Fan-wiki].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Sanchez_weapons.png ([File:Sanchez_weapons.jpg](https://battlebears.fandom.com/wiki/File:Sanchez_weapons.jpg)) (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Bind_Gun.png ([File:Bind_Gun.png](https://battlebears.fandom.com/wiki/File:Bind_Gun.png)) (re-opened)
- **Depiction for shorts:**
  - Sanchez braces the big azure rifle and sprays a wobbling purple ribbon beam.
  - **2013 setting:** the target slows to a crawl under a cartoon yellow "Z".
  - **2021+ setting:** the target zips off too fast, with speed lines [BBG News invention: speed lines], and overshoots a ledge or a power-up (the wiki's own usage note).
  - Pick one era per short and say which.
- **Confidence:** partial. The look is observed; the beam and the speed visuals are fan-wiki only; the 2026 version is unknown.

## Catastrophe (Melee, Heavy / Riggs; BBR v1.3.1, first week of the drop that began June 28 2012; carried into BBG; 2026 unconfirmed)
- **Official text:** "Let Riggs bring the kitten cuddlin' to you! You may not like how he does it, though, and living through it isn't likely... but hey, kittens!" [Game text via wiki] ([Catastrophe](https://battlebears.fandom.com/wiki/Catastrophe)).
  - The page says it was "released during the first week of v1.3.1" [Fan-wiki].
  - The in-game name is misspelled "CATASTOPHE": it reads that way on the Oct 2012 shop screenshot [Observed], and the wiki notes it [Fan-wiki].
- **Look:**
  - A **pair of calico cat-head gloves**, one over each fist [Observed, Catastrophe.png].
  - Each head is low-poly: brown back (#441D17–#5B3D23), rust-orange patches (#924920–#A35525) and white muzzle and cheeks (#D1C6C1–#F3F2F0).
  - Each side has one huge glossy **blue cartoon eye** (#0072CF–#0E74CA, with a white highlight), small pointed ears and a red open mouth (#7F0A0D) [Observed].
  - Each glove is about head-sized for Riggs, about 0.35× his height ≈ 0.4× Oliver [Observed; Inference].
  - The "BBR 1.3.1 and BEYOND!" promo graphic shows the same cat head among the 1.3.1 weapons [Observed, BBRWEAPONS.png]. A wiki user uploaded it in 2012, so official provenance is [Inference].
- **Firing:**
  - A two-glove melee punch [Fan-wiki].
  - **The stats conflict on the wiki:**
    - **Damage:** the page says "40 damage which can be doubled due to the second glove". The 2.6 notes say "Catastophe Melee Damage decreased from 30 to 25" [Fan-wiki].
    - **Modifiers, page body:** "a 20% speed reduction and a 10% health boost".
    - **Modifiers, trivia:** "the only Heavy melee with both a positive speed and health stat modifier".
    - **Modifiers, Health page:** "Catastrophe (5% health)".
    - **Modifiers, "Previous Stats":** "5% health boost, 5% health reduction / No speed modifier, 15% speed boost" [Fan-wiki].
    - **Screenshot:** the Oct 2012 shop screenshot shows "HEALTH -5%" and "SPEED +15%" [Observed].
  - The current BBG modifiers are therefore [Unverified].
  - No swing animation or sound is documented.
- **Projectile:** none (melee).
- **Impact / end result:** undocumented beyond damage [Unverified].
- **Era notes:**
  - "Like all v1.3.1 weapons and skins, the Catastrophe was offered to those who took part in the Forum Appreciation promotion, free of charge and before the official release date/week" [Fan-wiki].
  - The original price was 20 Gas [Fan-wiki].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Catastrophe.png ([File:Catastrophe.png](https://battlebears.fandom.com/wiki/File:Catastrophe.png); Oct 2012 shop screenshot, uploaded 2012-10-20, Riggs in the Teen Wolf skin)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Catastrophe_1.png ([File:Catastrophe_1.png](https://battlebears.fandom.com/wiki/File:Catastrophe_1.png))
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/BBRWEAPONS.png ([File:BBRWEAPONS.png](https://battlebears.fandom.com/wiki/File:BBRWEAPONS.png))
- **Depiction for shorts:** Riggs throws a one-two of cat-head punches. Each glove's big blue eye blinks on contact, with a "mrrp!" and a burst of yellow sparks and floating hearts [BBG News invention: sound and hit FX]. Keep the calico colours and one big eye per side.
- **Confidence:** partial. The look is observed; the stats conflict; the hit effects are unknown.

## ClubCobra (Melee, Combat Tech / Saberi; BBG 2.20, May 29 2015; 2026 unconfirmed)
- **Official text:** "A powerful melee made of jade and gold." [Game text via wiki] ([ClubCobra](https://battlebears.fandom.com/wiki/ClubCobra)).
- **Stats:**
  - 50 damage, 150,000 Joules, level 10 lock [Fan-wiki].
  - **Health modifier conflict:** the ClubCobra page says "+15% Health"; the Health page says "+10% health". The shop screenshot shows "HEALTH +10%" [Observed], so +10% is better supported.
- **Bundle:**
  - The Bundle Deals table lists Sandchez, Toxic Plague, Toxic Rifle and ClubCobra for 350,000 Joules, with no version or dates [Fan-wiki].
  - The bundle art reads "**SANDKING** BUNDLE" [Observed]. "Sandkind" is only the file name.
  - The file was uploaded 2015-06-01, three days after 2.20. Tying the bundle to the 2.20 launch is [Inference].
  - The art also shows ClubCobra's gold cobra with a green eye, beside a green Toxic Plague orb and the pink-purple scorpion-tailed Toxic Rifle [Observed].
- **Look:**
  - A **golden cobra-head club** [Observed, Clubcobra.png]. A straight gold shaft carved with zig-zag and glyph patterns ends in a hooded cobra head curling forward, with an open mouth.
  - A green jade eye (#29C74E–#29D250) sits in a dark-violet socket.
  - The grip is dark brown leather (#27160D–#2D1912) ending in a gold pommel hook.
  - Gold tones: lit #F9C10A, mid #DF9B0C, shadow #A37B02–#A67809, highlights #F3D52B–#FFD823.
  - Most of the "jade" is the eye; the club reads almost entirely gold [Observed; Inference].
  - Saberi holds it one-handed, raised. It is about 0.6× her height ≈ 0.6× Oliver.
- **Firing:** a melee swing; the animation is undocumented [Unverified].
- **Projectile:** none.
- **Impact / end result:** undocumented [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Clubcobra.png ([File:Clubcobra.jpg](https://battlebears.fandom.com/wiki/File:Clubcobra.jpg))
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/png/Sandkindbundle.png (File:Sandkindbundle.jpg) (re-opened)
- **Depiction for shorts:** Saberi swings the gold cobra overhead. On impact its mouth snaps shut with a gold flash and green sparkle chips [BBG News invention: hit FX]. Keep it gold, with a single jade-green eye.
- **Confidence:** partial. The look is observed; the swing and the hit are unknown.

## Hazard Toy (Primary, explosive and poison; Assassin / Botch; BBG 2.27, May 29 2017; missing from the wiki's Assassin page; 2026 unconfirmed)
- **Official text:** "Banned from elementary schools world wide, this weapon is as dangerous as it looks!" [Game text via wiki] ([Hazard Toy](https://battlebears.fandom.com/wiki/Hazard_Toy)).
- **Era:**
  - Released in 2.27 alongside Fidget Boomer (Sniper) and Spin Baby Spin (Arbiter), with a summer-themed No Bear's Land [Fan-wiki, Updates].
  - "It is based off of the Fidget Spinner" [Fan-wiki].
  - 60 Gas, level 1 [Fan-wiki].
- **Look:**
  - A **translucent dark-green three-bladed fidget spinner** [Observed, HazardToy.png, re-opened]. The wedge-shaped blades look like the arms of a radiation trefoil, probably the "hazard" pun [Inference].
  - It floats beside Botch, **almost face-on, tilted about 20–30°**: all three blades and the hub of concentric dark and light green rings are visible.
  - Botch's paws are held out at waist height.
  - Blade colours: main mass #1B4D1D–#1E5220, lit #206421, edges #3D8935 [Observed, sampled in this edit and by the image check].
  - Its diameter is about 0.5× Botch's height.
  - Botch's eyes glow lime #B7F923–#B7FA20 in the same shot.
- **Firing:**
  - "a projectile weapon which explodes upon contact" with "a straight trajectory compared to the curve of Chaos Toss, and a faster projectile speed than Toxic Plague" [Fan-wiki].
  - Rate of fire 1.5 s, ammo 3, reload 3.5 s, projectile 1,100 u/s, explosive 25–50 [Fan-wiki].
- **Projectile:** what visibly flies (the spinner itself or a pellet) is undocumented [Unverified].
- **Impact / end result:**
  - It explodes and "poisons enemies caught in the radius". The poison stacks across clouds, about 4 damage per tick over 5 s [Fan-wiki].
  - The Status Effects page lists Hazard Toy under Poisoned: "a purple/green skull will appear over the player's head" [Fan-wiki].
  - The cloud colour is undocumented. The wiki calls Botch's Chaos Toss cloud "toxic green" [Fan-wiki], so green is likely [Inference].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/HazardToy.png ([File:HazardToy.jpeg](https://battlebears.fandom.com/wiki/File:HazardToy.jpeg)) (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/fidget_group.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/v2/fidget.jpg (re-opened)
- **Depiction for shorts:** Botch flicks the dark-green trefoil spinner and it whizzes straight out [BBG News invention: the spinner itself flies]. It pops in a puff of green gas [Inference: colour]. A small purple-green cartoon skull bobs over each target's head while their health ticks down.
- **Confidence:** partial. The held look is observed; the flying object and the cloud colour are unknown.

## The Incredible Riggs (Skin, not a weapon; Heavy / Riggs; BBG 2.15, Dec 20 2014; seen in a Sept 2026 playtest thumbnail)
- **Official text:** "You won't like me when I'm green! " [Game text via wiki] ([The Incredible Riggs](https://battlebears.fandom.com/wiki/The_Incredible_Riggs)).
  - Price 400,000 Joules [Fan-wiki].
  - "It is a reference to the Incredible Hulk" [Fan-wiki].
- **Status:**
  - It is a skin whose page is miscategorised in Category:BBG Weapons [Fan-wiki].
  - The thumbnail of JustNubz's "BBG All Classes Showcase [Skins, Taunts, Weapons, and Melee] (from Closed Playtest #4)" (a fan video, Sept 20 2026) shows the loadout menu [Observed, re-opened]:
    - "CHARACTER HEAVY / SKIN THE INCREDIBLE RIGGS", with green Riggs on the pedestal and no gun in hand.
    - A "BUNDLE DEALS" banner and a "PRO-MODE FEATURES AVAILABLE NOW" sign.
    - A build string read as "3.0.5_2026.11.19_B1" over "8218727" ("B1" could be "81").
- **Look:**
  - A green-skinned, hugely muscled Riggs with a bulldog snarl and bared teeth [Observed]. Skin green is about #448B2F on the wiki's skin image and #449C2E in the 2026 thumbnail, with highlights #88C773.
  - **Torn maroon shorts:**
    - wiki image: shadow #5C2226 to lit #762F30 (range #501D20–#792E34);
    - 2026 thumbnail: about #6B2331.
  - A segmented grey-beige shell backpack with a blade stuck in it [Observed].
  - The concept art shows two backpack options: a rock shell, and a tech shell with a green spiral [Observed].
- **Weapon in the wiki's skin image:** the **Electric Honey**, not the Beebeegun. See the next section.
- **Impact / end result:** cosmetic only; skins change nothing mechanically [Inference].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Theincredibleriggs.png ([File:Theincredibleriggs.jpg](https://battlebears.fandom.com/wiki/File:Theincredibleriggs.jpg)) (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Incredibleriggsconceptart.png ([File:Incredibleriggsconceptart.jpg](https://battlebears.fandom.com/wiki/File:Incredibleriggsconceptart.jpg))
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/web/showcase_maxresdefault.jpg (https://i.ytimg.com/vi/-lAtv-j9Sms/maxresdefault.jpg) (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/web/ver_crop.png (re-opened)
- **Depiction for shorts:**
  - Use the in-game skin exactly: green skin, torn **maroon** shorts and the shell backpack.
  - Do not add Hulk trademarks such as purple trousers or Marvel lettering [Inference: IP caution].
  - If he fires the pink coil gun, call it the Electric Honey. If he uses his default Beebeegun, draw the black-and-gold version (see riggs.md correction).
- **Confidence:** observed (skin look and its presence in the 2026 playtest thumbnail).

## Electric Honey (BBG), the gun shown with The Incredible Riggs (Primary, Heavy / Riggs; original BBR primary; in Steam screenshot screen_00 and the Steam trailer, 2013 footage [Inference, strong]; seen in the Oct 2026 playtest)
This is a Riggs weapon, covered fully in the Riggs dossier. It is here because the draft misidentified it.
- **Official text:** "Electrically charged bees are slightly smaller* allowing for a higher bees-per-hive ratio and thus longer continuous fire!" [Game text via wiki] ([Electric Honey (BBG)](https://battlebears.fandom.com/wiki/Electric_Honey_(BBG))).
- **Identification:**
  - The Electric Honey (BBG) infobox shows Photo_19-04-13_12_50_47_PM.png, captioned "Riggs with the Electric Honey". It has a pink-and-purple striped body, a pink octagonal hive and a **glowing magenta spiral coil** [Fan-wiki; Observed, re-opened].
  - The Beebeegun infobox shows Photo_19-04-13_12_50_44_PM.png, captioned "Riggs with the Beebeegun": a black body with orange-and-black striped vents, a **gold** hive and no coil [Fan-wiki; Observed, re-opened].
- **Look (as with The Incredible Riggs)** [Observed]:
  - A dark gunmetal riveted minigun body with pink-and-blue striped vents and striped pink-blue wing fins.
  - A glossy pink octagonal hive (#DB4ACF–#FC83FE; #CB3ADC–#DF56F6 in the 2013 shot) with a cartoon bee peeking out.
  - Small yellow-and-black bees.
  - A glowing magenta spiral coil around the barrel, and a black muzzle.
- **2026:** in the Oct 2026 playtest (droid BBG's CmYil-JJdC0, first person) the gun has a glowing pink hexagonal hive with violet rings on a black body, and the HUD shows its icon with ammo at 93/120 [Observed, re-opened]. That it is the Electric Honey, on the classic model, is [Inference, strong] (riggs.addendum.md: HUD icon, 120 ammo, 200 health).
- **Firing / projectile:**
  - An automatic minigun, 120 ammo, 0.10 s rate of fire, with wind-up [Fan-wiki].
  - In Steam screenshot screen_00 (2013 footage [Inference, strong]), a rock-skinned Riggs fires it: the coil flares and thin pink tracer streaks fly out [Observed].
  - In trailer frames from 34.5 to 36.2 s, the hits are **pink-white starbursts** (about 34.8, 35.1 and 35.6 s) and the target flashes cyan-white [Observed].
- **Impact / end result:**
  - The pale-yellow stars in screen_00 and at 35.8–36.1 s appear while the orange bear and the teal bear are fighting in melee. So they probably come from the melee, not the gun [Inference].
  - No status effect [Fan-wiki].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/v2/png/Photo_19-04-13_12_50_47_PM.png (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/v2/png/Photo_19-04-13_12_50_44_PM.png (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/s00_beebee_zoom.png, a crop of /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/steam_screens/screen_00.jpg (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/v2/tr/eh_sheet.jpg (trailer, 34.6–36.2 s) (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/irigg_gun_zoom.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-gaps-r2/crops/cm_m2_gun.png and cm_max_hud.png (Oct 2026 playtest, CmYil-JJdC0) (re-opened)
- **Depiction for shorts:** the coil flares magenta and a stream of thin pink tracers pops into pink-white starbursts on the target. Tiny electric bees in the stream are a [BBG News invention] built on the official "Electrically charged bees" line.
- **Confidence:** observed.

---

## PART B: BBG weapon pages missing from Category:BBG Weapons

## MuskIt (Primary, radiation shotgun; Engineer / Graham; BBG 2.12, Oct 2 2014; 2026 unconfirmed)
- **Official text:** "The musk of the Gyrnobal has been known to turn people into mutants, but most blow up." [Game text via wiki] ([MuskIt](https://battlebears.fandom.com/wiki/MuskIt)).
- **Look:**
  - A musket-style long gun [Observed, Musket.png, re-opened]: dark brown barrel with white bands and a gold ring, a salmon-pink breech block (#AF5649–#C06C5B, about #B4614F) with a grey emblem, and a yellow stock (#CEA218–#CFB318) with a black label.
  - It is held at hip level and foreshortened toward the camera. Its visible length is about **0.5× Graham's height**; its true length is [Unverified].
- **Firing:**
  - "used like a shotgun, dealing damage and irradiating enemies in a small cone. When fired, it shoots green stuff of what appears to look like bug spray" [Fan-wiki].
  - Damage 30, radiation 35.5–55.5, rate of fire 1.5 s, ammo 3 [Fan-wiki].
- **Projectile:** a short green spray cone [Fan-wiki].
- **Impact / end result:** the Irradiated status (Status Effects lists MuskIt as a source) [Fan-wiki]:
  - "a yellow circle will appear over the player's head and a noise from a Geiger counter will begin sounding". As exposure grows, "three portions of the circle will dissolve into the common radioactivity symbol".
  - At 100 radiation points the target explodes; the blast radius is 150–200 units.
  - The icon stages are the wiki files Hazard-0.png to Hazard-3.png [Fan-wiki].
  - **Steam trailer (2013 footage [Inference, strong]), same status from a different weapon:** a Graham weapon with yellow ring-wave muzzle effects, likely the Gamma Ray [Inference]. This is the Graham segment (about 7.25–10.5 s, Gold Digger [Inference, per the maps research]). It is in the storyboard of SkyVu's May 30 2013 trailer rfAyqVJrli4 (2013 12–13 s = Steam 7.95–8.95 s) [Observed, storyboard size]. graham.md has withdrawn its earlier "2018 or later" reading, because some 2013 fan captures already have the toon outlines (graham.addendum.md, Incidental findings 1). Why the trailer's Graham is outlined when Dec 2013 fan captures of its Instagraham skin are not stays [Unverified]. The icon is also in official 2026 media: SkyVu's Aug 16 2026 "Official Playtest Highlights" thumbnail (C7uFxvSZ10c, HUD build 3.0.0) shows the yellow disc with black radiation wedges, stacked with a Slowed Z, over the target of a gold Graham's yellow beam [Observed, per 2026.addendum.md; crop re-opened].
    - About 8.5 s: a **yellow disc with a black radiation trefoil** hovers over the target's head.
    - About 9.0 s: the target bursts apart with a white flash and a white hexagonal shockwave ring [Observed].
  - The same icon should appear on MuskIt hits [Inference: shared status visuals].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Musket.png ([File:Musket.jpg](https://battlebears.fandom.com/wiki/File:Musket.jpg)) (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/musket_zoom.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/v2/tr/t18_icon.png (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/v2/tr/graham_seq.jpg (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-r4/crops/c7u_icon.jpg (Aug 16 2026 highlights thumbnail, C7uFxvSZ10c) (re-opened)
- **Depiction for shorts:**
  - A green bug-spray puff.
  - A yellow disc over the target fills in to a black radiation trefoil while a Geiger counter ticks faster.
  - Then a white flash and a hexagonal shockwave ring, with the target popping into confetti instead of coming apart [BBG News invention: confetti].
- **Confidence:** partial. The gun's look and the status icon are observed; the spray itself is fan-wiki only.

## Bind Field, formerly Slow Field (Secondary, arc-thrown field; Engineer / Graham; BBG 2.6, Dec 20 2013; 2026 unconfirmed)
- **Official text:** "Make your opponents feel as old as you do. All enemies within the field stop and dream about bingo." [Game text via wiki] ([Bind Field](https://battlebears.fandom.com/wiki/Bind_Field)).
- **Rename:** "originally named the Slow Field, most likely renamed to prevent confusion with the Special ability Slow Motion Field" [Fan-wiki]. The 2.6 list says "Slow Field" [Fan-wiki]. The rename date is unknown.
- **Look:**
  - A **dark-brown ball with neon-green seams (#2AF944–#2BFA45) and purple knob studs (#841783–#871B82)** in a buckyball pattern, held in Graham's hand [Observed, Slowfield.png, re-opened].
  - About **0.3× Graham's height**: 0.33× in my measurement, 0.28× in the image check.
- **Firing:** "firing a prickly purple-green ball in an arc" [Fan-wiki].
- **Projectile:** the studded ball, lobbed [Fan-wiki; held look Observed].
- **Impact / end result:**
  - It "detonates and forms a medium-sized force field which slows all opponents caught in its radius by 75% for 3 seconds" and deals no damage [Fan-wiki].
  - Status Effects lists "Slow Field" under Slowed, shown by a yellow "Z" [Fan-wiki].
  - The field's colour is undocumented [Unverified].
- **Images viewed:** /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Slowfield.png ([File:Slowfield.png](https://battlebears.fandom.com/wiki/File:Slowfield.png)) (re-opened)
- **Depiction for shorts:** the ball lands and a dome pops up [BBG News invention: dome colour]. Enemies inside slow to a crawl under dozing yellow "Z"s, matching the official "bingo" joke.
- **Confidence:** partial.

## Traffic Light (Melee, Chub Scout / Wil; release version not on the wiki, image uploaded 2015-05-07; 2026 unconfirmed)
- **Official text:** "Why is there no yellow light you ask? Wil only travels in two modes. He stops and sometimes he has to go." [Game text via wiki] ([Traffic Light](https://battlebears.fandom.com/wiki/Traffic_Light)).
- **Stats:** 45 damage, +10% speed, 150,000 Joules [Fan-wiki].
- **Look:**
  - A **yellow pole (#FDD406–#FED100) with black bands**, topped by a spiky grey signal head with **only a red and a green lamp** [Observed, Trafficlight.png].
  - Wil swings it like a mace; it is about 0.8× his height.
  - In that shot he wears a red cowl and a grey bear-emblem shirt; the skin name is unknown.
- **Firing / projectile / impact:** melee; the hit look is undocumented [Unverified].
- **Images viewed:** /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Trafficlight.png ([File:Trafficlight.png](https://battlebears.fandom.com/wiki/File:Trafficlight.png))
- **Depiction for shorts:** the lamp flips red as he winds up, then green as he swings [BBG News invention]. The "no yellow" joke is the official text.
- **Confidence:** partial.

## Social Butterfly (BBG) (Primary, "Saboteur" type; Combat Tech / Saberi; BBG 2.53, Apr 28 2018; 2026 unconfirmed)
- **Official text:** none on the wiki stub.
- **Stats:** "Primary - Saboteur", damage 0, rate of fire 2 s, ammo 5, reload 5 s, gravity 1000 units, projectile 1000 u/s, duration 0.5 s, 40 Gas [Fan-wiki] ([Social Butterfly (BBG)](https://battlebears.fandom.com/wiki/Social_Butterfly_(BBG))). The gravity value suggests an arcing shot [Inference].
- **Look / projectile / impact:** no image and no effect description; all [Unverified]. The infobox image field is empty, and the only file on the page belongs to the stub template.
- **Images viewed:** none exist on the wiki.
- **Depiction for shorts:** do not depict it until a 2026 frame shows it.
- **Confidence:** unknown.

---

## PART C: "Shared" weapons

## Finding: no BBG weapon is shared between classes (all eras)
- No page carries two class categories [Fan-wiki]:
  - 188 of the 189 pages (the 185 category pages plus the 4 orphans) carry exactly one class tag;
  - Bounce Lazer carries none;
  - Dragon Slayzer (BBG)'s tag is "Graham";
  - 18 Huggable pages use "Huggable (class)".
- The 186 weapon links on the class pages resolve to 186 different pages [Fan-wiki; category scan].
- **Where the false overlap in `weapons_by_class.json` comes from** (A Salt Rifle, Heavy A Salt Rifle, Soaker, Spreadshot, Steamshot, B.E.A.R. Club and Krikkit Bat under Riggs and Huggable):
  - It comes only from the "Changelog" scroll box on the Heavy (BBG) and Huggable (BBG) pages.
  - That box is a copy of the Soldier list headed "Weapons (WIP)". It also lists "Bearzooka" and links Soldier skins such as "Grey Oliver" and "O.C.O." [Fan-wiki; Inference: copy-paste].
- **The Heavy page's real weapon lists** [Fan-wiki]:
  - Primaries: Beebeegun, Provolowned, Field Medic, Big Iron, Electric Honey, Zombee Gun, Bounce Lazer, Flame Thrower.
  - Secondaries: Hivey League, Plasma Orb, Mother of Nature, Freeze Blast, Buzz Kill, Sucker Punch.
  - Melees: Barbed Gloves, Catastophe, Blood Spurt, Sword and Stone, Huggable Gloves, Zombee Gloves.
- **Name-sharing look-alikes, which are not shared weapons:**
  - **Minigun (Soldier):** a primary, BBG 2.11, Aug 27 2014; 45 Gas, damage 3, rate of fire 0.075 s, 80 ammo, −10% Speed, +20% Health [Fan-wiki]. Official text: "Mini refers to your enemies after its done with them." [Game text via wiki]. Look: a dark gunmetal four-barrel minigun held at the hip [Observed, Mini.png].
  - **Minigun (Combat Tech):** a Saberi secondary mounted on her "third arm": "She already had built herself a third arm to hold more firepower. Why not add a minigun to it for good measure?" [Game text via wiki]. It deploys for 10 s and fires low-damage hitscan beams alongside her primary [Fan-wiki]. The wiki's Missiles page says her missile launchers "emerge from the right side of the Combat Tech's backpack" [Fan-wiki].
  - **Bearzooka** (Soldier secondary) versus **Twin Bearzookas** (Demo primary): see Part E.
  - **The 2017 fidget-spinner trio** (Hazard Toy, Fidget Boomer, Spin Baby Spin) shares a concept, not a weapon: see Part G.
  - **Huggable Gloves:** a Heavy melee, "one of its original three melee weapons" [Fan-wiki]. That the name refers to the Huggable creatures is [Inference].
- **Confidence:** documented.

## Specials (all 11 classes; BBR → BBG; "10 SPECIAL EQUIPMENT" in 2026)
- **Official text:**
  - **Steam 2026:** "Grab your A Salt Rifle, Bearzooka and those Turkish SW Boots" and "10 SPECIAL EQUIPMENT" [Canon] ([Steam](https://store.steampowered.com/app/4408320)).
  - **Wiki:** "All characters are able to use all Specials. If you purchase a Special for one class, you don't have to buy it for another class." [Fan-wiki] ([Specials](https://battlebears.fandom.com/wiki/Specials)).
- **Per Special:**
  - The visuals come from the in-game description diagrams: 2D comic illustrations on a dark grid with a green glow outline [Observed].
  - Quotes are [Game text via wiki]; mechanics are [Fan-wiki]. Era is BBR/BBG; only the count and the SW Boots are confirmed for 2026.

| Special | Official text | Observed diagram | Effect visuals |
|---|---|---|---|
| Turkish SW Boots | "You want to jump? These allow it!" | Oliver mid-leap in red-and-black boots with white jet puffs | Big jump, usable mid-air, 4.5 s cooldown |
| Tesla Shield | "Detonates enemy projectiles on impact." | Orange-red wireframe geodesic cage of glowing nodes; a red rocket bounces off | "gigantic orb of red light"; does not block bullets |
| Slow Motion Field | "Slows down all nearby enemies for a limited time." | Astoria with a snail and yellow zig-zags at her feet | Yellow circle around the user; slowed enemies show a yellow "Z" |
| Iron Curtain | "Prevents death from coming in... but also from going out! Use Tillman's missiles to fire over the barrier while gaining protection from the front!" | Slanted green armoured wall with yellow lights in front of Oliver; a rocket hits it | Blocks frontal bullets and projectiles for 15 s (15 s cooldown); explosives stop but still blast; shotguns and the Demo's vertical secondaries are unaffected |
| Caffeine Injection | "Grants the user brief super speed!" | Wil sprinting with a coffee cup and red motion blur | Coffee-mug icon overhead (white mug with steam); white dust trail; 10 s |
| Healing Tent | "Activating the healing tent prevents you from moving but gives you health…" | Beige canvas tent with a green cross on grass (image uploaded 2021-12-06) | Beeping, "Zzzzzzz" signs. The cross was red until 2.53.5, when it "changed from red to green in order to avoid trouble with the Geneva conventions" |
| Propbearganda | "Increases all nearby teammates damage by 25%…" | Oliver with a loudspeaker mast blasting magenta; an ally with a purple fist icon | Speakers rise from the back playing the Bearbershop Quartet tune; purple fist icon |
| Cloaking | "Become invisible!…" | Translucent green outline of a big bear | Transparency; flickers when hit |
| Sixth Sense Goggles | "Discloses all enemy positions - even behind walls!…" | Oliver in purple and yellow goggles; red and blue outlines behind a wall | Team-coloured brackets |
| Flawless Disguise | "Neither team will be able to see who you are, trust no one!" | A cardboard box marked "THE ORANGE" over a crouching bear | Friend and foe hidden; blocks lock-ons |

- **Extra observed icon:** the coffee mug also appears as the equipped-Special button on the HUD in the Aug 2013 Bouncing Betty screenshot CRAZY_DEMO_LAND.jpg [Observed].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/specials1.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/specials2.png
  - These are built from /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png_sp/*.png (the wiki files TurkishSWBoots.jpg, Tesla_sheild.png, SlowMotionField.jpg, IronCurtain.jpg, CaffeineInjection.jpg, NewHealingTent.jpeg, Propbearganda.png, Cloaking.png, Sixth_sense_goggles.png, FlawlessDisguise.jpg, Special.jpg).
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/v2/sp_a.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/v2/sp_b.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/v2/png/Caffeine_Injection_Icon.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/png/CRAZY_DEMO_LAND.png (re-opened)
- **Depiction for shorts:**
  - Any bear can use any Special, so these make good cross-cast gags (Riggs in the cardboard box, Wil on caffeine).
  - Keep the icons: coffee mug, yellow Z, purple fist.
  - Use a **red** Healing Tent cross for a 2013–2018 setting and green for late-era or 2026 [Fan-wiki; 2026 colour Inference].
- **Confidence:** documented (text), observed (diagram art). The 2026 roster beyond the count and the SW Boots is unconfirmed.

---

## PART D: Retextures and variants

## Sci-Fi ASR (Primary, automatic; Soldier / Oliver; BBR v1.3.1, second week, summer 2012; in BBG; 2026 unconfirmed)
- **Official text:** "In the future, lasers will be the seasoning of choice among the elite while the common rabble shall continue to put analog salt-dust into their primitive bodies." [Game text via wiki] ([Sci-Fi ASR](https://battlebears.fandom.com/wiki/Sci-Fi_ASR)).
- **Status:**
  - "a retexture of the standard A Salt Rifle". 105,000 Joules, level 10, damage 5, rate of fire 0.15 s, +5% speed [Fan-wiki].
  - **Ammo conflict:** the infobox says 25 ("the lowest ammo of all automatics"), but the 2.6 notes say the clip went from 30 to 20 and damage from 5 to 5.5 [Fan-wiki].
  - It was a 2012 Forum Appreciation freebie [Fan-wiki].
  - It was sold in the "Sci-fi stimulus" bundle (Sci-Fi ASR, Sci-Fi HASR and the Skinless skin) for 285,000 Joules, Dec 20–31 2012 [Fan-wiki, Bundle Deals].
- **Look:**
  - **Base A Salt Rifle, for comparison** [Observed, Oliver3d.png, re-opened; concept "AR3" in ASRconcept.png]:
    - pale sage green (#93BBA8–#B4DEC2) with dusty salmon-rose panels (#7C5B5C shadow, about #CB9A90 lit);
    - a **clear salt-shaker canister** (#FDFFFF) on a ribbed hose on top;
    - a slate grip (#536270);
    - about **0.75× Oliver's height**.
  - **The Sci-Fi ASR** is **chrome and gunmetal** (#4D4A54 to #E0E0E0) [Observed, Oliver_SciFi_Asalt.png, re-opened; shop icon in Sci-Fi_HASR.png]:
    - the salt shaker becomes a hexagonal energy cell with **diagonal stripes graded red, orange and yellow** (#EF1712, #F85E17, #FCC827) and a **glowing orange hex cap** (#FC771B–#FEA11F);
    - **five dark-navy vent holes (three over two)** on the side;
    - a dark-teal blade tip (#0E4446–#195457).
- **Firing / projectile:**
  - Automatic [Fan-wiki]. The "lasers" exist only in the joke text [Game text via wiki].
  - Dban1's fan demo "[Oliver]: Primary - Sci-Fi ASR" (BBR, April 2013) shows, in its hq2 thumbnail [Observed, re-opened]:
    - a yellow-green-white flash at the target;
    - a HUD clip of "10 / 30", which fits the pre-2.6 clip of 30.
  - The pink beam in that frame comes from another player.
  - The tracer look is [Unverified].
- **Impact / end result:** bullet damage, no status effect [Fan-wiki].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/asr_group.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/asr_zoom.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/asr_concepts.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Oliver_SciFi_Asalt.png (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Oliver3d.png (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Sci-Fi_HASR.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/v2/sfasr_dots.png (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/web/P5EsIBxZS-k_hq2.jpg (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/v2/p5_hq2_zoom.png (re-opened)
- **Depiction for shorts:** Oliver's rifle in chrome, with the salt shaker replaced by a glowing red-to-yellow striped hex cell. If he fires it, use orange-yellow energy tracers [BBG News invention].
- **Confidence:** partial.

## Sci-Fi HASR (Primary, automatic; Soldier / Oliver; BBR v1.3.1, second week; in BBG; 2026 unconfirmed)
- **Official text:** "Look no further for reasons for people to get out of your way, you're holding the only one you need. Should a chump still refuse to step aside, this puppy has a convenient little button to change their mind." [Game text via wiki].
- **Status:**
  - "a retexture of the standard Heavy A Salt Rifle". 60 Gas, level 15, damage 7, rate of fire 0.125 s, ammo 50, reload 5 s [Fan-wiki].
  - Speed −10% per the infobox; the 2.6 notes changed it from −10 to −15 [Fan-wiki].
  - Sold in the Dec 2012 "Sci-fi stimulus" bundle [Fan-wiki].
- **Look:**
  - **Base HASR:** an AK-style rifle in the same sage-and-salmon scheme, with a **large ring-shaped drum** around the grip [Observed; concept "AR5"].
  - **The Sci-Fi version** is silver-grey with a dark gunmetal ring [Observed, Photo_19-04-13_12_01_58_PM.png (BBR, April 2013), Sci-Fi_HASR.png].
  - The Oct 2012 shop shot shows Oliver in the gore-styled "Skinless" skin; **do not use that skin in shorts**.
- **Firing / projectile / impact:**
  - Automatic bullets, no status effect [Fan-wiki].
  - Dban1's demo "[Oliver]: Primary - Sci-Fi HASR" (BBR, April 2013) shows a HUD of "46 / 50", then "0 / 50" with RELOAD, matching the wiki's 50 [Observed, re-opened].
  - The tracer look is [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Photo_19-04-13_12_01_58_PM.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Photo_19-04-13_12_02_04_PM.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Sci-Fi_HASR.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/web/ICIsRtcYckY_strip.jpg (re-opened)
- **Depiction for shorts:** a chrome HASR with a black drum ring, and fast muzzle flashes [BBG News invention].
- **Confidence:** partial.

---

## PART E: Cross-game carryovers

## Bearzooka (Secondary, explosive; Soldier / Oliver default; franchise weapon since BB Zombies; in BBR and BBG; in the Steam trailer, 2013 footage [Inference, strong]; named on the 2026 Steam page and seen in SkyVu's Jul 6 2026 "Classic Oliver" short)
- **Official text:**
  - "The basic weapon of any Soldier. Does a good amount of damage, with a decent area of effect (AOE). Useful for all situations." [Game text via wiki] ([Bearzooka (BBG)](https://battlebears.fandom.com/wiki/Bearzooka_(BBG))).
  - "Grab your A Salt Rifle, Bearzooka…" [Canon, Steam 2026].
  - "his powerful 'Bearzooka' Ultimate which deals massive damage and destroys obstacles" [Canon, BBH only].
- **The wiki on colour:** "In BBG and BB0, it is a rocket launcher with red and orange lines. In BBZ and BB-1 it is just a dark green rocket launcher." [Fan-wiki] ([Bearzooka](https://battlebears.fandom.com/wiki/Bearzooka)).
- **Look (resolved):**
  - **Body:** a **coral-red tube**, #A54447–#A34842 in the BBR April 2013 shop shot and #D05655–#CE544F under Steam-trailer lighting (2013 footage [Inference, strong]) [Observed]. On SkyVu's darkened Jul 6 2026 "Classic Oliver" card it reads ≈ #A2565A [Observed, per 2026.addendum.md; crop re-opened]. Length about 0.8× Oliver.
  - **Windows:** a row of **glowing orange window panels** (#EB7921–#FEA53C). They are **rectangular** on the BBR April 2013 model, **pointed, chevron-like hex panels** in the Steam trailer footage, and chevrons in the concept image. The 2026 "Classic Oliver" card also shows pointed panels. Grey metal bands and a black bore [Observed].
  - **Muzzle end:** it flares. It is a **grey-and-red checkered cone** in the Steam trailer footage (pointing at the target at about 4.4 s), on the 2026 "Classic Oliver" card and in the concept; the BBR April 2013 shop model shows only faint grey mottling there [Observed].
  - **How it is carried:** on the right shoulder, in the 2013 shop shot, in Dban1's demo "[Oliver]:Secondary - Bearzooka" (BBR, April 2013), in the Steam trailer (2013 footage [Inference, strong]) and on the 2026 "Classic Oliver" card [Observed].
  - **Concept image:** Bearzooka_Concept.png (captioned "Bearzooka concepts") is a crop of Soldier_Weapon.png, uploaded by a wiki user in Nov 2012 with no watermark. SkyVu provenance is [Inference].
  - **Steam trailer, 3.89–4.59 s** (t_0009 is really 4.22 s; 2013 footage [Inference, strong]: the same shot is at t=8 s in the storyboard of SkyVu's May 30 2013 trailer rfAyqVJrli4 [Observed, low-res]): the carrier is a **green-skinned** bear with a blue bandana mask, a waist belt of gold bullets with blue spikes, and a lavender-and-blue slab on its back [Observed]. The skin is unidentified. The Bearzooka is a Soldier weapon, so this is probably an Oliver skin [Inference].
  - **Green launchers in other contexts:**
    - The **BB: Zombies Bearzooka** (Bear.jpg, "Bearzooka in BBZ") is a dark-green tube stencilled "BEARZOOKA" with an arrow and yellow-and-black hazard stripes at the muzzle [Observed]. This is almost certainly where oliver.md's "green, hazard-striped tube" came from [Inference].
    - **Tillman's Twin Bearzookas** (Demo primary, BBG 2.17, Mar 8 2015) are two **yellow-olive tubes** (#71793C–#ABB157, median #8A9246) with dashed seams and **octagonal black muzzles with silver-grey rims**, one over each shoulder [Observed, Ohmagawdyas.png, re-opened]. Stats: explosives 15–25, 3 ammo, 750 u/s, −10% speed [Fan-wiki].
- **Firing:**
  - One rocket per shot; rate of fire 1.5 s, reload 2.5 s, projectile 1,000 u/s, explosives 40–60, AoE max-damage range 125 units and min-damage range 250 units [Fan-wiki].
  - **Ammo conflict:** the infobox says "Ammo 1"; the prose says it "has two shots without additional ammo" [Fan-wiki]. The April 2013 demo HUD reads "1 / 1", then "0 / 1" with RELOAD [Observed, re-opened]. Unused "incoming stats" listed 3 ammo [Fan-wiki].
- **Projectile:** the Steam trailer SkyVu put on the 2026 Steam page shows one rocket in flight from 1.92 s to 3.05 s [Observed]. The footage is from 2013 [Inference, strong]: the trailer's class cards are pixel-identical to SkyVu's May 30 2013 trailer rfAyqVJrli4, and this shot is in that trailer's storyboard too (t=6–7 s) [Observed, storyboard size]. It does not show the 2026 build. It is fired by a distant green-furred, blue-team Soldier holding a coral tube; the launch is a white smoke burst with an orange core. The rocket has a grey stepped hex nose, glowing yellow/orange checker panels in chevron bands, grey collars and a flared skirt, a maroon tail with pink-red square lights, and spiky orange-yellow flame shards, with white puffs trailing it at range. It flies toward and past the camera, under the airborne B-1000, and leaves the frame without detonating. That it is the Bearzooka's rocket is [Inference, high]: the same green character carries the coral Bearzooka at 3.89–4.59 s. (See shared.addendum.md, round 3, "Bearzooka (BBG) rocket", for the frame-by-frame trace and the reasons for the attribution.)
- **Impact / end result:**
  - An explosion with splash. "The user is very prone to suicide while using the Bearzooka." [Fan-wiki]
  - **Seen only in 2014–15 fan footage** (YouTube storyboard frames, low-res; per oliver.addendum.md, Bearzooka, Impact; crops opened in the later Oct 18 edit) [Observed]:
    - "Battle Bears Gold- Bearzooka Oliver Gameplay!" (7WSXU2LaxYo, Hammad Shahid, Mar 10 2014), t=56 s: a big faceted yellow polygon blast (≈ #F8EB6F) with a grey smoke puff (≈ #9C9B90) at its centre.
    - "Battle Bears Gold | 2.21 | Bearzooka Gameplay" (0ZbJ0-Za5Ws, SW, Jul 25 2015), t=38 s, HUD 0: a faceted yellow blast (≈ #F7E04F, bright #FFF259) beside a billowing dark-grey smoke cloud (≈ #5E5B63).
    - Crediting both blasts to the Bearzooka is [Inference, high]: both titles are Bearzooka gameplay, and the 2015 uploader's listed primary (Urine Trouble) does not explode.
  - **Not seen:** no official SkyVu media shows the blast. The Steam trailer rocket (2013 footage [Inference, strong]) leaves the frame at 3.05 s without detonating [Observed]. No 2026 frame shows a Bearzooka blast [Unverified for 2026]; the pale-yellow faceted blasts in 2026 fan frames are unattributed (2026.addendum.md, Bearzooka).
  - **The trailer is not evidence for the blast.** At 4.4–5.2 s on the t_ grid no rocket leaves the tube; on exact frames the cyan slash starts at 4.59 s (n137) [Observed: bz_shot_sheet.jpg]. The yellow-white wipe and the streak backdrop belong to B-1000's entrance: he slashes with a cyan blade, the green bear breaks apart, and the shot cuts to the "B-1000 / ASSAULT" title card [Observed].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Photo_19-04-13_12_02_26_PM.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/v2/bz2013_zoom.png (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Bearzooka_Concept.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/png/Bear.png ([File:Bear.jpg](https://battlebears.fandom.com/wiki/File:Bear.jpg)) (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Ohmagawdyas.png (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/v2/twin_muzzle.png (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/trailer/t_0009.jpg (4.22 s; nominally 4.0 s)
  - Oct 18 edit, re-opened from the round-3 trace (/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/shared-r3/): sheets/rocket_track.jpg, sheets/green_launch.jpg, sheets/green45_71.jpg, sheets/s74_85.jpg and tr/f_0088.png (the rocket, 1.92–3.05 s)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/shared_trailer_rule/b1000_shot.jpg (Steam t_0004–t_0007 against the 2013 storyboard's t=5–8 s)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/shared_r3_chk/bz_shot_sheet.jpg (exact frames n116–n150, 3.89–5.02 s)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/v2/tr/bz_full6.jpg (3.9–5.2 s) (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/v2/tr/bz_full4.jpg (4.4–4.7 s) (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/web/AZt_huguhzc_strip.jpg (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-r4/crops/byri_zooka.jpg (SkyVu's Jul 6 2026 "Classic Oliver" short) and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/oliver/gaps_r2/z/show_bear500.jpg (2026 playtest loadout render)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/shared_trailer_rule/steam_vs_2013_sb.jpg (Steam trailer frames against the rfAyqVJrli4 storyboard)
  - Later Oct 18 edit (the blast): /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/oliver/gaps_r2/z/bz7W_a.jpg (7WSXU2LaxYo, t=56 s) and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/oliver/gaps_r2/z/bz0Z_38.jpg (0ZbJ0-Za5Ws, t=36–42 s); metadata /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/oliver/gaps_r2/inv/inv_7WSXU2LaxYo.json and inv_0ZbJ0-Za5Ws.json
- **Depiction for shorts:**
  - A coral-red tube with glowing orange panels on Oliver's right shoulder.
  - The rocket follows the Steam trailer's 2013 footage: grey stepped hex nose, glowing yellow-orange checker panels, maroon tail, spiky orange flame shards and white puffs [Observed; its Bearzooka link is Inference, high]. It never detonates on screen there.
  - The blast follows the 2014–15 fan footage: a faceted yellow polygon blast with a grey or dark-grey smoke ball [Observed, low-res; its Bearzooka link is Inference, high]. Its 2026 look is unseen. Comic soot when it backfires is a [BBG News invention] (a gag built on the wiki's "prone to suicide" line).
  - Never draw it green, except for Tillman's twin tubes or a BB: Zombies / BB-1 flashback.
- **Confidence:** observed (look; the rocket, in 2013 footage, with its Bearzooka link an Inference, high); partial (firing; impact, seen only in low-res 2014–15 fan footage with its Bearzooka link an Inference, high, and in no official or 2026 frame).

## BBR-era weapons still in BBG (BBR Oct 2011–Apr 2013 → BBG relaunch May 24 2013)
Looks belong in the class dossiers. Dates are from the wiki's version pages and weapon pages [Fan-wiki], with the gaps noted.
- **BBR 1.0, Oct 8 2011.**
  - Only two wiki tables actually say "BBR v1.0": Soldier (BBG)/Weapons for the Soldier set (A Salt Rifle, Heavy A Salt Rifle, Soaker; Bearzooka, Spreadshot, TNT Launcher; B.E.A.R. Club, Krikkit Bat, Queensbury Rules) and Heavy (BBG)/Weapons for Electric Honey.
  - The other Heavy items (Beebeegun, Zombee Gun; Hivey League, Buzz Kill; Huggable Gloves, Zombee Gloves, Barbed Gloves) and the Demo melees (Double Hug, Good Morning) are described as "one of the original three…". Dating them to BBR 1.0 is [Inference].
  - The BBR Version 1.0 page lists only characters and maps.
- **BBR 1.1 (Nov 23 2011):** the Sniper arrives with the Viperifle. The Tomahawk "was the only secondary for the Sniper before v1.3" [Fan-wiki], so it predates 1.3; that it arrived with the Sniper is [Inference].
- **BBR 1.3 (May 3 2012):** the Chub Scout, with Boomstick, Balance Beam, Batterito, EZ Chee-Z, Bow and Arrow; and the Sniper's Capital Pains and Daydreamer [Fan-wiki, BBR Version 1.3 page].
  - **Doomstick conflict:** its own page says "It came out in v.1.3", while the BBR Version 1.3.1 page lists it among the 1.3.1 weapons.
- **BBR 1.3.1** (from June 28 2012, over four weeks): Doomstick, Killdoba, Steamshot, Plasma Orb, Provolowned, **Catastrophe**, Disciplinarian, Mamba's Boy, Eagle Standard, Golden Dragon, **Sci-Fi ASR**, Punk Bands, **Sci-Fi HASR**, Light Matter, Phat Man, Urine Trouble, Whipped Pain, Field Medic, Rockette Launcher, Presidentures, Beaver Fever.
- **BBR 1.3.2 (Aug 24 2012):** Mother of Nature, Big Iron, Blood Spurt, Sake Bomb, O.C.O. Gauntlet, Kumakiri. Bundle Deals were added ("Bundle Deals will be available in selected periods").
- **BBR 1.4 (Nov 28 2012):** the Engineer, with Power Glove, Turret, Wrench, Gamma Ray and others.
- **BBR 1.4.3 (Apr 15 2013):** Dead Eye, Fairy's Dust (the 1.4.3.1 text says "Fairy's Sparkle"), Static Shuffle, Señor Potato Cannon (now "Senor Potato"), Sole's Bane, Gernobyl.

**Story-game names reused in BBG** [Fan-wiki]:
- Bearzooka (BBZ, BB-1, BB0)
- Spreadshot (BB-1)
- Crossbow 2.0 (named after BBZ's Unicorn Crossbow)
- Arrow: the wiki says it "is probably the one that was stuck in Wil's leg in Battle Bears -1"
- Batterito (BLAST food)
- Dragon Slayzer (BB Overclock; added to BBG in 2.51)
- Twin Bearzookas (Tillman in BB Zero)

## BBG → BBH (2024) names
These names come from SkyVu's own BBH character page [Canon, battlebears.com/pages/characters]. BBH behaviour is **not** BBG behaviour.
- **BBH names that match a BBG weapon page** [BBG pages: Fan-wiki]:
  - Oliver: Acreambo Pistols, and the Bearzooka as his Ultimate.
  - Huggy: So Fly.
  - Riggs: "Beebee gun" (BBG: Beebeegun).
  - Wil: Boomstick.
  - Tillman: Blast-o-Mole.
  - Botch: Doom Cloud.
  - Sanchez: Adrenaline Gun and Speed Field.
- **BBH-only names (no BBG page):**
  - Wil: "Sarcastic Air Strike".
  - Tillman: "Firework Flurry" (BBG has "Fireworks").
  - Graham: "Photon Refractor" and "Turret Summon" (BBG has "Turret").
  - Saberi: "Huggable Splicer" and "Healing Turret".
  - Botch: "Doom Star".
- **Do not port BBH mechanics into BBG shorts** [Inference]. Examples: the four staggered Adrenaline Gun shots, and the BBH Beebee gun's "burst of shells".

---

## PART F: Removed and reworked weapons

| Item | Owner | Era in | Change | When | Source |
|---|---|---|---|---|---|
| Bind Gun → Adrenaline Gun | Arbiter | BBG 2.6 (Dec 20 2013) | Slowing beam became a speeding beam; renamed | Wiki stats edited 2021-06-18 UTC ("19th of June 2021"); page moved 2021-07-17 | [Fan-wiki] |
| Slow Field → Bind Field | Engineer | 2.6 | Renamed | Unknown | [Fan-wiki] |
| Bouncing Betty | Demo | 2.2 (Aug 21 2013) | "removed later" | After 2.31 (Mar 8 2018), when it was still being rebalanced; the page was in the past tense by 2020-05-22 | [Fan-wiki; window is Inference] |
| Greased Lightning | Arbiter | 2.9 (May 8 2014; "New: Greased Lightning Primary / 75 Gas") | "THIS WEAPON IS REMOVED!" | Note added 2020-11-10; removal date unknown | [Fan-wiki] |
| Last Resort | Assault (default secondary) | BBG 1.0 (2013) | "THIS WEAPON IS REMOVED" | Note on the page by 2020-11-09; the Assault (BBG) page still lists it | [Fan-wiki] |
| Capital Pains (red mode) | Sniper | — | "Red Capital Pains is currently removed" | Unknown | [Fan-wiki] |
| Hivey League stat modifier | Heavy | — | Speed penalty removed | v2.6 | [Fan-wiki] |
| Equipment | All | — | "All +1 Equipment has been removed except Speed +1"; "Equipment Slot 2 has been removed"; "Speed 2 Equipment has been moved to default movement" | BBG 3.0, Nov 15 2021 | [Fan-wiki, Updates] |

Notes:
- **Scale for this part:** B-1000 ~1.5×, Sanchez 1.0×, Tillman ~0.9× [BBG News invention, README line 54].
- None of these removals appears in any official 2026 text I could read. Whether these weapons return in 2026 is [Unverified].

## Bouncing Betty (Primary, explosive; Demo / Tillman; BBG 2.2, Aug 21 2013; removed between 2018 and 2020)
- **Official text:** "The master of explosions has a lovely friend named Betty. Tillman and her go way back, bouncing around exploding everywhere. Oh, to be young and explosively in love!" [Game text via wiki].
- **Look:**
  - A big shoulder-held **white and silver launcher with a wide black bore**, red and black fittings and a round red crosshair decal on the side, braced on Tillman's shoulder. The bore is about head-sized [Observed, Bouncing_Betty.png].
  - **Concept sheet:** the SkyVu-watermarked sheet with the BBG logo (Bouncing_Betty_Concept.jpg, uploaded 2013-08-10) shows the launcher's breech in six colour variants [Observed, re-opened]:
    - bodies in green, grey, black and white;
    - a "PUSH" label with a down arrow on a red, yellow or blue stripe;
    - a grinning cartoon bomb-face decal and a round button.
- **Firing / projectile:**
  - It "lobbed a large, black bomb with a lit fuse" [Fan-wiki].
  - **CRAZY_DEMO_LAND.jpg** (uploaded 2013-08-24, captioned "Bouncing Betty projectiles") shows [Observed, re-opened]:
    - several **round black cartoon bombs** in the air at once;
    - each with a sparking yellow-white fuse and a small red face mark;
    - dotted pale pink-white puffs trailing along a bouncing arc;
    - a HUD of "0 / 3".
  - Their size relative to a bear cannot be measured from that shot.
- **Stats:**
  - Infobox: explosives **16–32**, AoE 125/250, rate of fire 1.5 s, ammo 3, reload 4 s, 1,000 u/s, 300,000 Joules. The prose says 30–50 damage [Fan-wiki].
  - "After the change in 2.31, the cool down was decreased from 1.5 to 1 second, and the ammo was increased to 3" [Fan-wiki].
- **Impact:** each surface contact makes an explosion, and the bomb bounces three times before detonating on the third bounce. It "could not directly hit players" [Fan-wiki].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Bouncing_Betty.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/removed_group.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/png/CRAZY_DEMO_LAND.png (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/v2/betty_bombs.png (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/png/Bouncing_Betty_Concept.png (re-opened)
- **Depiction for shorts:** round black cartoon bombs with fizzing fuses boing-boing-boom down a corridor, trailing pale pink puffs [Observed], ending in three puffs of smoke and confetti [BBG News invention: confetti]. Mark the short "classic 2013–2018".
- **Confidence:** partial (look and projectile observed; blast look unknown).

## Greased Lightning (Primary, automatic; Arbiter / Sanchez; BBG 2.9, May 8 2014; removed)
- **Official text:** "It's automatic! It's systematic! Hydromatic!? Why it's Greased Lightning!!??" [Game text via wiki].
- **Look:** a **glossy red rifle (#940505–#990608) with white lightning-crack decals**, a grey toothed top rail and a tan cylinder at the rear [Observed, Greased_Lightning.png].
- **Firing / projectile:** "fires red-violetish lasers at a rapid rate"; rate of fire 0.13 s, ammo 30, −5% Speed, 75 Gas [Fan-wiki].
- **Impact:** damage only. "The weapon has a slight AOE, unfortunately that AOE deals no damage." [Fan-wiki]
- **Images viewed:** /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Greased_Lightning.png
- **Depiction for shorts:** rapid red-violet laser darts. Leave out the song lyrics and music [Inference: rights].
- **Confidence:** partial.

## Last Resort (Secondary, self-destruct; Assault / B-1000 default; BBG 1.0, 2013; removed, date unknown)
- **Official text:** "Winning takes sacrifice, and in this case that means blowing yourself up. Press and hold the fire button initiate a self-destruct sequence, wait 3 seconds and then boom!" [Game text via wiki].
- **Status:** "Last Resort was the default secondary weapon for the Assault class" and "THIS WEAPON IS REMOVED" [Fan-wiki]. The Assault (BBG) page still lists it under Secondary [Fan-wiki].
- **Look:**
  - The wiki image shows B-1000 from behind: maroon armour, an orange and white gun-arm and a grey axe blade with orange teeth. On his back is an **orange-gold (#A55409–#E89901) and black pack of two hexagonal modules with circular vents** [Observed, Last_Resort.png, re-opened].
  - SkyVu's own concept sheet "ENERGY BARRIER & ENERGY OVERFLOW" (BBG logo, uploaded 2013-09-24) shows nearly identical orange, white and black modules with circular vents [Observed, re-opened].
  - So the pack may be B-1000's standard back hardware or those items. Treating it as the Last Resort device is [Inference] at best.
- **Firing / impact:** hold fire for about 3 s, then self-explode for 200–400 damage, "the highest damage of any explosive weapon" [Fan-wiki].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Last_Resort.png (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/v2/png/B1000_weapons2-3-787x1024.png (re-opened)
- **Depiction for shorts:** B-1000 holds the trigger, a beeping countdown light flashes on his chest, then a giant cartoon "BOOM" cloud, and his robot head pops out of the smoke with a cheerful error beep [BBG News invention]. Do not animate the back pack as the bomb. No gore.
- **Confidence:** partial.

---

## PART G: Seasonal, promotional and limited drops
- The wiki marks **no BBG weapon as limited-time**. The items below were themed drops or promotions [Fan-wiki].
- **2026 official text:** the only limited item is a skin: "Sign Up & Wishlist for an Iconic Zombie Skin!" [Canon] ([play.battlebears.com](https://play.battlebears.com/)).
- **Steam playtest posts:** they list no weapon changes. The first says "There won't be any new features in this build" [Canon] ([Steam news](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=4408320)).
- **2026 playtest menu:** the Sept 2026 playtest thumbnail shows a "BUNDLE DEALS" banner, so a bundle shop exists in that build [Observed]; its contents are unknown.

**Promotions and bundles:**
- **BBR 1.3.1 Forum Appreciation (2012):** "Players who joined the forums could get the weapons and skins of v1.3.1 free and earlier than other people" [Fan-wiki].
- **The "BBR 1.3.1 and BEYOND!" graphic:** a red, white and blue starburst with a bald eagle above a pile of 1.3.1 weapons [Observed, BBRWEAPONS.png]:
  - the Eagle Standard;
  - the Presidentures dentures;
  - the Golden Dragon;
  - Mamba's Boy (a snake);
  - the Catastrophe cat head;
  - a Phat Man radiation bomb.
  - A wiki user uploaded it 2012-11-07; official provenance and a Fourth-of-July theme are [Inference].
- **Bundle Deals:** added in BBR 1.3.2, "available in selected periods" [Fan-wiki]. Examples:
  - Oct 20–22 2012;
  - **"Sci-fi stimulus"**: Sci-Fi ASR, Sci-Fi HASR and Skinless, 285,000 Joules, Dec 20–31 2012;
  - several Halloween bundles in Oct 2012 and Oct 2013;
  - the undated **"SANDKING" bundle** (Sandchez, Toxic Plague, Toxic Rifle, ClubCobra; 350,000 Joules; art uploaded 2015-06-01) [Fan-wiki; bundle name Observed on the art].

## Winter drops: S'no Matter (Demo primary, 2.15, Dec 20 2014); Let It Cold (Demo secondary) and Snowtato Launcher (Chub Scout primary), both 2.26, Jan 17 2017, with a winter No Bear's Land
- **Official text** (all [Game text via wiki]):
  - S'no Matter: "It S'no Matter how fast you can move, I can just freeze you! "
  - Let It Cold: "Your enemies won't have a skull or bones after being hit with ice cold rockets! These rockets explode on impact and freezes the opponent for a small duration"
  - Snowtato: "A makeshift potato launcher convertor to weapon of frosty devastation. Shoot snowballs that explode and turn them into flakes!"
- **Look:**
  - **S'no Matter, in game:** Tillman holds a two-handed device that renders only as a blown-out cyan-white glow (#5FC4DB → #9BFEFD; core #F3FDFD / #B0F7F7) [Observed].
  - **S'no Matter, concept:** "Tillmans S'no Matter" (Snomatterconcpetar.jpg, uploaded 2015-03-29; SkyVu provenance unverified) shows two variants of a launcher wrapped in red tartan cloth, with silver and grey bands, a white snowflake fin on top and cyan hexagonal gem studs [Observed, re-opened].
  - **Let It Cold:** two black shoulder racks, each with **two blue rockets (#2062DA–#3068D7)** carrying grinning green cartoon-face decals, on striped sticks with icy tips [Observed].
  - **Snowtato Launcher:** a silver barrel, a lavender-blue body and fins (#6D7DA9; range #7684A7–#98A7D1) and a white snow-heap hopper, held by Wil [Observed]. "When this weapon first came out, it had no weapon model that could be seen in the weapon equip menu" [Fan-wiki].
- **Projectile and impact** [Fan-wiki]:
  - **S'no Matter:** a slow grey projectile at 800 u/s, explosives 25–40, ammo 3, −10% movement speed. It freezes everyone in the blast for 2 s, teammates included.
  - **Let It Cold:** missiles "rain down" on enemies; explosives 20–40, ammo 4, freeze 3 s.
  - **Snowtato:** exploding snowballs, explosives 35–65, ammo 6. Lingering snow blocks explosives.
  - **Frozen-target look:** only the S'no Matter concept shows it. A lobbed arc lands as a jagged cyan-and-white ice mound encasing the target's lower body [Observed; provenance unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/winter_group.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/v2/winter.jpg (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Letitcold.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Snowtato.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Snomatter.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/v2/png/Snomatterconcpetar.png (re-opened)
- **Depiction for shorts:** targets are caught in a jagged cyan-and-white ice mound up to the waist, as in the concept, with chattering teeth [BBG News invention: teeth].
- **Confidence:** partial.

## Summer 2017 fidget trio: Fidget Boomer (Sniper primary), Spin Baby Spin (Arbiter primary), Hazard Toy (Assassin primary), all 2.27, May 29 2017
- **Official text** (both [Game text via wiki]):
  - Fidget Boomer: "Have toy tricks gone too far!? Explosions are safe right?"
  - Spin Baby Spin: "When I spin you spin!"
- **Look** [Observed]:
  - **Fidget Boomer:** a **rose-chrome three-lobed spinner** (#8B5160, highlights #DC8297) held up in Astoria's raised hand, about 0.45× her height.
  - **Spin Baby Spin:** a spinner with **opaque gunmetal arms pierced with holes and a glass hub**, held in Sanchez's mechanical right hand.
  - **Hazard Toy:** the dark-green trefoil from Part A.
- **Projectile and impact** (both [Fan-wiki]):
  - **Fidget Boomer:** "the fastest projectile speed in the game", 3000 u/s; explosives 40–70, ammo 4. It explodes after a short delay on surface contact; no status effect.
  - **Spin Baby Spin:** 1,300 u/s, explosives 20–35, ammo 6. It explodes and causes **Controls Reversed** for 8 s, shown as "a green question mark" overhead, with background music disabled.
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/frames/fidget_group.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/v2/fidget.jpg (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/FidgetBoomer.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/SpinBabySpin.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/HazardToy.png
- **Depiction for shorts:** a "fidget craze" short with three bears and three spinners: a pink pop, a green question mark and a purple-green poison skull.
- **Confidence:** partial.

## Late-era drops, 2018
- **Kelowna** (Arbiter primary, 2.31, Mar 8 2018):
  - No description: "the only Arbiter primary to lack a description" [Fan-wiki].
  - **Look:** a black gun with a **glowing violet canister (#5E2CFC–#5F2FE8)**, a purple-lens scope and a white crystal-spike muzzle crown [Observed, Kelowna.png].
  - **Stats:** 800 u/s, 10 ammo, 8 damage per second for 2 s [Fan-wiki].
  - **Impact:** a small projectile bursts into poison clouds containing "a clone of Arbiter doing the Creepin taunt", and kills play "Thriller" [Fan-wiki]. **Do not use that song** [Inference: rights].
- **I Lava You / "I Lava U"** (Sniper secondary, 2.51, Apr 13 2018):
  - **Mechanics:** proximity mines fired in a straight line at 1,200 u/s; 1 s priming, 100-unit trigger radius, 25–60 damage, 4 ammo [Fan-wiki].
  - The weapon "is based off of the unreleased Battle Bears Ultimate Lavarifle" [Fan-wiki].
  - **Look:** File:ILavaU.jpeg (Sniper (BBG) gallery, uploaded 2018-05-12) shows Astoria holding a compact gun [Observed, re-opened]. It has a gunmetal scope and muzzle with a red-glowing lens and tip, and a dark-brown "lava rock" body with glowing red-orange cracks (#871513 / #B93328 / #DD8663).
  - The mine's look is [Unverified].
- **Dragon Slayzer (BBG)** (Engineer secondary, 2.51):
  - A stub with no image. 400,000 Joules, explosives 10–20, damage 35, 800 u/s, duration 4 s, 4 ammo [Fan-wiki].
  - **The BB Overclock version (context only):** the wiki text says "a dragon with a sword coming out of its head… The laser… is an orange blast. The dragon's color is red" [Fan-wiki]. Its own Gear Up image (DSNew.jpg, "Default look of the Dragon Slayzer as shown on the Gear Up menu") shows a **grey-silver dragon** with a beige ribbed neck and a blade from its mouth [Observed, re-opened], which contradicts "red".
  - Whether BBG's version matches either is [Unverified].
- **Social Butterfly (BBG)** (2.53): see Part B.
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned/png/Kelowna.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/v2/png/ILavaU.png (re-opened)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/unassigned-check/v2/png/DSNew.png (re-opened)
- **Depiction for shorts:** Astoria lobs glowing lava-rock mines that tick for a second and then pop in an orange burst when someone steps close [BBG News invention: blast look].
- **Confidence:** partial (Kelowna and I Lava U looks observed); unknown (Dragon Slayzer).

---

## Corrections for the character file

Every "current text" below was checked to exist verbatim in /home/user/thallo-site/bbg-news-repo/characters/.

1. **oliver.md, line 51**
   - **Current text:** "The Bearzooka is drawn as a green, hazard-striped tube [Observed; Inference]."
   - **Correction:**
     - The BBG Bearzooka is a coral-red tube (#A54447 on the April 2013 BBR model; #D05655 under Steam-trailer light, 2013 footage [Inference, strong]) with a row of glowing orange window panels (#EB7921–#FEA53C), grey bands and a black bore.
     - The panels are rectangular on the April 2013 BBR model, and pointed and chevron-like in the Steam trailer footage and on SkyVu's Jul 6 2026 "Classic Oliver" card.
     - The flared muzzle end is grey-and-red checkered in the Steam trailer footage and on the 2026 card.
     - It rests on his right shoulder and is about 0.8× his height [Observed].
     - The green, hazard-striped launcher is the BB: Zombies Bearzooka (wiki File:Bear.jpg), the likely source of this line [Observed; Inference]. The only green launchers in BBG are Tillman's yellow-olive Twin Bearzookas.
   - **Evidence:**
     - Photo_19-04-13_12_02_26_PM.png (Bearzooka (BBG) infobox, "Oliver with the Bearzooka").
     - Dban1's "[Oliver]:Secondary - Bearzooka" thumbnails (April 2013).
     - Steam trailer frames at 3.89–4.59 s (t_0009, really 4.22 s; 2013 footage [Inference, strong]).
     - SkyVu's Jul 6 2026 "Classic Oliver" short (byri_kQBUS4; crop byri_zooka.jpg, 2026.addendum.md).
     - Bear.jpg ("Bearzooka in BBZ") and Ohmagawdyas.png.
     - The wiki's "In BBG and BB0, it is a rocket launcher with red and orange lines."
2. **oliver.md, line 75 (reference prompt)**
   - **Current text:** "He holds a chunky assault rifle and carries a green hazard-striped launcher tube on his back."
   - **Correction:** "He holds a chunky assault rifle and carries a coral-red launcher tube (#A54447) with a row of glowing orange window panels, grey bands and a flared muzzle end; in game it rests on his right shoulder."
   - **Evidence:** as item 1.
3. **sanchez.md, colours line**
   - **Current text:** "Bind Gun #1E6FD9"
   - **Correction:** "Bind Gun #0991D4–#138CC0 (lit #1CB5F3–#29B7EE, highlights #6BE4F7; reads #2D6D8F–#367494 in dim in-game light), glowing white-cyan round muzzle #DCE9F5–#EBF0F5 [Observed, sampled]."
   - **Evidence:**
     - Two independent samplings of Sanchez_weapons.png: the 900×691 card labelled "BIND GUN", uploaded 2013-12-20. sanchez.md's [card] link points to the same file name on battlebears.com via the Wayback Machine.
     - Bind_Gun.png.
4. **sanchez.md, reference prompt**
   - **Current text:** "Holds a large glossy blue sci-fi gun (#1E6FD9)."
   - **Correction:** "Holds a large, angular, glossy azure sci-fi rifle (#0991D4 with #1CB5F3 highlights) with stepped armour panels, an open slot along the top and a glowing white-cyan round muzzle, about 0.7× his height, two-handed across the chest."
   - **Evidence:** Sanchez_weapons.png and Bind_Gun.png, measured and sampled.
5. **sanchez.md, open questions**
   - **Current text:** ""Adrenaline Gun" (site) versus "Adrenaline Burst" (wiki)."
   - **Correction:**
     - Both names are on the wiki, for different games. "Adrenaline Gun" is the BBG page: the Bind Gun, with stats changed from slow to speed-up on 2021-06-18 UTC and the page moved on 2021-07-17.
     - "Adrenaline Burst" appears only in the wiki's Battle Bears Heroes table. SkyVu's own BBH page says "Adrenaline Gun".
   - **Evidence:** the Adrenaline Gun revision log, the Battle Bears Heroes wiki page, and battlebears.com/pages/characters.
6. **riggs.md, line 56 (Beebeegun look)**
   - **Current text:** "Their look is undocumented, so designs, like the toothbrush prop, are [BBG News invention]."
   - **Correction:**
     - The Beebeegun's look is documented in an in-game image: a black riveted minigun body (#262625–#282727) with orange-and-black striped vent panels, a glossy gold octagonal hive (#AF862A, highlights #D4AF38) with a cartoon bee, and yellow bee-wing fins; no coil [Observed, BBR April 2013 shop shot].
     - The pink-hive gun with a glowing magenta spiral coil is the Electric Honey, not the Beebeegun. It appears with The Incredible Riggs, in Steam screenshot screen_00 and in the Steam trailer at 34.5–36 s (2013 footage [Inference, strong]), where it fires pink tracer streaks with pink-white starburst hits [Observed]. The Oct 2026 playtest also shows it (droid BBG's CmYil-JJdC0, HUD 93/120) [Observed; that it is the Electric Honey is Inference, strong].
     - No image of Beebeegun fire is known [Unverified]. The toothbrush prop remains [BBG News invention].
   - **Evidence:**
     - Beebeegun infobox: Photo_19-04-13_12_50_44_PM.png, "Riggs with the Beebeegun".
     - Electric Honey (BBG) infobox: Photo_19-04-13_12_50_47_PM.png, "Riggs with the Electric Honey".
     - Theincredibleriggs.png, Steam screen_00.jpg, and trailer frames 34.6–36.2 s (2013 footage [Inference, strong]).
     - Oct 2026 playtest: CmYil-JJdC0 crops cm_m2_gun.png and cm_max_hud.png (riggs.addendum.md).
7. **riggs.md, line 56 (weapons list)**
   - **Current text:** "BBG defaults Beebeegun, Hivey League, Barbed Gloves [Fan-wiki] ([Heavy (BBG)][wh]);"
   - **Correction:** keep the line, and add an extra melee: Catastrophe (BBR 1.3.1, 2012; spelled "CATASTOPHE" in game), a pair of calico cat-head gloves with one big blue eye per side [Observed]. riggs.md has no separate extras list, so add it here.
   - **Evidence:** Catastrophe.png (Oct 2012 shop screenshot), Catastrophe_1.png, and the Catastrophe wiki page.
8. **riggs.md, line 57 (skins list)**
   - **Current text:** "Gold Riggs, Old Timey, No More Mr Ice Guy, Nature's Folly, Teen Wolf, The Incredible Riggs, Law Man, On A Roll, B and J, Rocky Horror."
   - **Correction:** keep the list and add a note: The Incredible Riggs (BBG 2.15, Dec 20 2014; green skin, torn maroon shorts, shell backpack; "You won't like me when I'm green! " [Game text via wiki]) is on the loadout screen in the thumbnail of JustNubz's Sept 20 2026 closed-playtest showcase [Observed].
   - **Evidence:** https://i.ytimg.com/vi/-lAtv-j9Sms/maxresdefault.jpg ("CHARACTER HEAVY / SKIN THE INCREDIBLE RIGGS") and the oEmbed title "BBG All Classes Showcase [Skins, Taunts, Weapons, and Melee] (from Closed Playtest #4)".
9. **b-1000.md, line 54**
   - **Current text:** "Defaults: Grenader ("does the throwing for you"), Last Resort ("wait 3 seconds and then boom!"), Axecutioner ("replace your hand with an axe")"
   - **Correction:**
     - Mark Last Resort as removed. Its wiki page says "THIS WEAPON IS REMOVED" (on the page by 2020-11-09) and "Last Resort was the default secondary weapon for the Assault class" [Fan-wiki]. The Assault (BBG) page still lists it.
     - When it was removed, what replaced it as default, and whether it is in the 2026 build are [Unverified].
     - Do not draw B-1000's orange hex back pack as the Last Resort device. SkyVu's "Energy Barrier & Energy Overflow" sheet shows near-identical modules [Inference].
   - **Evidence:** the Last Resort and Assault (BBG) wiki pages, the Last Resort revision log, Last_Resort.png and B1000_weapons2-3-787x1024.png.
10. **saberi.md, line 57**
    - **Current text:** "Energy Rifle, Plasma Machine Gun, Missiles, Minigun, Mallet, Sledgehammer; later Plasma Shotgun and Gamma Burst [Canon]"
    - **Correction:** the list is incomplete. Add [Fan-wiki]:
      - Toxic Rifle (primary, 2.15, Dec 20 2014);
      - Landmine (secondary, 2.19, Apr 26 2015);
      - ClubCobra (melee, 2.20, May 29 2015; "A powerful melee made of jade and gold." [Game text via wiki]; a gold cobra-head club with a green eye [Observed]);
      - Social Butterfly (primary, 2.53, Apr 28 2018; no image).
    - **Evidence:** the wiki Updates table; the Toxic Rifle and Landmine pages (category Combat Tech); the ClubCobra and Social Butterfly (BBG) pages; Clubcobra.png.
11. **botch.md, line 57**
    - **Current text:** "extras include Orbs, Fear Orbit, Cosmic Bomb, Gravity Well and Toxic Plague"
    - **Correction:**
      - Add Hazard Toy (primary, 2.27, May 29 2017): a translucent dark-green three-bladed fidget spinner with a ringed hub. Official text: "Banned from elementary schools world wide, this weapon is as dangerous as it looks!" [Game text via wiki].
      - It fires a fast straight projectile that explodes and leaves a stacking poison cloud; poisoned targets show a purple/green skull [Fan-wiki].
      - It is missing from the wiki's Assassin (BBG) list.
    - **Evidence:** the Hazard Toy and Status Effects pages, and HazardToy.png.
12. **graham.md, line 53**
    - **Current text:** "BBG defaults [Fan-wiki] Power Glove ("This weapon can HANDle any situation."), Turret ("Use it wisely, you only get one at a time.") and T Square ("Tee off on your opponents with this classic tool. Ouch.")"
    - **Correction:** keep the line, and add the two Engineer weapons whose pages are missing from Category:BBG Weapons:
      - **MuskIt** (primary, 2.12, Oct 2 2014): "The musk of the Gyrnobal has been known to turn people into mutants, but most blow up." [Game text via wiki]. A musket with a salmon-pink breech and a yellow stock that sprays a short green irradiating cone [Fan-wiki; Observed].
      - **Bind Field** (secondary, 2.6, Dec 20 2013, originally "Slow Field"): a dark-brown ball with neon-green seams and purple studs, lobbed to make a field that slows enemies 75% for 3 s [Fan-wiki; Observed].
    - **Evidence:** the MuskIt and Bind Field pages, Musket.png and Slowfield.png.
13. **wil.md, line 54**
    - **Current text:** "Senor Potato, Pie Bomb, Traffic Light [Fan-wiki]"
    - **Correction:**
      - The Traffic Light has official item text: "Why is there no yellow light you ask? Wil only travels in two modes. He stops and sometimes he has to go." [Game text via wiki].
      - Its look is documented: a yellow pole (#FED100) with black bands, topped by a spiky grey signal head with only a red and a green lamp [Observed].
      - Its page is missing from Category:BBG Weapons.
    - **Evidence:** the Traffic Light page and Trafficlight.png.
14. **Mapping file** (`weapons_by_class.json`; not a character file)
    - **Remove** A Salt Rifle, Heavy A Salt Rifle, Soaker, Spreadshot (BBG), Steamshot, B.E.A.R. Club and Krikkit Bat from Riggs and Huggable. They come from a copy-pasted changelog.
    - **Assign** Adrenaline Gun → Sanchez, Catastrophe → Riggs, ClubCobra → Saberi, Hazard Toy → Botch, MuskIt and Bind Field → Graham, Traffic Light → Wil, Social Butterfly (BBG) → Saberi.
    - **Drop** The Incredible Riggs (a skin) and "Soldier (BBG)/Weapons" (a list page mapped under Oliver).

## Open questions
- Does the 2026 Arbiter default fire the slowing Bind Gun or the speeding Adrenaline Gun, and did the model change from the 2013 azure rifle?
- What colour is the Bind Gun / Adrenaline Gun beam (the wiki says purple; no image exists), and is a sped-up target marked by any icon?
- Hazard Toy: does the spinner itself fly, and what colour is its poison cloud?
- Catastrophe, ClubCobra and Traffic Light: swing animations and hit effects are undocumented.
- Catastrophe's real stats: 40 or 25 damage? −20% or +15% speed? +10%, +5% or −5% health? (The page, the trivia, the Health page, the 2.6 notes and the 2012 screenshot disagree.)
- ClubCobra's health modifier: +10% (screenshot and Health page) or +15% (its own page)?
- Bearzooka ammo: 1 (infobox, 2013 HUD) or 2 ("two shots" in the prose)? Rocket: answered (Steam trailer 1.92–3.05 s, 2013 footage [Inference, strong]). Explosion: partly answered. A faceted yellow blast with grey smoke is seen only in low-res 2014–15 fan footage (Bearzooka link [Inference, high]); no official or 2026 frame shows it.
- Doomstick: BBR 1.3 (its own page) or 1.3.1 (the version page)?
- Social Butterfly has no image or effect description at all.
- When exactly were Bouncing Betty (after Mar 2018, before May 2020), Greased Lightning and Last Resort removed, and are any of them in the 2026 build?
- Is the orange hex pack on B-1000's back related to Last Resort, or is it standard hardware (Energy Barrier / Energy Overflow)?
- Are the pale-yellow stars near the Electric Honey's target (Steam screen_00, trailer 35.8–36.1 s) a gun effect or the melee fight's hit effect?
- Which skin is the green-skinned bear (blue bandana mask, gold-bullet belt) carrying the Bearzooka in trailer t_0009?
- MuskIt's true length (foreshortened in the only image).
- Steam claims "80+ primaries / 60+ secondaries / 50+ melees" against 77/64/46 on the wiki. Are there new or undocumented 2026 weapons?
- The Sept 20 2026 showcase thumbnail shows the build string "3.0.5_2026.11.19_B1". What does the date field mean?
- Archived SkyVu sources (BBR 1.3.1 blog; BBG 2.6, 2.20 and 2.27 notes) were unreachable through web.archive.org. Re-verify version dates and official wording when possible.
- Were the seasonal weapons ever time-limited, and does the in-game freeze match the S'no Matter concept's ice mound?
- Is the Bearzooka concept sheet (Soldier_Weapon.png, no watermark) official SkyVu art?
