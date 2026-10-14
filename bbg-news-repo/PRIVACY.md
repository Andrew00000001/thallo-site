# BBG News app privacy policy

BBG News is an unofficial Battle Bears Gold fan page, not affiliated with SkyVu. This policy covers the "BBG News" Discord app and the posting bot in this repository.

## What the app reads
The app does nothing on its own. When someone uses **Send to BBG News** on a message, Discord sends the app's relay that one message (its text, attachments, and its author's ID, username and display name, including a forwarded message's contents) plus basic details about the channel and server it's in. The relay uses only the video link and the author's name, and only when the BBG News owner is the one using it; anyone else gets a refusal and their request is discarded. The app can't read servers, channels or any other messages.

## What it does with it
The owner first asks the player for permission and confirms it in the app, along with the credit (the player's Discord name or an Instagram handle they asked for). The clip is then turned into an Instagram Reel and posted on the BBG News Instagram with that credit. Nothing else is done with your data, and it is not sold or shared with anyone else.

## What is stored, and for how long
- The relay that receives the button press stores nothing; it passes the clip link, credit and caption to this repository's GitHub Actions run.
- Your video is downloaded only for the few minutes it takes to process, on a temporary GitHub Actions machine that is wiped when the job ends. Location and other metadata are stripped from the video first.
- The finished Reel is published to Instagram. To let Instagram fetch it, it is pushed to this public repository's `bbg-media` branch (or, as a fallback, a temporary release file that is deleted right after). The branch is replaced at the next post, but GitHub can keep serving the replaced file at its old link until GitHub cleans it up; fully removing it may need a request to GitHub Support.
- This public repository's history keeps the Discord attachment ID of each posted clip, the posting date and the Instagram post ID. It keeps no names, handles, captions or files, and run logs leave them out too.

## Removing your data
Message the BBG News owner on the Battle Bears Discord. We'll delete the Instagram post and ask GitHub to remove any hosted copy if needed.

## Changes
Updates to this policy are made in this file; its history shows every change.
