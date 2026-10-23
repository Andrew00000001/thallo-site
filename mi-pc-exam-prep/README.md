# Michigan P&C Exam Prep

Interactive study app for the Michigan Property & Casualty Producer/Solicitor exam (PSI Series 16-81: 150 items, 2.5 hours, 74% to pass).

Open `index.html` in a browser. It is one self-contained file: the lesson narration and drawings are built into the page, so nothing else needs to sit next to it. Progress is saved in that browser.

- **Today**: daily plan with due reviews and new questions, streak, daily goal, XP and levels, badges, exam countdown, projected score and a mastery map of every outline section.
- **Watch**: 24 narrated whiteboard video lessons (about 160 minutes of narration), one or more per outline area. Terms are drawn and acted out by a recurring cast in everyday situations. Each lesson stops for things to do: story choices (pick what the character does next; a wrong pick plays out what goes wrong and lets you try again), quick checks, swipe cards, sorting, tap-to-explore drawings and sliders that run the exam math. Stars, sound effects (can be turned off), captions with the speaker's name, a transcript, speed control and resume; each ends with exam-style questions from the bank.
- **Learn**: a "how to study" page, then one study-guide section per exam-outline area plus exam-day logistics. Every fact cites its source.
- **Memory aids**: 125 memory hooks (each lists the exact facts it stands for), 30 confusion pairs with 154 drills, and 18 picture summaries.
- **Practice**: 601 questions in PSI item format with spaced repetition, confidence ratings (confident-but-wrong answers come back first), recall-first mode and a "why did I miss it" journal.
- **Games**: Lightning round, Survival, Boss battles per section, and Match (36 sets).
- **Math lab**: freshly generated problems with worked solutions for coinsurance, homeowners replacement cost, actual cash value, other-insurance sharing, split limits, Michigan PIP work loss, workers' comp premium and loss ratio.
- **Mock exam**: 150 questions weighted like the PSI outline, 2.5-hour timer, section-by-section results.
- **Flashcards**: 225 cards on a review schedule. **Key numbers**: 231 limits, deadlines and amounts.

Content was checked in October 2026 against the Michigan Compiled Laws (legislature.mi.gov), PSI's Series 16-81 outline and candidate bulletin, Michigan DIFS bulletins, FEMA/NFIP rules, U.S. Treasury (TRIA), and ISO/NCCI policy forms. Edition-dependent amounts name their form edition. Each area was researched, then fact-checked separately; the memory aids and lessons were then cross-checked against the study guide and questions. Every lesson was written, then checked by separate reviewers for facts, teaching and visuals, fixed, and re-checked until clean; each lesson's `.trace.md` maps its claims to sources and `.fixlog.md` records the review.

## Rebuild

`content/` holds the source data (`content/learn/` the memory aids, `content/lessons/` the lesson scripts with their trace, coverage and fix logs), `lessons/` the narration (MP3 masters, the 10 kbps Opus copies that get embedded in the page, timing and transcript checks), and `build/` the build scripts, player and drawing engine:

```
RES=content LEARN=content/learn LESSONS=content/lessons AUDIO=lessons ICONS=build/icons VALIDATOR=build WB=build/wb python3 build/build.py out.html
```

The script writes the page body; `index.html` wraps it in a full HTML document. The build refuses lesson audio that no longer matches its script, and embeds each lesson's Opus copy (`EMBED_AUDIO=0` links the MP3 files instead). The lesson data and audio are compressed inside the page (deflate and base85) and unpacked when it opens.

Lesson scripts follow `build/BRIEF2.md` and must pass `python3 build/validate2.py <lesson.json>`. Drawings are drawn by `build/wb/sketch.js` from the prop library in `build/wb/props_*.js` (`build/wb/PROPS_CATALOG.md` lists every prop). Narration is made by `build/narrate2.py` with the open Kokoro-82M voice model (ONNX, Apache-2.0; set `TTS_MODEL` to a folder with `model.onnx` and `voices.npz`), one voice for the narrator and one per cast member, and every line is transcribed back with faster-whisper (`small.en`, MIT) and compared word for word with the script; reviewed transcription differences are listed in `lessons/accepted.json`.

Bundled third-party code and fonts: rough.js (MIT, `build/wb/lib/rough.LICENSE`), the Patrick Hand font (SIL Open Font License 1.1, `build/wb/lib/hand.LICENSE`), tiny-inflate (MIT, `build/wb/lib/tiny-inflate.LICENSE`) and Lucide icons (ISC, `build/icons/LICENSE`).
