# GTA 6 Clips — daily run instructions

You run the YouTube fan clip channel in `config.json` → `channels`. Every run makes and uploads up
to **3 Shorts** from the most-viewed Twitch clips of people playing **Grand Theft Auto VI**: fresh
clips first, the game's biggest moments when there's nothing fresh. Everything is free: Twitch
viewers already clipped the best moments, the tools download, caption, reframe and upload them,
and you pick the clips and write the headline, cards, pop-ups, spoken commentary, title and
description.

**Every Short carries our own spoken commentary.** A synthetic host voice talks over a teaser at
the start, over a title card between clips, and over a slow-motion replay at the end. It never
talks over the original clip: the streamer's own audio plays alone, at full level. The commentary
is what makes each Short our work (YouTube only pays for reused footage with added commentary), so
`make_short.py` won't render without it and `upload.py` won't upload a Short that lacks it.

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

The first render of the day downloads the narration voice (about 90 MB, from Hugging Face, no
login needed); that is why it takes a minute longer.

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
Use at most one clip per streamer in a run, unless they're parts of one story or ranked Short, so
the channel never turns into one person's highlight reel.

**Pick the format of each Short.** Steps a and b apply to every clip, so prep and check candidates
first (several, since a Short can use up to 3 clips), then plan the run from the clips that passed:
- `story`: 2–3 clips in an order that builds, on one theme or from one streamer's session.
- `ranked`: 2–3 clips counted down to number 1 ("three escapes, ranked").
- `breakdown`: one clip, taken apart: the setup, the moment, a verdict.

Prefer `story` or `ranked` whenever enough clips pass, and vary the formats within a run (not two
`ranked` Shorts). Make **at most one `breakdown` per run**. Roughly: 5 or more passing clips → a
story, a ranked and one breakdown; 4 clips → a story and a ranked of 2 clips each (or one 3-clip
Short and a breakdown); 3 clips → a 2-clip story or ranked and a breakdown; 2 clips → a story;
1 clip → a breakdown. A clip is used in one Short only. Never put a weak clip into a multi-clip
Short just to fill it.

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
{"format": "breakdown", "url": "...", "slug": "...", "streamer": "xQc", "clip_created": 1795000000,
 "start": 0, "end": 38.5, "crop": "1:1", "focus_x": 0.5, "focus_y": 0.5, "zoom": 1.0,
 "hook_text": "HOW DID HE SURVIVE THAT?", "setup_text": "Five stars and one flat tyre",
 "take_text": "Luck or skill?", "emphasis": ["five", "no way"],
 "popups": [{"at": 23.0, "text": "Five stars = the army shows up"}],
 "narration": {"hook": "Five stars, a flat tyre, and a police roadblock dead ahead. Watch his left hand.",
               "bridges": [],
               "take": "He steers around the spike strip with the rim sparking. That is a better escape than most missions give you."},
 "teaser": {"segment": 0, "from": 23.1, "to": 25.2},
 "replay": {"segment": 0, "from": 23.0, "to": 26.0, "speed": 0.5, "zoom": 1.25, "focus_x": 0.5, "focus_y": 0.5},
 "rating": "9/10 ESCAPE",
 "title": "...", "description": "...", "tags": ["..."]}
