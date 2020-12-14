#!/usr/bin/python3
"""
Module that gets all the states
"""


def connectToDB():
    """ Connecting to the database """

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.arg[3], port=3306)

    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetch()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()

if __name__ == '__main__':
    import MySQLdb
    import sys
    connectToDB()
