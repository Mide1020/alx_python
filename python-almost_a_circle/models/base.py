#!/usr/bin/python3

"""this is to write the first class base
"""

class Base:
    """Base class for all future classes in this project.
    Manages the id attribute in all future classes and avoids duplicating the same code and bugs
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new instances of the Base class.
        Args:
        id(int):The ID of instances.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects