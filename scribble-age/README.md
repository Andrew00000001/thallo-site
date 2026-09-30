# Scribble Age

A free, fully automated pipeline for the YouTube channel **Scribble Age**
([@ScribbleAge](https://www.youtube.com/@ScribbleAge), channel `UC1q7Zvv9PeoL5smeMvAvwDQ`): weird,
true history stories told in warm, hand-drawn doodles. One new video a day.

## How it runs
A Claude routine, **"Scribble Age daily video"**, starts a fresh cloud session every day at
**11:52 AM Eastern**. That session follows [`AGENT.md`](AGENT.md) step by step:

1. `topics.py` picks today's topic from the planned calendar in `topics.json` (143 topics
   across 5 eras, about 5 months). It skips anything already on the channel.
2. The session researches the topic and writes an original, fact-checked script of 850–1,100 words.
3. It draws 2 shots per scene with the drawing kit, `doodle.py`.
4. `review.py` validates the episode and renders contact sheets. The session scores every shot
   and redraws the weak ones.
5. `make_video.py` builds the video: free Microsoft Edge neural voice, 4K renders with paper grain
   and vignette, camera moves, burned-in captions, and a thumbnail.
6. `upload.py` uploads it through the YouTube Data API and schedules it to go public at
   **3:00 PM Eastern**.

Each run's report arrives by push notification and email to the Claude account. Runs never commit
or push (scheduled sessions have no push access): the channel is the only record of past topics.

## Files
| File | Purpose |
|---|---|
| `AGENT.md` | The daily instructions the routine follows |
| `topics.json` / `topics.py` | Topic calendar and picker (no saved state needed) |
| `doodle.py` | Drawing kit: characters, mascot, settings, buildings, animals, props, effects |
| `review.py` | Pre-build checks and contact sheets |
| `make_video.py` | Voice, rendering, captions, assembly |
| `upload.py` | YouTube upload and scheduling |
| `assets/` | Patrick Hand font (SIL Open Font License) and the channel profile picture |

## Accounts and credentials
- **YouTube channel:** a brand account co-owned by ojj9582@gmail.com and bryceelenbaas@gmail.com.
  Make ojj9582 the primary owner on or after **Oct 3, 2026** (Google requires 7 days of ownership),
  then remove bryceelenbaas.
- **Upload app:** the Google Cloud project "Scribble Age Uploader" on ojj9582 (OAuth app in
  production, upload scope only). Its public info page is https://scribbleage.netlify.app.
- **Credentials:** `YT_CLIENT_ID`, `YT_CLIENT_SECRET` and `YT_REFRESH_TOKEN`, stored as
  environment variables in the Claude cloud environment "Default" (never in this repo).
- **Claude:** the routine, the cloud environment and this repo belong to the Claude account
  (bryceelenbaas@gmail.com).

## Common tasks
- **Pause or resume:** claude.ai/code → Routines → "Scribble Age daily video" → toggle it.
- **Post every other day** (saves usage): change the routine's schedule to
  `52 11 */2 * *` (America/Detroit).
- **Add topics:** append entries to an era list in `topics.json`. Each entry has `t` (the topic)
  and `k` (distinctive keywords used to spot duplicates).
- **Uploads fail with `token refresh failed`:** the refresh token was revoked or expired. Create a
  new one in the OAuth Playground (scope `youtube.upload`) as ojj9582, then update
  `YT_REFRESH_TOKEN`.
- **Dedupe against the whole channel, not just the latest 15 videos:** the current token is
  upload-only, so `topics.py` falls back to the RSS feed. Regenerate `YT_REFRESH_TOKEN` with both
  `youtube.upload` and `youtube.readonly` and it switches to the YouTube Data API automatically.
