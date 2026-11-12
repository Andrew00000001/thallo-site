# GTA 6 Clips

Free, automated pipeline that turns the most-viewed Twitch clips of **Grand Theft Auto VI** into
Shorts for the YouTube fan clip channel **GTA 6 Clips Daily** (@GTA6ClipsDailyTV). A Claude
Routine, "GTA 6 Clips daily Shorts", runs once a day, follows `AGENT.md`, and uploads up to 3
Shorts that go live at 12, 4 and 8 PM ET.

It is the sibling of `stream-clips/` (Kai Cenat Fan Clips, on the branch
`claude/youtube-streamer-clips-routine-qwjsb9`). The difference is the source: instead of one
streamer's clips, it reads the game's whole Twitch category, so the clips come from many streamers
and every Short credits its streamer on screen and in the description.

- `find_clips.py`: the top clips of the Twitch category "Grand Theft Auto VI" (viewers already cut
  the highlights): the last 24 hours and 7 days first, then the 30-day and all-time lists.
  English-language streams only. Skips clips already on the channel, other clips of the same
  moment, streamers in `skip_streamers`, and clips made before the game came out (`clips_from`)
- `make_short.py prep`: download (yt-dlp) and transcribe (faster-whisper) a clip, save preview frames
- `make_short.py render`: 1080x1920 Short with a blurred fill, reframed clip, punch-in zooms on the
  loudest moments, headline, streamer credit, setup and take cards, context pop-ups, word-by-word
  captions with emphasis, a progress bar and loop-friendly audio; stitches 2–3 clips into a story
  or ranked Short with chapter labels; adds the spoken commentary (see "Spoken commentary" below)
  and writes `<video>.json` with the narration numbers. `make_short.py frames` saves check frames
- `tts.py`: the offline narration voice (`speak(text, out_wav)`), Kokoro-82M on CPU
- `upload.py`: checks short.json (including the narration, see below), confirms the token belongs
  to the right channel (it refuses Kai Cenat Fan Clips, Scribble Age and Clip That Moment Now !),
  picks the next free publish slot and uploads. `--whoami` checks the token, `--dry-run` does everything but the upload,
  `--setup-channel` writes the channel description and keywords from `config.json`

## Spoken commentary
YouTube's reused-content policy only lets a channel use other creators' footage when it adds real
commentary, and it excludes content "without added voice commentary". So every Short carries
spoken commentary written by the daily agent (`narration` in short.json, see `AGENT.md`):

    [teaser + hook voice] [clip, own audio] ([bridge card + bridge voice] [clip, own audio])... [replay + take voice]

- **The voice never plays over the original clip.** The narration only lives in host pieces added
  around it: a 1–3 s teaser of the best moment (slowed to the length of the hook line), a darkened
  freeze-frame card with the next clip's label between clips (story and ranked Shorts), and a
  slow-motion, zoomed replay with a REPLAY tag and an optional verdict stamp, which the take line
  talks over. The clips keep their own audio at full level. Under the host voice the original
  audio is muted (not ducked): slowed-down clip audio sounds bad and the commentary stays clear.
- The narration is captioned in its own style (dark box, white text, amber current word, a
  COMMENTARY tag), nothing like the clip's own captions, so sound-off viewers and reviewers can
  see which words are ours. Word timings are spread over the length of each spoken line.
- **Formats** (`format` in short.json): `breakdown` (one clip), `story` (2–3 clips in order),
  `ranked` (2–3 clips counted down to number 1). `narration` is `{"hook", "bridges", "take"}`;
  `bridges` has one line fewer than there are clips.
- **No narration, no Short.** `make_short.py render` refuses to run without a complete plan, and
  exits non-zero with a message if speech can't be made (never a silent render). It also writes
  `<video>.json` (`total_seconds`, `narration_seconds`, `narration_share`, `format`, `clips`, a
  timeline and a hash of the narration text). `upload.py` refuses a Short with no hook or take line,
  the wrong number of bridges, a missing or stale sidecar, or a narration share outside
  `min_narration_share`..`max_narration_share`.

### The voice
- Engine: **Kokoro-82M** v1.0 (Apache-2.0 weights by hexgrad) run by the `kokoro-onnx` package
  (MIT) on onnxruntime, CPU only. Phonemes come from espeak-ng (GPL-3.0), which `kokoro-onnx`
  installs as the pip package `espeakng-loader`; it is used as a library and is not part of this
  repo. Everything installs with pip, nothing needs apt.
- Model files, from the Hugging Face repo `onnx-community/Kokoro-82M-v1.0-ONNX` (Apache-2.0):
  `onnx/model_quantized.onnx` (int8, about 92 MB) and the voice's style file `voices/<voice>.bin`
  (0.5 MB). Voice: `af_heart` (US English, female; the best-rated Kokoro voice).
