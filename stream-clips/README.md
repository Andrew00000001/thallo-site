# Stream Clips

Free, automated pipeline that turns Kai Cenat's Twitch streams into Shorts for the YouTube fan
channel Kai Cenat Fan Clips (every channel listed in `config.json` → `channels` gets each Short).
A scheduled Claude session follows `AGENT.md` once a day and makes 3 Shorts:

- `find_clips.py`: the streamer's most-viewed Twitch clips (viewers already cut the highlights),
  minus anything already posted
- `make_short.py prep`: download (yt-dlp) and transcribe (faster-whisper) a clip, save preview frames
- `make_short.py render`: 1080x1920 Short with a blurred fill, reframed clip, punch-in zooms on the
  loudest moments, headline, setup and take cards, context pop-ups, word-by-word captions with
  emphasis, a progress bar and loop-friendly audio; stitches 2–3 clips into a story Short with
  chapter labels. No voice-over
- `upload.py`: YouTube Data API upload to every channel; refuses any token that belongs to another channel

Needs `YT_CLIPS_CLIENT_ID`, `YT_CLIPS_CLIENT_SECRET` (an OAuth client in the Scribble Age Uploader
Google Cloud project; falls back to `YT_CLIENT_ID`/`YT_CLIENT_SECRET`) and one refresh token per
channel (`YT_CLIPS_REFRESH_TOKEN` for Kai Cenat Fan Clips), each with the scope
`https://www.googleapis.com/auth/youtube` and authorized on its own channel.
Profile picture: `assets/profile.png`.
Change the streamer in `config.json`. Font: Anton (SIL Open Font License, `assets/OFL.txt`).
