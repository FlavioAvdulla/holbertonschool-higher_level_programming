-- List all  the records with the score.

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;