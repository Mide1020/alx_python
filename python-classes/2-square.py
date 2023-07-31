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
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2