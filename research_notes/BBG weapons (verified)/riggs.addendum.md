<!-- gap pass 1 -->
# Riggs (Heavy): gap addendum (2026 kit evidence; projectiles and impacts for nine weapons)

This addendum covers only the gaps flagged for topic "riggs":
- the "2026 evidence for the Heavy kit" sub-topic;
- projectile and impact evidence for Zombee Gun, Provolowned, Big Iron, Flame Thrower, Plasma Orb, Freeze Blast, Sucker Punch, Field Medic and Bounce Lazer.

The 2026 sub-topic also identifies the gun seen in the droid BBG video: it is the Electric Honey.

**Sources reached today (2026-10-18)**
- **YouTube metadata** for the 24 named videos, via the innertube `next` endpoint: title, channel, date, description and chapters.
  - Durations come from the innertube search endpoint: CmYil-JJdC0 4:07; HKbwq7PolNc 1:17:11; aujTcdFuxdE 52:11.
  - The `player` endpoint returns LOGIN_REQUIRED, so **no video was watched**.
- **Thumbnails** for all 24 videos (maxresdefault/sddefault, maxres1–3 or sd1–3, hq1–3).
- **Chapter frames:** signed `hqdefault_<ms>.jpg` chapter thumbnails for aujTcdFuxdE and -lAtv-j9Sms. HKbwq7PolNc's chapter thumbnails are all the generic hqdefault, so they show nothing about its Riggs chapters.
- **Fan wiki (MediaWiki API):** pages Beebeegun, Electric Honey (BBG), Zombee Gun, Provolowned, Big Iron, Flame Thrower, Plasma Orb, Freeze Blast, Sucker Punch, Field Medic, Bounce Lazer and Heavy (BBG).
- **Not used:** no official SkyVu page adds weapon visuals beyond the main dossier. Every "Official text" line below is the in-game description as quoted by the wiki.

**Evidence conventions**
- **Folder:** all local files are under E = `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-gaps-r2/`.
  - `E/thumbs/<id>_<variant>.jpg` is a byte copy of `https://i.ytimg.com/vi/<id>/<variant>.jpg`.
  - `E/crops/*.png` are my crops of those files.
  - `E/chthumbs/*.jpg` are chapter frames.
  - I downloaded every file myself into this new folder. The earlier, unfinished `dl/riggs-gaps/` attempt was not used as evidence.
- **Thumbnail types:**
  - **maxres1/2/3** are YouTube auto-generated frames. Their exact timestamps are unknown. In the playtest videos they do not fall at 25/50/75% of the running time.
  - **maxresdefault/sddefault** is the uploader's chosen ("custom") thumbnail, which may carry overlays or edits.
  - **Chapter frames:** the number in `hqdefault_<n>.jpg` is read as a timestamp in milliseconds [Inference]. It is always a few seconds after the chapter start; for example, 1820133 falls in the chapter that starts at 30:10.
- **Colours:** hex codes are my samples (hue-filtered medians), not official codes [Observed, sampled].
- **Scale:** sizes use the BBG News scale chart (Oliver = 1.0x, Riggs ≈ 1.2x) [BBG News invention].

---

## Sub-topic: 2026 evidence for the Heavy kit (all slots; 2026 re-release playtest builds 3.0.2 and 3.0.7)

**Correction:** the main dossier says "No 2026 footage of any Heavy weapon firing has been seen". That is now out of date. 2026 playtest frames show five Riggs weapons: the Electric Honey, Flame Thrower, Zombee Gun, Bounce Lazer and Provolowned. Only one image, an uploader's custom thumbnail, shows a Heavy weapon actually firing.

### Videos and builds

| Video | Uploader / date | Build stamp read from frames |
|---|---|---|
| CmYil-JJdC0, "I Faced an ENTIRE TEAM of OLIVER PROS Using RIGGS… (Battle Bears Gold)" | droid BBG, Oct 16 2026, 4:07 | "3.0.7_2026.11.19_b7 / 260867" [Observed: E/crops/cm_stamps.png, from maxresdefault and maxres1–3]. The gap note's reading "3.6.7" is wrong. |
| HKbwq7PolNc, "Battle Bears Gold - Final PC Playtest (10/15/26)" | InstableGR, Oct 17 2026 | "3.0.7_2026.11.19_b7 / 33152" [Observed: E/crops/auj_stamps.png, from HKbwq7PolNc_maxres1] |
| aujTcdFuxdE, "Battle Bears Gold - PC Playtest #3 (8/21/26)" | InstableGR, Aug 21 2026 | "3.0.2 / 33152" [Observed: E/crops/auj_stamps.png] |

The second line of the stamp differs per uploader, so it is probably a player or account number [Inference].

InstableGR's Oct 17 description [fan text, quoted]:
> "We got skins for Riggs, Wil, and Huggable inspired by the classic games and two new weapons for Astoria"

and:
> "a public demo will be available on Steam for a few days starting October 19th as part of Steam Next Fest"

