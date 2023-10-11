#!/bin/usr/python3
"""
This module list all state that starts with N
"""

import MySQLdb
import sys


def list_states_with_N(username, password, database):
    """Connect to the MySQL server"""
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    """Create a cursor object to interact with the database"""
    cursor = db.cursor()

    """Execute the SQL query to retrieve states starting with 'N' """
    query = "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    """Fetch all the rows from the result set"""
    results = cursor.fetchall()

    """Print the results"""
    for row in results:
        print(row)

    """Close the cursor and the database connection"""
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script_name.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_states_with_N(username, password, database)