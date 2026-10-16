# Astoria (Sniper): weapons dossier

**Scope.** Astoria is Battle Bears Gold's Sniper class. "-SNIPER: Astoria" is listed on the 2026 Steam page [Canon]. The class was released in BBR v1.1 on Nov 23, 2011 ("Added Game Center, new sniper class, new weapons") [Fan-wiki transcription]. It has 90 HP [Fan-wiki]. The fan wiki's Sniper (BBG) page and Category:BBG Weapons list 18 weapons, and they match exactly: 8 primaries, 6 secondaries and 4 melees [Fan-wiki]. This dossier also covers 3 unreleased concepts and her BBO/BBH equivalents. Each section gives its era: BBR (2011–13), BBG (2013–21), BBG 2026 re-release, or BBH (2023/24).

**How I worked.**
- I re-fetched all 18 weapon pages, plus Sniper (BBG), Status Effects, Updates, Bundle Deals, Solid Fisher, Pandini, the BBG 2.6 log page and the BBR 1.3, 1.3.1, 1.4.2 and 1.4.3 pages. All came through the MediaWiki API today, saved under /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/pages/.
- I opened every image cited below with the Read tool. Hex values are approximate, sampled with PIL (`python -I`) from those images.
- I extracted my own trailer frames at 10 fps:
  - `a_NNN.jpg` covers 11.8–18.1 s, where t = 11.8 + (N−1)×0.1 s.
  - `b_NNN.jpg` covers 29.4–30.9 s, where t = 29.4 + (N−1)×0.1 s.
  - Both sets are in /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/tr/. Labelled contact sheets and zoom crops are in /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/.

**Reachable sources.**
- Fan wiki API and static images.
- Steam appdetails: 1 trailer, 5 screenshots and the store text.
- battlebears.com/pages/characters (live).
- YouTube oEmbed titles, plus the BATTLE BEARS channel RSS feed (15 latest videos, with dates and descriptions).
- i.ytimg.com thumbnails.

**Not reachable.**
- web.archive.org: curl returned 000 and WebFetch was refused. This blocks SkyVu's own 2.6 change log and the 2012 squarespace blog posts.
- archive.ph returned HTTP 429.
- YouTube video pages are empty or login-walled. I watched no video. Video evidence below comes only from the official Steam trailer file and from thumbnails.

**Size convention.** Sizes are in Astoria head-heights. Her head is 1.0× Oliver's on the BBG News scale chart. They were measured by eye from Gear Up frames and are foreshortened [Inference].

