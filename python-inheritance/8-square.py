#!/usr/bin/python3
"""A module that defines a Square class."""


class BaseGeometry:
    """A class representing a base geometry.

    Attributes:
        None.
    """

    def area(self):
        """Calculates the area of the geometry.

        Raises:
            Exception: If area is not implemented.

        Returns:
            The area of the geometry.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if a value is an integer and is greater than 0.

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def _str_(self):
        """Returns the string representation of the Rectangle instance.

        Returns:
            The string representation of the Rectangle instance.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height


class Square(Rectangle):
    """A class representing a square.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size)