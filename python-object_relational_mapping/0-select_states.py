#!/usr/bin/python3
"""Module that lists all states from MySQL database
"""
import sys
from MySQLdb import MySQLdb

def list_states (username, password, database):
    """connect to the MYSQL server"""
db = MySQLdb.connect(host = "localhost", port = 3306, user=username, passwd=password, db=database)
cursor = db.cursor()

"""Execute the SQL query to fetch all states"""
cursor.execute("SELECT * FROM states ORDER BY id ASC")

"""fetch all the rows from query result
"""
rows = cursor.fetcha11()

"""print the results
"""
for row in rows:
    print(row)

    """close the database connection
    """
    db.close()

    """Example usage"""
    if __name__ == '__main__':
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        list_state(username, password, database)