"""Render what is waiting at each gate as Markdown, for Bryce to read before approving."""

from . import store


def _flags(flags: list[dict]) -> str:
    if not flags:
        return "none"
    return "; ".join(f"\"{f['match']}\" ({f['reason']})" for f in flags)


def pick_section(conn) -> list[str]:
    rows = store.by_status(conn, "discovered")
    out = ["## Gate 1: pick products", ""]
    if not rows:
        return out + ["Nothing waiting.", ""]
    out += ["| ID | Product | Collection | Score | Price | Margin | Why it's trending | Flags |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for p in rows:
        d = p["score_detail"]
        flags = d["policy_flags"] + [f"unverified {u}" for u in d.get("unverified", [])]
        margin = "?" if d["margin"] is None else f"{d['margin']:.0%}"
        out.append(f"| {p['id']} | [{p['name']}]({p['source_url']}) | {p['category']} | {p['score']} "
                   f"| ${p['price']:.2f} | {margin} | {d.get('evidence') or ''} | {', '.join(flags) or 'none'} |")
    return out + [""]


def listing_section(conn) -> list[str]:
    rows = store.by_status(conn, "listing_drafted")
    out = ["## Gate 2: approve listings", ""]
    if not rows:
        return out + ["Nothing waiting.", ""]
    for p in rows:
        l = p["listing"]
        out += [f"### {p['id']}. {l['title']}", "", l["description"], "",
                *[f"- {s}" for s in l["selling_points"]], "",
                f"Price: ${l['suggested_price']:.2f}  ",
                f"Keywords: {', '.join(l['search_keywords'])}  ",
                f"Still needed: {', '.join(l['missing_info']) or 'nothing'}  ",
                f"Compliance flags: {_flags(l['compliance_flags'])}", ""]
    return out


def video_section(conn) -> list[str]:
    rows = store.by_status(conn, "scripts_drafted")
    out = ["## Gate 3: approve videos", ""]
    if not rows:
        return out + ["Nothing waiting.", ""]
    for p in rows:
        out += [f"### {p['id']}. {p['listing']['title']}", ""]
        for i, s in enumerate(p["scripts"], 1):
            out += [f"**Script {i}: {s['angle']}**", "", f"Hook: {s['hook']}", ""]
            out += [f"- {b['seconds']}: {b['voiceover']} ({b['visual']}; text: {b['on_screen_text']})"
                    for b in s["beats"]]
            out += ["", f"CTA: {s['call_to_action']}  ", f"Caption: {s['caption']} {' '.join(s['hashtags'])}  ",
                    f"AI label: {'yes' if s['ai_label'] else 'NO'}  ",
                    f"Compliance flags: {_flags(s['compliance_flags'])}", "",
                    f"Video prompt: {s['video_prompt']}", ""]
    return out


def render(conn) -> str:
    return "\n".join(["# Thallo agent: waiting for approval", "",
                      *pick_section(conn), *listing_section(conn), *video_section(conn)])
