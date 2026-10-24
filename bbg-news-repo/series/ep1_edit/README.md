# Episode 1 edit

## Teaser draft v1 (for Wed Oct 28): `teaser_draft_v1.mp4`

A first cut to review, not yet posted. 720×1280, 24 fps, about 14 s, −14 LUFS.

**Sections**
- **C1 (0-10.6 s):** take 1, Seedance job e17fe146-2939-4673-8a35-3ded5ae610a4, using its clean window (0-8.4 s).
  - The generated audio is stripped.
  - B-1000's four lines (Orion) are tightened: 0.16 s pauses inside a line and 0.32 s holds between lines.
  - Draft post chain: low cut, drive, soft clip, and an 8-bit bitcrush with roughly 12 kHz sample-and-hold, 55% wet. The pitch-variance reduction in `../voice_casting.md` is not applied yet.
  - Overlays: a red "● LIVE" label, a 6-frame cyan scan line, cyan corner brackets locking onto the pad at 1.2 s, and captions just above the bottom fifth.
- **Super (1.5 s):** "LOCAL HAZARDS" over "NOV 4", with an original two-note sting (synthesised sines).
- **End card (2 s, silent):** "Unofficial fan film, not affiliated with SkyVu; characters © SkyVu."

**Known draft compromises**
- From about 8.7 s the claws fan out, so the picture freezes at 8.4 s (a dead-still hold, in character) while the last line, "Launch pad destination: the other crashed dropship.", finishes. Its last ~2 s play over the hold.
- Alternatives:
  - accept the hold;
  - cut the line to "Launch pad: the other crashed dropship.", which changes the slate's locked words (Bryce's call);
  - retake C1 hoping for a longer clean window (45 credits).
- There are no servo, breeze or pad-hum SFX and no music yet.
- The lettering is DejaVu Sans Bold, a placeholder for the original sting lettering.

**Rebuild:** `build_teaser.py` (scratchpad paths; it needs the per-line FLACs in `../ep1_audio/b1000/` and the C1 clip from Higgsfield).
