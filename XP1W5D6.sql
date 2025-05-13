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

-- 1. Get all languages
SELECT * FROM language;

-- 2. Get all films with their language
SELECT film.title, film.description, language.name AS language
FROM film
JOIN language ON film.language_id = language.language_id;

-- 3. Get all languages even if no films exist in them
SELECT film.title, film.description, language.name AS language
FROM language
LEFT JOIN film ON film.language_id = language.language_id;

-- 4. Create new_film table and insert sample films
CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

INSERT INTO new_film (name) VALUES
('The Programmer Strikes Back'),
('AI: The Final Frontier'),
('Debugging Day');

-- 5. Create customer_review table with ON DELETE CASCADE
CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INT REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INT REFERENCES language(language_id),
    title VARCHAR(255),
    score INT CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 6. Insert two reviews linked to new_film and language
INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES 
(1, 1, 'Excellent!', 9, 'Loved the storytelling and execution.'),
(2, 2, 'Could be better', 6, 'Interesting premise but poor execution.');

-- 7. Delete a film with reviews to test ON DELETE CASCADE
DELETE FROM new_film WHERE id = 1;

-- Check remaining reviews (should not include review for film_id = 1)
SELECT * FROM customer_review;