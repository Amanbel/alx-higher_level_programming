#!/usr/bin/python3
import sys

if __name__ == "__main__" && len(sys.argv) == 4:
    import MySQLdb

    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORD BY states.id ASC")
    res = cur.fetchall()
    for row in res:
        print (row)
