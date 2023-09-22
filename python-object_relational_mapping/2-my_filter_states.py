import MySQLdb
import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 5:
    print("Usage: python search_states.py <mysql_username> <mysql_password> <database_name> <state_name>")
    sys.exit(1)

# Get command-line arguments
mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]
state_name = sys.argv[4]

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

# Prepare the SQL query using string formatting
query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"

# Execute the SQL query with the provided state name
cursor.execute(query, (state_name,))

# Fetch all the results
results = cursor.fetchall()

# Display the results
for row in results:
    print(row)

# Close the cursor and database connection
cursor.close()
db.close()
