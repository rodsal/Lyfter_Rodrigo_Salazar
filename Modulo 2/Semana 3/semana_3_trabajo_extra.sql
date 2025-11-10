-- SQLite
--1. **Crear categorías y ajustar productos**
    -- Cree la tabla `categories` con: `id` (PK autoincrement), `name` (UNIQUE, NOT NULL), `description`
CREATE TABLE category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name NVARCHAR UNIQUE NOT NULL,
    category_description NVARCHAR
);

    -- Agregue a `products` la columna `category_id` (INTEGER, puede permitir NULL)
ALTER TABLE products
ADD category_id INT;

    -- Inserte al menos 3 filas en `categories`
INSERT INTO category(category_name, category_description)
    VALUES ('Electrónicos','Esta categoria contiene articulos con funcionamiento electrico');

    -- Actualice algunos `products` asignándoles un `category_id`

UPDATE products SET
    category_id = 5
WHERE id = 5;

    -- Verifique con `SELECT * FROM products` (muestre `id, product_name, price, quantity, category_id`)
SELECT id, name, price, quantity, category_id
FROM products;

--2. **Carga de productos y filtros básicos**
    -- Inserte al menos **10** filas en `products` con `product_name`, `price`, `quantity`
INSERT INTO products (code, name, price, date, brand, category_id, quantity)
	VALUES ('EIN9238913', 'iPhone 13 Pro Max', 380000, '5/8/2021', 'Apple', '5', '5');

    -- Seleccione todos los productos
SELECT *
FROM products;

    -- Seleccione productos con `price > 50000`
SELECT *
FROM products
WHERE price > 50000;

    -- Seleccione productos cuyo `product_name` contenga la palabra “apple” usando `LIKE`
SELECT *
FROM products 
WHERE product_name LIKE 'apple';

    -- Liste los **5** productos más caros con `ORDER BY price DESC LIMIT 5`
SELECT *
FROM products
ORDER BY price DESC
LIMIT 5;

--3. **Campos nuevos en facturas y actualización**
    -- Agregue a `invoices` las columnas `phone` (TEXT, puede ser NULL) y `cashier_code` (TEXT, por defecto `'N/A'`)
    -- ESTA MODIFICACION FUE HECHA EN EL EJERCICIO NUMERO 3 DEL EJERCICIO DE LA SEMANA

    -- Actualice varias facturas asignando valores a `phone` y `cashier_code`
UPDATE invoice SET
    buyer_phone = 86816446,
    cashier_code = 1984
WHERE id = 3;

    -- Seleccione todas las facturas que tengan `phone` vacío o NULL
SELECT * 
FROM invoice
WHERE buyer_phone Is NULL;

    -- Seleccione una sola factura por `invoice_id`
SELECT *
FROM invoice
WHERE id = 3;


--4. **Correcciones de datos en productos**
    -- Establezca `quantity = 0` donde `price <= 0`
UPDATE products SET
quantity = 0
WHERE price <= 0;


    -- Aumente el `price` en **100** unidades para todos los productos cuando `quantity` sea menor a 10
UPDATE products SET
price = price + 100 
WHERE quantity < 10;


    -- Disminuya `quantity` en **1** para un `product_id` específico
UPDATE products SET
quantity = quantity - 1 
WHERE id = 5;


    -- Verifique con `SELECT * FROM products ORDER BY id ASC LIMIT 10`
SELECT * 
FROM products
ORDER BY id ASC
LIMIT 10;
