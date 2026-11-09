-- B03: List completed orders placed in October 2026.
SELECT order_id, customer_id, DATE(ordered_at) AS order_date
FROM orders
WHERE status = 'completed' AND ordered_at >= '2026-10-01' AND ordered_at < '2026-11-01'
ORDER BY order_date, order_id;
