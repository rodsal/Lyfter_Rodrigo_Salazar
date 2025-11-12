-- SQLite
    --2. **Agrupamiento y conteo cruzado**
        --- Usando las tablas de `Books`, `Customers` y `Rents`:
            --- Obtenga el número total de veces que cada cliente ha rentado un libro
SELECT customer.name, COUNT(*) as amountrented
FROM customer 
INNER JOIN rents
ON customer.id = rents.customer_id
GROUP BY customer.name;


            --- Ordene de mayor a menor y limite el resultado a los **3 clientes más activos**
SELECT customer.name, COUNT(*) as amountrented
FROM customer 
INNER JOIN rents
ON customer.id = rents.customer_id
GROUP BY customer.name
ORDER BY amountrented DESC
LIMIT 3;

        --- *Debe usar:* `GROUP BY`, `COUNT()`, `ORDER BY`, `LIMIT`
        
    --3. **Consulta con múltiples JOINS anidados**
        --- Genere un `SELECT` que devuelva lo siguiente:
            --- Nombre del cliente
            --- Nombre del libro
            --- Nombre del autor
            --- Estado del alquiler (`Rents.State`)
        --- *Debe manejar el caso en que un libro no tenga autor*
SELECT customer.name as Customer, books.name as Book, authors.name as Author, states.state as Sate
FROM rents
INNER JOIN customer ON customer.id = rents.customer_id
INNER JOIN books ON books.id = rents.book_id
INNER JOIN authors ON authors.id = books.author
INNER JOIN states ON states.id = rents.state_id;