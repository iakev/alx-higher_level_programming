#!/usr/bin/python3


"""
Module that takes in an argument and displays
values in states where name matches the argument
"""

import sys
import MySQLdb


if __name__ == "__main__":
    hst = "localhost"
    usr = sys.argv[1]
    passwod = sys.argv[2]
    dbname = sys.argv[3]
    search = str(sys.argv[4])
    prt = 3306
    query = """SELECT * FROM states WHERE name = %s ORDER BY id"""
    db = MySQLdb.connect(host=hst, user=usr,
                         passwd=passwod, db=dbname, port=prt)
    cur = db.cursor()
    cur.execute(query, (search,))
    rows = cur.fetchall()
    for row in rows:
        print(f"{row}")
