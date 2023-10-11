#!/usr/bin/python
"""
This module prints the first State object
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_first_state(username, password, db_name):
    # Create an engine to connect to the MySQL server
    engine = create_engine(
        f'mysql://{username}:{password}@localhost:3306/{db_name}'
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve and print the first State object based on states.id
    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python first_state.py <username> <password> <db_name>")
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    print_first_state(username, password, db_name)