# Stream Clips — daily run instructions

You run the YouTube fan clip channel **Kai Cenat Fan Clips** (`config.json` → `channels`). Every
run makes and uploads **3 Shorts** from Kai Cenat's most-viewed recent Twitch clips. Everything is free:
Twitch viewers already clipped the best moments, the tools download, caption, reframe and
upload them, and you pick the clips and write the hook, title and description.

## 1. Setup
```bash
cd /home/user/thallo-site 2>/dev/null || git clone https://github.com/Andrew00000001/thallo-site /home/user/thallo-site && cd /home/user/thallo-site
git fetch origin claude/youtube-streamer-clips-routine-qwjsb9 && git checkout claude/youtube-streamer-clips-routine-qwjsb9 && git pull origin claude/youtube-streamer-clips-routine-qwjsb9
cd stream-clips && pip install -q -r requirements.txt
```
If `YT_CLIPS_REFRESH_TOKEN` is missing, or neither `YT_CLIPS_CLIENT_ID` nor `YT_CLIENT_ID` is set,
**stop now** and report that the primary channel's upload token isn't set up. Don't build anything.

Then run `python3 upload.py --whoami`. If it exits with an error, stop and report it. Never edit
channel IDs in `config.json`; a token for any other channel (Scribble Age, Clip That Moment Now !)
is refused on purpose.

## 2. Find clips
```bash
python3 find_clips.py --count 8
```
It lists the most-viewed clips from the last 24 hours (widening to 7 and 30 days if needed),
minus anything already posted and near-duplicates of the same moment. Work down the list.

## 3. Make each Short (repeat until you have 3)
**a. Prep and watch.**
```bash
python3 make_short.py prep "<clip url>" --out /tmp/sc/N
```
Read the transcript and **look at all 4 frames** with the Read tool.

**b. Skip the clip** (go to the next candidate) if any of these is true:
- Someone else's content fills the screen or the audio: a movie, TV show, music video, sports
  broadcast, another creator's video, or a copyrighted song playing clearly. These get Content ID
  claims or copyright strikes, and three strikes deletes the channel.
- A TV network or studio logo is on screen (for example National Geographic). Those streams are
  co-productions, and the network may own the footage.
- Slurs, sexual content, gambling, drugs, graphic violence, or a stunt a kid could copy and get hurt.
- A private person's face, address or other personal details are the focus.
- Nothing happens, or it makes no sense without context you can't give in one sentence.

**c. Write** `/tmp/sc/N/short.json`:
```json
{"url": "...", "slug": "...", "clip_created": 1790431388, "start": 0, "end": 38.5, "crop": "4:3",
 "focus_x": 0.5, "focus_y": 0.5, "zoom": 1.0,
 "hook_text": "...", "title": "...", "description": "...", "tags": ["..."]}
```
- `clip_created`: copy it from find_clips. upload.py saves it as the video's recording date, so
  later runs skip other viewers' clips of the same moment.
- `start`/`end`: start on the action (cut any slow lead-in) and end right after the payoff.
  15–45 seconds is ideal; 60 is the most a Twitch clip has.
- `crop`: `vertical` (full-screen 9:16) for one person or IRL footage; `4:3` or `1:1` when there are
  two subjects or a facecam in a corner; `full` for wide gameplay. `focus_x`/`focus_y` move the crop,
  `zoom` (1.0–1.4) tightens it. The stream's own burned-in captions (bottom) and viewer counter
  (top) are cut off by default (`cut_bottom` 0.12, `cut_top` 0.06 in config.json); raise them in
  short.json only if they still show. Keep the chat box and sub counter out of the crop too.
- `hook_text`: on-screen headline, **6 words or fewer**, true, and about this moment.
- `title`: under 60 characters, includes "Kai Cenat", curiosity-driven but true, at most 1 emoji.
- `description`: one or two sentences of context, then these lines exactly:
  ```
  Clip: <twitch clip url>
  Watch Kai live: https://www.twitch.tv/kaicenat
  Fan channel. Not affiliated with Kai Cenat.
  #kaicenat #shorts #twitch
  ```
  The `Clip:` line is required; it's how later runs know the clip is already posted.
- `tags`: 8–12 relevant tags.
- **Accuracy:** the hook, title and description may only claim what you can see or
  hear in the clip or its Twitch title. Names, places and numbers must be certain; if not, leave
  them out. No invented drama.

**d. Render and check.**
```bash
python3 make_short.py render /tmp/sc/N/short.json --work /tmp/sc/N --out /tmp/sc/N/short.mp4
```
Pull 3 frames from the result (about 1 s in, the middle, and 2 s before the end) with ffmpeg
(`imageio_ffmpeg.get_ffmpeg_exe()`, `-vf scale=540:-2`) and look at them. Fix and re-render if the
headline is cut off or wraps past 2 lines, **the stream's own captions (white words with a purple
highlight) still show anywhere**, the viewer counter or chat shows, the subject is cropped out, or
anything is blank or broken.

**e. Upload** each Short as soon as it passes the check:
```bash
python3 upload.py /tmp/sc/N/short.json --video /tmp/sc/N/short.mp4 --publish-at auto
```
`auto` picks the next time in `config.json` → `publish_times` that is at least 2 hours after the
latest Short already live or scheduled on the channel, so Shorts never pile up, whatever time the
run happens. Don't pass other times or `--privacy public`. If an upload fails with a quota error,
stop making Shorts and report it.

If fewer than 3 clips pass the checks, upload the ones that do and say so. Never lower the bar
to fill the count.

## 4. Report
Don't commit or push: routine sessions can't push to this repo, and nothing depends on it. The
channel is the record: each video's `Clip:` line and recording date tell later runs what's posted.
Don't open pull requests or edit any files in the repo.

Finish with a short report: for each Short, the title, the YouTube URL, the publish time and the
Twitch clip it came from; clips you skipped and why; any problems. Paste every JSON line upload.py printed.
