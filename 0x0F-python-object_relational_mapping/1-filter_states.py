#!/usr/bin/python3
"""
module that filters states by N
"""

def connectToDB():
    """ Connecting to the database """

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.arg[3], port=3306)

    cur = conn.curson()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1][0] = 'N':
            print(row)

    curr.close()
    conn.close()

if __name__ == '__main__':
    import MySQLdb
    import sys
    connectToDB()
