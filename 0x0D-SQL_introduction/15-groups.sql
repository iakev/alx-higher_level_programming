-- Script lists number of records with the same score in the table 'second_table'"
SELECT DISTINCT score, COUNT(*) as number FROM second_table;
