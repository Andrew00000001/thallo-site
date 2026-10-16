# Oliver (Soldier): BBG weapons dossier

Oliver is the Soldier class in Battle Bears Gold. SkyVu's Steam copy lists him as "-SOLDIER: Oliver" [Canon, Steam appdetails 4408320, re-fetched today]. The wiki's Soldier (BBG)/Weapons table, which I re-read today, lists 21 BBG weapons: 9 primaries, 7 secondaries and 5 melees [Fan-wiki]. This dossier covers all 21. It also covers the Turkish SW Boots. They are a Special shared by every class, but SkyVu names them alongside his defaults: "Grab your A Salt Rifle, Bearzooka and those Turkish SW Boots and fight it out with friends across beloved Battle Bears locations." [Canon, Steam]. The 2026 Steam copy also promises "80+ PRIMARY WEAPONS 60+ SECONDARY WEAPONS 50+ MELEES 10 SPECIAL EQUIPMENT" [Canon]. None of SkyVu's 7 Steam news posts (Feb 24 to Oct 14, 2026) gives a Soldier-specific weapon list, stat change or price [Canon, absence checked today].

**Sources I could reach today.**
- Fan wiki: the MediaWiki API for all 21 weapon pages, the class page, its /Weapons and /Skins subpages, Status Effects, Versions, Bearzooka, Battle Bears Heroes, Power Glove and Turkish SW Boots. Image files came from static.wikia.nocookie.net. I also used the wiki's 32-px weapon icon sprite, File:WeaponSprite.png (2015).
- Steam appdetails and the Steam news API.
- battlebears.com/pages/characters.
- i.ytimg.com thumbnails. These include SD variants and YouTube's signed "key-moment" chapter thumbnails, which carry exact millisecond times, from SkyVu's own video "BATTLE BEARS GOLD Developer Update - Oliver Overhaul" (Apr 25, 2014) and from the 2026 JustNubz showcase's Soldier chapter.
- SkyVu's 2026 Steam trailer and screenshots, and the Steam clan banners.

**Blocked.** web.archive.org returned HTTP 403 through curl, and WebFetch reported "unable to fetch from web.archive.org". So the archived 2.6 change log and SkyVu blog posts are unread. battlebears.vanillaforums.com (the 2.8 and 2.17 balance notes) was refused by the proxy with a 502. I watched no videos. All YouTube evidence comes from single thumbnail frames.

**Image key.** These are absolute local folders. Wiki "File:" names are given where they exist.
- [W] = /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/oliver/png/ (PNG copies of wiki files). [W2], [W3] and [W4] are the sibling folders png2/, png3/ and png4/.
- [R] = /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/oliver-r3/ (my downloads and contact sheets). Subfolders: img/ (new wiki files), yt/ (thumbnails, named <id>_<variant>.jpg), ytk/ (key-moment frames), tr/ (trailer frames at 4 fps from 38.0 s, numbered f_NNN = 38.0 + (NNN-1) x 0.25 s).
- [D] = /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/oliver-dossier/img/
- [V] = /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/
- [C] = /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/oliver/official/clan/
- YouTube thumbnail URLs follow https://i.ytimg.com/vi/<id>/<variant>.jpg. hq1/hq2/hq3 and sd1/sd2/sd3 are YouTube's automatic frames at about 25%, 50% and 75% of the video. The times I give for them are approximate [Inference from the YouTube convention plus durations from the wiki metadata].

**Era notes.**
- Dates [Fan-wiki]: BBR launched Oct 8, 2011 (US) and was renamed BBG on May 24, 2013; BBG for Windows came out Dec 20, 2013.
- The wiki's 2013 demo videos (uploader Dban1, captions such as "Visit BBR.wikia.com for more!") are dated Apr 14–16, 2013. The "Photo 19-04-13" in-game item photos are from Apr 19, 2013. Both are therefore **late BBR, one month before the BBG rename** [Inference from the dates].
- SkyVu's own video description reads: "This week, Oliver receives the first overhaul! Trevor explains in detail all of the changes made to this elite Solider class." [Canon, YouTube 9qYIIH8NV-4 description]. The wiki's Versions page does not record which build shipped that overhaul [Fan-wiki, absence].

