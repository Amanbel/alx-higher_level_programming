#!/usr/bin/python3

"""Lists all the states which start
with the letter N"""

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE N%")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