### The gun in CmYil-JJdC0 is the Electric Honey (BBG), not the Beebeegun
- **HUD icon:** a black minigun with violet-lit slat panels, a pink striped hive with a pink tube, and three violet ring-spikes at the barrel. This is the Electric Honey icon. The ammo counter reads "93 /120" [Observed: E/crops/cm_max_hud.png from https://i.ytimg.com/vi/CmYil-JJdC0/maxresdefault.jpg].
- **Wiki stats:** Electric Honey "Ammo 120" and Beebeegun "Ammo 100" [Fan-wiki].
- **Health:** the HUD health bar maxes at 200 ("176/200", "106/200", "115/200", "164/200") [Observed]. That fits the Electric Honey, which has no health modifier; the Beebeegun's "+10% Health" would give 220 [Fan-wiki].
- **Verdict:** Electric Honey [Inference, strong].

### What each Riggs frame shows

**droid BBG, CmYil-JJdC0 (Oct 2026)**
- **Skin:** cel-shaded white fur (#E8EBEC) with black outlines [Observed].
- **HUD portrait:** a white bear face with bared, gritted teeth [Observed]. It matches the "NO MORE MR ICE GUY" icon in the 2026 skin menu, so the skin is probably No More Mr Ice Guy [Inference: E/crops/skin_compare2.png].
- **Auto frames maxres1–3:** all three show "0 /120" and RELOAD, so none shows Riggs firing [Observed].

**InstableGR, aujTcdFuxdE (Aug 2026)**
- **Match 1 frame, 0:11.9** (Kill Confirmed, Sky Pirates):
  - default Riggs with a blue armoured round back-shell, holding the Flame Thrower: a red can labelled "Coff…" on a grey grip [Observed, 336 px: E/chthumbs/auj_11866.jpg, E/crops/auj_m1_up.png]
  - HUD ammo "60 / 6?" with a red-can gun icon; health bar reads 240/240 [Observed, low-res]
- **Match 8 frame, 30:20.1** (Team Battle, Sky Pirates):
  - HUD "252 / 3??" with a dark-gun-and-green-topper icon; health 200/200 [Observed, low-res: E/chthumbs/auj_1820133.jpg, E/crops/auj_m8_up.png]
  - this fits the Zombee Gun (300 ammo [Fan-wiki]) [Inference]
  - the visible gun part is white with a red band; I could not reconcile it with the known Zombee Gun model [Unverified]
- **Match 10 frame, 38:31.1** (FFA, Space Oddity):
  - Riggs in red, health 200/200, HUD "32 / 32" with a blaster-and-pink-head icon, which is the Bounce Lazer (32 ammo [Fan-wiki])
  - a big green kill banner, "NAMEY" [Observed, low-res: E/chthumbs/auj_2311066.jpg, E/crops/auj_huds.png]
- **Auto frame maxres1** (Sky Pirates):
  - default Riggs at "79/240" health with "0 / 1" and RELOAD over a pink icon [Observed: E/crops/auj_m1_riggs.png]
  - this may be a 1-round Sucker Punch [Inference, weak]

**JustNubz, -lAtv-j9Sms (Sep 2026), Heavy chapter frame at 9:06.8** [Observed, 336 px: E/chthumbs/nubz_546800.jpg, E/crops/nubz_heavy_up.png]
- The skin menu lists:
  - "B AND J"
  - "ROCKY HORROR BUY NOW! 250"
  - "LAWYER RIGGS BUY NOW! 300"
  - "NO MORE MR ICE GUY BUY NOW! 50"
- Rocky Horror Riggs, in red cracked rock, holds the Provolowned: a cheese block with a white grater barrel.

**InstableGR, HKbwq7PolNc (Oct 2026)**
- **Riggs chapters:** Matches 1, 8, 9, 10 and 13 per the description. No frame of them was reachable: the chapter thumbnails are generic, and auto frames maxres1–3 show other classes (135 HP, 90 HP and a 120-HP engineer-style portrait) [Observed: E/crops/hk_huds.png].
- **Custom thumbnail:** a 3D render of a pale cyan-furred Riggs in ripped red trousers asleep before a red-cross medic tent, with the Provolowned lying across him, two pink faceted Huggables and a bear-logo box [Observed: E/crops/hk_max.png].
  - The render's origin is unknown; it may be 2026 loading art [Unverified].
  - The "Playtest 5" overlay is InstableGR's.

### Images viewed
- `E/grids/grid_CmYil-JJdC0.jpg`, `E/grids/grid_HKbwq7PolNc.jpg`, `E/grids/grid_aujTcdFuxdE.jpg`
- Crops of `https://i.ytimg.com/vi/CmYil-JJdC0/{maxresdefault,maxres1,maxres2,maxres3}.jpg`: cm_stamps, cm_m2_gun, cm_m1_full, cm_m1_right, cm_max_left, cm_max_hud
- HKbwq7PolNc: hk_huds, hk_max
- aujTcdFuxdE: auj_m1_riggs, auj_stamps
- Chapter frames: `E/crops/auj_chapters.png`, `E/crops/auj_huds.png`, auj_m1_up, auj_m8_up, nubz_heavy_up
- Skin comparisons: skin_compare, skin_compare2

### Depiction for shorts
A 2026-accurate Riggs short can show any of these five weapons in hand:
- Electric Honey (the safest choice)
- Flame Thrower can
- Zombee Gun
- Bounce Lazer
- Provolowned

Caption Electric Honey and Blood Spurt effects from the Steam trailer as 2013 footage.

**Confidence:** observed (that the weapons are in the 2026 build); partial (2026 firing effects).

---

## Electric Honey (BBG) (primary; original BBR 2012; 120 ammo per wiki; confirmed in the Oct 2026 playtest build)

- **Official text:** "Electrically charged bees are slightly smaller* allowing for a higher bees-per-hive ratio and thus longer continuous fire!" [Game text via wiki] (Electric Honey (BBG) page). The wiki notes "The Electric Honey used to have 140 ammo before it was nerfed in v2.6" [Fan-wiki].

**Look in 2026, first-person (CmYil-JJdC0 maxres2)** [Observed: E/crops/cm_m2_gun.png; colours sampled]
- **Body:** a charcoal-black boxy body (#282828–#383838).
- **Hive:** a glowing pink faceted hexagonal "hive" (≈#C145A5) with a paler centre. The gap note called this a "hexagonal coil".
- **Rings:** two or three violet energy rings (≈#AD54E3) hovering around it.
- **Tube:** a purple-and-blue banded tube (≈#8333BA) coiled down the right side.

**Same model in earlier eras**
- **Nov 2015 (BBG 2.22):** DiZ2hZ56Ylc maxres3 shows the same pink hexagonal hive with magenta rings on a black gun. Its HUD reads "/70", which does not match the wiki's 120 [Observed: E/grids/grid_DiZ2hZ56Ylc.jpg].
- **Sep 2016 (2.25.3):** an enemy Riggs carries the same glowing pink-hive gun [Observed: E/crops/bl_z8_fire.png].
- **Conclusion:** the 2026 model is the classic BBG model [Inference, strong].
- **Size:** it shares the Beebeegun mesh, about 0.7x Riggs (≈0.85x Oliver), per the main dossier; I did not re-measure it [Inference].

**Firing**
- **2015:** a pink-white glow at the hive while firing (HUD 51/70) [Observed: DiZ2hZ56Ylc maxres1 in the grid].
- **2026:** the uploader's custom thumbnail shows violet-pink branching lightning bolts (#C65DDA / #E574D0) crackling from the muzzle along the floor and up to the target, with ammo at 93/120 [Observed: E/crops/cm_max_left.png]. Because this is a custom thumbnail with a title overlay, added effects cannot be ruled out [Unverified].
- **The magenta beam in maxres1** is real: a long straight #E838F8 line ending in a pink-white glow at the bottom-right corner [Observed: E/crops/cm_m1_full.png].
  - It does not come from Riggs's muzzle, which is at the centre.
  - Riggs's HUD shows 0/120 and RELOAD at that moment.
  - So it is **not** his Electric Honey shot [Inference, strong]. Its source is [Unverified].

**Projectile**
- Wiki: hitscan minigun [Fan-wiki].
- 2026 custom thumbnail: no discrete bullets, only lightning arcs [Observed, possibly edited].

**Impact / end result**
- In the custom thumbnail, purple lightning bolts wrap the target (a red-marked enemy) [Observed].
- A pink-white crossed "X" spark flash hangs mid-air in front of the target [Observed].
- No explosion is shown.
- This fits the main dossier's 2013 trailer hit: a "starburst of long pink-magenta triangular shards".

**Images viewed:** E/crops/cm_m2_gun.png, cm_max_left.png, cm_max_hud.png, cm_m1_full.png, cm_m1_right.png; E/grids/grid_DiZ2hZ56Ylc.jpg; E/crops/bl_z8_fire.png

**Depiction for shorts:** a black minigun with a glowing pink hexagon hive and two orbiting violet rings. Show short violet lightning forks and a pink "X" sparkle on the target, then the target blinks and stumbles. Thicker lightning is [BBG News invention].

**Confidence:** observed (look); partial (firing).

---

## Zombee Gun (primary; original BBR 2012; changed in BBG 2.6; HUD consistent with it in the Aug 2026 playtest)

- **Official text:** "Most of the damage this weapon deals is psychological." [Game text via wiki]
- **Wiki:** "fires a continuous stream of what appears to be ground-up zombie Huggables"; 4.5 damage, 300 ammo, range 1000 [Fan-wiki].

**Look**
- **Topper:** a lime-green Huggable with leaf antennae sits on top of the gun, seen over Riggs's shoulder (Mar 2014) [Observed: E/crops/zg_qh_m3.png].
- **Ammo by era:**

| Date | Video | HUD ammo |
|---|---|---|
| Mar 2014 | qhSvn5iz1R0 | x/125 |
| Dec 2018 | AiTpe-gA9EE | 65/104 and 100/104 |
| Aug 2026 | aujTcdFuxdE, Match 8 | 252/3?? |
| Wiki | (current state) | 300 |

  [Observed: E/grids/grid_qhSvn5iz1R0.jpg, E/crops/zg_ai_max_hud.png, E/crops/auj_m8_up.png]. The counts vary by era, and equipment is not visible [Inference].

**Firing**
- Automatic. AiTpe-gA9EE was uploaded Dec 21 2018 by bearpantsbb. Its description says "Game is 'Battle Bears Royale'", but the HUD is BBG-style.
- maxres1 shows a dense cone of mixed chunks bursting from the muzzle and streaming to a target about 10 m away [Observed: E/crops/zg_ai_m1.png].

**Projectile** [Observed, sampled]
- flat dark-red splat blobs (≈#8D2221)
- lime-green blocky chunks and small round grinning lime-green Huggable heads (≈#75DC3E)
- a few small white bone-shaped bits
- a glowing yellow-green stream (≈#DDE858) over the last stretch to the target

**Impact / end result**
- The target, a grey bear on a lit platform, sits in a burst of yellow-green glow with pale chunks around it [Observed].
- The custom thumbnail (65/104, "KILLS +25 +100 STREAK +30") shows red splats and green Huggable bits around a red-armoured enemy [Observed: E/grids/grid_AiTpe-gA9EE.jpg].
- A kill shows the victim's name in big green letters ("WCS LOTUS", "STRAWBERRY") [Observed].
- The victim's death animation is not visible [Unverified].

**Images viewed:** E/grids/grid_AiTpe-gA9EE.jpg, E/crops/zg_ai_m1.png, E/crops/zg_ai_m3.png, E/crops/zg_ai_max_hud.png; E/grids/grid_qhSvn5iz1R0.jpg, E/crops/zg_qh_m3.png; E/grids/grid_gmCWU3DXBwI.jpg (no clear Zombee fire); E/crops/auj_m8_up.png

**Depiction for shorts:** keep the lime-green grinning mini-Huggable heads and the yellow-green stream. Replace the dark-red splats with lime-green slime and rainbow confetti so nothing reads as blood [BBG News invention].

**Confidence:** observed (2018 spray); partial (2026).

---

## Provolowned (primary; BBR 1.3.1 week 1, 2012; changed in BBR 1.4.2 and BBG 2.6; on the Sep 2026 playtest menu)

- **Official text:** "The list of dangers associated with over consumption of cheese just got a little bit longer. Four cheese blend your opponents into a quivering mass of curdled shame!" [Game text via wiki]
- **Wiki:** "small flies circling its circular cheese"; 100 ammo; 7.5 damage; a long wind-up [Fan-wiki].

**Look**
- **HUD icon (Jan 2014):** a silver grater barrel with slots, a cheese-block body with dark specks and an orange stock [Observed: E/crops/pv_4s_icon.png].
- **Sep 2026:** held at the hip by Rocky Horror Riggs on the skin menu; it reaches roughly from hip to knee, about 0.4–0.5x Riggs (≈0.5–0.6x Oliver) [Observed, approximate, 336 px: E/crops/nubz_heavy_up.png].
- **Render:** it also appears in the HKbwq7PolNc render [Observed: E/crops/hk_max.png].
- **Ammo:** x/80 in Jan 2014 (4SS31gsEkGg); x/130 in Jan 2016 (0xeOw6dCb3c), which equals 100 plus Ammo +2 [Observed; equipment Inference].

**Firing and projectile**
- **Jan 2014 (4SS31gsEkGg maxres2):** short, fat, glowing bright-yellow capsule tracers (≈#FEEE4F) fly from the muzzle to the target, with a pale pink-white glow at the spinning barrel [Observed: E/crops/pv_4s_m2.png].
- **Jan 2016 (0xeOw6dCb3c custom thumbnail, 51/130):** one thin straight pale violet-pink line runs from Riggs's gun into the distance [Observed: E/crops/pv_0x_max.png].
  - maxres3 shows similar rainbow-fringed thin lines while his ammo is full (130/130) [Observed: E/crops/pv_0x_m3.png].
  - So at least some of those lines are other players' fire [Inference]. The thin line is a Provolowned tracer only by [Inference, weak].

**Impact / end result**
- A yellow spiky starburst with a small cyan flash at the target (Jan 2014) [Observed].
- No cheese chunks or flies were seen [Unverified].

**Images viewed:** E/grids/grid_4SS31gsEkGg.jpg, E/crops/pv_4s_m2.png, pv_4s_icon.png; E/grids/grid_0xeOw6dCb3c.jpg, E/crops/pv_0x_m3.png, pv_0x_max.png; E/crops/nubz_heavy_up.png, hk_max.png

**Depiction for shorts:** spin up the grater barrel, then hose out stubby yellow cheese-coloured tracers that pop as yellow starbursts. Tiny cheese crumbs and the circling flies are [BBG News invention]; the flies are [Fan-wiki] but were not seen.

**Confidence:** observed (2014 tracers); partial.

---

## Big Iron (primary; BBR 1.3.2, Aug 24 2012; changed in BBG 2.6; 2026 unverified)

- **Official text:** "That's a big gun you have there pardner." [Game text via wiki]
- **Wiki:** 6 rounds, 50 damage, projectile at 2,000 u/s; "From the target's perspective, the bullet doesn't actually appear unless fired from some distance away" [Fan-wiki].

**Look**
- A grey revolver, held two-handed at chest height and aimed forward [Observed: E/crops/bi_bf_max.png (Mar 2014), E/crops/bi_tx_max.png (Feb 2016)].
- The Mar 2014 HUD icon is a revolver with a red grip [Observed: E/grids/grid_bfIxtDq-mpo.jpg].
- **Ammo:** /10 in 2014 (6 plus Ammo +2 = 10 [Inference]); /6 in 2016 [Observed].

**Firing**
- Semi-auto.
- Feb 2016 custom thumbnail (gameplay with text overlays): a yellow 4–5-point star muzzle flash at the barrel tip [Observed: E/crops/bi_tx_max.png; sampled ≈#BDBB38, mixed with background, reads mustard-yellow].
- Mar 2014: only a small red glow at the muzzle tip [Observed].

**Projectile:** never visible in any frame [Unverified], which fits the wiki's note.

**Impact / end result**
- **Feb 2016 custom thumbnail:** a big white smoke-puff cloud bursts on the target, a teal-armoured bear, with a small pink blob [Observed].
- **maxres3:** a white puff and a green floor glow at a target's feet at 0/6 [Observed: E/crops/bi_tx_m3.png].
- Whether these puffs are bullet hits or another effect is [Inference, moderate].
- Several targets in these frames also carry the Sucker Punch stun icon (see Sucker Punch), so the video pairs stun with Big Iron.

**Images viewed:** E/grids/grid_bfIxtDq-mpo.jpg, E/crops/bi_bf_max.png; E/grids/grid_TXaY9-RBh6U.jpg, E/crops/bi_tx_max.png, bi_tx_m3.png, bi_tx_m1.png

**Depiction for shorts:** a cowboy-style quick-draw with a yellow star muzzle flash, then an instant white "poof" cloud on the target, with no visible bullet. The comedic recoil is [BBG News invention].

**Confidence:** observed (muzzle flash and puff); partial (projectile).

---

## Flame Thrower (primary; BBG 2.14, Nov 29 2014; seen in hand in the Aug 2026 playtest)

- **Official text:** "Burn your enemies with the power of hot morning coffee without the lawsuit!" [Game text via wiki]
- **Wiki:** "Similar to the Cosmic Fire, it will shoot red-colored flames"; 40 ammo [Fan-wiki].

**Look** [Observed]
- A tall red can whose yellow-orange label starts "Coff…", so it is a coffee can, on a grey grip, held upright.
- Seen in Apr 2016 (E/grids/grid_9uOVYSOvCaQ.jpg; E/crops/ft_9u_m1.png) and in Aug 2026 (E/crops/auj_m1_up.png, 336 px).
- **Ammo:** /30 in 2016; 60/6? in 2026 [Observed; the reason for the difference is Inference].

**Firing and projectile**
- Not seen.
- The gap note said a "pale stream" appears in 9uOVYSOvCaQ hq1. That image is maxres1, and its HUD reads **30/30 (full)**.
- The pale cream shard rays there (long tapering white-cream spikes behind an enemy Riggs) are therefore not Flame Thrower output [Inference, strong; Observed: E/crops/ft_9u_m1.png].
- The flame colour remains [Fan-wiki] only.

**Impact / end result:** undocumented [Unverified].

**Images viewed:** E/grids/grid_9uOVYSOvCaQ.jpg, E/crops/ft_9u_m1.png, E/crops/auj_m1_up.png, E/chthumbs/auj_11866.jpg

**Depiction for shorts:** a red "Coffee" can sprays a short red-orange flame cone with coffee-steam puffs. Targets come away soot-faced, with smoke curling off their ears. Everything beyond "red-colored flames" is [BBG News invention].

**Confidence:** partial.

---

## Plasma Orb (secondary; BBR 1.3.1, 2012; −10% Health removed in BBG 2.6; 2026 unverified)

- **Official text:** "The amount of voltage this gun produces is just enough to turn anything it touches into a smoldering husk of its former self... is that enough you think?" [Game text via wiki]
- **Wiki:** "releases a spreading blast of purple electricity"; 2 ammo [Fan-wiki].

**Look**
- **Feb 2016 (AHgOlXZi6oo custom thumbnail; HUD 1/2):** held upright with a black barrel and a violet-lit glass section, and a big dark faceted globe containing white and blue-violet lightning inside a magenta-violet glow (sampled purple ≈#7C49A2) [Observed: E/crops/po_ah_max.png].
  - The video's title says "Field Medic", but the frame shows the Plasma Orb.
- **Jan 2014 (Xn6pGIr94vA):** the globe with violet-white crackle at the bottom of the frame; HUD 2/2 [Observed: E/crops/po_xn_max.png].

**Firing**
- Just after a shot (1/2), a white spiky starburst (≈#FFF6FF) flares at the globe's lower edge [Observed].
- The spreading purple blast in flight was not seen [Unverified].

**Impact / end result: the gap note's "green lightning" is the Shields special, not the Plasma Orb**
- 9uOVYSOvCaQ maxres3 (HUD 0/2) shows the target wrapped in a yellow-green glow with yellow heater-shield icons bearing green crosses [Observed: E/crops/po_9u_m3.png].
- The same shield-and-cross icon appears beside the word "SHIELDS" in the kill feeds of cDg2nI7ghMM sd3 and TXaY9-RBh6U [Observed: E/grids/grid_cDg2nI7ghMM.jpg, E/grids/grid_TXaY9-RBh6U.jpg].
- So that effect is the Shields special [Inference, strong].
- **Unattributed purple clouds:** AiTpe-gA9EE maxres3 shows lumpy violet puff clouds with dark spots around Riggs, with a 3-round secondary at 0/3. The uploader's hashtags include "#PlasmaOrb". The puffs look like the main dossier's Mother of Nature poison clouds [Observed: E/crops/zg_ai_m3.png]. Attribution is [Unverified].

**Images viewed:** E/grids/grid_AHgOlXZi6oo.jpg, E/crops/po_ah_max.png; E/grids/grid_Xn6pGIr94vA.jpg, E/crops/po_xn_max.png; E/crops/po_9u_m3.png; E/grids/grid_cDg2nI7ghMM.jpg

**Depiction for shorts:** the globe crackles, a white flash bursts at the muzzle, then a short fan of purple lightning lights the target up so its outline shows briefly, and it ends as a smoking, frazzled-fur "husk" with no injury. The fan shape follows the [Fan-wiki]; the frazzle is [BBG News invention].

**Confidence:** observed (look and muzzle flash); unknown (blast and impact).

---

## Freeze Blast (secondary; BBG 2.12, Oct 2 2014; 2026 unverified)

- **Official text:** "Blastin you with FREEEZEEEEE!!!" [Game text via wiki]
- **Wiki:** "fires small blue projectiles in an arc. On contact, these projectiles split and form damaging pools on the floor, similar to the Gernobyl. Enemies who step in the pools will be slowed down severely"; 5 ammo [Fan-wiki].

**Look**
- In the Sep 2016 loadout menu (version stamp "2.25.3 6760382"), the SECONDARY row reads "FREEZE BLAST" [Observed: E/crops/z8_menus.png].
- Its icon is a long pale-cyan icy gun with a teal block [Observed].
- No in-match frame shows it.

**Firing, projectile and impact:** not seen in any thumbnail of z8GcYdFIdBI [Unverified]. The wiki's description is the only source.

**Images viewed:** E/grids/grid_z8GcYdFIdBI.jpg, E/crops/z8_menus.png

**Depiction for shorts:** lob small glowing blue pellets in an arc. Each splits into a pale-blue frost puddle that freezes feet in place, with a slow-motion wobble. The colours and pool look are [BBG News invention] beyond the wiki text.

**Confidence:** unknown (effects); documented (text).

---

## Sucker Punch (secondary; original BBR 2012; ammo changed 1 → 6 → 3; a pink-icon 1-round secondary appears in the Aug 2026 playtest)

- **Official text:** "Lobs a projectile that will stun the target for a few seconds." [Game text via wiki]
- **Wiki:** "lobs a small, pink Huggable-like head"; "a blue Nuggs will appear over the player's head"; 2.6 s stun; 1,000 u/s [Fan-wiki].

**Look in hand**
- A grey launcher held muzzle-up, with three orange-and-black chevron bands and a pink faceted tip (the head) [Observed: UezzJrZ3u2I maxres1 (Sep 2013); E/crops/sp_ne_m2.png (Sep 2015)].
- The 2016 menu icon shows a pink Huggable head on the front of a grey box launcher with orange stripes [Observed: E/crops/z8_menus.png].

**Ammo eras** [Observed]
- x/1 in Sep 2013 (UezzJrZ3u2I), matching the wiki's original 1 round
- x/6 in Sep 2015 (neIf26qQkI4)
- possibly 0/1 in Aug 2026 (pink icon) [Inference, weak]

**Firing and projectile in flight**
- **Jul 2013 (0JnOxZH5XAc sd1):** a soft lime-green glow (≈#97ED2E) at the muzzle of the upturned pink-and-orange launcher [Observed, low-res: E/crops/sp_0j_sd1.png]. A small pink speck near a red-team target appears in sddefault [Observed, low-res: E/crops/sp_0j.png].
- **Sep 2015 custom thumbnail:** a pixelated pink Huggable head with a toothy open mouth and a yellow-orange flame trail, launched from a grey device [Observed: E/grids/grid_neIf26qQkI4.jpg]. Whether this is in-game or fan-made is [Unverified].

**Impact / end result**
- **Sep 2015 (maxres2, 3/6):** a pink-violet sparkly burst (≈#EE7EE0 / #D768E6) around a small pink object just in front of the enemy [Observed: E/crops/sp_ne_m2.png]. Reading this as the head at impact is [Inference].
- **Feb 2016 (TXaY9-RBh6U):** the stun icon over stunned targets: a blue Nuggs bird with a white crest, flanked by grey-white curved spin arcs. One target also sits in a yellow glow with star sparkles [Observed: E/crops/bi_tx_max.png, E/crops/bi_tx_m1.png]. This matches the [Fan-wiki] blue Nuggs.
- **Sep 2013 (maxres3, 0/1, just after "KILLS +25 +100"):** many pale-pink puff particles scattered in an arc through the air and a magenta-glowing object on the floor [Observed: E/crops/sp_ue_m3.png]. These could be the head and its trail (the wiki says the head "remain[s] intact") or a kill effect [Unverified].

**Images viewed:** E/grids/grid_0JnOxZH5XAc.jpg, E/crops/sp_0j.png, sp_0j_sd1.png; E/grids/grid_neIf26qQkI4.jpg, E/crops/sp_ne_m2.png; E/grids/grid_DiZ2hZ56Ylc.jpg (no Sucker Punch seen); E/grids/grid_UezzJrZ3u2I.jpg, E/crops/sp_ue_m3.png; E/crops/bi_tx_max.png, bi_tx_m1.png; E/crops/auj_m1_riggs.png

**Depiction for shorts:** "thoonk": a pink grinning Huggable head arcs out with a pink sparkle trail and bonks the target in a pink-violet sparkle burst. The target freezes mid-pose under a spinning blue bird with white spin arcs for about 2.6 s. The sparkle trail is [BBG News invention].

**Confidence:** observed (stun icon); partial (projectile).

---

## Field Medic (primary; BBR 1.3.1 week 4, Jul 2012; health penalty changed in BBG 2.6; 2026 unverified)

- **Official text:** "You ever wonder where the military stores all of its amputated limbs? Wonder no longer! Covering your head and fleeing is probably the best thing to do now." [Game text via wiki]
- **Wiki:** "fires a continuous stream of amputated limbs"; 40 ammo, range 850 [Fan-wiki].

**Look**
- A teal Huggable in an olive army helmet on top [Observed: xy-JjHD0k1s custom render and maxres2, E/grids/grid_xy-JjHD0k1s.jpg; cDg2nI7ghMM, E/grids/grid_cDg2nI7ghMM.jpg].
- The render shows the silver hexagonal muzzle [Observed].
- **Ammo:** /40 (2015–2016); /30 in Sep 2014, the "New Field Medic" video [Observed].

**Firing** (CG_CQrZ7nwA sddefault, Oct 2015, 17/40) [Observed, low-res: E/crops/fm_cg_sdd.png]
- A big pale cream-yellow spiky muzzle cone.

**Projectile** [Observed]
- olive-brown chunks
- one large white rounded chunk with an orange band

Reading these as "limbs" (and the white one as a cast) is [Inference].

**Impact / end result (kill)**
- **Oct 2015:** at point-blank range the kill banner appears as the victim's name in large green letters ("PHANTAZMADROIDZ") while chunks fly [Observed]. The victim's own death visual is hidden by the chunks [Unverified].
- **Jan 2016 (xy-JjHD0k1s maxres1, 0/40, "KILLS", "ASSIST +65"):** a white-grey smoke puff with dark bits near a distant enemy [Observed: E/crops/fm_xy_m1.png]. Attributing it to the Field Medic is [Inference, weak].
- AHgOlXZi6oo, titled "Field Medic", shows only the Plasma Orb in its thumbnails.

**Images viewed:** E/grids/grid_xy-JjHD0k1s.jpg, E/crops/fm_xy_m1.png, fm_xy_m2.png; E/grids/grid_CG_CQrZ7nwA.jpg, E/crops/fm_cg_sdd.png, fm_cg_sd1.png; E/grids/grid_cDg2nI7ghMM.jpg; E/grids/grid_AHgOlXZi6oo.jpg

**Depiction for shorts:** a cream muzzle cone sprays stitched plush arms and legs and a cast-wrapped toy leg that bounce off the target. A kill ends in a white "poof" cloud and the green name banner. The plush-limb treatment is [BBG News invention]; it keeps the joke without gore.

**Confidence:** observed (muzzle and chunks); partial (kill).

---

## Bounce Lazer (primary; BBG 2.19, Apr 26 2015; HUD consistent with it in the Aug 2026 playtest)

- **Official text:** "Turn this place into a rave! Bounce your lasers off of everything!" [Game text via wiki]
- **Wiki:** "fires a beam of rainbows similar to the Huggable (Class) Headlights"; 32 ammo; it bounces "10 times" and also "25 times" (the page contradicts itself) [Fan-wiki].

**Look** [Observed: E/crops/z8_menus.png (Sep 2016, The Incredible Riggs on the gear-up screen)]
- A small blue-grey blaster with yellow, orange and red trim, held one-handed at chest height, muzzle up.
- A pink Huggable head with an open mouth and tongue hangs below the grip; it is about fist-sized or a little larger.
- The blaster is about head-length, roughly 0.15–0.2x Riggs (≈0.2x Oliver) [Observed, approximate].
- The same pose appears in matches: E/grids/grid_TDlVWANcdvY.jpg, grid_6Eg5JOntSYA.jpg, grid_Hj92aAgUTM0.jpg.
- **Ammo:** /40 (Jul 2015, Sep 2016); /32 (Aug 2015, Apr 2016; Aug 2026) [Observed].

**Firing and projectile:** no beam is visible in any of the five Bounce Lazer videos' thumbnails [Unverified]. The rainbow beam rests on the main dossier's 2015 thumbnail.

**Impact on targets**
- **Sep 2016 (z8GcYdFIdBI sddefault and sd2; HUD 34/40 with the Bounce Lazer icon):** at point-blank range the enemy, a blue-team Riggs carrying a glowing pink-hive Electric Honey, flashes white and is engulfed in a cloud of yellow five-point cartoon stars (≈#F9EF44) [Observed: E/crops/bl_z8_fire.png].
  - That loadout's melee is Sword and Stone [Observed: E/crops/z8_menus.png], so the stars may be a melee-hit effect, not the beam [Unverified].
- **Aug 2026 (32/32):** a kill banner, "NAMEY" [Observed, low-res].

**Images viewed:** E/grids/grid_TDlVWANcdvY.jpg, grid_6Eg5JOntSYA.jpg, grid_Hj92aAgUTM0.jpg, grid_z8GcYdFIdBI.jpg; E/crops/bl_z8_fire.png, z8_menus.png, auj_huds.png

**Depiction for shorts:** a toy-sized blaster with a dangling pink Huggable head fires a thin rainbow beam that ricochets off walls at crisp angles. On a hit, the target flashes white inside a shower of yellow cartoon stars. The stars are [Observed] but unattributed, so treat them as [BBG News invention]-level licence.

**Confidence:** observed (look); partial (beam and impact).

---

## Corrections for the character file
All corrections apply to `/home/user/thallo-site/bbg-news-repo/characters/riggs.md`.

1. **Weapons bullet**
   - **Current:** "- **Weapons:** BBG defaults Beebeegun, Hivey League, Barbed Gloves [Fan-wiki] ([Heavy (BBG)][wh]); "Beebee gun" is official in BBH [Canon] ([characters][chars]); bee theme [Inference]. Their look is undocumented, so designs, like the toothbrush prop, are [BBG News invention]."
   - **Correction:** weapon looks are now documented from gameplay frames. The Oct 2026 playtest shows Riggs with the **Electric Honey**: a black minigun with a glowing pink hexagonal hive and violet rings, 120 rounds [Observed]. Aug–Sep 2026 frames show the Flame Thrower ("Coff…" can), a Zombee-Gun-type HUD, the Bounce Lazer and the Provolowned [Observed/Inference]. Keep only the toothbrush as [BBG News invention].
2. **Red card skin**
   - **Current:** "The red card skin is unnamed [Open]."
   - **Correction:** the Sep 2026 gear-up menu labels the red cracked-rock skin "ROCKY HORROR", 250 Gas [Observed, 336 px chapter frame]. The main dossier ties the trailer card to Rocky Horror.
3. **Skins list**
   - **Current:** "Riggs, Green, Purple, Brown, Orange, Olive; Gold Riggs, Old Timey, No More Mr Ice Guy, Nature's Folly, Teen Wolf, The Incredible Riggs, Law Man, On A Roll, B and J, Rocky Horror."
   - **Correction:** add that the 2026 menu shows "LAWYER RIGGS" (300) [Observed, low-res], which may rename "Law Man" [Unverified], and "NO MORE MR ICE GUY" at 50. The white gritted-teeth skin in droid BBG's Oct 2026 video is probably No More Mr Ice Guy [Inference].
4. **Open question on 2026 changes**
   - **Current:** "- His real voice (no audio heard), and any 2026 changes to kit, lines or default skin: the Q&A, demo and JustNubz showcase ([YouTube][show]) are unchecked."
   - **Correction:** the JustNubz showcase is partly checked (the Heavy chapter frame shows the skin menu and the Provolowned). Playtest frames confirm the Electric Honey, Flame Thrower, Bounce Lazer and a Zombee-type HUD in builds 3.0.2 and 3.0.7. Riggs's HUD maximum health reads 200 in some loadouts and 240 in others [Observed]. Voice and lines remain unchecked.
5. **Prompt pack weapon**
   - **Current:** "thick dark brawler gloves, chunky oversized close-range gun."
   - **Correction:** for 2026-accurate art, name the observed gun: "black boxy minigun topped by a glowing pink hexagonal hive with two orbiting violet energy rings and a purple coiled side tube (Electric Honey)" [Observed].
6. **Open question on weapon looks**
   - **Current:** "White or pale blue-grey fur? Eye colour? Height? The red card skin's name? What his weapons look like?"
   - **Correction:** the skin name and weapon looks are answered (see items 1–2). The fur question remains, though 2026 shows a cel-shaded white skin (#E8EBEC) [Observed].

## Open questions
- Is the Electric Honey's purple lightning in CmYil-JJdC0's custom thumbnail an unedited in-game effect? Check the Steam Next Fest demo (from Oct 19) or an unedited frame.
- What fired the long magenta beam (#E838F8) in CmYil-JJdC0 maxres1 while Riggs was reloading?
- The Flame Thrower stream ("red-colored flames" per the wiki) and its impact have never been observed.
- The Freeze Blast projectile and slowing floor pools have never been observed.
- Are the yellow cartoon stars in z8GcYdFIdBI a Bounce Lazer hit or a Sword and Stone melee hit? The Bounce Lazer beam on a target is still unseen.
- What does the Sucker Punch projectile look like in flight? Is the flame-trailed pink head in neIf26qQkI4's thumbnail in-game? Does 2026 really use 1 round?
- What are the victim's death visuals for Field Medic and Zombee Gun kills? The white puffs are unattributed.
- Ammo differs by era, against the wiki's current values:
  - Zombee Gun: 125 / 104 / 300
  - Electric Honey: 70 / 120
  - Provolowned: 80 / 100 / 130
  - Flame Thrower: 30 / 40 / 60
  - Field Medic: 30 / 40
  - Bounce Lazer: 32 / 40

  Which values does 2026 use?
- Why does Riggs's 2026 maximum health show 240 in some loadouts and 200 in others?
- What is the white Zombee Gun part in the Aug 2026 Match 8 frame, and what weapon is it?
- HKbwq7PolNc's Riggs matches (1, 8, 9, 10, 13) have no reachable frames.
- Where does the "Playtest 5" render come from (official 2026 art or fan-made), and is that Riggs the new "classic-inspired" skin?
- Does "LAWYER RIGGS" replace "Law Man"?


---

<!-- gap pass 2 -->
# Riggs (Heavy): addendum on the Beebeegun, Hivey League and Buzz Kill (firing and impact)

This addendum covers one gap only: how Riggs's three bee weapons fire and what happens where they hit. All three are the Heavy's bee-themed guns. The Beebeegun is the default primary, the Hivey League the default secondary, and the Buzz Kill an unlockable secondary [Fan-wiki] (https://battlebears.fandom.com/wiki/Heavy_(BBG)).

**Bottom line.** I found no image of bees in flight, of a Hivey League cone or of a Buzz Kill explosion. Firing and impact are still documented only in words: the item text plus the wiki's mechanics [Game text via wiki; Fan-wiki]. What changed today:
- **Wbf910 (tMYoL8PojiM):** the "long striped-gun icon" at 100/100 is the **Provolowned**, not the Beebeegun [Observed].
- **DArtist900 (TYTotVgZpq4):** the "x/120" weapon is **Electric Honey**, paired with a **Hivey League** icon [Observed].
- **PanoramicBB (Yl26Ukn3qSA, Aug 23 2013):** a new Everyplay capture shows the Beebeegun in a match, with a 160-round clip and tiny white flecks at the hive [Observed].
- **xBlush Bangarang (vHHlwQUiOGQ, Dec 4 2012, BBR era):** a hive-family secondary with a 3-round clip, which points to the Buzz Kill [Observed; Inference].
- **Rexnado01 (IqQJgohemMM):** the starburst cannot be tied to any Riggs weapon [Observed].

**Sources reached today (2026-10-18)**
- **Fan wiki (MediaWiki API):** I re-fetched Beebeegun, Hivey League, Buzz Kill, Heavy (BBG), Weapon Statistics, Status Effects and Riggs, and searched the File namespace for "bee", "buzz", "hivey", "honey" and "queen".
- **battlebears.com/pages/characters:** live, re-fetched.
- **Steam:** the news API for app 4408320, and all 73 community screenshots on its hub, posted Jul–Oct 2026 from builds 2.54.0 to 3.0.7. I downloaded and viewed all of them.
- **YouTube thumbnails:** maxresdefault, sddefault and hqdefault, plus frames 1–3 (maxres/sd/hq), with oEmbed titles and InnerTube upload dates and descriptions. That covers:
  - all 13 gap videos;
  - 30 more Heavy gameplay uploads found with InnerTube search;
  - 6 official SkyVu videos (IucMFqzR_Qw, wNpM1woYv7k, ssSdTy9Ynr0, MXdDQeY0xpw, 0gYEZCMQfmA, xp5B76ExuAI).

**Not reachable**
- **web.archive.org:** connections were reset, and archive.org returned HTTP 429. Archived SkyVu pages and patch notes are still unread.
- **Playback:** YouTube video playback and storyboards were blocked. **I watched no video**; all video evidence is thumbnail frames.

**Evidence folder:** /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-gaps-r3/ (subfolders thumbs/, crops/, sheets/, steam/, next/, wiki/, official/). Thumbnails are saved as thumbs/<id>_<name>.jpg; the source URL is https://i.ytimg.com/vi/<id>/<name>.jpg.

**One process note:** several images I opened early in the session were later dropped from my context before I had written notes on them. I re-opened every image that I cite below. Only re-opened images are listed as "Images viewed".

---

## What the gap-list videos actually show

Upload dates come from YouTube InnerTube; build stamps and loadouts are read from the HUD.

| Video | Uploader, date | Build / era | Loadout in HUD | Bee-weapon evidence |
|---|---|---|---|---|
| tMYoL8PojiM "(RIGGS) HEAVY GAMEPLAY" | Wbf910, May 13 2022 | stamp "2.53.6" [Observed] | **Provolowned** (100/100, 12/100) plus an unidentified dark-purple secondary [Observed] | None. The icon matches the wiki's Provolowned images (white grater barrel, cheese body with red flecks, garlic bulb, orange muzzle) [Observed: sheets/prov_cmp.jpg]. Its 100 rounds match the Provolowned's wiki ammo of 100 [Fan-wiki]. Riggs wears an all-gold skin [Observed]; that it is "Gold Riggs" is [Inference]. |
| TYTotVgZpq4 "Heavy Gameplay" | DArtist900, Jun 16 2022 | 2.53.6 [Observed] | **Electric Honey** (60, 67 and 0 of 120) plus a **Hivey League** icon [Observed; match to File:Hivey_league.png icon, Inference] | Hivey League equipped but not seen fired. A target shows yellow 5-point stars over its name. They cannot be tied to a weapon [Observed; attribution Unverified]. |
| V5JtQQxjutc | Splxsh Clpxz, Jul 8 2022 | 2.53.6 | Huggable weapons only | None. No Riggs in any frame [Observed]. |
| lPiffxa7v40 | [B.E.A.R] Clan Official, Sep 1 2013 | — | Sucker Punch (1/1) plus a 120-round primary [Observed] | None |
| THbbzRYceng "Cowboy Heavy" | Ekim BB, Aug 13 2013 | — | Big Iron (6 rounds) plus Sucker Punch [Observed] | None |
| MMySXcRZXPc, xhbAdiR6_LM, CtWm-eHhiFk | TNTHACKER585, all Jun 20 2013 | menu stamp "2.0" [Observed] | Electric Honey plus Sucker Punch [Observed] | None |
| zr_g604No1s | TNTHACKER585, Sep 19 2013 | — | Electric Honey (120) [Observed] | None |
| F62gDANSudU | Judcursa Apple, Aug 24 2013 | — | Electric Honey (118–120/120) plus a blurred **hive-family** secondary icon (amber slat strip, banded dome) [Observed] | Possibly the Hivey League or Buzz Kill. The similarly built Plasma Orb cannot be ruled out [Inference]. |
| yOltW_hhrZ8 | Wendell Stewart, Oct 28 2014 | — | Electric Honey-like primary with an 88-round counter plus an unidentified secondary [Observed] | None |
| b13G5uay9Cc | Just A Cheese Dog, May 1 2015 | — | Provolowned plus Sucker Punch [Observed] | None |
| IqQJgohemMM "DEATH BY RIGGS!!!!!!" | Rexnado01, **Aug 21 2026** (the brief said about Sep 2026) | stamp "3.0.2" [Observed] | The player is **Tillman**: a panda with the Big Shot drum icon, 6/7 [Observed] | None. The white-yellow starburst (maxres1) appears in front of the player's own panda. The caption "killed by riggs... AGAIN!!!" and a kill feed reading "[Riggs face] KILLS [panda]" (maxres2) name the killer, but no Riggs weapon is visible [Observed]. Treating the burst as a Riggs hit would be [Unverified]. |

**Other uploads that matter** (found today, not in the brief):
- **Yl26Ukn3qSA "Battle Bears Gold Heavy Gameplay 1v1"** (PanoramicBB, Aug 23 2013, Everyplay): Beebeegun at 0/160 and 159/160, plus Sucker Punch. Riggs, in the red cracked-rock Rocky Horror skin, holds the Beebeegun in maxres1 and maxres3 [Observed].
- **vHHlwQUiOGQ "#33 Heavy Gameplay – Battle Bears Royale"** (xBlush Bangarang, Dec 4 2012): Electric Honey (120) plus a hive-family secondary showing **2 / 3** rounds [Observed]. See the Buzz Kill section.
- **ftGRzdV33a8** (Hammad Shahid, Mar 9 2014): Big Iron (10 rounds) plus a hive-family secondary whose muzzle is hidden [Observed].
- **IucMFqzR_Qw**, the official BBR Sneak Peek (2011): sd3 shows "0 / 3" and grey smoke puffs [Observed]. Zoomed, the weapon icon in the top-right RELOAD box is the purple-framed Big Shot drum (grey drum, yellow muzzle disc; matches File:Big_Shot.jpg), and the HUD portrait at top left is a panda [Observed]. The small icon beside "0 / 3" is a cluster of brass shells, not the drum [Observed]. So the player is Tillman [Inference], and this is **not a Buzz Kill shot**. Do not reuse it for Riggs.
- **No bee weapon in any thumbnail frame:** SodtU3IU63g, wpg8_7XT4w8, TZzqZ3N3ya0, MoFiMk7otxQ, uGYhJnoHTmA, qmlxB5Zs7YY, OdCUgvvEt9Y, oYKPEZZctFw, 5nNN4Iv-sy4, b-14FpvlP5g, tE1l2LVL2CI, NRs1Wao1irI, iXr7wjY2eRI, wwumLJSv7Lc, S1xFILDzfsI, 3G3a9EVFnyA, K2Dl31lpb10, wgcJIio0PhI, dJ6efITC_Yc, qszQzHQWte4, EzvSW6mLOgk, MsbKQ7Wo6LY, CtbZrp5E6UE, MTIL555mNXI, aeEtor1v-0E, kyd1Imy3n9w, eWqBEhym3zA [Observed].

**2026 Steam community screenshots** (73 images, builds 2.54.0–3.0.7):
- No Beebeegun, Hivey League or Buzz Kill appears [Observed].
- In 3820529699 (Holly Daze, posted Oct 15 2026, build "3.0.7 2026.11.19 b7"), Riggs on the Bundle Deals screen holds the **Provolowned**. The skin list there reads CLASSIC RIGGS, "B AND J – EQUIPPED", ROCKY HORROR 250, LAWYER RIGGS 300 [Observed].
- In 3820529898, a loadout menu lists "SECONDARY Sucker Punch / MELEE Huggable Gloves / SPECIAL Slow Motion Field / EQUIPMENT Armour" [Observed]. That this is Riggs's loadout is [Inference]: those are Heavy items [Fan-wiki].
- The "KILLED BY" panels I opened (3805409987, 3805409758, 3774194980) show other classes' loadouts [Observed].

---

## Beebeegun (primary; default since BBR 2012; rebalanced in BBG 2.6, Dec 2013; on SkyVu's Jul 6 2026 Steam banner; in the Nov 2026 build: unverified)

- **Official text**
  - "Artificially accelerated and naturally angry bees. Also the bees are fired backwards. And their stingers are infused with adamantium." [Game text via wiki] (https://battlebears.fandom.com/wiki/Beebeegun, re-fetched today)
  - "Wielding his "Beebee gun," he excels in close combat, delivering a burst of shells that unleash severe damage when focused on a single target, proving lethal at short distances." [Canon] (https://battlebears.com/pages/characters, re-fetched 2026-10-18)
  - The page introduces "the first batch of heroes" and an "Ultimate" but never names a game [Canon]. Tying the quote to Battle Bears Heroes (BBH) is [Inference]. Its "burst of shells" does not describe the BBG minigun [Inference].
- **Look**
  - **2013 in-game** [Observed: Yl26Ukn3qSA maxres3 and maxres1; crops crops/yl_m3_gun.png and crops/yl_m1_gun.png]:
    - Riggs holds it low at the hip.
    - The body is a dark charcoal-brown box, sampled #342221–#372B2F under warm skatepark light [Observed, sampled].
    - On top sits a faceted gold hive, sampled #BE973B [Observed, sampled].
    - A bent yellow-and-black striped tube, like a bee's abdomen, runs from the hive; its yellow samples #BC984A [Observed, sampled].
    - Tiny white flecks, 2–6 px, hover by the hive and barrel [Observed: crops/yl_specks.png].
    - The wiki says "small bees circling its hive… purely cosmetic" [Fan-wiki]. That the flecks are those bees is [Inference].
  - **2013 HUD icon** [Observed: crops/yl_sd1_pri.png from Yl26Ukn3qSA sd1]: a dark gun with a ribbed octagonal barrel, amber markings, a gold hive and an orange-black tube.
  - **2026 official art** [Observed: re-opened /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/riggs-verify/crops/banner_riggs_gun.png, a crop of SkyVu's Jul 6 2026 "CLOSED TESTING" Steam banner]:
    - a black boxy body with a long dark octagonal barrel shroud (#353331);
    - slat windows filled with candy-striped orange and yellow cylinders (#D4831F / #EDBE21);
    - a zig-zag striped tube;
    - a banded orange-gold hive dome (#CF8A29 / #EFC437) with a small yellow-black, white-winged cartoon bee on it;
    - held across the chest by pale blue-grey Riggs in a maroon jacket [Observed, sampled].
  - **Size:** about 0.7× Riggs, which is about 0.85× Oliver on the BBG News scale chart [earlier pass's measurement; scale chart is BBG News invention].
- **Firing**
  - Automatic minigun with "Wind Up" and "Wind Down" barrel spin [Fan-wiki].
  - 5.5 damage, 0.1 s per shot, 100 ammo, 4 s reload, dispersion 0.08, +10% Health [Fan-wiki infobox].
  - Hitscan: "Automatics, shotguns, and others use hitscans… instantly registers a hit" [Fan-wiki, Weapon Statistics].
  - **New:** the Aug 2013 HUD reads x/160 [Observed]. That matches the wiki's 2.6 note "clip 160→150" [Fan-wiki], so a 160-round clip before Dec 2013 is [Inference].
  - No muzzle flash or tracer appears in any frame I opened [Observed absence]. Sound is undocumented [Unverified].
- **Projectile**
  - The item text says "angry bees… fired backwards" with adamantium stingers [Game text via wiki].
  - Mechanically the gun is hitscan, with no travelling projectile [Fan-wiki].
  - **No frame shows bees in flight** [Unverified].
- **Impact / end result**
  - No splash or status effect is listed [Fan-wiki]. "Plain bullet damage, no explosion" is [Inference].
  - The hit visual is unseen [Unverified].
  - Note on other footage: yellow stars over targets (TYTotVgZpq4) and white-yellow starbursts (IqQJgohemMM, tMYoL8PojiM maxres3) appear in BBG hit and kill moments [Observed]. None is attributable to the Beebeegun [Unverified].
- **Images viewed**
  - https://i.ytimg.com/vi/Yl26Ukn3qSA/maxresdefault.jpg, maxres1.jpg, maxres2.jpg, maxres3.jpg (sheets/yl26_full.jpg) and sd1.jpg
  - crops/yl_m3_gun.png, yl_m1_gun.png, yl_m1_far.png, yl_specks.png, yl_sd1_pri.png
  - riggs-verify/crops/banner_riggs_gun.png
  - https://i.ytimg.com/vi/tMYoL8PojiM/maxres2.jpg and maxres3.jpg (crops/tm_m2_icon2.png, tm_m3_scene.png, sheets/tm_icons.jpg, sheets/prov_cmp.jpg)
  - https://i.ytimg.com/vi/TYTotVgZpq4/ sddefault, maxres1–3 (sheets/sheet_TYTotVgZpq4.jpg, crops/ty_m1_center.png, ty_m1_tgt.png, ty_m1_gun.png)
- **Depiction for shorts**
  - Use the 2026 banner model: black box, candy-striped orange-yellow slats, a banded gold hive with one cartoon bee, and two or three tiny white-winged bees orbiting the hive at idle [Observed + Fan-wiki].
  - On the trigger, the barrels whine up to speed [Fan-wiki wind-up]. Then a dense stream of thin yellow streaks pours out, each a tiny tail-first cartoon bee [BBG News invention built on the Game text].
  - Hits pop small yellow "sting" sparks and fuzz puffs, with no explosion. A KO'd Huggable bursts into rainbow confetti [BBG News invention].
- **Confidence:** partial. The look is observed (2013 in-game and 2026 official art). Firing is documented as stats only. Projectile and impact are unknown.

## Hivey League (secondary; default since BBR 2012; "improved" in BBR 1.3, May 2012; speed penalty removed in BBG 2.6; seen in a 2.53.6 HUD in 2022; 2026: not seen)

- **Official text:** "Fires a spreading cone of angry bees! Great for close range battles with multiple targets close together." [Game text via wiki] (https://battlebears.fandom.com/wiki/Hivey_League, re-fetched)
- **Look**
  - **Menu icon** [Observed: crops/ref_hivey_icon.png, from the wiki's 2012 gear screen File:Hivey_league.png]:
    - a grey boxy gun with an amber slat strip and dark grip vents;
    - a gold hive dome with brown bands and two tiny white dots beside it (the dots as bees is [Inference]);
    - **a rectangular grey front block with a dark slot**.
  - The same icon is in DArtist900's 2.53.6 HUD (Jun 2022) [Observed: crops/ty_maxres1_sec.png, sheets/ty_sec.jpg, sheets/cmp_icons_all.jpg]. The identification by muzzle shape is [Inference, strong].
  - The 3D model (honeycomb muzzle with honey in the holes, gold hive, amber slats) was documented earlier from wiki gear screens and SkyVu's 2012 BBR trailer. I did not re-open those today [earlier pass, Observed then].
  - Trivia: "Honey seems to drip out on the barrel. This may suggest that the gun shoots both bees and honey." [Fan-wiki]
- **Firing**
  - Shotgun: "deals damage at close range in a cone of fire" and is hitscan; "All shotguns, including the Hivey League, have identical range." [Fan-wiki]
  - 0.75 s rate of fire, 6 s reload [Fan-wiki].
  - The ammo values conflict: infobox 4, text "six bullets", earlier 10. The damage is printed as "1525" [Fan-wiki].
  - Not seen fired in any frame [Unverified].
- **Projectile:** "a spreading cone of angry bees" [Game text via wiki]. Not seen [Unverified].
- **Impact / end result:** undocumented. There is no splash or status effect [Fan-wiki infobox lists none] [Unverified visual].
- **Where to look next:**
  - DArtist900, TYTotVgZpq4: Hivey League equipped [Observed].
  - Possibly F62gDANSudU (Judcursa Apple) and ftGRzdV33a8 (Hammad Shahid): hive-family icons, muzzle unreadable [Observed; Inference].
- **Images viewed:** crops/ref_hivey_icon.png, crops/ty_maxres1_sec.png, sheets/ty_sec.jpg, sheets/cmp_icons_all.jpg, crops/f62_sec.png, crops/ft_sd1_sec.png, sheets/hud_g1.jpg, sheets/hud_g2.jpg.
- **Depiction for shorts:**
  - The squat hive gun coughs a short, wide fan of five or six fat cartoon bees and a spray of honey droplets [Game text + Fan-wiki trivia; the bee count and honey spray are BBG News invention].
  - Two or three close targets get peppered with yellow sting sparks and stagger. Honey drips from the muzzle afterwards [BBG News invention].
- **Confidence:** partial.

## Buzz Kill (secondary; original BBR 2012 item; "Improved" in BBR 1.3; likely seen in a Dec 2012 BBR HUD; 2026: not seen)

- **Official text:** "Fires a queen bee which explodes a second or two after impact." [Game text via wiki] (https://battlebears.fandom.com/wiki/Buzz_Kill, re-fetched)
- **Look**
  - **Menu icon** [Observed: crops/ref_buzz_icon.png, from File:Hivey_league.png]: the Hivey League body and hive, but the front is **a flared grey cone with yellow ring stripes and a black point**.
  - The earlier pass also documented the 3D model (black hexagonal muzzle with concentric yellow-orange chevrons and a white smoke puff) [earlier pass, Observed then].
  - **New:** in xBlush Bangarang's BBR video vHHlwQUiOGQ (Dec 4 2012, map Desert Airmine), the HUD shows a hive-family secondary. Its front edge is grey with a vertical yellow stripe and is partly covered by the Electric Honey icon. Its counter reads **2 / 3** [Observed: crops/vh_max_icon.png, crops/vh_huds.jpg, sheets/cmp_secicons.jpg].
  - **Why I read it as the Buzz Kill [Inference, moderate]:**
    - A 3-round maximum matches the Buzz Kill (3 ammo) and none of the Hivey League's recorded values (4, 6 or 10) [Fan-wiki].
    - The large HUD icon in that frame is still the Electric Honey, so the frame probably catches a weapon switch [Inference].
- **Firing**
  - "Projectile speed value: 800"; "the only projectile in Battle Bears Gold that flies with an upward arc instead of a downward one" [Fan-wiki].
  - 1.5 s rate of fire, 3 ammo, 3.5 s reload, 25,000 Joules, level 3 [Fan-wiki].
  - In the same vHHlwQUiOGQ frame, a thin pale line rises steeply from behind Riggs into the sky and ends near a small dark speck [Observed: crops/vh_max_arc.png, crops/vh_max_full.png]. It could be a Buzz Kill trail. It could equally be a rope on Desert Airmine; another frame of the same video shows a similar line hanging from a tower [Observed]. So it is [Unverified].
- **Projectile:** "a large bee-like explosive" that "sticks to any surface or explodes on contact with another player" [Fan-wiki]. Not identified in any frame [Unverified].
- **Impact / end result**
  - It explodes "exactly 1.5 seconds after it landed" (the lead says "two seconds") or "immediately upon impact with an enemy player" [Fan-wiki].
  - Explosives 40–70; the Area of Effect row reads "Max Dmg 150.0, Min Dmg 300.0" (units unclear) [Fan-wiki].
  - It is "the Heavy's only weapon that causes an actual explosion" [Fan-wiki].
  - Explosives "are capable of damaging the user, where high self damage intake can result in a suicide" [Fan-wiki, Weapon Statistics].
  - Flyoff delay is 20 s [Fan-wiki]. What that means on screen is [Unverified].
  - In the vHHlwQUiOGQ frame, the distant target behind a black crate has a white puff and red-orange smears beside it [Observed: crops/vh_max_tgt.png]. Tying them to a Buzz Kill blast is [Unverified].
  - **The explosion's colour and shape are unknown** [Unverified].
- **Images viewed:**
  - crops/ref_buzz_icon.png, crops/vh_max_icon.png, crops/vh_max_small.png, sheets/vh_huds.jpg, sheets/cmp_secicons.jpg, crops/vh_max_full.png, crops/vh_max_arc.png, crops/vh_max_tgt.png, crops/vh_m2_full.png (from https://i.ytimg.com/vi/vHHlwQUiOGQ/maxresdefault.jpg, sddefault.jpg, maxres1–3.jpg)
  - crops/iu_sd3.png and sheets/iu_icons.jpg (IucMFqzR_Qw sd3, ruled out)
- **Depiction for shorts:**
  - A fat golden queen bee pops out of the cone and climbs in an upward arc [Fan-wiki], then splats and sticks to a wall [Fan-wiki].
  - It buzzes and blinks for a beat of about 1.5 s [Fan-wiki timing; the blinking is BBG News invention].
  - Then it bursts in a round yellow-orange cartoon blast with stinger-sparks and a few dazed bees spiralling out [BBG News invention]. A direct hit on a bear pops it at once [Fan-wiki]. Riggs can catch his own blast [Fan-wiki], which is a good gag beat.
- **Confidence:** partial.

---

## Corrections for the character file (/home/user/thallo-site/bbg-news-repo/characters/riggs.md)

1. **Line 56**
   - Current: "**Weapons:** BBG defaults Beebeegun, Hivey League, Barbed Gloves [Fan-wiki] ([Heavy (BBG)][wh]); "Beebee gun" is official in BBH [Canon] ([characters][chars]); bee theme [Inference]. Their look is undocumented, so designs, like the toothbrush prop, are [BBG News invention]."
   - Correction: the looks are documented. Beebeegun: black boxy hip minigun with a long octagonal barrel shroud, glowing amber or candy-striped orange-yellow slats, a gold hive with a little bee, and a striped bee-abdomen tube [Observed: 2013 gear-up and match capture; SkyVu's Jul 6 2026 Steam banner]. Hivey League: boxy grey shotgun with an amber slat strip, a gold banded hive and a rectangular honeycomb muzzle [Observed: wiki 2012 gear screen; SkyVu 2012 BBR trailer]. The bee theme is item text, not inference: "angry bees", "cone of angry bees" [Game text via wiki]. The battlebears.com "Beebee gun" line never names BBH, and it describes "a burst of shells", not the BBG minigun [Canon; BBH tie is Inference]. Only the toothbrush prop is [BBG News invention].
2. **Prompt pack, line 80**
   - Current: "chunky oversized close-range gun"
   - Correction: "black boxy minigun held at the hip, long octagonal barrel shroud, glowing orange-and-yellow candy-striped side slats, banded gold beehive dome with a tiny cartoon bee on top".
   - Evidence: the 2026 banner crop, sampled #353331, #D4831F/#EDBE21 and #CF8A29/#EFC437 [Observed].
3. **Ledger, line 89**
   - Current: "BBH "Beebee gun" and leap-smash Ultimate"
   - Correction: "battlebears.com characters page: "Beebee gun" ("a burst of shells") and leap-smash Ultimate [Canon]; that the page describes BB Heroes is [Inference]".
   - Evidence: the live page text, re-fetched 2026-10-18.
4. **Ledger, line 94**
   - Current: "bee theme [Inference]"
   - Correction: move it to documented material, citing the item text "Artificially accelerated and naturally angry bees…" and "Fires a spreading cone of angry bees!" [Game text via wiki].
5. **Open questions, line 100**
   - Current: "What his weapons look like?"
   - Correction: replace with "What do his bee weapons' shots and hits look like (no frame found)?"
   - Evidence: this addendum; the looks are observed, but firing and impact are unseen.

## Corrections to earlier research notes and the gap brief
- **Wbf910 HUD:** the brief reads its icon as "100/100, matching the Beebeegun's 100-round clip, with a long striped-gun icon". It is the **Provolowned**, which also has 100 rounds on the wiki [Observed: sheets/prov_cmp.jpg; Fan-wiki].
- **DArtist900 "x/120":** this is **Electric Honey** (120 rounds), not a Beebeegun. The secondary is the Hivey League [Observed].
- **Rexnado01 IqQJgohemMM:** uploaded **Aug 21 2026**, build "3.0.2". It is Tillman's point of view, and the starburst is not attributable to Riggs [Observed].
- **Beebeegun size conflict:** research_notes/BBG weapons (verified)/2026.md says "about 0.7× Oliver's height", but riggs.md says "≈ 0.7× Riggs ≈ 0.85× Oliver". Make them agree on 0.7× Riggs, which is about 0.85× Oliver [Inference].
- **IucMFqzR_Qw sd3** (0/3 rounds, grey smoke): the weapon icon in the RELOAD box is the Big Shot drum and the HUD portrait is a panda [Observed]. The icon beside "0 / 3" is a cluster of brass shells, not the drum [Observed]. So this is Tillman [Inference], not a Buzz Kill.

## Open questions
- What do Beebeegun bees, the Hivey League bee cone and the Buzz Kill queen bee and blast look like in motion? It needs actual video. The best candidates are:
  - Yl26Ukn3qSA (Beebeegun, Aug 2013);
  - TYTotVgZpq4 (Hivey League equipped, 2022);
  - vHHlwQUiOGQ (probable Buzz Kill, Dec 2012);
  - the Heavy chapter (8:50) of JustNubz's showcase -lAtv-j9Sms (2026 playtest).
- Are the Beebeegun, Hivey League and Buzz Kill in the Nov 4 2026 build? The 73 Steam community screenshots from 2026 builds show only the Provolowned, Sucker Punch and Huggable Gloves for Riggs.
- Is the white line in vHHlwQUiOGQ a Buzz Kill arc or a map rope?
- Are the white flecks by the Beebeegun hive the cosmetic circling bees?
- The SkyVu 2.6 changelog and the BBR 1.3 patch notes ("Improved… Hivey League", "Improved Buzz Kill") are still unread, because the archive was unreachable.
- Which Hivey League ammo value is right: 4, 6 or 10? And should the Buzz Kill fuse be 1.5 s or 2 s?
