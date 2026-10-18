<!-- gap pass 1 -->
# Oliver (Soldier): gap addendum, round 2
## Sake Bomb, Solar Wind Scar, Steamshot, Bearzooka, Minigun, Sci-Fi HASR, HASR, Soaker, Spreadshot, Kumakiri

This addendum covers only the open gaps listed for Oliver. Oliver is Battle Bears Gold's Soldier ("-SOLDIER: Oliver" [Canon, Steam]). It replaces the round-1 addendum at /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/out/verified/oliver.addendum.md. I re-opened that pass's key crops myself and checked them against new evidence. Where round 1 was wrong or incomplete, I say so.

**What is new this round: YouTube storyboard frames, including SkyVu's own video.** YouTube's player is still blocked here (LOGIN_REQUIRED). The public Invidious API at invidious.f5.si, however, returns each video's storyboard spec: the signed i.ytimg.com/sb/<id>/storyboard3_L<n>/M<k>.jpg URLs. Those sprite sheets download from i.ytimg.com.
- I downloaded the largest storyboard level for 40 videos and sliced it into frames. That level is 120–320 px wide, one frame every 1, 2, 5 or 10 s depending on video length.
- I watched no video. Every "t=" below is a storyboard tile time (tile index × interval). Each tile is YouTube's preview frame near that time [Inference from the storyboard convention].
- The Invidious video-stream proxy sits behind an Anubis bot challenge. I did not try to bypass it.

The most important new source is SkyVu's own **"BATTLE BEARS GOLD Developer Update - Oliver Overhaul"** (BATTLE BEARS channel, 9qYIIH8NV-4, Apr 25, 2014, 240 s; 320×180 storyboard every 2 s). Its frames show nearly every gap weapon firing in an official video, with the HUD naming the weapon in hand.

**Other sources reached today**
- Fan wiki (MediaWiki API), re-fetched: Sake Bomb, Solar Wind Scar, Steamshot, Bearzooka (BBG), Minigun (Soldier), Sci-Fi HASR, Heavy A Salt Rifle, Soaker, Spreadshot (BBG), Kumakiri, Status Effects, Bearscream Sandwich, Pick-Ups, Shield.
- Wiki file metadata for the 2013 demo clips. "File:Oliver Secondary - Steamshot-0" = YouTube F2rsMmK6K68, Dban1, Apr 15, 2013, 37 s.
- Storyboards of the 2026 showcase -lAtv-j9Sms (JustNubz, Sep 20, 2026, "(from Closed Playtest #4)"; 320×180 every 10 s), Soldier chapter 4:35–8:50.

**Blocked:** the YouTube player, transcripts and the Invidious stream proxy. I did not retry web.archive.org this round.

**Folder key (absolute)**
- [R] = /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/oliver/gaps_r2/
  - sb/<id>/f_<ms>.jpg: storyboard frames.
  - sb/<id>/cs_NN.jpg: contact sheets.
  - z/: my zooms.
  - inv/: Invidious metadata.
  - wiki/: wikitext.
  - thumbs/: 2013 demo thumbnails.
- [G] = /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/oliver-gaps/ (round-1 crops and thumbnails, re-opened this round where cited).

Hex values are medians I sampled with Python (scripts in /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/scripts_oliver_gaps_r2/). They come from tiny, compressed frames under game lighting, so treat them as approximate.

Scale follows the BBG News chart: Oliver = 1.0x.

## Shared findings (they change how several gap observations read)

**1. SkyVu's 2014 overhaul video is a weapon-by-weapon official reference.** Its on-screen text, in order:
- "Battle Bears Gold BaLaNcE uPdAtE" (t=10 s);
- "OLIVER OVERHAUL" (t=20–44 s), over a render of Oliver holding the brass Steamshot with HEALTH/SPEED bars;
- "Secondary Weapon Changes" (t=120–122 s);
- an end card "OLIVER OVERHAUL / BATTLE BEARS ULTIMATE / ROAD TO BBU" (t=210 s).

These are [Canon: SkyVu on-screen text, Observed in storyboard frames [R]z/ov_cards.jpg]. The description reads: "This week, Oliver receives the first overhaul! Trevor explains in detail all of the changes made to this elite Solider class." [Canon, YouTube description via Invidious; "Solider" sic].

HUD readings in that video [Observed; zooms [R]z/ov_icons_pri.jpg, ov_hud.jpg, ov_hud2.jpg, ov_148_hud.jpg, ov_190hud.jpg]:

| Weapon | Time in video | HUD ammo |
|---|---|---|
| ASR | 56–60 s | white-shaker icon |
| HASR | 66–68 s | 21/30, 10/30 |
| Soaker | 72–82 s | 25/50, 0/50, 28/50 |
| Sci-Fi HASR | 88–94 s | 17/20, 4/20, 16/20 |
| Bearzooka | 126–134 s | 1/2 |
| TNT-type grey tube | 138–146 s | 0/1 |
| Spreadshot | 148–154 s | 2/3, 1/3 |
| Sake Bomb | 162–180 s | 17/20 → 0/20 |
| Rockette | 184–190 s | 1/4 |

**2. Fan clips were recorded with equipment, so their magazines are not base values.** Ammo+ equipment adds rounds [Fan-wiki]. All the ammo readings below are "magazine seen on screen", not base stats [Inference].

**3. The 2026 playtest build has every gap weapon** [Observed, -lAtv-j9Sms storyboard, grids [R]z/show_sold_a.jpg, show_sold_b.jpg, show_sold_c.jpg]. The Soldier loadout lists:
- Primaries: ACREAMBO PISTOLS, MINIGUN, OCO GAUNTLET, SOAKER, SCI-FI HASR, SCI-FI ASR, A SALT RIFLE, HEAVY A SALT RIFLE, URINE TROUBLE (t=410–460 s).
- Secondaries: SOLAR WIND SCAR, SAKE BOMB, STEAMSHOT, ROCKETTE LAUNCHER, BEARZOOKA, TNT LAUNCHER, SPREADSHOT (t=470–490 s).
- Melees: KUMAKIRI, DISCIPLINARIAN, B.E.A.R. CLUB, QUEENSBURY RULES, KRIKKIT BAT (t=500–520 s).

The 2026 in-game descriptions match the wiki's quoted texts word for word (details per weapon below). The class card (t=280 s) reads: "OLIVER THE SOLDIER IS A WELL ROUNDED FIGHTER WITH DECENT SPEED AND HEALTH. USE HIS STARTING BEARZOOKA CAREFULLY AS IT IS EASY TO KILL YOURSELF WITH IT!" [Observed: SkyVu game text in the 2026 playtest build, seen in a fan-video frame].

Release content could still differ from Playtest #4 [Inference].

