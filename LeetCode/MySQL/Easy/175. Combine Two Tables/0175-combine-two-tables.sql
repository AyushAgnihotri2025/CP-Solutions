# Write your MySQL query statement below
select p.firstName , p.lastName, a.city , a.state
    from Person p LEFT JOIN Address a USING(personId)