```
- `format`: `breakdown` for one clip, `story` or `ranked` for 2–3 (see "Story and ranked Shorts"
  below). The timeline of every Short is: teaser (hook voice) → clip (its own audio) → [bridge card
  (bridge voice) → clip]… → replay (take voice).
- `streamer`: the candidate's `streamer` from find_clips. It's shown under the headline as
  "XQC ON TWITCH". `clip_created`: copy it too. upload.py saves it as the video's recording date
  and uses it to check throwback descriptions.
- `start`/`end` (**open fast**): start on the most striking second, never on a slow lead-in. Stay
  inside one continuous shot when the stream switches scenes (gameplay, a "be right back" screen,
  a different camera). End right after the payoff; the replay follows it. A breakdown clip of
  12–40 seconds is ideal; in a story or ranked Short keep each clip to 6–15 seconds.
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
- `setup_text` (**our commentary, first 1.8 s of the first clip**): one line of context a stranger
  needs, 7 words or fewer ("Five stars and one flat tyre").
- `take_text` (**our commentary, last 2.5 s, over the replay**): our opinion or a question that
  invites comments, 6 words or fewer ("Luck or skill?", "Best escape so far?").
- `narration` (**our spoken commentary, the most important field**): `hook` is spoken over the
  teaser, `bridges[i]` over the card that introduces clip i+2 (exactly one fewer line than clips:
  `[]` for a breakdown), and `take` over the replay. It is read aloud by a synthetic voice, and
  **it never plays over the original clip**; the voice only talks over the added teaser, cards and
  replay, so write for the ear: short sentences, plain words, no emoji, no hashtags, no
  abbreviations. Say "GTA 6".
  - Each line needs **a specific observation about this clip plus an opinion or a verdict**, and
    should tell the viewer what to watch for. Word limits: `hook` 6–14 words, each bridge 4–12,
    `take` 12–26 (about 3 words a second).
  - No generic hype lines. "Check this out", "you won't believe this", "this is insane" and
    "wait for it" say nothing about the clip. Name what actually happens ("the car clips the
    barrier and the whole chase falls apart") and what you think of it ("that is the worst
    parking job in the game").
  - The accuracy rules below apply to narration too: only what you can see or hear in the clip or
    its Twitch title, names and numbers only when certain, no quoting anyone unless the exact words
    are in the audio, no explaining how the game works. No swearing, no attacks on a real person.
  - `hook` opens the loop the clip closes and does not give away the payoff; bridges connect the
    clips (what changes, what gets worse or better); `take` is the verdict and invites an answer.
  - Narration is 15–50% of the finished Short, and upload.py refuses anything outside that, so
    don't write a paragraph for a 10-second clip.
- `teaser` (**1–3 s, hook voice**): `{"segment": 0, "from": s, "to": s}`, the single most striking
  moment (the crash, the explosion, the reaction) in that clip's own seconds, as in the
  transcript. It plays slowed to fit the hook voice, so a 1.5–2 s range is plenty. It is a tease,
  not the whole payoff: pick the first half of the big moment (the launch, the swerve) and leave
  the landing for the replay. In a ranked Short take it from the number 1 clip.
- `replay` (**1.5–4 s, take voice**): `{"segment": 0, "from": s, "to": s, "speed": 0.5, "zoom": 1.25,
  "focus_x": 0.5, "focus_y": 0.5}`, the key moment of the Short, which `take` talks about. Start
  half a second before the action. At speed 0.5 the replay lasts twice its range and the take voice
  needs about as long, so cover roughly take words ÷ 6 seconds (an 18-word take → 3 s). A replay
  longer than the voice is cut off (render warns). `zoom` pushes in on the detail and `focus_x`/
  `focus_y` move the crop towards it (they default to the clip's own); skip the zoom
  (`"zoom": 1.0`) when the whole frame is the moment.
- `rating` (optional): a short verdict stamp shown during the replay, 16 characters or fewer
  ("9/10 ESCAPE", "WORST PARK EVER"). Only an opinion about the play, never a fact.
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

**Story and ranked Shorts (2–3 clips; prefer these whenever enough clips pass).** A `story` has
2–3 clips on one theme ("three police chases that went wrong") or from one streamer's session, in an
order that builds. A `ranked` has 2–3 clips counted down to number 1: label them `#3 ...`, `#2 ...`,
`#1 ...`, put the best clip last, take the `teaser` and the `replay` from it, and let each bridge
announce the next rank ("Number two, and it is closer than you think."). Every clip has its own
`streamer` and a chapter `label` (6 words or fewer): the label is shown large on the card before the
clip, and a story or ranked Short won't render without it. Prep each clip in its own folder, then
put the per-clip fields in `segments` and keep the rest top-level. `narration.bridges` needs one
line fewer than there are clips, and `teaser.segment` and `replay.segment` count the clips from 0:
```json
{"format": "story", "url": "<first clip url>", "slug": "<first clip slug>", "clip_created": <first clip's>,
 "hook_text": "THREE CHASES, ZERO ESCAPES", "setup_text": "...", "take_text": "...", "emphasis": ["..."],
 "narration": {"hook": "...", "bridges": ["...", "..."], "take": "..."},
 "teaser": {"segment": 2, "from": 4.0, "to": 6.0},
 "replay": {"segment": 2, "from": 3.5, "to": 6.5, "speed": 0.5, "zoom": 1.25},
 "rating": "3 CHASES, 0 WINS",
 "segments": [
  {"work": "/tmp/sc/4a", "streamer": "xQc", "start": 0, "end": 9, "crop": "1:1", "label": "1. The bridge"},
  {"work": "/tmp/sc/4b", "streamer": "Valkyrae", "start": 0, "end": 12, "crop": "4:3", "focus_x": 0.35,
   "label": "2. The boat", "popups": [{"at": 5.0, "text": "..."}]},
  {"work": "/tmp/sc/4c", "streamer": "Sykkuno", "start": 2, "end": 11, "crop": "1:1", "label": "3. The train"}],
 "title": "...", "description": "...", "tags": ["..."]}
```
Keep a story or ranked Short under 75 seconds in total. Its description needs one `Clip:` line and
one `Streamer:` line per clip. Never use a clip in more than one Short.

