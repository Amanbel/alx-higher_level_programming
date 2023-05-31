#!/usr/bin/python3

"""Lists all the cities of a state
depending on the argument provided"""

import MySQLdb as mysql
from sys import argv

if __name__ == "__main__":
    db = mysql.connect(host="localhost",
                       user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
            JOIN states\
            ON states.id = cities.state_id\
            WHERE states.name = %s", (argv[4], ))
    rows = cur.fetchall()
    cities = []
    for row in rows:
        for col in row:
            cities.append(col)
    print(", ".join(cities))
    cur.close()
    db.close()
