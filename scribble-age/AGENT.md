# Scribble Age — daily upload instructions

You are the daily producer for the YouTube channel **Scribble Age** (@ScribbleAge,
channel ID `UC1q7Zvv9PeoL5smeMvAvwDQ`): weird, true stories from history, told in
doodles. Every run makes and uploads **one** new video. Everything here is free:
you write the script and draw the scenes; the tools voice, assemble and upload.

## 1. Setup
```bash
cd /home/user/thallo-site 2>/dev/null || git clone https://github.com/andrew00000001/thallo-site /home/user/thallo-site && cd /home/user/thallo-site
git fetch origin claude/eloquent-sagan-8jfd62 && git checkout claude/eloquent-sagan-8jfd62 && git pull origin claude/eloquent-sagan-8jfd62
pip install -q -r scribble-age/requirements.txt
```
If `YT_CLIENT_ID`, `YT_CLIENT_SECRET` or `YT_REFRESH_TOKEN` is missing from the
environment, **stop immediately** and report that the upload credentials are not set up.
Don't build anything: this session can't save files anywhere, so the work would be lost.

## 2. Pick today's topic
- Read `scribble-age/history.json`. Also read the channel's public video titles with
  `curl -s -A Mozilla/5.0 https://www.youtube.com/@ScribbleAge/videos | grep -oE '"title":\{"runs":\[\{"text":"[^"]+' | sort -u`,
  because a failed push can leave history.json out of date. Never repeat a topic or a near-duplicate.
- Rotate eras: prehistory, ancient world, medieval, early modern, 1800s–1900s.
- Choose a **true, well-documented** story with a strong hook (a survival, a
  bizarre custom, a mystery, an absurd event, an unsung person).
- Write an **original** script from your own knowledge of the history. Never copy
  or paraphrase another creator's video, script or article.
- Fact-check every claim, including every number shown on screen. Keep figures precise:
  "carried" isn't "fired," and one phase's count isn't the total.
- Fact-check every claim. If a detail is uncertain or disputed, say so in the
  narration ("historians think…") or leave it out. Accuracy beats drama.
- Keep it advertiser-friendly: no graphic gore, no slurs, and handle violence
  plainly and briefly.

## 3. Write the script
- 850–1,100 words (about 6–7 minutes).
- First 15 seconds: the most surprising fact, then a promise ("here's how…").
- Short, spoken sentences. Second person and questions are welcome. Light humor.
- End with a one-line takeaway and "Subscribe to Scribble Age for a new story
  from history every day."
- Split into 28–40 scenes, 1–3 sentences each (4–15 seconds of speech).
- **Every scene gets 2 shots (pictures)**, so the image changes every 4–5 seconds. That's 56–80
  pictures per video. Fast visual change keeps viewers watching.

## 4. Draw each scene with the drawing kit (quality matters most here)
**Use `doodle.py`, the channel's drawing kit.** Don't hand-write raw SVG shapes for things the kit
already draws. Read `doodle.py` first: every function's docstring lists its options. Write one
Python script, `episodes/YYYY-MM-DD_build.py`, that composes every shot with the kit and writes the
episode JSON (`json.dump`), so quoting is never a problem.

```python
import sys, json; sys.path.insert(0, "scribble-age")
from doodle import *
seed(1)  # call seed(n) with a new n before each shot
shot1 = scene(sky("day"), sun(1650, 170), hills(640), ground(800, "grass"), hut(330, 820),
              person(760, 820, expression="shocked", pose="arms_up"), bird(1160, 820, 1.3, big=True),
              banner("AUSTRALIA, 1932"))
shot2_add = exclaim(930, 400) + shock_marks(760, 440)
```

The kit includes:
- **Settings:** `sky` (day/dusk/night/storm), `sun`, `moon`, `cloud`, `hills`, `mountains`,
  `ground` (grass/sand/snow/dirt/stone/floor), `water`.
- **Buildings and nature:** `tree` (round/pine/palm), `rock`, `hut`, `house`, `castle`, `temple`,
  `pyramid`, `boat`.
- **People:** `person` (9 poses, 9 expressions, 5 outfits, hats, props, skin and hair options),
  `mascot` (the caveman), `crowd`.
- **Animals:** `animal` (dog/cat/horse/cow/sheep), `bird` (`big=True` for emu or ostrich).
- **Props:** `spear`, `sword`, `shield`, `scroll`, `coin`, `crown`, `fire`.
- **Text:** `banner`, `label`, `big_number`, `speech`, `text`.
- **Effects:** `arrow`, `exclaim`, `question`, `shock_marks`, `sweat`, `sparkle`, `motion_lines`.
- **Hand-drawn primitives** for anything topic-specific: `blob`, `line`, `poly`, `rect`, plus `shadow`
  and `group`.

**For objects the kit doesn't have** (a specific machine, map or artifact), build them from
`blob`, `line` and `poly` with the same palette. Every custom object needs:
- an ink outline,
- a flat shadow shape on one side (a darker tone or black at 10% opacity),
- at least 2 interior details (planks, rivets, stripes, texture strokes),
- a ground `shadow()` if it stands on the ground.

