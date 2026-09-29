# Stream Clips

Free, automated pipeline that turns Kai Cenat's Twitch streams into Shorts for the YouTube fan
channel **Kai Cenat Fan Clips** (@KaiCenatFanClipsHQ, owned by ojj9582@gmail.com). A Claude
Routine, "Stream Clips daily Shorts (Kai Cenat)", runs every day at 10:47 AM ET, follows
`AGENT.md`, and uploads up to 3 Shorts that go live at 12, 4 and 8 PM ET.

- `find_clips.py`: the streamer's most-viewed Twitch clips (viewers already cut the highlights):
  fresh ones first, then the 30-day and all-time lists when nothing fresh is left. Skips clips
  already on the channel, other clips of the same moment, and streams in `skip_windows`
- `make_short.py prep`: download (yt-dlp) and transcribe (faster-whisper) a clip, save preview frames
- `make_short.py render`: 1080x1920 Short with a blurred fill, reframed clip, punch-in zooms on the
  loudest moments, headline, setup and take cards, context pop-ups, word-by-word captions with
  emphasis, a progress bar and loop-friendly audio; stitches 2–3 clips into a story Short with
  chapter labels. No voice-over
- `upload.py`: checks short.json, confirms the token belongs to the right channel (it refuses
  Scribble Age and Clip That Moment Now !), picks the next free publish slot and uploads.
  `--whoami` checks the token, `--dry-run` does everything but the upload

## Credentials
Environment "Default" (claude.ai/code): `YT_CLIPS_CLIENT_ID`, `YT_CLIPS_CLIENT_SECRET` (the "Kai
Cenat Fan Clips" OAuth client in the Scribble Age Uploader Google Cloud project, ojj9582) and
`YT_CLIPS_REFRESH_TOKEN` (scope `https://www.googleapis.com/auth/youtube`, authorized on the channel).

## Runbook
- **Where the record lives:** on the channel. Each video's description has a `Clip:` line per
  Twitch clip; that's how runs avoid repeats. Routine sessions can't push to this repo, so
  nothing is written back here.
- **Pause or resume:** turn the Routine off or on in claude.ai (Routines), or ask Claude to.
- **Change the streamer:** edit `config.json` → `streamer` (and the channel description), plus
  the names in `AGENT.md`. Kick and YouTube-only streamers won't work from the cloud: YouTube
  blocks downloads there.
- **Skip a whole stream** (for example a TV co-production): add its UTC time range to
  `skip_windows`.
- **Add a second channel:** add it to `channels` with its own `token_env`; every Short then goes
  to both. Posting identical Shorts to two channels risks YouTube's spam policy, so prefer a
  different streamer per channel.
- **Known limits:** Kai's streams carry third-party content (movies, music, TV partners), so many
  clips are rejected; the all-time list keeps the channel supplied. Clips are used without Kai's
  permission, so a copyright claim or strike is possible.

Font: Anton (SIL Open Font License, `assets/OFL.txt`). Profile picture: `assets/profile.png`.
