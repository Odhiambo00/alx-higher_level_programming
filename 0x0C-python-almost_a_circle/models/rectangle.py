#!/usr/bin/python3

"""
Defines a class Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """
    class Rectangle that inherits from class Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes class Rectangle
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        width getter/setter
        """
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """
        height getter/setter
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """
        x getter/setter
        """
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """
        y getter/setter
        """
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
