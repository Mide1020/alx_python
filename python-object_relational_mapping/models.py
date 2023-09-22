from sqlalchemy import create_engine
from models import Base, State

# Define the database connection URL
db_url = 'mysql://<username>:<password>@localhost:3306/<database_name>'

# Create a SQLAlchemy engine
engine = create_engine(db_url)

# Create the 'states' table in the database
Base.metadata.create_all(engine)
