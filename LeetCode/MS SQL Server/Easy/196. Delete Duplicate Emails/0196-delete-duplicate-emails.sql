/* 
 Please write a DELETE statement and DO NOT write a SELECT statement.
 Write your T-SQL query statement below
 */
DELETE FROM PERSON
WHERE ID NOT IN(SELECT MIN(ID) FROM PERSON GROUP BY EMAIL)