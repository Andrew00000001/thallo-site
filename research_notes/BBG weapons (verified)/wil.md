# Wil (Chub Scout): weapons bible (verified edition)

**What this covers.** Wil is BBG's **Chub Scout**. The class blurb in the wiki's class template reads: "The masticator of mayhem, a Chub Scout is always prepared to even the odds for his team. His appetite for destruction is perfect for those simply wishing to wreak sweet havoc on their enemy." [Game text via wiki] (Template:Class:Chub_Scout_(BBG)). SkyVu's Steam page for the re-release lists "-CHUB SCOUT: Wil" and "80+ PRIMARY WEAPONS  60+ SECONDARY WEAPONS  50+ MELEES  10 SPECIAL EQUIPMENT  200+ COSMETIC ITEMS", with the release date "Nov 4, 2026" [Canon] (Steam store API, appid 4408320, fetched today).

**How complete this is.** The wiki class page "Chub Scout (BBG)" lists 20 weapons: 9 primaries, 6 secondaries and 5 melees. Category:Chub Scout (39 pages, listed today) contains the same 20. The draft covers all 21 entries in arsenal_wil.json (the 20 plus the BBH-only Sarcastic Air Strike).
- Traffic Light's categories are Battle Bears, Battle Bears Gold, Melee and Chub Scout. It is not in Category:BBG Weapons, so weapons_by_class.json["Wil"] lists only 19 [Observed: API].
- None of the 5 "_unassigned" pages belongs to Wil. Adrenaline Gun is Arbiter, Catastrophe is Heavy, ClubCobra is Combat Tech and Hazard Toy is Assassin; The Incredible Riggs is a skin (Versions 2.15).
- Later BBG additions are not Wil's either: Let It Cold (Demo), Fidget Boomer (Sniper), Spin Baby Spin (Arbiter), Kelowna (Arbiter) [Fan-wiki infoboxes].

**Era key** [Fan-wiki: Updates; Battle Bears Gold/Versions]
- **BBR:** Battle Bears Royale, from Oct 8, 2011. Wil arrives in BBR v1.3 (May 3, 2012).
- **BBG:** Battle Bears Gold, from 1.0 (May 24, 2013) through 2.53.3 (Aug 31, 2018), 3.0 (Nov 15, 2021) and 3.0.1 (Dec 18, 2021). The draft's "2013 to about 2018" was wrong.
  - The wiki's transcription of the 3.0 notes says "All +1 Equipment has been removed except Speed +1" and "Equipment Slot 2 has been removed". This matters when reading clip sizes.
  - Two 2018 fan uploads (v2.53) title the game "Battle Bears Royale/Royals" [Observed: video titles].
- **BBG 2026:** the Steam, iOS and Google Play re-release on Nov 4, 2026.
- **BBH:** Battle Bears Heroes, soft launch May 23, 2023 per the wiki; 2024 release.

**Sources reached today**
- Wiki MediaWiki API: every weapon page, the class page and template, the Updates, Versions and Versions/2.6 pages, BBR 1.3, 1.3.1 and 1.4.2, the skin pages, the lore pages (Arrow, Batterito, Boomstick McShootington, Bubble Gun (BB0), Blaster Cannon), and first revisions of 4 pages.
- battlebears.com/pages/characters, live.
- Steam store API.
- Local Steam trailer frames, plus my own extractions at 17.6–23.0 s.
- The 5 Steam screenshots. None shows Wil; screen_00's orange bear holding a banner is a Huggable [Observed].
- YouTube thumbnails (hqdefault, hq1–3, maxres) and oEmbed titles/channels for 42 videos.

I watched no video. Every YouTube [Observed] tag means a still thumbnail I opened.

**Not reached.** web.archive.org reset every connection (3 tries with backoff), and the availability API returned an "Internet Archive: Temporarily Offline" page. So SkyVu's BBG 2.6 change log (battlebears.com/battle-bears-gold-2-6-change-log/) stays unverified, and every patch figure below is [Fan-wiki].

**Paths**
- `$V` = `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-verify`
  - Wiki images (PNG copies): `$V/png/`
  - YouTube thumbnails: `$V/yt/<id>_<size>.jpg`
  - Zooms: `$V/crops/`
  - Contact sheets: `$V/sheets/`
  - My trailer extractions: `$V/trailer/f_<seconds>.png`
- `$T` = `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/trailer`. Frame t_N is at (N−1)×0.5 s.
- Hex values are medians of small crops. They are approximate and depend on lighting and compression.

**Scale.** Oliver = 1.0×. Wil ≈ 0.9× and pear-shaped [BBG News invention, house chart]. Weapon sizes are fractions of Wil's height, measured from loadout renders and trailer frames [Observed, approximate].

**What this verification changed (summary)**
1. **Default look: new official source.** SkyVu's own "Wil's Got MOVES" thumbnails (stamped "Wil Animations 21/03/2012") show the red padded helmet, ice-pop tank, red-lit elbow and knee pads, the ABBi backpack, the Boomstick with its red "00" readout, and the Balance Beam's violet emitter glow. The character file's "red cap" is a misreading of this padded helmet.
2. **Elbow pads have red lights too** (draft said only the knees).
3. **Team colours.** Concept File:Wil_skin.png shows team-coloured helmet, ice-pop print and pad lights. The draft's evq-fk6i8Eo citation shows a blue Monster Hoodie, not a helmet.
4. **"CLASSIC WIL" (2026) is not the helmet look.** It is a plain tan bear with a red tied headband and the ABBi backpack. Which skin is the 2026 default is unverified.
5. **The blue ice pop stays.** It is a prop on SkyVu's c.2012 card. The draft's "delete the blue ice pop" correction is withdrawn.
6. **Trailer details**
   - The Booty Duty backpack is red-and-black (team-coloured) with snacks, not black.
   - The Batterito is about 0.45–0.5× Wil's height long, not 0.3×.
   - Timestamps re-anchored.
7. **Pie Bomb gameplay uses an over-the-shoulder third-person camera** (draft said "first person").
8. **Clip sizes recorded from HUDs** for the Boomstick, Señor Potato, Pie Bomb, Chainsaw Shotgun, Sole's Bane and Pop Tart. The Boomstick's 1/1 HUD is the plain Boomstick, not Doomstick footage.
9. **Killdoba glitch video:** its hq1 does show a fire patch (source unattributed).
10. **Sole's Bane:** the pink-violet lightning source is unclear (draft asserted "another weapon").
11. **BBH quote:** the battlebears.com page names no game; the "BBH" tag is now marked [Inference].
12. **Melee release order.** Traffic Light page history, plus the 2.13 Fatman skin release, point to Traffic Light = 2.13 and Bow and Arrow = 2.16 [Inference].

---

## Wil's BBG default look (sub-topic; use in every short)
- **Official visual:** SkyVu's "Wil's Got MOVES" (BATTLE BEARS channel; title via oEmbed [Canon]). Its thumbnails carry the stamp "Wil Animations 21/03/2012" [Observed: i.ytimg.com/vi/r7TipV3IYtI/hqdefault.jpg, hq1.jpg, hq3.jpg; zooms `$V/crops/r7_hq1.png`, `$V/crops/r7_hqd.png`]. They show:
  - a red padded helmet;
  - a white tank top with a red ice-pop print;
  - black elbow and knee bands, each with a glowing red pad;
  - a grey ABBi backpack with a large camera lens;
  - Wil posing with the Boomstick and the Balance Beam.
