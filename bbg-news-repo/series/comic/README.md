# BBG News comics: lettering and page assembly

`letter.py` turns a pages JSON into finished Instagram carousel slides. It cover-fits the panel art (feature-film 3D stills built with the souls and Elements, per `characters/STYLE.md`), draws the panel borders and letters every page: speech balloons, shouts, whispers, thought clouds, captions, B-1000's HUD boxes, SFX, the cover title and the end card.

It uses Python 3 with Pillow and the standard library only.

```
python3 letter.py pages.json --out DIR [--root DIR_OF_IMAGES] [--jpg]
                  [--only s01,s02] [--guides] [--sheet] [--strict] [--fonts DIR]
```

| Flag | What it does |
|---|---|
| `--out DIR` | Writes `DIR/<page id>.png` for every page, at exactly the canvas size, sRGB, with an sRGB ICC profile embedded. |
| `--root DIR` | Panel `image` paths are relative to this folder. The default is the JSON file's folder. |
| `--jpg` | Also writes `DIR/<page id>.jpg` at quality 92 (4:4:4 chroma, so red and cyan lettering stays crisp). |
| `--only` | Renders only the listed page ids. |
| `--guides` | Also writes `DIR/guides/<id>.png`, an overlay showing the 40 px margin (green), Instagram's 3:4 profile-grid crop (magenta dashes), panel ids and sizes, letter boxes (cyan), tail targets (red crosses) and face boxes (red). Use it to place balloons. |
| `--sheet` | Also writes `DIR/contact_sheet.jpg`, all slides side by side. |
| `--strict` | Exits with status 2 if there was any warning (margin, gutter, overlap, face, off-canvas, size or font). |
| `--fonts DIR` | Font folder. The default is `assets/fonts/` in this repo (or `$BBG_FONT_DIR`). |

Warnings print to stderr and never stop a render, so pages can be previewed before every panel exists.

## The pages JSON

```json
{"canvas": [1080, 1350], "background": "#0d0d10",
 "pages": [
  {"id": "s01",
   "panels": [{"id": "p01", "rect": [40, 40, 1000, 620], "image": "panels/p01.png",
               "focus": [0.5, 0.4], "border": 6}],
   "letters": [{"type": "balloon", "text": "Oliver, we'll getcha... **home.**",
                "panel": "p01", "box": [80, 80, 420], "tail": [610, 420]}]}]}
```

- **Units.** `rect`, `box`, `tail`, `poly`, `faces` and `avoid` are canvas pixels, from the top-left. `focus` is a fraction (0–1) of the source image. Sizes are pixels on the canvas; the defaults below are for a 1080 px-wide canvas and scale with the canvas width.
- **Canvas.** The default is `[1080, 1350]` (Instagram 4:5). A carousel holds at most 20 slides; the script warns past that.
- **Order.** Panels are drawn first, then letters in list order, so later letters sit on top.
- Any key not listed can be left out.

### Page keys

| Key | Meaning |
|---|---|
| `id` | Slide id and output file name (`s01` → `s01.png`). Name slides so they sort in carousel order. |
| `panels` | List of panels (below). Can be empty. |
| `letters` | List of letters (below). |
| `background` | Overrides the top-level `background` (the gutter colour). |
| `avoid` | List of `[x, y, w, h]` boxes, usually faces. Any balloon, caption, HUD or end card body on one is a warning, and so is a tail tip that ends inside one. |

### Panel keys

| Key | Meaning |
|---|---|
| `id` | Panel id, used by letters' `panel` key and shown on placeholders and guides. |
| `rect` | `[x, y, w, h]`. The border is drawn inside it, so neighbouring rects give exact gutters. |
| `poly` | Instead of `rect`: a list of `[x, y]` points for a slanted or angled panel. The art cover-fits the polygon's bounding box, with antialiased edges and an inside border. |
| `image` | The panel art. A missing file renders as a labelled grey placeholder (panel id, file name, size) and a warning. |
| `focus` | `[fx, fy]`, the point of the source image kept centred in the crop (clamped so the crop never leaves the image). Default `[0.5, 0.5]`. |
| `zoom` | Crops tighter than a plain cover-fit, for example `1.4` to pull a close-up out of a wider still. Values below 1 are treated as 1 (no letterboxing). |
| `border` | Black border width in px (default 6; `0` for none). |
| `border_color` | Border colour (default black). |
| `bleed` | `true` for a full-bleed panel (such as the cover) that may cross the margin. |
| `faces` | `[x, y, w, h]` face boxes in canvas px, checked like the page's `avoid`. |

