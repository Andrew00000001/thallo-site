"""Stage 1: score trend candidates and build the gate-1 shortlist.

Input is a CSV of candidates. TikTok Creative Center's Top Products page has no
public API, so v1 takes a CSV typed or exported by hand. Once the Partner
Center app exists, List Opportunities (seller token) can feed the same CSV shape.

Required columns: name, price, cost, units_sold, growth_pct, source_url.
Optional column: category (one of config.CATEGORIES; detected from the name if blank).
"""

import csv
import math
import re

from . import compliance, config, store

REQUIRED = ("name", "price", "cost", "units_sold", "growth_pct", "source_url")


def detect_category(name: str) -> tuple[str | None, int]:
    """Return (category, keyword hits) for the best-matching Thallo collection."""
    best, best_hits = None, 0
    for cat, words in config.CATEGORIES.items():
        hits = sum(1 for w in words if re.search(rf"\b{re.escape(w)}\b", name, re.IGNORECASE))
        if hits > best_hits:
            best, best_hits = cat, hits
    return best, best_hits


def score(c: dict, max_units: int) -> dict | None:
    """Score one candidate from 0 to 100. Returns None when it is out of niche or under margin."""
    category = c.get("category") or None
    hits = 1
    if category not in config.CATEGORIES:
        category, hits = detect_category(c["name"])
    if not category:
        return None

    price, cost = float(c["price"]), float(c["cost"])
    if price <= 0:
        return None
    margin = (price - cost) / price
    if margin < config.MIN_MARGIN:
        return None

    units = max(int(float(c["units_sold"])), 0)
    growth = float(c["growth_pct"])

    fit = min(1.0, 0.6 + 0.2 * hits)
    # Log scale so one runaway seller doesn't flatten everyone else; growth capped at +200%.
    volume = math.log1p(units) / math.log1p(max_units) if max_units > 0 else 0.0
    trend = max(0.0, min(growth, 200.0)) / 200.0
    momentum = 0.6 * volume + 0.4 * trend
    margin_s = min(1.0, margin / 0.7)

    flags = [f["reason"] for f in compliance.check(c["name"])]
    risk = 1.0
    if category in config.HIGH_RISK_CATEGORIES:
        risk -= 0.5
    if flags:
        risk -= 0.5
    risk = max(risk, 0.0)

    w = config.WEIGHTS
    total = 100 * (w["fit"] * fit + w["momentum"] * momentum + w["margin"] * margin_s + w["risk"] * risk)
    if flags:
        total *= 0.5  # claims in the product name itself: keep it visible, but at the bottom
    return {
        "name": c["name"].strip(),
        "category": category,
        "price": price,
        "cost": cost,
        "units_sold": units,
        "growth_pct": growth,
        "source_url": c["source_url"],
        "score": round(total, 1),
        "score_detail": {
            "fit": round(fit, 2), "momentum": round(momentum, 2), "margin": round(margin, 2),
            "risk": round(risk, 2), "policy_flags": flags,
        },
    }


def load_csv(path: str) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    missing = [col for col in REQUIRED if rows and col not in rows[0]]
    if missing:
        raise ValueError(f"CSV is missing columns: {', '.join(missing)}")
    return rows


def discover(conn, csv_path: str) -> tuple[int, int]:
    """Score every row and store the in-niche ones. Returns (kept, dropped)."""
    rows = load_csv(csv_path)
    max_units = max((int(float(r["units_sold"])) for r in rows), default=0)
    kept = dropped = 0
    for r in rows:
        s = score(r, max_units)
        if s is None:
            dropped += 1
            continue
        store.upsert_candidate(conn, s)
        kept += 1
    return kept, dropped


def shortlist(conn, limit: int = 10) -> list[dict]:
    """Top candidates waiting at gate 1, best first."""
    return store.by_status(conn, "discovered")[:limit]
