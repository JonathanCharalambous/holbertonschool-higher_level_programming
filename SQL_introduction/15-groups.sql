-- Script that counts the number of times a score appears in the table
SELECT score, COUNT(score) as 'number'
FROM second_table
ORDER BY 'number' DESC
GROUP BY score;