Layout rules the script checks: a 40 px outer margin, gutters of 16–24 px between neighbouring rect panels, and no overlapping panels. Instagram's 3:4 profile grid trims about 34 px from each side of a 4:5 cover, which the 40 px margin covers.

### Letter keys (all types)

| Key | Meaning |
|---|---|
| `type` | `balloon`, `shout`, `whisper`, `thought`, `caption`, `hud`, `sfx`, `title` or `endcard`. |
| `text` | The words. `\n` forces a line break; `**word**` sets emphasis. Dialogue types are set in capitals automatically. |
| `panel` | The panel the letter belongs to. It's checked, and used by `clip`. |
| `box` | `[x, y, w]`: the top-left corner and the maximum outer width of the letter. The height is automatic. A fourth value sets a minimum height for captions, HUD boxes and end cards, or a maximum height for SFX and titles. |
| `tail` | `[x, y]`: the point the tail aims at, the speaker's mouth (for B-1000, his head). The tail stops short of it by `tail_gap`. |
| `size` | Text size in px. Dialogue (balloon, shout, whisper, thought, caption, HUD) never goes below 30; a smaller value is raised to 30 with a warning. |
| `font`, `bold` | Font keys (table below) or a font file path, for the body and the `**emphasis**` text. |
| `color` | Text colour. |
| `fill`, `outline`, `outline_width` | Shape fill, outline colour and outline width in px. |
| `upper` | `false` keeps the text's own case. |
| `lead` | Line spacing as a multiple of the size (dialogue default 1.17). |
| `fit` | `snug` (default) lets the shape shrink to hug the text; `box` keeps the full `box` width. |
| `anchor` | Where a snug shape sits inside `box`: `left`, `center` or `right` (balloons default to `center`, captions and HUD boxes to `left`). |
| `clip` | `true` clips the letter to its panel's shape (handy for SFX). |
| `bleed` | `true` allows the letter to cross the 40 px margin without a warning. |
| `id` | A name for warnings and guides (default `type#n`). |

Colours are `"#rgb"`, `"#rrggbb"`, `"#rrggbbaa"`, a CSS colour name, or `[r, g, b, a]`.

Every letter is kept inside the canvas: a shape that would run off is moved back in, with a warning. Balloons, captions and HUD boxes that overlap each other are warnings too.

### Letter types

**`balloon`**: the speech balloon. A white rounded ellipse (a superellipse, rounder than an oval) with a 3.5 px black outline, centred capitals in Comic Neue Bold at 36 px, and a tapered, gently curved tail that grows out of the balloon edge with no seam. The text wraps to fit the shape: the script tries every width up to `box` and every line count and keeps the most compact balloon close to a 1.9 : 1 shape, which gives the classic lozenge of short, long, short lines. Extra keys: `tail_gap` (default 0.8 × size), `tail_curve` (bend, default 0.14; 0 is straight, negative bends the other way), `tail_width` (base width as a multiple of size, default 0.78), `roundness` (superellipse exponent, default 2.3; 2 is a plain ellipse), `aspect` (preferred width-to-height, default 1.9), `pad_x`, `pad_y` (clearance as a multiple of size, defaults 0.55 and 0.42), `nudge_y` (px).

**`shout`**: a spiky burst balloon with emboldened 40 px capitals. The spike nearest the speaker becomes the tail. Extra keys: `spike` (spike length × size, default 0.62), `spike_spacing` (default 1.05 × size), plus the balloon keys. Spikes are random but repeatable (seeded from the page, letter and text).

