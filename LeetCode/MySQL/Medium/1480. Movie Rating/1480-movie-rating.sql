# Write your MySQL query statement below
(select U.name as 'results'
from MovieRating M left join Users U
on M.user_id = U.user_id
group by M.user_id
order by count(*) DESC, U.name
limit 1)
union all
(select M2.title as 'results'
from MovieRating M1 left join Movies M2
on M1.movie_id = M2.movie_id
where Year(M1.created_at) = '2020' and Month(M1.created_at) = '02'
group by M1.movie_id
order by avg(M1.rating) DESC, M2.title
limit 1);
