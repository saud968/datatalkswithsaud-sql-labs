-- I03: Top three products by completed-order revenue.
SELECT oi.product, SUM(oi.quantity * oi.unit_price_inr) AS revenue_inr
FROM order_items AS oi
JOIN orders AS o ON o.order_id = oi.order_id
WHERE o.status = 'completed'
GROUP BY oi.product
ORDER BY revenue_inr DESC, oi.product
LIMIT 3;
