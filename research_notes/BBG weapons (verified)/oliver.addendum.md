# Oliver (Soldier): gap addendum
## Sake Bomb, Solar Wind Scar, Steamshot, Bearzooka, Minigun, Sci-Fi HASR, HASR, Soaker, Spreadshot, Kumakiri

This addendum covers only the open gaps listed for Oliver. It builds on the verified dossier at /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/out/verified/oliver.md. Oliver is Battle Bears Gold's Soldier ("-SOLDIER: Oliver" [Canon, Steam]).

**What I could reach (Oct 17–18, 2026)**
- **YouTube metadata.** I fetched titles, channels, upload dates, descriptions and chapter lists for 44 videos through youtubei/v1/next. That covers every video ID named in the gaps, plus new leads:
  - m2Yp2QY2OCA, "Battle Bears Oliver Weapons Demonstrations", Bob Stuntsville, Aug 10, 2018.
  - ucPTtnEjLbk, "I sucks but [I AM BACK]! Oliver overhaul gameplay.", Apr 26, 2014.
  - G1Z5XxhF6CU, "BATTLE BEARS GOLD "OLIVER SETUP"", Jun 28, 2013.
  - _JeiI0KrSbA, "Longest steam shot ever?!", Nov 1, 2015.
  - 9nA-OaYAVzU, "SCI-FI ASR + STEAMSHOT Is a NASTY Combo", droid BBG, Sep 21, 2026.
  - SkyVu's own 9qYIIH8NV-4.
- **YouTube thumbnails.** I downloaded every available variant (hqdefault, hq1–3, sddefault, sd1–3, maxresdefault, maxres1–3; up to 1280×720) for 37 videos.
- **YouTube chapter frames.** I downloaded YouTube's signed chapter frames for m2Yp2QY2OCA (at 27.0, 69.9, 182.8 and 361.833 s) and 9qYIIH8NV-4.
- **Fan wiki (MediaWiki API).** Pages: Sake Bomb, Solar Wind Scar, Steamshot, Bearzooka (BBG), Minigun (Soldier), Sci-Fi HASR, Heavy A Salt Rifle, Soaker, Spreadshot (BBG), Kumakiri, Status Effects, Pick-Ups, Bearscream Sandwich, Shield, Battle Bears Gold/Versions and Soldier (BBG). I also downloaded File:A_life_upside_down.jpg at 2048×1536.
- **Official Steam trailer.** I extracted my own frames at 15 fps from 1.8 to 3.2 s.

**Blocked**
- YouTube player and storyboards:
  - WEB, MWEB and ANDROID_VR returned LOGIN_REQUIRED.
  - WEB_EMBEDDED_PLAYER returned "This video is unavailable".
  - TVHTML5_SIMPLY_EMBEDDED returned "no longer supported".
- YouTube transcripts: get_transcript returned 400 FAILED_PRECONDITION and timedtext returned 429. So Trevor's spoken overhaul notes could not be read.
- web.archive.org reset the connection three times.
- Everyplay, where most of these clips were recorded, is defunct.

**What the YouTube evidence is.** I watched no videos. All YouTube evidence below is single frames: YouTube's automatic thumbnails, which come from roughly 25/50/75% of the video [Inference], custom thumbnails, or signed chapter frames.

**Folder key.** [G] = /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/oliver-gaps/
- thumbs/<id>_<variant>.jpg: copies of https://i.ytimg.com/vi/<id>/<variant>.jpg.
- crops/: my sheets and zooms.
- kf/<id>_<ms>_hqdefault.jpg: signed chapter frames.
- tr_frames/r_NNN.png: trailer frame at 1.8 + (NNN−1)/15 s.
- img/: wiki files.
- next/: metadata.

Hex values are medians I sampled with Python under game lighting, so treat them as approximate.

## Method notes and shared findings (they change how several gap observations read)
- **The HUD weapon icon is the current weapon.**
  - The top-right icon and the ammo counter under it belong to the weapon in hand.
  - Proof from vUDdCvfaKK4 (Jun 4, 2021):
    - The Sake Bomb icon shows 2/4 while the jug is in hand [Observed, [G]crops/vUDd_m3.jpg].
    - A ring-rifle icon shows 16/50 while a rifle is in hand [Observed, [G]crops/vUDd_m1.jpg].
  - I used this to tie frames to weapons [Inference from these observed pairs].
- **Numbered thumbnails are not always in time order.**
  - In 2B8GQKOWDbQ, maxres2 reads timer 2:55 with 5/5 ammo, and maxres1 reads 2:51 with 4/5 [Observed].
  - The match timer counts down, so maxres2 comes first [Inference].
