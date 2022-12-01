-- Dislplays MAX value of temp for each state
-- highlights usage of MAX
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
