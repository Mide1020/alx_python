"""this is a class rectangle that inherits baseGeometric
"""


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
