-- displays a new column named number that display the number of times a score exists

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
