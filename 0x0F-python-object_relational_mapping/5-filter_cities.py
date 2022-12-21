#!/usr/bin/python3
"""
Module that takes in state name as an argument and displays
all cities in that state where name matches the argument
"""

import sys
import MySQLdb


if __name__ == "__main__":
    hst = "localhost"
    usr = sys.argv[1]
    passwod = sys.argv[2]
    dbname = sys.argv[3]
    state = str(sys.argv[4])
    prt = 3306
    query = """SELECT cities.name
    FROM cities
    WHERE cities.state_id =
    (SELECT states.id FROM
    states WHERE states.name = %s)
    ORDER BY cities.id"""
    db = MySQLdb.connect(host=hst, user=usr,
                         passwd=passwod, db=dbname, port=prt)
    cur = db.cursor()
    cur.execute(query, (state,))
    rows = cur.fetchall()
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            print(rows[i][j], end=", " if i != len(rows) - 1 else "\n")
