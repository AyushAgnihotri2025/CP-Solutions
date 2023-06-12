# Write your MySQL query statement below
SELECT name AS Employee
FROM Employee Table2
WHERE salary > (
    SELECT salary 
    FROM Employee
    WHERE id = Table2.managerId
)