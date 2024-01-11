#!/usr/bin/python3
""" script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. """
import sys
import MySQLdb

if __name__ == "__main__":
    with MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306) as db:
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'".format(sys.argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
