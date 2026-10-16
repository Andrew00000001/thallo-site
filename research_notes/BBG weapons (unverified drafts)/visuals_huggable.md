# Huggable (BBG) weapons dossier

**The class.** The Huggable is BBG's melee class. It has 90 health and the highest base speed of any class. Its primaries and secondaries are abilities, not guns, and it cannot switch away from one until the recharge finishes, so it leans on its paired melee weapons [Fan-wiki: Huggable (BBG) wikitext, re-fetched today]. The Steam page lists "-HUGGABLE: Huggable" and promises "80+ PRIMARY WEAPONS / 60+ SECONDARY WEAPONS / 50+ MELEES", with release on Nov 4, 2026 [Canon: Steam appdetails API, fetched today].

**The kit is 18 weapons** [Fan-wiki class page]:
- Primaries: Double Rainbow! (default), Headlights, So Fly, Static Shuffle, Losing Your Head.
- Secondaries: Tough Love (default), Mini Me, Peek A Boo, Super Size Me!, Phantom Hug, Charged Run.
- Melee: Bite Me (default), Seesaw, Whack-Tus, Presidentures, Punk Bands, Bearettas, Beaver Feaver.

**Mapping error.** weapons_by_class.json["Huggable"] wrongly adds 7 Soldier weapons: A Salt Rifle, Heavy A Salt Rifle, Soaker, Spreadshot (BBG), Steamshot, B.E.A.R. Club and Krikkit Bat. Each page's Class field or category says Soldier [Fan-wiki, checked today]. They come from a Soldier changelog pasted under "BBR Version 1.0" on the Huggable (BBG) page, which also lists Bearzooka and Oliver skins [Fan-wiki wikitext].

**Sources I reached today:**
- Fan-wiki MediaWiki API (all 18 weapon pages, the class page, version pages, Status Effects, Happy Hour, Metal Crush) and wiki images.
- The local official Steam trailer and screenshots.
- Steam appdetails.
- battlebears.com/pages/characters and the plush product page with its product images.
- YouTube oEmbed titles and one watch page's metadata. Videos themselves are LOGIN_REQUIRED, so I used thumbnails only. I watched no YouTube video.

**Sources I could not reach.** web.archive.org reset every connection: 18 curl attempts with backoff, the CDX API, and WebFetch (refused). So no official SkyVu patch note was read. Every per-version stat change below is the wiki's transcription [Fan-wiki].

**Method notes.**
- I extracted 2026 trailer frames from the local official trailer: tr/g_N at about 29.8 + (N-1)x0.1 s; tr2/r_N at 34.4 + (N-1)x0.2 s; tr2/s_N at 35.9 + (N-1)x0.1 s.
- Hex colours are sampled from the images with a 3x3 to 11x11 mean, so they are approximate.
- Scale: the BBG News chart sets Oliver = 1.0x and the Huggable at about 0.65x [BBG News invention]. Weapon sizes below are proportions measured on Gear Up renders [Inference] multiplied by 0.65.

**Model notes that apply to every weapon** [Observed]:
- 2013 3D model and 2026 trailer: hot pink. 2013 render mid tone about #B8377C with highlight #EC84BD. 2026 lit about #F06598 to #FD7FB1, shadow #9D2B56.
- Face: red glossy button eye with a stitched scar running up to the cream head bandage, a small black dot eye and a huge white grin.
- Head gear: green radio box with a thin silver antenna and a red ball tip.
- Body: zip-stitched chest scar, and a torn belly or chest showing grey-white crumpled filling.
- Wrists:
  - 2013 melee Gear Up renders: bare.
  - December 2013 ability renders (LYH.jpg, ChargedRunStance.jpg): dark grey cuffs, each set with a round glowing red light.
  - 2026 trailer (32.6 s): the same red-light cuffs.
  - 2D menu cards and 2012 art: dark or metal cuffs with blue gems. 2012 art also has a metal knee brace.

---

## Double Rainbow! (primary ability; default; BBR 2012 to BBG; not seen in 2026)

**Official text:** "Attack in all directions for a brief period of time. Use when diving into large groups of hapless victims!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Double_Rainbow!)

**Status and era:**
- Default primary [Fan-wiki].
- A BBR Gear Up "PRIMARY" screen uploaded to the wiki 2012-10-24 lists it first, above HEADLIGHTS (EQUIPPED) and SO FLY [Observed: Double_Rainbow.png; upload date from wiki file metadata]. Stat bars: EXPLOSIVES, AOE, DURATION, COOLDOWN [Observed].
- BBR 1.4.2 (28 Feb 2013): minimum damage 50 to 55 [Fan-wiki].
- BBG 2.2 (21 Aug 2013): it stopped spinning after the Huggable died [Fan-wiki class trivia].
- BBG 2.6 (20 Dec 2013): minimum 55 to 25, maximum 80 to 40, duration 3 to 5 [Fan-wiki].
- Current infobox: Explosives 45-90 per second, AoE, duration 4.0 s, recharge 7 s. The 4.0 s conflicts with 2.6's 5 [Fan-wiki].
- 2026: absent from the trailer and screenshots [Observed absence].

**Look:**
- 2013 menu card: the pink Huggable leans back mid-air with a small "o" mouth and a tear, arms out, dark wrist cuffs with blue round gems [Observed].
- Two broad rainbow arcs, each about six bands and rimmed in neon-green glow, sweep round its waist from left and right like an orbit ring. The whole orbit is about 1.8x the Huggable's width, about 1.2x Oliver [Observed; size Inference].
- Band colours, sampled: violet about #5F00F1, magenta #DC00DF, red, yellow #F0F715, green #2BDA40 to #26FA35, cyan #27E8EF, blue #1A35B1 [Observed].
- Icon: grinning pink face flanked by rainbow arcs on both sides [Observed].
- Possible in-game look: the official "BATTLE BEARS ROYALE Sneak Peek" (BATTLE BEARS channel, published Aug 31 2011 [Canon: watch-page metadata]) has an auto-frame showing a pink Huggable hugging a blue-and-white bear [Observed].
  - A flat, wide rainbow ribbon lies across the grass, bands from outside in: orange, yellow, green, cyan, lilac [Observed].
  - The HUD shows "CHARGING" over an icon that looks like a face flanked by violet and rainbow shapes [Observed].
  - Reading the icon as Double Rainbow and the ribbon as its effect is [Inference]. This is a pre-launch build.

**Firing:**
- One tap, centred on the Huggable. It "creates two spinning rainbows that rotate around the user" for several seconds. Melee cancels it early [Fan-wiki].
- Sound undocumented [Unverified].

**Projectile:** none. The rainbows orbit the user [Fan-wiki].

