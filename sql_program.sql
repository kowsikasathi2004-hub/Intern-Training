DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS branch;

CREATE TABLE branch (
    branch_id INT PRIMARY KEY,
    branch_name VARCHAR(50) NOT NULL,\
	address VARCHAR(200)
	);

CREATE TABLE product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2),
    category_id INT,
    FOREIGN KEY(category_id)
    REFERENCES category(category_id)
);

INSERT INTO category VALUES
(1,'Electronics'),
(2,'Clothing'),
(3,'Books');

INSERT INTO product VALUES
(101,'Laptop',65000,1),
(102,'Smartphone',25000,1),
(103,'T-Shirt',800,2),
(104,'Python Book',500,3);

SELECT * FROM category;
SELECT * FROM product;

SELECT
    p.product_id,
    p.product_name,
    p.price,
    c.category_name
FROM product p
JOIN category c
ON p.category_id = c.category_id

