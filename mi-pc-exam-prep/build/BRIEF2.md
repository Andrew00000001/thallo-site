# Interactive whiteboard lessons (v2): writer brief — Michigan P&C exam (PSI Series 16-81)

Today is 2026-10-22. Scratchpad root `S` = `/tmp/claude-0/-home-user-thallo-site/e971c816-8cd7-5b02-909e-28368863e9bd/scratchpad`.

The learner (Bryce) is preparing for the Michigan Property & Casualty Producer exam. Reading alone does not work well for them.
Their request: **"make the videos interactive, and make them more entertaining. Drawings and such explaining terms. Explaining
terms in more real life and easier to grasp rather than just reciting facts."** And then: **"kind of like the Henry Stickmin games
where you get to choose different answers."** (In those games a stick figure hits a decision point, you pick one of a few
options, and each one plays out as a short animation: wrong picks end in a funny FAIL screen and you try again, the right pick
moves the story on.) Studying anything incorrect "would be tragic": accuracy still outranks everything else.

You are rewriting one existing, already fact-checked lesson (`S/lessons/final/<ID>.json`) into the new format: a narrated
whiteboard video. Drawings sketch themselves in time with the narrator, recurring characters live through real Michigan
situations, every key term gets a plain-English meaning and a real-life picture, and the video stops every minute or so for an
activity the learner taps, sorts, drags or slides.

## 1. Facts: what you may say (unchanged rules)
- The old lesson `S/lessons/final/<ID>.json` is your factual backbone. Its fact trace is `S/lessons/drafts/<ID>.trace.md` (if
  present) and its verification notes `S/lessons/final/<ID>.review.md`. **Keep every exam fact the old lesson teaches** (coverage
  parity): you may move a detail into an activity (a swipe card, a sort item, an explore spot, a term card) but do not drop it.
  The old lesson's quiz questions may be reused, improved, or turned into other activities.
- Allowed sources for anything you add: `S/final/{reg,core,prop,auto,comm}_facts.md` (H1 blocks by section key; each block ends
  with "Flags": do not teach flagged points unless you carry the same caveat), the question bank `S/final/*_questions.json`,
  cards and key numbers in `S/final/`, memory aids `S/learn/*.final.json`, the outline `S/pc_outline.txt`. No outside facts,
  statistics, or "fun facts". Do not contradict any bank question. Use the bank's terminology.
- Michigan law beats the generic rule: say "In Michigan" for Michigan rules. Name the form edition (on screen in `src`, and in
  narration where an amount is edition-specific: "under the twenty eleven homeowners form").
