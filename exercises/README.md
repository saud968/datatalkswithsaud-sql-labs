# SQL exercises — attempt before opening `solutions/`

All queries use the CSVs in `data/`, loaded into SQLite by `scripts/run_all.py`. **Do not count revenue on cancelled or pending orders.** Sort results in a predictable way so they match `data/expected_results.json`.

## Beginner (B01–B04)

**B01 — Customer count.** How many registered customers exist? Return one row called `customer_count`.

**B02 — Orders by status.** How many orders are `completed`, `cancelled`, and `pending`? Return `status`, `order_count` in status alphabetical order.

**B03 — October completed orders.** Return `order_id`, `customer_id`, `order_date` (date only) for orders completed during October 2026. Sort by date then order ID.

**B04 — Customers by region.** Return `region`, `customer_count` sorted alphabetically.

## Intermediate (I01–I04)

**I01 — Completed revenue by region.** Join `customers → orders → order_items`, calculate revenue using item quantity × unit price, and filter to completed orders. Return `region`, `revenue_inr` sorted by revenue descending then region.

**I02 — Customers without orders.** Find customers with no matching rows in `orders`. Return `customer_id`, `customer_name` ordered by ID. Explain why an `INNER JOIN` would fail.

**I03 — Top three products.** Calculate completed-order revenue by product. Return `product`, `revenue_inr`, sorted by revenue descending (product alphabetical tie-break), limited to three results.

**I04 — Repeat completed buyers.** Return customers with two or more completed orders: `customer_id`, `customer_name`, `completed_orders`. Sort by completed order count descending then customer ID. Count **orders**, not order items.

## Advanced (A01–A04)

**A01 — Latest order per customer.** Use `ROW_NUMBER` to return each ordering customer's latest order, including its status: `customer_id`, `order_id`, `ordered_at`, `status`. Break ties with order ID descending. Sort by customer ID.

**A02 — Revenue ranking.** Include **all registered customers**, even those with no completed revenue. Calculate completed-order revenue and assign `DENSE_RANK` by revenue descending. Return `customer_id`, `customer_name`, `revenue_inr`, `revenue_rank`. Sort by rank then ID.

**A03 — Running daily revenue.** First aggregate completed-order revenue by calendar date, then calculate a cumulative sum using a window function. Return `order_date`, `daily_revenue_inr`, `running_revenue_inr` in date order.

**A04 — Data-quality exception.** Find `completed` orders that have **no** order-item rows. Return `order_id`, `customer_id`, `status`. Explain why silently treating these as zero-value purchases can mislead a stakeholder.

## Before checking answers

For each query, write down the grain, inclusion rules, joins, filter order and expected result shape. Compare against [expected output](../data/expected_results.json). Read [guided troubleshooting](../docs/START_HERE.md) if your totals disagree.
