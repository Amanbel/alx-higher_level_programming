-- sql query to create table with primary key
CREATE TABLE IF NOT EXISTS id_not_null(id INT PRIMARY KEY, name VARCHAR(256));
UPDATE id_not_null SET id=1
