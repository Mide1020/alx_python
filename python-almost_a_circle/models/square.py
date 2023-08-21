from models.rectangle import Rectangle

class Square(Rectangle):
    """A class representing a Square that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square (width and height).
            x (int, optional): The x-coordinate of the top-left corner. Defaults to 0.
            y (int, optional): The y-coordinate of the top-left corner. Defaults to 0.
            id (int, optional): The ID of the square. If not provided, a new ID will be generated.

        Raises:
            ValueError: If size is not positive, or if x or y is negative.
            TypeError: If size, x, or y is not an integer.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """int: The size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

# Example usage
if __name__ == "__main__":
    s = Square(5, 2, 3, 1)
    print(s)
    s.size = 8
    print("After resizing:")
    print(s)