**Default look of the wielder.** These notes matter for every weapon.
- In every in-game Gear Up image I opened, the default Astoria has cream fur and blue eyes (≈#468296). She wears team-coloured gear [Observed]:
  - red backpack and shoulder straps (≈#900C0A–#BE1E1E);
  - red belt with a dark-maroon quilted band (≈#461E1E) and a red side pouch;
  - red gloves;
  - red-and-white striped boots.
- The wiki says the default skin has "an ammo belt, a backpack and gloves with the colour of the team colour" [Fan-wiki].
- A recurring red-jacket outfit appears in several places [Observed]: the official 2.2 promo, the 2026 trailer title card and the Nov 2012 loadout. It has white sleeves, a round orange belt emblem and dark trousers. Its skin name is [Unverified].

---

## How Astoria's lock-on rifles work (Viperifle, Capital Pains, Mamba's Boy, Dead Eye)

**Mechanic.** Hold the reticle on a target and it locks in three stages [Fan-wiki]:
- **Semi-lock:** shots spread, even though the stat is 0.0 dispersion.
- **Green lock:** "100% accuracy" but base damage only.
- **White lock:** "guaranteed to kill the opponent, regardless of his/her remaining health." On the Dead Eye page, the white-lock scope "shows a red dot with white lines" [Fan-wiki].

Firing without a lock is a "no-scope".

**Target warning (status "Scoped").** "a red crosshair will appear over the player's head, indicating a headshot is in the process of being targeted. This does not affect the player in any way and serves only as a warning." Items capable: Viperifle, Capital Pains, Mamba's Boy, Dead Eye [Fan-wiki, Status Effects].

**Headshot kill.** The kill feed shows "HEAD SHOT" with a red crosshair-in-circle icon over the victim's portrait, plus "+100". Source: the official "BATTLE BEARS GOLD Developer Update - Astoria Overhaul" thumbnail (BATTLE BEARS channel, title via oEmbed [Canon]). I saw this in /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/yt/wUWf9O-YX4A_maxresdefault.jpg; which weapon made the kill is unknown [Observed]. A headshot "instantly deducts all the target's remaining health" [Fan-wiki].

**Depiction rule for all rifles.** Show a small red crosshair over the target's head while she holds the lock; that is the documented warning. Show the scope reticle turning green, then white, before a one-shot kill [Fan-wiki]. For the 13+ rating, the "kill" is the target popping into sparks (bears) or rainbow confetti (Huggables) per the BBG News house rules, not blood [BBG News invention].

---

## Viperifle (primary · default · BBR v1.1, Nov 23 2011 → BBG 2013–21 → in the 2026 build per official images)

**Official text:** "Keep targets centered in the screen to lock onto them. When your crosshairs turn green you are 100% accurate. If you can hold the lock a bit longer until they turn white you will get a head shot." ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Viperifle_(BBG)).

**Status and history**
- It was the only Sniper primary until BBR v1.3 (May 3, 2012) [Fan-wiki].
- BBG 2.6 (Dec 20, 2013): "Fire Rate decreased from 2.5 to 1.5", "Reload speed decreased from 5 to 4" [Fan-wiki transcription of the 2.6 log].
- Infobox: 45 damage, 3 ammo, 1.0 s rate of fire, 3.5 s reload, green lock 3 s, white lock 6 s [Fan-wiki].
- The 2026 stats are [Unverified].

**Look**
- A black/charcoal rifle (≈#0C0C0C–#242424) [Observed]. A dark-green liquid capsule sits on top (≈#325A0A, mean #3B6616 in the 2013 Gear Up), with green fins and vents beside the grip.
- A long thin barrel ends in an angular, open-jawed snake-head muzzle with a glowing lime eye (≈#82FA1E in the 2026 Steam screenshot) [Observed].
- The wiki agrees: "dark and green theme … liquids appears stored in containers, one on top of the scope itself, and two of them next to the trigger handle. The barrel end is shaped like a snake's mouth and is complemented with two green eyes" [Fan-wiki].
- It is held two-handed at chest height. It measures about 2.3 head-heights, roughly two-thirds of her standing height [Inference, from the BBR side view].
- **2026:** the same model appears in two places [Observed]:
  - Steam screenshot_01 and trailer ≈30.0–30.9 s, held by Astoria in a mint-green cucumber spa face mask with a blue top and blue polka-dot shorts.
  - Steam screenshot_04, held by default red-team Astoria.

**Firing.** One shot per pull after a lock [Fan-wiki]. No muzzle flash has been documented [Unverified]. The trailer clip ≈30.0–30.9 s shows her holding it, but no shot from her rifle is visible [Observed]. Yellow star sparks at another player's feet there are of unclear origin.

**Projectile**
- Wiki: "it releases a single, green, stream-like bullet that erupts into a splash of what appears to be venom. Said venom is merely cosmetic" [Fan-wiki].
- NEW [Observed]: the official 2026 teaser thumbnail matches this. The video is "TEASER TRAILER - Battle Bears Gold Returns November 4th 2026" (BATTLE BEARS channel, published Oct 2, 2026 per the channel RSS [Canon: title/date]). Its "GAMEPLAY" panel shows a cream bear with a red strap, seen from behind. A bright green, tapered streak (≈#2AEB74) runs up and away from her and ends in a small yellow-green splash at a distant figure.
- That the shooter is Astoria with the Viperifle is [Inference] (cream fur and red strap, plus the wiki text).
- Older evidence: the "Astoria Overhaul" thumbnail hq3 shows a Viperifle-like HUD icon, ammo 4/4, on a lava map. No shot is visible [Observed].

**Impact / end result.** A small green "venom" splash, cosmetic only [Fan-wiki]. In the 2026 teaser it reads as a yellow-green burst at the target [Observed, thumbnail]. A white-lock hit is a one-shot "HEAD SHOT" kill [Fan-wiki]. A green-lock hit does 45 base damage [Fan-wiki].

**Images viewed**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/conv2/Viperrifle.jpg.png (2013 Gear Up)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/conv2/Viperifle.png.png (BBR 2012 Gear Up, "VIPERIFLE EQUIPPED")
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/conv2/Viperifle.jpg.png (2015 Gear Up)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/crops/s01_astoria.png (Steam screenshot_01 crop)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/s04_ast.png and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/crops/s04_center.png (Steam screenshot_04)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/steam.jpg (all 5 Steam screenshots)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/b1.jpg and vip_grid.jpg (trailer 29.4–30.9 s, from tr/b_001–b_016)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/crops/viper_fire_grid.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/teaser_ast.png (from yt/d2ByJWrsoec_hq1.jpg)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/ytsheet_1.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/ov.jpg and ov_icons.jpg (overhaul thumbnails)

**Depiction for shorts.** Show the black rifle with the green capsule and snake-head muzzle; its lime eye glows while she locks. The reticle goes green, then white, and a small red crosshair hovers over the target's head. The shot is a thin bright-green streak ending in a small yellow-green splash; the target pops into sparks or confetti. Any muzzle flash or snake "hiss" is [BBG News invention].

**Confidence:** observed (look); partial (projectile seen only in one 2026 thumbnail and in wiki text).

---

## Capital Pains (primary · BBR v1.3, May 3 2012 → BBG; red mode later removed; 2026 status unverified)

**Official text:** "If the NASDAQ stock index is down the day before, it shoots much faster, has more ammo, but does less damage and locks slower." ~ Official Battle Bears Gold description [Game text via wiki]. The wiki adds: "This description is now outdated due to a stat change" (https://battlebears.fandom.com/wiki/Capital_Pains).

**Status and history**
- **Release:** BBR v1.3, with the Daydreamer [Fan-wiki].
- **Name:** originally the "Stock Rifle" (concept) [Fan-wiki].
- **Price:** 200,000 Joules in a 2013 Gear Up [Observed]. BBG 2.20 (May 29, 2015) "reduced from 200,000 joules to 150,000 joules" [Fan-wiki]. The current infobox says 150,000 J at level 15 [Fan-wiki].
- **BBG 2.6 changes** [Fan-wiki transcription]:
  - fire rate 2.5→2
  - reload 5→4
  - lock radius 375→350
  - dispersion .02→.00
  - "Market Down lock time decreased from 6 to 1.5"
  - "Market Down warning time decreased from 3 to 1"
- **Rework:** the wiki says "Red Capital Pains is currently removed, and all stats listed for it currently do not exist", with no date [Fan-wiki]. Red mode still existed in a fan video uploaded by ApplerGamers ("Red Capital Pains demonstration", YouTube QQrU7iCrGoo [title/channel via oEmbed]). The wiki file is dated Jan 4, 2014 [Fan-wiki].

**Look** [Observed]
- **Stock and grip:** a gold € sign as the stock and a gold $ sign as the grip and trigger guard (≈#DDAF41, highlights #FAE66E).
- **Body:** red (≈#9E1A18).
- **Scope:** a ball-shaped scope with a blue lens (≈#454C9F).
- **Magazine:** a green banknote wad.
- **Barrel:** a zig-zag shaped like a stock-market chart line. Its colour changes between images:
  - red (≈#92110F) in the June 2012 Gear Up;
  - green (mean ≈#138F09) in the Nov 2012 loadout;
  - silver-grey (≈#B4B4B4) in the 2015 Gear Up. The wiki captions that image "in green", which conflicts. It may be the "white" state ("It is possible for the Capital Pains to be white") [Inference].
- **Concept "Stock Rifle":** a black-to-red chart-line barrel ending in a green arrow, a magic-8-ball scope, a banknote magazine, gold €/$, and a "PLURIBUS … C" coin.
- **Menu icon:** a green zig-zag with $€.
- **Size:** about 2 head-heights [Inference].

**Firing.** Standard lock-on. The game checks the NASDAQ once a day at 00:00 GMT; a zero or positive change makes the rifle green and a negative one makes it red, for 24 h [Fan-wiki]. In the fan video thumbnails the ammo counter reads x/5 in red mode [Observed]. The POV player wears the Solid Fisher skin.

**Projectile.** "if it is negative, the bullets are red, if it is positive, the bullets are green" [Fan-wiki]. The red-mode fan thumbnails show thin red streak lines from the player toward a yellow target under a black lock reticle [Observed, low-res fan thumbnails; consistent with the wiki, not conclusive].

**Impact / end result.** Not documented [Unverified]. A white-lock hit is a one-shot headshot [Fan-wiki].

**Images viewed**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/conv2/Capital_Pains.jpg.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/conv2/Capital_Pains_Rifle.png.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/conv2/Gnifle-sniper-setup.png.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/conv2/Stock_Rifle.png.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/deadeye_gear.jpg (Another_dead_eye_view: "CAPITAL PAINS BUY NOW 200,000")
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/redcp.jpg (QQrU7iCrGoo hq1/hq2/hq3/maxres)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/fairy2.jpg (Aaaaa.jpg HUD icon)

**Depiction for shorts.** Show the €/$ "money gun" with the zig-zag chart barrel. Green day: a green barrel and green streak. Red day: a red barrel and red streak, as a ticker gag. The hit splash is [BBG News invention]; use a small burst of coins or confetti matching the bullet colour.

**Confidence:** observed (look); partial (projectile colour from wiki plus fan thumbnails); unknown (impact, 2026 status).

---

## Mamba's Boy (primary · BBR v1.3.1, Jun 28 2012 → BBG; nerfed 2013 and 2015; 2026 status unverified)

**Official text:** "This gun will send you crying back to your mamba. Trade aim and damage for a faster rate of fire." ~ Official Battle Bears Gold description [Game text via wiki]. The wiki adds "(This description is now inaccurate due to a stat rebalance)" (https://battlebears.fandom.com/wiki/Mamba%27s_Boy).

**Status and history**
- **Release:** "week three of the four-week weapons release" [Fan-wiki].
- **BBR 1.4.2** (Feb 28, 2013): clip 5→4, cooldown .35→.4, dispersion .01→.02 [Fan-wiki].
- **BBG 2.6** [Fan-wiki transcription]:
  - damage 23→22
  - fire rate .4→.35
  - clip 4→3
  - reload 3→4
  - "Speed decrease of -10% removed"
  - Ammo+ removed
- **BBG 2.20** (May 29, 2015): "Dead Eye and Mamba's Boy are nerfed" [Fan-wiki].
- **Bundles** [Fan-wiki Bundle Deals]:
  - Mean Mamba Bundle (Sniper + Mamba's Boy + the Demo skin Pandini, Mar 8–10, 2013)
  - Yo Mamba Bundle (Urine Trouble + Mother of Nature + Mamba's Boy, May 10–12, 2013)
  - Astoria Weapon Starter Pack (Mamba's Boy + Eagle Standard, Sep 22–Oct 7, 2013)
  - Splinter Sale (Mamba's Boy, Daydreamer, Solid Fisher, Flawless Disguise, Sep 14–16, 2012)

**Look** [Observed]
- A bright lime/yellow-green rifle (highlights ≈#D2E60A, mid ≈#46BE0A, mean ≈#71AD10). Its body is a snake with a dark-green hexagonal scale pattern (≈#1E5A0A).
- A lime scope sits on top.
- The muzzle is a snake head with a yellow eye and an open pink/orange mouth.
- It appears on the BBR 1.3.1 promo art as a green snake rifle with its jaws open.
- **Size:** about 2 head-heights [Inference].

**Firing.** Rapid lock-on sniper: the fastest green lock, a small lock radius and low damage per shot. A white lock still kills outright [Fan-wiki].

**Projectile.** No text description exists [Unverified]. The official "Astoria Overhaul" thumbnail hq1 has a lime-green Mamba-like HUD icon and ammo 8/10. A thick, pale-white tapered streak runs from Astoria's lime rifle to a target under a lock reticle [Observed]. That this is Mamba's Boy is [Inference]. The video's date and the meaning of 8/10 are [Unverified]; 8/10 matches no wiki stat set.

**Impact / end result.** Undocumented [Unverified]. A white-lock hit is a headshot kill [Fan-wiki].

**Images viewed**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/conv2/Mamba.jpg.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/conv2/Mamba's_Boy.jpg.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/conv2/BBRWEAPONS.png.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/bundles.jpg (Meanmambabundle, Yo_Mamba_Bundle, AstoriaStarter)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/deadeye_gear.jpg (Sniper_setup.jpg loadout, Apr 2013)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/ov.jpg, ov_icons.jpg and ov_muzzles.jpg

**Depiction for shorts.** Show a lime snake-skin rifle whose muzzle is an open-mouthed snake, firing quick pale streaks in rapid succession. Any snake animation, such as the jaws snapping on each shot, is [BBG News invention].

**Confidence:** observed (look); partial (projectile only in one unidentified-era thumbnail).

---

## Dead Eye (primary · announced Apr 2012, released BBR 1.4.3/1.4.3.1, Apr 15/23 2013 → BBG; nerfed 2015; in the 2026 trailer)

**Official text:** "Got a problem? The Deadeye is your solution. She may not have the biggest clip but she definitely has the biggest kick. If you understand the value of power, this is the rifle for you." ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Dead_Eye). BBR 1.4.3 release note: "-The Dead Eye: Astoria's strong single shot sniper rifle." [Fan-wiki transcription of SkyVu notes, Updates page].

**Status and history**
- **First shown:** on the old blog, Apr 13, 2012 [Fan-wiki; archive unreachable, Unverified].
- **Price:** the infobox says 60 Gas and the body says 120 Gas [Fan-wiki]. A 2013 Gear Up shows "DEAD EYE BUY NOW 120" Gas and "HEALTH -5%" [Observed].
- **BBG 2.6** [Fan-wiki transcription]:
  - reload 3.75→3
  - "Health Modifier increased from -5% to 0"
  - lock radius 200→350
  - warning time 3→2
- **BBG 2.20:** nerfed [Fan-wiki].
- **Damage:** the infobox says 75; the body says "(85 damage)" and "9 seconds … to reach green-locking", which conflicts with the infobox's 2 s [Fan-wiki].
- **2026:** the official trailer's ASTORIA / SNIPER title card shows her holding it [Observed]. It is probably in the 2026 build [Inference].

**Look** [Observed]
- A rifle built from cream/ivory bones (≈#FCE4CC, shading to #E4B484 and #9C6C54), lashed with red-brown cords (≈#9C543C, dark #3C0C0C).
- The stock is a flat shoulder-blade bone, the receiver a ribcage/vertebra section, and the magazine a bone.
- The scope is a beaked, toothed animal skull. The wiki says it is "moving as if it was biting something" and is "presumeably from a bird due to the large beak, though the teeth could indicate otherwise" [Fan-wiki].
- A very long thin bone barrel ends in a square muzzle with a dark bore.
- The Apr 2012 concept is whiter bone with dark wraps.
- **Size:** the longest of her rifles, about 3 head-heights [Inference, 2013 Gear Up]. On the 2026 title card she holds it upright across her body and the barrel leaves the top of the frame.

**Firing (2026 official trailer, ≈12.2–13.7 s)** [Observed]
- Astoria stands at the top of temple stairs on a lava-sky Aztec-style map, in the red jacket with white sleeves. She aims a pale weapon downhill.
- From ≈12.4 to 12.8 s a thin, twisting white streak with pale blue-grey edges runs from her rifle to the head of the target at the foot of the stairs. The target is a white-faced bear in a black suit.
- That this shot is the Dead Eye is [Inference]: the weapon looks pale, the skull effect follows, and the title card comes right after.

**Projectile.** The wiki says "a single, red, stream-like bullet" [Fan-wiki]. The trailer shows WHITE [Observed]. The colour therefore conflicts; follow the 2026 footage for 2026-era shorts.

**Impact / end result** [Observed, trailer]
- At the moment of impact (≈12.4 s) translucent red smoke (≈#F81828) blooms at the target.
- From ≈13.0 to 13.7 s it rises as large, glowing, translucent red buffalo/bull skulls with big curved horns.
- The target collapses and lies dead by ≈13.4 s.
- This matches the wiki: "erupts into a flurry of glowing, transparent buffalo skulls. These are merely cosmetic" [Fan-wiki].
- CAUTION: the orange flames that engulf the target at ≈12.4–13.2 s come from a separate fiery projectile entering from off-screen right at ≈12.3 s. They are not part of the Dead Eye effect [Observed; attribution is Inference].

**Images viewed**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/conv2/Dead_Eye.jpg.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/conv2/Dead_eye_blog.jpg.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/conv2/TheDeadEye-trans.png.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/conv2/Deadeye-concept-trans.png.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/concepts.jpg (143releasepic.png)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/deadeye_gear.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/a1.jpg, a2.jpg, a3.jpg and a4.jpg (trailer 11.8–18.1 s, from tr/a_001–a_064)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/streak_grid.jpg, streak_zoom.png, ast_grid.jpg and right_grid.jpg

**Depiction for shorts.** A long bone rifle with a biting skull scope, held upright for her hero pose. When fired, a thin white twisting streak hits the target. Ghostly red buffalo-skull smoke rises and fades, and the target flops over in a puff of sparks. No fire unless another bear is shooting, and no blood. Animating the skull scope's bite is allowed (wiki-documented).

**Confidence:** observed.

---

## Crossbow / "Unicorn Crossbow 2.0" (primary · BBG 2.2, Aug 21 2013; reworked in 2.6; 2026 status unverified)

**Official text:** "Leave it to Astoria to make a rapid fire weapon that shoots unicorn horns. Even worse is that she can charge up the weapon and release a stronger attack! What's next jackelope weapons?" ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Crossbow_(BBG)).

**Status and history**
- **Release:** SkyVu posted "BATTLE BEARS GOLD Update 2.2 Weapon Recap" [Canon: title/channel via oEmbed]. Its thumbnail shows "NEW WEAPONS!", with Astoria in the red jacket holding the crossbow [Observed].
- **BBG 2.6** [Fan-wiki transcription]: "Clip size reduced from 100 to 2", heat per shot 12→1, damage 20→50, charged damage 50→120.
- **Price:** 240,000→150,000 J in 2.20 [Fan-wiki].
- **Current infobox:** 15 ammo, 15 uncharged and 230 charged damage, so the numbers are inconsistent [Fan-wiki].
- **Name:** "2.0" because Oliver had a "Unicorn Crossbow" in Battle Bears: Zombies [Fan-wiki].

**Look** [Observed]
- A pearl-white/silver crossbow (≈#E4E4E4–#FCFCFC, shading #9C9C9C–#B4B4B4) with cream inset panels and diamond motifs.
- The front is a unicorn-head shape. A lavender crystal horn-bolt (≈#D3ABED) is loaded at the front, and the string is lavender.
- The concept sheet shows four finishes: silver with a violet-glow chamber, gold, gunmetal with a red-glow chamber, and copper with a cyan glow.
- **Size:** limb span about 2 head-heights [Inference].

**Firing.** Manual aim, with no lock and so no headshots. Uncharged shots are rapid. The charged shot zooms in more, and the "internal barrel with also rotate at a rapid rate and shine a bright purple aura"; it uses the whole magazine [Fan-wiki]. The official "Astoria Overhaul" thumbnail hq2 shows a white-pink muzzle flash and pink-violet streaks leaving a silver weapon, with a white crossbow HUD icon and ammo 3/3 [Observed]. A yellow six-segment wheel at the left of the screen may be a charge meter [Inference].

**Projectile.** "shining unicorn horns" [Fan-wiki]. In the overhaul thumbnail they read as pink-violet light streaks [Observed].

**Impact / end result.** A charged hit deals area damage "upon a hit on either an opponent or an object". The wiki files it under Explosives, and you can kill yourself with it [Fan-wiki]. The look of the burst is [Unverified].

**Images viewed**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/conv2/Crossbow.jpg.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/conv2/UnicornCrossbowconceptart.jpg.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/conv2/Crossbow_coming_to_BBG!!!.jpg.png (frame with the BBG logo and "CROSSBOW" on a blue vortex)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/recap22.jpg (BcEeAzXFChI thumbnails)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/ov.jpg and ov_muzzles.jpg

**Depiction for shorts.** A white unicorn-head crossbow spitting quick lavender horn-bolts. On charge, the inner barrel spins and glows purple, then releases one big horn that bursts. The burst style is [BBG News invention]; use a lavender sparkle pop.

**Confidence:** observed (look and muzzle); partial (projectile/impact).

---

## Blow Dart (primary · BBG 2.6, Dec 20 2013; 2026 status unverified)

**Official text:** "Just because it is the future does not mean there cannot be old school weaponry. Watch out for exploding darts!" ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Blow_Dart).

**Look** [Observed]. An orange-copper blowgun tube (≈#B04B1E) with glowing magenta/pink stripe panels (≈#D751C9 to #FA6EFA) and a purple section. It ends in an angular head with a pink-glowing slot at the muzzle. She holds it two-handed like a rifle. It is at least 1.1 head-heights long, heavily foreshortened [Inference].

**Firing.** Manual aim with no lock. 0.5 s rate of fire, 4 ammo, 4.5 s reload [Fan-wiki].

**Projectile.** "a small projectile" (a dart) at 1,000 u/s that sticks to "any solid surface (players included)" [Fan-wiki]. Its look was not observed [Unverified].

**Impact / end result.** It detonates 6 s after contact. "The explosion it creates is distinguishable because of its blue tinge and large Area of Effect" [Fan-wiki]. Explosive damage is 25–50, it can kill the user, and it is the only Sniper weapon boosted by Explosions+ [Fan-wiki]. The explosion was not observed [Unverified].

**Images viewed**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/dart_fidget.jpg (Blowdart.png and BlowDart.jpg)

**Depiction for shorts.** A puff from the copper tube sends a tiny pink-tipped dart that sticks to the target. A 6-second beat follows (comic timing), then a large blue-tinged blast. The dart's look and the countdown blink are [BBG News invention].

**Confidence:** observed (look); documented (impact).

---

## Art of War (primary · revealed Apr 27 2012, declared unused Aug 8 2013, released BBG 2.11, Aug 27 2014; 2026 status unverified)

**Official text:** "Paint the battlefield red, or orange, or yellow, or green, or blue, or violet. It doesn't really matter as long as its your enemies pallet." ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Art_of_War).

**Look** [Observed]
- **Barrel:** red (≈#B84133) with gold Chinese characters. They look like the traditional form 孫子兵法; the wiki types the simplified 孙子兵法 ("The Art of War").
- **Body:** a black and yellow receiver, a paintball hopper on top filled with multicolour balls, and a blue gem on the side.
- **Muzzle:** a paintbrush tip loaded with rainbow paint (red, orange, yellow, green, blue).
- **Concept line art:** labelled "The Art of War / Paintball Sniper Rifle", with a scope, a hopper and a small brush mounted under the barrel.
- No in-hand image was found, so its size relative to the bear is [Unverified].

**Firing.** No lock, so no headshots. 45 damage, 3 ammo [Fan-wiki].

**Projectile.** "a single stream-like bullet will be fired in the exact same direction of the crosshairs" [Fan-wiki].

**Impact / end result.** "erupting into a flurry of paint, however, it is merely cosmetic" [Fan-wiki]. Not observed [Unverified].

**Images viewed**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/aow.jpg (Images_(1).jpeg render, ArtofWar.png, ArtofWarconceptart.png)

**Depiction for shorts.** A brush-tipped paintball rifle firing a thin streak that splats into a multicolour paint burst. The rainbow splat colours follow the official text's list (red, orange, yellow, green, blue, violet); the exact splat shape is [BBG News invention].

**Confidence:** observed (look); documented (projectile/impact).

---

## Fidget Boomer (primary · BBG 2.27, May 29 2017; 2026 status unverified)

**Official text:** "Have toy tricks gone too far!? Explosions are safe right?" ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Fidget_Boomer).

**Look** [Observed]. A large dusty-pink/mauve chrome three-lobed fidget spinner (highlights ≈#BF8696, shadows ≈#79515D). She holds it raised in one hand at head height. In the Gear Up it looks about 2 head-heights across, but it is held toward the camera [Inference].

**Firing.** 0.3 s rate of fire, 4 ammo, 3 s reload [Fan-wiki]. The projectile speed conflicts: the infobox says 3000 u/s and the trivia says "the fastest projectile speed in the game", while the body says "the slow projectile speed" [Fan-wiki].

**Projectile.** Probably the spinner itself, thrown [Inference]. Not observed.

**Impact / end result.** "upon contact with a surface experiences a short delay before exploding (akin to the TNT Launcher)"; it "does not have a secondary effect". 40–70 explosive damage [Fan-wiki]. The explosion was not observed [Unverified].

**Images viewed**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/dart_fidget.jpg (FidgetBoomer.jpeg)

**Depiction for shorts.** She flicks the chrome-pink spinner. It whirs, lands, wobbles for a beat and explodes. The spin-whistle and the explosion colour are [BBG News invention].

**Confidence:** observed (look); documented (impact); partial overall.

---

## Tomahawk (secondary · default · BBR v1.1 2011 → BBG; 2026 status unverified)

**Official text:** "Unleash a terrified and angry hawk that temporarily blinds any player it hits! Great for running away from opponents that get too close." ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Tomahawk).

**Status.** It was the Sniper's only secondary before v1.3 [Fan-wiki]. BBG 2.6: duration 15→10, reload 2→1.5 [Fan-wiki transcription]. The infobox still says 15 s duration and 0.75 s reload, while the body says 10 s [Fan-wiki].

**Look** [Observed]
- A brown hawk with a cream chest (≈#FCE4B4), a yellow hooked beak and yellow talons, and blue-tipped feathers.
- It is trussed in coils of tan rope, including a loop around the beak.
- She holds it upright by its legs at shoulder height. It is about 1.7 head-heights tall [Inference].
- The concept art "tomahawk" shows the same bird in greyscale and in colour, with an orange eye.

**Firing.** Thrown: "the tied hawk will rotate forward with straight trajectory". It is hard to aim, has no AoE and does no damage. A bug can make it fly backwards [Fan-wiki].

**Projectile.** The rope-bound hawk tumbling end over end [Fan-wiki]. Not observed in flight.

**Impact / end result**
- Wiki: on contact it "will be let free of its retrains and violently thrash around their face, blinding them with a flurry of wings and feathers", a partial blind for 10 s (15 s per the infobox) [Fan-wiki].
- Fan screenshot "Tomahawk in effect" (Aztec lava map, target labelled "ASTORIA"): a large mass of brown and reddish-brown wings and feathers covers the target's head and upper body [Observed].

**Images viewed**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/hawks.jpg (Tomahawk.jpg, Tomahawk_concept.jpg)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/hawks2.jpg (Tomahawk.png BBR Mar 2012, Tomahawk.PNG Jun 2012, Download_(16).jpg)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/tomahawk_hit_zoom.png

**Depiction for shorts.** She lobs the rope-bound hawk, which spins end over end. On contact the ropes pop and an angry flurry of wings and feathers smothers the victim's face, who flails blind; no injury. The bird's facial acting is [BBG News invention].

**Confidence:** observed.

---

## Eagle Standard (secondary · BBR v1.3.1, Jun 28 2012 → BBG; 2026 status unverified)

**Official text:** "Flapping around in someone's face, getting up in their business and ruining their day for your own selfish purposes? Sounds like blatant patriotism to me!" ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Eagle_Standard).

**Status**
- A July 2012 Gear Up shows "BUY NOW 37,500" Joules and "SPECIAL SPEED -15%" in red, i.e. a penalty [Observed].
- BBG 2.6: "Cooldown multiplier decreased from -15% to -20%", reload 2.5→2, projectile speed 1000→1200 [Fan-wiki transcription].
- The infobox lists "15% Special Speed Increase" and the body "+20%", but the trivia says it "actually increases the amount of time" for specials. The modifier is therefore a penalty, not a boost [Observed + Fan-wiki].
- Current infobox: 75,000 J, 4 s blind, 6 ammo, 0.2 s rate of fire [Fan-wiki].

**Look** [Observed]
- A bald eagle: white head, yellow-orange hooked beak, dark-brown body bound in tan/gold rope bands, yellow talons, and a white tail fan below.
- She holds it upright by the legs at shoulder height, about 1.6 head-heights tall [Inference].
- CORRECTION: the white point under the bird is its white tail. It is not a "silver spike/pole-tip".
- The BBR 1.3.1 promo shows a bald eagle with wings spread over red-white-blue rays and stars.

**Firing / projectile.** A reskin of the Tomahawk: the tied eagle "will rotate forward with straight trajectory" [Fan-wiki].

**Impact / end result.** It "violently thrash[es] around their face, blinding them with a flurry of wings and feathers", for a partial blind of 4 s [Fan-wiki]. It probably looks like the Tomahawk's feather flurry, with white and dark-brown feathers [Inference; not observed].

**Images viewed**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/hawks.jpg (EagleStandard.jpg)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/hawks2.jpg (Eagle-Standard.PNG)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/eagle_zoom.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/conv2/BBRWEAPONS.png.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/bundles.jpg (AstoriaStarter)

**Depiction for shorts.** Same throw-and-flap gag as the Tomahawk, but a rope-wrapped bald eagle. A star-spangled sparkle trail is [BBG News invention], inspired by the official promo's red-white-blue rays.

**Confidence:** observed (look); documented (effect).

---

## Daydreamer (secondary · BBR v1.3, May 3 2012 → BBG; effect reworked; 2026 status unverified)

**Official text:** "Turn your opponents' daydream into a nightmare. Place this badboy on the ground and any yutz that steps on it will have their controls reversed for a few seconds." ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Daydreamer).

**Status and history**
- **Price:** the June 2012 Gear Up shows "BUY NOW 40" Gas [Observed]. The wiki body says 40 Gas and the infobox 32; there is a level-10 lock [Fan-wiki].
- **BBR 1.4.2:** reload 0.1→1.0 [Fan-wiki].
- **BBG 2.6:** clip 1→5, reload 1→2, Ammo+ removed [Fan-wiki transcription].
- **Rework 1:** the overhead icon changed from "a turquoise feather like a Nuggs'" to "a green question mark as of v.1.3.2" [Fan-wiki].
- **Rework 2:** inverted aiming was "eliminated in a much later update" (date unknown) [Fan-wiki].

**Look** [Observed]. A gold/bronze wire geodesic lattice like a dream-catcher (≈#A1854D), with a silver disc at the centre and a pale-blue crystal shard sticking out of the side. She holds it in one hand at hip height; it is about 0.8 head-heights across [Inference].

**Firing.** Placed on the ground, with a 2 s placement delay and a small trigger radius; it does no damage [Fan-wiki]. Once placed, it is "almost invisible (it is only noticeable by a small white crystal sticking out from the ground)" [Fan-wiki].

**Impact / end result**
- **Status "Controls Reversed"** [Fan-wiki, Daydreamer and Status Effects pages]:
  - movement is reversed for 8.0 s per the body (the infobox says 20 s);
  - "a green question mark will appear over the player's head";
  - background music is disabled and other sounds get "a mild echo";
  - explosives set it off harmlessly.
- **Possible trigger effect:** a 2013 fan upload titled "Detonate daydreamer" (unused on any page, no description) shows a wide ring of magenta electric arcs crawling over the floor and columns of white bubbles rising [Observed]. Its link to the Daydreamer rests only on the filename [Inference, medium-low].

**Images viewed**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/dream.jpg (Daydreamer.jpg, Daydreamer.PNG, Astoria-daydreamer.png, Detonate_daydreamer.jpeg)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/conv2/Gnifle-sniper-setup.png.png (loadout icon)

**Depiction for shorts.** She sets down a gold dream-catcher sphere and only its white crystal tip shows. A bear steps on it; a green "?" pops over its head and the music cuts to an echoey hush. It then walks backwards whenever it tries to walk forwards. The magenta-arc floor ring is optional and should be labelled as a fan-screenshot reference.

**Confidence:** observed (look); documented (status effect); partial (trigger visual).

---

## Fairy's Dust (secondary · BBR 1.4.3/1.4.3.1, Apr 2013 → BBG; in the 2026 trailer)

**Official text:** "Enemy got you in their cross hairs? Toss this lil' sack-o-magic and give 'em the slip. This magical concoction can be a real life saver!" ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Fairy%27s_Dust). BBR 1.4.3 note: "-Fairy's Dust: Astoria's magical concoction that confuses enemies and conceals movement." The 1.4.3.1 notes call it "Fairy's Sparkle" [Fan-wiki transcription of SkyVu notes].

**Status.** 165,000→125,000 J in 2.20 [Fan-wiki]. BBG 2.6: duration 3.5→4, clip 2→1, projectile speed 900→1000 [Fan-wiki transcription].

**Look** [Observed]. A glittery pink-to-purple sack (≈#DC78DA, highlights #FA96E6) tied with a red ribbon under a crumpled blue/cyan crystal top. Yellow, pink and purple four-point star sparkles float off it. It is held in one hand and is about 0.8 head-heights tall [Inference]. It also appears as a bottom icon on the official "1.4.3 UPDATE COMING SOON / WILD N' WACKY WEAPONS" promo.

**Firing.** Thrown. 1.5 s rate of fire, 1 ammo, 3 s reload [Fan-wiki].

**Projectile.** The sack, leaving a trail of tiny yellow and pink star sparkles [Observed, fan "close up during flight" screenshot].

**Impact / end result**
- The wiki: it bursts "into a large, blinding cloud of 'fairy dust' upon coming into contact with a surface", harmless and lasting 4 s. Sniper rifles can still lock on inside it [Fan-wiki].
- **2026 official trailer** [Observed]:
  - ≈13.8–14.0 s: Astoria (red jacket) holds the sack and drops or throws it at her feet.
  - ≈14.1 s: a pink star-burst pops.
  - ≈14.2–14.9 s: a huge translucent cloud with faceted, crystal-like edges swallows the temple stairs. It is hot magenta (≈#F828F8), shading to violet (≈#D828F8–#9818F8), with white twinkles.
  - The cloud is still on screen at ≈16.1 s.
  - ≈16.2–16.3 s: she steps out of it toward the camera holding the Dead Eye.
- **2013 fan screenshot:** the same faceted cloud reads more violet-purple (mean ≈#9704D4, with magenta #FA0AFA edges) [Observed].
- The wiki calls the cloud "purple". The 2026 footage leans magenta.

**Images viewed**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/fairy1.jpg (FairysDust.jpg, Fairy's_dust_close_up_during_flight.jpeg)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/fairy2.jpg (Cloud_for_fairy_dust.jpg, Aaaaa.jpg)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/fd_grid.jpg, a2.jpg and a3.jpg (trailer 13.4–16.5 s)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/concepts.jpg (143releasepic)

**Depiction for shorts.** She tosses the sparkly pink sack, which leaves a trail of tiny stars. It poofs into a giant faceted magenta-violet cloud with twinkles. She vanishes inside and then strolls out deadpan with the Dead Eye; this beat is lifted straight from the official trailer. Harmless; it lasts about 4 s.

**Confidence:** observed.

---

## Rake (secondary · in BBG by Jan 2014, release version undocumented; 2026 status unverified)

**Official text:** "Stop your opponents dead in their tracks with this exciting new gardening tool!" ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Rake).

**Status.** 100,000 J, no level lock [Fan-wiki]. "It used to do 999 damage"; the infobox now says 110 [Fan-wiki]. The image was uploaded Jan 25, 2014 (ApplerGamers) [Fan-wiki file metadata]. The wiki calls it "the only secondary that deals damage", which ignores I Lava You.

**Look** [Observed]. A dark-grey riveted metal rake head (≈#40454A) with five bright turquoise teeth (≈#33E5B7). The Gear Up shows it held head-up; the handle is mostly hidden. The skin in that image is black with red stripes and three glowing red lenses. This matches the wiki's Solid Fisher skin: "an all-black suit with team-colored stripes on the arms, legs and headband with three glowing headlights" [Fan-wiki]. That identification is [Inference].

**Firing.** Placed on the ground "much like the Daydreamer". Single use; it can be stacked [Fan-wiki].

**Impact / end result.** It "will spring up and damage any enemy that walks into the Rake" [Fan-wiki]. Shooting it also triggers it, explosives remove it, and it can kill its owner [Fan-wiki]. The spring-up visual was not observed [Unverified].

**Images viewed**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/conv2/Rake.jpg.png

**Depiction for shorts.** The classic step-on-the-rake gag: the turquoise-toothed rake springs up and the handle bonks the victim's face, with stars and no injury [BBG News invention, consistent with "spring up and damage"].

**Confidence:** observed (look); documented (effect).

---

## I Lava You / "I Lava U" (secondary · BBG 2.51, Apr 13 2018; 2026 status unverified)

**Official text:** none found. The wiki page quotes no official description and its infobox titles it "I Lava U" (https://battlebears.fandom.com/wiki/I_Lava_You).

**Look** [Observed]. A compact gun whose body is dark-brown lava rock (≈#754222) with glowing red-orange fissures (≈#BD3223, hot spots #FA825A). It has grey metal barrel and scope parts and a red glowing lens. She holds it two-handed at chest height; it is about 1.1 head-heights long [Inference]. The image is in the Sniper (BBG) generic-skins gallery, uploaded May 12, 2018 with the comment "Sniper with I Lava U" [Fan-wiki file metadata]. The I Lava You page itself currently has no image.

**Firing.** "It shoots proximity based mines in a straight line until it collides with a wall or floor." The mines can be detonated manually with reload. 1200 u/s, 4 ammo, 1.0 s priming time [Fan-wiki].

**Projectile.** Mines. Not observed [Unverified].

**Impact / end result.** "These explode if an enemy gets close to them", with a 100-unit trigger radius and 25–60 explosive damage [Fan-wiki]. The wiki says it is based on the unreleased Battle Bears Ultimate "Lavarifle" [Fan-wiki].

**Images viewed**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/conv2/ILavaU.jpeg.png

**Depiction for shorts.** Glowing lava-rock blobs fly straight, stick where they land and pulse, then erupt in orange fire-sparks when a bear walks near. The look of the mines and the blast is [BBG News invention].

**Confidence:** observed (look); documented (mechanic).

---

## Battering Ram (melee · default · BBR v1.1 → BBG; 2026 status unverified)

**Official text:** "Using revolutionary "Ram Skull" technology for maximum bashing ability, this is a weapon of last resort." ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Battering_Ram).

**Status.** 30 damage, +40% special speed [Fan-wiki]. BBG 2.6: Melee+1 10→5, Melee+2 15→10 [Fan-wiki transcription]. The page itself still lists +10/+20.

**Look** [Observed]. A grey stone club (≈#545454–#6C6C54) whose head is a curled ram horn, not a skull. It is lashed with dark leather straps and has a wrapped grip. The in-game texture shows orange, purple and green flecks at the base of the horn. It is held one-handed and is about 1.4 head-heights long [Inference].

**Firing.** A melee swing. Barks: "Watch it, swinging a club here!" and "Eee-yaaa!"; melee kill line: "I thought your head would be harder." [Fan-wiki].

**Impact / end result.** Not documented [Unverified].

**Images viewed**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/melee1.jpg (Battering_ram.png, Battering_Ram_Concept.jpg)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/deadeye_gear.jpg (Sniper_setup icon)

**Depiction for shorts.** A reluctant "last resort" bonk with the curled stone ram horn. The cartoon "thunk", stars and stagger are [BBG News invention].

**Confidence:** observed (look); unknown (hit effect).

---

## Brr-Ram-Ewe (melee · BBR era, in the Mar 2012 Gear Up → BBG; 2026 status unverified)

**Official text:** "Freshly shipped and still cold remains from an authentic once-living ram!" ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Brr-Ram-Ewe).

**Status.** The Mar and June 2012 Gear Ups show "BUY NOW 90,000" J [Observed]. The current wiki says 105,000 J at level 13 [Fan-wiki]. BBG 2.6: damage 33→35, cooldown modifier 0→5% [Fan-wiki transcription]. The page says 30 damage [Fan-wiki].

**Look** [Observed]. An icy, pale-blue crystalline ram-horn club (≈#5081A1, with white highlights), a dark handle and teal-blue wraps. About 1.5 head-heights long [Inference].

**Impact / end result.** Any freeze effect is undocumented [Unverified].

**Images viewed**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/melee1.jpg (Brr-ram-ewe.png, Brr-ram-eve.PNG)

**Depiction for shorts.** An ice-horn bonk. A puff of frost sparkles is [BBG News invention]; no freeze status is documented.

**Confidence:** observed (look); unknown (hit effect).

---

## Cybernetic Ram (melee · BBR era → BBG; 2026 status unverified)

**Official text:** "An ebony club imbued with needless fiery energy canals!" ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Cybernetic_Ram).

**Status.** The Gear Ups show the price falling [Observed]:
- 300 Gas (Mar 2012)
- 50 Gas (June 2012)
- 30 Gas (July 2012, in the Golden Dragon Gear Up)

The page body says "20 Gas" at level 12, and its trivia says "current price of 30 Gas" [Fan-wiki]. BBG 2.6: damage 35→40, speed modifier 0→10% [Fan-wiki transcription].

**Look** [Observed]. A black ram-horn club laced with glowing orange-red circuit and energy channels (≈#C76732 to #FAAA5A), including a ring motif on the horn. About 1.5 head-heights long [Inference].

**Impact / end result.** Undocumented [Unverified].

**Images viewed**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/melee2.jpg (Cybernetic_ram.png, Cybernetic-ram.PNG, Golden-Dragon.PNG)

**Depiction for shorts.** A black horn club whose orange circuits flare on the swing. Ember sparks on contact are [BBG News invention].

**Confidence:** observed (look); unknown (hit effect).

---

## Golden Dragon (melee · BBR v1.3.1, Jun 28 2012 → BBG; 2026 status unverified)

**Official text:** "Ever the connoisseur, an appreciator of the fine arts, it is up to you to make everyone else understand the beauty of this piece. Beating them up the side of the head with it is the logical place to start." ~ Official Battle Bears Gold description [Game text via wiki] (https://battlebears.fandom.com/wiki/Golden_Dragon).

**Status.** 50 Gas, 55 damage [Fan-wiki]. BBG 2.6: Melee+1 10→5, Melee+2 18→10 [Fan-wiki transcription]. The stat modifier conflicts: the wiki says +20% special speed, but the 2015 Gear Up shows "HEALTH +10%" [Observed].

**Look** [Observed]. A gold, scaled dragon-head club (≈#9D680E, highlights brighter gold) with a green gem eye, a dark-green crest and a scaled shaft. It also appears coiled at the centre of the BBR 1.3.1 promo. About 1.8 head-heights long [Inference].

**Impact / end result.** Undocumented [Unverified].

**Images viewed**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/melee2.jpg (Golden-Dragon.PNG, Golden_Dragon.jpg)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria/v2/conv2/BBRWEAPONS.png.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/fairy2.jpg (HUD melee icon)

**Depiction for shorts.** An "art connoisseur" bonk with a gold dragon-head club. Gold-glint sparks are [BBG News invention].

**Confidence:** observed (look); unknown (hit effect).

---

## Unreleased concepts (not in the BBG weapon category; use only as labelled easter eggs)

### Toucan (planned Tomahawk upgrade, 2012)
- **Status:** revealed on the SkyVu blog on Apr 27, 2012 as an "upgraded Toucan version of the Snipers' Tomahawk" [Fan-wiki; blog unreachable, Unverified]. Never released.
- **Look** [Observed]: a painted toucan with wings spread, black plumage, a yellow chest, an orange beak, a green-and-blue eye patch and a red under-tail.
- **Image:** /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/concepts.jpg (Toucan.png, uploaded Nov 26, 2012).
- **Confidence:** observed (concept only).

### Astoria's Super Scope (concept, wiki upload Nov 22, 2012)
- **Look** [Observed]: titled "ASTORIA'S SUPER SCOPE". A telescoping spyglass-rifle with an engraved silver tube, a brown leather cone stitched with X marks, gold bands, a big domed lens and a small flintlock-style grip, plus a separate front view of the round lens.
- **Mechanics:** none documented.
- **Image:** /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/concepts.jpg (Super_scope.jpg).
- **Confidence:** observed (concept only).

### Slumberbun land mine (concept, wiki upload Nov 20, 2012)
- **Look** [Observed]: "Slumberbun- land mine". A sleeping golden bread-bun dome, annotated "Not Actual Size", that wakes into a screaming bun with bulging red eyes when triggered.
- It looks like an early relative of her ground traps [Inference].
- **Image:** /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/astoria-r3/sheets/concepts.jpg (Slumberbun.png).
- **Confidence:** observed (concept only).

---

## Other eras (not BBG)

**BB Heroes (BBH, 2023/24): Sniper Rifle + "Explosive Retreat" Ultimate**
- Official text: "Astoria wields a sniper rifle for long-distance attacks, dealing more damage from afar. Up close, she's vulnerable but compensates with her "Explosive Retreat" Ultimate, diving away from the action when enemies get too close." [Canon, battlebears.com/pages/characters, re-fetched 2026-10-16].
- Wiki table: Sniper Rifle "2000 max" damage; Explosive Retreat "4 x 670"; 300 Shards; added May 2023 [Fan-wiki].
- Oct 14, 2024 balance: "Max Range Attack Damage Reduced (-20%)", "Min Rage Attack Damage Increased (+20%)" [Fan-wiki].
- I did not research its look [Unverified]. Do not mix it into BBG-era shorts without labelling the era.

**Battle Bears Overclock (BBO)**
- The "Viper Rifle" is "a direct carryover of the Viperifle (BBG)": hitscan, zoomable, 70 damage, 7 ammo, 20% crit [Fan-wiki].
- It "was originally only able to be obtained as a reward for Battle Bears Gold players who linked their accounts on Launch Day" [Fan-wiki].
- No image is on the page.

---

## 2026 re-release: what is actually shown

**Official (SkyVu / Steam)**
- The Steam store text lists "-SNIPER: Astoria" and "80+ PRIMARY WEAPONS / 60+ SECONDARY WEAPONS / 50+ MELEES" [Canon].
- The official Steam trailer ("Battle Bears Gold Premium - Trailer", the only movie in appdetails) shows [Observed]:
  - Dead Eye: shot and buffalo-skull smoke at ≈12.2–13.7 s; ASTORIA / SNIPER title card at ≈16.4–17.8 s.
  - Fairy's Dust: ≈13.8–16.3 s.
  - Viperifle: ≈30.0–30.9 s, in the cucumber-mask skin.
- Steam screenshots 01 and 04 both show the Viperifle [Observed].
- The official teaser thumbnail (d2ByJWrsoec, Oct 2 2026) shows a green stream shot from a cream, red-strapped bear [Observed]. I infer it is a Viperifle shot.

**Not shown**
- The other 15 Sniper weapons are not shown in any official 2026 material I could open. Their presence, stats and prices in 2026 are [Unverified].

**Fan sources**
- The JustNubz showcase ("BBG All Classes Showcase [Skins, Taunts, Weapons, and Melee] (from Closed Playtest #4)", title via oEmbed) could not be viewed.
- The official short "Never let bro know your next move" (qp5cFGLojyw, Sep 17 2026) shows a wide mint-green streak (≈#55DB7F) and a red ring crosshair. Neither its shooter nor its weapon can be identified [Observed, inconclusive].

---

## Corrections to the previous researcher's inventory

1. **Eagle Standard look.** The "silver spike or pole-tip" under the eagle is the bird's white tail fan [Observed, eagle_zoom.png].
2. **Eagle Standard modifier.** It is documented as a penalty: "SPECIAL SPEED -15%" in red in the July 2012 Gear Up, and the 2.6 log's "-15% to -20%" [Observed + Fan-wiki].
3. **Dead Eye trailer impact.** The orange fire on the target comes from a separate projectile from off-screen right (≈12.3 s), not from the Dead Eye. The Dead Eye's own effect is the white twisting streak plus red horned-skull smoke [Observed; attribution Inference].
4. **Viperifle projectile.** It is no longer purely text. The 2026 teaser thumbnail shows a bright-green stream with a yellow-green splash [Observed].
5. **Viperifle in 2026.** Also held by default red-team Astoria in Steam screenshot_04, not only in the spa skin [Observed].
6. **Cucumber-mask skin.** The "green face-mask" is a cucumber spa face mask: a mint mask with a cucumber slice over one eye, worn with a blue top and blue polka-dot shorts. The Mean Mamba Bundle contained the Sniper class, Mamba's Boy and Pandini. Pandini is a Demo skin, so the spa skin's name is still [Unverified].
7. **Cybernetic Ram price.** The July 2012 Gear Up shows 30 Gas, confirming the 300→50→30 sequence. The wiki's "20 Gas" is unexplained.
8. **Red Capital Pains video.** It is by the fan channel ApplerGamers (oEmbed). The POV skin is Solid Fisher.
9. **Rake Gear Up skin.** It matches the wiki's Solid Fisher description [Inference].
10. **Fidget Boomer speed.** The conflict is three-way: 3000 u/s (infobox), "fastest projectile speed in the game" (trivia), and "slow" (body).
11. **Detonate daydreamer.jpeg.** An unused, undescribed fan upload (Interamnia, May 10, 2013). Its Daydreamer link is the filename only.
12. **Fairy's Dust cloud colour.** It differs by source: violet in 2013 (≈#9704D4) and hot magenta in the 2026 trailer (≈#F828F8).
13. **Art of War characters.** The characters on the render and concept appear in traditional form (孫子兵法); the wiki types them simplified.

---

## Corrections for the character file (/home/user/thallo-site/bbg-news-repo/characters/astoria.md)

Flagged only; nothing was edited.

1. **Gear.**
   - Current: "- **Gear:** grey-blue backpack on dark straps, black woven utility belt [Observed]."
   - Correction: "- **Gear (BBG default):** team-colour gear: red backpack and shoulder straps, red belt with a dark-maroon quilted band and a red side pouch, red gloves, red-and-white striped boots [Observed]."
   - Evidence: every in-game Gear Up image opened (Viperrifle.jpg, Viperifle.jpg, Crossbow.jpg, Dead_Eye.jpg, Mamba.jpg, FairysDust.jpg). Sampled red ≈#900C0A–#BE1E1E, band ≈#461E1E. The wiki's default skin text: "an ammo belt, a backpack and gloves with the colour of the team colour". The grey-blue backpack and generic grey rifle come only from the 2D art File:Astoria-sniper-viperifle.png.
2. **Prompt pack.**
   - Current: "Grey-blue backpack (#6F8296) on dark straps, black woven ammo belt, red gloves. Long scoped sniper rifle held upright, other hand on hip."
   - Correction: "Red (team-colour) backpack and straps, red belt with a dark-maroon quilted band and red side pouch, red gloves, red-and-white striped boots. Holding the Viperifle: a black sniper rifle with a dark-green liquid capsule on top, green vents by the grip and a snake-head muzzle with a glowing lime eye."
   - Evidence as above, plus Steam screenshot_04.
3. **Placeholder colours.**
   - Current: "eyes #2E9C8A, backpack #6F8296, belt/straps #1F1F24, gloves #CC1818 (red team)".
   - Correction: sampled values: eyes ≈#468296 (blue-teal), backpack/straps/gloves ≈#900C0A–#BE1E1E, belt band ≈#461E1E.
4. **The teal-masked sniper.**
   - Current: "a teal-masked sniper in a 2026 Steam screenshot, which is Astoria only by [Inference]".
   - Correction: describe it as a mint-green cucumber spa face mask (cucumber slice over one eye), blue top and blue polka-dot shorts, holding the Viperifle. The same outfit appears on the official "MEAN MAMBA BUNDLE" Sniper bundle banner (Mar 8–10, 2013) and in the official trailer ≈30.0–30.9 s. It is still an inference that this is Astoria, but a strong one; the skin name is [Unverified].
5. **Battering Ram.**
   - Current: "the Battering Ram ram-skull club".
   - Correction: "the Battering Ram, a grey stone club whose head is a curled ram horn lashed with dark straps". Keep the quote: the game text says "Ram Skull" technology, but the model shows a horn, not a skull [Observed: Battering_ram.png, Battering_Ram_Concept.jpg].
6. **The hawk.**
   - Current: "Draw the hawk as an angry-bird gag, with no cultural styling [BBG News invention]."
   - Correction: keep the gag, but add the documented design and hit. A brown hawk with a cream chest, yellow hooked beak and talons, and blue-tipped feathers, trussed in tan rope including around the beak. Thrown tumbling; on contact the rope pops and a flurry of wings and feathers smothers the target's face, a partial blind with no damage [Observed + Fan-wiki].
7. **Weapons/props should name the 2026-visible arsenal.** Add:
   - the Dead Eye: a bone rifle with a biting skull scope, white streak plus red buffalo-skull smoke, and the 2026 title-card pose;
   - Fairy's Dust: a pink sparkle sack that bursts into a magenta-violet cloud, her escape move in the trailer [Observed, official trailer].
8. **Explosive Retreat (BBH) used in BBG-era beats.**
   - Current: "Her Explosive Retreat overshoots into a Huggable pile." and "Her Explosive Retreat lands her right back beside him."
   - Correction: Explosive Retreat is a BB Heroes (2023/24) Ultimate, not a BBG weapon. For BBG-default shorts, swap in Fairy's Dust (the trailer's own vanish-and-reappear beat) or the Tomahawk, or label the beat as BBH-era.
   - Also, in the Fighting line, "Up close, she's vulnerable but compensates with her 'Explosive Retreat' Ultimate" should be tagged as BBH.
9. **Eyes and negative prompt (non-weapon).**
   - Current: "teal-green, heavy-lidded" and a negative prompt containing "blue eyes".
   - Correction: all in-game BBG models opened show blue / blue-teal eyes (≈#468296), and the 2026 trailer title card shows blue eyes. Drop "blue eyes" from the negative prompt, or note the wiki's green-eye claim as fan-only.
10. **Open question on the 2026 default look.**
    - Current: "What default skin, taunts and audio does the 2026 build use?"
    - Correction: partly answered. Steam screenshot_04 shows the classic cream fur and red team gear with the Viperifle. The trailer title card uses the red-jacket outfit with the Dead Eye.

---

## Open questions

- Which of the 18 Sniper weapons are in the 2026 build, and with what stats and prices? Only the Viperifle, Dead Eye and Fairy's Dust appear in official 2026 material. The JustNubz Closed Playtest #4 showcase (Sniper chapter at 22:30) needs a human viewer.
- What is the date of the official "BATTLE BEARS GOLD Developer Update - Astoria Overhaul" (wUWf9O-YX4A), and what did it change? Its HUD ammo counts (8/10, 4/4, 3/3, 0/2) match no wiki stat set.
- What does the Mamba's Boy projectile look like (a pale white streak in one thumbnail)? And the Blow Dart dart and its blue-tinged explosion, the Fidget Boomer explosion, the I Lava You mines, the Art of War paint burst, the Rake spring-up, the charged Crossbow burst, and all four melee hit effects? None has been observed.
- Is the Dead Eye streak white (2026 trailer) or red (wiki), and did it change between eras?
- Is the Capital Pains' red mode still removed, and when was it removed? Is the 2015 silver barrel the "white" state?
- What is the true Eagle Standard modifier in 2026: penalty or boost?
- Does the "Detonate daydreamer" magenta arc ring really show the Daydreamer trigger?
- What are the names of the cucumber spa skin and the red-jacket/white-sleeve skin?
- SkyVu's own 2.6 change log (battlebears.com/battle-bears-gold-2-6-change-log/, archived 2015-10-29) and the Apr 13 and Apr 27, 2012 squarespace blog posts are still unreachable (Wayback blocked, archive.ph 429). Until they are checked, every patch-note line above is a [Fan-wiki] transcription.
