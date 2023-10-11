#!/usr/bin/python3
"""
This module  lists all State objects
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, db_name):
    """Create an engine to connect to the MySQL server"""
    engine = create_engine(
        f'mysql://{username}:{password}@localhost:3306/{db_name}'
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve and display State objects sorted by ID
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python list_states.py <username> <password> <db_name>")
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, db_name)