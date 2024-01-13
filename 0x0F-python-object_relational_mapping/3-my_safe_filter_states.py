#!/usr/bin/python3
""" script that takes in arguments and displays
    all values in the states table of hbtn_0e_0_usa
    where name matches the argument.
    But it's safe from MySQL injections!
"""
import MySQLdb
import sys

if __name__ == "__main__":
    with MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3]) as db:
        with db.cursor() as cursor:
            query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
            cursor.execute(query, (sys.argv[4],))

            rows = cursor.fetchall()
            for row in rows:
                print(row)
