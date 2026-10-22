# Michigan P&C Exam Prep

Interactive study app for the Michigan Property & Casualty Producer/Solicitor exam (PSI Series 16-81: 150 items, 2.5 hours, 74% to pass).

Open `index.html` in a browser. Progress is saved in that browser.

- **Today**: daily plan with due reviews and new questions, streak, daily goal, XP and levels, badges, exam countdown, projected score and a mastery map of every outline section.
- **Learn**: a "how to study" page, then one study-guide section per exam-outline area plus exam-day logistics. Every fact cites its source.
- **Memory aids**: 125 memory hooks (each lists the exact facts it stands for), 30 confusion pairs with 154 drills, and 18 picture summaries.
- **Practice**: 601 questions in PSI item format with spaced repetition, confidence ratings (confident-but-wrong answers come back first), recall-first mode and a "why did I miss it" journal.
- **Games**: Lightning round, Survival, Boss battles per section, and Match (36 sets).
- **Math lab**: freshly generated problems with worked solutions for coinsurance, homeowners replacement cost, actual cash value, other-insurance sharing, split limits, Michigan PIP work loss, workers' comp premium and loss ratio.
- **Mock exam**: 150 questions weighted like the PSI outline, 2.5-hour timer, section-by-section results.
- **Flashcards**: 225 cards on a review schedule. **Key numbers**: 231 limits, deadlines and amounts.

Content was checked in October 2026 against the Michigan Compiled Laws (legislature.mi.gov), PSI's Series 16-81 outline and candidate bulletin, Michigan DIFS bulletins, FEMA/NFIP rules, U.S. Treasury (TRIA), and ISO/NCCI policy forms. Edition-dependent amounts name their form edition. Each area was researched, then fact-checked separately; the memory aids were then cross-checked against the study guide and questions.

## Rebuild

`content/` holds the source data (`content/learn/` the memory aids) and `build/` the build script:

```
RES=content LEARN=content/learn python3 build/build.py out.html
```

The script writes the page body; `index.html` wraps it in a full HTML document.
