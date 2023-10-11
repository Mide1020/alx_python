#!/usr/bin/python3
"""
This module contains a script that is safe from
MySQL injections
"""
import MySQLdb
import sys


def search_states(username, password, database, state_name):
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

    """Execute the SQL query to retrieve states with matching name"""
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    """Fetch all the rows from the result set"""
    results = cursor.fetchall()

    """Print the results"""
    for row in results:
        print(row)

    """Close the cursor and the database connection"""
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script_name.py <username> <password> "
              "<database> <state_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        search_states(username, password, database, state_name)