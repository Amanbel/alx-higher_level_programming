#!/usr/bin/python3

"""Lists states from user input
that is provided as an argument"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb(host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states\
            WHERE name = {} ORDER BY states.id ASC".format(argv[4])

    cur.execute(query)
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
