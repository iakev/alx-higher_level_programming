#!/usr/bin/python3


"""
Module that lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

hst = "localhost"
usr = sys.argv[1]
passwod = sys.argv[2]
dbname = sys.argv[3]
prt = 3306
db = MySQLdb.connect(host=hst, user=usr,
                     passwd=passwod, db=dbname, port=prt)
cur = db.cursor()
cur.execute(f"SELECT * FROM states ORDER BY id")
rows = cur.fetchall()
for row in rows:
    print(f"{row}")
