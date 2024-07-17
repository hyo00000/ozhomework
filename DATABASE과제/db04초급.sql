USE classicmodels;
-- 생성(CREATE-초급)
INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit)
VALUES (123 ,'kimhyoyoung', 'hyoyoung', 'kim', '010-1234-5678', '123 Street', 'Suite 1', 'City', 'State', 'PostalCode', 'Country', 1002, 50000.00);

INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityinStock, buyPrice, MSRP)
VALUES ('S12_1234', '1972chevrolet', 'Classic Cars', '1:12', 'Second Gear Diecast', 'open door', 3618, 77.00, 123);

INSERT INTO employees (employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle)
VALUES (1234, 'hyoyoung', 'kim', 'x1234', 'hyo@classicmodelcars.com', 1, 1143, 'President'); 

INSERT INTO offices (officeCode, city, phone, addressLine1, addressLine2, state, country, postalCode, territory)
VALUES (8, 'Seoul', '+82 1012345678', '42 kyunghigil street', 'Level 3', 'Seoul', 'Korea', 1234, 'Asia');

INSERT INTO orders(orderNumber, orderDate, requiredDate, shippedDate, status, comments, customerNumber)
VALUES (10426, '2003-03-24', '2003-05-20', '2003-06-26', 'shipped', 'Check on availability.', 123);

INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber)
VALUES (10101, 'S10_4757', 27, 42.12, 2);

INSERT INTO payments (customerNumber, checkNumber, paymentDate, amount)
VALUES (123, 'HQ55023', '2004-08-20', 3455.00);

INSERT INTO productlines (productLine, textDescription, htmlDescription, image)
VALUES ('Classic Bicycle', 'Various classic cars models', null, null);

INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit)
VALUES (126 ,'ozcoding', 'coding', 'oz', '010-4321-5678', '124 Street', 'Suite 2', 'City', 'State', 'PostalCode', 'Country', 1002, 50000.00);

INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityinStock, buyPrice, MSRP)
VALUES ('S12_1236', '1975Ray', 'Classic Cars', '1:12', 'Second Gear Diecast', 'open door', 3638, 86.00, 126);

-- 읽기(READ-초급)
SELECT * FROM customers;
SELECT * FROM products;
SELECT * FROM employees;
SELECT * FROM offices;
SELECT * FROM orders;
SELECT * FROM orderdetails;
SELECT * FROM payments;
SELECT * FROM productlines;
SELECT * FROM customers WHERE city = 'Paris';
SELECT * FROM products WHERE buyPrice = 93.89;

-- 갱신(UPDATE-초급)
UPDATE customers SET addressLine1 = '128 street' WHERE customerNumber = 126;
UPDATE products SET buyprice = 100.00 WHERE productCode = 'S10_1678'; 
UPDATE employees SET jobTitle = 'President' WHERE employeeNumber = 1188; 
SET SQL_SAFE_UPDATES =0;
UPDATE offices SET phone = '+82 1098765432' WHERE city = 'sydney'; 
UPDATE orders SET status = 'Cancelled' WHERE OrderNumber = 10104; 
UPDATE orderdetails SET quantityOrdered = 65 WHERE productCode ='S 24_1937'; 
UPDATE payments SET amount = '1280.00' WHERE checkNumber = 'DB933704'; 
UPDATE productlines SET textDescription = 'cheap and good price'  WHERE productLine = 'Planes'; 
UPDATE customers SET email = 'john_updated@email.com' WHERE customerNumber = 128;
UPDATE products SET buyPrice = 100000.00 WHERE productCode = 'S10_4757';  

-- 삭제(DELETE-초급)
DELETE FROM customers WHERE customerNumber =126;
SET foreign_key_checks = 0;
DELETE FROM products WHERE productCode = 'S10_2016'; 
DELETE FROM employees WHERE employeeNumber = 1188;
DELETE FROM offices WHERE city = 'sydney'; 
DELETE FROM orders WHERE orderNumber = 10104; 
DELETE FROM orderdetails WHERE productCode ='S 24_1937'; 
DELETE FROM payments WHERE checkNumber = 'DB933704'; 
DELETE FROM productlines WHERE productLine = 'Planes';
DELETE FROM customers WHERE city = 'Melbourne';
DELETE FROM products WHERE productLine = 'Motorcycles';
