#!/usr/bin/python3

"""

Module models/rectangle: This module defines the Rectangle class.

"""
from models.base import Base

class Rectangle(Base):
    """A class representing a Rectangle that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        # (Constructor code as before...)

    # Other methods as before...

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle using arguments and keyword arguments.

        Args:
            *args: Positional arguments in the order: id, width, height, x, y.
            **kwargs: Keyword arguments as key/value pairs representing attributes.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

# Example usage
if __name__ == "__main__":
    r = Rectangle(10, 5, 2, 3, 1)
    print("Before update:")
    print(r)
    r.update(2, 8, 6)
    print("After positional update:")
    print(r)
    r.update(x=4, y=2, width=12)
    print("After keyword update:")
    print(r)