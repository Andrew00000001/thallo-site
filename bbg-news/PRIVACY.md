# BBG News bot privacy policy

BBG News is an unofficial Battle Bears Gold fan page, not affiliated with SkyVu. This policy covers the BBG News Discord bot and the posting bot in this repository.

## What the bot reads
In the BBG News Discord server's #submit-clips channel, the bot reads recent messages, including video attachments, the message text (for an `ig: @handle` or a caption), your Discord user ID and display name, and reactions.

## What it does with it
Only with your explicit OK (your 👍 on the bot's clip request, which shows the exact credit) and the BBG News owner's approval, the bot turns your clip into an Instagram Reel, posts it on the BBG News Instagram credited to your Instagram handle (if you gave one) or your Discord display name, and announces it with a still frame in the server's feed channel. Nothing else is done with your data, and it is not sold or shared with anyone else.

## What is stored, and for how long
- Your video is downloaded only for the few minutes it takes to process, on a temporary GitHub Actions machine that is wiped when the job ends.
- The finished Reel is published to Instagram. To let Instagram fetch it, it is pushed to this public repository's `bbg-media` branch (or, as a fallback, a temporary release file that is deleted right after). The branch is replaced at the next post, but GitHub can keep serving the replaced file at its old link until GitHub cleans it up; fully removing it may need a request to GitHub Support. Location and other metadata are stripped from the video first.
- This public repository's history keeps the Discord message IDs of submitted clips and, for posted ones, the posting date and Instagram post ID. It keeps no names, handles, message text or files. Run logs leave out player names, captions of clips and download links.

## Removing your data
Ask in the BBG News Discord or message the server owner. We'll delete the Instagram post and the feed announcement, and ask GitHub to remove any hosted copy if needed.

## Changes
Updates to this policy are made in this file; its history shows every change.
