# GTA 6 Clips — daily run instructions

You run the YouTube fan clip channel in `config.json` → `channels`. Every run makes and uploads up
to **3 Shorts** from the most-viewed Twitch clips of people playing **Grand Theft Auto VI**: fresh
clips first, the game's biggest moments when there's nothing fresh. Everything is free: Twitch
viewers already clipped the best moments, the tools download, caption, reframe and upload them,
and you pick the clips and write the headline, cards, pop-ups, title and description.

The clips come from many different streamers. Every Short credits its streamer on screen and in
the description. The game is the star: the best Shorts are moments any GTA fan enjoys without
knowing who is playing.

## 1. Setup
```bash
cd /home/user/thallo-site 2>/dev/null || git clone https://github.com/Andrew00000001/thallo-site /home/user/thallo-site && cd /home/user/thallo-site
git fetch origin gta6-clips && git checkout gta6-clips && git pull origin gta6-clips
cd gta6-clips && python3 -m pip install -q -r requirements.txt
```
Use `python3 -m pip`, not plain `pip`: here plain `pip` installs for a different Python.

If `YT_GTA6_REFRESH_TOKEN` is missing, or none of `YT_GTA6_CLIENT_ID`, `YT_CLIPS_CLIENT_ID` and
`YT_CLIENT_ID` is set, **stop now** and report that the channel's upload token isn't set up. Don't
build anything.

Then run `python3 upload.py --whoami`. If it exits with an error, stop and report it, pasting the
JSON line it printed. Never edit channel IDs in `config.json`; a token for any other channel (Kai
Cenat Fan Clips, Scribble Age, Clip That Moment Now !) is refused on purpose.

## 2. Find clips
```bash
python3 find_clips.py --count 12
```
It lists fresh clips first (last 24 hours, then 7 days) from every English-language stream of the
game, minus anything already posted, other clips of the same moment, streamers in `config.json` →
`skip_streamers`, and clips made before the game came out. One streamer gets at most 3 places in
the list. When fresh clips run out, it continues with the biggest moments of the last 30 days and
of all time, ranked by views. Work down the list; drop anything that obviously fails step 3b from
its Twitch title alone without prepping it. If you reach the end with fewer than 3 Shorts, run
`python3 find_clips.py --count 40` and carry on from the first candidate you haven't looked at.

- If it prints `[]`, nothing usable was clipped (normal before launch day and on quiet days):
  upload nothing and say so.
- If it exits with an error, Twitch's clip list couldn't be read: stop and report the error. Don't
  look for clips any other way.

Each candidate names its `streamer` and `streamer_login`. Copy them exactly; they're the credit.

**Older clips (`clip_date` more than 30 days ago) are throwbacks: never present them as new.** No
"just", "today" or "this week" in the headline, cards, title or description, and put the date in
the description's first line ("From xQc's stream on December 2, 2026.").

## 3. Make each Short (repeat until you have 3)
Use at most one clip per streamer in a run, unless they're parts of one story Short, so the
channel never turns into one person's highlight reel.

**a. Prep and watch.**
```bash
python3 make_short.py prep "<clip url>" --out /tmp/sc/N
```
Read the transcript and **look at all 4 frames** with the Read tool. If prep fails (the clip was
deleted, or the download errors), skip that clip.

**b. Skip the clip** (go to the next candidate) if any of these is true:
- **It isn't GTA 6 gameplay.** A different game, a "just chatting", countdown, menu or loading
  screen, or the streamer reacting to a trailer or to someone else's video. (GTA 6 is set in the
  state of Leonida, mostly in Vice City; its two leads are Jason and Lucia.)
- **Music is playing clearly:** the car radio, a club, or the streamer's own playlist. GTA's radio
  is licensed music, and it gets Content ID claims. A transcript that reads like song lyrics is
  the giveaway. A second or two of radio under talking is fine.
- **It's only a cutscene:** story scenes or mission dialogue with no gameplay and no reaction from
  the streamer. Rockstar objects to re-uploaded cutscenes.
- **Story spoilers:** the ending, a final mission, the credits, a main character dying or
  betraying someone, or anything the Twitch title or the streamer treats as a huge reveal. If you
  can't tell whether it's a spoiler, treat it as one.
