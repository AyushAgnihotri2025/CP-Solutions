/* Write your PL/SQL query statement below */
with cte as (
    select visited_on, sum(amount) as amount from Customer
    group by visited_on
)
select to_char(visited_on) as visited_on, amount, round(average_amount,2) as average_amount from (
    select visited_on,
    sum(amount) over (order by visited_on rows between 6 preceding and current row) amount,
    avg(amount) over (order by visited_on rows between 6 preceding and current row) average_amount,
    rank() over (order by visited_on) rnk
        from cte
) where rnk >= 7