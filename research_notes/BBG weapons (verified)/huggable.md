# Huggable (BBG) weapons dossier (verified and edited, 2026-10-17)

**The class.** The wiki's strategy text says the Huggable "has both primary and secondary abilities for use, but mostly relies on its strong melee attacks". It has "only 90 units" of health and "the highest base speed of any class". It also "cannot switch between them while the weapon is recharging" [Fan-wiki: Huggable (BBG), re-fetched today]. All seven melees come in pairs: "Landing one melee will do the listed damage, and landing both will essentially double it" [Fan-wiki]. The Steam page lists "-HUGGABLE: Huggable", promises "80+ PRIMARY WEAPONS / 60+ SECONDARY WEAPONS / 50+ MELEES" and gives a release date of Nov 4, 2026 [Canon: Steam appdetails for app 4408320, fetched today].

**The kit is 18 weapons** [Fan-wiki: class page]. Category:Huggable (class) holds exactly these 18 weapon pages plus skins [Fan-wiki: category listing, checked today].
- Primaries: Double Rainbow! (default), Headlights, So Fly, Static Shuffle, Losing Your Head.
- Secondaries: Tough Love (default), Mini Me, Peek A Boo, Super Size Me!, Phantom Hug, Charged Run.
- Melee: Bite Me (default), Seesaw, Whack-Tus, Presidentures, Punk Bands, Bearettas, Beaver Feaver.

**The class mapping has an error, confirmed.** weapons_by_class.json["Huggable"] has 25 entries. Seven of them are Soldier weapons: A Salt Rifle, Heavy A Salt Rifle, Soaker, Spreadshot (BBG), Steamshot, B.E.A.R. Club and Krikkit Bat. Each page's Class row or category says Soldier [Fan-wiki, checked today]. They come from a Soldier changelog pasted under "BBR Version 1.0" on the Huggable (BBG) page, which also lists Bearzooka and Oliver skins [Fan-wiki]. Two near-misses are not Huggable weapons either: Huggable Gloves is categorised Heavy and Double Hug is categorised Demo [Fan-wiki]. The "Huggable (BBG)/Weapons" subpage is a one-line stub [Fan-wiki].

**Sources reached today:**
- The fan-wiki MediaWiki API: all 18 weapon pages, the class page, BBR Version 1.3.1, 1.4.2 and 1.4.3, Battle Bears Gold/Versions and /2.6, Updates, Battle Bears Royale, Status Effects, Happy Hour, Metal Crush, Pink Huggable, Huggy, and the Beach Time, Pleather Face, Topsy Scurvy, Hannible and Gummable skin pages.
- Wiki file metadata, including the YouTube IDs of the demo videos embedded on the weapon pages, plus the wiki images themselves.
- The local official Steam trailer and the five Steam screenshots.
- battlebears.com/pages/characters, the plush product page and its product images.
- YouTube oEmbed titles and thumbnails. YouTube video playback is blocked here, so I watched no video, only thumbnails.
- Added 2026-10-18 for the So Fly Easter-egg note, from the verified maps research: the fan-wiki Shortest Parsec page, its revision history and revisions 32589, 64712 and 66693.

**Sources not reached.**
- web.archive.org reset the connection three times through curl, and WebFetch refused it.
- The official change log at battlebears.com/battle-bears-gold-2-6-change-log/ returns 404 on the live site.
- battlebears.vanillaforums.com was refused by the proxy.

So no SkyVu patch note was read. Every per-version number below is the wiki's transcription [Fan-wiki].

**Method.**
- I extracted frames from the local trailer at /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/trailer.mp4. Timestamps are trailer seconds.
  - f_NNN is at 29.5 + (NNN-1) x 0.1 s.
  - q_NNN is at 3.0 + (NNN-1)/30 s.
  - s_NNN is at 29.9 + (NNN-1)/30 s.
- Hex colours are means of small pixel patches, so they are approximate.
- Scale: the BBG News chart sets Oliver = 1.0x and the Huggable at about 0.65x [BBG News invention]. Weapon sizes are proportions measured on Gear Up renders, multiplied by 0.65 [Inference].
- Era: the 2D "menu display" cards on the wiki are April 2013 captures (Photo_27-04-13_*). The same cards already appear in October 2012 BBR Gear Up screenshots [Observed]. I call them "Gear Up cards (BBR, by Oct 2012)".

**Model notes for every weapon:**
- **Colour.** The 2026 pink is about #FE7BAC lit, #E24981 mid-tone and #A03559 shadow [Observed: trailer 32.7 s]. The 2013 render highlight is about #EEA1CD [Observed: LYH.jpg].
- **Face.** A red glossy button eye with a stitched scar running up to a cream head bandage, a small black dot eye and a huge white grin [Observed].
- **Head radio.** A green box with a thin grey antenna [Observed].
  - The ball tip is red on the 2013 Gear Up renders and in the 2026 trailer [Observed].
  - It is blue in 2012-13 in-game fan footage, in the Mini Me screenshot and on the 2D cards [Observed].
  - Skins vary: the red Seesaw render has a green tip [Observed].
- **Body.** A zip-stitched chest scar and a torn belly showing grey-and-white crumpled material [Observed]. The wiki calls it a "metalic jagged wound" with "what appears to be stuffing bulging out" [Fan-wiki: Pink Huggable].
- **Wrists.**
  - 3D default Pink: dark grey cuffs, each set with a round glossy red light [Observed: LYH.jpg and ChargedRunStance.jpg, uploaded 2013-12-21; 2026 trailer 32.6-32.7 s].
  - 2013 melee Gear Up renders: the weapon's mount covers the wrist, and the Presidentures card shows black wrist straps [Observed].
  - 2D cards mostly show cuffs with blue gems [Observed]. The exception is the August 2013 Tough Love infobox card, which shows plain dark bands [Observed].
  - The orange skin in-game wears blue wrist bands [Observed: Steam screen_00; LYH fan thumbnails].
- **2026 melee display.** In the trailer the Punk Bands show only during the swing (30.9-31.2 s). The arms show bare cuffs during the flight (30.4-30.8 s) and after the kill (32.6-32.7 s) [Observed]. That this is a general rule is [Inference].
- **Team banner.**
  - Red team: a tall, narrow red banner on a pole rising above the head, with three pale symbols stacked vertically [Observed: trailer 3.0-3.9 s; Dancing_Huggable.jpg, 2013].
  - Blue team: blue banners [Observed]. Steam screen_00 shows blue with orange shapes. Steam screen_04 / trailer 26.0 s shows dark blue with a teal swirl.
  - The wiki says the three white symbols are "lined up horizontally" [Fan-wiki: Pink Huggable], which the images contradict.
