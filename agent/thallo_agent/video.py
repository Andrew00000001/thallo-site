"""Stage 3: UGC-style video scripts and AI video prompts for listings approved at gate 2.

Output per product: 3 scripts, each with a hook, beats, on-screen text, a caption,
and a 9:16 generation prompt. Rendering the video (Higgsfield) and posting it are
separate steps; posting waits on the live creator-token test.
"""

from pydantic import BaseModel, ConfigDict

from . import compliance, llm, store

SYSTEM = """You write short TikTok Shop videos for Thallo, a clean-living store. The videos are \
AI-generated in a UGC style: handheld, natural light, one person talking to camera or showing the \
product in a real routine.

Rules:
- The on-camera person is a presenter, never a real customer. Do not write "I've been using this for \
weeks", "my honest review", or any line implying a personal purchase or results. Demonstrate the \
product instead.
- No disease, cure, treatment, detox, or weight-loss claims, and no guarantees. Supplements get \
structure/function wording only.
- Only use product facts given in the listing. Do not invent results, numbers, or certifications.
- Every script must set ai_label to true; TikTok requires a label on realistic AI-generated content.
- Hooks must land in the first 2 seconds. Keep each video 15 to 30 seconds."""


class Beat(BaseModel):
    model_config = ConfigDict(extra="forbid")

    seconds: str
    visual: str
    voiceover: str
    on_screen_text: str


class Script(BaseModel):
    model_config = ConfigDict(extra="forbid")

    angle: str
    hook: str
    beats: list[Beat]
    call_to_action: str
    caption: str
    hashtags: list[str]
    video_prompt: str
    ai_label: bool


class ScriptSet(BaseModel):
    model_config = ConfigDict(extra="forbid")

    scripts: list[Script]


def _prompt(p: dict) -> str:
    l = p["listing"]
    lines = [
        f"Product: {l['title']}",
        f"Description: {l['description']}",
        "Selling points: " + "; ".join(l["selling_points"]),
        f"Price: ${l['suggested_price']:.2f}",
    ]
    rejected = [n for n in (p.get("notes") or []) if n["gate"] == "video" and n["decision"] == "reject"]
    if rejected:
        lines.append("Previous scripts were rejected. Reviewer notes: " + "; ".join(n["note"] for n in rejected))
    lines.append(
        "Write 3 scripts with different angles: (1) problem then product, (2) a quick demo in a daily "
        "routine, (3) a close look at materials or ingredients. For each, video_prompt is one paragraph "
        "for a 9:16 AI video generator describing the presenter, setting, lighting, camera moves, and the "
        "product on screen."
    )
    return "\n".join(lines)


def script_text(s: dict) -> str:
    parts = [s["hook"], s["call_to_action"], s["caption"]]
    for b in s["beats"]:
        parts += [b["voiceover"], b["on_screen_text"]]
    return "\n".join(parts)


def draft(conn, product_id: int) -> list[dict]:
    p = store.get(conn, product_id)
    if p is None or p["status"] != "listing_approved":
        raise ValueError(f"Product {product_id} is not approved at the listing gate")
    scripts = [s.model_dump() for s in llm.generate(SYSTEM, _prompt(p), ScriptSet).scripts]
    for s in scripts:
        s["ai_label"] = True  # never trust the model on this one
        s["compliance_flags"] = compliance.check(script_text(s))
    store.update(conn, product_id, scripts=scripts, status="scripts_drafted")
    return scripts


def draft_all(conn) -> list[int]:
    done = []
    for p in store.by_status(conn, "listing_approved"):
        draft(conn, p["id"])
        done.append(p["id"])
    return done
