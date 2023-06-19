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

    def update(self, *args, **kwargs):
        """
        Updates the instance attributes from the arguments passed
        """

        i = 0;
        attributes = ['id', 'size', 'x', 'y']

        if len(args) > 0:
            for attr in attributes:
                if i > len(args) - 1:
                    break
                setattr(self, attr, args[i])
                i += 1
        else:
            for key, value in kwargs.items():
                if key not in attributes:
                    continue
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of Square instance
        """

        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