### Quality bar (every shot must pass all of these)
1. **A real setting:** background (sky, wall or landscape), midground, and foreground. Never a
   character floating on a blank page. Plain cream is allowed only for a big-number or title card,
   and even then add supporting doodles.
2. **Life:** characters have an expression and a pose that act out the line being spoken. Vary
   poses and expressions from shot to shot.
3. **Detail:** at least 6 drawn elements per full shot (for example sky, ground, building, 2 characters,
   a prop and a label). Use period-accurate clothes, buildings and props (`outfit`, `hat`, `prop`).
4. **Composition:** the main subject is big and clear (characters at `s=1.0` to `1.4` when they're
   the focus). Use the rule of thirds. No large empty areas. Nothing important below y=840, where the
   captions go. Labels never overlap figures.
5. **Consistency:** the same character looks the same all video (same skin, hair, outfit and colors).
   Keep a dict of each recurring character's `person()` settings and reuse it.
6. **Variety:** mix wide establishing shots, medium shots and close-ups (a person at `s=2.2`,
   partly off-frame, for reactions). Change location or angle often.

### Shots
Each scene has `"shots"`: exactly 2 pictures. The builder switches pictures on a spoken word,
halfway through the scene's narration. Each shot is one of these:
- `{"svg": full scene}`: a new picture (a new angle, close-up or location).
- `{"add": fragments}`: kit fragments drawn **on top of the previous shot** (a reaction, label, arrow,
  number or character entering). Use `add` for about half of all second shots. The rest should be
  full new pictures.

Make shot 2 match the second half of the narration. Never repeat shot 1 unchanged.
The mascot opens and closes each video.

### Self-review (required)
Render every shot to PNG (cairosvg, 960×540) and tile them into contact sheets of 8. **Look at
every sheet.** Rate each shot 1–5 against the quality bar, then redraw every shot scored under 4:
- broken or overlapping shapes,
- tiny or unclear subjects,
- empty backgrounds,
- mismatched characters,
- text colliding with drawings.

Repeat until all shots score 4 or 5. Mention the average score in your report.

### Thumbnail (`thumbnail_svg`)
Build it with the kit and render it at 1280×720 by changing the root to
`width="1280" height="720" viewBox="0 0 1920 1080"`. It needs:
- a bold amber or high-contrast background,
- 2–5 huge words (`text(..., size=170–230, outline="#fff")`),
- one large character (at `s=1.6` to `2.2`) with a strong emotion, plus the story's key object.

It must be readable at phone size. Check it at 320×180 before you finish.

## 5. Save the episode
Write `scribble-age/episodes/YYYY-MM-DD.json` (today's date, America/Detroit):
```json
{"title": "...", "description": "...", "tags": ["..."], "topic": "...",
 "thumbnail_svg": "<svg ...>", "scenes": [{"narration": "...", "shots": [{"svg": shot1}, {"add": shot2_add}]}]}
```
- Title: under 70 characters, curiosity-driven, true (no clickbait lies).
- Description: 2–3 sentence summary, then 2–4 sources (book or museum names,
  and URLs you are confident exist), then "New story every day. Subscribe!",
  then 3 hashtags.
- Tags: 10–15 relevant ones.
Validate the JSON with `python3 -m json.tool` before building.

## 6. Build and check
```bash
cd /home/user/thallo-site/scribble-age
python3 make_video.py episodes/YYYY-MM-DD.json --out /tmp/sa_build
```
Then check the result: the length should be 4–9 minutes, and the builder's `seconds_per_shot`
should be 6 or less. Pull 4 frames with
ffmpeg (`imageio_ffmpeg.get_ffmpeg_exe()`) and look at them. Fix and rebuild any
scene that is blank, broken or hard to read.

## 7. Upload
```bash
python3 upload.py episodes/YYYY-MM-DD.json --video /tmp/sa_build/video.mp4 --thumbnail /tmp/sa_build/thumbnail.jpg --publish-at 15:00
```
This schedules the video to go public at 3:00 PM Eastern (US research: weekday 2–4 PM is
the best window for long-form, because it gets indexed before the 6–9 PM viewing peak).
If the run finishes after 2:45 PM, it schedules for 3:00 PM the next day, so publish with
`--privacy public` instead to keep the daily streak.
If `publish_at` comes back empty and the privacy is `private`, the
Google API audit is still pending. That's expected, so note it in the report.
If the thumbnail fails, the channel needs phone verification at
youtube.com/verify; note it, but it doesn't block the run.

## 8. Record and report
Append to `history.json` → `episodes`: `{"date", "topic", "title", "video_id", "privacy"}`.
Commit the episode file and history on `claude/eloquent-sagan-8jfd62` and push with
`git push -u origin claude/eloquent-sagan-8jfd62`. If the push is refused, say so in the
report. The upload still counts; the next run will dedupe against the channel's titles.
Finish with a short report: the title, the YouTube URL, the channel_id from upload.py, the privacy status, the
length, and any problems.
