# BBG News auto-poster

Posts to the BBG News Instagram automatically from GitHub Actions. Runs every 15 minutes; most runs post nothing.

## What it posts

| Type | When | Source |
| --- | --- | --- |
| Official news | Within ~15 min of a new SkyVu announcement on the Battle Bears Gold Steam page | Steam News API |
| New official video | Within ~15 min of a new upload on the Battle Bears YouTube channel (a card that points to it; the video itself is not reposted) | YouTube Data API (optional) |
| **Community clips** | As soon as you approve a clip in your Discord | Your BBG News Discord server |
| Official trailer Reels | Off by default. Turn on `official_trailers` only after SkyVu OKs reposting | Steam store trailers |
| Countdown | 21, 14, 10, 7, 5, 3, 2, 1 days out, plus launch day, at 5pm ET | Release date read live from Steam |
| Fact post | 5pm ET on days without a countdown | `content/evergreen.json` (15 sourced facts) |

Limits: 3 auto posts + 3 clips per day (`config.json`). Old announcements and videos are skipped on the first run. Every caption ends with "BBG News is an unofficial fan page, not affiliated with SkyVu."

**Accuracy guard:** if Steam's release date ever differs from `launch_date` in `config.json` (e.g. a delay), the bot posts nothing and the run fails, so GitHub emails you. Update `launch_date`, `launch_line` and `footer_line`, then it resumes.

## How Discord clips work

In your **#submit-clips** channel:

1. A player posts a video. The bot reacts 👀 and replies asking for permission.
2. The player reacts 👍 on the bot's reply. That's their go-ahead to post it on Instagram with credit (Discord's developer terms require the player's explicit OK).
3. **You** react ✅ on the clip to approve it, or ❌ to reject it. Only your reactions count.
4. The bot makes a branded 9:16 Reel, posts it, replies with the link and reacts 📸.

- Your own clips skip step 2: just post and ✅.
- To write the caption yourself, reply to the clip with `caption: your text` before approving.
- Players get tagged as text in the caption if they add `ig: @theirhandle` to their message; otherwise their Discord name is used.
- Free Discord uploads max out at 20 MB, so ask players to trim to the best 10–30 seconds.
- Instagram runs a copyright check on every video. If it matches (usually music), the bot skips the clip and tells the player.
- The bot only looks at the newest 100 messages in #submit-clips, so keep that channel for clips.

Every post is also mirrored into your **#bbg-news-feed** channel, if you set one up.

## One-time setup

### 1. Instagram
1. Create the account, then switch it to a **Professional** account (Creator or Business) in the Instagram app's settings. The API only publishes to professional accounts.
2. Bio: `Unofficial fan page · Not affiliated with SkyVu`. Links: the Steam page (`https://store.steampowered.com/app/4408320/BATTLE_BEARS_GOLD/`) and your Discord invite.
3. At [developers.facebook.com/apps](https://developers.facebook.com/apps), create an app and pick **Business** as the type. Add the **Instagram** product. Open **Instagram > API setup with Instagram business login**, click **Generate token** next to your account, log in, and copy the token (valid 60 days).

### 2. Discord
1. Create your own server (e.g. "BBG News") with a **#submit-clips** channel and, optionally, a read-only **#bbg-news-feed** channel. You can't add a bot to the official Battle Bears server unless you have Manage Server there.
2. At [discord.com/developers/applications](https://discord.com/developers/applications): **New Application** → name it → **Create**.
   - **Bot** page: click **Reset Token** and copy it. Turn **Message Content Intent** ON (without it the bot can't see attachments). Turn **Public Bot** OFF.
   - **General Information** page: copy the **Application ID**, and set **Privacy Policy URL** to this repo's `bbg-news/PRIVACY.md` on GitHub.
3. Invite the bot by opening this link (put in your Application ID) and picking your server:
   `https://discord.com/oauth2/authorize?client_id=APPLICATION_ID&scope=bot&permissions=101440`
   (101440 = View Channel, Send Messages, Add Reactions, Attach Files, Read Message History.)
4. In Discord, turn on **User Settings → Advanced → Developer Mode**. Then long-press (or right-click) **#submit-clips** → **Copy Channel ID**, the same for **#bbg-news-feed**, and your own profile → **Copy User ID**.
5. Pin the rules from [DISCORD_RULES.md](DISCORD_RULES.md) in #submit-clips.
6. Only promote your server inside the official Battle Bears Discord where its rules allow it.

### 3. YouTube (optional)
For "new official video" posts: in [console.cloud.google.com](https://console.cloud.google.com), create a project, enable **YouTube Data API v3**, and create an **API key** (restrict it to that API). Skip this and those posts are simply off.

### 4. GitHub
Repo → **Settings → Secrets and variables → Actions**:

| Name | Type | Value |
| --- | --- | --- |
| `IG_ACCESS_TOKEN` | Secret | Instagram token |
| `GH_PAT` | Secret | Fine-grained token for this repo with **Secrets: Read and write**, used to renew the Instagram token on the 1st and 15th |
| `DISCORD_BOT_TOKEN` | Secret | Discord bot token |
| `YOUTUBE_API_KEY` | Secret | Optional |
| `DISCORD_OWNER_ID` | Variable | Your Discord user ID |
| `DISCORD_CLIPS_CHANNEL_ID` | Variable | #submit-clips channel ID |
| `DISCORD_FEED_CHANNEL_ID` | Variable | #bbg-news-feed channel ID (optional) |

Then **merge into the default branch**; GitHub only runs scheduled workflows there. Keep the repo **public**: Instagram downloads each image and video from it.

### 5. Test
Actions → *BBG News auto-post* → **Run workflow** with *preview* ticked: you get every image card plus two 10-second sample Reels as a downloadable artifact. Untick it to run for real.

## How media is hosted

Instagram never takes direct uploads on this kind of app; it downloads each file from a public URL. Each post pushes a single commit holding only that post's files to the `bbg-media` branch (replaced by the next post) and hands Instagram the commit-pinned `raw.githubusercontent.com` link. If Instagram rejects that link for a video, the bot retries once with a temporary GitHub Release asset and deletes it afterwards.

## Customize

- `config.json`: post hour, timezone, daily caps, countdown days, hashtags, footer text, `official_trailers`.
- `content/evergreen.json`: add fact posts. Keep each one sourced.

## Run locally

```sh
pip install -r requirements.txt
python bot.py preview   # needs ffmpeg for the sample Reels; output in out/preview/
```

Fonts: Anton and Barlow, SIL Open Font License (see `assets/fonts/`).
