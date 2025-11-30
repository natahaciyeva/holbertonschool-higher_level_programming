-- 11-best_score.sql
-- score >= 10 olan qeydləri score azalan sırada göstərir
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
