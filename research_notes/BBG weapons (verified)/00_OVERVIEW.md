# BBG News weapons and VFX bible: overview

This is the top page of the BBG News weapons and VFX bible. It covers what was researched, the combat effects every weapon shares, the rules for showing weapons in 13+ cartoon shorts, the biggest corrections to the character files, and how much of each weapon's look is confirmed.

The detail for each weapon lives in the 14 dossiers published with this page:
- **11 class dossiers:** `b-1000`, `oliver`, `riggs`, `huggable`, `tillman`, `astoria`, `wil`, `graham`, `botch`, `saberi`, `sanchez`. Each includes its gap addenda.
- **3 topic dossiers:**
  - `combat-vfx`: combat VFX and death conventions
  - `2026`: BBG 2026 re-release weapon changes
  - `shared`: unassigned, shared and special weapons

The overview summarises those dossiers and does not repeat their per-weapon detail. Section 5.2 is the exception: it adds one new check made for this overview, a pass through the 2026 playtest Gear Up menus.

**Labels used on every claim:**

| Label | Meaning |
|---|---|
| [Canon] | SkyVu's own words |
| [Game text via wiki] | In-game item text that the fan wiki quotes as official |
| [Fan-wiki] | The wiki's own descriptions, trivia and stats |
| [Observed] | Seen in an image or frame a researcher opened |
| [Inference] | Reasoning |
| [Unverified] | Could not be confirmed |
| [BBG News invention] | A proposed look where nothing documents it |

**Eras:**

| Era | What it covers |
|---|---|
| BB-1 / BB Zombies (BBZ) / BB Zero | Earlier story games |
| BBR | Battle Bears Royale, Oct 2011 to Apr 2013 [Fan-wiki] |
| BBG | Battle Bears Gold, relaunched May 24, 2013, with updates to 3.0.x in 2021 and 2.53.x builds in 2022–23 [Fan-wiki; Observed] |
| BBG 2026 | Steam, iOS and Google Play re-release on Nov 4, 2026 [Canon] |
| BBH | Battle Bears Heroes, soft launch May 2023, global Oct 2024 [Fan-wiki] |

---

## 1. What was researched, and which sources were reachable

### Scope
- **The roster.** All 187 BBG weapon pages on the fan wiki: 77 primaries, 64 secondaries and 46 melees, removed weapons included [Fan-wiki; Inference: arithmetic].
  - 183 of these sit in Category:BBG Weapons.
  - 4 are real weapons missing from that category: MuskIt, Bind Field, Traffic Light and Social Butterfly (BBG).
  - The category also holds two non-weapons: The Incredible Riggs (a skin) and "Soldier (BBG)/Weapons" (a list page).
- **Beyond the roster.** The 10 Specials, the status effects, pickups, death and kill conventions, BBH and BB Overclock equivalents, unshipped concept art, and everything new in the 2026 re-release.
- **The quick-reference table.** It has 443 rows across all passes. Deduplicated, it covers all 187 BBG weapon pages, plus the extras listed in 5.1 and sub-topic rows.
- **How each dossier was built:** a draft, then a source check that re-fetched every quote, then an image check that re-opened every image, then an edit. After that came a completeness critic and up to four rounds of gap passes per class.

### Reachable sources

| Source | What was used |
|---|---|
| Fan wiki (MediaWiki API) | Page wikitext, revision histories and dates, image files with upload dates, recent-changes log (only 7 edits in 2026, by one editor, none citing a 2026 source [Fan-wiki]). HTML pages return 403, so the API was used throughout. |
| Steam (app 4408320) | Store text (appdetails API), 5 screenshots, the 54 s "Battle Bears Gold Premium - Trailer", a 1.4 s store loop video, and all 7 Steam news posts (Feb 24 to Oct 14, 2026) with their banner images |
| SkyVu sites | battlebears.com (live; BBH-era character page and Shopify product JSON for merch), play.battlebears.com (sign-up page with the Oct 19–26 demo dates) |
| Official SkyVu YouTube ("BATTLE BEARS") | Titles, descriptions and dates through oEmbed and the innertube `next` endpoint, plus thumbnails. Covers 2013 launch-trailer and overhaul videos, 2026 shorts (Mar 4, Jun 20, Jun 25, Jul 2, Jul 6), the Aug 16 highlights, the Aug 21 livestream, the Aug 31 Sky Pirates video, the Oct 2 teaser and the Oct 12 Q&A. |
| Fan YouTube, 2012–2026 | Thumbnails (hq1–3, and 1280×720 maxres1–3 auto-frames) for hundreds of uploads, including about 28 2026 playtest uploads (Jul 9 to Oct 17). For a subset, the storyboard sprite frames were fetched through an Invidious mirror's storyboard data: 320×180 frames, one every 10 s or so. This subset includes the full JustNubz showcase (0–3080 s), SkyVu's Apr 2014 Oliver Overhaul, and several B-1000, Huggable, Riggs and Tillman clips. |
| App stores | BB Heroes App Store and Google Play screenshot sets |

### Not reachable
- **web.archive.org.** The connection was reset on every attempt, across all passes. No archived SkyVu blog post or patch note was re-read. That includes the BBR 1.3.1 blog, the BBG 2.6, 2.20 and 2.27 notes, and the Dead Eye post `battlebears.com/blog/item/138-the-weekend-update`. One saved copy of the 2.6 change log, from an earlier session, was used as [Canon]. Every other version date is [Fan-wiki].
- **YouTube video and audio.** Playback returns LOGIN_REQUIRED, and the transcript API returned FAILED_PRECONDITION. **No video was watched and no audio was heard.** Every YouTube claim rests on thumbnails or storyboard frames.
- **Reddit (blocked), Discord (no access), and web search** (returned nothing on the 2026 re-release).

