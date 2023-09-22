import MySQLdb
import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 4:
    print("Usage: python list_states_with_N.py <mysql_username> <mysql_password> <database_name>")
    sys.exit(1)

# Get command-line arguments
mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

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

# Execute the SQL query to retrieve the state of New York
cursor.execute("SELECT * FROM states WHERE name = 'New York'")

# Fetch the result (assuming there's only one)
result = cursor.fetchone()

# Display the result
if result:
    print(result)

# Close the cursor and database connection
cursor.close()
db.close()
