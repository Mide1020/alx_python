"""this is how to write rectangle class
"""
#!/usr/bin/python3

"""This defines a rectangle class"""
from models.base import Base

class Rectangle(Base):
 """representng a rectangle
 """

 def init(self, width, height, x=0, y=0, id=None):
  """Initializing a new Rectangle
  Args:
       width (int): The width of the new Rectangle.
       height (int): the height of the new rectangle.
       x (int): the x coordinate of the new rectangle.
       y (int): the y coordinate of the new rectangle.
       id(int): the identity of the new rectangle
  Raises:
       Typeerror: if either of widht or height is not an int.
       ValueError: if either of widht or height <-0.
       TypeError: if either of x or y is not an int.
       ValueError:if either of x or y < 0.
  """
  self.witdth = width
  self.height = height
  self.x = x
  self.y = y
  super().init(id)

  #property
  def width(self):
      """set/get the width of the Rectangle.
      """
      return self.__width
  
  #width.setter
  def width(self, value):
    if type(value) !=int:
         raise TypeError("widht must be an integer")
    if value <= 0:
       raise ValueError("width must be > 0")
    self.__width = value

  #property
 def height(self):
    """set/get the height of the rectangle
    """
    return self.__height
 
"""setting the height of the rectangle
"""
  #height.setter
def height(self, value):
   """the height function
   """
   if type(value) != int:
      raise TypeError("height must be an integer")
   if value <= 0:
      raise ValueError("height must be > 0")
   self.__height = value

   #property
def x(self):
      """set/get the x coordinate of the rectangle
      """
      return self.__x
   
   #x.setter
def x(self, value):
   if type(value) != int:
      raise TypeError("x must be an integer")
   if value < 0:
      raise ValueError("x must be  >= 0")
   self.__x = value