# Stream Clips

Free, automated pipeline for a YouTube fan channel that turns Kai Cenat's Twitch streams into
Shorts. A scheduled Claude session follows `AGENT.md` once a day and makes 3 Shorts:

- `find_clips.py`: the streamer's most-viewed Twitch clips (viewers already cut the highlights),
  minus anything already posted
- `make_short.py prep`: download (yt-dlp) and transcribe (faster-whisper) a clip, save preview frames
- `make_short.py render`: 1080x1920 Short with a blurred fill, reframed clip, headline,
  word-by-word captions and a spoken hook (free Edge TTS)
- `upload.py`: YouTube Data API upload; refuses any token that isn't the clips channel's

Needs `YT_CLIENT_ID`, `YT_CLIENT_SECRET` (same Google Cloud project as Scribble Age) and
`YT_CLIPS_REFRESH_TOKEN` (scopes `youtube.upload` and `youtube.readonly`, authorized on the clips channel).
Change the streamer in `config.json`. Font: Anton (SIL Open Font License, `assets/OFL.txt`).
