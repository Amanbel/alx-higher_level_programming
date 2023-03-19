-- sql query with subquery
SELECT name FROM cities WHERE state_id=(
	SELECT id FROM states WHERE name="California");
