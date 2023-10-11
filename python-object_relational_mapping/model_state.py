#!/usr/bin/python3
"""
This is a module that creates python file
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


"""Create a declarative base"""
Base = declarative_base()
"""Class for state base"""


class State(Base):
    """Define the State class"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)