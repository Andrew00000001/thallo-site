# B-1000 (Assault) weapons dossier

B-1000 is BBG's Assault class, a "half-ton murderous robot" [Game text via wiki, Shock N Claw]. Steam's 2026 store text names him as "ASSAULT: B-1000" [Canon, Steam appdetails 4408320, fetched 2026-10-16]. He did not exist in BBR (2012). The BBR 1.4.3 notes (Apr 2013) only tease "NEW Character Class- the B-1000! A robot made to kill." [Game text via wiki, Updates]. He launched with BBG 1.0 in May 2013 [Fan-wiki].

The wiki class page lists 14 weapons [Fan-wiki]:
- **Primaries:** Grenader, Bearail Gun, Energy Overflow, Super Rapid Chain Gun (SRCG), Lightning Bolt, Bass Cannon.
- **Secondaries (back modules):** Last Resort (removed), Metal Crush, Energy Barrier, Smoke Screen, Satellite.
- **Melees:** Axecutioner, Shock N Claw, Primus Sword.

**Sources and what I could reach (2026-10-16)**
- **Reached:**
  - Fan-wiki pages, re-fetched through the MediaWiki API (all official quotes below were re-checked against current wikitext).
  - Wiki images, re-downloaded and viewed: `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/wiki_img/png/`.
  - About 90 YouTube thumbnails (hq1/hq2/hq3/hqdefault/maxres), re-downloaded to `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/yt/` and named `<videoId>_<size>.jpg`. These cover 2013–2021 fan gameplay, official SkyVu videos and 2026 playtest uploads.
  - The local Steam trailer and its screenshots.
  - The live battlebears.com characters page and product JSON.
  - The Steam store API.
- **Not reached:**
  - The Internet Archive returned "Temporarily Offline" (HTTP 503) all session. SkyVu's archived release notes therefore could not be re-read.
  - YouTube playback is blocked. I watched no video and only saw thumbnails.

**Labels.** I opened every image cited as [Observed]. YouTube hq1/hq2/hq3 frames come from points inside the video; their exact timestamps are not given by YouTube.

