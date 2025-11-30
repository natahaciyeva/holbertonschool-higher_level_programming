-- 10-top_score.sql
-- Bu skript second_table cədvəlindəki bütün sətirləri score üzrə azalan sırada göstərir
SELECT score, name
FROM second_table
ORDER BY score DESC;
