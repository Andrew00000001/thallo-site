# Scribble Age

Free, automated pipeline for the YouTube channel Scribble Age (@ScribbleAge).
A scheduled Claude session follows `AGENT.md` once a day: it writes an original
history script, draws the doodle scenes as SVG, and runs:

- `make_video.py`: free Edge TTS voiceover, cairosvg rendering, ffmpeg zoom and burned-in captions → 1080p MP4 plus thumbnail
- `upload.py`: YouTube Data API upload (needs `YT_CLIENT_ID`, `YT_CLIENT_SECRET`, `YT_REFRESH_TOKEN`)

`history.json` tracks posted topics so the channel never repeats one.
Font: Patrick Hand (SIL Open Font License, `assets/OFL.txt`).
