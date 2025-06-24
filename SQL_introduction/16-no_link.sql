-- script that lists all records of the table second_table ordered by desc
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;