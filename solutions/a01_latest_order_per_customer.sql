-- A01: One latest order per customer; deterministic tie-break on order_id.
WITH ranked AS (
    SELECT o.customer_id, o.order_id, o.ordered_at, o.status,
           ROW_NUMBER() OVER (PARTITION BY o.customer_id ORDER BY o.ordered_at DESC, o.order_id DESC) AS rn
    FROM orders AS o
)
SELECT customer_id, order_id, ordered_at, status
FROM ranked
WHERE rn = 1
ORDER BY customer_id;
