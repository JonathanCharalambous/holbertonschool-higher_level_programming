-- Script that retrieves all cities in California
SELECT * 
FROM cities
WHERE state_id IN (
    SELECT id
    FROM states
    WHERE name = 'California'
)