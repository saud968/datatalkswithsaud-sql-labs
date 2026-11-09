-- B02: Count orders by status. Do not mistake a placed order for revenue.
SELECT status, COUNT(*) AS order_count
FROM orders
GROUP BY status
ORDER BY status;
