-- I01: Revenue is at order-item grain and completed orders only.
SELECT c.region, SUM(oi.quantity * oi.unit_price_inr) AS revenue_inr
FROM customers AS c
JOIN orders AS o ON o.customer_id = c.customer_id
JOIN order_items AS oi ON oi.order_id = o.order_id
WHERE o.status = 'completed'
GROUP BY c.region
ORDER BY revenue_inr DESC, c.region;
