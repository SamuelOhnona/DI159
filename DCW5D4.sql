-- Database: bootcamp

-- DROP DATABASE IF EXISTS bootcamp;

CREATE DATABASE bootcamp
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
)

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar')

SELECT * FROM FirstTab

CREATE TABLE SecondTab (
    id integer 
)

INSERT INTO SecondTab VALUES
(5),
(NULL)


SELECT * FROM SecondTab


--Q1
SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )
--answer : SELECT id FROM SecondTab WHERE id IS NULL → returns only NULL.
--So the query becomes:
--WHERE ft.id NOT IN (NULL)
--In SQL, NOT IN (NULL) always returns unknown (i.e., FALSE) for any comparison because NULL is not a value.

--Prediction: 0
--Because comparing anything to NULL in a NOT IN clause results in UNKNOWN, no rows are matched.

--Q2
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id = 5);
--Assumption
--SELECT id FROM SecondTab WHERE id = 5 returns only 5.
--So the query becomes:
--WHERE ft.id NOT IN (5)
--Which will exclude the row with id = 5, and include the rest:

--id = 6

--id = 7

--id = NULL → but NULL NOT IN (5) is also unknown, so it's excluded!

--Prediction: 2 (only id = 6 and id = 7 are counted)

--Q3
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN (SELECT id FROM SecondTab);
--Assumption
--SELECT id FROM SecondTab returns (5, NULL)
--So we get: WHERE ft.id NOT IN (5, NULL)
--Any NOT IN that contains a NULL returns UNKNOWN for all comparisons → so no rows are matched.
--Prediction: 0
--Again, presence of NULL in a NOT IN makes the whole filter return no result.

--Q4
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id IS NOT NULL);
--Assumption
--SELECT id FROM SecondTab WHERE id IS NOT NULL returns only (5)
--So again: WHERE ft.id NOT IN (5)
--Just like in Q2.
--Prediction: 2 (only id = 6 and id = 7 are counted)