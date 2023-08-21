#!/usr/bin/python3

"""

Module models/rectangle: This module defines the Rectangle class.

"""
from models.base import Base

class Rectangle(Base):
    """A class representing a Rectangle that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the top-left corner. Defaults to 0.
            y (int, optional): The y-coordinate of the top-left corner. Defaults to 0.
            id (int, optional): The ID of the rectangle. If not provided, a new ID will be generated.

        Raises:
            ValueError: If width or height is not positive, or if x or y is negative.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive.")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive.")
        self.__height = value

    @property
    def x(self):
        """int: The x-coordinate of the top-left corner."""
        return self.__x

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("X coordinate cannot be negative.")
        self.__x = value

    @property
    def y(self):
        """int: The y-coordinate of the top-left corner."""
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("Y coordinate cannot be negative.")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """Display the rectangle using '#' characters."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

# Example usage
if __name__ == "__main__":
    r = Rectangle(10, 5, 2, 7, 1)
    print(r)
    r.display()
