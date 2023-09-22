from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 4:
    print("Usage: python first_state.py <mysql_username> <mysql_password> <database_name>")
    sys.exit(1)

# Get command-line arguments
mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

# Define the database connection URL
db_url = f"mysql://{mysql_username}:{mysql_password}@localhost:3306/{database_name}"

try:
    # Create a SQLAlchemy engine
    engine = create_engine(db_url)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print the first State object, ordered by states.id
    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

except Exception as e:
    print(f"Error: {e}")
finally:
    # Close the session
    session.close()