**`whisper`**: a balloon with a dashed outline, the tail dashed too, and lighter Comic Neue Regular text at 33 px in dark grey. Extra keys: `dash` and `dash_gap` (× size, defaults 0.55 and 0.34), plus the balloon keys.

**`thought`**: a cloud of round puffs with a trail of three shrinking bubbles that leads toward `tail`. Extra keys: `bump` (puff radius × size, default 0.72), plus the balloon keys.

**`caption`**: a rectangular narration box, pale yellow (`#fff1a8`) with a 3 px black outline, centred capitals at 32 px. Lines are wrapped evenly. Extra keys: `align` (`center`, `left`, `right`), `radius` (corner radius px), `shadow` (`true`, or `[dx, dy]` in px, for a hard offset shadow), `shadow_color`.

**`hud`**: B-1000's LIVE box. A near-black translucent box with faint scan lines, a thin cyan outline and glowing cyan corner brackets, uppercase Share Tech Mono text in cyan with a soft glow. Extra keys: `live: true` adds a red "● LIVE" tag on the first row; `color` is `"cyan"` (default), `"white"` or any colour; `accent` recolours the outline and brackets; `align` (default `left`); `tail` draws a thin cyan leader line with an elbow from the box to a small lock ring on the target (B-1000's head, or the thing he is reporting on); `ring` (ring radius px, default 13); `scanlines: false`; `live_color`.

**`sfx`**: huge display lettering in Bangers: a yellow-to-orange gradient fill, a thick dark outline and a 3D extrusion, letters bouncing up and down a little, the whole word tilted. With no `size`, it fills the `box` width. Extra keys: `angle` (degrees; positive tilts counter-clockwise, so the word rises to the right; default 8), `fill` (a fill without `fill2` is solid), `fill2` (gradient bottom colour), `outline`, `outline_width` (× size, default 0.075), `extrude` (depth × size, default 0.07; 0 for none), `extrude_angle` (degrees, default 60, down and to the right), `extrude_color`, `bounce` (× size, default 0.05), `grow` (the last letter is 1 + grow times the first, for a rising "WHUMMM"), `outline2` and `outline2_width` (a second, outer outline), `shadow`, `font`.

**`title`**: the cover title. Big Bangers lettering with a gold gradient, a thick dark outline and a soft drop shadow, centred in `box`. With no `size` it fills the `box` width; `"fit": "lines"` sizes every line to the width separately, capped at `max_ratio` (default 1.45) times the smallest line, for a stacked "WE'LL GETCHA / HOME" title. Extra keys: as for `sfx`, plus `shadow` (`true`, `false`, or `[dx, dy]` as a multiple of size; default `[0.045, 0.06]`), `shadow_color`, `shadow_blur` (× size), `align`. `"font": "anton"` switches to the BBG News Anton face.

**`endcard`**: a full-width box of small centred text: Barlow SemiBold at 26 px, off-white on the BBG News near-black, with a gold rule along the top. With no `box`, it spans the margins and sits on the bottom margin. Extra keys: `rule` (colour, or `null` for none), `fill`, `color`, `outline`.

### Text details

- **Capitals and the letter I.** Dialogue is set in capitals. Comic Neue draws every capital I with crossbars; lettering convention keeps the crossbar I for the pronoun only (I, I'M, I'LL, I'D, I'VE), so every other I is drawn with the font's plain vertical stroke.
- **Emphasis.** `**word**` sets the word in Comic Neue Bold Italic, the usual comic emphasis.
- **Missing glyphs.** A character a font lacks (Comic Neue has no "●", for example) is drawn from Barlow, or from DejaVu Sans when Barlow lacks it too and the system has it, never as an empty box.
- **Sizes.** Defaults: balloon and thought 36/34, shout 40, whisper 33, caption 32, HUD 32, end card 26 px. Never set dialogue below 30.

## Fonts

All fonts live in `assets/fonts/`, each with its licence file beside it. Every font here is under the SIL Open Font License 1.1, which allows use in published images; the fonts themselves may be redistributed only with the licence.

