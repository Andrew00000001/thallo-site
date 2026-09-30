"""Run the Claude stages without an API key.

A Claude session (the daily routine) asks for the next job with ``task``, writes
the JSON itself, and hands it back with ``submit``. The same schema, compliance
check, and gate rules apply as when ``llm.generate`` calls the API directly.
"""

import json

from pydantic import ValidationError

from . import listing, store, video

# stage -> (status it works on, prompt builder, system prompt, schema)
STAGES = {
    "listing": ("pick_approved", listing._prompt, listing.SYSTEM, listing.ListingDraft),
    "scripts": ("listing_approved", video._prompt, video.SYSTEM, video.ScriptSet),
}


def next_task(conn) -> dict | None:
    """The next product waiting on a Claude-written draft, with everything needed to write it."""
    for stage, (status, build, system, schema) in STAGES.items():
        rows = store.by_status(conn, status)
        if rows:
            p = rows[0]
            return {
                "stage": stage,
                "product_id": p["id"],
                "instructions": system,
                "prompt": build(p),
                "json_schema": schema.model_json_schema(),
            }
    return None


def submit(conn, stage: str, product_id: int, raw: str) -> list[dict]:
    """Validate and store a draft. Returns the compliance flags found."""
    if stage not in STAGES:
        raise ValueError(f"Unknown stage '{stage}'. Use one of: {', '.join(STAGES)}")
    status, _, _, schema = STAGES[stage]
    p = store.get(conn, product_id)
    if p is None or p["status"] != status:
        raise ValueError(f"Product {product_id} is not waiting for a {stage} draft")
    try:
        draft = schema.model_validate(json.loads(raw)).model_dump()
    except (json.JSONDecodeError, ValidationError) as e:
        raise ValueError(f"Draft does not match the {stage} schema: {e}") from e

    if stage == "listing":
        return listing.save(conn, product_id, draft)["compliance_flags"]
    return [f for s in video.save(conn, product_id, draft["scripts"]) for f in s["compliance_flags"]]
