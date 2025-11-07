-- SQLite

--Limitaciones:
        -- 1. Cuando se usa el AUTOINCREMENT, no me deja setear el tamaño de la columna

-- 2. Replique las tablas creadas anteriormente en 
--@Ejercicios de Bases de Datos, con sus respectivos PKs, FKs, 
--constraints, y demás requerimientos.

CREATE TABLE products (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	code NVARCHAR NOT NULL,
	name NVARCHAR NOT NULL,
	price FLOAT DEFAULT 0,
	date DATETIME NOT NULL,
	brand VARCHAR NOT NULL
);

CREATE TABLE invoice (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_number INTEGER NOT NULL,
    purchase_date DATETIME NOT NULL,
    purchaser_email NVARCHAR NOT NULL,
    total FLOAT NOT NULL
);


CREATE TABLE products_invoice(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_factura INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad_comprada INT NOT NULL,
    total FLOAT NOT NULL
);

CREATE TABLE shopping_cart(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email NVARCHAR NOT NULL,
    cantidad INT NOT NULL
);

CREATE TABLE products_shopping_cart(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_product INT NOT NULL,
    id_shopping_cart INT NOT NULL 
);

INSERT INTO products (code, name, price, date, brand)
	VALUES ('H83774858SB', 'Jugo de Naranja', 1300.00, '5/9/2025', 'Florida Natural');

--3. Modifique la tabla de Facturas creada en el ejercicio anterior y 
--agregue una columna para almacenar también el número de teléfono del 
--comprador, y otra para el código de empleado del cajero que realizó la 
--venta.

ALTER TABLE invoice
	ADD buyer_phone INT;
ALTER TABLE invoice
    ADD employer_id INT;

INSERT INTO products (code, name, price, date, brand)
	VALUES ('UEY736728SA', 'Olla Arrocera', 1300000.00, '1/1/2024', 'Oster');

INSERT INTO invoice (invoice_number, purchase_date, buyer_email, total, buyer_phone, employer_id)
	VALUES ('362773673', '5/7/2025', 'comprador@gmail.com', 143000, 83840420, 6745);



--4. Realice los siguientes SELECT:

    --a. Obtenga todos los productos almacenados
SELECT *
FROM products;

SELECT *
FROM invoice;

    --b. Obtenga todos los productos que tengan un precio mayor a 50000
SELECT * 
FROM products
WHERE price > 50000

SELECT *
FROM products_invoice;

    --c. Obtenga todas las compras de un mismo producto por id.
SELECT *
FROM products_invoice
WHERE id_producto = 3;

    --d. Obtenga todas las compras agrupadas por producto, donde se muestre el 
    --total comprado entre todas las compras.
SELECT id_producto, COUNT(cantidad_comprada) as total_comprado, SUM (total) as total
FROM products_invoice
GROUP BY id_producto;

    --e. Obtenga todas las facturas realizadas por el mismo comprador
SELECT DISTINCT invoice_number
FROM invoice
WHERE buyer_email = 'rodrigo@gmail.com';


    --f. Obtenga todas las facturas ordenadas por monto total de forma descendente
SELECT *
FROM invoice
ORDER BY total DESC;


    --g. Obtenga una sola factura por número de factura.
SELECT *
FROM invoice
WHERE invoice_number = '92837823'