- **BBG loadout renders** (wiki) show the same outfit [Observed: File:Wil_default.png, Arrow.jpg, Bbooww.jpg, EZ_Chee-Z.jpg, Whipped_Pain.jpg, Pie_Bomb.png, Doomstick.jpg, Wil's_backpack.png]:
  - The helmet has round dark vent dimples and a black chin strap.
  - The tank top is ribbed, and the ice pop has a drip and a wooden stick.
- **Sampled colours:**
  - helmet #CF0012 lit to #9C040E shaded;
  - shirt #E0E0DE;
  - ice-pop print #D50010–#DD0110;
  - fur #A56C20 (shaded forehead) to #B07B40 (muzzle);
  - knee-pad light #8B0214 (dim menu light);
  - ABBi shell #525253–#595A59, lens blue-grey #62778C.
- **Team colours:**
  - The uncredited wiki concept sheet File:Wil_skin.png (uploaded 2012-11-27) shows a red version (red helmet, red ice pop, red pad lights) and a blue version (blue helmet, blue ice pop, blue pad lights) [Observed; origin presumed SkyVu, Unverified].
  - The BBR 1.3 trailer thumbnail shows a blue helmet in a match [Observed: wNpM1woYv7k hq1].
  - So the helmet, shirt print and pad lights are team-coloured [Inference].
  - evq-fk6i8Eo shows Wil in a **blue Monster Hoodie**, not a helmet [Observed]. The red version of that hoodie appears in o8rEXLT4n_0 and KsddBonDY88. Other skins are team-coloured too [Inference].
- **Card prop:** on SkyVu's c.2012 character card Wil eats a dripping cyan-blue ice pop (#05C0DD) [Observed: File:Wil_description.jpg]. That ice pop is a prop, separate from the shirt print.
- **2026 playtests:**
  - In-match thumbnails show the red padded helmet [Observed: OqSi3rfMdl8 hq1, "Battle Bears Gold Playtest 4 clips…" by Mingo; MS2wiArCiCA hq1, "Battle Bears Gold FINAL PLAYTEST"].
  - The loadout screen in MS2wiArCiCA hq2 reads "CHARACTER: CHUB SCOUT / SKIN: CLASSIC WIL" (faint) [Observed, low-res].
  - The model shown is a **plain golden-tan bear with a thin red headband**, with no helmet and no shirt [Observed, low-res].
  - hq3 shows the same look from behind: the headband is tied at the back with two tails, and he wears the ABBi backpack and holds the Bow [Observed, low-res].
  - Which skin is the 2026 default is [Unverified].
- **Steam trailer:** the Wil in the trailer wears the **Booty Duty** skin [Observed match: `$T/t_0037.jpg`–`t_0043.jpg` vs File:Booty_duty.png and File:Booty.png concept]. It has:
  - a red headband and a pink-white tank top;
  - red shorts, and red and orange striped wristbands and leggings;
  - a **red-and-black backpack covered in snacks** (cookie, candy, lollipop) [Observed: `$V/crops/tr_212.png`].
  - The wiki says "cookies, chips, candy bars, and lollipop on his team-coloured and black backpack" [Fan-wiki]. It also says only the default and Gift Wrapped skins carry ABBi [Fan-wiki: Gift Wrapped trivia].
- **Images viewed:**
  - `$V/sheets/s_r7TipV3IYtI.jpg`, `$V/crops/r7_hq1.png`, `$V/crops/r7_hqd.png`
  - `$V/sheets/g_default.jpg`, `$V/sheets/g_sec.jpg`, `$V/sheets/g_doom.jpg`
  - `$V/png/Wil_skin.png`, `$V/png/Wil_description.png`
  - `$V/sheets/s_wNpM1woYv7k.jpg`, `$V/sheets/s_evq-fk6i8Eo.jpg`, `$V/crops/oq_hq1.png`, `$V/sheets/s_MS2wiArCiCA.jpg`
  - `$V/crops/ms2_hq2.png`, `$V/crops/ms2_text.png`, `$V/crops/ms2_bear.png`, `$V/crops/ms2_hq3c.png`
  - `$V/sheets/g_skins.jpg`, `$V/crops/tr_212.png`
- **Depiction for shorts:** Use the red padded helmet, the ice-pop tank top and the ABBi backpack. Colour the helmet, print and pad lights in the team colour (red by default). Keep the blue ice pop as a hand-held snack prop.
- **Confidence:** observed.

## Boomstick (primary; default; BBR v1.3, May 3, 2012 → BBG; 2.6 rebalance; 2026 status unverified)
- **Official text:** "Trusty Boomstick McShootington. This guy does more damage if your enemy has a higher K/D ratio and less damage if they have a lower K/D ratio." [Game text via wiki] (wiki: Boomstick). The wiki trivia adds: "The boomstick used to be affected by Kill/Death ratio." No date is given [Fan-wiki].
- **Different game (BBH):** "Wil's "Boomstick" attack launches explosive pellets that burst on impact, covering a wide area." [Canon] (battlebears.com/pages/characters, fetched today). The page names no game. Its "Ultimate" moves and "first batch of heroes" wording mark it as BBH, not BBG [Inference].
- **Look:**
  - A compact near-black to dark grey pump shotgun modelled on the Franchi SPAS-12 [Fan-wiki trivia].
  - A boxy top rail with a row of round holes and a ribbed pump fore-end [Observed].
  - A small **red two-digit LED readout ("00")** on the receiver side [Observed: File:BoomBoom.png zoom `$V/crops/boom_gun.png`; also in SkyVu's 2012 animation test, `$V/crops/r7_hq1.png`].
  - About 0.4× Wil's height. In BoomBoom.png (Gift Wrapped skin) he holds it two-handed across the belly, muzzle down-right [Observed]. In the 2012 animation test he holds it out one-handed in a T-pose [Observed].
  - HUD icon: a dark grey shotgun with a red mark [Observed: 8HtBU9imRzo, -gRmjscGzQs, RukIckwnibs].
  - BB-1 (2010) 2D cutscene version: a grey-green shotgun lit by his lighter [Observed: File:Boomstick_McShootinton.png]. That is not BBG.
- **Firing:**
  - "When fired, the Boomstick releases a powerful, short ranged wave of bullets." "The Chub Scout uses it like a pump action shotgun." [Fan-wiki]
  - "All shotguns use hitscans on a short spread range." [Fan-wiki: Weapon Statistics]
  - Infobox: 55 damage, 1 s rate of fire, ammo 1, 1.5 s reload, +5% speed [Fan-wiki].
  - BBG 2.6 (Dec 20, 2013): damage 22→50, kill-difference bonus 7→2, fire rate .75→1 [Fan-wiki: Versions/2.6; SkyVu's log unreached].
  - Fan HUDs read 0/3, 1/3 and 3/3 in two BBG "Boom Stick" videos (8HtBU9imRzo, zt6DqETrDM4; Void Fyre) and 3/3 in a 2.23 video (RukIckwnibs maxres). They read 1/1 in -gRmjscGzQs [Observed: `$V/crops/hud_icons.png`, `$V/crops/ruk_icon.png`, `$V/crops/grm_icon.png`].
  - All of these show the plain Boomstick icon, so the 1/1 clip is not Doomstick footage. When the clip size changed is [Unverified].
  - Muzzle flash: not seen [Unverified].
- **Projectile:** None that travels; it is hitscan [Fan-wiki].
- **Impact / end result:**
  - In "HERE'S MY BOOMSTICK!!!(BOOMSTICK MCSHOOTINGTON GAMEPLAY)- Battle Bears Gold 2.25", small glowing yellow-orange spark dots are scattered around the target [Observed: i.ytimg.com/vi/D_t7M6WwYPg/maxresdefault.jpg]. Reading them as pellet hits is [Inference].
  - A magenta zig-zag streak in the same frame has an unclear source [Unverified].
  - Glowing orange "+" shapes near an enemy in -gRmjscGzQs hqdefault and hq2 may be pickups [Unverified].
  - The page gives no explosive or AoE stats, so BBG shows no splash [Fan-wiki; Inference]. Do not show BBH's exploding pellets in a BBG-era short [Inference].
- **Images viewed:**
  - `$V/sheets/g_boom.jpg` (BoomBoom.png, boom_gun zoom, Boomstick_McShootinton.png)
  - `$V/crops/r7_hq1.png`
  - `$V/sheets/s_8HtBU9imRzo.jpg`, `$V/sheets/s_zt6DqETrDM4.jpg`, `$V/sheets/s_-gRmjscGzQs.jpg`
  - `$V/yt/D_t7M6WwYPg_maxresdefault.jpg`
  - `$V/crops/hud_icons.png`, `$V/crops/ruk_icon.png`, `$V/crops/grm_icon.png`
- **Depiction for shorts:** A pump, a short cone of yellow-orange pellet sparks peppering the target, and a recoil hop. No explosion. The muzzle puff is a [BBG News invention].
- **Confidence:** partial (model observed; hit sparks seen only in a thumbnail).

## Doomstick (primary; BBR 2012 → BBG; 2.6 rebalance)
- **Official text:** "We give Wil a hard time but, the truth is, he is a far braver man than I for even touching this thing... 0__0" [Game text via wiki] (wiki: Doomstick).
- **Release:** The page says it "came out in v.1.3". The BBR Version 1.3.1 page (June 28, 2012) lists it among weapons "released gradually over four weeks" [Fan-wiki conflict].
- **Look:** The wiki describes "a firey, more hellish version with an eye in the middle" [Fan-wiki]. The images show [Observed: File:TbwrU.png "THE DOOMSTICK" graphic, File:Wil_doomstickers.png, File:Doomstick.jpg]:
  - a black and slate body crazed with glowing red-orange-yellow lava cracks;
  - a row of yellow-orange flame spikes along the top;
  - a bloodshot eyeball with an orange iris set in the side;
  - fleshy pink double barrels with red veins and pale ends, and a flesh-pink grip;
  - a length of about 0.45× Wil's height.
  - It also appears in SkyVu's in-game banners (File:Paqueta.png, File:Chubby_bundle.jpg) and in SkyVu's "BBR 1.3.1 and BEYOND!" promo art (File:BBRWEAPONS.png) [Observed].
  - It is held by the Booty Duty and Fatman skins [Observed: File:Booty_duty.png, File:Fatman.PNG].
  - A BBR menu shot shows Not-So-Slenderman Wil holding it, with "SPEED +7%" [Observed: File:Doomstick.png].
- **Firing:**
  - "Releases a powerful, short ranged wave of bullets"; used "like a pump action shotgun" [Fan-wiki]. It is hitscan like all shotguns [Fan-wiki: Weapon Statistics].
  - Infobox: 55 damage, 0.75 s rate of fire, ammo 2, 2.5 s reload, +5% speed. The intro's "three times the ammo" conflicts with this [Fan-wiki].
  - 2.6: damage 31→30, fire rate 1→.25, clip 2→3, kill-difference bonus 4→2 [Fan-wiki].
  - The 7% speed buff was removed in BBR 1.4.2 (Feb 28, 2013) [Fan-wiki]. Its code name is "KingSlayer" [Fan-wiki].
- **Projectile:** None visible (hitscan) [Fan-wiki].
- **Impact / end result:** I saw no in-game hit frame [Unverified]. Reuse the Boomstick's spark look [Inference].
- **Images viewed:** `$V/sheets/g_doom.jpg`, `$V/crops/doom_grip.png`, `$V/sheets/g_banners.jpg`, `$V/sheets/g_misc.jpg` (BBRWEAPONS.png, Doomstick.png BBR menu), `$V/sheets/g_skins.jpg`, `$V/sheets/g_melee.jpg` (Fatman zoom).
- **Depiction for shorts:** Wil holds it at arm's length; the eyeball swivels toward the target, then it fires the same yellow-orange pellet sparks. The swivelling eye is a [BBG News invention].
- **Confidence:** partial.

## Balance Beam (primary; level 15; BBR v1.3, May 3, 2012 → BBG)
- **Official text:** "The worse your team is doing than the other team, the more powerful this weapon is." [Game text via wiki]
- **Look:** a barbell or balance-scale gun, about 0.5× Wil's height across, held level at the waist [Observed: File:Balance_Beam.jpg, File:Balancebeam.png]:
  - a white and silver gun body;
  - a gold centre rod with two hexagonal gold weights;
  - a blue rod end and blue tip on one side, and a red end on the other;
  - a white pentagonal emitter glowing violet at its centre.
  - SkyVu's 2012 animation test shows the same build with a violet-white glow at the emitter while aimed [Observed: r7TipV3IYtI hqdefault, `$V/crops/r7_hqd.png`].
- **Firing:**
  - "Works like a standard hitscan automatic, firing beams in quick succession"; "fires slightly below the crosshairs" [Fan-wiki].
  - Range 3000 units, 0.15 s rate of fire, 50 ammo, 4 s reload, −10% health [Fan-wiki]. Fan HUDs read 22/50, 0/50 and 4/50 [Observed: o4FJDPNxyuA hq1–hq3].
  - Damage is 7.0, rising or falling 0.25 per kill (or bomb plant) that the team trails or leads by, with a minimum of 1 [Fan-wiki].
  - 2.6: scaling 1→.25 [Fan-wiki].
  - It is the class's only long-range weapon [Fan-wiki: class page].
- **Projectile / beam:** In "A BALANCED BATTLE(BALANCE BEAM GAMEPLAY) - Battle Bears Gold 2.22", a magenta-pink glow sits at the emitter and a faint thin pinkish line runs forward toward enemies [Observed, low-res: i.ytimg.com/vi/o4FJDPNxyuA/hq1.jpg, `$V/crops/o4f_hq1.png`]. Read it as thin magenta-violet beam pulses [Inference].
- **Impact / end result:** Not seen [Unverified].
- **Images viewed:** `$V/sheets/g_prim1.jpg`, `$V/sheets/s_o4FJDPNxyuA.jpg`, `$V/yt/o4FJDPNxyuA_maxresdefault.jpg` (fan title art made from a game render), `$V/crops/o4f_hq1.png`, `$V/crops/o4f_hq2.png`, `$V/crops/r7_hqd.png`.
- **Depiction for shorts:** Rapid thin magenta-violet beam ticks from the pentagon. Small violet sparks on hit are a [BBG News invention]. Gag: the beam fattens as the scoreboard turns against his team, which reflects the [Game text via wiki].
- **Confidence:** partial.

## Señor Potato (primary; BBR 1.4.3, Apr 15, 2013 → BBG)
- **Official text:** "You couldn't find a kinder gun if you tried! Not only does it fire a high velocity spud at your enemies, it also leaves piping hot fries behind to blister their feet." [Game text via wiki]
- **Update-note text:** The wiki's Updates page transcribes the 1.4.3.1 entry (Apr 23, 2013) as: "-Señor Potato Cannon: Wil shoots flaming spuds that explode on contact and leave piping hot french fries behind; Caution, fries do damage over time." The 1.4.3 entry reads "…french fries behi,Caution…" [Fan-wiki transcription of SkyVu notes; Unverified as Canon].
- **Look:** held at the hip, barrel forward, about 0.5× Wil's height long [Observed: File:Senor_Potato.jpg]:
  - a speckled golden potato (lit about #F7C56A) with a red Mr. Potato Head-style nose (#DC523A);
  - a white paper coffee cup on top;
  - silver-grey bicycle handlebars through the middle;
  - a pink-tan cardboard-tube barrel (lit about #DDA980).
  - The wiki lists "a coffee cup, a paper tube, bicycle handles, and a few "Mr. Potatohead" body parts" [Fan-wiki].
  - Concept sheet: four grey variants A–D [Observed: File:Señor_Potato_Concept.jpg].
- **Firing:**
  - Infobox: 1 s rate of fire, 3 ammo, 3.5 s reload, 1000 u/s [Fan-wiki]. "Confined to close-ranged combat only, due to its extreme arc" [Fan-wiki].
  - HUDs read 1/4 and 3/4 in BBR 1.4.3 footage [Observed: EfndjtWhm-0 hqdefault, hq2, hq3] and 6/6, 1/6 and 5/6 in a BBG fan video [Observed: XxEAr8mP4nE, `$V/crops/xxe_icon.png`]. The clip size changed over time [Inference].
- **Projectile:** "A potato spud" [Fan-wiki]. "Flaming" appears only in the update transcription [Fan-wiki]. No in-flight frame seen [Unverified].
- **Impact / end result:**
  - The spud "bursts into fries when it hits a player or surface". The fries also damage players "a large depth below the ground they are planted on" [Fan-wiki].
  - Stats: impact 65; explosive 35–50; AoE 125/250 [Fan-wiki]. 2.6 raised the AoE fields 100→200 and 300→400, which does not match the current infobox [Fan-wiki conflict].
  - An enemy stands in orange-yellow flame chunks under a column of dark smoke [Observed, low-res: i.ytimg.com/vi/XxEAr8mP4nE/hq3.jpg, `$V/crops/xxe_hq3.png`]. That fits burning fries [Inference]; the fry shape is not readable.
- **Images viewed:** `$V/sheets/g_prim1.jpg`, `$V/sheets/s_XxEAr8mP4nE.jpg`, `$V/sheets/s_EfndjtWhm-0.jpg`, `$V/crops/xxe_hq3.png`, `$V/crops/xxe_icon.png`, `$V/crops/efn_icon.png`, `$V/crops/efn_hq3.png`.
- **Depiction for shorts:** A high, smoking lob. The spud splits into glowing golden fries that stick upright in the floor like birthday candles and smoke for a beat, while bears hop on hot feet. The fry visuals are a [BBG News invention].
- **Confidence:** partial.

## Pie Bomb (primary; BBG 2.2, Aug 21, 2013; seen in the 2026 final playtest)
- **Official text:** "This explosive weapon will make you enjoy your last supper. It'll clean your plate. Prepare to pie...I mean...die! Okay, okay, you get the idea. It's a pie with a bomb in it." [Game text via wiki]
- **SkyVu's own video:** "BATTLE BEARS GOLD Update 2.2 Weapon Recap" (BATTLE BEARS channel) carries the on-screen caption '"Pie Bomb" / Wil Primary Weapon' [Canon: caption seen in i.ytimg.com/vi/BcEeAzXFChI/maxresdefault.jpg, `$V/crops/bc_max.png`].
- **Look:**
  - A golden-crust pie (#BCA77A) in a crimped silver foil tin (#B4B4B4), with a round black cartoon bomb (#1F1F1F) sitting in it and a short lit fuse throwing a white-yellow star spark [Observed: File:Pie_Bomb.png].
  - Wil carries it flat on one palm like a waiter's plate, in BBG and again on the 2026 "CLASSIC WIL" loadout screen [Observed: Pie_Bomb.png; MS2wiArCiCA hq2].
  - The pie is about 0.35× Wil's height wide.
  - In gameplay the camera is an **over-the-shoulder third-person** view (not first person): the black bomb dome and sparking fuse sit at the bottom centre of the screen [Observed: BcEeAzXFChI hq2 and hq3; 3X0gxm8IVGY; MS2wiArCiCA hq1 (2026)].
- **Firing:**
  - It launches the pie with "a fast projectile speed, relatively small AoE and large projectile, direct hits … are advised" [Fan-wiki].
  - 1,100 u/s, 0.45 s rate of fire, 3.5 s reload; derived from the Rockette Launcher [Fan-wiki].
  - HUDs read 2/2 in SkyVu's 2.2 recap and in a fan clip (a9pZW9OJI-8), and 4/4 later (3X0gxm8IVGY) and in the 2026 final playtest (MS2wiArCiCA hq1) [Observed]. The infobox says 4 [Fan-wiki]. Ammo +2 adds +2 [Fan-wiki], so an early 4/4 may be 2 plus equipment [Inference]. 3.0 removed +1 gear and the second equipment slot [Fan-wiki].
- **Projectile:** The pie-with-bomb itself [Game text via wiki]. It probably arcs: the wiki contrasts it with the Pop Tart Shuriken, which is "unaffected by gravity" [Inference]. No in-flight frame seen [Unverified].
- **Impact / end result:**
  - A bright white-yellow-orange fireball fills a corridor ahead, with grey smoke, at 0/2 ammo [Observed: i.ytimg.com/vi/a9pZW9OJI-8/hq3.jpg].
  - Explosive 25–50; AoE 150/300; 2.6 raised the AoE fields 75→100 and 150→200 [Fan-wiki].
  - It formerly did more damage when its user was losing [Fan-wiki].
  - File:Imagefdv.jpg, captioned "Pie Bomb as shown on the BATTLE BEARS Facebook page", is a photo of a MOGA-controller giveaway with a Huggable on the phone screen [Observed]. Do not use it.
- **Images viewed:** `$V/sheets/g_prim2.jpg`, `$V/crops/bc_max.png`, `$V/sheets/g_bc.jpg`, `$V/sheets/s_a9pZW9OJI-8.jpg`, `$V/sheets/s_3X0gxm8IVGY.jpg`, `$V/sheets/s_MS2wiArCiCA.jpg`, `$V/crops/ms2_bear.png`, `$V/png/Imagefdv.png`, `$V/crops/fdv_screen.png`, `$V/crops/hud_icons.png`.
- **Depiction for shorts:** He flicks the pie like a frisbee with the fuse sparking, and it bursts in a white-orange fireball. A harmless rain of crust flakes and filling dollops is a [BBG News invention].
- **Confidence:** observed (model, carry pose, gameplay view and blast; flight unseen).

## Chainsaw Shotgun (primary; BBG 2.2, Aug 21, 2013)
- **Official text:** "Chainsaws are cool. Shotguns that shoot chainsaws are cooler. Thanks BRJ." [Game text via wiki]
- **Look:**
  - A boxy purple-violet twin-tube launcher with cyan light strips and a grey toothed chainsaw bar along it. The muzzle glows white-hot [Observed: File:Chainsaw_Shotgun.png].
  - About 0.4× Wil's height, held two-handed at the chest.
  - The same gun appears in SkyVu's in-game "Boom Bundle" banner [Observed: File:Boombundle.png].
  - SkyVu's 2.2 promo art (BcEeAzXFChI hq1) shows Wil aiming it, with dark saw teeth along the top and bottom and a lavender-white glow in the mouth [Observed: `$V/crops/bc_hq1_wil2.png`].
- **Firing:**
  - "Fires a chainsaw that sticks to all surfaces including players, and detonates a second or two after impact with a rather large AoE" [Fan-wiki].
  - 0.75 s rate of fire, 3 ammo, 4.5 s reload; derived from the TNT Launcher. Like the Buzz Kill's bee, it can stick to players [Fan-wiki].
  - HUDs read 4/4 in 2.5 (KsddBonDY88) and 2/2 in 2.22 and 2.23 (du9-TFHf6Lg, ohJnpHcMabY) [Observed: `$V/crops/cs_huds.png`].
  - A yellow-white starburst flash bursts at the muzzle [Observed: KsddBonDY88 hq3, `$V/crops/ksdd_hq3.png`]. A soft white glow at the muzzle shows in ohJnpHcMabY hq1 [Observed, low-res].
- **Projectile:** A chainsaw [Fan-wiki].
  - ohJnpHcMabY hq1 shows a curved line of tan segments with a white puff on the grass ahead [Observed, low-res]. Whether that is the fired saw is [Unverified].
  - No clear in-flight frame.
- **Impact / end result:**
  - Infobox delay 0.75 s; 2.6 cut it .5→.25; the text says "a second or two". The figures conflict [Fan-wiki].
  - Explosive 35–70; AoE 100/200.
  - At launch the delay was said to be shorter when the team was losing [Fan-wiki].
  - Bug: on a direct hit the saw can hang in mid-air at the impact point until it detonates [Fan-wiki].
  - A small yellow-orange blast shows at a distance [Observed, low-res: ohJnpHcMabY hq3].
- **Images viewed:** `$V/sheets/g_prim1.jpg`, `$V/sheets/g_banners.jpg`, `$V/crops/bc_hq1_wil2.png`, `$V/sheets/s_KsddBonDY88.jpg`, `$V/crops/ksdd_hq3.png`, `$V/sheets/s_ohJnpHcMabY.jpg`, `$V/crops/ohj_hq1.png`, `$V/crops/ohj_hq3.png`, `$V/sheets/s_du9-TFHf6Lg.jpg`, `$V/sheets/s_KFJGtazYrdo.jpg`, `$V/crops/kfj_zoom.png` (no impact visible; the colourful patch is a wall mural), `$V/crops/cs_huds.png`.
- **Depiction for shorts:** A starburst muzzle flash, then a spinning saw blade thunks into a wall or bear, rattles for a beat, and pops in a yellow-orange blast. The rev beat and sawdust are a [BBG News invention].
- **Confidence:** partial.

## Bubble Gun (primary; BBG 2.12, Oct 2, 2014)
- **Official text:** "Bubble bubble pop, BUBBLE POP!" [Game text via wiki]
- **Look:** about 0.5× Wil's height [Observed: File:Bubble.jpg]:
  - a green sphere tank with yellow piping on top;
  - a yellow body;
  - a light-blue barrel ending in a yellow square-frame "wand" muzzle.
- **BB Zero version (2012, not BBG):** "It does not deal damage, but can deflect enemy projectiles" [Fan-wiki: Bubble Gun (BB0)].
  - Its 2D art: green sphere → orange sphere → blue tube → yellow trumpet bell, blowing a big iridescent violet-blue soap bubble [Observed: File:Bubble_Gun.jpg].
  - Concept art: line, grey and brass steampunk versions with a pink porthole [Observed: File:Bubble_Gun.png].
- **Firing:** "Will fire a blue projectile"; 800 u/s, 0.75 s rate of fire, 4 ammo, 3.5 s reload [Fan-wiki].
- **Projectile:** A blue projectile [Fan-wiki]. Not seen [Unverified]; no gameplay thumbnail found.
- **Impact / end result:** "When this projectile makes contact with any surface it will cause a big bubble to appear in the area where it was shot. After a second or two, this bubble will explode" [Fan-wiki]. Explosive 25–50; AoE 125/250; self-kill possible [Fan-wiki].
- **Images viewed:** `$V/sheets/g_prim2.jpg` (Bubble.jpg, Bubble_Gun.jpg, Bubble_Gun.png).
- **Depiction for shorts:** A blue glob splats, swells into a wobbling translucent bubble with a rainbow sheen borrowed from the BB0 art, then pops in suds and confetti. The BBG bubble look is a [BBG News invention].
- **Confidence:** partial (model only).

## Buster Cannon (primary; BBG 2.14, Nov 29, 2014)
- **Official text:** "Don't be a busta. Charge up your cannon and blow your enemies away with a powerful energy ball" [Game text via wiki]
- **Look:** a chunky arm-worn gauntlet cannon, about 0.45× Wil's height, covering most of his torso [Observed: File:Bustercannon.jpg]:
  - a gun-metal body with a mesh grille and two cone spikes;
  - an orange concentric-ring decal on the side;
  - a glowing pale-blue cube emitter at the front.
- **BB Zero ancestor ("Blaster Cannon"):** kitchen junk, namely a blue blender body, an orange spiral, salt shakers and an oven mitt [Observed: File:STORY_WEAPON.png], "powered by ABBi" [Fan-wiki]. Not BBG.
- **Firing:**
  - Semi-automatic energy orbs [Fan-wiki]. Uncharged shots do 20 damage with no AoE at 1,400 u/s [Fan-wiki].
  - A full 2.5 s charge gives 50–80 on a direct hit plus an AoE burst (150/300) at 1,500 u/s, and it spends the whole magazine. 100 ammo [Fan-wiki].
  - Trivia says it regenerates ammo [Fan-wiki]. HUDs read 100/100 and 0/100 [Observed].
  - Charge cue in the wiki: "a pulsating purple energy ring formed around the glove" [Fan-wiki]. In thumbnails it shows as swirling pink-magenta to violet rings with white cores wrapped around the gauntlet [Observed: i.ytimg.com/vi/evq-fk6i8Eo/hq1.jpg and hq3.jpg; 86mjqmdx708 hq2].
- **Projectile:** The orb itself is not isolated in any frame [Unverified].
- **Impact / end result:**
  - A pink-white burst on a hit enemy at 0/100 [Observed, low-res: icEIszkRrsA hq3].
  - Magenta electric crackle at the floor just after a shot, at 0/100 with RELOAD showing [Observed, low-res: 86mjqmdx708 hq1].
  - At full charge, an AoE burst around the orb [Fan-wiki].
- **Images viewed:** `$V/sheets/g_prim2.jpg`, `$V/crops/buster_low.png`, `$V/sheets/s_evq-fk6i8Eo.jpg`, `$V/crops/evq_max.png`, `$V/sheets/s_icEIszkRrsA.jpg`, `$V/sheets/s_86mjqmdx708.jpg`.
- **Depiction for shorts:** Pink-violet rings spin up around the glove and fire a pink-white plasma ball that bursts in a magenta crackle-ring. The ball's look is [Inference from the observed charge and hit colours].
- **Confidence:** partial.

## Snowtato Launcher (primary; BBG 2.26, Jan 17, 2017, with winter No Bear's Land)
- **Official text:** "A makeshift potato launcher convertor to weapon of frosty devastation. Shoot snowballs that explode and turn them into flakes!" [Game text via wiki]
- **Look:** the Señor Potato build in ice tones, about 0.45× Wil's height [Observed: File:Snowtato.jpeg]:
  - a lavender-blue frozen potato body (lit about #A7B7E6);
  - an ice-blue cup on top (#BDD9E0);
  - flat blue-grey side fins where the handlebars were (#6E7B9A);
  - a fat grey metal barrel (#545456–#888A8B).
  - At launch it had no menu model [Fan-wiki].
- **Firing:** Exploding snowballs; cooldown 2.2, 6 ammo, 4.5 s reload. It is the only Chub Scout primary that equipment does not affect [Fan-wiki]. One fan HUD reads 5/5 [Observed: _7wmOHdRMs4 hq1].
- **Projectile:** A snowball [Game text via wiki]. Not seen in flight [Unverified]. That video's fan title art shows a white snowball with flakes [Observed; fan art, not game].
- **Impact / end result:**
  - "Snow will remain present in the air in the Snowtato's area of effect for several seconds and block any explosives, even other Snowtato projectiles fired by the user" [Fan-wiki]. Explosive 35–65; AoE 150/300 [Fan-wiki].
  - In "BattleBearsRoyale 2.53.2 S4 Ep56: Snowtato Launcher Gameplay", a dense cluster of violet-indigo puffs (about #453267) hangs across the corridor [Observed: i.ytimg.com/vi/_7wmOHdRMs4/hq1.jpg, `$V/crops/snow_hq1.png`].
  - That this is the lingering snow is [Inference]. Why it is violet rather than white is [Unverified].
- **Images viewed:** `$V/sheets/g_prim1.jpg`, `$V/sheets/s__7wmOHdRMs4.jpg`, `$V/yt/_7wmOHdRMs4_maxresdefault.jpg`, `$V/crops/snow_hq1.png`, `$V/crops/snow_huds.png`.
- **Depiction for shorts:** A thunk, then a snowball bursts into a hanging cloud of chunky flakes. A second shot clinks off the cloud, per the wiki's blocking note. Keep the flakes white-lavender until gameplay is checked; that colour is a [BBG News invention].
- **Confidence:** partial.

## Batterito (secondary; default; BBR v1.3, May 3, 2012 → BBG → official 2026 trailer)
- **Official text:** "Set you mouth and you opponent's faces ablaze with fiery power of the batterito. Once consumed, fire will spew from your mouth and movement speed is increased until the inferno dies down." [Game text via wiki]
- **Look:** a bullet-shaped wrapped burrito hugged across the belly, **about 0.45–0.5× Wil's height long** (the draft's 0.3× was too small) [Observed: trailer 17.9 s, `$V/crops/batt_179.png`, `$V/crops/grid_179.png`; File:Wil.png]:
  - a dark grey wrapper (#554B4A–#6E656D);
  - a label band running green (#5CA021) → yellow (#F8E100) → orange (#FFA200), with "BATTERITO" in black block letters;
  - a dark band with small white text near the end;
  - a rounded yellow end cap (#FFDD17) with a pointed tip.
  - BLAST 2D (not BBG): a black wrapper with orange and yellow stripes, "BATTERITO" and "NUT FACT PEANUTS ARE NOT NUTS" [Observed: File:Batterup.jpg].
- **Firing (activation):**
  - He eats it. Damage starts "a second or two" later. Primary, melee and Specials are locked until it ends [Fan-wiki].
  - 70 DPS, +200 u/s [Fan-wiki]. Duration is 8 s in the infobox but "6 seconds" and "7-second" in the text [Fan-wiki conflict].
  - 2.6: damage 30→35, duration 10→6.5, reload 12→5 [Fan-wiki].
- **Official 2026 trailer** ("Battle Bears Gold Premium - Trailer") [Observed: `$T/t_0037.jpg`–`t_0048.jpg`; my extractions `$V/trailer/f_17.9.png`, `f_21.2.png`, `f_22.2.png`, `f_23.0.png`; tiles `$V/crops/tr_seq177.png`, `tr_seq186.png`]:
  - **17.8–17.9 s:** Wil (Booty Duty) hugs the Batterito at his belly.
  - **18.0 s:** both hands go to his mouth.
  - **18.5 s:** blue tears stream and his teeth clench.
  - **19.0 s:** arms fling out and his mouth gapes.
  - **19.5–20.0 s:** arms up, head back, as a yellow glow (#FFE241) floods in from the right.
  - **20.5–21.2 s:** seen from behind, he runs at a panda-faced bear in dark armour. Flame plumes billow beside his face; his red-and-black snack backpack is visible.
  - **22.0–22.2 s:** that bear stands lit pure white (#FFFFFF) amid fire, with orange smoke (#FF9227) rolling overhead.
  - **22.5–23.5 s:** the "Wil / CHUB SCOUT" card shows a thick flame jet from his crying, open mouth: yellow core (#FFE436), orange edges (#EEA13B). The jet runs toward a white-lit armoured bear.
- **Projectile:** None; a continuous mouth flame cone or jet [Game text via wiki; Observed].
  - Fan thumbnails show the same big orange-yellow fire cloud in front of Wil [Observed: rzGuh5Qga1Y hq1, "battle bears royale 1.3.1 batterito spamming w/ music"; -VwccFy5cuc hqdefault, "WIL'S LONGEST BATTERITO GAMEPLAY - Battle Bears Gold 2.27"].
  - The 2026 Playtest 4 thumbnail shows red-helmet Wil with blue tears and an open mouth [Observed: OqSi3rfMdl8 hq1]. That suggests the same "too hot" acting in 2026 [Inference].
- **Impact / end result:**
  - The target is lit white-hot. That Wil's flame did it is [Inference, supported by the title-card composition]. No knockback cue is visible [Observed].
  - With the Not-So-Slenderman skin, "the white spots where his eyes should be will grow into black eyes and a mouth will appear when he breathes the flame" [Fan-wiki].
- **Images viewed:** `$V/sheets/tr_a.jpg`, `tr_b.jpg`, `tr_c.jpg`, `$V/crops/tr_seq177.png`, `$V/crops/tr_seq186.png`, `$V/crops/batt_179.png`, `$V/crops/grid_179.png`, `$V/crops/tr_212.png`, `$V/crops/tr_222.png`, `$V/crops/tr_230.png`, `$V/sheets/g_sec2.jpg` (Wil.png, Batterito_(BBR).jpg, Batterup.jpg), `$V/sheets/s_rzGuh5Qga1Y.jpg`, `$V/crops/rzg_hq1.png`, `$V/crops/vwc_hqd.png`, `$V/crops/oq_hq1.png`.
- **Depiction for shorts:** Copy the trailer beat for beat: chomp, blue tears, clenched teeth, arms flung up, then a yellow-core, orange-edged flame jet while he sprints. The target flashes white. A sooty, blinking aftermath (no burns) is a [BBG News invention].
- **Confidence:** observed.

## Killdoba (secondary; BBR v1.3.1, June 28, 2012 → BBG)
- **Official text:** "\"Muy caliente\" is what you might say if you weren't so busy spewing fire and running faster than a burning, headless chicken. This mega-bean packs a punch but burns coming out twice, if you know what I mean." [Game text via wiki]
- **Look:**
  - A large burrito in crinkled white-silver foil with a tan tortilla end, hugged to the chest, about 0.3× Wil's height [Observed: File:Killdoba.jpg].
  - SkyVu banners show a white-wrapped burrito with red-brown chili filling bulging out [Observed: File:Paqueta.png; File:HungryScoutBundle.png, where Wil in a scout uniform holds two].
  - A BBR menu shot shows Dia De Los Muertos Wil and "HEALTH -5%" [Observed: File:Killdoba.png].
  - The infobox says "Primary", but the page category is Secondary [Fan-wiki error].
- **Firing (activation):**
  - A Batterito reskin: eat it, breathe fire for 4 s, gain +200 u/s. 70 DPS, 3 s reload [Fan-wiki].
  - 2.6: damage 37→45, duration 9→8, reload 13→7, health −5%→0 [Fan-wiki].
- **Projectile:** Mouth fire [Game text via wiki]. No Killdoba-specific frame is confirmed.
  - File:180px-Ci0oml.jpg (wiki caption "Tg the Killdoba") shows an orange-yellow fire burst down a corridor beside a cyan-lightning figure [Observed]. Nothing in it shows Wil [Unverified].
  - **Correction to the draft:** the "CRAZY BATTLE BEARS GOLD HACK/GLITCH! Killdoba fire lasting forever, facing temples" thumbnails show a non-Wil player, and **hq1 does show an orange-yellow fire patch** on the floor down the corridor [Observed: LOa3e4GyrCk hq1, `$V/crops/loa_hq1.png`]. Given the title, that may be lingering Killdoba fire [Inference].
- **Impact / end result:** As for the Batterito [Inference].
- **Images viewed:** `$V/sheets/g_sec2.jpg`, `$V/sheets/g_banners.jpg`, `$V/sheets/g_misc.jpg` (Killdoba.png menu), `$V/crops/ci0oml_x5.png`, `$V/sheets/s_LOa3e4GyrCk.jpg`, `$V/crops/loa_hq1.png`.
- **Depiction for shorts:** The same flame breath as the Batterito, then a comic after-burp puff. Making it bigger and redder is a [BBG News invention]. Skip the official text's toilet joke for 13+ tone.
- **Confidence:** partial.

## EZ Chee-Z (secondary; level 15; BBR v1.3, May 3, 2012 → BBG)
- **Official text:** "Chugging this can of cheese will cause you to swell up and explode, killing yourself and anyone unlucky enough to be caught in the blast." [Game text via wiki]
- **Look:** a spray-cheese aerosol can about 0.3× Wil's height, held up in one hand [Observed: File:EZ_Chee-Z.jpg; File:E-Z_Chee-Z.png shows a BBR menu with Dia De Los Muertos Wil]:
  - a white body (#F1F2F6) with a royal-blue lower half (#0474BB);
  - orange label marks;
  - an orange-yellow nozzle cap (#FECC27).
- **Firing (activation):**
  - "The player will shake the EZ Chee-Z can before eating its contents and bloating up to the point where the player will not be able to enter certain roofed areas". For 2 s he moves at "-50 u/s", then explodes [Fan-wiki].
  - Explosive 150–225 (the text says "minimum of 150 … peaks at 200"); AoE 150/400 [Fan-wiki].
  - "Shields will not prevent suicide". It has no reload and resets on death [Fan-wiki].
- **What I saw:**
  - In "EZ Cheese Spamming in the Noir" (greyscale), hqdefault shows a huge rounded body from behind [Observed]. hq1 is a BBR 1.3.0.1 menu with Dia De Los Muertos Wil holding the can [Observed].
  - In "KAMICHEEZE WIL!!!(EZ-CHEEZE GAMEPLAY)- Battle Bears Gold 2.24", Wil's beige back and shoulders fill most of the frame [Observed: 7fQLdyoldr4 hqdefault].
  - The BBR 1.3 trailer's "SECONDARY EDIBILITIES" thumbnail shows two over-the-shoulder clips (one with a blue helmet). Nothing there proves bloating [Observed: wNpM1woYv7k hq2]; that claim stays [Unverified].
- **Projectile:** None; he is the bomb [Fan-wiki].
- **Impact / end result:** A big blast centred on Wil that kills him and anyone in range [Fan-wiki]. The explosion's look was not seen [Unverified].
- **Images viewed:** `$V/sheets/g_sec.jpg`, `$V/sheets/g_sec2.jpg`, `$V/sheets/s_iSgdJ1qHmMA.jpg`, `$V/sheets/s_7fQLdyoldr4.jpg`, `$V/sheets/s_wNpM1woYv7k.jpg`, `$V/crops/wnpm_hq2.png`.
- **Depiction for shorts:** Shake, a glug, then Wil inflates into a beach ball, waddles slowly, and BOOMs. The orange-yellow cheese-cloud blast, the cheese-dusted crater and the sheepish respawn are a [BBG News invention]. Keep it cartoon, never gore.
- **Confidence:** partial.

## Whipped Pain (secondary; BBR v1.3.1, June 28, 2012 → BBG)
- **Official text:** "This hillarious party stunt is about to go all over the faces of your enemies. It may take a bit longer than the E-Z Chee-Z but the pay off packs a larger punch." [Game text via wiki]
- **Look:** a red (#FF1819) and white whipped-cream aerosol can with a red cap, about 0.3× Wil's height [Observed: File:Whipped_Pain.jpg]. HUD icon: a red and white can [Observed].
- **In-match:**
  - File:Images(2).jpg is captioned "Wil bloating up after using the Whipped Pain." [Fan-wiki caption]. It is a low-res copy of the same clip as the thumbnails of "Battle bears royale 1.3.1 whipped pain glitch?" and "…what the heck!? Whipped pain": same 0:22 timer, same 18–9 score [Observed: oA22vOD9KBI, gMz53R_72UI].
  - In those, Wil is seen from behind in a black suit, holding the red can in a white hand. His body fills much of the frame [Observed]. The draft's identification of the skin as Dia De Los Muertos is [Unverified].
- **Firing (activation):** As the EZ Chee-Z, but he explodes after 5 s, with a wider blast. Explosive 225–400; AoE 250/600; −10% health [Fan-wiki].
- **Impact / end result:**
  - In "CREAMICIDE WIL(WHIP PAIN GAMEPLAY)… Battle Bears Gold 2.30", hq2 shows a bloated Wil (red Monster Hoodie) holding the can up while a white spray streams from the nozzle [Observed, low-res: o8rEXLT4n_0 hq2, `$V/crops/o8_hq2.png`]. hq3 shows white puffs bursting near a distant enemy [Observed, low-res].
  - "Battle Bears F.U.N : amazing WHIPPED PAIN…" hq1 shows large flat white shapes covering much of the screen; the build stamp reads 2.53.6 [Observed: i.ytimg.com/vi/3Z65fUow2UQ/hq1.jpg]. Reading them as cream on the camera is [Inference]. Its hq3 shows Wil bloated in the Gift Wrapped skin [Observed].
  - The draft's "2024" date for that video is [Unverified]; I could not check the upload date.
- **Images viewed:** `$V/sheets/g_sec.jpg`, `$V/sheets/g_misc.jpg` (Images(2).jpg), `$V/sheets/s_oA22vOD9KBI.jpg`, `$V/sheets/s_gMz53R_72UI.jpg`, `$V/sheets/s_o8rEXLT4n_0.jpg`, `$V/crops/o8_hq2.png`, `$V/crops/o8_hq3.png`, `$V/sheets/s_3Z65fUow2UQ.jpg`, `$V/yt/3Z65fUow2UQ_maxresdefault.jpg`, `$V/png/Purple-Pain-bundle.png` (banner shows no weapon).
- **Depiction for shorts:** A long, ticking 5-second swell, with cream already spraying from the nozzle. Then a huge white whipped-cream blast plasters nearby bears' faces. The spray and white splats are observed; the cherry landing on top is a [BBG News invention].
- **Confidence:** partial.

## Sole's Bane (secondary; BBR 1.4.3, Apr 15, 2013 → BBG)
- **Official text:** "Wil doesn't want to share his toys but he's more than happy to share the pain of stepping on one of the buggers." [Game text via wiki]
- **Update-note text:** "-Sole's Bane: Wil leaves a trail of pain with colorful mines that sure to give any opponent a sore foot." [Fan-wiki transcription of SkyVu 1.4.3 notes; Unverified as Canon]
- **Look:**
  - An armful heap of interlocking toy bricks (red, green, yellow, blue, orange, white, black), about 0.35× Wil's height wide, held at the belly [Observed: File:SolesBane.jpeg].
  - The same heap is held in a match [Observed: RukIckwnibs hq2].
  - The HUD icon is an orange 2×4 brick [Observed: `$V/crops/ruk_hud.png`].
- **Firing (activation):**
  - "A pile of Lego bricks that Wil throws in the air when activated. It has small AoE … but does a lot of damage." "The throwing effect keeps going on even if the player dies" [Fan-wiki].
  - 50 damage, 4.5 s duration, 3 ammo, 2 s rate of fire, 3 s reload, +5% speed. Ammo+ equipment does not affect it [Fan-wiki].
  - 2.6: duration 4→6, reload 7→6, speed modifier 0→10% [Fan-wiki].
  - HUDs read 2/2 in 2.23 (RukIckwnibs) and 2/3 and 0/3 in "Legos....(SOLE'S BANE GAMEPLAY)- Battle Bears Royals 2.53" [Observed: V6FLnB_c_fk].
  - The "throws" (wiki) and "trail of mines" (update text) accounts differ. The duration stat fits bricks lying on the floor as timed caltrops [Inference].
- **Projectile / impact:** Neither the scatter nor the trigger was seen [Unverified]. V6FLnB_c_fk hq3 shows a pink-violet lightning burst near an enemy with Sole's Bane selected; its source is unclear [Unverified]. The draft attributed it to "another weapon" without evidence.
- **Images viewed:** `$V/sheets/g_sec2.jpg`, `$V/sheets/s_RukIckwnibs.jpg`, `$V/crops/ruk_hud.png`, `$V/crops/ruk_max.png`, `$V/sheets/s_V6FLnB_c_fk.jpg`.
- **Depiction for shorts:** Wil tosses the heap overhead and bricks rain into a colourful carpet behind him. A chasing bear steps on one and hops clutching its foot. The pop of sparks and the hop are a [BBG News invention].
- **Confidence:** partial.

## Pop Tart Shuriken (secondary; BBG 2.25, Mar 21, 2016)
- **Official text:** "Breakfast just got deadly." [Game text via wiki]
- **Release date:** The Versions table lists 2.25 with no date; the Updates page gives Mar 21, 2016 [Fan-wiki].
- **Look:** a six-pointed star toaster pastry, about 0.2× Wil's height across, held up in one hand [Observed: File:218426BB-3EEC-43E7-B36F-4EA0806BD23A_1.png]:
  - a tan crust rim;
  - white and pink frosting;
  - green, pink and yellow sprinkles;
  - a hole in the centre.
- **Firing:**
  - "Wil flings two Pop Tart themed shurikens in a straight line". They are "unaffected by gravity", travel at 1,600 u/s and have a "clip size of 3, which means a total of 6 Shurikens" [Fan-wiki].
  - 0.5 s rate of fire, 3 s reload [Fan-wiki].
  - Fan 2.25 HUDs read 4/8, 0/8 and 8/8 [Observed: uAtfV_9vEYc hq1–hq2, `$V/crops/pt_huds.png`; v9yFp06dn00 hq1]. That conflicts with the infobox [Fan-wiki vs Observed].
  - Its original "shining" sound on each throw was changed to one sound per press [Fan-wiki].
- **Projectile:** A rainbow-stripe trail (red, orange, yellow, green, blue, violet bands) with white star sparkles behind the pastry, matching the wiki's Nyan Cat note [Observed: i.ytimg.com/vi/uAtfV_9vEYc/hq1.jpg; q8a8noCNVcg hqdefault].
- **Impact / end result:**
  - A small explosion: explosive 10–30; AoE 50/150. It "cannot damage the user or explode enemy bodies" [Fan-wiki].
  - In "WIL THE POPTART NINJA!!!… 2.25", pink-red puff chunks scatter around the hit target [Observed: v9yFp06dn00 hqdefault]. Reading them as hit or explosion puffs is [Inference].
- **Images viewed:** `$V/sheets/g_sec2.jpg`, `$V/sheets/s_uAtfV_9vEYc.jpg`, `$V/sheets/s_q8a8noCNVcg.jpg`, `$V/sheets/s_v9yFp06dn00.jpg`, `$V/crops/pt_huds.png`.
- **Depiction for shorts:** A ninja double-throw. Two frosted stars streak in on rainbow trails with sparkle stars, then pop into pink frosting puffs. The sprinkle confetti is a [BBG News invention].
- **Confidence:** observed.

## Bow (melee; default; BBR v1.3, May 3, 2012 → BBG; seen in the 2026 final playtest)
- **Official text:** "Last time Wil got Bow and Arrow together certain words were exchanged and hearts were broken. They haven't spoken in weeks. Wil doesn't want to talk about it." [Game text via wiki]
- **Look:**
  - A plain wooden longbow with a taut pale string and a cream striped grip wrap, about 0.8–0.9× Wil's height, held upright at his side [Observed: File:Bbooww.jpg].
  - The same bow is held by "CLASSIC WIL" in the 2026 final playtest [Observed, low-res: MS2wiArCiCA hq3, `$V/crops/ms2_hq3b.png`].
  - The wiki says it is "probably the bow that the Huggable used to shoot Wil in Battle Bears -1" [Fan-wiki].
- **Firing:** None. It is a melee swing with the bow; no arrow is fired [Inference from the official joke].
  - "It deals 70 damage and does not have any Stat Modifiers"; same range as the Arrow [Fan-wiki].
  - 2.6 changed only its Melee+ values [Fan-wiki].
  - A large wooden bow arc crosses the screen in RukIckwnibs maxres, possibly mid-swing [Observed, low-res; Inference].
- **Projectile:** None.
- **Impact / end result:** Undocumented [Unverified].
- **Images viewed:** `$V/sheets/g_sec.jpg`, `$V/crops/ms2_hq3b.png`, `$V/crops/ms2_hq3c.png`, `$V/crops/ruk_max.png`, `$V/sheets/g_banners.jpg` (the Chubby Bundle shows a bow icon).
- **Depiction for shorts:** He swings it like a club. The string twangs ("THWANG") and the target sees stars. [BBG News invention]
- **Confidence:** partial.

## Arrow (melee; level 10; BBR v1.3, May 3, 2012 → BBG; wiki page "Arrow (BBG)")
- **Official text:** "Trusty old arrow. What say we get it stuck in someone else's leg this time?" [Game text via wiki]
- **Look:** a single wooden-shaft arrow about 0.6× Wil's height, gripped near the fletching and held upright like a short spear [Observed: File:Arrow.jpg]:
  - a pointed silver-grey head;
  - pale white to blue fletching.
- **Origin:**
  - BB-1 lore: a Huggable shot Wil with an arrow (in the knee). He pulled it out, used it as a weapon and to open vents, and calls it a "really rigid, pointy band-aid" [Fan-wiki: Arrow].
  - The BBG page says the BBG Arrow is "probably the one that was stuck in Wil's leg" [Fan-wiki].
- **Firing:** None; a hand-held stab or jab [Inference].
  - Now 45 damage and +15% health; 110,000 Joules [Fan-wiki].
  - 2.6: damage 45→55, health 0→10% [Fan-wiki]. Trivia: "Originally, the Arrow dealt 55 damage … before it was nerfed" [Fan-wiki].
- **Impact / end result:** Undocumented [Unverified].
- **Images viewed:** `$V/sheets/g_default.jpg` (Arrow.jpg).
- **Depiction for shorts:** A comic poke to the backside, a yelp and sparks. Keep it a poke, never a wound. [BBG News invention]
- **Confidence:** partial.

## Bow and Arrow (melee; probably BBG 2.16, Jan 30, 2015)
- **Official text:** "Wil's bow and arrow has made up and joined forces to fight against evil! Too bad Wil doesn't know how to use it still. Maybe next time.." [Game text via wiki]
- **Release conflict:** The Versions table lists it under both 2.13 (Oct 31, 2014) and 2.16 (Jan 30, 2015) [Fan-wiki]. Its page was created 2015-01-31, the day after 2.16 [Fan-wiki page history]. So 2.16 is likely [Inference].
- **Look:** the wooden bow with the arrow (grey head, white fletching) laid along it in one hand. The bow is about 0.8× Wil's height [Observed: File:Bowandarrow.jpg].
- **Firing:** None. Per the official joke he still cannot shoot it, so it works as a club [Inference].
  - Now 45 damage, −10% speed, +20% health; 150,000 Joules [Fan-wiki].
  - The first revision (2015-01-31) read 65 damage, −10% speed, +15% health [Fan-wiki page history].
- **Impact / end result:** Undocumented [Unverified].
- **Images viewed:** `$V/sheets/g_melee.jpg` (Bowandarrow.jpg).
- **Depiction for shorts:** He nocks the arrow, aims, fumbles, then whacks the bear with the whole bundle. [BBG News invention]
- **Confidence:** partial.

## Traffic Light (melee; no release version listed; probably BBG 2.13, Oct 31, 2014)
- **Official text:** "Why is there no yellow light you ask? Wil only travels in two modes. He stops and sometimes he has to go." [Game text via wiki]
- **Release:**
  - The page's first revision is dated 2014-11-01, the day after 2.13 [Fan-wiki page history].
  - 2.13 also added the Fatman skin [Fan-wiki: Versions], the skin Wil wears in the Traffic Light icon.
  - So 2.13's new melee was probably the Traffic Light [Inference].
- **Look:**
  - A yellow pole with black bands near the head and at the grip, topped by a dark grey angular signal head with a red lamp above a green lamp and no amber. About 0.8× Wil's height, shouldered like a mace [Observed: File:Trafficlight.png, `$V/crops/traffic.png`].
  - Wil wears the **Fatman** skin: a red cowl with ears, a grey suit, a gold bear chest emblem, a yellow-black belt, and red gloves and boots. It matches File:Fatman.PNG [Observed]. The wiki says Fatman "is a reference to Batman" [Fan-wiki].
- **Firing:** None; a melee club [Inference]. Now 45 damage, +10% speed, 150,000 Joules. The first revision read 12% speed and 200,000 Joules [Fan-wiki page history].
- **Impact / end result:** Undocumented [Unverified].
- **Images viewed:** `$V/sheets/g_melee.jpg` (traffic zoom, Trafficlight.png, Fatman zoom).
- **Depiction for shorts:** The lamp flips red ("STOP") as he bonks someone, then green ("GO") as he waddles off. [BBG News invention, from the official joke]
- **Confidence:** partial.

## Selfie Stick (melee; BBG 2.21, Jul 3, 2015)
- **Official text:** "But first, let me hit you with this!" [Game text via wiki]
- **Look:**
  - A yellow pole with a black-striped yellow grip, topped by a smiling yellow bear-face head, about 0.7× Wil's height [Observed: File:Image7.PNG, low-res, `$V/crops/selfie.png`]. That the head is a phone in a bear case is [Inference].
  - Wil wears the **Lunchador** skin: a red luchador mask with gold trim, red trunks and wristbands, and a bare furry chest. It matches File:Lunchador.png [Observed].
- **Firing:** None; a melee club [Inference]. 45 damage, −20% health, +20% speed; 125,000 Joules [Fan-wiki].
- **Impact / end result:** Undocumented [Unverified].
- **Images viewed:** `$V/sheets/g_melee.jpg`, `$V/sheets/g_skins.jpg`.
- **Depiction for shorts:** A selfie flash pops in the target's face, then the bonk. [BBG News invention]
- **Confidence:** partial.

## Sarcastic Air Strike (BBH ultimate only; not in BBG)
- **Official text:** "His Ultimate, "Sarcastic Air Strike," features A.B.B.I., his mocking robot backpack, executing a devastating airstrike, raining destruction across the battlefield." [Canon] (battlebears.com/pages/characters, fetched today). The page names no game; BBH-only status is [Inference] from its "Ultimate" terminology and the wiki's BBH update.
- **Status:** BBH "Reworked Wil Attack and Ultimate" on June 20, 2023; Wil's reload went 1.5 s→1.3 s on Aug 29, 2023 [Fan-wiki: Updates]. No BBG or BBG 2026 equivalent was found [Unverified].
- **Look, firing, impact:** No visual opened [Unverified]. In BBG, ABBi is a grey shell with a large camera lens [Observed: File:Wil's_backpack.png; r7TipV3IYtI hq1].
- **Depiction for shorts:** Only in BBH-labelled content: ABBi's lens flashes, she sighs a sarcastic line, and a cartoon bombing run pounds the area. [BBG News invention]
- **Confidence:** documented (text only).

---

## Corrections to the previous inventory (arsenal_wil.json and the draft)
1. **Boomstick "small red mark":** it is a red two-digit LED readout ("00") on the receiver [Observed: BoomBoom.png zoom; SkyVu 2012 animation test].
2. **EZ Chee-Z in the BBR 1.3 trailer:** the "SECONDARY EDIBILITIES" clips do not prove bloating; one shows a blue team helmet [Observed]. Mark it [Unverified].
3. **The 2026 trailer skin is Booty Duty** (unidentified in the arsenal). Its backpack is **red-and-black** (team-coloured), not black.
4. **Traffic Light icon skin = Fatman** (the arsenal said "red-masked superhero-style skin").
5. **Pie Bomb:** SkyVu's 2.2 recap captions it "Wil Primary Weapon" with a 2/2 HUD [Canon caption; Observed]. Gameplay is third-person over the shoulder, not first person.
6. **Batterito size:** about 0.45–0.5× Wil's height, not 0.3×.
7. **Team colours:** evq-fk6i8Eo is a blue Monster Hoodie, not a blue helmet. Team colouring of the helmet, print and pads rests on wNpM1woYv7k hq1 and the concept File:Wil_skin.png.
8. **"CLASSIC WIL" (2026)** is a headband look with ABBi, not the red-helmet default.
9. **Elbow pads** carry red lights, like the knee pads.
10. **Killdoba glitch video:** hq1 shows a fire patch; the source is unattributed.
11. **Sole's Bane hq3 lightning:** the source is unclear.
12. **Clip-size observations** were added for the Boomstick (3 and 1), Señor Potato (4 and 6), Pie Bomb (2 then 4), Chainsaw Shotgun (4 then 2), Sole's Bane (2 then 3) and Pop Tart (8).
13. **Era key:** BBG updates ran to 3.0.1 (Dec 18, 2021), not "about 2018".

## Corrections for the character file (`/home/user/thallo-site/bbg-news-repo/characters/wil.md`)
1. **Look, line 49.**
   - Current: "Exception: no researcher has described his BBG 2013 in-game default, so until it is checked the model uses the closest observed proxies." … "outfit from the March 2012 BBR animation-test frame, "a brown bear in a red cap, white shirt and a grey backpack" [Observed, low-res]"
   - Correction: describe the observed default.
     - Red padded helmet with vent dimples and a black chin strap.
     - White ribbed tank top with a red ice-pop print.
     - Black elbow and knee bands with red-lit pads.
     - Grey ABBi backpack with a large camera lens.
     - The helmet, print and pad lights are team-coloured (blue on blue team) [Observed concept; Inference].
     - The "red cap" in SkyVu's March 2012 animation test is this padded helmet.
     - In 2026, playtest matches still show the red helmet, but a separate skin named "CLASSIC WIL" is a plain tan bear with a red tied headband and ABBi. Which is the 2026 default is unverified.
   - Evidence: i.ytimg.com/vi/r7TipV3IYtI/hqdefault.jpg, hq1, hq3 ("Wil Animations 21/03/2012", SkyVu channel); File:Wil_default.png, Arrow.jpg, Bbooww.jpg, Doomstick.jpg, Wil's_backpack.png; File:Wil_skin.png; wNpM1woYv7k hq1; OqSi3rfMdl8 hq1; MS2wiArCiCA hq1–hq3.
2. **Line 49.**
   - Current: "The research never describes his BBG trailer card ([Steam][steam]) or the 2026 playtest showcase ([fan upload][showcase]); check both before locking the model."
   - Correction: The Steam trailer's "Wil / CHUB SCOUT" card (22.5–23.5 s) shows Wil in the Booty Duty skin: red headband, pink-white tank, red shorts, striped wristbands and leggings, and a red-and-black snack-covered backpack. He eats a Batterito at 17.8–20 s and breathes a yellow-core, orange-edged flame jet [Observed]. The JustNubz showcase is still unwatched; its thumbnails show no Wil.
   - Evidence: `$T/t_0037`–`t_0048.jpg`; `$V/trailer/f_17.9.png`, `f_21.2.png`, `f_23.0.png`; File:Booty_duty.png; wiki Booty Duty page.
3. **Colours, line 51.**
   - Current: "Unsampled picks [BBG News invention]: cap #C8352E, shirt #F2EFE6, ABBi grey #8B9299, eyes #141414, ice pop #3FA7E0."
   - Correction:
     - Helmet (not cap) #CF0012 lit to #9C040E shaded.
     - Shirt #E0E0DE.
     - Shirt ice-pop print #D50010–#DD0110 (red team).
     - ABBi shell #525253–#595A59, lens #62778C (menu lighting).
     - Card ice-pop prop #05C0DD.
     - Keep eyes as a pick.
   - Evidence: median crops of File:Wil_default.png, Arrow.jpg, Wil's_backpack.png, Wil_description.jpg (sample.py output in this session).
4. **Colours, line 51.**
   - Current: "researcher's estimates from the 2024 portrait, not official [Inference]: fur #D8AC57, mid #B88A46, shadow #754F26, light #DFCA95."
   - Correction: Add BBG-era samples: menu-render fur #A56C20 (shaded forehead) to #B07B40 (muzzle). The BBG model is a deeper orange-brown than the BBH portrait. The c.2012 card's fur samples about #DAA849.
   - Evidence: crops of File:Wil_default.png and File:Wil_description.jpg.
5. **Weapons & props, line 54.**
   - Current: "**Weapons & props:** default Boomstick [Fan-wiki] ([Chub Scout (BBG)][ws]), named in BBH [Canon] ([characters][chars]); BB-1's "arrow that he pulled from his leg" and "Boomstick McShootington" [Press] ([TouchArcade][ta]); Senor Potato, Pie Bomb, Traffic Light [Fan-wiki]; blue ice pop [Observed]."
   - Correction: List the full BBG kit.
     - Primaries: Boomstick, Doomstick, Balance Beam, Señor Potato, Pie Bomb, Chainsaw Shotgun, Bubble Gun, Buster Cannon, Snowtato Launcher.
     - Secondaries: Batterito, Killdoba, EZ Chee-Z, Whipped Pain, Sole's Bane, Pop Tart Shuriken.
     - Melees: Bow, Arrow, Bow and Arrow, Traffic Light, Selfie Stick.
     - Default loadout: Boomstick, Batterito, Bow.
     - Pie Bomb is captioned "Wil Primary Weapon" in SkyVu's 2.2 recap [Canon caption].
     - BBG's Boomstick is a hitscan pump shotgun with no splash [Fan-wiki]. The "explosive pellets" Boomstick is the BBH version [Canon text; BBH by Inference].
     - Keep the blue ice pop, but label it as the c.2012 card's snack prop [Observed]. It is distinct from the team-coloured ice-pop print on his BBG shirt.
   - Evidence: wiki class page and Category:Chub Scout; BcEeAzXFChI maxres caption; battlebears.com/pages/characters; File:Wil_description.jpg; File:Wil_skin.png.
6. **Fighting, line 61.**
   - Current: "**Fighting:** "a highly situational class" with "a wide variety of explosive weapons" [Fan-wiki] ([Chub Scout (BBG)][ws]); ABBi's "Sarcastic Air Strike" [Canon] ([characters][chars])."
   - Correction: Mark Sarcastic Air Strike as BBH only. In BBG his signature beats are the edibles: Batterito fire breath (official 2026 trailer [Observed]) and the EZ Chee-Z / Whipped Pain inflate-and-explode [Game text via wiki].
   - Evidence: trailer frames t_0037–t_0048; wiki EZ Chee-Z and Whipped Pain descriptions; the battlebears.com text uses BBH "Ultimate" wording.
7. **Prompt pack, line 76.**
   - Current: "red cap, white shirt; compact grey robot backpack with one camera-eye lens; chunky cartoon shotgun; alternate pose with a dripping blue ice pop;"
   - Correction: "red padded sports helmet with black chin strap, white ribbed tank top with a red ice-pop print, black elbow and knee bands with glowing red pads; compact grey robot backpack with one camera-eye lens; dark grey pump shotgun with a small red digital readout; alternate pose with a dripping blue ice pop;"
   - Evidence: r7TipV3IYtI hq1 (official); File:Wil_default.png; BoomBoom.png zoom; File:Wil_description.jpg (ice-pop prop).
8. **Video prompt, line 77.**
   - Current: "A round golden-tan teddy-bear soldier in a red cap, with nub hands and a one-eyed robot backpack"
   - Correction: "A round golden-tan teddy-bear soldier in a red padded helmet, with nub hands and a one-eyed robot backpack"
   - Evidence: r7TipV3IYtI thumbnails; BBG loadout renders; 2026 playtest thumbnails OqSi3rfMdl8 hq1 and MS2wiArCiCA hq1.
9. **Canon vs invention ledger, line 84.**
   - Current: "the red-cap look as default [Observed + Inference]"
   - Correction: "the red padded helmet as default [Observed: SkyVu 2012 animation test; BBG loadout renders]"
   - Evidence: as above.
10. **Open questions, line 88.**
    - Current: "what his BBG card and 2026 default skin show (red cap? ABBi?)"
    - Correction: Partly answered.
      - The trailer card uses Booty Duty, whose snack backpack is not ABBi.
      - 2026 playtest matches show the red padded helmet.
      - A 2026 skin named "CLASSIC WIL" is a headband-wearing tan bear with ABBi.
      - Still open: which skin is the 2026 default, and whether 2026 changed his kit.
    - Evidence: trailer frames; OqSi3rfMdl8 hq1; MS2wiArCiCA hq1–hq3; wiki Gift Wrapped trivia.
11. **Signature skins, line 55** (addition).
    - Current: "**Signature skins** [Fan-wiki] ([Chub Scout (BBG)][ws]): Gold Wil, Old Timey, Monster Hoodie, Lunchador, Sleepover, Chub Scout."
    - Correction: Add the skins seen on weapons:
      - Booty Duty (2026 trailer);
      - Fatman (Traffic Light icon);
      - Lunchador (Selfie Stick icon);
      - Gift Wrapped (Boomstick, Balance Beam and Doomstick renders);
      - Dia De Los Muertos (BBR EZ Chee-Z and Killdoba menus);
      - Not-So-Slenderman (BBR Doomstick menu);
      - "Classic Wil" (2026 final playtest).
    - Evidence: File:Booty_duty.png, Trafficlight.png, Image7.PNG, BoomBoom.png, Balancebeam.png, Wil_doomstickers.png, E-Z_Chee-Z.png, Killdoba.png, Doomstick.png; MS2wiArCiCA hq2.

## Open questions
- What do the Bubble Gun's blue projectile and bubble, and the chainsaw in flight, look like in BBG? No gameplay frame was found.
- What colour is the Buster Cannon orb? The charge rings and hit bursts are pink-magenta, but the orb itself is not isolated.
- What does the Balance Beam beam look like at full resolution?
- Is the Snowtato's lingering cloud really violet, or white tinted by lighting or team?
- What do the Señor Potato fries look like on the ground, and does the spud visibly burn in flight? "Flaming spuds" comes only from the wiki's transcription of the 1.4.3 notes.
- Sole's Bane: does Wil throw the bricks in the air, or leave a trail of floor mines? Neither the scatter nor the trigger has been seen. And what is the pink-violet lightning in V6FLnB_c_fk hq3?
- What do the EZ Chee-Z and Whipped Pain explosions look like, and does the white spray from the Whipped Pain nozzle start before the blast?
- Clip sizes changed across versions (Boomstick 3 vs 1; Señor Potato 4 vs 6 vs 3; Pie Bomb 2 vs 4; Chainsaw 4 vs 2 vs 3; Sole's Bane 2 vs 3; Pop Tart 8 vs 3). When did each change, and how did v3.0's removal of +1 equipment and Equipment Slot 2 affect them?
- When was the Boomstick's K/D damage scaling removed?
- Which skin is Wil's 2026 default: the red-helmet look seen in matches, or the "CLASSIC WIL" headband skin? Did any Chub Scout weapon change, get renamed or get removed for 2026? The Pie Bomb, Bow and Batterito are seen in 2026 material; the others are unverified. Watch the JustNubz showcase from 28:11 and check SkyVu's launch patch notes.
- Is the 2.13 melee the Traffic Light, with Bow and Arrow in 2.16 (page histories point that way)?
- Which skin is the black-suited, white-handed Wil in the 2012 Whipped Pain clips (Dia De Los Muertos or another)?
- SkyVu's BBG 2.6 change log and the archived blog remain unreached: web.archive.org reset connections, and its availability API returned "Temporarily Offline" today.
