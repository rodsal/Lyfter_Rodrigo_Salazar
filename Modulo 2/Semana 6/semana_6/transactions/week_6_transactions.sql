
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address VARCHAR(255),
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    active BOOLEAN DEFAULT TRUE
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    category VARCHAR(50),
    creation_date TIMESTAMP,
    active BOOLEAN DEFAULT TRUE
);

CREATE TABLE invoices (
    invoice_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10, 2) NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    purchase_date TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);


CREATE OR REPLACE FUNCTION process_purchase(
    p_user_id INT,
    p_product_id INT,
    p_quantity INT,
    OUT p_result TEXT,
    OUT p_invoice_id INT
)
RETURNS RECORD
LANGUAGE plpgsql
AS $function$
DECLARE
    v_current_stock INT;
    v_price DECIMAL(10, 2);
    v_total DECIMAL(10, 2);
    v_user_exists INT;
    v_product_active BOOLEAN;
BEGIN

    SELECT COUNT(*) INTO v_user_exists
    FROM users
    WHERE user_id = p_user_id AND active = TRUE;
    
    IF v_user_exists = 0 THEN
        p_result := 'ERROR: User does not exist or is inactive';
        p_invoice_id := NULL;
        RETURN;
    END IF;
    

    SELECT stock, price, active
    INTO v_current_stock, v_price, v_product_active
    FROM products
    WHERE product_id = p_product_id
    FOR UPDATE; 
    
    IF v_price IS NULL THEN
        p_result := 'ERROR: Product does not exist';
        p_invoice_id := NULL;
        RETURN;
    END IF;
    
    IF v_product_active = FALSE THEN
        p_result := 'ERROR: Product is not available';
        p_invoice_id := NULL;
        RETURN;
    END IF;
    
    IF v_current_stock < p_quantity THEN
        p_result := 'ERROR: Insufficient stock. Available: ' || v_current_stock;
        p_invoice_id := NULL;
        RETURN;
    END IF;
    
    v_total := v_price * p_quantity;
    

    INSERT INTO invoices (user_id, product_id, quantity, unit_price, total)
    VALUES (p_user_id, p_product_id, p_quantity, v_price, v_total)
    RETURNING invoice_id INTO p_invoice_id;
    

    UPDATE products
    SET stock = stock - p_quantity
    WHERE product_id = p_product_id;
    
    p_result := 'SUCCESS: Purchase completed. Invoice #' || p_invoice_id || ' - Total: ₡' || v_total;
    
EXCEPTION
    WHEN OTHERS THEN
        p_result := 'ERROR: Transaction failed - ' || SQLERRM;
        p_invoice_id := NULL;
        RAISE;
END;
$function$;


CREATE OR REPLACE FUNCTION return_product(
    p_invoice_id INT,
    p_notes TEXT DEFAULT NULL,
    OUT p_result TEXT
)
RETURNS TEXT
LANGUAGE plpgsql
AS $function$
DECLARE
    v_invoice_exists INT;
    v_already_returned BOOLEAN;
    v_product_id INT;
    v_quantity INT;
BEGIN
  
    SELECT COUNT(*), MAX(returned), MAX(product_id), MAX(quantity)
    INTO v_invoice_exists, v_already_returned, v_product_id, v_quantity
    FROM invoices
    WHERE invoice_id = p_invoice_id
    FOR UPDATE; 
    
    IF v_invoice_exists = 0 THEN
        p_result := 'ERROR: Invoice does not exist';
        RETURN;
    END IF;
    
    IF v_already_returned = TRUE THEN
        p_result := 'ERROR: This invoice was already returned';
        RETURN;
    END IF;
    

    UPDATE products
    SET stock = stock + v_quantity
    WHERE product_id = v_product_id;
    

    UPDATE invoices
    SET returned = TRUE,
        return_date = CURRENT_TIMESTAMP,
        notes = COALESCE(p_notes, 'Product returned')
    WHERE invoice_id = p_invoice_id;
    
    p_result := 'SUCCESS: Product returned. Stock updated (+' || v_quantity || ' units)';
    
EXCEPTION
    WHEN OTHERS THEN
        p_result := 'ERROR: Return transaction failed - ' || SQLERRM;
        RAISE;
END;
$function$;
