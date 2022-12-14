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
    state = sys.argv[4]
    prt = 3306
    query = """SELECT *
    FROM cities
    INNER JOIN states
    ON cities.state_id = states.id
    ORDER BY cities.id"""
    db = MySQLdb.connect(host=hst, user=usr,
                         passwd=passwod, db=dbname, port=prt)
    cur = db.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    count = 0
    cities = []
    for i in range(len(rows)):
        if rows[i][4] == state:
            count += 1
            cities.append(rows[i][2])
    for i in range(len(cities)):
            print(cities[i], end=", " if i !=len(cities) - 1 else "\n")
