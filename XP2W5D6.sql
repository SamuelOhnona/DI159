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

-- 1. Update the language of some films to Spanish (language_id = 2)
UPDATE film
SET language_id = 2
WHERE film_id IN (1, 2, 3);

-- 2. Show foreign keys of the customer table
-- (run this manually in psql or view in pgAdmin)
-- \d customer

-- 3. Drop customer_review table
DROP TABLE IF EXISTS customer_review;

-- 4. Count how many rentals are outstanding (not returned yet)
SELECT COUNT(*) AS outstanding_rentals
FROM rental
WHERE return_date IS NULL;

-- 5. 30 most expensive movies still not returned
SELECT film.title, film.rental_rate
FROM rental
JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN film ON inventory.film_id = film.film_id
WHERE rental.return_date IS NULL
ORDER BY film.rental_rate DESC
LIMIT 30;

-- 6. Find the 4 films based on clues

-- 6.1. Sumo wrestler + Penelope Monroe
SELECT f.title
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE a.first_name = 'Penelope' AND a.last_name = 'Monroe'
AND (f.description ILIKE '%sumo%' OR f.title ILIKE '%sumo%');

-- 6.2. Short documentary (< 60min) rated 'R'
SELECT title
FROM film
WHERE rating = 'R'
AND length < 60
AND description ILIKE '%documentary%';

-- 6.3. Rented by Matthew Mahan, paid > 4$, returned between 28 Jul - 1 Aug 2005
SELECT f.title
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN payment p ON r.rental_id = p.rental_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
AND p.amount > 4.00
AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';

-- 6.4. Film watched by Matthew Mahan, includes "boat", expensive to replace
SELECT f.title, f.replacement_cost
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC;