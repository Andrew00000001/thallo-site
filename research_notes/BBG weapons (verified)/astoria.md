# Astoria (Sniper): weapons dossier (verified and edited)

Astoria is the Sniper class in Battle Bears Gold (BBG). The 2026 Steam page lists "-SNIPER: Astoria" [Canon] (https://store.steampowered.com/api/appdetails?appids=4408320, re-fetched 2026-10-17). The fan wiki's Updates page gives the class's arrival as BBR 1.1, Nov 23, 2011: "Added Game Center, new sniper class, new weapons" [Fan-wiki transcription]. The Sniper (BBG) page gives her "a value of '''90'''" health [Fan-wiki].

The class page lists 18 weapons: 8 primaries, 6 secondaries and 4 melees. They match the class mapping file's 18 "Astoria" pages exactly [Fan-wiki]. None of the 5 unassigned category pages is a Sniper weapon. This dossier covers all 18. It also covers the lock-on mechanic, 3 unreleased concepts, the BB Heroes (BBH) and BB Overclock (BBO) equivalents, and what official 2026 material actually shows.

Eras used below:
- BBR: Battle Bears Royale, 2011–13.
- BBG: Battle Bears Gold, 2013–21 updates.
- BBG 2026: the re-release, Nov 4, 2026.
- BBH: BB Heroes, soft launch 2023, global 2024.

**Sources reachable today (2026-10-17)**
- Fan wiki through the MediaWiki API. I re-fetched all 18 weapon pages plus these supporting pages: Sniper (BBG), Sniper (BBG)/Weapons (a one-line stub), Status Effects, Updates, Battle Bears Gold/Versions and /2.6, BBR Version 1.3, 1.3.1, 1.4.2 and 1.4.3, Bundle Deals, Solid Fisher, Pandini, Call Off Duty, Assassino, Astoria (Skin), Viper Rifle (BBO) and Battle Bears Heroes. Saved under /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/pages/.
- Wiki images on static.wikia.nocookie.net. I re-downloaded about 100 files, converted them from WebP and opened them.
- Steam appdetails: store text, 5 screenshots and the single trailer "Battle Bears Gold Premium - Trailer".
- battlebears.com/pages/characters (live).
- YouTube oEmbed titles, the BATTLE BEARS channel RSS feed (15 latest uploads, with dates) and i.ytimg.com thumbnails.

**Not reachable**
- web.archive.org: curl returned 000 or the tunnel closed mid-exchange, and WebFetch was refused. The archive.org availability API answered, but returned no snapshots for battlebears.com/battle-bears-gold-2-6-change-log/ or battlebears.com/blog/item/138-the-weekend-update. The snapshot URLs listed in the earlier notes are therefore [Unverified]. Every patch-note line below is the wiki's transcription [Fan-wiki].
- YouTube watch pages redirect to a Google "sorry" page. I watched no video. Video evidence comes only from the official Steam trailer file (frames I extracted), from thumbnails and, for the trailer-era note below, from the YouTube storyboard of SkyVu's 2013 trailer.

**Method**
- I extracted my own trailer frames with ffmpeg at 10 fps into /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/tr/:
  - a_NNN.jpg: t = 11.8 + (N−1)×0.1 s.
  - b_NNN.jpg: t = 29.4 + (N−1)×0.1 s.
  - Labelled sheets: sheetA1–A4.jpg and sheetB.jpg.
- Crops and stacks are in /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/.
- Hex values are approximate. They were sampled with PIL (python -I) from the images named.

**Size convention.** The BBG News scale chart is Oliver = 1.0×. The character file puts Astoria at 1.0× Oliver's height [BBG News invention]. Weapon sizes below are in Astoria head-heights (her head is roughly a third of her standing height in the Gear Up models). They were judged by eye from foreshortened menu poses [Inference].

**Wiki stats are era-mixed.** BBG 3.0 (Nov 15, 2021) says "All +1 Equipment has been removed except Speed +1" and "Equipment Slot 2 has been removed" [Fan-wiki transcription, Updates]. Every wiki equipment table is therefore pre-2021, and the 2026 stats are [Unverified].

**The Steam trailer and screenshots are 2013 footage, not the 2026 build.**
- The trailer SkyVu put on the 2026 Steam page ("Battle Bears Gold Premium - Trailer") and the five Steam screenshots are most likely re-edited 2013 launch footage [Inference, strong]. The trailer's class cards are pixel-matched to SkyVu's May 30, 2013 trailer "BATTLE BEARS GOLD Trailer: Award-Winning Multiplayer Shooter Game" (rfAyqVJrli4), and each screenshot is a trailer frame (maps overview, research_notes/BBG maps (verified)/00_OVERVIEW.md, section 0, item 1).
- Every Astoria shot in it is also in that 2013 trailer. I matched the 2013 trailer's YouTube storyboard (160×90, one frame a second; re-fetched 2026-10-18) against my own Steam-trailer frames, which run 4.1 s ahead [Observed]:
  - the Aztec Dead Eye shot: Steam 12.9 and 13.9 s, greyscale MSE 93 and 100;
  - the Fairy's Dust cloud: 14.9 and 15.9 s, MSE 269 and 378;
  - the ASTORIA / SNIPER card: 16.9 s, MSE 158;
  - the Space Oddity clip with the Call Off Duty Viperifle: 30.9 and 31.9 s, MSE 121 and 150. The Steam clip runs without a cut from 30.0 s.
  - Unrelated frames score about 7,000–8,700.
- The maps notes leave the Space Oddity clip's capture date open, because its pillar top blooms to near-white. The storyboard match puts that clip in the May 2013 trailer as well, so it is 2013 footage too [Inference, strong]. Screenshot_01 is a frame of it; screenshot_04 is a Shortest Parsec frame.
- None of it shows the Oct 2026 build. The 3.0.7 playtest build lights Space Oddity in a warmer, more golden grade than screenshot_01 [Observed].
- Below, these are "the Steam trailer" and "Steam screenshot_0N", dated "(2013 footage [Inference, strong])". 2026 claims rest on 2026 captures and SkyVu's 2026 thumbnails.
- Images viewed for this note:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/huggable-gaps2/sb/rfAyqVJrli4/cs_00.jpg and cs_01.jpg (the 2013 trailer's storyboard; the Aztec scene at 17–20 s, the Astoria card at 21 s, Space Oddity at 35–36 s)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/astoria_trailer_check/so_clip_2013_vs_steam.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/astoria_trailer_check/cont_sheet.jpg (Steam trailer 29.8–31.1 s)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/maps/dl/environment-conventions/sheets/so_steam_vs_hk.jpg (screenshot_01 beside build 3.0.7)

---

## Default look of the wielder (affects every weapon shot)

- **In-game BBG default skin "Astoria"** [Observed]:
  - Fur: cream (highlight ≈#E8D7A4, shade ≈#B3A87C).
  - Eyes: blue/blue-teal. The mean of four Gear Ups is ≈#5391A1.
  - Team-colour gear on the red team: red backpack and shoulder straps; a red belt with a dark-maroon quilted band (≈#462122–#512A27) and a red side pouch (≈#9D0000–#AD0301); red gloves; red-and-white striped boots.
  - Wiki text: it "depicts the Sniper wearing an ammo belt, a backpack and gloves with the colour of the team colour" [Fan-wiki, Astoria (Skin)].
  - Images: conv2/Astoria-Default.png.png, conv/Viperrifle.jpg.png and others listed below.
- **Red-jacket outfit = the "Assassino" skin** [Inference, strong; resolved by the verifier].
  - Where it appears [Observed]: red jacket with white sleeves, a round orange belt emblem, dark trousers, red boots and a brown hip pouch. It is in the Nov 2012 loadout (File:Gnifle-sniper-setup.png), the 2013 Dead Eye Gear Up (File:DeadEye.jpg), the official 2.2 promo thumbnail and the Steam trailer (Dead Eye shot, Fairy's Dust, title card; 2013 footage [Inference, strong]). In 2026, a fan frame of the Oct 15 final playtest (HKbwq7PolNc maxres2, build 3.0.7) shows a cream bear from behind in the same red jacket with white sleeves and a brown backpack [Observed]; it is Astoria by [Inference] from the Sniper's 90/90 health (see the addendum).
  - Wiki text: Assassino "features Astoria in a team colored jacket with a white shirt underneath, black pants, backpack and ammo belt" [Fan-wiki].
  - The wiki's own previews File:Assasino1.PNG and File:Assassino.png show the same outfit, with "ASSASSINO BUY NOW 125,000" in the menu [Observed]. That matches the trivia "It cost 125,000 Joules before update 2.1" [Fan-wiki].
- **Mint face mask + cucumber slice = the "Call Off Duty" skin** [Inference, strong; resolved by the verifier].
  - Wiki text: "a mint-colored mud-mask with a cucumber piece on the left eye … pink shirt with a light pink robe and dark pink night panties with small dots on them. Pink is changed to light blue if the player is on Team Blue … her ammo-belt features a bag of ice cream" [Fan-wiki].
  - Steam screenshot_01 and the trailer's Space Oddity clip (≈30.0–30.8 s; 2013 footage [Inference, strong]) show exactly the blue (Team Blue) version with an ice-cream tub on the belt [Observed]. The wiki's File:Call_off_duty.png shows the pink version [Observed].
- **Solid Fisher skin**: all-black suit with red stripes and three glowing red head-lamps [Observed, File:Solid_Fisher.png]. Wiki text: "an all-black suit with team-colored stripes on the arms, legs and headband with three glowing headlights" [Fan-wiki]. It appears in several weapon images below.
- Images viewed for this section:
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/skins_sheet.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/assassino.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/skins2.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/misc.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/conv2/AstoriaDescription.jpg.png

---

## How Astoria's lock-on rifles work (sub-topic: Viperifle, Capital Pains, Mamba's Boy, Dead Eye)

- **Official text:** "Keep targets centered in the screen to lock onto them. When your crosshairs turn green you are 100% accurate. If you can hold the lock a bit longer until they turn white you will get a head shot." ~ Official Battle Bears Gold description, Viperifle [Game text via wiki] (https://battlebears.fandom.com/wiki/Viperifle_(BBG)).
- **Look (reticle):**
  - Stage 1: "When holding the cross-hair over any opponent player, a black cross-hair will appear" [Fan-wiki, Capital Pains].
  - Green lock: "all shots fired at the opponent have 100% accuracy.(but will only do base damage)" [Fan-wiki, Viperifle].
  - White lock on the Dead Eye: "The scope shows a red dot with white lines" [Fan-wiki, Dead Eye].
  - Fan Everyplay thumbnails show a black circular reticle over the target before lock [Observed, QQrU7iCrGoo hq1; overhaul hq3].
- **Firing:**
  - The lock builds in three stages while the target stays in the reticle: semi-lock, green, white [Fan-wiki].
  - Firing without a lock is a "no-scope"; shots then spread even where the listed dispersion is 0.0 [Fan-wiki].
  - The Crossbow, Blow Dart and Art of War cannot lock [Fan-wiki].
- **Target warning (status "Scoped"):** "When a player is locked onto by an opponent's sniper rifle (reticule turns green), a red crosshair will appear over the player's head, indicating a headshot is in the process of being targeted. This does not affect the player in any way and serves only as a warning." Items capable: Viperifle, Capital Pains, Mamba's Boy, Dead Eye [Fan-wiki, Status Effects].
- **Impact / end result:**
  - A white-lock shot "is guaranteed to kill the opponent, regardless of his/her remaining health" [Fan-wiki]. Capital Pains adds "(unless they have Shields)" [Fan-wiki].
  - "When a Sniper makes a headshot, the shot instantly deducts all the target's remaining health" [Fan-wiki, Sniper (BBG)].
  - A headshot kill "shows up differently on the kill update feed" [Fan-wiki, Mamba's Boy].
  - The official "BATTLE BEARS GOLD Developer Update - Astoria Overhaul" thumbnail shows that feed row: Astoria's portrait, "HEAD SHOT", a red crosshair-in-circle icon over the victim's portrait, and "+100" [Observed]. The title is via oEmbed [Canon: title/channel only]. Which weapon made that kill is unknown; the weapon in her hand cannot be made out [Observed].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/yt/wUWf9O-YX4A_maxresdefault.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/ov_hand.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/ov_icon.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/ov_stack.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/redcp_stack.png
- **Depiction for shorts:**
  - Black reticle over the target, then it turns green; a small red crosshair pops over the victim's head as the warning; the reticle turns white for the one-shot.
  - The 13+ "kill" is the target popping into sparks (bears) or rainbow confetti (Huggables), with no blood [BBG News invention].
- **Confidence:** documented (mechanic); observed (kill-feed icon only).

---

## Viperifle (primary · default · BBR 1.1, Nov 23 2011 → BBG 2013–21, as in the Steam trailer → 2026: probably the teaser thumbnail's green shot)

- **Official text:** "Keep targets centered in the screen to lock onto them. When your crosshairs turn green you are 100% accurate. If you can hold the lock a bit longer until they turn white you will get a head shot." ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Viperifle_(BBG)).
- **Status and history:**
  - Default primary; "Up until v1.3, it was the only primary for the Sniper" [Fan-wiki].
  - BBG 2.6 (Dec 20, 2013): "Fire Rate decreased from 2.5 to 1.5", "Reload speed decreased from 5 to 4" [Fan-wiki transcription].
  - Infobox: 45 damage, 3 ammo, 1.0 s rate of fire, 3.5 s reload, green lock 3.0 s, white lock 6.0 s [Fan-wiki].
  - 2026 stats [Unverified].
- **Look:**
  - A black/charcoal rifle with a dark-green liquid capsule on top (≈#305216 mean, highlights ≈#388741) and green fins/vents by the grip. A long thin barrel ends in an angular open-jaw snake-head muzzle with a glowing lime eye (≈#84FE1F, Steam screenshot_01) [Observed].
  - The wiki agrees: "It has a dark and green theme … special liquid containers (magazines) are dark green … one on top of the scope itself, and two of them next to the trigger handle. The barrel end is shaped like a snake's mouth and is complemented with two green eyes" [Fan-wiki].
  - Held two-handed at chest height, about 2–2.5 head-heights long [Inference].
  - The same model shows in BBR 2012 (Mar and June) and BBG 2013 and 2015 Gear Ups [Observed].
  - **Steam trailer and screenshots** (2013 footage [Inference, strong]; see the note at the top) [Observed]:
    - Steam screenshot_01 and trailer ≈30.0–30.8 s (the Space Oddity clip): held by Astoria in the Call Off Duty skin (Team Blue version).
    - Steam screenshot_04 (Shortest Parsec): a tiny default red-gear Astoria (about 100 px tall) holds a dark rifle with a green top capsule. That this is the Viperifle is [Inference].
  - **2026:** the only sighting is the green shot in SkyVu's 2026 teaser thumbnail (Projectile, below), the Viperifle by [Inference].
  - CAUTION: File:Astoria-sniper-viperifle.png is 2D art with a generic grey rifle, not the in-game model [Observed].
- **Firing:**
  - One shot per pull after a lock [Fan-wiki].
  - No muzzle flash is documented [Unverified].
  - In the trailer at 30.0–30.8 s she aims but no shot from her rifle is visible. The muzzle flash at ≈30.3 s and the yellow star sparks at ≈30.5 s belong to other players [Observed].
- **Projectile:**
  - Wiki: "When fired, it releases a single, green, stream-like bullet that erupts into a splash of what appears to be venom. Said venom is merely cosmetic and has no added functionality" [Fan-wiki].
  - The official teaser "TEASER TRAILER - Battle Bears Gold Returns November 4th 2026" (d2ByJWrsoec, published 2026-10-02 per channel RSS) has a thumbnail hq1 whose "GAMEPLAY" panel shows a cream bear with a red strap, seen from behind. A bright green tapered streak (most-saturated ≈#01FC6F, mean ≈#23934D) runs from her toward a distant figure and ends in a small yellow-green splash [Observed]. The title and date are [Canon].
  - That this is Astoria firing the Viperifle is [Inference] (cream fur and red strap, plus the wiki text).
  - Overhaul thumbnail hq3: Viperifle-like HUD icon, ammo 4/4, black reticle on the Aztec lava temple; no shot visible [Observed].
- **Impact / end result:**
  - A small cosmetic green "venom" splash [Fan-wiki]. In the 2026 teaser it reads as a yellow-green burst [Observed, thumbnail].
  - Green lock: 45 base damage [Fan-wiki]. White lock: a one-shot HEAD SHOT [Fan-wiki].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/viper_sheet.jpg (File:Viperrifle.jpg 2013, File:Viperifle.jpg 2015, File:Viperifle.png BBR Mar 2012)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/new1.jpg (File:Viperrifle.PNG, June 2012)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/s01_ast.png (Steam screenshot_01)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/s04_full.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/s04_ast2.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/tr/sheetB.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/vp_sheet.jpg (trailer 29.4–31.0 s)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/yt/d2ByJWrsoec_hq1.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/teaser_gp.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/ov_stack.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/skins2.jpg
- **Depiction for shorts:**
  - Black rifle, dark-green top capsule, snake-head muzzle whose lime eye glows while she holds the lock.
  - The reticle goes black, then green, then white, and a small red crosshair hovers over the target's head.
  - The shot is a thin bright-green streak ending in a small yellow-green splash; the target pops into sparks or confetti.
  - A muzzle flash or snake "hiss" is [BBG News invention].
- **Confidence:** observed (look); partial (projectile: one 2026 thumbnail plus wiki text).

---

## Capital Pains (primary · BBR 1.3, May 3 2012 → BBG; red mode later removed, date unknown; 2026 status unverified)

- **Official text:** "If the NASDAQ stock index is down the day before, it shoots much faster, has more ammo, but does less damage and locks slower." ~ Official Battle Bears Gold description [Game text via wiki]. The wiki adds: "N.B. : This description is now outdated due to a stat change for the weapon." (https://battlebears.fandom.com/wiki/Capital_Pains)
- **Status and history:**
  - Released in 1.3 "together with the Daydreamer" [Fan-wiki]. "The Capital Pains used to be called the Stock Rifle" [Fan-wiki].
  - Price: "CAPITAL PAINS BUY NOW ! 200,000" Joules in May 2013 Gear Ups [Observed, File:Another_dead_eye_view.jpg and File:Mambas_Bly_by_applergamers.jpg]. BBG 2.20 (May 29, 2015): "Capital Pains reduced from 200,000 joules to 150,000 joules" [Fan-wiki]. Infobox: 150,000 J, level 15 [Fan-wiki].
  - Infobox stats: 60 damage, 2 ammo, 1.5 s, 5 s reload, 6.0 s lock [Fan-wiki].
  - BBG 2.6 [Fan-wiki transcription]:
    - fire rate 2.5→2
    - reload 5→4
    - lock radius 375→350
    - dispersion .02→.00
    - "Market Down lock time decreased from 6 to 1.5"
    - "Market Down warning time decreased from 3 to 1"
  - The page heading reads "Red Capital Pains is currently removed, and all stats listed for it currently do not exist." No date is given [Fan-wiki].
  - The wiki's demo video file was uploaded 2014-01-04 by ApplerGamers [Fan-wiki file metadata]. It is YouTube QQrU7iCrGoo, "Red Capital Pains demonstration" by the fan channel ApplerGamers [title/channel via oEmbed].
- **Look** [Observed]:
  - Gold € sign as the stock and gold $ sign as the grip/trigger guard (≈#D3B45C, light ≈#FFE17E). Red body (≈#931917). A green banknote-wad magazine. A barrel shaped like a zig-zag stock-chart line.
  - The barrel colour changes by image:
    - red, June 2012 (File:Capital_Pains_Rifle.png);
    - green, Nov 2012 loadout (≈#0C9206) and the Nov 2013 Gear Up File:Capitalpains.jpg (≈#0FA70A);
    - silver-grey, 2015 (≈#A6A6A0, File:Capital_Pains.jpg), although the wiki captions that image "in green". The grey may be the "white" state ("It is possible for the Capital Pains to be white") [Inference].
  - Scope: in June 2012 the in-game scope is topped by a black magic-8-ball marked "8", with a blue lens. In 2015 it is a black scope with a blue lens.
  - Concept "Stock Rifle": a black-to-red chart-line barrel ending in a green arrow, an 8-ball scope, a banknote magazine, gold €/$, and an "E PLURIBUS … ¢" coin.
  - Menu/HUD icon: a green zig-zag with €.
  - About 2 head-heights long, chart barrel included [Inference].
- **Firing:**
  - Standard lock-on [Fan-wiki].
  - "Once every 24 hours (at 00.00 GMT) the game checks this particular stock": positive (and 0.0) turns it green; negative turns it red [Fan-wiki].
  - Red mode in fan thumbnails shows ammo x/5 (2/5, 0/5, 3/5) [Observed]. The POV skin is black with red stripes, i.e. Solid Fisher [Inference].
- **Projectile:**
  - "if it is negative, the bullets are red, if it is positive, the bullets are green" [Fan-wiki].
  - Red-mode fan thumbnails hq1/hq3 show thin red dotted streaks from the player to a yellow target under a black reticle [Observed, low-res fan thumbnails; consistent with the wiki, not conclusive].
- **Impact / end result:**
  - The look is undocumented [Unverified].
  - A big yellow star-burst fills fan thumbnail hq2 but cannot be attributed to this rifle [Observed; attribution Unverified].
  - A white-lock hit is a one-shot headshot [Fan-wiki].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/cp_stack.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/cp15_zoom.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/cp12_zoom.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/cp12_zoom2.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/gnifle.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/new2.jpg (File:Capitalpains.jpg)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/adev.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/redcp_stack.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/aaaaa_small.png
- **Depiction for shorts:**
  - The €/$ "money gun" with an 8-ball scope and a zig-zag chart barrel.
  - Green day: a green barrel and green bullet streak. Red day: a red barrel and red streak (a ticker gag).
  - The hit splash is [BBG News invention]: a small burst of coins or confetti in the bullet's colour.
- **Confidence:** observed (look); partial (projectile colour from wiki plus fan thumbnails); unknown (impact, 2026 status).

---

## Mamba's Boy (primary · BBR 1.3.1, Jun 28 2012 → BBG; nerfed 1.4.2 Feb 2013, 2.6 Dec 2013, 2.20 May 2015; 2026 status unverified)

- **Official text:** "This gun will send you crying back to your mamba. Trade aim and damage for a faster rate of fire." ~ Official Battle Bears Gold description [Game text via wiki]. The wiki adds: "(This description is now inaccurate due to a stat rebalance)" (https://battlebears.fandom.com/wiki/Mamba%27s_Boy).
- **Status and history:**
  - Released "in week three of the four-week weapons release" [Fan-wiki].
  - BBR 1.4.2: clip 5→4, cooldown 0.35→0.4, dispersion 0.01→0.02 [Fan-wiki].
  - BBG 2.6 [Fan-wiki transcription]:
    - damage 23→22
    - fire rate .4→.35
    - clip 4→3
    - reload 3→4
    - "Speed decrease of -10% removed"
    - Ammo+1/+2 removed
  - That speed penalty is visible as "SPEED -10%" in red in the July 2012 (File:Mambas-Boy.PNG) and May 2013 (File:Mambas_Bly_by_applergamers.jpg) Gear Ups [Observed].
  - BBG 2.20: "Dead Eye and Mamba's Boy are nerfed" [Fan-wiki].
  - Infobox: 150,000 J, 20 damage, 4 ammo, 0.4 s, 4.0 s reload, green/white lock 3.0/3.0 s [Fan-wiki].
  - Bundles [Fan-wiki, Bundle Deals; banners Observed]:
    - Splinter Sale (Mamba's Boy, Daydreamer, Solid Fisher, Flawless Disguise), Sep 14–16, 2012.
    - Mean Mamba Bundle (Sniper, Mamba's Boy, the Demo skin Pandini), Mar 8–10, 2013; its banner shows Call Off Duty Astoria.
    - Yo Mamba Bundle (Urine Trouble, Mother of Nature, Mamba's Boy), May 10–12, 2013.
    - Astoria Weapon Starter Pack (Mamba's Boy + Eagle Standard), Sep 22–Oct 7, 2013.
- **Look** [Observed]:
  - A bright lime/yellow-green rifle (mean ≈#76AF14, light ≈#D8EC0F, dark ≈#296306) with dark-green spots. A lime capsule scope sits on top.
  - The barrel is a snake's body ending in a snake-head muzzle with an open pink-orange mouth.
  - Shown on the BBR 1.3.1 promo (upper right) as a green snake rifle with jaws open.
  - About 2 head-heights long [Inference].
  - The colour skins in the wiki gallery (Santa's Lil Sniper, She Fu, The Seer, Battle Damaged, Call Off Duty) hold this rifle [Observed].
- **Firing:** the wiki's text calls it "the fastest green-locking rifle", with a small lock radius and low damage per second. That conflicts with its own infobox, whose 3.0 s green lock equals the Viperifle's [Fan-wiki, conflicting]. A white lock still kills outright [Fan-wiki].
- **Projectile:**
  - No text description exists [Unverified].
  - Official "Astoria Overhaul" thumbnail hq1: lime-green Mamba-style HUD icon, ammo 8/10. Her lime rifle is in the foreground, and a thin pale-white streak runs toward a target under a reticle [Observed].
  - That the weapon is Mamba's Boy is [Inference]. The video's date and the meaning of 8/10 are [Unverified].
- **Impact / end result:** undocumented [Unverified]. A white-lock hit is a headshot kill [Fan-wiki].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/mamba_zoom.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/conv/Mambas_Boy.jpg.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/mambly.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/new1.jpg (File:Mambas-Boy.PNG)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/bbrw.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/bundles.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/new3.png (File:Astoria_banner_02.png)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/ssetup.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/ov_stack.png
- **Depiction for shorts:** a lime snake-skin rifle whose muzzle is an open-mouthed snake, firing quick thin pale streaks in rapid succession. Jaw-snap or hiss animation is [BBG News invention].
- **Confidence:** observed (look); partial (projectile seen only in one thumbnail of unknown era).

---

## Dead Eye (primary · shown Apr 2012 → released BBR 1.4.3 Apr 15 2013 / 1.4.3.1 Apr 23 2013 → BBG; 2.6 removed its health penalty; nerfed 2.20; in the Steam trailer, 2013 footage; 2026 status unverified)

- **Official text:**
  - "Got a problem? The Deadeye is your solution. She may not have the biggest clip but she definitely has the biggest kick. If you understand the value of power, this is the rifle for you." ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Dead_Eye).
  - BBR 1.4.3 note: "-The Dead Eye: Astoria's strong single shot sniper rifle." [Fan-wiki transcription of SkyVu's update text, Updates page]
- **Status and history:**
  - "first displayed on the old Battle Bears blog on April 13th. 2012" [Fan-wiki; blog unreachable, Unverified]. It reappeared Feb 1, 2013 as a "more reddish-tinged" redesign [Fan-wiki].
  - Price: the infobox says 60 Gas; the body says "It costs 120 Gas" [Fan-wiki].
  - May 2013 Gear Ups show "DEAD EYE BUY NOW ! 120" Gas with "HEALTH -5%" in red [Observed]. The official "STEALTH! SOLID FISHER + DEAD EYE 120 GAS / 50% OFF" bundle banner dates from Oct 19–22, 2013 [Observed banner; dates Fan-wiki].
  - BBG 2.6: reload 3.75→3; "Health Modifier increased from -5% to 0"; lock radius 200→350; warning time 3→2 [Fan-wiki transcription].
  - BBG 2.20: nerfed [Fan-wiki].
  - Damage: the infobox says 75; the body says "(85 damage)" and "It takes 9 seconds for the Dead Eye to reach green-locking", against the infobox's 2.0 s [Fan-wiki, conflicting]. Ammo 1 [Fan-wiki].
  - The Steam trailer shows her holding it on the ASTORIA / SNIPER title card [Observed], but that card is 2013 footage [Inference, strong]; the same card is in SkyVu's May 2013 trailer (see the note at the top). No 2026 capture in these notes shows the Dead Eye, so its 2026 status is [Unverified].
- **Look** [Observed]:
  - A rifle built from cream/ivory bones lashed with red-brown cords, with a flat shoulder-blade stock, a ribcage/vertebra receiver and a bone magazine.
  - The scope is a beaked, toothed animal skull. A very long thin bone barrel ends in a square muzzle with a dark bore.
  - The Apr 2012 concept ("Astoria's Deadeye (Primary)") is whiter bone with dark-green/black wraps.
  - Wiki: "The scope of this rifle is the head of an animal, moving as if it was biting something" and "made up of various bones held together by cowskin-strings. The scope is a skull, presumeably from a bird due to the large beak, though the teeth could indicate otherwise" [Fan-wiki].
  - The longest of her rifles, about 3 head-heights [Inference].
  - On the Steam trailer's title card (≈16.4–17.8 s) she holds it upright across her body in the Assassino outfit; the barrel leaves the top of the frame [Observed].
- **Firing (Steam trailer; 2013 footage [Inference, strong])** [Observed]:
  - ≈12.2–12.9 s: Astoria stands at the top of the Aztec-temple stairs (lava-sky map) in the red jacket.
  - At ≈12.4–12.8 s a thin, jagged, lightning-like white streak runs from the weapon at her chest to the head of a white-faced bear in a black suit at the foot of the stairs. In the 12.6 s frame it clearly starts at her hands.
  - The blue electric orb at the upper right of these frames is unrelated.
  - That this shot is the Dead Eye is [Inference]: skull smoke follows, and she reappears holding the Dead Eye.
- **Projectile:** the wiki says "a single, red, stream-like bullet" [Fan-wiki]; the Steam trailer (2013 footage [Inference, strong]) shows a WHITE jagged streak [Observed]. Use white, as the classic 2013 look; the 2026 bullet colour is [Unverified].
- **Impact / end result** [Observed, trailer]:
  - At ≈12.4 s translucent red smoke (≈#F9292D) blooms beside the target.
  - From ≈13.0 to 13.7 s, large glowing translucent red horned skull shapes (≈#F32833) rise above the target.
  - The target topples between ≈13.1 and 13.4 s and lies still.
  - This matches the wiki: "erupts into a flurry of glowing, transparent buffalo skulls. These are merely cosmetic" [Fan-wiki].
  - CAUTION: the orange flames on the target from ≈12.4 s come from a separate yellow-orange projectile that enters from off-screen right at ≈12.3 s. They are not the Dead Eye's effect [Observed; attribution Inference].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/conv/DeadEye.jpg.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/conv/Dead_Eye.jpg.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/de_concepts.png (TheDeadEye-trans, Deadeye-concept-trans, Dead_eye_blog)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/new3.png (File:Dead_Eye_Concept.jpg)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/conv/143releasepic.png.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/adev.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/yadev.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/bundles.png (Stealth)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/tr/sheetA1.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/line_126.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/skull_pair.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/tr/sheetA2.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/tr/sheetA3.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/tr/sheetA4.jpg
- **Depiction for shorts:**
  - A long bone rifle with a biting skull scope, held upright for her hero pose. Animating the skull's bite is wiki-documented.
  - Fired: a thin jagged white streak; ghostly red horned-skull smoke rises and fades; the target flops over in a puff of sparks.
  - No flames unless another bear is shooting, and no blood.
- **Confidence:** observed.

---

## Crossbow / "Unicorn Crossbow 2.0" (primary · BBG 2.2, Aug 21 2013; reworked 2.6; 2026 status unverified)

- **Official text:** "Leave it to Astoria to make a rapid fire weapon that shoots unicorn horns. Even worse is that she can charge up the weapon and release a stronger attack! What's next jackelope weapons?" ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Crossbow_(BBG)).
- **Status and history:**
  - BBG 2.2 [Fan-wiki, Updates].
  - SkyVu's "BATTLE BEARS GOLD Update 2.2 Weapon Recap" (BcEeAzXFChI) [Canon: title/channel via oEmbed]. Its thumbnail hq1 shows "NEW WEAPONS!", "LOCK AND LOADOUT! Switch characters during battle!", and Astoria in the Assassino red jacket aiming the white crossbow [Observed].
  - BBG 2.6: "Clip size reduced from 100 to 2", heat per shot 12→1, damage 20→50, charged damage 50→120 [Fan-wiki transcription].
  - BBG 2.20: 240,000→150,000 J [Fan-wiki].
  - Current infobox: 15 ammo; damage "Uncharged:15*" / "Charged: 230*"; 2 s reload; 1.5 s charge; "20% Special Speed Increase". The numbers are self-contradictory: the page notes "Damage stats listed in game are different than tested damage stats" [Fan-wiki].
  - "It is called '2.0' due to Oliver having a weapon called the 'Unicorn Crossbow' in Battle Bears: Zombies" [Fan-wiki].
- **Look** [Observed]:
  - A pearl-white/silver crossbow with cream inset panels and diamond motifs, and a unicorn-head front.
  - A lavender crystal horn-bolt (≈#D2AAEB; deep ≈#B278F2) is loaded at the front; the string is lavender.
  - The concept sheet shows four finishes: silver (violet glow), gold (pale glow), gunmetal (red glow) and copper (cyan glow).
  - Limb span about 2 head-heights; held two-handed at chest [Inference].
- **Firing:**
  - Manual aim with no lock, so no headshots [Fan-wiki].
  - On charge "it zooms in more than normal" and "its internal barrel with also rotate at a rapid rate and shine a bright purple aura"; "Using a charged shot will be considered using a full magazine of ammo" [Fan-wiki].
  - Overhaul thumbnail hq2 [Observed]: a white-pink muzzle flash and pink-violet light streaks leaving a silver weapon, with a white crossbow HUD icon and ammo 3/3. A yellow six-segment wheel at the left of the screen may be a charge meter [Inference].
- **Projectile:** "shining unicorn horns" [Fan-wiki]; in the thumbnail, pink-violet light streaks [Observed].
- **Impact / end result:**
  - Charging adds "AOE damage upon a hit on either an opponent or an object". "A direct hit from a charged blast will deal 230 damage" [Fan-wiki].
  - It is in Category:Explosives, and "It was the first Sniper weapon that could directly cause the player to suicide" [Fan-wiki].
  - The look of the burst is [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/xbow_stack.png (Crossbow.jpg, UnicornCrossbowconceptart.jpg, Crossbow_coming_to_BBG!!!.jpg)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/recap_stack.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/ov_stack.png
- **Depiction for shorts:** a white unicorn-head crossbow spitting quick lavender horn-bolts. On charge, the inner barrel spins and glows purple, and one big horn flies and bursts. The burst style (a lavender sparkle pop) is [BBG News invention].
- **Confidence:** observed (look, muzzle); partial (projectile, impact).

---

## Blow Dart (primary · BBG 2.6, Dec 20 2013; 2026 status unverified)

- **Official text:** "Just because it is the future does not mean there cannot be old school weaponry. Watch out for exploding darts!" ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Blow_Dart).
- **Status:**
  - 60 Gas, level 1; released v2.6 [Fan-wiki; the 2.6 log lists "Sniper primary - Blow Dart"].
  - Also in the "Lunar New Year" bundle (Astoria, She Fu, Daydreamer, Golden Dragon, Blow Dart). That bundle's banner shows She Fu Astoria holding it [Fan-wiki, Bundle Deals; banner Observed].
- **Look** [Observed]:
  - An orange-copper blowgun tube (≈#AF4D22) with glowing magenta/pink stripe panels (≈#D755C7, light ≈#FB6BF9) and a purple section. It ends in an angular head with a pink-glowing slot at the muzzle.
  - Held two-handed like a rifle; at least about 1.1 head-heights long, heavily foreshortened [Inference].
- **Firing:** manual aim with no lock: "a 100% accurate manual-aim weapon". 0.5 s rate of fire, 4 ammo, 4.5 s reload [Fan-wiki].
- **Projectile:** "a small projectile" at 1,000 u/s (infobox) that sticks to "any solid surface (players included)" [Fan-wiki]. Its look is not observed [Unverified].
- **Impact / end result:**
  - It detonates 6 s after contact. "The explosion it creates is distinguishable because of its blue tinge and large Area of Effect (AoE)" [Fan-wiki].
  - Explosive damage 25–50; "the player is prone to suicide" [Fan-wiki].
  - The explosion is not observed [Unverified].
  - The trivia says it is "the only Sniper weapon that can be enhanced with Explosives+ Equipment". That is contradicted by the Fidget Boomer and I Lava U pages, which both list Explosions+ effects [Fan-wiki, conflicting].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/bd_fb.jpg (Blowdart.png, BlowDart.jpg)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/bundles.png (New_Year's_bundle.PNG)
- **Depiction for shorts:** a puff from the copper tube; a tiny dart sticks to the target; a 6-second comic beat; then a large blue-tinged blast. The dart's look and the blinking countdown are [BBG News invention].
- **Confidence:** observed (look); documented (impact).

---

## Art of War (primary · revealed Apr 27 2012, declared unused Aug 8 2013, released BBG 2.11 Aug 27 2014; 2026 status unverified)

- **Official text:** "Paint the battlefield red, or orange, or yellow, or green, or blue, or violet. It doesn't really matter as long as its your enemies pallet." ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Art_of_War).
- **Status:**
  - 60 Gas. Infobox: 45 damage, 3 ammo, 1.0 s, 5.5 s reload [Fan-wiki].
  - Revealed on the blog Apr 27, 2012 "fully modelled and textured" alongside the Toucan; declared unused Aug 8, 2013; released in 2.11 [Fan-wiki; blog and Facebook unreachable, Unverified].
- **Look** [Observed]:
  - A red barrel (≈#DF372D) with gold Chinese characters. The render and concepts show the traditional form 孫子兵法; the wiki types the simplified 孙子兵法 ("The Art of War").
  - A black-and-yellow receiver, a paintball hopper on top full of multicolour balls, and a blue gem on the side.
  - The muzzle is a paintbrush tip loaded with red, orange, yellow, green and blue paint.
  - Concept line art: "The Art of War / Paintball Sniper Rifle", with a scope, a hopper and a small brush mounted under the barrel.
  - No in-hand image was found, so its size relative to the bear is [Unverified].
- **Firing:** no lock, so no headshots [Fan-wiki].
- **Projectile:** "a single stream-like bullet will be fired in the exact same direction of the crosshairs" [Fan-wiki]. It is "thin" [Fan-wiki].
- **Impact / end result:** "erupting into a flurry of paint, however, it is merely cosmetic and has no added functionality" [Fan-wiki]. Not observed [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/aow_stack.png (Images_(1).jpeg, ArtofWar.png, ArtofWarconceptart.png)
- **Depiction for shorts:** a brush-tipped paintball rifle fires a thin streak that splats into a burst of red, orange, yellow, green, blue and violet paint (the official text's list). The splat shape is [BBG News invention].
- **Confidence:** observed (look); documented (projectile, impact).

---

## Fidget Boomer (primary · BBG 2.27, May 29 2017; 2026 status unverified)

- **Official text:** "Have toy tricks gone too far!? Explosions are safe right?" ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Fidget_Boomer).
- **Status:** 60 Gas. Released in 2.27 alongside Spin Baby Spin and Hazard Toy [Fan-wiki].
- **Look** [Observed]: a large dusty-pink/mauve chrome three-lobed fidget spinner (mean ≈#6E4B55, highlights ≈#AC838E), held raised in one hand at head height. About 2 head-heights across, but foreshortened toward the camera [Inference].
- **Firing:**
  - 0.3 s rate of fire, 4 ammo, 3 s reload; 40–70 explosive damage [Fan-wiki].
  - Projectile speed conflicts three ways: 3000 u/s (infobox); "This has the fastest projectile speed in the game" (trivia); "the slow projectile speed can be an issue" (body) [Fan-wiki].
  - Explosions+ applies [Fan-wiki].
- **Projectile:** probably the spinner itself, thrown [Inference]. Not observed.
- **Impact / end result:** "upon contact with a surface experiences a short delay before exploding (akin to the TNT Launcher)"; it "does not have a secondary effect" [Fan-wiki]. The explosion is not observed [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/bd_fb.jpg (FidgetBoomer.jpeg)
- **Depiction for shorts:** she flicks the chrome-pink spinner; it whirs, lands, wobbles for a beat and explodes. The spin-whistle and the explosion colour are [BBG News invention].
- **Confidence:** observed (look); documented (impact); partial overall.

---

## Tomahawk (secondary · default · BBR 1.1, 2011 → BBG; 2026 status unverified)

- **Official text:** "Unleash a terrified and angry hawk that temporarily blinds any player it hits! Great for running away from opponents that get too close." ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Tomahawk).
- **Status:**
  - Default. It "was the only secondary for the Sniper before v1.3" [Fan-wiki].
  - BBG 2.6: duration 15→10, reload 2→1.5 [Fan-wiki transcription].
  - Infobox: 15 s duration, 0.75 s reload, 3000 u/s, and "15% Special Speed Increase". The body says 10 s, and says the Tomahawk "doesn't possess" the special-speed modifier [Fan-wiki, conflicting].
- **Look** [Observed]:
  - A brown hawk with a cream chest, a yellow hooked beak with a dark tip, yellow talons and blue-tipped feathers, trussed in coils of tan rope (body ≈#997646, light ≈#DBC994).
  - She holds it upright by the legs, raised at shoulder/head height. About 1.7 head-heights tall [Inference].
  - Concept art ("tomahawk"): the same bird in greyscale and in colour, with an orange eye and rope across the beak.
  - Wiki: "It appears as a restrained hawk, tied up with a coil of rope" [Fan-wiki].
- **Firing:** thrown: "the tied hawk will rotate forward with straight trajectory". It does no damage, has "no noticeable AoE", and is "quite hard to aim". A bug can make it "fly backwards behind the player" [Fan-wiki].
- **Projectile:** the rope-bound hawk tumbling forward [Fan-wiki]. Not observed in flight.
- **Impact / end result:**
  - Wiki: "it will be let free of its retrains and violently thrash around their face, blinding them with a flurry of wings and feathers"; a partial blind of 10 s (15 s per the infobox) [Fan-wiki].
  - Fan screenshot "Tomahawk in effect" (File:Download_(16).jpg; Aztec lava map; target labelled "ASTORIA"): a large mass of brown and reddish-brown wings and feathers covers the target's head and upper body [Observed].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/hawk_sheet.jpg (Tomahawk.jpg, Tomahawk_concept.jpg)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/hawk2_sheet.jpg (Tomahawk.png Mar 2012, Tomahawk.PNG June 2012, Download_(16).jpg)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/new3.png (Sniper_christmas.png: Santa's Lil Sniper holding the Tomahawk)
- **Depiction for shorts:** she lobs the rope-bound hawk, which tumbles end over end. On contact the ropes pop and an angry flurry of wings and feathers smothers the victim's face; the victim flails blind, with no injury. The bird's facial acting is [BBG News invention].
- **Confidence:** observed.

---

## Eagle Standard (secondary · BBR 1.3.1, Jun 28 2012 → BBG; 2026 status unverified)

- **Official text:** "Flapping around in someone's face, getting up in their business and ruining their day for your own selfish purposes? Sounds like blatant patriotism to me!" ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Eagle_Standard).
- **Status:**
  - July 2012 Gear Up: "BUY NOW 37,500" Joules and "SPECIAL SPEED -15%" in red [Observed].
  - BBG 2.6: reload 2.5→2, projectile speed 1000→1200, "Cooldown multiplier decreased from -15% to -20%" [Fan-wiki transcription].
  - Infobox: 75,000 J, 4 s blind, 6 ammo, 0.2 s rate of fire, 4.0 s reload, 3000 u/s, "15% Special Speed Increase" [Fan-wiki].
  - Modifier direction:
    - Pre-2.6 it is documented as a penalty: the red "-15%" in the 2012 Gear Up, and the trivia "Prior to v2.6, the Eagle Standard had a 15% special speed stat modifier … it actually increases the amount of time it needs to recharge" [Observed + Fan-wiki].
    - For post-2.6 BBG, the page body says "It has a 20% special speed boost, which decreases the time" [Fan-wiki], and the sign in the 2.6 line is ambiguous. The current and 2026 direction is [Unverified].
- **Look** [Observed]:
  - A bald eagle: white head, yellow-orange hooked beak, dark-brown body bound in tan/gold rope bands, yellow talons and a white tail fan below.
  - Held upright by the legs at shoulder/head height, about 1.6 head-heights tall [Inference].
  - The BBR 1.3.1 promo shows a bald eagle with wings spread over red-white-blue rays and stars. The official "ASTORIA WEAPON STARTER PACK" banner shows an eagle with spread wings behind Astoria [Observed].
- **Firing / projectile:** "The Eagle Standard is a reskin of the Tomahawk"; "the tied eagle will rotate forward with straight trajectory" [Fan-wiki].
- **Impact / end result:** it is "let free of its retraints and violently thrash around their face, blinding them with a flurry of wings and feathers"; a partial blind of 4 s [Fan-wiki]. It probably looks like the Tomahawk's flurry in white and dark-brown feathers [Inference; not observed]. A fan video "Trolling with Eagle Standard" (9s3y4u53B2Y) returns 403 on oEmbed [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/hawk_sheet.jpg (EagleStandard.jpg)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/hawk2_sheet.jpg (Eagle-Standard.PNG)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/bbrw.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/bundles.png (AstoriaStarter.jpg)
- **Depiction for shorts:** the same throw-and-flap gag as the Tomahawk, but with a rope-wrapped bald eagle. A star-spangled sparkle trail is [BBG News invention], inspired by the official promo's red-white-blue rays.
- **Confidence:** observed (look); documented (effect).

---

## Daydreamer (secondary · BBR 1.3, May 3 2012 → BBG; status icon changed 1.3.2; aim inversion removed later; 2026 status unverified)

- **Official text:** "Turn your opponents' daydream into a nightmare. Place this badboy on the ground and any yutz that steps on it will have their controls reversed for a few seconds." ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Daydreamer).
- **Status and history:**
  - June 2012 Gear Up: "BUY NOW 40" Gas [Observed]. The body says 40 Gas, the infobox 32; level 10 lock [Fan-wiki].
  - BBR 1.4.2: reload 0.1→1.0 [Fan-wiki]. BBG 2.6: clip 1→5, reload 1→2, Ammo+ removed [Fan-wiki transcription].
  - The overhead icon "used to have a turquoise feather like a Nuggs' … but this was changed to a green question mark as of v.1.3.2" [Fan-wiki].
  - The aiming inversion "was eliminated in a much later update" (date unknown) [Fan-wiki].
- **Look** [Observed]:
  - A gold/bronze wire geodesic lattice (≈#A28B5B) with a silver disc at the centre and a pale-blue crystal shard sticking out.
  - Held in one hand at hip height, about 0.8 head-heights across [Inference].
  - The Lunar New Year banner draws it as a round web with a dangling blue crystal [Observed].
  - Wiki: "It appears as a standard native American dream catcher" [Fan-wiki].
- **Firing:** placed on the ground with a 2 s placement delay and a small trigger radius; no damage [Fan-wiki]. "When placed on the ground the Daydreamer is almost invisible (it is only noticeable by a small white crystal sticking out from the ground)" [Fan-wiki].
- **Impact / end result:**
  - **Status "Controls Reversed"**: "a green question mark will appear over the player's head … background music will be disabled and other sounds will feature an mild echo" [sic] [Fan-wiki, Status Effects].
  - Movement is reversed for 8.0 s per the body (20 s per the infobox). "This weapon can be triggered by explosives without any effect on the player" [Fan-wiki].
  - Possible trigger visual: an unused fan upload "Detonate daydreamer" (Interamnia, May 10, 2013) shows a wide ring of magenta electric arcs over the floor and columns of white bubbles around a cyan-ringed pad [Observed]. Its link to the Daydreamer rests on the filename only [Inference, medium-low].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/dd_sheet.jpg (Daydreamer.jpg, Daydreamer.PNG, Astoria-daydreamer.png)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/detdd.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/gnifle.png (loadout icon)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/bundles.png (New Year's bundle)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/skins2.jpg (Exercisist holding it)
- **Depiction for shorts:** she sets down the gold wire sphere and only its white crystal tip shows. A bear steps on it: a green "?" pops over its head, the music cuts to an echoey hush, and it walks backwards whenever it tries to go forward. The magenta-arc floor ring is optional and must be flagged as a fan-screenshot reference. Draw it as a sci-fi wire gadget, with no cultural costume styling [BBG News invention].
- **Confidence:** observed (look); documented (status effect); partial (trigger visual).

---

## Fairy's Dust (secondary · BBR 1.4.3 Apr 15 2013 / 1.4.3.1 Apr 23 2013 → BBG; in the Steam trailer, 2013 footage; named in a 2026 playtest loadout)

- **Official text:**
  - "Enemy got you in their cross hairs? Toss this lil' sack-o-magic and give 'em the slip. This magical concoction can be a real life saver!" ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Fairy%27s_Dust).
  - BBR 1.4.3 note: "-Fairy's Dust: Astoria's magical concoction that confuses enemies and conceals movement." The 1.4.3.1 note calls it "-Fairy's Sparkle" [Fan-wiki transcription].
- **Status:**
  - BBG 2.20: 165,000→125,000 J [Fan-wiki].
  - BBG 2.6: "uration [sic] increased from 3.5 to 4", clip 2→1, projectile speed 900→1000 [Fan-wiki transcription].
  - Infobox: 1.5 s, 1 ammo, 3 s reload, 1,000 u/s, "5% Speed Increase, 10% Special Speed Increase" [Fan-wiki].
  - 2026: the hq3 thumbnail of JustNubz's "Battle Bears Gold Playtest #3 Part 1" (qt43iTdANbM, build 3.0.2) shows a Sniper loadout reading "SECONDARY FAIRY'S DUST" with a pink-sack icon [Observed, low-res; title via oEmbed; also in 2026.md].
- **Look** [Observed]:
  - A glittery translucent pink-to-purple sack (≈#DD7ADB, light ≈#FB9CEA) tied with a red ribbon under a crumpled blue/cyan crystal-like top, with yellow, pink and purple four-point star sparkles floating off it.
  - Held in one hand, about 0.8 head-heights tall [Inference].
  - It appears as an icon on the "1.4.3 UPDATE COMING SOON / WILD N' WACKY WEAPONS" promo, and the Old-Timey skin preview holds it.
  - Wiki: "a purple sack with unknown, sparkling dust inside" [Fan-wiki].
- **Firing:** thrown; it bursts "upon coming into contact with a surface" [Fan-wiki].
- **Projectile:** the tiny sack, trailing yellow and pink star sparkles [Observed, fan "close up during flight" screenshot].
- **Impact / end result:**
  - Wiki: "a large, blinding cloud of 'fairy dust'"; "a huge, harmless cloud of purple dust that can partially block a player's sight"; it lasts 4 s, and "sniper rifles can still lock on to an enemy inside the cloud" [Fan-wiki].
  - 2013 fan screenshots: a faceted, crystal-like violet-purple cloud (≈#9901E1) with star twinkles [Observed].
  - **Steam trailer (2013 footage [Inference, strong])** [Observed]:
    - ≈13.8–14.0 s: Astoria (Assassino jacket) holds the sparkly sack at the top of the stairs.
    - ≈14.1 s: a pink burst at her position.
    - ≈14.2–16.0 s: a huge translucent faceted cloud swallows the stairs. It is hot magenta (≈#F323F4–#FE26FE) shading to violet (≈#B11EFD), with white twinkles; other players' pink and white shots streak through it.
    - ≈16.1–16.3 s: she drops into view in front of the cloud, holding the Dead Eye.
    - The title card follows at ≈16.4 s.
  - The wiki says "purple"; the 2013 fan screenshot reads violet; the Steam trailer, also 2013 footage, leans magenta. The 2026 cloud colour is [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/fd_imgs.jpg (FairysDust.jpg, Fairy's_dust_close_up_during_flight.jpeg)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/fdcloud.png (Cloud_for_fairy_dust.jpg)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/aaaaa_small.png (Aaaaa.jpg)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/conv/143releasepic.png.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/tr/sheetA2.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/tr/sheetA3.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/skins2.jpg (Old-Timey)
- **Depiction for shorts:** she tosses the sparkly pink sack, which trails tiny stars; it poofs into a giant faceted magenta-violet cloud with twinkles; she vanishes, then drops out deadpan with the Dead Eye. This beat is lifted from the Steam trailer (2013 footage). The cloud is harmless and lasts about 4 s.
- **Confidence:** observed.

---

## Rake (secondary · in BBG by Jan 2014, release version undocumented; 2026 status unverified)

- **Official text:** "Stop your opponents dead in their tracks with this exciting new gardening tool!" ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Rake).
- **Status:**
  - 100,000 J, no level lock. Infobox: 110 damage, 10 ammo, 1 s reload, 0.5 s cooldown, "5% Health Increase, 10% Special Speed Increase" [Fan-wiki].
  - "It used to do 999 damage" [Fan-wiki].
  - The only image was uploaded 2014-01-25 by ApplerGamers [Fan-wiki file metadata].
  - The page calls it "the only secondary that deals damage", which ignores I Lava You (25–60 explosive damage) [Fan-wiki, conflicting].
- **Look** [Observed]:
  - A dark-grey riveted metal rake head (≈#42464A) with five bright turquoise teeth (≈#34E6B8). The Gear Up shows it held head-up; the handle is mostly hidden.
  - The skin in that image matches File:Solid_Fisher.png: black suit, red stripes, three glowing red head-lamps [Observed comparison].
- **Firing:** "placed on the ground, much like the Daydreamer". It is single-use and stackable, and "The Rake can also be triggered if you shoot at it" [Fan-wiki].
- **Impact / end result:** it "will spring up and damage any enemy that walks into the Rake"; "Rakes can be removed by explosives"; "It is possible to commit suicide with this weapon" [Fan-wiki]. The spring-up is not observed [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/rake_small.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/rake_teeth.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/misc.jpg (Solid_Fisher.png)
- **Depiction for shorts:** the classic step-on-the-rake gag: the turquoise-toothed rake springs up and the handle bonks the victim's face, with stars and no injury [BBG News invention, consistent with "spring up and damage"].
- **Confidence:** observed (look); documented (effect).

---

## I Lava You / "I Lava U" (secondary · BBG 2.51, Apr 13 2018; 2026 status unverified)

- **Official text:** none found. The page quotes no official description, and its infobox titles it "I Lava U" (https://battlebears.fandom.com/wiki/I_Lava_You).
- **Status:** 60 Gas, level 1 [Fan-wiki]. "New weapon for Sniper (BBG) - the I Lava You", 2.51, April 13, 2018 [Fan-wiki, Updates]. "This weapon is based off of the unreleased Battle Bears Ultimate Lavarifle weapon" [Fan-wiki].
- **Look** [Observed]:
  - A compact gun whose body is dark-brown lava rock with glowing red-orange fissures (≈#A03520, hot ≈#FF6855), plus grey metal barrel and scope parts and a red glowing lens.
  - Held two-handed at chest, about 1.1 head-heights long [Inference].
  - The image is in the Sniper (BBG) generic-skins gallery (uploaded 2018-05-12, comment "Sniper with I Lava U") [Fan-wiki file metadata]. The weapon page itself has no image.
- **Firing:** "It shoots proximity based mines in a straight line until it collides with a wall or floor … The mines can be detonated manually if you click the reload button." 1.5 s rate of fire, 4 ammo, 4.0 s reload, 1200 u/s, 1.0 s priming, 100-unit trigger radius; Explosions+ applies [Fan-wiki].
- **Projectile:** mines. Not observed [Unverified].
- **Impact / end result:** "These explode if an enemy gets close to them", for 25–60 damage [Fan-wiki]. Not observed [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/ilava_small.png
- **Depiction for shorts:** glowing lava-rock blobs fly straight, stick where they land and pulse, then erupt in orange fire-sparks when a bear walks near. The look of the mines and the blast is [BBG News invention].
- **Confidence:** observed (look); documented (mechanic).

---

## Battering Ram (melee · default · BBR era → BBG; 2026 status unverified)

- **Official text:** "Using revolutionary "Ram Skull" technology for maximum bashing ability, this is a weapon of last resort." ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Battering_Ram).
- **Status:**
  - Default melee: "It deals 30 damage and provides a 40% boost to the player's special speed" [Fan-wiki].
  - Equipped in the Mar 2012 BBR Gear Up [Observed].
  - BBG 2.6: Melee+1 10→5, Melee+2 15→10 [Fan-wiki transcription]. The page still lists +10/+20.
- **Look** [Observed]:
  - A grey stone club whose head is a curled ram horn (tan ridged rings, ≈#5A533C mean, light ≈#D2C394), lashed with dark purple-brown straps, with a wrapped grip. The in-game texture has orange, purple and green flecks near the horn.
  - The concept art shows the same horn shape and no skull.
  - Held one-handed, about 1.4 head-heights long [Inference].
- **Firing:** a melee swing.
  - The Sniper's class-wide melee lines (Sniper (BBG) page, not specific to this club): swing, "Watch it, swinging a club here!" and "Eee-yaaa!"; melee kill, "Not bad. You got closer to me than most corpses." and "I thought your head would be harder." [Fan-wiki].
- **Impact / end result:** not documented [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/bram.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/bram_zoom.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/conv/Battering_Ram_Concept.jpg.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/ssetup.png (loadout icon)
- **Depiction for shorts:** a reluctant "last resort" bonk with the curled stone horn. The cartoon "thunk", the stars and the stagger are [BBG News invention].
- **Confidence:** observed (look); unknown (hit effect).

---

## Brr-Ram-Ewe (melee · BBR era, in the Mar 2012 Gear Up → BBG; 2026 status unverified)

- **Official text:** "Freshly shipped and still cold remains from an authentic once-living ram!" ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Brr-Ram-Ewe).
- **Status:**
  - Mar and June 2012 Gear Ups: "BUY NOW 90,000" J [Observed]. Now 105,000 J, level 13 [Fan-wiki].
  - The page says 30 damage, "a 20% special speed stat modifier and a 10% increase in the player's health"; "Prior to v2.6, the Brr-Ram-Ewe had no stat modifier" [Fan-wiki].
  - BBG 2.6: damage 33→35, cooldown modifier 0→5% [Fan-wiki transcription].
- **Look** [Observed]: an icy, pale-blue crystalline curled-horn club (≈#5484A2, light ≈#8DBAD8, white highlights) with a dark handle and teal-blue wraps. About 1.5 head-heights long [Inference].
- **Firing:** a melee swing.
- **Impact / end result:** any freeze effect is undocumented [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/melee_sheet.jpg (Brr-ram-ewe.png, Brr-ram-eve.PNG)
- **Depiction for shorts:** an ice-horn bonk. A puff of frost sparkles is [BBG News invention]; no freeze status is documented.
- **Confidence:** observed (look); unknown (hit effect).

---

## Cybernetic Ram (melee · BBR era → BBG; 2026 status unverified)

- **Official text:** "An ebony club imbued with needless fiery energy canals!" ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Cybernetic_Ram).
- **Status:**
  - Gear Up prices [Observed]: "300" Gas (Mar 2012); "50" (June 2012); "30" (July 2012).
  - That matches the trivia: "Before update 1.3, the Cybernetic Ram cost 300 Gas. Its price was then lowered to 50 Gas, before being changed to the current price of 30 Gas" [Fan-wiki]. The page body's "It costs 20 Gas" at level 12 is unexplained [Fan-wiki, conflicting].
  - BBG 2.6: damage 35→40, speed modifier 0→10% [Fan-wiki transcription].
- **Look** [Observed]: a black curled-horn club laced with glowing orange-red circuit/energy channels (≈#D27D45, light ≈#FFB673), with a ring motif on the horn. About 1.5 head-heights long [Inference].
- **Firing:** a melee swing.
- **Impact / end result:** undocumented [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/melee_sheet.jpg (Cybernetic_ram.png, Cybernetic-ram.PNG, Golden-Dragon.PNG)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/bram.png
- **Depiction for shorts:** a black horn club whose orange circuits flare on the swing. Ember sparks on contact are [BBG News invention].
- **Confidence:** observed (look); unknown (hit effect).

---

## Golden Dragon (melee · BBR 1.3.1, Jun 28 2012 → BBG; 2026 status unverified)

- **Official text:** "Ever the connoisseur, an appreciator of the fine arts, it is up to you to make everyone else understand the beauty of this piece. Beating them up the side of the head with it is the logical place to start." ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Golden_Dragon).
- **Status:**
  - 50 Gas, 55 damage, "a 20% increase in the player's Special Speed"; "Prior to v2.6, the Golden Dragon had no stat modifier" [Fan-wiki].
  - BBG 2.6: Melee+1 10→5, Melee+2 18→10 [Fan-wiki transcription].
  - The 2015 Gear Up (File:Golden_Dragon.jpg) shows "HEALTH +10%" while she holds it [Observed], which conflicts with the wiki's special-speed modifier.
- **Look** [Observed]:
  - A gold, scaled dragon-head club (≈#9B6811, light ≈#DEA00F) with a green gem eye, a dark crest and a scaled shaft.
  - Coiled at the centre of the BBR 1.3.1 promo. She Fu Astoria holds it on the Lunar New Year banner.
  - It is the HUD melee icon in File:Aaaaa.jpg.
  - About 1.8 head-heights long [Inference].
- **Firing:** a melee swing.
- **Impact / end result:** undocumented [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/melee_sheet.jpg (Golden-Dragon.PNG, Golden_Dragon.jpg)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/bbrw.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/bundles.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/aaaaa_small.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/gnifle.png
- **Depiction for shorts:** an "art connoisseur" bonk with a gold dragon-head club. Gold-glint sparks are [BBG News invention].
- **Confidence:** observed (look); unknown (hit effect).

---

## Toucan (unreleased Tomahawk upgrade · concept, 2012)

- **Official text:** none found. The wiki says it was revealed with the Art of War as "an upgraded Toucan version of the Snipers' Tomahawk" (blog, Apr 27, 2012) [Fan-wiki; blog unreachable, Unverified].
- **Look** [Observed]: a painted toucan with wings spread: black plumage, yellow throat and chest, an orange beak, a green-and-blue eye patch and a red under-tail. Wiki upload 2012-11-26 [Fan-wiki file metadata].
- **Firing / projectile / impact:** never released; none documented [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/concepts.png
- **Depiction for shorts:** easter egg only, labelled as an unreleased concept. Any effect is [BBG News invention].
- **Confidence:** observed (concept look only).

## Astoria's Super Scope (unreleased concept · wiki upload 2012-11-22)

- **Official text:** none; the art is titled "ASTORIA'S SUPER SCOPE" [Observed].
- **Look** [Observed]: a telescoping spyglass-rifle with a small flintlock-style pistol grip, an engraved silver tube, a brown leather cone stitched with X marks, gold bands and a big domed lens, plus a separate "Front" view of the round lens.
- **Firing / projectile / impact:** none documented [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/concepts.png
- **Depiction for shorts:** easter-egg prop only [BBG News invention for any use].
- **Confidence:** observed (concept look only).

## Slumberbun land mine (unreleased concept · wiki upload 2012-11-20)

- **Official text:** none; labelled "Slumberbun- land mine" [Observed].
- **Look** [Observed]: a sleeping golden bread-bun dome (annotated "Not Actual Size") that wakes, when triggered (arrow), into a screaming bun with bulging red eyes.
- It looks like an early relative of her ground traps [Inference].
- **Firing / impact:** none documented [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/concepts.png
- **Depiction for shorts:** easter egg only; any explosion is [BBG News invention].
- **Confidence:** observed (concept look only).

---

## BB Heroes Sniper Rifle + "Explosive Retreat" Ultimate (BBH, added May 2023; not BBG)

- **Official text:** "Astoria wields a sniper rifle for long-distance attacks, dealing more damage from afar. Up close, she's vulnerable but compensates with her "Explosive Retreat" Ultimate, diving away from the action when enemies get too close." [Canon, battlebears.com/pages/characters, re-fetched 2026-10-17]
- **Stats** [Fan-wiki]:
  - Wiki BBH table: Sniper Rifle "2000 max" damage, "Very long" range; Explosive Retreat "4 x 670"; 300 Shards; May 2023. The table's blurb: "Agile and precise, a deadly sniper, Astoria's main weapon is range. You are at a severe disadvantage when enemies are close by so plan your equipment and special accordingly!"
  - Oct 14, 2024 balance: "Max Range Attack Damage Reduced (-20%)", "Min Rage [sic] Attack Damage Increased (+20%)".
- **Look / firing / impact:** not researched here [Unverified].
- **Depiction for shorts:** never mix into BBG-era shorts without an on-screen era label.
- **Confidence:** documented (text only).

## BB Overclock "Viper Rifle" (BBO; not BBG)

- **Official text:** none on the page.
- **Stats and history** [Fan-wiki]:
  - Hitscan and zoomable: 70 damage, 7 ammo, 1.2 RoF, 4.1 reload, 20% crit chance, 300% crit damage, 130 Gems.
  - "It is a direct carryover of the Viperifle (BBG) designed for Overclock."
  - "The Viper Rifle was originally only able to be obtained as a reward for Battle Bears Gold players who linked their accounts on Launch Day."
- **Look:** the page has no image [Unverified].
- **Confidence:** documented (stats only).

---

## 2026 re-release: what official 2026 material shows

- **Steam store** [Canon]: "-SNIPER: Astoria" and "80+ PRIMARY WEAPONS / 60+ SECONDARY WEAPONS / 50+ MELEES"; release date "Nov 4, 2026".
- **Steam trailer "Battle Bears Gold Premium - Trailer"** (the only movie in appdetails). SkyVu re-used it on the 2026 Steam page, but it is 2013 footage [Inference, strong] and does not show the 2026 build (see the note at the top). What it shows [Observed]:
  - ≈12.2–13.7 s: the Dead Eye shot (white jagged streak) and red horned-skull smoke.
  - ≈13.8–16.3 s: Fairy's Dust.
  - ≈16.4–17.8 s: ASTORIA / SNIPER title card with the Dead Eye, Assassino jacket.
  - ≈30.0–30.8 s: Viperifle in the Call Off Duty skin (Team Blue), in the Space Oddity clip.
- **Steam screenshots** (trailer frames; 2013 footage [Inference, strong]) [Observed]: 01, a frame of the Space Oddity clip, shows the Viperifle in Call Off Duty. 04 shows a tiny default red-gear Astoria with a dark green-topped rifle (Viperifle by [Inference]). 00, 02 and 03 show no identifiable Astoria.
- **Official teaser thumbnail** (d2ByJWrsoec, 2026-10-02): a green streak from a cream, red-strapped bear [Observed]; a Viperifle shot by [Inference].
- **Official short qp5cFGLojyw** (2026-09-17):
  - The title is "Never let them know your next move! #battlebears #wishlist" [Canon, oEmbed/RSS]. The on-screen caption in its thumbnails reads "Never let bro know your next move" [Observed].
  - The thumbnails show a wide mint-green tapered streak (hq2) and a red ring crosshair (hq1) [Observed]. Shooter and weapon are unidentified [inconclusive].
- **Other channel uploads (RSS, Aug 20–Oct 16, 2026):** the thumbnails I opened show no identifiable Sniper weapon [Observed].
- **Not shown:** the other 15 Sniper weapons appear in no official 2026 material I could open, and the Dead Eye and Fairy's Dust appear only in the re-used 2013 footage. In official material, their 2026 presence, stats and prices are [Unverified]. Fan 2026 captures add a few: Fairy's Dust, the Crossbow and the Battering Ram in a Playtest #3 loadout (2026.md), and the Art of War and the Rake in the Aug 2026 beta (addendum).
- **JustNubz showcase:** "BBG All Classes Showcase [Skins, Taunts, Weapons, and Melee] (from Closed Playtest #4)" [title via oEmbed]. Its auto-thumbnails show only Gear Up screens of other classes [Observed]. The Sniper chapter at 22:30 needs a human viewer.
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/steam_sheet.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/qp_stack.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/yt/qp5cFGLojyw_maxresdefault.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/qp1_zoom.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/qp2_zoom.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/rss1.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/crops/rss2.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-verify/yt/d2ByJWrsoec_maxresdefault.jpg
- **Confidence:** observed (what each image shows). The three weapons in the Steam trailer and screenshots are 2013 footage [Inference, strong]; of the three, official 2026 material shows only the Viperifle, in the teaser's green shot, by [Inference].

---

## Verifier's changes to the draft (all checked against re-fetched pages or images opened today)

1. **Skin names resolved.** The cucumber/mint-mask skin is **Call Off Duty**; the blue colouring is the Team Blue variant [Fan-wiki description matches Observed]. The red jacket with white sleeves is the **Assassino** skin [Inference, strong; wiki description plus its own preview images]. The draft had both as [Unverified].
2. **Misquoted video title.** The draft gave qp5cFGLojyw as "Never let bro know your next move". The official title is "Never let them know your next move! #battlebears #wishlist"; the "bro" line is the on-screen caption.
3. **Misquoted Status Effects text.** The page says "an mild echo" [sic], not "a mild echo".
4. **Eagle Standard.** The draft concluded "The modifier is therefore a penalty, not a boost". The penalty is documented only for pre-2.6 (2012 Gear Up and trivia). The post-2.6 direction is ambiguous (page body says a boost; the 2.6 line's sign is unclear) and is now [Unverified].
5. **Blow Dart.** The draft repeated "the only Sniper weapon boosted by Explosions+" without comment. The Fidget Boomer and I Lava U pages both list Explosions+ effects, so the trivia is contradicted.
6. **Battering Ram barks.** These are the Sniper's class-wide melee lines from the Sniper (BBG) page, not from the Battering Ram page. The second melee-kill line was added.
7. **Capital Pains.** The in-game June 2012 model already has a magic-8-ball scope; the draft said only the concept did. File:Capitalpains.jpg (Nov 2013 upload) adds a second green-barrel image.
8. **Mamba's Boy.** The 2012 and 2013 Gear Ups show "SPEED -10%" in red, confirming the 2.6 note. The overhaul thumbnail streak is thin, not "thick". The wiki's "fastest green-locking" claim conflicts with its own infobox.
9. **Steam screenshot_04.** The figure is about 100 px tall, so the Viperifle identification is downgraded to [Inference].
10. **Overhaul HUD ammo counts.** The draft said they "match no wiki stat set". Two of them can be read against the wiki: 0/2 equals the Capital Pains infobox ammo of 2, and 4/4 equals Viperifle 3 + Ammo+1 [Inference]. 8/10 and 3/3 match nothing.
11. **Dead Eye shot.** I confirmed from a full-resolution crop at 12.6 s that the white streak starts at Astoria's hands. It is jagged and lightning-like. The blue orb in the frame is unrelated.
12. **New images used.**
    - File:Stealth.jpg (official Dead Eye + Solid Fisher banner).
    - File:New_Year's_bundle.PNG (Daydreamer, Golden Dragon and Blow Dart on official art).
    - File:Astoria_banner_02.png (Weapon Starter Pack banner).
    - File:Splinter-sales.png.
    - File:Viperrifle.PNG, File:Mambas-Boy.PNG, File:Mambas_Bly_by_applergamers.jpg, File:Yet_another_dead_eye_view!.jpg, File:Dead_Eye_Concept.jpg and File:Capitalpains.jpg.
    - The wiki skin gallery (which rifle each skin holds).
13. **Archive status.** The archive.org availability API returned no snapshots today for the 2.6 change log or blog item 138, so the earlier notes' snapshot URLs are [Unverified].
14. **Kept from the draft after checking:**
    - all official quotes;
    - every 2.6, 1.4.2 and 2.20 line;
    - all release dates and bundle dates;
    - the Eagle Standard's white tail;
    - the separate fire projectile in the Dead Eye scene;
    - the Fidget Boomer speed conflict;
    - the Rake's Solid Fisher skin;
    - the Detonate-daydreamer caveat;
    - the Fairy's Dust colour difference (violet in fan screenshots, magenta in the Steam trailer; both are now read as 2013, so it is not an era shift);
    - the traditional characters on the Art of War.

---

## Corrections for the character file (/home/user/thallo-site/bbg-news-repo/characters/astoria.md)

Flagged only; nothing was edited.

1. **Gear line**
   - Current: "- **Gear:** grey-blue backpack on dark straps, black woven utility belt [Observed]."
   - Correction: "- **Gear:** in-game BBG default (team colour; red team shown): red backpack and shoulder straps, red belt with a dark-maroon quilted band and red side pouch, red gloves, red-and-white striped boots [Observed]. The grey-blue backpack and black woven belt come from the 2D character card only [Observed]."
   - Evidence: every in-game Gear Up opened (Viperrifle.jpg, Crossbow.jpg, Mamba.jpg, FairysDust.jpg, Astoria-Default.png); the wiki's Astoria (Skin) text "an ammo belt, a backpack and gloves with the colour of the team colour"; the card File:AstoriaDescription.jpg shows the grey-blue backpack.
2. **Prompt pack**
   - Current: "Grey-blue backpack (#6F8296) on dark straps, black woven ammo belt, red gloves. Long scoped sniper rifle held upright, other hand on hip."
   - Correction: "Red team-colour backpack and straps, red belt with a dark-maroon quilted band and red side pouch, red gloves, red-and-white striped boots. Holding the Viperifle two-handed: a black sniper rifle with a dark-green liquid capsule on top, green vents by the grip and an angular snake-head muzzle with a glowing lime eye."
   - Evidence: as item 1, plus Steam screenshot_01 and the wiki's Viperifle design text.
3. **Placeholder colours**
   - Current: "eyes #2E9C8A, backpack #6F8296, belt/straps #1F1F24, gloves #CC1818 (red team)"
   - Correction: sampled in-game values: eyes ≈#5391A1 (blue-teal); backpack, straps, pouch and gloves ≈#9D0000–#BB2427; belt band ≈#462122–#512A27; fur highlight ≈#E8D7A4, shade ≈#B3A87C.
   - Evidence: PIL samples from File:Viperrifle.jpg, File:Viperifle.jpg, File:Mamba.jpg and File:Crossbow.jpg (eye mean of four images).
4. **The teal-masked sniper**
   - Current: "a teal-masked sniper in a 2026 Steam screenshot, which is Astoria only by [Inference]"
   - Correction: "the Call Off Duty skin (mint mud-mask with a cucumber slice, robe, polka-dot shorts, ice-cream tub on the belt; blue on Team Blue) holding the Viperifle in Steam screenshot_01 and the Steam trailer at ≈30.0–30.8 s (2013 footage [Inference, strong])".
   - Evidence: the wiki's Call Off Duty description ("Pink is changed to light blue if the player is on Team Blue"), File:Call_off_duty.png and the official Mean Mamba Bundle banner. The same Space Oddity moment is in SkyVu's May 30, 2013 trailer rfAyqVJrli4 (storyboard match; see the note at the top).
5. **The BBG splash card**
   - Current: "the BBG splash card (blue eyes, red-and-white top, arms crossed; possibly a skin [Inference]; [Steam trailer][steam])"
   - Correction: "the Steam trailer's ASTORIA / SNIPER title card (2013 footage [Inference, strong]): the Assassino skin (team-colour jacket, white sleeves, dark trousers) holding the Dead Eye bone rifle upright [Observed; skin ID Inference]".
   - Evidence: trailer ≈16.4–17.8 s (sheetA4.jpg); the same card at 21 s in the storyboard of SkyVu's May 30, 2013 trailer rfAyqVJrli4; the wiki's Assassino text "team colored jacket with a white shirt underneath, black pants"; File:Assasino1.PNG and File:DeadEye.jpg.
6. **Battering Ram**
   - Current: "the Battering Ram ram-skull club"
   - Correction: "the Battering Ram, a grey stone club whose head is a curled ram horn, lashed with dark straps". Keep the game-text quote ("Ram Skull" technology); the model shows a horn, not a skull.
   - Evidence: File:Battering_ram.png and File:Battering_Ram_Concept.jpg.
7. **The hawk**
   - Current: "Draw the hawk as an angry-bird gag, with no cultural styling [BBG News invention]."
   - Correction: keep the gag but add the documented design and hit: a brown hawk with a cream chest, yellow hooked beak and talons and blue-tipped feathers, trussed in tan rope. Thrown, it tumbles; on contact the ropes pop and a flurry of wings and feathers smothers the target's face, a partial blind with no damage [Observed + Fan-wiki].
   - Evidence: File:Tomahawk.jpg, File:Tomahawk_concept.jpg, File:Download_(16).jpg and the Tomahawk page text.
8. **Weapons/props omits the arsenal the Steam trailer shows**
   - Current: "- **Weapons/props:** a sniper rifle [Canon] (BBG default: the Viperifle [Fan-wiki] …); the Tomahawk, … the Battering Ram ram-skull club, …"
   - Correction: add the Dead Eye (bone rifle with a biting skull scope; white jagged streak; red horned-skull smoke on hit) and Fairy's Dust (a pink sparkle sack that bursts into a huge magenta-violet faceted cloud; her vanish beat) [Observed, Steam trailer] (2013 footage [Inference, strong]). In 2026, only Fairy's Dust is seen, as loadout text in a fan Playtest #3 thumbnail [Observed, low-res]; the Dead Eye's 2026 status is [Unverified].
   - Evidence: trailer ≈12.2–17.8 s (sheetA1–A4.jpg); qt43iTdANbM hq3 (2026 loadout).
9. **BBH Explosive Retreat used in BBG-era beats**
   - Current: "3. Her Explosive Retreat overshoots into a Huggable pile. She freezes, then tiptoes backward." and "Her Explosive Retreat lands her right back beside him."
   - Correction: Explosive Retreat is a BB Heroes Ultimate (BBH table and battlebears.com), not a BBG item. In BBG-default shorts, swap in Fairy's Dust (the trailer's own vanish-and-reappear beat) or the Tomahawk, or label the beat BBH-era. Tag the Fighting line's quote as BBH as well.
   - Evidence: battlebears.com/pages/characters [Canon] and the wiki's Battle Bears Heroes table; Explosive Retreat is not among the 18 BBG Sniper items.
10. **Eyes and negative prompt**
    - Current: "- **Eyes:** teal-green, heavy-lidded and unimpressed [Observed]." and a negative prompt containing "blue eyes".
    - Correction: in-game 3D models (2012–2015 Gear Ups and the Steam trailer, 2013 footage [Inference, strong]) show blue/blue-teal eyes (≈#5391A1); the 2D card shows teal-green. Remove "blue eyes" from the negative prompt, and use blue-teal for 3D shorts.
    - Evidence: the Gear Ups listed in item 3 and trailer frames ≈16.4–17.8 s.
11. **Open question on her outfit**
    - Current: "Are her eyes green or blue? Is the red-and-white outfit her default or a skin?"
    - Correction: answered. In-game eyes are blue/blue-teal. The red-and-white jacket is a skin (Assassino) [Inference, strong]; the default skin is plain cream with team-colour backpack, belt and gloves (File:Astoria-Default.png).
    - Evidence: as items 5 and 10.
12. **Open question on the 2026 look**
    - Current: "What default skin, taunts and audio does the 2026 build use? The [Astoria Overhaul][overhaul] and [2026 showcase][showcase] videos haven't been viewed."
    - Correction: still open for the 2026 build. The Steam trailer and screenshots cannot answer it: they show the Assassino jacket with the Dead Eye and Fairy's Dust, Call Off Duty with the Viperifle (trailer, screenshot_01) and a small default red-gear Astoria (screenshot_04), but all of it is 2013 footage [Inference, strong]. The 2026 fan frames in the addendum show two looks. Takishi's Aug 2 beta (B-8uQcs1DFA, build 3.0.0) shows plain cream fur and a team-colour backpack (blue in maxres2, red in maxres1), with no jacket visible [Observed], which fits the default skin [Inference]. The Oct 15 playtest (HKbwq7PolNc maxres2, build 3.0.7) shows the Assassino-style red jacket [Observed; Astoria by Inference]. Whether the jacket is the 3.0.7 default or that player's skin is open. Taunts and audio remain open.
    - Evidence: Steam screenshots and trailer frames listed above; the 2013 storyboard match (note at the top); the addendum's thumbs/aow_B-8uQcs1DFA_maxres1.jpg and _maxres2.jpg, and thumbs/gap1_HKbwq7PolNc_maxres2.jpg.

---

## Open questions

- Which of the 18 Sniper weapons are in the 2026 build, and with what stats and prices? The Viperifle, Dead Eye and Fairy's Dust appear in the Steam trailer and screenshots, but that is 2013 footage [Inference, strong]. Among real 2026 sources, SkyVu's teaser thumbnail probably shows a Viperifle shot [Inference], and fan captures show Fairy's Dust, the Crossbow and the Battering Ram (Playtest #3 loadout, 2026.md) and the Art of War and the Rake (Aug 2026 beta, addendum). The JustNubz Closed Playtest #4 showcase (Sniper chapter at 22:30) needs a human viewer.
- What is the date of "BATTLE BEARS GOLD Developer Update - Astoria Overhaul" (wUWf9O-YX4A), and what did it change? Its thumbnail ammo counts (8/10, 4/4, 3/3, 0/2) only partly match wiki stats.
- None of these has been observed:
  - the Mamba's Boy projectile (beyond one pale streak);
  - the Blow Dart dart and its "blue tinge" explosion;
  - the Fidget Boomer explosion;
  - the I Lava U mines and blasts;
  - the Art of War paint burst;
  - the Rake spring-up;
  - the charged Crossbow burst;
  - any of the four melee hit effects.
- Is the Dead Eye bullet white (Steam trailer, 2013 footage [Inference, strong]) or red (wiki), did it change between eras, and what colour is it in the 2026 build?
- When was red Capital Pains removed, and is the 2015 silver barrel the "white" state? Does the NASDAQ mechanic exist in 2026?
- In which direction does the Eagle Standard's special-speed modifier work after 2.6, and in 2026?
- Does the "Detonate daydreamer" magenta arc ring really show the Daydreamer trigger?
- In the trailer's Dead Eye scene, the victim holds a black rifle with red-orange lava-crack texture. Is that an Astoria weapon (I Lava U-like) or another class's gun? It is unidentified.
- SkyVu's own 2.6 change log (battlebears.com/battle-bears-gold-2-6-change-log/), the Apr 13 and Apr 27, 2012 blog posts and blog item 138 remain unreached. Today's Wayback availability API returned no snapshots, so every patch-note line stays a [Fan-wiki] transcription.
