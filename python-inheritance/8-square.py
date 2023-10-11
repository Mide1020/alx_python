#!/usr/bin/python3
"""
7-rectangle.py
Module containing the Rectangle class that inherits from BaseGeometry.
"""
Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """
    A square class that inherits from Rectangle

    Attributes:
    __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
        size (int): The size of the square.

        Raises:
        TypeError: If size is not an integer.
         ValueError: If size is not positive.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
        str: String representation of the Square instance.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """
        Returns the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size * self.__size
    