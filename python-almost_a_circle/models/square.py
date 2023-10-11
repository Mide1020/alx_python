#!/usr/bin/python3
"""
Module on Square class that inherits from Rectangle
"""
from models.rectangle import Rectangle

class Square(Rectangle):

    """
    Class on Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Function of size

        Intializes self
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        The function of width
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Value function 
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        String function 
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"