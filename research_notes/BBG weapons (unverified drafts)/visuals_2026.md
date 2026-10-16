# BBG 2026 re-release: weapon changes

This dossier compares the weapons of the 2026 re-release of *Battle Bears Gold* (Steam PC, iOS and Google Play, Nov 4, 2026) with the 2013–2021 game. It covers what SkyVu has said, what official 2026 images show, what fan playtest uploads show (titles, descriptions and thumbnails only), and how the fan wiki changed in 2026.

**Sources I reached:**
- The Steam store API for app 4408320: store text, 5 screenshots, the header and a 1.4 s embedded store video.
- The Steam news API: all 7 BBG posts from Feb 24 to Oct 14, 2026, plus their images.
- The official "Battle Bears Gold Premium - Trailer" (54 s), as local frames.
- battlebears.com and play.battlebears.com (the official sign-up page).
- YouTube metadata through the innertube `next` endpoint (exact titles, descriptions, dates and chapters) for 10 official and about 16 fan videos, and their thumbnails.
- The fan-wiki API: class and item pages, and the full 2026 recent-changes log.

**Not reachable:**
- YouTube video, storyboards and captions (LOGIN_REQUIRED; the transcript API returned FAILED_PRECONDITION). **I have not watched any video.** That includes the JustNubz showcase, the Oct 12 Q&A and the livestreams.
- Reddit (blocked).
- Discord (not accessible). No Discord-sourced weapon claim turned up on the open web.
- Web search, which returned nothing about the 2026 re-release.

Archive.org was not needed.

