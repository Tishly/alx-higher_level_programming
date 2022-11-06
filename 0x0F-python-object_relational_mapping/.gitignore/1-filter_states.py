#!/usr/bin/python3
<<<<<<< HEAD
"""
A script that lists all states from the
database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv


def main():
    """
    main app - runs on initialization
    """
    MY_HOST = "localhost"
    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]
    MY_PORT = 3306

    db = MySQLdb.connect(
            host="localhost", user=MY_USER,
            password=MY_PASS, db=MY_DB, port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")

    rows = cur.fetchall()
    for row in rows:
        print(row)

if __name__ == '__main__':
    main()
=======
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    [print(state) for state in c.fetchall()]
>>>>>>> ed52e4a57b57756c2e848df1e1be85bfcdc96fc5
