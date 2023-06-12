# Write your MySQL query statement below
SELECT p.product_name, SUM(o.unit) AS unit
FROM
Products p
INNER JOIN Orders o
ON p.product_id=o.product_id
WHERE 
 o.order_date>='2020-02-01'
AND o.order_date <'2020-03-01'
GROUP BY p.product_name
HAVING SUM(o.unit)>=100