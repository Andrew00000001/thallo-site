# Narrated video lessons — writer brief (Michigan P&C exam, PSI Series 16-81)

Today is 2026-10-22. The learner (Bryce) is studying for the Michigan Property & Casualty Producer/Solicitor
licensing exam with our study app. He finds learning from reading alone hard, so we are adding short narrated,
animated lessons ("videos"). Each lesson is a JSON script: a narrator voice (text-to-speech, generated later from
your `say` text) plus animated on-screen visuals rendered by the app from your structured fields. Studying anything
incorrect "would be tragic": accuracy outranks everything else.

Scratchpad root: `/tmp/claude-0/-home-user-thallo-site/e971c816-8cd7-5b02-909e-28368863e9bd/scratchpad` (below: `S/`).

## Where facts come from (the ONLY allowed sources)
Everything you put on screen or in narration must be supported by the already-verified content:
- Study guide: `S/final/{reg,core,prop,auto,comm}_facts.md`. H1 blocks by section key: reg_facts.md: `reg`, `logistics`;
  core_facts.md: `gen`, `basics`, `wc`; prop_facts.md: `mi` (Michigan laws), `dwelling`, `ho`; auto_facts.md: `auto`;
  comm_facts.md: `cpp`, `bop`, `other`. Each H1 block ends with a "Flags" list of uncertainties: do not teach flagged
  points unless you carry the same caveat; prefer to leave them out.
- Question bank: `S/final/*_questions.json` (`{id, topic, sub, q, choices, answer, explain, source}`; topic `mi` = Michigan
  laws, counted under basics). Flashcards `*_cards.json`, key numbers `*_numbers.json`.
- Memory aids: `S/learn/mn_*.final.json` (hooks: `{id, sec, title, technique, hook, unpack[], watch_out, question_ids}`),
  `S/learn/cp_*.final.json` (confusion pairs), `S/learn/vs_*.final.json` (visual summaries).
- PSI outline: `S/pc_outline.txt`.
No outside facts, no "fun facts", no statistics not in those files. If something you want to say is not in them,
leave it out. Do not contradict any question in the bank. Use the bank's and the outline's terminology.
Michigan law beats the generic rule: say "In Michigan" for Michigan-specific rules. When the facts file names a form
edition for an amount (for example the 2011 homeowners forms, 2013 BOP, 2018 Personal Auto Policy), name it on screen
(scene `src`) and do not present edition-specific amounts as universal.

## Learning design (why the format looks like this)
- Narration + visuals, not walls of text (modality principle): the screen shows short labels, numbers and diagrams;
  the voice explains. Keep on-screen text short; never put whole narration sentences on screen except in captions.
- Short segments that build step by step (segmenting/signaling): reveal items one at a time with `show`, in the order
  the narrator talks about them.
- Retrieval practice: 2-3 "quiz" scenes per lesson where the video pauses and the learner must answer before the
  explanation plays. Place them right after the content they test (or one as a "predict first" warm-up).
- Concrete stories: at least one `scenario` (a Michigan everyday situation analyzed step by step) or a worked
  `formula` example per lesson.
