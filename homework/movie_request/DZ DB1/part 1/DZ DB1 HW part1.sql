-- task 1
select * from IMDB;
-- task 2
select Title, Rating from IMDB
WHERE Rating > 8
order by Rating DESC;
-- task 3
select distinct genre from genre;
-- task 4
select * FROM IMDB
WHERE Rating > 8.5;
-- task 5
select Title, cast(Runtime as INT) as rt FROM IMDB
where rt > 120
order by rt asc;