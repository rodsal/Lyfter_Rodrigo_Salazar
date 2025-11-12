-- SQLite

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL,
    author INT 
);

CREATE TABLE authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL
);

CREATE TABLE customer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL,
    email VARCHAR NOT NULL 
);

CREATE TABLE states (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    state VARCHAR NOT NULL
);

CREATE TABLE rents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INT NOT NULL,
    customer_id INT NOT NULL,
    state_id INT NOT NULL
);

--INSERT INTO books (name, author)
--    VALUES ('Don Quijote', 1);
--INSERT INTO books (name, author)
--    VALUES ('Vagabond 1-3', 3);
--INSERT INTO books (name, author)
--    VALUES ('Dragon Ball 1', 4);
--INSERT INTO books (name)
--    VALUES ('The Book of the 5 Rings');
--INSERT INTO books (name, author)
--    VALUES ('La Divina Comedia', 2);

--INSERT INTO authors (name)
--    VALUES ('Miguel de Cervantes');
--INSERT INTO authors (name)
--    VALUES ('Dante Alighieri');
--INSERT INTO authors (name)
--    VALUES ('Takehiko Inoue');
--INSERT INTO authors (name)
--    VALUES ('Akira Toriyama');
--INSERT INTO authors (name)
--    VALUES ('Walt Disney');

--INSERT INTO customer (name, email)
--    VALUES ('John Doe', 'j.doe@email.com');
--INSERT INTO customer (name, email)
--    VALUES ('Jane Doe', 'jane@doe.com');
--INSERT INTO customer (name, email)
--    VALUES ('Luke Skywalker', 'darth.son@email.com');

--INSERT INTO states (state)
--    VALUES ('Returned');
--INSERT INTO states (state)
--    VALUES ('On Time');
--INSERT INTO states (state)
--    VALUES ('Overdue');

--INSERT INTO rents (book_id, customer_id,state_id)
--    VALUES (1,2,1);
--INSERT INTO rents (book_id, customer_id,state_id)
--    VALUES (2,2,1);
--INSERT INTO rents (book_id, customer_id,state_id)
--    VALUES (1,1,2);
--INSERT INTO rents (book_id, customer_id,state_id)
--    VALUES (3,1,2);
--INSERT INTO rents (book_id, customer_id,state_id)
--    VALUES (2,2,3);

    --1. Obtenga todos los libros y sus autores
SELECT books.name as BookName, authors.name as AuthorName
FROM books
LEFT JOIN authors as authors
ON authors.id = books.author;

    --2. Obtenga todos los libros que no tienen autor
SELECT name, author
FROM books
WHERE author IS NULL;

    --3. Obtenga todos los autores que no tienen libros
SELECT authors.name as Author, books.name as Book
FROM authors
LEFT JOIN books
ON authors.id = books.author
WHERE books.name IS NULL;

    --4. Obtenga todos los libros que han sido rentados en algún momento
SELECT rents.id as rentid, books.name as book
FROM books
INNER JOIN rents
ON books.id = rents.book_id;

    --5. Obtenga todos los libros que nunca han sido rentados
SELECT books.name as book, rents.id
FROM books
LEFT JOIN rents
ON books.id = rents.book_id
WHERE rents.id  IS NULL;

    --6. Obtenga todos los clientes que nunca han rentado un libro
SELECT customer.name as customer, rents.id
FROM customer
LEFT JOIN rents
ON customer.id = rents.customer_id
WHERE rents.id  IS NULL;

    --7. Obtenga todos los libros que han sido rentados y están en estado “Overdue”
SELECT rents.id as rentid, books.name as book, states.state as state
FROM books
INNER JOIN rents
ON books.id = rents.book_id
INNER JOIN states
ON states.id = rents.state_id
WHERE states.state = 'Overdue';

