#!/usr/bin/python3

"""
Defines class Square that inherits from class Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes class Square
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        size getter/setter
        """

        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
        Informal string representation of a Square
        """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
