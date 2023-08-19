#!/usr/bin/python3

"""

Module models/rectangle: This module defines the Rectangle class.

"""

from models.base import Base

class Rectangle(Base):

    """

    Rectangle class inherits from Base and represents a rectangle.

    Attributes:

        __width (int): The width of the rectangle.

        __height (int): The height of the rectangle.

        __x (int): The horizontal position of the rectangle.

        __y (int): The vertical position of the rectangle.

    Public Methods:

        - __init__(self, width, height, x=0, y=0, id=None): Initializes a Rectangle instance.

        - area(self): Returns the area of the Rectangle instance.

    """

    def __init__(self, width, height, x=0, y=0, id=None):

        """

        Initialize a Rectangle instance.

        Args:

            width (int): The width of the rectangle.

            height (int): The height of the rectangle.

            x (int, optional): The horizontal position of the rectangle. Defaults to 0.

            y (int, optional): The vertical position of the rectangle. Defaults to 0.

            id (int, optional): The unique identifier of the rectangle. Defaults to None.

        """

        super().__init__(id)

        self.width = width

        self.height = height

        self.x = x

        self.y = y

    
@property


    def width(self):

        """Getter for width."""

        return self.__width

    
@width
.setter

    def width(self, value):

        """Setter for width."""

        self.integer_validator("width", value)

        self.__width = value

    
@property


    def height(self):

        """Getter for height."""

        return self.__height

    
@height
.setter

    def height(self, value):

        """Setter for height."""

        self.integer_validator("height", value)

        self.__height = value

    
@property


    def x(self):

        """Getter for x."""

        return self.__x

    
@x
.setter

    def x(self, value):

        """Setter for x."""

        self.integer_validator("x", value)

        self.__x = value

    
@property


    def y(self):

        """Getter for y."""

        return self.__y

    
@y
.setter

    def y(self, value):

        """Setter for y."""

        self.integer_validator("y", value)

        self.__y = value

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

        if name == "width" or name == "height":

            if value <= 0:

                raise ValueError(f"{name} must be > 0")

        elif name == "x" or name == "y":

            if value < 0:

                raise ValueError(f"{name} must be >= 0")

    def area(self):

        """

        Calculate and return the area of the rectangle.

        Returns:

            int: The area of the rectangle.

        """

        return self.__width * self.__height

if __name__ == "__main__":

    r1 = Rectangle(3, 2)

    print(r1.area())

    r2 = Rectangle(2, 10)

    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)

    print(r3.area()) 