**Impact / end result:**
- Explosive-type damage to anyone within range, falling off with distance [Fan-wiki: infobox].
- Explosions+ raises the damage. With Flawless Disguise it causes self-injury [Fan-wiki].
- Near the end, "the range of the two rainbows will slowly decrease until they completely disappear" [Fan-wiki].
- No hit visuals documented [Unverified].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Photo_27-04-13_11_29_40_AM.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/primary_cards.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Double_Rainbow.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sneak_sheet.jpg (built from https://i.ytimg.com/vi/IucMFqzR_Qw/hq1.jpg, hq2.jpg, hq3.jpg, hqdefault.jpg)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sneak_icon.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sneak_bottom.png

**Depiction for shorts:** two flat, glossy rainbow ribbons with green-glow edges whip round the Huggable at waist height like a rotor, then shrink to nothing. Bears in range tumble away in rainbow confetti [BBG News invention, following the card and the wiki's shrinking-range text].

**Confidence:** partial.

---

## Headlights (primary ability; the class's only long-range attack; BBR by Feb 2012 to BBG; not seen in 2026)

**Official text:**
- "Remove your head and fire out a cutting death beam of rainbow essence. This is the Huggable's only ranged attack!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Headlights)
- Related SkyVu wording: "Limited Edition Huggable Pink Battle Bear Plushie comes with a unique detachable head that uncovers a secret rainbow beam, the source of the Huggable's power!" [Canon] (https://battlebears.com/products/huggable-plushie-with-in-game-bonus, fetched today)

**Status and era:**
- 32,000 Joules, level 4 [Fan-wiki].
- BBR 1.2.1.1 (3 Feb 2012): "Fixed bugs including the one caused by the Soaker and Headlights" [Game text via wiki: Updates page].
- BBR 1.4.2: damage 40 to 45 per second, duration 2.7 to 4.0 s [Fan-wiki].
- BBG 2.1 (15 Jul 2013): range "significantly shortened" and Damage+ no longer applied, per the usage text. The trivia contradicts this on which equipment applies [Fan-wiki].
- BBG 2.2: it stopped firing after death [Fan-wiki].
- BBG 2.6: damage 45 to 35, duration 4 to 5 [Fan-wiki].
- Infobox: 60 damage per second, 5 s, recharge 6 s, range 1250 units. The usage text says a 5 s recharge [Fan-wiki].
- 2026: not seen [Observed absence].

**Look:**
- 2013 menu card: the head is off and held low at the Huggable's side, still wearing radio, antenna and tear. A white sparkle burst sits at the neck stump [Observed].
- A straight, wide beam runs out horizontally. Bands top to bottom: violet #3C0589, purple #60077A, magenta #920C55 to #C81462, orange #D99912, yellow #DAEC18, green #3DCA26 to #25EC5C, cyan #22B0D5, blue #163F74 [Observed, sampled].
- The beam is about as thick as the head: about 0.3x the Huggable's height, about 0.2x Oliver [Inference]. The card also shows a metal knee brace and a blue-gem cuff [Observed].
- Icon: face with a white burst and a rainbow band [Observed: Double_Rainbow.png list].
- Official plush design sheet on battlebears.com: a headless pink body with a jagged, lightning-shaped rainbow ribbon (purple, red, green, blue, yellow) bursting up out of the neck, the grinning head lying beside it [Observed].
- The plush photo shows a rainbow-striped satin handkerchief pulled from the neck opening [Observed].

**Firing:**
- One tap. The Huggable "takes off its head and shoots a rainbow beam", a "long, continuous rainbow beam lasting a few seconds". The player steers by aiming and cannot melee while it fires [Fan-wiki].
- Glitch: it pulls off a Hannible-skin head whatever the skin [Fan-wiki].

**Projectile:**
- A continuous beam [Fan-wiki].
- Said to be inspired by the BB-1, Zombies and Zero headshot death, where the head "would fly off far into the distance, leaving behind a trail of rainbows" [Fan-wiki].

**Impact / end result:** sustained damage while the beam stays on target [Fan-wiki]. No hit visuals documented [Unverified].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Photo_27-04-13_11_29_41_AM.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/primary_cards.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Double_Rainbow.png (icon in list)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/plush/BATTLE-BEARS_Huggable_Plush_1800x1800.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/plush_beam.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/plush/BB_Huggable_Plush_comp_1200x1200.png

**Depiction for shorts:** it lifts its head off with both paws and tucks it under one arm. A white sparkle pops at the neck and a straight, head-thick rainbow laser (violet on top to blue on the bottom) sweeps across. Afterwards it pops the head back on [card and plush art; the re-attachment is BBG News invention].

**Confidence:** partial.

---

## So Fly (primary ability, movement attack; BBR 2012 to BBG; likely in the 2026 trailer; BBH Ultimate)

**Official text:**
- "Fly forward with a burst of speed while damaging all in your way. Also very useful for getting around the maps! Aim up fly up!" [Game text via wiki] (https://battlebears.fandom.com/wiki/So_Fly)
- BBH: "Huggy's Ultimate, So Fly, allows him to soar across large parts of the map, dealing increased damage to enemies for a short period when he lands." [Canon] (https://battlebears.com/pages/characters, fetched today)

**Status and era:**
- 60 Gas, level 6. Originally 25,000 Joules, moved to Gas in BBR 1.4.2 [Fan-wiki].
- In the October 2012 Gear Up list [Observed].
- v2.0 added mid-air steering; v2.0 is the BBG launch numbering [Inference from the wiki BBR page].
- BBG 2.2: death fix. BBG 2.6: speed 500 to 510, damage 50-70 to 60-80, tired time 5 to 4 [Fan-wiki].
- Infobox: Explosives 15-30 (conflicts with the usage text's 60-80), 3 s, recharge 9.5 s, 575 u/s [Fan-wiki].

**Look:**
- 2013 card: the Huggable flies horizontally head first in a Superman pose, one arm forward wearing a blue-gem cuff [Observed].
- A wavy rainbow trail streams from its feet: violet #5D00EB, magenta #A309A0, red #DF181E, yellow #E6F71F, green #2DC138, cyan #27DFED, blue #0F27F1. A white sparkle burst sits where the trail meets the body, with sparkles in the trail [Observed, sampled].
- Icon: face with a rainbow trail [Observed].

**2026 official trailer, about 30.1-30.8 s** [Observed: g_004 to g_011]:
- The pink Huggable climbs up from below a ledge (30.1-30.3 s).
- It rises on a broad, translucent vertical light column: orange-red at the top (#FE9558, #A8641F), bright yellow in the middle (#FFF671) and a green fringe on one edge (#82DC4A, #47AB47).
- It then flies horizontally, belly down and head first, arms swept back, antenna up (30.5-30.8 s).
- Identifying this as So Fly is [Inference]: the pose matches and there is no HUD.

**CORRECTION to the earlier inventory:** the huge magenta crystal-shard pillar with a white core and a flat magenta floor ring is not So Fly's effect. It erupts at the take-off spot from about 30.7 s and lingers to about 32.4 s.
- It matches the wiki's in-game screenshot captioned "Happy Hour explosion", which shows Tillman's Demo secondary [Observed: happy_hour_explosion.png].
- Red finned missiles with yellow flame tails fall through the same shots at about 30.3, 31.4, 31.6 and 32.6 s, right after Tillman's splash card. They match the Happy Hour item render [Observed: g_006, g_017, g_019, g_029, hh_compare.png].
- So that FX is most likely Happy Hour [Inference].
- Steam screenshot 01 is a still of this moment [Observed].

**Firing:**
- One tap. The Huggable itself is the projectile. It can go any direction, including up, and is steerable since v2.0 [Fan-wiki].
- It can reach places no other class can, such as the Shortest Parsec Easter egg [Fan-wiki].

**Projectile:** the Huggable in "a stream of rainbows" [Fan-wiki].

**Impact / end result:**
- Contact damage of 60-80, depending on proximity and time in contact [Fan-wiki].
- No hit FX seen [Unverified].
- BBH adds a damage boost after landing [Canon].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Photo_27-04-13_11_29_45_AM.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/primary_cards.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Double_Rainbow.png
- Trailer frames: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/tr/g_006.jpg (30.3 s), /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/tr/g_008.jpg (30.5 s), /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/tr/g_010.jpg (30.7 s), /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/tr/g_011.jpg (30.8 s)
- Trailer crops: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/launch_seq.png, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/col09.png, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/hug_fly_crops.png, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/magenta_fx.png, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/tr_sheetA.jpg
- Steam screenshot: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/steam_screens/screen_01.jpg
- Happy Hour reference: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/ref/happy_hour_explosion.png, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/ref/hh_compare.png

**Depiction for shorts:** a crouch, a pop upward on a translucent orange-yellow-green light column, then a head-first Superman streak with a wavy seven-band rainbow contrail and white sparkles at its feet. Bears it clips spin away in sparkles [2026 column observed; contrail from the card; the knock-away is BBG News invention]. Do not reuse the magenta crystal pillar, which is Tillman's Happy Hour [Inference].

**Confidence:** partial (the card is observed; the 2026 flight is observed but identified by inference).

---

## Static Shuffle (primary; chargeable short/mid-range "shotgun"; BBR 1.4.3, April 2013, to BBG)

**Official text:**
- "This mid-range attack might just be enought to spark your opponent's demise!" [Game text via wiki, typo as quoted] (https://battlebears.fandom.com/wiki/Static_Shuffle)
- Release note: "Static Shuffle: Huggable's mid-range attack! Charge up and watch electricity fly! Damage and size depend on charge length." [Game text via wiki: BBR store notes as transcribed on https://battlebears.fandom.com/wiki/Battle_Bears_Royale ; the Updates page truncates it to "charge leng,"]

**Status and era:**
- BBR 1.4.3, dated April 15, 2013 on the Updates page. The BBR infobox says it went out as 1.4.3.1 on April 23, 2013 [Fan-wiki].
- 60 Gas, level 1. Originally 180 Gas, then the most expensive weapon. It is the only Huggable primary that Damage+ affects [Fan-wiki].
- It is absent from the October 2012 primary list [Observed].
- No later reworks recorded. Not seen in 2026.

**Look:**
- 2013 card: the head is pushed high on a long, stretched, stitched neck rising from a frayed collar. Open-mouthed happy face, wide eyes, antenna with a blue tip [Observed].
- Four jagged lightning bolts radiate around it, white core (#C5EBEE) with cyan-teal edges (#5B979C). Blue-gem wrist cuff [Observed].
- Concept sketches A, B and C, white line on black [Observed: 551341_….png]:
  - A and B show the Huggable with paws pressed to its head among lightning bolts. This matches the wiki's "rubs its head" charge [Inference].
  - Only C shows the head raised on a stretched neck, eyes shut happily.
  - The wiki labels them "Concept art". Uploaded 2013-04-14 [wiki file metadata]. The Facebook-style filename suggests a SkyVu Facebook post [Inference; Unverified].
- HUD icon: a pale blue-tinted Huggable face flanked by white-cyan lightning, with "CHARGING" over it while recharging [Observed: fan thumbnails by Dban1, 2013].

**Firing:**
- Tap for an uncharged blast, or hold or double-tap to charge for up to 6 s [Fan-wiki].
- While charging, "the Huggable rubs its head on its body to induce frictional static electricity" with a high-pitched static sound that "gradually becomes louder and more harsh" [Fan-wiki].
- A full charge is "much more violent and shining" [Fan-wiki].

**Projectile:**
- "a bright blue blast of electricity is shot from where the Huggable's head should have been" [Fan-wiki].
- Short range. The charged blast reaches further. 60 damage uncharged, 75 charged; reload 2.5 s [Fan-wiki].
- Size depends on charge [Game text via wiki].

**Impact / end result:**
- "small electrical particles will remain present in the air for several seconds" and damage enemies who touch them. No self-damage [Fan-wiki].
- Dying mid-use (not by explosion) leaves the body decapitated [Fan-wiki].
- The wiki screenshot is a top-down death view of a headless red Huggable body on a red-orange floor, with the HUD showing "CHARGING" and a Seesaw melee icon [Observed].

**CONFLICT:** the official card keeps the head on a stretched neck. The wiki says the blast comes from where the head should be and lists Static Shuffle as a head-removal attack [Fan-wiki].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Photo_27-04-13_11_29_47_AM.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/primary_cards.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/551341_10152742125825174_1995293618_n.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Static_shuffle_head_decapitation.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/ingame_misc.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/static_thumbs.png (built from https://i.ytimg.com/vi/c6MuK2LKDGk/ and https://i.ytimg.com/vi/jOTucJV9zRQ/ hqdefault, hq1, hq2, hq3)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/hud_icons2b.png

**Depiction for shorts:** the paws rub the head fast as a crackle builds. The neck springs up like a jack-in-the-box and a short cone of blue-white lightning bursts out. A few sparks hang in the air for a beat [card and wiki; the spring gag is BBG News invention].

**Confidence:** partial.

---

## Losing Your Head (primary; explosive; BBG 2.6, 20 Dec 2013)

**Official text:** "Just when you thought the huggable could not be any more dangerous, it takes it's head off and tries to kill you... to death. " [Game text via wiki, typo as quoted] (https://battlebears.fandom.com/wiki/Losing_Your_Head)

**Status and era:**
- Added in BBG 2.6 at 100,000 Joules, no level lock [Fan-wiki: 2.6 page].
- No later changes recorded. Not seen in 2026.

**Look:**
- It has no menu slide; the Gear Up shows the normal stance [Fan-wiki].
- LYH.jpg (uploaded 2013-12-21) shows the 3D Pink Huggable, arms out, with dark wrist cuffs set with glowing round red lights [Observed].
- The explosion was not seen in any image [Unverified].
- Fan demo thumbnails ("Losing Your Head Demonstration", ApplerGamers) show an orange-skin Huggable from behind and no blast [Observed].

**Firing:** one tap. "The Huggable will shake off its head, which will land at its feet and explode almost instantly". It works in mid-air, and melee before the head lands cancels it [Fan-wiki].

**Projectile:** the dropped head [Fan-wiki].

**Impact / end result:**
- "a bright blue blast. The explosion created in large and spherical, and will envelop the Huggable". Damage falls off with distance, and there is no self-damage [Fan-wiki].
- Then "the Huggable simply grabs a new head, seemingly out of nowhere, and attaches it to its body" [Fan-wiki].
- The blast is "very similar to those caused by the Phantom Hug, the only difference between the two being the actual colour of the blast" [Fan-wiki].
- Explosives 30-70. Recharge 2.5 s in the infobox, "four second reload" in the text [Fan-wiki].
- Glitch: dying right after use leaves no head at all [Fan-wiki].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/LYH.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/ph_lyh_cr.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/zoom/yt_sShVWYc6MpQ.png

**Depiction for shorts:** the head shakes off, bounces once at its feet and flashes, and a big blue sphere blooms around the Huggable. A fresh head pops on from off-screen [wiki-based; the sphere's look is BBG News invention].

**Confidence:** documented.

---

## Tough Love (secondary; self-buff; default; BBR 2012 to BBG)

**Official text:** "Conjure within yourself ancient primal magicks and funnel it into a temporary 50% bonus to all melee damage!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Tough_Love)

**Status and era:**
- Default secondary [Fan-wiki].
- A 2012 BBR Gear Up "SECONDARY" list shows TOUGH LOVE, MINI ME and PEEK A BOO (EQUIPPED), with DURATION and COOLDOWN bars [Observed: Tough_Love.png].
- BBR 1.4.2: cooldown 20 to 15, duration 30 to 35 [Fan-wiki].
- BBG 2.6: tired time 7 to 14, duration 35 to 10 [Fan-wiki].
- Infobox: 20 s duration, 4 s recharge (conflicts) [Fan-wiki].

**Look:**
- Menu card (2012-13): the Huggable, with blue wrist cuffs, runs after a fleeing brown bear in a red headband, red wristbands and a grey backpack, inside a cloud of glossy red hearts trailing behind. Hearts are about #D73066 highlight and #B30D34 shade [Observed].
- 2013 infobox card: a grinning Huggable with a torn leg showing stuffing chases a sweating, alarmed brown bear in a red headband and gold-bullet bandolier, red hearts behind [Observed]. The bear resembles Oliver [Inference].
- Icon: the face inside a cluster of red hearts [Observed].

**Firing:**
- "the Huggable will waves its hands for approximately 3 seconds", and melee interrupts it [Fan-wiki].
- Then "the Huggable is trailed by a stream of hearts". Re-using it resets the timer [Fan-wiki].

**Projectile:** none.

**Impact / end result:**
- Melee damage +50% [Game text via wiki].
- The in-game heart trail was not seen [Unverified].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Photo_27-04-13_11_29_52_AM.png and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Tough_love.png (both via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/secondary_cards.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Tough_Love.png

**Depiction for shorts:** a frantic hand-waving "spell", then a trail of glossy red hearts puffs off it as it sprints at a nervous bear [card and wiki].

**Confidence:** partial.

---

## Mini Me (secondary; shrink; BBR 2012 to BBG)

**Official text:** "Become very tiny and make it that much harder for enemies to hit you!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Mini_Me)

**Status and era:**
- 45,000 Joules, level 8 [Fan-wiki]. In the 2012 secondary list [Observed].
- BBR 1.4.2 fixed Mini Me glitches on three maps [Fan-wiki].
- BBG 2.6: duration 20 to 7 [Fan-wiki]. Infobox: 8 s duration, 10 s recharge [Fan-wiki].

**Look:**
- Card: three fading, dark, translucent Huggable afterimages with green outlines (#28881E) step down from large to small, ending in a small solid pink Huggable, with green sparkles [Observed].
- Icon: a small face in front of a larger dark silhouette [Observed].
- The "Mini Me in use" screenshot is a low third-person view from behind the Huggable's bandaged head and radio (blue-tipped antenna). The HUD shows the face-plus-silhouette icon and a Punk Bands melee icon. Size can't be judged from it [Observed].
- The Gold Huggable glitch screenshot shows the Gold skin from behind in a blue-lit space [Observed]. That it is inside a wall is the wiki's caption [Fan-wiki].

**Firing:**
- The activation animation is the same as Peek A Boo's, with a sound "similar to the 'Help me out' teamspeak ... almost like the Huggable is laughing" [Fan-wiki].
- No speed increase. It cannot collect pickups unless it jumps, and lock-ons are harder [Fan-wiki].

**Impact / end result:**
- None.
- Death glitch: it "may occasionally return to normal size and then freeze" [Fan-wiki].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Photo_27-04-13_11_29_54_AM.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/secondary_cards.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Tough_Love.png (icon)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/083C005C-CFF5-4B94-8170-AED887E633D8-1835-0000011331752478.png and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Mini_Me_glitch.png (both via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/ingame_misc.png)

**Depiction for shorts:** three neon-green ghost outlines snap down to a toy-sized Huggable with a giggle and a puff of green sparkles [following the card].

**Confidence:** partial.

---

## Peek A Boo (secondary; invisibility; BBR 2012 to BBG)

**Official text:** "By pressing small amounts of rainbow out of their bodies, Huggables can match the color of their surroundings and become all but invisible to the untrained eye!" [Game text via wiki; the page labels it "Offical"] (https://battlebears.fandom.com/wiki/Peek_A_Boo)

**Status and era:**
- 115,000 Joules, level 17 [Fan-wiki]. In the 2012 list, EQUIPPED [Observed].
- BBR 1.4.2: cooldown 60 to 50, duration 20 to 25, tired 10 to 8, damage bonus 0 to 10 (it does not work), and a team-coloured aura added [Fan-wiki].
- BBR 1.4.3: the outline was removed from Cloaking only [Fan-wiki].
- BBG 2.6: outline removed from Peek A Boo; visibility minimum 0.02 to 0.01 and maximum 0.2 to 0.1; cooldown 50 to 40; duration 25 to 30; tired 8 to 3 [Fan-wiki].
- Infobox: 4 s duration, 6 s recharge (conflicts) [Fan-wiki].

**Look:**
- Card: the Huggable is reduced to an empty black silhouette with a neon-green outline (antenna, ears, arm). Its lower half sinks into puffy white clouds (#F4F4F4, shaded #BBD2E0), with floating white-blue bubbles (#DAE4F3) [Observed].
- Icon: the face in white clouds [Observed].
- A pre-1.4.2 wiki thumbnail (320x180) shows grass, a big pinkish-white glowing ring at left and a grey translucent figure with a blue team marker in the centre [Observed]. Which element is the Huggable is [Unverified].
- Before 1.4.2 the Huggable showed as "a light greyish shape". From 1.4.2 to 2.6, neon red or blue lines picked out its features [Fan-wiki].

**Firing:**
- "a short burst of rainbow energy will be emitted above the Huggable and the player will become totally invisible" [Fan-wiki].
- Taking damage makes it flicker visible. Attacking or using a Special ends it. Snipers and Demos cannot lock on [Fan-wiki].

**CONFLICT:** the wiki's rainbow burst (and the official text's "rainbow") versus the card's white foam and bubbles.

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Photo_27-04-13_11_29_57_AM.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/secondary_cards.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Tough_Love.png (icon)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Mqdefaul.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/ingame_misc.png)

**Depiction for shorts:** a soap-bubble "poof" with a faint rainbow shimmer, after which only a faint outline remains and then nothing [card plus official text; the blend is BBG News invention].

**Confidence:** partial.

---

## Super Size Me! (secondary; grow plus stomp AoE; BBG 2.20, 29 May 2015)

**Official text:** "Super Size your huggable! Damage foes with the stomps of your feet while they scream in terror of your size! " [Game text via wiki] (https://battlebears.fandom.com/wiki/Super_Size_Me!)

**Status and era:**
- 150,000 Joules, level 10. Added in BBG 2.20, which the versions list dates 29 May 2015 [Fan-wiki].
- It "used to be the only Huggable secondary that heals while being used, although it no longer heals" (undated) [Fan-wiki].
- Not seen in 2026.

**Look:** the wiki page has no image [Observed: empty image list]. No official image found [Unverified].

**Firing:**
- "the Huggable will grow in size and have more Melee hitbox while the player starts to create colored shockwaves similar to those of the Happy Hour and Metal Crush" [Fan-wiki].
- Slowed by 25%. Explosive 20-40, 4 s, recharge 6 s [Fan-wiki].

**Shockwave reference:**
- The wiki's in-game "Happy Hour explosion" screenshot shows a white-cored magenta pillar of crystal shards and a flat magenta ring racing across the floor [Observed].
- Metal Crush makes a "golden shockwave that spreads out like the splash made by the Happy Hour" [Fan-wiki].
- Super Size Me!'s own colour and scale factor are [Unverified].

**Images viewed:** /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/ref/happy_hour_explosion.png (reference only)

**Depiction for shorts:** the Huggable balloons to giant size, and each stomp sends a flat coloured ring racing across the floor while bears hop or tumble [BBG News invention, following the wiki's comparison].

**Confidence:** documented.

---

## Phantom Hug (secondary; saboteur projectile; the only ranged Huggable secondary; BBG 2.2, 21 Aug 2013)

**Official text:** "The Huggable's ability to love will make time seem like it comes to a halt. When actually it's just your feet and you're about to die." [Game text via wiki] (https://battlebears.fandom.com/wiki/Phantom_Hug)

**Status and era:**
- 40 Gas, level 1. Added in 2.2 [Fan-wiki].
- The promo art was uploaded to the wiki 2013-08-01, before release [file metadata].
- Not seen in 2026.

**Look:**
- Promo art: "BATTLE BEARS GOLD" logo top right and a faint "...ENTERTAINM..." watermark at lower left [Observed].
- A translucent, glowing pink ghost Huggable (#F09EB4, #E47A94, pale core #F4E9DD) with a yellow-white glowing rim is wrapped over the face of a screaming muscular white bear. The bear wears red wristbands and a red belt with a gold-rimmed red oval buckle, and claws at the ghost [Observed].
- The real Huggable stands small at lower right, grinning, with blue-gem cuffs [Observed].
- The same art is the menu display (PH_MenuDisplay) and the wiki front-page crop [Observed].
- Fan thumbnail ("First Phantom Hug Match...", Arsenic Sushi): purple-magenta crackling wisps at the Huggable's paws. The top-right HUD icon is a Huggable face followed by a row of grey copies [Observed]. Reading these as the launch and the Phantom Hug icon is [Inference].

**Firing:** a single shot. Ammo 1, reload 5 s, 5% speed boost [Fan-wiki].

**Projectile:**
- "a cluster of pink energy in the shape of a Huggable", described as a "clone" [Fan-wiki].
- It passes through the Iron Curtain and destroys Proximity Mines [Fan-wiki].

**Impact / end result:**
- On any surface or player "it will explode in a moderate AoE" [Fan-wiki].
- Victims cannot move or turn for 2.5 s but can still attack, jump and use Specials. No damage [Fan-wiki].
- Status icon: "a yellow Z will appear over the player's head" (Slowed; Phantom Hug is listed as "(immobile)") [Fan-wiki: Status Effects].
- A yellow block "Z" flanked by two curved white arrows appears over an orange Huggable in the "Charged Run Demonstration" thumbnail. Its cause in that clip is unknown [Observed].
- Losing Your Head's blast is "very similar" apart from colour [Fan-wiki], so Phantom Hug's burst is likely a pink sphere [Inference].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Phantom_Hug.png, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Frontpage-news-phantom-hug.png and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/PH_MenuDisplay.png (all via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/ph_lyh_cr.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/zoom/yt_Ac4XjUzc6tY.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/hud_icons.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/zoom/yt_eRL6OoX--zA.png

**Depiction for shorts:** a see-through pink ghost Huggable with a glowing yellow-white rim flies out, wraps over a bear's face in a hug and bursts in a pink puff. The bear's feet stay stuck and a yellow "Z" with two curved white arrows floats over its head [art plus wiki; the puff's look is BBG News invention].

**Confidence:** partial.

---

## Charged Run (secondary; ground dash; the only Huggable secondary that deals direct damage; BBG 2.6, 20 Dec 2013)

**Official text:** "And I ran, I ran so far away, I ran all night and day… had to destroy all the Battle Bears?" [Game text via wiki] (https://battlebears.fandom.com/wiki/Charged_Run)

**Status and era:**
- Added in 2.6 at 160 Gas [Fan-wiki: 2.6 page and usage text]. The infobox and class page now say 60 Gas, and no price drop is documented [Fan-wiki].
- Not seen in 2026.

**Look:**
- The Gear Up stance (uploaded 2013-12-21) shows the 3D Pink Huggable with one arm raised (dark grey wrist band) and the other bent, with a round red light at the wrist [Observed]. The wiki says it is identical to the Phantom Hug stance [Fan-wiki].
- Fan demo thumbnails (ApplerGamers) show an orange-skin Huggable from behind on a starry map. One frame has the yellow Z overhead and a green translucent disc ahead. No run FX are visible [Observed].

**Firing:**
- Tap for an instant dash, or hold to charge. The Huggable cannot move while charging [Fan-wiki].
- A full charge is "indicated by sparkling particles coming out of the Huggable's body" and a Crossbow-like charged sound [Fan-wiki].

**Projectile:**
- The Huggable runs along the ground at 600 units per second [Fan-wiki].
- The run lasts 1.5 s, or 4 s fully charged. Charge time is given as both 3 s and 2.5 s. Recharge 6 s [Fan-wiki].

**Impact / end result:**
- 40 damage, once per opponent it runs through. Melee cancels it [Fan-wiki].
- The equipment table (Damage+) conflicts with the trivia, which says Explosives equipment applies [Fan-wiki].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/ChargedRunStance.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/ph_lyh_cr.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/zoom/yt_eRL6OoX--zA.png

**Depiction for shorts:** it crouches as sparkles leak from its body, then rockets along the floor. Bears it passes through spin like bowling pins in rainbow sparkles [the sparkles follow the wiki; the rest is BBG News invention].

**Confidence:** documented.

---

## Bite Me (melee; paired, one per paw; default; BBR 2011/12 to BBG; a version on BBH Huggy)

**Official text:** "That's a bit of iron-y." [Game text via wiki] (https://battlebears.fandom.com/wiki/Bite_Me)

**Status and era:**
- Default melee [Fan-wiki]. In the 2012 BBR melee list (screen uploaded 2012-11-25) [Observed].
- A dark jaw icon appears as the melee slot in the August 2011 Sneak Peek HUD [Observed; identification Inference].
- Damage: BBR 1.4.2 35 to 40; BBG 2.6 40 to 35; the page now says 80 after an undated buff [Fan-wiki].
- BBH Huggy wields "two automatic clamping bear traps strapped around his hands, that have dried up bits of rainbow colors on the edges of the teeth and base" [Fan-wiki: Huggy page].

**Look:**
- Two BLACK bear-trap jaws. Each is an open teardrop or C-shaped loop of black metal (#0B0E0D to #202A25) set with zigzag teeth smeared with iridescent rainbow (red, green, blue, violet), hinged on a round black disc clamped over each paw [Observed].
- Each jaw is about 0.4x the Huggable's height, about 0.28x Oliver [Inference].
- Icon: a dark crocodile-style jaw with rainbow teeth and a silver hinge [Observed].
- The 2012 screen's only stat bar is DAMAGE [Observed].

**Firing:** a melee swing with both paws. Damage is "often doubled due to the duplicate melees" [Fan-wiki]. The swing animation is unseen.

**Projectile:** none.

**Impact / end result:**
- The wiki reads the rainbow smears as "Huggable blood" [Fan-wiki].
- Generic 2026 melee hit FX: pale-yellow five-point stars at contact, and the target flashes white [Observed, on Punk Bands hits; see that section].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Photo_27-04-13_11_30_26_AM.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/melee_cards.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/HuggyBiteMeCR.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/cr_renders.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Bite_me.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sneak_bottom.png

**Depiction for shorts:** twin black traps snap shut with a metallic CLACK. Pale-yellow stars pop at contact, and the rainbow on the teeth reads as paint, never blood [traps observed; stars from 2026 FX; tone is BBG News invention].

**Confidence:** observed.

---

## Seesaw (melee; paired chainsaw hands; BBR 2012 to BBG)

**Official text:** "The Battle Bear who fashioned the first Huggable with chainsaw hands should not have been faulted for his scientific pursuits, but he was." [Game text via wiki] (https://battlebears.fandom.com/wiki/Seesaw)

**Status and era:**
- Price conflict: the class page says 20 Gas; the weapon page says 40 Gas with a level 3 lock. Price history: 5,700 Joules, then 50, 25 and 40 Gas [Fan-wiki].
- In the 2012 list, with a SPECIAL SPEED stat [Observed].
- BBR 1.4.2: damage 45 to 49, special cooldown -15% to -20% [Fan-wiki].
- BBG 2.6: damage 49 to 45, and the modifier became +10% speed [Fan-wiki].

**Look:**
- An orange boxy chainsaw housing (#C43D0A) over each paw, with black vent stripes and a small sticker [Observed].
- A long dark-grey guide bar (#373636) whose teeth are iridescent rainbow along the edge and tip [Observed].
- Total length about 0.7x the Huggable's height, about 0.45x Oliver [Inference].
- The 2012 screen shows it on a brown patchwork skin with shirt and tie [Observed], likely the Pleather Face skin [Inference].
- The official Huggabundle banner (2012) shows rainbow drips falling off the bar [Observed].
- Icon: an orange body with a grey bar and rainbow teeth. It is also the HUD melee icon in the Static Shuffle death screenshot [Observed].

**Firing:**
- Melee with both paws: 40 per saw, often doubled. It has the "slowest draw time but also the longest duration and largest hitbox" and +10% speed [Fan-wiki].
- Engine sound undocumented.

**Impact / end result:** the rainbow "blood". The wiki says it is likely based on Riggs' BB-1 Chainsaw [Fan-wiki].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Photo_27-04-13_11_30_30_AM.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/melee_cards.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/HuggySeesawCR.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/cr_renders.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Seesaw.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/gearup_melee2012.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Huggabundle.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/misc_melee.png)

**Depiction for shorts:** twin orange chainsaws rev, and the rainbow-toothed bars flick rainbow droplets like paint [art observed; the paint framing is BBG News invention].

**Confidence:** observed.

---

## Whack-Tus (melee; paired cactus clubs; one of the original three melees; seen in the 2026 playtest)

**Official text:** "Whack-tus? Darn near killctus." [Game text via wiki] (https://battlebears.fandom.com/wiki/Whack-Tus)

**Status and era:**
- 50,000 Joules, level 9. Formerly named "The Prick" and priced at 2,500 Joules [Fan-wiki].
- A partly visible "WHACK-TUS" row sits under Seesaw in the 2012 list [Observed, partial text].
- BBR 1.4.2: 40 to 43. BBG 2.6: 43 to 40, plus a -10% special cooldown. The page now says 60 damage and +30% special speed [Fan-wiki].
- 2026: the Closed Playtest #4 Gear Up shows the Pink Huggable holding it [Observed: JustNubz showcase auto-thumbnail; fan source].

**Look:**
- Big dark-green cactus clubs (#2A4A20, shade #1C2F1A) sheathe each forearm: ridged columns studded with lighter-green spikes [Observed].
- Each is about 0.5x the Huggable's height, about 0.35x Oliver [Inference].
- 2026: the same green clubs (#2F422D) on the Pink Huggable [Observed].
- The wiki says the icon has yellow spikes while the model is dark green [Fan-wiki].

**Firing:** a clapping swing [Fan-wiki: Punk Bands page], with a shorter draw time and duration than Presidentures [Fan-wiki].

**Impact / end result:** no specific FX documented [Unverified].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Photo_27-04-13_11_30_32_AM.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/melee_cards.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/HuggyWhacktusCR.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/cr_renders.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/yt/showcase_hq3.jpg (https://i.ytimg.com/vi/-lAtv-j9Sms/hq3.jpg)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/zoom/showcase_hq3_crop.png

**Depiction for shorts:** a double cactus clap with a puff of green needles and yellow stars [BBG News invention].

**Confidence:** observed.

---

## Presidentures (melee; paired wooden dentures, a Bite Me reskin; BBR 1.3.1, 28 Jun 2012)

**Official text:** "I cannot tell a lie, this weapon is historically inaccurate in a great many ways." [Game text via wiki] (https://battlebears.fandom.com/wiki/Presidentures)

**Status and era:**
- 30,000 Joules, no level lock. Released in week 2 of BBR 1.3.1; the Updates page dates 1.3.1 to June 28, 2012 [Fan-wiki].
- It appears in the official "BBR 1.3.1 and BEYOND!" promo pile [Observed: BBRWEAPONS.png].
- BBG 2.6: 45 to 40, plus +10% health. The page body says 15% [Fan-wiki].

**Look:**
- Carved wooden false-teeth jaws: dark-brown bark outer edge (#8F4626), pale tan inner wood with wavy grain (#F0C89D), pale sawtooth teeth, and cut-log tree-ring discs at the hinge ends [Observed].
- About 0.4x the Huggable's height, about 0.26x Oliver [Inference].
- Icon: a tan jaw with white teeth and a log-end circle [Observed].
- The wiki's equipped render uses the Hannible skin: red grille mask and a red-and-white straitjacket [Observed].

**Firing:** melee like Bite Me: 70 damage, often doubled, with a longer draw than Whack-Tus. The joke is George Washington's wooden teeth [Fan-wiki].

**Impact / end result:** none documented.

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Presidentures.png and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/BBRWEAPONS.png (both via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/misc_melee.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Photo_27-04-13_11_30_23_AM.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/melee_cards.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/HuggyPresidenturesCR.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/cr_renders.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Bite_me.png

**Depiction for shorts:** giant wooden dentures chomp with a hollow wooden clack and a few splinters. Avoid the Hannible skin [BBG News invention].

**Confidence:** observed.

---

## Punk Bands (melee; paired spiked arm cuffs; BBR 1.3.1 to BBG; in the 2026 trailer and a Steam screenshot)

**Official text:** "Your band doesn't get any gigs and your mom won't let you wear your little sister's jeans. It's too much pain for one person to bare, so make someone else feel it for a while! " [Game text via wiki; the wiki notes "bare" as a typo] (https://battlebears.fandom.com/wiki/Punk_Bands)

**Status and era:**
- 110,000 Joules (was 100,000), no level lock. Released in week 2 of BBR 1.3.1 [Fan-wiki]. Shown in the 1.3.1 promo [Observed].
- After BBR 1.4.1 it claps once instead of twice [Fan-wiki].
- BBR 1.4.2: 45 to 40; speed penalty -25% to -20% [Fan-wiki].
- BBG 2.2: penalty -20% to -17% [Fan-wiki].
- BBG 2.6: 51 to 45; the speed penalty became a 10% special-cooldown reduction [Fan-wiki].
- 2026: in the official trailer and Steam screenshot 00 [Observed].

**Look:**
- Oversized black cylindrical cuffs over each forearm, with rows of white cone spikes on gold/tan square bases (#DEA437) and a rounded pink end cap (#DB4784) [Observed].
- About 0.5x the Huggable's height long and 0.17x thick: about 0.33x and 0.11x Oliver [Inference].
- In the 2026 trailer the spike bases read cream-white and the cap stays pink [Observed: 30.9 s].
- The wiki says the cap is "always pink" [Fan-wiki]. The official 2012 Huggabundle banner shows a red cap on a red glossy Huggable [Observed], while the 2026 cyan Huggable has a pink cap [Observed].

**Firing:**
- A clapping swing with both arms [Fan-wiki].
- 2026 trailer: the pink Huggable swings Punk Bands at a sniper bear (teal face mask, blue polka-dot outfit) at about 30.9-31.1 s. The sniper renders pure white (hit flash) at 30.9-31.0 s [Observed].
- Steam screen_00 and trailer 35.9-36.3 s: a cyan Huggable swings a pink-capped Punk Band at an orange Huggable, and pale-yellow five-point stars burst at impact and around its feet [Observed].

**Impact / end result:**
- 2026 trailer, 31.2-32.2 s: a run of big starburst flashes engulfs the sniper [Observed]:
  - red-orange flame-like shards (about 31.2-31.3 s)
  - a bright yellow starburst (#FDF351, about 31.4-31.7 s)
  - white bursts with lavender-purple edges (#9978F6, about 31.8-32.2 s)
- The sniper then lies face-down while the grinning Huggable stands over it (32.5-32.6 s), before the "Huggable / HUGGABLE" splash card at about 33.0-34.0 s [Observed].
- Whether the starbursts are Punk Bands hit or kill FX, the falling Happy Hour missiles, or trailer editing is [Unverified].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Photo_27-04-13_11_30_21_AM.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/melee_cards.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/HuggyPunkCR.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/cr_renders.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Huggabundle.png and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/BBRWEAPONS.png (both via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/misc_melee.png)
- Trailer frames and crops: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/tr/g_012.jpg, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/tr/g_015.jpg, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/tr/g_017.jpg, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/tr/g_019.jpg, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/tr/g_022.jpg, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/tr/g_026.jpg, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/tr/g_029.jpg, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/hit_seq.png, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/hug2026_detail.png, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/trailer/t_0068.jpg
- Steam screenshot and crops: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/steam_screens/screen_00.jpg, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/s0_hug.png
- Riggs-segment sheets: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/riggs_seg.jpg, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/cyan_orange.png

**Depiction for shorts:** a double-fisted spiked haymaker. The target flashes white, pale-yellow stars pop, and for a KO the target flops face-down while the Huggable grins over it [2026 observed]. Any extra starburst is optional colour [BBG News invention].

**Confidence:** observed.

---

## Bearettas (melee; paired spiked pistol gauntlets, never fired; BBG 2.21, 3 Jul 2015)

**Official text:** "Good thing Huggables don't have thumbs, otherwise they would actually be able to use these" [Game text via wiki] (https://battlebears.fandom.com/wiki/Bearettas)

**Status and era:**
- 20 Gas, level 5. Added in BBG 2.21 [Fan-wiki]. The wiki page is a stub.
- Not seen in 2026.

**Look:**
- Two oversized pistol-shaped gauntlets run along each forearm, strapped on rather than held: magenta-pink (#D3407F, #A73C5A) and dark grey, with a glowing cyan stripe, two round barrel holes, a serrated front edge, a row of white cone spikes along the top, and white flourish decals [Observed].
- About 0.5x the Huggable's height, about 0.33x Oliver [Inference].
- Shown on a pink Huggable wearing orange-rimmed sunglasses and red floral swim shorts [Observed], probably the Beach Time skin [Inference].
- Colours on the default skin, and the earlier report of a "B" emblem, are [Unverified].

**Firing:**
- Melee only: 65 damage, +20% speed, -50% special speed [Fan-wiki].
- "two modified pistols, fitted with some sort of arm guards and spikes, which are what are used as the actual weapon" [Fan-wiki].
- No bullets [Inference from the official text].

**Images viewed:** /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Image19.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/misc_melee.png)

**Depiction for shorts:** it aims the pistol gauntlets, squeezes with no thumbs and nothing happens, so it swings the spiked guards instead [official text and render; the gag is BBG News invention].

**Confidence:** observed (one render).

---

## Beaver Feaver (melee; paired wooden chainsaws, a Seesaw reskin; BBR 1.3.1, June 2012)

**Official text:** "Cut your enemies down to size!... and then stack their bodies in a river and raise a family in there again or something... I'm sorry, that analogy got away from me pretty quick there." [Game text via wiki] (https://battlebears.fandom.com/wiki/Beaver_Feaver)

**Status and era:**
- 20 Gas, no level lock. Released in week 2 of 1.3.1 as "Beaver Fever" [Fan-wiki].
- The in-game list spells it "BEAVER FEAVER" [Observed].
- BBR 1.4.2: 33 to 42, health +25% to +20% [Fan-wiki]. The 2012 screen still shows "HEALTH +25%" [Observed].
- BBG 2.6: 42 to 40 [Fan-wiki].

**Look:**
- A wooden chainsaw. The blade is maroon-brown wood carved with a cross-hatched waffle pattern (#4C2511 to #623117), edged with orange-peach teeth [Observed].
- It is mounted in a slatted wooden crate housing with silver metal corners and lime-green tape binding at the joint (#5E7A15 to #81922B) [Observed].
- About 0.65x the Huggable's height, about 0.42x Oliver [Inference].
- Icon: the waffle blade with its crate [Observed].

**Firing:** like Seesaw: 40 per saw, often doubled, +20% health [Fan-wiki].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Photo_27-04-13_11_30_15_AM.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/melee_cards.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/HuggyBeaverCR.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/cr_renders.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Beaver_Fever.png (via /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/v2/sheets/gearup_melee2012.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/BBRWEAPONS.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable/png/Bite_me.png

**Depiction for shorts:** wooden saw blades whirr like chattering beaver teeth and spit wood chips [BBG News invention].

**Confidence:** observed.

---

## Corrections to the previous inventory (found on re-check)

1. **2026 So Fly FX.** The magenta crystal pillar and floor ring at 30.7-32.4 s is very likely Tillman's Happy Hour explosion, not So Fly [Inference from the wiki "Happy Hour explosion" screenshot and the matching red missiles; Observed]. So Fly's own 2026 trail is the orange-to-yellow-to-green light column at 30.4-30.8 s.
2. **Wrist cuffs.** The 2013 melee renders show bare wrists. The red-light cuffs appear in the December 2013 ability renders and in 2026. Blue gems appear only on 2D art [Observed].
3. **Static Shuffle concept sketches.** A and B show paws pressed to the head; only C shows the stretched neck [Observed].
4. **Tough Love's chased bear.** It wears a red headband in both cards, plus a gold-bullet bandolier on the 2013 card and a grey backpack on the 2012 card. It is probably Oliver [Inference].
5. **Release dates.** The Updates page dates BBR 1.4.3 to April 15, 2013, and 1.4.3.1 shipped April 23 per the BBR infobox. BBR 1.3.1 is June 28, 2012 [Fan-wiki].
6. **Seesaw's 2012 screen skin** is a brown patchwork skin with shirt and tie, likely Pleather Face [Inference].
7. **Whack-Tus was already named Whack-Tus** in the late-2012 menu [Observed, partial row].
8. **The magenta figure inside the 2026 burst** at 32.3-32.5 s is a dark red bear briefly tinted pink, not a Huggable [Observed: pink_figure.png].

## Corrections for the character file (/home/user/thallo-site/bbg-news-repo/characters/huggable.md)

1. **"steel bear-trap jaws over both paws"** (Prompt pack). Change to: "two black bear-trap jaws (open C-shaped loops) clamped over both paws, zigzag teeth smeared with iridescent rainbow". Evidence: Photo_27-04-13_11_30_26_AM.png, HuggyBiteMeCR.jpg, Bite_me.png [Observed].
2. **"Metal wristbands with blue gems, a metal knee brace"** (Prompt pack). For the 3D/BBG look, use dark grey wrist cuffs, each with a round glowing red light, and no knee brace. Keep the blue-gem bands and knee brace for a 2D comic-card style only. Evidence: LYH.jpg, ChargedRunStance.jpg, 2026 trailer 32.6 s (red lights); the 2013 melee renders show bare wrists; 2D cards and 2012 art show blue gems [Observed].
3. **"a small red team banner with three white symbols on its back"** (Prompt pack). This is stated as fact but is a BBG News choice. 2026 footage shows a blue banner with orange shapes, a dark-blue banner with teal swirl art, and a white panel with rainbow dots in a red-and-white striped frame (apparently a banner) [Observed]. Label it [BBG News invention] or follow 2026.
4. **Body & eyes line, "Possibly official 2012 art adds metal wristbands with blue gems and a knee brace [Observed]"**. Add that these are 2D-only, and that the 3D model shows red-light cuffs or bare wrists [Observed].
5. **Weapons bullet.** It lists only 9 of 18. Give the full kit [Fan-wiki] and upgrade Bite Me to observed black traps.
6. **Comedy beat "The Bearettas squirt out of its thumbless paws like soap"**. The Bearettas are strapped along the forearms as spiked gauntlets (Image19.PNG) [Observed], so they cannot slip out of its paws. Use "it aims, has no thumbs, nothing fires" instead.
7. **Prompt pack "a boxy military-green radio with a white antenna"**. In the 3D model it is a thin silver antenna with a red ball tip [Observed]. The 2D cards often show a blue tip.
8. **Prompt pack "a torn belly patch showing metal"**. The renders and 2026 trailer show grey-white crumpled filling; the wiki calls it stuffing. "Metal" is [Unverified].

## Open questions

- What do Double Rainbow!, Headlights, Static Shuffle, Losing Your Head, the Tough Love heart trail, Mini Me, Peek A Boo, Super Size Me!, Phantom Hug and Charged Run look like in-game in 3D? This needs gameplay frames. The JustNubz showcase Huggable chapter (14:16-17:44) is the best lead, but YouTube is blocked here.
- Are the 31.2-32.2 s starbursts Punk Bands kill FX, Happy Hour hits, or edit FX? Is the 30.4-30.8 s flight definitely So Fly?
- Static Shuffle in-game: does the head come off, or does the neck stretch?
- What did BBG 2.11's "Huggable overhaul" (27 Aug 2014) change? The official 2.6 change log and SkyVu patch notes are unread because the Wayback Machine was unreachable.
- What are the 2026 prices and stats? Open conflicts: Seesaw 20 vs 40 Gas, Charged Run 60 vs 160 Gas, Bite Me 35 vs 80.
- Does the yellow Z show on Phantom Hug victims in 2026? What caused the Z in the Charged Run demo?
- Super Size Me!'s shockwave colour and size factor.
- Peek A Boo activation: does it read as rainbow or as bubbles?
- Punk Bands cap colour on other skins. Bearettas colours on the default skin.
- 2026 team banner rules.
