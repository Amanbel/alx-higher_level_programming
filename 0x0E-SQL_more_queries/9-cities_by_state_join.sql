-- sql query for JOIN statment
SELECT cities.id, cities.name, states.name FROM
cities JOIN states ON cities.id=states.id;
