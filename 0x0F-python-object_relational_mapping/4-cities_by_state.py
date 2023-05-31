#!/usr/bin/python3

"""Lists all the rows from the table
cities using MySQLdb module"""

import MySQLdb as mysql
from sys import argv

if __name__ == "__main__":
    db = mysql.connect(host="localhost",
                       user=argv[1], passwd=argv[2], db=argv[3],
                       port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
            FROM cities\
            JOIN states\
            ON cities.state_id = states.id\
            ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
