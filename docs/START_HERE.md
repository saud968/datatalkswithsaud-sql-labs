# Start Here — Free SQL Labs

**Who:** Aspiring data analysts and BI developers who know basic tables and want reproducible practice.
**What you need:** Python 3.9+ for one-command validation; optionally a SQLite editor to run and edit SQL interactively.
**No account needed:** Everything runs on your own machine with the built-in SQLite library.

## The scenario

You're supporting a small fictional online store. The manager wants revenue by region and product, which customers haven't ordered, the latest order per buyer, and a trustworthy revenue trend.

But the raw data is messy in a business-rule sense: pending and cancelled orders are present, two customers have not ordered, and one **completed** order has no items. Your job is to produce explainable answers without changing the data to force desired totals.

## How to practice

1. Open [the exercise list](../exercises/README.md). Start with B01, then B02–B04.
2. Read the three CSV headers to understand their keys and their grain.
3. Write your solution **without** copying from `solutions/`.
4. Check the output shape and sort order against [expected results](../data/expected_results.json).
5. Only then inspect the relevant `solutions/*.sql` file, and explain why its joins and filters are correct.
6. Try I01–I04, then A01–A04. For advanced queries, draw out what each CTE contains before using a window function.
7. Run `python scripts/run_all.py` to verify all **supplied** solutions and fixtures.

## Data dictionary

| Table | Grain | Key | Important columns |
|---|---|---|---|
| `customers` | One row per customer | `customer_id` | `region`, `signup_date` |
| `orders` | One row per order | `order_id` | `customer_id`, `ordered_at`, `status` |
| `order_items` | One row per order item | `order_item_id` | `order_id`, `product`, `quantity`, `unit_price_inr` |

## Common mistakes

- `COUNT(*)` after joining orders to line items counts item rows, not unique orders.
- `WHERE o.status = 'completed'` after a `LEFT JOIN` to `orders` removes customers with no matching orders; place that condition inside `ON` when you want all customers.
- A sum of `quantity * unit_price_inr` over **all** statuses overstates completed revenue.
- Grouping raw order-item rows by day and then directly applying running totals without grouping to day grain causes multiple running-total rows per day.
- A completed order with no items is **not** evidence of zero earned revenue. Flag it for investigation.

## Validation and expected results

Running `scripts/run_all.py` reports each SQL file's passing result. Expected row values are in JSON and are checked in order, so queries use deterministic `ORDER BY` clauses. If you modify the dataset or rules, **do not simply edit expected results to make the tests pass**; explain the changed logic and revalidate independently.

## Using this in your portfolio

Explain the business question, show one query, describe join grain and status filters, and record one anomaly you found. Use the **synthetic** data only. No screenshots of employer, customer or proprietary systems.
