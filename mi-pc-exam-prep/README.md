# Michigan P&C Exam Prep

Interactive study app for the Michigan Property & Casualty Producer/Solicitor exam (PSI Series 16-81: 150 items, 2.5 hours, 74% to pass).

Open `index.html` in a browser (keep the `lessons/` folder next to it for the narrated lessons). Progress is saved in that browser.

- **Today**: daily plan with due reviews and new questions, streak, daily goal, XP and levels, badges, exam countdown, projected score and a mastery map of every outline section.
- **Watch**: 24 narrated, animated video lessons (about 132 minutes in all), one or more per outline area. Each pauses for quick-check questions, has captions, a transcript, speed control and resume, and ends with exam-style questions from the bank.
- **Learn**: a "how to study" page, then one study-guide section per exam-outline area plus exam-day logistics. Every fact cites its source.
- **Memory aids**: 125 memory hooks (each lists the exact facts it stands for), 30 confusion pairs with 154 drills, and 18 picture summaries.
- **Practice**: 601 questions in PSI item format with spaced repetition, confidence ratings (confident-but-wrong answers come back first), recall-first mode and a "why did I miss it" journal.
- **Games**: Lightning round, Survival, Boss battles per section, and Match (36 sets).
- **Math lab**: freshly generated problems with worked solutions for coinsurance, homeowners replacement cost, actual cash value, other-insurance sharing, split limits, Michigan PIP work loss, workers' comp premium and loss ratio.
- **Mock exam**: 150 questions weighted like the PSI outline, 2.5-hour timer, section-by-section results.
- **Flashcards**: 225 cards on a review schedule. **Key numbers**: 231 limits, deadlines and amounts.

Content was checked in October 2026 against the Michigan Compiled Laws (legislature.mi.gov), PSI's Series 16-81 outline and candidate bulletin, Michigan DIFS bulletins, FEMA/NFIP rules, U.S. Treasury (TRIA), and ISO/NCCI policy forms. Edition-dependent amounts name their form edition. Each area was researched, then fact-checked separately; the memory aids and lessons were then cross-checked against the study guide and questions.

## Rebuild

`content/` holds the source data (`content/learn/` the memory aids, `content/lessons/` the lesson scripts), `lessons/` the narration audio with its timing and transcript checks, and `build/` the build scripts:

```
RES=content LEARN=content/learn LESSONS=content/lessons AUDIO=lessons ICONS=build/icons VALIDATOR=build python3 build/build.py out.html
```

The script writes the page body; `index.html` wraps it in a full HTML document. The build refuses lesson audio that no longer matches its script.

Lesson scripts follow `build/BRIEF.md` and must pass `python3 build/validate.py <lesson.json>`. Narration is made by `build/narrate.py` with the open Kokoro-82M voice model (ONNX, Apache-2.0; set `TTS_MODEL` to a folder with `model.onnx` and `voices.npz`), and every line is transcribed back with faster-whisper (`small.en`, MIT) and compared word for word with the script; reviewed transcription differences are listed in `lessons/accepted.json`. Icons are from Lucide (ISC license, `build/icons/LICENSE`).
