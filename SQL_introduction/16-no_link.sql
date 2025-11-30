-- 16-no_link.sql
-- name sütunu boş olmayan sətirləri göstərir, score üzrə azalan sırada
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
