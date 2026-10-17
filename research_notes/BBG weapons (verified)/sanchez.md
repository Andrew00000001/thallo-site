# Sanchez (Arbiter): weapons dossier (verified edition)

**What this covers.** Sanchez is Battle Bears Gold's **Arbiter** class.
- BBG 2.6 added him on Dec 20, 2013 [Fan-wiki: Updates; Battle Bears Gold/Versions/2.6; Arbiter (BBG) changelog].
- The 2.6 class blurb reads: "Back from the brink of death, Sanchez has been rebuilt from the arm up! Use his unique weaponry to slow down opponents and finish them off with his devastating melee attacks." [Game text via wiki] (Battle Bears Gold/Versions/2.6; the Updates page has the typo "brink of dea").
- The Steam page for the Nov 4, 2026 re-release lists "-ARBITER: Sanchez" among the classes and "80+ PRIMARY WEAPONS 60+ SECONDARY WEAPONS 50+ MELEES" [Canon] (Steam appdetails 4408320, re-fetched 2026-10-17). It gives no Arbiter kit.

**How complete this is.**
- The wiki class page "Arbiter (BBG)" lists 14 weapons: 6 primaries (Bind Gun, Parashoot, Glue Bomb, Greased Lightning, Spin Baby Spin, Kelowna), 5 secondaries (Speed Field, Cloak Field, Invulnerable Field, Carpet Bomb, Drain Field) and 3 melees (Blade Augment, Stealth Knife, Harvester) [Fan-wiki].
- Category:Arbiter (29 pages, listed today) contains the same 14 weapon pages. "Bind Gun" redirects to "Adrenaline Gun".
- weapons_by_class.json["Sanchez"] has only 13, because "Adrenaline Gun" sits in "_unassigned". It belongs to Sanchez.
- All 14 entries of arsenal_sanchez.json are covered below.

**Era key** [Fan-wiki: Updates, unless marked]
- **BB Zombies:** Sanchez is the Pelican't pilot who crashes. He has no weapon kit.
- **BBR (2012):** no Arbiter class; the class is "New" in BBG 2.6.
- **BBG:** 2.6 (Dec 20, 2013) through 2.53.3 (Aug 31, 2018), then 3.0 (Nov 15, 2021) and 3.0.1. The 3.0 notes say "All +1 Equipment has been removed except Speed +1" and "Equipment Slot 2 has been removed".
- **BBG 2026:** the Steam, iOS and Google Play re-release [Canon: Steam date].
- **BB Heroes (BBH, 2024):** a different game.

**Sources reached today (2026-10-17)**
- Wiki MediaWiki API: all 14 weapon pages with their revision histories and 30 old revisions, plus Arbiter (BBG), Status Effects, Updates, Battle Bears Gold/Versions and /2.6, Taunts, and the skin pages Judge Sanchez, Tron-Tastic!, Bear of Rhodes, Sanchez (Skin) and The Gold Pack.
- Every wiki image named on those pages, converted from WebP to PNG.
- battlebears.com/pages/characters (live).
- Steam appdetails.
- All 108 local trailer frames and the 5 Steam screenshots.
- YouTube: thumbnails (hqdefault, hq1–3, maxres), oEmbed titles and channels, and watch-page dates and descriptions for 31 videos.

**I watched no video.** Every YouTube [Observed] tag means a still thumbnail I opened. hq1, hq2 and hq3 are YouTube's automatic frames from roughly 25%, 50% and 75% of the runtime [Inference].

**Not reached: web.archive.org.**
- The proxy answered HTTP 403 "Blocked by egress policy", then dropped connections. I tried 3 times with backoff for each of: the 2.6 notes (snapshots 20131224204516 and 20140214154039), the Jun 2014 post (20140617141419) and the weapon-card JPG.
- WebFetch refuses the domain.
- The availability API answers, but it returns no snapshot for the Jun 2014 "tillman-overhaul-new-sanchez-weapons-in-bbg" post.
- Every archived SkyVu quote therefore stays [Canon, quoted in prior notes; Unverified today].
- YouTube thumbnails for the wiki's two demo-video files (0zBUHqR6Wkc Parashoot, I7I02IwJIec Carpet Bomb) return HTTP 404.

**Scale.** Sanchez is 1.0× Oliver, lean, with the right arm about 1.5× the left [BBG News invention: characters/README.md scale chart]. Weapon sizes below are fractions of Sanchez's visible height in the wiki's loadout-screen renders [Inference, approximate]. Hex values are medians or clusters of small crops and depend on lighting and compression [Observed, approximate].

**Arsenal at a glance** [Fan-wiki unless marked]

| Weapon | Slot | Added | Status |
|---|---|---|---|
| Bind Gun → Adrenaline Gun | Primary | 2.6, Dec 20, 2013 | Default. Reworked from slowing to speeding up its targets around Jun 19, 2021. 2026 name and effect unverified |
| Glue Bomb | Primary | 2.6 | Unlock (90,000 J, now 60,000 J) |
| Greased Lightning | Primary | Changelog says 2.9; wiki page created Jun 7, 2014 | **REMOVED.** The banner was added 2020-11-10; no removal date is given |
| Parashoot | Primary | 2.18, Apr 3, 2015 | Unlock, level 20 |
| Spin Baby Spin | Primary | 2.27, May 29, 2017 | Unlock |
| Kelowna | Primary | 2.31, Mar 8, 2018 | Unlock |
| Speed Field | Secondary | 2.6 | Default |
| Cloak Field | Secondary | 2.6 | Unlock |
| Invulnerable Field | Secondary | Changelog says 2.9; page created Jun 7, 2014 | Unlock |
| Carpet Bomb | Secondary | 2.15, Dec 20, 2014 | Unlock, level 10 |
| Drain Field | Secondary | 2.16, Jan 30, 2015 | Unlock, level 20 |
| Blade Augment | Melee | 2.6 | Default |
| Harvester | Melee | 2.6 | Unlock |
| Stealth Knife | Melee | 2.21, Jul 3, 2015 | Unlock |

