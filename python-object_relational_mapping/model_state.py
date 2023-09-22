from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    Represents a state entity in a database.

    This class defines the structure of the 'states' table, including its columns and constraints.

    Attributes:
        id (int): An auto-generated, unique integer representing the primary key of the state.
            It cannot be null and is automatically incremented.
        name (str): A string representing the name of the state, with a maximum length of 128 characters.
            It cannot be null.

    Note:
        This class is intended to be used with SQLAlchemy to interact with a MySQL database.
        To create the corresponding table in the database, use Base.metadata.create_all(engine),
        where 'engine' is a SQLAlchemy engine instance connected to the database.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
