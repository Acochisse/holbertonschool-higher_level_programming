#!/usr/bin/python3
"""
takes an argument and displays all values in the states table
"""

def connectToDB():
    """ Connecting to the database """

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.arg[3], port=3306)

    cur = conn.curson()
    cur.execute("SELECT * FROM states WHERE name='{}'\
                ORDER BY id ASC.".format(sys.argv[4])

    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == sys.argv[4]:
            print(row)

    curr.close()
    conn.close()
