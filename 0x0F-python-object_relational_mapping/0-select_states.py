#!/usr/bin/python3

"""
Fetches all records from the 'states' table in a specified MySQL database.
Usage: script.py <MySQL username> <MySQL password> <database name>
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Establish a database connection
    conn = MySQLdb.connect(
        host="localhost",  # Database server address
        port=3306,  # Database server port
        user=argv[1],  # MySQL username from command-line argument
        passwd=argv[2],  # MySQL password from command-line argument
        db=argv[3]  # Database name from command-line argument
    )

    # Execute a query to select all records from 'states', ordered by 'id'
    cur = conn.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY id ASC")
    query_rows = cur.fetchall()

    # Print each row of the query result
    for row in query_rows:
        print(row)

    # Close the cursor and connection to clean up
    cur.close()
    conn.close()
