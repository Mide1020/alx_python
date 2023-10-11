#!/usr/bin/python3
"""This module will be Sql injection free
and it will list id,cities and state in ASC
order
"""

import MySQLdb
import sys


def list_cities_by_state(username, password, database, state_name):
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

    """Execute the SQL query to retrieve cities of the specified state"""
    query = ("SELECT cities.id, cities.name, states.name "
             "FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC")
    cursor.execute(query, (state_name,))

    """Fetch all the rows from the result set"""
    results = cursor.fetchall()

    """Extract and print only the city names"""
    city_names = [row[1] for row in results]
    print(", ".join(city_names))

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
        list_cities_by_state(username, password, database, state_name)