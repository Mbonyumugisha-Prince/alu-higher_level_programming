#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""

from .rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square inheriting Rectangle
    Attributes:
        size (int): The size of the square
        x (int): The x coordinate
        y (int): The y coordinate
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """Returns a dictionary representation of the square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y,
        }

