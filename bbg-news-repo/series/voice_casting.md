# Voice casting: Episode 1 (original AI voices)

Bryce ruled on 2026-10-20 that voices may be original AI voices: Higgsfield preset voices, never cloned from or imitating a real person. On 2026-10-22 he left the casting to BBG News's own judgement and research. Robot treatment (B-1000's digital grit) is added in the edit.

## Cast

| Character | Voice (Higgsfield preset) | voice_id | Runner-up | Confidence |
|---|---|---|---|---|
| B-1000 | **Orion** | ed69c516-92d2-4b30-a967-617737a342e5 | Callum (858499d9-fef5-40e1-bc29-b4dc661dc283) | High |
| Sanchez | **Jasper** | a7b8abe9-47f1-553e-a9df-87945a7e5bc8 | Fraser (6705e465-7b52-5915-a1d8-b1222885e01d) | Medium |
| Oliver | **John** | 6b528d43-c056-4a2f-9d82-1591a7ba13b0 | Dylan (b847bc29-f184-583a-8ad9-d1f1e16d1a60) | Medium |

Generate with `seed_audio`, `voice_type: preset`. If a take fails on the points under "Watch for" below, switch to the runner-up for that character.

## How they were chosen (2026-10-22)

1. **Transcripts.** Whisper transcribed all 44 male preset previews. Many are self-descriptions, which the old pitch-only shortlist could not see. Brooks, for example, calls himself "soothing… gentle middle American clarity", which is wrong for Sanchez.
2. **Measurements.** Every preview was measured for:
   - pitch: median, range, and variability with phrase declination removed;
   - pace: syllables per second;
   - grit: HNR, CPPS, jitter and shimmer;
   - projection: alpha ratio and H1-H2;
   - apparent vocal-tract length;
   - brightness: spectral centroid and 2-4 kHz presence;
   - an accent hint from Whisper's language ID.
3. **Two independent lenses per character:**
   - spec match: the soul's Voice section turned into measurable targets;
   - casting director: persona, the actual Episode 1 lines, and the soul's rules.
4. **A final decision.** For each character it tried to refute the leading pick against the runner-up, and checked that the three leads stay distinct when they share a scene.

The data is in `voice_research/`:
- `transcripts.json`;
- `features_v2.json`;
- `final_distinct.json` (pairwise distinctness);
- `casting_panel.json` (both lenses' top 5s and the full decision).

## Why each voice

- **B-1000: Orion.**
  - Both lenses ranked him first under every weighting. His preview is already a status report: "Systems online. I am Orion. Data processing complete."
  - His natural 0.5-0.9 s pauses match C1's "line, then a half-second dead-still hold".
  - Measurements:
    - pitch 108 Hz, mid-low;
    - among the flattest in-phrase pitch of the speaking voices;
    - he projects, which suits "slightly too loud";
    - clipped pace, a light texture on a clean base, and a large tract.
  - He stays intelligible under heavy bitcrush.
  - The risk is the "smooth AI narrator" archetype. That's a style risk, not an imitation: the preset is original and brisk, never directed toward a slow, ominous film-AI read.
- **Sanchez: Jasper.**
  - A real baritone (core about 95 Hz), the warmest spectrum of the credible baritones, natural gravel, and the widest range of the low voices.
  - His one preview line swoops from 182 Hz down to 66 Hz, which covers grand, proud, resigned, and a future native "D'oh!".
  - Slow pace, and a neutral accent: the soul says "the joke is his melodrama, never his accent".
  - Sterling's self-described persona was closest, but he was ruled out: a Southern accent would become part of the joke, he is fast, and his range is narrow.
  - Fraser projects more but has less range.
  - Jasper's weaknesses are the darkest presence of all 44 and a slightly breathy source. Both are fixable in post.
- **Oliver: John.**
  - Bright and very clean, and the grin and the crack must come from the raw voice, because Oliver gets no effects.
  - His preview is cocky self-praise ("Hey, yay! The name's John!"), and he lifts 7-8 semitones on exclamations; C2 is three in a row.
  - He has headroom for the yelp, and the flattest in-phrase pitch of the Oliver candidates, for C4's deadpan.
  - He is the most distinct from Jasper of any candidate.
  - Andre was ruled out because his phrase-ends drop into Sanchez's register.
  - John and Dylan tied on the lenses' average; John wins on proven attitude and distance from Sanchez.

**Distinctness:** the three sit about an octave apart: Jasper at about 95 Hz, Orion at 108 Hz with a flat contour and bitcrush, and John at 174 Hz, bouncy. Episode 1's only on-screen pair, Jasper and John, is the most separated finalist pair. Orion and Jasper are close raw, but they never share an Episode 1 scene. When they do meet later, keep B-1000's crush at medium or heavier.

## Generating the lines

To fit Higgsfield's 5-a-day limit, each character's lines go in one generation, one sentence per line with paragraph breaks, and are split at the silences in the edit. Any line that misses is regenerated on its own. Episode 1's lines (episode1_package.md) are:

- **B-1000 (Orion).**
  - C1, the teaser: "B one thousand. Live. Scanning location." / "Hazard: crashed dropship." / "Status: still crashed." / "Launch pad destination: the other crashed dropship."
  - Sign-off: "Kill credit: jump pad." / "Assist: Huggables." / "Next location: Steamyard Blues." / "Uploading..."
  - "Tee-hee." on its own, 3-4 takes.
  - Post:
    1. reduce the pitch variance by 50-70%, keeping the final falls;
    2. add light drive;
    3. bitcrush (about 11 kHz sample-and-hold, 8-bit, 60% wet; heavier on shouts), with no vocoder or ring-mod;
    4. sit him 2-3 dB above the dialogue bus.

    Give the "Tee-hee" a lighter crush, pitched up 3-5 semitones if it comes out flat.
- **Sanchez (Jasper).**
  - The lines: "Oliver, we'll getcha... home." / "This arm, I did not ask for." / "But look at it." / "Home." / "...Mayday."
  - Watch for: about 0.5 s before "home" (cut it in the edit if needed); a lift on "look"; a chesty, proud "Home." rather than fry (try "Home!" if it creaks).
  - "...Mayday." should be small and resigned, about 6 dB down.
  - Post: a +2-3 dB presence bell near 3 kHz and a low cut below 70 Hz. No bitcrush.
  - Spanish phrases are spoken plainly, never with a put-on accent.
- **Oliver (John).**
  - The lines: "Sanchez! Buddy! You look GREAT!" / "...Fry?" / "...That's THEIR ship."
  - Watch for: whether his nasality reads cocky or whiny (cut 2-3 dB around 1-1.5 kHz if whiny), and whether "THEIR" cracks upward in C4 (if not, splice from a second take).
  - For C2's full mouth: a low-pass around 3-4 kHz and soft mouth noise.
  - Never prompt for a "funny voice".

**Optional auditions** (only if takes are borderline and the daily limit allows): Dylan on Oliver's C2 and C4 lines, and Fraser on "But look at it." and "Home.".

The 2026-10-21 reels (four preset previews per character, from the old pitch-only shortlist) are superseded.
