-- lists  all records of the table
-- don't list rows without a name value
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC, name DESC