## House look (applies to every weapon)
- **Mounting (fixed):** the primary is built onto B-1000's RIGHT forearm, the melee onto his LEFT forearm, and the secondary is a BACK module. He never holds anything in a hand.
  - Evidence [Observed]: the wiki front renders `B-1000Skin.png`, `Gold1000.png`, `Orange1000.png`, `Grenader.png`, `EnergyOverflow.png`; the back views `Last_Resort.png`, `Metal_Crush.png`, `Satellite_.png`; and the official grey T-shirt art (https://cdn.shopify.com/s/files/1/0370/2469/4408/files/BB_shirt_GreyB1000_model.png).
  - The wiki adds that he is "the only class that displays all of its weapons all the time" [Fan-wiki].
  - The 2D class portrait (`B-1000.png`, `Assaultimage.png`) draws gun and claws MIRRORED [Observed]. Do not copy its arm layout.
- **Weapon colours stay the same on every skin:** orange, white and black hardware with cyan accents. Skins recolour only the armour [Observed across Silver/Gold/Orange/default renders]. The exceptions are the Primus Sword (silver and pink) and the Bass Cannon (olive and black with blue).
- **Approximate hex values** sampled from official in-game art [Inference: sampled, not official codes]:
  - Lit hardware orange #E58D2B (shadowed renders read #A0–#A7 5x10 brown-orange, e.g. #A75C10).
  - Cream-white #F3ECD2 / #E0D7CF; near-black #1C1A18.
  - Eye cyan #38D6D7; claw cyan #2BDCF1.
- **Scale:** the BBG News scale chart puts B-1000 at about 1.5x Oliver's height [BBG News invention, from the character file]. Weapon sizes below are fractions of B-1000's height, estimated from the renders [Inference], then converted to Oliver units.
- **How a kill looks:** BBG kills break bodies into chunky separate pieces, not gore [Observed].
  - In the Steam trailer at 4.95–5.3 s, a green Demo comes apart into head (blue bandana), torso and arm, which fly upward. Frames: `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/trailer/k_5.0.jpg`, `k_5.1.jpg`, `k_5.3.jpg` in the same folder.
  - In Steam screenshot `screen_04.jpg`, red armour chunks fly through the air.
- **Splash sizes from the wiki's AoE numbers**, read as max-damage/min-damage radii in game units [Fan-wiki numbers; Inference on meaning]:

| Weapon | AoE |
|---|---|
| Last Resort | 200/400 |
| Metal Crush | 125/400 |
| Grenader | 125/250 |
| Satellite | 125/250 |
| Bearail | 90/220 |
| Bass Cannon | 75/150 |
| SRCG | 50/100 |

  Lightning Bolt and Energy Overflow have no AoE.
- **Signature promo loadout:** Bearail Gun + Shock N Claw + Metal Crush.
  - It appears in the Steam trailer (1.5–6.9 s), the trailer's B-1000 splash card (5.8–6.6 s), the T-shirt and most store renders [Observed].
  - The wiki's DEFAULT loadout is different: Grenader + Axecutioner, plus Last Resort (2013) or Smoke Screen (wiki, by 2020) [Fan-wiki].

## Arsenal at a glance
| Weapon | Slot | Added | 2026 evidence |
|---|---|---|---|
| Grenader | Primary (default) | 2013 launch | Steam screenshot `screen_04` / trailer 26 s, capture date unknown [Observed]; JustNubz showcase frame, probable [Inference] |
| Bearail Gun | Primary | 2013 launch | Official 2026 playtest highlights thumbnail + fan 2026 closed test [Observed] |
| Energy Overflow | Primary | 2.3, Sep 27 2013 | none found |
| SRCG | Primary | 2.7, Jan 23 2014 | none found |
| Lightning Bolt | Primary | 2.7, Jan 23 2014 | none found |
| Bass Cannon | Primary | 2.20, May 29 2015 | none found |
| Last Resort | Secondary | 2013 launch; later REMOVED | none found |
| Metal Crush | Secondary | 2013 launch | Steam trailer (era unknown) |
| Energy Barrier | Secondary | 2.3 | fan 2026 closed test [Observed] |
| Smoke Screen | Secondary (later default per wiki) | 2.7 | none found |
| Satellite | Secondary | 2.7 | none found |
| Axecutioner | Melee (default) | 2013 launch | none found |
| Shock N Claw | Melee | 2013 launch | fan 2026 closed test, low-res [Observed] |
| Primus Sword | Melee | 2.21, Jul 3 2015 | pink X-guard blade in 2026 thumbnails [Observed]; identity [Inference] |

**Launch kit.** A fan demo description from June 4, 2013 lists the launch kit as Bearail ("110K Joules"), Grenader, Metal Crush, Last Resort ("Suicidal explosion like Whipped Cream"), Shock n claw and Axecutioner [Unverified: fan video description, YouTube NJKRl54kc54 / cke79KdKQ-M]. This matches the wiki's six launch pages.

**2.7 wave.** A fan video "Battle Bears Gold Update 2.7 Beta" (YouTube WPVJTueNX1o, hq1) shows a "NEW WEAPONS" promo card [Observed]. On it, a default B-1000 carries a big drum chain gun (the SRCG), next to icons of the Smoke Screen pack, the Lightning Bolt cannon and a Satellite-style orange pod with a cyan lens. Where the card came from is [Unverified].

## Grenader (primary, default; 2013 launch; 2026 unconfirmed)
- **Official text:** "Got a weak arm? Fear not! This honey of a weapon does the throwing for you. Now you can sit back and relax while pelting your enemies with explosives from afar." [Game text via wiki] (https://battlebears.fandom.com/wiki/Grenader)
- **Status and history:**
  - Default primary, level 1 [Fan-wiki]. Beta name "Grrnade Launcher" [Fan-wiki].
  - The current wiki stats (rate of fire 1.5 s, ammo 4, reload 5 s, 750 u/s, explosives 45–70) come from an unsourced 2020-11-09 wiki edit. The usage prose still says "ammo clip of three" and "1 second rate of fire" [Fan-wiki].
  - The HUD ammo maximum varies by clip [Observed in `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/crops/gren_hud.jpg`]:
    - "/4": June 2013 (NJKRl54kc54_hq1) and Dec 2013 (6-bciTQmJn4_hq1/hq2).
    - "/6": 2014 clips (PLZG_TQe9YE_hq1/hq3, UBZwQSTEx1k_hq1).
    - "/3": 2015 clips (SJx-s0--z7I, ZEwCAXkkplc, sxYKPH3GAx0) and 2018 (6zv-C5K11i4).
  - Ammo+ equipment adds +1/+2 [Fan-wiki], so the base clip cannot be read from these counters alone [Inference].
  - **2026:** the same B-1000 shot appears in Steam screenshot `screen_04` and trailer 26.0–26.8 s; its capture date is unknown. A B-1000 in the 2026 showcase store frame carries an orange-and-white cylinder that is probably this weapon [Inference]. Presence in the 2026 build: [Unverified].
- **Look:**
  - Overall [Observed: `Grenader.png`, `Axecutioner.png` front view]: a chunky octagonal cylinder launcher fitted over the RIGHT forearm.
  - Body: riveted white panels framed in orange.
  - Muzzle: a black octagonal tube.
  - Hose: a black ribbed hose arcs over the top like a carry handle.
  - Sides: a black ribbed side grille and small orange fin spikes.
  - Length: about 0.4x B-1000's height [Inference], so about 0.6x Oliver [BBG News scale].
  - Colours: orange #E58D2B lit / #A75C10 shaded; white #E0D7CF; black #1E1F1C; gunmetal #686561 [Inference: sampled].
  - In `screen_04` (crop `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/crops/s04_b1000.jpg`), the same white-and-orange cylinder hangs muzzle-down, with two black hoses looping down its sides, on an orange-and-blue B-1000 [Observed].
- **Firing:**
  - Semi-auto, "shoots grenades in an arc" [Fan-wiki].
  - Reload look per the wiki: "the barrel will look like it's charging like the Power Glove, but with strong golden light, eventually forming a golden orb" [Fan-wiki]. This is CONFIRMED in-game [Observed: ZEwCAXkkplc_hq1 (0/3 RELOAD), sxYKPH3GAx0_hq2 (0/3 RELOAD), 6-bciTQmJn4_hq2 (0/4 RELOAD); zooms at `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/crops/gren_orb_zoom.jpg` and `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/crops/proj_zoom.jpg`].
  - What the frames show: a soft glowing ball about as wide as the muzzle or wider sits on the black muzzle cap. Its core is white-yellow #FBFDDE, then lemon #F5FC93, with an orange rim.
- **Projectile:**
  - The wiki says: "The projectile looks like it's set on fire with something else rotating or orbiting it, also emitting fire" [Fan-wiki].
  - What I saw [Observed, low-res: uDul96UTAJY_hq2, a 2013 clip; sxYKPH3GAx0_hq2, 2015]: a bright white-yellow ball (#FBFDDE core, gold halo #B69431) followed by a comet-like trail of yellow-orange blobs (#ECB235). In the 2015 frame a short yellow streak leaves the glowing muzzle.
  - The "orbiting" element is not resolvable at thumbnail resolution [Unverified].
  - Speed 750 u/s [Fan-wiki].
- **Impact / end result:**
  - The wiki says it explodes on contact with any player or surface "into a damaging, golden orb", "a rather huge and bright blast". Explosive damage 45–70, AoE 125/250. It knocks back airborne players. Self-damage risk is high [Fan-wiki].
  - [Observed, ambiguous: PLZG_TQe9YE_hq3 (`/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/crops/plzg_hq3_glow.jpg`)]: a soft golden dome of light with white sparks on the floor near a Grenader-armed B-1000 at 1/6. It is probably a Grenader blast [Inference].
- **Images viewed:**
  - https://static.wikia.nocookie.net/battlebears/images/0/00/Grenader.jpg/revision/latest?cb=20130722023941
  - Axecutioner.jpg
  - `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/steam_screens/screen_04.jpg`
  - Trailer 26.0–26.8 s (`/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/trailer/h_26.4.jpg`)
  - https://i.ytimg.com/vi/{6-bciTQmJn4,UBZwQSTEx1k,PLZG_TQe9YE,6zv-C5K11i4,SJx-s0--z7I,ZEwCAXkkplc,uDul96UTAJY,sxYKPH3GAx0,NJKRl54kc54}/hq1.jpg|hq2.jpg|hq3.jpg
- **Depiction for shorts:**
  - The launcher bucks upward and lobs a glowing gold ball with a short fiery comet tail in a high arc.
  - On contact it swells into a bright golden sphere wider than a bear, with a flash and spark spray, and knocks bears backward.
  - Between volleys a gold orb visibly "charges" on the muzzle.
  - The sphere's exact size and timing are [BBG News invention].
- **Confidence:** partial. The look and reload orb are observed; the projectile is observed at low resolution; the blast is documented only.

## Bearail Gun (primary; 2013 launch; seen in 2026 playtest)
- **Official text:** "This devastating laser creates a colossal explosion upon impact. Anything this powerful takes time so keep the enemies in your sight while it builds up. Trust us, vaporizing your friend has never been more fun!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Bearail_Gun). Beta text "Gun go boom" [Fan-wiki].
- **Status and history:**
  - Costs 110,000 Joules at level 1 [Fan-wiki]. A June 2013 fan description also gives "110K Joules" [Unverified].
  - "Upon its initial release, the Bearail Gun originally had no golden laser from the shooter to the target... SkyVu added the bullet effect in a later update" [Fan-wiki; version unknown].
  - The 2020 wiki edit changed explosives 55–75 to 75–90 and reload 3.5 s to 3 s [Fan-wiki].
  - **2026 [Observed]:**
    - The official BATTLE BEARS video "Battle Bears Gold launches Nov 4, 2026 - Official Playtest Highlights" (YouTube C7uFxvSZ10c; title [Canon]), thumbnail hq1 (zoom `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/crops/c7u_hq1_3x.jpg`): a maroon B-1000 arm holds the Bearail Gun up, the HUD reads 0/1, and a pale yellow streak runs diagonally to the distance.
    - The fan upload "Battle Bears Gold Closed Testing EXTENDED Footage" (M1kaa717, Sept 22 2026, jbdhitBvSL8 hq2/hq3) shows it at 0/1 on B-1000s wearing the Energy Barrier, with health "/180".
    - So it is in the 2026 playtest builds [Observed]. Whether it ships Nov 4 is [Unverified].
  - **BBH (2024):** the wiki lists B1000's attack as "Shock N Claw + Bearail Gun" [Fan-wiki]. The official site says "B1000s twin functionality attack 'Slice n Bite' offers both range and melee" [Canon, battlebears.com/pages/characters, re-fetched 2026-10-16].
- **Look:**
  - Overall [Observed: `Bearail_G.png`, `B-1000Skin.png`, `Gold1000.png`, `Orange1000.png`, `B-1000_default.png`, the T-shirt]: a long, slab-sided rectangular arm-gun on the RIGHT forearm.
  - Detailing: a black core with orange frame rails running its length, white end panels and a small round port underneath.
  - Idle pose: held vertical, muzzle up, or angled down.
  - Length: about 0.44x B-1000's height [Inference], so about 0.65x Oliver [BBG News scale].
  - Colours [Inference: sampled from File:B1000battlepackbundle.png]: orange #E58D2B, cream #F3ECD2, dark #362C26.
- **Firing:**
  - It "charges for 1 second, with a glowing gold light"; the light shows even when the user is cloaked [Fan-wiki].
  - The early concept sheet [Observed: `B-1000_concept_1.png`] reads "Charge-up" (a round emitter with a red glowing core), then a big red orb, "then a quick particle blast". The concept is red; the game is gold.
  - In-game at the moment of firing [Observed: q77eEbDzOiY_hq2 (2.5, Dec 2013), gNxIQSmQcJY_hq2, YUZdF7gPZeA_hq2; zooms `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/crops/bear_zoom.jpg` and `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/crops/beam_blast.jpg`]: with ammo 0/1 and RELOAD showing, a golden flare with spiky forward rays bursts at the muzzle, and long yellow-white streaks run toward the target.
- **Projectile:**
  - A hitscan beam: "no travel time, infinite range", zero dispersion [Fan-wiki].
  - The official in-game banner File:B1000battlepackbundle.png (wiki upload 2015-05-08) shows a straight, pencil-thin beam [Observed: `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/wiki_img/battlepack_3x.png`]. It is lemon yellow #EDDC31–#F7E95C with a pale core #F9F2A3.
  - In the trailer at 1.5 s, a thin straight yellow line crosses the arena at ground level [Observed: `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/trailer/g_1.5.jpg`]. Whose shot it is is [Unverified].
- **Impact / end result:**
  - "colossal explosion upon impact with any surface or player"; "exploding with a large AoE, emitting particles and light. It also produces a dim light wave". Explosives 75–90 (the prose says 70–90), AoE 90/220 [Fan-wiki].
  - The banner ends the beam in a starburst of pale-yellow sparks (#FDF4B3) [Observed].
  - In 2lmiVEBA8_8_hq3 a white-gold flash engulfs a target at close range [Observed, low-res].
  - At 4.5 s in the trailer, B-1000 levels the gun point-blank at a Demo before switching to the claw kill. No clean beam hit is shown [Observed].
- **Images viewed:**
  - https://static.wikia.nocookie.net/battlebears/images/b/b5/Bearail_G.jpg/revision/latest?cb=20130611084013
  - https://static.wikia.nocookie.net/battlebears/images/8/81/B1000battlepackbundle.png/revision/latest?cb=20150508223801
  - https://static.wikia.nocookie.net/battlebears/images/2/27/B-1000_concept_1.png/revision/latest?cb=20130604102154
  - B-1000Skin/Gold1000/Orange1000/B-1000_default PNGs in `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/wiki_img/png/`
  - https://i.ytimg.com/vi/{q77eEbDzOiY,3gnUeL5c73M,gNxIQSmQcJY,3ERPLdeYxJ8,lVaJGd2WhHc,sViZH-3shTM,2rxn3bl66Ms,APSoZxRCU0I,4OtByuL2bI4,YUZdF7gPZeA,2lmiVEBA8_8,C7uFxvSZ10c,jbdhitBvSL8}/hq1–hq3.jpg
  - Trailer frames `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/trailer/sheet_kill.jpg`
- **Depiction for shorts:**
  - B-1000 plants his feet and a gold glow builds at the muzzle for one beat.
  - A pencil-thin lemon-yellow beam snaps instantly to the target.
  - At the far end there is a big gold-white burst with spark rays, then a faint ring of light rolls outward, and the target pops into chunky pieces.
  - The ring's size and speed are [BBG News invention].
- **Confidence:** observed for the look, beam and muzzle flare. The explosion is partial.

## Energy Overflow (primary; BBG 2.3, Sept 27 2013; 2026 unconfirmed)
- **Official text:** "Sometimes you have hold it in and wait for the right moment, then release all over your enemy. What? I'm talking about this energy shotgun. What'd you think I was talking about?" [Game text via wiki] (https://battlebears.fandom.com/wiki/Energy_Overflow). It is innuendo, so don't quote it in a 13+ post.
- **Status and history:**
  - Added in 2.3 ("Assault class primary weapon - Energy Overflow") [Game text via wiki, Updates]. Costs 60 Gas [Fan-wiki].
  - 2.6.1 (Dec 2013): "Assault will no longer fire Energy Overflow on respawn" [Game text via wiki].
  - The 2020 wiki edit changed: charged damage 130 to 140, reload 6 s to 4 s, and the modifier to "+10% Speed". The prose still says "10% health reduction", an internal conflict [Fan-wiki].
  - A 2026-09-20 edit added "Charge Time 3" with no source [Fan-wiki].
  - BBH: the wiki lists it as B1000's Ultimate [Fan-wiki]. Official BBH text says only "his lethal Ultimate, which boasts stun capability" [Canon].
- **Look:**
  - Store render [Observed: `EnergyOverflow.png`]: a short, wide cylinder on the right forearm with white and orange armour plates, a grey hexagonal muzzle and a ring of small cyan lights around it.
  - In-game 2013–2014 [Observed: 1ykwGM9cCs4_hq3 (Oct 2013), aX1zTX9Nlfk_hq1, aB32umy6uT0_hq2; zoom `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/crops/eo_zoom.jpg`]: white fins with glowing cyan panels stick out of the barrel. This matches the HUD icon (gL12RHDQ_mI maxres) and the SkyVu-watermarked concept sheet `B1000_weapons2-3-787x1024.png`, which shows a closed finless cylinder and an open version with fins and cyan panels [Observed].
  - The fins probably fold open in use [Inference].
  - Length: about 0.33x B-1000's height [Inference], so about 0.5x Oliver.
  - Colours: orange #A15514 (shaded), white #DED6D0, gunmetal #736F68, black #1A1814; cyan glow (not sampled; use claw cyan #2BDCF1) [Inference].
- **Firing:**
  - A chargeable "energy shotgun": two uncharged shots of 45, or one full-charge blast of 140 that empties the clip. A partial charge uses 1 ammo, which regenerates [Fan-wiki].
  - While charging, "particles converge on the barrel"; at full charge "orbs of light will appear at the tip of the barrel" [Fan-wiki].
  - Very short range [Fan-wiki].
- **Projectile:**
  - Per the wiki, "a single golden burst of damaging energy" [Fan-wiki]. It is probably a hitscan spread like other shotguns [Inference].
  - [Observed, low-res: gL12RHDQ_mI_maxresdefault (2/2)]: short yellow-gold streaks fly ahead, and a flat yellow oval glow sits on the floor in front of B-1000.
- **Impact / end result:**
  - No explosive damage and no AoE [Fan-wiki].
  - [Observed: 1ykwGM9cCs4_hq3 at 0/2]: a yellow-white burst with spark rays on a white bear tagged "OLIVER".
- **Images viewed:**
  - https://static.wikia.nocookie.net/battlebears/images/2/2c/EnergyOverflow.jpg/revision/latest?cb=20130928011029
  - https://static.wikia.nocookie.net/battlebears/images/8/84/B1000_weapons2-3-787x1024.png/revision/latest?cb=20130924113344
  - https://i.ytimg.com/vi/{1ykwGM9cCs4,aB32umy6uT0,38x-uzcWvxk,okijlI9RQ9E,aX1zTX9Nlfk,gL12RHDQ_mI}/hq1–hq3.jpg
  - gL12RHDQ_mI maxresdefault.jpg
- **Depiction for shorts:**
  - The fins snap open and the cyan panels brighten as gold motes spiral into the muzzle.
  - On release, a short, fat cone of golden energy blasts out, and the target flashes and staggers or pops.
  - The fin-opening on charge is [BBG News invention, consistent with the concept sheet].
- **Confidence:** partial.

## Super Rapid Chain Gun / SRCG (primary; BBG 2.7, Jan 23 2014; 2026 unconfirmed)
- **Official text:** "Everything about B1000 is loud and explosive, so why not give him a chain gun that fires explosive bullets?" [Game text via wiki] (https://battlebears.fandom.com/wiki/Super_Rapid_Chain_Gun)
- **Status and history:**
  - Released in v2.7 per its own wiki page; the wiki Updates list omits it [Fan-wiki]. It appears on the 2.7 "NEW WEAPONS" card [Observed: WPVJTueNX1o_hq1; zoom `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/crops/wpv_hq1_3x.jpg`].
  - Price: the prose says 100 Gas; the infobox has said 60 Gas since the 2020 edit [Fan-wiki]. The prior researcher reported 100 Gas in File:SRCG.jpg (v2.7 store); I did not re-check it.
  - HUD clip [Observed]: 40/40 and 0/40 in a Nov 2015 clip (9wfcVslrjoU_hq1/hq3), matching the wiki's 40. A Jan 29 2014 clip (DNcZwCdJSIk) shows "/75" on a Satellite-wearing B-1000. That clip may show a launch clip size of 75 [Inference; Unverified].
  - The 2020 edit changed damage 8 to 5, explosive 5–7 to 2–4, rate of fire 0.09 to 0.08 s, and reload 5.7 to 5.25 s [Fan-wiki].
- **Look:**
  - Store render [Observed: `SRCG__r_.png`]: a wide orange-and-white drum on the right forearm. Stacked, stepped concentric rings narrow toward the front, ending in an orange end cap with a small black square port with several holes. A cyan light window sits on the side.
  - 2.7 card [Observed]: a silver ring section with white tick marks, a black multi-barrel cluster ringed in orange, and an orange-yellow capsule mounted on top.
  - Length: about 0.35x B-1000's height [Inference], so about 0.5x Oliver.
  - Colours: orange #A6621A, silver #818181, white #D5D6D6, cyan #278A98, black #13170F [Inference: sampled].
- **Firing:** full-auto minigun with "wind-up and wind-down delays". Rate of fire 0.08 s, dispersion 0.06; hitscan per the Bass Cannon trivia [Fan-wiki].
- **Projectile:**
  - "explosive bullets" [Game text via wiki].
  - [Observed, attribution uncertain: DNcZwCdJSIk_hq2/hq3, zoom `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/crops/srcg_lb_zoom.jpg`]: pale cyan-white streaks rise from beside B-1000 toward a target, which shows a small white-pink starburst. Because a Satellite is on his back, these may be Satellite missiles [Unverified].
- **Impact / end result:** 5 direct damage + 2–4 explosive per round, with a "noticeable AoE" of 50/100 [Fan-wiki].
- **Images viewed:**
  - https://static.wikia.nocookie.net/battlebears/images/4/45/SRCG_%28r%29.png/revision/latest?cb=20140125180656
  - https://i.ytimg.com/vi/{9wfcVslrjoU,rcAO0usVTAM,DNcZwCdJSIk,WPVJTueNX1o}/hq1–hq3.jpg
- **Depiction for shorts:**
  - The barrel cluster whines up to speed.
  - A rapid stream of tiny bright tracer rounds pops into small orange-gold puffs along the target area.
  - It whirs down after release.
  - The tracer and puff colours are [BBG News invention].
- **Confidence:** partial. The look is observed; the rounds are unknown.

## Lightning Bolt (primary; BBG 2.7, Jan 23 2014; 2026 unconfirmed)
- **Official text:** "Pew pew pew Lightning Bolt! What no explosion? At least it fires quickly and packs a whallop!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Lightning_Bolt)
- **Status and history:**
  - 2.7 "Assault primary - Lightning Bolt" [Game text via wiki, Updates]. Costs 150,000 Joules [Fan-wiki].
  - HUD "/3" in every clip I opened, from 2014 to a 2021 build labelled 2.53.6 [Observed: LXxMq6L-WuA, -ZQ7c0TYn2k, kSl4FDgIyD8, BROMHVU3Frs, 2usCJJKrJfY, LJyV35r98FM, 7osH2UbN6MM, jXdcze9skQY, rcAO0usVTAM]. This matches the wiki's ammo 3.
  - The 2020 edit changed rate of fire 1 s to 2 s and reload 5 s to 6 s [Fan-wiki].
- **Look:**
  - [Observed: `Lighting_bold__cr_.png`, Silver skin; 2.7 card icon]: a rounded orange-and-white arm cannon. Its black octagonal muzzle holds a glowing cyan lens, a cyan light strip with dots runs along its side, and a small black scope or tube sits on top.
  - Length: about 0.3x B-1000's height [Inference], so about 0.45x Oliver.
  - Colours: orange #B17A33, gunmetal #6C6E6E, black #1A1B1C [Inference: sampled].
- **Firing:** semi-automatic, "fully accurate", fires "in sync with the player's crosshairs", sniper-like [Fan-wiki].
- **Projectile:**
  - "will fire a purple bolt of damaging energy"; "no AoE, projectile or travel time" [Fan-wiki].
  - NOT observed in any frame I opened. The floating blue lightning-bolt shapes in LJyV35r98FM_hq3, jXdcze9skQY_hq2 and 2usCJJKrJfY_hq2 are map pickup or HUD icons, not shots [Observed; Inference].
- **Impact / end result:** no explosion: "What no explosion?" [Game text via wiki]. 50 damage [Fan-wiki].
- **Images viewed:**
  - https://static.wikia.nocookie.net/battlebears/images/d/dc/Lighting_bold_%28cr%29.png/revision/latest?cb=20140125012149
  - https://i.ytimg.com/vi/{LXxMq6L-WuA,-ZQ7c0TYn2k,kSl4FDgIyD8,BROMHVU3Frs,2usCJJKrJfY,LJyV35r98FM,7osH2UbN6MM,jXdcze9skQY,rcAO0usVTAM}/hq1–hq3.jpg
  - Crops `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/crops/lb_targets.jpg` and `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/crops/7os_hq3_streak.jpg`
- **Depiction for shorts:**
  - The cyan lens flashes and an instant, jagged purple bolt cracks from muzzle to target.
  - A small violet zap flashes on the target. No fireball.
  - Purple comes from the wiki; the bolt shape and flash are [BBG News invention].
- **Confidence:** partial. The look is observed; the bolt is documented only.

## Bass Cannon (primary; BBG 2.20, May 29 2015; 2026 unconfirmed)
- **Official text:** "Blow your opponents away with the Bass Canon! Explosive melody that does aoe damage " [Game text via wiki; "Canon" is misspelt in the original per wiki trivia] (https://battlebears.fandom.com/wiki/Bass_Cannon)
- **Status and history:**
  - 2.20 "New Weapons - Bass Cannon" [Game text via wiki, Updates].
  - A SkyVu Facebook post appears in a fan video thumbnail, "BATTLE BEARS GOLD | UPDATE 2.20 | COMING TODAY! 5-29-15" (YouTube cDW-mWikVAk hq2/hq3; zooms `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/crops/cdw_text.jpg` and `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/crops/cdw_hq3.jpg`) [Observed; SkyVu wording seen second-hand, original post not checked]. It reads:
    - "The update has been approved and will appear on your device with-in a few hours!"
    - "Check out the new items: -B1000 Bass Cannon"
    - "Loud & Proud Bundle -Bass Cannon -Super Size Me" plus a pistol item I could not read
    - "Readjusted prices for current items"
  - Price: its wiki screenshot shows "BUY NOW 100" gas [Observed: Bass_cannon_.jpg]. The infobox has said 60 Gas since 2020 [Fan-wiki].
  - HUD clip: "/31" in every 2.20–2.25 clip I opened (8u_UbesuFXU, GEU_TdbCy-g, JarAzKmr2QI, LTFb5KyA49c, XFFksUDewpE, aT85tycVwXM, arWWsxTEFao, td4osCU4LfQ) [Observed]. The wiki says ammo 20 (+5 with Ammo+1) [Fan-wiki]. The 2015 clip was probably about 31 [Inference].
- **Look:**
  - [Observed: `Bass_cannon_.png` store render and in-game frames]: a dark olive/black cylindrical cannon on the right forearm with an orange middle band, dark-blue rectangular windows and two round black ports.
  - Muzzle: a speaker or turbine disc, with curved white vanes over a pale-blue cone.
  - Length: about 0.3x B-1000's height [Inference], so about 0.45x Oliver.
  - Colours: black #141715, olive #32402E, orange #BB6C2C, window blue #18495F [Inference: sampled].
- **Firing:**
  - Continuous fire, 0.25 s per wave [Fan-wiki].
  - "It plays a generic dubstep loop that is paused and continued as the player stops and starts firing" [Fan-wiki].
- **Projectile:**
  - "emits cyan sound waves that explode on contact"; 1,200 u/s [Fan-wiki].
  - What I saw [Observed: GEU_TdbCy-g_hq1, aT85tycVwXM_hq3, arWWsxTEFao_hq2/hq3, JarAzKmr2QI_hq2, td4osCU4LfQ_hq2; sheet `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/crops/bass_teams.jpg` and zoom `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/crops/bass_zoom.jpg`]: two or three nested OCTAGONAL ring outlines, semi-transparent, bright cyan-to-blue (#58CAE3, #4589DC, #1879FD, pale #D8F9FD). They fly out from the speaker muzzle, each about as wide as a bear's torso.
  - In the 2.20 sneak peek (XFFksUDewpE_hq1) the rings are dark magenta-maroon (#580929) [Observed]. They may be team-coloured [Inference; Unverified].
- **Impact / end result:**
  - 10 direct damage + 10–20 explosive in a small radius (AoE 75/150) [Fan-wiki].
  - "Rarely, the Bass Cannon can blow your enemy away if they are hit by it while in midair" [Fan-wiki].
  - [Observed: arWWsxTEFao_hq3]: a smaller blue octagon with a white spark flare where a wave strikes near a target.
- **Images viewed:**
  - https://static.wikia.nocookie.net/battlebears/images/9/90/Bass_cannon_.jpg/revision/latest?cb=20150617005719
  - https://i.ytimg.com/vi/{arWWsxTEFao,td4osCU4LfQ,8u_UbesuFXU,LTFb5KyA49c,GEU_TdbCy-g,JarAzKmr2QI,A9Zqkr9L4X8,aT85tycVwXM,evq-fk6i8Eo,ZyfoISWsphc,XFFksUDewpE,cDW-mWikVAk}/hq1–hq3.jpg
- **Depiction for shorts:**
  - The speaker cone pumps, and nested cyan octagon rings thump out on the beat.
  - Each ring pops in a small blue-white spark burst on contact, and airborne targets get bounced away.
  - Use original music, not a real dubstep track. Beat-syncing the rings is [BBG News invention].
- **Confidence:** observed.

## Last Resort (secondary; 2013 launch default; later REMOVED; 2026 unconfirmed)
- **Official text:** "Winning takes sacrifice, and in this case that means blowing yourself up. Press and hold the fire button initiate a self-destruct sequence, wait 3 seconds and then boom!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Last_Resort)
- **Status and history:**
  - The current page is headed "NOTE: THIS WEAPON IS REMOVED" and says it "was the default secondary" [Fan-wiki]. Per the prior researcher's diff, the edit was made 2020-11-09.
  - No SkyVu note, version or date for the removal was found [Unverified].
  - It was in use in 2013: a June 4 2013 fan demo describes it as "Suicidal explosion like Whipped Cream" [Unverified: fan description], and an Oct 16 2013 fan clip is titled "Trying out Last Resort".
- **Look:**
  - [Observed: `Last_Resort.png`, `Last_Resort-Figure_2.png`; in play in NJKRl54kc54_hq1–3, mX-wRChpK1w_hq1, gL12RHDQ_mI_maxresdefault]: a BACKPACK of two stacked orange boxes with black panels.
  - Each box holds a large dark round speaker-like disc plus small round dials, with white triangle accents.
  - Size: about torso-wide and 0.3x B-1000's height [Inference], so about 0.45x Oliver.
  - Colours: orange #9B540D, black #1C1719, warm white #DACBC5 [Inference: sampled].
- **Firing:**
  - Hold fire to start a self-destruct. The official text says 3 s; the wiki's usage prose says 4 s.
  - Moving or releasing cancels it and starts a 3.5 s reload [Fan-wiki].
- **Projectile:** none. B-1000 is the bomb.
- **Impact / end result:**
  - 200–400 explosive damage with AoE 200/400, "the highest damage of any explosive weapon". It counts as a suicide [Fan-wiki].
  - Aftermath [Observed, low-res: mX-wRChpK1w_hq2, Oct 2013, overhead camera; zoom `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/crops/mx_hq2.jpg`]: the kill feed reads "SUICIDE", a dark grey smoke puff hangs in the air, and small red-and-white chunks lie scattered on the floor. hq3 shows the post-death scoreboard.
  - The blast itself was not observed.
- **Images viewed:**
  - https://static.wikia.nocookie.net/battlebears/images/e/e6/Last_Resort.jpg/revision/latest?cb=20130727003625
  - https://static.wikia.nocookie.net/battlebears/images/9/92/Last_Resort-Figure_2.jpg/revision/latest?cb=20131020201446
  - https://i.ytimg.com/vi/{mX-wRChpK1w,NJKRl54kc54,cke79KdKQ-M,gL12RHDQ_mI}/hq1–hq3.jpg
- **Depiction for shorts:**
  - B-1000 freezes in place while the pack's speaker discs flash and beep faster for 3 seconds.
  - Then a huge golden-white blast, and B-1000 pops into chunky robot parts (head, plates, bolts) that clatter down in a smoke puff. No gore.
  - The beep and flash count-in is [BBG News invention].
  - Label it a retired 2013 weapon.
- **Confidence:** partial.

## Metal Crush (secondary; 2013 launch; in the Steam trailer)
- **Official text:** "Render the space between you and your opponent meaningless in the most lethal and awesomest way possible." [Game text via wiki] (https://battlebears.fandom.com/wiki/Metal_Crush)
- **Status and history:**
  - Beta name "Leap N Destroy" [Fan-wiki].
  - It was sold in the official "TOOLS OF DESTRUCTION" bundle with Shock N Claw, Rusty Devil and Iron Bear for "375 GAS" [Observed: `Assaultsale.png`, 2013].
  - Price history:
    - v2.7 store: "METAL CRUSH BUY NOW! 100" gas [Observed: `Satellite_.png`, v2.7 store].
    - 2.20: "reduced from 100 gas cans to 70 gas cans" [Game text via wiki, Updates].
    - Now 60 Gas [Fan-wiki].
  - Reload behaviour changed in 2.0, 2.2 and 2.3 [Fan-wiki].
- **Look:**
  - [Observed: `Metal_Crush.png`, v2.7 store icon, YaXJyU2lAdc_hq1, 4dqiYnb-2kI_hq3, trailer 1.8–2.1 s (`/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/trailer/sheet_15.jpg`)]: a back unit of two riveted white plates, like folded wings, over orange lower sections perforated with round holes, on a black spine with an orange core.
  - Size: about 0.35x B-1000's height [Inference], so about 0.5x Oliver.
  - Colours: white #DBD4CE, gunmetal #89817C, orange #964C07, black #181514 [Inference: sampled].
- **Firing (the leap):**
  - "the Assault will leap through the air at high speed at the angle of roughly 35 degrees" [Fan-wiki].
  - In the trailer at 2.8–3.9 s [Observed: `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/trailer/sheet_leap.jpg`], B-1000 sails across the arena with a big orange-yellow fireball glowing at his body and an orange comet trail behind him. At 3.0 s a large yellow-orange flash fills the top of the frame.
  - After a leap (0/1, RELOAD) [Observed: YaXJyU2lAdc_hq1, 4dqiYnb-2kI_hq3; zoom `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/crops/mc_zoom.jpg`], the round holes glow hot orange-yellow like thruster vents.
  - Fan clip 7V4XQIPM2I4_hq2 shows a B-1000 high above a ramp [Observed].
- **Impact / end result:**
  - "the Assault class uses its left arm to smash the ground, creating a damage-dealing golden shockwave that spreads out like the splash made by the Happy Hour". 70–110 explosive (the prose says 55–110), AoE 125/400. He is immobile for 2.5 s after landing [Fan-wiki].
  - [Observed, ambiguous: 7V4XQIPM2I4_hq3]: yellow splats and yellow chevrons on the floor around a landed B-1000 at 0/1. They may be the shockwave or a floor decal [Unverified].
- **Images viewed:**
  - https://static.wikia.nocookie.net/battlebears/images/8/86/Metal_Crush.jpg/revision/latest?cb=20130727003810
  - https://static.wikia.nocookie.net/battlebears/images/4/40/Assaultsale.jpg/revision/latest?cb=20130831005445
  - https://static.wikia.nocookie.net/battlebears/images/0/0d/Satellite_.jpg/revision/latest?cb=20140124014354
  - https://i.ytimg.com/vi/{GNGxJ3MTuB4,YaXJyU2lAdc,4dqiYnb-2kI,5ZMF7tIjbyU,7V4XQIPM2I4,2rxn3bl66Ms,cke79KdKQ-M}/hq1–hq3.jpg
  - Trailer 1.5–3.9 s
- **Depiction for shorts:**
  - He crouches, the perforated vents flare orange, and he rockets up on a fire jet at a shallow ~35° arc.
  - He slams down left-arm-first, and a flat golden ring ripples across the floor, bouncing bears off their feet.
  - He stays stuck kneeling for a beat.
  - The ring's look is [BBG News invention, guided by the wiki's "golden shockwave"].
- **Confidence:** partial. The leap is observed; the shockwave is documented only.

## Energy Barrier (secondary; BBG 2.3; seen in 2026 playtest)
- **Official text:** "Make those pesky bullets less pesky with this brand new shield! Upon activation all damage recieved is reduced by 50%!" [Game text via wiki; "recieved" as quoted] (https://battlebears.fandom.com/wiki/Energy_Barrier)
- **Status and history:**
  - 2.3 "Assault class secondary weapon - Energy Barrier" [Game text via wiki]. Beta page name "Shield" [Fan-wiki].
  - "ENERGY BARRIER BUY NOW! 120,000" Joules in the v2.7 store [Observed: `Satellite_.png`].
  - The 2020 edit changed duration 6 s to 2 s and ammo 1 to 2 [Fan-wiki].
  - 2026: worn in the fan "Closed Testing EXTENDED Footage" (jbdhitBvSL8_hq2/hq3, Sept 22 2026) [Observed: `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/crops/jbd_zoom.jpg`].
- **Look:**
  - [Observed: `Energy_barrier.png`, many gameplay frames]: a rounded black-and-orange BACKPACK. Four white hexagonal pods at its corners each hold a dark round grille, with mirrored white-and-orange chevrons in the centre.
  - Concept notes [Observed: `B1000_weapons2-3-787x1024.png`, SkyVu watermark]: "Shield emits from Sides", "Shield emits from top when opened/initiated", "opens to emit Shield".
  - Size: about 0.35x B-1000's height [Inference].
  - Colours: white #D4C8C1, orange #A4590E, black #211C19 [Inference: sampled].
- **Firing:** activation self-buff. 2 s duration, 2 charges, 5 s reload [Fan-wiki].
- **Projectile:** none.
- **Impact / end result:**
  - "When activated, the player will begin to glow their team coloured, and all damage received will be weakened by 50%" [Fan-wiki].
  - Status Effects page: "No overhead icon shown" [Fan-wiki].
  - The glow was NOT observed. The green "+" shields in several frames are pickups [Inference].
- **Images viewed:**
  - https://static.wikia.nocookie.net/battlebears/images/9/97/Energy_barrier.jpg/revision/latest?cb=20130928085444
  - The concept sheet
  - https://i.ytimg.com/vi/{q77eEbDzOiY,sViZH-3shTM,jbdhitBvSL8,BROMHVU3Frs,kSl4FDgIyD8}/hq1–hq3.jpg
- **Depiction for shorts:**
  - The four pods pop open.
  - A thin shell of team-coloured light (red or blue) wraps B-1000 for 2 seconds, and incoming shots spark off it at half strength.
  - The shell's shape and the pod-opening are [BBG News invention].
- **Confidence:** partial.

## Smoke Screen (secondary; BBG 2.7; later the wiki default; 2026 unconfirmed)
- **Official text:** "B1000 has his own version of hide and seek. It is called: Hide in smoke and then kill everyone!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Smoke_Screen)
- **Status and history:**
  - 2.7 "Assault secondary - Smoke Screen" [Game text via wiki].
  - "SMOKE SCREEN BUY NOW! 100,000" Joules in the v2.7 store [Observed: `Satellite_.png`].
  - Since the 2020 edit the wiki lists it as "Default" [Fan-wiki]. I infer it replaced the removed Last Resort as default; when is unknown [Inference].
- **Look:**
  - [Observed: `Smoke_screen__cr_.png`, the 2.7 card, jf3f8Yx2j78, jXdcze9skQY, sxYKPH3GAx0]: a white, rounded, shield-shaped BACKPACK with a thick orange outline and segmented white panels.
  - Colours: white #E5E5E4, orange #9A591E [Inference: sampled].
- **Firing:** activation; 5 s cloud, 2 charges, 1 s cooldown, 3 s reload. "can only be activated directly from the Assault's backpack" [Fan-wiki].
- **Projectile:** none.
- **Impact / end result:**
  - "the Smoke Screen will instantly release a huge, harmless white cloud" that disorients enemies [Fan-wiki].
  - [Observed: sxYKPH3GAx0_hq3, a 2.23 clip of a B-1000 wearing this pack]: the screen is almost entirely white with only his arm visible. This is consistent with standing inside the cloud [Inference].
- **Images viewed:**
  - https://static.wikia.nocookie.net/battlebears/images/5/52/Smoke_screen_%28cr%29.jpg/revision/latest?cb=20140125015812
  - https://i.ytimg.com/vi/{jf3f8Yx2j78,sxYKPH3GAx0,jXdcze9skQY,WPVJTueNX1o}/hq1–hq3.jpg
- **Depiction for shorts:**
  - The pack's panels puff and a thick white cloud balloons out to fill the room in about a second.
  - Only his cyan eye-slits glow inside it.
  - The eye-glow beat is [BBG News invention].
- **Confidence:** partial.

## Satellite (secondary; BBG 2.7; 2026 unconfirmed)
- **Official text:** "A small orb that fires missiles whenever he fires, the satellite is a B1000's best friend!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Satellite)
- **Status and history:**
  - 2.7 "Assault secondary - Satellite" [Game text via wiki].
  - The v2.7 store shows "SATELLITE BUY NOW! 100" gas, with a "2.7" version label [Observed: `Satellite_.png`]. The wiki now says 60 gas [Fan-wiki].
  - The page is a stub [Fan-wiki].
- **Look:**
  - [Observed: `Satellite__cr_.png`, `Satellite_.png`, DNcZwCdJSIk_hq1–hq3]: on B-1000's BACK, an orange octagonal frame cradles a glossy white sphere with a cyan, liquid-like band inside it. Two cyan lights sit on top of the frame.
  - Size: about 0.3x B-1000's height [Inference].
  - Colours: orange #A1591C, white #E1E1E1, cyan #25BFE4 [Inference: sampled].
  - No image shows it detaching or orbiting [Unverified].
- **Firing:**
  - It "fires missiles whenever he fires" [Game text via wiki]: "the Satellite will fire eight missiles" and then reloads for 5 s [Fan-wiki].
  - Infobox: "8 disc fires", duration 15 s [Fan-wiki].
- **Projectile:**
  - Missiles at 1,500 u/s [Fan-wiki].
  - [Observed, attribution uncertain: DNcZwCdJSIk_hq2/hq3]: pale cyan-white streaks rising toward a target. These may be the missiles [Inference; Unverified].
- **Impact / end result:** 20–50 explosive, AoE 125/250 [Fan-wiki].
- **Images viewed:**
  - https://static.wikia.nocookie.net/battlebears/images/1/1c/Satellite_%28cr%29.jpg/revision/latest?cb=20140125015712
  - Satellite_.jpg (above)
  - https://i.ytimg.com/vi/{DNcZwCdJSIk,6zv-C5K11i4,_J4ELhJhKzM,uDul96UTAJY}/hq1–hq3.jpg
- **Depiction for shorts:**
  - The orb stays docked in its cradle.
  - Whenever B-1000 shoots, the orb's cyan band flares and it spits small white missiles with cyan exhaust that pop in small gold blasts.
  - The missile look is [BBG News invention].
  - Keep it docked unless the short labels a free-flying orb as invention.
- **Confidence:** partial.

## Axecutioner (melee, default; 2013 launch; 2026 unconfirmed)
- **Official text:** "Why carry an axe in your hand when you can replace your hand with an axe?" [Game text via wiki] (https://battlebears.fandom.com/wiki/Axecutioner). Beta text "Smack you with axe, you go boom." [Fan-wiki trivia].
- **Status and history:** default melee [Fan-wiki, Category:Default]. Early name "Axe Time" [Fan-wiki]. The 2020 edit changed damage 30 to 70 [Fan-wiki].
- **Look:**
  - [Observed: `Axecutioner.png`; back views in `Last_Resort.png` and `Metal_Crush.png`]: B-1000's LEFT forearm ends in an axe.
  - Head: a grey, stone-textured block with a hammer-like back carries a large curved grey-white blade with scratches and orange tabs.
  - Attachment: a white ribbed sleeve and an orange octagonal cuff with white squares, plus an orange fin.
  - It has no glow and no cyan.
  - Size: blade span about 0.35x B-1000's height [Inference], so about 0.5x Oliver.
  - Colours: stone grey #7F7A74, blade white #F0EAE2, orange #9C500B, black #181615 [Inference: sampled].
- **Firing:** melee swing. 70 damage, no stat modifiers [Fan-wiki].
- **Projectile:** none.
- **Impact / end result:** the swing and hit were not observed. Kills follow the house break-apart style [Inference].
- **Images viewed:** https://static.wikia.nocookie.net/battlebears/images/3/36/Axecutioner.jpg/revision/latest?cb=20130727002359 ; Last_Resort.jpg ; Metal_Crush.jpg
- **Depiction for shorts:**
  - A heavy overhand chop with a metal clang and a spray of sparks.
  - The target crumples or breaks into chunky pieces.
  - The axe never glows.
  - Clang and sparks are [BBG News invention].
- **Confidence:** partial.

## Shock N Claw (melee; 2013 launch; signature promo melee; seen in 2026 playtest)
- **Official text:** "As if a half-ton murderous robot wasn't dangerous enough on its own, we've gone and added 3 razor sharp claws, you're welcome." [Game text via wiki] (https://battlebears.fandom.com/wiki/Shock_N_Claw)
- **Status and history:**
  - Costs 45,000 Joules [Fan-wiki]. Part of the TOOLS OF DESTRUCTION bundle (375 GAS) [Observed: `Assaultsale.png`].
  - 45 damage with a +30% special-speed modifier [Fan-wiki].
  - 2026: cyan claw blades are visible on a B-1000 in jbdhitBvSL8_hq3 [Observed, low-res].
  - BBH: the wiki lists "Shock N Claw + Bearail Gun" [Fan-wiki].
- **Look:**
  - [Observed: `Shock_N_Claw.png`, `B-1000Skin.png`, `Orange1000.png`, the T-shirt, trailer 1.7–6.6 s]: a black/orange/white armoured gauntlet on the LEFT forearm with THREE long, parallel, translucent cyan blades streaked with white.
  - A white segmented hose with cyan rings loops from the gauntlet back to the arm.
  - Blade length: about 0.4x B-1000's height [Inference], so about 0.6x Oliver.
  - Colours: cyan #2BDCF1, pale cyan #A6ECF3, white streak #F3FBFB, black #191A17 [Inference: sampled].
  - The 2D portrait draws them longer and mirrored [Observed].
- **Firing:**
  - "used in a swinging motion" [Fan-wiki].
  - No electric effect is documented; the name is a pun on "Shock and Awe" [Fan-wiki].
- **Projectile:** none.
- **Impact / end result** [Observed: Steam trailer 4.5–5.4 s; frames `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/trailer/sheet_kill.jpg`]:
  - B-1000 sweeps the claws up into a green Demo at point-blank range.
  - A tall yellow-white light column flares behind him (4.6 s).
  - Horizontal orange-yellow streaks fill the frame (4.7–5.1 s).
  - The Demo comes apart into separate chunky pieces (head with blue bandana, torso, arm) that fly upward.
  - The claws then sweep across the camera (5.4 s).
  - Whether the flash and streaks are the claw-hit effect or trailer styling is [Unverified].
- **Images viewed:**
  - https://static.wikia.nocookie.net/battlebears/images/7/73/Shock_N_Claw.jpg/revision/latest?cb=20130727002433
  - Assaultsale.jpg ; B-1000.png ; Assaultimage.jpg ; the T-shirt PNG
  - Trailer frames
  - https://i.ytimg.com/vi/jbdhitBvSL8/hq3.jpg
- **Depiction for shorts:**
  - A fast rising three-blade swipe with cyan motion trails.
  - On a kill, the victim pops into chunky toy-like pieces in a gold-orange flash.
  - No electricity unless it is labelled [BBG News invention].
- **Confidence:** observed.

## Primus Sword (melee; BBG 2.21, July 3 2015; probably in 2026 builds)
- **Official text:** "A swing of the primus sword can send even the mightiest bear retreating with their tails behind their legs." [Game text via wiki] (https://battlebears.fandom.com/wiki/Primus_Sword)
- **Status and history:**
  - 2.21 "New Melees ... Primus Sword" [Game text via wiki, Updates]. Costs 60 Gas (75 before the 2020 edit), level 5 lock. 85 damage, "the highest damaging melee", +10% health [Fan-wiki].
  - Trivia: "a reference to the sword of Primus in Transfomers" [Fan-wiki].
  - **2026:**
    - Official highlights C7uFxvSZ10c_hq1: a pink-outlined arrowhead blade with a cyan-white inner line beside the Bearail Gun [Observed].
    - JustNubz showcase (-lAtv-j9Sms_hq1; zoom `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/crops/show_hq1_3x.jpg`): a holly-wreathed brown B-1000 in the 2026 store holds a pink-and-silver blade with an X-shaped guard. The same screen lists the taunts Growth Spurt, Falling Apart and "BIG ROBO BUY NOW! 100" [Observed].
    - That both blades are the Primus Sword is [Inference].
- **Look:**
  - [Observed: `Image4.png`, 254x303 px, upscaled `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/b1000-dossier/r2/crops/image4_4x.png`]: a long, flat, angular silver-grey blade (#A9B6BB) with hot-pink edge trim (#DB0954), a thin inner line, and an angular X-shaped crossguard in dark magenta (#701531).
  - It is the longest B-1000 weapon: about 0.7x B-1000's height [Inference], so about 1.0x Oliver.
  - The image shows it on a bright red skin that matches Mega Ursatron [Inference].
- **Firing:** melee swing (not observed).
- **Projectile:** none.
- **Impact / end result:** 85 damage [Fan-wiki]. The hit was not observed.
- **Images viewed:**
  - https://static.wikia.nocookie.net/battlebears/images/1/1a/Image4.PNG/revision/latest?cb=20150705194620
  - https://i.ytimg.com/vi/C7uFxvSZ10c/hq1.jpg
  - https://i.ytimg.com/vi/-lAtv-j9Sms/hq1.jpg
- **Depiction for shorts:**
  - A wide, heavy two-handed-feeling slash with a pink edge-glint, sending the target tumbling back ("tails behind their legs").
  - The glint is [BBG News invention].
- **Confidence:** partial.

## Corrections for the character file (/home/user/thallo-site/bbg-news-repo/characters/b-1000.md)
1. **Gun-arm and blade line.**
   - Current: "**Weapons:** orange-and-white gun-arm, blue energy blade [Observed: screenshot]; gun-arm right, claw-blades left [Observed: T-shirt]."
   - Correction: in the default screenshot (File:B-1000Skin.jpg) the gun-arm is the BEARAIL GUN, a long black slab with orange frame rails and white end panels. The "blue energy blade" is the SHOCK N CLAW: three translucent cyan claw blades with a looping white-and-cyan hose. The T-shirt layout is correct: gun on his right arm, claws on his left.
2. **Gun-arm identification.**
   - Current: "gun-arm = Grenader is [Inference]"
   - Correction: this is wrong. The Grenader is a fat octagonal white-and-orange launcher with a black looping hose (File:Grenader.jpg). The gun-arm in the default screenshots is the Bearail Gun.
3. **Defaults.**
   - Current: "Defaults: Grenader ("does the throwing for you"), Last Resort ("wait 3 seconds and then boom!"), Axecutioner ("replace your hand with an axe")"
   - Correction: make it era-dependent:
     - 2013 launch defaults: Grenader, Last Resort, Axecutioner [Fan-wiki].
     - The wiki now marks Last Resort "REMOVED" and lists Smoke Screen as the default secondary. No SkyVu date is known.
4. **Extras list.**
   - Current: "Extras: Satellite, Smoke Screen, chain gun, Shock N Claw [Fan-wiki]."
   - Correction: the kit has 14 items. Add Bearail Gun, Energy Overflow, Lightning Bolt and Bass Cannon (primaries); Metal Crush and Energy Barrier (secondaries); and Primus Sword (melee).
5. **Satellite in idle.**
   - Current: "**Idle:** slow scanning sweeps; the Satellite circles him like a pet [BBG News invention]."
   - Correction: keep the label, but every image shows the Satellite docked in an orange cradle on his back. Draw it docked unless the gag is clearly flagged as invention.
6. **Prompt pack weapons.**
   - Current: "right forearm a chunky orange-and-white grenade-launcher arm, left forearm a heavy axe blade with a glowing cyan edge"
   - Correction: this mixes weapons; the axe never glows. Pick one loadout:
     - (a) Wiki defaults: right forearm a fat octagonal white-and-orange grenade launcher with a black ribbed hose looping over it; left forearm a grey stone-textured battle-axe head with a curved, scratched grey-white blade, orange cuff, no glow.
     - (b) Signature: right forearm a long black rectangular rail-gun with orange frame rails and white end panels; left forearm a gauntlet with three long translucent cyan claw blades and a looping white-and-cyan hose; back a white winged jump-pack with orange perforated vents.
7. **Colours line.**
   - Current: "Unsampled estimates: eyes #5FE3FF, gun-arm orange #E07B2C / white #E8E6E1"
   - Correction: now sampled from official in-game art: eye cyan about #38D6D7; hardware orange about #E58D2B lit (#A75C10 shaded); cream-white #F3ECD2 / #E0D7CF; claw cyan #2BDCF1.
8. **"Drone" wording.**
   - Current: "has a drone "best friend""
   - Correction: SkyVu's text calls it "A small orb that fires missiles". Say "orb", not "drone", which implies free flight.
9. **Open question on the left arm.**
   - Current open question: "axe, blade or claws as the default left arm"
   - Answer: the default melee is the Axecutioner (axe) [Fan-wiki]. The Shock N Claw (45,000 Joules) is the promo/signature melee seen in the trailer, the T-shirt and most renders [Observed].
10. **Open question on the 2026 build.**
    - Current open question: "what the 2026 build keeps"
    - Partial answer: official and fan 2026 playtest thumbnails show the Bearail Gun, Energy Barrier and Shock N Claw [Observed], plus a pink X-guard blade that is probably the Primus Sword [Inference]. The other 10 items are unconfirmed.

## Open questions
- When and why was Last Resort removed (the wiki notes it only from 2020-11-09)? Is it in the 2026 build?
- Which of the 14 weapons ship in the Nov 4 2026 build? Only the Bearail Gun, Energy Barrier and Shock N Claw (plus a probable Primus Sword) are seen in 2026 footage.
- What does the Grenader blast look like on camera, how big is it, and what is the "rotating or orbiting" part of the shell?
- What does the Lightning Bolt's "purple bolt" look like? No frame shows it.
- What do the SRCG rounds and impacts look like? Was its launch clip 75 (Jan 2014 HUD) rather than 40?
- What do the Satellite missiles look like? Does the orb ever leave its cradle?
- What does the Metal Crush golden landing shockwave look like (size, colour, ring vs dome)?
- What do the Energy Barrier team-colour glow and the Smoke Screen cloud volume look like?
- Bass Cannon rings: cyan in most clips but maroon in the 2.20 sneak peek. Are they team-coloured? Clip size 31 (2015 HUD) vs 20 (wiki)?
- Do the Energy Overflow's cyan fins fold out only when charging?
- In the trailer claw kill, are the light column and orange streaks an in-game hit effect or trailer editing? Is that footage 2013 or 2026?
- Grenader clip size history: /4 (2013), /6 (2014), /3 (2015). Which of these come from equipment?
- BBH: is "Slice n Bite" a copy error, and what is the stun Ultimate's official name?
- SkyVu's own 2.3, 2.7, 2.20 and 2.21 release notes could not be re-read because the Internet Archive was offline. Retry the archived battlebears.com change-log URLs.
