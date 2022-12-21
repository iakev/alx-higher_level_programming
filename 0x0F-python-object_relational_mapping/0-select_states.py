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
def query_db():
    """
    Establishes actual connection to database
    and performs the query and prints the results
    """

    db = MySQLdb.connect(host=hst, user=usr,
                         passwd=passwod, db=dbname, port=prt)
    cur = db.cursor()
    cur.execute(f"SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(f"{row}")

if __name__ == "__main__":
    query_db()
