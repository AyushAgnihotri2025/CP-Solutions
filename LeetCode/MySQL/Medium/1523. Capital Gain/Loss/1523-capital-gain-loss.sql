# Write your MySQL query statement below
select stock_name,sum(if(operation='Sell',price,-price)) as capital_gain_loss from stocks group by stock_name;