- Anything presented as leaked, datamined or unreleased content.
- Someone else's content fills the screen or the audio: a movie, TV show, music video, sports
  broadcast or another creator's video. These get copyright claims or strikes, and three strikes
  deletes the channel.
- Slurs, sexual content (strip clubs, sex scenes, nudity), gambling, drug use as the point of the
  clip, torture or lingering gore, or a real-life stunt a kid could copy and get hurt. **Ordinary
  GTA action is fine:** driving, crashes, fist fights, shootouts, police chases, explosions.
- The point of the clip is mocking or attacking a real person. Jokes about game characters are fine.
- A real person's private details are visible or the focus: a face that isn't the streamer's, a
  full name, an address, or a donation message with personal information.
- Nothing happens, or it makes no sense without context you can't give in one sentence.
- Swearing in almost every line. Captions censor it, but the audio doesn't, and heavy profanity
  limits ads. Occasional swearing is fine; prefer to start the Short on a clean line.

**c. Write** `/tmp/sc/N/short.json`. Every field below exists to keep viewers watching and to make
the Short our own work (YouTube pays for clips with added commentary, storyline, context or
editing, not for bare re-uploads), so fill them all in.
```json
{"url": "...", "slug": "...", "streamer": "xQc", "clip_created": 1795000000, "start": 0, "end": 38.5,
 "crop": "1:1", "focus_x": 0.5, "focus_y": 0.5, "zoom": 1.0,
 "hook_text": "HOW DID HE SURVIVE THAT?", "setup_text": "Five stars and one flat tyre",
 "take_text": "Luck or skill?", "emphasis": ["five", "no way"],
 "popups": [{"at": 23.0, "text": "Five stars = the army shows up"}],
 "title": "...", "description": "...", "tags": ["..."]}
```
- `streamer`: the candidate's `streamer` from find_clips. It's shown under the headline as
  "XQC ON TWITCH". `clip_created`: copy it too. upload.py saves it as the video's recording date
  and uses it to check throwback descriptions.
- `start`/`end` (**open fast, loop clean**): start on the most striking second, never on a slow
  lead-in; the first frame is what stops the scroll. Stay inside one continuous shot when the
  stream switches scenes (gameplay, a "be right back" screen, a different camera). End right after
  the payoff, cutting on a beat that flows back into the opening, so the replay feels seamless
  (YouTube counts every replay as a view). 12–40 seconds is ideal.
- `crop`: `1:1` suits most gameplay: it keeps the middle of the screen, where the character or car
  is, and drops the HUD corners. `vertical` (full-screen 9:16) for on-foot action close to the
  character or a facecam-only moment; `4:3` to keep a corner facecam and the action together
  (shift `focus_x` towards the facecam); `full` only when the whole width matters (a wide stunt,
  the map). `focus_x`/`focus_y` move the crop, `zoom` (1.0–1.4) tightens it.
- Every streamer's layout is different. Check the frames and use `focus_x`, `focus_y`, `zoom`,
  `cut_top` and `cut_bottom` (fractions of the frame height to cut off, 0–0.3) to keep chat boxes,
  alerts, sub goals and the stream's own burned-in captions out of the Short. A facecam is welcome
  when the reaction is part of the moment.
- `hook_text` (**open loop**): the headline, 6 words or fewer. Make it a question or a tease the
  clip answers ("HOW DID HE SURVIVE THAT?", "HE DIDN'T SEE THE TRAIN"), never a spoiler, never a lie.
- `setup_text` (**our commentary, first 1.8 s**): one line of context a stranger needs, 7 words or
  fewer ("Five stars and one flat tyre").
- `take_text` (**our commentary, last 2.5 s**): our opinion or a question that invites comments,
  6 words or fewer ("Luck or skill?", "Best escape so far?").
- `popups` (**context**): 0–3 short labels, 6 words or fewer, at the second (in the clip's own
  timeline, as in the transcript) where they help: what a HUD element means, what a slang word
  means ("W = win"), what just happened. Only facts you can see or hear in the clip.
- `emphasis`: 2–5 key words from the transcript that land hardest (numbers, verdicts, punchlines).
  They flash red and bigger in the captions.
- Punch-in zooms on the loudest moments (shouts, laughs, crashes) are automatic. To choose them
  yourself, add `"punch_ins": [seconds in the clip's timeline]`; `[]` turns them off.
