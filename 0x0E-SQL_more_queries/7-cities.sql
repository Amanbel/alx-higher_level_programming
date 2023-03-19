-- sql query to create a database and a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	id INT NOT NULL AUT_INCREMENT UNIQUE PRIMARY KEY,
	state_id INT NOT NULL, FOREIGN KEY(state_id) REFERENCES states(id));
