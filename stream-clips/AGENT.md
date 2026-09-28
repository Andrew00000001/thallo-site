# Stream Clips — daily run instructions

You run fan clip Shorts for two YouTube channels (`config.json` → `channels`): **Kai Cenat Fan
Clips** (primary) and **Clip That Moment Now !**. Every run makes **3 Shorts** from Kai Cenat's
most-viewed recent Twitch clips, and each Short is uploaded to both channels. Everything is free:
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

Then run `python3 upload.py --whoami`. It checks every channel's token and prints one line each.
If it exits with an error, the primary channel can't be used: stop and report. If only the second
channel shows `"ok": false`, carry on (uploads skip that channel) and include its error in the report.
Never edit channel IDs in `config.json`; a token for any other channel is refused on purpose.

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
{"url": "...", "slug": "...", "start": 0, "end": 38.5, "crop": "4:3", "focus_x": 0.5, "focus_y": 0.5, "zoom": 1.0,
 "hook_text": "...", "hook_voice": "...", "title": "...", "description": "...", "tags": ["..."]}
```
- `start`/`end`: start on the action (cut any slow lead-in) and end right after the payoff.
  15–45 seconds is ideal; 60 is the most a Twitch clip has.
- `crop`: `vertical` (full-screen 9:16) for one person or IRL footage; `4:3` or `1:1` when there are
  two subjects or a facecam in a corner; `full` for wide gameplay. `focus_x`/`focus_y` move the crop,
  `zoom` (1.0–1.4) tightens it. Crop out the stream's own caption bar, chat box and sub counter
  when you can; our captions replace them.
- `hook_text`: on-screen headline, **6 words or fewer**, true, and about this moment.
- `hook_voice`: **one sentence, 14 words or fewer**, read aloud over the start of the clip. It gives
  the context a new viewer needs ("Kai just asked a tour guide in Iceland to…"). Always include
  it: our commentary is what makes the Short more than a re-upload. Say "Kai", not "Kai Cenat",
  because the voice mispronounces "Cenat".
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
- **Accuracy:** the hook, voice line, title and description may only claim what you can see or
  hear in the clip or its Twitch title. Names, places and numbers must be certain; if not, leave
  them out. No invented drama.

**d. Render and check.**
```bash
python3 make_short.py render /tmp/sc/N/short.json --work /tmp/sc/N --out /tmp/sc/N/short.mp4
```
Pull 3 frames from the result (about 1 s in, the middle, and 2 s before the end) with ffmpeg
(`imageio_ffmpeg.get_ffmpeg_exe()`, `-vf scale=540:-2`) and look at them. Fix and re-render if the
headline is cut off or wraps past 2 lines, the stream's own captions still show next to ours, the
subject is cropped out, or anything is blank or broken.

**e. Upload** each Short as soon as it passes the check (the Nth Short uses the Nth time in
`config.json` → `publish_times`, unless this run's prompt gives other times; the prompt wins):
```bash
python3 upload.py /tmp/sc/N/short.json --video /tmp/sc/N/short.mp4 --publish-at <HH:MM>
```
If that time is already past today, or less than 20 minutes away, use `--privacy public` instead of
`--publish-at` so the Short goes live now rather than piling onto tomorrow's slots.
The command uploads to every channel and prints one JSON line per channel (a video, a `skipped`
note, or an `error`). Then copy `short.json` to `stream-clips/shorts/YYYY-MM-DD-N.json` (today's
date, America/Detroit) and append to `history.json` → `shorts`:
`{"date", "slug", "clip_created", "title", "publish_at", "videos": {"<channel name>": "<video_id>"}}`
(`clip_created` comes from find_clips). If an upload fails with a quota error, stop making
Shorts and report it.

## 4. Record and report
Commit `history.json` and `shorts/` on `claude/youtube-streamer-clips-routine-qwjsb9`
and push with `git push -u origin claude/youtube-streamer-clips-routine-qwjsb9`. If the push is
refused, say so; the uploads still count, and the next run dedupes against the channels themselves.
Don't open pull requests or touch files outside `stream-clips/`.

Finish with a short report: for each Short, the title, both YouTube URLs, the publish time and the
Twitch clip it came from; clips you skipped and why; any problems. Paste every JSON line upload.py printed.
