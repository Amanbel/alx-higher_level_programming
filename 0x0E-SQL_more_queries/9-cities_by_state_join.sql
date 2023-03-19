-- sql query for JOIN statment
SELECT cities.id, cities.name, states.name FROM hbtn_0d_usa.cities JOIN hbtn_0d_usa.states ON hbtn_0d_usa.cities.id=hbtn_0d_usa.states.id;
