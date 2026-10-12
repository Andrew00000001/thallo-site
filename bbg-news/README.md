# BBG News auto-poster

Posts to the BBG News Instagram automatically from GitHub Actions. Runs every hour; most runs post nothing.

## What it posts

| Type | When | Source |
| --- | --- | --- |
| Official news | Within ~1 hour of any new SkyVu announcement on the Battle Bears Gold Steam page | Steam News API |
| Countdown | 21, 14, 10, 7, 5, 3, 2, 1 days out, plus launch day, at 5pm ET | Release date read live from Steam |
| Fact post | 5pm ET on days without a countdown, in order from `content/evergreen.json` | 15 verified facts, each with its source in the caption |

Limits: max 2 posts per day. Old announcements are skipped on the first run.

**Accuracy guard:** if Steam's release date ever differs from `launch_date` in `config.json` (e.g. a delay), the bot posts nothing and the run fails, so GitHub emails you. Update `launch_date`, `launch_line` and `footer_line`, then it resumes.

## One-time setup

1. **Instagram:** create the account, then in the Instagram app's settings switch it to a **Professional** account (Creator or Business). The API only publishes to professional accounts. Suggested bio: `Fan account · Not affiliated with SkyVu`. Bio link: `https://store.steampowered.com/app/4408320/BATTLE_BEARS_GOLD/`
2. **Meta app:** at [developers.facebook.com/apps](https://developers.facebook.com/apps), create an app and pick **Business** as the type. Add the **Instagram** product. In the left menu open **Instagram > API setup with Instagram business login**, click **Generate token** next to your account, log in, and copy the token (valid 60 days).
3. **GitHub secrets** (repo > Settings > Secrets and variables > Actions):
   - `IG_ACCESS_TOKEN`: the token from step 2.
   - `GH_PAT`: a fine-grained personal access token for this repo with **Secrets: Read and write**. The refresh workflow uses it to renew the Instagram token on the 1st and 15th of each month.
4. **Merge into the default branch.** GitHub only runs scheduled workflows there. The repo must stay **public**: Instagram downloads each image from `raw.githubusercontent.com`.
5. **Test:** Actions > *BBG News auto-post* > Run workflow. Tick *preview* to get the images as a downloadable artifact without posting. Untick it to post for real.

## Customize

- `config.json`: post hour, timezone, daily cap, countdown days, hashtags, footer text.
- `content/evergreen.json`: add fact posts. Keep each one sourced. When the bank runs out, fact posts stop (news and countdown keep going).

## Run locally

```sh
pip install -r requirements.txt
python bot.py preview   # renders every post type to out/preview/ with captions.md
```

Fonts: Anton and Barlow, SIL Open Font License (see `assets/fonts/`).
