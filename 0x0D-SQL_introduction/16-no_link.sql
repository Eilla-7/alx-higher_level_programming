-- List records with a non-null name value in second_table of the database
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
