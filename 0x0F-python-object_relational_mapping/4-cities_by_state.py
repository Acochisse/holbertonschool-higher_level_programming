#!/usr/bin/python3
"""
Module for managing MySQL
"""


def connectToDB():
    """ Connecting to the database """

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.arg[3], port=3306)

    cur = conn.curson()
    cur.execute("SELECT cities.id, cities.name FROM cities INNER \
                JOIN states on cities.state_id=states.id \
                ORDER BY cities.id ASC")

    query_rows = cur.fetchall()
    for row in query_rows:
            print(row)

    curr.close()
    conn.close()

if __name__ == '__main__':
    import MySQLdb
    import sys
    connectToDB()
