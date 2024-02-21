#!/usr/bin/python3
""" lists all states from database with the use of parameterized queries """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    nme = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (nme, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
