class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Calculates the area of the geometry"""
        raise NotImplementedError("area() is not implemented")

    def perimeter(self):
        """Calculates the perimeter of the geometry"""
        raise NotImplementedError("perimeter() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer
        Args:
            name (str): name of the value being validated
            value (int): value to be validated
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiates a Rectangle object
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        if isinstance(width, int) and isinstance(height, int):
            if width > 0 and height > 0:
                self.__width = width
                self.__height = height
            else:
                raise ValueError("width and height must be greater than 0")
        else:
            raise TypeError("width and height must be integers")
