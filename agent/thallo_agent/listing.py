"""Stage 2: draft TikTok Shop listings for products approved at gate 1.

Drafts are stored for gate 2. Creating the product on TikTok Shop
(Create Product, seller token) is intentionally not wired up yet.
"""

from pydantic import BaseModel, ConfigDict

from . import compliance, llm, store

SYSTEM = """You write TikTok Shop product listings for Thallo, a clean-living store that sells \
supplements, organic clothing, red light therapy devices, and non-toxic cookware. \
Thallo's voice is calm, warm, and specific: it talks about ingredients, materials, and daily routines, \
never hype.

Rules every listing must follow:
- Describe what the product is, what it is made of, and how people use it. No disease, cure, \
treatment, detox, or weight-loss claims, and no "FDA approved", "clinically proven", or guarantees.
- For supplements, use structure/function wording only (for example "supports restful sleep") and \
never name a medical condition.
- Do not invent specs, certifications, or test results. If a fact is not in the product data, leave it out \
and list it under missing_info instead.
- Title under 100 characters, plain words, no emoji."""


class ListingDraft(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str
    description: str
    selling_points: list[str]
    search_keywords: list[str]
    suggested_price: float
    image_shot_list: list[str]
    missing_info: list[str]


def _prompt(p: dict) -> str:
    lines = [
        f"Product: {p['name']}",
        f"Thallo collection: {p['category']}",
        f"Current market price: ${p['price']:.2f} (our cost ${p['cost']:.2f})",
        f"Trend source: {p['source_url']}",
    ]
    rejected = [n for n in (p.get("notes") or []) if n["gate"] == "listing" and n["decision"] == "reject"]
    if rejected:
        lines.append("A previous draft was rejected. Reviewer notes: " + "; ".join(n["note"] for n in rejected))
    lines.append(
        "Write the listing: title, a 120 to 200 word description, 4 to 6 selling points, 8 to 12 search "
        "keywords, a suggested price, a shot list of 5 product photos, and any product facts we still need."
    )
    return "\n".join(lines)


def listing_text(d: dict) -> str:
    return "\n".join([d["title"], d["description"], *d["selling_points"], *d["search_keywords"]])


def draft(conn, product_id: int) -> dict:
    p = store.get(conn, product_id)
    if p is None or p["status"] != "pick_approved":
        raise ValueError(f"Product {product_id} is not approved at the pick gate")
    result = llm.generate(SYSTEM, _prompt(p), ListingDraft).model_dump()
    result["compliance_flags"] = compliance.check(listing_text(result))
    store.update(conn, product_id, listing=result, status="listing_drafted")
    return result


def draft_all(conn) -> list[int]:
    done = []
    for p in store.by_status(conn, "pick_approved"):
        draft(conn, p["id"])
        done.append(p["id"])
    return done
