-- I02: LEFT JOIN preserves customers who have no orders.
SELECT c.customer_id, c.customer_name
FROM customers AS c
LEFT JOIN orders AS o ON o.customer_id = c.customer_id
WHERE o.order_id IS NULL
ORDER BY c.customer_id;
