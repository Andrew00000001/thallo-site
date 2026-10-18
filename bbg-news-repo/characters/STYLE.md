# BBG News house style: feature-film 3D

Chosen by Bryce on 2026-10-17 from the 9-style board (style #4). The rebuilt character souls, model sheets and every short use this style. It replaces the earlier "chunky low-poly early-2010s mobile-game 3D" house style.

## The look

- **Render:** polished, stylized 3D animation with a feature-film finish. Soft, rounded shapes, appealing cartoon proportions and bold, readable silhouettes.
- **Faces:** expressive, with clear brows and eyes. Each character keeps the face shapes set in its soul (Oliver's heavy brows and smirk, Riggs's half-lidded glare, the Huggable's fixed toothy grin).
- **Surfaces:**
  - **Bears:** short, soft plush fur.
  - **Robot parts** (joints, plates, gear): clean painted metal or plastic.
  - **The Huggable:** fuzzy plush with visible stitched seams, a bandage and a button eye.
  - **Weapons:** colours and shapes from the verified weapons research.
- **Lighting:** soft global illumination, a warm key light, a cool fill and a gentle rim light, with cinematic depth of field.
- **Colour:** saturated but natural. Red team is the default.
- **Frame:** 9:16 vertical, composed for Reels.

## Habits that keep it from looking generic

1. **Same references every shot:** use each character's Element or model sheet in every image and video, so faces and gear never drift.
2. **One lighting setup per scene:** keep it fixed across shots, with no mid-scene changes of time of day or colour.
3. **Snappy timing:** strong poses, quick moves and clear holds (squash and stretch). Avoid slow, floaty, drifting motion and constant camera wander.
4. **Simple staging:** one clear action per shot and few characters on screen. Keep backgrounds uncluttered.
5. **Check every take:** reject any take with morphing, extra limbs, melted props or changing gear. Never post a take that breaks the model sheet.
6. **Finish when editing (free):** a light film grain, one consistent colour grade per episode, and the standard end card.
7. **Label it:** every short stays labelled as an unofficial AI fan film (see the README's end card and caption rules).

## Prompt wording

- **Model sheet:** "Fan-art character model sheet (front, side, back and three-quarter views) of *Name*, *description*; polished stylized feature-film 3D animation character, soft rounded shapes, expressive face, soft plush fur, clean painted metal robot parts, bold readable silhouette. Neutral grey background, even studio lighting, no text."
- **Video suffix:** "Polished feature-film 3D animation, soft rounded shapes, expressive faces, soft plush fur, soft global illumination, cinematic lighting, snappy cartoon timing with strong poses and holds."
- **Framing line:** "Vertical 9:16 framing.", placed right before the video suffix in every video starter and weapon shot.
- **Shared negative list:** photorealistic fur, realistic anatomy, blood, gore, sexual content, real-person likeness, official logos, text, watermarks, morphing, extra limbs, low-poly, flat 2D.
  - **Sanctioned variant:** Saberi only: "extra paws, extra legs, a second mechanical arm" replaces "extra limbs", because her third arm is a defining feature. No other soul changes these strings, apart from the per-shot rules below.
- **Weapon shots:** one shot = the character line from the soul's video starter + one action (a weapon snippet replaces the starter's own action, never adds to it) + the framing line "Vertical 9:16 framing." + the video suffix, which always comes last.
- **Colours in prompts:** write colours as words in every prompt; keep sampled or placeholder hex codes in a separate "Colour key (outside the prompt)" line, for tools that accept a palette and for checking takes. Generators paint hex codes as swatches or text.
- **Weapon names:** keep in-game weapon names out of image and video prompt text, because tools read them literally ("Doom Cloud" becomes a storm cloud, "Bearzooka" invites lettering or a generic green bazooka). Describe each weapon by its look, and keep the name in the snippet title, labels and notes.
- **Paste-ready text:** keep notes, sheet choices, overlay reminders and per-shot negative changes out of the text to be pasted: put them after a closing quote or in a separate line marked as not for pasting, so no note or status-sprite name reaches a tool.
- **Co-stars in frame:** a negative applies to the whole frame, so in shots with other characters drop any negative term that describes a co-star (its fur, eyes, build, clothing or gear) and rely on each character's Element. A soul may also keep such terms in a "solo shots only" line.
- **Faceted effects:** where the research shows a hard-edged faceted blast, dome, cube cluster, shard burst or ice chunk (00_OVERVIEW §2.1 and §2.4), render it as crisp cut-crystal facets with smooth bevelled edges inside an otherwise smooth shot. Faceted smoke puffs and goo become soft rounded puffs and glossy blobs, and soft particle fire stays soft. In any shot that prompts a faceted effect, swap "low-poly" in the shared negative for "low-poly character models".
- **2D flashbacks:** a clearly marked BB-1, BB Zombies or BLAST flashback may use a 2D-cel look; drop "flat 2D" from that shot's negative only. Every other alternate look is rendered in the house 3D style.
- **Status sprites and HUD graphics** (Irradiated disc, Slowed Z, Poisoned skull, Controls Reversed "?", Stunned bird, reticles and lock brackets, HEAD SHOT and kill-feed cards) are never written into an image or video prompt. Generate without them, keep the full negative list, and add them in the edit as original-art overlays drawn to 00_OVERVIEW §2.6 (§2.2 for the kill feed and HEAD SHOT card): Controls Reversed is a glossy lime "?"; Slowed is a chunky lemon-yellow block "Z" with a dark outline between two white crescent orbit arrows; Poisoned is a round dark-purple or green skull.

## Still to do

Done: the eleven character souls were rebuilt in this style on 2026-10-18, with the verified weapons research applied (for example, the Bearzooka is coral-red, not green). Still to do: make the model sheets and the short scripts in this style from the rebuilt souls.
