<!-- gap pass 1 -->
# Wil (Chub Scout): gap addendum on the Señor Potato, Doomstick, Balance Beam, Bubble Gun, Snowtato Launcher and Sole's Bane

**What this covers.** This addendum fills the open visual gaps for six of Wil's weapons in the verified Wil dossier (`out/verified/wil.md`). For the Señor Potato it covers the spud in flight. For the Doomstick and Balance Beam it covers what a hit looks like. For the Bubble Gun and Snowtato Launcher it covers projectile and impact. For Sole's Bane it covers the throw and the trigger. Wil is BBG's Chub Scout. The class blurb reads: "The masticator of mayhem, a Chub Scout is always prepared to even the odds for his team." [Game text via wiki] (Template:Class:Chub_Scout_(BBG)).

**Sources I reached today (Oct 18, 2026)**
- **Wiki (MediaWiki API, re-read today):** Senor Potato, Doomstick, Balance Beam, Bubble Gun, Snowtato Launcher, Sole's Bane, Static Shuffle, Doom Cloud, Smoke Screen, Bind Field, Fairy's Dust, Slow Motion Field, Bearscream Sandwich, Not-So-Slenderman and the Battle Bears Gold/Versions and Versions/2.6 pages. I also listed wiki images by name prefix. No extra in-game shots exist for these weapons beyond the known renders.
- **YouTube:**
  - Thumbnails for 30+ videos, including the higher-resolution `maxres1/2/3` (1280×720) and `sd1/2/3` (640×480) frames. `maxresN` is the same frame as `hqN`: the RMS pixel difference is 5–9, against 41–91 for a different frame (checked on ORYnnvqn19w, HKbwq7PolNc and w1lx3MdRaDQ) [Observed via pixel comparison].
  - Titles and channels via oEmbed; upload dates, descriptions and chapters via YouTube's `next` endpoint.
  - I watched no video. Every YouTube [Observed] below is a still thumbnail I opened.
- **Official 2026 Steam trailer** (`visuals/trailer.mp4`, 1920×1080). I made new extractions at 26.0–32.0 s and 38.8–40.8 s. The trailer re-edits 2013 launch footage (see `out/verified/2026.md`).
- **Steam news API for app 4408320:** 7 SkyVu announcements, Feb–Oct 2026. None names a Wil weapon. The Oct 14 post lists "Custom keybinds -Jukebox -UI controller support -Lighting improvements -Lots of bug fixes" [Canon].

**Not reached.**
- web.archive.org returned "429 Too Many Requests" on 9 tries with backoff, and WebFetch is blocked for that domain. SkyVu's 1.4.3, 2.6, 2.12 and 2.26 notes therefore stay [Fan-wiki transcription] / [Unverified].
- YouTube video and storyboard access is blocked.

**Paths**
- `$G` = `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil/gaps`
  - `$G/yt/<id>_<size>.jpg`: thumbnails
  - `$G/crops/`: zooms
  - `$G/sheets/`: contact sheets
  - `$G/trailer/f_<s>.png`: my trailer extractions
  - `$G/json/`: oEmbed and next data
  - `$G/wiki/`: wiki JSON
- `$V` = `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-verify` (earlier wiki renders)
- Hex values are medians of hue-filtered pixels from compressed thumbnails. They are approximate.

**Scale.** Oliver = 1.0×; Wil ≈ 0.9× and pear-shaped [BBG News invention, house chart].

**Era key** [Fan-wiki: Versions]
- BBR: from Oct 2011.
- BBG: 1.0 on May 24, 2013, through 3.0.1 (Dec 18, 2021).
- BBG 2026: the re-release on Nov 4, 2026. Playtest build stamps seen: "3.0.2 / 33152" (Aug 2026) and "3.0.7_2026.11.19_b7" (Oct 2026) [Observed].
- BBH: 2023–24.

**Headline findings**
1. **Señor Potato in flight (2026):** I identified the Mingo hq2 object. At 1280×720 a brown spud is leaving the Señor Potato's cardboard-tube barrel inside a broad white-hot trail. The gun's googly eye and red nose are in the foreground [Observed].
2. **Fries are in the official trailer.** At 30.0–31.6 s, about 7 burning fry stubs smoke on the Space Oddity floor [Observed]. Calling them Señor Potato fries is [Inference]; they match BBR Señor Potato footage.
3. **The 2026 "Wil-type long spear-gun (27/70)" is the Balance Beam.** It fires a magenta beam, and 27/70 fits 50 + Ammo +2 [Observed; Inference].
4. **Balance Beam hit:** a small magenta spiky flare at the target [Observed, 2019].
5. **Bubble Gun:** the bubbles are huge translucent iridescent domes on the floor. A solid teal ball is the probable projectile [Observed; Inference].
6. **Sole's Bane is in 2026 builds** (HUD icon) [Observed]. The pink-violet "lightning" in earlier Sole's Bane frames is probably not Sole's Bane [Inference].
7. **Snowtato:** the HUD icon is confirmed in two videos, with clip 5/5 [Observed]. The violet puff cloud now has a competing explanation, Fairy's Dust [Fan-wiki].

---

## Señor Potato (primary; BBR 1.4.3, Apr 15, 2013 → BBG → seen in the Oct 2026 final playtest)
- **Official text:**
  - "You couldn't find a kinder gun if you tried! Not only does it fire a high velocity spud at your enemies, it also leaves piping hot fries behind to blister their feet." [Game text via wiki] (Senor Potato).
  - Update note: "-Señor Potato Cannon: Wil shoots flaming spuds that explode on contact and leave piping hot french fries behind; Caution, fries do damage over time." [Fan-wiki transcription of SkyVu 1.4.3.1 notes; Unverified as Canon].