- Elaboration: explain WHY a rule exists when the facts files give the reason. Point out exam traps ("Watch out: the
  exam likes to swap X and Y") where the confusion pairs/hooks identify them.
- Reuse existing memory hooks verbatim (scene type `hook` with `mn` = its id) where one fits; list used ids in `hooks`.
- Pretraining: the title scene + `objectives` preview what's coming. End with a `recap` of 3-5 takeaways.

## Voice and style for `say`
Warm, clear tutor talking to one person. Second person ("you"). Short sentences (aim under 25 words). Active voice.
Signal structure ("First... Second... Here's the trap."). No hype, no filler, no jokes that could confuse, no
"In this video" (say "In this lesson"). 420-820 words of narration per lesson (about 3-5 minutes).

### `say` vs `text` (each narration beat has both)
- `say` = exactly what the voice reads. Write numbers, dollar amounts, percents, dates and ordinals as WORDS:
  "two hundred fifty thousand dollars", "eighty percent", "July first, twenty twenty", "thirty days".
  No digits and no symbols ($ % / + & = # § @) in `say`. Spell acronyms as spaced letters: "C G L", "H O three",
  "P I P", "P P I", "U M", "N F I P", "D I F S", "B O P", "A C V". Do not read statute or form numbers aloud
  ("MCL 500.3107c", "CG 00 01") — put those in the scene's `src` instead. No "e.g.", "i.e.", "etc." (say "for example").
- `text` = the caption shown on screen for that beat: the SAME words as `say`, but with normal written forms:
  numerals and symbols ("$250,000", "80%", "July 1, 2020", "30 days"), acronyms unspaced ("CGL", "HO-3", "PIP").
  Do not use / + = < > # @ § in `text` either: write "and", "or", "per", "plus".
  The validator checks word-for-word that `text` and `say` say the same thing.

## File format (one JSON file per lesson)
```json
{
  "id": "L14",
  "sec": "auto",              // reg | gen | basics | dwelling | ho | auto | cpp | bop | wc | other  (Michigan-law "mi" lessons use basics)
  "guide": "auto",            // study-guide section to open for reading: logistics | reg | gen | basics | mi | dwelling | ho | auto | cpp | bop | wc | other
  "title": "Michigan no-fault: PIP, PPI and residual liability",  // <= 70 chars
  "summary": "One sentence, <= 160 chars.",
  "objectives": ["Name the six PIP medical levels", "..."],        // 2-4, each <= 90 chars
  "scenes": [ ... 8 to 14 scenes, first "title", last "recap" ... ],
  "check": ["auto-021", "auto-017", "auto-031"],   // 3-5 existing question ids the lesson fully prepares you to answer
  "hooks": ["mn-mn_auto-01"],                      // memory hook ids used (may be empty)
  "sources": ["MCL 500.3107c", "MCL 500.3121", "..."]  // every source behind the lesson's facts
}
```
Every scene has `type`, `beats` (narration, at least one), and per type the fields below. Content scenes (all types
except title, quiz, recap) need `title` (<= 60 chars) and `src` (<= 140 chars: the citation for that scene's facts,
shown small on screen, for example "MCL 500.3107c; DIFS PIP FAQ"). Optional `icon` on many items: any icon name from
`S/lessons/icons_dl/package/icons/` (Lucide). Useful ones: house car building-2 factory briefcase shield shield-check
scale gavel file-text clipboard-list calendar clock timer dollar-sign banknote percent calculator users user hard-hat
hammer flame droplets cloud-lightning triangle-alert ban circle-check circle-x lock landmark store truck ship tractor
heart-pulse hospital umbrella layers book-open badge-check map-pin mail search eye lightbulb handshake gem package
warehouse wrench zap cpu waves siren receipt piggy-bank hand-coins file-signature stamp flag target trophy brain wheat
fence cloud-hail baby dog plane bike ruler.

A beat: `{"text": "...", "say": "...", "show": 2, "hl": 1}`. `show` = how many of the scene's revealable items are
visible from this beat on (cumulative, never decreasing; the scene's last beat must show all items). `hl` (optional)
= index of the item to highlight during this beat. text/say <= 300 chars each.

Scene types:
- `title`: `title` (<= 70), `subtitle` (<= 110), `icon` (required). 1-2 beats (hook the learner: why this matters on the exam).
- `bullets`: `items: [{label <= 48, detail? <= 110, icon?}]` 2-5. Unordered points.
- `steps`: same item shape, 2-5; numbered sequence (process, order, ranks). `"ladder": true` draws them as rising levels
  (first item at the bottom), good for levels like PIP limits.
- `compare`: `columns: [{name <= 32, icon?, points: [<= 4 strings <= 80]}]` 2-3; optional `tell` (<= 140): the one-line
  way to tell them apart. `show` counts columns; set `"tell": true` on the beat that reveals the tell.
- `timeline`: `items: [{at <= 16 ("10 days"), label <= 40, detail? <= 90}]` 2-6 in time order. Deadlines, notice periods.
- `table`: `columns: [2-4 headers <= 24]`, `items: [rows]` 2-6, each row an array of cells (<= 44 chars), same length as columns.
- `formula`: `given: [<= 4 short setup facts <= 60]` (optional), `items: [{label <= 40, expr <= 60, value <= 24}]` 2-5
  lines; the last line is the answer. Worked math: coinsurance, ACV, pro rata, split limits, WC premium.
  Arithmetic must be exact (double-check every line).
- `scenario`: `icon`, `story` (<= 260: the situation), `items: [{label <= 48, detail? <= 110}]` 0-4 reasoning steps,
  `answer` (<= 140). Set `"answer": true` on the beat that reveals the answer. Ask the question in the narration first.
- `bignum`: `items: [{value <= 14 ("74%", "$1 million"), label <= 50}]` 1-4 stat tiles. Key numbers to remember.
- `quiz`: `q` (<= 200), `choices` (3-4, each <= 80, shown in this order, never shuffled), `answer` (0-based index), `why`
  (<= 200, shown after answering), `beats` (narration asking the question; end with an invitation like "Pick an answer."
  The video then waits for the learner), `reveal` (1-3 beats narrated after the learner answers; the first reveal beat
  must state the correct answer in words and why). Exactly one defensible answer; plausible distractors drawn from
  real confusions; must be fully answerable from what the lesson taught before it (or, for a warm-up quiz, from
  everyday reasoning, with the reveal teaching the rule). No "all of the above"/"none of the above".
- `hook`: `hook` (<= 160) — copy an existing hook verbatim and set `mn` to its id, OR write a new short hook (omit `mn`)
  that is accurate and not misleading; `items`: up to 4 strings (<= 100) unpacking exactly what it stands for.
- `recap`: `title` optional, `items`: 3-5 strings (<= 70), the takeaways.

Rules: 8-14 scenes; 2-3 quiz scenes; at least one scenario or formula scene; first scene `title`, last `recap`.

## Validate
Run `python3 -I S/lessons/validate.py S/lessons/drafts/<ID>.json` and fix until it prints OK. It checks the schema,
lengths, icons, question/hook ids, `show` logic, digits/symbols in `say`, and word-for-word text/say agreement.

## Deliverables (per lesson)
1. `S/lessons/drafts/<ID>.json` — validated.
2. `S/lessons/drafts/<ID>.trace.md` — a fact trace: a table with one row per factual claim in the lesson (on-screen or
   spoken, including quiz answers and every number), giving the scene index, the claim, and the exact supporting quote
   with file name (facts file line, question id, card, or hook id). A fresh verifier will check every row.
Self-check before finishing: every number traced; quiz answers unambiguous; nothing contradicts the bank; nothing
Michigan-specific stated as universal or vice versa; edition-specific amounts labeled; check ids are answerable from
the lesson; arithmetic exact.

## Lesson plan (id, title, sec, guide, outline topics to cover; prioritize what the exam weights and the bank tests)
- L00 Your exam: format, scoring and a study plan (sec reg, guide logistics): 150 items, 2.5 hours, 74% (111), section
  weights, unscored items, test-day rules (ID, arrival, prohibited items), licensing steps (NIPR application, PE, exam,
  validity windows), how to use spaced review/quizzes — from reg_facts `logistics` block and learn/howto.final.md.
- L01 Producer licensing, appointments and CE (reg/reg): types of licensees, producer/counselor/business entity,
  appointment and termination deadlines, change of name/address, reporting actions, assumed names, CE.
- L02 Unfair trade practices, discipline, fraud and privacy (reg/reg): misrepresentation, false advertising, twisting,
  inducement, rebating, unfair discrimination, coercion/boycott, fiduciary duties, forgery, cease and desist,
  suspension/revocation, penalties and fines, insurance fraud, consumer privacy.
- L03 Risk, insurers and how insurance works (gen/gen): risk, exposure, hazard, peril, loss; avoidance, retention,
  sharing, reduction, transfer; insurable risk elements; adverse selection; law of large numbers; reinsurance;
  stock vs mutual; ratings; distribution systems.
- L04 Agency and contract law (gen/gen): producer/insurer relationship; express, implied, apparent authority;
  responsibilities to the insured; contract elements; adhesion, aleatory, personal, unilateral, conditional;
  ambiguities, reasonable expectations, indemnity, utmost good faith, representations vs warranties, concealment,
  fraud, waiver and estoppel.
- L05 Negligence, damages and liability (basics/basics): negligence elements and defenses (Michigan rules as in the
  facts), compensatory special vs general, punitive, absolute, strict, vicarious liability.
- L06 Hazards, perils, losses and valuation (basics/basics): insurable interest, underwriting and loss ratio, physical/
  moral/morale hazards, named vs open perils, direct vs consequential loss, blanket vs specific, construction types,
  ACV, replacement cost, functional replacement cost, agreed value, stated amount.
- L07 Policy structure, insureds, limits and other insurance (basics/basics): DICE + endorsements, named/first named/
  additional insureds, policy period and territory, deductibles, other insurance (primary/excess, pro rata,
  contribution by equal shares, nonconcurrency), per occurrence/per person/split/combined single/aggregates,
  restoration of limits.
- L08 Coinsurance, conditions and claims (basics/basics): coinsurance (worked formula), vacancy/unoccupancy, duties
  after loss, assignment, abandonment, liberalization, subrogation, salvage, claim settlement options, duty to
  defend, standard mortgage clause, loss payable, no benefit to bailee, applications and binders, claims handling.
- L09 Michigan required provisions and property-casualty laws (basics/mi): mandatory fire policy provisions and
  appraisal (500.2833), cancellation and nonrenewal (2123, 3020), Essential Insurance Act, TRIA, termination of
  authority (1209), plus other `mi` block items the bank tests.
- L10 Dwelling policies (dwelling/dwelling): DP forms and purpose, Coverages A-E, other coverages, exclusions,
  conditions, selected endorsements, personal liability supplement.
- L11 Homeowners forms and Section I coverages (ho/ho): HO-2 through HO-8, definitions, Coverages A-D, additional
  coverages, special limits that the bank tests.
- L12 Homeowners perils, exclusions, conditions and loss settlement (ho/ho): perils insured against by form,
  exclusions, conditions, replacement-cost loss settlement with a worked 80% example.
- L13 Homeowners Section II and endorsements (ho/ho): Coverage E and F, additional coverages, exclusions, and the
  outline's selected endorsements (Michigan special provisions, fungi, incidental occupancies, earthquake, scheduled
  personal property, personal property replacement cost, home day care, business pursuits, watercraft, personal
  injury, home business).
- L14 Michigan no-fault: PIP, PPI and residual liability (auto/auto): PIP benefits and medical levels (dates), who
  qualifies for low levels/opt-out, PPI ($1 million, what it does/doesn't cover), residual liability and required
  limits, mini-tort, tort thresholds as the facts give them.
- L15 Michigan auto laws: limits, proof, cancellation and the placement facility (auto/auto): financial
  responsibility limits, proof of insurance, MAIPF, cancellation/nonrenewal grounds and notices, rental vehicle
  coverage, aftermarket crash parts.
- L16 The Personal Auto Policy (auto/auto): definitions, Part A liability + supplementary payments + exclusions,
  Part B med pay, Part C UM/UIM (rejection, limits), Part D collision vs other than collision, deductibles,
  transportation expense, Part E duties, selected endorsements (miscellaneous type vehicle, extended non-owned,
  Michigan PIP/PPI endorsements).
- L17 Commercial auto (auto/auto): BAP, garage, physical damage, truckers, motor carrier forms; covered auto symbols;
  garagekeepers; selected endorsements (lessor additional insured, mobile equipment, Michigan PIP/PPI, drive other
  car, individual named insured); Motor Carrier Act of 1980.
- L18 The commercial package and CGL (cpp/cpp): CPP components, CGL Coverages A/B/C, supplementary payments, who is
  an insured, limits, occurrence vs claims-made (trigger, retro date, basic vs supplemental ERP), premises/operations,
  products-completed operations, insured contract, OCP, pollution.
- L19 Commercial property and business income (cpp/cpp): conditions form, BPP, condo forms, builders risk, business
  income and extra expense, legal liability, causes of loss basic/broad/special, ordinance or law, spoilage, peak
  season, value reporting.
- L20 Crime, inland marine, equipment breakdown and farm (cpp/cpp): burglary/theft/robbery definitions, discovery vs
  loss sustained, crime coverages; nationwide marine definition and inland marine forms; equipment breakdown; farm
  coverage parts A-J.
- L21 The businessowners policy (bop/bop): eligibility and purpose, Section I property (coverage, limits, deductibles,
  loss conditions, optional coverages), Section II liability, Section III conditions, selected endorsements.
- L22 Workers' compensation (wc/wc): Michigan act (exclusive remedy, employers covered, covered injuries,
  occupational disease, benefits, second injury fund), federal acts (FELA, USL&H, Jones Act), policy Parts 1-6,
  voluntary compensation, premium computation (worked example), self-insurance and placement facility.
- L23 Umbrella, specialty liability, bonds, surplus lines and flood (other/other): personal and commercial umbrella/
  excess, E&O, professional, D&O, fiduciary, liquor, EPLI, surety bonds (parties, types), surplus lines, NFIP
  (WYO vs government, coverage, limits, deductibles, waiting period), boatowners, recreational vehicles, self-
  insurance, risk retention groups, cyber.
Cover the highest-yield points well rather than everything thinly; 3-5 minutes cannot cover every bullet of a big
section, so prioritize what the bank tests most (count questions by `sub`) and what the hooks/pairs flag as traps.
