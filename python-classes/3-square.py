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
        self.__size = size

    @property
    def size(self):
        """Get or set the size of the square.

        The size must be an integer, otherwise a TypeError is raised.
        If the size is less than 0, a ValueError is raised.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
    