## Bottom line
- **SkyVu has not announced any new, removed, rebalanced or reworked weapon for 2026** [Inference: none of the store text, 7 Steam posts, battlebears.com, play.battlebears.com or official YouTube descriptions mention one].
- SkyVu's official wording is "packed with new modes, maps, skins and more!" [Canon] (battlebears.com) and "new stuff!" [Canon] (YouTube descriptions).
- Its teaser frames read "SAME / ICONIC / GAMEPLAY" [Observed: official teaser thumbnail https://i.ytimg.com/vi/d2ByJWrsoec/hq1.jpg, low-res].
- The final playtest build lists "LIGHTING, EFFECT & TEXTURE IMPROVEMENTS" [Canon: Oct 14 Steam post image]. So weapon effects may *look* somewhat different from 2013 even where the weapons are unchanged [Inference].
- **The Steam trailer and all five Steam screenshots show 2013 footage, not the 2026 build.** They document the 2013 look [Inference, strong; see the trailer section].
- **Confirmed in 2026, by name in an official source:** A Salt Rifle, Bearzooka and Turkish SW Boots [Canon].
- **Seen in 2026 builds (official or fan thumbnails):** Bearzooka; A Salt Rifle (HUD); Grenader-style gun-arm plus Axecutioner (B-1000 default); Crossbow, Fairy's Dust and Battering Ram (loadout text); Whack-Tus; a white-and-orange B-1000 gun-arm that is probably the Bearail Gun; a yellow ray that is probably the Gamma Ray; the O.C.O. Gauntlet and a fan-reported "Dark OCO Gauntlet".
- **Everything else is unknown for 2026,** and the 2026 counts on Steam roughly match the 2013–2021 roster.

## Official 2026 statements that touch weapons (sub-topic)
- **Steam store:**
  - "Grab your A Salt Rifle, Bearzooka and those Turkish SW Boots and fight it out with friends across beloved Battle Bears locations." [Canon]
  - "Try thousands of unique LOADOUT combos: 80+ PRIMARY WEAPONS / 60+ SECONDARY WEAPONS / 50+ MELEES / 10 SPECIAL EQUIPMENT / 200+ COSMETIC ITEMS" [Canon]
  - "Choose from 11 unique classes, mix hundreds of thousands of loadout combinations" [Canon]
  - "Additional note: All assets in this game are created by human artists." [Canon]
  - Source: https://store.steampowered.com/api/appdetails?appids=4408320
- **battlebears.com:** "This year we're bringing it back to Steam PC and Mobile, packed with new modes, maps, skins and more!" [Canon] (https://battlebears.com/).
- **play.battlebears.com** says "Play the demo on Steam from October 19-26" [Canon]. It has no weapon text [Inference]. Its five gallery images are the five Steam screenshots (pixel MSE ≈ 0.5) [Observed via pixel comparison].
- **Steam news** [Canon] (https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=4408320):
  - Jul 6: "There won't be any new features in this build and any progress made will not carry over to launch."
  - Jul 28: "An experimental new gamemode."
  - Aug 19: "New Map: Sky World."
  - Oct 14: "Headline additions: -Custom keybinds -Jukebox -UI controller support -Lighting improvements -Lots of bug fixes"
  - The Oct 14 banner also lists "-REDEEM CODE SYSTEM -ANDROID SUPPORT … -LIGHTING, EFFECT & TEXTURE IMPROVEMENTS" [Canon, image text; Observed: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/sheets/C.png].
  - The same Oct 14 post asks testers to "record some footage, ideally on PC and without the UI" for "our Steam and store pages" [Canon]. Store visuals may therefore be replaced [Inference].
- **Official YouTube descriptions** (@battlebears):
  - "BBG LAUNCHES NOV 4 on Steam & Mobile with new stuff!" [Canon] (d2ByJWrsoec, Oct 2).
  - "Gameplay highlights from the new Sky Pirates map!" [Canon] (r91WkR10W2A, Aug 31).
  - "Highlights from our first two Discord playtests" [Canon] (C7uFxvSZ10c, Aug 16).
  - "CEO Ben Vu answers the most-asked BBG questions!" [Canon] (pmE2jKQLSms, Oct 12; not transcribed).
  - None mentions weapons [Inference].
  - The Aug 21 livestream (xP27fWSCSKs) shows a chapter "Character and loadout showcase" at 9:24 [Unverified authorship: the chapter titles may be auto-generated]. Unwatched.

## Roster size: Steam counts vs the 2013–2021 wiki roster (sub-topic)
- **Wiki class pages** total 76 primaries, 64 secondaries and 46 melees [Fan-wiki: weapons sections of the 11 "(BBG)" class pages]. The lists are incomplete: Hazard Toy, an Assassin primary, is missing from "Assassin (BBG)" [Fan-wiki].
- **Specials:** the wiki says "there are currently 10 specials available" [Fan-wiki] (Specials page). That matches Steam's "10 SPECIAL EQUIPMENT" [Canon].
- **Comparison:** Steam's "80+" primaries and "50+" melees are a few above the wiki lists, and "60+" secondaries fits [Inference]. It cannot be told whether 2026 adds a few items or the wiki is simply incomplete [Unverified].

## Builds seen in 2026 footage (sub-topic)
- **July playtest builds show "2.54.0"** on screen [Observed in fan thumbnails: https://i.ytimg.com/vi/hBchsfEdeDM/hq1.jpg, https://i.ytimg.com/vi/-RSuAlfOUow/hq3.jpg, https://i.ytimg.com/vi/f4O-9_3WznQ/hq1.jpg].
- **Later builds** [Observed: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/crops/versions.png]:

  | Version on screen | Video | Date |
  |---|---|---|
  | "3.0.0" | Official highlights | Aug 16 |
  | "3.0.2" | JustNubz Playtest #3 | Aug 21 |
  | "3.0.3" | Official Sky Pirates thumbnail | Aug 31 |
  | "3.0.5_2026.11.19_B1" | JustNubz showcase | Sep 20 |

- **Context:** the wiki's version table stops at 2.25 [Fan-wiki]. "2.54.0" is probably the late legacy client, matching "no new features" in July, and 3.0.x is the re-release branch [Inference].

## The Steam trailer is 2013 footage (sub-topic)
- **Official text:** the title is "Battle Bears Gold Premium - Trailer" [Canon] (Steam movie 257411324). "Premium" is not explained anywhere I found [Unverified].
- **Evidence it is 2013 footage:**
  - The 2013 YouTube trailer is "BATTLE BEARS GOLD Trailer: Award-Winning Multiplayer Shooter Game" (May 30, 2013). Its description reads "New Assault Class: The B-1000 -9 skins available! -2 Primary Weapons! -2 Secondary Weapons! -2 Melee Weapons!" [Canon] (https://www.youtube.com/watch?v=rfAyqVJrli4).
  - Its hq1, hq2, hq3 and maxres thumbnails match Steam-trailer frames at 11.9 s, 29.0 s, 42.8 s and 29.9 s. Pixel MSE is 77, 495, 72 and 54, against a median of about 9,000 [Observed via pixel comparison].
  - The 2013 video runs about 69 s (YouTube heatmap) against 54 s on Steam [Inference]. So the Steam trailer is a re-edit of the 2013 launch trailer [Inference].
  - Only the 8 launch classes get cards (B-1000, Graham, Astoria, Wil, Tillman, Huggable, Riggs, Oliver), with no Botch, Saberi or Sanchez [Observed].
  - The current trailer files carry Aug 28, 2026 URL timestamps [Inference from the Unix `t=` value].
- **The five Steam screenshots are frames of this trailer** [Observed: pixel best match, MSE 237–1,214 against medians of 9,152–12,627]:

  | Screenshot | Trailer time |
  |---|---|
  | screen_00 | 36.4 s |
  | screen_01 | 30.7 s |
  | screen_02 | 50.6 s |
  | screen_03 | 9.8 s |
  | screen_04 | 26.4 s |

- **Weapon shots in the trailer** (2013 visuals; IDs are [Inference] unless stated):

  | Time | What happens [Observed] | Likely weapon [Inference] |
  |---|---|---|
  | 1.5–3.5 s, mine map | B-1000 (maroon armour, white and orange shoulder plates) has a three-blade glowing cyan claw on one arm and an orange-and-black gun-arm on the other. At 2.5 s it fires an orange fireball (core ≈ #F86808 to #FFA030); at 3.0 s it bursts on an airborne target. Blue orbs with cyan zigzag lightning hover overhead (unidentified). At 3.5 s a pink figure shoots a vertical rainbow streak. | Grenader for the gun-arm |
  | 4.0–5.0 s | A green-skinned, blue-headbanded Oliver shoulders the coral-red Bearzooka while huge orange flame streaks fill the frame. | Bearzooka |
  | 7.0–10.5 s | Graham (rainbow cap, from behind) in the mine. A magenta laser streak crosses. At 8.5 s a yellow-and-black radiation trefoil hovers over a target; at 9.0–10.0 s a yellow cube-cluster blast with white hexagonal floor rings, a white dome edged with cyan lightning, and flying orange bits. | Gamma Ray irradiate-then-explode |
  | 12.0–13.5 s, temple map | A thin white zigzag line reaches a white-headed bear in black, who bursts into stylized orange flame tongues (burning) and collapses face-down. A red translucent horned shape floats nearby (unidentified). | none named |
  | 14.0–16.0 s | A huge magenta faceted cloud swallows the stairs; Astoria runs out of it. | Fairy's Dust |
  | 18.5–22.0 s | Wil cries and is engulfed by a yellow-orange blast, then flung. A blue-team panda holds a purple-grey drum cannon with a gold muzzle ring, and fire blooms beside it (unidentified Demo weapon). | none named |
  | 24.0–27.5 s | Missile-cam of an olive shell approaching a space station. A yellow canister with a black trefoil descends in a vertical yellow light column into a red-and-white room, then a giant flat-shaded yellow-white blast (≈ #FCE454) flings red armour pieces. | Phat Man |
  | 30.0–32.5 s | A pink Huggable dashes in trailing magenta crystal shards. A white-yellow starburst hits Astoria (teal mask, blue polka-dot dress, dark-green sniper rifle), who ends face-down. | unidentified Huggable dash |
  | 34.5–36.6 s | Riggs in a red cracked-rock skin fires a black gun with purple LED panels. It shoots a pink tiered dome with a magenta spiral trail, and yellow stars appear at the target's feet. He then punches a gold Huggable with a bandage-wrapped glove spiked with pale-green crystals. | glove = Barbed Gloves; the gun is unidentified |
  | 38.6–41.0 s, lava cave | A bear in an orange hard hat fires a straight yellow beam with white ripple rings at the muzzle. A white-and-blue bear with a dark-blue disc (pink-purple circuitry) fires a thin magenta beam, and the hard-hat bear falls. | beam = Gamma Ray |
  | 43–53.5 s, aerial shots | Yellow tracer dots, a golden half-dome blast (47.0 s), pink laser lines, a yellow-orange cube blast with a white shock ring (50.5 s), a vertical yellow-orange cone, then orange octagonal ring shockwaves and white smoke (52.5–53.5 s). | none named |

- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/frames/trsheets/sheet_00.png through sheet_08.png (built from /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/trailer/t_*.jpg)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/frames/full/p_b1000a.png, p_b1000b.png, p_graham.png, p_astoria.png, p_wil.png, p_wil2.png, p_till.png, p_hug.png, p_riggs.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/sheets/S.png (screen_00–04 and the header)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/crops/bbg13_sheet.png (2013 YouTube thumbnails)
- **Depiction for shorts:** use the trailer only as a 2013 look reference. Do not caption it as "2026 gameplay" [Inference].
- **Confidence:** observed (2013 visuals) / documented (that it is 2013 footage, by inference).

## Fan showcase and fan playtest uploads (sub-topic)
- **JustNubz showcase:**
  - Title: "BBG All Classes Showcase [Skins, Taunts, Weapons, and Melee] (from Closed Playtest #4)" (Sep 20, 2026).
  - Description: "As the title states, showcasing all skins, taunts, primaries, secondaries, and melee in the closed playtest of BBG (the 4th one)". Chapters run from "0:00 Assault (B-1000)" to "47:23 Arbiter (Sanchez)".
  - This is the fan's text [Unverified] (https://www.youtube.com/watch?v=-lAtv-j9Sms). I did not watch the video.
  - Its thumbnails show [Observed: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/sheets/J.png]:
    - "SKIN THE INCREDIBLE RIGGS" (green Hulk-parody Riggs), build 3.0.5.
    - A Huggable with green cactus wrist-clubs (Whack-Tus).
    - A B-1000-like figure in a festive skin with a red crystalline sword and an orange-and-white gun-arm. The sword is the Primus Sword only by [Inference].
    - A taunt list reading "GROWTH SPURT / FALLING APART / BIG ROBO".
- **Other fan uploads, all dated 2026** (titles and descriptions are [Unverified] fan text):
  - Slinkster: "Battle Bears Gold Beta Test #2", "#3" and "#4".
  - JustNubz: "Closed Playtest #2 Match 1–8", "Playtest #3 Part 1–3", "Playtest #4 (Raw 3 Hours…)", "Playtest #4 1v1 w/ Gold44 (Bonus)" and "BBG Tutorial Speedrun".
  - anpanmannix: "Battle Bears Gold Item descriptions and Overview" (Jul 30). Its chapters include "Oliver Primaries", "Special Items" and "Equipment".
  - foyth: "i play the bbg beta with bearail" (Sep 30).
  - droid BBG: "BATTLE BEARS GOLD Is More INTENSE Than I Remember".
  - Thumbnails viewed: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/yt/sheets_more/more_0.png through more_3.png, and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/crops/fan_g1.png through fan_g6.png.

## 2026 wiki edits (sub-topic)
The wiki's whole recent-changes log has 7 edits, all by Alphabbr, Sep 18–23, 2026 [Fan-wiki] (https://battlebears.fandom.com/api.php?action=query&list=recentchanges). None cites a 2026 build or source [Inference]. The Gold Digger edit says "this got updated … some time ago", which suggests old knowledge [Inference].
- **Hazard Toy** (Assassin primary): "Explosives 35-50 → 25-50" and "Damage 5 → 4" [Fan-wiki]. Its in-game text: "Banned from elementary schools world wide, this weapon is as dangerous as it looks!" [Game text via wiki]. Its trivia says it "is based off of the Fidget Spinner" and it "poisons enemies caught in the radius" [Fan-wiki].
- **Energy Overflow** (Assault primary): added "Charge Time = 3" [Fan-wiki]. The wiki describes "particles converge on the barrel", "orbs of light", and a charged shot as "a single golden burst of damaging energy" [Fan-wiki].
- **Rake** (Sniper secondary): added "Rakes can be removed by explosives." [Fan-wiki].
- **Soldier (BBG)/Weapons:** category tags only [Fan-wiki].
- **Generalissimo** (a Wil skin): one sentence added [Fan-wiki]. Not a weapon.

None of these three weapons is seen in 2026 footage, so their 2026 status is unknown [Unverified].

---

## A Salt Rifle (Soldier primary; named on the 2026 Steam page)
- **Official text:**
  - "Grab your A Salt Rifle, Bearzooka and those Turkish SW Boots…" [Canon] (Steam).
  - "Standard pun rifle issued to all soldiers. Help it out by equipping extra damage equipment!" [Game text via wiki] (A Salt Rifle).
- **Look:**
  - The 2012 wiki render shows a long rifle in pale grey-mint (highlights ≈ #E0F0F0, mid ≈ #C0E0D0, shade ≈ #809090) with dark-grey parts (≈ #404040) and a muted red stripe (≈ #705050 in shade). Oliver holds it two-handed at the hip; it is about 0.6× Oliver's height [Observed: wiki Oliver3d.png, uploaded 2012-12-29; hex and scale Inference].
  - In the 2026 tutorial build (2.54.0), the HUD icon is a grey rifle with red parts reading 70/70 [Observed, low-res: https://i.ytimg.com/vi/-RSuAlfOUow/hq1.jpg]. The tutorial's 70 ammo matches the wiki's tutorial note "Ammo: 70" [Fan-wiki].
  - The gold-Oliver card's silver rifle (2013 trailer, 41.5–42.5 s) is reused on the Oct 12, 2026 Q&A thumbnail [Observed]. That it is the ASR is [Unverified].
- **Firing:** automatic; damage 6, 0.15 s rate of fire, 25 ammo, 3.0 s reload, "perfect accuracy" [Fan-wiki]. No 2026 firing frame identified [Unverified].
- **Projectile:** undocumented [Unverified].
- **Impact / end result:** undocumented [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/sheets/boots_asr.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/crops/up_-RSuAlfOUow_hq1.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/sheets/O1.png
- **Depiction for shorts:** a pale grey rifle with a red stripe, held at the hip. Rapid small white muzzle pops; hits throw tiny sparks [BBG News invention for the muzzle and hit effects].
- **Confidence:** partial.

## Bearzooka (Soldier secondary; named on the 2026 Steam page; same look in 2013 footage and the 2026 playtest)
- **Official text:**
  - Steam names it, as quoted above [Canon].
  - "The basic weapon of any Soldier. Does a good amount of damage, with a decent area of effect (AOE). Useful for all situations." [Game text via wiki] (Bearzooka (BBG)).
- **Look:** a shoulder-carried coral-red tube with glowing orange chevron and arrow windows, grey bands, a grey-and-red checkered flared rear end and a dark hexagonal muzzle [Observed].
  - Sampled colours, trailer 4.8 s: tube lit ≈ #DE604D to #E46C54, shade ≈ #D25443; windows ≈ #FC9C24 to #FFA82D; checker grey ≈ #676C6B [Observed; hex Inference].
  - Size: about 0.75–0.9× Oliver's height, foreshortened in every view [Inference].
  - The same design appears in the 2012 wiki concept, labelled "Rocket", which also sketches "Thrown missile" ideas [Observed], and in the 2013 wiki in-game photo [Observed].
  - In 2026 the tutorial and item-overview thumbnails show the same coral-pink tube with gold bands and a hexagonal muzzle, ≈ #A84860 / #904848 in dim light [Observed, low-res]. No visual change is detectable [Inference].
  - **The wiki's "rocket launcher with red and orange lines" is right** [Fan-wiki]. The green hazard-striped launcher is the BB Zombies one: "In BBZ and BB-1 it is just a dark green rocket launcher" [Fan-wiki].
- **Firing:**
  - Rate of fire 1.5 s, ammo 1, reload 2.5 s, 1,000 u/s [Fan-wiki]. The wiki also says "two shots without additional ammo", so it contradicts itself [Fan-wiki].
  - The 2026 tutorial HUD reads 1/1 [Observed, low-res].
  - Muzzle flash not observed [Unverified].
- **Projectile:** a rocket [Inference from the concept label]. The in-game rocket has not been seen [Unverified].
- **Impact / end result:**
  - Explosives 40–60 damage; AoE "Max Dmg: 125 units / Min Dmg: 250 units"; "The user is very prone to suicide while using the Bearzooka" [Fan-wiki].
  - The orange-yellow flame streaks at 4.5–5.0 s cannot be credited to the Bearzooka rather than the B-1000 [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/wiki/img/bz_pair.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/crops/bz_trailer_crop.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/frames/trsheets/sheet_00.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/frames/full/p_b1000b.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/crops/up_-RSuAlfOUow_hq3.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/crops/-RSuAlfOUow_hq3_bzcrop.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/crops/up_YEiD_hq1.png
- **Depiction for shorts:** Oliver shoulders a coral-red tube with glowing orange chevrons. It fires a stubby rocket with an orange flame tail, which bursts into an orange-yellow puff with sparks and soot [BBG News invention for the rocket and blast look].
- **Confidence:** observed (look); unknown (projectile and blast).

## Turkish SW Boots (Special, not a weapon; named on the 2026 Steam page)
- **Official text:**
  - Steam names them, as quoted above [Canon].
  - "You want to jump? These allow it!" [Game text via wiki] (Turkish SW Boots).
- **Look:** in the wiki icon, Oliver leaps in red studded boots with white jet puffs from the soles; the older icon shows him lifting off on twin white cloud columns [Observed]. The boots are about 0.2× Oliver's height [Inference]. The 2026 look has not been observed [Unverified].
- **Firing:**
  - Jump power 600; cooldown 4.5 s (2.5 s before v2.6); level 8; 40 Gas [Fan-wiki].
  - Usable while airborne since v2.0, which allows a double jump [Fan-wiki].
- **Projectile:** none [Fan-wiki].
- **Impact / end result:** mobility only, no damage [Fan-wiki].
- **Images viewed:** /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/sheets/boots_asr.png
- **Depiction for shorts:** two white puff-jets under red studded boots for a big hop, with a second puff mid-air [BBG News invention for the sound and timing].
- **Confidence:** documented (2013 era); unknown (2026 visual).

## Grenader (Assault primary, default; B-1000 default loadout seen in an official 2026 thumbnail)
- **Official text:** "Got a weak arm? Fear not! This honey of a weapon does the throwing for you. Now you can sit back and relax while pelting your enemies with explosives from afar." [Game text via wiki] (Grenader)
- **Look:**
  - The B-1000's right arm ends in an orange-and-white drum-barrel launcher with black bands [Observed: wiki Grenader.jpg]. The barrel is about 0.5× Oliver's height, on a B-1000 of about 1.5× [Inference].
  - The official Aug 21, 2026 livestream thumbnail shows the loadout screen ("CHARACTER ASSAULT", "SKIN B1000") with the same gun-arm and an axe [Observed: https://i.ytimg.com/vi/xP27fWSCSKs/hq2.jpg]. Naming it the Grenader rests on the wiki listing it as the default [Inference].
- **Firing:**
  - Arcing grenades; ammo 4 in the infobox but "ammo clip of three" in the text; 1.5 s rate; 5 s reload; 750 u/s [Fan-wiki].
  - On reload, "the barrel will look like it's charging … with strong golden light, eventually forming a golden orb" [Fan-wiki].
- **Projectile:** "looks like it's set on fire with something else rotating or orbiting it" [Fan-wiki].
- **Impact / end result:**
  - Grenades "explode into a damaging, golden orb", "a rather huge and bright blast"; 45–70 damage; AoE 125/250 [Fan-wiki].
  - Trailer 2.5–3.0 s: an orange fireball bursts on an airborne target [Observed; ID Inference].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/sheets/wiki_cmp.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/sheets/O4.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/frames/trsheets/sheet_00.png
- **Depiction for shorts:** a lobbed fiery grenade with a little orbiting flame pops into a bright golden sphere; robots shed bolts and bears throw sparks [BBG News invention beyond the wiki words].
- **Confidence:** partial.

## Axecutioner (Assault melee, default; seen in the same official 2026 thumbnail)
- **Official text:** "Why carry an axe in your hand when you can replace your hand with an axe?" [Game text via wiki] (Axecutioner)
- **Look:** a grey battleaxe head bolted onto the B-1000's left forearm, with an orange cuff [Observed: wiki Axecutioner.jpg; the 2026 loadout thumbnail xP27fWSCSKs hq2, low-res]. The blade is about 0.4× Oliver's height [Inference].
- **Firing:** melee; 70 damage [Fan-wiki].
- **Projectile:** none.
- **Impact / end result:** undocumented [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/sheets/wiki_cmp.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/sheets/O4.png
- **Depiction for shorts:** a flat chop with a clang and a shower of sparks [BBG News invention].
- **Confidence:** partial.

## Bearail Gun (Assault primary; probably the white-and-orange gun-arm in 2026 footage)
- **Official text:** "This devastating laser creates a colossal explosion upon impact. Anything this powerful takes time so keep the enemies in your sight while it builds up. Trust us, vaporizing your friend has never been more fun!" [Game text via wiki] (Bearail Gun)
- **Look:**
  - A long white gun-arm with orange trim, black panels and cyan crystal fins near the tip, on the B-1000's right arm [Observed: official https://i.ytimg.com/vi/C7uFxvSZ10c/hq1.jpg, Aug 16, 2026; fan https://i.ytimg.com/vi/2Vdvp2mW4KY/hq1.jpg and hq2.jpg].
  - Naming it rests on the fan title "i play the bbg beta with bearail" [Unverified] plus the wiki's "golden laser" [Inference].
  - It could instead be the Lightning Bolt, which also shows a white-and-orange gun-arm with a blue light in its wiki image [Observed: wiki Lighting_bold_(cr).png].
- **Firing:**
  - It charges "for a second before firing an extremely fast, golden laser" with "no travel time, infinite range" [Fan-wiki].
  - The 2026 HUD reads 0/1 after the shot [Observed, low-res].
- **Projectile:** pale-gold straight streaks (≈ #F8F8A8 to #F8E888) [Observed; hex Inference].
- **Impact / end result:**
  - A "colossal explosion", 70–90 damage [Fan-wiki].
  - In 2026 a white starburst with sparks appears at the far end [Observed, low-res: 2Vdvp2mW4KY hq1].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/sheets/official_zoom.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/crops/fan_g2.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/sheets/wiki_cmp.png
- **Depiction for shorts:** a one-second hum while glow gathers at the tip, then a pencil-straight gold beam and a big white-gold pop. The target tumbles out in bolts and sparks [BBG News invention for the charge hum and the pop].
- **Confidence:** partial.

## Gamma Ray (Engineer primary; in the 2013 trailer; probably in an official 2026 thumbnail)
- **Official text:** "Turn your enemies in to walking explosives with this radioactive ray gun. It does very little damage on initial impact, but once you charge them up all the way...BOOM! The radioactive symbol over their head indicates how charged they are. The bigger they are, the longer it takes to blow them up, however yielding a much larger and more aggressive explosion." [Game text via wiki] (Gamma Ray)
- **Look:**
  - 2013: a bear in an orange hard hat fires from an orange handheld device with white ripple rings at the muzzle [Observed: trailer 38.6–39.0 s].
  - 2026 (official v3.0.0 thumbnail): gold-skinned Graham, with a blocky gold backpack and antenna, fires a thin straight yellow ray (≈ #F8F858) from an orange claw-like emitter, with ripple rings at the muzzle and a white sparkle spray at the end [Observed: https://i.ytimg.com/vi/C7uFxvSZ10c/maxresdefault.jpg].
  - Naming it rests on the wiki's "constant yellow beam" [Inference]. The emitter is about 0.3× Oliver's height [Inference].
- **Firing:** a "short-ranged constant yellow beam"; 1 damage per shot, and each shot adds 4.5 radiation points [Fan-wiki].
- **Projectile:** a beam [Fan-wiki].
- **Impact / end result:**
  - When the target is fully irradiated it explodes with a radius of 150–200 units, damaging others [Fan-wiki].
  - Trailer 8.5–10.0 s: a trefoil over a target, then a yellow cube-cluster blast with white hexagonal floor rings [Observed; link Inference].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/frames/full/p_g2.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/frames/trsheets/sheet_01.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/frames/trsheets/sheet_06.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/sheets/O1.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/sheets/official_zoom.png
- **Depiction for shorts:** a wobbly yellow ray while a trefoil icon fills above the victim, then a cartoon pop of yellow cubes and rings; the victim bursts into bolts or confetti [BBG News invention for the fill animation].
- **Confidence:** partial.

## Crossbow / "Unicorn Crossbow 2.0" (Sniper primary; named in a 2026 loadout)
- **Official text:** "Leave it to Astoria to make a rapid fire weapon that shoots unicorn horns. Even worse is that she can charge up the weapon and release a stronger attack! What's next jackelope weapons?" [Game text via wiki] (Crossbow (BBG))
- **Look:**
  - 2026: the loadout panel reads "PRIMARY CROSSBOW", with a white winged-crossbow icon [Observed, low-res: https://i.ytimg.com/vi/qt43iTdANbM/hq3.jpg, JustNubz Playtest #3, build 3.0.2].
  - 2013: a white-silver winged crossbow with a lilac string and purple crystal accents, held at the chest; its span is about 0.6× Oliver's height [Observed: wiki Crossbow.jpg; scale Inference].
- **Firing:**
  - Uncharged 15, charged 230; charge time 1.5 s; 15 ammo; 2 s reload; no lock-on [Fan-wiki].
  - Fully charged, "its internal barrel will also rotate at a rapid rate and shine a bright purple aura" [Fan-wiki].
- **Projectile:** "shining unicorn horns" [Fan-wiki].
- **Impact / end result:** a charged hit adds AoE damage [Fan-wiki]; the look is undocumented [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/crops/qt43_hq3_panel.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/wiki/img/crossbow_view.png
- **Depiction for shorts:** sparkly white horn-darts; the charged shot spins with a purple glow and bursts into pastel sparkles [BBG News invention for the burst].
- **Confidence:** partial.

## Fairy's Dust (Sniper secondary; named in a 2026 loadout; cloud seen in the 2013 trailer)
- **Official text:** "Enemy got you in their cross hairs? Toss this lil' sack-o-magic and give 'em the slip. This magical concoction can be a real life saver!" [Game text via wiki] (Fairy's Dust)
- **Look:**
  - A pink-purple sack (≈ #E46CE4) tied at the neck, with sparkles [Observed: wiki FairysDust.jpg; hex Inference]. The sack is about 0.15× Oliver's height [Inference].
  - The 2026 loadout reads "SECONDARY FAIRY'S DUST" with a pink-sack icon [Observed, low-res].
- **Firing:** thrown; 1 ammo; 1.5 s rate; 3 s reload; 1,000 u/s [Fan-wiki].
- **Projectile:** the sack [Fan-wiki].
- **Impact / end result:**
  - "a huge, harmless cloud of purple dust that can partially block a player's sight", lasting 4 s, with no damage [Fan-wiki].
  - Trailer 14.0–16.0 s: a giant magenta faceted cloud (≈ #FC3CFC / #E43CFC) fills the temple stairs, and Astoria runs out of it [Observed; ID Inference].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/frames/trsheets/sheet_02.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/sheets/wiki_cmp.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/crops/qt43_hq3_panel.png
- **Depiction for shorts:** a tossed sack poofs into a room-filling magenta glitter cloud, enemies stagger, and Astoria strolls out [BBG News invention for the staggering].
- **Confidence:** observed (2013 cloud); partial (2026).

## Battering Ram (Sniper melee; named in a 2026 loadout)
- **Official text:** "Using revolutionary "Ram Skull" technology for maximum bashing ability, this is a weapon of last resort." [Game text via wiki] (Battering Ram)
- **Look:**
  - A ram skull with curling horns on a long handle, swung like a mace [Observed: wiki Battering_ram.png menu photo]. It is about 0.6× Oliver's height [Inference].
  - The 2026 loadout reads "MELEE BATTERING RAM" [Observed, low-res].
- **Firing:** melee; 30 damage, +40% special speed [Fan-wiki].
- **Projectile:** none.
- **Impact / end result:** undocumented [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/sheets/wiki_cmp.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/crops/qt43_hq3_panel.png
- **Depiction for shorts:** a horn-first bonk with a "baa"-free thud and cartoon stars [BBG News invention].
- **Confidence:** partial.

## Whack-Tus (Huggable melee; seen in a 2026 showcase thumbnail)
- **Official text:** "Whack-tus? Darn near killctus." [Game text via wiki] (Whack-Tus)
- **Look:**
  - 2026: a Pink Huggable (skin row "PINK HUGGABLE") with a spiky dark-green cactus club over each wrist [Observed: https://i.ytimg.com/vi/-lAtv-j9Sms/hq3.jpg].
  - 2013: the same cacti on an orange Huggable skin [Observed: wiki HuggyWhacktusCR.jpg]. The wiki calls the weapon "a consistant dark green all over" [Fan-wiki].
  - Each cactus is about 0.3× Oliver's height [Inference].
  - Its former name is documented [Fan-wiki]; it is not for use on screen.
- **Firing:** melee; 60 damage, +30% special speed [Fan-wiki].
- **Projectile:** none.
- **Impact / end result:** undocumented [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/sheets/J.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/sheets/wiki_cmp.png
- **Depiction for shorts:** a double cactus bonk that puffs out green needles and sparks [BBG News invention].
- **Confidence:** observed (presence and look); unknown (impact).

## O.C.O. Gauntlet and the fan-reported "Dark OCO Gauntlet" (Soldier primary; in 2026 per a fan)
- **Official text:** "Spawn orbs of energy that damage when touched and explode on direct impact." [Game text via wiki] (O.C.O. Gauntlet)
- **Look:**
  - 2012: a grey-and-black armoured gauntlet with cyan "OCO" lettering and a keypad, plus a big cyan-white mitten version (≈ #0CCCE4) [Observed: wiki OCO_Gauntlet.png].
  - 2026: the JustNubz 1v1 description says "I was trying to match him with the Dark OCO Gauntlet by using the OCO Gauntlet" [Unverified, fan description] (https://www.youtube.com/watch?v=IWGH-6K7fEc).
  - Its thumbnails show a Dark O.C.O.-skinned bear (black with orange-red glowing cracks) and a black bear with a magenta-glowing hand and a magenta orb [Observed: https://i.ytimg.com/vi/IWGH-6K7fEc/hq1.jpg and hq2.jpg].
  - The wiki has no "Dark O.C.O. Gauntlet" page (missingtitle) [Fan-wiki]. Whether the Dark variant is new in 2026 is unknown [Unverified].
- **Firing:** an orb spawns and sits for 2 s without dealing damage, then "will accelerate very fast". Three orbs per load; orbs implode after 10 s [Fan-wiki].
- **Projectile:** large orbs with "a dark blue core and a pulsing light blue field" [Fan-wiki]. The Dark variant may be magenta [Inference].
- **Impact / end result:** an implosion; 40–60 damage plus 30 on a direct hit; AoE 50/150 [Fan-wiki].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/crops/fan_g1.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/sheets/wiki_cmp.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/sheets/official_zoom.png (official v3.0.0 thumbnail with a Dark O.C.O.-skinned figure mid-air)
- **Depiction for shorts:** a cyan orb, or a magenta one for the Dark variant [Inference], hovers, then zips forward and implodes with a ring flash [BBG News invention for the ring].
- **Confidence:** partial (base gauntlet); unknown (Dark variant).

## Phat Man (Demo secondary; in the 2013 trailer only; 2026 unknown)
- **Official text:** "Phat chance that you'll be dodging this baby. Flies out of sight and, just when you've forgotten about it, hits fast and hard like a liquored up grandpa." [Game text via wiki] (Phat Man). The alcohol joke must not be reused on screen.
- **Look:**
  - On Tillman's card, an olive-drab shell with a yellow band rides on his back [Observed: trailer 28–29.5 s].
  - The missile-cam shows olive and yellow with black marks (24–25.5 s). A yellow canister with a black radiation trefoil descends in a vertical yellow light column (26.0–26.4 s) [Observed].
  - Naming it the Phat Man rests on the trefoil plus the wiki's "launchable nuclear missile" [Inference]. The shell is about 0.7× Oliver's height [Inference].
- **Firing:** lock-on; it "will ascend into the air quickly, before falling down"; 1 ammo; 10 s reload; −10% speed [Fan-wiki].
- **Projectile:** a missile [Fan-wiki].
- **Impact / end result:**
  - 65–195 damage; AoE 200/600 [Fan-wiki].
  - Trailer 26.5–27.5 s: a screen-filling flat-shaded yellow-white blast (≈ #FCE454) with red armour pieces flying [Observed].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/frames/trsheets/sheet_04.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/frames/full/p_till.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/sheets/S.png
- **Depiction for shorts:** a whistle from the sky and a yellow spotlight beam, then a screen-filling yellow cube burst; everyone is flung amid raining bolts [BBG News invention for the whistle].
- **Confidence:** observed (2013); unknown (2026).

## Barbed Gloves (Heavy melee, default; in the 2013 trailer only; 2026 unknown)
- **Official text:** not fetched [Unverified].
- **Look:** a bandage-wrapped glove studded with pale-green crystal spikes. Riggs, in a red cracked-rock skin, punches a gold Huggable with it, and it appears again on the Riggs card [Observed: trailer 36.5–38.0 s]. Naming it the Barbed Gloves rests on the default Heavy melee listed on the wiki [Inference].
- **Firing:** melee.
- **Projectile:** none.
- **Impact / end result:** undocumented [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/frames/full/p_riggs.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/frames/trsheets/sheet_06.png
- **Depiction for shorts:** a spiked bandaged haymaker that knocks out a spray of sparks [BBG News invention].
- **Confidence:** observed (2013 look); unknown (2026).

## Unidentified weapon-like items in official 2026 art and 2026 footage (sub-topic)
- **Official Jul 6, 2026 "CLOSED TESTING" Steam banner** [Observed: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/sheets/banner_zoom.png]:
  - A panda-faced bear with a long white rifle with black panels and a three-pronged tip.
  - A skull-faced bear with a lime-green camo toy gun.
  - An eye-patched brown bear with a grey gun.
  - The B-1000 with a cyan crystal blade.
  - A pale-blue heavyset bear with a black gatling whose barrels glow orange-yellow. It may be Riggs's Beebeegun, which the wiki calls a minigun [Inference].
  - A Graham-like bear (orange hard hat, cyan goggles) with an orange chainsaw with rainbow chain teeth.
  - Names for all of these are [Unverified].
- **Steam store loop video:** a gold Huggable flies with a white-yellow-green-cyan-purple faceted trail [Observed: /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/frames/extras_sheet.png]. Which ability it shows is [Unverified].
- **Recurring 2026 map objects:**
  - Blue lightning-bolt objects lie around maps. The HUD uses the same icon for joules ("⚡+200"), so they are probably not weapons [Inference].
  - Green shield icons with a plus around players are probably the Shield pickup [Inference].
  - A "Z" icon above an enemy is probably a sleep status [Inference].
  - All observed in /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/sheets/O3.png and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/2026-changes/crops/fan_g4.png.
- **Confidence:** unknown.

## Status summary
- **Named in an official 2026 source:** A Salt Rifle, Bearzooka, Turkish SW Boots [Canon].
- **Seen in 2026 builds, named on screen or identified with good support:** Bearzooka, A Salt Rifle (HUD), Grenader and Axecutioner (default B-1000 loadout), Crossbow, Fairy's Dust, Battering Ram, Whack-Tus [Observed, low-res].
- **Probable in 2026:** Bearail Gun, Gamma Ray, O.C.O. Gauntlet [Inference / Unverified].
- **Reported by a fan only:** "Dark OCO Gauntlet" [Unverified].
- **2013 trailer only:** Phat Man, Barbed Gloves, the Fairy's Dust cloud and Gamma Ray effects.
- **Visual changes:** none detectable in thumbnail-resolution evidence [Inference]. SkyVu lists "LIGHTING, EFFECT & TEXTURE IMPROVEMENTS" [Canon].
- **Everything else:** unknown.

## Corrections for the character file
1. **oliver.md, line 51.**
   - Current: "The Bearzooka is drawn as a green, hazard-striped tube [Observed; Inference]."
   - Correction: "In BBG the Bearzooka is a coral-red shoulder tube (≈ #DE604D lit, #D25443 shade) with glowing orange chevron windows (≈ #FC9C24), grey bands, a grey-and-red checkered flared rear and a dark hexagonal muzzle [Observed: wiki 2012 concept and 2013 in-game photo; Steam trailer 4.0–5.0 s; 2026 tutorial thumbnail]. The green hazard-striped launcher belongs to the 2009 BB Zombies cutscenes [Fan-wiki: 'In BBZ and BB-1 it is just a dark green rocket launcher']."
2. **oliver.md, Prompt pack.**
   - Current: "He holds a chunky assault rifle and carries a green hazard-striped launcher tube on his back."
   - Correction: "He holds a long pale grey-white rifle with a muted red stripe (A Salt Rifle) and shoulders a coral-red bazooka tube with glowing orange chevrons and a checkered flared rear (Bearzooka)."
3. **oliver.md, Prompt pack (costume; outside weapons; flagged for the soul owner).**
   - Current: "Green-and-dark-grey shoulder harness, small green backpack, no clothing."
   - Correction: "BBG default Oliver wears a red headband (red team), a diagonal bandolier of bullets, and red wrist and ankle bands with silver studs. A blue headband marks the blue team [Observed]. Verify before replacing the BB-1-era harness."
4. **astoria.md, line 49.**
   - Current: "a teal-masked sniper in a 2026 Steam screenshot, which is Astoria only by [Inference]"
   - Correction: "a teal-masked sniper in a Steam store screenshot that is a frame of the 2013 trailer footage reused on the 2026 store page (trailer 30.7 s), Astoria by [Inference]"
5. **riggs.md, line 52.**
   - Current: "the 2026 trailer card shows a red faceted skin instead [Observed]"
   - Correction: "the Steam trailer card (2013 trailer footage reused on the 2026 store page) shows a red faceted skin instead [Observed]"
6. **riggs.md, line 56.**
   - Current: "Their look is undocumented, so designs, like the toothbrush prop, are [BBG News invention]."
   - Correction: "The default melee is visible in the Steam trailer (2013 footage, 36.5–38 s): a bandage-wrapped glove studded with pale-green crystal spikes (Barbed Gloves by [Inference]). Beebeegun and Hivey League looks remain undocumented; designs for those, like the toothbrush prop, are [BBG News invention]."
7. **botch.md, line 53.**
   - Current: "He has no splash card in the 2026 Steam trailer [Observed] and postdates the 2013 trailer's eight launch classes [Canon]"
   - Correction: "He has no splash card in the Steam trailer, which reuses the 2013 launch trailer's footage of the eight launch classes [Observed; Inference]"
8. **saberi.md, line 53.**
   - Current: "neither the 2013 BBG trailer nor the 2026 Steam trailer shows a splash card for her, and whether one exists elsewhere is unknown [Observed]"
   - Correction: "the Steam trailer is a re-edit of the 2013 BBG trailer footage and shows no splash card for her; whether one exists elsewhere is unknown [Observed; Inference]"

## Open questions
- Does the 2026 build add, remove or rebalance any weapon? No patch notes exist yet, and Steam's "80+" primaries and "50+" melees exceed the wiki's 77 and 46.
- What did "LIGHTING, EFFECT & TEXTURE IMPROVEMENTS" (final playtest, Oct 15) change in weapon effects?
- Is the "Dark OCO Gauntlet" new in 2026 or an old skin-linked variant? Does it really fire magenta orbs?
- Is the B-1000's white-and-orange gun-arm in 2026 footage the Bearail Gun or the Lightning Bolt?
- What does "Premium" in the Steam trailer title mean? Will a 2026-footage trailer replace the 2013 recut? SkyVu asked testers for UI-less footage for the store on Oct 14.
- What do the unwatched sources show? The JustNubz showcase (all weapons, build 3.0.5), the Aug 21 livestream "Character and loadout showcase", the Oct 12 Q&A and the Oct 19–26 Next Fest demo.
- What are the orange chainsaw with rainbow teeth (official banner), the black glowing gatling and the gold Huggable flight trail on the store page?
- Did the Sept 2026 wiki stat edits (Hazard Toy 25–50 explosives and 4 damage, Energy Overflow 3 s charge, Rake removable by explosives) come from the 2026 playtests or from old knowledge?
- What is the "2.54.0" build line? The wiki's version table stops at 2.25.
