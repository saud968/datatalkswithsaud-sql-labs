#!/usr/bin/env python3
"""Run all SQL lab solutions against an in-memory SQLite database; requires Python 3.9+."""
from pathlib import Path
import csv
import json
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = """
CREATE TABLE customers (
 customer_id TEXT PRIMARY KEY, customer_name TEXT NOT NULL, city TEXT NOT NULL,
 region TEXT NOT NULL, signup_date TEXT NOT NULL
);
CREATE TABLE orders (
 order_id TEXT PRIMARY KEY, customer_id TEXT NOT NULL REFERENCES customers(customer_id),
 ordered_at TEXT NOT NULL, status TEXT NOT NULL CHECK(status IN ('completed','cancelled','pending')),
 channel TEXT NOT NULL
);
CREATE TABLE order_items (
 order_item_id TEXT PRIMARY KEY, order_id TEXT NOT NULL REFERENCES orders(order_id),
 product TEXT NOT NULL, quantity INTEGER NOT NULL CHECK(quantity > 0),
 unit_price_inr INTEGER NOT NULL CHECK(unit_price_inr >= 0)
);
"""
TABLES = {
 'customers': ('customer_id','customer_name','city','region','signup_date'),
 'orders': ('order_id','customer_id','ordered_at','status','channel'),
 'order_items': ('order_item_id','order_id','product','quantity','unit_price_inr'),
}

def connect():
    conn = sqlite3.connect(':memory:')
    conn.execute('PRAGMA foreign_keys = ON')
    conn.executescript(SCHEMA)
    for table, fields in TABLES.items():
        with (ROOT / 'data' / (table + '.csv')).open(newline='', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            assert tuple(reader.fieldnames or []) == fields, f'{table}: invalid columns'
            rows = [tuple(int(row[k]) if k in ('quantity', 'unit_price_inr') else row[k] for k in fields) for row in reader]
        conn.executemany(f'INSERT INTO {table} VALUES ({",".join("?" for _ in fields)})',rows)
    return conn

def run_all():
    conn = connect()
    try:
        expected = json.loads((ROOT / 'data/expected_results.json').read_text(encoding='utf-8'))
        found = set()
        for file in sorted((ROOT / 'solutions').glob('*.sql')):
            statement = file.read_text(encoding='utf-8')
            # Educational safety: solutions are SELECT-only; no network, no external DB.
            rows = [list(row) for row in conn.execute(statement).fetchall()]
            assert file.name in expected, f'Missing expected result for {file.name}'
            assert rows == expected[file.name], f'FAIL {file.name}: expected={expected[file.name]!r}; actual={rows!r}'
            found.add(file.name)
            print(f'PASS {file.name}: {len(rows)} result rows')
        assert found == set(expected), 'Expected results contain unmatched exercise names'
        bad = conn.execute('PRAGMA foreign_key_check').fetchall()
        assert not bad, f'Foreign key failures: {bad}'
        print(f'\nSUCCESS: {len(found)} SQL solution checks matched expected results.')
    finally:
        conn.close()

if __name__ == '__main__':
    try: run_all()
    except Exception as exc:
        print(f'VALIDATION FAILED: {exc}',file=sys.stderr)
        sys.exit(1)
