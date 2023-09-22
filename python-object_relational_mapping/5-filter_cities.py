import MySQLdb
import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 5:
    print("Usage: python list_cities_by_state.py <mysql_username> <mysql_password> <database_name> <state_name>")
    sys.exit(1)

# Get command-line arguments
mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]
state_name = sys.argv[4]

try:
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Use a prepared statement to prevent SQL injection
    query = "SELECT cities.id, cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the results
    results = cursor.fetchall()

    # Display the results
    for row in results:
        print(row)

except MySQLdb.Error as e:
    print(f"Error: {e}")
finally:
    # Close the cursor and database connection
    cursor.close()
    db.close()
