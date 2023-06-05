#!/usr/bin/python3

"""
Defines a class rectangle
"""


class Rectangle:
    """
    class Rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle

        Args:
            width (int): The width of rectangle
            height (int): The height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get/set rectangle width
        """

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Get/set rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Returns the rectangle area
        """

        return self.width * self.height

    def perimeter(self):
        """
        Returns the rectangle perimeter
        """

        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width * 2) + (self.height * 2)
