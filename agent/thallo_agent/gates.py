"""The three human approval gates. Nothing advances without an explicit approve."""

from . import store

# gate -> (status it acts on, status after approve)
GATES = {
    "pick": ("discovered", "pick_approved"),
    "listing": ("listing_drafted", "listing_approved"),
    "video": ("scripts_drafted", "video_approved"),
}


class GateError(ValueError):
    pass


def _check(conn, product_id: int, gate: str) -> dict:
    if gate not in GATES:
        raise GateError(f"Unknown gate '{gate}'. Use one of: {', '.join(GATES)}")
    p = store.get(conn, product_id)
    if p is None:
        raise GateError(f"No product with id {product_id}")
    waiting = GATES[gate][0]
    if p["status"] != waiting:
        raise GateError(f"Product {product_id} is '{p['status']}', not waiting at the {gate} gate ('{waiting}')")
    return p


def _add_note(p: dict, gate: str, decision: str, note: str | None) -> list:
    notes = list(p.get("notes") or [])
    notes.append({"gate": gate, "decision": decision, "note": note or ""})
    return notes


def approve(conn, product_id: int, gate: str, note: str | None = None) -> None:
    p = _check(conn, product_id, gate)
    store.update(conn, product_id, status=GATES[gate][1], notes=_add_note(p, gate, "approve", note))


def reject(conn, product_id: int, gate: str, note: str | None = None) -> None:
    """Gate 1 rejects drop the product for good; later gates send it back to be redrafted."""
    p = _check(conn, product_id, gate)
    status = "rejected" if gate == "pick" else {"listing": "pick_approved", "video": "listing_approved"}[gate]
    store.update(conn, product_id, status=status, notes=_add_note(p, gate, "reject", note))
