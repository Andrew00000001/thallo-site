"""Command line entry point: python -m thallo_agent <command>."""

import argparse
import json
import sys

from . import discovery, gates, handoff, listing, review, store, video


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="thallo_agent", description=__doc__)
    ap.add_argument("--db", help="SQLite file (default: $THALLO_DB, else the shared project folder, else agent/thallo.db)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    d = sub.add_parser("discover", help="score a CSV of trend candidates")
    d.add_argument("csv")
    s = sub.add_parser("shortlist", help="show the top candidates waiting at gate 1")
    s.add_argument("--limit", type=int, default=10)
    sub.add_parser("draft-listings", help="draft listings for products approved at gate 1")
    sub.add_parser("draft-scripts", help="draft video scripts for listings approved at gate 2")
    sub.add_parser("task", help="print the next draft for a Claude session to write, as JSON")
    t = sub.add_parser("submit", help="store a draft written by a Claude session")
    t.add_argument("stage", choices=list(handoff.STAGES))
    t.add_argument("id", type=int)
    t.add_argument("file", help="JSON file matching the task's json_schema")
    r = sub.add_parser("review", help="write everything waiting at a gate to Markdown")
    r.add_argument("--out", default="-", help="file path, or - for stdout")
    sub.add_parser("status", help="list every product and its stage")
    for name in ("approve", "reject"):
        g = sub.add_parser(name, help=f"{name} a product at a gate")
        g.add_argument("id", type=int)
        g.add_argument("--gate", required=True, choices=list(gates.GATES))
        g.add_argument("--note")

    a = ap.parse_args(argv)
    with store.connect(a.db) as conn:
        if a.cmd == "discover":
            kept, dropped = discovery.discover(conn, a.csv)
            print(f"Kept {kept} candidates, dropped {dropped} (out of niche or under margin).")
        elif a.cmd == "shortlist":
            for p in discovery.shortlist(conn, a.limit):
                flags = ", ".join(p["score_detail"]["policy_flags"])
                print(f"{p['id']:>4}  {p['score']:>5}  {p['category']:<12} {p['name']}" + (f"  [{flags}]" if flags else ""))
        elif a.cmd == "draft-listings":
            print(f"Drafted listings for: {listing.draft_all(conn) or 'nothing waiting'}")
        elif a.cmd == "draft-scripts":
            print(f"Drafted scripts for: {video.draft_all(conn) or 'nothing waiting'}")
        elif a.cmd == "task":
            print(json.dumps(handoff.next_task(conn), indent=2))
        elif a.cmd == "submit":
            with open(a.file, encoding="utf-8") as f:
                raw = f.read()
            try:
                flags = handoff.submit(conn, a.stage, a.id, raw)
            except ValueError as e:
                print(e, file=sys.stderr)
                return 1
            print(f"Saved {a.stage} draft for product {a.id}; {len(flags)} compliance flag(s).")
        elif a.cmd == "review":
            text = review.render(conn)
            if a.out == "-":
                print(text)
            else:
                with open(a.out, "w", encoding="utf-8") as f:
                    f.write(text)
                print(f"Wrote {a.out}")
        elif a.cmd == "status":
            for p in store.all_products(conn):
                print(f"{p['id']:>4}  {p['status']:<18} {p['name']}")
        elif a.cmd in ("approve", "reject"):
            try:
                getattr(gates, a.cmd)(conn, a.id, a.gate, a.note)
            except gates.GateError as e:
                print(e, file=sys.stderr)
                return 1
            print(f"{'Approved' if a.cmd == 'approve' else 'Rejected'} product {a.id} at the {a.gate} gate.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
