# Thallo TikTok Shop agent

The first three stages of the pipeline in the [design doc](https://claude.ai/code/artifact/9714edcf-145a-4975-be2d-56730ddc1708): trend shortlist, listing drafts, and UGC video scripts. Every stage stops at a human approval gate. Nothing here calls TikTok or publishes anything.

| Stage | Command | Waits at |
| --- | --- | --- |
| 1. Trend shortlist | `discover <csv>`, `shortlist` | Gate 1: pick |
| 2. Listing drafts | `task` / `submit listing` (or `draft-listings` with an API key) | Gate 2: listing |
| 3. Video scripts + AI video prompts | `task` / `submit scripts` (or `draft-scripts` with an API key) | Gate 3: video |

Not built yet, on purpose: creating products on TikTok Shop (Create Product, seller token) and posting shoppable videos (Post Shoppable Video, creator token). Posting waits on one live test of the shop's own account authorizing as a creator. Rendering videos from the prompts is done with Higgsfield outside this code.

## How it runs

A daily Claude routine does the work (steps in [ROUTINE.md](ROUTINE.md)). It researches trends on the public web, fills the candidate CSV, writes listing and script drafts itself through `task` / `submit`, and posts a review in the project. No Anthropic API key is needed, and data lives in the project's shared folder so it survives between runs. Bryce approves or rejects by replying in the project.

## Setup

```
cd agent
python3 -m pip install -r requirements.txt
```

Optional: with `ANTHROPIC_API_KEY` set, `draft-listings` and `draft-scripts` call the Claude API directly instead of going through `task` / `submit`.

## Commands

```
python3 -m thallo_agent discover candidates.csv     # score today's candidates
python3 -m thallo_agent review --out review.md      # read what's waiting
python3 -m thallo_agent approve 4 --gate pick       # or: reject 4 --gate pick --note "why"
python3 -m thallo_agent task                       # next draft to write (JSON), or null
python3 -m thallo_agent submit listing 4 draft.json  # store it; runs the compliance check
python3 -m thallo_agent approve 4 --gate listing
python3 -m thallo_agent approve 4 --gate video
python3 -m thallo_agent status
```

A pick rejection drops the product for good, so it is not suggested again. A listing or video rejection sends it back one step, and the redraft sees your note.

## Candidate CSV

Required columns: `name, price, source_url`. Optional: `category` (detected from the name if blank), `cost`, `units_sold`, `growth_pct`, `evidence`. A blank number is scored as neutral and flagged "unverified", never guessed. `examples/candidates_sample.csv` is made-up sample data for testing, not market data.

The routine fills this from public web research, within each site's terms; it does not scrape TikTok or Creative Center, which has no public API. Once the Partner Center app exists, List Opportunities can feed the same shape.

## Scoring

Score is 0 to 100: category fit 30%, momentum (log units sold plus growth) 35%, margin 25%, policy risk 10%. Candidates outside Thallo's four collections or under 30% margin are dropped. Supplements and red light devices get a risk penalty, and a product whose name itself makes a health claim is halved so it sinks to the bottom. Weights live in `thallo_agent/config.py`.

## Compliance checks

`compliance.py` flags cure, treatment, disease, detox, weight-loss, and guarantee claims, plus lines that pose as a real customer's review. Flags show up in the review file; they don't block anything, they inform your approval. Every script is forced to carry the AI-generated label.

## Tests

```
python3 -m pytest
```

Claude calls are replaced with fixed outputs in tests, so they run without an API key.
