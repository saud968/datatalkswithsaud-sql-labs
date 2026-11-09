-- A04: Data quality exception: completed order with no item rows.
-- This should be flagged, not silently assigned a made-up amount.
SELECT o.order_id, o.customer_id, o.status
FROM orders AS o
LEFT JOIN order_items AS oi ON oi.order_id = o.order_id
WHERE o.status = 'completed'
GROUP BY o.order_id, o.customer_id, o.status
HAVING COUNT(oi.order_item_id) = 0
ORDER BY o.order_id;
