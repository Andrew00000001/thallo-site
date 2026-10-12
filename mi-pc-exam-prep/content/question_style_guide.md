# Style guide: rewording the Michigan P&C bank (PSI Series 16-81) in PSI item style

Scope: the `q` and `choices` fields of the 336 items in `final/{reg,auto,core,prop,comm}_questions.json`. The `explain` and `source` fields keep their full citations: form numbers, editions, MCL sections and DIFS bulletins.

## 0. What this guide can and cannot promise

- Public sources contain no actual Michigan PSI questions. The current Michigan bulletin (b3560, effective 6/10/2025) has no sample items. The 2021 edition shows only a non-insurance screen demo about the U.S. flag.
- The only official PSI insurance sample items are 3 items in PSI's Pennsylvania candidate booklet. It was checked in the 1/22/2026 edition (bulletin 7282) and the 2015 edition.
- The bank therefore cannot be made "the same as" the real test. What it can do is follow:
  1. PSI's published formats and its way of naming policies;
  2. published item-writing standards for licensure exams.
- This guide does both, and it puts accuracy above all style rules.

## 1. Evidence tags and precedence

| Tag | Meaning | Main sources |
|---|---|---|
| [ACCURACY] | Mandatory guardrail. Overrides every other rule. | User requirement |
| [OFFICIAL] | Published by PSI | PA booklet (formats and 3 sample items); PSI Michigan 16-81 content outline; PSI Ohio/PA bulletins ("do not read into the question"); PSI IRS-SEE bulletin ("single best answer"; non-insurance) |
| [CONVENTION] | Published item-writing standard | Haladyna & Downing 1989; Haladyna, Downing & Rodriguez 2002; ARELLO Item Writing Principles 2011 (PSI is ARELLO-accredited); NBME 2016; ASC 2025 |
| [ANECDOTAL] | Prep-provider claims. Used as a tie-breaker only. | JustInsurance 2026; Word & Brown 2023; National Online Insurance School 2026 |
| [HOUSE] | Our own consistency choice. No external evidence; lowest weight. | — |

Precedence: ACCURACY > OFFICIAL > CONVENTION > ANECDOTAL > HOUSE. When OFFICIAL and CONVENTION conflict, follow PSI. Example: ASC puts completion options in lowercase with end punctuation; PSI does not.

## 2. Accuracy guardrails [ACCURACY], highest priority

**G1. Freeze the fact and the key.** A rewrite may change wording, option order and punctuation only. It must not change:
- the rule being tested;
- any number, date, percentage or limit;
- modal verbs and bounds such as must/may/shall, at least/no more than, within/before/after;
- the party, coverage or condition the stem asks about;
- which choice text is keyed.

After reordering, set `answer` to the new index of the same key text. Then diff the key text before and after.

**G2. Keep exactly one defensible answer.**
- Read each distractor on its own against the new stem.
- If a trimmed stem or option lets a distractor become true or arguably true, restore the qualifier or move it into the stem (model item M7). "Arguably true" includes a different edition, a different date, an unstated exception, or a Michigan-versus-ISO difference.
- PSI tells candidates: "Only consider the actual information given in the question, do not read into the question by considering any possibilities or exceptions" [OFFICIAL]. Every fact the key depends on must therefore appear in the stem.
- Word-count targets never override this rule.

**G3. Edition pins.** The stem must keep a plain-language edition qualifier whenever the key depends on a form edition. That covers an amount, percentage, time period or rule that differs between ISO editions, or one the bank verified in only one edition. Examples:
- "Under the 2011 ISO Homeowners forms,"
- "Under the 2018 ISO Personal Auto Policy,"
- "Under the 2020 ISO Business Auto Coverage Form,"
- "Under the 1988 ISO Dwelling Basic Form (DP-1),"

Known cases, from `final/*_facts.md`:

| Policy | Edition issue |
|---|---|
| Homeowners | Dollar amounts are from the 2011 program; the 2022 program changed several. HO-2, HO-5 and HO-8 were verified only in the 2000 editions. |
| Personal Auto Policy | Amounts verified only in the 2018 edition |
| Business Auto | Transportation expense and loss of use: $30/day, $900 max (2020) vs $20/day, $600 max (2013) |
| DP-1 and DP-2 (1988) | Rental value 10% vs 20%; vacancy 30 vs 60 days; suit limit 1 vs 2 years |
| Commercial Crime | Insuring agreements reportedly differ between the 2015 and 2022 editions |