**4. Overlays that are not weapon effects** [Fan-wiki, Status Effects/Shield; Observed in these clips]:
- The white coffee mug is Caffeinated.
- Green glow with shield icons is the Shield pickup or respawn protection: "shields will circle around the player, making them immune to damage for 10 seconds".
- The yellow "Z" is Slowed.

**5. Magenta crackling arcs are not tied to any one gun.** I saw them around:
- the TNT-type tube in SkyVu's video (t=138–140 s, 0/1);
- Oliver's hands in KZ4o3mztMtM (t=20–22 s);
- the Solar Wind Scar in 6tCraoXnI_E (t=36, 118 s);
- the Minigun in [G]crops/mini_3xfq_sd3.jpg.

So they are a player-state effect, not a weapon effect [Inference, high]. Round 1 identified them as the Bearscream Sandwich buff from the wiki caption on File:A_life_upside_down.jpg. I did not re-open that image this round [Inference, carried over]. The wiki page says the pickup "doubles the damage of all the player's weapons for 20 seconds" [Fan-wiki, Bearscream Sandwich].

---

## Sake Bomb (secondary; BBR v1.3.2, 2012; x/20 sprayer in SkyVu's Apr 2014 overhaul; x/4–6 by 2021; listed in the 2026 playtest)
- **Official text:** "A shot from this will make you wine and stumble." [Game text via wiki] (https://battlebears.fandom.com/wiki/Sake_Bomb).
- **Wiki** [Fan-wiki]:
  - "Secondary - Saboteur"; ammo 4; rate of fire 1 s; reload 3 s; duration 4.0 s; 1000 u/s.
  - "fires non-damaging projectiles in an arc. If any opponents (including the user) are hit within its small AoE, they will receive a control reversal for 4 seconds."
  - "The face on the Weapon is  a Daruma."
- **Version history from HUD readings with the Daruma-jug icon** [Observed]:
  - Jan 5, 2014: 4/5 and 5/5 (2B8GQKOWDbQ; [G]crops/2B8GQKOWDbQ_sheet.jpg). This is pre-overhaul; 4 plus Ammo+1 [Inference].
  - **Apr 25, 2014, SkyVu's own video:** 17/20, 9/20, 4/20, 3/20, 5/20, 0/20, RELOAD (9qYIIH8NV-4 t=162–180 s; [R]z/ov_sake.jpg, ov_sake2.jpg).
  - Apr 26, 2014: 20/20 ([G]crops/ucPT_sd1_hud.jpg).
  - Jan 25, 2018: 5/28 ([G]crops/zQMA_m1_hud.jpg). 28 is probably 20 plus Ammo equipment [Inference].
  - Aug 10, 2018: 1/20 (m2Yp2QY2OCA chapter frame at 361.833 s; [G]crops/m2Yp_361_z.jpg). Also 6 left at t=345 s ([R]z/m2Yp_345.jpg).
  - Jun 4, 2021: 2/4 ([G]crops/vUDd_m3.jpg).
  - Jun 23, 2021: 2–5 (L0REouUo-68 t=2–74 s; [R]z/L0RE_hud.jpg). Round 1 read a max of 6; the "/6" is too small to read in my zoom.
  - **Conclusion:** the overhaul made it a ~20-round weapon. That lasted at least to Aug 2018, and it was back to the wiki's 4 (+equipment) by Jun 2021 [Inference from dated, official and fan HUD readings].
  - 2026: "SAKE BOMB" is in the Playtest #4 secondary list [Observed, [R]z/show_sold_b.jpg t=470–480 s]. Its 2026 magazine was not shown.
- **Look**
  - **From behind, in hand:** a squat, faceted, dark-maroon jug (body ≈ #471D15 in shadow) with yellow-outlined red-orange flame or teardrop decals (≈ #D89550 sampled from few pixels; round 1 measured ≈ #EC4727 in a sharper frame). It is held at his right shoulder [Observed, [R]z/ov_sake.jpg].
  - **Front, shown when he flips it during reload** (SkyVu video t=180 s; L0REouUo-68 t=24 s): a white Daruma face with heavy black brows, and a round red emblem with a gold kanji-like mark [Observed, [R]z/ov_sake2.jpg, [R]z/L0RE_a.jpg]. The HUD icon has the same face and a tan rope loop [Observed, [R]z/sake_huds.jpg].
  - About head-sized, roughly 0.3–0.35x his height [Inference].
- **Firing**
  - On every shot, in 2014, 2018 and 2021 alike, **a cream-white "crown" of liquid splashes up out of the jug's neck**, with small white droplets flying ahead [Observed]:
    - SkyVu video t=168 s at 4/20 ([R]z/ov_sake.jpg);
    - m2Yp2QY2OCA t=345 s ([R]z/m2Yp_345.jpg);
    - L0REouUo-68 t=26, 46, 50, 52, 72 s at 4/5/4/2/3 ([R]z/L0RE_a.jpg);
    - DxHcbyg9oPg ([G]crops/DxHc_def_jug.jpg).
  - So the neck splash is the firing effect of both the 20-round and the 4-round versions. That corrects round 1, which tied it to the 20-round version only [Observed; Inference].
  - Muzzle-splash colour: cream-white. Round 1 measured ≈ #DFD7BE; I did not re-sample it.
  - Sound is undocumented.
- **Projectile**
  - Small white droplets and blobs [Observed, SkyVu video t=168 s; L0REouUo-68 t=26 s].
  - In Jan 2018, white blobs mid-air and flat white disc "splats" on the floor ([G]thumbs/zQMAJ2DRVhw_maxres2.jpg, [G]crops/zQMA_m3_center.jpg) [Observed].
  - Whether the arc the wiki describes is visible cannot be judged from single frames [Unverified].
- **Impact / end result**
  - **SkyVu video, Apr 2014** [Observed, [R]z/ov_sake.jpg, ov_sake2.jpg, ov_sake_tgt.jpg]:
    - at t=166–178 s, grey smoke puffs (≈ #888987) and then cream puff chunks (≈ #E1DCE0) swallow the target "PLAYER 152192";
    - a small green "?" (≈ #6BB058, a few pixels) sits under the target's name tag at t=162–170 s.
  - **Jan 2014 (2B8GQKOWDbQ)** [Observed, [G]crops/2B8GQKOWDbQ_sheet.jpg]:
    - maxres1 (4/5): SIRIS is engulfed in cream and white puffs;
    - maxresdefault: a big glossy lime "?" with a separate dot under the name "SIRIS".
  - **Nov 2017:** the shooter of the HASR clip xvZdk873arU has a big green "?" beside his own HUD, with white puffs nearby, so an enemy Sake Bomb hit him [Observed, [R]sb/xvZdk873arU/cs_01.jpg t=78 s].
  - **Aug 2018:** a white foamy splash at his feet and a multicolour kill flash at the target [Observed, [G]crops/m2Yp_361_z.jpg]. Crediting the flash to the Sake Bomb is an [Inference, low].
  - **Jun 2021:** a lime spike splash under an enemy ([G]crops/L0RE_m2_spikes.jpg) [Observed]. Crediting it to the Sake Bomb is an [Inference, medium].
  - Wiki on the status [Fan-wiki, Status Effects]: "a green question mark will appear over the player's head"; "background music will be disabled and other sounds will feature an mild echo" ("an mild" sic).
  - "The Sake Bomb is the Soldier's only weapon that cannot damage opponents." [Fan-wiki].
- **Images viewed:** [R]z/ov_sake.jpg, ov_sake2.jpg, ov_sake_tgt.jpg, L0RE_a.jpg, L0RE_hud.jpg, m2Yp_345.jpg, sake_huds.jpg, sake_prev.jpg, vUDd_a.jpg, m2Yp_kf_182_361.jpg; [R]sb/9qYIIH8NV-4/cs_00–05.jpg; [R]sb/xvZdk873arU/cs_01.jpg; [R]sb/NORn6h4Qq7Y/cs_01.jpg; [G]crops/2B8GQKOWDbQ_sheet.jpg, DxHc_def_jug.jpg, zQMA_m3_center.jpg, L0RE_m2_spikes.jpg; [G]thumbs/zQMAJ2DRVhw_maxres2.jpg.
- **Depiction for shorts**
  - Oliver swings the maroon flame-decal jug forward. A cream-white crown splashes from its neck and white droplets fly out (observed).
  - Where they land, grey smoke and cream puffs pop around the target, flat white splats mark the floor, and a glossy lime "?" with a separate dot springs up over the victim's head (observed). The victim walks the wrong way for 4 seconds while the music drops out (documented).
  - On reload he flips the jug to flash the Daruma face (observed).
  - A cartoon "hic!" is a [BBG News invention].
- **Confidence:** observed.

## Solar Wind Scar (secondary; BBG v2.11, Aug 27, 2014; Gas item; listed in the 2026 playtest)
- **Official text:** "Cut a star in half and imbued it with power. It's said that even standing in it wake will singe the flesh." [Game text via wiki] (https://battlebears.fandom.com/wiki/Solar_Wind_Scar; "it wake" sic). The same words appear in the 2026 build: "CUT A STAR IN HALF AND IMBUED IT WITH POWER. IT'S SAID THAT EVEN STANDING IN IT WAKE WILL SINGE THE FLESH." [Observed, -lAtv-j9Sms t=470 s, [R]z/show_sold_b.jpg]. The 2026 stat panel shows a "RADIATION" bar; its value is not legible at 320×180 [Observed, [R]z/show_stats2.jpg].
- **Wiki** [Fan-wiki]:
  - "Secondary - Radiation Explosives"; damage 45.0; radiation 70 per second; duration 4.0 s; ammo 1; reload 4.0 s; 1000 u/s.
  - "creates an orange slash, that travels in a straight direction. It will travel through walls, and when it hits someone, a dark, circular radiation belt will spawn."
- **Look**
  - A long silver blade with a gold/orange guard, held upright in the right hand and rising above his head (about 1.0–1.2x) [Observed: m2Yp2QY2OCA t=190–205 s with a sword icon at 0, [R]z/m2Yp_b.jpg; scale Inference].
  - Round 1 also logged the upright blade in KZ4o/IqHS/IY1A thumbnails. The wiki sprite "sws" is a straight silver blade with a gold guard [Observed, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/oliver-final/crops/sprite_soldier.png].
- **Firing:** one swing [Fan-wiki: ammo 1]. The blade sparkles yellow at the hilt just after a swing (m2Yp t=200 s) [Observed].
- **Projectile**
  - **A long, thin, flame-textured orange crescent**, tapered at both ends and slightly curved: ≈ #E07C0F–#E47D10, bright core ≈ #F49810–#F59A10 [Observed].
  - **In 6tCraoXnI_E (Sep 30, 2015):** at t=36, 72, 84, 118, 198 and 204 s it leaves Oliver's right side diagonally up and to the right. On screen it is longer than the bear is tall [Observed, [R]z/sws_6tCr.jpg; scale Inference].
  - **In cKOHCD5LBN8 (Apr 22, 2016):** in flight at t=0–1 and 5–7 s [Observed, [R]z/cKOH_a.jpg].
  - **In IY1AVcEzDr8:** at t=370 s [Observed, [R]z/sws_IY1A.jpg].
  - Passing through walls is not seen [Unverified].
- **Impact / end result**
  - **Radiation icon.** In IqHSyVVvCQw (Feb 13, 2016), a flat yellow disc (≈ #E7C038, bright #F4CE40) floats in mid-air at t=70 and t=164–172 s [Observed, [R]z/sws_IqHS_rad.jpg]:
    - at t=164–166 s it is a full disc with a dark centre;
    - at t=168, 170 and 172 s a wedge is missing, and the wedge grows.
  - That this is the Irradiated stage icon matches the wiki: "a yellow circle will appear over the player's head and a noise from a Geiger counter will begin sounding"; "three portions of the circle will dissolve into the common radioactivity symbol" [Fan-wiki, Status Effects]. The match is an [Inference]. At this resolution only one missing wedge is visible.
  - Whose head the disc floats over is not clear; it hangs above Oliver's side of the frame [Unverified].
  - At 100 RP the target explodes; "The blast radius caused by an exploding irradiated opponent is between 150-200 units." [Fan-wiki].
  - The "dark, circular radiation belt" is not seen in any frame [Unverified].
  - **Unattributed:** a lime-green line (≈ #68C142, bright #91E95A) in cKOHCD5LBN8 at t=5 s [Observed; source unknown].
- **Images viewed:** [R]z/sws_6tCr.jpg, sws_6tCr_after.jpg, cKOH_a.jpg, sws_IqHS_rad.jpg, IqHS_a.jpg, sws_IY1A.jpg, sws_KZ4o.jpg, m2Yp_b.jpg, show_sold_b.jpg, show_stats2.jpg; [R]sb/cKOHCD5LBN8/cs_00.jpg; [R]sb/IqHSyVVvCQw/cs_00.jpg, cs_01.jpg; /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/oliver-final/crops/sprite_soldier.png.
- **Depiction for shorts**
  - One big upward-diagonal swing flings a long flaming-orange crescent that flies straight (observed).
  - The struck bear gets a yellow disc over its head that loses wedges as Geiger clicks speed up (observed and documented).
  - A dark smoky ring on the floor for the documented "radiation belt" is a [BBG News invention]. Show any 100-RP pop as a confetti burst.
- **Confidence:** observed (slash and icon); the belt is unknown.

## Steamshot (secondary; BBR v1.3.1 week 1, 2012; 30 Gas; listed in the 2026 playtest): the green steam is now seen
- **Official text:** "Steam power the demise of your enemies and look dapper while doing it. The gentleman's weapon, for a man who knows taste and isn't afraid to melt a face." [Game text via wiki] (https://battlebears.fandom.com/wiki/Steamshot). The identical text appears in the 2026 build [Observed, -lAtv-j9Sms t=480 s].
- **Wiki** [Fan-wiki]:
  - "Secondary - Shotgun"; damage 35; rate of fire 1.5 s; ammo 3; reload 5 s.
  - "It is a retexture of the [[Spreadshot (BBG)]]".
  - "When activated, it releases a quick spread of damaging green steam."
  - The page embeds "File:Oliver Secondary - Steamshot-0" as "Steamshot Weapon Demonstration". Its file metadata gives videoId F2rsMmK6K68, "[Oliver]: Secondary - Steamshot", Dban1, 37 s, uploaded Apr 15, 2013 [Fan-wiki file metadata via API].
- **Look:** a brass body, green glass domes, copper stacks and a honeycomb hex muzzle. This is the gun Oliver holds in SkyVu's "OLIVER OVERHAUL" title render (9qYIIH8NV-4 t=30–44 s) [Observed, [R]z/ov_cards.jpg]. It matches the verified dossier. About 0.55–0.7x [Inference].
- **Firing / projectile**
  - **2013 wiki demo F2rsMmK6K68:** at t=3, 17 and 26 s a **spiky lime-green starburst** (≈ #80BC41, bright ≈ #99CD54) bursts at the muzzle and fans forward [Observed, [R]z/F2rs_a.jpg, F2rs_burst.jpg].
    - The HUD icon in these frames has the same shape as the brass Steamshot icon in the clip's thumbnails, which read 1/3, 0/3, 1/3 and 2/3 [Observed, [R]z/F2rs_hud.jpg, F2rs_thumbs.jpg].
    - This is late BBR, one month before the BBG rename [Inference from date].
  - **2018 demo m2Yp2QY2OCA:** at t=245 s the HUD shows the brass Steamshot icon at 2 (3 at t=235 s). **A long column of streaky lime-green spray** (bright ≈ #88F760) streams forward from the gun toward the targets [Observed, 160×90, [R]z/m2Yp_235.jpg, m2Yp_245_z.jpg, m2Yp_hud3.jpg].
  - So the "green steam" is real: a short, spiky lime burst at the muzzle that streams forward as green streaks. The wiki's "green" is right, and the verified dossier's white-or-green question is settled for colour [Observed].
- **sDVr1PqEHC4 (the gap's named source, Hammad Shahid, Mar 22, 2015, "BBG- Oliver ASR+Steamshot Combo Gameplay"):**
  - I checked the HUD every 4 s (67 frames, [R]z/sDVr_icons.jpg) and the 9 greenest frames ([R]z/sDVr_green.jpg).
  - Every readable icon is the ASR. No Steamshot icon and no green steam appear [Observed absence].
  - Shots are 1.5 s apart and the storyboard samples every 2 s, so the clip may still contain Steamshot shots [Inference].
- **Impact / end result**
  - In the 2013 demo thumbnail hq1 (0/3, just after a shot), the target throws off a white puff and a trail of small pink flecks [Observed, [R]z/F2rs_thumbs.jpg]. Crediting this to the Steamshot is an [Inference].
  - Whether the steam lingers on the target is [Unverified].
- **Images viewed:** [R]z/F2rs_a.jpg, F2rs_b.jpg, F2rs_burst.jpg, F2rs_hud.jpg, F2rs_thumbs.jpg; [R]sb/F2rsMmK6K68/cs_00.jpg, cs_01.jpg; [R]z/m2Yp_235.jpg, m2Yp_245_z.jpg, m2Yp_hud3.jpg, m2Yp_c.jpg, m2Yp_d.jpg; [R]z/sDVr_icons.jpg, sDVr_green.jpg, sDVr_full_a.jpg, sDVr_28.jpg, sDVr_hud.jpg, sDVr_def_hud.jpg, sDVr_m1_center.jpg; [G]crops/sDVr1PqEHC4_sheet.jpg; [R]z/ov_cards.jpg.
- **Depiction for shorts**
  - The dapper brass gun hisses out a short, spiky lime-green burst that streams forward as green streaks (observed).
  - The target is left coughing in a white puff with pink flecks (observed style).
  - Keep "melt a face" offscreen: a sooty, steaming bear is a [BBG News invention].
- **Confidence:** partial. Firing and projectile are now observed at low resolution; the impact is only an Inference.

## Bearzooka (BBG) (secondary; default since BBR v1.0, 2011; x/2 in SkyVu's Apr 2014 overhaul; named in SkyVu's 2026 Steam copy; in the Steam trailer, 2013 footage [Inference, strong]; in the 2026 playtest)
- **Official text**
  - "The basic weapon of any Soldier. Does a good amount of damage, with a decent area of effect (AOE). Useful for all situations." [Game text via wiki] (https://battlebears.fandom.com/wiki/Bearzooka_(BBG)).
  - Steam: "Grab your A Salt Rifle, Bearzooka and those Turkish SW Boots..." [Canon].
  - 2026 class card: "USE HIS STARTING BEARZOOKA CAREFULLY AS IT IS EASY TO KILL YOURSELF WITH IT!" [Observed, 2026 playtest text, -lAtv-j9Sms t=280 s].
- **Look** [Observed]
  - A coral hexagonal shoulder tube (≈ #9F5D5E, highlight #B4696C), with glowing orange-yellow panels and a pink hexagonal muzzle cap around a dark round bore.
  - SkyVu's official store render in the overhaul video shows Oliver shouldering it muzzle-to-camera (t=198 s, [R]z/ov_198.jpg).
  - The 2026 playtest render shows the same design on a black lava-crack skin (t=490 s; tube ≈ #9E5E5D, bright #B5625C; [R]z/show_bear500.jpg).
  - In a 2015 render the checker band sits right behind the pink muzzle cap ([G]crops/bz_0ZbJ_muzzle.jpg).
  - It is the same design from 2013 to 2026. About 0.6–0.7x his height [Inference].
- **Firing**
  - **HUD history** [Observed]:
    - 1/1 in Apr 2013 (verified dossier);
    - 3/3 on Mar 10, 2014 (round 1, 7WSXU2LaxYo);
    - **1/2 in SkyVu's own overhaul video** (t=126–134 s; [R]z/ov_hud2.jpg);
    - 3/4 and 2/4 on Aug 14, 2014 ([R]z/sfh_mTVP_hud.jpg, t=12–16 and 54 s);
    - 2/4 on Jul 25, 2015 ([G]thumbs/0ZbJ0-Za5Ws_maxres3.jpg). The uploader's description lists "-Ammo+2".
  - So after the overhaul the base was 2 rounds and Ammo+2 made 4 [Inference]. This contradicts the wiki's equipment table, where Ammo +1/+2 = "+ 0 bullets", and agrees with its text, "has two shots without additional ammo".
  - 2026 stat panel at t=490 s, read at low resolution: "EXPLOSIVES 60", "AOE 250", "COOLDOWN 1.5", reload "2.5" [Observed, low-res, [R]z/show_stats2.jpg and show_sold_b.jpg]. That matches the wiki infobox (40–60, 250, 1.5 s, 2.5 s).
  - **Launch:** round grey smoke puffs at the muzzle and a dotted trail of grey puffs downrange [Observed, [G]thumbs/0ZbJ0-Za5Ws_maxres3.jpg].
- **Projectile**
  - **BBG-era footage:** the rocket body is never visible [Unverified].
  - **Steam trailer, 2.87–3.00 s** (2013 footage [Inference, strong]: SkyVu re-used it on the 2026 Steam page, and the same shot is at t=7 s in the storyboard of SkyVu's May 30, 2013 trailer rfAyqVJrli4 [Observed, 160×90]; round-1 crop, re-opened): a rocket with a grey hexagonal nose cone, a body of glowing orange and yellow squares, a grey rear collar and fin, and a spiky orange-yellow flame tail [Observed, [G]crops/tr_rocket_018.jpg]. That it is a Bearzooka rocket is an [Inference, medium-high]: it shares the tube's hex-and-glowing-panel design.
- **Impact / end result**
  - **Mar 10, 2014 (7WSXU2LaxYo t=56 s):** a big faceted yellow polygonal blast (≈ #F8EB6F) with a grey smoke puff (≈ #9C9B90) at its centre [Observed, [R]z/bz7W_a.jpg].
  - **Jul 25, 2015 (0ZbJ0-Za5Ws t=38 s, HUD 0):** a faceted yellow blast (≈ #F7E04F, bright #FFF259) beside a billowing dark-grey smoke cloud (≈ #5E5B63) [Observed, [R]z/bz0Z_38.jpg].
  - Crediting both blasts to the Bearzooka is an [Inference, high]: the titles are "Bearzooka" gameplay, and the 2015 uploader's primary is Urine Trouble, which does not explode.
  - **Steam trailer (2013 footage [Inference, strong]):** a white-edged orange-yellow blast, then a soft yellow fireball that flings the B-1000 upward [Observed, [G]crops/tr_blast_strip.jpg; cause Inference].
  - **Excluded:** a huge magenta-white cloud in mTVPzAM0m7o at t=10–14 s is already present while the Sci-Fi HASR is in hand (10/30), before the Bearzooka shot [Observed, [R]z/sfh_mTVP_12.jpg], so it is not a Bearzooka blast [Inference]. 574_vzigCqI and sxM32PyNNRs were not re-opened this round. Round 1 excluded them as other weapons.
- **Images viewed:** [R]z/ov_198.jpg, ov_bz.jpg, ov_hud2.jpg, show_bear500.jpg, show_sold_b.jpg, show_stats2.jpg, show_txt1.jpg, show_txt2.jpg, show_txt3.jpg, bz0Z_a.jpg, bz0Z_38.jpg, bz7W_a.jpg, sfh_mTVP.jpg, sfh_mTVP_hud.jpg, sfh_mTVP_12.jpg, AZt_a.jpg, AZt_thumbs.jpg, AZt_sd3_sd1_zoom.jpg, AZt_sd3_zoom.jpg; [R]sb/AZt_huguhzc/cs_00.jpg, cs_01.jpg; [G]crops/bz_0ZbJ_muzzle.jpg, tr_rocket_018.jpg, tr_blast_strip.jpg; [G]thumbs/0ZbJ0-Za5Ws_maxres3.jpg.
- **Depiction for shorts**
  - Shoulder the coral hex tube, pink hex muzzle forward. Fire with a burst of round grey puffs and a dotted grey puff trail (observed).
  - The rocket is the design observed in the Steam trailer (2013 footage): grey hex nose, glowing orange-yellow squares, spiky flame tail.
  - It lands in a faceted yellow polygon blast with a grey or dark-grey smoke ball (observed). The target pops apart into toy pieces (observed in the Steam trailer, 2013 footage [Inference, strong]; see verified dossier).
  - Showing the rocket at about 0.3x a bear's length is a [BBG News invention].
- **Confidence:** observed (look, launch smoke, blast). The rocket model rests on the Steam trailer (2013 footage) and an Inference; no 2026 frame shows it.

## Minigun (Soldier) (primary; BBG v2.11, Aug 27, 2014; 45 Gas; magazine changed after release; listed in the 2026 playtest)
- **Official text:** "Mini refers to your enemies after its done with them." [Game text via wiki] (https://battlebears.fandom.com/wiki/Minigun_(Soldier); "its" sic).
- **Wiki** [Fan-wiki]:
  - ammo 80; Ammo +1 "+ 10 bullets", Ammo +2 "+ 20 bullets";
  - "This weapon was insanely overpowered on release due to a typo in its explosive damage values, which made it able to kill any enemy in less than 2 seconds from full health. It has since been changed and the bullet damage has been nerfed as well."
- **HUD** [Observed]:
  - x/130 on Aug 30, 2014: 130 at t=50 and 76 s, 66/130 in sd3 (3xfq8nO2cDY; [R]z/mini_a.jpg; [G]crops/mini_3xfq_sd3.jpg).
  - 130 cannot be reached from 80 + 20, so the release magazine was larger and later cut [Inference]. Round 1 also logged 100/100 in Feb 2016 (jGNMEN83ABo); I did not re-open it.
  - 2026: "MINIGUN" is in the Playtest #4 primary list [Observed, [R]z/show_sold_b.jpg t=410–420 s].
- **Look:** dark gunmetal with three barrels (verified dossier). It is not clear in these third-person frames [Unverified].
- **Firing / projectile:** a long thin white streak (tracer) runs from the gun to the target at t=60 s [Observed, [R]z/mini_a.jpg]. That it is a tracer is an [Inference].
- **Impact / end result**
  - White-cream starburst flashes with rays burst on targets at t=50, 52, 60 and 64 s (core ≈ #FBECC2) [Observed, [R]z/mini_a.jpg].
  - In sd3 the starburst swallows the struck bear [Observed, [G]crops/mini_3xfq_sd3.jpg].
  - A lime-yellow glow (≈ #EAF88F) at t=66 s, during RELOAD, is unattributed [Observed].
  - The release-era "explosive damage" may explain the blast-sized hit flash [Inference].
  - The magenta crackle at the gun's base in sd3 is a player-state effect, not the Minigun (Shared finding 5) [Inference].
- **Images viewed:** [R]z/mini_a.jpg; [R]sb/3xfq8nO2cDY/cs_01.jpg; [G]crops/mini_3xfq_sd3.jpg; [R]z/show_sold_b.jpg.
- **Depiction for shorts**
  - A hose of thin white tracer streaks that ends in a big white-cream starburst on the target (observed).
  - Barrel spin-up and a casing waterfall are a [BBG News invention]. Add no magenta arcs unless the scene shows a power-up.
- **Confidence:** observed (tracer and hit flash); the third-person model is partial.

## Sci-Fi HASR (primary; BBR v1.3.1 week 2, 2012; level 15; x/20 in SkyVu's Apr 2014 overhaul; listed in the 2026 playtest)
- **Official text:** "Look no further for reasons for people to get out of your way, you're holding the only one you need. Should a chump still refuse to step aside, this puppy has a convenient little button to change their mind." [Game text via wiki] (https://battlebears.fandom.com/wiki/Sci-Fi_HASR).
- **Wiki:** ammo 50; Ammo +1 "+ 15 bullets", Ammo +2 "+ 25 bullets"; "It is a retexture of the standard [[Heavy A Salt Rifle]]" [Fan-wiki].
- **HUD with the dark-ring rifle icon** [Observed]:
  - 50 in Apr 2013 (verified dossier);
  - 78/80 and 52/80 on Jan 5, 2014 ([G]crops/2B8GQKOWDbQ_sheet.jpg);
  - **17/20, 4/20 and 16/20 in SkyVu's video** (t=88–94 s; [R]z/ov_icons_pri.jpg, ov_sfh.jpg);
  - 30, 27, 10, 15 and 19 of 30 in Aug 2014 (mTVPzAM0m7o; [R]z/sfh_mTVP_hud.jpg);
  - 46/60 and 60/60 in Jun 2016 (Gqv2NiOpntU t=160–170 s; [R]z/sfh_Gqv2.jpg).
  - So the magazine changed over time, and the overhaul cut it to a 20 base [Inference].
  - 2026: "SCI-FI HASR" is in the Playtest #4 list [Observed, t=430–440 s].
- **Look:** a silver-white HASR with a dark gunmetal ring loop (verified dossier; HUD icon [Observed]).
- **Firing:** a strong magenta glow at the muzzle (≈ #EC1BF8, bright #F21FFE) [Observed]. Seen in the SkyVu video at t=88 and 94 s, in vSoYuP-8QzM at t=56–60, 160 and 248 s, in Gqv2NiOpntU at t=160 s, and in mTVPzAM0m7o at t=8–10 and 52 s.
- **Projectile:**
  - small magenta dots between muzzle and target (vSoYuP-8QzM t=56 s);
  - a magenta beam-like streak toward a target (mTVPzAM0m7o t=52 s).
  - [Observed, [R]z/sfh_vSoY.jpg, sfh_mTVP.jpg]. Reading them as bolts is an [Inference].
- **Impact / end result**
  - SkyVu video t=94 s: a magenta-white burst on a pink bear [Observed, [R]z/ov_sfh.jpg].
  - Gqv2NiOpntU t=160–170 s: magenta splashes on the far ledge and wall [Observed, [R]z/sfh_Gqv2.jpg].
  - Jan 2014: yellow five-point stars and bars around the target [Observed, [G]crops/2B8GQKOWDbQ_sheet.jpg maxres3].
  - The "convenient little button" has no documented function [Unverified].
- **Images viewed:** [R]z/ov_sfh.jpg, ov_icons_pri.jpg, sfh_vSoY.jpg, sfh_Gqv2.jpg, sfh_mTVP.jpg, sfh_mTVP_hud.jpg, sfh_mTVP_12.jpg, show_sold_b.jpg; [G]crops/2B8GQKOWDbQ_sheet.jpg.
- **Depiction for shorts:** the silver rifle with the dark ring glows hot magenta at the muzzle and spits small magenta bolts that pop as magenta-white bursts on hit (observed). Any special "button" shot is a [BBG News invention].
- **Confidence:** observed.

## Heavy A Salt Rifle (HASR) (primary; BBR v1.0, 2011; 110,000 Joules; x/30 in SkyVu's Apr 2014 overhaul; listed in the 2026 playtest)
- **Official text:** "With higher capacity and lower damage the Heavy A Salt Rifle gives its owner more room for error before reloading but at the cost of stopping power." [Game text via wiki] (https://battlebears.fandom.com/wiki/Heavy_A_Salt_Rifle).
- **HUD with the red-ring rifle icon** [Observed]:
  - 60 in 2013 (verified dossier);
  - **21/30 and 10/30 in SkyVu's video** (t=66–68 s; [R]z/ov_icons_pri.jpg, ov_hasr.jpg);
  - 60 again in Nov 2017 (xvZdk873arU t=46–50 s; [R]sb/xvZdk873arU/cs_01.jpg).
  - 2026: "HEAVY A SALT RIFLE" is in the Playtest #4 list [Observed, t=440–460 s].
- **Firing / projectile**
  - SkyVu video t=66 s: a thin red streak from muzzle to target [Observed]. Whether it is a tracer or an aim line is an [Inference].
  - Nov 2017, t=58–60 s (HUD 29, 17): a long pale-cream tracer streak from the muzzle toward the targets [Observed].
- **Impact / end result:** white sparkle flecks at the targets (xvZdk873arU t=62 s, HUD 6) [Observed]. Attribution is an [Inference, medium].
- **Images viewed:** [R]z/ov_hasr.jpg, ov_icons_pri.jpg; [R]sb/xvZdk873arU/cs_01.jpg; [R]z/show_sold_b.jpg.
- **Depiction for shorts:** a fast spray of pale-cream tracers ending in small white sparkle pops (observed). Brass casings are a [BBG News invention].
- **Confidence:** partial.

## Soaker (primary; BBR v1.0, 2011; 60,000 Joules, level 10; x/50 in SkyVu's Apr 2014 overhaul; listed in the 2026 playtest): the stream is now seen
- **Official text:** "The range is limited compared to other rifles, but it's way more accurate!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Soaker). The same line appears in the 2026 build [Observed, -lAtv-j9Sms t=420 s]. Its 2026 stat panel reads "AMMO 50" [Observed, low-res, [R]z/show_stats2.jpg].
- **Wiki** [Fan-wiki]: damage 5; rate of fire 0.1 s; ammo 60; reload 4 s; range 950 units; "This weapon is based on the Super Soaker".
- **HUD with the yellow-tank icon** [Observed]:
  - 60 in 2013 (verified dossier);
  - 80 on Jan 11, 2014 (fjBn5OQZfyE; round 1);
  - **25/50, 0/50 (RELOAD) and 28/50 in SkyVu's video** (t=72–82 s; [R]z/ov_soaker.jpg, ov_icons_pri.jpg).
- **Look:** in hand, its front is a **bright yellow nozzle block** [Observed, SkyVu video t=72–82 s]. The gap note's "yellow droplets near the muzzle" in fjBn5OQZfyE are these yellow gun parts [Observed, [G]crops/soak_fjBn_nozzle.jpg; Inference].
- **Firing / projectile**
  - **SkyVu video:** a straight **pale cyan-white water jet** (bright ≈ #CCF5F4, body ≈ #91BBBC) runs from the yellow nozzle to the target. Small droplets scatter beside the gun [Observed, [R]z/ov_soaker.jpg t=72, 80, 82 s].
  - **Fan footage, Jan 2014:** the same pale jet at t=58 and 68 s [Observed, [R]z/soak_fjBn.jpg].
- **Impact / end result**
  - A white-cyan splash bursts on the struck bear: core ≈ #F5FBFB, edges ≈ #C7F5F3, with droplets flying off (SkyVu video t=72 and 80 s; fjBn5OQZfyE t=64 s) [Observed].
  - No status effect [Fan-wiki: not on the Status Effects list].
  - In oe7AqC-1mhM ("URINE & SOAKER SUICIDE GLTICH!?"), a pale-blue splash bursts next to the shooter at t=58 s [Observed, [R]z/soak_oe7A.jpg]. Which gun made it is [Unverified].
- **Images viewed:** [R]z/ov_soaker.jpg, ov_icons_pri.jpg, soak_fjBn.jpg, soak_oe7A.jpg, show_sold_b.jpg, show_stats2.jpg; [G]crops/soak_fjBn_nozzle.jpg.
- **Depiction for shorts:** the yellow-nozzled water gun fires a straight pale cyan-white jet that bursts into a white-cyan splash with flying droplets on the target (observed). A soaked, dripping, annoyed target is a [BBG News invention].
- **Confidence:** observed.

## Spreadshot (BBG) (secondary; BBR v1.0, 2011; 35,000 Joules, level 4; x/3 in SkyVu's Apr 2014 overhaul; rapid-fire rework by Oct 2021; listed in the 2026 playtest)
- **Official text:** "Useless at range but devastating up close. Handy for close encounters..." [Game text via wiki] (https://battlebears.fandom.com/wiki/Spreadshot_(BBG)).
- **Wiki:** "Secondary - Shotgun"; damage 20; rate of fire 0.75 s; ammo 6; reload 3 s [Fan-wiki].
- **HUD with the salmon six-tube icon** [Observed]:
  - 4 in 2013 and Mar 2014 (verified dossier and round 1);
  - **2/3 and 1/3 in SkyVu's video** (t=148–154 s; [R]z/ov_148_hud.jpg);
  - 4/4 in LHrWhD7-vGg (t=245 s);
  - x/20 in Oct 2021 (round 1, w2AhIi7WYRU).
  - The uploader of w2AhIi7WYRU, Sorapie, wrote: "They tweaked the spreadshot to be a weird rapid fire weapon. It does higher dps than before, but is overall way worse in my opinion." [Unverified: fan description, quoted via Invidious].
  - 2026: "SPREADSHOT" is in the Playtest #4 list [Observed, t=490 s]. Whether 2026 uses the classic or the 2021 version is [Unverified].
- **Look:** a salmon six-tube muzzle with a sage chamber (verified dossier).
- **Firing / projectile:** pellets are not visible in any frame [Unverified].
- **Impact / end result**
  - **SkyVu video t=148 s (2/3, a shot just fired):** a billowing **lime-green cloud** (≈ #779A5E, bright ≈ #96C378) envelops the white target "PLAYER 152192" from the feet up [Observed, [R]z/ov_148_z.jpg, ov_sec.jpg].
  - Crediting it to the Spreadshot is an [Inference, medium]. It matches the "green swirling wisps" round 1 saw in sd2, and the Steamshot, the Spreadshot's retexture, shows green too.
  - **LHrWhD7-vGg t=175 s:** a big yellow five-point star at close range [Observed, [R]z/sps_LHrW.jpg; attribution Inference].
  - **2021 (w2AhIi7WYRU):** orange-yellow fire bursts and a yellow-green-white burst at targets (t=26, 116 s) [Observed, [R]z/sps_w2Ah.jpg]. Other players are firing in those frames, so attribution is [Unverified].
- **Images viewed:** [R]z/ov_148_z.jpg, ov_148_hud.jpg, ov_sec.jpg, ov_sec2.jpg, sps_w2Ah.jpg, sps_LHrW.jpg, show_sold_b.jpg.
- **Depiction for shorts**
  - A short cone blast from the six-tube muzzle that wraps the target in a puff of lime-green smoke (observed in the official video; attribution Inference), with yellow star pops.
  - Pellet colour is a [BBG News invention]. Use the 3–6-round pump-shotgun version for classic-era shorts.
- **Confidence:** partial.

## Kumakiri (melee; BBR v1.3.2, 2012; 75,000 Joules, level 30; listed in the 2026 playtest)
- **Official text:** "It's baaack!" [Game text via wiki] (https://battlebears.fandom.com/wiki/Kumakiri).
- **Wiki** [Fan-wiki]:
  - "It deals 110 damage. Unlike the Soldier's other melee weapons, it has a different animation which features a downward slash. It has a Stat Modifier of -10% Health."
  - "The description refers to the [[Katana]] used by [[Oliver]] in [[Battle Bears -1]]."
- **Look**
  - In sYpY-ZHHlkg (Feb 21, 2014, fan title "spreadshot,oco gauntlel and kumakiri"), a grey-skinned Oliver with a red headband holds a long, thin silver blade upright or slanted in his right hand, about his own height (1.0x) [Observed, [R]z/kum_a.jpg t=150, 160, 285, 340 s; scale Inference].
  - The blade is slightly curved at t=160 s [Observed]. The wiki sprite "kum" is a curved silver blade with a dark hilt [Observed, /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/oliver-final/crops/sprite_soldier.png].
  - **2026:** "KUMAKIRI" heads the Playtest #4 melee list. In the t=500 s render the bear holds a long straight blade upright that reads pale yellow-green under the menu's green light (≈ #87A158) [Observed, [R]z/show_bear500.jpg]. Which row is selected is not legible, so that this blade is the Kumakiri is an [Inference].
- **Firing:** "a downward slash" [Fan-wiki]. Not seen in frames.
- **Impact / end result:** still unseen. A melee clash at t=265 s in sYpY-ZHHlkg shows white puffs and a yellow-white starburst around a long white blade, but who swung it is unclear [Observed; Unverified attribution].
- **Images viewed:** [R]z/kum_a.jpg; [R]sb/sYpY-ZHHlkg/cs_00.jpg–cs_03.jpg; [R]z/show_bear500.jpg, show_sold_c.jpg; /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/oliver-final/crops/sprite_soldier.png.
- **Depiction for shorts:** an overhead downward slash with the slightly curved silver katana (documented and observed), ending in white puffs and a yellow star spark (observed shared melee style). A white arc smear is a [BBG News invention].
- **Confidence:** partial.

---

## Corrections to the gap notes and to round 1
- **Sake Bomb, 2B8GQKOWDbQ.**
  - The green "?" belongs to SIRIS.
  - The green-glowing bear with shield icons is BLUESHOCK under the Shield pickup.
  - The yellow stars come with the Sci-Fi HASR in hand (52/80).
  - The "round red-orange object with flame decals" is the Sake Bomb jug seen from behind. SkyVu's video confirms it: the same object is held under the Sake Bomb icon and flipped to show the Daruma face at t=180 s.
- **Round 1 tied the neck "splash crown" to the 20-round version only.** The 2021 4-to-6-round version shows it too (L0REouUo-68 t=26–72 s), so it is the Sake Bomb's firing effect in every era.
- **Steamshot, "steam not seen".** It is now observed as lime-green: in the wiki's own 2013 demo (F2rsMmK6K68 t=3, 17, 26 s) and the 2018 demo (m2Yp2QY2OCA t=245 s). The named source sDVr1PqEHC4 shows only the ASR in its storyboard.
- **Bearzooka.** SkyVu's own overhaul shows 1/2. The 4-round readings fit 2 + Ammo+2 [Inference]. The wiki's "+ 0 bullets" for Ammo+ on the Bearzooka does not fit.
- **Minigun.** The magenta arcs are a player-state effect, not the gun.
- **Soaker.** The "yellow droplets" are the gun's yellow nozzle parts. The actual stream is pale cyan-white.
- **Verified dossier (/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/out/verified/oliver.md).**
  - Its Bearzooka bullet treats the class-card line as "[Fan-wiki ... that it appears in game is Unverified]". The line is now observed in the 2026 build.
  - "Projectile: Undocumented" for the Sake Bomb, Minigun, Soaker and Sci-Fi HASR should be replaced with the observations above.

## Corrections for the character file (/home/user/thallo-site/bbg-news-repo/characters/oliver.md)
1. **Line 51.** Current: "The Bearzooka is drawn as a green, hazard-striped tube [Observed; Inference]."
   - Correction: "In BBG the Bearzooka is a coral hexagonal shoulder tube with glowing orange panels and a pink hex muzzle cap around a dark bore [Observed: SkyVu's Apr 2014 overhaul video store render at 3:18; 2015 render; 2026 playtest render]. It fires with round grey smoke puffs and explodes in a faceted yellow blast with grey smoke [Observed, fan footage 2014–15]. The green hazard-striped tube is the 2009 BB Zombies design [Observed, File:Bear.jpg, per the verified dossier]."
2. **Line 75 (character reference prompt).** Current: "He holds a chunky assault rifle and carries a green hazard-striped launcher tube on his back."
   - Correction: "He holds the A Salt Rifle (green-and-salmon rifle with a white salt shaker on top) and shoulders the Bearzooka: a coral hexagonal tube with glowing orange panels and a pink hex muzzle cap with a dark bore."
3. **Line 57.** Current: "whose Bearzooka is "easy to kill yourself with" [Game text via wiki]".
   - Correction: re-label as observed in game. The 2026 playtest class card reads "USE HIS STARTING BEARZOOKA CAREFULLY AS IT IS EASY TO KILL YOURSELF WITH IT!" [Observed, -lAtv-j9Sms storyboard t=280 s].
4. **Line 61 (comedy beat 1).** Current: "Bearzooka recoil blasts him through a wall."
   - Correction: no recoil is documented. Ground the gag in self-damage: the 2026 card's "EASY TO KILL YOURSELF WITH IT!" and the wiki's "very prone to suicide".
   - Use the observed visuals: grey puff launch, faceted yellow blast, grey smoke, toy-piece break-apart.
   - The gag itself stays a [BBG News invention].
5. **Line 51 (katana).** Current: "He also has an improvised katana [Canon, channel unconfirmed]".
   - Add: "In BBG the katana is the Kumakiri melee ("It's baaack!" [Game text via wiki], referring to his BB-1 katana [Fan-wiki]). It is a long, slightly curved silver blade about his own height [Observed, 2013 and 2014 fan footage], and it is still listed in the 2026 playtest [Observed]."
6. **Line 97 (open questions).** Current: "The [2026 showcase] and [Oliver Overhaul] videos have not been viewed."
   - Correction: "Neither video has been watched. Their storyboard frames have been reviewed, though.
     - SkyVu's Apr 25, 2014 Oliver Overhaul shows changed magazines: HASR 30, Soaker 50, Sci-Fi HASR 20, Bearzooka 2, Spreadshot 3, Sake Bomb 20.
     - The Sept 2026 Closed Playtest #4 showcase lists all 21 classic Soldier weapons with their original descriptions [Observed, storyboard frames].
     - Trevor's spoken explanations are still unheard."

## Open questions
- What exactly did Trevor say in the Apr 2014 overhaul? The frames show the new magazines (HASR 30, Soaker 50, Sci-Fi HASR 20, Bearzooka 2, Spreadshot 3, Sake Bomb 20, TNT 1), but not damage or reload changes, and no transcript is reachable.
- Which Sake Bomb ships in 2026 (4-round lob or 20-round)? When between Aug 2018 and Jun 2021 did it revert?
- Does the Spreadshot's lime-green cloud (SkyVu video t=148 s) belong to the Spreadshot, and is it the same effect as the Steamshot's green burst? What do the pellets look like?
- Solar Wind Scar: what does the "dark, circular radiation belt" look like? Does the crescent visibly pass through walls? Over whose head does the yellow disc in IqHSyVVvCQw float, and is the single missing wedge the wiki's three-wedge stage at low resolution?
- What are the 2026 magazine sizes for the Minigun (130 in 2014, 100 in 2016, 80 on the wiki), the Sci-Fi HASR (50/80/20/30/60 over time) and the Soaker (the 2026 panel reads about 50)? The 320×180 storyboard is too small to confirm the digits.
- Is the Steam-trailer rocket (2013 footage) the Bearzooka's (shared hex-and-glowing-panel design), or the TNT Launcher's or another weapon's? What does the 2026 rocket look like?
- What does a Kumakiri hit look like? Is the long, straight, pale blade in the 2026 render at t=500 s really the Kumakiri?
- Does the Steamshot's green steam linger as a cloud on the target, and what does a Steamshot kill look like?
- Does a higher-resolution source exist? The Invidious API also lists 320×180 storyboards for some videos (9qYIIH8NV-4, Gqv2NiOpntU, -lAtv-j9Sms). A watchable copy of the overhaul video would settle most of these questions.