### Two facts that change how the evidence must be read
1. **The Steam trailer and all five Steam screenshots are 2013 footage, not the 2026 build.**
   - The trailer is a re-edit of SkyVu's May 30, 2013 launch trailer, rfAyqVJrli4 [Observed: thumbnail pixel matches, MSE about 17–495 against a median of about 9,000; dating Inference, strong].
   - Each of the five screenshots is a frame of that trailer [Observed].
   - Use them as a 2013 look reference only, and never caption them as 2026 gameplay [Inference].
   - The gameplay matches too: the 2013 trailer's YouTube storyboard lines up with the Steam trailer at a constant offset of about 4 s, 45 of 55 frames [Observed, per 2026.md, "The Steam trailer is 2013 footage"].
   - That includes the Space Oddity clip (about 30.0–32.8 s) and screen_01, a frame of it. The maps research's Space Oddity dossier left its date open, because its pillar top blooms to near-white, unlike 2013–2021 fan captures, so it might be a newer or relit capture [Inference]. But the same moment, bloom included, is in the 2013 storyboard (2013 35–36 s = Steam 30.85–31.95 s) [Observed], so it is 2013 footage too [Inference, strong; research_notes/BBG maps (verified)/00_OVERVIEW.md, section 0, item 1]. Why it blooms is [Unverified]. It does not show the Oct 2026 lighting either [Observed, per the maps overview].
   - The Graham segment (about 7.25–10.5 s) is 2013 footage too: it is in the same storyboard (2013 12–13 s = Steam 7.95–8.95 s) [Observed, per 2026.md]. Its toon outlines do not date it to 2018 or later: some 2013 fan captures already have them (graham.addendum.md, Incidental findings 1) [Observed].
