#!/usr/bin/python3
"""
Module on Base
This module demostrate a class base that has private attribute.
"""


class Base:
    """
    This is a class for the base
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        Intializes a Base instance
        args: 
        id (int): The value for the attribute.
        Attributes:
        id (int): The public instance attribute for storing the id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects