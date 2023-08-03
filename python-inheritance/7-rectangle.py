"""this is a class rectangle that inherits baseGeometry
"""

class BaseGeometry:

    """A class representing a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

def __init__(self, width, height):
        """Initializes a Rectangle instance with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

def area(self):
        """Calculates the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height

def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            A string representation of the rectangle in the format:
            "[Rectangle] <width>/<height>"
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
