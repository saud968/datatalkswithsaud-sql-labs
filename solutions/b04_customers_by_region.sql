-- B04: Count registered customers by region.
SELECT region, COUNT(*) AS customer_count
FROM customers
GROUP BY region
ORDER BY region;
