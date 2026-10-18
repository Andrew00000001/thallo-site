<!-- gap pass 1 -->
# Sanchez: Greased Lightning addendum (hit look and "REMOVED" status)

This addendum covers one gap: the hit look of Sanchez's (Arbiter) Greased Lightning, which the verified dossier marked as unobserved, plus what the four uncited videos say about its "REMOVED" status. Everything else about Sanchez stands as written in `research_notes/BBG weapons (verified)/sanchez.md`.

**What I could reach today**
- **YouTube stills.** Every video in the gap, plus six more Greased Lightning uploads the search turned up, returned its still thumbnails from i.ytimg.com (sddefault, sd1–sd3, hq1–hq3, maxres/hq720 where they exist).
- **YouTube metadata.** I got titles and channels through oEmbed, and exact upload dates, descriptions and comments through the youtubei `next` endpoint. Files: `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/sanchez-gaps/next/` and `.../sanchez-gaps/meta/`.
- **Fan-wiki API.** I pulled the Greased Lightning page and all 22 of its revisions, plus Caffeine Injection, Fidget Boomer, Battle Bears Gold/Versions, Updates, Arbiter (BBG) and Weapon Statistics. Files: `.../sanchez-gaps/wiki/`.

**What I could not reach**
- **web.archive.org.** The proxy logs "ws_closed_mid_exchange" on every try, the availability API eventually returned HTTP 429, and WebFetch refuses the domain. SkyVu's Jun 2014 post "tillman-overhaul-new-sanchez-weapons-in-bbg" therefore stays unread. The availability API now reports snapshots 20140617141419 and 20141022042112 for it; prior notes said it had none.
- **Everyplay originals.** The availability API has no snapshot of the Everyplay pages behind these uploads (6144234, 9878511, 9907890).

**How to read the evidence**
- **I watched no video.** Every [Observed] tag below means a still I opened. sd1/sd2/sd3 (and hq1–hq3) are YouTube's automatic frames from about 25%, 50% and 75% of the runtime [Inference], so the timestamps below are approximate. sddefault and maxres are usually the middle frame, or a custom image where noted.
- **Hex values** are medians of small crops of compressed stills [Observed, approximate].

**Videos used**

| ID | Uploader, title | Upload date | Length | Role here |
|---|---|---|---|---|
| 6L9-oeL-x1o | HellNaw, "Greased Lightning Gameplay(BBG)" | Jun 25, 2014 | 4:17 | gap item; launch era |
| AVVg-fk_RnE | GoogleMyFist, "Sanchez New Weapons- Greesed Lightning" | Sep 18, 2014 | 4:13 | extra; pre-rework |
| smplbld5gfo | LXSXL, "This is the new Greased Lightning? Unnacceptable." | Oct 1, 2014 | 4:22 | gap item; rework |
| Zw7Vvc-VSCI | LXSXL, "There Are Times I'm Stuck Playing Defense" | Oct 7, 2014 | 4:25 | extra; HUD check |
| A7VWjfGET1A | Benedict Siow, "Battle Bears Gold Greased Ligtning" | Mar 12, 2015 | 4:31 | extra; menu model and hit |
| TwhAqkhrHwI | SW, "TORMENTA ELÉCTRICA(GREASE LIGHTNING GAMEPLAY) \| 2.21 \| Battle Bears Gold" | Jul 30, 2015 | 4:43 | extra; **best hit frame** |
| 69RebIRIheg | SW, "WHACKY SET #9 Sanchez Gameplay - Battle Bears Gold 2.23" | Dec 29, 2015 | 4:25 | extra; ammo math |
| 4D5s8lSclTM | SW, "MEGA OPTIONAL ELECTRIC STORM!!(SANCHEZ GREASE LIGHTNING GAMEPLAY)- Battle Bears Gold 2.25" | Jul 15, 2016 | 4:33 | extra; hit frame |
| pkfymcukjbY | foodood, "Greased lightning returns (battle bears)" | Jun 26, 2023 | 4:16 | gap item; 2023 status |
| 1ro5_csFNHQ | Splxsh Clpxz, "Battle Bears Gold Greased Lightning" | Jul 20, 2023 | 4:06 | gap item; 2023 status |

---

## Greased Lightning (primary, automatic; unlock, 75 Gas; added Jun 2014; reworked about Oct 1–2, 2014; wiki "REMOVED" note Nov 10, 2020; seen in live matches on build "2.53.6" in Jun–Jul 2023; 2026 unverified)

