-- SELECT * FROM train;
-- SELECT Name, Survived FROM train;
-- SQLLITE HAVE NO BOOL

-- SELECT NAME, age FROM train
-- WHERE Survived = 1 and age = 35
-- ORDER BY age, name
-- LIMIT 10;

-- ASC по возрастанию
-- DESC  по уббыванию
-- AND OR 
-- LIMIT

-- SELECT name as Name_female FROM train
-- where Pclass = 1 and sex='female';

-- SELECT NAME FROM train
-- WHERE sIBSP=0 AND Parch=0;

-- SELECT name, Pclass FROM train
-- where fare > 100;

-- select name, Pclass, age 
-- from train
-- WHERE Pclass !=1 and age > 18;

-- select Name, Pclass 
-- from train
-- where fare > 100 and Pclass;

-- select name from train
-- where name like 'William%';

-- BETWEEN
-- SELECT name, age from train
-- where age between 2 and 6;

-- IN (1 or 3 or 4)
-- select name, age from train
-- where age in (1, 5, 8);

-- like
-- %-любое кол-во символов
-- _-один символ

-- JOIN = join INNER
-- left JOIN
-- right JOIN
-- full join

-- JOIN INNER 
-- SELECT name, Survived from test 
-- join gender_submission
-- ON test.PassengerId = gender_submission.PassengerID
-- WHERE test.Pclass = 1;

-- pseudonames
-- SELECT name, Survived from test t
-- join gender_submission gs
-- ON t.PassengerId = gs.PassengerID
-- WHERE t.Pclass = 1;
-- 
-- RIGHT JOIN
-- LEFT JOIN - в основном он

-- SELECT name, Survived from test t
-- left join gender_submission gs
-- on t.PassengerId = gs.PassengerId;

-- id user 
-- id name user_id

-- Функции пагрегации 
-- count() - количество запсей
-- подпись негласное правило
-- SELECT count(*) as count_age FROM train;

-- бесполезный запрос
-- SELECT name, count(*) as count_passenger FROM train;

-- select name, age, count(*) as count_passenger FROM train
-- GROUP BY age;

-- max()
-- select name, max(age) as max_age from train
-- where Pclass = 1
-- group by name;

-- min()
-- avg()
-- в се они возвращают одно значение