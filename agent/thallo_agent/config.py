"""Store niche, scoring weights, and model settings."""

import os

MODEL = os.environ.get("THALLO_MODEL", "claude-opus-5-5")

_SHARED = "/mnt/project-files"  # the project's shared folder outlives any one session


def _default_db() -> str:
    if os.path.isdir(_SHARED):
        os.makedirs(os.path.join(_SHARED, "thallo-agent"), exist_ok=True)
        return os.path.join(_SHARED, "thallo-agent", "thallo.db")
    return os.path.join(os.path.dirname(__file__), "..", "thallo.db")


DB_PATH = os.environ.get("THALLO_DB") or _default_db()

# Thallo's four collections, from index.html. Keywords decide category fit.
CATEGORIES = {
    "supplements": ["supplement", "vitamin", "magnesium", "collagen", "protein", "probiotic",
                    "electrolyte", "creatine", "greens", "omega", "capsule", "gummies"],
    "clothing": ["organic cotton", "linen", "hemp", "bamboo", "merino", "loungewear",
                 "t-shirt", "tee", "socks", "leggings", "hoodie", "sweatpants"],
    "red_light": ["red light", "infrared", "led mask", "light therapy", "light panel", "photobiomodulation"],
    "cookware": ["cast iron", "stainless steel", "ceramic", "carbon steel", "non-toxic", "pfas-free",
                 "ptfe-free", "cookware", "skillet", "dutch oven", "pan", "pot"],
}

# Categories that TikTok Shop and US regulators scrutinize most.
HIGH_RISK_CATEGORIES = {"supplements", "red_light"}

# Weights for the shortlist score (sum to 1.0).
WEIGHTS = {"fit": 0.30, "momentum": 0.35, "margin": 0.25, "risk": 0.10}

MIN_MARGIN = 0.30  # candidates below 30% gross margin are dropped
