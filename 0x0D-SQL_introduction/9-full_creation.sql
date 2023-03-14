-- sql query which creates a table and injects it with data
CREATE TABLE IF NOT EXISTS second_table (
	id int,
	name varchar(256),
	score int
	);
INSERT INTO second_table VALUES (1, "John", 10);
INSERT INTO second_table VALUES (2, "Alex", 3);
INSERT INTO second_table VALUES (3, "Bob", 14);
INSERT INTO second_table VALUES (4, "George", 8);
