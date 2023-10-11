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