#!/usr/bin/python3
""" A script that lists all cities from the database hbtn_0e_4_usa """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM
                    cities INNER JOIN states ON states.id = cities.id""")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
