# Michigan P&C Exam Prep

Interactive study app for the Michigan Property & Casualty Producer/Solicitor exam (PSI Series 16-81: 150 items, 2.5 hours, 74% to pass).

Open `index.html` in a browser. Progress is saved in that browser.

- **Study guide**: one section per exam-outline area, plus exam-day logistics. Every fact cites its source.
- **Practice**: 336 questions with instant feedback, explanations and sources.
- **Mock exam**: 150 questions weighted like the PSI outline, 2.5-hour timer, section-by-section results.
- **Flashcards**: 225 cards. **Key numbers**: 231 limits, deadlines and amounts.

Content was checked in October 2026 against the Michigan Compiled Laws (legislature.mi.gov), PSI's Series 16-81 outline and candidate bulletin, Michigan DIFS bulletins, FEMA/NFIP rules, U.S. Treasury (TRIA), and ISO/NCCI policy forms. Edition-dependent amounts name their form edition. Each area was researched, then fact-checked separately.

## Rebuild

`content/` holds the source data and `build/` the build script:

```
RES=content python3 build/build.py out.html
```

The script writes the page body; `index.html` wraps it in a full HTML document.