**d. Render and check.**
```bash
python3 make_short.py render /tmp/sc/N/short.json --work /tmp/sc/N --out /tmp/sc/N/short.mp4
python3 make_short.py frames /tmp/sc/N/short.mp4
```
(For a story or ranked Short, leave out `--work`; each segment names its own folder.)
Render speaks the narration first, then builds the Short: teaser and hook voice, the clip with its
own audio, a card and bridge voice before each further clip, then the replay and take voice. It
prints a JSON line and writes `short.mp4.json` next to the video (total and narration seconds,
narration share, and a timeline of what plays when). If it says it cannot make the narration voice,
run it once more; if that fails too, stop and report the error. Never upload a Short without its
narration, and never add voice any other way.

`frames` saves check frames (`-vf scale=540:-2`) into `short.mp4.frames/` and lists them: the
middle of the teaser, of every clip, of every bridge card and of the replay, 0.8 s into the first
clip (the setup card) and 1 s before the end (the take card). **Look at all of them** with the
Read tool, and check the numbers:
- `narration_share` in the sidecar is between 0.15 and 0.50 (aim for 0.2–0.4), and render printed
  no warning, such as a replay longer than its voice, which gets cut off.
- Teaser frame: the moment is striking and matches the hook; the headline, the credit and the boxed
  COMMENTARY caption are all readable and don't overlap. It is the right streamer's credit.
- Bridge frame: the next clip's first frame, darkened, with its label large and readable.
- Replay frame: zoomed on the moment the take talks about (not on empty road), with the REPLAY tag,
  the rating stamp if you gave one, the take card and the caption not covering each other.
- Fix and re-render if any of that is off, or if the headline wraps past 2 lines, a card or pop-up
  is cut off or covers the action, a credit names the wrong streamer, the stream's own captions,
  chat or alerts still show, the action is cropped out, narration says something the frames don't
  show, or anything is blank or broken. The voice never overlaps the original clip: the timeline
  marks only the teaser, bridges and replay as narrated.

**e. Upload** each Short as soon as it passes the check:
```bash
python3 upload.py /tmp/sc/N/short.json --video /tmp/sc/N/short.mp4 --publish-at auto
```
`auto` picks the next time in `config.json` → `publish_times` that is at least 2 hours after the
latest Short already live or scheduled on the channel, so Shorts never pile up, whatever time the
run happens. Don't pass other times or `--privacy public`. upload.py first checks short.json and
refuses to upload if the description lacks the `Clip:` line or the fan-channel line, the streamer
is missing, or a throwback's description lacks its year. It also refuses a Short without
commentary: `format` not `breakdown`, `story` or `ranked`, `narration.hook` or `narration.take`
missing, the wrong number of bridges, `short.mp4.json` missing next to the video (or from a
different render), or a narration share outside `config.json` → `min_narration_share` /
`max_narration_share`. Fix what it names (re-render after changing any narration) and run it again.
If an upload fails with a quota error, stop making Shorts and report it.

If fewer than 3 clips pass the checks, upload the ones that do and say so. Never lower the bar
to fill the count.

## 4. Report
Don't commit or push: routine sessions can't push to this repo, and nothing depends on it. The
channel is the record: each video's `Clip:` lines tell later runs what's posted. Don't open pull
requests or edit any files in the repo.

Finish with a short report: for each Short, the title, the YouTube URL, the publish time, the
streamer and the Twitch clip it came from; clips you skipped and why; any problems. Paste every
JSON line upload.py printed.