2. **The JustNubz "BBG All Classes Showcase" (-lAtv-j9Sms, Sep 20, 2026, Closed Playtest #4, build "3.0.5_2026.11.19_B1") is a Gear Up menu walkthrough.**
   - All 309 storyboard frames (0–3080 s) show the loadout menu: 3D models, item lists, description pop-ups and stat panels [Observed].
   - Whether any combat appears between the 10 s samples is [Unverified].
   - Watching it settles 2026 models, names and in-game text. It does not settle projectiles or impacts (see 5.3).

---

## 2. The shared combat VFX language

The `combat-vfx` dossier holds the full evidence. Gap-pass upgrades are folded in below.

### 2.1 Overall look
- **Two effect styles sit side by side** [Observed: 2013 captures and the Steam trailer]:
  - **Soft, billowing particle fire** with dark orange-brown smoke, and painterly semi-transparent cartoon flames (about #F47E3E / #FAA751).
  - **Hard-edged, flat-shaded, translucent faceted volumes**, used for specific blasts: domes, shard bursts, ice chunks, white faceted smoke puffs.
- **Shockwaves** are flat octagonal rings sliding along the floor: white on the space station, white/grey or orange in the cave [Observed].
- **Status effects** are flat 2D sprites floating over heads [Observed].
- **Ink outline.** The Steam trailer and its screenshots (2013 footage [Inference, strong]) and the Steam store loop video (date not established) give characters a thick black ink outline [Observed]. 2026 in-game captures with a HUD show it too: SkyVu's "Official Playtest Highlights" (build 3.0.0) and InstableGR's Oct 15 final-playtest upload (build 3.0.7) [Observed: combat-vfx.md, Ink outline]. This is not a clean 2026-only change:
  - 2013 footage already shows outlines on Gold Graham and the circuit-pattern Graham skins [Observed].
  - The default Graham has one by 2023 [Observed].
  - The 2026 playtest menu model shows none [Observed].
  - So outlines are skin- and era-dependent, and the in-game 2026 rule is [Unverified].
- **2026 effects.** SkyVu's final-playtest notes list "LIGHTING, EFFECT & TEXTURE IMPROVEMENTS" [Canon: image text in the Oct 14 Steam post]. 2026 effects may therefore differ from 2013 even where a weapon is unchanged [Inference].

### 2.2 How a kill looks (no blood anywhere in any source examined)

| Convention | What is seen | Label |
|---|---|---|
| Intact collapse | The victim goes limp and topples whole, usually face-down. In one trailer shot the corpse vanished in a single frame about 3 s later, with no fade. | [Observed: trailer 12.6–16.0 s, 31.7 s, 40.1 s, 41.1 s] |
| Break-apart ("gib") | The body pops into about 4–7 large, clean, toy-like pieces (head, torso and legs, backpack or flag) that keep their colours and show no insides. Seen after a Phat Man blast, a radiation detonation, a B-1000 close-range attack, Last Resort (B-1000 bursts into head, plates, cyan claw blades and gun in a white flash), and kills from Bouncing Betty, Blast-O-Mole, Hand Cannon, Doom Cloud and Gravity Well. | [Observed; per-weapon attribution often Inference] |
| What decides intact versus pieces | Unknown. The wiki ties gibbing to most Demo explosives. | [Unverified; Fan-wiki] |
| Huggable in BBG | Breaks into orange or pink plush pieces with gold sparkles | [Observed: trailer 9.0 s] |
| Huggable in SkyVu merch | Headless Huggable, white stuffing from the neck, vertical rainbow column. This is official art, not gameplay. | [Canon: "Huggable Rainbow Explosion" T-shirt, 2023] |
| Kill marker | Three blue lightning-bolt Joule tokens (blue bolt on a dark-maroon hexagon) drop where a player dies and vanish after 10 s. In BBG since v2.1. | [Fan-wiki; Observed in 2013, 2023 and 2026 frames] |
| Kill feed | "[killer] KILLS [victim]" with team-outlined portraits and a red X on the loser. Also "HEAD SHOT" (red crosshair on the victim's portrait), "SUICIDE", "ASSIST +11", and a green "OH BABY" (meaning unknown). | [Observed] |
| Not seen anywhere | Confetti; Tillman's "pink and red flesh" (wiki) | [Unverified] |

### 2.3 Hits
- **Melee contact:** 4–7 yellow five-point cartoon stars plus a one-frame bright flash; the knocked-out victim collapses face-down [Observed: 2013, 2021 and the 2013 trailer footage].
- **Beam hits:** pink four-point star sparks [Observed].
- **Bullet and explosive-round hits:** white or cream spiky starbursts [Observed: Minigun (Soldier), Gold Member, Bearail Gun, A Salt Rifle 2026].
- **Damage flash:** the target flashes flat bright (lemon yellow, white or white-blue) for about one frame [Observed].
- **Damage numbers:** none seen in any frame [Observed absence].

### 2.4 Explosions (the main families)

| Family | Examples |
|---|---|
| Lemon/white faceted dome or cube cluster, often with white or orange octagonal floor rings | Phat Man, the radiation self-detonation, Grenader, Bearzooka (2014–15 fan footage); a pale-yellow translucent style (about #FAFFB0) in 2026 frames [Observed] |
| White electric dome | Light Matter: white sphere wrapped in cyan lightning [Observed] |
| Black electric sphere | Dark Matter: opaque black sphere in cyan lightning [Observed, BBR 2012] |
| Coloured crystal or energy domes | Happy Hour (magenta crystal cone and ring), Cosmic Bomb (green sphere), Gravity Well (lime half-dome), Pain Field (magenta hex dome, not an explosion), Losing Your Head and Blow Dart (cyan) [Observed; some attribution Inference] |
| Soft fireball with dark smoke | Big Shot, Dragon Slayzer, Pie Bomb, Carpet Bomb [Observed] |
| Columns and scatters | Blast-O-Mole (a marching row of flame pillars), Fireworks (scattered orange fire puffs with spark flecks), Metal Crush (light column, then nested orange octagonal rings) [Observed] |
| Smoke | White or grey faceted puffs; Phat Man adds a white faceted mushroom cloud [Observed]. Shorts use no mushroom framing; see 3.5. |

### 2.5 Beams and tracers
- **Shape:** flat ribbons with a white-hot core [Observed].
- **Colour families** [Observed unless noted]:
  - **Hot pink / magenta (the most common):** Sci-Fi ASR, Sci-Fi HASR, Lightning Bolt, Greased Lightning, Bind/Adrenaline Gun, Plasma Machine Gun, Balance Beam, Electric Honey, Turret streaks, Energy Rifle (2013).
  - **Gold or yellow:** Bearail Gun (pencil-thin); Gamma Ray (thick ribbon with concentric arc rings at the muzzle).
  - **Rainbow:** Art of War, Bounce Lazer.
  - **Lime or mint:** Viperifle, Mamba's Boy, MuskIt jet.
  - **Cyan:** Energy Rifle (2016), Minigun (Combat Tech) (2016).
- **Colours drift between years.** For example, Energy Rifle and Minigun (Combat Tech) go from magenta in 2013 to cyan in 2016, so effect colour is era-specific [Observed; Inference].

### 2.6 Status effects
Every status is a flat sprite over the head unless noted.

| Status | Visual | Caused by | Label |
|---|---|---|---|
| Irradiated | Yellow disc (about #F0C30C–#FBFE13) cut into six wedges. The wedges drop out in stages until a yellow trefoil on a black disc remains. A Geiger tick speeds up. At 100 RP the target bursts (150–200 units, damaging others). | Gamma Ray, Gernobyl, Radiation Rod, MuskIt, Plasma Shotgun, Gamma Burst, Solar Wind Scar | [Observed; Fan-wiki] |
| Slowed / held | Chunky lemon-yellow block "Z" with a dark outline between two white crescent orbit arrows | Slow Motion Field, Glue Bomb, Bind Field, Phantom Hug, the Bind Gun until Jun 2021, Black Hole (likely) | [Observed] |
| Poisoned | Round skull, dark purple (about #410C3A) or green; the cloud takes the weapon's colour | Mother of Nature, Chaos Toss, Fear Orbit, Toxic Plague, Hazard Toy, Toxic Rifle, Kelowna | [Observed; Fan-wiki] |
| Controls reversed | Glossy lime "?"; music cuts and sounds echo | Sake Bomb, Daydreamer, Spin Baby Spin | [Observed; Fan-wiki] |
| Stunned | Blue Nugg bird with a white crest between white spin arcs; 2.6 s | Sucker Punch | [Observed icon; Fan-wiki] |
| Frozen | No icon. A closed faceted ice chunk, opaque white-lavender on top and translucent teal below, with the victim dimly visible inside. 2 s (S'no Matter) or 3 s (Let It Cold). | S'no Matter, Let It Cold | [Observed, low-res 2015; identity Inference] |
| Caffeinated | White coffee mug overhead, white dust at the feet | Caffeine Injection | [Observed; Fan-wiki] |
| Damage taken up | No icon; the target stands inside a magenta hex dome | Pain Field | [Fan-wiki; Observed] |
| Damage taken down | Whole-body team-colour wash: red, or cyan-blue on the blue team | Energy Barrier | [Observed] |
| Damage taken down | No icon | Invulnerable Field | [Fan-wiki] |
| Sped up | No icon documented, no image | Adrenaline Gun (2021+) | [Unverified] |
| Scoped | Red crosshair over the head during a sniper green lock | Sniper lock-on primaries | [Fan-wiki] |
| Blinded | Dark or Light Matter sphere; hawk or eagle feathers over the face; Fairy's Dust cloud; Parashoot canopy | various | [Observed; Fan-wiki] |
| Shielded | Four green / pale yellow-green heater shields orbit the player; also 4.5 s after respawn | Shield pickup | [Observed; Fan-wiki] |

### 2.7 Team colours
- **Where team colour shows** [Observed; Fan-wiki]:
  - accents: the Soldier's headband, bands and ammo straps; the Huggable's flag; Tillman's armour; Astoria's pack, belt and gloves; Riggs's gear; Wil's helmet and print;
  - the HUD and the kill-feed outlines;
  - Plant the Bomb gear.
- **Projectiles keep each weapon's own colour** [Inference from Observed].
- **Team-coloured effects:**
  - The only one in later BBG is the Energy Barrier glow (v2.3+) [Observed].
  - The Cloaking aura existed only in BBR v1.4.2 [Fan-wiki].
  - The Peek A Boo neon lines ran from v1.4.2 to v2.6 [Fan-wiki].
- **2026 flag:** some 2026 Huggables carry a white flag with rainbow dots, not a team flag [Observed]. Whether it is a skin flag is [Unverified].

---

## 3. Rules for showing weapons accurately in 13+ cartoon shorts

### 3.1 Pick one era per short and say which
Era-locked traps:

| Item | What changes | Label |
|---|---|---|
| Arbiter default gun | "Bind Gun" slows targets (Dec 2013 to Jun 2021). "Adrenaline Gun" speeds them up (Jun 2021 on). The 2026 menu uses the name "ADRENALINE GUN" with the post-2021 stats, but the 2026 class blurb still says "slow down opponents". | [Fan-wiki; Observed, see 5.2] |
| Bearail Gun beam | "originally had no golden laser"; SkyVu added it later (date unknown) | [Fan-wiki] |
| Removed weapons | Last Resort, Bouncing Betty (still live in 2.31, past tense by May 2020), Greased Lightning (wiki note Nov 2020, yet equipped in 2023 builds) | [Fan-wiki; Observed] |
| Healing Tent cross | Red until 2.53.5, then green | [Fan-wiki] |
| Peek A Boo and Cloaking outlines | Team-coloured only in BBR v1.4.2 (Cloaking) or v1.4.2–v2.6 (Peek A Boo) | [Fan-wiki] |
| Tillman's look | Teal pack in 2D art and BBH. In BBG 3D: red sash, a back bar carrying the secondaries, treaded wheels. | [Observed] |
| Steam trailer and screenshots | 2013 footage only, the Space Oddity clip (about 30.0–32.8 s) and screen_01 included; why that clip's pillar top blooms is unexplained | [Inference, strong; bloom cause Unverified] |
| BBH-only kit | Never in BBG shorts: Explosive Retreat, Sarcastic Air Strike, Doom Star, Huggable Splicer, Healing Turret, Firework Flurry, Photon Refractor, Turret Summon. Also never use BBH behaviour: the Boomstick's explosive pellets, the Adrenaline Gun's four staggered shots, the "Beebee gun" shell burst, Riggs's leap-smash. | [Canon BBH text; Inference] |
| Story-game Bearzooka | Green with hazard stripes is BB Zombies / BB-1 only | [Observed; Fan-wiki] |

### 3.2 From evidence to depiction
- **[Observed] look or effect:** copy it, including the sampled hex values. Treat those values as estimates: they are medians sampled from wiki images, frames and thumbnails, not official codes [Inference].
- **[Fan-wiki] or [Game text via wiki] only:** follow the text. Build the missing visuals from the house grammar in Section 2: the effect family, star sparks, the status sprite. Tag the invented parts [BBG News invention].
- **Nothing documented:** invent within the house grammar, label it, and keep it out of anything captioned "how it looks in the game".
- **Low-resolution or inferred attribution:** you may use it, but carry its label into the production notes, never a stronger one.

### 3.3 Default loadouts and where weapons sit on the body
Defaults are [Fan-wiki] unless noted. Exact looks and scale (in "× Oliver") are in each class dossier.

| Character | Default primary / secondary / melee | Carry convention |
|---|---|---|
| B-1000 | Grenader / Last Resort (removed; the wiki lists Smoke Screen as default since 2020) / Axecutioner. The 2026 livestream loadout shows the Grenader with an axe [Observed]. Signature promo kit: Bearail Gun + Shock N Claw + Metal Crush [Observed]. | Gun on the right forearm, melee on the left forearm, secondaries as back units. The Satellite stays docked on the back [Observed]. |
| Oliver | A Salt Rifle / Bearzooka / B.E.A.R. Club | Rifle at the hip; Bearzooka on the right shoulder [Observed] |
| Riggs | Beebeegun / Hivey League / Barbed Gloves | Miniguns and shotguns hip-held; melee is two gloves [Observed] |
| Huggable | Double Rainbow! / Tough Love / Bite Me | Abilities centred on itself; melees paired over both paws [Observed] |
| Tillman | Big Shot / Fireworks / Buzzard | Primaries in both hands; secondaries on the back bar; melees on two white back arms [Observed] |
| Astoria | Viperifle / Tomahawk / Battering Ram | Rifles two-handed; traps placed on the ground [Observed; Fan-wiki] |
| Wil | Boomstick / Batterito / Bow | Edibles hugged at the belly; the Pie Bomb carried flat on a palm [Observed] |
| Graham | Power Glove / Turret / T Square | Right hand; the T Square gripped by the blade like a club [Observed] |
| Botch | Doom Cloud / Pain Field / Crass Knuckles | No held props: translucent lime constructs float beside him [Observed] |
| Saberi | Energy Rifle / Missiles / Mallet | Secondaries on a khaki jointed "third arm" beside her head [Observed] |
| Sanchez | Bind Gun → Adrenaline Gun / Speed Field / Blade Augment | Prosthetic right arm. The Speed, Cloak and Invulnerable Field orbs come from the forearm gauntlet; the Drain Field is thrown [Fan-wiki]. The blade appears only when the melee is equipped [Observed]. |

### 3.4 Deaths, impacts and gore
- **A death is one of two things:** a floppy, intact pratfall, or a pop into clean toy pieces [Observed]. Add the three blue Joule bolts as the kill marker [Observed; their use as a kill marker in shorts is Inference]. A hard cut or a one-frame vanish is game-accurate [Observed once].
- **Huggables:** white stuffing plus a vertical rainbow column, following SkyVu's merch [Canon: merch art]. Plush chunks with gold sparkles are the in-game alternative [Observed]. Never show rainbow "blood" spray or confetti as if it were in the game; confetti is [BBG News invention].
- **Robots** shed bolts and plates; B-1000 really breaks into head, plates, claws and gun [Observed]. **Bears** throw sparks [BBG News invention].
- **Never reproduce gore-flavoured source material:**
  - the wiki's Tillman "pink and red flesh" and the Seesaw blood trivia;
  - the Field Medic "amputated limbs" and the Zombee Gun "bones": draw these as olive plush chunks and toy parts;
  - the "Skinless" Oliver skin;
  - the name "Blood Spurt" on screen.
- **Hits** follow the star convention in 2.3. Status sprites follow 2.6. They read clearly at Instagram size [Inference].

### 3.5 Content, rights and IP flags (13+)
- **Music:** no licensed music or lyrics. The wiki says a Kelowna kill plays "Thriller", and the Greased Lightning text quotes the song [Fan-wiki].
- **Item-text lines to keep off screen** [Game text via wiki]:
  - alcohol jokes (Phat Man, Sake Bomb);
  - "melt a face" (Steamshot);
  - "stalking children" (the Not-So-Slenderman skin text);
  - "ritalin" (Gummable).
- **No real-war imagery:** no mushroom-cloud or real-bomb framing for the Phat Man, which puns on a WWII bomb [Fan-wiki].
- **Avoid third-party IP:**
  - the Hulk (The Incredible Riggs);
  - Mario: the Old School Graham skin, which appears in nearly all 2026 Graham footage [Observed];
  - the Bullet Bill look of the Big Shot round.

### 3.6 Sound
Only a few sounds are documented [Fan-wiki]:
- Gamma Ray Geiger ticks that speed up and are audible to nearby players;
- the Bass Cannon's dubstep loop;
- the Propbearganda Bearbershop tune;
- music cut-out and echo under Controls Reversed;
- Wrench "metal noises";
- class barks.

Every other sound effect is [BBG News invention].

### 3.7 Captions and HUD
- **Captions:**
  - Say "classic 2013 look" for anything taken from the Steam trailer or screenshots, the Space Oddity clip (about 30.0–32.8 s) and screen_01 included. Name the source "the Steam trailer" or "Steam screenshot screen_0N", never "2026 trailer".
  - Say "2026 playtest" only for frames from the 3.0.x builds.
- **HUD-style elements** (kill feed, HEAD SHOT card, icons) are redrawn in original art, with no game UI or logos [BBG News invention].

---

## 4. Most important corrections to the character files

The dossiers hold about 150 correction entries. Below they are deduplicated and ranked. Paths are under `/home/user/thallo-site/bbg-news-repo/characters/` unless stated. All flagged phrases were re-checked today and are still present in those files [Observed: grep]. Each dossier's "Corrections" section has the full current text, the corrected text and the evidence.

### 4.1 Cross-file fixes (apply everywhere)
1. **"2026 trailer" / "2026 Steam screenshot" means 2013 footage.**
   - Re-label in `astoria.md` (line 49), `riggs.md` (line 52), `botch.md` (line 53), `saberi.md` (line 53), `graham.md` (line 49) and `tillman.md` (line 48).
   - Evidence: thumbnail pixel matches of rfAyqVJrli4 to Steam-trailer frames; the screenshots are trailer frames [Observed].
   - This includes the Space Oddity clip (about 30.0–32.8 s) and screen_01. The Space Oddity dossier left their date open, but the same moment is in the 2013 trailer's storyboard [Observed] (see section 1, fact 1). Only the clip's bloom is unexplained [Unverified].
2. **BBH items presented as BBG.**
   - Astoria's Explosive Retreat (loglines and the Fighting line).
   - Riggs's "astonishing leap and ground-smashing ability" and "Beebee gun … burst of shells".
   - Wil's Sarcastic Air Strike and "explosive pellets" Boomstick.
   - SkyVu's character page never names its game, so tying it to BBH is [Inference, strong].
   - Re-tag all of these BBH.
3. **"Rainbow confetti" deaths.**
   - `README.md` (line 57) and `riggs.md` (lines 17, 72) present confetti as if sourced.
   - Re-label it [BBG News invention]. Add the observed baseline: intact collapse or clean toy pieces. Add SkyVu's merch look for Huggables: stuffing plus a rainbow column [Canon: merch].
4. **Team colour.**
   - BBG 3D gear is team-coloured. Red is the BBG News default; blue is the same skin on the blue team [Fan-wiki; Observed].
   - Remove "blue headband" from Oliver's negative prompt.
   - Add the team-colour note to `README.md` (line 53).

### 4.2 Per-file fixes

| File | Wrong now | Fix | Evidence |
|---|---|---|---|
| `oliver.md` (lines 51, 75) | "green, hazard-striped" Bearzooka | Coral-red octagonal tube with glowing orange chevron or window panels, grey collars, grey-checkered flared end and pink hex muzzle cap. Shoulder-carried. Same design 2012–2026. Sampled about #A24D4E–#A54447 (2013) to #D05655–#E36F61 (2026 lighting). The green tube is the BB Zombies one. | Wiki Photo_19-04-13_12_02_26_PM.png; trailer 3.9–4.8 s; 2026 tutorial and Playtest #4 HUD; File:Bear.jpg "Bearzooka in BBZ" [Observed; Fan-wiki] |
| `oliver.md` (lines 50, 75, 76) | Green-and-grey harness, green backpack | 3D default (2012–2026): team-colour headband, wrist and ankle bands, brass-bullet bandolier, pale grey-white or lavender hex backpack with team trim. The green harness appears only in 2D art and menu icons (2012 card, BB-1, the BBR-era icon Sw_boots.png uploaded 2013-01-13). | OliverSkin.png; 2026 frames EQwloJnrOko, DAchqX_mi6Y, MhJakRqd9ew [Observed]; Soldier (BBG)/Skins [Fan-wiki] |
| `oliver.md` (gags) | Bearzooka "recoil blasts him through a wall" | No recoil is documented; the trailer shooter stays planted. Ground the gag in self-splash. "EASY TO KILL YOURSELF WITH IT!" is in-game text in the 2026 class card. | -lAtv-j9Sms storyboard 280 s [Observed]; Bearzooka page [Fan-wiki] |
| `oliver.md` (line 57) | "easy to kill yourself with" labelled [Game text via wiki] | Now [Observed: 2026 in-game class card]. On the wiki it is template text. | As above |
| `oliver.md` (katana, skins) | Katana from BB-1 only | BBG's katana is the Kumakiri. SkyVu's Jul 6, 2026 "Classic Oliver" short shows a katana swing (blue-violet arc, yellow stars). Add the Classic Oliver skin. | byri_kQBUS4 frames [Observed]; Kumakiri page [Fan-wiki] |
| `b-1000.md` (line 54, prompts) | Gun-arm read as the Grenader; "blue energy blade"; an axe "with a glowing cyan edge" | The screenshot gun-arm is the Bearail Gun; the cyan blades are the Shock N Claw; the Axecutioner never glows. Pick one loadout per shot: default (Grenader + grey axe) or signature (Bearail + cyan claws). | B-1000Skin.jpg vs Bearail_G.jpg and Grenader.jpg; trailer 2.6–7.0 s [Observed] |
| `b-1000.md` (defaults, extras) | Last Resort shown as current; extras list incomplete | Last Resort marked REMOVED on the wiki since 2020-11-09 and absent from the visible 2026 list. Use the 13-item 2026 list. Do not draw the orange hex back pack as the Last Resort device. | Wiki revisions; 2026 Gear Up storyboard [Observed] |
| `b-1000.md` (Satellite) | "drone" circling him | "A small orb that fires missiles whenever he fires" (also the 2026 in-game text). It stays docked in an orange cradle with cyan pads. | v2.7 store; 6zv-C5K11i4; 2026 storyboard 240 s [Observed] |
| `b-1000.md` (palette) | Unsampled picks | Sampled: eye cyan about #38D6D7; hardware orange #E58D2B / #A75C10; claw cyan #2BDCF1; Bearail beam #EDDC31–#F7E95C | [Inference: sampled] |
| `riggs.md` (line 56, prompts) | "Their look is undocumented"; "dark brawler gloves" | Looks are documented. Beebeegun: black boxy hip minigun, amber or candy-striped slats, gold hive with a bee, no coil. Hivey League: grey, gold hive, honeycomb muzzle. Barbed Gloves: mustard-yellow plush mitts in black barbed wire. The pink-hive, magenta-coil gun is the Electric Honey, not the Beebeegun. | Infobox captions "Riggs with the Beebeegun" / "…Electric Honey"; Jul 6, 2026 Steam banner [Observed] |
| `riggs.md` (lines 52, 57) | Unnamed red trailer skin | Rocky Horror (named on the 2026 menu, 250 Gas). Also on the 2026 menu: The Incredible Riggs, Lawyer Riggs, No More Mr Ice Guy. | Wiki; -lAtv-j9Sms frames [Observed] |
| `riggs.md` (gear) | Bandolier and green pack described as the default | Card-only. BBG 3D wears red team gear: helmet, harness with medallion, bands, round backpack. | 2013–15 Gear Up shots [Observed] |
| `huggable.md` | "steel bear-trap jaws"; blue-gem wristbands and knee brace; small banner; white antenna; metal belly | Black C-shaped jaws with rainbow-smeared teeth. 3D cuffs are dark grey with red lights. Tall narrow team banner on a pole. Antenna tipped with a red ball (blue in 2012–13). Grey-and-white stuffing (the wiki says "metalic"). List all 18 weapons. Phantom Hug has no launcher, and the "CANDY!" box is the Gummable skin. | Gear Up cards; LYH.jpg; trailer 3.0–3.9 s and 32.6 s [Observed] |
| `huggable.md` (gags) | Bearettas "squirt out"; Oliver "catches" Double Rainbow | Bearettas are strapped on and can't fire ("Huggables don't have thumbs" [Game text via wiki]). Double Rainbow! is two flat six-stripe ribbons orbiting at hip height, not a beam. | Image19.PNG; trailer 7.2–8.5 s [Observed] |
| `tillman.md` | Chest-hatch cannon; teal pack as the 3D default; wheels as an invention; "olive artillery shell"; four-weapon list | The Big Shot is a hand-held drum braced at the belly. The 3D model is pale pink-white with a red sash, a back bar of four red firecracker rockets (with grinning Huggable faces) and treaded wheels (observed, not invented). The card missile is the Phat Man. List all 18 weapons. The Blast-O-Mole is itself the projectile. 2.6 raised base health from 150 to 170 [Canon]. | Big_Shot.jpg; Tillman-default-front.png; trailer 21.7 s and 25.6–29 s; JWxY0Ung2Rs [Observed] |
| `astoria.md` | Grey-blue pack and black belt; teal-green eyes; "ram-skull club"; Explosive Retreat gags | In 3D: red team pack, belt and gloves; blue-teal eyes (about #5391A1). The Battering Ram head is a curled stone horn. Trailer skins: Assassino (Dead Eye card) and Call Off Duty (Viperifle). Add the Dead Eye, Fairy's Dust and the Tomahawk design. Two new weapons arrived Oct 15, 2026 (unnamed; one seen as a HUD icon only). | Gear Ups; trailer 12–17.8 s and 30 s; HKbwq7PolNc [Observed; fan claim] |
| `wil.md` | "red cap"; unsampled palette; partial kit | Default is a red padded helmet with chin strap, a white tank top with a team-colour ice-pop print and red-lit pads; it is still the in-match default in 2026. The trailer card is the Booty Duty skin. The 20-item kit; the BBG Boomstick is a non-explosive pump shotgun. Sarcastic Air Strike is BBH only. ABBi's design is split by era. | SkyVu 2012 animation test r7TipV3IYtI; renders; 2026 thumbnails [Observed] |
| `graham.md` | "black-rimmed glasses, red track jacket, orange drill-gun"; incomplete list; Gernobyl quote label; olive pack as default | The trailer look is the Instagraham skin; the "drill-gun" is the Gamma Ray. List all 17 weapons (add MuskIt and Bind Field). The Gernobyl App Store quote is a wiki transcription, and the quote is truncated. In-game backpack is a boxy red radio (team-coloured). The Turret cannot turn. | Instagrahamrl.png; Graham_default.png; trailer 7–12 s [Observed]; Updates page [Fan-wiki] |
| `graham.md` (Turret text) | Quotes "Use it wisely, you only get one at a time." | The 2026 Gear Up description reads: "PLACE THIS DEVICE ON THE GROUND WHILE FACING THE ENEMY AND IT WILL DO ALL THE KILLING FOR YOU! IF YOU WISH TO REPOSITION, YOU CAN ALWAYS USE THE SELF-DESTRUCT BUTTON TO DESTROY A TURRET & THEN PLACE A NEW ONE." The wiki line may be older or a different field. | -lAtv-j9Sms storyboard 2290 s [Observed: 2026 in-game text]; crop `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/overview/crops/texts2_x4.png` |
| `botch.md` | Green palm flame as base look; "two glowing orbs circling him"; incomplete list; colour #6CF542; 90 health; blue-lit bands | The palm flame is the Cosmic Fire (added 2.3); the default companion is the lime starfish Doom Cloud. Orbs hover one per paw and never circle. List all 15 (Hazard Toy is missing from the wiki class page). Sampled lime is about #A5FD23–#B0FF23. HUDs read 85 health in most years. In-game guards are red-lit. Allow poison-skull icons in weapon shots. | DefaultBotch2 vs BotchSkin.jpg; HUDs 2015–2026 [Observed] |
| `saberi.md`, `research_notes/Battle Bears character lore/saberi_sanchez.md`, `reports/Battle Bears character lore.md` | "purple core", violet #9B4DFF, blue-grey arm #7A7F86, "cartoon missiles" | Magenta glow (about #C000B0–#FC00FE). The 2014 art shows the Plasma Shotgun and Gamma Burst; SkyVu calls it "the preview art for Saberi's new weapons" [Canon]. Khaki jointed third arm with brass caps. Twin stacked grey-green missiles. Add Toxic Rifle, Landmine, ClubCobra and Social Butterfly. Durations are era-dependent. | saberi29 art; PlasmaMachineGun.png; SideMissiles.png [Observed] |
| `sanchez.md` | Bind Gun royal blue #1E6FD9; "short forearm blade"; all fields "from a button" | Cyan/azure, not royal blue. Card about #0991D4–#1CB5F3; 3D render steel-cyan about #468FAB (dim #2D6D8F–#367494); white-cyan round muzzle. The 2013–16 beam is a crackling hot-pink ribbon, and hits show the yellow-Z Slowed icon. No blade in gun poses. Only Speed, Cloak and Invulnerable come from the gauntlet; the Drain Field is a thrown leech that becomes a red, sunglasses-wearing, fanged projection with bats. | Sanchez_weapons.png; Bind_Gun.png; GoF3Hy4QQis; xAp9gFMriAU [Observed] |
| `sanchez.md` (2026 name) | "Bind Gun or Adrenaline Gun in 2026" | The 2026 Playtest #4 menu lists "ADRENALINE GUN" with Damage 7, Ammo 55, Reload 4, Duration 0.5, Speed +2%, the post-2021 wiki stats. The 2026 class blurb still reads "USE HIS UNIQUE WEAPONRY TO SLOW DOWN OPPONENTS". The 2026 effect itself is unseen. | -lAtv-j9Sms storyboard 2950 s and 2850 s [Observed; new in this overview]; crops `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/overview/crops/show_2950000_x4.png` and `texts2_x4.png` |

**Unresolved conflict to settle in the Sanchez dossier:** the Bind/Adrenaline Gun's length. One pass measured about 0.35× his height, another about 0.7–0.75× [Observed; the measurements disagree]. Re-measure on Bind_Gun.png before modelling.

### 4.3 Fixes already applied to the dossiers (no character-file change)
The Frozen look was upgraded from concept-only to the observed in-game ice chunk. The fix landed in `combat-vfx`, `tillman` and `shared`, in both the Markdown and the meta files. The concept image catches only the target's legs and back; it does not encase the target [Observed].

---

## 5. Confidence summary

### 5.1 How much of each weapon's look is confirmed (all 187 BBG weapon pages)

**How the counts were made:** each weapon takes the best label any row in its class dossier gives it, gap passes included [Inference: method]. The labels mean:
- **Observed:** the dossier rates the visuals as seen.
- **Partial:** the look is seen, but the firing or impact is missing, low-resolution, or tied to the weapon only by inference.
- **Documented:** text only, no image of the effect, or no image at all.
- **Unknown:** neither look nor effect is known.

| Class | Weapons | Observed | Partial | Documented | Unknown |
|---|---|---|---|---|---|
| B-1000 (Assault) | 14 | 7 | 7 | 0 | 0 |
| Oliver (Soldier) | 21 | 12 | 9 | 0 | 0 |
| Riggs (Heavy) | 20 | 7 | 13 | 0 | 0 |
| Huggable | 18 | 8 | 10 | 0 | 0 |
| Tillman (Demo) | 18 | 9 | 9 | 0 | 0 |
| Astoria (Sniper) | 18 | 4 | 13 | 1 (Eagle Standard) | 0 |
| Wil (Chub Scout) | 20 | 5 | 15 | 0 | 0 |
| Graham (Engineer) | 17 | 5 | 11 | 1 (Double Wrench, no image exists) | 0 |
| Botch (Assassin) | 15 | 10 | 5 | 0 | 0 |
| Saberi (Combat Tech) | 12 | 7 | 5 | 0 | 0 |
| Sanchez (Arbiter) | 14 | 5 | 7 | 2 (Cloak Field, Invulnerable Field) | 0 |
| **Total** | **187** | **79** | **104** | **4** | **0** |

**How to read the counts:**
- **The "Observed" count is generous for melees.** For 12 melees it means the model is seen and the hit falls back on the shared star convention: Seesaw, Whack-Tus, Presidentures, Bearettas, Beaver Feaver, Buzzard, Double Hug, Good Morning, T Square, Crowbar, Sledgehammer and ClubCobra. Without them, **67 weapons have an observed firing or impact frame** tied to them, at least by inference [Inference: count].
- **Most visual evidence is from 2013–2023, not the 2026 build.** About 15 weapons have any effect frame from 2026 footage [Inference: count from rows]. They are:
  - Bearail Gun, Gamma Ray, A Salt Rifle, Sci-Fi ASR, Balance Beam, Señor Potato;
  - Gravity Well, Rocket Propelled Lance, Plasma Shotgun, Gamma Burst;
  - O.C.O. Gauntlet, Metal Crush and the katana, in official 2026 shorts (build unverified);
  - Electric Honey, in a possibly edited fan thumbnail;
  - Energy Barrier.

**Items outside the 187:**

| Group | Items |
|---|---|
| New in 2026 | "DOCO GAUNTLET" (Soldier primary; menu only, see 5.2) — partial. Two Oct 15 Astoria weapons: one seen as a HUD icon only (partial), one unseen (unknown). |
| BB Heroes | Huggable Splicer observed; Healing Turret, Doom Star, BBH Boomstick and BBH Sniper Rifle partial; Sarcastic Air Strike and Explosive Retreat documented |
| BB Overclock | Viper Rifle unknown |
| Concepts | Unshipped concepts (focus Rods, Toucan, Super Scope, Slumberbun mine, Trebuchet): concept art only |

### 5.2 Which weapons the 2026 build carries (new check for this overview)
I read the storyboard frames that were already downloaded for the whole JustNubz Playtest #4 showcase (Sep 20, 2026, build 3.0.5_2026.11.19_B1). Each class's weapon lists and description pop-ups are legible at 320×180 [Observed: `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/oliver/gaps_r2/sb/-lAtv-j9Sms/cs_00.jpg` to `cs_15.jpg`; crops in `/tmp/claude-0/-home-user-thallo-site/91c60972-6d3f-51de-9a92-c1d563bcf5a4/scratchpad/weapons/dl/overview/crops/`].

**Result:** 178 of the 187 wiki weapons are named on screen, with one more probable [Observed].
- **Fully listed:** Oliver, Riggs, Astoria and Saberi.
- **Not seen in the sampled frames:**
  - Last Resort, Bouncing Betty and Greased Lightning, all three wiki-"removed";
  - Losing Your Head, Phantom Hug, Charged Run;
  - Bubble Gun, Hazard Toy.
  - One Graham melee entry, probably the Double Wrench, is illegible.
- **Caveat:** the lists scroll and the frames are 10 s apart, so absence is **not** proof of removal [Inference].

**Findings from the same frames:**
- **"DOCO GAUNTLET" is a separate Soldier primary in the 2026 list** (Buy 100 Gas). Its stat panel reads AOE 90, Explosives 90, Reload 2.5, Ammo 2, Speed +15%. Oliver is shown in the Dark O.C.O. skin with orange-red crackle [Observed, low-res: storyboard 460 s and 3070 s].
  - The wiki has no page for it [Fan-wiki: missingtitle].
  - It is very likely the "Dark OCO Gauntlet" in JustNubz's 1v1 video description [Inference].
  - Whether it is new in 2026 is [Unverified]. Steam's "80+ primaries" against the wiki's 77 leaves room for it [Canon; Inference].
- **The Arbiter default is named "ADRENALINE GUN" in 2026**, with post-2021 stats (see 4.2) [Observed].
- **Several weapons carry 2026 in-game text that the wiki lacks or words differently** [Observed: 2026 in-game text]:
  - Social Butterfly: "FORCE YOUR ENEMY TO BE HOOKED TO YOUR PROWESS LIKE A JUICY INSTAGRAM FULL OF HEARTS". The wiki stub has no text at all.
  - Power Glove: "THE PRECURSOR TO THE O.C.O. GLOVE, THIS WEAPON CAN RAPIDLY FIRE SMALL ORBS OF ENERGY…"
  - Turret: see 4.2.
  - Capital Pains: the 2026 text still describes the NASDAQ "down day" mode, which the wiki calls removed.
  - These can upgrade many [Game text via wiki] labels in the dossiers to [Observed: 2026 in-game text].

### 5.3 Biggest remaining gaps
1. **Default-loadout effects are still unseen, though shorts will use them most** [Unverified]:
   - Beebeegun bees in flight; the Hivey League cone; Barbed Gloves hits;
   - the Power Glove orb;
   - Turret rounds (pink streaks attributed by inference only);
   - the Grenader in a 2026 build;
   - the Adrenaline Gun speed-up and its marker;
   - the Bearzooka blast in official media (fan 2014–15 only).
2. **Weapons with no in-game image of the effect, or of anything:**
   - Double Wrench (no image at all);
   - Cloak Field and Invulnerable Field domes;
   - Eagle Standard in action;
   - Social Butterfly's effect (its text suggests a pull or "hook" [Inference]);
   - Rake spring-up; I Lava U mines;
   - Reverse Fountain spray; RPL blast;
   - Let It Cold freeze; Nova column;
   - Kelowna clone;
   - the DOCO Gauntlet orb;
   - both Oct 15 Astoria weapons.
3. **2026 look of nearly every effect.** "LIGHTING, EFFECT & TEXTURE IMPROVEMENTS" [Canon] means colours and shapes may have moved since 2013–2016, which already drifted (magenta to cyan beams).
4. **Mechanics that change the look but are unresolved:**
   - what makes a kill gib rather than collapse;
   - whether the 2026 ink outline is in-game;
   - Hazard Toy cloud colour (purple in 2018, green in 2021);
   - the white rainbow-dot Huggable flag;
   - Bearzooka ammo (1 or 2);
   - the Sanchez gun length conflict.
5. **Era dating.** Version dates for most items are [Fan-wiki], because SkyVu's archived notes could not be reached.

### 5.4 How to close them (cheapest first)
1. **Play the Steam Next Fest demo (Oct 19–26, 2026) and record our own footage.** This is the definitive 2026 look [Canon: play.battlebears.com dates]. Shot list:
   - each class's default loadout firing at a dummy or teammate;
   - one kill per default weapon;
   - every status sprite;
   - the Adrenaline Gun hit;
   - the DOCO Gauntlet.

   Then re-check against the Nov 4 launch build.
2. **Read the remaining 2026 in-game text from the showcase frames already on disk** (about 30 minutes). Upgrade the dossiers' quote labels and add the Social Butterfly and DOCO Gauntlet entries.
3. **Watch by hand, at full resolution:**
   - the JustNubz showcase (-lAtv-j9Sms, 51 min), for 2026 weapon models, taunts and stat panels at each chapter. It is a menu walkthrough, so it will not show projectiles.
   - match footage with chapters, for effects:
     - InstableGR's final PC playtest, HKbwq7PolNc (Oct 15; per-class match chapters);
     - InstableGR's PC Playtest #3, aujTcdFuxdE;
     - JustNubz 1MP1rFi4t-Q and uNZA3nlABOA;
     - [LA]Huggable "WE ARE BACK" games #1–7;
     - droid BBG CmYil-JJdC0 (Riggs) and Dwc66f0q9Rk / DEDQ517trWM (Oliver);
     - Mika_do's playtest parts.

   Pause on hits, kills and status sprites. Log timestamps against the open-questions lists in each dossier.
4. **Watch the unwatched official videos:**
   - Oct 12 Q&A (pmE2jKQLSms), for any weapon changes;
   - Aug 21 livestream, chapter "Character and loadout showcase" at 9:24 (xP27fWSCSKs);
   - Aug 16 highlights (C7uFxvSZ10c);
   - SkyVu's 2014 Riggs, Astoria, Tillman and Oliver Overhaul developer videos.
5. **Retry web.archive.org from another network** for the BBR 1.3.1 blog, the BBG 2.6/2.20/2.27/2.31 notes and the Dead Eye post. These would upgrade era dates from [Fan-wiki] to [Canon].
6. **Ask SkyVu directly**, since it approved BBG News. It asked playtesters on Oct 14 for UI-less footage [Canon]. A request for a weapons and effects reference, or confirmation of 2026 additions (DOCO Gauntlet, the two Astoria weapons), would settle the unknown rows fastest [Inference].