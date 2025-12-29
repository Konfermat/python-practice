-- create table Authors (
-- 	AuthorID INTEGER PRIMARY key AUTOINCREMENT,
-- 	FirstName TEXT,
-- 	LastName TEXT
-- );
-- CREATE TABLE Books (
-- 	BookID INTEGER PRIMARY key AUTOINCREMENT,
-- 	Title TEXT,
-- 	AuthorID INTEGER,
-- 	Price REAL,
-- 	FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID) ON DELETE CASCADE
-- );

-- INSERT INTO Authors (FirstName, LastName) VALUES ('Марк', 'Твен');
-- INSERT INTO Authors (FirstName, LastName) VALUES ('Иван', 'Гончаров');

-- INSERT INTO BOOKS (Title, AuthorID, Price) VALUES ('Приключения Тома Соера', 1, 1.5);
-- INSERT INTO BOOKS (Title, AuthorID, Price) VALUES ('Обломов', 2, 2.1);
-- INSERT INTO BOOKS (Title, AuthorID, Price) VALUES ('Обычная история', 2, 1.9);

-- SELECT * from Authors;
-- SELECT * FROM Books;

-- DELETE FROM Books;
-- DELETE FROM Authors;

-- SELECT * FROM Books;
-- SELECT * FROM Authors;
