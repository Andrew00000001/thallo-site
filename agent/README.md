# Thallo TikTok Shop agent

The first three stages of the pipeline in the [design doc](https://claude.ai/code/artifact/9714edcf-145a-4975-be2d-56730ddc1708): trend shortlist, listing drafts, and UGC video scripts. Every stage stops at a human approval gate. Nothing here calls TikTok or publishes anything.

| Stage | Command | Waits at |
| --- | --- | --- |
| 1. Trend shortlist | `discover <csv>`, `shortlist` | Gate 1: pick |
| 2. Listing drafts | `draft-listings` | Gate 2: listing |
| 3. Video scripts + AI video prompts | `draft-scripts` | Gate 3: video |

Not built yet, on purpose: creating products on TikTok Shop (Create Product, seller token) and posting shoppable videos (Post Shoppable Video, creator token). Posting waits on one live test of the shop's own account authorizing as a creator. Rendering videos from the prompts is done with Higgsfield outside this code.

## Setup

```
cd agent
python3 -m pip install -r requirements.txt
export ANTHROPIC_API_KEY=...   # stages 2 and 3 call Claude
```

## Daily run

```
python3 -m thallo_agent discover candidates.csv     # score today's candidates
python3 -m thallo_agent review --out review.md      # read what's waiting
python3 -m thallo_agent approve 4 --gate pick       # or: reject 4 --gate pick --note "why"
python3 -m thallo_agent draft-listings
python3 -m thallo_agent approve 4 --gate listing
python3 -m thallo_agent draft-scripts
python3 -m thallo_agent approve 4 --gate video
python3 -m thallo_agent status
```

A pick rejection drops the product for good, so it is not suggested again. A listing or video rejection sends it back one step, and the redraft sees your note.

## Candidate CSV

Columns: `name, category, price, cost, units_sold, growth_pct, source_url`. Leave `category` blank to detect it from the name. `examples/candidates_sample.csv` is made-up sample data for testing, not market data.

TikTok Creative Center's Top Products page has no public API, so v1 takes a CSV filled in by hand. Once the Partner Center app exists, List Opportunities can produce the same shape.

## Scoring

Score is 0 to 100: category fit 30%, momentum (log units sold plus growth) 35%, margin 25%, policy risk 10%. Candidates outside Thallo's four collections or under 30% margin are dropped. Supplements and red light devices get a risk penalty, and a product whose name itself makes a health claim is halved so it sinks to the bottom. Weights live in `thallo_agent/config.py`.

## Compliance checks

`compliance.py` flags cure, treatment, disease, detox, weight-loss, and guarantee claims, plus lines that pose as a real customer's review. Flags show up in the review file; they don't block anything, they inform your approval. Every script is forced to carry the AI-generated label.

## Tests

```
python3 -m pytest
```

Claude calls are replaced with fixed outputs in tests, so they run without an API key.
