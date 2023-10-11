#!/usr/bin/python3
"""This Module takes an argument and diaplay all values of a state
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

    """Create a cursor object to interact with the database'"""
    cursor = db.cursor()

    """Execute the SQL query to retrieve states with matching name"""
    query = ("SELECT * FROM states "
             "WHERE BINARY name = '{}' "
             "ORDER BY id ASC").format(state_name)
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
    if len(sys.argv) != 5:
        print("Usage: python script_name.py <username> <password> "
              "<database> <state_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        search_states(username, password, database, state_name)