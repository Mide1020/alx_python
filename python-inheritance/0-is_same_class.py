"""This module defines a Square class.

The Square class represents a square with a private instance attribute 'size'.
It allows instantiation with an optional size, and provides a method 'area' to calculate the square's area.
The size attribute can be accessed using a property 'size' with a setter for validation.

"""

class Square:
    """A class representing a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        _init_(self, size=0): Initializes a square object with an optional size.
        size(self): Getter method to retrieve the size of the square.
        size(self, value): Setter method to set the size of the square.
        area(self): Calculates and returns the area of the square.
    """
    def is_same_class(obj, a_class):
     """
    This function checks if an object is exactly an instance of a specified class.

    Args:
    obj: Any object.
    a_class: Any class.

    Returns:
    True if the object is exactly an instance of the specified class, otherwise False.
    """
     if type(obj) == a_class:
        return True
     else:
        return False