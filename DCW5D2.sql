SELECT COUNT(*) FROM actors;

INSERT INTO actors (first_name, last_name, birth_date)
VALUES (NULL, NULL, NULL);

-- The result will depend on how the table was defined:If the columns first_name and last_name are defined with the NOT NULL constraint (which is very common), the database will reject the insertion and show an error message.

ERROR: null value in column "first_name" violates not-null constraint

--The NOT NULL constraint is used to ensure that a column must always contain a value — in other words, it cannot be left empty.If the columns do not have a NOT NULL constraint, then the insertion will succeed, and the empty fields will be stored as NULL.