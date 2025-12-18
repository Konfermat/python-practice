
--inner JOIN
-- выводит на соответствие записи 
-- select e.full_name, c.email, c.phone_number
-- from Employees as e 
-- join Contacts as c
-- on E.contact_id = C.contact_id

-- left JOIN
-- получим все 12 записей не смотря на отсутсвие
-- select e.full_name, c.email
-- from Employees as e 
-- left join Contacts as c
-- on E.contact_id = C.contact_id;

-- left JOIN
-- меняем местами Contacts и Employees
-- select e.full_name, c.email
-- from Contacts as e 
-- left join Employees as c
-- on E.contact_id = C.contact_id;

-- HAVING и WHERE оба фильтруют
-- WHERE на уровне строк
-- HAVING во время результата

-- Порядок выполнения операций
-- FROM, JOIN, WHERE, GROUP BY, 
-- Агрегации, HAVING, ORDER BY

-- ЗАДАНИЕ
-- Узнать в каком отделе работает более
-- двух сотрудников
--
-- select d.department_name, count(e.employee_id)
-- as employee_count from Departments as d
-- join Employees as e
-- on d.department_id = e.department_id
-- group by d.department_name
-- having count(e.employee_id) >= 2;

--ЗАДАНИЕ
-- найти проекты в которых участвуют сотрудники
-- принятые на работу после 2022г и общее 
-- кол-тво таких сотрудников в проекте больше
-- одного
--
-- select p.project_name, count(e.employee_id)
-- as count_emp_project from Projects as p
-- join ProjectAssignments as pa
-- on p.project_id = pa.project_id
-- join Employees as e
-- on pa.employee_id = e.employee_id
-- where e.hire_date > '2020-12-31'
-- group by p.project_name
-- having count(e.employee_id) > 1;

-- ЗАДАНИЕ 1 Эффективность отделов
--
-- определить отделы которые активно
-- участвуют в двух проектах
-- находящиеся в статусе active
-- и имеет более двух сотрудников
-- select d.department_name, count(DISTINCT p.project_id) as active_projects_count
-- from departments as d
-- join Employees as e on d.department_id = e.department_id
-- join ProjectAssignments as pa on e.employee_id = pa.employee_id
-- join Projects as p on pa.project_id = p.project_id
-- where p.status = 'Active'
-- group by d.department_name
-- having count(e.employee_id) > 2
-- order by active_projects_count desc;1

--ЗАДАНИЕ 2
--
-- select e.full_name, e.hire_date
-- from Employees as e
-- left join Contacts as c on e.contact_id = c.contact_id
-- where c.email is NULL
-- and (e.full_name like 'B%' or e.full_name like 'E%')
-- and e.hire_date <= '2025-01-01'

-- НОВАЯ ТЕМА
-- ПОДЗАПРОСЫ
-- where для фильтрации строк внешних запросов
-- скалярный подзапрос (один запрос) после where
-- найти всех сотрудников, работающих в отделе
-- основанном после 2015 

-- select DISTINCT d.department_name, e.full_name
-- from Employees as e
-- join Departments as d
-- -- условие
-- on e.department_id = d.department_id
-- where d.department_id in
-- (select department_id from Departments
-- where foundation_year > 2015);

-- найти среднее кол-во задач на один проект
-- для проектов в статусе active
-- вывести только те проекты
-- в котрых задач больше чем это среднее
--
-- select T1.project_name, T1.task_count FROM
-- (select p.project_name, count(t.task_id) as task_count
-- from Projects as p join Tasks as t
-- on p.project_id = t.project_id
-- where p.status = 'Active'
-- group by p.project_name) as T1
-- where T1.task_count > 
-- (select avg(task_count) from (
-- select count(t.task_id) as task_count
-- from Projects as p join Tasks as t
-- on p.project_id = t.project_id
-- where p.status = 'Active'
-- ));



