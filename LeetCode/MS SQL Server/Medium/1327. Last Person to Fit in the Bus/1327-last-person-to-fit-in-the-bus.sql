/* Write your T-SQL query statement below */
with cte1 as
(
    select *, 
    -- aggregate weight by over for each row inclusively
    sum(weight) over(order by turn rows between unbounded preceding and current row) as floating_sum 
    from queue 
),
cte2 as
(
    select 
        person_name, 
        floating_sum, 
        dense_rank() over(order by floating_sum desc) as row_numb -- getting row number
    from cte1 
    where floating_sum <= 1000
)
select top 1 person_name from cte2 
order by row_numb asc