- Cache: the Hugging Face cache, `$HF_HOME/hub` (default `~/.cache/huggingface/hub`), plus one small
  `$HF_HOME/gta6-kokoro/*.npz` made from the voice file. The first render in a fresh sandbox
  downloads about 93 MB; later calls reuse the cache. No login or token is needed.
- Loudness: each line is loudness-normalised to the same target as the clips (-14 LUFS, true peak
  -1.5 dB), 48 kHz mono, with 0.1 s of lead-in silence.
- `config.json` -> `narrator`: `engine` (`kokoro`), `voice` (any Kokoro voice name, for example
  `am_michael`, `af_bella`), `speed` (0.5–2.0, default 1.0), `repo` and `model_file` (another
  precision from the same repo, e.g. `onnx/model.onnx` for full precision, about 325 MB).
  `min_narration_share` (0.15) and `max_narration_share` (0.5) are the limits `upload.py` enforces
  on narration seconds divided by total seconds.
- Try it: `python3 tts.py "Some words to say." out.wav`.

## One-time setup
1. **Create the channel.** Done on 2026-11-11: GTA 6 Clips Daily (@GTA6ClipsDailyTV), a brand
   account under the owner's main Google account. That is a different Google account from the
   one that owns Kai Cenat Fan Clips.
2. **Make its upload token.** Open https://developers.google.com/oauthplayground, click the gear,
   tick "Use your own OAuth credentials", and enter the same client ID and secret the Kai Cenat
   pipeline uses (`YT_CLIPS_CLIENT_ID` and `YT_CLIPS_CLIENT_SECRET` in the Claude cloud
   environment "Default"). In step 1 type the scope `https://www.googleapis.com/auth/youtube`,
   click "Authorize APIs", and when Google asks which account to use, pick the owner's main
   account and then **GTA 6 Clips Daily**. In step 2 click "Exchange authorization code for
   tokens" and copy the refresh token.
   (If Google says `redirect_uri_mismatch`, add `https://developers.google.com/oauthplayground`
   to that OAuth client's authorized redirect URIs in the Google Cloud console and try again.)
3. **Store it.** In claude.ai/code, open the cloud environment "Default" and add the variable
   `YT_GTA6_REFRESH_TOKEN` with that token. Never put it in this repo.
4. **Tell the pipeline which channel it is.** Done: the channel's ID, name and handle are in
   `config.json` → `channels`. `upload.py --whoami` refuses any token that belongs to a
   different channel and names the channel it does belong to.
5. **Test, then switch on.** Done on 2026-11-11: a rehearsal run in the cloud passed (token and
   channel check, clip listing, a stand-in render and a dry-run upload), and the routine is on.
   The first real upload happens once the game is out and has clips.

## Credentials
Environment "Default" (claude.ai/code): the OAuth client `YT_CLIPS_CLIENT_ID` and
`YT_CLIPS_CLIENT_SECRET` (shared with the Kai Cenat pipeline; set `YT_GTA6_CLIENT_ID` and
`YT_GTA6_CLIENT_SECRET` only if this channel ever gets its own client) and `YT_GTA6_REFRESH_TOKEN`
(scope `https://www.googleapis.com/auth/youtube`, authorized on the GTA 6 channel with that same
client). YouTube allows 100 API uploads a day per Google Cloud project, far more than all the
channels on this project use.

## Runbook
- **Where the record lives:** on the channel. Each video's description has a `Clip:` line per
  Twitch clip; that's how runs avoid repeats. Routine sessions can't push to this repo, so
  nothing is written back here.
- **Pause or resume:** turn the Routine off or on in claude.ai (Routines), or ask Claude to.
- **Keep this repo attached to the Routine as its repository.** A session that only clones the
  repo itself treats these scripts as outside code, and its permission check sometimes refuses
  to run them ("Code from External"); two rehearsals stopped that way. With the repo attached,
  the session starts inside the checkout and the scripts run normally.
- **Post more often:** add times to `publish_times` and a second daily schedule to the Routine.
  Every run draws on the Claude plan's usage.
- **A streamer asks not to be clipped, or files a claim:** delete their videos from the channel
  and add their Twitch login to `skip_streamers`.
- **Another game:** change `game` in `config.json` (the exact Twitch category name goes in
  `twitch_name`) and the game-specific rules in `AGENT.md`. Kick and YouTube-only streams won't
  work from the cloud: YouTube blocks downloads there.
- **find_clips fails with "couldn't list any Twitch clips":** Twitch changed its public web API.
  The fix is to switch `list_clips()` to the official Twitch API ("Get Clips" with `game_id`),
  which needs a free Twitch developer app (client ID and secret).
- **Known limits:** GTA's radio is licensed music, so driving clips with the radio up are
  rejected. Clips are used without the streamers' or Rockstar's permission, so a copyright claim
  or strike is possible; three strikes deletes the channel.

Font: Anton (SIL Open Font License, `assets/fonts/OFL.txt`).
