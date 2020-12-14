#!/usr/bin/python3
"""
Module that injects
"""

def connectToDB():
    """ Connecting to the database """

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.arg[3], port=3306)

    cur = conn.curson()
    cur.execute("SELECT * FROM states WHERE name=%s \
                 ORDER BY id ASC", (sys.argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
            print(row)

if __name__ == '__main__':
    import MySQLdb
    import sys
    connectToDB()
