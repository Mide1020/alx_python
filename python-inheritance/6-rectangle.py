#!/usr/bin/python3

"""

Module 6-rectangle: This module defines the Rectangle class.

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

if __name__ == "__main__":

    r = Rectangle(3, 5)

    print(r)

    print(dir(r))

    try:

        print("Rectangle: {} - {}".format(r.width, r.height))

    except Exception as e:

        print("[{}] {}".format(e.__class__.__name__, e))

    try:

        r2 = Rectangle(4, True)

    except Exception as e:

        print("[{}] {}".format(e.__class__.__name__, e))
