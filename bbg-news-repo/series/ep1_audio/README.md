# Episode 1 voice takes

These are original AI voices: Higgsfield `seed_audio` presets, cast in `../voice_casting.md`. Each character's lines were generated in one take, which is in `raw/`, and split at the silences into one file per line. The files are 48 kHz FLAC, with no processing; the post chains are in `voice_casting.md`.

| File | Line | Status |
|---|---|---|
| `b1000/b1000_c1_l1_…` | "B one thousand. Live. Scanning location." | OK |
| `b1000/b1000_c1_l2_…` | "Hazard: crashed dropship." | Check by ear: Whisper hears "crash dropship". It may be normal run-together speech. |
| `b1000/b1000_c1_l3_…` | "Status: still crashed." | OK |
| `b1000/b1000_c1_l4_…` | "Launch pad destination: the other crashed dropship." | OK, with the same "crashed" check as l2 |
| `b1000/b1000_signoff_l1…l4` | "Kill credit: jump pad." / "Assist: Huggables." / "Next location: Steamyard Blues." / "Uploading..." | OK |
| `sanchez/sanchez_c2_…` | "Oliver, we'll getcha... home." | OK. About 0.55 s before "home", as directed. There is also a comma pause after "Oliver", which can be tightened in the edit. |
| `sanchez/sanchez_c3_l1_…` | "This arm, I did not ask for." | OK |
| `sanchez/sanchez_c3_l2_…` | "But look at it." | **Retake.** There is no lift on "look"; it falls flat into fry. |
| `sanchez/sanchez_c4_home` | "Home." | **Retake.** Half the frames are creaky fry (median 75 Hz), not the proud chest voice the shot needs. |
| `sanchez/sanchez_c5_mayday` | "...Mayday." | OK; the small, resigned read the shot needs. |

Generated 2026-10-23: B-1000 job 800f594e-fa20-4969-a00e-bade032be576 (Orion); Sanchez job f400bc09-2919-4429-83ab-d533677b3a67 (Jasper). Still to come: B-1000's "Tee-hee" (3-4 takes), Oliver's lines (John), and Sanchez's two retakes, with Fraser on the same two lines for comparison.
