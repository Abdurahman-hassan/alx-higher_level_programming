#!/usr/bin/python3

"""
Retrieves and prints the names of cities from a specific state in the
hbtn_0e_4_usa database. The search for the state name is case-sensitive.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Establishes connection to the specified MySQL database
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # Prepares and executes a query to find cities in the given state
    cur = conn.cursor()
    cur.execute("""SELECT cities.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE BINARY states.name = %s
                ORDER BY cities.id ASC""", (argv[4],))

    # Concatenates and prints city names in a comma-separated string
    print(", ".join([row[0] for row in cur.fetchall()]))

    # Closes the cursor and connection to clean up
    cur.close()
    conn.close()
