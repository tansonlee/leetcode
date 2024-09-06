# Write your MySQL query statement below


with second_degree_follower as (
    select f1.f as follower
    from (
        -- users that follow someone
        select distinct follower as f
        from follow
    ) as f1
    inner join 
    (
        -- users that are followed by someone
        select distinct followee as f
        from follow
    ) as f2
    on f1.f = f2.f
)
select follower, 
       (select count(*) from follow where follow.followee = second_degree_follower.follower) as num
from second_degree_follower
order by follower;


