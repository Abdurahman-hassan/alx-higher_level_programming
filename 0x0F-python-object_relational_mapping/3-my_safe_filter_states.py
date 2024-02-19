#!/usr/bin/python3

"""
Script to fetch and print information about a state from the database
hbtn_0e_0_usa based on the provided state name (case-sensitive).

Usage: ./script_name.py mysql_username mysql_password database_name state_name
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM `states` WHERE BINARY(`name`) = %s "
                "ORDER BY id ASC", (argv[4],))

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()
