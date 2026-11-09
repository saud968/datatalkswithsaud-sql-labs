# DataTalksWithSaud — SQL Labs

**Free, runnable SQL practice with synthetic e-commerce data and independently verifiable answers.**

Learn SQL by solving genuine reporting and data-quality questions. No paid database, cloud warehouse, login, or special Python package required: this project uses **Python's built-in SQLite** engine.

> **Start here:** [Beginner guide](docs/START_HERE.md) · [Exercises](exercises/README.md) · [Expected output](data/expected_results.json)

## What you'll learn

| Level | Practice | Skills |
|---|---|---|
| Beginner | B01–B04 | `SELECT`, `COUNT`, `WHERE`, date filtering, `GROUP BY` |
| Intermediate | I01–I04 | `JOIN`, `LEFT JOIN`, `SUM`, `HAVING`, top products |
| Advanced | A01–A04 | `ROW_NUMBER`, `DENSE_RANK`, running totals, missing-order-item audits |

## Why this lab matters

The scenario uses three connected datasets: **12 customers, 34 orders, and order items**. Some orders are cancelled or pending, two customers have no orders, and **one completed order has no line items**. This creates realistic questions about join grain, inclusion rules, and when a number should not be trusted.

- **Revenue rule:** Include item-level revenue **only on completed orders**. Pending and cancelled orders are excluded.
- **Order-item grain:** One order can have several line items. Count orders using their unique ID, not joined rows.
- **Data-quality rule:** A completed order with no line items is an exception. Do not invent a price or assume that it was a genuine zero-value purchase.
- All names and transactions are **fictional**, independently written educational examples—not client data.

## Quick start

1. Download the repository (green **Code → Download ZIP**) and unzip it.
2. Open a command prompt or terminal in the project folder.
3. Run `python scripts/run_all.py` (or `python3 scripts/run_all.py`).
4. You should see **12 PASS checks**. The script loads three CSVs into an **in-memory** SQLite database, runs the solution queries, and compares outputs with the published expected-results fixture.
5. Optionally run `python scripts/audit_source.py` to verify key business-rule totals directly from CSVs without executing the SQL queries.
6. Try each challenge in [exercises/README.md](exercises/README.md) without looking at `solutions/`, then compare your SQL and results.

A successful validation checks **the supplied SQL and data**, not whether a learner independently understands the solution. Run and modify the queries in a SQLite-compatible editor to experiment. Python 3.9+ is recommended; SQLite needs window-function support (3.25+).

## Repository contents

```text
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── data/
│   ├── customers.csv
│   ├── orders.csv
│   ├── order_items.csv
│   └── expected_results.json
├── docs/START_HERE.md
├── exercises/README.md
├── solutions/              # 12 executable .sql files
├── scripts/
│   ├── run_all.py          # Self-contained SQLite validator
│   └── audit_source.py     # Independent raw-CSV cross-check
└── .github/workflows/validate.yml
```

## SQL compatibility

The solutions have been **executed using Python's SQLite**. They are not claimed to be tested in Snowflake, SQL Server, PostgreSQL, or MySQL. Some syntax (such as `DATE()` or `LIMIT`) must be adapted for those engines. A separate, tested dialect-specific edition may be added later.

## More free DataTalksWithSaud learning projects

- **[Power BI Labs — Sales Data Quality Challenge](https://github.com/saud968/datatalkswithsaud-powerbi-labs)**: work with messy synthetic sales data, document exclusions, and reconcile report totals.
- **[All learning projects](https://github.com/saud968)**: visit the author's GitHub profile for new free exercises.

## Share and contribute

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing changes. Open an issue with a reproducible query/error and expected result. No private company data, credentials, client SQL, or paid course files.

Created by **DataTalksWithSaud** · [Saud's GitHub](https://github.com/saud968) · [Topmate](https://topmate.io/saud_ansari) · [LinkedIn](https://www.linkedin.com/in/saud-ansari968/)

Released under the MIT license. No endorsement by SQLite or any cloud data platform is implied.
