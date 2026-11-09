-- A03: First aggregate to day grain, then calculate a cumulative sum.
WITH daily_revenue AS (
    SELECT DATE(o.ordered_at) AS order_date,
           SUM(oi.quantity * oi.unit_price_inr) AS daily_revenue_inr
    FROM orders AS o
    JOIN order_items AS oi ON oi.order_id = o.order_id
    WHERE o.status = 'completed'
    GROUP BY DATE(o.ordered_at)
)
SELECT order_date, daily_revenue_inr,
       SUM(daily_revenue_inr) OVER (
           ORDER BY order_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_revenue_inr
FROM daily_revenue
ORDER BY order_date;
