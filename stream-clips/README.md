# Stream Clips

Free, automated pipeline that turns Kai Cenat's Twitch streams into Shorts and posts each one to
two YouTube channels (Kai Cenat Fan Clips and Clip That Moment Now !, listed in `config.json`).
A scheduled Claude session follows `AGENT.md` once a day and makes 3 Shorts:

- `find_clips.py`: the streamer's most-viewed Twitch clips (viewers already cut the highlights),
  minus anything already posted
- `make_short.py prep`: download (yt-dlp) and transcribe (faster-whisper) a clip, save preview frames
- `make_short.py render`: 1080x1920 Short with a blurred fill, reframed clip, headline,
  word-by-word captions and a spoken hook (free Edge TTS)
- `upload.py`: YouTube Data API upload to every channel; refuses any token that belongs to another channel

Needs `YT_CLIPS_CLIENT_ID`, `YT_CLIPS_CLIENT_SECRET` (an OAuth client in the Scribble Age Uploader
Google Cloud project; falls back to `YT_CLIENT_ID`/`YT_CLIENT_SECRET`) and one refresh token per
channel (`YT_CLIPS_REFRESH_TOKEN`, `YT_CLIPS2_REFRESH_TOKEN`), each with the scope
`https://www.googleapis.com/auth/youtube` and authorized on its own channel.
Profile picture: `assets/profile.png`.
Change the streamer in `config.json`. Font: Anton (SIL Open Font License, `assets/OFL.txt`).
