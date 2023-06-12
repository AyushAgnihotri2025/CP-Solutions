# Write your MySQL query statement below
select query_name, 
ROUND(AVG(rating / position), 2) AS quality,
round(SUM(rating<3)/count(query_name)*100,2) as poor_query_percentage 
from queries
group by query_name;