| Key | File | Used for | Licence | Source |
|---|---|---|---|---|
| `comic` | `ComicNeue-Bold.ttf` | Dialogue | OFL 1.1 (`OFL-ComicNeue.txt`), © 2014 The Comic Neue Project Authors | Google Fonts repo, `https://raw.githubusercontent.com/google/fonts/main/ofl/comicneue/ComicNeue-Bold.ttf` (upstream `https://github.com/crozynski/comicneue`, commit c5ee07b) |
| `comic-italic` | `ComicNeue-BoldItalic.ttf` | `**Emphasis**` | as above | `https://raw.githubusercontent.com/google/fonts/main/ofl/comicneue/ComicNeue-BoldItalic.ttf` |
| `comic-light` | `ComicNeue-Regular.ttf` | Whispers | as above | `https://raw.githubusercontent.com/google/fonts/main/ofl/comicneue/ComicNeue-Regular.ttf` |
| `bangers` | `Bangers-Regular.ttf` | SFX and titles | OFL 1.1 (`OFL-Bangers.txt`), © 2010 The Bangers Project Authors | `https://raw.githubusercontent.com/google/fonts/main/ofl/bangers/Bangers-Regular.ttf` (upstream `https://github.com/googlefonts/bangers`, commit ca6d2f1) |
| `mono` | `ShareTechMono-Regular.ttf` | B-1000's HUD | OFL 1.1 (`OFL-ShareTechMono.txt`), © 2012 Carrois Type Design, Reserved Font Name "Share" | `https://raw.githubusercontent.com/google/fonts/main/ofl/sharetechmono/ShareTechMono-Regular.ttf` |
| `anton` | `Anton-Regular.ttf` | Alternative display face | OFL 1.1 (`OFL-Anton.txt`) | Already in the repo |
| `barlow` | `Barlow-SemiBold.ttf` | End card, placeholders, glyph fallback | OFL 1.1 (`OFL-Barlow.txt`) | Already in the repo |

Comic Neue, Bangers and Share Tech Mono were downloaded on 2026-10-26 from the Google Fonts GitHub repository (`github.com/google/fonts`), each with its `OFL.txt` saved as `OFL-<Name>.txt`. SHA-256:

```
3e7e5fccfd7e0788f317b43312151c1bd5cf058c9697a8d83eac3939050bd61e  ComicNeue-Bold.ttf
5c312c2a2fa64eee82f3b87fcfab8f3b12a5e59b043124401d322eb323cfbf16  ComicNeue-BoldItalic.ttf
a0ee5a37c8b27c4db0700137d928598b1e23b0089e1546a8961909176b779360  ComicNeue-Regular.ttf
4160a7311de9342674cce9160cde9fcbb30f48190397d86ff1b70b455af65824  Bangers-Regular.ttf
9ceab1f87414829af259c0f537573ae03ef7dd3147c0b27a36a1a0beb6732677  ShareTechMono-Regular.ttf
```

If a font file is missing, the script falls back (Comic Neue → Barlow, Bangers → Anton, Share Tech Mono → Barlow) and prints a warning, so check the output before posting. Share Tech Mono's Reserved Font Name means a modified copy must be renamed; we use it unmodified.

## Rendering notes

- All vector lettering is drawn at 4× and box-filtered down, so outlines, tails and burst points are antialiased and crisp.
- Panel art is resampled with Lanczos straight from the source crop. An embedded colour profile is converted to sRGB first, and an alpha channel is flattened onto black.
- Text has no colour profile of its own; output files carry an sRGB ICC profile so Instagram reads the colours as sRGB.

## Limitations

- The script can't see faces. Mark them with `faces` or `avoid` and it will warn when a balloon body or tail tip lands on one; check every page with `--guides` and by eye.
- Balloons don't join (no linked balloon pairs), and a balloon has one tail.
- Wrapping never hyphenates. A word wider than its box widens the shape with a warning; a balloon word wider than the canvas stops the render.
- Text runs left to right in Latin script only. Kerning works within a run; it is not applied across an emphasis change.
- The end card type takes any text. `characters/README.md`'s end card wording is written for shorts ("Unofficial fan film..."); whether the comic says "fan comic" is Bryce's call.
