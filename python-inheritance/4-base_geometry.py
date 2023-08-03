"""this class define BaseGeometry class
"""

class BaseGeometry:
    """A base geometry class that defines the area method.

    This class provides a base implementation for the area method, which can
    be used by subclasses to calculate the area of different shapes.

    Examples:
        Here's an example of how you can use this class:

        >>> bg = BaseGeometry()
        >>> bg.area()
        Traceback (most recent call last):
        ...
        NotImplementedError: area() is not implemented
    """

    def area(self):
        raise NotImplementedError("area() is not implemented")
