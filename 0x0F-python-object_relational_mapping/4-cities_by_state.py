#!/usr/bin/python3

"""
Fetches and prints information about cities and their corresponding states from
the hbtn_0e_4_usa database. This script demonstrates how to join two tables and
sort the result.

Usage: ./script_name.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Establish database connection
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # Execute SQL query to retrieve city and state information
    cur = conn.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC""")

    # Display each city and its corresponding state
    for row in cur.fetchall():
        print(row)

    # Close connections to release resources
    cur.close()
    conn.close()