- **Look (2026, new):** In Mingo, "Wil you tuck me into bed tonight? (BATTLE BEARS GOLD FINAL PLAYTEST - NOV 4th RELEASE!!!!)" (Oct 17, 2026; build stamp "3.0.7_2026.11.19_b7"), maxres2 is the 1280×720 version of the hq2 cited in the gap. It shows the weapon held by the camera player [Observed: `$G/yt/ORYnnvqn19w_maxres2.jpg`; `$G/crops/ory_m2_potato.png`]:
  - a golden potato body (≈ #F0C664 lit, #DFB667 shade);
  - a round red Mr. Potato Head-style nose (≈ #B43C2B);
  - a pink ear and a big white googly eye with a black pupil;
  - a pink-tan cardboard-tube barrel (≈ #F5C6A2 where lit by the trail), flared at the mouth with one band, pointing up and forward.
  - This matches the BBG render File:Senor_Potato.jpg (coffee cup, handlebars, tube, Potato Head parts) [Observed: `$V/png/Senor_Potato.png`].
  - Seen from Gold Wil's side, the coffee cup and handlebar are visible at the hip [Observed: `$G/crops/7di_m3_gold.png`, 7dIxzrgiB0Y maxres3].
- **Who fires it in the 2026 frame:**
  - The camera player has a round grey-white head with grey ears and a black suit with a red cuff [Observed: ORYnnvqn19w maxres2 and sddefault]. That matches File:Not_so_slenderman.png, a faceless pale head over a black suit with a red tie and cuffs [Observed: `$V/png/x_ot_so_slenderman.png`].
  - So it is **Wil in the Not-So-Slenderman skin** [Inference; the Señor Potato is a Chub Scout weapon (Fan-wiki)]. The gap's "flying … behind Wil" should read "leaving Wil's own barrel".
  - In sddefault the same player faces a default-look Wil (red vented helmet, white ribbed tank top with a red ice pop). Both hold red-and-white aerosol cans (Whipped Pain by [Inference]) [Observed: `$G/yt/ORYnnvqn19w_sddefault.jpg`].
- **Firing:**
  - Infobox: 1 s rate of fire, 3 ammo, 3.5 s reload, 1000 u/s [Fan-wiki]. "Confined to close-ranged combat only, due to its extreme arc" [Fan-wiki].
  - Clip readouts by era [Observed]:

    | Era | Clip readouts | Source |
    |---|---|---|
    | BBR, Apr 2013 | 1/4, 0/4 | ENP2hDgNL_8 maxres1–3 |
    | BBG, June 2014 | 4/4, 3/4, 2/4, 1/4, 0/4 | Nathan Ye videos rXof_z1BCfI, 8qvBaaZQRhI, pLgnOnsMWBQ |
    | Jan 2015, 2.21–2.22 and Jul 2015 | 3/3, 2/3, 1/3, 0/3 | gJhrAKcno3M, IbC1S6CArrI, 1PPkt0_HQZQ, tkV7YvsJWSU, cOV7xi__i_Q |

    The 3-round clip in the infobox therefore applies from at least Jan 2015 [Inference].
  - The 2026 frame hides the HUD [Observed].
  - In the 2015 loadout screen the menu reads "PRIMARY SENOR POTATO / SECONDARY SOLE'S BANE", with default-look Wil holding a bow [Observed: `$G/yt/cOV7xi__i_Q_maxres1.jpg`].
- **Projectile (new, 2026):**
  - The spud has just cleared the tube mouth [Observed: ORYnnvqn19w maxres2]. It is a plain brown-gold oblong potato (≈ #CC9231 lit) with darker brown "eye" spots (≈ #8F5615), about as wide as the barrel mouth.
  - **The spud itself is not on fire** in this frame [Observed].
  - It sits inside a broad, straight, white-hot trail: a cream-white core (≈ #FEFFFA) with warm yellow-orange edges (≈ #F0B65D). The trail runs from the muzzle to the top of the frame, where a pale ring hangs over a golden platform [Observed: `$G/crops/ory_m2_ring.png`].
  - That the trail is the shot's own path is [Inference]. What the ring is remains [Unverified].
  - "Flaming spuds" stays a [Fan-wiki transcription]. In 2026 the heat reads as the trail, not a burning potato [Inference].
- **Impact / end result:**
  - **Blast:** In "H[O.C.O][SS]/[OF]#8 BIMBO EL INFILTRADO!! (SENOR POTATO) | Battle Bears Gold 2.21" (Nov 22, 2015), at RELOAD 0/3 a huge flat-shaded fireball fills the centre of the frame [Observed: `$G/yt/tkV7YvsJWSU_maxres2.jpg`, `$G/crops/tkv_m2_boom.png`]. It has an orange body (≈ #F28E36), yellow flares (≈ #FFFC53) and a pale-yellow core (≈ #FEFEAE).
  - **Fries, BBR (Apr 25, 2013):** "Battle Bears Royale: Wil Senor Potato Gameplay!…" maxres2 (RELOAD 0/4, Gold Wil) shows about five vertical flame columns rising from small yellow blocky stubs on the floor where an enemy stood [Observed: `$G/crops/enp_m2_fire.png`]. The flames are orange-red (≈ #E38E4E) with yellow cores.
  - **Fries, official trailer (footage date unverified; probably 2013-era [Inference]):** At 30.0–31.2 s on Space Oddity, beside a jump pad behind the central pillar, there are about 7 stubby yellow-orange fry blocks (highlights ≈ #FFD356). Each has an orange flame tongue (≈ #D3883B) and a grey-white smoke wisp. Flame plus stub is roughly as tall as a bear standing near the pillar; the stub alone is short [Observed, approximate: `$G/trailer/f_30.3.png`, `$G/crops/tr303_fries.png`, `$G/crops/tr303_full.png`, sequence `$G/sheets/tr_fries_seq.jpg`].
    - The flames shrink by 31.6 s and are nearly gone at 32.0 s, though the shot is edited [Observed].
    - That these are Señor Potato fries is [Inference]: they match the BBR clip and the official text. This also supports the [Inference] in `research_notes/BBG maps (unverified drafts)/research_space-oddity.md`.
  - **Fries at a distance:** In "Señor Potato Gameplay - Battle Bears Gold 2.22", maxres3 (2/3), three or four pink-red flame tongues (≈ #B82955, paler cores) stand on a temple roof against Aztec Attack's magenta sky [Observed: `$G/crops/1pp_m3_pink.png`]. Fries tinted by the sky is [Inference].
  - **Fries, 2026:** a low-res patch of orange flame (≈ #E4852E) with yellow blocky bits at the lower edge of ORYnnvqn19w maxres2 [Observed, low-res: `$G/crops/ory_m2_floor.png`]. That these are fries is [Inference].
  - Mechanics: the fries also hurt players "a large depth below the ground they are planted on". Impact 65; explosive 35–50 [Fan-wiki].
- **Images viewed:**
  - 2026: `$G/yt/ORYnnvqn19w_maxres1.jpg`, `_maxres2.jpg`, `_maxres3.jpg`, `_sddefault.jpg`; `$G/crops/ory_m2_potato.png`, `ory_m2_fire.png`, `ory_m2_top.png`, `ory_m2_floor.png`, `ory_m2_ring.png`, `ory_m2_br.png`; `$G/sheets/ory_m1_bits.jpg`
  - Older fan videos: `$G/sheets/s_ENP2hDgNL_8.jpg`, `$G/crops/enp_m2_fire.png`; `$G/sheets/s_tkV7YvsJWSU.jpg`, `$G/crops/tkv_m2_boom.png`; `$G/sheets/s_rXof_z1BCfI.jpg`, `s_8qvBaaZQRhI.jpg`, `s_pLgnOnsMWBQ.jpg`, `s_gJhrAKcno3M.jpg`, `s_cOV7xi__i_Q.jpg`, `s_ZrU9j7rfGmI.jpg`, `s_1PPkt0_HQZQ.jpg`, `s_IbC1S6CArrI.jpg`, `s_7dIxzrgiB0Y.jpg`, `s_XxEAr8mP4nE.jpg`; `$G/crops/rxof_hq1_mid.png`, `rxof_hq3_left.png`, `8qv_hq1_gun.png`, `plg_hq3_mid.png`, `cov_m3_fire.png`, `1pp_m3_pink.png`, `7di_m3_gold.png`, `xxe_sd3_target.png`
  - Trailer and renders: `$G/sheets/tr_fries_seq.jpg`, `$G/sheets/tr_28_32.jpg`, `$G/trailer/f_30.3.png`, `$G/crops/tr303_fries.png`, `tr303_full.png`; `$V/png/Senor_Potato.png`, `$V/png/x_ot_so_slenderman.png`
- **Inconclusive:**
  - rXof_z1BCfI hq1 shows small yellow vertical flecks on the floor near an enemy (fries?).
  - pLgnOnsMWBQ hq3 shows an orange flame puff with a cyan streak under a ceiling emitter (a burning spud?).
  - ZrU9j7rfGmI (BBR, May 2013) shows only a pink heart-shaped blob and a small tan cube [Observed; identity Unverified].
- **Depiction for shorts:** A thunk from the cardboard tube, and a plain brown spud arcs out inside a white-hot streak. It bursts in a flat orange-and-yellow fireball and leaves a small cluster of upright fry stubs, each with a flickering orange flame and a smoke wisp, which fade after a beat [Observed]. A bear hopping on hot feet is a [BBG News invention]; keep it to cartoon hops, no burns shown.
- **Confidence:** observed. The spud in flight, gun, blast and flames are seen. Tying the trailer and 2026 flames to this weapon is [Inference].

## Doomstick (primary; BBR v1.3/1.3.1, 2012 → BBG; 2.6 rebalance on Dec 20, 2013; not seen in 2026 material)
- **Official text:** "We give Wil a hard time but, the truth is, he is a far braver man than I for even touching this thing... 0__0" [Game text via wiki] (Doomstick).
- **Look:**
  - The HUD icon is the same in four videos: a dark red-black pump shotgun with a row of glowing yellow-orange dots along the top, a pale eyeball with an orange-red ring set in the receiver, and a red-brown barrel [Observed: `$G/sheets/doom_hud.jpg`, from rUjXj4f6mdg sd2, ryI4O43eVRs sd2, hYW93uwB3Hs maxresdefault, 0JH_1wV7r0o hq2].
  - This matches the lava-crack, eyeball model in File:Wil_doomstickers.png [Observed earlier: `$V/png/Wil_doomstickers.png`]. The wiki calls it "a firey, more hellish version with an eye in the middle" [Fan-wiki].
- **Firing:**
  - "Releases a powerful, short ranged wave of bullets"; used "like a pump action shotgun" [Fan-wiki].
  - Clip readouts [Observed]:

    | Era | Clip readouts | Source |
    |---|---|---|
    | BBR, Aug 27, 2012 | 1/2, 2/2 | yFfQoMdvChg; its description reads "Testing doomstick, with 2 damage and 2 speed" |
    | BBG, Aug 23, 2013 | 2/2, 1/2, 0/2 | hYW93uwB3Hs |
    | Jan 2, 2014 and Aug 1, 2014 | 5/5 | ryI4O43eVRs, rUjXj4f6mdg |
    | Jul 5, 2014 | 1/5 | lG4UEoxgoc4 hq3 |

  - This fits the wiki's 2.6 changes, "Clip size increased from 2 to 3" and "Ammo +2 increased from 0 to 2", which give 3 + 2 = 5 [Fan-wiki: Versions/2.6; Inference]. The Versions table dates 2.6 to "December 20th, 2013" [Fan-wiki].
- **Muzzle flash (new):** In "#8 Battle Bears Royale: Gameplay - The amazing Doomstick" (xBlush Bangarang, Aug 27, 2012), maxres1 shows a large, soft, cream-white bloom (≈ #F7CDA2) between Wil's barrel and the target, at close range, with the Doomstick icon on the HUD [Observed: `$G/crops/yff_m1_hit.png`, `$G/sheets/s_yFfQoMdvChg.jpg`].
  - Reading it as the shotgun's blast puff is [Inference].
  - The steaming coffee mug in the same frame is an overhead status icon (Caffeine Injection by [Inference]), not the gun.
- **Projectile:** none visible; shotguns are hitscan [Fan-wiki: Weapon Statistics].
- **Impact / end result (new, partial):**
  - In "BATTLE BEARS GOLD WIL GAMEPLAY (WITH DOOMSTICK)" (Aug 23, 2013), maxres3 shows a killed enemy lying face-down, intact, in the mine, with his rifle beside him [Observed: `$G/crops/hyw_m3_body.png`]. The feed shows "KILLS", "+25 +100" and "STREAK +20".
  - Three blue-white lightning-bolt icons in a blue glow hover above the body [Observed]. These fit the Joules drop: "Three [Joules pickups] are dropped… and disappear after 10 seconds" [Fan-wiki: Pick-Ups, via `out/verified/combat-vfx.md`; Inference].
  - In "Battle bears gold 12-3 streak doomstick gameplay" (Jan 2, 2014), sd3 shows red, green, cyan and yellow blotches plus a big white puff around a bear on a dark platform [Observed, low-res: `$G/crops/ryi_sd3_hit.png`]. What caused it is [Unverified].
  - lG4UEoxgoc4 hq3 shows a small white puff with red flecks on a distant ridge [Observed, low-res: `$G/crops/lg4_hq3_puff.png`]. It is unattributed [Unverified].
  - No pellet spark has been isolated [Unverified].
- **Images viewed:** `$G/sheets/s_rUjXj4f6mdg.jpg`, `s_ryI4O43eVRs.jpg`, `s_hYW93uwB3Hs.jpg`, `s_0JH_1wV7r0o.jpg`, `s_yFfQoMdvChg.jpg`, `s_lG4UEoxgoc4.jpg`, `doom_hud.jpg`, `lg4_icons.jpg`; `$G/crops/ryi_sd3_hit.png`, `0jh_hq2_hit.png` (inconclusive), `yff_m1_hit.png`, `hyw_m3_body.png`, `hyw_m1_feed.png`, `hyw_m1_feed2.png`, `hyw_m1_buff.png`, `lg4_hq3_puff.png`.
- **Depiction for shorts:** Wil braces the red-black, lava-dotted shotgun; the eyeball glints. One pump sends out a big cream-white blast puff. The target flops over intact, and three little blue lightning-bolt tokens pop up above it [Observed]. Glowing lava-coloured sparks at the hit are a [BBG News invention]. No blood.
- **Confidence:** partial.

## Balance Beam (primary; level 15; BBR v1.3, May 3, 2012 → BBG → seen in the Oct 2026 final playtest)
- **Official text:** "The worse your team is doing than the other team, the more powerful this weapon is." [Game text via wiki]
- **Look:**
  - A white gun body with a gold rod, two gold hexagonal weights, a blue tip and a red end, and a white pentagon emitter glowing violet [Observed: `$V/png/Balance_Beam.png`, re-opened].
  - Gold Wil holds it at the waist, firing from the pentagon [Observed: DDz8bLbWPyo maxres2/3].
  - **HUD icon (new):** the gun seen side-on. A grey-white body with a fishtail-shaped grip and stock, a gold cone (the hex weight), a red-orange-gold shaft and a pale arrowhead tip [Observed: `$G/sheets/icons_cmp.jpg`, comparing the 2026 HKbwq7PolNc maxres1 icon with the 2019 DDz8bLbWPyo maxres2 icon].
- **2026 status (new):**
  - In InstableGR, "Battle Bears Gold - Final PC Playtest (10/15/26)" (build "3.0.7_2026.11.19_b7"), maxres1 shows the Balance Beam firing [Observed: `$G/yt/HKbwq7PolNc_maxres1.jpg`]. The shooter is a tan bear with a blue tied headband, and the gun's white body and gold hex weight are visible. The HUD reads 27/70 with the Balance Beam icon and the Sole's Bane brick icon above it.
  - The map is Desert Airmine (red mesas, windmill, rope lines) [Observed], so this is most likely "Match 1 (Team Battle, Desert Airmine, Wil/Riggs)", the only Wil chapter on that map [Inference from chapter titles].
  - 70 = 50 + the wiki's "Ammo +2 → + 20 bullets" [Fan-wiki; Inference]. This fits the wiki's 3.0 note that "+1" equipment was removed but "+2" kept [Fan-wiki transcription; Inference].
- **Firing:** "Works like a standard hitscan automatic, firing beams in quick succession"; 0.15 s rate of fire; range 3000; "fires slightly below the crosshairs" [Fan-wiki].
- **Projectile / beam (new):**
  - In "BATTLE OF GODS - Battle Bears Royale 3v3/4v4 with Gold Skin Orbs and Balance Beam" (bearpantsbb, Jan 21, 2019), two or three thin, straight magenta lines (≈ #C73DA6–#CA36A3, with a lighter lavender strand) run from the white pentagon emitter to the target and converge there [Observed: `$G/crops/ddz_m2_beam.png`, `ddz_m3_beam.png`].
  - The yellow rays in the same frame belong to the Gold Skin Orbs named in the title [Inference].
  - In 2026 the beam is a single bright magenta streak (≈ #CA23A9, pale-pink core ≈ #F0C0EB) with small white sparkle dots along it, running steeply up to an enemy on a billboard [Observed: `$G/crops/hkb_m1_beam.png`, `hkb_m1_target.png`].
  - Several strands at once = successive 0.15 s beams drawn while the muzzle bobs [Inference].
  - The beam colour is the same magenta from the 2.22-era video (o4FJDPNxyuA; the earlier dossier's "faint thin pinkish line") through 2019 to 2026 [Observed].
- **Impact / end result (new):**
  - At the beam's end, a small magenta spiky star-flare sits on an enemy half-hidden behind the Space Oddity pillar [Observed: `$G/crops/ddz_m3_tip.png`, 2019].
  - In ddz_m2 the distant target glows white-pink where the strands meet [Observed].
  - In 2026 a small yellow-white flare with green and orange flecks sits where the beam meets the enemy [Observed, low-res: `$G/crops/hkb_m1_target.png`]. That it is the hit spark rather than the enemy's own fire is [Inference].
  - No knockback or special kill effect is seen or documented [Unverified].
- **Images viewed:** `$G/yt/HKbwq7PolNc_maxres1.jpg`, `$G/sheets/s_HKbwq7PolNc.jpg`, `$G/crops/hkb_m1_beam.png`, `hkb_m1_target.png`, `hkb_m1_hud.png`, `hkb_m1_icon.png`; `$G/sheets/s_DDz8bLbWPyo.jpg`, `$G/crops/ddz_m2_beam.png`, `ddz_m2_far.png`, `ddz_m3_beam.png`, `ddz_m3_tip.png`, `ddz_m2_icon.png`; `$G/sheets/icons_cmp.jpg`, `s_o4FJDPNxyuA.jpg`; `$V/png/Balance_Beam.png`.
- **Depiction for shorts:** The violet pentagon glows, and rapid, thin magenta beam strands (with a pale-pink core) stitch from the emitter to the target. Each hit pops a tiny magenta star-spark [Observed]. Gag: the beam gets brighter as the scoreboard turns against Wil's team. That reflects the [Game text via wiki]; the brightening itself is a [BBG News invention].
- **Confidence:** observed.

## Bubble Gun (primary; BBG 2.12, Oct 2, 2014; last seen in a 2.53.5 fan upload; 2026 unconfirmed)
- **Official text:** "Bubble bubble pop, BUBBLE POP!" [Game text via wiki]
- **Release:** The Versions table row for "2.12" reads "*New Weapons … **[[Bubble Gun]]" and is dated "October 2nd, 2014" [Fan-wiki].
- **Look:**
  - A green sphere tank with yellow piping, a yellow body and a light-blue barrel with a yellow square-frame muzzle [Observed earlier: `$V/png/Bubble.png`].
  - **HUD icon (new):** the green sphere tank with a blue light, yellow frame and piping. The secondary slot shows the orange Sole's Bane brick [Observed: `$G/crops/bub_m1_hud.png`].
- **Firing:**
  - "Will fire a blue projectile"; 800 u/s; 0.75 s rate of fire; 4 ammo; 3.5 s reload [Fan-wiki].
  - In "Bubble gun is a good weapon (battle bears)" (foodood, Nov 25, 2021; build stamp 2.53.5) the HUD reads 6/6 and 0/6 RELOAD [Observed: `$G/sheets/s_w1lx3MdRaDQ.jpg`]. That fits 4 + "Ammo +2 … + 2 bullets" [Fan-wiki; Inference].
  - The uploader's description: "You just need to be good at predicting and prob give it ammo" [fan text].
- **Projectile (new):** A solid teal-blue ball (≈ #2CA7BC) with a white highlight and a white splash-puff behind it, plus a second smaller teal ball nearer the wall, in flight at mid-range [Observed: `$G/crops/bub_m2_proj.png`]. That these are the Bubble Gun's "blue projectile" is [Inference].
- **Impact / end result (new):**
  - Two huge **translucent iridescent domes** sit on the floor of the Huggable-crate corridor [Observed: `$G/yt/w1lx3MdRaDQ_maxres2.jpg`, `$G/crops/bub_m2_bubbles.png`, `bub_m2_left.png`].
  - They are clear, with a blue-teal sheen (≈ #6CA4B9), violet fringes (≈ #8C50A2), soft pink edges and bright white specular streaks (≈ #FAFDFD). Background and an enemy show through them.
  - Each dome is several times a bear's width across. This is approximate; depth is uncertain [Observed, approximate].
  - This matches "a big bubble to appear in the area where it was shot" [Fan-wiki]. The pop, "After a second or two, this bubble will explode", was not seen [Unverified]. Explosive 25–50; AoE 125/250; self-kill possible [Fan-wiki].
  - The BB Zero version's deflection ("can deflect enemy projectiles") is a different game [Fan-wiki: Bubble Gun (BB0)].
- **Images viewed:** `$G/sheets/s_w1lx3MdRaDQ.jpg`, `$G/yt/w1lx3MdRaDQ_maxres2.jpg`, `$G/crops/bub_m2_bubbles.png`, `bub_m2_left.png`, `bub_m2_proj.png`, `bub_m1_hud.png`, `bub_m3_right.png`.
- **Depiction for shorts:** A wet "plip": a teal ball splats and swells into a big soap-bubble dome with a rainbow sheen [Observed]. Bears inside press their noses on the wall; after a beat it pops in suds and rainbow confetti. The pop's look is a [BBG News invention].
- **Confidence:** partial (bubble observed; pop not seen).

## Snowtato Launcher (primary; BBG 2.26, Jan 17, 2017; 2026 unconfirmed)
- **Official text:** "A makeshift potato launcher convertor to weapon of frosty devastation. Shoot snowballs that explode and turn them into flakes!" [Game text via wiki]
- **Look:**
  - The Señor Potato build in ice tones: a lavender-blue potato, an ice-blue cup, blue-grey fins and a grey barrel [Observed earlier: `$V/png/Snowtato.png`].
  - **HUD icon (new):** a dark slate-blue potato body with a short brown pistol grip. It appears in both "(NEW UPDATE) "SNOWTATO" WEAPON REVIEW DEFINATELY WORTH BUYING" (Mateusz bb, uploaded Jan 18, 2017, the day after the wiki's 2.26 date) and "BattleBearsRoyale 2.53.2 S4 Ep56: Snowtato Launcher Gameplay" (Sep 1, 2018) [Observed: `$G/sheets/snow_icons.jpg`]. So both videos are genuine Snowtato footage [Inference].
- **Firing:**
  - Cooldown 2.2; ammo 6; reload 4.5 s; "the only Chub Scout (BBG) primary not affected by equipment of any kind" [Fan-wiki].
  - **Both videos read 5/5** [Observed: cyv2EZwzW7A maxresdefault and maxres1–3; _7wmOHdRMs4 maxres1]. If equipment cannot change it, the base clip was 5 in 2017–2018, not 6 [Inference; conflicts with the Fan-wiki infobox].
- **Projectile:** "snowballs" [Game text via wiki]. Still not seen in flight [Unverified].
- **Impact / end result:**
  - "Snow will remain present in the air in the Snowtato's area of effect for several seconds and block any explosives, even other Snowtato projectiles fired by the user" [Fan-wiki]. Explosive 35–65; AoE 150/300 [Fan-wiki].
  - Re-checked at 1280×720: _7wmOHdRMs4 maxres1 (5/5, score 0–0) shows dozens of separate rounded, dark-outlined violet-indigo puffs (≈ #3E197D) scattered through the Space Oddity corridor and drifting toward the camera, plus one pale lavender translucent ring-puff [Observed: `$G/yt/_7wmOHdRMs4_maxres1.jpg`, `$G/crops/snow_m1_puffs.png`].
  - **New caution:** Fairy's Dust (a Sniper secondary) makes "a huge, harmless cloud of purple dust" [Fan-wiki: Fairy's Dust], so purple puffs alone do not prove Snowtato snow.
  - The puffs here are many separate particles, not one cloud, which leans toward the Snowtato's "flakes" [Inference]. Attribution and colour stay [Unverified].
  - The 2017 review frames on snowy No Bear's Land show only an ambiguous white puff on a ledge and a panda-faced enemy [Observed, low-res: `$G/crops/cyv_md_puff.png`, `cyv_m3_puff.png`]. No identifiable snow burst.
- **Images viewed:** `$G/sheets/s_cyv2EZwzW7A.jpg`, `$G/crops/cyv_md_mid.png`, `cyv_m3_mid.png`, `cyv_md_puff.png`, `cyv_m3_puff.png`, `cyv_m3_icon.png`, `cyv_m1_icon.png`; `$G/sheets/s__7wmOHdRMs4.jpg`, `$G/yt/_7wmOHdRMs4_maxres1.jpg`, `$G/crops/snow_m1_puffs.png`, `snow_m1_cloud.png`, `snow_m1_icon2.png`, `snow_m1_hud.png`; `$G/sheets/snow_icons.jpg`.
- **Depiction for shorts:** A thunk, then a snowball bursts into a lingering curtain of chunky flake-puffs. A second shot clinks harmlessly off the curtain (per the wiki's blocking note). Use white-lavender flakes; that colour is a [BBG News invention] until gameplay confirms violet versus white.
- **Confidence:** partial.

## Sole's Bane (secondary; BBR 1.4.3, Apr 15, 2013 → BBG → HUD icon seen in the Aug and Oct 2026 playtests)
- **Official text:**
  - "Wil doesn't want to share his toys but he's more than happy to share the pain of stepping on one of the buggers." [Game text via wiki]
  - Update note: "-Sole's Bane: Wil leaves a trail of pain with colorful mines that sure to give any opponent a sore foot." [Fan-wiki transcription of SkyVu 1.4.3 notes; Unverified as Canon]
- **2026 status (new):**
  - The orange 2×4 brick icon sits in Wil's secondary slot in InstableGR's "PC Playtest #3 (8/21/26)" maxres3 (build stamp "3.0.2", Frozen Pundra, beside a 100/100 primary) [Observed: `$G/yt/aujTcdFuxdE_maxres3.jpg`, `$G/crops/auj_m3_icon.png`].
  - It is also above the Balance Beam in HKbwq7PolNc maxres1 (build 3.0.7) [Observed: `$G/crops/hkb_m1_icon.png`].
  - The aujTcdFuxdE frame is most likely "Match 5 (Team Battle, Frozen Pundra, B-1000/Botch/Wil)" [Inference from chapters]. The 100/100 primary looks like the Buster Cannon [Inference].
  - The throw itself is not seen in 2026 [Unverified].
- **Look:**
  - An armful heap of studded toy bricks held at the belly [Observed earlier: `$V/png/SolesBane.png`].
  - Re-sampled in "WHACKY SET #7: Will Gameplay - Battle Bears Gold 2.23" (SW, Dec 18, 2015) [Observed: `$G/yt/RukIckwnibs_maxres2.jpg`, `$G/crops/ruk_m2_heap2.png`]: red ≈ #CE1A0E, orange ≈ #E68114, yellow ≈ #D6A323, green ≈ #65B42D, blue ≈ #198CCD.
  - The uploader lists the set as "-Boomstick / -Soles Bane / -Bow and Arrow / -Slowfield / -Ammo+2 / -Melee+2" [fan text].
- **Firing (activation):**
  - "A pile of Lego bricks that Wil throws in the air when activated. It has small AoE … but does a lot of damage." "The throwing effect keeps going on even if the player dies" [Fan-wiki].
  - 50 damage, 4.5 s duration, 3 ammo, 2 s rate of fire [Fan-wiki]. 2.6: duration 4→6, speed modifier 0→10% [Fan-wiki: Versions/2.6].
  - **New:** At HUD **0/2** (both charges spent) Wil still holds the full heap. A single blue 2×2 studded brick (≈ #1794D4) hangs in mid-air at waist height beside him [Observed: RukIckwnibs maxres2]. Two enemies in the doorway carry yellow "Z" icons, which mark the Slow Motion Field ("a yellow 'Z' is displayed above their head" [Fan-wiki: Slow Motion Field]).
  - So the held heap is a fixed prop, and individual bricks spawn and fly when it is used [Inference]. The lone airborne brick is the only throw evidence seen.
  - In Manu's "Chubscout weapon showcase / Doomstick,soles bane,bow" (Jul 5, 2014), a small blue, green and red brick cluster sits at Wil's hip [Observed, low-res: `$G/crops/lg4_hq1_wide.png`, `lg4_sd_low.png`].
- **Projectile / impact:**
  - The floor carpet or "trail of mines" and the step-on trigger are still not seen [Unverified].
  - **Re-assessment of the "pink-violet lightning":**
    - In V6FLnB_c_fk maxres3 (2/3, Oct 3, 2018) the magenta-white burst sits between Wil and an enemy in white-and-blue robot armour holding a purple gun [Observed: `$G/crops/v6f_m3_bolt.png`, `v6f_m3_enemy.png`]. It is probably the enemy's own weapon [Inference].
    - Separately, floor-level magenta crackles at the player's position (≈ #F774F1) appear in hYW93uwB3Hs maxres1 alongside a "POWER UP" kill-feed line, and in rXof_z1BCfI hq1 [Observed: `$G/crops/hyw_m1_buff.png`, `hyw_m1_feed.png`, `rxof_hq1_mid.png`]. These fit the Bearscream Sandwich buff, documented as "a swirling magenta and pink electric ring around the player's body" (`out/verified/combat-vfx.md`, Observed there) [Inference].
    - RukIckwnibs maxres3 shows a violet-white burst where Wil's arm meets a blue-hooded enemy [Observed: `$G/crops/ruk_m3_spark.png`]. Its source is [Unverified].
    - No text gives Sole's Bane any electric effect [Fan-wiki; Game text via wiki]. **Do not draw lightning for Sole's Bane** [Inference].
- **Images viewed:** `$G/sheets/s_RukIckwnibs.jpg`, `$G/yt/RukIckwnibs_maxres2.jpg`, `RukIckwnibs_maxres3.jpg`, `$G/crops/ruk_m2_bricks.png`, `ruk_m2_heap.png`, `ruk_m2_heap2.png`, `ruk_m3_spark.png`; `$G/sheets/s_V6FLnB_c_fk.jpg`, `$G/yt/V6FLnB_c_fk_maxres3.jpg`, `$G/crops/v6f_m3_bolt.png`, `v6f_m3_enemy.png`, `$G/sheets/v6f_hands.jpg` (uninformative); `$G/sheets/s_lG4UEoxgoc4.jpg`, `$G/crops/lg4_hq1_wide.png`, `lg4_sd_low.png`, `lg4_hq1_low.png`; `$G/yt/aujTcdFuxdE_maxres3.jpg`, `$G/sheets/s_aujTcdFuxdE.jpg`, `auj_huds.jpg`, `$G/crops/auj_m3_icon.png`, `auj_m3_hud.png`, `auj_m3_orb.png`.
- **Depiction for shorts:** Wil flings a handful of bright studded bricks (red, orange, yellow, green, blue) out of the heap he keeps hugging. They clatter into a scattered carpet behind him. A chasing bear steps on one, freezes, and hops clutching its foot with a cartoon "!" spark. The carpet layout, hop and spark are a [BBG News invention]; the bricks and their colours are [Observed]. No lightning.
- **Confidence:** partial.

---

## 2026 chapter coverage (what the thumbnails can and cannot show)
- **HKbwq7PolNc** ("Battle Bears Gold - Final PC Playtest (10/15/26)", InstableGR, 1:17:11) [Observed: chapter titles via next API]:
  - maxres1 → Match 1 (Desert Airmine, Wil): Balance Beam [Inference].
  - maxres2 shows a white bear with a rifle (2/4), and maxres3 an overhead gear platform (32/120). Neither is Wil [Observed].
  - Match 5 (17:43) and Match 16 (1:04:35, "Plant the Bomb, Marecraft, Wil") remain unwatched [Unverified].
- **aujTcdFuxdE** ("Battle Bears Gold - PC Playtest #3 (8/21/26)", 52:11):
  - maxres3 → Match 5 (Frozen Pundra): the Sole's Bane icon [Inference].
  - maxres1 and maxres2 show other classes [Observed].
  - Matches 4 (12:33), 9 (34:19) and 12 (47:49) remain unwatched [Unverified].
- **ORYnnvqn19w** (Mingo, 7:29, no chapters):
  - maxres2: Señor Potato.
  - maxres1: a dead Wil at 0/165 with the red-and-white can (1/1) and a "SUICIDE" feed line [Observed].
  - maxres3: a red lance with a checker band (Tillman's by [Inference]).

## Corrections to earlier research files (outside the character file)
1. `out/verified/2026.addendum.md`, HKbwq7PolNc row
   - Current: "a Wil-type long spear-gun (27/70)"
   - Correction: the **Balance Beam**, seen side-on in the HUD. 27/70 = 50 + Ammo +2.
   - Evidence: `$G/sheets/icons_cmp.jpg` (2026 icon vs the 2019 Balance Beam video icon); the white body and gold hex weight in Wil's hands; the magenta beam (`$G/crops/hkb_m1_beam.png`).
2. Gap note
   - Current: "brown potato-shaped object flying beside a white streak, behind Wil"
   - Correction: the spud is leaving the Señor Potato's own barrel, fired by the camera player, a Wil in the white-headed, black-suited Not-So-Slenderman skin [Inference]. The gun's googly eye and red nose are in the foreground.
   - Evidence: `$G/crops/ory_m2_potato.png`.
3. `out/verified/wil.md`, Snowtato
   - Add the Fairy's Dust purple-cloud alternative to the "violet = lingering snow" [Inference].
   - Record clip 5/5 in two videos (2017 and 2018) against the infobox's 6.
4. `out/verified/wil.md`, Sole's Bane
   - Current: "its source is unclear"
   - Correction: probably not Sole's Bane. The V6FL burst sits at an enemy's gun; the floor-level magenta crackles elsewhere co-occur with "POWER UP" (Bearscream Sandwich).
5. `out/verified/wil.md`, Doomstick
   - Add the clip timeline: 2 in 2012–Aug 2013, then 5/5 in 2014 (3 + Ammo +2).
   - Add the white muzzle bloom and the intact kill with three Joules bolts.
6. `research_notes/BBG maps (unverified drafts)/research_space-oddity.md`
   - Add that the trailer's "orange flame sticks … probably … burning fries" now match the BBR Señor Potato footage (ENP2hDgNL_8 maxres2). This remains [Inference].

## Corrections for the character file (`bbg-news-repo/characters/wil.md`)
1. **Weapons & props**
   - Current: "Senor Potato, Pie Bomb, Traffic Light [Fan-wiki]"
   - Correction: "Señor Potato (wiki page title "Senor Potato") [Fan-wiki]. It is seen firing in the Oct 2026 final playtest build 3.0.7: a brown spud in a white-hot trail, plus burning fry stubs [Observed: ORYnnvqn19w maxres2; trailer 30.0–31.6 s]. Also Pie Bomb and Traffic Light [Fan-wiki]. The Balance Beam (magenta beam) and the Sole's Bane HUD icon also appear in 2026 builds 3.0.2–3.0.7 [Observed: HKbwq7PolNc maxres1; aujTcdFuxdE maxres3]."
   - Evidence: `$G/crops/ory_m2_potato.png`, `$G/crops/tr303_fries.png`, `$G/crops/hkb_m1_icon.png`, `$G/crops/auj_m3_icon.png`.
2. **Open questions**
   - Current: "whether 2026 changed his kit, barks or taunts"
   - Correction: "whether 2026 changed his kit (the Señor Potato, Balance Beam and Sole's Bane are present in 2026 playtest builds [Observed]; the Doomstick, Bubble Gun and Snowtato Launcher are unconfirmed), barks or taunts"
   - Evidence: as above.
3. **Look**
   - Current: "The research never describes his BBG trailer card ([Steam][steam]) or the 2026 playtest showcase ([fan upload][showcase]); check both before locking the model."
   - Correction: add that the Oct 2026 build 3.0.7 shows a default-look Wil (red vented helmet; white ribbed tank top with a red ice pop) and a Not-So-Slenderman Wil [Observed: ORYnnvqn19w sddefault and maxres2]. The JustNubz showcase is still unwatched.
   - Evidence: `$G/yt/ORYnnvqn19w_sddefault.jpg`, `$V/png/x_ot_so_slenderman.png`.

## Open questions
- Señor Potato in 2026: how many fries, how long they burn, and whether the spud ever shows flame. The only 2026 frame shows an unburnt spud in a white-hot trail.
- What is the pale ring at the top of ORYnnvqn19w maxres2: an impact ring or something unrelated?
- Doomstick: is there a pellet hit spark? Is the Doomstick in the 2026 build?
- Balance Beam: does the beam visibly change as its damage scales, or with team colour?
- Bubble Gun: what does the pop look like, how long does the dome last, does it block shots, and is it in 2026?
- Snowtato: the snowball in flight; whether the lingering flakes are violet or white (versus Fairy's Dust); clip 5 vs 6; 2026 presence.
- Sole's Bane: thrown overhead or laid as a floor trail? How many bricks, and what is the step-on trigger visual?
- SkyVu's own 1.4.3, 2.6, 2.12 and 2.26 notes (web.archive.org rate-limited or blocked today).
- Unwatched 2026 Wil chapters: HKbwq7PolNc Match 5 (17:43) and Match 16 (1:04:35); aujTcdFuxdE Matches 4 (12:33), 9 (34:19) and 12 (47:49); JustNubz showcase Chub Scout at 28:11. These need a human viewer.


---

<!-- gap pass 2 -->
# Wil: Sarcastic Air Strike (BBH), addendum

This addendum covers one gap: Wil's **"Sarcastic Air Strike"** Ultimate. It exists only in **Battle Bears Heroes (BBH)**, the 3v3 mobile/PC brawler (soft launch May 23, 2023; global launch 2024; still on sale in 2026). It is not in Battle Bears Gold (BBG, 2013–2021) or the BBG 2026 re-release. A short era-guard note on the **BBH Boomstick attack** is included because the same card describes it and it must not leak into BBG depictions.

**Sources reached (Oct 18, 2026):**
- battlebears.com/pages/characters, fetched live today.
- The wiki MediaWiki API: Battle Bears Heroes, Updates, ABBi, Boomstick, Wil, and file info.
- The App Store API, using SkyVu's artist lookup, which returns "BB HEROES: 3v3 Brawl & Royale", id 6479357768, last updated 2026-02-08.
- The Google Play page for com.skyvu.bbh.
- The Steam appdetails API for BBG 2026 (app 4408320).
- YouTube thumbnails from i.ytimg.com, including the maxres1/2/3 frames.
- The YouTube `next` endpoint, for upload dates and descriptions only.
- BlueStacks third-party guides.

**Blocked:**
- YouTube video and storyboards. The `player` endpoint returned LOGIN_REQUIRED "Sign in to confirm you're not a bot" for the IOS and ANDROID_VR clients; the embedded clients returned errors.
- Reddit, which returned 403.

**I did not watch any video.** Every visual claim below comes from a still image I opened.

**Downloads:** /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/

---

## Sarcastic Air Strike (BBH Ultimate; BBH only; reworked June 20, 2023; not in BBG or BBG 2026)

### Official text

**Site text.** "Wil - Scout … Wil's "Boomstick" attack launches explosive pellets that burst on impact, covering a wide area. His Ultimate, "Sarcastic Air Strike," features A.B.B.I., his mocking robot backpack, executing a devastating airstrike, raining destruction across the battlefield." [Canon] (https://battlebears.com/pages/characters, fetched live 2026-10-18; plain straight quotes as above).

**In-game hero card.** I read it in a fan upload's thumbnail (https://i.ytimg.com/vi/Zgplo6qdclk/maxresdefault.jpg and the crop /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/completeness-r3/crops/wil_card.png):
- Text: "Ultimate: "Sarcastic Air Strike" Wil deploys A.B.B.I: his sarcastic robot backpack who carries out a powerful airstrike. A.B.B.I. flies in a straight line across the battlefield, dropping bombs ..." [Observed: game text in a fan frame].
- The card has a "Show More" link; **the rest of the sentence is cut off and was not found anywhere** [Unverified].
- The card spells the name two ways: "A.B.B.I:" then "A.B.B.I.".
- Stats on the card: "DAMAGE PER SECOND 441", "RANGE VERY LONG" [Observed].
- Upload: S8 KBW_Overwatch, "Battle Bears Heroes: Wil but he has explosive shotgun and an A.B.B.i Air Strike", uploaded **Jul 1, 2023**, 5:34 long [Observed: YouTube `next` metadata]. That is the BBH soft-launch build.

**Wiki stats.** The wiki's BBH character table gives "Sarcastic Air Strike", Damage per second "369", Range "Very long", Price "Default (150 Shards)", Release "May 2023" [Fan-wiki] (Battle Bears Heroes page, via the API). The same table quotes this blurb: "The masticator of mayhem, a Chub Scout is always prepared to even the odds for his team…" [Fan-wiki, unsourced].
- **Why the numbers differ:** 441/369 = 1.195 and 538/450 = 1.196 (the attack numbers). Both sets differ by the same factor, so the card was most likely captured at a higher hero level than the wiki's level-1 values [Inference].

### Status and era

- The wiki's Updates page dates the BBH soft launch to **May 23, 2023** [Fan-wiki].
- Version 1.0.27, **June 20, 2023**: "Reworked Wil Attack and Ultimate" [Fan-wiki] (Updates page, via the API).
- **Aug 29, 2023**: "Wil / Reload Speed Reduced by 13% (1.5s to 1.3s)" [Fan-wiki].
- The Jul 1, 2023 video title says "Wil but he has explosive shotgun and an A.B.B.i Air Strike", 11 days after the rework. That suggests the explosive Boomstick and the ABBi air strike are the **post-rework** kit [Inference].
- What Wil's attack and Ultimate were from May 23 to June 20, 2023 is unknown [Unverified].
- The other fan video, S8 KBW_Overwatch "Battle Bears Heroes: Wil Gameplay" (dExPQiFiC1c), was uploaded **May 23, 2023**, so it predates the rework [Observed: metadata].
  - Its 50% frame shows the player as a red-headed bear [Observed: https://i.ytimg.com/vi/dExPQiFiC1c/maxres2.jpg].
  - Its victory frame shows a red luchador-masked bear in the centre slot [Observed: https://i.ytimg.com/vi/dExPQiFiC1c/maxres3.jpg].
  - This is probably Wil in his "Lunchador" skin [Inference; the skin name is Fan-wiki].
- **Still live in 2026:**
  - The App Store BBH listing (updated 2026-02-08) lists "Wil the Chub Scout" [Canon: store text].
  - The site text above is live today [Canon].
- **Not in BBG:** the BBG 2026 Steam text lists "CHUB SCOUT: Wil" and has no Ultimates and no air strike [Canon: Steam appdetails, fetched today]. BBG classes have no Ultimate slot [Inference from the BBG loadout system].

### Look (the caster, ABBi; the strike itself was not seen)

**BBH 2024 key art (official).** Sources:
- Google Play screenshot gp00 (the "Big Indie Pitch WINNER" group shot).
- The official "Battle Bears Heroes TrailerYT 2b with Titles for Google Play" thumbnail (https://i.ytimg.com/vi/POXHAk2bKyo/maxresdefault.jpg; BATTLE BEARS channel, Sep 25, 2024).
- The same art at 4096 px on the wiki (File:BBH_Splash.png).

What the key art shows [Observed]:
- **Shape:** a shield or badge-shaped robot, a rounded inverted triangle, about **0.3× Wil's height**, so roughly 0.27–0.3× Oliver on the BBG News chart. The size is [Inference]: measured on the key art, which has perspective, and Wil's ~0.9× comes from the BBG News chart.
- **Frame:** gunmetal grey, #575F66 lit and #292D31 in shade.
- **Lower plate:** navy, #041333, with **three short yellow-gold bars** (#D2A824 / #CAA933).
- **Lens:** one large glossy camera lens with a blue outer ring (#22548A), a violet-purple iris (#4A4388) and a white glint (#BDC9DF).
- **Placement:** it floats or stands in front of Wil's legs.
- That this robot is ABBi is [Inference]: the wiki says ABBi has "a single camera for an eye", and the robot is paired with Wil.

Wil in the same art wears a red-tinted bubble helmet (#BB0B19) and a white ribbed tank top with a dark-red ice-pop print [Observed]. Whether that is his BBH default or a skin is [Unverified].

Sampled from /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/crops/splash_wil_abbi.png.

**BBH 2023 in-game default (hero card and victory screen).** Brown leather straps cross his shoulders [Observed: https://i.ytimg.com/vi/Zgplo6qdclk/maxres3.jpg; also the official portrait https://cdn.shopify.com/s/files/1/0370/2469/4408/files/Wil_BBH_HeroIcon_1_480x480.png]. ABBi's in-game model on his back is never visible from the front [Unverified]; that the straps belong to ABBi is [Inference].

**Older ABBi designs (do not use for BBH shorts).**
- **BB Zero teaser, 2012, official** [Observed: https://i.ytimg.com/vi/wNDCES4VieM/maxres3.jpg, the third auto-thumbnail, roughly 3/4 through the 53 s video (timing is Inference); crop /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/crops/zero_abbi_arms.png]:
  - a round silver-grey lens housing (#9D9D9B) behind Wil's head, with a cracked cover, a small "ABBi" label and a glowing blue iris slit;
  - two articulated silver arms that end in dark rotary multi-barrel drums (#3D3C42) with cyan indicator lights.
- **BB0 promo art (wiki File:BB0_PROMO.png)** [Observed]: ABBi is a backpack with a jointed white arm holding a lens head with a **green** lens.
- **wiki File:ABBi.png lens close-up** (exact source not verified): the lens rim reads "Warning: Exposure to fat evokes sarcasm" [Observed]. This probably explains the "Sarcastic" name [Inference].

### Firing

- **Slot and type:** it is the Ultimate (charge meter).
- **HUD:**
  - Ultimate button: a gold bear-face emblem in a circle with a cyan charge ring [Observed: https://i.ytimg.com/vi/Zgplo6qdclk/maxres2.jpg; https://i.ytimg.com/vi/JKnjdFW7ISE/maxres2.jpg].
  - Card icon: a yellow tile with a white paw print [Observed: card crop].
- **Launch:** "Wil deploys A.B.B.I" [Game text, Observed in fan frame].
- **Not found:** how ABBi detaches, takes off or returns; any muzzle or launch flash; any sound or voice line [Unverified].

### Projectile

- ABBi herself travels: she "flies in a straight line across the battlefield, dropping bombs ..." [Game text, Observed in fan frame].
- The result is "raining destruction across the battlefield" [Canon].
- Range is "VERY LONG" [Game text] / "Very long" [Fan-wiki].
- Damage is given **per second** (441 / 369), so the strike probably deals damage over time along its path rather than in a single blast [Inference].
- Not found: bomb shape and colour, number of bombs, ABBi's flight height and speed, any trail, and whether a target line is shown before the strike [Unverified].

### Impact / end result

- **No image of the impact was found** [Unverified].
- **Do not use the red discs in Brick Battle frames as reference.** Brick Battle footage shows rows of **three evenly spaced red discs with dark starburst centres**, next to a parallel row of three grey puffs [Observed: official Google Play screenshot captioned "BRICK BATTLE"; official "Brick Battle Championship Match!" thumbnails https://i.ytimg.com/vi/XiMjGoHPNRY/maxres1.jpg (match clock 1:49) and maxres2.jpg (1:27); BlueStacks game-mode image gm_2]. The same layout is still there 22 seconds later, and it appears beside the brick cart in other matches. It is almost certainly a **map feature**, not the air strike [Inference].
- **Nearest observed BBH explosion style (for matching only):**
  - Wil's own pellet impacts are pale cream-yellow crackle bursts, brightest #EEE8C7 [Observed: Zgplo6qdclk maxres2].
  - Big BBH blasts are yellow-white puff clusters inside a thin white ring [Observed: App Store "FAST 3v3 MODES" screenshot; not linked to Wil].

### Images viewed

All files below sit under /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/, given as full paths.

**Crops:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/completeness-r3/crops/wil_card.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/crops/z_maxres2_burst.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/crops/z_boomstick_bbh.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/crops/z_victory_wil.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/crops/d_maxres2_player.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/crops/iph2_game.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/crops/pox_wil.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/crops/splash_wil_abbi.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/crops/abbi_lens_text.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/crops/zero_abbi_arms.png

**Contact sheets:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/sheets/JKnjdFW7ISE.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/sheets/OQrmLlynY1o.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/sheets/0029-TLegLE.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/sheets/ihkXJS4Oatk.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/sheets/8C7JH7STmyo.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/sheets/KLcjIqjf5sc.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/sheets/big1.jpg (4CxQM8F6yh0, g3iAyG1ZGoU, Qun_zUxWwJs, QwEqD3pvLiI)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/sheets/big2.jpg (J7dzsDYZGXw, XiMjGoHPNRY, JM-PUJdxRFc, TcoYL7W38ik, vubyBrDeQmE)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/sheets/official2.jpg (eQBsn_45x5w, b6K9Z9mVskU, DJmrYA9jBG0, i3YCsPjB0_s, lYhRbDXTVLg)
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/sheets/bbh_appstore.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/sheets/gplay.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/sheets/POXHAk2bKyo.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/sheets/bluestacks_cg.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/sheets/bluestacks_tl_gm.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/sheets/abbi_refs.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/sheets/zero_teaser.jpg

**Other images:**
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/img/Wil_BBH_HeroIcon.png
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/img/BBH_Splash_small.jpg
- /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/img/ABBi_in_BBG_small.jpg (a BBG map graffiti of ABBi's eye, not a weapon)

**Thumbnail URLs:**
- https://i.ytimg.com/vi/Zgplo6qdclk/{hqdefault,hq1,hq2,hq3,maxresdefault,maxres1,maxres2,maxres3}.jpg
- https://i.ytimg.com/vi/dExPQiFiC1c/{hqdefault,hq1,hq2,hq3,maxres1,maxres2,maxres3}.jpg
- https://i.ytimg.com/vi/JKnjdFW7ISE/maxres2.jpg
- https://i.ytimg.com/vi/XiMjGoHPNRY/{maxres1,maxres2,maxres3}.jpg
- https://i.ytimg.com/vi/wNDCES4VieM/maxres1-3.jpg

**Thumbnail timing:** YouTube's auto-thumbnails 1/2/3 sit at roughly 25/50/75% of the video [Inference]. For Zgplo6qdclk that is about 1:24 / 2:47 / 4:10; for dExPQiFiC1c about 1:09 / 2:18 / 3:27.

### Depiction for shorts

Use this only in a BBH-labelled short, never in a BBG one.
1. Wil slaps a button and **ABBi** pops up. Draw her as the 2024 key-art robot: gunmetal shield shape, navy plate with three yellow bars, one big violet-blue lens.
2. She rolls her lens and sighs a sarcastic line [BBG News invention].
3. She **flies in a straight line** across the arena and **drops bombs** along the way [Game text].
4. Each bomb pops into a cream-yellow cartoon puff with rainbow confetti. Targets get sooty faces and tumble over, with no injury shown [BBG News invention].

Everything in the bomb design, explosion colour, number of bombs and flight height is [BBG News invention] until someone sees the real flyover.

### Confidence

**documented** (the text and stats are solid). ABBi's BBH look is observed in key art. The strike visuals themselves are **unknown**.

---

## Era guard: Boomstick (BBH Attack; BBH only since the June 20, 2023 rework; not the BBG Boomstick)

### Official text

- "Attack: "Boomstick" Wil's Boomstick fires three explosive pellets in a wide spread. These projectiles explode upon impact producing a small AOE." Card stats: "DAMAGE 3 x 538", "RANGE SHORT" [Observed: game text in fan frame; Zgplo6qdclk maxresdefault, Jul 1, 2023].
- Site text: "Wil's "Boomstick" attack launches explosive pellets that burst on impact, covering a wide area." [Canon].
- Wiki BBH table: "3 x 450", Range "Short", Reload "Very slow" [Fan-wiki].
- Contrast with BBG: in BBG the Boomstick is a 1-round pump shotgun that "releases a powerful, short ranged wave of bullets" [Fan-wiki: Boomstick page]. **Never give the BBG Boomstick explosive pellets.**

### Look (BBH 2023 model)

[Observed: https://i.ytimg.com/vi/Zgplo6qdclk/maxresdefault.jpg; crop /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/crops/z_boomstick_bbh.png]
- **Gun:** a charcoal-black pump shotgun (#212524–#353430), roughly as long as Wil is wide.
- **Receiver:** a row of round vent holes on top and a **red two-digit LED "00" readout** (#9B2815). The same readout appears in the 2012 BB0 promo art [Observed].
- **Barrel:** a ribbed pump grip and a thin cyan light streak along the top.
- **How he holds it:** two-handed, across his belly, in silver-white mitts.
- **Outfit:** gold shell clips on his chest strap (#997842), navy shorts (#242A44), fur #C89039.

### Firing and impact

[Observed: https://i.ytimg.com/vi/Zgplo6qdclk/maxres2.jpg, match clock 1:32; crop /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/wil-airstrike/crops/z_maxres2_burst.png]
- **After a shot:** two pale cream-yellow crackling spark bursts (brightest #EEE8C7) sit 1–2 body-lengths ahead of Wil, and two brass casings eject to his right.
- **Ammo bar:** 3 segments, 2 still full. Reading that as one shot used out of three is [Inference].
- **Ultimate ring:** not full, so these bursts are attack pellets, not the strike [Inference].
- **Aim indicator:** a translucent white wide wedge in front of Wil, which fits the "wide spread" [Observed: JKnjdFW7ISE maxres2 (Gift Wrapped skin, upload Dec 18, 2025); reading it as the Boomstick's aim cone is Inference].

### Depiction for shorts

BBH-labelled only: three glowing pellets fan out and each one pops into a small cream-yellow crackle with confetti. For BBG shorts, keep the plain shotgun blast and pump [Inference].

### Confidence

**partial**.

---

## Corrections for the character file (/home/user/thallo-site/bbg-news-repo/characters/wil.md)

1. **Line 8, canon anchor 2.** Current: `… His Ultimate, 'Sarcastic Air Strike,' features A.B.B.I., his mocking robot backpack, executing a devastating airstrike." [Canon, BBH-era site text]`.
   - Problem: the sentence does not end there. The live text continues ", raining destruction across the battlefield."
   - Also, the elided middle sentence ("Wil's "Boomstick" attack launches explosive pellets…") is **BBH-only**.
   - Correction: quote the full sentence exactly and tag the whole anchor "BBH (2023–) only".
   - Evidence: battlebears.com/pages/characters, fetched 2026-10-18.
2. **Line 61, Fighting.** Current: `ABBi's "Sarcastic Air Strike" [Canon] ([characters][chars]).`
   - Correction: "BBH only (soft launch May 23, 2023; kit reworked June 20, 2023): Wil's Ultimate "Sarcastic Air Strike", in which "Wil deploys A.B.B.I…" who "flies in a straight line across the battlefield, dropping bombs" [Game text, fan frame]. It does not exist in BBG or BBG 2026."
   - Evidence: the card in Zgplo6qdclk maxresdefault; the wiki Updates page; the Steam appdetails.
3. **Line 54, Weapons & props.** Current: `default Boomstick [Fan-wiki] ([Chub Scout (BBG)][ws]), named in BBH [Canon] ([characters][chars]);`
   - Correction: add "The BBH Boomstick fires three explosive pellets (small AOE) [Game text]; the BBG Boomstick is a 1-shell pump shotgun 'wave of bullets' [Fan-wiki]. Do not mix them."
   - Evidence: card crop; wiki Boomstick page.
4. **Line 53, ABBi.** Current: `a single camera eye [Fan-wiki] ([ABBi][wabbi]); probably the Zero teaser's one-eyed, minigun-armed unit [Observed; Inference].`
   - Correction: split the design by era.
     - BB Zero 2012: a round silver lens housing with a cracked cover and an "ABBi" label, mounted behind Wil's head, with two articulated arms ending in rotary multi-barrel drums [Observed: wNDCES4VieM maxres3].
     - BBH 2024: a gunmetal shield-shaped robot with a navy plate, three yellow bars and one violet-blue lens [Observed: official key art, Google Play screenshot, POXHAk2bKyo thumbnail; identifying it as ABBi is Inference].
5. **Line 51, Colours.** Current: `ABBi grey #8B9299` (labelled an unsampled pick).
   - Correction: for BBH content, use sampled key-art values: frame #575F66 / #292D31, plate #041333, bars #D2A824, lens ring #22548A, iris #4A4388.
   - Keep #8B9299 only as a [BBG News invention] for the unobserved BBG backpack.
6. **Line 76, Prompt pack** (optional). Current: `compact grey robot backpack with one camera-eye lens`. This is fine for BBG. For any BBH-labelled prompt, add "shield-shaped gunmetal drone, navy lower plate with three yellow bars, large violet-blue lens".

## Open questions

- What is the full "Show More" text of the Sarcastic Air Strike card (how many bombs, any slow or knockback)?
- What does the flyover actually look like: does ABBi detach from Wil, what is her flight height and speed, is a target line shown, what do the bombs and explosions look like and what colour are they, how long does it last? This needs a logged-in viewer for Zgplo6qdclk (5:34) or JKnjdFW7ISE (15 min).
- What were Wil's BBH attack and Ultimate before the June 20, 2023 rework? (dExPQiFiC1c, May 23, 2023, should show the old kit.)
- Is the 2024 key-art shield-drone ABBi also the in-game BBH model, and is the bubble helmet with ice-pop tank top his BBH default or a skin?
- Does ABBi have a voice line in BBH? Leah Smith is credited for ABBi only in BBR.
- What are the rows of three red discs in Brick Battle maps? Map hazard, spawn pads, or the store text's "Angry Bombs"?
- The BlueStacks tier list calls Wil "the best long-range hero" with "precision shot" and "camouflage". That contradicts SkyVu's card ("RANGE SHORT") and should be treated as unreliable [Inference].
