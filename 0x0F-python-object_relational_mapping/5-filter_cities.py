#!/usr/bin/python3
""" A script that takes in the name of a state
    as an argument and lists all cities of that state,
    using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":
    state = sys.argv[4]
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM cities
                   INNER JOIN states ON states.id = cities.state_id
                   WHERE states.name = %s""", (state, ))
    rows = cursor.fetchall()
    result = ', '.join(row[0] for row in rows)
    print(result)
    cursor.close()
    db.close()
