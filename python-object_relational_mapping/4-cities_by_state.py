#!/usr/bin/python3
"""script that lists all states from the db hbtn_0d_usa"""

import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]


    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name" 
        " FROM cities JOIN states on cities.state_id = states.id"
        " ORDER BY cities.id ASC"
        )

    rows = cursor.fetchall()

    for result in rows:
        print(result)
