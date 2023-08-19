#!/usr/bin/python3

"""

Module 8-square: This module defines the Square class.

"""

class BaseGeometry:

    """

    BaseGeometry class provides a basic structure for geometrical calculations.

    Public Methods:

    - area(): Raises an exception indicating that area calculation is not implemented.

    """

    def area(self):

        """

        Calculate the area of the geometry (not implemented).

        Raises:

            Exception: Indicates that the area() method is not implemented.

        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """

        Validate if a given value is a positive integer.

        Args:

            name (str): The name of the value being validated.

            value (int): The value to be validated.

        Raises:

            TypeError: If value is not an integer.

            ValueError: If value is not a positive integer.

        """

        if not isinstance(value, int):

            raise TypeError(f"{name} must be an integer")

        if value <= 0:

            raise ValueError(f"{name} must be a positive integer")

class Rectangle(BaseGeometry):

    """

    Rectangle class inherits from BaseGeometry and represents a rectangle.

    Attributes:

        __width (int): The width of the rectangle.

        __height (int): The height of the rectangle.

    Public Methods:

    - __init__(self, width, height): Initializes a Rectangle instance.

    """

    def __init__(self, width, height):

        """

        Initialize a Rectangle instance.

        Args:

            width (int): The width of the rectangle.

            height (int): The height of the rectangle.

        """

        self.integer_validator("width", width)

        self.integer_validator("height", height)

        self.__width = width

        self.__height = height

    def __str__(self):

        """

        Return a string representation of the rectangle.

        Returns:

            str: The rectangle description in the format [Rectangle] <width>/<height>.

        """

        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):

        """

        Calculate and return the area of the rectangle.

        Returns:

            int: The area of the rectangle.

        """

        return self.__width * self.__height

class Square(Rectangle):

    """

    Square class inherits from Rectangle and represents a square.

    Attributes:

        __size (int): The size of the square.

    Public Methods:

    - __init__(self, size): Initializes a Square instance.

    """

    def __init__(self, size):

        """

        Initialize a Square instance.

        Args:

            size (int): The size of the square.

        """

        self.integer_validator("size", size)

        super().__init__(size, size)

        self.__size = size

    def __str__(self):

        """

        Return a string representation of the square.

        Returns:

            str: The square description in the format [Square] <size>/<size>.

        """

        return f"[Square] {self.__size}/{self.__size}"

if __name__ == "__main__":

    s = Square(13)

    print(s)

    print(s.area())