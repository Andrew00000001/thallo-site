# Episode 1 voice takes

These are original AI voices: Higgsfield `seed_audio` presets, cast in `../voice_casting.md`. Each character's lines were generated in one take, which is in `raw/`, and split at the silences into one file per line. The files are 48 kHz FLAC, with no processing; the post chains are in `voice_casting.md`.

| File | Line | Status |
|---|---|---|
| `b1000/b1000_c1_l1_…` | "B one thousand. Live. Scanning location." | OK |
| `b1000/b1000_c1_l2_…` | "Hazard: crashed dropship." | Check by ear: Whisper hears "crash dropship". It may be normal run-together speech. |
| `b1000/b1000_c1_l3_…` | "Status: still crashed." | OK |
| `b1000/b1000_c1_l4_…` | "Launch pad destination: the other crashed dropship." | OK, with the same "crashed" check as l2 |
| `b1000/b1000_signoff_l1…l4` | "Kill credit: jump pad." / "Assist: Huggables." / "Next location: Steamyard Blues." / "Uploading..." | OK |
| `b1000/b1000_teehee_t2` | "Tee-hee." | **Pick** (Oct 25). Clean and voiced (HNR 11.5 dB, no fry): each syllable starts near 125 Hz and falls, with a re-lift on "hee". Pitch it up 3-5 semitones with a lighter crush in post, per `voice_casting.md`. |
| `b1000/b1000_teehee_t1`, `…_t3_hee-hee` | "Tee-hee!" / "Hee-hee!" | Alternates. t1 ends in a little fry; t3 is the cleanest (HNR 13.0 dB) but says "Hee-hee". |
| `sanchez/sanchez_c2_…` | "Oliver, we'll getcha... home." | OK. About 0.55 s before "home", as directed. There is also a comma pause after "Oliver", which can be tightened in the edit. |
| `sanchez/sanchez_c3_l1_…` | "This arm, I did not ask for." | OK |
| `sanchez/sanchez_c3_l2_…` | "But LOOK at it!" | OK (Oct 25 retake, replacing the flat take). "Look" now lifts from about 60 Hz on "but" to 127 Hz, and "it" falls away. |
| `sanchez/sanchez_c4_home` | "Home." | **Fails, twice.** Oct 23: half the frames are fry (median 75 Hz). Oct 25 "Home!": it starts at 101 Hz and sinks to 66 Hz, with 65% of frames below 75 Hz. Fraser's audition passes it (below). |
| `sanchez/sanchez_c5_mayday` | "...Mayday." | OK; the small, resigned read the shot needs. |
| `oliver/oliver_c2_l1_…` | "Sanchez! Buddy! You look GREAT!" | OK. Bright and bouncy: median 231 Hz, lifting up to +12 semitones. |
| `oliver/oliver_c2_l2_fry` | "...Fry?" | Usable. It rises like a question (102→169 Hz) but is breathy and quiet, which suits the full mouth; muffle it in post. |
| `oliver/oliver_c2_l2_fry_alt` | "Fry?" | Alternate (Oct 25). 7 dB louder and rising 77→159 Hz, but just as breathy (HNR 3.8 dB). |
| `oliver/oliver_c4_…` | "...That's THEIR ship." | **Fails, twice.** Oct 24: whispered (HNR 0.4 dB). Oct 25, without the ellipsis: still breathy (HNR 2.9 dB, about half the frames unvoiced), with no crack on "THEIR". The pitch tracker reads it mostly near 90 Hz, about an octave under his usual 174-230 Hz, which suggests creak. The Oct 25 take is kept in `raw/` only. Oct 26 tries three punctuation variants after a bright primer word. |

**Fraser audition** (`auditions/`, Oct 25), on the same two lines as Jasper's retake:
- "But LOOK at it!": "look" lifts 75→144 Hz (+11 semitones).
- "Home!": a proud, voiced exclamation peaking at 206 Hz (median 186 Hz, no fry). Only the quiet release after it creaks (4 dB down), and it fades out in the edit.

Jasper clearly failed "Home" and Fraser clearly passed it, so under the casting rule Fraser records all five Sanchez lines on Oct 26. Sanchez switches to Fraser only if the whole set passes; otherwise Jasper stays.

Jobs:
- 2026-10-23: B-1000 800f594e-fa20-4969-a00e-bade032be576 (Orion) and Sanchez f400bc09-2919-4429-83ab-d533677b3a67 (Jasper).
- 2026-10-24: Oliver 1de57d6c-0ec1-4e27-86e5-730987586c9e (John).
- 2026-10-25: Jasper f5c07bcb-39d5-4a71-99ea-96c28172fcc1, Fraser a38858a6-7727-4d76-abfe-b8a238dbf782, John 095ff54b-7aaf-4451-a3cd-96e138c35f5f and Orion ("Tee-hee") 3c1fc439-f787-41cb-9afc-5f6f9981b6c8.

Still to come:
- Oct 26: Fraser's full Sanchez set;
- Oct 26: Oliver's C4 variants.

**Lesson:** a line that opens with "..." comes out whispered or breathy in `seed_audio`, so put pauses in the edit instead.

**Measuring:** use Praat's sounding spans, not Whisper's word times, to place words. On these short takes Whisper's times ran 0.04-0.25 s early, and it put the first word at 0.0 s even when speech began 0.4 s in.
