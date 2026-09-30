# Daily routine

A scheduled Claude session runs this once a day. It needs no Anthropic API key: the session writes the drafts itself through `task` and `submit`. Agent data lives in the project's shared folder (`/mnt/project-files/thallo-agent/`), so it survives between runs.

The routine never publishes, lists, or posts anything. It fills the shortlist, drafts what Bryce approved since the last run, and posts one review for him in the project.

## Steps

1. **Set up.** Check out the agent branch, `cd agent`, and `python3 -m pip install -r requirements.txt`.
2. **Research trends.** Use web search to find 10 to 20 products gaining attention in Thallo's four collections (supplements, organic clothing, red light therapy, non-toxic cookware), with a TikTok Shop angle where possible. Read only public pages through normal search and browsing. Do not scrape TikTok, Creative Center, or any site that forbids automated collection in its terms, and do not log in anywhere.
3. **Write the CSV** to `/mnt/project-files/thallo-agent/candidates-YYYY-MM-DD.csv` with columns `name,category,price,cost,units_sold,growth_pct,source_url,evidence,signal`. Rules:
    - `source_url` is a page you actually opened, and `evidence` is one short line from it saying why the product is trending.
    - `price` is the retail price shown on that page.
    - `signal` is `sales` for TikTok Shop sales rankings, `social` for TikTok content volume, or `editorial` for press and review picks.
    - Leave `cost`, `units_sold`, and `growth_pct` blank unless the page states them. Never estimate; blanks are scored as neutral and flagged "unverified".
4. **Score:** `python3 -m thallo_agent discover <csv>`.
5. **Draft what was approved.** Repeat until `python3 -m thallo_agent task` prints `null`:
    - Read the task's `instructions`, `prompt`, and `json_schema`.
    - Write JSON that matches the schema and follows the instructions, save it to a scratch file, and run `python3 -m thallo_agent submit <stage> <product_id> <file>`.
    - If submit rejects the JSON, fix it and resubmit.
6. **Review.** `python3 -m thallo_agent review --out /mnt/project-files/thallo-agent/review-YYYY-MM-DD.md`, then post a short summary in the project with that file attached: the top 5 new candidates, any drafts waiting, and every compliance flag.
7. **Approvals** come back as chat replies ("approve 4", "reject 6: too pricey"). Apply each with `approve` or `reject --gate <gate> --note`, then run step 5 again.
