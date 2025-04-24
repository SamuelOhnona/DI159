-- Database: dvdrental

-- DROP DATABASE IF EXISTS dvdrental;

CREATE DATABASE dvdrental
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

-- 1. All columns from the “customer” table
SELECT * FROM customer;

-- 2. Display full name with alias “full_name”
SELECT first_name || ' ' || last_name AS full_name
FROM customer;

-- 3. Get all unique account creation dates
SELECT DISTINCT create_date
FROM customer;

-- 4. All customer details ordered by first name (descending)
SELECT * FROM customer
ORDER BY first_name DESC;

-- 5. Film ID, title, description, release year, rental rate (ascending by rental rate)
SELECT film_id, title, description, release_year, rental_rate
FROM film
ORDER BY rental_rate ASC;

-- 6. Address + phone of customers in the Texas district
SELECT address, phone
FROM address
WHERE district = 'Texas';

-- 7. All movie details where movie_id is 15 or 150
SELECT *
FROM film
WHERE film_id IN (15, 150);

-- 8. Check if your favorite movie exists (replace 'Inception' with your choice)
SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title = 'Inception';

-- 9. Movies starting with the first 2 letters of the title (replace 'In' accordingly)
SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title ILIKE 'In%';

-- 10. The 10 cheapest movies
SELECT *
FROM film
ORDER BY rental_rate ASC
LIMIT 10;

-- 11. The next 10 cheapest movies (without using LIMIT directly)
SELECT *
FROM (
    SELECT *, ROW_NUMBER() OVER (ORDER BY rental_rate ASC) AS row_num
    FROM film
) AS ranked
WHERE row_num BETWEEN 11 AND 20;

-- 12. Join customer and payment (first name, last name, amount, payment date), ordered by customer id
SELECT c.first_name, c.last_name, p.amount, p.payment_date
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY c.customer_id ASC;

-- 13. Movies not in inventory
SELECT *
FROM film
WHERE film_id NOT IN (
    SELECT film_id FROM inventory
);