**What this verification changed** (details are in each section)
1. **Drain Field: sunglasses and bats are observed.** A Mar 24, 2016 fan frame (xAp9gFMriAU hq1) shows the red field creature wearing dark-grey sunglasses, with small black bats with glowing red eyes flying around it. The draft said neither was seen. The field is red, not "dark".
2. **Drain Field concept art:** only the creature is coloured. The syringes, dome and health crosses are greyscale; the draft's "red liquid" is wrong (pixel check).
3. **Parashoot canopy:** the Apr 2015 maxres frame shows a **large** dark-grey dome (#393C3C, light-grey rim) over the target's head and upper body. The small black ball with a white rim and pale-cyan streaks is a separate object at the target's hip. The draft merged the two.
4. **Parashoot holder:** 0njNOuanL3E hq1 shows a dark red-black skin with a yellow helmet chevron (probably Judge Sanchez [Inference]), not Tron-Tastic!.
5. **Blade Augment card swoosh:** it is grey on the captioned card (Sanchez_weapons.jpg) but **red/pink** (#BE706B, #DB9F9A) on the textless card (Arbiter_sanchez.jpg). The draft's "grey, not red" was half right.
6. **Bind Gun stat history fixed.** The 0.15 s rate of fire, the 1 s slow and 40 ammo date from Dec 2014 (rev 68395). 45 ammo and slow 0.9 date from Jun 2018 (rev 75783). The draft dated these to 2020.
   - Two more HUD frames now match the wiki's 40-round magazine: "0 / 40" (Jul 2015) and "35 / 40" (Mar 2016).
   - A second Bind Gun hit with the Slowed icon is observed (Mar 2016).
7. **Speed Field citation fixed.** Rev 58375 is the **Cloak Field** page. The Speed Field's Dec 2013 revision is 58374, and it said the orb "cannot be used in mid-air" and that speed is "doubled". Both contradict the current page.
8. **Carpet Bomb slot "conflict" resolved.** The same editor removed "primary" on Jan 7, 2015 with the comment "I corrected the mistake that the carpet bomb was a primary".
9. **Greased Lightning HUD frames were swapped.** 5pXfHBEON4M hq1 reads "0 / 22" (RELOAD) and hq2 reads "22 / 22". That Sanchez fired the observed beam is now marked [Inference].
10. **Stealth Knife launch-week wiki values:** 85 damage, −15% Health, +15% Movement Speed, 75 Gas. They became 400,000 J on Jul 23, 2015, and are now 70 damage, −10%, +20%, 150,000 J.
11. **New status-icon reference:** a white **coffee mug** floats over Sanchez's head in tTqrtzqG-dU hq1. That is the "Caffeinated" icon from the Caffeine Injection special, a speed boost not caused by any Arbiter weapon [Fan-wiki: Status Effects; Observed].
12. **Tron-Tastic! line colour:** the wiki skin page says "red/blue neon lines", which supports the team-colour reading of the cyan-lined 2016 frame.
13. **Extra gun reference:** the Bear of Rhodes skin render (File:Bearofrhodes.png) also shows the same cyan Bind Gun.
14. **Spin Baby Spin 2022 burst:** a big lime-green burst with a dark-green spiral decal on a wall nearby, HUD "2 / 6" (eEw00KhDdTw hq3). The 2022 HUDs show build "2.53.6" [Observed].
15. **Removed character-file corrections.** The draft's video-prompt rewrite ("taps the red lamp"), its Judge/Creepin additions and the "official renders" wording are gone. They were inventions or additions, not errors; the renders are fan-uploaded in-game loadout captures.

---

## Shared visual language (sub-topic: status icons, HUD, skins)

- **Slowed icon** [Observed]
  - A chunky yellow "Z" (about #EEEC39–#FCFF0E) between two white curved arrows that form a circle, floating over the victim.
  - Seen in:
    - GoF3Hy4QQis hq3 (Jan 30, 2014, over "HARRY")
    - tTqrtzqG-dU hq3 (Mar 8, 2014, "BEARBEARIAN")
    - xzRwifNTXWU hq1 and hq3 (Dec 23, 2013)
    - Wfy_1E0CZBE hq2 (Dec 27, 2014, "K@MBO$$")
    - xAp9gFMriAU hq1 (Mar 24, 2016, "PLAYER 11003264")
    - t-Dupfa6rsE hq1 (Jan 15, 2017, "BEARY10")
    - RRI-ejnlcww hq3 (May 30, 2017, "HOI")
    - JVEQQqyafzE hq1 and hq2 (Sep 20, 2026)
  - The wiki says only "a yellow Z will appear over the player's head" [Fan-wiki: Status Effects].
  - Wiki Slowed sources: "Slow Motion Field, Phantom Hug (immobile), Slow Field, Bind Gun, Glue Bomb" [Fan-wiki]. A Z alone does not prove which weapon caused it [Inference].
  - An hourglass Special button appears in several Sanchez HUDs (RRI-ejnlcww, t-Dupfa6rsE, 5gKnLQX1sUc) [Observed]; plausibly the Slow Motion Field [Inference].
  - Wiki bug, Mar 2014: "teammates hit by the purple beam [...] display a 'Slowed' status effect above their head" [Fan-wiki rev 61247].
- **Caffeinated icon (not an Arbiter weapon):** "a coffee mug will appear over the player's head, indicating a boost in speed" [Fan-wiki]; source: Caffeine Injection.
  - Observed: a white mug over Tron-Tastic! Sanchez, and a mug Special button, in tTqrtzqG-dU hq1 (Mar 8, 2014). Mug Special buttons also appear in xzRwifNTXWU and GcPIzMXFYT4.
  - Do not use this mug for the Adrenaline Gun's speed-up. No icon is documented for that.
- **Controls Reversed:** "a green question mark will appear over the player's head" [Fan-wiki]. Observed as a lime-green "?" beside a pink Huggable (eEw00KhDdTw hqdefault and hq2, Mar 1, 2022).
- **Poisoned:** "a purple/green skull will appear over the player's head" [Fan-wiki]. The Kelowna cloud puffs are themselves skull-shaped [Observed].
- **Damage Resistance** (Invulnerable Field): "No overhead icon shown. Players affected receive 50% less damage. Effect stacks." [Fan-wiki].
- **Forearm lamp** [Observed: Arbiter.jpg, 480px-InvulnerableField.jpg]
  - Every field render shows the red-black prosthetic forearm with a glowing red lamp panel (#B30303 core, #740707, dark #3A0101).
  - That this lamp is the "button on his arm" is [BBG News invention]; the wiki's "command gauntlet" and "button" are text only [Fan-wiki].
- **Skins seen holding his weapons** [Observed]
  - Default: maroon helmet, red visor, grey camo shirt, olive camo trousers.
  - Judge Sanchez: black suit with red stripes, three gold stars on a gold helmet band, gold-rimmed red visor, gold chevrons on the helmet sides. It is in the Kelowna and Stealth Knife renders [Observed, compared with File:Judge_Sanchez.png]. The wiki calls it "red-black style" [Fan-wiki].
  - Gold Sanchez: gold with red gems.
  - Tron-Tastic!: black with glowing lines. The lines are red-orange in 2014, 2015, Mar 2016, 2018 and 2026 frames and cyan in Yx36xc6nXVk hq1 (Jan 12, 2016). The wiki says "red/blue neon lines" [Fan-wiki], so the colour is probably the team colour [Inference].
  - Bear of Rhodes (2.21): yellow-red armour, render holding the cyan Bind Gun.
  - A dark-navy-armoured Sanchez with a yellow helmet chevron (5twbNI7iakw, kwtuHF2SQHo); skin unidentified.
- **Unexplained pink crackle** [Observed]
  - A pink-magenta electric crackle wraps Sanchez's lower body or hand in:
    - tTqrtzqG-dU hqdefault and hq2 (0/5, RELOAD)
    - O60Fq06wfec hq2 (0/5)
    - 0njNOuanL3E hq1
    - kso2WuRLZpo hqdefault (2/15, so it is not tied only to an empty magazine)
    - vcwRC2cQ1ik maxres
  - Its cause is [Unverified]. Do not animate it as a weapon effect.
- **2026 trailer and Steam screenshots:** Sanchez is in none of the 108 trailer frames (hero cards: B-1000, Graham, Astoria, Wil, Tillman, Huggable, Riggs, Oliver) and none of the 5 screenshots. screen_04 shows a B-1000 and a red-spotted bear, not Sanchez [Observed].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/gof_crops.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/glue.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/xz_y2.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/mid.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/mid_crops.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/para.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/para2.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/para_holders.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/y2026.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/judge.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/skins.png (Bearofrhodes.png, Trontastic.png, Golden_Sanchez.png, Sanchez.png, iTJ94TmSrGk maxres)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/renders_sec_melee.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/trailer_0.png, trailer_1.png and trailer_2.png in the same folder (frames t_0001–t_0108 of /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/visuals/trailer/)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/tr_pink.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/steam.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/s04.png

---

## Bind Gun → Adrenaline Gun (primary, default; Bind Gun Dec 2013 to Jun 2021, then Adrenaline Gun; 2026 identity unverified)

- **Official text**
  - Bind Gun: "One weapon to slow them all!" [Game text via wiki] (https://battlebears.fandom.com/index.php?oldid=58371, Dec 21, 2013; also in the current page's trivia).
  - Adrenaline Gun: "The only bad thing about being faster than light is that you always live in darkness" [Game text via wiki]. The wiki adds "~Official Battle Bears Gold description, submitted by community member Wilpower784" (https://battlebears.fandom.com/wiki/Adrenaline_Gun).
  - The weapon card labels the gun "BIND GUN" with an up-arrow [Observed: File:Sanchez_weapons.jpg, a 900×691 wiki copy uploaded 2013-12-20]. That it is SkyVu's card is [Inference]: arsenal notes give the official upload as sanchez_weapon_ad2-900x691.jpg, but the archive was unreachable.
  - "Using his unique slowing weapons, Sanchez can change the tide of a match!" [Canon, Microsoft Store 2014, quoted in prior notes; Unverified today].
  - battlebears.com/pages/characters: "Sanchez's "Adrenaline Gun" rapidly fires four staggered projectiles with a fast reload time." [Canon] (re-fetched 2026-10-17).
    - The page never names a game. That it describes BB Heroes is [Inference]; its roster includes a "Brick Battle Specialist" and a "NECROMANCER".
    - Do not use it for BBG.
- **Rework**
  - "This weapon used to be called Bind Gun with a speedMultiplier of 0.8, but it was changed into the adrenaline gun on the 19th of June 2021" [Fan-wiki].
  - SSP Rism added that text on 2021-06-18 23:32 UTC [Fan-wiki history]; the one-day gap is probably a time zone [Inference].
  - Thecheeselover moved the page on 2021-07-17 with the comment "New name for the weapon".
  - Both are before BBG 3.0 (Nov 15, 2021).
- **Look**
  - The loadout render is a chunky, glossy, faceted cyan/teal sci-fi blaster [Observed: Bind_Gun.png]:
    - midtones #3C7089 / #468FAB
    - highlights #6CBCD0
    - panel lines #1A465F / #0F1C24
    - a round muzzle with a white core (#E9F0F6) haloed in pale blue (#9FC9EF)
  - It is held across the chest or hip, the rear gripped by the red-black prosthetic right hand [Observed]. It is about 0.35× his height [Inference].
  - The card draws it longer (about 0.6×) and brighter: cyan #1A9BD5, highlight #3BC8F2, shade #3C6C76 [Observed].
  - 2D promo art (Arbiter_Class, the Sanchez_Release 2.6 banner, Arbiter_(BBG)-infobox) draws it darker royal/steel blue: #146399, #2673A8, deep #0D344E. It has a big round barrel, a blue-lens muzzle and a glowing blue glyph panel [Observed].
  - The Bear of Rhodes skin render (fan upload 2015-09-19) shows the same cyan gun [Observed].
  - In third-person play it is the same cyan block at the right hip; in first person, a cyan stub at lower left [Observed: GoF3Hy4QQis hq1 and hq3; IAGq4yS4ggo hq2].
  - **2026:** the "Arbiter (Sanchez)" chapter thumbnail of JustNubz's Sep 20, 2026 "BBG All Classes Showcase" is file hqdefault_2855033, a frame at about 47:35, inside the chapter that the description lists as "47:23 Arbiter (Sanchez)".
    - It shows the loadout menu ("CHARACTER ARBITER", "SKIN TRON-TASTIC!", "TAUNT NONE") and Tron-Tastic! Sanchez holding the same cyan gun with a glowing white muzzle [Observed].
    - I did not watch the video.
  - May 18, 2022: Gold Sanchez with a blue gun, HUD "55 / 55", build "2.53.6" [Observed: EXf5g_uzhc0 hq1].
- **Firing**
  - Automatic [Fan-wiki].
  - The beam leaves the muzzle with a white-pink flare [Observed: GoF3Hy4QQis hq1].
  - Wiki stat history [Fan-wiki revs]:
    - Dec 2013 (58371): ammo 50; Ammo+1/+2 add +10/+20.
    - Mar 2014 (61247): damage 5.25, reload 3.5 s.
    - Dec 2014 (68395): damage 7.5, slow 0.95, rate of fire 0.15 s, ammo 40, reload 4 s, slow lasts 1 s.
    - Jun 2018 (75783): damage 6.0, slow 0.9, rate of fire 0.15 s, ammo 45, slow lasts 1 s.
    - Apr 2020 (76600): text rewritten to "slowed down [...] by 10%"; same stats.
    - Nov 2020 (77107): damage 5.0, "20% per hit", ammo 55, slow lasts 1.25 s.
    - Adrenaline Gun (current): damage 7.0, "Speed Effect 50% per hit", 0.15 s, ammo 55, reload 4 s, "Duration of Speed 0.5 seconds", +2% Speed; Ammo+1/+2 add +5/+10.
  - HUD ammo seen [Observed]:
    - "32 / 70" (Dec 21, 2013 PTB, Y2IbsH718QA hq3). That is 50 plus +20 from Ammo +2 under the Dec 2013 table [Inference].
    - "34 / 50" and "25 / 50" (Jan 30, 2014, GoF3Hy4QQis hq1 and hq3).
    - "0 / 40" (Jul 22, 2015, IAGq4yS4ggo hq2, Tron-Tastic! holding a pale-blue gun).
    - "35 / 40" (Mar 24, 2016, xAp9gFMriAU hq1, blue-gun HUD icon). Both match the wiki's Dec 2014 ammo of 40.
    - "50 / 50" (Jan 15, 2017, t-Dupfa6rsE hq1). That is probably 40 plus Ammo+ equipment [Inference].
    - "55 / 55" (May 18, 2022).
  - No sound is documented [Unverified].
- **Projectile**
  - Wiki: "seems to shoot a purple beam of energy. It is not completely accurate as the beam tends to move left and right slightly" (Dec 2013). From May 2014: "tends to move in an oval-like wave" [Fan-wiki].
  - **Observed:** a continuous, jagged, crackling hot pink-magenta to lilac beam with white-hot flecks, drawn like a wavering electric arc rather than a straight laser.
    - Sampled #D38CB4, #E698D6, #F1AAEE, peaks #FFC0FF and white.
    - Sources: GoF3Hy4QQis hq1 and hq3; Y2IbsH718QA hq3; also xAp9gFMriAU hq1.
  - No image shows the post-2021 Adrenaline beam [Unverified]. The wiki still says "shoots a purple beam" [Fan-wiki].
- **Impact / end result**
  - At the hit point: a white-pink starburst with thin violet lightning tendrils crackling outward. The victim shows the yellow-Z Slowed icon [Observed: GoF3Hy4QQis hq3 on "HARRY"; xAp9gFMriAU hq1 on "PLAYER 11003264"].
  - 2013–2021 effect: "The longer the target is under the effect, the slower they will become, possibly to the point of becoming immobile" [Fan-wiki rev 61247].
  - Post-2021 effect: targets are "drastically sped up for a brief amount of time", "an easy way to cause them to fall off the map, run into a Sanchez melee or barely miss their intended destination" [Fan-wiki]. No overhead icon is documented for it [Unverified].
  - "If the target has a Shield, the speed up effect will be applied, but damage is not inflicted." "Moving backwards while shooting can hurt yourself and even kill you" [Fan-wiki].
  - **2026:** in a Sep 20, 2026 playtest thumbnail, a magenta beam with a white core enters from off-screen right toward a bear (orange hard hat, red box backpack) who shows the yellow-Z icon [Observed: JVEQQqyafzE hq1 and hq2, "【Battle Bears Gold】Playtest Part1", Mika_do].
    - The shooter is off screen. So slowing exists in the 2026 build, but the frame does not show that the Bind Gun survived [Inference].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/png/Sanchez_weapons.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/png/Arbiter_sanchez.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/renders_primary.png (Bind_Gun.png)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/renders_sec_melee.png (Arbiter_png.png, the Sanchez-page copy of the same render)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/promo2d.png (Arbiter_Class.png, Sanchez_Release.png, Arbiter_(BBG)-infobox.png, BBH_Profile_Sanchez.png)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/skins.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/gof.png and /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/gof_crops.png (https://i.ytimg.com/vi/GoF3Hy4QQis/hqdefault.jpg, hq1, hq2, hq3; "[ED] Battle Bears Gold 2.6 Update! Sanchez Bind Gun Gameplay!", Epic Domination BBG, Jan 30, 2014)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/early_crops.png (Y2IbsH718QA hq3, "Battle bears gold: FFA Sanchez gameplay PTB", K_20_20_K, Dec 21, 2013)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/hud_checks.png (xAp9gFMriAU hq1 and IAGq4yS4ggo hq2 HUDs)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/crops/xap_bats_x5.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/mid.png (t-Dupfa6rsE hq1, EXf5g_uzhc0 hq1)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/versions.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/y2026.png (chapter thumbnail https://i.ytimg.com/vi/-lAtv-j9Sms/hqdefault_2855033.jpg at 336×188, upscaled to /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/crops/chap_arbiter_x3.png; https://i.ytimg.com/vi/JVEQQqyafzE/hq1.jpg, hq2, hq3)
- **Depiction for shorts:** Sanchez braces the chunky cyan blaster at his hip and sprays a wavering, crackling hot-pink beam with white sparks [Observed]. Each hit pops a white-pink starburst with violet crackle, and the victim wades in slow motion under the yellow "Z"-and-arrows swirl [Observed look; the slow-motion acting is BBG News invention]. This is the 2013–2021 behaviour. For a post-2021 gag, the same beam makes the victim zoom off and overshoot [BBG News invention built on the Fan-wiki rework]. Never claim which one the 2026 game uses.
- **Confidence:** observed (look, beam, hit, Slowed icon, 2013–2016). Unknown for the 2026 name and effect.

## Glue Bomb (primary, unlock; BBG 2.6, Dec 20, 2013, to present)

- **Official text:** "Glue plus bomb equals very slow battle bears." [Game text via wiki] (https://battlebears.fandom.com/wiki/Glue_Bomb). The card reads "GLUE BOMB / Throw at Enemy" [Observed].
- **Status:**
  - 90,000 J at launch [Fan-wiki: 2.6 page; rev 58550, Dec 22, 2013]. Now 60,000 J ("It used to cost 90,000 Joules"); no date is given [Fan-wiki].
  - The Dec 2013 text: "The Glue Bomb sticks to walls and does a huge amount of damage in a large radius. Besides just blowing up enemies, it also can be used to drastically slow down enemies." [Fan-wiki rev 58550].
- **Look**
  - A sphere of rounded black/gunmetal armour plates (#1D1D26, #413B4E, #545363), split by glowing seams that form a cross. The seam core is hot magenta (#F423F3) with a lilac glow (#C69DD2, #DA8DE0) and a deep edge (#611A6A) [Observed: Glue_Bomb.png].
  - Carried low in the prosthetic right hand. Palm-sized, about 0.2× his height [Inference].
  - Card icon: navy plates (#141623, #3B3E53) with a violet glowing cross (#481E89) and white glints (#E6DFED) [Observed].
  - HUD icon: the same plated sphere with a hot-pink cross [Observed: Glue_bomb_on_a_wall.jpg].
  - Stuck on a wall: a small dark plated ball with a glowing hot-pink cross [Observed: File:Glue_bomb_on_a_wall.jpg, fan screenshot uploaded 2013-12-22].
- **Firing**
  - "When thrown, the Glue Bomb while fly in an arc and stick to the first solid object it comes into contact with" [Fan-wiki].
  - The card diagram shows a stick figure lobbing a purple ball along pale-blue arc lines [Observed].
  - Rate of fire 2.25 s, ammo 4, reload 4 s [Fan-wiki].
  - HUD ammo seen [Observed]:
    - "2 / 3" (Dec 22, 2013)
    - "3 / 3" (Y2IbsH718QA hq1, Dec 21, 2013)
    - "1 / 3" (xzRwifNTXWU hq1 and hq3, Dec 23, 2013; 5gKnLQX1sUc hq2, Jan 21, 2018)
    - "2 / 5" (jS2I01x4ES4 hq1, Jan 30, 2014)
    - "5 / 5", "2 / 5" and "0 / 5" (tTqrtzqG-dU, Mar 8, 2014). These counts probably include Ammo+ equipment [Inference].
  - The wiki gave ammo 3 in Dec 2013 [Fan-wiki rev 58550].
- **Projectile**
  - In flight: a small dark sphere with a glowing pink cross [Observed: tTqrtzqG-dU hq3].
  - Detonation delay conflict [Fan-wiki]: the Usage says "sticks to surfaces and explodes on impact" and also "after a one second delay, explode", while the infobox says "Explosion Delay 0 seconds".
- **Impact / end result**
  - Wiki: damages and slows all enemies in the area of effect. Slow 80% for 2 s, explosives 15–40. It "affects a large radius, potentially bring whole teams to a standstill" [Fan-wiki].
  - Observed looks:
    - (a) Two large, thin, concentric blue rings (#274377 / #325585, brightest #2F6BAB) around a small pale inner ring, with no fireball [Observed: File:Sonic_wave_glue_bomb.jpg; wiki caption "A Glue Bomb releasing a slowing field" (Fan-wiki)].
    - (b) A translucent pale-cyan bubble sphere with a white-blue core, and a faint ring on the ground [Observed: jS2I01x4ES4 hq1, "FIVE GLUE BOMBS!!!!????", CheeseclanBBG, Jan 30, 2014].
    - (c) Faint pale-blue ripple rings on the snow beside a victim who shows the yellow Z [Observed: tTqrtzqG-dU hq3].
    - (d) A big yellow-white flash over a victim showing the Z, with a glue-bomb HUD at "1 / 3" [Observed: xzRwifNTXWU hq3, Dec 23, 2013]. That the flash is the bomb is [Inference].
  - Card diagram: the victim stands in blue ripple rings, wrapped in a crackling purple outline [Observed, both cards].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/png/Sanchez_weapons.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/png/Arbiter_sanchez.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/renders_primary.png (Glue_Bomb.png)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/inplay_wiki.png (Glue_bomb_on_a_wall.png, Sonic_wave_glue_bomb.png)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/gbw.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/glue.png (https://i.ytimg.com/vi/tTqrtzqG-dU/hqdefault.jpg, hq1, hq2, hq3; "Battle Bears Gold- Sanchez Glue Bomb!!", Hammad Shahid, Mar 8, 2014)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/xz_y2.png (xzRwifNTXWU, "Battle Bears Sanchez/Arbiter first try", B-Daman Testing Grounds, Dec 23, 2013)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/early_crops.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/mid_crops.png (Mf-6wj67Trw hqdefault, Apr 20, 2016: cyan flash and a Z, not attributable)
- **Depiction for shorts:** Sanchez lobs a black plated orb with a glowing magenta cross in an arc, and it sticks to the wall or floor with a "thwack" [Observed look; the sound is BBG News invention]. It bursts as a pale-cyan bubble with thin blue rings rippling outward [Observed]. Everyone inside crawls in slow motion under yellow-Z swirls, outlined in purple crackle as on the card [Observed card and icon; the timing is BBG News invention].
- **Confidence:** observed.

## Greased Lightning (primary, unlock; 2.9-era, mid-2014; later REMOVED, removal date undocumented)

- **Official text:** "It's automatic! It's systematic! Hydromatic!? Why it's Greased Lightning!!??" [Game text via wiki] (https://battlebears.fandom.com/wiki/Greased_Lightning). The wiki says the name and description reference the 1978 film Grease [Fan-wiki].
- **Status**
  - 75 Gas, level 1 [Fan-wiki].
  - The class changelog lists it under 2.9; the wiki's 2.9 entry (May 8, 2014) does not. The wiki page was created Jun 7, 2014 [Fan-wiki].
  - SkyVu's Jun 6, 2014 post "Two brand new Sanchez weapons are also now available in the game!" is quoted in prior notes [Canon, Unverified today]. Pairing it with this weapon is [Inference].
  - Launch stats (rev 65732, Jun 29, 2014): damage 5.0, rate of fire 0.1 s, ammo 40, reload 4 s, +10% Speed. Trivia then: "This is the only Arbiter Primary that does not include a slowing effect" [Fan-wiki].
  - Current values from the Mar 4, 2018 "updated stats and trivia" edit: 6.0 damage, 0.13 s, 30 ammo, −5% movement speed [Fan-wiki].
  - "NOTE: THIS WEAPON IS REMOVED!" was added 2020-11-10 by Alphabbr ("added note"). No source or date is given for the removal itself [Fan-wiki; Unverified].
- **Look**
  - A red assault rifle (#9C0001, shadow #620001) with white jagged lightning-bolt decals, a silver ribbed top rail (#90908D / #B8B8B8), a grey underside and muzzle, and a tan block on top at the rear (#C79B75 / #A06E52) [Observed: Greased_Lightning.png].
  - Held two-handed across the chest, muzzle down-right. About 0.45× his height [Inference].
  - HUD icon: a small red rifle [Observed: 5pXfHBEON4M hq2; Yx36xc6nXVk hqdefault].
- **Firing**
  - Automatic [Fan-wiki].
  - The HUD maximum is "22" in two 2016 videos [Observed]:
    - Yx36xc6nXVk hqdefault and hq2: "22 / 22", Jan 12, 2016.
    - 5pXfHBEON4M hqdefault, hq1 and hq3: "0 / 22" (RELOAD); hq2: "22 / 22"; Apr 5, 2016.
  - That matches neither wiki value (40 in 2014, 30 now). An unrecorded balance pass is possible [Inference].
  - **Probable launch footage:** GcPIzMXFYT4 ("BBG: Sanchez's New Weapon!", Hammad Shahid, Jun 6, 2014) shows a HUD icon of a red rifle with a tan top block, matching the render, and counts "17 / 40", "40 / 40" and "0 / 40", matching the launch ammo of 40 [Observed].
    - The player's whole body is rendered blue with white electric swirls, so the class cannot be confirmed from the frame [Observed].
    - That this is Greased Lightning is [Inference].
- **Projectile**
  - Wiki: "fires a red version of the Bind Gun" (Jun 2014); now "fires red-violetish lasers at a rapid rate" [Fan-wiki].
  - **Observed:** a thin, straight pink-magenta laser with a white core, running between Gold Sanchez's side of the frame and an enemy soldier, with a white flare at the soldier's end [5pXfHBEON4M hq1; colour by eye, too thin to sample]. Sanchez's HUD reads "0 / 22 RELOAD". That he fired it is [Inference].
- **Impact / end result:** "dealing damage with no secondary effect, unlike the other Arbiter primaries", and "The weapon has a slight AOE, unfortunately that AOE deals no damage" [Fan-wiki]. The white flare at the target is the only hit look seen [Observed; attribution Inference].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/renders_primary.png (Greased_Lightning.png)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/greased.png (https://i.ytimg.com/vi/5pXfHBEON4M/hqdefault.jpg, hq1, hq2, hq3, "Battle Bears Gold: Sanchez the Arbiter Gameplay with Greased Lightning", PK Deathrow314, Apr 5, 2016; Yx36xc6nXVk hqdefault, hq1, hq2, hq3, Hdjbens, Jan 12, 2016)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/5p_check.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/gc.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/gc_check.png
- **Depiction for shorts:** a red rifle with white lightning decals rattles out rapid, thin pink-magenta lasers with white cores [Observed]. Hits spark and do nothing else [BBG News invention matching the Fan-wiki's "no secondary effect"]. Caption it as a retired weapon.
- **Confidence:** partial.

## Parashoot (primary, unlock, level 20; BBG 2.18, Apr 3, 2015, to present)

- **Official text:** "Make your opponents take cover, IN YOUR PARACHUTE! " [Game text via wiki] (https://battlebears.fandom.com/wiki/Parashoot).
- **Status**
  - Apr 3, 2015 page (rev 70125): 300,000 J, damage 9.0, rate of fire 0.2, ammo 15, reload 4 s, 1,200 u/s. It said "released [...] of v2.17", later corrected to 2.18 [Fan-wiki].
  - 2.20 (May 29, 2015): "Parashoot reduced from 300,000 joules to 200,000 joules" [Fan-wiki: Updates].
  - The class changelog's "2.18 New: Parashoot Primary / 200,000 Joules" shows the post-2.20 price [Inference].
  - Current infobox: 150,000 J, damage 10, 0.1 s, ammo 20, 1.5 s effect, reload 5 s, 1,400 u/s [Fan-wiki].
  - HUD counts [Observed]:
    - "15 / 15" (vcwRC2cQ1ik hq1, Apr 6, 2015)
    - "8 / 15" (vcwRC2cQ1ik maxres)
    - "0 / 15" (5twbNI7iakw hq1 and hq2, Apr 27, 2016)
    - "15 / 15" (5twbNI7iakw hq3)
    - "2 / 15" (kso2WuRLZpo hqdefault, Mar 10, 2018)
    - The 20-round magazine is therefore later than Mar 2018 [Inference].
- **Look**
  - A chunky silver-white launcher (#B4B9BF) with a wide black hexagonal muzzle block, a pale icy-blue translucent side panel (#C2D6DB / #D5EDED), a mauve-violet accent at the rear (#65385C / #9E658B) and a white hooked fin on top [Observed: Para_shoot.jpg].
  - Held at chest height, pointing forward, supported by the prosthetic arm. About 0.45–0.5× his height [Inference].
  - In play it reads as a white-silver gun with a purple glow [Observed]. Holders seen:
    - a dark red-black Sanchez with a yellow helmet chevron (0njNOuanL3E hq1; probably Judge Sanchez [Inference]; not Tron-Tastic!)
    - a dark-navy-armoured Sanchez (5twbNI7iakw hq1 and hq2)
    - Gold Sanchez (kso2WuRLZpo)
  - In the loadout side panel of SpinBabySpin.jpeg (May 2017), the top icon is a silver gun with fins and pink accents [Observed]; probably the Parashoot [Inference].
- **Firing:** "works as a semi-automatic weapon, being able to fire projectiles in quick succession" [Fan-wiki].
- **Projectile**
  - Never clearly seen in flight [Unverified].
  - In the vcwRC2cQ1ik maxres frame, a small black ball with a white rim and pale-cyan streaks sits at the target's hip [Observed]. Reading it as an incoming shot is [Inference].
- **Impact / end result**
  - "When these projectiles make contact with any enemy, they will be opened in a parachute that sticks to the enemy, damaging the enemy and also blocking his/her view" for 1.5 s [Fan-wiki].
  - **Observed** (vcwRC2cQ1ik maxres, "PARACAÍDAS EN LA CABEZA!! (SANCHEZ PARASHOOT)", Chocoindustries®, Apr 6, 2015): an orange-and-blue armoured target with a **large** dark-grey dome (#393C3C, light-grey rim) over its head, about as wide as its upper body. A title overlay partly covers the frame. Reading the dome as the canopy is [Inference], supported by the title ("parachutes on the head").
  - In vcwRC2cQ1ik hq1, a distant target's head is covered by a lumpy lilac-white shape [Observed, low-res; Inference].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/renders_primary.png (Para_shoot.png, SpinBabySpin.png)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/para.png (https://i.ytimg.com/vi/vcwRC2cQ1ik/maxresdefault.jpg, hq1, hq2, hq3; 0njNOuanL3E hq1, hq2, hq3, "Battle Bears Gold | 2.18 Update | NEW WEAPON FOR SANCHEZ | NEW SKIN FOR WIL | GAMEPLAY", SW, Apr 7, 2015; TVbvWO_zZ2c maxres, Sep 28, 2015, a "0 / 2" HUD with no parachute visible; kso2WuRLZpo hqdefault)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/crops/vc_canopy_x4.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/para2.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/para_holders.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/drain.png (5twbNI7iakw frames)
- **Depiction for shorts:** the hex-muzzled silver launcher pops off quick shots [Observed look]. Each hit blooms into a big dark-grey canopy that drops over the victim's head and shoulders, and the victim gropes blindly for a beat [Observed low-res frame plus Fan-wiki effect; the staging is BBG News invention].
- **Confidence:** partial.

## Spin Baby Spin (primary, unlock; BBG 2.27, May 29, 2017, to present)

- **Official text:** "When I spin you spin!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Spin_Baby_Spin). The wiki says it is based on the fidget spinner [Fan-wiki].
- **Status:** launched at 150 Gas, explosives 15–25, ammo 5 (rev 74992, May 29, 2017). Now 60 Gas, explosives 20–35, ammo 6, effect 8 s [Fan-wiki]. It is added in 2.27 alongside Fidget Boomer and Hazard Toy, but is missing from the class changelog [Fan-wiki: Updates].
- **Look**
  - A three-lobed gunmetal fidget spinner. Each lobe is a block with a hole, around a dark glossy domed hub (#2F3739, #242C2E, highlight #4D5757) [Observed: SpinBabySpin.jpeg].
  - Held flat in the prosthetic hand at the waist. About 0.3× his height across [Inference].
  - HUD icon: a dark green-grey spinner silhouette [Observed: RRI-ejnlcww hq3; O60Fq06wfec hq2; eEw00KhDdTw frames].
- **Firing:** "a projectile weapon that explodes on contact"; rate of fire 1 s, 1,300 u/s [Fan-wiki].
  - HUD "4 / 5" (May 30, 2017) and "0 / 5" (Jun 28, 2017) match the launch ammo of 5 [Observed].
  - HUD "1 / 6", "4 / 6" and "2 / 6" (Mar 1, 2022, build label "2.53.6") match the current ammo of 6 [Observed].
- **Projectile:** flight never seen [Unverified].
- **Impact / end result**
  - It "explodes on contact and causes the Reversed Controls effect on any enemies caught in the radius" [Fan-wiki].
  - Status Effects: "a green question mark will appear over the player's head". Controls are inverted, "background music will be disabled and other sounds will feature an mild echo", and "Originally, the aiming camera would also be inverted." [Fan-wiki].
  - **Observed burst, 2017:** green and pale-lime star sparkles with curly lime swirl wisps around a target (RRI-ejnlcww hq3, "Battle Bears Gold: Spin Baby Spin weapon for Sanchez...", SmTony Anthony, May 30, 2017). That target also shows a yellow Z, probably from another slow source such as the uploader's hourglass Special [Inference].
  - **Observed, 2022:**
    - A white blocky puff at a target and a lime-green "?" beside a pink Huggable (eEw00KhDdTw hqdefault and hq2, "New favorite Sanchez loadout (battle bears)", foodood, Mar 1, 2022).
    - A big lime-green burst at a target ("SHAMAR"), with a dark-green spiral swirl on the wall beside it, while the HUD shows the spinner at "2 / 6" (hq3). That this is the Spin Baby Spin blast is [Inference].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/renders_primary.png (SpinBabySpin.png)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/eew_all.png (eEw00KhDdTw hqdefault, hq2; https://i.ytimg.com/vi/RRI-ejnlcww/hq3.jpg; O60Fq06wfec hq2, "BattleBearsGold 2.27 S3 Ep97: Spin Baby Spin Gameplay...", Jun 28, 2017)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/eew_hud.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/crops/eew_hq3_x3.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/mid_crops.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/versions.png
  - G1y7NuT10v4 hq1 (Sep 22, 2018) is only a title card [Observed: sheets/mid.png in the same folder].
- **Depiction for shorts:** Sanchez flicks the gunmetal spinner, which whirs flat through the air [BBG News invention]. It bursts into lime star sparkles and curly swirls [Observed]. Victims sprout a lime-green "?" and stumble the wrong way while the music cuts out [Fan-wiki effect]. Avoid real toy branding.
- **Confidence:** partial.

## Kelowna (primary, unlock; BBG 2.31, Mar 8, 2018, to present)

- **Official text**
  - None for the item. "This is the only Arbiter primary to lack a description" [Fan-wiki].
  - SkyVu's channel "BATTLE BEARS" (@battlebears) streamed "SkyVuBen rocks New Kelowna Weapon!" ("Streamed live on Mar 9, 2018"), described "Battle Bears Gold Weekly Meetup 3-9-18" [Canon: official video title and description] (https://www.youtube.com/watch?v=0i1NRO9OS2k).
- **Status:** launched at 500,000 J; damage 4.0/s for 2 s; rate of fire 0.25 s; ammo 20; reload 3 s (rev 75737, Mar 11, 2018). Now 150,000 J, 8.0/s for 2 s, 0.75 s, ammo 10, reload 4 s; 800 u/s throughout [Fan-wiki].
  - "The weapon is named after the city that Screenzilla resides in." [Fan-wiki]
  - It is missing from the class changelog [Fan-wiki].
- **Look**
  - A dark gunmetal blaster [Observed: Kelowna.jpeg] with:
    - a glowing violet liquid canister slung underneath (#3A0DBB, #AE9AF5, white-violet #E8E2FD)
    - a top scope with a glowing violet lens
    - a spiky white-lavender crystal shell around the front (#D0CDE7, #F7F5FD, shade #7F7B9D)
    - a white ring muzzle
  - About 0.45× his height [Inference].
  - The render's skin is **Judge Sanchez** [Observed: compared with File:Judge_Sanchez.png].
  - In SkyVu's stream thumbnails [Observed: 0i1NRO9OS2k hqdefault, hq1, hq2, hq3, maxres]:
    - Tron-Tastic! (red-orange lines) and Gold Sanchez hold it.
    - The HUD reads "20 / 20" and "8 / 20".
    - The loadout screen shows the version "2.31".
- **Firing:** the HUD's 20 matches the launch ammo [Observed]. "fires a small projectile that explodes once it comes in contact with a surface" [Fan-wiki]. Flight never seen [Unverified].
- **Impact / end result**
  - Wiki: "it will produce a clone of Arbiter doing the Creepin taunt among clouds of poison". Enemies are Poisoned, "a purple/green skull" overhead (Status Effects) or "a small purple skull over their head" (rev 75737). "the user is also susceptible to the poison" [Fan-wiki].
  - Creepin, per the wiki's Taunts page: "The Arbiter starts staggering like a zombie, similar to the zombies in Michael Jackson's Thriller." [Fan-wiki].
  - Trivia: "When someone is killed by this, it plays Thriller by Michael Jackson. The dance the Sanchez does is unrelated to the Thriller choreography." [Fan-wiki]
  - **Observed:** translucent purple puffs (#86579B, #8C56AE, light #B48CC1) drifting in the air. Several are shaped like cartoon skulls with white eye and nose holes, among white translucent puffs, on a white-washed frame [0i1NRO9OS2k hq2, official SkyVu stream].
  - **Observed:** dense swarms of small purple-violet puffs over a carnival floor and ramp [kwtuHF2SQHo hqdefault, hq2, hq3, "kelowna new battle bears gold weapon demonstration and gameplay", SSP_Rism, Mar 9, 2018; HUD "3 / 20", "12 / 20", "20 / 20"].
  - The Sanchez clone is not visible in any frame [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/renders_primary.png (Kelowna.png)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/judge.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/kel.png (https://i.ytimg.com/vi/0i1NRO9OS2k/hqdefault.jpg, hq1, hq2, hq3, maxresdefault; kwtuHF2SQHo hqdefault, hq1, hq2, hq3)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/crops/kel_hq2_x3.png
- **Depiction for shorts:** the crystal-nosed blaster plinks a violet pellet that pops into a drifting cloud of purple skull-shaped puffs [Observed]. A see-through Sanchez double shuffles zombie-style inside it [BBG News invention from the Fan-wiki clone]. Victims get a small purple skull overhead [Fan-wiki]. Use original spooky music only: no Thriller audio and no copied choreography.
- **Confidence:** partial.

## Speed Field (secondary, default; BBG 2.6, Dec 20, 2013, to present)

- **Official text**
  - "Gotta go fast! Any player who enters the field gets their speed doubled!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Speed_Field).
  - Card: "SPEED FIELD / Creates Dome-like Structure", with a "NORMAL | FAST | NORMAL" diagram [Observed].
  - battlebears.com, about the other game's Super: "His Super, "Speed Field," creates an area that significantly boosts his and his allies' movement speed, whilst causing chaos to groups of enemies." [Canon; game unnamed on the page; BBH is Inference].
- **Look**
  - Card icon: a glossy yellow sphere (#F4E40D, #D6CB5A, shade #89812D) engraved with a hexagon/honeycomb pattern [Observed].
  - No held prop. The render on the Speed and Cloak Field pages (File:Arbiter.jpg) shows Sanchez empty-handed with the red forearm lamp lit [Observed].
  - The Dec 21, 2013 Speed Field revision (58374) says: "The Arbiter does not appear to be holding the orb. It also applies to his Cloak Field, which also does not show up in his hands. This may be a visual glitch in the game." [Fan-wiki]. The Cloak Field rev 58375 says the same about the Speed Field.
  - The infobox wrongly gives "Type: Primary" [Fan-wiki error].
- **Firing**
  - Current text: "the Arbiter will produce a hazy, light yellow orb, which appears from a command gauntlet on his arm. This procedure will work in mid-air, but has greater effect if placed on the ground." and "To activate it, Sanchez hits a button on his arm. It has 2 ammo." [Fan-wiki]. The gauntlet and button wording first appears Dec 24, 2013 (rev 58841).
  - Dec 21, 2013 text (rev 58374): "the Arbiter will place down a bright yellow orb with a hazy texture on the ground. It cannot be used in mid-air, however." [Fan-wiki]. This contradicts the current mid-air line.
  - Lasts 8 s, reload 1.5 s, +1% Speed passive [Fan-wiki].
- **Projectile:** none; it is a deployed dome [Fan-wiki].
- **Impact / end result**
  - "The field created is a dome similar in size to the Pain Field or Cloak Field but with a somewhat translucent light yellow haze to it. Any player, even an opponent, that steps into the field will have their speed increased by 150 u/s as long as they are in the field." [Fan-wiki]. Sanchez's base speed is 275 [Fan-wiki: class page].
  - Dec 2013 version: "a somewhat translucent bright yellow glaze", speed "doubled" [Fan-wiki rev 58374].
  - Card diagram: a thick yellow arch labelled FAST over a running stick figure with speed lines, NORMAL on either side [Observed; the textless card shows only FAST].
  - **Fan frame:** a yellow glow around a figure and a bright yellow glow band on the floor ahead [Observed: 5gKnLQX1sUc hq2, "BOOM!!! SANCHEZ IS FASTER THAN YOU! - Battle Bears Gold 2.28", SW, Jan 21, 2018]. That this is the Speed Field is [Inference].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/png/Sanchez_weapons.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/png/Arbiter_sanchez.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/renders_sec_melee.png (Arbiter_jpg.png)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/speed.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/crops/5gk_x3.png
- **Depiction for shorts:** a yellow honeycomb orb blooms out of Sanchez's arm into a translucent yellow dome [Fan-wiki and card; the staging is BBG News invention]. Anyone who crosses the edge, friend or foe, blurs forward with cartoon speed lines [Game text via wiki; Fan-wiki].
- **Confidence:** partial.

## Cloak Field (secondary, unlock; BBG 2.6, Dec 20, 2013, to present)

- **Official text:** "Sanchez is really good at hide and seek. Any player who enters the field gains cloaking!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Cloak_Field). Card: "Cloak Field / Creates Dome-like Structure" [Observed].
- **Status:** 80 Gas at launch and in the page body; the infobox says 60 Gas and wrongly gives "Type: Primary" [Fan-wiki conflict and error].
- **Look:** card icon is a glossy purple sphere (#7D39C1, #A878CF, highlight #FBEEFD) wrapped in white circuit-like bands [Observed]. No held prop [Observed: Arbiter.jpg; Fan-wiki rev 58375].
- **Firing**
  - Current: "a hazy, light purple orb, which appears from a command gauntlet on his arm. This procedure will not work if used in mid-air" [Fan-wiki].
  - Dec 21, 2013 (rev 58375): "the Arbiter will place down a hazy light purple orb down on the ground" [Fan-wiki].
  - Ammo 2, reload 4 s, lasts 15 s, visibility 0% [Fan-wiki].
- **Projectile:** none [Fan-wiki].
- **Impact / end result**
  - "a dome similar in size to the Pain Field or Speed Field and has a somewhat translucent light purple haze". Anyone, enemies included, who "stays there for 0.75 seconds will be given automatic cloaking for the duration of the field. If a player attacks, they will reveal themselves until they stop attacking." [Fan-wiki]
  - Dec 2013 addition: "The player will then quickly fade back into a cloaked state." [Fan-wiki rev 58375]
  - Trivia: "the first weapon to make you 100% invisible while moving as long as you remain in the field" [Fan-wiki].
  - Card diagram: a stick figure with a gun behind a purple glowing arch, dash lines beyond the arch, and a second gun-holding figure outside [Observed].
  - No in-game image of the dome or of a cloaked player was found [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/png/Sanchez_weapons.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/png/Arbiter_sanchez.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/renders_sec_melee.png
- **Depiction for shorts:** a purple circuit orb unfolds into a faint violet dome [Fan-wiki and card]. Characters who linger inside fade to nothing and flicker back whenever they fire, then fade out again [Fan-wiki behaviour; the shimmer look is BBG News invention].
- **Confidence:** documented.

## Invulnerable Field (secondary, unlock; changelog says 2.9, page created Jun 7, 2014; to present)

- **Official text:** "With great power comes great invulnerability" [Game text via wiki] (https://battlebears.fandom.com/wiki/Invulnerable_Field).
- **Status**
  - The class changelog lists it under 2.9 at 1,000,000 J. 2.20 (May 29, 2015): "Invulnerable Field reduced from 1,000,000 joules to 250,000 joules". The infobox now says 150,000 J [Fan-wiki].
  - Rebalanced: duration 10 s → 4 s, rate of fire 0.75 s → 1.5 s, reload 7.5 s → 5 s [Fan-wiki rev 64941, Jun 9, 2014, vs current].
  - Pairing it with SkyVu's "Two brand new Sanchez weapons" post is [Inference].
- **Look:** no prop. The render shows him empty-handed with the red forearm lamp lit, identical to the Speed and Cloak Field render [Observed: 480px-InvulnerableField.jpg, fan upload 2014-06-08].
- **Firing:** "a hazy, light blue orb, which appears from a command gauntlet on his arm"; grounded only; ammo 2 [Fan-wiki].
- **Projectile:** none [Fan-wiki].
- **Impact / end result**
  - A dome "similar in size to the Pain Field or Speed Field". "Any player that steps into the field takes 50% less damage", stacking as "0.5^(Number of Field)" [Fan-wiki].
  - "No overhead icon shown" [Fan-wiki: Status Effects].
  - Trivia: "it only reduces damage and does not protect players to the point of actual invulnerability" [Fan-wiki].
  - No dome colour is given beyond the "light blue" orb, and no in-game image was found [Unverified].
- **Images viewed:** /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/renders_sec_melee.png (480px-InvulnerableField.png)
- **Depiction for shorts:** a pale-blue translucent dome; bullets landing inside throw half-size, dulled sparks, and no icon appears over anyone [BBG News invention built on the Fan-wiki]. Show it as damage reduction, not invincibility.
- **Confidence:** documented.

## Carpet Bomb (secondary, unlock, level 10; BBG 2.15, Dec 20, 2014, to present)

- **Official text:** "This carpet has been through years of training to prepare for war!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Carpet_Bomb).
- **Status**
  - **Slot:** secondary. The Dec 20, 2014 revision (68521) said "Primary - Explosives" and "is a primary weapon". On Jan 7, 2015 the same editor changed the text, commenting "I corrected the mistake that the carpet bomb was a primary" (rev 68678) [Fan-wiki history]. The Updates entry and the class changelog say secondary [Fan-wiki].
  - Price: 275,000 J (Dec 2014 page), 250,000 J (changelog), 150,000 J (current infobox) [Fan-wiki].
  - Stats: Dec 2014: explosives 30–45, rate of fire 2.8 s, ammo 2, reload 4.6 s, 950 u/s. Mar 2018: 10–20, 1.5 s, ammo 2, reload 3 s, 800 u/s. Now: 7.5–15, 1 s, ammo 3, reload 3 s, 600 u/s [Fan-wiki revs 68521, 75722, current].
  - HUD "1 / 2" in Dec 20, 2014 (8gT_b3QGBgg hq1, hq2), Jan 12, 2016 (Yx36xc6nXVk hq1) and Jul 2016 (Death_by_Carpet.png) frames [Observed]. That matches the 2-round magazine.
- **Look**
  - A rolled rug: black (#060303) with tan-brown key and knotwork borders (#8A6F52, #604C32, dark #331B11) [Observed: Carpetbomb.jpg].
  - **One end is a black cap with two white cartoon eyes and a grey screw-like fuse spike; the carpet has a face** [Observed: Death_by_Carpet.png crop; 8gT_b3QGBgg hq1].
  - Carried diagonally across the chest, or upright in the right hand. About 0.6× his height long [Inference].
- **Firing:** "When launched, the Carpet Bomb will fly in an arc, and it will stop once it reaches an object, a solid base or a player, even a teammate." [Fan-wiki]
- **Projectile:** the rolled carpet itself [Observed: Yx36xc6nXVk hq1]. That frame shows, inside a big yellow-orange fireball:
  - a patterned roll with an eyed black cap and fuse near Tron-Tastic! Sanchez's cyan-lined arm
  - a plain brown rod mid-air
  - a second roll with a fuse beside the enemy "OWURA.KWAKU"
- **Impact / end result**
  - "When it stops, the carpet will be opened and fire starts to burst around it [...] It does 3 rapid explosions, before stopping." Its AoE is large enough that "the player can easily commit suicide" [Fan-wiki].
  - **Observed:** a large fireball with a white core (#FFFFFE), pale yellow (#FEFE8F) and tan (#D4B26F), billowing white smoke and an orange ring on the grass, engulfing a pink Huggable [Death_by_Carpet.png, fan screenshot uploaded 2016-07-26].
  - Neither the unrolled carpet nor the triple-burst rhythm was seen [Unverified].
  - The wiki's demo video file (YouTube I7I02IwJIec) has no thumbnails left (HTTP 404).
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/renders_sec_melee.png (Carpetbomb.png)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/inplay_wiki.png (Death_by_Carpet.png)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/gbw_carpet.png (carpet face crop)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/crops/yx_hq1_x3.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/crops/8gt_hq1_x3.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/carpet_stealth.png (https://i.ytimg.com/vi/8gT_b3QGBgg/hqdefault.jpg, hq1, hq2, hq3, "Battle Bears Gold | SANCHEZ' CARPET BOMB | 2.15 UPDATE | GAMEPLAY", SW, Dec 20, 2014; vdSoyNEWq6A maxres, Chocoindustries®, Apr 15, 2015)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/mid.png (Wfy_1E0CZBE hq2)
- **Depiction for shorts:** Sanchez hurls the googly-eyed rolled rug end over end [Observed look]. It thumps down, flops open, and three quick fire-puffs ripple across it into a white-and-yellow fireball with an orange ground ring [Fan-wiki sequence plus Observed fireball]. Victims tumble out sooty and sparking [BBG News invention].
- **Confidence:** observed.

## Drain Field (secondary, unlock, level 20; BBG 2.16, Jan 30, 2015, to present)

- **Official text:** "Toss this sucker at the nearest enemy and watch as his life force is drained from him and transferred to you!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Drain_Field).
- **Status:** 55 Gas. Rebalanced from 35/s damage and 20 healing per 1.5 s (rev 69349, Feb 16, 2015) to 25/s and 25 per 1 s. Ammo 1, reload 4.5 s, 800 u/s [Fan-wiki].
- **Look**
  - Held: an orange-brown curved slug or leech (#793A24, #B56F46, deep #621D0E) with a dark slit marking, in the prosthetic hand. About 0.3× his height [Observed: Drainfield.jpg; size Inference].
  - The wiki called it "the fish-like creature that holds in it's hand" in Feb 2015 and calls it "the leech-like creature" now [Fan-wiki].
  - **Concept art:** File:Drainfield.png, uploaded 2015-02-16 by a fan editor with the comment "This is concept art for the drain field". It is hand-lettered "Sanchez drain field". SkyVu provenance is [Unverified]. It shows [Observed]:
    - a red, drop-shaped creature with a hooked tip and a dark band with one eye across its face, wrapped in white wind rings with up-arrows, beside small black bear silhouettes with guns
    - a grey dome with a cross emblem and a syringe
    - a dripping syringe
    - four health crosses being drained
  - Only the creature is coloured. The syringes, dome and crosses are greyscale, so there is no "red liquid" (pixel check).
- **Firing:** "the Arbiter will toss the leech-like creature that flies in an arc" [Fan-wiki]. HUD "1 / 1" [Observed: xAp9gFMriAU hq2 and hq3].
- **Projectile:** the leech creature [Fan-wiki]; not seen in flight [Unverified].
  - A brown, open-mouthed creature with red eyes, white fangs and a black-and-white dotted stripe appears next to Sanchez in 5twbNI7iakw hq3 [Observed]. With a Parashoot HUD showing, it cannot be attributed [Unverified].
- **Impact / end result**
  - Wiki: "When it makes contact with any solid surface, a dark field will be formed with bats in it. Any opponent that is in its range will take damage, and their lost health will be transferred to the user. The user will not receive overheal".
  - Trivia: "the other fields are formed around the user while the Drain Field won't" and "The field formed appears to be a projection of a live creature wearing sunglasses." [Fan-wiki]
  - **Observed (Apr 27, 2016):** a giant translucent **red** creature projection (#A22F1F, #A43B27) filling the view, with a ring of white triangular fangs around a huge mouth, a pink glow inside and dark bars across the top [5twbNI7iakw maxres, "BLINDNESS OF DRAINING ENERGY(DRAIN FIELD & PARASHOOT SANCHEZ GAMEPLAY)", SW].
  - **Observed (Mar 24, 2016):** the same red creature (shadowed #642D21, lips #7A0C08) **wearing dark-grey sunglasses (#49454D) with white glints**, a wide mouth lined with white triangular teeth, and **small black bats with glowing red eyes** flying in front of it [xAp9gFMriAU hq1, "THE LIFE STEALER(SANCHEZ DRAIN FIELD GAMEPLAY)", SW]. That frame's HUD shows the Bind Gun at "35 / 40" and a Slowed target, so the field and the beam are on screen together.
  - The wiki's "sunglasses" and "bats" are confirmed. Its "dark field" is not: the field is red [Observed vs Fan-wiki].
  - The concept art's dark eye band matches the in-game sunglasses [Inference].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/renders_sec_melee.png (Drainfield_jpg.png)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/inplay_wiki.png (Drainfield_png.png)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/drain.png (https://i.ytimg.com/vi/5twbNI7iakw/maxresdefault.jpg, hq1, hq2, hq3; https://i.ytimg.com/vi/xAp9gFMriAU/maxresdefault.jpg, hq1, hq2, hq3)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/drain_crops.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/crops/xap_glasses_x4.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/crops/xap_bats_x5.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/bats.png
- **Depiction for shorts:** Sanchez lobs the sleepy-looking orange leech. Where it lands, a huge see-through red ghost-creature in dark sunglasses balloons up with a ring of white teeth, while little black bats with red eyes flutter around it [Observed]. Ribbons of red-pink sparkle (never blood) stream from victims to Sanchez, who glows contentedly [BBG News invention].
- **Confidence:** observed (field look); partial (throw and drain visuals).

## Blade Augment (melee, default; BBG 2.6, Dec 20, 2013, to present)

- **Official text:** "Sanchez did not ask for this, but he still thinks it is really really cool." [Game text via wiki] (https://battlebears.fandom.com/wiki/Blade_Augment). Card: "Blade Augment / Attaches to Arm" [Observed].
- **Look**
  - "It appears as a blade attached to Sanchez's arm by a metal rod." [Fan-wiki]
  - **Observed:** a long, gently curved, single-edged silver blade (edge #BCBCC0 / #A5A5AB) with a dark jagged zigzag temper line, mounted under the red-black prosthetic forearm [Blade_Augment.png].
  - It reaches far past the fist toward the opposite foot: about 0.6× his height, so **not short** [Inference from render].
  - Card icon: the long blade on a dark red-black gauntlet with a glowing red lamp [Observed].
- **Firing:** melee swing, 110 damage, no stat modifier; Melee+1/+2 add +10/+20 [Fan-wiki].
- **Projectile:** none.
- **Impact / end result**
  - Card diagram: a stick figure slashes a curved blade, then a second stick figure runs. The swoosh trails differ between the two card files [Observed]:
    - **grey** (#6F6F6F–#9A9A9A) on the captioned card, Sanchez_weapons.jpg (uploaded 2013-12-20)
    - **red/pink** (#BE706B, #DB9F9A) on the textless card, Arbiter_sanchez.jpg (uploaded 2013-12-18)
  - The in-game hit was not seen [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/png/Sanchez_weapons.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/png/Arbiter_sanchez.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/bd_compare.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/renders_sec_melee.png (Blade_Augment.png)
- **Depiction for shorts:** one wide, theatrical arm-blade sweep with a swoosh trail, either grey or red like the two card versions [Observed card styles]. The hit lands as white sparks and a clank [BBG News invention]. Show the blade only when the melee is out; the gun renders show no blade.
- **Confidence:** partial.

## Harvester (melee, unlock; BBG 2.6, Dec 20, 2013, to present)

- **Official text:** "It is Harvest time!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Harvester). Card: "HARVESTER / Similar to Clover Claws" [Observed].
- **Status:** 120 Gas at launch [Fan-wiki: 2.6 page; rev 59126]. The current page says "It costs 20 Gas", probably a typo [Fan-wiki; Inference]. Damage went from 65 to 70, and Melee+ from +5/+10 to +10/+20 [Fan-wiki revs].
- **Look**
  - "a gauntlet with three metallic claws protruding outwards" [Fan-wiki].
  - **Observed:** a dark gunmetal gauntlet (#565155, #363136) over the prosthetic fist, with a round glowing yellow lens on top (#DBCE25). Three long, curved, polished silver claws (#E1E1E4, #B6B5B9, #89898B) jut forward from the knuckles [Harvester.jpg and card].
  - About 0.3× his height [Inference].
  - The wiki compares it to the Shock N Claw and to Shredder's claws [Fan-wiki].
- **Firing:** "used in a swinging motion"; 70 damage, +10% speed [Fan-wiki].
- **Projectile:** none.
- **Impact / end result:** the card diagram shows three red jagged slash marks outlined in yellow [Observed, both cards]. The in-game hit was not seen [Unverified].
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/png/Sanchez_weapons.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/png/Arbiter_sanchez.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/renders_sec_melee.png (Harvester.png)
- **Depiction for shorts:** a three-claw swipe that leaves three red-and-yellow jagged slash streaks hanging in the air, like the card [Observed card]. Victims spark and stagger [BBG News invention].
- **Confidence:** partial.

## Stealth Knife (melee, unlock; BBG 2.21, Jul 3, 2015, to present)

- **Official text:** "Salvaged from a stealth bomber, this melee weapon can sometimes strike without even being seen!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Stealth_Knife). The wiki ties the description to "the Pelican't which Sanchez crashed in Battle Bears: Zombies" [Fan-wiki].
- **Status**
  - Jul 2, 2015 (rev 71369): 85 damage, −10% health, "+10% special speed", 75 Gas.
  - Jul 3, 2015 (rev 71411): 85 damage, −15% Health, +15% Movement Speed, 75 Gas.
  - Jul 23, 2015 (rev 71515): 400,000 J. The class changelog also says 400,000 J.
  - Now: 70 damage, −10% Health, +20% Movement Speed, 150,000 J [Fan-wiki].
- **Look**
  - A dark navy/indigo faceted blade-gauntlet shaped like a stealth bomber (#0F0C29, #1B172F, #222142), with chevron fins and glowing cyan edge lines. A translucent cyan energy blade (#1AFCF9, #39FEFE) extends from it [Observed: Image51.PNG, fan upload 2015-07-05].
  - The render's skin is Judge Sanchez [Observed].
  - In play, Tron-Tastic! Sanchez (red-orange lines) holds the same dark angular blade with a cyan energy edge [Observed: IAGq4yS4ggo maxres, "STEALTH KILLS DE SANCHEZ | 2.21 | Battle Bears Gold", SW, Jul 22, 2015].
  - About 0.35–0.4× his height [Inference].
- **Firing:** melee [Fan-wiki].
- **Projectile:** none.
- **Impact / end result:** no mechanic is documented for "strike without even being seen" [Unverified]. The hit look was not seen [Unverified].
  - iTJ94TmSrGk maxres ("Battle Bears Gold: 2.21 UPDATE REVIEW", SW, Jul 2, 2015) shows fan-made promo art of a red-helmeted bear holding a cyan crystal blade. It matches no Sanchez skin render I opened (it is not Bear of Rhodes), so I don't attribute it.
- **Images viewed:**
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/renders_sec_melee.png (crops/image51_x3.png from Image51.png)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/crops/iag_max.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/crops/iag_blade.png
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/carpet_stealth.png (https://i.ytimg.com/vi/IAGq4yS4ggo/maxresdefault.jpg, hq1, hq2; iTJ94TmSrGk maxres)
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-verify/sheets/skins.png
- **Depiction for shorts:** the dark bomber-shaped blade blinks out of sight mid-swing, leaving only a cyan streak, and the victim never sees it coming [BBG News invention from the official description].
- **Confidence:** partial.

---

## Corrections for the character file

File: /home/user/thallo-site/bbg-news-repo/characters/sanchez.md. Flagged only; I did not edit it.

1. **"arm #A3141E / #1B1A1C, Bind Gun #1E6FD9."**
   - Correction: the Bind Gun is cyan/teal. 3D render: #468FAB / #3C7089, highlights #6CBCD0, panel lines #1A465F, muzzle glow #E9F0F6. The card is brighter (#1A9BD5, highlight #3BC8F2).
   - #1E6FD9 is closest to the 2D promo art (about #146399–#2673A8) but more saturated than any source.
   - Evidence [Observed]: Bind_Gun.png, Sanchez_weapons.png and Arbiter_Class.png, sampled today.
2. **"glossy blue Bind Gun"**
   - Correction: "glossy cyan Bind Gun". In 2013–2016 footage it fires a wavering, crackling hot-pink beam, and hits show a white-pink starburst plus the yellow-Z Slowed icon [Observed]. GoF3Hy4QQis hq1 and hq3, Y2IbsH718QA hq3, xAp9gFMriAU hq1.
3. **"yellow Speed Field, purple Cloak Field and dark purple Glue Bomb orbs [Observed] ([card][card])."**
   - Correction: the Glue Bomb is a black/gunmetal plated sphere with a glowing violet (card #481E89) to hot-magenta (3D #F423F3) cross.
   - The Speed Field orb is glossy yellow with a honeycomb pattern. The Cloak Field orb is purple with white circuit bands.
4. **"Fields come from "a command gauntlet on his arm" [Fan-wiki] ([Speed Field][speed])."**
   - Narrow it. The Speed, Cloak and Invulnerable Field pages say the orb "appears from a command gauntlet on his arm" [Fan-wiki]. The Drain Field is tossed in an arc and forms where it lands [Fan-wiki].
   - The field renders show empty hands and a lit red forearm lamp [Observed]; no activation has been observed.
5. **"fields fire from a button on his arm [Fan-wiki] ([Speed Field][speed])."**
   - Correction: only the Speed Field page says "To activate it, Sanchez hits a button on his arm" [Fan-wiki]. The Drain Field is thrown and the Carpet Bomb is a lobbed explosive.
6. **Prompt pack: "with glowing red light strips and a short forearm blade; left arm normal size. Holds a large glossy blue sci-fi gun (#1E6FD9)."**
   - Correction: remove the "short forearm blade" from gun poses; no gun render shows a blade. When the Blade Augment is equipped, it is long (about 0.6× his height), curved, single-edged silver with a dark zigzag temper line.
   - Gun: a chunky glossy cyan faceted blaster (#468FAB, highlights #6CBCD0, dark #1A465F) with a round glowing white muzzle, held across the chest or hip.
7. **"Bind Gun or Adrenaline Gun in 2026, and which skins and taunts survive; the demo and [playtest showcase][showcase] are unviewed."**
   - Update: the showcase's "47:23 Arbiter (Sanchez)" chapter thumbnail shows a 2026 playtest loadout with skin "TRON-TASTIC!" and the same cyan default gun model [Observed].
   - A Sep 20, 2026 playtest thumbnail (JVEQQqyafzE) shows a magenta beam and the yellow-Z Slowed icon, so slowing exists in 2026; the shooter is unseen.
   - The gun's 2026 name and effect, and the videos themselves, remain unviewed and unverified.
8. **"BBH has an "Adrenaline Gun" [Canon] ([characters][chars])"**
   - Correction: the battlebears.com/pages/characters text is [Canon], but the page names no game (zero mentions of "Heroes" or "Gold"). That it describes BBH is [Inference].

## Open questions

See the open_questions field.
