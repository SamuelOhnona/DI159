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

-- Create the students table with appropriate columns and data types
CREATE TABLE students (
    id SERIAL PRIMARY KEY,         -- Auto-incrementing ID
    first_name VARCHAR(50),        -- Student's first name
    last_name VARCHAR(50),         -- Student's last name
    birth_date DATE                -- Student's date of birth
);

-- Insert student records into the students table
-- Dates are formatted using TO_DATE with 'DD/MM/YYYY'
INSERT INTO students (first_name, last_name, birth_date) VALUES
('Marc', 'Benichou', TO_DATE('02/11/1998', 'DD/MM/YYYY')),
('Yoan', 'Cohen', TO_DATE('03/12/2010', 'DD/MM/YYYY')),
('Lea', 'Benichou', TO_DATE('27/07/1987', 'DD/MM/YYYY')),
('Amelia', 'Dux', TO_DATE('07/04/1996', 'DD/MM/YYYY')),
('David', 'Grez', TO_DATE('14/06/2003', 'DD/MM/YYYY')),
('Omer', 'Simpson', TO_DATE('03/10/1980', 'DD/MM/YYYY')),

('Samuel', 'Ohnona', TO_DATE('15/08/1999', 'DD/MM/YYYY'));

-- 1. Select all students
SELECT * FROM students;

-- 2. Select only first names and last names
SELECT first_name, last_name FROM students;

-- 3. Select the student with ID = 2
SELECT first_name, last_name FROM students WHERE id = 2;

-- 4. Select the student named Marc Benichou
SELECT first_name, last_name FROM students 
WHERE last_name = 'Benichou' AND first_name = 'Marc';

-- 5. Select students with last name Benichou OR first name Marc
SELECT first_name, last_name FROM students 
WHERE last_name = 'Benichou' OR first_name = 'Marc';

-- 6. Select students whose first name contains the letter 'a'
SELECT first_name, last_name FROM students 
WHERE first_name ILIKE '%a%';

-- 7. Select students whose first name starts with the letter 'a'
SELECT first_name, last_name FROM students 
WHERE first_name ILIKE 'a%';

-- 8. Select students whose first name ends with the letter 'a'
SELECT first_name, last_name FROM students 
WHERE first_name ILIKE '%a';

-- 9. Select students whose second-to-last letter of the first name is 'a'
SELECT first_name, last_name FROM students 
WHERE first_name ~ '.a.$';

-- 10. Select students with ID equal to 1 OR 3 (2 students can't have the same ID as asked in the exercise)
SELECT first_name, last_name FROM students 
WHERE id IN (1, 3);

-- 11. Select students born on or after January 1st, 2000
SELECT * FROM students 
WHERE birth_date >= TO_DATE('01/01/2000', 'DD/MM/YYYY');