- **Official text:** "It's automatic! It's systematic! Hydromatic!? Why it's Greased Lightning!!??" [Game text via wiki] (https://battlebears.fandom.com/wiki/Greased_Lightning). No SkyVu text I could read describes how it fires or what a hit looks like. The Jun 2014 SkyVu post is unread [Unverified].

- **Status / era (new findings)**
  - **Launch era.** The HellNaw HUD (Jun 25, 2014) reads "50 / 50" beside the red-rifle icon [Observed: https://i.ytimg.com/vi/6L9-oeL-x1o/sddefault.jpg]. GoogleMyFist's HUD (Sep 18 upload) reads "0 / 50 RELOAD" [Observed: AVVg-fk_RnE sddefault, sd1, sd3]. Both fit the wiki's launch ammo of 40 plus Ammo +2 (+10) [Fan-wiki; Inference].
  - **The Oct 2014 rework, which the verified dossier missed.**
    - LXSXL uploaded "This is the new Greased Lightning? Unnacceptable." on Oct 1, 2014. Its HUD shows the red-rifle icon at "12 / 12" [Observed: smplbld5gfo sddefault and sd2, about 2:11].
    - A commenter (@Rico19998, "12 years ago") wrote: "Ik i just used it to they could have atleast increased the reload speed" [Unverified, fan comment].
    - Wiki rev 67757 (Clinkzbone, 2014-10-02 12:19 UTC) changed damage from 5.0 to 7.0, rate of fire from 0.1 s to 0.04 s and ammo from 40 to 14. Rev 68011 (2014-11-01) set ammo to 17 and the modifier to "−5% movement speed" (it was +10%) [Fan-wiki].
    - The wiki dates 2.12 to "October 2nd, 2014" [Fan-wiki: Battle Bears Gold/Versions], so the rework probably shipped with 2.12 [Inference].
    - A 2017 trivia edit says: "This weapon underwent a rebalance and since then has the fastest RoF of any weapon in Battle Bears Gold, a title that was previously held by Orbs" [Fan-wiki, rev 75027].
  - **Ammo math (fixes the dossier's "matches neither wiki value").**
    - Every HUD maximum after the rework is 12, 17 or 22 [Observed]:
      - 12: smplbld5gfo, Oct 1, 2014.
      - 22: Zw7Vvc-VSCI sd1 "13 / 22", Oct 7, 2014; TwhAqkhrHwI sd2 "20 / 22" and sd3 "2 / 22", 2015; 69RebIRIheg "0 / 22"; 4D5s8lSclTM "22 / 22" and "0 / 22"; 1ro5_csFNHQ "22 / 22" and "0 / 22", 2023.
      - 17: A7VWjfGET1A sd3 "17 / 17", 2015; pkfymcukjbY "0 / 17", 2023.
    - With the wiki's equipment table (Ammo +1 = +5, Ammo +2 = +10) [Fan-wiki], these are 12, 12 + 5 and 12 + 10 [Inference].
    - SW's own set list for 69RebIRIheg includes "-Ammo +2", and that HUD reads "0 / 22" [Observed description and still]. This supports a base of 12.
    - So the wiki's base values of 14 (Oct 2014), 17 (Nov 2014–2017) and 30 (Mar 2018 edit) do not match any observed HUD [Inference].
  - **Removal.**
    - The wiki added "NOTE: THIS WEAPON IS REMOVED!" on 2020-11-10 (Alphabbr, "added note") [Fan-wiki].
    - A comment on TwhAqkhrHwI by @_fray, dated "6 years ago" (so about 2020), reads "i miss grased lightning😭" [Unverified, fan comment with a relative date].
  - **2023 sightings (bears on "REMOVED").**
    - foodood, Jun 26, 2023: Gold Sanchez fires it at "0 / 17". The corner label reads "2.53.6 / 12008697" [Observed: https://i.ytimg.com/vi/pkfymcukjbY/maxresdefault.jpg, sd1, sd2].
    - Splxsh Clpxz, Jul 20, 2023: the HUD shows the same red lightning-decal rifle icon at "22 / 22" and "0 / 22 RELOAD", with the label "2.53.6 / 12101469" [Observed: 1ro5_csFNHQ sd1, sd2/maxres, sd3; icon crop].
    - So the weapon was equippable and firing in live matches in mid-2023 [Observed]. foodood's 2026 playtest frame carries the same second number, "12008697" [Observed: FNrzU5wMzFg sd1], so that number is an account ID and "2.53.6" is the client build [Inference].
    - Whether it returned to the store or players simply still owned it is unknown. "returns" in the title is ambiguous, and the description only says "Along with caffeine injection and fidget boomer" [Observed text; Unverified meaning].
    - The wiki's Updates page lists 2.53.3 (Aug 31, 2018) and then "3.0" (Nov 15, 2021: "All +1 Equipment has been removed except Speed +1"). It does not list 2.53.6 [Fan-wiki]. That conflicts with a 2023 HUD of 17 (12 + Ammo +1) on a 2.53.6 client [Inference; open question].
  - **2026.** No 2026 frame I opened shows Sanchez or this gun. The [LA]Huggable "WE ARE BACK" games (JyyNKoDVVQo, GZPfTi8wkj4; build "3.0.7 2026.11.19 b7") and foodood's Sep 20, 2026 playtest (FNrzU5wMzFg) show other classes [Observed]. Its presence in the Nov 4, 2026 release is [Unverified].

- **Look** (confirms the dossier, adds the in-game menu model)
  - **2015 main menu.** Default-skin Sanchez holds a glossy red rifle with white jagged lightning decals, a silver ribbed top rail, a grey muzzle block and a tan block on top at the rear. He holds it at waist height across his body, angled down toward the viewer's left [Observed: https://i.ytimg.com/vi/A7VWjfGET1A/sd1.jpg, about 1:08; crop a7_sd1_sanchez.png].
  - **Colour.** The red samples #C43C3D (median) to #C42920 (most saturated) on that compressed frame. The earlier render sample was #9C0001 [Observed].
  - **HUD icon.** The same red-rifle silhouette, with a tan/olive top tube, in 2014, 2015 and 2023 [Observed: smpl_sdd_icon.png, zw_sd1_hud.png, 6l9_hud.png, 1ro5_sd1_icon.png].
  - **Fan thumbnail.** SW's custom thumbnail reuses a Sanchez render that holds it one-handed at his left side, muzzle down-right [Observed: TwhAqkhrHwI maxresdefault; a fan-edited image].
  - **Size.** About 0.45× Sanchez's height, as before [Inference]. On the BBG News chart Sanchez is 1.0× Oliver [BBG News invention].

- **Firing**
  - Automatic. After the rework it had the "fastest RoF of any weapon" (0.04 s per the Oct 2014 wiki) [Fan-wiki].
  - **Muzzle.** A soft pink glow at the gun (#E691B7) in Sep 2014 [Observed: AVVg-fk_RnE sd1, about 1:03, crop avv_sd1_center.png]. A white ring-shaped flash with a pink-violet core at the gun in a 2016 frame [Observed: https://i.ytimg.com/vi/4D5s8lSclTM/maxresdefault.jpg, custom fan thumbnail]. An orange-red hot tip in 2015 [Observed: TwhAqkhrHwI sd3].
  - A lime-green glow near the gun in 2023 (#CBFD6E) [Observed: pkfymcukjbY maxres]. Calling it a muzzle effect is [Inference, weak].
  - **Sound:** undocumented [Unverified].

- **Projectile**
  - A thin, ruler-straight beam with a white core and pink-magenta edges, drawn as one continuous line from muzzle to target [Observed].
    - 2023: median #D888C2, saturated #EB70AC, white core #FFFBF8 [Observed: pkfymcukjbY maxres; crop pk_max_beam.png].
    - 2016: #EA7CD0 / #EE5FCD [Observed: 4D5s8lSclTM maxres].
    - 2015: a near-white beam with a pink tinge [Observed: TwhAqkhrHwI sd3].
  - It reads as an instant hit (hitscan) [Inference]. The wiki gives no projectile speed [Fan-wiki].
  - Wiki wording: "a red version of the Bind Gun" (Jun 2014); now "red-violetish lasers" [Fan-wiki].
  - Unlike the 2013–2016 Bind Gun's wavering, crackling arc (verified dossier), this beam is straight and thin [Observed comparison].

- **Impact / end result (the gap)**
  - **Best frame (2015, BBG 2.21 per the title).**
    - Tron-Tastic!-style Sanchez (black with cyan lines), HUD "2 / 22", fires the beam at a blue-team bear named "TIME FOR PARTY" in mid-jump.
    - At the target a large white spiky starburst bursts open: long blade-like shards (#FEFEFA), mostly flaring up and back.
    - Around it is a wide web of thin, branching red lightning arcs: core about #DC1021, softer glow #E06F70 and pink halo #EE9DAB.
    - The arcs spread several target-heights across the frame [Observed: https://i.ytimg.com/vi/TwhAqkhrHwI/sd3.jpg, about 3:32; crops tw_sd3_hit.png and tw_sd3_hud.png, where the rifle icon shows behind a KineMaster watermark]. Sizes measured from one still: starburst about 3× the target's height, arcs about 5–6× wide [Inference; perspective unknown].
    - The target shows no status icon and no visible knockback in the still [Observed].
  - **2016 confirmation.** The beam runs from Sanchez's red gun to a distant enemy, which sits inside a white starburst with red-orange arcs (#D5503A, saturated #EB3515) [Observed: 4D5s8lSclTM maxresdefault; a custom fan thumbnail over a gameplay frame]. Both SW titles call the effect an "electric storm" ("TORMENTA ELÉCTRICA", "MEGA OPTIONAL ELECTRIC STORM") [Observed titles].
  - **2015, close range.** White starburst shards and red-orange crackle (#D94E35) between Sanchez and an enemy, HUD "17 / 17" [Observed: A7VWjfGET1A sd3, about 3:23; crop a7_sd3_center.png]. The full magazine means this could be the first shot of a burst or another source [Inference].
  - **Pre-rework (Sep 2014).** Only a small white-yellow spike flare at an enemy's head while Sanchez reloads at "0 / 50" [Observed: AVVg-fk_RnE sddefault; crop avv_sdd_target.png]. It may be the enemy's own muzzle flash [Unverified]. Compare the dossier's "white flare" in 5pXfHBEON4M hq1.
  - **2023.** The beam ends in an orange-red hot spot on the target, with no large starburst in that still [Observed: pkfymcukjbY maxres, crop pk_max_beam.png].
  - **Mechanics.** Damage only: "dealing damage with no secondary effect, unlike the other Arbiter primaries", and "The weapon has a slight AOE, unfortunately that AOE deals no damage" [Fan-wiki]. The red arcs are plausibly the visual of that zero-damage AOE [Inference].
  - **KO look:** no kill frame seen [Unverified].
  - **Do not animate these as Greased Lightning effects** (they are in the same videos):
    - **White dust cloud with a coffee mug overhead.** This is the Caffeine Injection Special: "the symbol of a coffee cup will appear above the player and there will be a trail of white dust around their feet" [Fan-wiki]. Seen in smplbld5gfo sd1, pkfymcukjbY sd1 and A7VWjfGET1A maxres (an enemy with a mug and white puffs) [Observed; identification Inference].
    - **Orange-yellow fireball halfway along the beam** in pkfymcukjbY sd1. Its source is unknown. The description also names the Fidget Boomer, which is a Sniper explosive [Fan-wiki; Unverified].
    - **Magenta electric swirl around Sanchez's legs** at "50 / 50" (6L9-oeL-x1o sddefault). It matches the dossier's "unexplained pink crackle" and the Bearscream Sandwich aura in combat-vfx [Inference].
    - **Thin pink line ending in a magenta glow ball at a grey barrel** (A7VWjfGET1A sd2, HUD "1 / 2", Sanchez dead). That HUD belongs to a 2-ammo weapon, not Greased Lightning [Inference].
    - **Pink beam in 4D5s8lSclTM sd1.** Sanchez's HUD reads "22 / 22" and he wears the yellow-Z Slowed icon, so someone else fired it [Inference].
    - **Pale-cyan full-screen wash** (Zw7Vvc-VSCI sd1), **snowflake cluster** (1ro5_csFNHQ sd3) and **red room lasers** (69RebIRIheg sddefault) are unexplained [Unverified].

- **Images viewed** (all under `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/`)
  - **Individual stills:**
    - `sanchez-gaps/yt/smplbld5gfo_sddefault.jpg`, `_sd1.jpg`, `_sd2.jpg`, `_sd3.jpg`
    - `sanchez-gaps/yt/6L9-oeL-x1o_sddefault.jpg`
    - `sanchez-gaps/yt/1ro5_csFNHQ_maxresdefault.jpg`, `_sd1.jpg`, `_sd2.jpg`, `_sd3.jpg`
    - `sanchez-gaps/yt/pkfymcukjbY_maxresdefault.jpg`, `_sd1.jpg`, `_sd2.jpg`, `_sd3.jpg`
  - **Contact sheets of sddefault and sd1–sd3:** `sanchez-gaps/sheets/sheet_A7VWjfGET1A.png`, `sheet_TwhAqkhrHwI.png`, `sheet_4D5s8lSclTM.png`, `sheet_Zw7Vvc-VSCI.png`, `sheet_AVVg-fk_RnE.png`, `sheet_69RebIRIheg.png`, `sheet_JyyNKoDVVQo.png`, `sheet_GZPfTi8wkj4.png`, `sheet_FNrzU5wMzFg.png`
  - **Crops** in `sanchez-gaps/crops/`: smpl_sd1_center.png, smpl_sdd_icon.png, 1ro5_sd3_center.png, 1ro5_sd1_icon.png, pk_max_beam.png, pk_sd1_beam.png, a7_sd1_sanchez.png, a7_sd3_center.png, a7_sd2_beam.png, a7_max_center.png, a7_sdd_hud.png, tw_sd3_hit.png, tw_sd3_hud.png, tw_max_render.png, 4d_max_hit.png, 4d_sd1_beam.png, zw_sd1_hud.png, zw_sd1_player.png, 6l9_player.png, 6l9_hud.png, avv_sd1_center.png, avv_sdd_target.png. A first crop, a7_sd1_menu.png, missed the target.
  - **Re-opened for comparison:** `sanchez-verify/sheets/greased.png` and `unassigned/png/Greased_Lightning.png`
  - **Source URLs:** https://i.ytimg.com/vi/<ID>/<variant>.jpg for each ID above.

- **Depiction for shorts:** Sanchez hip-fires a glossy red rifle with white lightning decals, with a soft pink glow at the muzzle. A ruler-straight beam (white core, pink edges) snaps to the target, where a white spiky starburst pops and thin red lightning forks crackle outward in a wide web, then vanish; the target flinches with no status icon [Observed]. Fire it in rapid bursts that empty the magazine fast, then show a long reload [Fan-wiki stats; timing is BBG News invention]. The crackle-zap sound is [BBG News invention], and so is a KO where the bear pops into sparks and rainbow confetti. Caption it "classic BBG weapon (2014–2020; seen again in 2023)". Never imply it is in the 2026 release. Leave out the "Grease" song and lyrics [Inference: rights].
- **Confidence:** observed for the projectile and the hit look (stills only, two independent SW videos plus a third consistent frame). Kill look, sound and 2026 status are unknown.

---

## Corrections for the character file

`/home/user/thallo-site/bbg-news-repo/characters/sanchez.md` never mentions Greased Lightning, so nothing in it needs correcting for this gap. Optional addition under "Weapons/props": "Retired 2014 primary Greased Lightning: red lightning-decal rifle; straight white-core pink beam; white starburst with red lightning arcs on hit [Observed]."

The gap's findings do correct the two weapons dossiers. Exact text and fixes are in `soul_corrections`:
1. **Verified sanchez.md, ammo line.** "That matches neither wiki value (40 in 2014, 30 now)…" should become: base 12 since the Oct 2014 rework, with 17 = 12 + Ammo +1 and 22 = 12 + Ammo +2.
2. **Verified sanchez.md, stat history.** Add the Oct–Nov 2014 rework (revs 67757 and 68011).
3. **Verified sanchez.md, impact and depiction.** Replace "white flare… only hit look seen" and "Hits spark and do nothing else" with the starburst plus red arcs.
4. **Verified sanchez.md heading and shared.md Part F row.** Add the 2023 sightings on build "2.53.6".
5. **shared.md depiction.** "rapid red-violet laser darts" should become a continuous straight beam.

## Open questions
- Is Greased Lightning in the Nov 4, 2026 build? The Arbiter chapter (47:23) of the JustNubz showcase is unviewed.
- Did it return to the store in 2023, or did owners keep it? Why do 2023 clients read "2.53.6" when the wiki lists a 3.0 on Nov 15, 2021 that removed +1 equipment, yet a 2023 HUD shows 17 (12 + Ammo +1)?
- What was the exact stat history? Observed base ammo is 12, against the wiki's 14 (Oct 2014), 17 (Nov 2014) and 30 (Mar 2018). Was the Mar 2018 edit real?
- Does the small 2014 flare versus the big 2015–2016 starburst reflect the rework or just distance and frame choice?
- What do a KO and the firing sound look and sound like?
- SkyVu's Jun 6, 2014 post (snapshots 20140617141419 and 20141022042112) is still unread because web.archive.org drops every connection.
