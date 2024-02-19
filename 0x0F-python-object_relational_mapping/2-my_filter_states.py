#!/usr/bin/python3

"""
Fetches and prints information about a specified state from the 'states'
table in the 'hbtn_0e_0_usa' database. The state name is case-sensitive and
must be provided as a command-line argument.
"""

from sys import argv

import MySQLdb

if __name__ == '__main__':
    # Establish a secure connection to the MySQL database
    conn = MySQLdb.connect(
        host="localhost",  # Database server address
        port=3306,  # Database server port
        user=argv[1],  # MySQL username from the command-line argument
        passwd=argv[2],  # MySQL password from the command-line argument
        db=argv[3]  # Database name from the command-line argument
    )

    # Execute a SQL query to find a specific state by its name,
    # ensuring case-sensitive matching
    cur = conn.cursor()
    query = """SELECT *
               FROM `states`
               WHERE BINARY(`name`) = '{}'
               ORDER BY id ASC""".format(argv[4])
    cur.execute(query)
    query_rows = cur.fetchall()

    # Print each matching row for the specified state name
    for row in query_rows:
        print(row)

    # Close the cursor and connection to clean up resources
    cur.close()
    conn.close()
