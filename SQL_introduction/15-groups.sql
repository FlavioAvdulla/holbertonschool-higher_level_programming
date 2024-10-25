-- Select the score and name columns from the second_table

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;