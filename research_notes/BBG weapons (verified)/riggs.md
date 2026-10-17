# Riggs (Heavy): BBG weapons dossier (verified and edited)

Riggs is the Heavy in Battle Bears Gold (BBG). Steam's 2026 store text lists "-HEAVY: Riggs" [Canon] (https://store.steampowered.com/api/appdetails?appids=4408320, re-fetched 2026-10-17; release date "Nov 4, 2026"). The wiki quotes the in-game class blurb as: "Riggs the heavy is built like a tank, and moves like a stone. Keep clear of wide open spaces as his primary weapons have poor accuracy! Your melee attack is devastating!" [Game text via wiki] (Template:Class:Heavy (BBG)).

The BBG arsenal has 20 items: 8 primaries, 6 secondaries and 6 melees [Fan-wiki] (https://battlebears.fandom.com/wiki/Heavy_(BBG)).
- **Original BBR (2012) kit**, per the class page's first revision (2012-02-03): Beebeegun, Electric Honey and Zombee Gun; Hivey League, Buzz Kill and Sucker Punch; Barbed Gloves, Huggable Gloves and Zombee Gloves [Fan-wiki].
- **Later additions** (all dates [Fan-wiki], from the Updates and version pages):

| Update | Date | New Heavy items |
|---|---|---|
| BBR 1.3.1 | Jun 28, 2012 (rolled out over 4 weeks) | Provolowned, Field Medic, Plasma Orb, Catastrophe |
| BBR 1.3.2 | Aug 24, 2012 | Big Iron, Mother of Nature, Blood Spurt |
| BBG 2.11 | Aug 27, 2014 | Sword and Stone |
| BBG 2.12 | Oct 2, 2014 | Freeze Blast |
| BBG 2.14 | Nov 29, 2014 | Flame Thrower |
| BBG 2.19 | Apr 26, 2015 | Bounce Lazer |

Steam's 2026 text gives only totals ("80+ PRIMARY WEAPONS 60+ SECONDARY WEAPONS 50+ MELEES") [Canon]. There is no official 2026 per-class list.

### What changed in this verification pass
1. **The Steam store trailer is 2013 footage, not 2026 gameplay.**
   - I matched thumbnails of SkyVu's YouTube video rfAyqVJrli4, "BATTLE BEARS GOLD Trailer: Award-Winning Multiplayer Shooter Game" (channel "BATTLE BEARS", via oEmbed), against my own 10 fps frames of the Steam trailer.
   - Matches: hq1 → 11.9 s, hq3 → 42.8 s, maxres → 29.9 s, hqdefault → 29.9 s. Pixel MSE was 20–35, against a median of about 7,000–7,900 [Observed, pixel comparison].
   - Steam screenshot screen_00 is the trailer frame at 36.4 s (MSE 223 against a median of 10,162).
   - So the Steam trailer re-edits the 2013 launch trailer [Inference, strong]. Electric Honey and Blood Spurt appear in that footage; this does **not** show they are in the 2026 build.
2. **New 2026 evidence:** SkyVu's Jul 6, 2026 Steam "CLOSED TESTING" announcement banner shows Riggs holding the **Beebeegun** [Observed].
3. **Wrong identification fixed:** the 2012 BBR trailer frame 0gYEZCMQfmA/hq3 shows the **Hivey League**, not the Beebeegun.
4. **Wrong file names fixed:** File:Laser_(2).PNG and File:FlameThrower_(2).png. The names "Laser_2.PNG" and "FlameThrower_2.png" do not exist.
5. **Labels fixed:**
   - Beebeegun "no splash" is now [Inference].
   - The battlebears.com hero text is tied to BB Heroes only by [Inference].
   - The Riggs Overhaul thumbnails' 2014 date is [Inference].
   - The Beebeegun concept caption is attributed to the right file.
6. **Mother of Nature:** the big skull-flask shape in the Overhaul hq2 thumbnail is re-read.
7. **Sucker Punch:** the head has two ears, not one.
8. **Blood Spurt:** the "white flash" frame is the punch pose redrawn as line art, which points to an edit transition.
9. **Era fix:** BBU/BBO dates corrected.
10. **Cross-dossier conflicts** are listed near the end.

### Sources reached today (2026-10-17)
- **Fan wiki (MediaWiki API):**
  - all 20 weapon pages
  - Heavy (BBG), Heavy (BBG)/Weapons (empty) and Template:Class:Heavy (BBG)
  - Status Effects, Updates, Battle Bears Gold/Versions/2.6, Rocky Horror, The Incredible Riggs, Riggs, Riggs (Hero), Laser, Battle Bears Overclock and Battle Bears Heroes
  - video-file metadata for the two fan videos
- **Wiki images:** 80 File: images downloaded and opened by me.
- **Official sources:**
  - battlebears.com/pages/characters (live, HTTP 200)
  - Steam appdetails API
  - Steam news API for app 4408320, plus its four announcement banners
- **Local trailer:** trailer.mp4, re-extracted at 10 fps for 33.5–38.6 s, plus a full 10 fps low-res set for matching.
- **YouTube thumbnails** (maxres, hqdefault, hq1–hq3) for xp5B76ExuAI, 0gYEZCMQfmA, rfAyqVJrli4, dhQaJKzwgAg, qdzWcRJG8KI, -lAtv-j9Sms and 4A3sWm3hhso, with titles and channels via oEmbed.

### Not reachable
- **web.archive.org:** curl connections fail (HTTP 000). archive.org/wayback/available returns no snapshot for battlebears.com/battle-bears-gold-2-6-change-log/. SkyVu's 2.6 changelog therefore stays unread, and every stat history below is [Fan-wiki].
- **YouTube watch pages:** they redirect to Google's "sorry" page, through both curl and WebFetch.
- **I watched no video.** Video evidence is thumbnails plus the local Steam trailer.

### Conventions
- **Evidence folder:** /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/
  - Wiki image File:X is saved as png/X.png in that folder; characters such as ( ) ' & become _.
  - My trailer frames are in tr/f_NNN.jpg, where f_NNN sits at 33.5 s + (NNN−1) × 0.1 s.
- **Hex codes** are approximate samples (median or dominant colour), not official codes [Observed, sampled]. I re-sampled these myself:
  - Beebeegun 2013 and 2026
  - Electric Honey 2013-trailer footage
  - Bounce Lazer, Flame Thrower can, Sucker Punch head and Big Iron
  - Rocky Horror and Riggs's fur

  The other hex codes are the first researcher's samples. I checked them against the images by eye.
- **Sizes** are fractions of Riggs's standing height in the gear-up screenshots [Observed, approximate]. They are converted with the BBG News scale chart (Riggs ≈ 1.2× Oliver) [BBG News invention].

### Shared visual language
- **Heavy guns** are oversized boxy miniguns, shotguns and launchers, held low at the hip [Observed]. Most carry a themed topper [Observed]:
  - a hive on the Beebeegun, Electric Honey, Hivey League and Buzz Kill
  - a cheese lump on the Provolowned
  - a Huggable on the Field Medic and Zombee Gun, and a Huggable head on the Sucker Punch
  - a plasma globe on the Plasma Orb
  - a red can on the Flame Thrower
- **Exceptions:**
  - Big Iron is a plain revolver.
  - Freeze Blast has only a small orange cap.
  - Bounce Lazer's Huggable head hangs below the grip as a pommel.
  - Mother of Nature is a vine-bound log [Observed].
- **Shared meshes:**
  - Beebeegun and Electric Honey are one mesh, recoloured [Observed].
  - Field Medic and Zombee Gun are one stubby mesh [Observed], matching the wiki's "retexture of the Zombee Gun" [Fan-wiki].
  - Hivey League and Buzz Kill share a body and hive but have different muzzles [Observed].
  - Barbed, Huggable and Zombee Gloves are one creature-mitt mesh, recoloured [Observed].
  - The wiki calls the Provolowned "a re-texture of the Beebeegun" [Fan-wiki], but the images show a clearly different cheese-and-grater model [Observed]. The phrase probably refers to shared minigun mechanics [Inference].
- **Default 3D Riggs in the 2013–2015 gear-up screenshots** [Observed, sampled; e.g. File:Big_Iron.jpg, File:BuzzKill.jpg]:
  - pale blue-grey fur (lit ≈ #8898A8–#8EAAB3)
  - a red segmented helmet with the grey ear tips showing
  - a red chest harness with a round red medallion ringed in yellow-green
  - red forearm and shin bands, and a red round backpack
- **Team colour:**
  - Official BBR-era renders and the 2012 SkyVu trailer show the same gear in blue [Observed: File:Heavy.png, File:Heavy_Class.jpg, https://i.ytimg.com/vi/0gYEZCMQfmA/hq1.jpg].
  - The Rocky Horror concept File:Rocky.png shows one red and one blue rock version [Observed]. The wiki says the skin is "team coloured rock" [Fan-wiki].
  - So gear colour is probably team colour [Inference].
- **Rocky Horror skin** (in the trailer and Steam screen_00):
  - red cracked rock with near-black cracks, red eyes and a black round back-shield [Observed]
  - it samples from #952522 (screen_00) to #AE3526 (lit chest, trailer 34.8 s), rust-red to brick-red
  - the wiki has it as "a rock monster-like Riggs… cracked fragments of team coloured rock", 250 Gas, released BBR 1.3.1 week 4 [Fan-wiki]
  - the 2012 skin menu shows "BUY NOW 400" [Observed: File:Rocky-front.png], so it originally cost 400 Gas
- **Riggs in the 2026 banner:** pale blue-grey fur (#96BBC2) and a ragged maroon jacket with white fur trim [Observed]. The skin's name is [Unverified].

---

## Beebeegun (primary; default since BBR 2012; rebalanced BBG 2.6, Dec 20 2013; shown in official Jul 2026 Steam art; 2026 build unverified)
- **Official text:**
  - BBG item text: "Artificially accelerated and naturally angry bees. Also the bees are fired backwards. And their stingers are infused with adamantium." [Game text via wiki] (https://battlebears.fandom.com/wiki/Beebeegun)
  - battlebears.com: "Wielding his "Beebee gun," he excels in close combat, delivering a burst of shells that unleash severe damage when focused on a single target, proving lethal at short distances." [Canon] (https://battlebears.com/pages/characters, re-fetched today)
  - That page never names Battle Bears Heroes; it says "Let's dive into the first batch of heroes!" Tying the quote to BB Heroes (BBH) is [Inference]. It is a strong one: the page talks of an "Ultimate", and the wiki's BBH table lists Riggs's attack as "Beebee Gun", his Ultimate as "He can fly now?", damage "5 x 306" and "May 2023" [Fan-wiki].
  - It describes a burst of shells, not the BBG minigun stream [Inference]. Do not mix the two.
- **Status and history:**
  - The first page revision (2012-03-26) reads "default heavy machine gun. moderate damage. has long continous fire" [Fan-wiki, early].
  - Default price, level 1 [Fan-wiki].
  - The BBG 2.6 page lists "Damage increased from 7 to 6" (sic), clip 160→150, reload 3→4.5 and dispersion 0.05→0.07 [Fan-wiki]. These conflict with the current infobox (100 ammo, 4 s, 0.08).
  - A fan video (TPLK1ng, "Battle Bears Gold gameplay!", 4A3sWm3hhso) has a HUD minigun icon with a gold top and "160 / 160" ammo [Observed: https://i.ytimg.com/vi/4A3sWm3hhso/hq1.jpg; crop /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/crops/tplk_hud.png]. That this is the pre-2.6 160-round Beebeegun is [Inference].
  - **2026:** SkyVu's Steam announcement "First BATTLE BEARS GOLD Playtest This Thursday!" (2026-07-06, Steam news API for app 4408320) carries a "CLOSED TESTING" banner. In it, Riggs, the pale blue-grey Heavy, holds this gun [Observed; identification by matching the 2012/2013 model, Inference, strong]. Whether the gun ships in the Nov 2026 build, and whether the render is new, are [Unverified].
- **Look:**
  - **2012–2013** [Observed: File:Photo_19-04-13_12_50_44_PM.png (2013 gear-up), File:Beebee.png (2012 gear screen, Riggs in a brown skin with a red suit)]:
    - Body: a long, faceted, charcoal-black boxy minigun (#2A2A2A, dominant #282828) with a long octagonal barrel shroud.
    - Sides: glowing amber slatted panels (#E0AA44).
    - Topper: a faceted gold hive (#C5A533; 2012 #D3B74A) near the rear. A bent yellow-and-black striped tube, like a bee's abdomen, runs from the hive.
    - Bees: tiny white-winged cartoon bees sit on and beside the hive. These are the wiki's "small bees circling its hive" [Fan-wiki].
    - Held low at the right hip, barrel angled down and forward.
    - Length ≈ 0.7× Riggs ≈ 0.85× Oliver.
  - **2026 banner** [Observed: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/steam/banner_jul6.png; crop /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/crops/banner_riggs_gun.png; side-by-side /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/sheets/bee_cmp.png]:
    - The same layout: a black boxy body (#323232) and a long octagonal shroud ending in a flat octagonal muzzle.
    - The slat windows are rows of glowing candy-striped orange-and-yellow cylinders (#C7701C, highlights #E8B808).
    - The bent tube has a yellow-orange zigzag stripe.
    - The hive is a rounded, banded orange-gold dome (#B27820), not the faceted 2013 hive, with a small yellow-black, white-winged cartoon bee on it.
    - Held across the body in both hands.
- **Concept lineage:**
  - File:Beebeegun_original_concept.jpg is a grey sketch labelled "Riggs: Plasma Globe Glob Launcher", showing a three-barrel gun with a plasma globe and red recoil arrows [Observed].
  - In the Heavy (BBG) gallery its caption reads "This weapon is what the Heavy is holding in the main cast lineup. It is a hybrid of two successful concepts, which are today know as the Beebeegun and Plasma Orb." [Fan-wiki]
  - The 2D lineup art (File:Riggs-heavy.png, File:Heavy.jpg, File:RIGGS.jpg) shows that hybrid: a black triple-barrel gun with yellow striped accents and a pink plasma globe [Observed].
- **Firing:**
  - Automatic minigun with "Wind Up" and "Wind Down" barrel spin (wind-up value 375, wind-down 450, max rotation 3000).
  - 0.1 s per shot, 5.5 damage, 100 ammo, 4 s reload, dispersion 0.08, +10% Health.
  - All of the above [Fan-wiki]. Hitscan per "Automatics, shotguns, and others use hitscans" [Fan-wiki, Weapon Statistics].
  - Muzzle flash and sound are undocumented [Unverified].
- **Projectile:**
  - The item text says angry bees fired backwards [Game text via wiki].
  - No image of Beebeegun fire was found [Unverified].
  - The same mesh, recoloured as Electric Honey, draws a straight streak in the 2013 trailer footage. Transferring that look is [Inference].
- **Impact / end result:** the wiki gives no splash or status effect for it. "No splash, no status" is [Inference] from its "Automatic" type and the hitscan rule. The hit visual is [Unverified].
- **Images viewed:**
  - File:Photo_19-04-13_12_50_44_PM.png, File:Beebee.png, File:Beebeegun_original_concept.jpg, File:Riggs-heavy.png, File:Heavy.jpg, File:RIGGS.jpg
  - the Steam banner https://clan.akamai.steamstatic.com/images/46006015/3b7f9b97cdb4f799bbc696475d327f4d7c7a9523.png (saved as steam/banner_jul6.png)
  - https://i.ytimg.com/vi/4A3sWm3hhso/hq1.jpg, hq2.jpg, hq3.jpg
  - crops bee13_gun.png, bee12_gun.png and banner_riggs_gun.png, all in /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/crops/
- **Depiction for shorts:** use the 2026-banner look: candy-striped orange slats, a banded gold hive with a little bee. The barrels spin up with a whine, then a straight tracer stream fires, peppered with tiny tail-first cartoon bees. Small yellow "sting" sparks pop on the target, with no explosion [BBG News invention, modelled on the Electric Honey footage].
- **Confidence:** partial (look observed, including 2026 official art; firing and impact unseen).

## Provolowned (primary; BBR 1.3.1 week 1, Jun–Jul 2012; changed in BBR 1.4.2 and BBG 2.6; 2026 unverified)
- **Official text:** "The list of dangers associated with over consumption of cheese just got a little bit longer. Four cheese blend your opponents into a quivering mass of curdled shame!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Provolowned)
- **Status and history:**
  - 50 Gas, level 1. Forum Appreciation members got it free and early.
  - BBR 1.4.2 (Feb 28, 2013): 120,000 Joules → 100 Gas; damage 9.0→9.5; dispersion 0.08→0.07.
  - BBG 2.6: damage 9.5→8.5, clip 100→80, reload 4.5→5.
  - All [Fan-wiki]. 2026 [Unverified].
- **Look** [Observed: File:Provolowned.png (render with the BATTLE BEARS logo; official provenance Unverified), File:Gnifle-heavy-setup.png (2012 gear, Teen Wolf skin), File:BBRWEAPONS.png ("BBR 1.3.1 and BEYOND!" promo), File:Provolowned-navi-icon.png]:
  - Body: a pale-yellow cheese block (#FDDEA9 / #EFC18E) flecked with red-brown and black specks, tied with brown twine.
  - Handle and stock: a bent orange crust- or rind-like tube on top at the rear, an orange vertical grip, and an orange-red rind stock.
  - Barrel: a silver box-grater block (#C3C3C3, shade #737373) with rows of slots along the sides and round holes on the end face.
  - Top: a white rounded lump tied with twine, plus an angled silver plate.
  - Held at the hip. Length ≈ 0.5–0.6× Riggs ≈ 0.65× Oliver.
  - It is a different mesh from the Beebeegun, despite the wiki's "re-texture" wording [Observed vs Fan-wiki].
- **Firing:**
  - Automatic minigun with a notably long wind-up. 7.5 damage, cooldown 0.126, 100 ammo, 5 s reload, dispersion 0.08. Hitscan.
  - All [Fan-wiki].
  - The cosmetic "small flies circling its circular cheese" [Fan-wiki] is not visible in the stills [Unverified].
- **Projectile:** undocumented [Unverified]. The item text implies cheese ("Four cheese blend") [Inference].
- **Impact:** unknown [Unverified].
- **Images viewed:** File:Provolowned.png, File:Gnifle-heavy-setup.png, File:BBRWEAPONS.png, File:Provolowned-navi-icon.png.
- **Depiction for shorts:** a slow comedic wind-up, then a spray of shredded-cheese flecks from the grater muzzle. The target ends up coated in grated cheese, with two cartoon flies buzzing around [BBG News invention].
- **Confidence:** partial.

## Field Medic (primary; BBR 1.3.1 week 4, Jul 2012; health penalty changed in BBG 2.6; 2026 unverified)
- **Official text:** "You ever wonder where the military stores all of its amputated limbs? Wonder no longer! Covering your head and fleeing is probably the best thing to do now." [Game text via wiki] (https://battlebears.fandom.com/wiki/Field_Medic)
- **Status and history:**
  - 60 Gas, level 1 [Fan-wiki].
  - The 2012 gear screen shows "HEALTH -8%" [Observed: File:Field_medic.png], and the wiki says the 8% reduction was removed in 2.6 [Fan-wiki]. The current infobox still lists −10% Health / 20% Speed [Fan-wiki conflict].
  - The 2.6 entries "damage 19→15, cooldown 0.4→2" do not fit an automatic [Fan-wiki conflict].
- **Look** [Observed: File:Photo_19-04-13_12_50_38_PM.png (2013), File:Field_medic.png (2012), File:BBRWEAPONS.png]:
  - A short, stubby rotary gun on the same mesh as the Zombee Gun.
  - Centre: a cardboard shipping-box section (#D7CAB4 lit, #73665D shade).
  - Front: a black-and-silver ribbed hexagonal housing ending in a silver hexagonal muzzle plate with six bores ringed around a centre bolt. Rear: a black ribbed tube.
  - Topper: a teal Huggable (#106A7B) with a white grin and small fins, wearing an olive-drab army helmet.
  - The 2013 shot has white four-point sparkles by the muzzle. Whether they are a game effect or a menu highlight is [Unverified].
  - Length ≈ 0.45–0.5× Riggs ≈ 0.6× Oliver. In 2012 it is held one-handed and raised.
- **Firing:**
  - Automatic, 6.4 damage, 0.1 s, 40 ammo, 3.5 s reload, 850-unit range [Fan-wiki].
  - The wiki says it "fires a continuous stream of amputated limbs" [Fan-wiki].
  - Fan footage [Observed: https://i.ytimg.com/vi/qdzWcRJG8KI/hq2.jpg and hq3.jpg (bearpantsbb, published 2020-05-03 per wiki video metadata); crop /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/crops/fm_hq3.png]:
    - a black-skinned Riggs fires with the teal helmeted Huggable visible on the gun
    - a large pale-yellow and cream spiky muzzle-flash cone
  - The uploader's description lists "Set used - Field Medic / Sucker Punch / Huggable Gloves / Turkish SW Boots / Ammo 2 / Speed 2" [fan text, via wiki video metadata]. The same description mentions "BBO Offensive Playstyle", but the items are BBG items [Inference].
  - The HUD reads "18 / 50" and "25 / 50", which is consistent with 40 base ammo plus Ammo 2 [Inference].
- **Projectile:** a spray of small tumbling dark olive-green and tan chunks, plus white bone-like bits, flies toward the target [Observed, low-res]. Reading them as "limbs" is [Fan-wiki / Inference].
- **Impact:** the chunks burst against a red-armoured player amid yellow-white spark spikes. No blood is visible at thumbnail resolution [Observed, low-res]. The kill look is unknown.
- **Images viewed:**
  - File:Photo_19-04-13_12_50_38_PM.png, File:Field_medic.png, File:BBRWEAPONS.png
  - https://i.ytimg.com/vi/qdzWcRJG8KI/hq1.jpg, hq2.jpg, hq3.jpg, maxresdefault.jpg
  - crops fm_hq2.png and fm_hq3.png
- **Depiction for shorts:** the stubby tan-and-teal gun shudders and spits a cone of cream sparks full of plush stuffed arms and legs (seams and fluff, no blood). They bonk off the target and bounce on the floor [BBG News invention, built on the observed burst].
- **Confidence:** observed (low-res fan footage).

## Big Iron (primary; BBR 1.3.2, Aug 24 2012; changed in BBG 2.6; 2026 unverified)
- **Official text:** "That's a big gun you have there pardner." [Game text via wiki] (https://battlebears.fandom.com/wiki/Big_Iron)
- **Status and history:**
  - 60,000 Joules, level 15 [Fan-wiki].
  - The 1.3.2 notes read "New weapons for Soldier and Heavy classes" [Fan-wiki quoting update notes]. A promo banner reads "New Weapons: Soldier & Heavy Classes" [Observed: File:Update_1_3_2_coming_soon.jpeg].
  - "originally intended as a secondary weapon, but was switched with the Mother of Nature" [Fan-wiki].
  - 2.6 lists damage 25→30, reload 4→3 and projectile speed 1900→1800, against the current infobox's 50 damage and 2,000 u/s [Fan-wiki conflict].
  - The wiki says the name may reference the Marty Robbins song, whose outlaw had "20 notches on his revolver" [Fan-wiki].
- **Look** [Observed: File:Big_iron_poster.png, File:Big_Iron.jpg (2013 gear-up), File:Big_iron.png (2012), File:1.3.2WEAPONS.png]:
  - An oversized snub-barrel revolver in gunmetal (barrel ≈ #715D5E, frame ≈ #4E4D4F) with a darker cylinder.
  - Tally scratches on the barrel top: vertical strokes with diagonal slashes. Reading them as the song's "notches" is [Inference].
  - A dark red wooden grip with grain (#541613 / #872B26).
  - 2013: held two-handed at chest height. 2012: held one-handed toward the camera.
  - Length ≈ 0.5× Riggs ≈ 0.6× Oliver.
- **Firing:**
  - Semi-automatic, 0.5 s, 6 ammo, 3 s reload, 50 damage. Listed as "Explosives*" but "lacks any sort of AoE".
  - A real projectile at 2,000 u/s.
  - Bug: "the bullet doesn't actually appear unless fired from some distance away".
  - All [Fan-wiki].
- **Projectile:** the bullet's look is undocumented [Unverified].
- **Impact:** direct hit only, no splash [Fan-wiki]. The visual is unknown.
- **Images viewed:** File:Big_iron_poster.png, File:Big_Iron.jpg, File:Big_iron.png, File:1.3.2WEAPONS.png, File:Update_1_3_2_coming_soon.jpeg. File:Big_Iron_hacker.jpg shows a different, armoured character and was not used.
- **Depiction for shorts:** one booming shot with a big muzzle flash and a short bright streak. The target rocks back in a puff of sparks. Riggs blows on the barrel and scratches one more notch [BBG News invention].
- **Confidence:** partial.

## Electric Honey (BBG) (primary; original BBR 2012; changed in BBR 1.4.2 and BBG 2.6; shown in the Steam store trailer, which is 2013 footage; 2026 build unverified)
- **Official text:** "Electrically charged bees are slightly smaller* allowing for a higher bees-per-hive ratio and thus longer continuous fire!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Electric_Honey_(BBG))
- **Status and history:**
  - 10,000 Joules, level 2; originally 8,000 Joules [Fan-wiki].
  - Ammo history conflicts: the trivia says "140 ammo before it was nerfed in v2.6", the 2.6 page says magazine 120→50, and the infobox says 120 [Fan-wiki].
  - The usage text says "5 damage per bullet" while the infobox says 5.5 [Fan-wiki].
  - **2026:** it appears only in 2013 trailer footage reused on the Steam page (see "What changed") [Observed; Inference]. Its 2026 status is [Unverified].
- **Identification** [Observed]: the April 2013 in-game loadout screen File:Heavy_setup.jpg labels the equipped primary "ELECTRIC HONEY", and Riggs holds this exact pink-hive, magenta-ring gun. File:Theincredibleriggs.jpg (2015) shows the same gun.
- **Look:** the Beebeegun mesh, recoloured.
  - **2012–2015** [Observed: File:Photo_19-04-13_12_50_47_PM.png; side-by-side /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/sheets/eh_cmp.png]:
    - a black body with glowing violet slat panels
    - a magenta-pink faceted, striped hive with a tiny bee on it
    - a lavender-and-purple striped bent tube
    - three translucent magenta energy rings spiralling around the barrel
    - the wiki: "small bees circling its hive as well as purple energy rings on the hive and barrel" [Fan-wiki]
  - **Trailer, 2013 footage** [Observed: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/crops/tr348_zoom.png (f_014, 34.8 s); /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/steam_screens/screen_00.jpg]:
    - held by Rocky Horror Riggs
    - a round, banded hot-pink hive with two pink ball-tipped antennae
    - violet striped LED panels on charcoal
    - magenta rings at the muzzle (#DB72D1, light #F888F8) with white cores
  - Length ≈ 0.7× Riggs ≈ 0.85× Oliver.
- **Firing:**
  - Automatic with a moderate wind-up (500 / 300 / 2000), 5.5 damage, 0.10 s, 120 ammo, 3 s reload, dispersion 0.06; hitscan [Fan-wiki].
  - Trailer 34.3–36.4 s [Observed: frames f_009–f_030; sheets /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/sheets/tr_a.png and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/sheets/tr_b.png]: continuous fire while the magenta rings pulse and flare at the muzzle.
- **Projectile:**
  - A straight streak runs from muzzle to target [Observed]. At 34.8 s it is a fairly wide, translucent dark-grey core with a pale edge near the gun, turning pink-magenta near the target. In other frames (34.3 s, 36.4 s) it shows as a thin pink line.
  - Individual bees cannot be made out at 1080p [Unverified].
- **Impact:**
  - On the target, a starburst of long pink-magenta triangular shards with soft pale-pink puffs. The target, a cyan Huggable-type bear, flashes paler and keeps moving. No explosion [Observed, 34.8–35.7 s].
  - Pale-yellow five-point cartoon stars burst around the cyan bear's feet at 35.9–36.4 s, including screen_00. At that moment the cyan bear and a gold Huggable are trading melee blows, so the stars' source is [Unverified]. Do not treat them as an Electric Honey effect.
- **Images viewed:**
  - File:Photo_19-04-13_12_50_47_PM.png, File:Electric_Honey.png (2012), File:Heavy_setup.jpg, File:Theincredibleriggs.jpg, File:Image-1.jpeg (the BBO version: an orange-and-black coiled design, not BBG)
  - screen_00.jpg; my frames f_001–f_032
  - sheets tr_a.png, tr_b.png and eh_cmp.png
  - crops tr348_zoom.png, f014_left.png and s00_right.png
- **Depiction for shorts:** spinning magenta rings, a humming straight tracer with a purple-pink edge, and pink crystal-shard sparks with pink puffs on each hit [Observed basis]. Optional tiny violet "electric bees" riding the stream [BBG News invention]. Do not caption it as 2026 gameplay.
- **Confidence:** observed (2013 footage).

## Zombee Gun (primary; original BBR 2012; changed in BBG 2.6; on the menu in SkyVu's "Riggs Overhaul" thumbnail, about 2014; 2026 unverified)
- **Official text:** "Most of the damage this weapon deals is psychological." [Game text via wiki] (https://battlebears.fandom.com/wiki/Zombee_Gun)
- **Status and history:**
  - 100,000 Joules (originally 80,000), level 12 [Fan-wiki].
  - 2.6: damage 5→6, clip 300→200, range 1000→750, "+10% speed" added. The current infobox gives 4.5 damage, 300 ammo, range 1,000, +15% Speed and −7.5% Health [Fan-wiki conflict].
  - The 2012 gear screen shows no stat modifier [Observed: File:Zombee.png].
  - SkyVu's "Riggs Overhaul" menu thumbnail shows Riggs holding it, with the version stamp "2.9" [Observed: https://i.ytimg.com/vi/xp5B76ExuAI/hq1.jpg].
- **Look** [Observed: File:Photo_19-04-13_12_50_49_PM.png, File:Zombee.png; zoom /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/crops/zg_zoom.png]:
  - The Field Medic's stubby mesh in charcoal, blotched with dark blood-red.
  - A round muzzle of concentric dark-red rings.
  - Topper: a bright lime-green Huggable with two leaf-like antennae, dot eyes, a huge white grin and a dark-red smear at the mouth corner.
  - Length ≈ 0.45–0.5× Riggs ≈ 0.6× Oliver.
  - File:ZombeeOC.png shows a brown zombie-bear skin holding a cyan gun. It is not this weapon [Observed].
- **Firing:**
  - Automatic, 4.5 damage, 0.1 s, 300 ammo, 4 s reload [Fan-wiki].
  - "a continuous stream of what appears to be ground-up zombie Huggables" [Fan-wiki].
  - The first revision (2012-02-18) says it "fires bones and green liquid… the liquid doesnt stay in one place, it moves around slightly" [Fan-wiki, early].
- **Projectile:** no image [Unverified].
- **Impact:** unknown [Unverified].
- **Images viewed:** File:Photo_19-04-13_12_50_49_PM.png, File:Zombee.png, File:ZombeeOC.png, https://i.ytimg.com/vi/xp5B76ExuAI/hq1.jpg.
- **Depiction for shorts:** wobbling lime-green slime globs mixed with a few cartoon bone shapes. They splat as green goo and rainbow confetti, with no red [BBG News invention, built on Fan-wiki].
- **Confidence:** partial.

## Bounce Lazer (primary; BBG 2.19, Apr 26 2015; 2026 unverified)
- **Official text:** "Turn this place into a rave! Bounce your lasers off of everything!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Bounce_Lazer)
- **Status:**
  - 50 Gas, level 15 [Fan-wiki].
  - The page lacks Category:Heavy, but the class page lists it [Fan-wiki].
- **Look** [Observed: File:Bounce_lazer.jpg (2015 gear-up); zoom /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/crops/bl_gun.png]:
  - A small, weathered, slate-blue boxy blaster (#2E4D61 to #3D5A6B).
  - A short dark hexagonal muzzle on top, yellow-orange vent slits, and a green-to-orange light panel.
  - A vertical green-yellow-orange gradient strip runs down the grip.
  - A pink Huggable head hangs at the base like a pommel: light-pink round ears, X eyes, a wide open grin and its tongue out.
  - Held one-handed, pointing up at shoulder height. Pistol-sized: ≈ 0.3× Riggs including the head ≈ 0.35× Oliver.
  - Reading the head as the power source echoes the BB-1 laser, which Riggs powers with a Huggable's head [Inference; see Era equivalents].
- **Firing:**
  - "fires a beam of rainbows similar to the Huggable (Class) Headlights" [Fan-wiki].
  - 40 damage per second, rate 0.2, 32 ammo, 4 s reload, 1,250-unit range, +10% Speed [Fan-wiki].
  - Bounce count conflict: "It bounces 10 times" in the usage text versus "It can bounce 25 times" in the trivia [Fan-wiki].
- **Projectile (beam)** [Observed: https://i.ytimg.com/vi/dhQaJKzwgAg/hq1.jpg (RepeatingImp72, an Everyplay capture published 2015-05-01 per wiki video metadata); zoom /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/crops/bl_beam.png]:
  - A thin, perfectly straight beam striped in rainbow bands, red through violet.
  - It runs from the muzzle up to a point on a structure. From there a long, thin reflected line, pale pink-white with rainbow edging, continues off at a sharp new angle.
  - The beam is made of straight segments with crisp corners.
  - The HUD icon shows the blue-grey gun with the pink head [Observed].
- **Impact:** a small bright flare where the beam bounces, and sparkles at the muzzle [Observed, low-res]. The effect on targets was not seen [Unverified].
- **Images viewed:** File:Bounce_lazer.jpg; https://i.ytimg.com/vi/dhQaJKzwgAg/hqdefault.jpg, hq1.jpg, hq2.jpg, hq3.jpg.
- **Depiction for shorts:** a neon rainbow laser ricochets in straight zig-zag segments with a sparkle flash at every wall [Observed basis]. Targets glow and shed rainbow confetti under rave lighting [BBG News invention].
- **Confidence:** observed (fan footage, low-res).

## Flame Thrower (primary; BBG 2.14, Nov 29 2014; 2026 unverified)
- **Official text:** "Burn your enemies with the power of hot morning coffee without the lawsuit!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Flame_Thrower)
- **Status:** 60 Gas, no level listed [Fan-wiki].
- **Look** [Observed: File:Flamethrower_.jpg (2015 gear-up); zoom /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/crops/ft_can.png]:
  - A tall red rectangular can (#A72122, dominant #A82828) stands on top, with a yellow-orange sun or flame emblem and white text on its side label.
  - Under it sits a wide black hexagonal accordion-ribbed barrel. Its end face is pure black, with no visible bore.
  - A silver segmented grip at the rear.
  - Held across the body at waist height. ≈ 0.4× Riggs ≈ 0.5× Oliver.
- **Lineage:**
  - The wiki says it references "the flame thrower Oliver made himself in Battle Bears: Zombies" [Fan-wiki].
  - The BB Zombies cards show a grey pipe gun with a perforated nozzle and duct tape, topped by a red can with a rising-sun logo, spraying orange fire and black smoke [Observed: File:FlameThrower.png, File:FlameThrower_(2).png; zoom /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/crops/bbz_can.png].
  - The can's word may read "Coffee", but the image is too low-res and that reading is [Unverified]. Reading the BBG can as a coffee can is [Inference] (the item text says "hot morning coffee").
- **Firing:**
  - 12 damage, rate 0.125, 40 ammo, 4 s reload, +20% Speed, −10% Health.
  - Mid-range; "Similar to the Cosmic Fire, it will shoot red-colored flames".
  - All [Fan-wiki].
- **Projectile:** red flames [Fan-wiki]. The BBG flame visual was not seen [Unverified].
- **Impact:** unknown [Unverified].
- **Images viewed:** File:Flamethrower_.jpg, File:FlameThrower.png, File:FlameThrower_(2).png.
- **Depiction for shorts:** a red-orange flame jet with coffee-steam wisps. The target ends up soot-blackened with smoking ear tips, no burns [BBG News invention].
- **Confidence:** partial.

## Hivey League (secondary; default since BBR 2012; "improved" in BBR 1.3 on May 3 2012; speed penalty removed in BBG 2.6; 2026 unverified)
- **Official text:** "Fires a spreading cone of angry bees! Great for close range battles with multiple targets close together." [Game text via wiki; labelled "BBR Description" in the page's first revision, 2012-10-20] (https://battlebears.fandom.com/wiki/Hivey_League)
- **Status and history:**
  - BBR 1.3 notes: "Improved Spreadshot and Hivey League behavior." [Fan-wiki quoting update notes]
  - The speed modifier went −15% → −5% → removed. The 2012 gear screen shows "SPEED -15%" [Observed: File:Hivey_league.png].
  - 2.6: damage 30→20, cooldown 1.7→1, reload 5→4.5, "Speed reductions of 5% removed" [Fan-wiki].
  - Wiki conflicts:
    - ammo 4 (infobox) vs "six bullets" (text) vs "Ammo: 10" (previous stats), and the page says it once had "4 ammo"
    - damage printed as "1525"
    - the trivia calls it "the only default weapon to feature a Stat Modifier", which contradicts the Beebeegun's "+10% Health" [Fan-wiki]
- **Look** [Observed: File:Heavy.png (blue-gear render), File:Heavy_Class.jpg ("HEAVY (RIGGS)" card, 2012-06-05), File:Hivey_league.png (2012), File:Rocky-front.png and File:Riggs-default-front.png (2012 skin menu, Riggs holding it)]:
  - Body: boxy, with an amber ribbed vent panel and an orange underside stripe. The body is light grey or white in renders but mid-grey in game captures.
  - Topper: a gold hexagonal hive with amber bands and a bee face or emblem.
  - Muzzle: a front block whose face is a cluster of hexagonal black holes with yellow honey pooled in them. This matches the trivia "Honey seems to drip out on the barrel" [Fan-wiki].
  - A tiny white-winged bee flies beside the hive in the 2012 shot.
  - In SkyVu's 2012 BBR trailer, blue-gear Riggs holds this gun [Observed: https://i.ytimg.com/vi/0gYEZCMQfmA/hq1.jpg, showing the gold hive and honeycomb muzzle; https://i.ytimg.com/vi/0gYEZCMQfmA/hq3.jpg, showing the side view: tan-grey body, amber slat panel with bee emblem, orange stripe, banded gold hive]. The match to the Hivey League renders is [Inference, strong]. The earlier draft wrongly gave hq3 to the Beebeegun.
  - Length ≈ 0.5× Riggs ≈ 0.6× Oliver.
- **Firing:**
  - Shotgun: a short-range hitscan cone; "All shotguns… have identical range" [Fan-wiki].
  - 0.75 s, 6 s reload [Fan-wiki].
- **Projectile:** "angry bees" [Game text via wiki]. Not seen [Unverified].
- **Impact:** unknown [Unverified].
- **Images viewed:** File:Heavy.png, File:Heavy_Class.jpg, File:Hivey_league.png, File:Rocky-front.png, File:Riggs-default-front.png; https://i.ytimg.com/vi/0gYEZCMQfmA/hq1.jpg, hq2.jpg, hq3.jpg, maxresdefault.jpg.
- **Depiction for shorts:** the honeycomb muzzle coughs a fan of angry cartoon bees and honey droplets. Targets swat and hop under tiny yellow sting sparks [BBG News invention].
- **Confidence:** partial.

## Plasma Orb (secondary; BBR 1.3.1, Jun–Jul 2012; repriced in BBR 1.4.2; −10% Health removed in BBG 2.6; 2026 unverified)
- **Official text:** "The amount of voltage this gun produces is just enough to turn anything it touches into a smoldering husk of its former self... is that enough you think?" [Game text via wiki] (https://battlebears.fandom.com/wiki/Plasma_Orb)
- **Status and history:**
  - 60 Gas, level "None". The trivia says "It used to cost 150,000 Joules" and "It used to cost 100 gas" [Fan-wiki].
  - The 2012 gear screen shows "HEALTH -10%" [Observed: File:Plasma_orb.png].
  - 2.6: damage 42→45, cooldown 2→1.5, health reduction removed [Fan-wiki]. The infobox says 40 damage [conflict].
- **Look** [Observed: File:Plasma_Orb.png render, File:Plasma_orb.png (2012), File:ROcky_Horror.png, File:Riggs_Default.png (2013-01), File:BBRWEAPONS.png, File:Heavy_setup.jpg icon]:
  - Body: a dark gunmetal and navy launcher with a navy pistol grip.
  - Muzzle: a glowing octagonal magenta muzzle with vertical slats (#D22477 / #D4449F, white-hot core), plus two magenta vents on top.
  - Topper: a dark glass dome crawling with blue-white and violet lightning.
  - Small blue sparkle sprites float beside the dome.
  - Held at the hip. ≈ 0.4× Riggs ≈ 0.5× Oliver.
  - That it descends from the "Plasma Globe Glob Launcher" sketch is [Inference]. The wiki names that file the Beebeegun original concept, and its caption calls the 2D gun a hybrid of the Beebeegun and Plasma Orb [Fan-wiki].
- **Firing:**
  - A "re-skin of the Hivey League" shotgun that "releases a spreading blast of purple electricity". 40 damage, 1.5 s, 2 ammo, 5 s reload [Fan-wiki].
  - The layout matches the Hivey League (box body, dome topper, front block), but the topper and muzzle differ [Observed; Inference].
- **Projectile:** purple electricity [Fan-wiki]. Not seen [Unverified].
- **Impact:** "smoldering husk" [Game text via wiki]. The visual is unknown [Unverified].
- **Images viewed:** File:Plasma_Orb.png, File:Plasma_orb.png, File:ROcky_Horror.png, File:Riggs_Default.png, File:BBRWEAPONS.png, File:Heavy_setup.jpg, File:Beebeegun_original_concept.jpg, File:Riggs-heavy.png. File:Plasma_shotgun.jpg is the Combat Tech's "Plasma Shotgun" and was not used.
- **Depiction for shorts:** the globe crackles brighter, then a short forked cone of violet lightning. The target is left soot-dark with frizzed fur and a wisp of smoke [BBG News invention].
- **Confidence:** partial.

## Mother of Nature (secondary; BBR 1.3.2, Aug 24 2012; changed in BBG 2.6 and 2.7; shown in SkyVu's "Riggs Overhaul" thumbnails, about 2014; 2026 unverified)
- **Official text:** "Shoots poisonous berries at your enemies that drain their health over time." [Game text via wiki] (https://battlebears.fandom.com/wiki/Mother_of_Nature)
- **Status and history:**
  - 50,000 Joules, level 20 [Fan-wiki].
  - The 2012 gear screen shows "HEALTH -10%" and the stat labels DAMAGE / DURATION / COOLDOWN / RELOAD [Observed: File:Mother_of_nature.png].
  - 2.6: "Damage increased from 7 to 10", cooldown 2.5→2, reload 7→5.
  - "In v2.7, the Mother of Nature's -10% Health Reduction was removed, but has been re implemented since." [Fan-wiki]
- **Look** [Observed: File:Photo_19-04-13_12_50_55_PM.png (2013), File:Mother_Of_Nature.png render, File:Mother_of_nature.png (2012), File:1.3.2WEAPONS.png, File:Update_1_3_2_coming_soon.jpeg]:
  - A hollow log cannon in bark brown (#7C5643 / #503026) with a jagged, splintered open muzzle showing pale tan inner wood and a dark hollow.
  - Crimson and purple fungus-like growths on the bark, and yellow-green moss along the bottom.
  - Bound with bright green vine loops.
  - Held at the hip like a bazooka. ≈ 0.6× Riggs ≈ 0.7× Oliver.
  - The same log is the HUD weapon icon in SkyVu's Overhaul thumbnail [Observed: https://i.ytimg.com/vi/xp5B76ExuAI/maxresdefault.jpg].
- **Firing:**
  - 750 u/s arcing lob, 2 ammo, 2.5 s, 6 s reload [Fan-wiki].
  - The Overhaul thumbnails' HUD reads "1 / 2" [Observed].
- **Projectile:** "a large purple berry that travels with an arc" [Fan-wiki]. No unambiguous image of the berry in flight [Unverified].
- **Impact:**
  - Wiki [Fan-wiki]:
    - "When this berry comes into contact with any surface, it will burst open, creating a large purple plume of poison"
    - the poisoned get "a small purple skull over their head"
    - 4 damage per second for 10 s; it stacks, and the user can poison himself
    - the Status Effects page says "a purple/green skull will appear over the player's head"
  - SkyVu "Riggs Overhaul" thumbnails [Observed: https://i.ytimg.com/vi/xp5B76ExuAI/maxresdefault.jpg and hq2.jpg; zooms /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/crops/ov_max_target.png and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/crops/ov_hq2_zoom.png]:
    - **maxres:** a translucent dark-purple haze dome engulfs the target, with a purple swirl ring on the floor around it. Above the victim's head floats a magenta-purple round-bottomed flask (or berry with a stem) with a skull face, inside a red bracket. Reading the bracket as a targeting marker is [Inference].
    - **hq2:** a lumpy cloud of round, mid-purple puffs surrounds the target. A large translucent purple flask-shaped skull icon of the same design floats near the camera, above and left of Riggs's head, while Riggs's own health bar shows red.
    - That this big icon is the poison marker over Riggs himself (self-poisoning, which the wiki says can happen) is [Inference]. It could be something else [Unverified].
- **Images viewed:**
  - File:Photo_19-04-13_12_50_55_PM.png, File:Mother_Of_Nature.png, File:Mother_of_nature.png, File:1.3.2WEAPONS.png, File:Update_1_3_2_coming_soon.jpeg
  - https://i.ytimg.com/vi/xp5B76ExuAI/maxresdefault.jpg, hqdefault.jpg, hq2.jpg
- **Depiction for shorts:** a fat purple berry lobs in an arc and bursts into a purple puff-cloud, with a swirl ring on the floor. A little purple skull-flask icon bobs over the victim, who coughs and tints faintly purple. No vomit or gore [Observed basis + BBG News invention for the cough and tint].
- **Confidence:** observed (SkyVu thumbnails, about 2014 by inference).

## Freeze Blast (secondary; BBG 2.12, Oct 2 2014; 2026 unverified)
- **Official text:** "Blastin you with FREEEZEEEEE!!!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Freeze_Blast)
- **Status:** level 1. Price conflict: 150,000 Joules on the class page versus 225,000 in the infobox [Fan-wiki].
- **Look** [Observed: File:Freeze.jpg (2014 gear-up)]:
  - Body: an ice-textured pale cyan block (dominant #88C8C8 / #98D8D8) with a side window of glowing yellow bars and an orange ribbed cap on top.
  - Barrels: two of them, a thick upper and a thin lower. Each ends in a white, jagged, frost-encrusted cap with a round black bore.
  - Held at the hip, pointed forward. ≈ 0.7× Riggs ≈ 0.85× Oliver.
- **Firing:**
  - 0.5 s, 5 ammo, 4 s reload; explosives 5–10, damage 5 [Fan-wiki].
  - "fires small blue projectiles in an arc" [Fan-wiki].
- **Projectile:** small blue projectiles [Fan-wiki]. Not seen [Unverified].
- **Impact:**
  - "On contact, these projectiles split and form damaging pools on the floor, similar to the Gernobyl. Enemies who step in the pools will be slowed down severely" [Fan-wiki].
  - The page's "radiation damage" wording looks copied from the Gernobyl [Inference].
  - The Status Effects page gives "Slowed" a "yellow Z" overhead but does not list Freeze Blast [Fan-wiki]. So its icon is [Unverified].
  - The Buzz Kill page calls Freeze Blast an explosive that does not "create an explosion as such" [Fan-wiki].
- **Images viewed:** File:Freeze.jpg. File:Freezer.jpg is an unrelated fridge-character icon.
- **Depiction for shorts:** blue ice globs arc over, crack apart and spread frosty puddles. Victims skid in slow motion with frost on their fur and chattering teeth [BBG News invention].
- **Confidence:** partial.

## Buzz Kill (secondary; original BBR 2012; "improved" in BBR 1.3; 2026 unverified)
- **Official text:** "Fires a queen bee which explodes a second or two after impact." [Game text via wiki; labelled "BBR Description" in the first revision, 2012-10-20] (https://battlebears.fandom.com/wiki/Buzz_Kill)
- **Status and history:**
  - 25,000 Joules, level 3 [Fan-wiki].
  - BBR 1.3 notes: "Improved Buzz Kill" [Fan-wiki quoting update notes].
  - Previous stats: max explosives 50, rate 1.7 s, fly-off delay 2 s (now 20 s) [Fan-wiki].
- **Look** [Observed: File:BuzzKill.jpg (2013 gear-up), File:Buzz_kill.png (2012), File:Gnifle-heavy-setup.png (icon)]:
  - The Hivey League body in grey, with an amber ribbed panel.
  - Topper: a gold hexagonal hive with an orange band and a bee emblem.
  - Muzzle: a black hexagonal face with concentric yellow-orange chevron stripes, like a bee's rear.
  - A soft white smoke puff hangs at the muzzle in both the 2012 and 2013 shots.
  - The 2012 gear screen's stat labels read EXPLOSIVES / AOE / COOLDOWN / RELOAD [Observed].
  - ≈ 0.55× Riggs ≈ 0.65× Oliver.
- **Firing:**
  - 800 u/s projectile; "the only projectile in Battle Bears Gold that flies with an upward arc instead of a downward one".
  - 3 ammo, 1.5 s, 3.5 s reload.
  - All [Fan-wiki].
- **Projectile:** "a large bee-like explosive" that "sticks to any surface" [Fan-wiki]. Not seen [Unverified].
- **Impact:**
  - It explodes "exactly 1.5 seconds after it landed" (the lead says "two seconds"), or "immediately upon impact with an enemy player".
  - Explosives 40–70 with area of effect; "the Heavy's only weapon that causes an actual explosion".
  - All [Fan-wiki]. The explosion visual is unknown [Unverified].
- **Images viewed:** File:BuzzKill.jpg, File:Buzz_kill.png, File:Gnifle-heavy-setup.png.
- **Depiction for shorts:** a fat golden queen bee rises in an upward arc and sticks to a wall, blinking and buzzing for 1.5 s. Then it pops in a round yellow-orange cartoon blast, with a few dazed bees spiralling out [BBG News invention].
- **Confidence:** partial.

## Sucker Punch (secondary; original BBR 2012; ammo changed 1→6→3; 2026 unverified)
- **Official text:**
  - "Lobs a projectile that will stun the target for a few seconds." [Game text via wiki] (https://battlebears.fandom.com/wiki/Sucker_Punch)
  - The first revision (2012-05-27) reads "Stuns friend and foe the sucker punch launches a huggable head to stun suckers in its path!" [Fan-wiki, early; possibly old in-game text, Unverified].
- **Status:**
  - 75,000 Joules, level 14 [Fan-wiki].
  - "Sucker Punch originally had 1 ammo but then was changed to 6 ammo, which was then changed to the current 3 ammo" [Fan-wiki]. The usage text still says "It has six ammo" [Fan-wiki conflict].
- **Look** [Observed: File:SuckerPunch.jpg (Rocky Horror skin); zoom /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/crops/sp_zoom.png]:
  - A compact grey box launcher with a tan ribbed underside and a short ribbed barrel.
  - A pink faceted Huggable head (#EA768A, lit #F898A8) is mounted on its front. It has two small pointed pink ears on top, black dot eyes and a big white toothy grin.
  - ≈ 0.3× Riggs ≈ 0.35× Oliver.
- **Firing:** lobs at 1,000 u/s in an arc; 3 ammo; 3 s reload; +10% Speed [Fan-wiki].
- **Projectile:**
  - "a small, pink Huggable-like head". It stays intact after hitting, can physically push players, and can penetrate the Iron Curtain [Fan-wiki].
  - Not seen in flight [Unverified].
- **Impact:**
  - Stunned for 2.6 s. "a blue Nuggs will appear over the player's head"; the victim cannot move, use Specials, reload or use weapons [Fan-wiki].
  - Originally the icon was "a green question mark" [Fan-wiki].
  - Stun icon [Observed: File:Images_(3).jpg, the Status Effects page's "Stunned Status symbol"]: a round sky-blue bird-like Nuggs with a white crest feather, flanked by white crescent "spin" arcs.
  - Possible SkyVu shot [Observed: https://i.ytimg.com/vi/xp5B76ExuAI/hq3.jpg; crops /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/crops/ov_hq3_hud.png and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/crops/ov_hq3_scene.png]:
    - the HUD weapon icon is a pink Huggable head on a box with red-and-white hazard stripes
    - the ammo reads "4 / 6", which fits the 6-ammo era
    - a cream-coloured bear with a teal headband is engulfed in a bright yellow-white crackling burst
  - That this is a Sucker Punch hit is [Inference]. Whether the hazard-striped icon means a remodelled launcher is [Unverified].
- **Images viewed:** File:SuckerPunch.jpg, File:Images_(3).jpg, https://i.ytimg.com/vi/xp5B76ExuAI/hq3.jpg.
- **Depiction for shorts:** a pink plush head bonks the target with a yellow-white flash and bounces away intact. The target freezes mid-pose while a blue Nuggs bird circles its head between white spin arcs [Observed + Fan-wiki; the bounce gag is BBG News invention].
- **Confidence:** partial.

## Barbed Gloves (melee; default since BBR 2012; changed in BBG 2.6; 2026 unverified)
- **Official text:** "Oven mitts for serving hot pain." [Game text via wiki] (https://battlebears.fandom.com/wiki/Barbed_Gloves)
- **Status:**
  - Default; "It does not have any Stat Modifiers"; "tied for the strongest out of all Heavy melees" [Fan-wiki].
  - 70 damage per glove on the page, versus the 2.6 entry "Melee Damage decreased from 35 to 20" [Fan-wiki conflict].
- **Look** [Observed: File:Photo_19-04-13_12_51_16_PM.png (2013), File:Barbed_gloves.png (2012)]:
  - Two huge rounded creature-shaped plush mitts worn over the forearms, each with black dot eyes at the fist end.
  - Mustard-yellow (#BFB044 / #C7BA4B), wrapped in black barbed wire, with red-brown scratch and stitch marks.
  - Each glove is about the size of Riggs's head (≈ 0.25× his height). Together they span his chest.
  - They are not "dark brawler gloves".
- **Swing:** a two-glove punch; "can be doubled due to the second glove used in the attack" [Fan-wiki].
- **Impact:** unknown [Unverified].
- **Images viewed:** File:Photo_19-04-13_12_51_16_PM.png, File:Barbed_gloves.png.
- **Depiction for shorts:** a one-two plush-mitt haymaker. The barbed wire throws little spark glints, and the target spins away with cartoon stars [BBG News invention].
- **Confidence:** partial.

## Catastrophe (in-game spelling "CATASTOPHE") (melee; BBR 1.3.1 week 1, Jun 2012; changed in BBR 1.4.2 and BBG 2.6; 2026 unverified)
- **Official text:** "Let Riggs bring the kitten cuddlin' to you! You may not like how he does it, though, and living through it isn't likely... but hey, kittens!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Catastrophe)
- **Spelling and history:**
  - The in-game list spells it "CATASTOPHE" [Observed: File:Catastrophe.png, File:Heavy_setup.jpg, File:Gnifle-heavy-setup.png].
  - 20 Gas, no level lock [Fan-wiki].
  - The 2012 gear screen shows "HEALTH -5% / SPEED +15%" [Observed]. BBR 1.4.2 removed the −5% Health and "Added +5% speed boost" [Fan-wiki].
  - The page also claims "20% speed reduction and a 10% health boost", and its previous stats list both "No speed modifier" and "15% speed boost" [Fan-wiki internal conflict].
  - 2.6 lists damage 30→25 [Fan-wiki].
- **Look** [Observed: File:Catastrophe_1.png render, File:Catastrophe.png (2012), File:BBRWEAPONS.png, File:Heavy_setup.jpg]:
  - Each glove is a blocky calico cat head with off-white, orange and brown patches.
  - One huge glossy blue cartoon eye per head (#318BD8).
  - A pink-red open mouth at the punching end, and dark brown ear tips.
- **Swing:** a two-glove punch, 40 damage per glove, doubled by the second glove [Fan-wiki].
- **Impact:** unknown [Unverified].
- **Images viewed:** File:Catastrophe_1.png, File:Catastrophe.png, File:BBRWEAPONS.png, File:Heavy_setup.jpg.
- **Depiction for shorts:** the cat-head gloves yowl and hiss on each punch, with a puff of calico fur and cartoon scratch lines but no wounds [BBG News invention].
- **Confidence:** partial.

## Blood Spurt (melee; BBR 1.3.2, Aug 24 2012; changed in BBR 1.4.2 and BBG 2.6; shown in the Steam store trailer, which is 2013 footage; 2026 build unverified)
- **Official text:** "Bolo your enemies!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Blood_Spurt). Reading the name as a nod to the film *Bloodsport* and to Bolo Yeung is [Inference].
- **Status and history:**
  - 60,000 Joules, no level lock [Fan-wiki].
  - BBR 1.4.2 "Removed +15% health boost" [Fan-wiki].
  - 2.6: "Melee Damage decreased from 45 to 30… Health increase of 10% added". The page gives 70 damage, −10% Health, +10% Speed [Fan-wiki conflict].
  - **2026:** shown only in 2013 trailer footage reused on the Steam page [Observed; Inference]. Its 2026 status is [Unverified].
- **Look** [Observed: File:Blood_spurt.png render, File:Blood_Spurt.jpg (2013 gear-up), File:1.3.2WEAPONS.png, trailer f_033 at 36.7 s; comparison /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/sheets/bs_cmp.png]:
  - Fists wrapped in tan bandage tape (#E0BDA1 / #EFCDB2) with dark crack lines.
  - Pale ice-blue knuckle blocks (#9AC2C8). These stay pale blue even on the Rocky Horror skin, so they belong to the weapon model [Observed; Inference].
  - Studded with long, glassy crystal spikes in green, gold and rose-copper.
  - This is the trailer glove. It is not the Barbed Gloves, which are mustard-yellow barbed-wire mitts [Observed].
- **Swing and impact** [Observed: trailer frames f_031–f_052 (36.5–38.6 s); sheet /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/sheets/tr_c.png; crop /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/crops/tr367_glove.png]:
  - 36.5–36.7 s: in close-up, Rocky Horror Riggs cocks his right fist at shoulder height beside a gold Huggable-class bear (antennae, blue eyes).
  - 36.8 s: a near-white frame redraws the same punch pose as white fill with red and black outlines. Reading this as a stylised edit transition into the card, not an in-game impact flash, is [Inference, strong].
  - 36.9–38.2 s: the "RIGGS / HEAVY" title card. The fist is pressed into the gold bear's face, with white light glints on the crystal spikes. An orange round emblem with circular holes sits behind "RIGGS".
  - No blood is shown.
  - Two-glove punch: "Although different in design, the Blood Spurt uses the same swing animation as the Heavy's other melee weapons" [Fan-wiki].
- **Images viewed:** File:Blood_spurt.png, File:Blood_Spurt.jpg, File:1.3.2WEAPONS.png; trailer frames f_031–f_052.
- **Depiction for shorts:** a crystal-studded jab with a starburst of glints on contact, then a comic-panel freeze-frame [Observed basis + BBG News invention]. Keep the name off-screen or treat it as a joke, with no blood.
- **Confidence:** observed (2013 footage).

## Sword and Stone (melee; modelled in 2012, released BBG 2.11 on Aug 27 2014; repriced in 2.20 on May 29 2015; 2026 unverified)
- **Official text:** "Riggs knew he wasn't the chosen one but dislike the idea of losing, so he took the stone with the sword." [Game text via wiki] (https://battlebears.fandom.com/wiki/Sword_and_Stone)
- **Status and history:**
  - "fully modeled and textured, first previewed back in 2012… being deemed scrapped content until prior the v2.11 update" [Fan-wiki].
  - Price conflict: 150,000 Joules on the page and class list, versus the Updates entry for 2.20, "reduced from 1,000,000 joules to 300,000 joules" [Fan-wiki].
  - No level lock [Fan-wiki].
- **Look** [Observed: File:The_Sword_AND_the_Stone_Model.png; concept File:The_Sword_AND_the_Stone.jpg (identical to File:Riggsmelee.jpg), hand-labelled "(For Riggs) The Sword AND the Stone"]:
  - A longsword with a bronze curved crossguard and a hexagonal pommel.
  - A brown leather-wrapped grip.
  - A steel blade etched with dark runes.
  - The tip is sunk in a grey boulder patched with green moss.
  - In the concept: a gold guard, a round silver pommel and a paler stone.
  - "does not resemble any form of gloves" [Fan-wiki].
  - The in-hand size and grip were not seen [Unverified]. Swinging the whole sword-and-boulder like a club is [Inference].
- **Swing:** 40 damage, "doubled if both hits connect"; −7.5% Health, +15% Speed [Fan-wiki].
- **Impact:** unknown [Unverified].
- **Images viewed:** File:The_Sword_AND_the_Stone_Model.png, File:The_Sword_AND_the_Stone.jpg, File:Riggsmelee.jpg.
- **Depiction for shorts:** Riggs holds the hilt and swings the boulder end like a mace: a rock "thunk", a sword "shing" and a puff of moss and dust [BBG News invention].
- **Confidence:** partial.

## Huggable Gloves (melee; original BBR 2012; changed in BBG 2.6; 2026 unverified)
- **Official text:** "Everything about this would make you think that these gloves are soft and weak. For some reason you are wrong (you know why)." [Game text via wiki] (https://battlebears.fandom.com/wiki/Huggable_Gloves)
- **Status and history:** 20 Gas, level 5. Before 2.6: 50 damage per glove and no modifier [Fan-wiki].
- **Look** [Observed: File:Photo_19-04-13_12_51_23_PM.png, File:Huggable_Gloves.png (2012)]: the Barbed Gloves mesh in hot pink and magenta (#DE2162 / #E54178), with black dot eyes and no wire.
- **Swing:**
  - Two-glove punch, 40 damage, +10% Speed [Fan-wiki].
  - The fan "Most Intense Match" set uses them, but no melee moment appears in its thumbnails [Observed].
- **Impact:** unknown [Unverified].
- **Images viewed:** File:Photo_19-04-13_12_51_23_PM.png, File:Huggable_Gloves.png.
- **Depiction for shorts:** squeaky-toy thuds with puffs of pink fluff. The victim looks betrayed [BBG News invention].
- **Confidence:** partial.

## Zombee Gloves (melee; original BBR 2012; changed in BBG 2.6; 2026 unverified)
- **Official text:** "While devastating, decomposition softens up the impact - at least a little." [Game text via wiki] (https://battlebears.fandom.com/wiki/Zombee_Gloves)
- **Status and history:**
  - 50,000 Joules (originally 75,000), level 11 [Fan-wiki].
  - Modifier conflict: "30% special speed reduction" in the page text versus "Special Cooldown reduction of 10% added" on the 2.6 page [Fan-wiki].
- **Look** [Observed: File:Photo_19-04-13_12_51_26_PM.png]: the same mitt mesh in zombie green (#559F3E / #6FAA58), with dot eyes and open gashes edged in red showing pale rib-like stripes.
- **Swing:** two-glove punch, 40 damage [Fan-wiki].
- **Impact:** unknown [Unverified].
- **Images viewed:** File:Photo_19-04-13_12_51_26_PM.png.
- **Depiction for shorts:** squelchy hits that fling green goo flecks. Recolour the red gash edges green or purple to keep it 13+ [BBG News invention].
- **Confidence:** partial.

---

## Era equivalents (do not mix them into BBG shots)
- **BB-1 (2010):**
  - "Riggs makes the laser by smashing an out-of-energy laser gun into a Green Huggable's head… the gun shoot out a powerful green laser that could penetrate multiple Huggables at once. When in its Hyper mode, the laser becomes reflective" [Fan-wiki, Laser].
  - The cutscene frame shows a dark green gun jammed onto a green Huggable, firing a bright green beam, with Riggs below [Observed: File:Laser.png].
  - That this is the ancestor of the Bounce Lazer's ricochet is [Inference].
  - The line "A huggable's rainbow soul can power a laser gun!" comes from the YouTube copy for "BB-1 Riggs 2/10: Firin' the Laser!" (esHWLlXDv-0). oEmbed today gives its channel as "BattleBearsGame", not the confirmed SkyVu channel "BATTLE BEARS" [Canon, channel unconfirmed; description not re-read because YouTube blocks it].
  - File:Riggs-trailer-holding-gun.png is a 2D cel frame of Riggs with a dark machine gun with a perforated shroud [Observed]. Its source and era are [Unverified].
- **BB Zombies (2009):**
  - Oliver's Laser!!! card: a welding-masked bear, and a prism splitting a white beam into a rainbow [Observed: File:Laser_(2).PNG]. The wiki: Oliver "uses it to focus the rainbow energy from a dead Huggable" [Fan-wiki].
  - Oliver's flamethrower: a grey perforated pipe gun with a red sun-logo can [Observed: File:FlameThrower.png, File:FlameThrower_(2).png].
- **BB Fortress (BBF, 2013):** Riggs uses a Minigun ("Takes a little bit to get going but once it gets going its damage is unrivaled!" [Game text via wiki, "Official Battle Bears Fortress Description"]) and Dual Lasers [Fan-wiki, Riggs (Hero)].
- **BB Ultimate (BBU) and BB Overclock (BBO):**
  - Dates [Fan-wiki, Battle Bears Overclock page]:
    - BBU launched June 25, 2014 and was pulled in late 2014.
    - The BBUv2 public beta ran June 15 to November 27, 2015.
    - BBO released February 10, 2016 on the App Store, with Google Play following.
  - File:HMGNew.jpg is a grey-and-white minigun with cyan slots. It was uploaded 2014-07-01 and is used on Minigun (BBO) [Observed]. That it shows BBU 2014 is [Inference].
  - File:Image-1.jpeg is the orange-and-black coiled Electric Honey (BBO), uploaded 2016-02-28 [Observed]. The wiki says it "shoots larger, slower projectiles" [Fan-wiki].
- **BB Heroes (BBH; soft launch May 23, 2023; global release Oct 3, 2024 [Fan-wiki]):**
  - Attack "Beebee Gun" (5 × 306), Ultimate "He can fly now?" [Fan-wiki].
  - battlebears.com: "Riggs's Ultimate showcases his astonishing leap and ground-smashing ability, disrupting enemies and terrain alike." [Canon text; the BBH link is Inference]

## Official SkyVu video and art notes
- **"BATTLE BEARS GOLD Developer Update - Riggs Overhaul"** (xp5B76ExuAI): the title and channel "BATTLE BEARS" are confirmed by oEmbed [Canon].
  - The menu thumbnail shows version "2.9". BBG 2.9 is dated May 8, 2014 on the wiki [Fan-wiki], so the video dates to about May 2014 [Inference].
  - A search snippet of its description ("Game Designer SkyVu Trevor explains in detail all of the changes in store for Riggs") was not found again [Unverified].
  - Thumbnails show the Zombee Gun (menu), Mother of Nature (poison) and a Sucker Punch-style HUD.
  - What the overhaul changed is [Unverified].
- **"BATTLE BEARS GOLD Trailer: Award-Winning Multiplayer Shooter Game"** (rfAyqVJrli4, channel "BATTLE BEARS"): its thumbnails match the Steam trailer frame-for-frame (see "What changed").
- **"BATTLE BEARS ROYALE Official Game Trailer AVAILABLE NOW ON THE APP STORE"** (0gYEZCMQfmA, channel "BATTLE BEARS"): blue-gear Riggs with the Hivey League (hq1, hq3).
- **Steam announcements for app 4408320** (Steam news API):
  - Jul 6, 2026, "First BATTLE BEARS GOLD Playtest This Thursday!": the "CLOSED TESTING" banner with Riggs and the Beebeegun [Observed].
  - Oct 14, 2026: a "CLOSED TESTING 5" banner listing "-LIGHTING, EFFECT & TEXTURE IMPROVEMENTS" [Canon, image text]. It shows no Heavy weapon.

## Wiki conflicts to keep visible
- **Stat histories:** the 2.6 page's numbers often contradict the current infoboxes (Beebeegun, Electric Honey, Big Iron, Field Medic, Zombee Gun, Barbed Gloves, Blood Spurt).
- **Electric Honey:** ammo 140 vs 120→50 vs 120; damage 5 vs 5.5.
- **Hivey League:** ammo 4 vs 6 vs 10; damage "1525"; the "only default with a Stat Modifier" claim.
- **Bounce Lazer:** 10 vs 25 bounces.
- **Buzz Kill:** 1.5 s vs 2 s fuse.
- **Sucker Punch:** 3 vs "six" ammo.
- **Modifiers:** Catastrophe; Field Medic; Zombee Gun; Zombee Gloves.
- **Prices:** Freeze Blast 150k vs 225k; Sword and Stone 150k vs 300k.
- **Freeze Blast:** "radiation" wording.
- **Provolowned:** "re-texture of the Beebeegun" versus the visibly different model.
- **Category errors:** the wiki's Category:BBG Weapons includes the skin "The Incredible Riggs". weapons_by_class.json's "Riggs" key also wrongly includes A Salt Rifle, Heavy A Salt Rifle, Soaker, Spreadshot (BBG), Steamshot, B.E.A.R. Club and Krikkit Bat (from a copied Soldier changelog), and Catastrophe sits in "_unassigned" because the class page links "Catastophe".

## Corrections to the previous inventory and draft
- **Field Medic muzzle:** a silver hex plate with six bores around a centre bolt, not "dark six-hole".
- **Freeze Blast:** two barrels with white frost caps, not one barrel with a three-pronged clamp.
- **Provolowned top:** an angled silver plate plus a white twine-tied lump, not a "white wedge".
- **Electric Honey tracer:** a straight streak, translucent dark-grey or thin pink depending on the frame. The impact adds soft pink puffs to the shards.
- **Hivey League body:** white or light grey in renders, mid-grey in game.
- **Era:** the Steam trailer is 2013 footage. "Present in the 2026 trailer" is now "shown in reused 2013 footage" for Electric Honey and Blood Spurt.
- **Beebeegun 2026:** "not seen in 2026 media" is now "seen in the official Jul 6, 2026 Steam banner".
- **Misattribution:** BBR trailer hq3 belongs to the Hivey League, not the Beebeegun.
- **File names:** File:Laser_(2).PNG and File:FlameThrower_(2).png.
- **Labels:** Beebeegun "no splash" is [Inference]; the concept caption belongs to File:Beebeegun_original_concept.jpg; the Plasma Orb lineage is [Inference].
- **Sucker Punch head:** two ears.
- **Mother of Nature hq2:** the large skull-flask is probably a status icon, not a cloud puff.
- **BBU/BBO:** dates fixed.

## Cross-dossier conflicts (for the orchestrator)
- **visuals_2026.md** calls the trailer glove at 36.5–38 s the "Barbed Gloves". The images match the **Blood Spurt**: tan tape, crystal spikes, pale-blue knuckles, as in File:Blood_spurt.png and File:Blood_Spurt.jpg. The Barbed Gloves are yellow barbed-wire mitts.
- visuals_2026.md also describes the Riggs shot as firing "a pink tiered dome with a magenta spiral trail". The pink dome is the gun's hive and the spiral is the muzzle rings; the projectile is a straight streak [Observed].
- visuals_2026.md's proposed riggs.md correction 6 should not be applied as written.
- **visuals_shared.md** identifies the gun in File:Theincredibleriggs.jpg and Steam screen_00 as the **Beebeegun**. It is the **Electric Honey**: identical to the Electric Honey infobox image, and labelled "ELECTRIC HONEY" in File:Heavy_setup.jpg. Its proposed riggs.md Beebeegun description (pink hive, magenta coil, pink tracers) should not be applied.

## Corrections for the character file
File: /home/user/thallo-site/bbg-news-repo/characters/riggs.md. Each verified correction, with its exact current text, is listed in `soul_corrections`:
1. The weapon looks are documented.
2. The prompt-pack gloves and gun are wrong.
3. The bandolier and pack are the 2D card look; the BBG 3D default wears red (or blue) gear.
4. The red skin is Rocky Horror.
5. The trailer is reused 2013 footage showing Electric Honey and a Blood Spurt punch.
6. The "leap and ground-smashing" and "close combat" lines belong to the battlebears.com hero page (BBH by inference).
7. Keep the BBG Beebeegun distinct from the hero-page "Beebee gun".
8–10. The open questions are answered or partly answered.

## Open questions
See `open_questions`.