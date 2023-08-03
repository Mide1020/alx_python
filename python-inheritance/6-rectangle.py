"""
writing a class rectangle
 """

def BaseGeometry(5-base_geometry.py):
 
 class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiates a Rectangle object
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