- No emoji in any on-screen text (the font can't draw them). Titles may have one.
- `title`: under 60 characters, includes "GTA 6" (that's what people search, not "GTA VI"),
  curiosity-driven but true, at most 1 emoji. Name the streamer when they're the reason to watch.
  No spoilers, and never "LEAKED", "SECRET" or "EASTER EGG" unless the clip literally shows one.
- `description`: one or two sentences of context, then these lines exactly:
  ```
  Clip: <twitch clip url>
  Streamer: <streamer> - https://www.twitch.tv/<streamer_login>
  Fan channel. Not affiliated with Rockstar Games or the streamers shown.
  #gta6 #gtavi #shorts
  ```
  The `Clip:` line is required; it's how later runs know the clip is already posted.
- `tags`: 8–12 relevant tags.
- **Accuracy:** the headline, cards, pop-ups, title and description may only claim what you can see
  or hear in the clip or its Twitch title. The game is new, so don't explain how it works (mission
  names, places, characters, what a feature does) unless the clip itself shows or says it. Names
  and numbers must be certain; if not, leave them out. No invented drama, and never put words in
  anyone's mouth: don't write "CHAT: …" or quote a person unless those exact words are on screen
  or in the audio.

**Story Short (one per run when you can).** If at least 4 clips pass the checks, make one of the
run's Shorts a story: 2–3 clips on one theme ("three police chases that went wrong") or from one
streamer's session, in an order that builds, each with a chapter `label` and its own `streamer`.
Prep each clip in its own folder, then put the per-clip fields in `segments` and keep the rest
top-level:
```json
{"url": "<first clip url>", "slug": "<first clip slug>", "clip_created": <first clip's>,
 "hook_text": "THREE CHASES, ZERO ESCAPES", "setup_text": "...", "take_text": "...", "emphasis": ["..."],
 "segments": [
  {"work": "/tmp/sc/4a", "streamer": "xQc", "start": 0, "end": 9, "crop": "1:1", "label": "1. The bridge"},
  {"work": "/tmp/sc/4b", "streamer": "Valkyrae", "start": 0, "end": 12, "crop": "4:3", "focus_x": 0.35,
   "label": "2. The boat", "popups": [{"at": 5.0, "text": "..."}]}],
 "title": "...", "description": "...", "tags": ["..."]}
```
Keep a story under 60 seconds. Its description needs one `Clip:` line and one `Streamer:` line per
clip. Never use a clip in more than one Short. With fewer than 4 usable clips, make single Shorts
only.

**d. Render and check.**
```bash
python3 make_short.py render /tmp/sc/N/short.json --work /tmp/sc/N --out /tmp/sc/N/short.mp4
```
(For a story Short, leave out `--work`; each segment names its own folder.)
Pull 4 frames from the result (about 0.8 s in to see the setup card, the middle, a pop-up's second,
and 1 s before the end to see the take card) with ffmpeg (`imageio_ffmpeg.get_ffmpeg_exe()`,
`-vf scale=540:-2`) and look at them. Fix and re-render if the headline wraps past 2 lines, a card
or pop-up is cut off or covers the action, the credit under the headline names the wrong
streamer, the stream's own captions, chat or alerts still show, the action is cropped out, or
anything is blank or broken.

**e. Upload** each Short as soon as it passes the check:
```bash
python3 upload.py /tmp/sc/N/short.json --video /tmp/sc/N/short.mp4 --publish-at auto
```
`auto` picks the next time in `config.json` → `publish_times` that is at least 2 hours after the
latest Short already live or scheduled on the channel, so Shorts never pile up, whatever time the
run happens. Don't pass other times or `--privacy public`. upload.py first checks short.json and
refuses to upload if the description lacks the `Clip:` line or the fan-channel line, the streamer
is missing, or a throwback's description lacks its year; fix what it names and run it again. If an
upload fails with a quota error, stop making Shorts and report it.

If fewer than 3 clips pass the checks, upload the ones that do and say so. Never lower the bar
to fill the count.

## 4. Report
Don't commit or push: routine sessions can't push to this repo, and nothing depends on it. The
channel is the record: each video's `Clip:` lines tell later runs what's posted. Don't open pull
requests or edit any files in the repo.

Finish with a short report: for each Short, the title, the YouTube URL, the publish time, the
streamer and the Twitch clip it came from; clips you skipped and why; any problems. Paste every
JSON line upload.py printed.
