"""writing an empty class
"""
class BaseGeometry:
    """
    This is an empty base class for geometry-related functionality.

    Attributes:
        None

    Methods:
        None

    Description:
        BaseGeometry serves as a foundation for defining specific geometric shapes
        or operations in derived classes. It provides a common base for organizing
        geometry-related functionality without any specific implementation.
    """

    def __repr__(self):
        """
        Returns a string representation of the BaseGeometry instance.

        Returns:
            str: A string representation of the instance.
        """
        return "<{} object at {}>".format(type(self).__module__ + "." + type(self).__name__, hex(id(self)))

# Example usage:
if __name__ == "__main__":
    bg = BaseGeometry()

    print(bg)
    print(dir(bg))
    print(dir(BaseGeometry))