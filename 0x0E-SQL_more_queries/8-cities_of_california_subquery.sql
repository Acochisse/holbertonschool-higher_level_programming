-- Script that queries all the cities in cal that can be found in the cities db

SELECT id, name
FROM cities
WHERE state_id = (
      SELECT id
      FROM states
      WHERE name = "California"
)
ORDER BY cities.id;
