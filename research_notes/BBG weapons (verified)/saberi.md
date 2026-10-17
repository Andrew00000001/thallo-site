# Saberi (Combat Tech) weapons dossier, verified edition

Saberi is the Combat Tech class in Battle Bears Gold (BBG). SkyVu added her in update 2.4 on Oct 24, 2013: "New Combat Tech Class: Saberi" [Canon: 2.4 notes, saved copy].
- **How her kit works:**
  - She holds one primary in her paws.
  - A jointed "third arm" reaches out from behind her back and holds her secondary beside her for a timed window ("Saberi decided to create herself a third arm and put them there" [Game text via wiki: Missiles]; timing [Fan-wiki: Missiles, Minigun (Combat Tech), Gamma Burst]).
  - Her melees are two hammers and a club.
- **Kit size:** 5 primaries, 4 secondaries and 3 melees [Fan-wiki: Combat Tech (BBG) class page, re-fetched today].
- **Battle Bears Heroes (BBH):** BBH recasts her as a Medic with two new weapons [Canon: battlebears.com/pages/characters]. The wiki dates her BBH release to "Summer 2023" [Fan-wiki].

**Sources reached (2026-10-17)**
- Fan wiki MediaWiki API: all 12 weapon pages, the class page, Status Effects, Updates, Battle Bears Gold/Versions, Battle Bears Heroes, Sake Bomb, Sucker Punch and Phantom Hug. I also pulled the full revision history of every weapon page and the image metadata and image files. Every Saberi weapon page was last edited on 2020-11-10.
- battlebears.com/pages/characters (live).
- Steam appdetails 4408320 (live). It shows "-COMBAT TECH: Saberi" and release "Nov 4, 2026".
- YouTube:
  - I re-downloaded thumbnails (maxres1-3 at 1280x720 where offered).
  - Upload dates and descriptions come from YouTube's `youtubei/v1/next` metadata. oEmbed gave titles and channels.
  - I have watched no video.
- The local official Steam trailer frames t_0001-t_0108 and Steam screenshots 00-04.

**Not reachable**
- web.archive.org failed every time today:
  - 119 curl attempts between 18:08 and 19:07 (connection reset, HTTP 000).
  - WebFetch: "unable to fetch from web.archive.org".
  - The availability API answered "429 Too Many Requests".
- So every [Canon] SkyVu blog quote below comes from copies an earlier session saved on 2026-10-14: `W/dl/saberi/official/prior/u24.html.txt`, `u29.html.txt`, `u29peek.html.txt`, `cl26.html.txt` and `saberi29.png`. I re-read them today but could not re-fetch them. The 2.6 change-log copy has no author or date line.
- SkyVu's "Saberi-Blog.png" is still unviewed.

**Eras**
- BBR (2012): no Combat Tech.
- BBG 2013-2021: 2.4 launch kit, then additions through 2.53 in 2018. Fan titles from 2018 call the game "Battle Bears Royale 2.53" [Observed: video titles].
- BBG 2026 re-release: Steam lists the class. A fan beta thumbnail shows two of her 2.9 weapons.
- BBH: Huggable Splicer and Healing Turret.

**Path key** (every file cited below was opened today)
- `W` = /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons
- `V` = W/dl/saberi-verify
  - `V/png/` holds wiki images re-downloaded today (converted from WebP).
  - `V/yt/<videoId>/<frame>.jpg` holds YouTube thumbnails.
  - `V/crops/` holds my crops and contact sheets.
- `W/visuals/trailer/t_NNNN.jpg` = Steam trailer frame at (N-1)×0.5 s.

**Size and colour conventions**
- Scale: Saberi = 1.0x Oliver [BBG News invention, from the BBG News scale chart]. So "x her height" means "x Oliver".
- Sizes are estimates from the wiki model screenshots [Inference].
- Hex values are approximate median (or lit-percentile) samples from the named image, not official values.

## What this verification changed (summary)
- **Missiles:** the two missiles are stacked one above the other, not side by side. The dark hexagons seen head-on are most likely the black nose cones, not tail ends.
- **Missiles blast:** I found a candidate frame for the Missiles explosion: a translucent yellow and lime faceted starburst while the Missiles button is active and the primary is empty.
- **Minigun:** 2016 footage shows its beams as pale cyan crackling bolts, not only magenta.
- **Energy Rifle:**
  - The main-menu rifle is mid-grey, not "pale grey-green".
  - The "2013 HUD icon" citation pointed at a 2016 video. It is now fixed to an Oct 2013 frame.
  - A Nov 2013 Energy Rifle kill frame shows the victim breaking into chunks.
- **Secondary button colours:** green = ready, cyan = deployed, red ring refilling with green = recharging. The draft had cyan for "ready or active".
- **Irradiated icon:** the wiki says "three stages" but shows four icons. The full trefoil stage is visible in the 2026 trailer.
- **ClubCobra:** "+10% vs +15% Health" is not a contradiction. +10% (with -5% speed) was the 2015 value, and +15% is the wiki's Nov 2020 value.
- **Landmine:** it also uses the backpack button (cyan when active, red-green while recharging). It is not purely an ammo weapon.
- **2026:** the full build stamp on the 2026 beta thumbnail reads "3.0.7_2026.11.19_b7". The Steam-trailer claim is corrected: it has no Saberi card, but its gameplay is not proven to be 2013 footage.
- **Dates:** B7FHI1aDgsw is dated Oct 28 2013 (the draft said "probably"). The Minigun beta "1 Joule" price is confirmed as a placeholder by the uploader's note "IGNORE THE PRICES, THIS IS BETA".

## Class-wide visual rules (apply to every weapon below)

