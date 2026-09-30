import os

import pytest

from thallo_agent import compliance, discovery, gates, listing, llm, review, store, video

SAMPLE = os.path.join(os.path.dirname(__file__), "..", "examples", "candidates_sample.csv")


@pytest.fixture
def conn(tmp_path):
    with store.connect(str(tmp_path / "t.db")) as c:
        yield c


def names(rows):
    return [r["name"] for r in rows]


def test_detect_category_uses_whole_words():
    assert discovery.detect_category("Red light therapy panel")[0] == "red_light"  # "panel" is not "pan"
    assert discovery.detect_category("Stainless steel skillet")[0] == "cookware"
    assert discovery.detect_category("Phone case with glitter")[0] is None


def test_discover_keeps_niche_and_drops_the_rest(conn):
    kept, dropped = discovery.discover(conn, SAMPLE)
    # Phone case is out of niche; ceramic pan is under the 30% margin floor.
    assert (kept, dropped) == (5, 2)
    got = names(discovery.shortlist(conn))
    assert "Phone case with glitter" not in got
    assert "Ceramic nonstick pan PFAS-free" not in got


def test_policy_flags_lower_the_score(conn):
    discovery.discover(conn, SAMPLE)
    ranked = discovery.shortlist(conn)
    detox = ranked[-1]
    assert detox["name"] == "Detox tea that cures bloating"  # best sales in the file, still last
    assert detox["score_detail"]["policy_flags"]
    assert detox["score_detail"]["risk"] == 0.0


def test_compliance_catches_claims_and_fake_testimonials():
    reasons = {f["reason"] for f in compliance.check(
        "This cures anxiety disorder. I've been using this for a month. Guaranteed results!")}
    assert {"disease cure claim", "names a disease", "poses as a real customer testimonial",
            "absolute guarantee"} <= reasons
    assert compliance.check("Supports restful sleep as part of your evening routine.") == []


def test_gates_enforce_order(conn):
    discovery.discover(conn, SAMPLE)
    pid = discovery.shortlist(conn)[0]["id"]
    with pytest.raises(gates.GateError):
        gates.approve(conn, pid, "listing")  # can't skip gate 1
    gates.approve(conn, pid, "pick", "looks good")
    assert store.get(conn, pid)["status"] == "pick_approved"
    with pytest.raises(gates.GateError):
        gates.approve(conn, pid, "pick")  # already past it


def test_rejected_pick_is_not_resuggested(conn):
    discovery.discover(conn, SAMPLE)
    p = discovery.shortlist(conn)[0]
    gates.reject(conn, p["id"], "pick", "not our brand")
    discovery.discover(conn, SAMPLE)  # next run sees the same product again
    assert store.get(conn, p["id"])["status"] == "rejected"
    assert p["name"] not in names(discovery.shortlist(conn))


FAKE_LISTING = listing.ListingDraft(
    title="Magnesium Glycinate Capsules, 120 Count",
    description="A gentle form of magnesium for your evening routine. Guaranteed to work.",
    selling_points=["Glycinate form", "120 capsules"],
    search_keywords=["magnesium", "glycinate"],
    suggested_price=24.99,
    image_shot_list=["bottle front"],
    missing_info=["third-party testing"],
)

FAKE_SCRIPTS = video.ScriptSet(scripts=[video.Script(
    angle="routine demo",
    hook="My wind-down routine, in 20 seconds",
    beats=[video.Beat(seconds="0-3", visual="bedside table", voiceover="Two capsules with water.",
                      on_screen_text="evening routine")],
    call_to_action="Tap the product below",
    caption="Evening routine",
    hashtags=["#magnesium"],
    video_prompt="Vertical 9:16, warm lamp light, presenter at a bedside table.",
    ai_label=False,
)])


