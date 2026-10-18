# BBG weapons research (verified)

Start with `00_OVERVIEW.md`. It covers sources, the shared combat effects, rules for showing weapons in shorts, the main corrections and the confidence summary.

Each class (`b-1000`, `oliver`, `riggs`, `huggable`, `tillman`, `astoria`, `wil`, `graham`, `botch`, `saberi`, `sanchez`) and each topic (`combat-vfx`, `2026`, `shared`) has:
- `<key>.md`: the verified dossier. For every weapon it gives the official text, look, firing, projectile, impact and a depiction note for shorts, with a source label on every claim.
- `<key>.meta.json`:
  - `quickref`: one row per weapon.
  - `soul_corrections`: verified fixes for the character files.
  - `open_questions`.
- `<key>.addendum.md` and `<key>.addendum.meta.json`: the gap passes run after the completeness critic, same format.

Indexes:
- `quickref_all.json`: all 443 quick-reference rows.
- `corrections_all.json`: all 262 verified character-file corrections.

**How it was checked:**
1. Draft.
2. Source check: every quote re-fetched.
3. Image check: every cited image re-opened.
4. Edit.
5. Completeness critic and gap passes.
6. Overview.

**Not reachable:** web.archive.org (connection resets) and YouTube playback. YouTube evidence comes from thumbnails and storyboard frames only.
