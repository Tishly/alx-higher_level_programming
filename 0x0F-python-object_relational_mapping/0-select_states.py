#!/usr/bin/python3
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
# base64.b64encode("password".encode("utf-8"))
