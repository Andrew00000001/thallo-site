# Finished comics

Bryce's standing instructions (Oct 30):
- Every finished comic goes into his Google Drive, organized in folders.
- **Only fully completed work goes in.** A comic qualifies only when every slide is final, it has passed the final review and Bryce has approved it.
- Never drafts, contact sheets, loose panels, alternate takes or work in progress. A comic gets its folder here only then, because anything in this folder is uploaded.

**How it works**
- Each finished comic gets a folder here holding:
  - its slides as numbered posting JPGs (1080×1350, the `letter.py --jpg` output);
  - `post.txt`, with the caption, the alt text and the posting notes.
- `index.json` maps each folder to its Drive path under My Drive. The pattern is **BBG News › Comics › \<series and episode\> › \<post date\> \<Teaser or Carousel\>**, for example `BBG News/Comics/Local Hazards Ep 1 · We'll Getcha Home/2026-10-28 Teaser`.
- `tools/drive_upload.py` creates any missing folders and uploads anything not yet in Drive. Files already there are skipped, so it is safe to run again.
- **When it runs:** right after Bryce approves a locked comic.
  - Run it directly when the session can see the key (`GDRIVE_*` set).
  - Otherwise start a fresh upload session, which has the repository checked out and the environment's key. Starting it means `create_session` with:
  - `source_url` `https://github.com/Andrew00000001/thallo-site`;
  - `source_revision` `claude/lucid-archimedes-6dmd7h`, or the default branch once merged;
  - the prompt below.

  A scheduled task can't do this job, because the sessions it starts have no repository attached.

Upload-session prompt:

> Upload BBG News's finished comics to Bryce's Google Drive. Run `python3 -I bbg-news-repo/tools/drive_upload.py`. It reads `GDRIVE_CLIENT_ID`, `GDRIVE_CLIENT_SECRET` and `GDRIVE_REFRESH_TOKEN` from the environment and uploads every folder under `bbg-news-repo/comics_final/` not yet in My Drive › BBG News Comics.
> - Exit 2 means the key isn't set: report that in one line, pointing to `bbg-news-repo/comics_final/README.md`.
> - Otherwise report what was uploaded, or the error line.
>
> Never print, log or commit the credential values. Do not edit, commit or push anything.

**One-time setup (Bryce, on a computer, about 10 minutes).** It is your own Google key with the `drive.file` scope, which lets it see and change only the files it creates.
1. In the Google Cloud console (console.cloud.google.com), create a project and enable the **Google Drive API**.
2. Set up the **OAuth consent screen** (Google Auth Platform):
   - app name and your email; audience **External**; add your Gmail as a test user;
   - then **Publish** the app, because in Testing mode Google expires the key after 7 days.
3. Create an **OAuth client ID** of type **Web application**:
   - add the authorized redirect URI `https://developers.google.com/oauthplayground`;
   - keep the client ID and client secret.
4. Open https://developers.google.com/oauthplayground:
   - In the ⚙ menu, tick **Use your own OAuth credentials** and enter the client ID and secret.
   - In Step 1, type the scope `https://www.googleapis.com/auth/drive.file`, click **Authorize APIs** and sign in. If Google says the app isn't verified, choose Advanced and continue.
   - In Step 2, click **Exchange authorization code for tokens** and copy the **refresh token**.
5. In the Claude cloud environment's settings (the environment menu in the session title bar, then Edit), add three environment variables:
   - `GDRIVE_CLIENT_ID`;
   - `GDRIVE_CLIENT_SECRET`;
   - `GDRIVE_REFRESH_TOKEN`.

   Never paste them into a chat. New sessions pick them up, and that includes the upload sessions. Then say "Drive key is in" in the BBG News chat, and the teaser uploads right away.

Check without uploading: `python3 -I tools/drive_upload.py --dry-run`.

**Status (Oct 30):**
- The key is set, and the Google app ("BBG News Drive Uploader", project "BBG News Drive") is published "In production" with the `drive.file` scope only, so the refresh token doesn't expire after 7 days.
- The Oct 28 teaser is verified in Drive at My Drive › BBG News › Comics › Local Hazards Ep 1 · We'll Getcha Home › 2026-10-28 Teaser. The first, flat "BBG News Comics" folder was moved to the trash.
- The app's home page and privacy policy links point at this branch:
  - `https://github.com/Andrew00000001/thallo-site/tree/claude/lucid-archimedes-6dmd7h/bbg-news-repo`
  - `.../blob/claude/lucid-archimedes-6dmd7h/bbg-news-repo/PRIVACY.md`

  If the branch is merged into main and deleted, update both links in the Google Auth Platform's Branding page to the main-branch paths.
