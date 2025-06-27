-- Script to find all info about cities in California using JOIN
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
WHERE states.name = 'California';