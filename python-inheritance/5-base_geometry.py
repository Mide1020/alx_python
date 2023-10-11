#!/usr/bin/python3
"""
Module on the BaseGeometry class.
"""

class TheMetaclass(type):
    """
    This class contain adefault parent obj.
    """
    def __dir__(subclass):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
class BaseGeometry(metaclass=TheMetaclass):
    """
    An empty class file defining the base geometry.
    """
    def __dir__(subclass):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    """
    Method to remove the initsubclass
    """
    def area(self):

        """
        Calculate the area of the geometry.

        Raises:
            Exception: This method is not implemented.
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """
        Validating integer value

        Args:
            name (str): The name of the value being validated.
            value: The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        