- **Generic melee hit FX.**
  - In 2026 the target flashes pure white (30.9-31.1 s), and pale-yellow five-point stars burst at contact (35.7-36.3 s; Steam screen_00) [Observed].
  - Yellow hit stars also appear in a 2013 BBG fan thumbnail [Observed: https://i.ytimg.com/vi/Ac4XjUzc6tY/hq3.jpg].

---

## Double Rainbow! (primary ability; default; in the BBR Gear Up by Oct 2012, then BBG; not confirmed in 2026)

- **Official text:** "Attack in all directions for a brief period of time. Use when diving into large groups of hapless victims!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Double_Rainbow!)

**Status and era:**
- Default primary [Fan-wiki].
- The BBR Gear Up "PRIMARY" screen File:Double_Rainbow.jpg (uploaded 2012-10-24) lists DOUBLE RAINBOW!, HEADLIGHTS (EQUIPPED) and SO FLY, with stat bars EXPLOSIVES, AOE, DURATION and COOLDOWN [Observed; date from file metadata].
- BBR 1.4.2 (28 Feb 2013): minimum damage 50 to 55 [Fan-wiki: BBR Version 1.4.2].
- BBG 2.2 (21 Aug 2013): it no longer keeps spinning after the Huggable dies [Fan-wiki: class trivia].
- BBG 2.6 (20 Dec 2013): minimum 55 to 25, maximum 80 to 40, duration 3 to 5 [Fan-wiki: 2.6 page].
- Current infobox: Explosives 45-90 per second; AoE "Max Dmg 125.0, Min Dmg 250.0"; duration 4.0 s, which conflicts with 2.6's 5; recharge 7 s [Fan-wiki].
- 2026: no confirmed shot. The trailer's rainbow burst at 3.27-3.85 s is a candidate (see the last weapon section) [Inference].

**Look:**
- Gear Up card: the Huggable leans back mid-air with a small "o" mouth and a tear, arms out, wearing blue-gem cuffs [Observed].
- Two broad rainbow arcs rimmed in neon-green glow sweep around its waist from left and right like an orbit ring [Observed].
  - Left arc, outer to inner: deep blue to cyan (#3ADCDA), green (#26F436), yellow (#F2FB17), red (#F10112), magenta (#D512C6) [Observed, sampled].
  - The ring is about 1.8x the Huggable's width, about 1.2x Oliver [Inference].
- List icon: a grinning pink face flanked by rainbow arcs [Observed].
- Possible in-game look, pre-launch BBR:
  - The official "BATTLE BEARS ROYALE Sneak Peek" (BATTLE BEARS channel, published 2011-08-31 [Canon: oEmbed author and wiki file metadata]) has an auto-frame where a pink Huggable hugs a white bear with blue goggles [Observed: hq2.jpg].
  - A flat, wide rainbow ribbon lies on the grass beside them, banded orange (#F5971F), yellow (#F2C234), green, cyan and lilac [Observed].
  - The HUD shows "CHARGING" over a face icon flanked by violet and rainbow shapes [Observed, blurry].
  - Reading the ribbon as Double Rainbow is [Inference].

**Firing:**
- One tap, centred on the Huggable. It "creates two spinning rainbows that rotate around the user and damage anyone within its range, lasting for several seconds" [Fan-wiki].
- Using melee during it cancels it [Fan-wiki].
- Sound undocumented [Unverified].

**Projectile:** none. The rainbows orbit the user [Fan-wiki].

**Impact / end result:**
- It damages anyone in range [Fan-wiki]. That damage falls off with distance is [Inference from the AoE row].
- Explosions+ adds +5/+10 [Fan-wiki]. With Flawless Disguise it "results in self injury and eventually suicide" [Fan-wiki].
- "As it is nearing the end of its duration, the range of the two rainbows will slowly decrease until they completely disappear" [Fan-wiki].
- Hit visuals undocumented [Unverified].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/prim_cards.jpg (from .../huggable-verify/png/Photo_27-04-13_11_29_40_AM.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/dr_tl_lists.jpg (from .../huggable-verify/png/Double_Rainbow.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/sneak_sheet.jpg, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/sneak_icon.png and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/sneak_bottom.png (from https://i.ytimg.com/vi/IucMFqzR_Qw/hqdefault.jpg, hq1, hq2, hq3)

**Depiction for shorts:** two glossy, flat rainbow ribbons with green-glow rims whip around the Huggable at waist height like a rotor, then shrink to nothing. Bears in range tumble away in rainbow confetti [BBG News invention, following the card and the wiki's shrinking-range text].

**Confidence:** partial.

---

## Headlights (primary ability; the class's only long-range attack; BBR by Feb 2012, then BBG; not seen in 2026)

**Official text:**
- "Remove your head and fire out a cutting death beam of rainbow essence. This is the Huggable's only ranged attack!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Headlights)
- Related SkyVu wording: "Limited Edition Huggable Pink Battle Bear Plushie comes with a unique detachable head that uncovers a secret rainbow beam, the source of the Huggable's power!" [Canon] (https://battlebears.com/products/huggable-plushie-with-in-game-bonus, re-fetched today)

**Status and era:**
- 32,000 Joules, level 4 [Fan-wiki].
- BBR 1.2.1.1 (3 Feb 2012): "Fixed bugs including the one caused by the Soaker and Headlights" [Game text via wiki: Updates page, which says it carries the official App Store update text].
- BBR 1.4.2: damage 40 to 45 per second, duration 2.7 to 4.0 s [Fan-wiki].
- BBG 2.1 (15 Jul 2013): the usage text says its damage "could not be enhanced by the use of Damage+" and its range "was significantly shortened". The trivia and equipment table contradict it on which equipment applies (Explosions+ is listed) [Fan-wiki].
- BBG 2.2: it stopped firing after death [Fan-wiki].
- BBG 2.6: damage 45 to 35, duration 4 to 5 [Fan-wiki].
- Infobox: 60 damage per second, 5 seconds, recharge 6 seconds, range 1250 units. The usage text says "a 5 second recharge" [Fan-wiki].
- 2026: not seen [Observed absence in the trailer and Steam screenshots].

**Look:**
- **CORRECTED.** On the Gear Up card the Huggable is bowed forward horizontally on its legs. Its head is pulled off and sits low at the front of the body (frame left), still wearing bandage, radio, blue-tipped antenna and a tear on its cheek [Observed].
  - Nothing visibly holds the head. The draft's "held at its side" is not supported.
  - A white sparkle burst sprays from the neck opening, and the beam fires horizontally out of the neck to the right, away from the face [Observed].
  - The same card shows a blue-gem cuff on the forearm and a metal knee brace on the rear leg [Observed].
- Beam bands, top to bottom: violet #320C6D, purple #620977, magenta #AE0A7D, red #C92F2C, yellow #DBED1D, green #53B418 to #26EB67, teal-cyan #147396 to #25A3BA, blue #162483 [Observed, sampled].
- The beam is about as thick as the head: about 0.3x the Huggable's height, about 0.2x Oliver [Inference].
- List icon: a face with a white burst and a rainbow band [Observed: Double_Rainbow.jpg list].
- Official plush design sheet on battlebears.com: a headless pink body with a jagged, lightning-shaped rainbow ribbon (purple, red, green, blue, yellow) bursting up from the neck, the grinning head lying beside it [Observed].
- Official plush photo: a rainbow-striped satin handkerchief pulled from the neck opening [Observed].

**Firing:**
- "Firing the Headlights only requires the player to shoot once", after which the Huggable takes "off its head and fire[s] a long, continuous rainbow beam lasting a few seconds" [Fan-wiki].
- The player must "constantly concentrate the beam on the target", and "cannot use their melee weapons while the Headlights is activated" [Fan-wiki].
- Glitch: "no matter what skin the player uses, they will pull off a Hannible skin head" [Fan-wiki].

**Projectile:**
- A continuous beam [Fan-wiki].
- The wiki says it is "seemingly based off of" the Huggable headshot death in BB -1, Zombies and Zero, "where the head would fly off far into the distance, leaving behind a trail of rainbows" [Fan-wiki].

**Impact / end result:** sustained damage while the beam stays on target [Fan-wiki]. Before 2.1, with Damage+ it "could potentially deal over 200 damage" [Fan-wiki]. Hit visuals are undocumented [Unverified].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/headlights_zoom.png and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/prim_cards.jpg (from .../png/Photo_27-04-13_11_29_41_AM.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/list2012.jpg (from .../png/Headlights.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/plush_sheet.jpg (from https://battlebears.com/cdn/shop/products/BATTLE-BEARS_Huggable_Plush_1800x1800.png, BB_Huggable_Plush_comp_1200x1200.png and BB_Huggable_Plush_pr_solo_1200x1200.png)

**Depiction for shorts:** it bows forward, pops its head off and sets it down in front. A white sparkle bursts at the neck, and a straight, head-thick rainbow laser (violet on top to blue on the bottom) streams out of the neck hole. Afterwards it screws the head back on [card and plush art; the re-attachment is BBG News invention].

**Confidence:** partial.

---

## So Fly (primary ability, movement attack; BBR by Oct 2012, then BBG; likely shown in the 2026 trailer; also BBH Huggy's Ultimate)

**Official text:**
- "Fly forward with a burst of speed while damaging all in your way. Also very useful for getting around the maps! Aim up fly up!" [Game text via wiki] (https://battlebears.fandom.com/wiki/So_Fly)
- BBH: "Huggy's Ultimate, So Fly, allows him to soar across large parts of the map, dealing increased damage to enemies for a short period when he lands." [Canon] (https://battlebears.com/pages/characters, re-fetched today)

**Status and era:**
- 60 Gas, level 6 [Fan-wiki]. "So Fly originally cost 25,000 Joules" [Fan-wiki]. BBR 1.4.2 changed the price from "25,000 Joules to 60 Gas" [Fan-wiki: BBR Version 1.4.2].
- EQUIPPED in the October 2012 Gear Up list [Observed: So_Fly.jpg, uploaded 2012-10-23].
- "As of v2.0, players can change direction in mid-air" [Fan-wiki]. The BBR page says "The v2.0 installment of Battle Bears Royale saw Battle Bears Gold" [Fan-wiki], although the BBG versions list starts at 1.0 (24 May 2013), then 2.1.
- BBG 2.2: the death fix [Fan-wiki].
- BBG 2.6: flying speed 500 to 510, damage 50-70 to 60-80, tired time 5 to 4 [Fan-wiki].
- Infobox: Explosives 15-30, which conflicts with the usage text's 60-80; 3 seconds; recharge 9.5 seconds; 575 u/s [Fan-wiki].
- The wiki embeds an Everyplay video, "Battle Bears Huggable Gameplay [So Fly]" (YouTube Do3Ja12MpSI, published 2015-04-07 [Fan-wiki file metadata]). It is now unavailable on YouTube (oEmbed 404). The wiki's cached thumbnail shows a pink Huggable from behind on a lava map. Its HUD primary icon is the So Fly face-with-rainbow-trail [Observed]. No flight FX are visible.

**Look:**
- Gear Up card: the Huggable flies horizontally, head first, in a Superman pose, one arm forward wearing a blue-gem cuff [Observed].
- A wavy rainbow trail streams from its feet, with a white sparkle burst where the trail meets the body and sparkles in the trail [Observed].
- Trail bands, sampled in the draft and consistent with my view: violet #5D00EB, magenta #A309A0, red #DF181E, yellow #E6F71F, green #2DC138, cyan #27DFED, blue #0F27F1 [Observed].
- List icon: a face with a rainbow flag trail [Observed].

**2026 official trailer, 30.1-30.8 s** [Observed: frames f_007 to f_014 and s_007 to s_025]:
- At 30.17-30.30 s the pink Huggable rises from below a ledge.
- From 30.30 s a broad, translucent vertical ribbon appears under its feet as it climbs.
  - Colours run in rainbow order, red-orange nearest the Huggable (#FE9558), then bright yellow (#FFF671), then a green fringe further down (#82DC4A, #47AB47) [Observed, sampled].
- From 30.5 s it flies horizontally, belly down and head first, arms swept back with bare cuffs, antenna up [Observed].
- Identifying this as So Fly is [Inference]: the "Aim up fly up" rise and the card pose match, and there is no HUD.

**The magenta crystal burst is not So Fly.**
- Tillman's "TILLMAN / DEMO" splash card plays at 28.5-29.9 s [Observed].
- A red finned missile with a yellow flame tail falls from the top of frame at 30.17-30.57 s and reaches the base of the ribbon at about 30.57-30.63 s [Observed].
- A white-cored magenta crystal-shard pillar with a flat magenta floor ring erupts there at 30.70 s and lingers to about 32.4 s [Observed].
- This matches the wiki's in-game screenshot captioned "Happy Hour explosion" [Observed: Happy_hour_explosion.jpeg], shot from a Demo (panda) player with "0/5" ammo [Observed]. It also matches the wiki text "falling back down ... exploding into a damaging shock-wave" [Fan-wiki: Happy Hour].
- So the pillar is Tillman's Happy Hour [Inference], and Steam screenshot 01 is a still of this moment [Observed].

**Firing:**
- One tap, after which the Huggable "will fly forward a short distance in a stream of rainbows". It "can be used in any direction", and steering has worked since v2.0 [Fan-wiki].
- It is "the only class that can reach" the Shortest Parsec Easter egg [Fan-wiki: Huggable (BBG) trivia]. This is contested:
  - It echoes a line the map page carried from April 2013 to May 2014, "There is an Easter Egg on this map that can only be reach by Huggables" [Fan-wiki: Shortest Parsec rev 32589, 2013-04-21; spelt "reached" from later that day].
  - An edit on 2014-05-27 replaced that line (rev 64712, "Fixed Trivia feature: Easter Egg"). The current map page says the red-base meteorite "can be reached only by using So Fly[Huggable] and Metal Crush[B-1000]" [Fan-wiki: Shortest Parsec, re-fetched 2026-10-18; the same text is in rev 66693, 2014-08-06].

**Projectile:** the Huggable itself, "in a stream of rainbows" [Fan-wiki].

**Impact / end result:**
- Contact damage "according to the proximity of the hit and the duration", from 60 at minimum to a peak of 80 [Fan-wiki].
- No hit FX seen [Unverified].
- In BBH it adds a damage boost after landing [Canon].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/prim_cards.jpg (from .../png/Photo_27-04-13_11_29_45_AM.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/list2012.jpg (from .../png/So_Fly.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/up/sofly_thumb.png (wiki thumbnail https://static.wikia.nocookie.net/battlebears/images/f/f5/Battle_Bears_Huggable_Gameplay_So_Fly/revision/latest?cb=20150502165007)
- Trailer crops: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/sofly_zoom.jpg, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/sofly_zoom2.jpg, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/column_seq.jpg and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/column_seq2.jpg
- Trailer contact sheet: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/full_37.jpg
- Steam screenshots: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/steam_sheet.jpg (screen_01 to screen_04)
- Happy Hour reference: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/hh_small.jpg (from .../png/Happy_hour_explosion.png)

**Depiction for shorts:** a crouch, then a pop upward that leaves a broad, washed-out rainbow ribbon (red at its feet, yellow, then green) standing in the air, then a head-first Superman streak trailing a wavy seven-band rainbow with white sparkles at its feet [2026 ribbon observed; contrail from the card]. Bears it clips spin away in sparkles [BBG News invention]. Never add a magenta crystal pillar, which belongs to Tillman's Happy Hour [Inference].

**Confidence:** partial (the card is observed; the 2026 flight is observed but identified by inference).

---

## Static Shuffle (primary; chargeable short- to mid-range "shotgun"; BBR 1.4.3, April 2013, then BBG; not seen in 2026)

**Official text:**
- "This mid-range attack might just be enought to spark your opponent's demise!" [Game text via wiki, typo as quoted] (https://battlebears.fandom.com/wiki/Static_Shuffle)
- Release note: "Static Shuffle: Huggable's mid-range attack! Charge up and watch electricity fly! Damage and size depend on charge length." [Game text via wiki: BBR update text on https://battlebears.fandom.com/wiki/Battle_Bears_Royale; the Updates page truncates it to "charge leng,"]

**Status and era:**
- BBR 1.4.3, dated April 15, 2013 on the Updates page. The 1.4.3 page says "This update has been released, but as 1.4.3.1", and the BBR infobox dates 1.4.3.1 to Apr. 23rd 2013 [Fan-wiki].
- 60 Gas, level 1. "It originally cost 180 Gas, being the most expensive weapon at the time" [Fan-wiki].
- "It is the only Huggable (Class) primary affected by damage equipment" (+5/+10) [Fan-wiki].
- It is absent from the October 2012 primary list [Observed].
- No later rework is recorded. Not seen in 2026.

**Look:**
- Gear Up card: the head is pushed high on a long, stretched, stitched neck rising from a frayed collar. The face is open-mouthed and happy with wide eyes, and the antenna has a blue tip [Observed].
- Four jagged lightning bolts radiate around it, white-core (#C5EBEE) with cyan-teal edges (#5B979C) [Observed]. A blue-gem cuff is on its arm [Observed].
- Concept sketches A, B and C, white line on black [Observed: 551341_….png, uploaded 2013-04-14, captioned "Concept art" on the weapon page]:
  - A and B show the Huggable with its paws pressed to the sides of its head, amid lightning bolts. That this matches the wiki's head-rubbing charge is [Inference].
  - C shows the head raised on a stretched neck, eyes shut happily.
  - That the Facebook-style filename means a SkyVu Facebook post is [Inference; Unverified].
- HUD icon: a pink-and-blue Huggable face with a white grin, flanked by white-cyan lightning bolts. "CHARGING" overlays it while recharging [Observed: thumbnails of "[Huggable]: Primary - Static Shuffle (Uncharge Shots)" and "... Static Shuffle Charged", by Dban1 (@TheHuggableEmpire), 2013-04-15/16; fan source].
- In those 2013 in-game thumbnails the Huggable is seen from behind with its head on, wearing a blue-tipped antenna. No blast is visible [Observed].

**Firing:**
- Tap for a single burst, or charge "by holding the shoot button or double tap" [Fan-wiki].
- While charging, "a high pitched static sound is emitted as the Huggable rubs its head on its body to induce frictional static electricity", and "the sound gradually becomes louder and more harsh" [Fan-wiki].
- "After 6 seconds of charge, the electricity emitted by the Huggable will become much more violent and shining" [Fan-wiki].

**Projectile:**
- "a bright blue blast of electricity is shot from where the Huggable's head should have been" [Fan-wiki].
- Very short range. Charged, "the blast will reach further and deal an additional 15 damage, peaking at 75" (60 uncharged), with a reload of 2.5 seconds [Fan-wiki].
- "Damage and size depend on charge length" [Game text via wiki].

**Impact / end result:**
- "small electrical particles will remain present in the air for several seconds", damaging enemies who touch them. "The Huggable cannot commit suicide by these means" [Fan-wiki].
- Dying mid-use ("excluding death via explosion") leaves the body "with their head decapitated" [Fan-wiki].
- The wiki screenshot (Static_shuffle_head_decapitation.jpeg, 2013-05-10, not used on any page today) is a top-down view [Observed]:
  - a headless glossy red Huggable body lies spread-eagled on a red-orange floor;
  - its red head lies separately nearby under a white Huggable-face marker;
  - the HUD shows "CHARGING" over the lightning-face icon and a Seesaw melee icon.

**CONFLICT:** the official card keeps the head on a stretched neck. The wiki says the blast comes "from where the Huggable's head should have been" and lists Static Shuffle as a head-removal attack [Fan-wiki].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/prim_cards.jpg (from .../png/Photo_27-04-13_11_29_47_AM.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/png/551341_10152742125825174_1995293618_n.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/decap_small.jpg (from .../png/Static_shuffle_head_decapitation.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/ss_yt_sheet.jpg, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/ssc_yt_sheet.jpg and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/ss_icon_body.png (from https://i.ytimg.com/vi/jOTucJV9zRQ/ and https://i.ytimg.com/vi/c6MuK2LKDGk/ hqdefault, hq1, hq2, hq3)

**Depiction for shorts:** its paws rub its head fast as a crackle builds. The neck springs up like a jack-in-the-box and a short cone of blue-white lightning bursts out. A few sparks hang in the air for a beat [card and wiki; the spring gag is BBG News invention].

**Confidence:** partial.

---

## Losing Your Head (primary; explosive; BBG 2.6, 20 Dec 2013)

- **Official text:** "Just when you thought the huggable could not be any more dangerous, it takes it's head off and tries to kill you... to death. " [Game text via wiki, typo as quoted] (https://battlebears.fandom.com/wiki/Losing_Your_Head)

**Status and era:**
- Added in BBG 2.6 at 100,000 Joules [Fan-wiki: 2.6 page and versions list], with "no level lock" [Fan-wiki].
- No later changes recorded. Not seen in 2026.

**Look:**
- "the only Huggable primary weapon not to have a menu display slide"; the Gear Up shows the normal stance [Fan-wiki].
- LYH.jpg (uploaded 2013-12-21) shows the 3D Pink Huggable with arms out and dark grey wrist cuffs, each set with a round glossy red light with a pale rim [Observed].
- Fan demo "Losing Your Head Demonstration" (ApplerGamers, wiki upload 2014-01-05):
  - hqdefault, hq1 and hq2 show an orange-skin Huggable from behind, head on, with blue wrist bands [Observed].
  - hq3 is washed in cyan-white (#BAFBFE to #58EEF6) with a green "LEGENDARY" kill-streak banner [Observed].
  - Reading hq3 as the "bright blue blast" filling the camera is [Inference].

**Firing:**
- One tap: "the Huggable will shake off its head, which will land at its feet and explode almost instantly" [Fan-wiki].
- It works in mid-air, and melee before the head lands cancels it [Fan-wiki].

**Projectile:** the dropped head [Fan-wiki].

**Impact / end result:**
- "a bright blue blast. The explosion created in large and spherical, and will envelop the Huggable" [Fan-wiki].
- Damage is higher the closer the enemy is, and there is no self-damage [Fan-wiki].
- "After the explosion, the Huggable simply grabs a new head, seemingly out of nowhere, and attaches it to its body" [Fan-wiki].
- Its explosion is "very similar to those caused by the Phantom Hug, the only difference between the two being the actual colour of the blast" [Fan-wiki].
- Explosives 30-70; AoE "Max Dmg 50.0, Min Dmg 300.0"; recharge 2.5 seconds in the infobox, "four second reload" in the text [Fan-wiki].
- Glitch: dying right after use leaves "not ... any head at all" [Fan-wiki].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/lyh_cr_sheet.jpg (from .../png/LYH.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/lyh_yt_sheet.png and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/up/lyh_hq3.png (from https://i.ytimg.com/vi/sShVWYc6MpQ/hqdefault.jpg, hq1, hq2, hq3)

**Depiction for shorts:** it shakes its head off, the head bounces once at its feet and flashes, and a big cyan-blue sphere blooms around the Huggable. A fresh head pops on from off-screen [wiki-based; the sphere's exact look is BBG News invention].

**Confidence:** documented.

---

## Tough Love (secondary; self-buff; default; BBR by Oct 2012, then BBG)

- **Official text:** "Conjure within yourself ancient primal magicks and funnel it into a temporary 50% bonus to all melee damage!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Tough_Love)

**Status and era:**
- Default secondary [Fan-wiki].
- The 2012 BBR Gear Up "SECONDARY" list shows TOUGH LOVE, MINI ME and PEEK A BOO (EQUIPPED), with DURATION and COOLDOWN bars [Observed: Tough_Love.jpg, uploaded 2012-10-23].
- BBR 1.4.2: cooldown 20 to 15, duration 30 to 35 [Fan-wiki].
- BBG 2.6: tired time 7 to 14, duration 35 to 10 [Fan-wiki].
- Infobox: 20-second duration, 4-second recharge, which conflicts with the version notes [Fan-wiki].

**Look:**
- Gear Up card (in the 2012 list): the pink Huggable with blue-gem cuffs runs after a fleeing brown bear in a red headband, red wristbands and a grey backpack. Glossy red hearts surround and trail it, about #D73066 highlight and #B30D34 shade [Observed].
- Infobox card (Tough_love.jpg, uploaded 2013-08-27): a grinning Huggable with plain dark wrist bands and a body tear showing grey, in front of a sweating brown bear in a red headband with a gold-bullet bandolier, with red hearts behind [Observed]. The bear resembles Oliver [Inference].
- List icon: the face in a cluster of red hearts [Observed].
- **NEW in-game evidence, BBG 2013:** in the wiki screenshot Dancing_Huggable.jpg (uploaded 2013-07-14) a pink Beach Time Huggable carrying a red team banner is trailed by a stream of small glossy hearts, mostly pink-red (#F32B5D, #F04171, #DD3F65) with a few lilac (#AE89C5) and peach (#EFAD7A) ones, white-rimmed [Observed].
  - The uploader's description reads it as "The Beach Time huggable is using Double Rainbow without the rainbows" [Fan-wiki: file description].
  - Matching the hearts to Tough Love's "trailed by a stream of hearts" is [Inference].

**Firing:**
- "the Huggable will waves its hands for approximately 3 seconds; any interruption will make the ability void (e.g. using a melee weapon)" [Fan-wiki].
- Then "the Huggable is trailed by a stream of hearts", and re-using it resets the duration [Fan-wiki].

**Projectile:** none.

**Impact / end result:** all melee damage +50% for the duration [Game text via wiki]. No hit FX of its own is documented [Unverified].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/sec_cards.jpg (from .../png/Photo_27-04-13_11_29_52_AM.png and .../png/Tough_love.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/dr_tl_lists.jpg (from .../png/Tough_Love.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/png/Dancing_Huggable.png and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/dancing_zoom.png

**Depiction for shorts:** a frantic three-beat hand-waving "spell", then a stream of small glossy pink-red hearts (a few lilac) puffs off it as it sprints at a nervous bear [card, wiki and the 2013 screenshot].

**Confidence:** partial.

---

## Mini Me (secondary; shrink; BBR by Oct 2012, then BBG)

- **Official text:** "Become very tiny and make it that much harder for enemies to hit you!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Mini_Me)

**Status and era:**
- 45,000 Joules, level 8 [Fan-wiki]. In the 2012 secondary list [Observed].
- BBR 1.4.2 fixed "Mini Me glitches in Battlefield Airpad, Facing Temples and Spacecraft" [Fan-wiki].
- BBG 2.6: duration 20 to 7 [Fan-wiki]. Infobox: 8-second duration, 10-second recharge [Fan-wiki].

**Look:**
- Gear Up card: three fading, dark, translucent Huggable afterimages with green outlines (#28881E) step down from large to small, ending in a small solid pink Huggable, with green sparkles [Observed].
- List icon: a small face in front of a larger dark silhouette [Observed].
- "Mini Me in use" screenshot (uploaded 2013-03-28): a low third-person view from behind the Huggable's bandaged head and green radio (blue-tipped antenna). The HUD shows the face-plus-silhouette icon and a Punk Bands melee icon. Size cannot be judged from it [Observed].
- **CORRECTED.** File:Mini_Me_glitch.jpg (2013-06-20) shows the yellow Gold skin from behind, red-tipped antenna, in a blue-lit corridor [Observed]. The file has no description and is used on no page [Fan-wiki metadata]. That it shows a wall clip is [Inference from the filename and the page trivia], not a wiki caption.

**Firing:**
- "the action done by the Huggable is actually the same as when one uses Peek A Boo", with a sound "similar to the 'Help me out' teamspeak. It sounds almost like the Huggable is laughing" [Fan-wiki].
- It gives no speed increase. The Huggable cannot collect pickups unless it uses Jump, the Turkish SW Boots or So Fly, and Sniper/Demo lock-ons are harder [Fan-wiki].

**Impact / end result:**
- None.
- Death glitch: it "may occasionally return to normal size and then freeze ... or ... sink through the floor" [Fan-wiki].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/sec_cards.jpg (from .../png/Photo_27-04-13_11_29_54_AM.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/list2012.jpg (from .../png/Mini_Me.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/minime_shots.jpg (from .../png/083C005C-CFF5-4B94-8170-AED887E633D8-1835-0000011331752478.png and .../png/Mini_Me_glitch.png)

**Depiction for shorts:** three neon-green ghost outlines snap down to a toy-sized Huggable with a giggle and a puff of green sparkles [following the card; the giggle follows the wiki].

**Confidence:** partial.

---

## Peek A Boo (secondary; invisibility; BBR by Oct 2012, then BBG)

- **Official text:** "By pressing small amounts of rainbow out of their bodies, Huggables can match the color of their surroundings and become all but invisible to the untrained eye!" [Game text via wiki; the page labels it "Offical"] (https://battlebears.fandom.com/wiki/Peek_A_Boo)

**Status and era:**
- 115,000 Joules, level 17 [Fan-wiki]. EQUIPPED in the 2012 list [Observed].
- BBR 1.4.2: cooldown 60 to 50, duration 20 to 25, tired time 10 to 8, damage 0 to 10 (the page says it "does not work"), and "Player becomes easier to spot due to team-coloured aura" [Fan-wiki].
- BBR 1.4.3: the neon outline was removed "only for Cloaking" [Fan-wiki].
- BBG 2.6: the outline was removed from Peek A Boo [Fan-wiki: trivia]; minimum visibility 0.02 to 0.01, maximum 0.2 to 0.1, cooldown 50 to 40, duration 25 to 30, tired time 8 to 3 [Fan-wiki: 2.6 page].
- Infobox: 4-second duration, 6-second recharge, which conflicts [Fan-wiki].

**Look:**
- Gear Up card: the Huggable reduced to an empty black silhouette with a neon-green outline (antenna, ears, arm). Its lower half sinks into puffy white clouds (#F4F4F4, shaded #BBD2E0) among floating white-blue bubbles (#DAE4F3) [Observed].
- List icon: the face in white clouds [Observed].
- Pre-1.4.2 wiki thumbnail (Mqdefaul.jpg, 320x180, captioned "A Huggable using Peek A Boo prior to v1.4.2" [Fan-wiki]): grass, a large pinkish-white glowing ring at left and a grey translucent figure with a blue team marker in the centre [Observed]. Which element is the Huggable is [Unverified].
- Before 1.4.2 the Huggable was "marked by a light greyish shape". From 1.4.2 to 2.6, "neon red/blue lines (depending on the player's team)" picked out its features [Fan-wiki].
- 2026 candidate: the trailer's unidentified rainbow burst at 3.27-3.85 s (see the last weapon section) [Observed effect; link Inference].

**Firing:**
- "a short burst of rainbow energy will be emitted above the Huggable and the player will become totally invisible" [Fan-wiki].
- Taking damage makes it visible "for an instant". Attacking or using a Special ends it, and Snipers and Demos cannot lock on [Fan-wiki].

**Impact / end result:** none on enemies [Fan-wiki].

**CONFLICT:** the wiki's rainbow burst, and the official text's "rainbow", versus the card's white clouds and bubbles.

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/sec_cards.jpg (from .../png/Photo_27-04-13_11_29_57_AM.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/list2012.jpg (from .../png/Peek_A_Boo.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/ph_sheet.jpg (from .../up/Mqdefaul.png)

**Depiction for shorts:** a short fan of rainbow rays bursts upward off the Huggable, a soap-bubble "poof" follows, and it fades to a faint outline and then nothing [2026 burst plus card plus official text; the blend is BBG News invention].

**Confidence:** partial.

---

## Super Size Me! (secondary; grow plus stomp AoE; BBG 2.20, 29 May 2015)

- **Official text:** "Super Size your huggable! Damage foes with the stomps of your feet while they scream in terror of your size! " [Game text via wiki] (https://battlebears.fandom.com/wiki/Super_Size_Me!)

**Status and era:**
- 150,000 Joules, level 10. Added in BBG 2.20, which the versions list dates May 29th, 2015 [Fan-wiki].
- "It used to be the only Huggable secondary that heals while being used, although it no longer heals" (undated) [Fan-wiki].
- Not seen in 2026.

**Look:** the page has no image [Observed: empty image list], and a File-namespace search found none [Observed]. No official image found [Unverified].

**Firing:**
- "the Huggable will grow in size and have more Melee hitbox while the player starts to create colored shockwaves similar to those of the Happy Hour and Metal Crush" [Fan-wiki].
- Slow amount 25%; Explosive damage 20-40; AoE "Max Dmg 200.0, Min Dmg 400.0"; 4 seconds; recharge 6 seconds [Fan-wiki].

**Shockwave reference:**
- The wiki's in-game "Happy Hour explosion" screenshot shows a white-cored magenta pillar of crystal shards and a flat magenta ring racing across the floor [Observed].
- Metal Crush makes "a damage-dealing golden shockwave that spreads out like the splash made by the Happy Hour" [Fan-wiki].
- Super Size Me!'s own colour and scale factor are [Unverified].

**Images viewed:** /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/hh_small.jpg (reference only)

**Depiction for shorts:** the Huggable balloons to giant size, and each stomp sends a flat coloured ring racing across the floor while bears hop or tumble [BBG News invention, following the wiki's comparison].

**Confidence:** documented.

---

## Phantom Hug (secondary; saboteur projectile; the only ranged Huggable secondary; BBG 2.2, 21 Aug 2013)

- **Official text:** "The Huggable's ability to love will make time seem like it comes to a halt. When actually it's just your feet and you're about to die." [Game text via wiki] (https://battlebears.fandom.com/wiki/Phantom_Hug)

**Status and era:**
- 40 Gas, level 1. Added in 2.2 [Fan-wiki].
- The promo art (Phantom_Hug.jpg) was uploaded to the wiki 2013-08-01, before release [file metadata]. It illustrates the wiki news post "New weapons in Battle Bears Gold update 2.2", which says the weapons were "announced on the Battle Bears Facebook page" [Fan-wiki].
- Not seen in 2026.

**Look:**
- Promo art: a "BATTLE BEARS GOLD" logo at top right and a faint "SkyVu Entertainment" watermark [Observed]. That it is official promo art is [Inference from the logo, watermark and wiki news post].
- A translucent, glowing pink ghost Huggable (#F09EB4, #E47A94, pale core #F4E9DD) with a yellow-white glowing rim wraps over the face of a screaming muscular white bear. The bear wears red wristbands and a red belt with a gold-rimmed red oval buckle, and claws at the ghost [Observed].
- The real Huggable stands small at lower right, grinning, with blue-gem cuffs [Observed].
- The same art is the menu display (PH_MenuDisplay.jpg) and the wiki front-page crop [Observed].
- Fan thumbnail ("First Phantom Hug Match... Ragequitter Noob lol #BBG #Nub", Arsenic Sushi) [Observed]:
  - purple-magenta crackling wisps around the Huggable's paws, with a violet vertical streak ahead;
  - the top-right HUD icon is a Huggable face followed by a row of grey copies.
  - Reading these as the launch and the Phantom Hug icon is [Inference].

**Firing:** single shot. Ammo 1, reload 5 seconds, and a 5% speed boost to the user [Fan-wiki].

**Projectile:**
- "a cluster of pink energy in the shape of a Huggable"; it "briefly creates a 'clone' of the character" [Fan-wiki].
- It passes through the Iron Curtain and destroys Proximity Mines [Fan-wiki].

**Impact / end result:**
- On contact with "any surface or player, it will explode in a moderate AoE" [Fan-wiki].
- Victims cannot move or turn for 2.5 seconds but can still attack, jump and use Specials. It deals no damage [Fan-wiki].
- Status icon: "a yellow Z will appear over the player's head, indicating a reduction in speed", and Phantom Hug is listed with "(immobile)" [Fan-wiki: Status Effects].
- A yellow block "Z" flanked by two curved white arrows appears over an orange Huggable in the "Charged Run Demonstration" thumbnail [Observed]. Its cause in that clip is unknown.
- Losing Your Head's blast is "very similar" apart from colour [Fan-wiki], so Phantom Hug's burst is likely a large pink sphere [Inference].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/ph_sheet.jpg (from .../png/Phantom_Hug.png, .../png/Frontpage-news-phantom-hug.png and .../up/PH_MenuDisplay.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/fan_sheet.jpg (from https://i.ytimg.com/vi/Ac4XjUzc6tY/ and https://i.ytimg.com/vi/eRL6OoX--zA/ hqdefault, hq1, hq2, hq3)

**Depiction for shorts:** a see-through pink ghost Huggable with a glowing yellow-white rim flies out, wraps over a bear's face in a hug and bursts in a pink sphere. The bear's feet stay stuck as a yellow "Z" with two curved white arrows floats over its head [art plus wiki; the sphere's look is BBG News invention].

**Confidence:** partial.

---

## Charged Run (secondary; ground dash; the only Huggable secondary that deals direct damage; BBG 2.6, 20 Dec 2013)

- **Official text:** "And I ran, I ran so far away, I ran all night and day… had to destroy all the Battle Bears?" [Game text via wiki] (https://battlebears.fandom.com/wiki/Charged_Run)

**Status and era:**
- Added in 2.6 at 160 Gas [Fan-wiki: 2.6 page; the page intro says "It costs 160 Gas and has no level lock"].
- The infobox and class page now say 60 Gas, and no price drop is documented [Fan-wiki].
- Not seen in 2026.

**Look:**
- Gear Up stance (ChargedRunStance.jpg, uploaded 2013-12-21): the 3D Pink Huggable with one arm raised (dark grey wrist band) and the other bent, with a round red light at the wrist [Observed].
- The wiki says the stance is "identical to that which the Huggable takes on when equipped with Phantom Hug" [Fan-wiki].
- Fan demo thumbnails (ApplerGamers, 2014-01-04) show an orange-skin Huggable from behind on a starry map. One frame has the yellow "Z" overhead and a green translucent disc ahead. No run FX are visible [Observed].

**Firing:**
- Tap to run at once, or hold to charge, during which "the Huggable is rendered immobile" [Fan-wiki].
- "A full charge will be indicated by sparkling particles coming out of the Huggable's body and a sound similar to a fully charged Crossbow will play" [Fan-wiki].

**Projectile:**
- The Huggable runs "forward on the ground at 600 units per second" [Fan-wiki].
- The run lasts 1.5 seconds, or 4 seconds fully charged. Full charge is given as both 3 seconds (infobox) and 2.5 seconds (text). Recharge 6 seconds [Fan-wiki].

**Impact / end result:**
- 40 damage, once per opponent it runs through. Melee cancels it [Fan-wiki].
- The equipment table (Damage+) conflicts with the trivia, which says Explosives equipment applies [Fan-wiki].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/lyh_cr_sheet.jpg (from .../png/ChargedRunStance.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/fan_sheet.jpg (from https://i.ytimg.com/vi/eRL6OoX--zA/ thumbnails)

**Depiction for shorts:** it plants its feet as sparkles leak from its body, then rockets along the floor. Bears it passes through spin like bowling pins in rainbow sparkles [the sparkles follow the wiki; the rest is BBG News invention].

**Confidence:** documented.

---

## Bite Me (melee; paired, one per paw; default; in the August 2011 BBR Sneak Peek HUD, then BBG; BBH Huggy's version)

- **Official text:** "That's a bit of iron-y." [Game text via wiki] (https://battlebears.fandom.com/wiki/Bite_Me)

**Status and era:**
- Default melee [Fan-wiki].
- In the 2012 BBR melee list (Bite_me.png, uploaded 2012-11-25), whose only stat bar is DAMAGE [Observed].
- A dark croc-jaw icon with coloured teeth is the melee slot in the official August 2011 Sneak Peek HUD [Observed; identification Inference].
- Damage history [Fan-wiki]:
  - BBR 1.4.2: 35 to 40.
  - BBG 2.6: 40 to 35.
  - The page now says "It deals 80 damage" after being "buffed recently" (undated).
- BBH Huggy wields "two automatic clamping bear traps strapped around his hands, that have dried up bits of rainbow colors on the edges of the teeth and base" [Fan-wiki: Huggy page].

**Look:**
- Two black bear-trap jaws, each an open teardrop or C-shaped loop of black metal (#0D0F0E to #212021) with zigzag teeth smeared in iridescent rainbow (red, green, blue, violet). Each is hinged on a round black disc clamped over a paw [Observed].
- Each jaw is about 0.4x the Huggable's height, about 0.28x Oliver [Inference].
- Icon: a dark crocodile-style jaw with rainbow teeth and a silver hinge [Observed].

**Firing:** a melee swing with both paws. Damage is "often doubled due to the duplicate melees" [Fan-wiki]. The swing animation is unseen.

**Projectile:** none.

**Impact / end result:**
- The wiki reads the rainbow smears as "Huggable blood" [Fan-wiki].
- Generic 2026 melee hit FX: the target flashes white, and pale-yellow five-point stars pop at contact [Observed on Punk Bands hits].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/melee_cards.jpg (from .../png/Photo_27-04-13_11_30_26_AM.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/cr_sheet.jpg (from .../png/HuggyBiteMeCR.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/png/Bite_me.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/sneak_bottom.png

**Depiction for shorts:** twin black traps snap shut with a metallic CLACK, and pale-yellow stars pop at contact. The rainbow on the teeth reads as paint, never blood [traps observed; stars from 2026 FX; tone is BBG News invention].

**Confidence:** observed.

---

## Seesaw (melee; paired chainsaw hands; BBR by Oct 2012, then BBG)

- **Official text:** "The Battle Bear who fashioned the first Huggable with chainsaw hands should not have been faulted for his scientific pursuits, but he was." [Game text via wiki] (https://battlebears.fandom.com/wiki/Seesaw)

**Status and era:**
- Price conflict: the class page says 20 Gas; the weapon page says 40 Gas with a level 3 lock. Price history: 5,700 Joules, then 50, 25 and 40 Gas [Fan-wiki].
- In the October 2012 list (Seesaw.png, uploaded 2012-10-24), with DAMAGE and SPECIAL SPEED bars [Observed].
- BBR 1.4.2: damage 45 to 49, "Special cooldown reduction changed from -15% to -20%" [Fan-wiki].
- BBG 2.6: damage 49 to 45, "Changed Special cooldown increase of 15% to Speed increase of 10%" [Fan-wiki; the two pages disagree on the sign].
- In the Aug 2013 Huggabundle, with Punk Bands and the Gummable skin: 250 Gas, discounted to 190 [Fan-wiki: Bundle Deals].

**Look:**
- An orange boxy chainsaw housing (#C13C0C to #CA3E0D) over each paw, with black vent stripes and a small sticker [Observed].
- A long dark-grey guide bar whose teeth are iridescent rainbow along the edge and tip [Observed].
- Total length about 0.7x the Huggable's height, about 0.45x Oliver [Inference].
- The 2012 screen shows it on a brown patchwork-face skin with red shirt, black tie and jeans [Observed]. That this is the Pleather Face skin is [Inference].
- The wiki's equipped render uses a glossy red skin [Observed], likely Gummable [Inference].
- The official Huggabundle banner (uploaded 2012-09-29) shows rainbow drips falling off the bar [Observed].
- Icon: an orange body with a grey bar and rainbow teeth. It is also the HUD melee icon in the Static Shuffle death screenshot [Observed].

**Firing:**
- Melee with both paws: "40 damage per saw", often doubled [Fan-wiki].
- It has the "slowest draw time but also the longest duration and largest hitbox", and +10% speed [Fan-wiki].
- Engine sound undocumented [Unverified].

**Impact / end result:** rainbow "Huggable blood" on the bar [Fan-wiki]. The wiki says it is "likely based off of the Chainsaw from Battle Bears -1" used by Riggs [Fan-wiki].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/melee_cards.jpg (from .../png/Photo_27-04-13_11_30_30_AM.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/cr_sheet.jpg (from .../png/HuggySeesawCR.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/png/Seesaw.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/png/Huggabundle.png and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/bundle_seesaw.png

**Depiction for shorts:** twin orange chainsaws rev, and the rainbow-toothed bars flick rainbow droplets like paint [art observed; the paint framing is BBG News invention].

**Confidence:** observed.

---

## Whack-Tus (melee; paired cactus clubs; one of the original three melees; seen in the 2026 playtest)

- **Official text:** "Whack-tus? Darn near killctus." [Game text via wiki] (https://battlebears.fandom.com/wiki/Whack-Tus)

**Status and era:**
- 50,000 Joules, level 9 [Fan-wiki]. "It used to be called 'The Prick'" and "used to cost 2,500 Joules" [Fan-wiki].
- A partly visible "WHACK-TUS" row sits under Seesaw in the October 2012 list [Observed, partial text].
- BBR 1.4.2: damage 40 to 43 [Fan-wiki].
- BBG 2.6: damage 43 to 40, plus "Special Cooldown reduction of 10% added" [Fan-wiki].
- The page now says 60 damage and a "+30% special speed stat modifier" [Fan-wiki].
- 2026: a Closed Playtest #4 Gear Up frame shows CHARACTER HUGGABLE, SKIN PINK HUGGABLE, with the Huggable holding green cactus clubs [Observed: JustNubz showcase auto-thumbnail hq3; fan source; the frame's timestamp is unknown].
- BBH (2024): the official "BATTLE BEARS HEROES Official Trailer 4K" (BATTLE BEARS channel) has a frame of BBH Huggy (pink, white belly, blue-tipped antenna) beside a "HUG… / MELE…" title card. It wears one big green spiked cactus club on its arm and a small spiky green piece on the other [Observed: https://i.ytimg.com/vi/ihkXJS4Oatk/hq1.jpg]. Whether this is Whack-Tus by name is [Unverified].

**Look:**
- Big dark-green cactus clubs (#20351A to #2B4B23) sheathe each forearm: ridged columns studded with lighter-green spikes [Observed].
- Each is about 0.5x the Huggable's height, about 0.35x Oliver [Inference].
- 2026: the same dark-green clubs (about #2F422D) on the Pink Huggable [Observed].
- The wiki says the icon has yellow spikes while the model is "a consistant dark green all over" [Fan-wiki].

**Firing:** a clapping swing, the same motion as Punk Bands [Fan-wiki: Punk Bands page]. It "does less damage than the Presidentures, but has a much shorter draw time and duration" [Fan-wiki].

**Impact / end result:** no specific FX documented [Unverified].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/melee_cards.jpg (from .../png/Photo_27-04-13_11_30_32_AM.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/cr_sheet.jpg (from .../png/HuggyWhacktusCR.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/nubz_sheet.jpg (from https://i.ytimg.com/vi/-lAtv-j9Sms/hqdefault.jpg, hq1, hq2, hq3)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/bbh_sheet.jpg and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/bbh_hq1.png

**Depiction for shorts:** a double cactus clap, a puff of green needles and yellow stars [BBG News invention; the stars follow the 2026 hit FX].

**Confidence:** observed.

---

## Presidentures (melee; paired wooden dentures, a Bite Me reskin; BBR 1.3.1, June 2012)

- **Official text:** "I cannot tell a lie, this weapon is historically inaccurate in a great many ways." [Game text via wiki] (https://battlebears.fandom.com/wiki/Presidentures)

**Status and era:**
- 30,000 Joules, no level lock. Released in week 2 of BBR 1.3.1; the Updates page dates 1.3.1 to June 28, 2012 [Fan-wiki].
- It appears in the "BBR 1.3.1 and BEYOND!" promo pile with the BATTLE BEARS logo (BBRWEAPONS.png, uploaded 2012-11-07) [Observed].
- BBG 2.6: damage 45 to 40, "Added health increase of 10%". The page body now says 70 damage and "a 15% health increase" [Fan-wiki].

**Look:**
- Carved wooden false-teeth jaws: a dark-brown bark outer edge (about #8E442B), pale tan inner wood with wavy grain (#F0C89D), pale sawtooth teeth, and cut-log tree-ring discs at the hinge ends [Observed].
- About 0.4x the Huggable's height, about 0.26x Oliver [Inference].
- Black straps fix each jaw at the wrist [Observed: Gear Up card].
- Icon: a tan jaw with white teeth and a log-end circle [Observed].
- The wiki's equipped render uses the Hannible skin (red grille mask, cream straitjacket with red straps) [Observed].

**Firing:** melee like Bite Me, damage "often doubled", with "a much longer draw time" than Whack-Tus [Fan-wiki]. The page calls it "most likely a joke about the fact that George Washington ... had wooden teeth" [Fan-wiki].

**Impact / end result:** none documented [Unverified].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/png/Presidentures.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/png/BBRWEAPONS.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/melee_cards2.jpg (from .../png/Photo_27-04-13_11_30_23_AM.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/cr_sheet.jpg (from .../png/HuggyPresidenturesCR.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/png/Bite_me.png (icon)

**Depiction for shorts:** giant wooden dentures chomp with a hollow wooden clack and a few splinters. Avoid the Hannible skin [BBG News invention].

**Confidence:** observed.

---

## Punk Bands (melee; paired spiked arm cuffs; BBR 1.3.1, then BBG; in the 2026 trailer and a Steam screenshot)

- **Official text:** "Your band doesn't get any gigs and your mom won't let you wear your little sister's jeans. It's too much pain for one person to bare, so make someone else feel it for a while! " [Game text via wiki; the wiki notes "bare" as a typo] (https://battlebears.fandom.com/wiki/Punk_Bands)

**Status and era:**
- 110,000 Joules ("It used to cost 100,000 Joules"), no level lock. Released in week 2 of BBR 1.3.1 [Fan-wiki]. Shown in the 1.3.1 promo pile [Observed].
- "after the v1.4.1 update, it only claps once, where it used to clap twice" [Fan-wiki].
- BBR 1.4.2: damage 45 to 40; speed reduction -25% to -20% [Fan-wiki].
- BBG 2.2: speed reduction 20% to 17% [Fan-wiki].
- BBG 2.6: damage 51 to 45, and "Changed Speed Reduction of -17% to Special Cooldown reduction of 10%" [Fan-wiki; the 1.4.2 and 2.6 damage figures don't chain].
- The page now says 70 damage with "a +10% special speed stat modifier" [Fan-wiki].
- In the Aug 2013 Huggabundle [Fan-wiki].
- 2026: in the official trailer and Steam screenshot 00 [Observed].

**Look:**
- Oversized black cylindrical cuffs over each forearm, with rows of white cone spikes on gold-tan square bases (#DEA437) and a rounded pink end cap (#DB4784) [Observed: 2013 card and render].
- About 0.5x the Huggable's height long and 0.17x thick: about 0.33x and 0.11x Oliver [Inference].
- 2026 trailer, 30.9 s: the spike studs read cream-white with pale tan edges, and the cap stays pink [Observed].
- "The top 'hand' part of this weapon will always remain pink no matter what skin" [Fan-wiki].
- But the official Huggabundle banner shows a red cap on a red glossy Huggable [Observed], while the 2026 cyan Huggable has a pink cap [Observed].
- The wiki's equipped render is on the Topsy Scurvy pirate skin (brown spotted bandana, striped shirt) [Observed; skin identified from the Topsy Scurvy page, Fan-wiki].

**Firing:**
- A clapping swing with both arms [Fan-wiki].
- 2026 trailer [Observed]:
  - At 30.9-31.1 s the pink Huggable swings a Punk Band at a sniper bear (teal face mask, blue polka-dot outfit), who renders pure white (hit flash) at 31.0-31.1 s.
  - At 35.6-35.7 s, a cyan Huggable wearing Punk Bands on both arms swings at an orange Huggable. From 35.8 to 36.3 s pale-yellow five-point stars burst at impact and around the targets' feet. Steam screen_00 is a still of this exchange.

**Impact / end result:**
- 2026 trailer, 31.2-32.2 s: a run of big starburst flashes engulfs the sniper [Observed]:
  - red-orange flame shards (31.2-31.3 s);
  - a bright yellow starburst (#FDF351, 31.4-31.7 s);
  - white bursts with lavender-purple edges (#9978F6, 31.8-32.2 s).
- Red Happy Hour missiles fall in the same shots at about 31.5-31.6 and 32.5 s [Observed]. So whether the starbursts are Punk Bands hit or kill FX, Happy Hour hits or trailer edit FX is [Unverified].
- The sniper then lies face-down while the grinning Huggable stands over it, cuffs bare and no weapon visible (32.5-32.7 s), before the "Huggable / HUGGABLE" splash card (about 32.9-34.2 s) [Observed].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/melee_cards2.jpg (from .../png/Photo_27-04-13_11_30_21_AM.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/cr_sheet.jpg (from .../png/HuggyPunkCR.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/bundle_punk.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/png/BBRWEAPONS.png
- Trailer: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/punk_zoom.jpg, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/punk2026_zoom.png, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/tsheet_21.jpg, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/tsheet_41.jpg, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/tsheet_61.jpg, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/cyan_orange_zoom.jpg, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/f032_hug.jpg, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/f033_hug.jpg and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/pinkfig_zoom.jpg
- Steam: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/steam_screens/screen_00.jpg

**Depiction for shorts:** spiked black cuffs flash into view for a double-fisted haymaker. The target flashes white, pale-yellow stars pop, and for a KO the target flops face-down while the Huggable grins over it with bare red-light cuffs [2026 observed]. Any extra starburst is optional colour [BBG News invention].

**Confidence:** observed.

---

## Bearettas (melee; paired spiked pistol gauntlets, never fired; BBG 2.21, 3 Jul 2015)

- **Official text:** "Good thing Huggables don't have thumbs, otherwise they would actually be able to use these" [Game text via wiki] (https://battlebears.fandom.com/wiki/Bearettas)

**Status and era:**
- 20 Gas, level 5 [Fan-wiki]. Added in BBG 2.21 ("New Melees ... Bearettas", July 3rd, 2015) [Fan-wiki: versions list]. The page is a stub.
- Not seen in 2026.

**Look:**
- Two oversized pistol-shaped gauntlets run along each forearm, strapped on rather than held [Observed]. Details:
  - magenta-pink (#D3407F, #A73C5A) and dark grey;
  - a glowing cyan stripe and a small cyan "B" emblem on the side;
  - two grey barrel tubes at the front end and two round holes in the pink body;
  - a row of white cone spikes along the top, and white flourish decals.
- **CORRECTED:** the draft had the "B" emblem as unverified; it is visible, though at low resolution.
- About 0.5x the Huggable's height, about 0.33x Oliver [Inference].
- Shown on a pink Huggable with orange-rimmed sunglasses and red floral swim trunks [Observed]. This is the Beach Time skin, whose trunks are "team-colored" [Fan-wiki: Beach Time; identification Inference].
- Colours on the default skin are [Unverified].

**Firing:**
- Melee only: 65 damage, "+20% speed increase and a -50% Special Speed decrease" [Fan-wiki].
- "two modified pistols, fitted with some sort of arm guards and spikes, which are what are used as the actual weapon" [Fan-wiki].
- No bullets [Inference from the official text].

**Impact / end result:** none documented [Unverified].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/up/Image19.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/bearetta_zoom.png

**Depiction for shorts:** it aims the pistol gauntlets, squeezes with no thumbs and nothing happens, so it swings the spiked guards instead [official text and render; the gag is BBG News invention].

**Confidence:** observed (one render).

---

## Beaver Feaver (melee; paired wooden chainsaws, a Seesaw reskin; BBR 1.3.1, June 2012)

- **Official text:** "Cut your enemies down to size!... and then stack their bodies in a river and raise a family in there again or something... I'm sorry, that analogy got away from me pretty quick there." [Game text via wiki] (https://battlebears.fandom.com/wiki/Beaver_Feaver)

**Status and era:**
- 20 Gas, no level lock. Released in week 2 of 1.3.1; the 1.3.1 page lists it as "Beaver Fever" [Fan-wiki].
- The in-game list spells it "BEAVER FEAVER" [Observed].
- BBR 1.4.2: damage 33 to 42, health boost +25% to +20% [Fan-wiki].
- **CORRECTED:** the October 2012 screen predates 1.4.2, so of course it shows "HEALTH +25%" [Observed].
- BBG 2.6: damage 42 to 40 [Fan-wiki]. The page now says "40 damage per saw" and "a 20% health increase" [Fan-wiki].

**Look:**
- A wooden chainsaw. The blade is maroon-brown wood carved with a cross-hatched waffle pattern (#582F16 to #5A2D15), edged with orange-peach teeth [Observed].
- It is mounted in a slatted wooden crate housing with silver metal corners and lime-green tape binding at the joint (#5E7A15 to #81922B) [Observed].
- About 0.65x the Huggable's height, about 0.42x Oliver [Inference].
- Icon: the waffle blade with its crate [Observed].
- It also appears as the waffle-bladed saw in the 1.3.1 promo pile [Observed].

**Firing:** like Seesaw, "40 damage per saw", often doubled [Fan-wiki].

**Impact / end result:** none documented [Unverified].

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/melee_cards2.jpg (from .../png/Photo_27-04-13_11_30_15_AM.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/cr_sheet.jpg (from .../png/HuggyBeaverCR.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/png/Beaver_Fever.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/png/BBRWEAPONS.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/png/Bite_me.png

**Depiction for shorts:** wooden saw blades whirr like chattering beaver teeth and spit wood chips [BBG News invention].

**Confidence:** observed.

---

## Unidentified Huggable rainbow burst (sub-topic; 2026 official trailer, 3.27-3.85 s)

- **Official text:** none ties this shot to a named weapon [Unverified].

**What it shows** [Observed: trailer frames q_005 to q_027, 30 fps]:
- 3.0-3.2 s: a small pink Huggable carrying a tall red banner with pale symbols stands on a cave ledge while a B-1000 fires in the foreground and a thin yellow tracer streaks along the floor toward it.
- 3.27 s: two rainbow beams shoot out horizontally left and right from a glowing magenta point at its feet.
- 3.33-3.53 s: four or five rainbow rays fan upward in a V from that point.
- 3.60-3.80 s: the rays narrow into a blue-violet column above it. Meanwhile the Huggable glows bright pink-white with its arms flung out.
- 3.87 s: the Huggable is plain pink again. The shot cuts at about 3.9 s.
- Ray colours, sampled: red-orange #D1441C, amber #D7A421, lime #ADD635, green #1CB940, teal #12CC93, cyan #1894C9, blue #1749AF, violet #8F36A6, magenta core #D325A2 [Observed].

**Which weapon?** [Inference] Two readings:
- The wiki's Peek A Boo text ("a short burst of rainbow energy will be emitted above the Huggable") and its official text ("pressing small amounts of rainbow out of their bodies"). Mini Me shares the activation animation [Fan-wiki].
- Double Rainbow! ("two spinning rainbows that rotate around the user"), given the two horizontal beams at 3.27 s.

Neither is confirmed: the Huggable does not visibly vanish or shrink before the cut [Observed].

**Projectile:** none observed. The rays stay anchored at the Huggable [Observed].

**Impact / end result:** none observed in the shot.

**Images viewed:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/early_zoom.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/early_rainbow.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/early_hug_tight.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/banner_2026.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-verify/crops/full_1.jpg

**Depiction for shorts:** usable as a generic "Huggable powers up" beat: a magenta spark at its feet, rainbow rays fanning up into a column, and a pink-white glow [Observed]. Do not caption it as a specific ability until it is identified [BBG News invention].

**Confidence:** partial.

---

## Editor's changes to the draft (all re-checked today)

1. **Headlights card.** The head is detached and sits low in front of the bowed body, with nothing shown holding it. The beam fires out of the neck hole away from the face. The draft said the head was "held low at the Huggable's side".
2. **Wrists.**
   - The 2013 melee renders are not "bare": the weapon mounts cover the wrists, with black straps on the Presidentures card.
   - The Aug 2013 Tough Love card shows plain dark bands, not blue gems.
   - The orange skin in-game has blue bands.
3. **Antenna tip.** It is red on Gear Up renders and in 2026, and blue in 2012-13 in-game footage and 2D cards.
4. **So Fly.** The column rises from the Huggable's feet in rainbow order, so it is its own trail. The falling Happy Hour missile lands at the column's base just before the magenta burst, which strengthens the Happy Hour attribution. I added the wiki-embedded So Fly gameplay video (Do3Ja12MpSI), now gone from YouTube.
5. **NEW 2026 shot.** I added the unidentified rainbow burst at 3.27-3.85 s.
6. **Tough Love.** I added the 2013 in-game heart stream (Dancing_Huggable.jpg). The uploader reads it as Double Rainbow.
7. **Losing Your Head.** The fan thumbnail hq3 shows a cyan-white wash, a candidate for the blue blast. The draft said "no blast".
8. **Mini_Me_glitch.jpg.** It has no wiki caption, so "inside a wall" is inference.
9. **Bearettas.** The cyan "B" emblem is now observed.
10. **Whack-Tus.** Added a BBH-era cactus club from the official BBH trailer thumbnail.
11. **2026 trailer melee display.** Weapons appear only during swings; idle arms show red-light cuffs.
12. **Labels and wording.**
    - So Fly v2.0 is relabelled [Fan-wiki] instead of [Inference].
    - Double Rainbow's damage falloff is relabelled [Inference] instead of a quoted infobox claim.
    - Whack-Tus 2.6 is reworded to "10% special-cooldown reduction".
    - Punk Bands' current 70 damage and +10% special speed are added.
    - The Beaver Feaver "still shows +25%" wording is fixed.
    - The Phantom Hug promo provenance is added.
    - The Gear Up card era is corrected to "BBR, by Oct 2012".
13. **Team banner.** The red banner with three pale symbols is observed in both 2013 and 2026. This reverses the draft's character-file correction #3.
14. **Torn belly.** The wiki does call the wound "metalic". The draft wrongly called "metal" unverified.
15. **So Fly, Shortest Parsec Easter egg (2026-10-18, from the verified maps research).** The class page's "only class that can reach" claim is now marked contested. It echoes map-page wording replaced on 2014-05-27 (rev 64712), and the current map page credits B-1000's Metal Crush as well as So Fly.

## Corrections for the character file (/home/user/thallo-site/bbg-news-repo/characters/huggable.md)

1. **Prompt pack, "steel bear-trap jaws over both paws".**
   - Change to: "two black bear-trap jaws (open C-shaped loops on round black wrist discs) clamped over both paws, zigzag teeth smeared with iridescent rainbow".
   - Evidence: Photo_27-04-13_11_30_26_AM.png, HuggyBiteMeCR.jpg and Bite_me.png (2012 Gear Up) [Observed].
2. **Prompt pack, "Metal wristbands with blue gems, a metal knee brace".**
   - For the 3D BBG and 2026 look, use dark grey wrist cuffs, each with a round glossy red light, and no knee brace.
   - Evidence for the red lights: LYH.jpg and ChargedRunStance.jpg (2013-12-21) and the 2026 trailer at 32.6-32.7 s [Observed].
   - Blue-gem bands and the knee brace appear only on 2D art: Huggable-suction-pose.png and the Gear Up cards, with the knee brace on the Headlights card [Observed].
3. **Prompt pack, "a small red team banner with three white symbols on its back".**
   - Keep red with three white symbols, which is observed in BBG 2013 (Dancing_Huggable.jpg) and in the 2026 trailer at 3.0-3.9 s.
   - Change "small" to "a tall, narrow vertical banner on a pole rising above its head, symbols stacked vertically".
   - Blue-team Huggables carry blue banners (Steam screen_00 and screen_04) [Observed].
   - The draft's proposed correction, that 2026 shows only blue or white banners, is wrong.
4. **Prompt pack, "a boxy military-green radio with a white antenna".**
   - Change to "a boxy green radio with a thin grey antenna tipped with a red ball (2013 renders and 2026); 2012-13 in-game footage and 2D cards show a blue tip".
   - Evidence: the 2013 CR renders, LYH.jpg and the trailer at 32.6 s show red; the Static Shuffle fan thumbnails (2013) and the Mini Me in-use screenshot show blue [Observed].
5. **Prompt pack, "a torn belly patch showing metal"; Look line, "a torn belly showing metal [Observed]".**
   - Refine to "a torn belly showing grey-and-white crumpled stuffing". Images show grey and white crumpled material [Observed], and the wiki says "metalic jagged wound" with "stuffing bulging out" [Fan-wiki: Pink Huggable].
   - So "metal" is [Fan-wiki], not [Observed].
6. **Look line, "Possibly official 2012 art adds metal wristbands with blue gems and a knee brace [Observed] ([art][art2012])."**
   - Append: "2D art only; the 3D model wears dark grey cuffs with red lights (or the weapon mount), and the orange skin in-game wears blue bands" [Observed: LYH.jpg, 2026 trailer 32.6 s, Steam screen_00].
7. **Weapons bullet, which lists 9 of 18.**
   - Give the full kit [Fan-wiki: class page]:
     - Primaries: Double Rainbow! (default), Headlights, So Fly, Static Shuffle, Losing Your Head.
     - Secondaries: Tough Love (default), Mini Me, Peek A Boo, Super Size Me!, Phantom Hug, Charged Run.
     - Melee: Bite Me (default), Seesaw, Whack-Tus, Presidentures, Punk Bands, Bearettas, Beaver Feaver.
   - Upgrade "Bite Me (bear-trap hands, per the wiki)" to "Bite Me (black bear-trap jaws with rainbow-smeared teeth) [Observed]".
8. **Comedy beat, "The Bearettas squirt out of its thumbless paws like soap, so it hugs them instead."**
   - The Bearettas are pistol gauntlets strapped along the forearms (Image19.PNG) [Observed], so they cannot slip out of its paws.
   - Use instead: "it aims the strapped-on Bearettas, has no thumbs to pull the triggers, nothing fires, so it clubs with the spikes" [official text plus render].

## Open questions

- What do Double Rainbow!, Headlights, Static Shuffle, Losing Your Head, Mini Me, Peek A Boo, Super Size Me!, Phantom Hug and Charged Run look like in 3D in 2026? This needs gameplay frames. The JustNubz showcase Huggable chapter (14:16-17:44) is the best lead, but YouTube video is blocked here.
- Which ability is the 2026 trailer's rainbow burst at 3.27-3.85 s: Peek A Boo or Mini Me activation, Double Rainbow!, or something else?
- Are the 31.2-32.2 s starbursts Punk Bands kill FX, Happy Hour hits or edit FX? Is the 30.3-30.8 s flight definitely So Fly?
- Shortest Parsec Easter egg: can only the Huggable reach it (the class page), or can B-1000's Metal Crush reach the red-base meteorite too (the map page since 2014, where some players also claim a Jump Boots double jump)? Is it still reachable in 2026?
- Static Shuffle in-game: does the head come off (wiki) or does the neck stretch (card)?
- Is the cyan-white wash in the LYH demo thumbnail hq3 the "bright blue blast"?
- Is the 2013 heart stream in Dancing_Huggable.jpg Tough Love, as inferred, or a Double Rainbow glitch, as the uploader says?
- What did BBG 2.11's "Huggable overhaul" (27 Aug 2014) change? The official 2.6 change log and SkyVu patch notes are unread: the live URL is 404 and the Wayback Machine was unreachable.
- What are the 2026 prices and stats? Open conflicts: Seesaw 20 vs 40 Gas, Charged Run 60 vs 160 Gas, Bite Me 35 vs 80 damage, Punk Bands 45 vs 70 damage.
- Does the yellow "Z" show on Phantom Hug victims in 2026? What caused the "Z" and the green disc in the Charged Run demo? The Status Effects page also lists Slow Motion Field, Slow Field, Bind Gun and Glue Bomb.
- What are Super Size Me!'s shockwave colour and size factor?
- Peek A Boo activation: rainbow rays or a cloud of bubbles?
- What colour is the Punk Bands cap on other skins (pink per the wiki, red in the Huggabundle art)? What colours do the Bearettas take on the default skin?
- Is BBH Huggy's cactus club the Whack-Tus by name?
- In 2026, are melee weapons drawn only during swings as a rule? What are the team banner rules beyond red and blue?