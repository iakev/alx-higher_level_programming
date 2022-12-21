#!/usr/bin/python3


"""
Module that lists all states with a name starting with a literal N from
specified database
"""

import sys
import MySQLdb


if __name__ == "__main__":
    hst = "localhost"
    usr = sys.argv[1]
    passwod = sys.argv[2]
    dbname = sys.argv[3]
    prt = 3306
    db = MySQLdb.connect(host=hst, user=usr,
                         passwd=passwod, db=dbname, port=prt)
    cur = db.cursor()
    cur.execute(f"SELECT * FROM states")
    rows = cur.fetchall()
    for i in range(len(rows)):
        if rows[i][1][0] == "N":
            print(f"{rows[i]}")
