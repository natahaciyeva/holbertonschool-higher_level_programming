-- 15-groups.sql
-- Score üzrə qruplaşdırıb sayını (number) göstərir
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
