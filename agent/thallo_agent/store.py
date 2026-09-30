"""One SQLite row per product; each stage writes its output into that row."""

import json
import sqlite3
from contextlib import contextmanager

from . import config

SCHEMA = """
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    category TEXT,
    price REAL,
    cost REAL,
    units_sold INTEGER,
    growth_pct REAL,
    source_url TEXT,
    score REAL,
    score_detail TEXT,
    status TEXT NOT NULL,
    listing TEXT,
    scripts TEXT,
    notes TEXT,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
);
"""

JSON_FIELDS = ("score_detail", "listing", "scripts", "notes")


@contextmanager
def connect(path: str | None = None):
    conn = sqlite3.connect(path or config.DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def _row(r: sqlite3.Row | None) -> dict | None:
    if r is None:
        return None
    d = dict(r)
    for f in JSON_FIELDS:
        if d.get(f):
            d[f] = json.loads(d[f])
    return d


def upsert_candidate(conn, c: dict) -> None:
    """Insert a new candidate, or refresh numbers on one still waiting at gate 1."""
    conn.execute(
        """INSERT INTO products (name, category, price, cost, units_sold, growth_pct, source_url,
                                 score, score_detail, status)
           VALUES (:name, :category, :price, :cost, :units_sold, :growth_pct, :source_url,
                   :score, :score_detail, 'discovered')
           ON CONFLICT(name) DO UPDATE SET
               category=excluded.category, price=excluded.price, cost=excluded.cost,
               units_sold=excluded.units_sold, growth_pct=excluded.growth_pct,
               source_url=excluded.source_url, score=excluded.score,
               score_detail=excluded.score_detail, updated_at=CURRENT_TIMESTAMP
           WHERE products.status = 'discovered'""",
        {**c, "score_detail": json.dumps(c["score_detail"])},
    )


def get(conn, product_id: int) -> dict | None:
    return _row(conn.execute("SELECT * FROM products WHERE id = ?", (product_id,)).fetchone())


def by_status(conn, status: str) -> list[dict]:
    rows = conn.execute("SELECT * FROM products WHERE status = ? ORDER BY score DESC", (status,)).fetchall()
    return [_row(r) for r in rows]


def all_products(conn) -> list[dict]:
    return [_row(r) for r in conn.execute("SELECT * FROM products ORDER BY id").fetchall()]


def update(conn, product_id: int, **fields) -> None:
    for f in JSON_FIELDS:
        if f in fields and fields[f] is not None:
            fields[f] = json.dumps(fields[f])
    sets = ", ".join(f"{k} = :{k}" for k in fields)
    conn.execute(f"UPDATE products SET {sets}, updated_at = CURRENT_TIMESTAMP WHERE id = :id",
                 {**fields, "id": product_id})
