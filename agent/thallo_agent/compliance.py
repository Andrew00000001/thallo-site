"""Flag copy that is likely to be rejected by TikTok Shop review or break US ad rules.

This is a first-pass filter for the human gates, not legal review. It catches
disease and cure claims, absolute guarantees, and fake-testimonial phrasing.
"""

import re

# (pattern, reason). Patterns match whole words, case-insensitive.
RULES = [
    (r"\bcures?\b|\bcured\b", "disease cure claim"),
    (r"\btreats?\b|\btreatment for\b", "treatment claim"),
    (r"\bprevents?\b (cancer|disease|diabetes|covid|illness)", "disease prevention claim"),
    (r"\bheals?\b", "healing claim"),
    (r"\b(cancer|diabetes|alzheimer'?s|arthritis|depression|anxiety disorder|covid)\b", "names a disease"),
    (r"\bfda[- ]approved\b", "FDA approval claim"),
    (r"\bdoctor[- ]recommended\b|\bclinically proven\b", "unsupported authority claim"),
    (r"\bguaranteed?\b|\b100% (safe|effective)\b|\bno side effects\b", "absolute guarantee"),
    (r"\blose \d+ ?(lbs|pounds|kg)\b|\bweight loss\b", "weight-loss claim"),
    (r"\bdetox(es|ify)?\b", "detox claim"),
    (r"\bi('ve| have) been using (this|it) for\b|\bas a (real|verified) customer\b|\bmy honest review\b",
     "poses as a real customer testimonial"),
]

_COMPILED = [(re.compile(p, re.IGNORECASE), reason) for p, reason in RULES]


def check(text: str) -> list[dict]:
    """Return one finding per rule hit: {"match": str, "reason": str}."""
    findings = []
    for pattern, reason in _COMPILED:
        for m in pattern.finditer(text or ""):
            findings.append({"match": m.group(0), "reason": reason})
    return findings
