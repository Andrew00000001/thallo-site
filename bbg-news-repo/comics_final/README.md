# Finished comics

Bryce's standing instruction (Oct 30): every finished comic goes into his Google Drive as soon as it is finished.

**How it works**
- Each finished comic gets a folder here holding:
  - its slides as numbered posting JPGs (1080×1350, the `letter.py --jpg` output);
  - `post.txt`, with the caption, the alt text and the posting notes.
- `index.json` maps each folder to its Drive folder title.
- `tools/drive_upload.py` uploads anything not yet in Drive to **My Drive › BBG News Comics › \<title\>**. Files already there are skipped, so it is safe to run again.
- A scheduled task runs it every day in a fresh cloud session. The production run also fires it right after a comic is locked.

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

   Never paste them into a chat. New sessions pick them up, and that includes the daily upload task.

Check without uploading: `python3 -I tools/drive_upload.py --dry-run`.