How to apply the pin:
- Take the year from the edition date in the item's `source` field: HO 00 03 05 11 → 2011; PP 00 01 09 18 → 2018; CA 00 01 11 20 → 2020; DP 00 01 07 88 → 1988; CG 00 01 04 13 → 2013; BP 00 03 07 13 → 2013; CP 00 10 10 12 → 2012.
- Do not use the copyright year or an assumed "current" edition.
- When in doubt, pin.
- Drop the edition only when the item tests a concept with no number AND neither the explanation nor the facts file flags an edition difference.

**G4. Date pins.** Values that are indexed or reset periodically keep their effective window in plain words:
- PIP work-loss maximum (October 1–September 30 years)
- Qualified health coverage deductible cap (July 1, 2026–June 30, 2027)
- MCCA retention (July 1, 2025–June 30, 2027)
- Guaranty Association CPI-adjusted amounts

Items about a change in the law keep the date of the change: "issued or renewed after July 1, 2020"; "as amended in 2019".

If an item asks for an indexed statutory base amount, the stem must say so ("base amount, before the annual inflation adjustment"). Otherwise the current adjusted figure is also defensible. Example: prop-003, base $25,000,000 vs $39,920,000 for 2026.

Never replace a date with "currently" or "today".

**G5. Authority pins.** Keep whatever makes the key right; name the authority (ARELLO #12).
- Never swap "Michigan law" for a policy title, or the reverse, when the two differ. Example (prop-008): Michigan fire law requires payment within 30 days after proof of loss; the unendorsed ISO HO condition says 60 days.
- Federal rules stay "federal".
- Positions that come only from DIFS stay "According to DIFS,".
- If a plain "Michigan law" could point to two different rules, use a plain description instead: "Michigan's no-fault law", "Michigan's surplus lines law", "Michigan's auto cancellation law". This covers two statutes with different deadlines, and a statutory exception the stem must rule out.
- If no plain description exists, keep the section number in parentheses at the end of the clause. Accuracy beats style.

**G6. Distractors stay wrong; add no new facts.**
- After removing a rationale clause or an absolute word, check the remaining text: the key must still be true and each distractor still false.
- Prefer reusing existing distractors. A new distractor value or statement is allowed only if the explanation, the source or `final/*_facts.md` shows it is wrong.
- Never introduce a value that is correct under another edition, date or state rule, unless the stem's pin rules it out and the explanation says so.

**G7. Leave `explain` and `source` alone, with two exceptions:**
- Fix explanations that refer to choices by letter or position after reordering. Example: reg-009, "The first choice ... the second ...".
- If you add a pin to a stem, make sure the explanation names the same edition or date.

**G8. Flag instead of fixing.** If an item cannot be made PSI-like without changing what it tests, leave it unchanged and list it for content review (Section 6).

## 3. Format rules

**F1 [OFFICIAL]** Four options and one keyed answer, the "single best answer". PSI letters the options A–D in the Pennsylvania booklet; how the app displays them is out of scope.

**F2 [OFFICIAL]** Use only PSI's three stem forms:
- **Incomplete sentence ending in ":"** — "Actual cash value is generally accepted to mean:"
- **Direct question ending in "?"** — "Which one of the following is covered under the Liability Coverage of the Business Auto Coverage Form?"
- **"...all of the following EXCEPT:"** — EXCEPT in capitals, last word before the colon.

**F3 [OFFICIAL]** Options start with a capital letter and have no closing period, in every stem form (PSI's samples).
- Remove closing periods from the 7 items that use them: reg-002, 014, 027, 030, 037, 049, 060.
- This overrides ASC's lowercase-and-punctuation convention.

**F4 [OFFICIAL]** Name policies, coverages and endorsements by title, never by ISO form number or edition code. This applies to stems and options.
- PSI's sample says "the Business Auto Coverage Form".
- The Michigan outline uses titles: "Homeowners Policy", "HO-2 through HO-8", "Commercial General Liability Coverage Forms", "Businessowners Policy", "Special Provisions - Michigan", "Other than Collision (Comprehensive)".
- Capitalize titled parts: "Coverage C – Personal Property", "the Liability Coverage". Generic coverage words may be lowercase, as in PSI's "comprehensive coverage".
- See table T1.

**F5 [OFFICIAL + CONVENTION]** Refer to law by authority, not by section number.
- No official stem contains a section number. The outline puts section numbers only in parentheses after topic names.
- The outline names acts by title ("Essential Insurance Act", "Motor Carrier Act of 1980"), and stems may do the same.
- Every legal item names its authority (ARELLO #12). See table T2 and G5.

**F6 [CONVENTION]** No "___" blank at the start or middle of a stem (Haladyna 1989; ARELLO multiple-choice rule #3).
- Rewrite as an incomplete sentence ending in ":" or as a direct question.
- For a two-blank item, ask a direct question and write each option as a labeled pair (M5). Do not split the item unless both new items can be fully verified.
- Affected items: auto-043, 051, 052; comm-016, 027, 033, 044, 045, 050.

**F7 [OFFICIAL + CONVENTION]** Negatives belong in the stem only, capitalized as EXCEPT or NOT (ARELLO multiple-choice rule #6; Haladyna 2002).
- Use them sparingly; do not add new negative items. The current share (25 of 336) is fine.
- Avoid double negatives.
- Capitalize EXCEPT or NOT only when it reverses what the candidate must select. When NOT describes a condition, write it in lowercase or rephrase positively. Examples: core-013 "who is NOT appointed"; reg-036, auto-044, prop-003, 004, 016, 038, 056, comm-028, 039.
- Write all other emphasis words in lowercase but keep the word: WITHOUT, OTHER, INSURED, LOWEST, FIRST, ADDITIONAL, NONHAZARDOUS, MOST, AT A MINIMUM, AND, COVERED, INELIGIBLE, AVAILABLE, THIRD. PSI's samples capitalize only EXCEPT.

**F8 [CONVENTION]** Order options logically (Haladyna; NBME; ASC).
- Numeric and time-period options go in ascending order, in one format.
- "None" or "No notice" goes first; "Unlimited" or "No limit" goes last.
- Order pairs by the first value, then the second. Order dates chronologically.
- Then update `answer` (G1).
- Never change values to restore answer-position balance. Rebalance only by reordering options that are not numeric.
- About half the bank's numeric sets are out of order, including every numeric set in auto (an artifact of answer-position balancing).

**F9 [CONVENTION]** Options must be parallel, similar in length, and complete the stem grammatically.
- Avoid article cues: use "a(n)", or move the article into the options. Example: reg-054 "a: Insurance counselor".
- Fix these mismatches:
  - auto-040 "limited to: Unlimited"
  - auto-009 "aggregate of: 10 consecutive days"
  - auto-010 "guilty of a civil infraction"
  - prop-034 B, which contradicts the stem
  - auto-046 B
- The key must not be the uniquely longest or most qualified option (NBME flaw list). In the bank, the key is the longest option in 31% of items by characters and 23% by words, against 25% by chance. Check case by case.

**F10 [CONVENTION]** Options carry no rationale.
- Delete "because…", "since…", "; [explanation]" and parenthetical asides from options. They lengthen keys and give clues; PSI's options run 1–9 words.
- 26 items, 35 choices; list in Report 3, Section 6.
- Apply G6 after each deletion. If the deleted clause held a fact the key needs, move that fact into the stem.

**F11 [CONVENTION]** No "all of the above" or "none of the above". The bank has none; keep it that way.

**F12 [CONVENTION]** Absolute words must not mark wrong answers (Haladyna; ARELLO #14; NBME). Words like always, never, automatically, regardless and "at all" appear almost only in distractors; there are 31 clear cases.
- Rewrite such a distractor as a specific wrong rule (wrong number, party, time or condition) taken from the explanation.
- Keep an absolute only where it is literally true, including in keys.
- Apply G6.

**F13 [OFFICIAL + CONVENTION]** Keep stems concise. PSI's sample stems run 8–18 words; the bank averages 23.8.
- Recall items: aim for 25 words or fewer.
- Scenarios: put the facts in 1–3 short sentences, then one question sentence, and aim for 45 words or fewer.
  - This matches PSI's vignette layout in its Texas Division of Workers' Compensation designated-doctor exam.
  - It also follows ARELLO #3 and #10 and Haladyna's "minimize the amount of reading" and "avoid window dressing".
- Cut definitions in parentheses and side remarks that the key does not need. G2 overrides length.

**F14 [CONVENTION]** Put the central idea in the stem (Haladyna 2002).
- PSI's direct-question sample is focused: "Which one of the following is covered under ...?"
- Turn an open "Which statement is correct?" (21 items) into a focused stem only when all four options address the same point. Otherwise leave it.

**F15 [CONVENTION]** Use plain, entry-level language (ARELLO #10).
- Spell out uncommon abbreviations the first time they appear: Michigan Catastrophic Claims Association (MCCA), Business Auto Coverage Form (not "BACF"), qualified health coverage, extended reporting period, gross vehicle weight rating.
- PIP, PPI, CGL and HO-3/DP-3-style form designations may stay.

**F16 [ANECDOTAL]** Keep recall items direct. Do not turn definition items into scenarios. One prep provider says PSI takes a "more direct definitional approach" than Pearson VUE. Use this only as a tie-breaker.

**F17 [HOUSE]** Consistency choices:
- "the Director" (of DIFS)
- dates written as "January 1, 2026"
- one number format per item: "$1,000,000", not a mix with "$1 million"
- names or roles kept short ("Dan", "a producer", "the insured")
- vary the "Under …" opener: 33% of stems start with it. PSI's samples put the policy title inside the sentence.

## 4. Transformation tables

**T1. Policy references.** Use plain names in stems and options. Add the edition year only under G3.

| Bank text | Stem wording |
|---|---|
| HO 00 03 05 11 / "HO-3 (HO 00 03 05 11)" | "the Homeowners policy (HO-3)"; with numbers: "the 2011 ISO Homeowners forms" |
| HO 00 04 / 00 05 / 00 06 / 00 08 | "the HO-4 (Contents Broad Form)", "HO-5 (Comprehensive Form)", "HO-6 (Unit-Owners Form)", "HO-8 (Modified Coverage Form)" |
| HO 04 61, HO 04 90, HO 04 54, HO 04 27, HO 24 75 | "the Scheduled Personal Property endorsement", "the Personal Property Replacement Cost endorsement", "the Earthquake endorsement", "the Limited Fungi, Wet or Dry Rot, or Bacteria Coverage endorsement", "the Watercraft endorsement" |
| DP 00 01 / 02 / 03; DL 24 01 | "the Dwelling Policy Basic Form (DP-1)" / "Broad Form (DP-2)" / "Special Form (DP-3)"; "the Personal Liability Supplement" |
| PP 00 01 09 18 / "PAP" | "the Personal Auto Policy"; parts by title, e.g., "Part A – Liability Coverage"; with numbers: "the 2018 ISO Personal Auto Policy" |
| PP 03 06 | "the Extended Non-Owned Coverage endorsement" |
| CA 00 01 11 20 / "BACF" | "the Business Auto Coverage Form"; with numbers: "the 2020 ISO Business Auto Coverage Form" |
| CA 00 05 | "the Garage Coverage Form" |
| CG 00 01 / CG 00 02 | "a Commercial General Liability (CGL) policy" / "a claims-made CGL policy" |
| CP 00 10; CP 10 10 / 10 20 / 10 30; CP 00 30 | "the Building and Personal Property Coverage Form"; "the Causes of Loss – Basic / Broad / Special Form"; "the Business Income (and Extra Expense) Coverage Form" |
| IL 00 17; IL 04 15 | "the Common Policy Conditions"; "the Protective Safeguards endorsement" |
| BP 00 03 07 13 | "the Businessowners policy"; with numbers: "the 2013 ISO Businessowners Coverage Form" |
| CR 00 21 | "the Commercial Crime Coverage Form" |
| Workers' comp policy | "the Workers' Compensation and Employers Liability Insurance Policy" |

**T2. Law references.**

| Bank text | Stem wording |
|---|---|
| "Under MCL 500.xxxx" (Insurance Code) | "Under Michigan law," / "Under the Michigan Insurance Code," |
| MCL 500.3101–.3179 (Chapter 31) | "Under Michigan's no-fault law," |
| "Under current MCL 500.3115" | "Under Michigan's no-fault law as amended in 2019," (G4) |
| MCL 500.19xx | "Under Michigan's surplus lines law," |
| MCL 500.79xx | "Under Michigan law, the Michigan Property and Casualty Guaranty Association …" |
| MCL 500.2833 | "Under Michigan's mandatory fire policy provisions," (G5) |
| Chapter citations ("Chapter 32", "Chapter 12") | Drop the chapter number and describe the subject ("an auto policy cancellation notice under Michigan law"), subject to G5 |
| "According to DIFS Bulletin 96-02" | "According to DIFS," |
| "(49 CFR 387.9)" | "Under federal motor carrier rules (Motor Carrier Act of 1980)," |
| TRIA "as reauthorized in 2019 (current law as of October 2026)" | "Under the Terrorism Risk Insurance Act, as reauthorized in 2019," (keep the pin, cut the remark in parentheses) |
| "the director" / "commissioner" | "the Director" |

**T3. Other recurring fixes.**
- core-033: remove "(Construction Code 6)" etc. from the options, since the codes are clues, and write "most" in lowercase.
- prop-037 to prop-056: replace the repeated "(HO 00 03 05 11)" with "Under the 2011 ISO Homeowners forms," only where G3 applies. Otherwise write "the Homeowners policy (HO-3)".
- Form numbers inside options (prop-026, prop-063, prop-065, comm-043): replace them with form titles.

## 5. Model items (OUR illustrative items, rewritten from our own bank; these are NOT PSI items)

**M1 (reg-003): state law by name; statute number and rationale clause removed; logical order**
- Before: "…because of low production, which is not a cause listed in MCL 500.1239. What notice must the insurer give the director?" One option read "No notice, because the termination was not for cause".
- After: **Under Michigan law, what notice must an insurer give the Director when it terminates its relationship with a producer because of low production?**
  - A. No notice is required
  - B. Notice at least 15 days before the termination takes effect
  - **C. Notice within 30 days after the effective date of the termination** ✔
  - D. Notice within 90 days after the effective date of the termination
- The key moves from A to C. Removing "not a cause listed in 1239" is safe because the 30-day rule applies to any termination (per the explanation).

**M2 (auto-018): law-change date kept; EXCEPT format; ascending order**
- After: **For Michigan auto policies issued or renewed after July 1, 2020, a named insured may choose all of the following PIP medical (allowable expense) limits EXCEPT:**
  - **A. $100,000** ✔
  - B. $250,000
  - C. $500,000
  - D. Unlimited coverage
- The key moves from B to A. The July 1, 2020 pin stays (G4).

**M3 (auto-015): indexed amount; the date pin stays; options ascending**
- After: **Dan is injured in a Michigan auto accident on November 15, 2026. He earned $10,000 a month and cannot work for several months. He does not prove a lower income tax advantage. Ignoring other offsets, what is the most PIP pays for work loss for one 30-day period?**
  - A. $7,201
  - **B. $7,455** ✔
  - C. $8,500
  - D. $10,000
- The key moves from D to B. The accident date must stay: it places the claim in the October 1, 2026–September 30, 2027 window. $7,201 was the prior year's cap.

**M4 (prop-041): form number replaced by title; edition kept as a plain-year pin**
- Before: "…from an HO-3 (HO 00 03 05 11) insured's home…"
- After: **Under the 2011 ISO Homeowners forms, a burglar steals $4,000 of jewelry from the home of an insured with an HO-3 policy. Ignoring the deductible, the policy will pay:**
  - A. $1,000
  - **B. $1,500** ✔
  - C. $2,500
  - D. $4,000
- The pin is mandatory (G3): the 2022 HO program changed several amounts.

**M5 (auto-052): two blanks become a direct question; edition pin; pairs ordered**
- After: **Under the 2018 ISO Personal Auto Policy, Part A supplementary payments include up to how much for bail bonds and up to how much a day for loss of earnings to attend hearings or trials at the insurer's request?**
  - A. Bail bonds $250; loss of earnings $200 a day
  - **B. Bail bonds $250; loss of earnings $250 a day** ✔
  - C. Bail bonds $1,000; loss of earnings $100 a day
  - D. Bail bonds $2,000; loss of earnings $250 a day
- The key moves from C to B. The amounts were verified only in the 2018 edition, so the pin stays.

**M6 (comm-013): no edition needed (concept, no number); rationale removed from the key**
- After: **A contractor finishes one part of a project, and the owner starts using that part while other contractors keep working elsewhere on the project. Under a Commercial General Liability policy, an injury arising from the finished part is treated as:**
  - **A. Completed operations** ✔
  - B. Ongoing operations until all work called for in the contract is finished
  - C. Completed operations only after the owner signs a written acceptance certificate
  - D. Excluded until the policy renews
- The key was "Completed operations, because the owner has put that part to its intended use". That fact is already in the stem, so the clause can go.

**M7 (comm-014): plain-language scenario; a qualifier moved from an option into the stem to keep one answer (G2)**
- Before: option D read "Injury occurred 8/1/2026; claim first made 2/1/2028; the occurrence was never reported and no Supplemental ERP was bought".
- After: **A business has a claims-made CGL policy from January 1, 2026, to January 1, 2027, with a retroactive date of January 1, 2022. It had no earlier claims-made policy, never reported an occurrence to the insurer, and did not buy the Supplemental Extended Reporting Period. Which claim is covered?**
  - A. Injury on June 1, 2021; claim first made March 1, 2026
  - **B. Injury on June 1, 2023; claim first made March 1, 2026** ✔
  - C. Injury on August 1, 2026; claim first made February 1, 2028
  - D. Injury on March 1, 2027; claim first made May 1, 2027
- Simply deleting D's tail would make it arguably covered under the basic extended reporting period, so that fact moves to the stem. The key moves from C to B.

**M8 (comm-070): negative cleanup; legal standard kept**
- Before: "Under MCL 500.1910, there is a rebuttable presumption that coverage is AVAILABLE from authorized insurers, so it may not be placed in surplus lines, for all of the following EXCEPT:"
- After: **Under Michigan's surplus lines law, coverage is presumed to be available from authorized insurers for all of the following EXCEPT:**
  - A. Private passenger auto physical damage
  - B. Any coverage readily available from 3 or more authorized insurers at competitive terms
  - C. Michigan no-fault auto insurance for someone who is not a self-insurer
  - **D. Coverage not obtainable after a diligent search among authorized insurers** ✔
- The rewrite removes the section number, the capitalized AVAILABLE and the consequence clause. "Presumed" stays because it is the rule being tested.

Already compliant, leave as is: core-001, "A condition that increases the probability of a loss, such as poor housekeeping in a factory, is called a(n):" (PSI Format 1).

## 6. Per-item checklist and items to flag

Checklist, in order:
1. Same key text, and `answer` index updated.
2. Every number, date, modal verb and bound unchanged.
3. Edition, date and authority pins present wherever G3–G5 apply.
4. Each distractor still false on its own; no new unsupported facts.
5. F2 stem form; F3 punctuation; F4/F5 naming; F7 capitals; F8 order; F9/F10 parity with no rationale.
6. Explanation letter or position references fixed (G7); `source` untouched.

Flag for content review; do not restyle:
- **prop-057.** Its `source` cites a Texas HO form. Re-verify it first, and note that every option carries its own justification.
- **comm-055** (P-1 schedule symbol), **auto-025** (Chapter 31A numbering), **prop-064** (amounts pre-printed in the schedule). These test form or Code trivia rather than a rule, so rewording cannot fix them. Keep or replace them as a content decision.
- **Edition currency (owner decision).** Pins keep items accurate, but no one knows which ISO editions PSI Michigan tests. California's regulator says "current editions of Insurance Services Office (ISO) policies will be used". Our Homeowners amounts are from 2011, and the 2022 program changed several.
