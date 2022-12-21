#!/usr/bin/python3
"""
Module to lists all cities from specified database
"""

import sys
import MySQLdb


if __name__ == "__main__":
    hst = "localhost"
    usr = sys.argv[1]
    passwod = sys.argv[2]
    dbname = sys.argv[3]
    prt = 3306
    query = """SELECT cities.id, cities.name, states.name
    FROM cities JOIN states WHERE states.id = cities.state_id
    ORDER BY cities.id"""
    db = MySQLdb.connect(host=hst, user=usr,
                         passwd=passwod, db=dbname, port=prt)
    cur = db.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(f"{row}")
