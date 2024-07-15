-- CREATE DATABASE fishbread_db;
-- USE fishbread_db;
-- CREATE TABLE USERS(
	-- user_id INT AUTO_INCREMENT PRIMARY KEY,
    -- username VARCHAR(255) NOT NULL,
    -- age INT NOT NULL,
    -- email VARCHAR(100) UNIQUE,
    -- is_business VARCHAR(10)
-- );

-- CREATE TABLE ORDERS(
	-- order_id INT AUTO_INCREMENT PRIMARY KEY,
    -- user_id INT,
    -- order_date DATE,
    -- amount DECIMAL(10,2),                 
	-- FOREIGN KEY(user_id) REFERENCES USERS(user_id)
-- );

-- CREATE TABLE INVERTORY(
	-- item_id INT AUTO_INCREMENT PRIMARY KEY,
    -- item_name VARCHAR(255) NOT NULL,
    -- quantity INT NOT NULL
-- );
-- CREATE TABLE SALES(
	-- sale_id INT AUTO_INCREMENT PRIMARY KEY,
    -- order_id INT,
    -- item_id INT,
    -- quantity_sold INT NOT NULL,
    -- FOREIGN KEY(order_id) REFERENCES ORDERS(order_id),
    -- FOREIGN KEY(item_id) REFERENCES INVERTORY(item_id)
-- );
-- CREATE TABLE DAILY_SALES(
	-- date DATE PRIMARY KEY,
    -- total_sales DECIMAL(10,2) NOT NULL
-- ); 



