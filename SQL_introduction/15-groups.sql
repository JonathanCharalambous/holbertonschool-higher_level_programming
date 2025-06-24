-- Script that counts the number of times a score appears in the table
SELECT score, COUNT(score)
FROM second_table
GROUP BY score;