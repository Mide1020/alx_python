#!/usr/bin/python3
"""Rectangle module"""

BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry"""

    def _init_(self, width, height):
        """Initialize a Rectangle instance

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def _str_(self):
        """Return the string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)