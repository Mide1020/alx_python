#!/usr/bin/python3

"""
This is a module on the area of rectangle
"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """"
    This is a class for rectangle
    """
    def __init__(self, width, height):
        """
        Intialization of rectangle
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.

        Returns:
            str: String representation of the Rectangle instance.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height
    