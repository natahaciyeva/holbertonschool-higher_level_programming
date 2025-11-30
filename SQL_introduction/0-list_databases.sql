-- 0-list_databases.sql
-- Bu skript mövcud verilənlər bazalarını əlifba sırasına görə göstərir
SELECT SCHEMA_NAME AS `Database`
FROM INFORMATION_SCHEMA.SCHEMATA
ORDER BY SCHEMA_NAME;
