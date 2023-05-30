#!/usr/bin/python3

"""Lists all rows of states table
by the MySQL module"""

import MySQLdb
import sys
if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    res = cur.fetchall()
    for row in res:
        print(row)
    cur.close()
    db.close()