## Shared visual language (used by several weapons below)
- **Bullet muzzle flash and hit.** Bullets leave a small yellow-orange 4–5-point star flash at the muzzle. A matching yellow-orange star pops on the struck enemy [Observed, A Salt Rifle demo https://i.ytimg.com/vi/guopL_SYkYA/sddefault.jpg].
- **Shot hitting a surface.** A white-yellow V-shaped spark appears [Observed, Spreadshot demo JnGvsjOISNQ hq1, about 3.5 s].
- **Distant hits.** A grey-white puff with a pale-yellow core [Observed, HlYoml_9Wx0 sddefault].
- **Melee hit.** A cluster of chunky yellow 5-point cartoon stars [Observed, Krikkit Bat demo JFi380KnDUM hq1, about 6 s]. The same stars ring a struck character in SkyVu's 2026 Steam screenshot [V]/steam_screens/screen_00.jpg [Observed].
- **Explosions, 2013.**
  - A faceted, low-poly yellow-orange chunk with round grey cartoon smoke puffs [Observed, Y8uyyLgcsrQ hq1, about 5.5 s; source of the blast unknown].
  - A huge white starburst with long rays plus grey smoke [Observed, guopL_SYkYA sd2, about 10.5 s; source unknown].
  - Dark-grey round smoke puffs after a TNT kill [Observed, [R]/img/Images_age_of_Oliver_killing_Riggs_with_TNT_launcher.png].
- **Explosions, 2026 official.** Chunky, faceted, translucent yellow-white blasts with flying debris [Observed, [V]/steam_screens/screen_02.jpg and screen_03.jpg; trailer 26.5–27.5 s]. SkyVu's Closed Testing 5 banner (Oct 14, 2026) lists "LIGHTING, EFFECT & TEXTURE IMPROVEMENTS" [Canon; text read in the image [C]/b7c8f8f133ad960899cce9f3d232b42847891d08.png]. So 2026 effects may differ from the 2012–14 captures [Inference].
- **Status icons.**
  - Controls Reversed: "a green question mark will appear over the player's head" [Fan-wiki, Status Effects].
  - Irradiated: "a yellow circle will appear over the player's head and a noise from a Geiger counter will begin sounding". The circle dissolves into the radiation symbol, and the target explodes at 100 RP [Fan-wiki].
- **Kill.** No frame I opened clearly shows what a defeated bear does. After kills register, the Spreadshot demo shows a bright yellow-orange glowing blob on the floor (JnGvsjOISNQ hqdefault and hq3) [Observed; what it is is Unverified].
- **Headband colour.**
  - Blue in AZt_huguhzc, HlYoml_9Wx0, sDq7aTPa4Uw, ICIsRtcYckY, F2rsMmK6K68, JQ4MjeJfp2M, guopL_SYkYA and ku2RHse4lPA [Observed].
  - Red in P5EsIBxZS-k, 1pOpppsjyuQ, 5u0X3LDgwWM, JnGvsjOISNQ, Y8uyyLgcsrQ, JFi380KnDUM and every store shot [Observed].
  - That this is the team colour is an [Inference].

## Oliver model for framing (2013 BBR/BBG)
Approximate colours were sampled under arena lighting from [W]/Photo_19-04-13_12_02_36_PM.png [Observed]:
- Very dark-brown fur (about #38190A in the arena light) and a red headband (about #A2000D).
- A crossed bandolier of brass cartridges (about #E9D85A to #F6EB98) on dark-red straps (about #7F000A), plus red wristbands.
- Red knee bands with silver-ringed red buttons (about #900611, ring about #B2BBC1).
- A pale grey-lavender backpack (about #745F7E).

Weapon sizes below are estimates against Oliver = 1.0x (ears to feet), taken from item photos [Inference].

---

## A Salt Rifle (ASR) (primary; default since BBR v1.0, 2011; named in SkyVu's 2026 Steam copy)
- **Official text:** "Standard pun rifle issued to all soldiers. Help it out by equipping extra damage equipment!" [Game text via wiki] (https://battlebears.fandom.com/wiki/A_Salt_Rifle). From Steam: "Grab your A Salt Rifle, Bearzooka and those Turkish SW Boots and fight it out with friends across beloved Battle Bears locations." [Canon].
- **Look:**
  - A sage/mint-green rifle (about #95A092, highlights about #BED8CB) with salmon-pink inset panels, a row of rounded green ribs along the forend, a grey ribbed pistol grip, a thin silver barrel and a squared stock [Observed].
  - **On top sits a white salt shaker (about #CCE3DE), fed through a curved, ribbed sleeve** [Observed, [W]/Oliver3d.png (File:Oliver3d.png); [R]/img/A_salt_rifle.png, a BBR store side view from Mar 2012].
  - The concept sheet shows AR1 to AR4. AR3 has a glass shaker fed through a ribbed hose, and the shipped model matches it [Observed [W]/ASRconcept.png; the match is Inference].
  - Held two-handed at chest or waist; about 0.6x Oliver long [Inference].
  - Wiki icon: a green/red rifle with a white shaker [Observed, sprite tile "asr" in [R]/icons_soldier.png].
  - 2026 (fan footage): in the closed-playtest loadout menu, Oliver in the Night Bear skin ("SKIN NIGHT BEAR" on screen) holds a grey gun with a white block on top, upright beside his head [Observed, key-moment frame at 4:44.97 of -lAtv-j9Sms, [R]/ytk/-lAtv-j9Sms_284966_w336.jpg].
  - That matches File:Night.jpg (2014), where Night Bear holds the ASR [Observed [R]/img/Night.jpg]. That the 2026 gun is the ASR is an [Inference].
- **Firing:**
  - Stats: "Primary - Automatic", long range, "perfect accuracy"; damage 6, rate of fire 0.15 s, ammo 25, reload 3.0 s. Ammo+1/+2 adds 8/15 bullets, Damage+1/+2 adds 0.5/1.0 [Fan-wiki].
  - The Apr 2013 demo HUD reads x/25 [Observed, guopL_SYkYA sd1/sd2/sd3].
  - The muzzle flash is a small yellow-orange star (guopL_SYkYA sddefault) [Observed].
  - The Tutorial version has 70 ammo [Fan-wiki]. The Tutorial capture shows 70/70 with the ASR icon [Observed [D]/Tutorial_BBG_.jpg].
  - Sound is undocumented.
- **Projectile:**
  - The name puns on salt, and the Sci-Fi ASR text contrasts lasers with "analog salt-dust" [Game text via wiki]. That the ASR "fires salt" is an [Inference].
  - A thin yellow-red line runs toward a target in guopL_SYkYA sd1 (about 5 s) [Observed]; that it is a tracer is an [Inference].
- **Impact / end result:** A yellow-orange star flash on the struck enemy (guopL_SYkYA sddefault) [Observed]. No status effect [Fan-wiki].
- **Images viewed:** [W]/Oliver3d.png; [W]/ASRconcept.png; [R]/img/A_salt_rifle.png; [R]/img/Night.jpg; [R]/ytk/-lAtv-j9Sms_284966_w336.jpg; [D]/Tutorial_BBG_.jpg; [D]/Tutorial_2.jpg; https://i.ytimg.com/vi/guopL_SYkYA/{sddefault,sd1,sd2,sd3}.jpg; [R]/icons_soldier.png.
- **Depiction for shorts:** The white shaker on top is what identifies the gun (documented). Fire small yellow tracer flecks from a star-shaped muzzle flash, with yellow star pops on hits (observed style). A puff of white salt grains on each hit is a [BBG News invention].
- **Confidence:** partial.

## Heavy A Salt Rifle (HASR) (primary; one of the original three, BBR v1.0, 2011; 110,000 Joules)
- **Official text:** "With higher capacity and lower damage the Heavy A Salt Rifle gives its owner more room for error before reloading but at the cost of stopping power." [Game text via wiki] (https://battlebears.fandom.com/wiki/Heavy_A_Salt_Rifle).
- **Status:**
  - 110,000 J, level 1. Price history 8,000 → 10,000 → 100,000 → 110,000 J [Fan-wiki].
  - The current damage of 8 is higher than the ASR's 6, which contradicts "lower damage". The stats changed after the text was written [Inference].
- **Look:**
  - An AK-style rifle ("design seems to be based off of the AK-47" [Fan-wiki]) in olive green with salmon/red panels.
  - **A large grey-and-red ring loops from the stock round the grip.** The ring is about 0.3x Oliver across; the gun is about 0.55x long [Observed [W]/Photo_19-04-13_12_02_04_PM.png, [W]/HASR_weapon_concept.png ("AR5"), [W]/Soldier_Weapon.png, [R]/img/Heavy_A_salt_Rifle.png (BBR store, Mar 2012), [R]/img/Oliver_overhaul.png; scale is Inference].
  - Held at the hip, angled down [Observed].
- **Firing:**
  - Stats: automatic, mid range, "partial inaccuracy"; damage 8, rate of fire 0.125 s, ammo 60, reload 5 s, dispersion 0.08, -15% speed [Fan-wiki].
  - The Apr 2013 HUD reads x/60 (HlYoml_9Wx0 sd1, about 6 s) [Observed].
  - **In SkyVu's Apr 25, 2014 Oliver Overhaul video, the HUD shows the HASR icon at x/30.** The key-moment frame at 68.966 s reads 5/30 ([R]/ytk/9qYIIH8NV-4_68966_w336.jpg), and sd1 reads 8/30 ([R]/ov_icons_r3.png) [Observed]. The overhaul may have halved the magazine [Inference]; whether that shipped is [Unverified].
- **Projectile:** None visible [Unverified].
- **Impact / end result:** While firing, a grey-white smoke puff with a pale-yellow core appears at the far end of a walkway (HlYoml_9Wx0 sddefault, HUD 21/60) [Observed]. Crediting it to the HASR rounds is an [Inference].
- **Images viewed:** [W]/Photo_19-04-13_12_02_04_PM.png; [W]/HASR_weapon_concept.png; [W]/Soldier_Weapon.png; [R]/img/Heavy_A_salt_Rifle.png; [R]/img/Oliver_overhaul.png; https://i.ytimg.com/vi/HlYoml_9Wx0/{sddefault,sd1,sd2,sd3}.jpg; [R]/ytk/9qYIIH8NV-4_68966_w336.jpg; https://i.ytimg.com/vi/9qYIIH8NV-4/sd1.jpg.
- **Depiction for shorts:** The ring silhouette is the read (documented). Show a fast spray with a little spread, yellow star pops up close and grey puffs at range (observed style). Brass casings flicking out are a [BBG News invention].
- **Confidence:** partial.

## Soaker (primary; one of the original three, BBR v1.0, 2011; 60,000 Joules, level 10; nerfed later)
- **Official text:** "The range is limited compared to other rifles, but it's way more accurate!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Soaker).
- **Status:**
  - It once tied for the fastest rate of fire and was "the highest damaging primary(dealing 100 damage per second ...)... before it's stats were reduced". No date is given [Fan-wiki].
  - BBG v2.6 (Dec 20, 2013): "Soaker and Urine Trouble issues have been fixed" [Fan-wiki, Versions].
- **Look:**
  - "This weapon is based on the Super Soaker" [Fan-wiki].
  - A green-grey water-gun body with salmon panels. **A big bright-yellow pressure tank (about #F8E126) with red-orange diagonal stripes (about #BC4022) sits on top**, plus a small round yellow tank and a pump grip under the barrel.
  - Sources: [Observed [W]/Soaker_Concept.png ("AR4"), [W]/ASRconcept.png, [W]/Photo_19-04-13_12_02_08_PM.png, [R]/img/Soaker.png (store, Mar 2012), sprite tile "soa"].
  - About 0.55x [Inference].
- **Firing:**
  - Stats: automatic, close range (950 units); damage 5, rate of fire 0.1 s, ammo 60, reload 4 s, +10% speed [Fan-wiki].
  - The Apr 2013 HUD reads x/60 (Y8uyyLgcsrQ) [Observed].
  - A May 2014 Everyplay clip titled "...Oliver Soaker" reads 0/70 (dZWA5i0krBY sddefault/sd1) [Observed]. That this is a post-overhaul change is an [Inference].
- **Projectile:**
  - No frame shows it [Unverified].
  - The Super Soaker basis, and the Urine Trouble retexture that "fires urine", suggest a liquid stream [Inference].
- **Impact / end result:**
  - In the Apr 2013 demo, a pink target shows a white, cyan and pink flash ringed with small yellow stars (Y8uyyLgcsrQ hqdefault) [Observed].
  - Nearby, a faceted yellow chunk flies with grey smoke puffs (hq1, about 5.5 s) [Observed].
  - Crediting either to the Soaker is [Unverified]. The stars match the melee-hit style.
- **Images viewed:** [W]/Soaker_Concept.png; [W]/ASRconcept.png; [W]/Photo_19-04-13_12_02_08_PM.png; [R]/img/Soaker.png; https://i.ytimg.com/vi/Y8uyyLgcsrQ/{hqdefault,hq1,hq2,hq3}.jpg; https://i.ytimg.com/vi/dZWA5i0krBY/{sddefault,sd1,sd2,sd3}.jpg; [R]/yt_asr_soak_zoom.png.
- **Depiction for shorts:** Use the yellow striped tank as the identifier (documented). A clear-blue water jet, shaped like the observed Urine Trouble stream (thin at the nozzle, widening into droplets), that splashes on contact is a [BBG News invention].
- **Confidence:** partial.

## Urine Trouble (primary; BBR v1.3.1 week 3, 2012; Gas item)
- **Official text:** "Life is full of worries. Most of life's worries, however, can't get in your eyes, mouth, and nose at the same time." / "This one can. And it will." [Game text via wiki] (https://battlebears.fandom.com/wiki/Urine_Trouble).
- **Status:**
  - Price conflict: 60 Gas in the infobox vs 75 Gas in the /Weapons table and class changelog. It was originally 150,000 J; level 1 [Fan-wiki].
  - Forum Appreciation participants got it early for free [Fan-wiki].
  - Covered by the v2.6 fix [Fan-wiki].
- **Look:**
  - "It is a retexture of the Soaker" [Fan-wiki].
  - A white and maroon-red body (about #6C212C / #A93943) with green flame decals and orange oval vents.
  - **A large translucent amber tank (about #FCB246 / #F39E45)** on a grey hose fitting, plus a small amber bubble.
  - A long clear tube barrel with an orange tip and a white nozzle, and a ribbed grey pump.
  - Sources: [Observed [W]/Qjc7y.png, [W4]/ile:BBRWEAPONS.png, [R]/img/Oliver_overhaul.png, sprite tile "urt"]. In hand it reads as a yellow-cream gun (sDq7aTPa4Uw hq1) [Observed].
  - About 0.55x [Inference].
- **Firing:**
  - Stats: automatic, close range (750 units); damage 6.25, rate of fire 0.1 s, ammo 40, reload 5 s, +10% speed. It has the highest base DPS of the Soldier primaries [Fan-wiki].
  - The Apr 2013 HUD reads x/40 [Observed].
- **Projectile:**
  - "As its name suggests, it fires urine" [Fan-wiki].
  - **A wiki capture, File:Urine trouble range.jpeg (uploaded May 10, 2013), shows the stream** [Observed [R]/img/Urine_trouble_range.jpeg].
  - Fired by an enemy Oliver, it is a bright yellow (about #F6E635) liquid jet. It starts thin and straight, with a small yellow glow at the muzzle, then widens into a ribbon that breaks into droplets.
- **Impact / end result:**
  - The stream ends in a trail of yellow splats with orange edges on the floor [Observed, same file].
  - In the 2013 demo, a thin yellow streak runs next to a pink target (sDq7aTPa4Uw hqdefault), and a pink-white blob appears at range (hq3, about 15 s) [Observed; attribution is Inference].
  - No status effect [Fan-wiki, not on the Status Effects list].
- **Images viewed:** [W]/Qjc7y.png; [W4]/ile:BBRWEAPONS.png; [R]/img/Urine_trouble_range.jpeg; [R]/img/Oliver_overhaul.png; https://i.ytimg.com/vi/sDq7aTPa4Uw/{hqdefault,hq1,hq2,hq3}.jpg; [R]/yt_fx_zoom.png; [R]/new_c_zoom.png.
- **Depiction for shorts:** Show a lemonade-yellow stream that is thin at the nozzle and fans into droplets and floor splats (observed). Keep it gag-level. The official text aims at "eyes, mouth, and nose", so cut away before contact. A disgusted recoil from the target is a [BBG News invention].
- **Confidence:** observed.

## Sci-Fi ASR (SFASR) (primary; BBR v1.3.1 week 2, 2012; seen in SkyVu's July 2026 banner)
- **Official text:** "In the future, lasers will be the seasoning of choice among the elite while the common rabble shall continue to put analog salt-dust into their primitive bodies." [Game text via wiki] (https://battlebears.fandom.com/wiki/Sci-Fi_ASR).
- **Status:**
  - 105,000 J, level 10; originally 90,000 J [Fan-wiki]. The 90,000 J price shows in an Apr 2013 store capture [Observed [R]/img/Oco_gauntlet.jpeg].
  - **2026:** in SkyVu's "CLOSED TESTING" banner (Steam post of Jul 6, 2026), the Sam-Are-I-skinned Oliver holds a grey gun with a ribbed grip, topped by a dark canister with glowing red-orange slits [Observed [C]/3b7f9b97cdb4f799bbc696475d327f4d7c7a9523.png; crop [R]/clan_jul6_oliver.png].
  - The skin matches File:SAm-Are-i.png [Observed [W3]/ile:SAm-Are-i.png]. That the gun is the SFASR is an [Inference, high].
- **Look:**
  - A chunky silver-grey rifle (about #BCBCBC to #E4E4E4) with four dark holes (2x2) on the barrel shroud, a dark teal muzzle tip and a ribbed grey grip and magazine.
  - **On top is a tilted canister with glowing red-orange-yellow slits and a glowing cream-orange hexagonal end cap** [Observed [W]/Oliver_SciFi_Asalt.png; sprite tile "sfa"].
  - "a retexture of the standard A Salt Rifle" [Fan-wiki]. About 0.55x [Inference].
- **Firing:**
  - Stats: automatic; damage 5, rate of fire 0.15 s, ammo 25 ("the lowest ammo of all automatics"), reload 2.0 s, +5% speed [Fan-wiki].
  - The Apr 2013 HUD reads x/30 (P5EsIBxZS-k) [Observed], vs 25 in the infobox.
- **Projectile:** The text implies lasers [Game text via wiki → Inference]. Their colour and shape are undocumented [Unverified].
- **Impact / end result:** At about 9.5 s (P5EsIBxZS-k hq2), a vertical yellow-white light flash bursts on the struck enemy, with a pink-magenta glowing bar in the foreground [Observed]. Which weapon made them is [Unverified].
- **Images viewed:** [W]/Oliver_SciFi_Asalt.png; [C]/3b7f9b97cdb4f799bbc696475d327f4d7c7a9523.png; [R]/clan_jul6_oliver.png; [W3]/ile:SAm-Are-i.png; [R]/img/Oco_gauntlet.jpeg; https://i.ytimg.com/vi/P5EsIBxZS-k/{hqdefault,hq1,hq2,hq3}.jpg.
- **Depiction for shorts:** Use the glowing slit canister as the read (documented in 2012 and 2026 art). Short red-orange laser bolts matching the canister glow are a [BBG News invention]. Yellow-white hit flashes follow the observed style.
- **Confidence:** partial.

## Sci-Fi HASR (primary; BBR v1.3.1 week 2, 2012; level 15)
- **Official text:** "Look no further for reasons for people to get out of your way, you're holding the only one you need. Should a chump still refuse to step aside, this puppy has a convenient little button to change their mind." [Game text via wiki] (https://battlebears.fandom.com/wiki/Sci-Fi_HASR).
- **Status:**
  - Price conflict: 60 Gas in the infobox vs 85 Gas in the /Weapons table and changelog [Fan-wiki]. **The Apr 2013 store shows a gas-can icon with "85"** [Observed [R]/img/Oco_gauntlet.jpeg], so 85 Gas was at least the 2013 price. It was originally 130,000 J [Fan-wiki].
  - A May 2013 loadout capture pairs it with the Steamshot, Kumakiri and Turkish SW Boots [Observed [R]/img/Kumakiri_another.jpg].
- **Look:**
  - A silver-white retexture of the HASR with a **dark gunmetal ring loop** [Observed [W]/Photo_19-04-13_12_01_58_PM.png; sprite tile "sfh"].
  - Held upright in the demo [Observed ICIsRtcYckY hq3]. About 0.55x [Inference].
- **Firing:**
  - Stats: automatic, mid range; damage 7.0, rate of fire 0.125 s, ammo 50, reload 5 s, dispersion 0.05, -10% speed, "56 base DPS" [Fan-wiki].
  - The Apr 2013 HUD reads x/50 [Observed ICIsRtcYckY].
  - The "convenient little button" has no documented function [Unverified].
- **Projectile, impact / end result:** None visible in the frames [Unverified].
- **2026:**
  - In the official trailer (38.25–41.25 s), the Gold Oliver skin stands on the lava map holding a **silver-grey gun with a black curved loop under it**. An Engineer-type bear's yellow beam hits him and he flashes yellow [Observed [R]/tr/f_002.jpg to f_014.jpg; [R]/tr_gold_zoom.png].
  - That this is the Sci-Fi HASR is an [Inference, medium-low].
  - On the Oliver card (41.5–42.75 s) he holds a silver-grey blocky barrel with a black angular upper block [Observed [R]/tr_card_gun.png]; which gun it is is [Unverified].
- **Images viewed:** [W]/Photo_19-04-13_12_01_58_PM.png; [R]/img/Oco_gauntlet.jpeg; [R]/img/Kumakiri_another.jpg; https://i.ytimg.com/vi/ICIsRtcYckY/{hqdefault,hq1,hq2,hq3}.jpg; [R]/tr_oliver_sheet.png; [R]/tr_gold_zoom.png; [R]/tr_card_gun.png.
- **Depiction for shorts:** Use the silver gun with the dark ring (documented). Pale cyan rounds, and the "little button" firing one charged shot, are [BBG News invention]; do not present them as canon.
- **Confidence:** partial.

## O.C.O. Gauntlet (primary; BBR v1.3.2, 2012; 45,000 Joules, level 20)
- **Official text:** "Spawn orbs of energy that damage when touched and explode on direct impact." [Game text via wiki] (https://battlebears.fandom.com/wiki/O.C.O._Gauntlet). The Engineer's Power Glove text links to it: "The precursor to the O.C.O. Glove, this weapon can rapidly fire small orbs of energy..." [Game text via wiki].
- **Status:**
  - Originally 20 Gas [Fan-wiki]. An Oct 2012 store tile reads "OCO GAUNTLET / BUY NOW ! / 20" beside a gas-can icon [Observed [R]/img/OCO_gauntlet_.jpg].
  - It cost 45,000 J by Apr 2013 [Observed [R]/img/Oco_gauntlet.jpeg].
  - The game spells it "OCO Gauntlet", and O.C.O. stands for "Over Clocked Oliver" [Fan-wiki; the spelling is Observed in the store].
- **Look:**
  - The render shows two pieces.
  - The first is a black/gunmetal armoured gauntlet (about #2A292B, greys about #989698) with **glowing cyan (about #16C8E9) claw stripes and "OCO" lettering** and a keypad block with cyan buttons and a D-pad.
  - The second is a cyan mitten with white glowing circuit lines, a white ring on the palm and a white cuff.
  - Sources: [Observed [W]/OCO_Gauntlet.png; [W4]/1.3.2WEAPONS.png; sprite tile "oco"].
  - Worn on the right hand, about head-sized (about 0.3x) [Observed [W3]/Gold_Oliver.png, [W3]/ile:SAm-Are-i.png; scale is Inference].
  - In the store a white-blue electric crackle rises over the glove [Observed [R]/img/Oco_gauntlet.jpeg]. The wiki calls this the cosmetic "electrical charge being absorbed" [Fan-wiki].
- **Firing:**
  - Type "Primary - Explosives". Each orb "is initially spawned at a stationary position ... where for 2 seconds it does not deal damage", then "will accelerate very fast over a short distance in the direction the player was aiming" [Fan-wiki].
  - Up to three orbs, released with a delay. Each orb self-implodes after 10 s, and an enemy standing in front of a new orb sets it off early [Fan-wiki].
  - Stats: explosives 40–60 (+30 on a direct hit), AoE 50/150, cooldown 1.0 s, ammo 1, reload 2.0 s, 1,500 u/s, 12 s total life, +10% speed [Fan-wiki].
  - The Apr 2013 HUD reads x/2 [Observed 1pOpppsjyuQ].
- **Projectile:**
  - **A large translucent sphere with visible low-poly facets: a pale cyan-white to pale-green field around a saturated blue core.** A cyan square bracket outline appears beside it [Observed 1pOpppsjyuQ hqdefault, hq1 about 12 s, hq2 about 24 s].
  - The wiki describes it as "a dark blue core and a pulsing light blue field" [Fan-wiki].
- **Impact / end result:**
  - A huge pale green-cyan translucent burst fills the view near enemies (hq3, about 36 s) [Observed].
  - An enemy touching the orb makes it "implode dealing damage to any enemies in the explosion's AoE" [Fan-wiki]. Self-kill is possible [Fan-wiki].
  - Glitches: orbs explode when spawned while looking down, and with the Iron Curtain they fly upward [Fan-wiki].
- **Images viewed:** [W]/OCO_Gauntlet.png; [W4]/1.3.2WEAPONS.png; [W3]/Gold_Oliver.png; [W3]/ile:SAm-Are-i.png; [W2]/ile:Red_Blue_OCO.png; [R]/img/OCO_gauntlet_.jpg; [R]/img/Oco_gauntlet.jpeg; https://i.ytimg.com/vi/1pOpppsjyuQ/{hqdefault,hq1,hq2,hq3}.jpg; [R]/yt_fx_zoom.png.
- **Depiction for shorts:** Follow the documented sequence: the orb hangs harmless for a beat crackling cyan, then rockets forward and implodes in a pale cyan-green flash. The visibly faceted sphere is observed. Showing the implosion as an inward suck is a [BBG News invention].
- **Confidence:** observed.

## Minigun (Soldier) (primary; BBG v2.11, Aug 27, 2014; 45 Gas; reworked after release)
- **Official text:** "Mini refers to your enemies after its done with them. " [Game text via wiki] (https://battlebears.fandom.com/wiki/Minigun_(Soldier)).
- **Status:**
  - "insanely overpowered on release due to a typo in its explosive damage values ... It has since been changed and the bullet damage has been nerfed as well." [Fan-wiki].
  - It is not the Combat Tech Minigun. The wiki file File:Minigun.jpg (2013) shows a different character with a floating hex orb, **not** this gun; do not use it [Observed [R]/img/Minigun.jpg].
- **Look:**
  - A compact, boxy gunmetal rotary gun in a hexagonal housing, with **three barrel muzzles in a triangle**, a top carry loop and a small yellow band on top. Held at the hip [Observed [W]/Mini.png (File:Mini.jpg, Oct 31, 2014); [R]/img/Minigun.jpeg (the Sam-Are-I skin on the "2.11" matchmaking screen); sprite tile "mng"].
  - About 0.45x [Inference].
- **Firing:** Automatic; damage 3, rate of fire 0.075 s, ammo 80, reload 5 s, -10% speed, +20% health. "It is best used for long ranged combat" [Fan-wiki].
- **Projectile:** Undocumented and not seen [Unverified]. The trivia's "explosive damage values" implies the release build's rounds carried explosive damage [Inference].
- **Impact / end result:** Undocumented [Unverified].
- **Images viewed:** [W]/Mini.png; [R]/img/Minigun.jpeg; [R]/img/Minigun.jpg (rejected); [R]/new_c_zoom.png; [R]/icons_soldier.png.
- **Depiction for shorts:** The three-barrel triangle is the read (observed). Barrel spin-up, a dense stream of yellow tracers and a waterfall of brass casings are a [BBG News invention]; yellow star pops follow the observed style.
- **Confidence:** partial.

## Acreambo Pistols (primary; BBG v2.18, Apr 3, 2015; Oliver's BB Heroes basic attack)
- **Official text:** "Cream your opponents with the all new dual wielding pistols! Run around and shoot like your in the matrix! " [Game text via wiki; "your" is sic per the wiki] (https://battlebears.fandom.com/wiki/Acreambo_Pistols). BBH: "His 'Acreambo Pistols' can cause problems for enemies at all ranges, with capabilities to fire lots of bullets in quick succession, these are complimented by his powerful 'Bearzooka' Ultimate which deals massive damage and destroys obstacles." [Canon, https://battlebears.com/pages/characters, re-read today].
- **Status:** Price conflict: 60 Gas in the infobox vs 75 Gas in the /Weapons table and changelog [Fan-wiki]. In BBH it is Oliver's default attack, listed at "6 x 360" damage and "Long" range, May 2023 [Fan-wiki].
- **Look:**
  - **Two blocky light-blue/teal pistols** (shadow samples about #2C7490 / #1F5D76), each with an over-under pair of muzzle holes (large on top, small below) and **red-and-white candy chevrons** on the slide, one in each hand [Observed [W]/Image-1428969087.png (uploaded Apr 13, 2015); sprite tile "acp"].
  - Concept art: the gingerbread "Gingervitus" Oliver dual-wields candy-striped pistols with yellow-white muzzle flashes on a snowy "Battle Bears Royale" banner [Observed [W]/AcreamboPistolsandSnoMatterconceptart.png].
  - Each pistol is about 0.2x [Inference].
- **Firing:** Automatic, dual-wielded; "It fires two bullets per one ammo spent"; damage 6.0, rate of fire 0.3 s, ammo 28, reload 5.0 s, -10% health, +10% speed [Fan-wiki].
- **Projectile:** "The projectile looks like toothpaste." [Fan-wiki]. Not observed: the wiki's 2015 video I5sH910fE94 returns no thumbnails [Unverified].
- **Impact / end result:** "It is the only weapon in the game to not have an animation when the projectile hits a surface." [Fan-wiki].
- **Images viewed:** [W]/Image-1428969087.png; [W]/AcreamboPistolsandSnoMatterconceptart.png; [W2]/BBH_Profile_Oliver.png; [R]/zoom_prim.png; [R]/icons_soldier.png.
- **Depiction for shorts:** Fire alternating toothpaste-like ribbons that simply vanish on contact, with no splat (both documented). Ribbon colours in red, white and teal are a [BBG News invention]. A sideways "matrix" dive follows the game text ("like your in the matrix").
- **Confidence:** partial.

## Bearzooka (BBG) (secondary; default since BBR v1.0, 2011; named in SkyVu's 2026 Steam copy; BB Heroes Ultimate)
- **Official text:**
  - "The basic weapon of any Soldier. Does a good amount of damage, with a decent area of effect (AOE). Useful for all situations." [Game text via wiki] (https://battlebears.fandom.com/wiki/Bearzooka_(BBG)).
  - Class blurb: "Oliver the soldier is a well rounded fighter with decent speed and health. Use his starting Bearzooka carefully as it is easy to kill yourself with it!" [Game text via wiki, Template:Class:Soldier (BBG)].
  - The 2026 Steam line [Canon], and in BBH a "powerful 'Bearzooka' Ultimate which deals massive damage and destroys obstacles" [Canon].
- **Look:**
  - **A coral-red hexagonal tube** (about #A14445, lit about #AD5155) with **glowing orange rectangular panels** (about #F78C1A to #FB9E27) between grey hex collars (about #63595A).
  - A wide, flared hex muzzle with a dark bore at the front; a narrower rear section ending in a bolted hex end plate.
  - Carried on the shoulder, or under the arm at the right hip in third person. About 0.7x long.
  - Sources: [Observed [W]/Photo_19-04-13_12_02_26_PM.png; [R]/img/BBR_Bearzooka.png (store, Mar 2012); AZt_huguhzc sddefault/sd1, where the bolted rear plate faces the camera; sprite tile "bzk"; scale is Inference].
  - The wide end is the muzzle: the TNT Launcher, "a retexture of the Bearzooka" [Fan-wiki], fires from its wide, checker-banded end (JQ4MjeJfp2M hqdefault) [Observed; applying this to the Bearzooka is Inference].
  - Concept: a red tube with yellow-orange chevron decals, a flared red/grey checkered bell (the muzzle, by the TNT evidence) and a black pistol grip, labelled "ROCKET" [Observed [W]/Bearzooka_Concept.png, [W]/Soldier_Weapon.png].
  - **Era:** "In BBG and BB0, it is a rocket launcher with red and orange lines. In BBZ and BB-1 it is just a dark green rocket launcher." [Fan-wiki, Bearzooka]. The **dark-green "BEARZOOKA"-lettered tube with yellow/black hazard stripes is BB Zombies (2009)** [Observed [W2]/ile:Bear.png].
- **Firing:**
  - Stats: explosives 40–60, AoE max-damage radius 125 / min-damage radius 250, rate of fire 1.5 s, ammo 1, reload 2.5 s, 1,000 u/s. Ammo+ adds +0; Explosions+ adds +7.5/+15 [Fan-wiki].
  - Conflict: the page text says "has two shots without additional ammo", but the infobox says 1 [Fan-wiki]. The Apr 2013 HUD reads 0/1 and 1/1 [Observed AZt_huguhzc].
  - Planned "Incoming stats" were ammo 3, rate of fire 1 s, explosives 20–40 and reload 3 s [Fan-wiki]; whether they shipped is [Unverified].
  - "The user is very prone to suicide while using the Bearzooka." [Fan-wiki].
  - The /Weapons table wrongly gives its type as "Primary" [Fan-wiki error].
- **Projectile:** A rocket (a "Bazooka" pun [Fan-wiki]). Its model and trail are not seen. A small green dot in the doorway ahead (AZt_huguhzc sddefault) [Observed]; that it is the rocket is [Unverified].
- **Impact / end result:** No Bearzooka-specific explosion frame exists. A small white-grey smoke puff hangs behind a wooden doorway after firing (sd3, about 21 s) [Observed; attribution is Inference]. For explosion style, see the shared section (faceted yellow chunks, grey round puffs, 2026 faceted yellow-white blasts) [Observed generic].
- **Images viewed:** [W]/Photo_19-04-13_12_02_26_PM.png; [W]/Bearzooka_Concept.png; [W]/Soldier_Weapon.png; [W2]/ile:Bear.png; [R]/img/BBR_Bearzooka.png; [R]/img/Oliver_overhaul.png; https://i.ytimg.com/vi/AZt_huguhzc/{sddefault,sd1,sd2,sd3}.jpg; [R]/yt_bz_zoom.png; [R]/zoom_sec.png; [V]/steam_screens/screen_02.jpg, screen_03.jpg.
- **Depiction for shorts:** Put the coral hex tube with glowing orange panels on his shoulder (documented), firing from the wide end. A stubby rocket with a short orange flame and grey puff trail is a [BBG News invention]. Use a faceted yellow-white blast with round grey cartoon smoke (observed generic style). Oliver caught in his own blast is grounded in the class text ("easy to kill yourself with it").
- **Confidence:** partial.

## Spreadshot (BBG) (secondary; one of the original three, BBR v1.0, 2011; 35,000 Joules, level 4)
- **Official text:** "Useless at range but devastating up close. Handy for close encounters..." [Game text via wiki] (https://battlebears.fandom.com/wiki/Spreadshot_(BBG)).
- **Look:**
  - A salmon-red and sage-green shotgun with **the same silhouette as the Steamshot**, which "is a retexture of the Spreadshot (BBG)" [Fan-wiki].
  - A round hex chamber (sage about #5E6E5F, pale grey-green rings about #98A7A0), two red stacks on top, a grey ribbed rod barrel and a curled grey hose underneath.
  - **At the muzzle, a ring of six salmon-red hexagonal tubes** (about #8C504D / #773133).
  - Sources: [Observed [W]/Photo_19-04-13_12_02_29_PM.png; [R]/img/BBR_Spreadshot.PNG (store, Mar 2012); sprite tile "sps"].
  - Held at the hip [Observed]; about 0.55x [Inference].
  - The previous inventory called the hex-tube ring the "rear". It sits where the Steamshot's six-hole muzzle sits in the 2014 key art ([R]/img/Oliver_overhaul.png), so it is the muzzle [Inference].
  - Concept "SPREADSHOT 1" was a red-and-green multi-barrel gun with perforated side plates; that is not what shipped [Observed [W]/Spreadshot_concept.png, [W]/Shotgun_concept.png].
  - The BB-1 ancestor was "a grey-coloured shotgun-like weapon ... five red projectiles" [Fan-wiki, Spreadshot; Observed [W2]/ile:Mzl.ywvsskvf.480x480-75.png].
- **Firing:**
  - Stats: shotgun, close range; damage 20, rate of fire 0.75 s, ammo 6, reload 3 s [Fan-wiki].
  - The Apr 2013 HUD reads x/4 [Observed JnGvsjOISNQ].
  - **SkyVu's Apr 2014 Overhaul video shows the Spreadshot's icon at x/3**: maxresdefault reads 1/3 and sd2 reads 2/3 [Observed [R]/ov_icons_r3.png]. The icon matches wiki sprite "sps" [Observed].
- **Projectile:** Pellets are not visible [Unverified]. In the Overhaul frames where the Spreadshot is equipped:
  - magenta crackling energy runs between Oliver's gun and a panda enemy (maxresdefault) [Observed [R]/ov_zoom_r3.png];
  - lime-green swirling wisps surround a target (sd2) [Observed].
  - Whether either is a Spreadshot effect is [Unverified].
- **Impact / end result:** A white-yellow V-shaped spark burst on a crate (JnGvsjOISNQ hq1, about 3.5 s) [Observed].
- **Images viewed:** [W]/Photo_19-04-13_12_02_29_PM.png; [W]/Spreadshot_concept.png; [W]/Shotgun_concept.png; [W2]/ile:Mzl.ywvsskvf.480x480-75.png; [R]/img/BBR_Spreadshot.PNG; https://i.ytimg.com/vi/JnGvsjOISNQ/{hqdefault,hq1,hq2,hq3}.jpg; https://i.ytimg.com/vi/9qYIIH8NV-4/{maxresdefault,sddefault,sd1,sd2,sd3}.jpg; [R]/ov_icons_r3.png; [R]/ov_zoom_r3.png.
- **Depiction for shorts:** Fire a short cone of small pellets from the six-tube muzzle, ending in white-yellow V sparks (the sparks are observed). Salmon-red pellets matching the gun are a [BBG News invention].
- **Confidence:** partial.

## TNT Launcher (secondary; one of the original three, BBR v1.0 per the /Weapons table; 45,000 Joules, level 13)
- **Official text:** "Use the TNT Launcher to fire multiple projectiles at at a time. Projectiles do not explode on contact but stick around and blow up after a second or two." [Game text via wiki] (https://battlebears.fandom.com/wiki/TNT_Launcher).
- **Status:** The class changelog's v1.0 list omits it, which is a wiki conflict. It was originally 55,000 J. Planned "Incoming stats" were ammo 3, rate of fire 1.5 s, 27–54 damage and reload 5 s; whether they shipped is [Unverified] [Fan-wiki].
- **Look:**
  - The Bearzooka model in light grey/silver (about #6B6B6B in shade) with glowing orange panels (about #F48721).
  - **A grey/black checker band at the wide muzzle end**, and a black pistol grip.
  - Sources: [Observed [W]/Photo_19-04-13_12_02_31_PM.png; [R]/img/TNT_Launcher.png (store, Oct 2012, Pocket Pygmy skin); [R]/img/Oliver_overhaul.png; sprite tile "tnt"]. About 0.7x [Inference].
- **Firing:**
  - Stats: arcing lobs, 3 rounds, rate of fire 1.0 s, reload 3.0 s, 35–75 explosives, AoE 100/250, 1,000 u/s [Fan-wiki].
  - HUD readings: 0/3 to 3/3 in Apr 2013 [Observed JQ4MjeJfp2M]; 1/3 in a 2016 capture [Observed].
  - **Muzzle flash: a spiky yellow-orange starburst** with three to four long spikes at the checkered end (JQ4MjeJfp2M hqdefault and hq1, about 7 s) [Observed].
- **Projectile:**
  - Not seen [Unverified].
  - SkyVu's Soldier concept sheet has "THROWN MISSILE" sketches: a round red bomb with a lit fuse, and a bundle of red dynamite sticks tied with rope with a red ribbon tail [Observed [W]/Soldier_Weapon.png, [W]/Bearzooka_Concept.png]. Linking them to the TNT is an [Inference].
- **Impact / end result:**
  - The charges "stick to the first solid surface they land on" and, after a 1 s delay, "explode in a large AoE, larger than that created by the Bearzooka". They "cannot hit other players directly", and only an Iron Curtain, Tesla Shield or Bass Cannon hit detonates them early [Fan-wiki].
  - A 2016 capture titled "...Oliver killing Riggs with TNT launcher" shows dark-grey round smoke puffs over the kill area, with the kill in the feed [Observed [R]/img/Images_age_of_Oliver_killing_Riggs_with_TNT_launcher.png].
- **Images viewed:** [W]/Photo_19-04-13_12_02_31_PM.png; [W]/Soldier_Weapon.png; [W]/Bearzooka_Concept.png; [R]/img/TNT_Launcher.png; [R]/img/Images_age_of_Oliver_killing_Riggs_with_TNT_launcher.png; [R]/img/Oliver_overhaul.png; https://i.ytimg.com/vi/JQ4MjeJfp2M/{hqdefault,hq1,hq2,hq3}.jpg; [R]/yt_fx_zoom.png; [R]/new_c_zoom.png.
- **Depiction for shorts:** A spiky starburst at the muzzle (observed), then the charge lobs in an arc, sticks with a thunk and fuses for one beat (documented timing). Then a big blast with grey round smoke puffs (observed). Drawing the charge as a red dynamite bundle is an [Inference] from the concept sheet.
- **Confidence:** partial.

## Rockette Launcher (secondary; BBR v1.3.1 week 4, 2012; 110,000 Joules)
- **Official text:** "You know, because it shoots those little rocks... you know what they're called, the little ones... the... uh... rockettes?" / "*Not affiliated with the Radio City Music Hall*" [Game text via wiki] (https://battlebears.fandom.com/wiki/Rockette_Launcher).
- **Status:** Price history 200,000 → 100,000 → 110,000 J. It is the "third retexture" in the Bearzooka line [Fan-wiki].
- **Look:**
  - A rough stone tube: pale grey-green stone (about #AAA593 / #8F9081) in the middle, lavender/purple flagstone ends (about #665E74) and copper-brown bands (about #6F4421) that are rope bindings in the concept.
  - A stone grip wrapped in rope.
  - Sources: [Observed [W]/Photo_19-04-13_12_02_24_PM.png, [W]/Rockette_Launcher_concept.png, [W4]/ile:BBRWEAPONS.png; sprite tile "rol"]. About 0.7x [Inference].
- **Firing:**
  - Stats: hybrid; "very fast projectiles that arc over long distances"; rate of fire 0.3 s, ammo 3, 1,300 u/s [Fan-wiki].
  - Conflicts within the page: reload is 4.0 s in the infobox vs "a moderate 3 second reload" in the text; damage is 10–25 (+30 on a direct hit) in the infobox vs "a minimum of 15 to a semi-maximum of 30" in the text [Fan-wiki].
  - The Apr 2013 HUD reads 2/2 [Observed 5u0X3LDgwWM].
- **Projectile:** **A grey-blue faceted rock** flying against a sandy sky (5u0X3LDgwWM hq3, about 16.5 s) [Observed].
- **Impact / end result:**
  - A small AoE plus extra damage on direct hits [Fan-wiki].
  - The rocks "remain intact as a physical object for several seconds, rolling around the floor or remaining completely still", and sometimes "physically push or propel other players, even teammates" [Fan-wiki].
  - A yellow-white glow at the frame edge in hqdefault [Observed; attribution Unverified].
- **Images viewed:** [W]/Photo_19-04-13_12_02_24_PM.png; [W]/Rockette_Launcher_concept.png; [W4]/ile:BBRWEAPONS.png; https://i.ytimg.com/vi/5u0X3LDgwWM/{hqdefault,hq1,hq2,hq3}.jpg; [R]/yt_fx_zoom.png.
- **Depiction for shorts:** Rapid lobbed grey-blue rocks (observed) that pop on landing, then bounce, roll or lie still and nudge bystanders (documented). The colour of the dust puff is a [BBG News invention].
- **Confidence:** observed.

## Steamshot (secondary; BBR v1.3.1 week 1, 2012; 30 Gas)
- **Official text:** "Steam power the demise of your enemies and look dapper while doing it. The gentleman's weapon, for a man who knows taste and isn't afraid to melt a face." [Game text via wiki] (https://battlebears.fandom.com/wiki/Steamshot).
- **Status:** Originally 20 Gas; once sold for 1 Joule. The class changelog also lists it under BBR v1.0, which contradicts the 1.3.1 release [Fan-wiki].
- **Look:**
  - A brass/gold steampunk shotgun (about #935B26 to #B1803C) with a **green glass chamber dome** (about #5E7F28, highlight about #C4CD7A) in a brass cage.
  - Copper stacks topped with green gems (three in the concept, two visible in the 2014 key art) and black-and-gold engraved housing.
  - The barrel is perforated silver in the concept and a coil spring in the key art.
  - **The muzzle is a gold disc with six round holes in the key art, and yellow honeycomb pads in the in-game photo.**
  - A segmented grey hose curls under it to a wooden stock piece.
  - Sources: [Observed [W]/Steamshot_concept.png, [W]/Photo_19-04-13_12_02_21_PM.png, [R]/img/Steamshot.png (store, Oct 2012), [R]/img/Oliver_overhaul.png; sprite tile "sts"]. About 0.55–0.7x [Inference].
- **Firing:** Damage 35, rate of fire 1.5 s, ammo 3, reload 5 s [Fan-wiki]. The Apr 2013 HUD reads x/3 [Observed F2rsMmK6K68].
- **Projectile:** "When activated, it releases a quick spread of damaging green steam." [Fan-wiki]. No green steam is visible in the frames I opened [Observed absence].
- **Impact / end result:**
  - In the Apr 2013 demo, hit targets throw off white puff clouds plus a spray of small pink-red flecks (F2rsMmK6K68 hq1 about 9 s, hq2 about 18.5 s) [Observed]. Crediting these to the Steamshot is an [Inference].
  - **Correction:** the green wisps in SkyVu's Overhaul thumbnail (sd2) were credited to the Steamshot before. The HUD icon in that frame is the Spreadshot's [Observed], so that attribution is withdrawn.
- **Images viewed:** [W]/Steamshot_concept.png; [W]/Photo_19-04-13_12_02_21_PM.png; [W4]/ile:BBRWEAPONS.png; [R]/img/Steamshot.png; [R]/img/Oliver_overhaul.png; [R]/img/Oliver-steamshot.png (2D art of an older green-harness Oliver with a brass gun; origin unknown); https://i.ytimg.com/vi/F2rsMmK6K68/{hqdefault,hq1,hq2,hq3}.jpg; [R]/yt_fx_zoom.png.
- **Depiction for shorts:** A short hissing cone of steam from the six-hole muzzle. Its colour is open: green per the wiki [Fan-wiki], white in the 2013 frames [Observed], so a pale green-white mix is a reasonable compromise [Inference]. The target goes sooty and steaming rather than "melt a face" (a [BBG News invention], kept 13+).
- **Confidence:** partial.

## Sake Bomb (secondary; BBR v1.3.2, 2012; 50,000 Joules; reworked "much later")
- **Official text:** "A shot from this will make you wine and stumble." [Game text via wiki] (https://battlebears.fandom.com/wiki/Sake_Bomb).
- **Status:** Originally 90,000 J; once 1 Joule, and briefly free to new players. The effect originally also reversed the victim's aiming; "This was eliminated in a much later update" (no date given) [Fan-wiki].
- **Look:**
  - A squat dark-brown/maroon sake jug (about #4C221B) painted with a **Daruma face**: a cream-white face (about #FDDFA6), heavy black brows and moustache swirls, and round staring eyes.
  - Red-orange maple-leaf/flame motifs (about #CD251F / #DC8E4B), a red kanji-style emblem in a circle, a corked neck and a **looped tan rope handle** (about #B37955).
  - Sources: [Observed [W]/SAKEBOMB.png, [W]/Sake_Bomb_Concept.png (caption "Oliver's Sake Bomb (Secondary)"), [W4]/1.3.2WEAPONS.png, [R]/img/Oliver_overhaul.png]. "The face on the Weapon is a Daruma." [Fan-wiki].
  - In the Oct 2012 store he holds it up one-handed with the jug's open mouth toward the camera, wearing a white skin with red circuit lines [Observed [R]/img/Sake.png]. About 0.3x (head-sized) [Inference].
- **Firing:**
  - Type "Secondary - Saboteur"; it "fires non-damaging projectiles in an arc". Rate of fire 1 s, ammo 4, reload 3 s, 1,000 u/s; the exact AoE is unknown [Fan-wiki].
  - The store's stat labels read "DURATION / AMMO / RELOAD" [Observed [R]/img/Sake.png].
- **Projectile:** Undocumented [Unverified].
- **Impact / end result:**
  - Everyone in the small AoE, including the user, gets "a control reversal for 4 seconds" [Fan-wiki].
  - Status visuals: "a green question mark will appear over the player's head"; forward moves backward and left moves right. "background music will be disabled and other sounds will feature an mild echo" [Fan-wiki, Status Effects].
  - "The Sake Bomb is the Soldier's only weapon that cannot damage opponents." [Fan-wiki].
- **Images viewed:** [W]/SAKEBOMB.png; [W]/Sake_Bomb_Concept.png; [W4]/1.3.2WEAPONS.png; [R]/img/Sake.png; [R]/img/Oliver_overhaul.png.
- **Depiction for shorts:** A green "?" pops over the victim, who walks the wrong way for a 4-second beat while the music drops out (all documented). The jug's contents bursting into a pale mist cloud is a [BBG News invention].
- **Confidence:** partial.

## Solar Wind Scar (secondary; BBG v2.11, Aug 27, 2014; Gas item)
- **Official text:** "Cut a star in half and imbued it with power. It's said that even standing in it wake will singe the flesh." [Game text via wiki] (https://battlebears.fandom.com/wiki/Solar_Wind_Scar).
- **Status:** Price conflict: 60 Gas in the infobox vs 75 Gas in the /Weapons table and changelog. Planned "Incoming stats" were damage 70, duration 5 s, 900 u/s and radiation 60/s; whether they shipped is [Unverified] [Fan-wiki].
- **Look:**
  - **A long, broad, single-edged silver blade** with a slight curve and a jagged back edge near the tip.
  - A gold/orange guard crackling with yellow sparks, and an orange-and-black grip.
  - Held upright in both hands. The blade rises well above Oliver's head (about 1.2–1.5x in the item photo, exaggerated by the low camera).
  - Sources: [Observed [W]/Solar.png (File:Solar.jpg, Oct 31, 2014); sprite tile "sws"; scale is Inference].
- **Firing:** Type "Secondary - Radiation Explosives"; damage 45.0, radiation 70 per second, duration 4.0 s, ammo 1, reload 4.0 s, 1,000 u/s [Fan-wiki].
- **Projectile:** "Solar Wind Scar creates an orange slash, that travels in a straight direction. It will travel through walls" [Fan-wiki]. Not observed: the wiki's video "Solar wind scar gameplay" (tarKiQU1n1I, Sep 2014) returns no thumbnails [Unverified].
- **Impact / end result:**
  - "when it hits someone, a dark, circular radiation belt will spawn. Any enemy that enters the field will be irradiated, and receive physical damage." The user can irradiate himself [Fan-wiki].
  - Irradiated visuals: a yellow circle over the head that breaks into the radiation symbol in stages, plus Geiger clicks that speed up. At 100 RP the target explodes, with a blast radius of 150–200 units [Fan-wiki, Status Effects].
  - Lore: the wiki ties the text to Wil's BB Zero katana that "cut a star in half" [Fan-wiki].
- **Images viewed:** [W]/Solar.png; [D]/Hazard-0.png to Hazard-3.png (white line-art radiation icons); [R]/conc_tall.png.
- **Depiction for shorts:** A sword swing launches a flat orange crescent that passes through a wall and leaves a dark ring on the floor; anyone in the ring gets the yellow radiation icon and Geiger clicks (all documented). A heat shimmer on the ring is a [BBG News invention]. Show any 100-RP blast as a cartoon pop with confetti, never gore.
- **Confidence:** documented.

## B.E.A.R. Club (melee; default since BBR v1.0, 2011)
- **Official text:** "Basic" / "Elongated" / "Assault" / "Rod" / "?" [Game text via wiki] (https://battlebears.fandom.com/wiki/B.E.A.R._Club). This reads as an acrostic for B.E.A.R. [Inference].
- **Look:**
  - A **lime-green** (about #83AA32 to #9BBE45) cricket-bat blade with a column of round holes and a slot.
  - A grey lower section with a yellow/black hazard band, and a black grip with a yellow accent. The concept is titled "Standard Issue Bear C.L.U.B".
  - Sources: [Observed [W]/Photo_19-04-13_12_02_36_PM.png, [W]/BEARClubconcept.png; sprite tile "bc"]. Held upright; about 0.9x [Inference].
  - "looks like a cricket bat" [Fan-wiki].
- **Firing:** Melee, 70 damage, no stat modifiers. Melee+1/+2 adds +10/+20. It is the Tutorial melee [Fan-wiki].
- **Projectile:** None (melee).
- **Impact / end result:** No B.E.A.R. Club frame exists. Soldier melee hits show yellow cartoon stars (Krikkit demo) [Observed; applying that here is Inference]. Melee-kill barks include "Judo-super-karate!" [Fan-wiki, Soldier (BBG)].
- **Images viewed:** [W]/Photo_19-04-13_12_02_36_PM.png; [W]/BEARClubconcept.png; [R]/img/BBR_Kumakiri.jpg (store list icon).
- **Depiction for shorts:** A cricket-style swing with a burst of yellow stars (observed style). The cartoon "thwack" sound is a [BBG News invention].
- **Confidence:** partial.

## Krikkit Bat (melee; one of the original three, BBR v1.0; 30,000 Joules, level 11)
- **Official text:** "Authorized for use in Brockian Ultra-Cricket - Remember: The winning team shall be the first team that wins." [Game text via wiki] (https://battlebears.fandom.com/wiki/Krikkit_Bat).
- **Look:**
  - A white/silver sci-fi cricket bat (about #BBBFC2 / #DADADC) with **a glowing red light near the tip**, a thin blue circuit line, a small grille and a segmented black-grey grip.
  - Sources: [Observed [W]/KrikkitBatCR.png (held by Oliver in a white skin with red circuit lines), [W]/Krikkitbatconcept.png; sprite tile "kb"]. About 0.9x [Inference].
- **Firing:** Melee, 45 damage, +30% Special Speed. Price history 75,000 → 60,000 → 30,000 J [Fan-wiki].
- **Projectile:** None (melee).
- **Impact / end result:** **A burst of big yellow 5-point cartoon stars** at the point of contact (JFi380KnDUM hq1, about 6 s) [Observed].
- **Images viewed:** [W]/KrikkitBatCR.png; [W]/Krikkitbatconcept.png; https://i.ytimg.com/vi/JFi380KnDUM/{hqdefault,hq1,hq2,hq3}.jpg.
- **Depiction for shorts:** Swing, then yellow stars burst on contact (observed). A flare of the red tip light is a [BBG News invention].
- **Confidence:** observed.

## Queensbury Rules (melee; one of the original three, BBR v1.0; 30,000 Joules, level 2)
- **Official text:** "Suitable for use in winning reprieve from heavy English taxation as a scrappy underdog team in 1893 India." [Game text via wiki] (https://battlebears.fandom.com/wiki/Queensbury_Rules).
- **Look:**
  - A brown wooden cricket bat (about #6D4A18 / #845C26) with gold (about #C9B03E to #E8D23C) decoration: a handlebar moustache, a boxing fist, "QBR" lettering and two boxers.
  - Sources: [Observed [W]/Photo_19-04-13_12_02_56_PM.png, [W]/Queensburyrulesconcept.png; the concept's handwritten title appears to read "Queensbarry Rules"]. About 0.9x [Inference].
  - "the art on both sides of the bat resemble several elements of the sport" (boxing) [Fan-wiki].
- **Firing:** Melee, 45 damage, +15% Health. Originally 20,000 J [Fan-wiki].
- **Projectile:** None (melee).
- **Impact / end result:** Not shown; generic melee stars [Inference].
- **Images viewed:** [W]/Photo_19-04-13_12_02_56_PM.png; [W]/Queensburyrulesconcept.png.
- **Depiction for shorts:** A gentleman boxer's stance before the swing is a [BBG News invention]; yellow stars on the hit follow the observed style.
- **Confidence:** partial.

## Disciplinarian (melee; BBR v1.3.1 week 1, 2012)
- **Official text:** "Elbows on the table? That's a paddlin'. Skirt 6 inches above the knees? That's a paddlin'. Refusing a paddlin'? That's a paddlin'." [Game text via wiki] (https://battlebears.fandom.com/wiki/Disciplinarian).
- **Status:** Price conflict: 20 Gas with no level lock on the weapon page vs 60 Gas in the /Weapons table and changelog. The trivia also mentions 75,000 J and a 37,500 J sale price that stuck [Fan-wiki].
- **Look:**
  - An orange-yellow (about #F0B84D / #CA8E3E) bat with **ruler markings**: black numbers 1–6 and tick marks.
  - "the only bat where its two front faces are not identical, with one side resembling a short ruler and the other a traditional school teacher" [Fan-wiki].
  - The store list icon and the wiki sprite show a cream round face on a black panel on the orange bat [Observed, sprite tile "dsc"; [R]/img/BBR_Kumakiri.jpg list].
  - Sources: [Observed [W]/Photo_19-04-13_12_02_43_PM.png; [W4]/ile:BBRWEAPONS.png]. About 0.9x [Inference].
- **Firing:** Melee, 45 damage, +10% speed [Fan-wiki].
- **Projectile:** None (melee).
- **Impact / end result:** A swing into a green-skinned enemy throws a yellow spark burst, and the kill feed registers the kill (ku2RHse4lPA hq3, about 8 s) [Observed].
- **Images viewed:** [W]/Photo_19-04-13_12_02_43_PM.png; [W4]/ile:BBRWEAPONS.png; [R]/img/BBR_Kumakiri.jpg; https://i.ytimg.com/vi/ku2RHse4lPA/{hqdefault,hq1,hq2,hq3}.jpg.
- **Depiction for shorts:** Flip the bat to show the teacher face, then swat with a spark burst (the faces are documented, the spark is observed). The flip itself is a [BBG News invention].
- **Confidence:** observed.

## Kumakiri (melee; BBR v1.3.2, 2012; 75,000 Joules, level 30)
- **Official text:** "It's baaack!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Kumakiri). "The description refers to the Katana used by Oliver in Battle Bears -1" [Fan-wiki].
- **Look:**
  - **A long curved katana** with a wavy, jagged hamon pattern, a black square tsuba, a gold collar and pommel, and a black-and-gold wrapped hilt.
  - Sources: [Observed [W]/Kumakiri_Edit.png, [W]/Kumakiri_Concept_2.png (caption "Oliver's Kumakiri (Melee)"), [W4]/1.3.2WEAPONS.png, [R]/img/BBR_Kumakiri.jpg (store, Oct 2012), [R]/img/Kumakiri_another.jpg (May 2013 loadout, Sam-Are-I skin)].
  - The early concept was a straight katana [Observed [W]/Kumakiri_concept.png]. Held raised; about 0.9–1.0x [Inference].
- **Firing:**
  - Melee, 110 damage, -10% Health. The store panel reads "HEALTH -10%" [Observed [R]/img/BBR_Kumakiri.jpg].
  - "the highest level lock of all weapons" (30) [Fan-wiki].
  - "Unlike the Soldier's other melee weapons, it has a different animation which features a downward slash." [Fan-wiki].
- **Projectile:** None (melee).
- **Impact / end result:** Not shown; generic melee stars [Inference].
- **Era:** The BB-1 Katana was "forged from a plumbing pipe, using the intense energy of a Red Huggable's hug" [Fan-wiki, Katana]. BB-1 art shows Oliver slicing a red Huggable [Observed [W2]/ile:Sword.png].
- **Images viewed:** [W]/Kumakiri_Edit.png; [W]/Kumakiri_Concept_2.png; [W]/Kumakiri_concept.png; [W4]/1.3.2WEAPONS.png; [R]/img/BBR_Kumakiri.jpg; [R]/img/Kumakiri_another.jpg; [W2]/ile:Sword.png.
- **Depiction for shorts:** An overhead downward slash (documented) with yellow stars on the hit (observed style). A white arc smear trailing the blade is a [BBG News invention].
- **Confidence:** partial.

## Turkish SW Boots (shared Special, not a Soldier weapon; Tutorial item; named in SkyVu's 2026 Steam copy)
- **Official text:** "You want to jump? These allow it!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Turkish_SW_Boots). From Steam: "...those Turkish SW Boots..." [Canon].
- **Status:** 40 Gas, level 8; the Tutorial's Special. Before v2.0 the boots could not fire in mid-air; the recharge was 2.5 s before v2.6 and is 4.5 s now [Fan-wiki].
- **Look:**
  - In 2D promo art, Oliver wears chunky red boots with yellow studs that blast white smoke jets [Observed [W3]/ile:TurkishSWBoots.png].
  - The wiki's "Original Turkish SW Boots image" shows huge white jet plumes under an older Oliver with a blue headband and green harness [Observed [W3]/ile:Sw_boots.png].
  - The HUD and loadout icon is a pair of red-and-white boots [Observed [D]/Tutorial_BBG_.jpg, [R]/img/Kumakiri_another.jpg].
- **Firing / effect:** "a jump larger than that of the Pro-Mode Jump and can additionally be activated while airborne, allowing a chained double jump"; jump power 600 [Fan-wiki].
- **Projectile, impact / end result:** None.
- **Images viewed:** [W3]/ile:TurkishSWBoots.png; [W3]/ile:Sw_boots.png; [D]/Tutorial_BBG_.jpg; [R]/img/Kumakiri_another.jpg.
- **Depiction for shorts:** Twin white jet plumes on take-off, then a second puff for the mid-air double jump (observed in art and documented).
- **Confidence:** partial.

---

## Corrections for the character file (/home/user/thallo-site/bbg-news-repo/characters/oliver.md)
1. "The Bearzooka is drawn as a green, hazard-striped tube [Observed; Inference]."
   - **Correction:** The BBG Bearzooka is a coral-red hexagonal tube with glowing orange panels and grey hex collars, firing from the wide end [Observed]. That matches the wiki's "red and orange lines" [Fan-wiki].
   - The green, hazard-striped, "BEARZOOKA"-lettered tube is the BB Zombies (2009) design [Observed [W2]/ile:Bear.png; Fan-wiki].
2. Prompt pack: "He holds a chunky assault rifle and carries a green hazard-striped launcher tube on his back."
   - **Correction:** "He holds the A Salt Rifle, a sage-green rifle with salmon-pink panels and a white salt shaker mounted on top. He shoulders the Bearzooka, a coral-red hexagonal launcher tube with glowing orange panels." [Observed].
3. Prompt pack: "Green-and-dark-grey shoulder harness, small green backpack, no clothing."
   - **Correction:** For the BBG 2013 default model: a red headband, a crossed bandolier of brass cartridges on dark-red straps, red wristbands, red knee bands with silver-ringed red buttons and a pale grey-lavender backpack [Observed, in-game photos].
   - The green harness belongs only to older 2D art (File:Sw_boots.png, File:Oliver-steamshot.png) [Observed].
4. "A green-and-dark-grey harness with grey clips [Observed] and a small green backpack [Inference]." Same correction as item 3, labelled as BBG 2013 in-game evidence.
5. Video prompt starter: "...in a green-and-grey harness..." → replace with "...in a red headband and brass-bullet bandolier...".
6. Colours line, "the unsampled harness green #4E6B35, strap grey #3A3D40, clips #8E949A". For BBG framing, use the sampled gear colours instead: headband about #A2000D, cartridges about #E9D85A, straps about #7F000A, knee buttons about #900611 with rings about #B2BBC1, pack about #745F7E [Observed, sampled from [W]/Photo_19-04-13_12_02_36_PM.png].
7. Negative prompt: "...pants or shirts, blue headband, gold or engraved skin...". Remove "blue headband". 2013 BBG captures show a blue headband in many matches (probably the team colour [Inference]), and the BBH portrait headband is blue [Observed]. Instead, make red the default in the positive prompt.
8. "The gold trailer-card Oliver is likely a skin [Inference]."
   - **Correction:** It matches the Gold Oliver skin (Gold Bundle, BBR v1.4, 1,710 Gas [Fan-wiki]) [Observed match with File:Gold_Oliver.jpg].
   - In the trailer he holds a silver-grey gun with a black loop (38.25–41.25 s), possibly the Sci-Fi HASR [Inference].
9. "He also has an improvised katana [Canon, channel unconfirmed]". Add the era: that is the BB-1 (2010) Katana. The BBG equivalent is the Kumakiri melee (BBR v1.3.2, level 30), whose text "It's baaack!" refers to it [Fan-wiki].
10. Skins list. Optional additions:
    - Sam-Are-I appears in SkyVu's Jul 6, 2026 Steam banner holding the Sci-Fi ASR [Observed].
    - Night Bear (v2.12, 75 Gas [Fan-wiki]) is the skin shown in the 2026 playtest loadout menu (fan footage) [Observed].
11. Comedy beat 1, "Bearzooka recoil blasts him through a wall". No recoil is documented. The canon hook is his own blast radius ("easy to kill yourself with it") [Game text via wiki], so re-ground the gag in the self-blast; it remains a [BBG News invention].

Also outside the soul: /home/user/thallo-site/research_notes/Battle Bears character lore/animation_reference.md line 116 ("A green launcher tube with yellow/black hazard stripes. [INFERENCE] This is probably the Bearzooka"). It probably is a Bearzooka, but the BB Zombies/BB-1 design, not the BBG one.

## Corrections to the previous inventory
- **Spreadshot.** The six-hex-tube ring is the muzzle, not the "rear". The shipped model shares the Steamshot silhouette [Observed sprite tiles and store shot; Inference].
- **Steamshot.** The green wisps in the Overhaul sd2 thumbnail were credited to the Steamshot. That frame's HUD shows the Spreadshot icon at 2/3 [Observed], so the attribution is withdrawn.
- **Urine Trouble.** The stream is now firmly observed in File:Urine trouble range.jpeg, May 2013. Previously it rested on one low-confidence streak.
- **Sci-Fi HASR price.** The Apr 2013 store shows 85 Gas [Observed].
- **O.C.O. Gauntlet price.** The Oct 2012 store tile shows 20 Gas and the Apr 2013 store shows 45,000 J [Observed].
- **HASR.** SkyVu's Apr 2014 Overhaul video shows the HASR icon at x/30 (exact frame 68.966 s) [Observed].
- **Soaker.** It shows x/60 in Apr 2013 and x/70 in a May 2014 clip [Observed].
- **Bearzooka concept.** The checkered flared end is most likely the muzzle, not the rear, by the TNT muzzle-flash evidence [Observed + Inference].
- **Minigun.** File:Minigun.jpg is not the Soldier gun [Observed].
- **2013 era label.** The April 2013 demos and photos are late BBR, not BBG [Fan-wiki dates].

## Wiki conflicts (unchanged, now with in-game checks)
- **Prices**, infobox vs /Weapons table and changelog: Urine Trouble 60 vs 75 Gas; Sci-Fi HASR 60 vs 85 (85 observed in 2013); Acreambo 60 vs 75; Solar Wind Scar 60 vs 75; Disciplinarian 20 vs 60 Gas.
- **Bearzooka ammo:** "two shots" in the text vs 1 in the infobox (1 observed in 2013).
- **Rockette:** reload 4.0 vs 3 s and damage 10–25 vs 15–30, within the same page.
- **2013 HUD ammo counts vs infoboxes:** Sci-Fi ASR 30 vs 25, Spreadshot 4 vs 6, Rockette 2 vs 3, O.C.O. 2 vs 1.
- **Class changelog errors:** it puts the Steamshot in BBR v1.0, lists the B.E.A.R. Club twice and omits the TNT Launcher.
- **HASR text vs stats:** the text says "lower damage", but its damage of 8 is higher than the ASR's 6.

## Open questions
- What do the rifles' projectiles look like in flight? This covers the ASR, HASR, Soaker, both Sci-Fi rifles and the Minigun, plus the Acreambo "toothpaste". It needs gameplay video; the Soldier chapter of the 2026 showcase (4:35–8:50) is the best lead.
- What do the Bearzooka rocket and its explosion look like, and the TNT, Sake Bomb and Solar Wind Scar projectiles? No frame shows them.
- Is the Steamshot's steam green (wiki) or white (2013 frames)? And what are the green wisps and magenta crackle in SkyVu's 2014 Overhaul frames, which were taken with the Spreadshot equipped?
- What exactly did the Apr 2014 Oliver Overhaul change, and in which build? The frames show HASR x/30, Spreadshot x/3 and an unidentified 8-round weapon. SkyVu's 2.6 change log and the forum balance notes are blocked here.
- Is the 2026 trailer's silver gun with the black loop the Sci-Fi HASR? Do the 2026 prices and stats differ from the wiki?
- What does a defeated bear look like on screen in BBG, given the glow blobs seen after kills?
- Does the 2026 "EFFECT & TEXTURE IMPROVEMENTS" build change these effects?