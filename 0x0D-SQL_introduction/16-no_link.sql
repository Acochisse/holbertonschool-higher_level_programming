-- script the displays all the records of second_table

SELECT score, name FROM second_table WHERE name IS NOT NULL and name != "" ORDER BY DESC;
