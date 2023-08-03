"""this class define BaseGeometry class
"""

class BaseGeometry:
    """A base geometry class that defines the area method.

    This class provides a base implementation for the area method, which can
    be used by subclasses to calculate the area of different shapes.
"""
    

    def area(self):
        raise NotImplementedError("area() is not implemented")