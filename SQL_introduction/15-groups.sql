-- Script that counts the number of times a score appears in the table
SELECT score, COUNT(score) as 'number'
FROM second_table
GROUP BY score
ORDER BY 'number' DESC;