def test_listing_then_video_flow(conn, monkeypatch):
    discovery.discover(conn, SAMPLE)
    pid = discovery.shortlist(conn)[0]["id"]
    gates.approve(conn, pid, "pick")

    monkeypatch.setattr(llm, "generate", lambda system, prompt, schema, effort="high":
                        FAKE_LISTING if schema is listing.ListingDraft else FAKE_SCRIPTS)

    assert listing.draft_all(conn) == [pid]
    p = store.get(conn, pid)
    assert p["status"] == "listing_drafted"
    assert any(f["reason"] == "absolute guarantee" for f in p["listing"]["compliance_flags"])

    with pytest.raises(ValueError):
        video.draft(conn, pid)  # listing not approved yet
    gates.approve(conn, pid, "listing")
    assert video.draft_all(conn) == [pid]
    p = store.get(conn, pid)
    assert p["status"] == "scripts_drafted"
    assert p["scripts"][0]["ai_label"] is True  # forced on even when the model says no

    md = review.render(conn)
    assert "Gate 3: approve videos" in md and "Magnesium Glycinate" in md


def test_listing_reject_sends_back_with_notes(conn, monkeypatch):
    discovery.discover(conn, SAMPLE)
    pid = discovery.shortlist(conn)[0]["id"]
    gates.approve(conn, pid, "pick")
    seen = {}

    def fake(system, prompt, schema, effort="high"):
        seen["prompt"] = prompt
        return FAKE_LISTING

    monkeypatch.setattr(llm, "generate", fake)
    listing.draft(conn, pid)
    gates.reject(conn, pid, "listing", "drop the guarantee line")
    assert store.get(conn, pid)["status"] == "pick_approved"
    listing.draft(conn, pid)
    assert "drop the guarantee line" in seen["prompt"]


def test_blank_numbers_are_neutral_and_flagged(conn, tmp_path):
    csv_path = tmp_path / "c.csv"
    csv_path.write_text(
        "name,category,price,cost,units_sold,growth_pct,source_url,evidence\n"
        "Linen loungewear set,,$68.00,,,,https://example.com/a,Featured in a spring trend roundup\n"
    )
    assert discovery.discover(conn, str(csv_path)) == (1, 0)
    d = discovery.shortlist(conn)[0]["score_detail"]
    assert d["margin"] is None
    assert d["unverified"] == ["cost", "units sold", "growth"]
    assert "Featured in a spring trend roundup" in review.render(conn)


def test_handoff_runs_stages_without_the_api(conn, monkeypatch):
    from thallo_agent import handoff

    def no_api(*a, **k):
        raise AssertionError("handoff must not call the API")

    monkeypatch.setattr(llm, "generate", no_api)
    discovery.discover(conn, SAMPLE)
    pid = discovery.shortlist(conn)[0]["id"]
    assert handoff.next_task(conn) is None  # nothing approved yet
    gates.approve(conn, pid, "pick")

    task = handoff.next_task(conn)
    assert (task["stage"], task["product_id"]) == ("listing", pid)
    assert "title" in task["json_schema"]["properties"]
    with pytest.raises(ValueError):
        handoff.submit(conn, "listing", pid, '{"title": "missing fields"}')
    flags = handoff.submit(conn, "listing", pid, FAKE_LISTING.model_dump_json())
    assert any(f["reason"] == "absolute guarantee" for f in flags)

    gates.approve(conn, pid, "listing")
    assert handoff.next_task(conn)["stage"] == "scripts"
    handoff.submit(conn, "scripts", pid, FAKE_SCRIPTS.model_dump_json())
    assert store.get(conn, pid)["scripts"][0]["ai_label"] is True
    assert handoff.next_task(conn) is None


def test_signal_ranks_sales_data_above_editorial_picks(conn, tmp_path):
    csv_path = tmp_path / "c.csv"
    csv_path.write_text(
        "name,category,price,source_url,signal\n"
        "Stainless steel skillet,,60,https://example.com/a,editorial\n"
        "Cast iron dutch oven,,60,https://example.com/b,sales\n"
    )
    discovery.discover(conn, str(csv_path))
    top = discovery.shortlist(conn)[0]
    assert top["name"] == "Cast iron dutch oven"
    assert "growth" not in top["score_detail"]["unverified"]