- **Stories and analogies are claims too.** Every story outcome ("covered", "not covered", "the insurer pays $15,000", "Tony
  can sue") must follow from a sourced rule, with the facts of the story stated clearly enough that the answer is unambiguous
  (for example say "the house had been empty for 70 days" when vacancy matters; say "an HO-3 under the 2011 form"). Pick
  situations that are clean textbook cases, not borderline ones. An analogy explains a concept from everyday life ("a
  deductible works like the first slice you pay for yourself"); it must never imply a rule that is false, and if a natural
  analogy would mislead on an exam point, add one sentence on where the comparison stops ("Unlike a bet, though, ...").
- No real company names, brands, or real people. The insurer is just "the insurance company" (drawn as the `insurer` building).
  Places: real Michigan cities and regions are fine (Grand Rapids, Detroit, Lansing, Traverse City, the U.P.).

## 2. How to teach (what "entertaining and real life" means here)
- **Open with a story, not a list.** The title scene sets up a situation that the lesson resolves ("It's January in Grand
  Rapids. Sam Miller's house is about to have a very bad week.").
- **One main story thread per lesson** where possible, with the recurring cast; each new term arrives because the story needs it.
- **Term scenes** (`term`) for the key vocabulary: the word, its plain-English meaning, a real-life picture, and how the exam
  says it or the trap. Draw the real-life picture. 2-5 term scenes per lesson.
- **Concrete before abstract**: show what happens to a person, then name the rule.
- **Signal traps** with the exam line ("Watch out: the exam likes to swap X and Y") where the memory aids flag a confusion.
- **Humor**: light and situational (Michigan weather, a dog with opinions, Tony's pizza oven). Never at the expense of
  accuracy, never sarcastic, nothing that a learner could remember instead of the rule.
- Reuse memory hooks (`hook` scene with `mn` and the exact hook text) where one fits; list used ids in `hooks`.
- **Choose-your-path moments are the heart of the lesson** (`choice`, 2-4 per lesson): the story reaches a decision ("Tony
  smells smoke. What does he do first?"), the learner picks one of 2-4 options, and the stick figures act it out. Wrong options
  play a short, funny-but-true consequence and end in FAIL with a one-line explanation of the rule; the right option succeeds and
  the story continues. Design the wrong options from the real exam traps (the common misconceptions), so failing teaches.
  Comedy comes from the situation and the drawing (Sam sleeping while the basement floods, Tony hiding behind the pizza oven),
  never from a false rule: every outcome shown must be what the policy or the law actually does, stated with care ("can put
  the claim at risk", not "is automatically denied", unless the source says so).
- **Interactivity every 60-90 seconds** (4-8 activities in all, choices included). Prompt narration is short ("Your turn: covered or not?"). The
  learner acts; then the reveal narration (1-3 beats) states the rule behind the answers. Activities must be fully answerable
  from what came before (except a `warmup` quiz, which must be guessable from common sense and teaches the rule in its reveal).
- **Voice**: warm tutor, second person, short sentences (under 25 words), active voice. 800-900 words of narration (about
  5.5-6 minutes; hard limits 550-1300), counting choice outcomes. Characters may speak short lines in their own voice (`voice` field), at most 30% of
  the words. LISTEN-ONLY: the learner listens and should never have to read. Every fact shown on screen in a teaching scene
  (term card fields, list and recap items, hook items, table cells, drawing labels that state a rule) must also be spoken
  in that scene's narration. Activity text (quiz question and choices, cards, sort items, spots, options, why/fail/win) is
  read aloud automatically from short narrated clips (lessons/clips.py); give a clip a "clipsay" override only when its
  automatic spoken form is wrong. The narrator does the teaching; characters ask the questions a real person would ask, react, or state facts of
  the story ("I haven't lived there since March.").

## 3. The cast (fixed looks and voices; use them consistently)
| who | role | voice |
|---|---|---|
| `dana` | Dana, the insurance agent (producer). Explains, advises, sometimes is the one who gets regulated | af_bella |
| `sam` | Sam Miller, homeowner in Grand Rapids (with `jen`, Jen Miller) | am_michael |
| `jen` | Jen Miller | bf_emma |
| `tony` | Tony, owns Tony's Pizza in Detroit (business owner: BOP, CGL, commercial property, crime, WC) | am_fenrir |
| `rosa` | Rosa, commuter and driver in Lansing (auto, no-fault) | bf_emma |
| extras | `kid`, `adjuster`, `judge`, `thief`, `worker`, `doctor`, `boss`, `neighbor`, `grandma`, `regulator` | am_puck or bf_emma |
The narrator's voice is `narrator` (default; omit `voice`). Characters are drawn with `{"p":"person","opt":{"who":"tony", ...}}`.

## 4. File format
```json
{ "id": "L12", "sec": "ho", "guide": "ho",              // keep the old lesson's id, sec and guide
  "title": "<= 70 chars", "summary": "<= 160 chars", "objectives": ["2-4 items, <= 90 chars"],
  "scenes": [ ... 11-15 scenes (hard limits 9-18), first "title", last "recap" ... ],
  "check": ["3-5 existing question ids the lesson fully prepares you to answer"], "hooks": [], "sources": ["every source"] }
```
Every scene: `type`, `beats` (narration; at least one), and per type the fields below. All scenes except title, quiz, recap need
`title` (<= 60 chars) and `src` (<= 140: the citation for the scene's facts, shown small on screen).

**Beat**: `{"text": "...", "say": "...", "voice": "tony", "show": 2, "hl": "oven"}`. For an extra with a story name, add
`"speaker": "Vic"` (<= 16) so captions say "Vic:" instead of the voice's role ("Worker:").
- `say` = exactly what is spoken. Numbers, money, percents, dates and ordinals as WORDS ("two hundred fifty thousand dollars",
  "eighty percent", "July first, twenty twenty"). No digits or symbols ($ % / + & = # § @). Acronyms as spaced letters ("H O
  three", "P I P", "C G L", "N F I P", "B O P", "A C V", "U M"). Never read statute or form numbers aloud (put them in `src`).
  No "e.g.", "i.e.", "etc.".
- `text` = the caption: the same words with normal written forms ("$250,000", "80%", "HO-3", "PIP"). No / + = < > # @ § (write
  "and", "or", "per", "plus"). The validator checks text and say word for word.
- `show` (structured scenes and `term`): how many items are visible from this beat on (non-decreasing; last beat shows all).
- `hl`: in structured scenes, the index of the item to highlight; in scenes with a drawing, an element `id` (or list of ids)
  that glows while this beat plays.
- text/say <= 300 chars each.

### Scene types
Content (canvas sizes are in drawing units, x right, y down; `draw` is the list of drawing elements, section 5):
- `title`: `title` (<= 70), `subtitle` (<= 110), optional `draw` on a 90 x 72 canvas (the story's opening picture). 1-2 beats.
- `sketch`: a full-width drawing (160 x 72) that builds up beat by beat: a story moment, a cause-and-effect chain, who-pays-whom
  arrows, a comparison drawn side by side (use a `divider`). `title`, `src`, `draw` required.
- `term`: `term` (<= 40), `plain` (<= 150, plain-English meaning), `example` (<= 170, a real-life example: a cast story or an
  everyday analogy), optional `exam` (<= 150, how the exam phrases it, or the trap), optional `kind` (<= 20, label above the
  word, default "Term"; e.g. "Peril", "Michigan rule"). `draw` (80 x 72, left side) required. Beats reveal fields with `show`:
  1 = word, 2 = plain, 3 = example, 4 = exam (3 if no exam). Typical: 3-4 beats.
- Structured scenes keep the old shapes (see `S/lessons/BRIEF.md`): `bullets`, `steps` (`ladder`), `formula`, `scenario`,
  `bignum`, `hook`, `recap` may add an optional `draw` (80 x 72, shown left of the content); `compare`, `timeline`, `table` have
  no drawing. Prefer `term`/`sketch`/activities over walls of bullets; use `table`/`timeline` only where a list of numbers or
  deadlines really is the content.
- `recap`: 3-5 takeaways (<= 70 each), optional `draw` (the cast celebrating, the main picture again).

Activities (the video pauses after the last prompt beat until the learner finishes; then `reveal` plays). All need `beats`
(the prompt), `reveal` (1-3 beats that state the rule behind the answers), and except quiz: `title`, `src`.
- `quiz`: `q` (<= 200), `choices` (3-4, <= 80, never shuffled), `answer` (0-based), `why` (<= 200), optional `warmup: true`,
  optional `draw` (80 x 72: the situation). One defensible answer; distractors from real confusions; no all/none of the above.
  The first reveal beat states the right answer in words and why.
- `swipe`: rapid judgment cards. `options` (2-3 buttons, <= 18 chars: "Covered" / "Not covered", "Physical" / "Moral" /
  "Morale", "Insurable" / "Not insurable"), `cards` (3-6): `{"text": "<= 110: a concrete real-life situation", "answer": i,
  "why": "<= 150: the rule, shown after they choose", "draw": [optional, 100 x 56 mini drawing]}`. Mix the answers.
- `sort`: drag or tap items into 2-3 labeled boxes. `bins: [{"name": "<= 22"}]`, `items` (4-8): `{"text": "<= 60", "bin": i,
  "why": "<= 120, shown if they misplace it"}`. Every bin gets at least one item.
- `explore`: tap glowing spots on a full drawing (160 x 72) to discover what each part is. `draw` with `id`s, and `spots`
  (2-6): `{"on": "<element id>", "label": "<= 40", "text": "<= 170"}`. Great for "parts of a policy", "Coverages A-F on the
  Miller property", "who is who in a surety bond".
- `choice`: choose what the character does, Henry Stickmin style. `title`, `src`, `ask` (optional, <= 40: the question shown
  above the buttons, default "What would you do?"), `draw` (the decision moment, on a 160 x 58 canvas), `beats` (the set-up,
  ending with the question), `options` (2-4):
  `{"label": "<= 44: the action, in the character's terms", "ok": true|false, "draw": [the outcome, 160 x 58],
  "beats": [1-2 outcome beats, <= 40 words in all; a character may say a line], "fail": "<= 150: for wrong options, the rule
  that makes it a FAIL", "win": "<= 150: for the right option, why it works"}`. Exactly one option has `"ok": true`. The outcome
  drawing should show the consequence (the flooded basement, the denied-claim stamp, the angry neighbor); the player adds a big
  FAIL stamp to wrong outcomes automatically (top right; move it with `"failAt": [x, y]` on the option, or on the scene for all options).
  Outcome elements use `at`/`cue` against the option's own beats. `reveal` (1-2 beats) plays after the right pick and states
  the rule. A star is earned only for a right first pick; the player counts the FAILs found, so make each wrong option a
  different, instructive mistake.
- `slider`: a live calculator for math topics. `calc` (one of below), `params` (the fixed numbers), `var` (the slider:
  `{"key": <the calc's variable>, "label": "<= 40", "min", "max", "step", "start", "money": true}`), optional `goal`
  `{"op": "gte"|"lte"|"eq", "value": n, "text": "<= 120: the challenge", "done": "<= 60: shown when reached"}`, optional
  `draw` (80 x 72). The page computes every number, so the math is always right; your narration must match it exactly.
  | calc | variable (`var.key`) | params | what it shows |
  |---|---|---|---|
  | `coins` | `limit` | `value`, `pct`, `loss`, `ded` | commercial coinsurance (CP 00 10): pay = loss × limit ÷ (pct × value) − ded, max limit; no penalty when limit ≥ pct × value |
  | `horc` | `limit` | `rc`, `loss`, `acv` | HO 2011 80% rule: limit ≥ 80% RC: pay the loss (max limit); else greater of ACV or loss × limit ÷ (80% RC); deductible ignored |
  | `deductible` | `loss` | `ded`, optional `limit` | pay = loss − ded (0 if negative), max limit |
  | `prorata` | `loss` | `a`, `b`, optional `na`, `nb` (names) | other insurance pro rata by limits: A pays loss × a ÷ (a + b) |
  | `split` | `inj1` | `pp`, `pa`, optional `others` (list of other injured persons' damages) | split BI limits: each person capped at pp, total capped at pa |
  | `wcprem` | `payroll` | `rate` (per $100), `mod` | WC premium = payroll ÷ 100 × rate × mod |
  | `lossratio` | `losses` | `premium` | loss ratio = losses ÷ earned premium |
  | `acv` | `age` | `rc`, `life` | straight-line ACV = rc − rc × age ÷ life |

Rules: 9-18 scenes (aim 12-15); 4-8 activities: 2-4 `choice` scenes, 1-3 quizzes, and at least one other type (swipe, sort,
explore or slider); at least 2 term scenes; drawings in at least 5 scenes (aim: almost every scene). Words: 800-1100 in all,
counting choice outcome beats (hard limits 550-1300): all 24 lessons' audio must fit inside one web page.

## 5. Drawing elements (`draw`)
Each element is an object; `x`, `y` are its **center** in canvas units. Common fields:
- `p`: a prop name (see the catalog `S/wb/PROPS_CATALOG.md` and the picture sheets `S/wb/catalog/*.png` — look at them) or a
  primitive (below). Any Lucide icon is also available as `{"p":"icon","name":"<lucide name>"}` (redrawn by hand), for objects
  with no prop.
- `h` (height) or `w` (width) in canvas units; `opt` (prop options, e.g. person `who`/`pose`/`mood`/`hold`, car `color`);
  `color` (outline: ink blue red green orange purple yellow gray brown sky pink teal); `flip: true` mirrors; `rot` degrees.
- `id`: name it so arrows, bubbles, rings, `hl` and explore spots can refer to it.
- Timing: `at` = the beat index (counting `beats` then `reveal`) when it appears (default 0); `cue` = a word in that beat's
  `text` — it appears exactly when the narrator says that word (great for "Then, *crash*..."); `out` = a later beat index when
  it fades away; `move: {"to": [x, y], "at": beat, "cue": "word", "dur": 1.4, "sfx": "whoosh"}` slides it somewhere (a car
  driving into a tree, money moving from the insurer to Sam).
- Entrances: `anim`: `draw` (default: it sketches itself stroke by stroke), `pop`, `stamp` (default for stamps), `fade`,
  `slide-l`, `slide-r`, `drop`, `grow`, `fall`, `write` (default for text). Loops while visible: `loop`: `flicker` (fire),
  `bob`, `shake`, `spin`, `pulse`, `wobble`, `float`. Sound effect when it appears: `sfx`: `ding`, `buzz`, `pop`, `stamp`,
  `whoosh`, `click`, `crash`, `tada`, `cash`, `boing` (stamps thud automatically). Use sound sparingly: 0-3 per scene.
- `over: true` = this element is meant to overlap others (fire on a roof, water over a basement) — silences the overlap check.

Primitives:
- `label`: `text` (<= 70), `size` (default 4.5; min 3.4), `w` (wrap width, default 60), `align` (`left`/`right`), `bold`,
  `box: true` (sketchy box), `under: true` (underline), `bg` (highlighter color behind).
- `num`: a big handwritten number or amount: `text` (<= 14), `size` (default 10).
- `note`: a sticky note: `text` (<= 120), `w` (default 34), `paper` (color, default yellow).
- `stamp`: rubber stamp: `text` (<= 16, e.g. "Covered", "Not covered", "Excluded", "Void", "Paid"), `color` (green/red), `rot`.
- `bubble`: speech bubble: `text` (<= 120), `w` (default 40), `to` (the speaker's id: tail points at their head), `think: true`.
- `arrow`: `from`, `to` (element ids or [x, y]), `bend` (-0.5..0.5, default 0.12), `label` (text along it), `dash`, `bold`,
  `head` (`end`/`both`/`none`).
- `line` (`from`, `to`, `dash`), `divider` (`x`: dashed vertical line splitting the canvas), `box` (`w`, `hh` height, `title`,
  `fill`, `dash`, `r`), `circle` (`r`, `text`, `fill`), `check`/`cross` (`h`), `ring` (`on`: circles an element), `xout`
  (`on`: crosses it out).

Changing a drawing mid-scene: an element's pose, mood or text is fixed, so to change it, give the old element `"out": k` and add
a replacement at the same spot with `"at": k` (Sam happy until beat 2, then Sam shocked from beat 2).
The choice canvas (160 x 58) is shown above the option buttons, so it displays smaller than a sketch: draw its people 30-40
units tall and props correspondingly large, and keep the outcome's punchline big and central.
Layout tips: keep 2-3 units from the edges; people are about 22-30 tall, houses 30-40, cars 12-16 tall; text labels 4-5 high.
Leave the bottom-center strip (y > 64) free of important text (captions sit there). Do not cram: 4-10 elements per scene reads
best. Draw what the narrator is saying at that moment (use `at`/`cue`), not everything at once.

## 6. Check your work (required, iterate until clean)
1. `python3 -I S/lessons/validate2.py S/lessons/v2/<ID>.json` until it prints OK.
2. `cd S/wb && node tools/lshot.js ../lessons/v2/<ID>.json shots_<ID> --states` renders every scene in the real player
   (final state of each scene; activities before and after answering; for `choice`, every option's outcome with its FAIL or
   success panel) and lists warnings: overlaps, off-canvas elements, text
   that had to shrink. Fix every warning (or mark intended overlaps `over: true`). Then **Read every screenshot** and fix
   anything cluttered, misleading, ugly, too small to read, or not matching the narration. Also run once with
   `--theme dark` and check a few scenes.
3. Re-read your narration aloud in your head: does it sound like a friendly tutor telling a story, not a list being recited?

## 7. Deliverables
1. `S/lessons/v2/<ID>.json` — validated, screenshots reviewed.
2. `S/lessons/v2/<ID>.trace.md` — a fact trace: one row per factual claim (spoken, on screen, in drawings/stamps, activity
   answers and why-texts, every number, every story outcome), with the scene index, the claim, and the exact supporting
   quote with file name (facts file, question id, card, hook id, or the old lesson's trace row). A fresh verifier checks every row.
3. `S/lessons/v2/<ID>.coverage.md` — every fact the old lesson taught, and where it now lives in the new lesson (scene index and
   field). Anything dropped must be justified (only if it is wrong or duplicated).
