#!/usr/bin/python3

"""Lists all the rows from the table
cities using MySQLdb module"""

import MySQLdb as mysql
from sys import argv

if __name__ == "__main__":
    db = mysql.connect(host="localhost",
                       user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM cities ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
