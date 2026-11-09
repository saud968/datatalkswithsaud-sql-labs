-- A02: Include all registered customers, including those with zero completed revenue.
-- Filter completed orders inside a LEFT JOIN, not a WHERE clause.
WITH customer_sales AS (
    SELECT c.customer_id, c.customer_name,
           COALESCE(SUM(oi.quantity * oi.unit_price_inr), 0) AS revenue_inr
    FROM customers AS c
    LEFT JOIN orders AS o ON o.customer_id = c.customer_id AND o.status = 'completed'
    LEFT JOIN order_items AS oi ON oi.order_id = o.order_id
    GROUP BY c.customer_id, c.customer_name
)
SELECT customer_id, customer_name, revenue_inr,
       DENSE_RANK() OVER (ORDER BY revenue_inr DESC) AS revenue_rank
FROM customer_sales
ORDER BY revenue_rank, customer_id;
