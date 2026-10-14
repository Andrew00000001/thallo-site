# BBG News auto-poster

Posts to the BBG News Instagram (an unofficial Battle Bears Gold fan page) from GitHub Actions. It checks every 15 minutes, and posts a clip as soon as you send it from Discord.

## What it posts

| Type | When | Source |
| --- | --- | --- |
| **Community clips** | Right after you send one from Discord with the **Send to BBG News** app | Any server you're in, e.g. the official Battle Bears server |
| Official news | Within ~15 min of a new SkyVu announcement on the Battle Bears Gold Steam page | Steam News API |
| New official video | Within ~15 min of a new upload on the Battle Bears YouTube channel (a card that points to it; the video isn't reposted) | YouTube Data API (optional) |
| Official trailer Reels | Off by default. Turn on `official_trailers` only after SkyVu OKs reposting | Steam store trailers |
| Countdown | 21, 14, 10, 7, 5, 3, 2, 1 days out, plus launch day, at 5pm ET | Release date read live from Steam |
| Fact post | 5pm ET on days without a countdown | `content/evergreen.json` (15 sourced facts) |

Limits: 3 automatic posts per day (`config.json`); clips you send don't count toward it. Every caption ends with "BBG News is an unofficial fan page, not affiliated with SkyVu."

**Accuracy guard:** if Steam's release date ever differs from `launch_date` in `config.json` (e.g. a delay), the bot posts nothing and the run fails, so GitHub emails you. Update `launch_date`, `launch_line` and `footer_line` (and dated facts in `content/evergreen.json`, like `fact-platforms`), then it resumes.

## Sending a clip from Discord

1. **Ask the player first.** For example: *"That clip is sick! Mind if I post it on BBG News, an unofficial Battle Bears Gold fan page on Instagram? I'll credit you. Got an IG handle you want tagged?"*
2. Once they say yes, long-press their message (right-click on a computer) → **Apps** → **Send to BBG News**.
3. In the form:
   - **Credit** is filled in with their Discord name. Change it to `@theirhandle` to credit their Instagram. Type `BBG News` for your own clip.
   - **Caption** is optional.
   - Tick **The player said I can post this**.
   - Leave **Clip link** as it is.
4. A private reply (only you see it) says it was sent, then updates to **✅ Posted to Instagram** with the link, or tells you why it couldn't be posted.

Good to know:
- It works in any server you're in, with no admin rights, because the app is installed on your account. Only you can use it.
- The clip has to be a video file in the message (MP4, MOV, …), at least 3 seconds. Links to videos can't be sent. Free Discord uploads max out at 20 MB.
- Only the first 90 seconds are used (`max_video_seconds` in `config.json`); the reply tells you when a clip was trimmed. Files over 100 MB (`max_clip_mb`) are refused.
- Instagram checks every video for copyrighted material (usually music) and may refuse it; you'll be told.
- The private reply can only be updated for 15 minutes. If a clip can't be posted after that, the GitHub run fails instead, so GitHub emails you.
- If the server has turned off external apps, the app still works; its replies are private either way.

## One-time setup

### 1. Instagram
1. Create the account, then switch it to a **Professional** account (Creator or Business) in the Instagram app's settings. The API only publishes to professional accounts.
2. Bio: `Unofficial fan page · Not affiliated with SkyVu`. Link: `https://store.steampowered.com/app/4408320/BATTLE_BEARS_GOLD/`
3. At [developers.facebook.com/apps](https://developers.facebook.com/apps), create an app and pick **Business** as the type. Add the **Instagram** product. Open **Instagram > API setup with Instagram business login**, click **Generate token** next to your account, log in, and copy the token (valid 60 days).

### 2. Discord app
1. At [discord.com/developers/applications](https://discord.com/developers/applications): **New Application** → name it "BBG News" → **Create**.
2. **Installation** page: under Installation Contexts tick **User Install** (Guild Install isn't needed). Install Link: **Discord Provided Link**. Under Default Install Settings → User Install, add the scope **applications.commands**. Save. (Leave **Public Bot** on, on the Bot page: Discord won't keep an install link for a private app. Others could install the app, but the relay ignores everyone but you.)
3. **Bot** page: **Reset Token** and copy it. It's only used once, to add the command.
4. **General Information** page: copy the **Application ID** and **Public Key**, and set **Privacy Policy URL** to `https://github.com/Andrew00000001/bbg-news/blob/main/PRIVACY.md`.
5. Put the Application ID in `config.json` (`discord_app_id`). In `relay/worker.js`, set `OWNER_ID` (your Discord user ID: turn on User Settings → Advanced → Developer Mode, then tap your profile → Copy User ID) and `DISCORD_PUBLIC_KEY`.

### 3. Cloudflare relay (free)
Discord needs an always-on web address to send the button press to. This tiny relay passes it to GitHub.
1. Make a GitHub token for the relay: [this pre-filled link](https://github.com/settings/personal-access-tokens/new?name=BBG+News+relay&description=Discord+clip+dispatch&actions=write&expires_in=none) → **Only select repositories** → `bbg-news` → **Generate token**. It can only start this repo's workflows.
2. Sign up at [dash.cloudflare.com](https://dash.cloudflare.com). **Workers & Pages** → **Create application** → **Hello World** template → **Deploy** → **Edit code**. Replace everything with `relay/worker.js` (with your IDs filled in) and click **Deploy**.
3. The Worker's **Settings → Variables and Secrets → Add**: type **Secret**, name `GH_TOKEN`, value = the token from step 1. **Deploy**.
4. Copy the Worker's address (`https://….workers.dev`). In the Discord Developer Portal → **General Information** → **Interactions Endpoint URL**, paste it and **Save Changes**. Discord tests it on save.

### 4. GitHub
`bbg-news` repo → **Settings → Secrets and variables → Actions → New repository secret**:

| Name | Value |
| --- | --- |
| `IG_ACCESS_TOKEN` | Instagram token |
| `GH_PAT` | Fine-grained token for this repo with **Secrets: Read and write**, used to renew the Instagram token on the 1st and 15th |
| `DISCORD_BOT_TOKEN` | Discord bot token |
| `YOUTUBE_API_KEY` | Optional: a YouTube Data API v3 key for "new official video" posts (console.cloud.google.com → enable YouTube Data API v3 → create an API key) |

Then **Actions → Register Discord command → Run workflow** once, and install the app on your account: open `https://discord.com/oauth2/authorize?client_id=APPLICATION_ID` → **Add to my apps**.

Until `IG_ACCESS_TOKEN` is added the bot stays idle. Keep this repo **public**: Instagram downloads each image and video from it.

### 5. Test
**Actions → BBG News auto-post → Run workflow** with *preview* ticked gives you every image card plus two 10-second sample Reels as a downloadable artifact. Then send a clip from Discord.

## How media is hosted

Instagram never takes direct uploads on this kind of app; it downloads each file from a public URL. Each post pushes a single commit holding only that post's files to the `bbg-media` branch and hands Instagram the commit-pinned `raw.githubusercontent.com` link. The next post replaces the branch, but GitHub keeps serving a replaced commit by its link until GitHub cleans it up, so treat every pushed file as public (that includes a clip that Instagram's copyright check then blocks). If Instagram can't fetch a video from that link, the bot retries once with a temporary GitHub Release asset and deletes it afterwards.

## Customize

- `config.json`: post hour, timezone, daily cap, countdown days, hashtags, footer text, `official_trailers`.
- `content/evergreen.json`: add fact posts. Keep each one sourced.

## Run locally

```sh
pip install -r requirements.txt
python bot.py preview   # needs ffmpeg for the sample Reels; output in out/preview/
```

Fonts: Anton and Barlow, SIL Open Font License (see `assets/fonts/`).
