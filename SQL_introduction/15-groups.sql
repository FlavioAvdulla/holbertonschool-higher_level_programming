-- Select the score and the count of records for each score as 'number'

SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;