- **Magenta crackling ring arcs come from a pickup, not from any gun.**
  - File:A_life_upside_down.jpg (uploaded Apr 27, 2013 by ApplerGamers) is captioned on the wiki's Bearscream Sandwich page "A Solider with the Bearscream Sandwich." [Fan-wiki, "Solider" sic].
  - It shows the Sam-Are-I Oliver ringed by crackling magenta arcs (≈ #F75FF6, bright #FE7FFF) [Observed, [G]img/A_life_small.jpg; zoom [G]crops/alife_arcs.jpg].
  - The same arcs appear around the Minigun (3xfq8nO2cDY, whose kill feed reads "POWER UP"), around the Bearzooka (mTVPzAM0m7o sd3), and at a ring-rifle in 2021 (vUDdCvfaKK4 maxres1) [Observed].
  - So they are the Bearscream Sandwich damage buff, not a weapon effect [Inference, high].
  - The wiki conflicts on the buff's size: it "doubles the damage of all the player's weapons for 20 seconds" (Bearscream Sandwich page) vs "Triples the amount of damage the player deals for twenty seconds." (Pick-Ups page) [Fan-wiki].
- **Green glow with green shield icons is the Shield pickup or respawn protection.**
  - Wiki: "shields will circle around the player, making them immune to damage for 10 seconds" and "When the player respawns, they have the shields for 4.5 seconds (to discourage spawn killing)." [Fan-wiki, Shield].
  - Seen on BLUESHOCK in 2B8GQKOWDbQ maxresdefault, and in IqHSyVVvCQw maxres3, sYpY-ZHHlkg hq3 and w2AhIi7WYRU maxres2 [Observed].
- **Other overlays that are not weapon effects** [Fan-wiki, Status Effects]:
  - Coffee mug = Caffeinated ("a coffee mug will appear over the player's head"; Caffeine Injection).
  - Purple fist = Damage Enhanced ("a purple fist symbol"; Propbearganda).
  - Yellow "Z" = Slowed.
  - I saw all three in these clips [Observed].

---

## Sake Bomb (secondary; BBR v1.3.2, 2012; reworked to a ~20-round version around the Apr 2014 Oliver Overhaul; back to 4 rounds by Jun 2021)
- **Official text:** "A shot from this will make you wine and stumble." [Game text via wiki] (https://battlebears.fandom.com/wiki/Sake_Bomb).
- **Wiki stats** [Fan-wiki]:
  - "Secondary - Saboteur"; ammo 4; rate of fire 1 s; reload 3 s; duration 4.0 s; 1000 u/s.
  - Equipment: "Ammo +1 | + 1 bullets", "Ammo +2 | + 2 bullets".
  - "fires non-damaging projectiles in an arc ... they will receive a control reversal for 4 seconds".
- **SkyVu on the overhaul:** "This week, Oliver receives the first overhaul! Trevor explains in detail all of the changes made to this elite Solider class." [Canon, description of 9qYIIH8NV-4, BATTLE BEARS channel, Apr 25, 2014; "Solider" sic]. The changes themselves are spoken in the video and could not be read here.
- **Era evidence (HUD readings with the Sake Bomb icon)** [Observed]:
  - Jan 5, 2014: 4/5 and 5/5 (2B8GQKOWDbQ, CheeseclanBBG, "Sake Bomb Demonstration"). That is 4 plus Ammo +1 [Inference].
  - Apr 26, 2014: 20/20 (ucPTtnEjLbk sd1, fan title "Oliver overhaul gameplay") [[G]crops/ucPT_sd1_hud.jpg].
  - Apr 29, 2014: 13/28 and 28/28 (DxHcbyg9oPg, Hammad Shahid, fan title "Oliver Overhaul: Sci Fi ASR+Sake Bomb!") [[G]crops/DxHc_def_hud.jpg].
  - Jan 25, 2018: 5/28, 23/28 and 15/28 (zQMAJ2DRVhw, SW, title "... - Battle Bears Gold 2.28") [[G]crops/zQMA_m1_hud.jpg].
  - Aug 10, 2018: 1/20 (m2Yp2QY2OCA chapter frame at 361.833 s) [[G]crops/m2Yp_361_z.jpg].
  - Jun 4, 2021: 2/4 (vUDdCvfaKK4 maxres3).
  - Jun 23, 2021: 2/6 and 6/6 (L0REouUo-68 sddefault and maxres3). That is 4 plus Ammo +2 [Inference].
- **What the readings mean.**
  - The 20- and 28-round magazines cannot come from the wiki's 4 + 1/+2.
  - So the Sake Bomb became a roughly 20-round weapon right after SkyVu's Apr 25, 2014 overhaul. That version lasted at least to Aug 2018, and the weapon was back to 4 rounds by Jun 2021 [Inference from dated HUD readings]. 28 is probably 20 plus Ammo equipment [Inference].
  - No changelog reached confirms the dates. The wiki page does not mention the 20-round version.
  - 2026 status: no 2026 source names the Sake Bomb [Unverified].
- **Look in play**
  - **From behind, in hand.** It is held at his right shoulder: a squat, faceted, dark-maroon body (≈ #66181A–#6F1920). It carries red-orange teardrop or flame decals (≈ #EC4727, bright #FB7143) outlined in yellow (≈ #FAD044), plus a round red-orange emblem with a spiral, kanji-like mark [Observed: [G]thumbs/2B8GQKOWDbQ_maxres1.jpg, _maxres2.jpg; [G]crops/NORn_m2.jpg; [G]crops/vUDd_m3.jpg; [G]crops/L0RE_m2_spikes.jpg; [G]crops/m2Yp_361_z.jpg].
  - These decals match the "leaf motifs" and emblem on the wiki's SAKEBOMB.png [Inference]. About head-sized, 0.3–0.35x [Inference].
  - **Front.** A white Daruma face with heavy black brows, a dark open neck and a tan rope loop:
    - in the 2018 demo's "Secondaries" card, an in-game render ([G]crops/m2Yp_182_z.jpg, 182.8 s);
    - carried by a teammate in Nov 2017 ([G]crops/hasr_xvZd_m1.jpg);
    - on the HUD icon ([G]crops/L0RE_m2_hud.jpg) [Observed].
- **Firing**
  - Lob version (2012–early 2014 and again by 2021): "fires non-damaging projectiles in an arc" [Fan-wiki]. No frame shows it in flight [Unverified].
  - ~20-round version (from Apr 2014): with 13/28 on the HUD, a cream-white crown of liquid (≈ #DFD7BE) splashes up out of the jug's neck. Small white droplet streaks fly ahead toward the crosshair [Observed, [G]crops/DxHc_def_jug.jpg from DxHcbyg9oPg maxresdefault; same frame as maxres2].
  - In an Apr 26, 2014 overhead frame at 20/20, long curving trails of cream-white beads cross the grass near Oliver [Observed, [G]crops/sake_ucPT_sd1.jpg]. That they are sake is an [Inference].
- **Projectile**
  - Lob version: undocumented [Unverified].
  - ~20-round version: white droplets in a short spray [Observed, as above].
- **Impact / end result**
  - **Jan 2014 (lob era)**
    - With 4/5 on the HUD (one jug just thrown), a burst engulfs the target "SIRIS": chunky, faceted cream puffs (≈ #D5BBAD–#D0BAA6) and smooth white ovals (≈ #E4E4E3) [Observed, [G]crops/sake_puff.jpg].
    - In another frame of the same clip, a glossy, slime-like lime "?" floats beside SIRIS's name tag. It has a dark outline (shade ≈ #51A406, light ≈ #61E51A) and a separate oval "dot" [Observed, [G]crops/sake_qmark.jpg]. SIRIS is in the foreground under its name tag, so the "?" is read as SIRIS's [Inference]. This is the controls-reversed icon.
    - Wiki: "a green question mark will appear over the player's head"; "background music will be disabled and other sounds will feature an mild echo" [Fan-wiki, Status Effects; "an mild" sic].
  - **Correcting the gap note**
    - In 2B8GQKOWDbQ maxresdefault, the green glow with three shield icons is on a different player, BLUESHOCK. That is the Shield effect, not the Sake Bomb.
    - In maxres3 the yellow five-point stars and short yellow bars burst around SIRIS while the HUD reads 52/80 with the Sci-Fi HASR icon equipped. So the stars are rifle hits [Observed; Inference].
  - **2015–2018 (~20-round era)**
    - May 2015: a small green "?" over a distant target, with grey-white puffs around it [Observed, [G]crops/NORn_m2.jpg].
    - Jan 2018 [Observed, [G]thumbs/zQMAJ2DRVhw_maxres2.jpg, _maxres3.jpg; [G]crops/zQMA_m3_center.jpg, zQMA_m1.jpg]:
      - white puff balls and faceted chunks, and flat white disc "splats" on the floor;
      - the big lime "?" over nearby players;
      - a small "?" under the shooter's own HUD portrait, so he reversed himself, which the wiki allows ("including the user").
    - Aug 2018 (361.833 s): a white foamy splash spreads on the ice at Oliver's feet. A multicolour flash (magenta, white, yellow, green, cyan) with cream puffs bursts at a target as a kill registers [Observed, [G]crops/m2Yp_361_z.jpg]. Attribution is an [Inference, low].
  - **Jun 2021 (lob era again)**
    - With 2/6 on the HUD, a crown of lime-green crystalline spikes (≈ #9AFE31, bright #D1FF41) bursts from a ledge just under a white enemy [Observed, [G]crops/L0RE_m2_spikes.jpg].
    - That this is the Sake Bomb's landing splash is an [Inference, medium].
  - The weapon does no damage: "The Sake Bomb is the Soldier's only weapon that cannot damage opponents." [Fan-wiki].
- **Images viewed**
  - [G]crops/2B8GQKOWDbQ_sheet.jpg; [G]thumbs/2B8GQKOWDbQ_maxresdefault.jpg, _maxres1.jpg, _maxres2.jpg, _maxres3.jpg; [G]crops/sake_def_icon.jpg, sake_qmark.jpg, sake_puff.jpg
  - /tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/oliver-final/crops/sprite_soldier.png
  - [G]crops/vUDdCvfaKK4_sheet.jpg, vUDd_m3.jpg
  - [G]crops/zQMAJ2DRVhw_sheet.jpg; [G]thumbs/zQMAJ2DRVhw_maxres2.jpg, _maxres3.jpg; [G]crops/zQMA_m3_center.jpg, zQMA_m1.jpg, zQMA_m1_hud.jpg
  - [G]crops/L0REouUo-68_sheet.jpg, L0RE_m2_spikes.jpg, L0RE_m2_hud.jpg
  - [G]crops/NORn6h4Qq7Y_sheet.jpg, NORn_m1.jpg, NORn_m2.jpg
  - [G]crops/DxHcbyg9oPg_sheet.jpg, DxHc_def_hud.jpg, DxHc_def_jug.jpg
  - [G]crops/ucPTtnEjLbk_sheet.jpg, sake_ucPT_sd1.jpg, ucPT_sd1_hud.jpg, ucPT_def_hud.jpg
  - [G]crops/m2Yp_kf_sheet.jpg (from [G]kf/m2Yp2QY2OCA_{27000,69900,182800,361833}_hqdefault.jpg), m2Yp_361_z.jpg, m2Yp_182_z.jpg
  - [G]crops/hasr_xvZd_m1.jpg
- **Depiction for shorts**
  - Classic (2013) version: Oliver lobs the Daruma jug in an arc.
    - On contact, a pop of chunky cream puffs and white ovals swallows the target.
    - A glossy lime "?" with a separate dot springs up over the target's head.
    - The target walks the wrong way for a 4-second beat while the music cuts out.
    - All of this is observed or documented.
  - 2014–18 version: the jug sprays a cream-white splash from its neck, and the splats land as flat white discs [Observed].
  - A cartoon "hic!" from the victim is a [BBG News invention].
- **Confidence:** partial. Impact and status icon are observed; the lob-era projectile is unknown.

## Solar Wind Scar (secondary; BBG v2.11, Aug 27, 2014; Gas item)
- **Official text:** "Cut a star in half and imbued it with power. It's said that even standing in it wake will singe the flesh." [Game text via wiki] (https://battlebears.fandom.com/wiki/Solar_Wind_Scar; "it wake" sic).
- **Wiki stats:** "Secondary - Radiation Explosives"; damage 45.0; radiation 70 per second; duration 4.0 s; ammo 1; reload 4.0 s; 1000 u/s [Fan-wiki].
- **HUD readings:** 1/1 and 0/1 in Dec 2014 (KZ4o3mztMtM), Sep 2015 (6tCraoXnI_E), Feb–Apr 2016 (IqHSyVVvCQw, cKOHCD5LBN8, IY1AVcEzDr8) [Observed]. That matches ammo 1.
- **Look in play**
  - A long silver blade held upright in the right hand, rising above his head (about 1.0–1.2x), with a dark-and-gold/orange hilt.
  - The HUD icon is the sword with a gold-orange guard.
  - Sources [Observed]: [G]crops/sws_KZ4o_sd1.jpg (tan skin, blue headband, lava map); [G]thumbs/IqHSyVVvCQw_maxres1.jpg (black skin with glowing orange lava cracks); [G]crops/sws_6tCr_m2.jpg; [G]crops/sws_IY1A_m1.jpg. Scale is an [Inference].
- **Firing:** one swing, then the HUD drops to 0/1 and a 4 s reload [Observed; Fan-wiki].
- **Projectile**
  - A long, thin orange crescent or streak, tapered at both ends, slightly curved, with flame texture: ≈ #EB7F0D, bright core ≈ #F69520 [Observed].
    - In flight in mid-air over Sky View (cKOHCD5LBN8 maxres2, timer 2:56, HUD 0/1) [[G]crops/sws_cKOH_crescent.jpg].
    - Leaving the blade diagonally at launch, in two custom thumbnails built on gameplay frames (6tCraoXnI_E and IqHSyVVvCQw maxresdefault) [[G]crops/sws_6tCr_def.jpg, sws_IqHS_def.jpg].
  - At mid range the crescent is about as long as a bear is tall [Inference].
  - Wiki: "creates an orange slash, that travels in a straight direction. It will travel through walls" [Fan-wiki]. Passing through walls is not observed.
- **Impact / end result**
  - **Radiation icon.** A flat yellow disc (≈ #FBCC0B) split into six segments by thin black spokes around a black centre hole, floating near a bear's head [Observed]:
    - IqHSyVVvCQw maxres2, Feb 2016 [[G]crops/sws_IqHS_m2_icon.jpg];
    - IY1AVcEzDr8 maxres1, Apr 2016, over an enemy whose whole model is tinted bright lime [[G]crops/sws_IY1A_m1.jpg].
    - This matches the wiki: "a yellow circle will appear over the player's head and a noise from a Geiger counter will begin sounding"; "three portions of the circle will dissolve into the common radioactivity symbol"; at 100 RP the target explodes with a blast radius "between 150-200 units" [Fan-wiki, Status Effects].
  - The lime tint looks like the Shield glow seen elsewhere, so it may not be a radiation effect [Inference, low].
  - In cKOHCD5LBN8 maxres2, a dark bear tumbles in mid-air with pink flecks just behind the flying crescent [Observed]. Cause: [Inference].
  - The "dark, circular radiation belt" [Fan-wiki] is not seen in any frame [Unverified].
  - Unattributed in cKOH (maxresdefault and maxres2): a straight lime-green line (≈ #56DA34, bright #96F352) from near Oliver's blade to a bear on the fort [Observed; source unknown].
- **Images viewed**
  - [G]crops/cKOHCD5LBN8_sheet.jpg; [G]thumbs/cKOHCD5LBN8_maxresdefault.jpg, _maxres2.jpg; [G]crops/sws_cKOH_crescent.jpg
  - [G]crops/IqHSyVVvCQw_sheet.jpg, sws_IqHS_def.jpg, sws_IqHS_m2_icon.jpg; [G]thumbs/IqHSyVVvCQw_maxres1.jpg
  - [G]crops/6tCraoXnI_E_sheet.jpg, sws_6tCr_def.jpg, sws_6tCr_m2.jpg
  - [G]crops/KZ4o3mztMtM_sheet.jpg, sws_KZ4o_sd1.jpg
  - [G]crops/IY1AVcEzDr8_sheet.jpg, sws_IY1A_m1.jpg
- **Depiction for shorts**
  - One big two-handed swing flings a long flaming-orange crescent that flies straight (observed).
  - The struck bear gets the yellow six-segment radiation disc over its head and Geiger clicks (observed and documented).
  - The dark radiation ring on the floor is documented but its look is unseen. A dark smoky ring is a [BBG News invention].
  - Show any 100-RP pop as a cartoon burst with confetti.
- **Confidence:** observed (slash and icon); belt unknown.

## Steamshot (secondary; BBR v1.3.1 week 1, 2012; 30 Gas): no new visual of the steam
- **Official text:** "Steam power the demise of your enemies and look dapper while doing it. The gentleman's weapon, for a man who knows taste and isn't afraid to melt a face." [Game text via wiki] (https://battlebears.fandom.com/wiki/Steamshot).
- **Wiki:** "When activated, it releases a quick spread of damaging green steam." [Fan-wiki].
- **Look** [Observed, [G]crops/m2Yp_182_z.jpg, 2018 demo "Secondaries" card at 182.8 s]:
  - a brass body;
  - a green glass dome in a brass cage;
  - two copper stacks with green gems;
  - a silver rod barrel;
  - a gold honeycomb muzzle disc with round holes.
  - This matches the verified dossier.
- **Firing, projectile, impact:** still not seen. What I checked:
  - **sDVr1PqEHC4** (Hammad Shahid, Mar 22, 2015, "BBG- Oliver ASR+Steamshot Combo Gameplay"; 264 s per the wiki file metadata).
    - Wiki file page File:BBG- Oliver ASR+Steamshot Combo Gameplay: uploaded May 2, 2015 by Thecheeselover. The API's imageusage lists no page embedding it today.
    - In its 1280×720 maxresdefault and maxres1–3, the HUD shows only the ASR icon, and the ammo digits are missing [Observed].
    - There is no Steamshot on screen and no green steam.
    - maxres1 shows a dark-brown splatter on the boardwalk floor [Observed; unattributed].
  - **_JeiI0KrSbA** ("Longest steam shot ever?!", Nov 1, 2015) [Observed]: a blue x/36 primary; a pale yellow-green translucent cone at the muzzle; and a bat at 0/2. No Steamshot icon or model can be identified.
  - **9nA-OaYAVzU** (2026, "SCI-FI ASR + STEAMSHOT") [Observed]: only the grey rifle with magenta muzzle glow and magenta orbs, plus a white smoke column rising to an airborne enemy. That column is probably a jump plume [Inference].
- **Images viewed:** [G]crops/sDVr1PqEHC4_sheet.jpg; [G]thumbs/sDVr1PqEHC4_maxres1.jpg; [G]crops/_JeiI0KrSbA_sheet.jpg, steam_Jei_def.jpg, steam_Jei_sd1.jpg, steam_Jei_sd3.jpg; [G]crops/9nA-OaYAVzU_sheet.jpg, 9nA_def.jpg, 9nA_m3.jpg; [G]crops/m2Yp_182_z.jpg.
- **Depiction for shorts:** unchanged from the verified dossier. A short cone of steam from the honeycomb muzzle; its colour is [Unverified] (green per the wiki). A pale green-white mix stays a compromise [Inference].
- **Confidence:** partial (look); projectile unknown.

## Bearzooka (BBG) (secondary; default since BBR v1.0, 2011; named in SkyVu's 2026 Steam copy; seen in the 2026 trailer)
- **Official text:** "The basic weapon of any Soldier. Does a good amount of damage, with a decent area of effect (AOE). Useful for all situations." [Game text via wiki] (https://battlebears.fandom.com/wiki/Bearzooka_(BBG)). Steam: "Grab your A Salt Rifle, Bearzooka and those Turkish SW Boots..." [Canon].
- **Look**
  - **Which end is the muzzle (settled).** In the 2015 custom thumbnail of 0ZbJ0-Za5Ws, Oliver points the tube at the camera [Observed, [G]crops/bz_0ZbJ_muzzle.jpg from [G]thumbs/0ZbJ0-Za5Ws_maxresdefault.jpg]:
    - the wide end has a pink hexagonal end cap (tube ≈ #A95E54) around a dark round bore;
    - a band of grey-and-coral checkers sits directly behind that cap on the flared section;
    - glowing yellow-orange rectangular panels (≈ #E79925, bright #F4A936) sit between grey hex collars;
    - the narrower rear has a grey hex collar.
    - The thumbnail looks like an in-game render [Inference].
    - So the checker band, the pink hex cap and the bore are all on the same muzzle end.
  - Jun 2013 loadout (G1Z5XxhF6CU sd2, "2.0" in the corner): the Zombie skin holds it muzzle-on, showing the pink hex rim and dark bore [Observed, [G]crops/G1Z5_sd2.jpg].
  - Mar 2014: candy-cane skin, rear plate toward the camera, 3/3 [Observed, [G]crops/bz_7WSX_def.jpg].
  - Aug 2014: rear view at 4/4 [Observed, [G]crops/mTVPzAM0m7o_sheet.jpg sd1 and sd3]. The magenta arcs in sd3 are the Bearscream buff.
- **Firing**
  - **HUD history** [Observed]:
    - 0/1 and 1/1 in Apr 2013 (verified dossier);
    - 3/3 on Mar 10, 2014 (7WSXU2LaxYo);
    - 4/4 on Aug 14, 2014 (mTVPzAM0m7o);
    - 4/4, 0/4 and 2/4 on Jul 25, 2015 (0ZbJ0-Za5Ws; the uploader's listed set includes "Ammo+2").
  - **Wiki conflicts** [Fan-wiki]:
    - infobox ammo 1;
    - text "has two shots without additional ammo";
    - equipment table Ammo +1/+2 = "+ 0 bullets";
    - planned "Incoming stats": ammo 3, Ammo +1 "+1 rocket", Ammo +2 "+2 rockets".
  - 4 rounds with Ammo +2 fits a base of 2 plus 1 per level. It does not fit the Incoming stats (3 + 2 = 5). So by 2014–15 the base was probably 2 [Inference].
  - **Launch (2015).** At 2/4, just after a shot, round grey smoke puffs (≈ #605751–#6A5B52 under lava light) bunch at the muzzle. A dotted line of grey puffs leads to a bigger grey puff cloud downrange. The rocket body itself is not visible [Observed, [G]thumbs/0ZbJ0-Za5Ws_maxres3.jpg].
- **Projectile (2026 official trailer, 2.87–3.00 s)** [Observed, [G]tr_frames/r_017.png–r_019.png; crops [G]crops/tr_rocket_017.jpg, tr_rocket_018.jpg, tr_rocket_019.jpg]:
  - a hexagonal rocket with a grey hex nose cone;
  - a grey body with glowing orange-yellow rectangular panels (≈ #FFAF0E, highlights #FFE329);
  - a dark rear collar studded with small red squares;
  - a tail of 3–4 long, spiky orange-yellow flames.
  - It flies from near a distant green-furred, blue-headbanded bear toward and past the camera.
  - That this is a Bearzooka rocket is an [Inference, medium-high]. It shares the tube's hex-and-glowing-panel design, and the verified dossier shows that green bear shouldering the Bearzooka at about 4 s.
  - Its size against a bear cannot be measured, because it passes close to the camera.
- **Impact / end result (2026 trailer, 2.67–2.87 s)** [Observed, [G]crops/tr_blast_strip.jpg from r_014–r_017]:
  - 2.73 s: a faceted orange-yellow blast outlined with white crackle lines hits the B-1000's chest.
  - 2.87 s: a large soft yellow fireball (core ≈ #FFE01E) as the B-1000 is flung upward trailing flame.
  - That a Bearzooka rocket caused it is an [Inference].
  - 2015: a grey puff cloud downrange (0ZbJ0 maxres3) [Observed].
- **Excluded** [Observed; Inference]:
  - 574_vzigCqI ("Update 2.17 Bearzooka", Mar 11, 2015): a panda-skinned player with an olive-green tube and a red missile icon, 0/3 and 2/3. Not the Soldier's coral Bearzooka; probably Tillman's Twin Bearzookas from v2.17 [Inference]. Its maxres3 shows a soft yellow ground blast [Observed, [G]crops/574_m3.jpg].
  - sxM32PyNNRs: a glitch clip of a Riggs loadout ("2.23") holding the Iron Curtain with Oliver's TNT Launcher (3/3). No Bearzooka rocket.
- **Images viewed**
  - [G]crops/0ZbJ0-Za5Ws_sheet.jpg; [G]thumbs/0ZbJ0-Za5Ws_maxresdefault.jpg, _maxres3.jpg; [G]crops/bz_0ZbJ_muzzle.jpg
  - [G]crops/G1Z5XxhF6CU_sheet.jpg, G1Z5_sd2.jpg
  - [G]crops/7WSXU2LaxYo_sheet.jpg, bz_7WSX_def.jpg, bz_7WSX_m1.jpg
  - [G]crops/mTVPzAM0m7o_sheet.jpg
  - [G]crops/574_vzigCqI_sheet.jpg, 574_m3.jpg, 574_def_icon.jpg
  - [G]crops/sxM32PyNNRs_sheet.jpg
  - [G]crops/tr_rocket_sheet.jpg, tr_rocket_017.jpg, tr_rocket_018.jpg, tr_rocket_019.jpg, tr_blast_strip.jpg
- **Depiction for shorts**
  - Shoulder the coral hex tube, muzzle forward: pink hex cap, dark bore, checker band right behind the cap.
  - Fire with a burst of grey round puffs.
  - Use the observed 2026 rocket: grey hex nose, glowing orange panels, red-studded collar, spiky orange flame tail. Give it a dotted grey puff trail.
  - End in a soft yellow fireball, faceted and white-edged at first contact.
  - The rocket at about 0.3x a bear's length is a [BBG News invention].
- **Confidence:** observed (look, launch smoke, 2026 rocket); the link between the trailer rocket and the Bearzooka is an Inference.

## Minigun (Soldier) (primary; BBG v2.11, Aug 27, 2014; 45 Gas; changed after release)
- **Official text:** "Mini refers to your enemies after its done with them." [Game text via wiki] (https://battlebears.fandom.com/wiki/Minigun_(Soldier); "its" sic).
- **Wiki** [Fan-wiki]:
  - ammo 80; Ammo +1 "+ 10 bullets", Ammo +2 "+ 20 bullets", so 100 at most;
  - "This weapon was insanely overpowered on release due to a typo in its explosive damage values ... It has since been changed and the bullet damage has been nerfed as well."
- **HUD readings with the dark-green Minigun icon** [Observed]:
  - 130/130, 0/130 and 66/130 on Aug 30, 2014 (Kal, 3xfq8nO2cDY);
  - 130/130 and 104/130 on Aug 30, 2014 (Kal, EhIA-6KzfBo);
  - 130/130 on Dec 31, 2014 (KZ4o3mztMtM sddefault);
  - 100/100 and 51/100 on Feb 26, 2016 (jGNMEN83ABo). That is 80 + 20 [Inference].
  - The 130-round magazine of 2014 cannot be reached with the wiki's numbers. So the release version had a larger magazine, and it was later cut [Inference]. That fits "It has since been changed".
- **Firing / projectile:** long, thin, white-cream streaks run from the gun to the target [Observed, [G]crops/mini_3xfq_sd1.jpg, mini_3xfq_sd3.jpg, mini_EhIA_sd3.jpg]. They are tracers [Inference].
- **Impact / end result**
  - A large cream-white starburst (core ≈ #FAF4DA–#FBFBEA) with long pale-peach rays (≈ #F4CF9E–#F5D1AD) swallows the struck bear [Observed, 3xfq8nO2cDY sd3 at 66/130 and EhIA-6KzfBo sd3 at 104/130].
  - 2016: a big white smoke burst with debris at a target [Observed, jGNMEN83ABo maxres3; attribution Inference].
  - The release-era "explosive damage values" may explain the blast-sized hit flash [Inference].
- **Not the gun's effect**
  - The magenta-violet crackling arcs around the gun in 3xfq8nO2cDY are the Bearscream Sandwich buff: the kill feed reads "POWER UP", and the arcs match the wiki-captioned A_life_upside_down.jpg.
  - EhIA-6KzfBo, the same uploader on the same day, shows no arcs [Observed; Inference, high].
  - The coffee mug over his head is the Caffeinated icon.
- **Images viewed:** [G]crops/3xfq8nO2cDY_sheet.jpg, mini_3xfq_sd1.jpg, mini_3xfq_sd3.jpg, mini_3xfq_icon.jpg; [G]crops/EhIA-6KzfBo_sheet.jpg, mini_EhIA_sd3.jpg; [G]crops/jGNMEN83ABo_sheet.jpg; [G]crops/KZ4o3mztMtM_sheet.jpg; [G]img/A_life_small.jpg; [G]crops/alife_arcs.jpg.
- **Depiction for shorts:** a hose of thin white tracer streaks that ends in a big cream-white starburst with peach rays on the target (observed). Barrel spin-up and a casing waterfall are a [BBG News invention]. Do not add magenta arcs unless the scene includes a Bearscream Sandwich pickup.
- **Confidence:** observed (tracers and hit flash); the model in third person is still unclear.

## Sci-Fi HASR (primary; BBR v1.3.1 week 2, 2012; level 15)
- **Official text:** "Look no further for reasons for people to get out of your way, you're holding the only one you need. Should a chump still refuse to step aside, this puppy has a convenient little button to change their mind." [Game text via wiki].
- **Wiki:** ammo 50; Ammo +1 "+ 15 bullets", Ammo +2 "+ 25 bullets" [Fan-wiki].
- **HUD readings with the silver ring-rifle icon** [Observed]:
  - 23/50 on Apr 27, 2013 ([G]img/A_life_small.jpg; matches the wiki's 50);
  - 78/80 and 52/80 on Jan 5, 2014 (2B8GQKOWDbQ, [G]crops/sake_def_icon.jpg). 80 cannot be reached from 50 +15/+25 [Inference];
  - 0/30 on Aug 14, 2014 (mTVPzAM0m7o);
  - 60/60 and 0/60 on May 15, 2016 (vSoYuP-8QzM);
  - 23/60 and 0/60 on Jun 14, 2016 (Gqv2NiOpntU).
  - So the magazine changed several times. The x/30 reading fits the overhaul period [Inference].
  - DSmQtBO8HvI ("New Sci-Fi HASR sucks. Sorry Skyvu.", Apr 27, 2014) shows a Huggable loadout in its frames, so it is not usable [Observed, [G]crops/DSmQ_def.jpg, DSmQ_sd1_hud.jpg].
- **Firing:** a soft magenta glow at the muzzle (≈ #F43AD2, bright #FD69F5) [Observed: 2B8GQKOWDbQ maxresdefault; [G]crops/sfh_mTVP_def.jpg; [G]crops/sfh_Gqv2_m1.jpg].
- **Projectile:** small magenta dots hang between the muzzle and a distant target [Observed, [G]crops/sfh_mTVP_def.jpg]. That they are bolts is an [Inference].
- **Impact / end result**
  - 2016: a bright magenta-pink orb burst with a white core (≈ #FE7CFC) on the struck bear's chest, with short yellow streaks [Observed, [G]crops/sfh_Gqv2_m1.jpg].
  - Jan 2014: yellow five-point stars and short yellow bars around the target [Observed, [G]thumbs/2B8GQKOWDbQ_maxres3.jpg].
- **Correcting the gap note:** in mTVPzAM0m7o the crackling arcs are in sd3, around the Bearzooka (4/4), not at the Sci-Fi HASR. They are the Bearscream buff. The Sci-Fi HASR frames (sddefault and sd2, 0/30) show only the soft glow [Observed].
- **Related:** in 2026 the grey Sci-Fi ASR (identified only by the fan title of 9nA-OaYAVzU) also shows a magenta muzzle glow and magenta orbs flying toward the target [Observed, [G]crops/9nA_m3.jpg]. The 2013 Sci-Fi ASR demo had a pink-magenta bar (verified dossier). So magenta seems to be the "Sci-Fi" family colour [Inference].
- The "convenient little button" remains undocumented [Unverified].
- **Images viewed:** [G]img/A_life_small.jpg; [G]crops/sake_def_icon.jpg; [G]thumbs/2B8GQKOWDbQ_maxresdefault.jpg, _maxres3.jpg; [G]crops/mTVPzAM0m7o_sheet.jpg, sfh_mTVP_def.jpg; [G]crops/vSoYuP-8QzM_sheet.jpg; [G]crops/Gqv2NiOpntU_sheet.jpg, sfh_Gqv2_m1.jpg; [G]crops/DSmQtBO8HvI_sheet.jpg, DSmQ_def.jpg, DSmQ_sd1_hud.jpg; [G]crops/9nA_m3.jpg.
- **Depiction for shorts:** the silver rifle with its dark ring glows magenta at the muzzle and spits small magenta bolts, which pop as magenta-pink orbs with white cores on hit (observed). A special "button" shot is a [BBG News invention].
- **Confidence:** observed (muzzle glow and hit burst); partial for the bolts.

## Heavy A Salt Rifle (HASR) (primary; BBR v1.0, 2011; 110,000 Joules)
- **Official text:** "With higher capacity and lower damage the Heavy A Salt Rifle gives its owner more room for error before reloading but at the cost of stopping power." [Game text via wiki].
- **HUD readings** [Observed]:
  - Nov 13, 2017 (xvZdk873arU, title "Battle bears gold heavy a salt rifle gameplay", a "2.27" in the custom thumbnail): the salmon rifle icon with a red ring at 46/60 and 60/60. This matches the wiki's 60.
  - Jun 4, 2021 (vUDdCvfaKK4 maxres1): a red-grey ring-rifle icon, closer to the HASR sprite than the Sci-Fi HASR's black ring, at 16/50. 50 is not a HASR value in the wiki (60, +10/+20), so the identification is [Unverified] [[G]crops/vUDd_m1_icon.jpg].
- **Firing / projectile**
  - 2017: tiny white-yellow sparkle flecks at the muzzle; no tracer visible [Observed, [G]crops/hasr_xvZd_m1.jpg].
  - 2021: magenta crackle at the muzzle, which is the Bearscream type [Inference], and a magenta starburst near the targets. But a panda enemy fires a magenta-glowing gun in the same frame, so the attribution is [Unverified] [Observed, [G]crops/vUDd_m1_muzzle.jpg, vUDd_m1_flash.jpg].
- **Impact / end result:** no new attributable frame [Unverified].
- **Images viewed:** [G]crops/xvZdk873arU_sheet.jpg, hasr_xvZd_m1.jpg; [G]crops/vUDdCvfaKK4_sheet.jpg, vUDd_m1.jpg, vUDd_m1_icon.jpg, vUDd_m1_muzzle.jpg, vUDd_m1_flash.jpg.
- **Depiction for shorts:** unchanged. A fast spray with small white-yellow muzzle sparkles (observed, 2017). Hit pops follow the shared yellow-star style [Inference].
- **Confidence:** partial.

## Soaker (primary; BBR v1.0, 2011; 60,000 Joules, level 10)
- **Official text:** "The range is limited compared to other rifles, but it's way more accurate!" [Game text via wiki].
- **HUD readings** [Observed]:
  - Jan 11, 2014 (fjBn5OQZfyE, Benedict Siow, "21 kills with soaker!"): Soaker icon (yellow tank) at 80/80 and 0/80. That is 60 + Ammo +2, which adds "+ 20 bullets" [Fan-wiki; Inference].
- **Correcting the gap note.** The "small yellow droplets near the muzzle" are two rounded yellow parts fixed to the front of the gun's dark body. They match the Soaker's yellow tanks (see the store art in the verified dossier) [Observed, [G]crops/soak_fjBn_nozzle.jpg; that they are part of the gun is an Inference, medium].
- **Projectile:** still not seen [Unverified].
- **Impact / end result (unattributed)** [Observed, [G]crops/soak_oe7A_def.jpg]:
  - In oe7AqC-1mhM (SW, Nov 9, 2015, "URINE & SOAKER SUICIDE GLTICH!?"), three red-orange spiky spark bursts sit on a box at the wall just after the magazine empties (0/65).
  - The weapon icon is hidden under a KineMaster watermark ([G]crops/soak_oe7A_icon.jpg), and the title names both guns, so which gun it is remains [Unverified].
  - Its maxres1 shows big pale-yellow stars bursting around the shooter himself, matching the "suicide" in the title [Observed; Inference].
- **Images viewed:** [G]crops/fjBn5OQZfyE_sheet.jpg, soak_fjBn_def.jpg, soak_fjBn_nozzle.jpg, soak_fjBn_sd1.jpg; [G]crops/oe7AqC-1mhM_sheet.jpg, soak_oe7A_def.jpg, soak_oe7A_icon.jpg.
- **Depiction for shorts:** unchanged. The yellow-tank water gun is the identifier. A clear water jet is a [BBG News invention].
- **Confidence:** partial.

## Spreadshot (BBG) (secondary; BBR v1.0, 2011; 35,000 Joules, level 4; reworked to rapid fire in 2021)
- **Official text:** "Useless at range but devastating up close. Handy for close encounters..." [Game text via wiki].
- **HUD history** [Observed]:
  - 4 in Apr 2013 (verified dossier);
  - 3/4 and 4/4 on Mar 1, 2014 (LHrWhD7-vGg);
  - 3 in SkyVu's Apr 2014 overhaul video (verified dossier);
  - 0/20 RELOAD on Oct 9, 2021 (w2AhIi7WYRU), with the Spreadshot icon and the Spreadshot in hand [[G]crops/sps_w2Ah_m1.jpg, sps_w2Ah_m2.jpg].
  - The wiki infobox says ammo 6, 0.75 s [Fan-wiki].
- **2021 rework.** Uploader Sorapie's description: "They tweaked the spreadshot to be a weird rapid fire weapon. It does higher dps than before, but is overall way worse in my opinion." [Unverified: fan description; the 20-round magazine is Observed].
- **Look 2021:** the same model as before: a ring of six pink hex tubes at the muzzle, a sage-green chamber and a pink hose [Observed, w2AhIi7WYRU maxres2 and its render thumbnail].
- **Projectile, impact:** pellets still not seen [Unverified].
- **Related:** the magenta crackle at Oliver's gun in SkyVu's 2014 overhaul frames (open question in the verified dossier) matches the Bearscream arcs [Inference].
- **Images viewed:** [G]crops/w2AhIi7WYRU_sheet.jpg, sps_w2Ah_m1.jpg, sps_w2Ah_m2.jpg; [G]crops/LHrWhD7-vGg_sheet.jpg.
- **Depiction for shorts:** for a classic short, a short cone of pellets from the six-tube muzzle with white-yellow sparks (verified dossier). Pellet colour is a [BBG News invention]. Do not use the 2021 rapid-fire version for the classic era.
- **Confidence:** partial.

## Kumakiri (melee; BBR v1.3.2, 2012; 75,000 Joules, level 30)
- **Official text:** "It's baaack!" [Game text via wiki].
- **Look in game** [Observed, [G]crops/G1Z5_def.jpg; scale Inference]:
  - Jun 28, 2013 loadout (G1Z5XxhF6CU; "2.0" in the corner; Zombie skin).
  - A long, slightly curved silver katana with a wavy edge line, a black guard, a gold collar and a dark hilt.
  - Held upright one-handed, the blade is about as tall as the bear (0.9–1.0x).
  - The same loadout lists Special "FLAWLESS DISGUISE", Equipment "EXPLOSIONS +2" and "AMMO +2" [Observed].
- **HUD:** the melee slot shows the curved Kumakiri icon on the Sam-Are-I Oliver in Apr 2013 [Observed, [G]img/A_life_small.jpg].
- **Firing:** "a different animation which features a downward slash" [Fan-wiki].
- **Impact / end result:** still unseen. sYpY-ZHHlkg ("spreadshot, oco gauntlel and kumakiri", Feb 21, 2014) shows no Kumakiri in its frames: a menu with a grey-skin Oliver holding a cyan electric gun, a "HEAD SHOT" kill notice, and a teammate with shields [Observed, [G]crops/sYpY-ZHHlkg_sheet.jpg].
- **Images viewed:** [G]crops/G1Z5XxhF6CU_sheet.jpg, G1Z5_def.jpg; [G]img/A_life_small.jpg; [G]crops/sYpY-ZHHlkg_sheet.jpg.
- **Depiction for shorts:** an overhead downward slash (documented) with the shared melee stars (observed style). A white arc smear is a [BBG News invention].
- **Confidence:** partial.

---

## Corrections to the gap notes and the verified dossiers (evidence above)
**Gap notes**
- **Sake Bomb, 2B8GQKOWDbQ.**
  - The green "?" belongs to the foreground player SIRIS.
  - The green-glowing target with shield icons is BLUESHOCK, under the Shield effect.
  - The yellow stars in hq3 happen with the Sci-Fi HASR in hand (52/80).
  - The "round red-orange object with flame decals" is the Sake Bomb jug seen from behind.
- **Minigun.** The magenta-violet arcs are the Bearscream Sandwich buff, not the gun.
- **Sci-Fi HASR, mTVPzAM0m7o.** The arcs surround the Bearzooka in sd3. The Sci-Fi HASR frames show only a soft magenta glow.
- **Soaker, fjBn5OQZfyE.** The "yellow droplets" are most likely the gun's yellow tank parts.

**/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/out/verified/oliver.md**
- **Sake Bomb, "Projectile: Undocumented".** Add the 20/28-round version from Apr 2014 (cream spray from the neck, white puffs and splats) and the return to 4 rounds by Jun 2021. Impact visuals are now observed (cream-white puff burst, lime "?").
- **Solar Wind Scar.** The orange crescent is now observed, and so is the six-segment radiation disc.
- **Bearzooka.**
  - Add HUD 3/3 (Mar 2014) and 4/4 (Aug 2014; Jul 2015 with Ammo +2).
  - Add the grey puff launch trail and the 2026 trailer rocket.
- **Minigun, "Projectile: Undocumented and not seen".** Now: white tracer streaks and a cream-white starburst; 130-round magazine in 2014, 100 in 2016.
- **Sci-Fi HASR, "None visible".** Now: magenta muzzle glow, magenta dots and a magenta orb hit.
- **Spreadshot.** Add the 2021 rework (x/20 rounds).
- **Open question on "magenta crackle ... with the Spreadshot equipped".** Probably the Bearscream Sandwich buff [Inference].

**/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/out/verified/2026.md**
- Its Bearzooka line "a grey-and-red checkered flared rear end, and a pink hexagonal muzzle cap with a dark round bore" puts the checker band on the rear.
- In the 2015 render, the checker band is directly behind the pink hex muzzle cap, on the wide front end ([G]crops/bz_0ZbJ_muzzle.jpg).

## Corrections for the character file (/home/user/thallo-site/bbg-news-repo/characters/oliver.md)
1. **Line 51.** Current: "The Bearzooka is drawn as a green, hazard-striped tube [Observed; Inference]."
   - Correction: "In BBG the Bearzooka is a coral hexagonal shoulder tube with glowing orange panels and grey hex collars. Its wide muzzle end has a pink hex cap around a dark bore, with a grey-and-coral checker band right behind the cap [Observed: 2013 loadout, 2015 render, 2026 trailer]. It fires with a burst of round grey smoke puffs [Observed, 2015]. The 2026 trailer shows a grey hex rocket with glowing orange panels and a spiky orange flame tail [Observed; that it is the Bearzooka's is Inference]. The green hazard-striped tube is the BB Zombies design [Observed, File:Bear.jpg]."
2. **Line 75 (character reference prompt).** Current: "He holds a chunky assault rifle and carries a green hazard-striped launcher tube on his back."
   - Correction: "He holds the A Salt Rifle and shoulders the Bearzooka: a coral hexagonal tube with glowing orange panels, a pink hex muzzle cap with a dark bore and a checker band just behind it."
3. **Line 61 (comedy beat 1).** Current: "Bearzooka recoil blasts him through a wall. He comes back sooty: "Meant to do that.""
   - Correction: no recoil is documented. Re-ground the beat in self-damage ("The user is very prone to suicide while using the Bearzooka." [Fan-wiki]).
   - Use the observed visuals: a grey puff trail, the hex rocket with its spiky orange tail, and a soft yellow fireball.
   - The beat itself stays a [BBG News invention].
4. **Line 51 (katana).** Current: "He also has an improvised katana [Canon, channel unconfirmed]".
   - Add: in BBG the sword is the Kumakiri melee, a long, slightly curved silver katana with a wavy edge line, black guard, gold collar and dark hilt, held upright one-handed at about his own height [Observed: Jun 2013 in-game loadout, G1Z5XxhF6CU].
5. **Line 97 (open questions).** Current: "The [2026 showcase] and [Oliver Overhaul] videos have not been viewed."
   - Correction: keep "not viewed", and add the following.
   - SkyVu's Apr 25, 2014 description: "This week, Oliver receives the first overhaul! Trevor explains in detail all of the changes made to this elite Solider class." [Canon].
   - Fan footage dated Apr 26–29, 2014 shows the Sake Bomb as a ~20-round sprayer afterwards [Observed].
   - Transcripts are blocked from this sandbox.

## Open questions
- What exactly did the Apr 2014 Oliver Overhaul change? The frames suggest: the Sake Bomb at ~20 rounds; the Sci-Fi HASR at x/30; the Spreadshot at x/3; the Bearzooka at 3–4. SkyVu's spoken notes and forum changelog are unreachable here.
- When did the Sake Bomb return to a 4-round lob (between Aug 2018 and Jun 2021)? Which version ships in 2026?
- In the lob version, what flies? Does the jug itself sail through the air?
- Is the lime-green spike splash in 2021 (L0REouUo-68) the Sake Bomb's landing effect?
- Solar Wind Scar: what does the "dark, circular radiation belt" look like? Does the crescent visibly pass through walls? What is the straight lime line in cKOHCD5LBN8?
- Steamshot: is the steam green (wiki) or white? No frame anywhere shows it firing.
- What does the Soaker's stream look like? What do the Spreadshot's pellets look like? Does 2026 use the classic 4–6-round Spreadshot or the 2021 rapid-fire one?
- What are the 2026 stats for the Minigun (2014: 130 rounds; 2016: 100; wiki: 80) and the Sci-Fi HASR (50 / 80 / 30 / 60 over time)?
- What does a Kumakiri hit look like? Is its modifier +10% or −10% health?
- Is the 2026 trailer rocket (2.87–3.00 s) really from the Bearzooka, rather than the TNT Launcher or another weapon?
- Does the Bearscream Sandwich double or triple damage (wiki conflict)? Does it still show the magenta arcs in 2026?
