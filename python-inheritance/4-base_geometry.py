"""

Module 4-base_geometry: This module defines the BaseGeometry class.

"""

class BaseGeometry:

    """

    BaseGeometry class provides a basic structure for geometrical calculations.

    Public Methods:

    - area(): Raises an exception indicating that area calculation is not implemented.

    """

    def area(self):

        """

        Calculate the area of the geometry (not implemented).

        Raises:

            Exception: Indicates that the area() method is not implemented.

        """

        raise Exception("area() is not implemented")

if __name__ == "__main__":

    bg = BaseGeometry()

    try:

        print(bg.area())

    except Exception as e:

        print("[{}] {}".format(e.__class__.__name__, e))