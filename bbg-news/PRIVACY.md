# BBG News bot privacy policy

BBG News is an unofficial Battle Bears Gold fan page, not affiliated with SkyVu. This policy covers the BBG News Discord bot and the posting bot in this repository.

## What the bot reads
In the BBG News Discord server's #submit-clips channel, the bot reads recent messages, including video attachments, the message text (for an `ig: @handle` or a caption), your Discord user ID and display name, and reactions.

## What it does with it
Only with your explicit OK (your 👍 on the bot's reply) and the BBG News owner's approval, the bot turns your clip into an Instagram Reel and posts it on the BBG News Instagram, credited to your Instagram handle (if you gave one) or your Discord display name. Nothing else is done with your data, and it is not sold or shared with anyone else.

## What is stored, and for how long
- Your video is downloaded only for the few minutes it takes to process, on a temporary GitHub Actions machine that is wiped when the job ends.
- The finished Reel is published to Instagram. To let Instagram fetch it, it is briefly hosted on this public repository's `bbg-media` branch (replaced at the next post) or a temporary release file (deleted right after).
- This public repository keeps only Discord message IDs for clips in the channel's newest 100 messages: no names, handles, text or files. Run logs leave out player names and captions of clips.

## Removing your data
Ask in the BBG News Discord or message the server owner. We'll delete the Instagram post and any data we hold about your clip.

## Changes
Updates to this policy are made in this file; its history shows every change.