- **The third arm:**
  - In game it is a thin khaki-grey rod arm (rod ≈#5A5447, lit #736C5C) with rounded tan/brass joint caps (≈#6A5C39, lit ≈#807152) [Observed: V/png/SideMissiles.png, V/png/SideMinigun.png, V/png/Missiles.png].
  - Every secondary sits on it at head height, out to her right (the viewer's left in front views) [Observed: V/png/Missiles.png, Minigun.png, Gammaburst.png, Landmine.png].
  - SkyVu's 2014 art shows a similar khaki jointed arm (rod ≈#6B5942) holding the saucer above her head [Observed: V/official/saberi29_copy.png].
  - The wiki says the missile launchers "slowly emerge from the right side of the Combat Tech's backpack" [Fan-wiki: Missiles]. It says the Gamma Burst disc emerges "from the Combat Tech's backpack" [Fan-wiki: Gamma Burst].
- **Signature glow:**
  - Her glowing tech parts are magenta/hot pink, not violet. In game: PMG core ≈#FC00FE, Minigun barrel ≈#BE00AF (lit #DB00C9), Plasma Shotgun crystal ≈#E144EC (lit #F9A2FA), Gamma Burst rim ≈#C725DB-#F9A1FE [Observed, sampled from V/png/ images].
  - The 2014 art reads ≈#F643FE-#FF45FF [Observed: saberi29_copy.png].
  - Exceptions: the Landmine's cyan circuitry (≈#529396, bright #34C9D0) and the Toxic Rifle's pink liquids [Observed].
- **Secondary system:**
  - Tapping the secondary deploys it. The button "will turn blue and not respond to tapping for the duration of the ability", then recharges [Fan-wiki: Missiles; similar wording on Minigun (Combat Tech) and Gamma Burst].
  - She is "the only class that cannot switch weapons at all and the only class which adds a button to the HUD (the button used to activate her secondaries)" [Fan-wiki: Combat Tech (BBG)].
  - In fan frames the button ring is green when ready, cyan while deployed, and a red ring filling with green while recharging:
    - green while the PMG fires: V/yt/B7FHI1aDgsw/hq3.jpg
    - cyan with Minigun beams: V/yt/B7FHI1aDgsw/hq1.jpg
    - red-green: V/yt/LSBL0QqCa_o/hq1.jpg
    - cyan for the Landmine: V/yt/ua2j5t23T80/maxres1.jpg
    - [Observed; reading green as "ready" is Inference]
- **Status icons used by her weapons:**
  - **Irradiated (in game):**
    - At low radiation, a yellow disc split by thin black lines into six wedges around a black centre floats over the target [Observed: official SkyVu footage V/yt/wUWf9O-YX4A/maxres2.jpg, May 21 2014].
    - Mid-stage it shows a yellow disc with black cut-outs [Observed: V/yt/Rn_X7MA23ho/maxres1.jpg, Jun 4 2014; V/yt/Q46ZMPrChm4/maxres1.jpg, Oct 5 2017].
    - At the top stage a bold yellow-and-black radiation trefoil appears [Observed: 2026 Steam trailer W/visuals/trailer/t_0018.jpg, 8.5 s, on a target hit by an Engineer; V/crops/t18_rad.png].
    - Yellow samples: ≈#F0C30C (2014).
  - **Irradiated (wiki account):**
    - "a yellow circle will appear over the player's head and a noise from a Geiger counter will begin sounding, indicating a chance at a premature death by self explosion, regardless of any health remaining" [Fan-wiki: Status Effects].
    - "three portions of the circle will dissolve into the common radioactivity symbol" [Fan-wiki]. The page says this "happens in three stages", but its table shows four icons (1-24, 25-49, 50-74 and 75-99 RP). The icons are black silhouettes of a six-wedge disc losing alternate wedges until a trefoil remains [Observed: V/png/Hazard-3.png … Hazard-0.png; V/crops/sh_hazard2.png].
    - At 100 RP the target explodes. The blast radius is "between 150-200 units", and decay is "estimated to be around 3-5 RP per second" [Fan-wiki].
  - **Poisoned:**
    - "a purple/green skull will appear over the player's head" [Fan-wiki: Status Effects].
    - Observed as a round dark-purple skull (≈#410C3A) [Observed: V/yt/JO5-kfnENtM/maxresdefault.jpg; V/crops/jo5_skull.png].
    - The same icon appears in official SkyVu footage on another class's victim [Observed: V/yt/xp5B76ExuAI/maxres2.jpg, May 7 2014].
- **Melee contact:** yellow 5-point cartoon stars scatter around a target hit at close range in Saberi footage [Observed: V/yt/n84q9Ptu13c/maxres3.jpg, Jul 12 2015; V/yt/0rQcyVwWSOs/maxres3.jpg, Jan 16 2016; which melee hit is Inference]. This matches the shared BBG melee-star convention.
- **2026:**
  - The only 2026 image of her weapons is M1kaa717's "BATTLE BEARS GOLD 2026 FINAL BETA HIGHLIGHTS" (Oct 16 2026) [Observed: V/yt/s9W6eLXj9qc/maxres3.jpg].
    - It shows Saberi from behind: dark-brown fur, a red white-dotted bandana and a red top.
    - She holds the Plasma Shotgun with the Gamma Burst saucer out.
    - The corner build stamp reads "3.0.7_2026.11.19_b7 / 11502154" [Observed: V/crops/s9w_stamp2.png]. What the "2026.11.19" in the build label means is [Unverified].
  - **The Steam trailer:**
    - It has class cards for B-1000, Graham, Astoria, Wil, Tillman, the Huggable, Riggs and Oliver, but none for Saberi. I could not identify her in any gameplay frame [Observed: W/visuals/trailer/t_0001-t_0108; V/crops/trailer_sheet_0..3.png].
    - The Graham verifier matched the cards to SkyVu's May 30 2013 trailer. The gameplay's capture date is unsettled [cross-reference: out/verified/graham.md].
  - The JustNubz showcase lists "44:12 Combat Tech (Saberi)" and "47:23 Arbiter (Sanchez)" in its description [Observed: YouTube metadata W/dl/2026-changes/yt/next_-lAtv-j9Sms.json]. It is unwatched.

## Energy Rifle (primary, default; BBG 2.4, Oct 24 2013 onward; 2026 unconfirmed)
- **Official text:**
  - SkyVu gives only the name: "2 Primary Weapons (Energy Rifle, Plasma Machine Gun)" [Canon: 2.4 notes, saved copy of https://web.archive.org/web/20131101183026/http://battlebears.com/battle-bears-gold-update-2-4-now-available-release-notes/].
  - "Other babies have toys, Saberi had this Energy Rifle. She patched it and rebuilt it hundreds of times, but this trusty rapid firing gun has been with her forever." [Game text via wiki] (https://battlebears.fandom.com/wiki/Energy_Rifle)
- **Look:**
  - The wiki model seen head-on (caption "Saberi with the Energy Rifle", uploaded 2013-10-25) is weathered grey-tan metal [Observed: V/png/EnergyRifle.png; V/crops/er_gun.png]:
    - a ribbed upper ring (≈#60594E, lit #B1ACA2)
    - a pale grey cylindrical segment (≈#828381)
    - a squared lower body (≈#4B453F-#534E45) ending in a round black muzzle
  - She raises it at shoulder height in her right paw, muzzle toward the viewer, with her other arm across her chest [Observed: same image].
  - In a main-menu screenshot (wiki upload Nov 2014; capture date unknown) she holds a long mid-grey rifle (≈#4E4F4A, lit ≈#5E665F) with a round dark muzzle, pointing to her right at chest height. It is roughly 0.5x her height [Observed: V/png/Combat_tech.png; V/crops/ct_gun.png; length and identity are Inference].
  - HUD icon: a long grey-brown rifle silhouette [Observed: V/yt/xuV8Rc4mGeU/maxres1.jpg, Oct 25 2013].
- **Firing:**
  - Single shots. "the Energy Rifle fires off a straight purple plasma ray in the exact direction of the crosshairs", hitting "the first opponent it comes into contact with". "It is extremely accurate as it has no angle of dispersion." [Fan-wiki]
  - Current infobox: damage 20, rate of fire 1 s, ammo 6, reload 4 s [Fan-wiki].
  - Revision history [Fan-wiki]:

    | Date | Damage | Ammo | Rate of fire | Reload |
    |---|---|---|---|---|
    | Oct 28 2013 | 55 | 4 | 1 s | 3.5 s |
    | Dec 28 2013 | 50 | 3 | 1 s | 3.5 s |
    | Mar 6 2014 | 35 | 6 | 0.8 s | 5 s |
    | Sep 18 2014 | 40 | 6 | 0.8 s | 5 s |
    | Mar 11 2018 | 30 | 6 | 0.75 s | 4.75 s |
    | Nov 10 2020 | 20 | 6 | 1 s | 4 s |

  - The HUD reads "/4" in Oct-Dec 2013 [Observed]:
    - V/yt/tw2ATkRTKTE/sddefault.jpg (Oct 4 2013 beta)
    - xuV8Rc4mGeU (Oct 25 2013)
    - NcaNiWdT6dE/hqdefault (Nov 2 2013)
    - jnkMl7m2qmk (Nov 16 2013)
    - 8F69eJnbIg8 (Dec 1 2013)
  - One Nov 2 2013 video reads "7 / 7" [Observed: V/yt/wAQLCQDHUZk/maxresdefault.jpg; V/crops/sh_waq_ammo.png]. Ammo equipment is the likely reason [Inference].
  - The HUD reads "/6" in 2015-2016: n84q9Ptu13c (Jul 12 2015) and uel_FVoF0L4 (Mar 19 2016) [Observed].
  - Wiki trivia: "Even though it says in the description that it's a rapid firing gun, it actually has a RoF of 1 second." [Fan-wiki]
  - The firing sound is undocumented [Unverified].
- **Projectile:**
  - **2013:** a magenta ribbon beam (bright ≈#FF23B7). A pink corkscrew spiral wraps its first stretch, flanked by two translucent violet wing-like flares (≈#DB5AF2) [Observed: V/yt/NcaNiWdT6dE/hqdefault.jpg, Nov 2 2013; V/crops/sh_nca.png].
  - **2016:** a straight pale cyan beam (≈#A2CEE0, bright #B4EFFF) [Observed: V/yt/uel_FVoF0L4/maxresdefault.jpg, Mar 19 2016, ammo 0/6]. In that frame the Missiles button is also cyan (deployed), so the attribution to the rifle is [Inference].
  - Whether the colour changed in a patch, or depends on team or skin, is [Unverified].
- **Impact / end result:**
  - **2013:**
    - A pale pink-white half-dome flash where the ray lands [Observed: NcaNiWdT6dE/hqdefault; V/crops/nca_target.png].
    - A small magenta half-dome glow on the ground [Observed: V/yt/xuV8Rc4mGeU/maxresdefault.jpg and maxres2.jpg].
  - **Kill frame (Nov 2013):** the struck target breaks into large brown toy-like chunks, and a blue lightning-bolt Joules pickup pops out. The kill feed reads "KILLS … +25 +100" [Observed: NcaNiWdT6dE/hqdefault; nca_target.png]. The Missiles button is cyan in the same frame, so which weapon made the kill is [Inference].
  - **2016:** white concentric ripple rings on the floor around the hit point [Observed: uel_FVoF0L4/maxresdefault].
  - No status effect is documented [Fan-wiki].
- **Images viewed:** V/png/EnergyRifle.png; V/png/Combat_tech.png; V/crops/er_gun.png; V/crops/ct_gun.png; V/crops/sh_er.png; V/yt/NcaNiWdT6dE/{maxresdefault,maxres1,maxres2,maxres3,hqdefault}.jpg (sheet V/crops/sh_nca.png); V/crops/nca_target.png; V/yt/xuV8Rc4mGeU/{maxresdefault,maxres1,maxres2,maxres3}.jpg (V/crops/sh_xuv.png); V/yt/uel_FVoF0L4/{maxresdefault,maxres1-3}.jpg (V/crops/sh_uel.png); V/yt/tw2ATkRTKTE/sd*.jpg (V/crops/sh_tw2.png); V/yt/jnkMl7m2qmk/sd*.jpg (V/crops/sh_jnk.png); V/crops/sh_waq_ammo.png.
- **Depiction for shorts:** Saberi raises the long weathered grey-tan rifle and fires one straight magenta ray per beat, with a pink corkscrew and violet "wings" at the muzzle. It ends in a pink-white half-dome pop on the target [Observed, 2013 look]. Use the pale-cyan beam only for a 2016-set short. Recoil hops and spark chips are [BBG News invention]. For a KO, show clean toy-like chunks and a bolt-shaped pickup, never gore [Observed style].
- **Confidence:** observed (2013 look and shot); partial (beam colour across eras).

## Plasma Machine Gun (primary; BBG 2.4, Oct 24 2013; 2026 unconfirmed)
- **Official text:**
  - SkyVu gives only the name [Canon: 2.4 notes].
  - "When others were learning to ride bikes, Saberi was building combustible engines. However that engine just so happened to be hooked up to power this machine gun." [Game text via wiki] (https://battlebears.fandom.com/wiki/Plasma_Machine_Gun)
- **Look:**
  - Seen head-on, a large octagonal grey metal muzzle housing about 0.2x her height across [size Inference].
  - Four dark trapezoid vents surround a glowing magenta core (≈#FC00FE), with white glow puffs on both sides.
  - She holds it at chest height [Observed: V/png/PlasmaMachineGun.png; V/crops/pmg_muzzle.png, pmg_core.png].
  - In play it is a chunky grey blaster with magenta-glowing slots, and the HUD icon is a grey blaster with magenta [Observed: V/yt/NcaNiWdT6dE/maxres1.jpg, 28/30; V/yt/wRXMFQqYxRQ/sddefault.jpg, Aug 28 2014, 40/40; identification from the ammo count is Inference].
- **Firing:**
  - "The Plasma Machine Gun works like a standard hitscan automatic, firing beams in quick succession" [Fan-wiki].
  - Current: damage 3, 0.15 s, ammo 40, reload 4 s, dispersion 0.03 [Fan-wiki].
  - Oct 2013: damage 8.0, 0.2 s, ammo 30, reload 3 s. Ammo became 40 on Mar 8 2014 [Fan-wiki revisions].
  - Price: 80 Gas in every revision up to 2018, then 60 Gas from Nov 2020 [Fan-wiki].
  - The HUD reads "/30" in B7FHI1aDgsw and LSBL0QqCa_o (Oct 28 2013), yKXifUx8lyY (Oct 29 2013), NcaNiWdT6dE (Nov 2 2013) and 4iVi02vnIPk (Jan 28 2014). It reads "/40" by Aug 28 2014 (wRXMFQqYxRQ) [Observed].
- **Projectile:**
  - Thin magenta-pink beam lines converge on the target while the Minigun button is recharging, so the beams are the PMG's [Observed: V/yt/yKXifUx8lyY/maxres1.jpg, Oct 29 2013, 15/30].
  - Pink-white beams fire with the Minigun button green (not deployed) [Observed: V/yt/B7FHI1aDgsw/hq3.jpg, Oct 28 2013, 21/30].
  - A violet streak at 20/30 [Observed: V/yt/tw2ATkRTKTE/sd3.jpg, Oct 4 2013 beta].
- **Impact / end result:** a white-pink puff and flash on the target's body [Observed: yKXifUx8lyY/maxres1]. No status effect [Fan-wiki].
- **Images viewed:** V/png/PlasmaMachineGun.png; V/crops/pmg_muzzle.png; V/crops/pmg_core.png; V/crops/sh_pmg_ps_gb.png; V/yt/yKXifUx8lyY/{maxresdefault,maxres1-3}.jpg (V/crops/sh_ykx.png); V/yt/B7FHI1aDgsw/{hqdefault,hq1-3}.jpg, V/yt/LSBL0QqCa_o/{hqdefault,hq1-3}.jpg, V/yt/4iVi02vnIPk/hq1.jpg (V/crops/sh_b7.png); V/yt/wRXMFQqYxRQ/sd*.jpg (V/crops/sh_wrx.png); V/yt/NcaNiWdT6dE/maxres1.jpg.
- **Depiction for shorts:** a rattling stream of thin magenta laser lines from the octagonal grey muzzle, with white puffs at its sides and small pink-white pops on the target [Observed]. Heat shimmer on the muzzle would be a [BBG News invention].
- **Confidence:** observed (low-res for the shot).

## Plasma Shotgun (primary, shotgun; BBG 2.9, May 8 2014; seen in a 2026 beta frame)
- **Official text:**
  - "New Saberi Weapons: / Plasma Shotgun: You know a great way to exfoliate your skin, white hot plasma! Caution may cause severe salt" [Canon: 2.9 notes, SkyVu Nick, May 8 2014, saved copy of https://web.archive.org/web/20140512024150/http://battlebears.com/battle-bears-gold-update-2-9-now-available/].
  - The wiki's in-game version adds asterisks: "*Caution may cause severe salt*" [Game text via wiki].
  - SkyVu's May 1 2014 post: "here’s a higher resolution version of the preview art for Saberi’s new weapons" [Canon: saved copy of the 2.9 sneak peek]. The art itself reads "SABERI WEAPONS!" and "2.9 COMING SOON!" [Observed: saberi29_copy.png].
- **Look:**
  - **2014 official art** [Observed: V/official/saberi29_copy.png; V/crops/saberi29_half.png]:
    - twin stacked silver barrels with violet-lit muzzles
    - an olive/khaki receiver with a row of round portholes (≈#5A4F4D)
    - a glowing magenta crystal ridge on top (≈#FB4DFE)
    - a silver rear housing around a swirling magenta core (≈#FF45FF)
    - held two-handed at hip height, roughly 0.6-0.7x her height long [length Inference]
  - **In-game wiki model** (caption "Saberi with the Plasma Shotgun", uploaded 2015-05-07) [Observed: V/png/Plasma_shotgun.png; V/crops/ps_model.png]:
    - two hexagonal dark-grey barrels (≈#777681) pointing at the viewer
    - a khaki receiver (≈#6D6759)
    - a magenta crystal strip on top (≈#E144EC, lit #F9A2FA)
    - a glowing magenta disc at the rear (≈#B56BBE, lit #FC8AFC)
  - The art and the model match [Observed]. SkyVu names only two new weapons in 2.9 [Canon], and the wiki captions the model as the Plasma Shotgun [Fan-wiki]. Calling the art's gun the Plasma Shotgun therefore rests on those two facts.
  - **In play:**
    - The HUD icon is a long grey gun with a magenta round end, with a small disc icon above it [Observed: V/yt/Bgvpayoqsg4/sddefault.jpg, May 11 2014; V/yt/s9W6eLXj9qc/maxres3.jpg, 2026].
    - From behind, the rear disc glows ≈#F67DFB [Observed: V/yt/Rn_X7MA23ho/maxresdefault.jpg].
    - In 2026 the held gun is grey with a segmented magenta-glowing strip (≈#EC68F9) [Observed: s9W6eLXj9qc/maxres3; V/crops/s9w_saberi.png].
- **Firing:**
  - 5 shells, 1 s rate of fire, 5 s reload, damage plus a "Radiation" value [Fan-wiki infobox].
  - Revision history [Fan-wiki]. The first revision (May 9 2014) titled the weapon "The Spreadshot" in its body text, probably a copy error [Inference].

    | Date | Damage | Radiation | Rate of fire |
    |---|---|---|---|
    | May 9 2014 | 35 | none listed | 1.6 s |
    | Sep 18 2014 | 40 | 40 | 1.2 s |
    | Apr 10 2020 | 30 | 45 | 1 s |
    | Nov 10 2020 | 25 | 25 | 1 s |

  - The HUD reads "/5" in May-Jun 2014 (Bgvpayoqsg4, Rn_X7MA23ho), 2016-2018 (0rQcyVwWSOs, Q46ZMPrChm4, _qdzLv19cWc) and 2026 (s9W6eLXj9qc, 3/5) [Observed].
  - Muzzle: a pink-purple sparkle cloud with a white core at the barrel [Observed: V/yt/Rn_X7MA23ho/maxres1.jpg, ammo 2/5].
  - The spread pattern is undocumented [Unverified].
- **Projectile:**
  - No individual pellets are visible in any frame I opened [Observed absence].
  - "white hot plasma" [Canon] suggests a white-pink plasma blast rather than pellets [Inference].
- **Impact / end result:**
  - A large soft pink-white sparkly burst on the wall or target (edge ≈#FAA0F9, core ≈#FEFCFF) [Observed: V/yt/Rn_X7MA23ho/maxres3.jpg].
  - The target gets the yellow Irradiated disc [Observed: Rn_X7MA23ho/maxres1 (2014); Q46ZMPrChm4/maxres1 (2.27, Oct 2017)]. The Status Effects page lists it among the "Items capable" of Irradiated [Fan-wiki].
  - A target that reaches 100 RP self-explodes [Fan-wiki].
  - A purple-pink-white sparkle burst with green glow surrounds a downed enemy while the Gamma Burst button is cyan [Observed: V/yt/0rQcyVwWSOs/maxres1.jpg, 2.23, Jan 16 2016]. Which weapon caused it is [Inference].
- **Images viewed:** V/official/saberi29_copy.png (V/crops/saberi29_half.png); V/png/Plasma_shotgun.png; V/crops/ps_model.png; V/yt/Rn_X7MA23ho/{maxresdefault,maxres1-3}.jpg (V/crops/sh_rn.png, rn_m1_icon.png, rn_m3_burst.png); V/yt/Q46ZMPrChm4/{maxresdefault,maxres1-3}.jpg (V/crops/sh_q46.png); V/yt/Bgvpayoqsg4/sd*.jpg (V/crops/sh_bg.png); V/yt/s9W6eLXj9qc/{maxresdefault,maxres1-3}.jpg (V/crops/sh_s9w.png, s9w_saberi.png); V/yt/0rQcyVwWSOs/{maxresdefault,maxres1-3}.jpg (V/crops/sh_0rq.png, 0rq_m1.png).
- **Depiction for shorts:** a chunky twin-barrel olive-and-silver gun with a glowing magenta crystal spine. Each shot is a pink sparkle cough at the muzzle, then a big pink-white sparkle splash on the target, and a yellow radiation disc starts ticking over the victim's head [Observed]. A cartoon "exfoliated" shine on the victim would be a [BBG News invention].
- **Confidence:** observed.

## Toxic Rifle (primary, poison automatic; BBG 2.15, Dec 20 2014 per the wiki; 2026 unconfirmed)
- **Official text:**
  - "Spray your enemy with toxins that deal poison damage overtime and can stack with each bullet!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Toxic_Rifle)
  - No SkyVu note was found; the archive was unreachable [Unverified].
  - Release: the wiki page says it was "released in the v2.15", and the Updates table lists 2.15 on December 20, 2014 [Fan-wiki]. The earliest fan footage is Jan 26 2015 (gvBdwTy5KEM) [Observed: metadata].
- **Look:**
  - **In-game model** (caption "Combat Tech with the Toxic Rifle", uploaded 2015-02-15) [Observed: V/png/Toxicrifle.png; V/crops/sh_tox_lm.png]:
    - a hot-pink/magenta gun body (≈#C651B0, lit #E49ACA) with a dark pyramid vent at the muzzle and small round vents on top
    - a segmented purple scorpion tail rising from the gun, holding an upturned white-capped bottle with a skull label and lilac liquid (≈#B973B6) beside her face
    - a white-capped bottle of bright pink liquid (≈#F887E2) hanging below the gun
    - Gun plus tail span about 0.5x her height [Inference].
  - **In play** it is a grey-and-pink gun with a capped bottle on top [Observed: V/yt/DyvVVZ_C8ME/maxres3.jpg; V/yt/gvBdwTy5KEM/sd*.jpg]. The HUD icon is the pink scorpion gun [Observed].
  - **Concept art** (uploaded 2015-02-20 by wiki user "Thecheeselover", caption "Concept Art for the Toxic Rifle"; author and official status [Unverified]) [Observed: V/crops/toxic_concept_900.png]:
    - a line drawing with a blade at the muzzle, three oval vents and a scorpion tail of oval segments holding a skull-and-crossbones bottle
    - two skull-labelled jars hanging under the barrel
    - plus a small colour thumbnail in hot pink with a bubbly texture, cyan outlines and pink-liquid jars
- **Firing:**
  - "The Toxic Rifle is an automatic rifle that inflicts poisoning on targets" [Fan-wiki].
  - Current: "3.0 per second for 2 seconds", 0.25 s, ammo 15, reload 5.5 s, "-10% Health" [Fan-wiki].
  - History [Fan-wiki revisions]:
    - Dec 2014 to Mar 2018: "4.0 per second for 3.0 seconds", 0.2 s, ammo 13, reload 4 s.
    - Apr 2020: 5.0/s for 3 s, 0.25 s, ammo 15.
  - Each extra hit stacks the poison [Game text via wiki; Fan-wiki].
  - The HUD reads "/17" in 2015 and 2017 [Observed: gvBdwTy5KEM 11/17, 0/17, 17/17; DyvVVZ_C8ME 17/17, 14/17]. That fits 13 base plus Ammo +1 (+4) [Inference from the wiki equipment table].
- **Projectile:** a hot-pink tracer streak (≈#F58EF4, bright #FDABF7) [Observed: V/yt/DyvVVZ_C8ME/maxres3.jpg, Aug 24 2017; V/crops/dyv_m3.png].
- **Impact / end result:**
  - A white-pink flash at the hit point [Observed: dyv_m3.png].
  - A poisoned target (a panda-faced bear) is wrapped in a pink glow, with crackling pink tendrils reaching it and a dark-purple skull icon (≈#410C3A) above its head [Observed: V/yt/JO5-kfnENtM/maxresdefault.jpg, Feb 20 2016; V/crops/jo5_md.png, jo5_skull.png].
  - That loadout also had the Minigun, so the crackling tendrils may be the Minigun's [Inference]. The skull fits the Toxic Rifle's poison [Inference].
  - Damage over time, with no knockback documented [Fan-wiki].
- **Images viewed:** V/png/Toxicrifle.png; V/png/Toxic_Rifle_concept_art.png (V/crops/toxic_concept_900.png); V/png/x_Battlebears_Gold_toxic_rifle_gameplay.png (V/crops/sh_extra.png); V/yt/gvBdwTy5KEM/sd*.jpg (V/crops/sh_gvb.png); V/yt/DyvVVZ_C8ME/{hqdefault,maxres1-3}.jpg (V/crops/sh_dyv.png, dyv_m3.png); V/yt/JO5-kfnENtM/{maxresdefault,maxres1-3}.jpg (V/crops/sh_jo5.png, jo5_md.png, jo5_skull.png).
- **Depiction for shorts:** a candy-pink scorpion-tailed rifle with skull bottles spits hot-pink tracer darts. Victims glow pink with a little dark-purple skull bobbing over their head [Observed]. Making the skull grow a notch with each stacked hit is a [BBG News invention].
- **Confidence:** observed (look); partial (shot and impact attribution).

## Social Butterfly (BBG) (primary, "Saboteur"; BBG 2.53, Apr 28 2018 per the wiki; 2026 unconfirmed)
- **Official text:** none found. The wiki stub has no item description, and no SkyVu note was found [Unverified].
- **Look:**
  - It is a **crossbow** [Observed]. In hand [Observed: V/yt/5Wsfn8XwT0g/maxres1.jpg, Jul 20 2021; V/crops/5ws_m1_xbow.png]:
    - a purple-and-gunmetal stock (bright ≈#A30DA4) with dark grey rails and swept grey bow limbs
    - orange butterflies (≈#A0401F) perched on the white bolt tips
    - a third small orange butterfly on a white shaft just ahead of the bow; reading it as a bolt in flight is [Inference]
  - Head-on (2018): two stacked pairs of grey recurve limbs with a purple centre, orange butterflies on top and a white bolt down the middle [Observed: V/yt/Wre1oS8Lfkw/maxresdefault.jpg, Apr 30 2018; V/crops/wre_xbow.png].
  - HUD icon (2021) and fan-thumbnail render (2018): a purple-and-grey crossbow whose round body is ringed by pale spikes, with a blue orb [Observed: V/yt/ua2j5t23T80/maxres1.jpg; V/yt/dgOyOegG6-E/maxresdefault.jpg; V/crops/dgo_render.png].
  - The limbs are about shoulder-wide, roughly 0.4x her height [Inference].
  - Do not confuse it with the Battle Bears Overclock weapon for Astoria, which "fires butterflies at a slow pace which deal a lot of damage" [Fan-wiki: Social Butterfly].
- **Firing:**
  - Typed "Primary - Saboteur" [Fan-wiki]. The only other wiki weapons typed Saboteur are Sake Bomb, Sucker Punch and Phantom Hug, all "Secondary - Saboteur" [Fan-wiki]. Their Status Effects entries are controls reversed, stunned and slowed/"immobile" [Fan-wiki: Status Effects].
  - Current: damage 0, rate of fire 2 s, ammo 5, reload 5.0 s, gravity 1000 units, projectile speed 1000 u/s, duration 0.5 s [Fan-wiki].
  - Apr 10 2020 stub: duration 1 s, ammo 3, rate of fire 2 s, reload 4.0 s, gravity 750, speed 1250, damage 15 [Fan-wiki].
  - The HUD reads "2 / 3" and "3 / 3" in Apr 2018 (dgOyOegG6-E), then "5 / 5", "4 / 5", "1 / 5" and "0 / 5" in Jul 2021 (ua2j5t23T80, 5Wsfn8XwT0g) [Observed].
- **Projectile:** butterfly-tipped bolts [Observed, loaded bolts]. The gravity value implies an arcing lob [Inference].
- **Impact / end result:** undocumented [Unverified]. A 0.5 s non-damaging effect is implied by the stats and the "Saboteur" type; which effect it is remains [Unverified].
- **Images viewed:** V/yt/5Wsfn8XwT0g/{hqdefault,maxres1-3}.jpg (V/crops/sh_5ws.png, 5ws_m1_xbow.png); V/yt/ua2j5t23T80/{maxresdefault,maxres1-3}.jpg (V/crops/sh_ua2.png); V/yt/dgOyOegG6-E/{maxresdefault,maxres1-3}.jpg (V/crops/sh_dgo.png, dgo_render.png); V/yt/Wre1oS8Lfkw/{maxresdefault,maxres1-3}.jpg (V/crops/sh_wre.png, wre_xbow.png).
- **Depiction for shorts:** Saberi shoulders a purple, spike-ringed crossbow and lobs a bolt with an orange butterfly riding the tip [Observed]. What happens on hit (a dizzy flutter of butterflies, or a target compelled to wave hello) is a [BBG News invention]. Keep it damage-free, as the stats say [Fan-wiki].
- **Confidence:** partial.

## Missiles (secondary, default; BBG 2.4; timed third-arm weapon; 2026 unconfirmed)
- **Official text:**
  - "2 Secondary Weapons (Missiles, Minigun)" [Canon: 2.4 notes].
  - "Because she couldn't quite figure out where to attach his missiles to her rifle, Saberi decided to create herself a third arm and put them there." [Game text via wiki] (sic, "his") (https://battlebears.fandom.com/wiki/Missiles)
- **Look:**
  - From the side: two missiles **stacked one above the other**, pointing forward at face-to-shoulder height on the third arm [Observed: V/png/SideMissiles.png].
  - Each missile has [Observed: V/png/SideMissiles.png]:
    - a pale grey-green body (≈#787261, lit #D1CABC) with a thin green stripe (≈#7A8861)
    - a black cone nose (≈#212025)
    - dark tail fins (≈#28272A)
    - Each is about 0.5x her height long [Inference].
  - Head-on: two dark hexagonal ends stacked on a grey bracket, out to her right beside her head [Observed: V/png/Missiles.png; V/png/SaberiSkin.png]. Since the missiles face forward, these are most likely the black nose cones seen end-on [Inference].
  - HUD icon: two missiles, one above the other. The Oct 1 2013 beta store reads "MISSILES EQUIPPED", and the store model stands with crossed arms while the arm holds the pod [Observed: V/yt/66csovuHEAk/maxres3.jpg; V/crops/sh_66c.png].
- **Firing:**
  - "Upon activating the secondary, a pair of missile launchers slowly emerge from the right side of the Combat Tech's backpack." [Fan-wiki]
  - Then "the missile launchers will release two explosive missiles, with short cooldowns in between, as long as the shoot button/ double tap is tapped". They keep firing "even if the primary is reloading" [Fan-wiki].
  - Current: explosives 35-50, AoE "Max Dmg 100, Min Dmg 250.0" (the body text reads these as radii), cooldown 0.8 s, ammo 10, duration 10 s, projectile speed 1,500 u/s, reload 30 s [Fan-wiki].
  - History [Fan-wiki revisions]. The wiki itself calls the duration "disputed".

    | Date | Explosives | Rate of fire | Duration | Recharge |
    |---|---|---|---|---|
    | Oct 29 2013 | 35-80 | 2.6 s | "8 seconds (?)" | 15 s |
    | Apr 12-13 2014 | 20-30 | 0.8 s | 8 s | 15 s |
    | Apr 10 2020 | 12.5-25 | (cooldown n/a) | 8 s | 15 s |
    | Nov 10 2020 | 35-50 | 0.8 s cooldown | 10 s | 30 s |

- **Projectile:**
  - With the Missiles button cyan (deployed), a yellow-white launch flash sits at her lower right, and a thin straight pale line runs to a white puff at the target. Blue square brackets frame the target [Observed: V/yt/8F69eJnbIg8/sddefault.jpg and sd2.jpg, Dec 1 2013; V/crops/8f6_sd.png]. Reading the line as a missile trail is [Inference]. What the brackets mean is [Unverified].
  - A dotted line of white puffs along the floor toward a target [Observed: V/yt/wAQLCQDHUZk/maxres1.jpg, Nov 2 2013]. In that frame the Missiles button is already recharging (red-green), so a lingering trail is only an [Inference].
- **Impact / end result:**
  - **Candidate blast:** a translucent faceted starburst of long yellow (≈#CCD928, lit #DBF242) and lime-green (≈#65EE49) spikes with red streaks, at the enemy's position. In the same frame the Missiles button is cyan, the primary reads 0 and "RELOAD", and the kill feed shows "KILLS … STREAK +130" [Observed: V/yt/wAQLCQDHUZk/maxres3.jpg, Nov 2 2013; V/crops/waq_m3_star.png, waq_m3_tr.png]. Attributing it to the Missiles is [Inference]; the wiki says they fire while the primary reloads.
  - Splash damage falls off between the 100 and 250 unit radii [Fan-wiki].
  - A Nov 2013 kill with the Missiles deployed shows the victim breaking into brown toy-like chunks [Observed: NcaNiWdT6dE/hqdefault; attribution Inference]. This is consistent with the combat-VFX dossier's explosive "gib" convention.
- **Images viewed:** V/png/SideMissiles.png; V/png/Missiles.png; V/png/SaberiSkin.png (V/crops/sh_mis_front.png); V/yt/66csovuHEAk/{maxresdefault,maxres1-3}.jpg (V/crops/sh_66c.png); V/yt/8F69eJnbIg8/sd*.jpg (V/crops/sh_8f6.png, 8f6_sd.png); V/yt/wAQLCQDHUZk/{maxresdefault,maxres1-3}.jpg (V/crops/sh_waq.png, waq_m3_star.png, waq_m3_tr.png, waq_m3_full.png); V/crops/nca_target.png.
- **Depiction for shorts:** the arm swings a stacked twin-missile pod up beside her head, and each tap fires a pair with a yellow-white flash and thin pale trails [Observed, attribution Inference]. They burst into a translucent yellow-and-lime faceted starburst [Observed candidate]. Toy-chunk KOs and spark confetti are [BBG News invention, styled on the shared BBG explosion].
- **Confidence:** partial.

## Minigun (Combat Tech) (secondary; BBG 2.4; timed third-arm weapon; 2026 unconfirmed)
- **Official text:**
  - Named in the 2.4 notes [Canon].
  - "She already had built herself a third arm to hold more firepower. Why not add a minigun to it for good measure?" [Game text via wiki] (https://battlebears.fandom.com/wiki/Minigun_(Combat_Tech))
- **Look:**
  - On the arm beside her head sits a boxy weathered grey-khaki housing (≈#626152, lit #787C6D). Two blocky end plates surround a glowing magenta barrel cylinder with dark bands (≈#63015B shade to #B504A8 lit). It is about 0.35x her height long [Observed: V/png/SideMinigun.png; size Inference].
  - Head-on: an octagonal grey ring around a big magenta glow (≈#BE00AF, lit #DB00C9), out to her right at head height [Observed: V/png/Minigun.png; V/png/Gold_Saberi.png].
  - HUD icon: a grey box with magenta bands [Observed: V/yt/B7FHI1aDgsw/hq1.jpg; V/yt/yKXifUx8lyY/maxres1.jpg].
- **Firing:**
  - "it deploys for 10 seconds once the player taps the 'secondary' button". "During this duration, the player can use the shoot button to continuously fire low-damage beams in addition to their primary". "After the 10 seconds end, the player must wait an additional 30 seconds" [Fan-wiki].
  - Current: damage 10, cooldown 0.1666666667 s, ammo 60 [Fan-wiki].
  - History [Fan-wiki revisions]:
    - Oct 29 2013: damage 5.0, 10 s on, 16 s recharge.
    - Jan 2014: recharge 10 s.
    - Apr 13 2014: damage 6, 0.2 s, ammo 40, 8 s on.
    - Sep 2014: damage 7.
    - Apr 2020: damage 3.5.
    - Nov 2020: damage 10, 10 s on, 30 s recharge.
  - Price conflict: the infobox says 60 Gas, but the body says "It costs 80 Gas", and every revision before Nov 2020 had 80 Gas [Fan-wiki].
  - The Oct 1 2013 beta store showed "MINIGUN / BUY NOW!" with a Joules bolt and "1". Taunts and skins in the same store also cost "1" [Observed: V/yt/66csovuHEAk/maxres2.jpg, maxres3.jpg]. The uploader's description says "IGNORE THE PRICES, THIS IS BETA" [Observed: YouTube metadata V/yt/next_66csovuHEAk.json]. So "1" is a placeholder.
- **Projectile:**
  - **2013:** thick magenta-white crackling, jagged beams stream from Saberi to the target while the Minigun button is cyan [Observed: V/yt/B7FHI1aDgsw/hq1.jpg, Oct 28 2013; V/crops/b7_hq1.png; V/yt/LSBL0QqCa_o/hq3.jpg, Oct 28 2013].
  - **2016:** a pale cyan crackling bolt (≈#5FC6E5) reaches the target while the Minigun button is cyan [Observed: V/yt/JO5-kfnENtM/maxres2.jpg, Feb 20 2016; V/crops/jo5_m2_tgt2.png]. Whether this was a patch change or a team tint is [Unverified].
- **Impact / end result:** a white-cyan spark burst with a pink streak on the target [Observed: JO5-kfnENtM/maxres2; attribution Inference]. No status effect [Fan-wiki].
- **Images viewed:** V/png/SideMinigun.png; V/png/Minigun.png; V/png/Gold_Saberi.png (V/crops/sh_mg.png); V/yt/B7FHI1aDgsw/{hqdefault,hq1-3}.jpg; V/yt/LSBL0QqCa_o/{hqdefault,hq1-3}.jpg (V/crops/sh_b7.png, b7_hq1.png, b7_hq3.png); V/yt/66csovuHEAk/maxres2.jpg, maxres3.jpg; V/yt/JO5-kfnENtM/maxres2.jpg (V/crops/jo5_m2_tgt2.png).
- **Depiction for shorts:** the arm pops a boxy grey gun with a glowing magenta core beside her head. It hoses crackling magenta-white beams alongside her rifle and peppers the target with white sparks [Observed]. A spin-up whine is a [BBG News invention].
- **Confidence:** observed (look); partial (shot).

## Landmine (secondary, explosives; BBG 2.19, Apr 26 2015 per the wiki; 2026 unconfirmed)
- **Official text:**
  - "Toss explosive packages everywhere, just like the mailman!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Landmine)
  - The wiki Updates table lists "Combat Tech's Land Mine" under 2.19, April 26, 2015 [Fan-wiki]. The earliest fan footage is May 2 2015 [Observed: metadata].
  - The in-game spelling ("Landmine" or "Land Mine") is [Unverified].
- **Look:**
  - Held by a tan claw on the arm, out to her right at head height [Observed: V/png/Landmine.png, uploaded 2015-04-29]:
    - a grey cylindrical canister with glowing cyan circuit lines and dots (≈#529396, bright #34C9D0)
    - a glossy dark purple-black lid
    - a pale tan box with black diagonal stripes on top. Reading the box as the "package" is [Inference].
  - It is about 0.3x her height wide [Inference].
  - The skin in that screenshot has a white face mask and brown body paint with white spirals. That it is "Voodoo" is [Inference].
  - HUD/secondary button icon: the canister with its dark lid and beige top [Observed: V/yt/ua2j5t23T80/maxres1.jpg; V/png/x_Battle_Bears_Gold_Land_Mine-------to_suicide___.png].
- **Firing:**
  - "while the secondary is activated it's able to fire up to two mines". "Once one of the mines is fired, it will fly on a straight direction and will arc over long distances. If the projectile hits an enemy before it reaches the ground, it will explode on contact." [Fan-wiki]
  - Landed mines "after they prime … will explode whenever an enemy gets close enough". Otherwise they "explode in about 30 seconds automatically" (10 s in the 2015 revision) [Fan-wiki].
  - "whenever a mine explodes, the primary weapon will reload" [Fan-wiki; Unverified].
  - The secondary button shows the same cyan (active) and red-green (recharging) rings as her timed secondaries [Observed: ua2j5t23T80/maxres1 cyan, maxresdefault red-green].
  - Current: explosives 30-80, trigger radius 100, priming 2.25 s, AoE "Max Dmg 100.0, Min Dmg 300.0", rate of fire 1.25 s, ammo 3, reload 6 s, +10% speed, 100,000 Joules, level 15 lock [Fan-wiki].
  - History [Fan-wiki revisions]:
    - Apr 2015: explosives 30-50, priming 5 s, AoE 90/300, rate of fire 3 s, ammo 2, reload 5 s, +5% speed.
    - Jan 2019: 30-80, AoE 100/300, rate of fire 1 s.
    - Nov 2020: priming 2.25 s, 1.25 s, ammo 3, reload 6 s, +10% speed.
- **Projectile:** the thrown mine's in-flight look is undocumented [Unverified]. Presumably it is the canister-and-box seen on the arm [Inference].
- **Impact / end result:**
  - No explosion frame could be attributed [Unverified].
  - The wiki-embedded "Land Mine to suicide" video thumbnail (May 2 2015) has a large glossy magenta-pink sphere filling the right edge of the frame. What it is remains [Unverified] [Observed: V/png/x_Battle_Bears_Gold_Land_Mine-------to_suicide___.png; V/yt/YpYjwP0rQjM/sd*.jpg].
  - The title implies self-kills are possible [Inference].
- **Images viewed:** V/png/Landmine.png (V/crops/sh_tox_lm.png); V/png/x_Battle_Bears_Gold_Land_Mine-------to_suicide___.png (V/crops/sh_extra.png); V/yt/YpYjwP0rQjM/{sddefault,sd1-3}.jpg (V/crops/sh_lm.png); V/yt/ua2j5t23T80/{maxresdefault,maxres1-3}.jpg (V/crops/sh_ua2.png).
- **Depiction for shorts:** the arm lobs a cyan-circuited canister "parcel" that thunks down, primes, and pops when someone steps near [behaviour from Fan-wiki]. The blink, and a yellow-orange faceted pop with cardboard confetti, are [BBG News invention].
- **Confidence:** partial.

## Gamma Burst (secondary, radiation explosives; BBG 2.9, May 8 2014; seen in a 2026 beta frame)
- **Official text:**
  - "Gamma Burst: Saberi Smash! Creates a deadly radiation area around the player." [Canon: 2.9 notes, saved copy]
  - The disc appears in SkyVu's "preview art for Saberi’s new weapons" [Canon; Observed: saberi29_copy.png].
- **Look:**
  - **2014 art:** a flat saucer on the khaki jointed arm above her head. A grey riveted metal cap with holes and claw brackets sits over a fat glowing magenta rim (≈#F643FE, white-hot highlights) [Observed: V/official/saberi29_copy.png].
  - **In-game wiki model** (caption "Combat Tech with the Gamma Burst", uploaded 2015-02-15): the same saucer out to her right at head height. The cap is ≈#5F5A68 and the rim ≈#C725DB-#F9A1FE [Observed: V/png/Gammaburst.png; V/crops/gb_model.png].
  - **In play (May 11 2014):** a saucer of grey metal segments over a glowing magenta band, carried low beside her [Observed: V/yt/Bgvpayoqsg4/sddefault.jpg].
  - **2026:** the same saucer, carried low at her right, with a grey-green cap (≈#6A8C62) and a magenta rim (≈#D892DA-#F1A9F2) [Observed: V/yt/s9W6eLXj9qc/maxres3.jpg; V/crops/s9w_saberi.png].
  - It is about 0.25-0.3x her height across [Inference].
  - HUD icon: a grey disc with a magenta ring [Observed: V/yt/0rQcyVwWSOs/maxres1.jpg; s9W6eLXj9qc/maxres3].
- **Firing:**
  - "Upon activating the secondary, a purple disk-like structure will emerge from the Combat Tech's backpack." [Fan-wiki]
  - "After the short activation sequence, the gamma burst will create a yellow dome-like structure around the user, and any enemy inside it will receive damage while also being irradiated. This effect can be used 8 times during the 10 second duration of the ability, and is meant for close combat only." [Fan-wiki]
  - History [Fan-wiki revisions]:
    - **Launch (May 9 2014):** 10-15 damage (25-35 radiation), AoE 200/400, 8 s, 5 uses, reload 15 s, 5% speed boost. The first revision's infobox said 50 Gas while the body said 300,000 Joules; the infobox was changed to 300,000 Joules the same day.
    - **Sep 2014:** 6 s duration.
    - **Apr 2020:** AoE 150/300.
    - **Nov 2020:** 30-40 (30-45 radiation), 10 s, 8 uses, reload 30 s, 150,000 Joules.
- **Projectile:** none; it is a burst centred on Saberi [Fan-wiki].
- **Impact / end result:**
  - **2026:** a huge bright yellow-white glow fills the space around and ahead of Saberi (lit ground ≈#FFFF8B, white at the top). A nearby target carries the yellow Irradiated disc [Observed: V/yt/s9W6eLXj9qc/maxres3.jpg; V/crops/s9w_target.png]. This fits the wiki's "yellow dome-like structure" [Fan-wiki], but the dome's edge is not visible in this low-res frame.
  - **Feb 10 2018 (2.29):** with the saucer out, lime-green glowing crescent curls and purple-white wisps engulf an enemy [Observed: V/yt/_qdzLv19cWc/maxres2.jpg; attribution Inference].
  - **Jan 16 2016 (2.23):** a purple-pink-white sparkle burst with green glow around a downed enemy while the Gamma Burst button is cyan [Observed: V/yt/0rQcyVwWSOs/maxres1.jpg; V/crops/0rq_m1.png].
  - Irradiated targets that reach 100 RP self-explode [Fan-wiki: Status Effects]. The radiation-blast look (a yellow faceted blast with toy-chunk gibs) is in the combat-VFX dossier; it was not observed for this weapon.
  - Wiki trivia: "This deals both explosive and radiation damage." [Fan-wiki]
- **Images viewed:** V/official/saberi29_copy.png; V/png/Gammaburst.png (V/crops/gb_model.png, sh_pmg_ps_gb.png); V/yt/Bgvpayoqsg4/sd*.jpg; V/yt/s9W6eLXj9qc/maxres3.jpg (V/crops/s9w_saberi.png, s9w_target.png, s9w_stamp2.png); V/yt/_qdzLv19cWc/{maxresdefault,maxres1-3}.jpg (V/crops/sh_qdz.png); V/yt/0rQcyVwWSOs/maxres1.jpg (V/crops/0rq_m1.png).
- **Depiction for shorts:** "Saberi Smash!" The arm brings the glowing magenta saucer round. A bright translucent yellow dome flashes out around her, and every enemy inside gets a yellow radiation disc ticking over its head [Observed/Fan-wiki]. A victim who fills up pops into clean toy chunks and sparks [BBG News invention, styled on the shared radiation blast]. The lime-green curls are an era-specific alternative [Observed, 2018].
- **Confidence:** observed (the 2026 glow is low-res).

## Mallet (melee, default; BBG 2.4; 2026 unconfirmed)
- **Official text:**
  - "2 Melee Weapons (Mallet, Sledgehammer)" [Canon: 2.4 notes].
  - "Sometimes in order to solve a problem you just need to hit it with a hammer." [Game text via wiki]
- **Look:**
  - A big wooden mallet: a light-brown log head (≈#B07632, lit #B88745) with visible end-grain rings, on a yellow collar. It has a dark grey ribbed grip and a tan/yellow end cap.
  - She holds it one-handed, diagonally across her chest. The head is about 0.26x her height and the whole tool about 0.47x [Observed: V/png/Mallet.png; sizes Inference].
- **Firing:**
  - A melee swing. Damage 45 (Oct 2013), 35 (Dec 2019), 70 (Nov 2020) [Fan-wiki revisions]. "does not have any Stat Modifiers" [Fan-wiki].
  - Swing barks: "Slam!" and "Smmmash!" [Fan-wiki transcription].
- **Projectile:** none.
- **Impact / end result:**
  - Yellow 5-point stars scatter around a target hit at close range [Observed: V/yt/n84q9Ptu13c/maxres3.jpg; V/yt/0rQcyVwWSOs/maxres3.jpg; which melee is Inference].
  - Melee-kill barks include "Hammers fix anything!" and "Imma pound some sense into you!" [Fan-wiki].
- **Images viewed:** V/png/Mallet.png (V/crops/sh_melee.png); V/crops/sh_n84.png; V/crops/n84_m3.png; V/crops/sh_0rq.png.
- **Depiction for shorts:** a cartoon log-mallet bonk with a burst of yellow stars [Observed]. A comic "thonk" and a wobbling victim are [BBG News invention].
- **Confidence:** observed (look); partial (hit).

## Sledgehammer (melee; BBG 2.4; rebalanced in 2.6, Dec 20 2013; 2026 unconfirmed)
- **Official text:**
  - "Saberi Changes: / Sledge Hammer / Damage increased from 45 to 50 / Speed modifier increased from -5% to 10%" [Canon: "BATTLE BEARS GOLD Update 2.6 Change Log", saved copy of https://web.archive.org/web/20151029082644/http://battlebears.com/battle-bears-gold-2-6-change-log/; not re-fetchable today]. The wiki dates 2.6 to December 20, 2013 and links that change log [Fan-wiki: Updates].
  - "Sometimes a bigger hammer is necessary for bigger problems." [Game text via wiki]
- **Look:** a blocky dark steel-grey head (≈#3A3D43) with a cross-head (Phillips) screw on its side, a pink collar (lit ≈#B35E8D) and a dark wrapped handle. The head is about 0.26x her height and the whole tool about 0.48x [Observed: V/png/Sledgehammer.png; sizes Inference].
- **Firing:**
  - Melee: 50 damage, +10% speed [Canon 2.6; Fan-wiki].
  - The wiki's Oct-Dec 2013 revisions said 60 damage, which contradicts SkyVu's "from 45" [Fan-wiki error].
  - Wiki trivia: "Prior to v2.6, the Sledgehammer had a 5% Speed Reduction." The damage meter shows only "for the Windows version of BBG" [Fan-wiki].
- **Projectile:** none.
- **Impact / end result:** undocumented for this weapon specifically. Use the shared yellow melee stars [Inference].
- **Images viewed:** V/png/Sledgehammer.png (V/crops/sh_melee.png).
- **Depiction for shorts:** an overhead swing of the screw-headed steel hammer with a star burst on contact [stars Inference]. A "bigger problem" escalation gag is a [BBG News invention].
- **Confidence:** observed (look).

## ClubCobra (melee; BBG 2.20, May 29 2015 per the wiki; 2026 unconfirmed)
- **Official text:** "A powerful melee made of jade and gold." [Game text via wiki] (https://battlebears.fandom.com/wiki/ClubCobra)
- **Look:**
  - An angular golden club shaped like a rearing cobra head with open jaws and a purple-and-green eye. It has engraved gold (≈#AE810D, lit #E9C237), a dark brown wrapped grip and a gold crescent pommel. It is about 0.6x her height [Observed: V/png/Clubcobra.png, uploaded 2015-06-17; size Inference].
  - There is no green jade surface apart from the eye [Observed].
- **Firing:**
  - Melee. 150,000 Joules, level 10 lock [Fan-wiki].
  - The May 29 2015 revision gave 75 damage, "-5% Speed Modifier" and "+10% Health Modifier". The Nov 10 2020 revision gives 50 damage and "+15% Health Modifier" [Fan-wiki revisions].
  - The in-game shop screenshot reads "HEALTH +10%", with a Joules bolt and a price starting "1" [Observed: V/png/Clubcobra.png]. This matches the 2015 wiki values, so +10% vs +15% is a dated change, not a contradiction [Inference].
- **Projectile:** none.
- **Impact / end result:** undocumented [Unverified].
- **Images viewed:** V/png/Clubcobra.png (V/crops/sh_melee.png).
- **Depiction for shorts:** Saberi swings the gold cobra club and its jaws seem to snap at the hit, with gold sparkle stars. The jaw-snap and gold stars are [BBG News invention].
- **Confidence:** observed (look).

## Huggable Splicer (BBH main attack; Battle Bears Heroes, not BBG)
- **Official text:** "Saberi's "Huggable Splicer" attack unleashes a wide spray of huggable bits in a sweeping motion, ideal for hitting multiple enemies despite its inaccuracy. She's less effective in singular, long-range confrontations." [Canon: battlebears.com/pages/characters, re-fetched live 2026-10-17, saved at V/official/characters.html]
- **Look:** no weapon image found [Unverified]. Her BBH portrait shows blonde bangs, a white knotted bandana, a wink, a navy suit with grey straps and a red backpack [Observed: V/png/BBH_Profile_Saberi.png].
- **Firing:** a wide, inaccurate, sweeping spray [Canon]. The wiki gives damage "15 x 190", range Normal, reload "Very slow", 600 Shards and release "Summer 2023" [Fan-wiki: Battle Bears Heroes table].
- **Projectile:** "huggable bits" [Canon]. Their look is undocumented [Unverified].
- **Impact / end result:** undocumented [Unverified].
- **Images viewed:** V/png/BBH_Profile_Saberi.png (V/crops/sh_misc.png).
- **Depiction for shorts:** BBH only. A fan of plush scraps and rainbow fluff is a [BBG News invention]. Never mix it into a BBG-era short.
- **Confidence:** documented.

## Healing Turret (BBH Ultimate; not BBG)
- **Official text:** "Her Ultimate, "Healing Turret," provides a healing radius for her and her teammates, excluding non-player units." [Canon: same live page]
- **Look:** no image found [Unverified]. The wiki lists an "HP of HealBox" of 3360, implying a destructible box [Fan-wiki; Inference].
- **Firing:** a deployable heal zone [Canon]. Healing 468 per second, range "Very long" [Fan-wiki].
- **Projectile:** none.
- **Impact / end result:** heals her and teammates inside the radius, "excluding non-player units" [Canon].
- **Images viewed:** none exist that I could find.
- **Depiction for shorts:** BBH only. A small medkit box with a green pulse ring is a [BBG News invention].
- **Confidence:** documented.

## Corrections for the character file
File: /home/user/thallo-site/bbg-news-repo/characters/saberi.md. Every "Current" string below was checked against the file today.

1. **Line 57, Weapons/props.**
   - **Current:** "- **Weapons/props:** Energy Rifle, Plasma Machine Gun, Missiles, Minigun, Mallet, Sledgehammer; later Plasma Shotgun and Gamma Burst [Canon] ([2.4 notes][n24]; [2.9 notes][n29]), probably the 2014 art's purple-core double-barrel gun and glowing disc [Inference]. BBH: Huggable Splicer, Healing Turret [Canon] ([characters][chars])."
   - **Correction:** "Launch kit (2.4): Energy Rifle, Plasma Machine Gun, Missiles, Minigun, Mallet, Sledgehammer [Canon]. Plasma Shotgun and Gamma Burst in 2.9 [Canon]; SkyVu calls the 2014 art 'the preview art for Saberi’s new weapons' [Canon], and its twin-barrel magenta-crystal gun and magenta-rimmed saucer match the in-game models the wiki captions as the Plasma Shotgun and Gamma Burst [Observed; Fan-wiki]. Later: Toxic Rifle (2.15), Landmine (2.19), ClubCobra (2.20), Social Butterfly (2.53) [Fan-wiki]; the Social Butterfly is a crossbow with butterfly-tipped bolts [Observed, fan footage]. BBH: Huggable Splicer, Healing Turret [Canon]."
   - **Evidence:** the saved sneak-peek copy W/dl/saberi/official/prior/u29peek.html.txt; saberi29_copy.png against V/png/Plasma_shotgun.png and V/png/Gammaburst.png; the wiki Updates table; V/crops/5ws_m1_xbow.png.
2. **Line 55, colours.**
   - **Current:** "tech glow #9B4DFF, arm metal #7A7F86"
   - **Correction:** "tech glow magenta ≈#C000B0–#FC00FE in game (PMG core #FC00FE, Plasma Shotgun crystal ≈#E144EC), ≈#F643FE–#FF45FF in the 2014 art; third arm: thin khaki-grey rods ≈#5A5447 (lit #736C5C) with rounded tan/brass joint caps ≈#6A5C39 (lit ≈#807152) [Observed, sampled]"
   - **Evidence:** pixel samples of V/png/PlasmaMachineGun.png, Plasma_shotgun.png, SideMinigun.png, SideMissiles.png and V/official/saberi29_copy.png.
3. **Line 82, prompt pack (character reference).**
   - **Current:** "One mechanical third arm (#7A7F86) rises from a backpack, holding a purple-glowing disc (#9B4DFF); she holds a chunky double-barrelled gun with a glowing purple core and has a short mallet at her side."
   - **Correction:** "One thin jointed khaki-grey mechanical arm with tan joint caps rises from behind her, holding above her head a flat grey riveted saucer with a glowing magenta rim (#F643FE); she holds a twin-barrelled olive-and-silver plasma shotgun with a glowing magenta crystal ridge and a magenta core in a silver rear housing, and has a wooden log-headed mallet with a dark ribbed grip at her side."
   - **Evidence:** saberi29_copy.png (SkyVu 2014 art); V/png/Mallet.png.
4. **Line 83, video prompt starter.**
   - **Current:** "fires a burst of cartoon missiles"
   - **Correction:** "swings a twin missile pod (two pale grey-green missiles stacked one above the other, each with a thin green stripe, black nose cone and dark fins) up beside her head and fires them in pairs with a yellow-white flash"
   - **Evidence:** V/png/SideMissiles.png and V/png/Missiles.png (stacked pod); wiki Missiles page ("release two explosive missiles"); V/yt/8F69eJnbIg8/sddefault.jpg (flash while the Missiles button is active).
5. **Line 64, backpack timing.**
   - **Current:** "the backpack weapon runs 10 s, reloads 30 s"
   - **Correction:** "the backpack secondaries Missiles, Minigun and Gamma Burst run 10 s and recharge 30 s by the wiki's Nov 2020 stats; earlier wiki values were Missiles 8 s/15 s, Minigun 8 s/10 s (from Apr 2014) and Gamma Burst 8 s/15 s at launch, then 6 s; the Landmine also deploys from the same button but is listed with ammo (3), a 1.25 s rate of fire and a 6 s reload instead of a duration [Fan-wiki]"
   - **Evidence:** wiki revision histories (V/revs/Missiles.json, Minigun__Combat_Tech_.json, Gamma_Burst.json, Landmine.json); Landmine button rings in V/yt/ua2j5t23T80/maxres1.jpg and maxresdefault.jpg.
6. **Line 53, 2026 model.**
   - **Current:** "Her 2026 model is unconfirmed; neither the 2013 BBG trailer nor the 2026 Steam trailer shows a splash card for her, and whether one exists elsewhere is unknown [Observed]."
   - **Correction:** "A 2026 final-beta fan thumbnail shows her from behind with dark-brown fur, the red white-dotted bandana and red top, wielding the Plasma Shotgun with the Gamma Burst saucer out [Observed, low-res fan thumbnail]. The 2026 Steam trailer has class cards for B-1000, Graham, Astoria, Wil, Tillman, the Huggable, Riggs and Oliver but none for her, and she is not identifiable in its gameplay [Observed]."
   - **Evidence:** V/yt/s9W6eLXj9qc/maxres3.jpg (M1kaa717, Oct 16 2026); W/visuals/trailer/t_0001-t_0108 (V/crops/trailer_sheet_0..3.png).
7. **Line 54, backpack-mount citation.**
   - **Current:** "backpack-mounted per the wiki [Fan-wiki] ([Missiles][missiles]; [Minigun][minigun])"
   - **Correction:** "backpack-mounted per the wiki [Fan-wiki] ([Missiles][missiles]; [Gamma Burst](https://battlebears.fandom.com/wiki/Gamma_Burst)); the wiki's in-game screenshots show the arm reaching out from behind her back to hold each secondary beside her head [Observed]"
   - **Evidence:** the Minigun (Combat Tech) page never mentions the backpack. The Missiles page ("emerge from the right side of the Combat Tech's backpack") and the Gamma Burst page ("emerge from the Combat Tech's backpack") do. Images: V/png/SideMissiles.png, SideMinigun.png.
8. **Line 98, ledger.**
   - **Current:** "- Gun and disc names, Undead as the banner bear, BBH hex values [Inference]."
   - **Correction:** "- Undead as the banner bear, BBH hex values [Inference]. The 2014 art is SkyVu's 'preview art for Saberi’s new weapons' [Canon]; gun = Plasma Shotgun and disc = Gamma Burst via matching wiki-captioned in-game models [Observed; Fan-wiki]."
   - **Evidence:** as item 1.
9. **Line 105, open question.**
   - **Current:** "- Does 2026 keep the Combat Tech kit and polka-dot look? The October demo and [playtest showcase][showcase] are unviewed."
   - **Correction:** "- The 2026 final beta keeps the red polka-dot bandana look, the Plasma Shotgun and the Gamma Burst (bright yellow burst field) [Observed, fan thumbnail]; the rest of the 2026 kit is unverified (the showcase's Combat Tech chapter, 44:12–47:23, is unwatched)."
   - **Evidence:** V/yt/s9W6eLXj9qc/maxres3.jpg; W/dl/2026-changes/yt/next_-lAtv-j9Sms.json (description timestamps).
10. **Research notes, /home/user/thallo-site/research_notes/Battle Bears character lore/saberi_sanchez.md, line 58.**
    - **Current:** "Gear: she holds a chunky double-barrelled gun with a glowing purple core. A mechanical "third arm" rises from behind her and holds a purple-glowing disc."
    - **Correction:** "Gear: she holds a twin-barrelled olive-and-silver gun with a magenta crystal ridge and a magenta core. A khaki jointed "third arm" rises from behind her and holds a grey riveted saucer with a glowing magenta rim."
    - **Evidence:** saberi29_copy.png samples (ridge ≈#FB4DFE, core ≈#FF45FF, rim ≈#F643FE, arm ≈#6B5942).
11. **Report, /home/user/thallo-site/reports/Battle Bears character lore.md, line 143.**
    - **Current:** "holds a chunky double-barrelled gun with a glowing purple core, and has a mechanical third arm rising behind her with a purple-glowing disc [Observed]"
    - **Correction:** "holds a twin-barrelled olive-and-silver gun with a glowing magenta crystal ridge and magenta core, and has a khaki jointed third arm rising behind her with a grey saucer whose rim glows magenta [Observed]"
    - **Evidence:** as item 10.

## Open questions
- **Energy Rifle:** what colour is the beam in each era (magenta ribbon in 2013, pale cyan in 2016)? Is the change a patch, a team tint or a skin effect? The 2016 cyan frame also had the Missiles deployed.
- **Missiles:** is the Nov 2013 yellow-and-lime faceted starburst (wAQLCQDHUZk maxres3) really the Missiles' blast? What do the Landmine explosion and the thrown mine look like? What was the glossy magenta sphere in the May 2015 "Land Mine to suicide" thumbnail?
- **Minigun:** did its beam colour change from magenta-white (2013) to pale cyan (2016)?
- **Social Butterfly:** which 0.5 s "Saboteur" effect does it apply (controls reversed, stun or slow, as for Sake Bomb, Sucker Punch and Phantom Hug)? Do the butterfly bolts fly visibly?
- **Gamma Burst:** is the field a yellow dome (wiki; bright yellow glow in 2026), lime-green curls (2018), or both in sequence? No frame shows a dome edge.
- **2026 kit:** does the 2026 build keep the Energy Rifle, PMG, Toxic Rifle, Social Butterfly, Missiles, Minigun, Landmine and the three melees? The JustNubz chapter 44:12-47:23 is unwatched. What does the build label "3.0.7_2026.11.19_b7" mean?
- **2.9 preview art:** was the "Developer Update video" that first showed it the Apr 25 2014 "Oliver Overhaul" episode? That episode's description calls itself the "first edition" of the series, and the Riggs edition came only on May 7, after the May 1 sneak peek. So the answer is very likely yes [Inference], but unconfirmed.
- **"Saberi Redesign (Early 2.11)" (wRXMFQqYxRQ, Aug 28 2014):** what changed, a model change or a skin?
- **Toxic Rifle concept art:** who made it, and is it official?
- **Minigun price:** is it 60 Gas (2020 infobox) or 80 Gas (every earlier revision and the body text)?
- **SkyVu text:** is there SkyVu text for 2.15, 2.19, 2.20 or 2.53? What does the 2014 "Saberi-Blog.png" show? web.archive.org refused all 119 attempts today. The [Canon] 2.4, 2.6 and 2.9 quotes rest on copies saved on 2026-10-14.
- **Landmine mechanics:** are the wiki's claims right that a mine explosion reloads the primary, and that one activation fires "up to two mines"? Is the in-game name "Landmine" or "Land Mine"?
