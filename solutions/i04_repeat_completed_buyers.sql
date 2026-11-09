-- I04: Only customers with at least two completed orders.
SELECT c.customer_id, c.customer_name, COUNT(*) AS completed_orders
FROM customers AS c
JOIN orders AS o ON o.customer_id = c.customer_id
WHERE o.status = 'completed'
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(*) >= 2
ORDER BY completed_orders DESC, c.customer_id;
