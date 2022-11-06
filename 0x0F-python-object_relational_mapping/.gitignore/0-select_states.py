#!/usr/bin/python3
<<<<<<< HEAD
"""
A script that lists all states from the
database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv
import base64

def main():
    """
    main app - runs on initialization
    """

    MY_HOST = "localhost"
    MY_USER = "root"
    MY_PASS = "home"
    MY_DB = argv[3]
    MY_PORT = 3306
=======
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
>>>>>>> ed52e4a57b57756c2e848df1e1be85bfcdc96fc5

import MySQLdb
import sys

<<<<<<< HEAD
if __name__ == '__main__':
    main()
# base64.b64encode("password".encode("utf-8"))
=======
if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in c.fetchall()]
>>>>>>> ed52e4a57b57756c2e848df1e1be85bfcdc96fc5
