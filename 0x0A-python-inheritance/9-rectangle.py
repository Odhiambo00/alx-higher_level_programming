#!/usr/bin/python3

"""
Defines class Rectangle that inherits from class BaseGeometry
"""


class BaseGeometry:
    """
    A class with a public attribute
    """

    def area(self):
        """
        Raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Class Rectangle
    """

    def __init__(self, width, height):
        """
        Initializes Rectangle class instance attributes
        """

        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """
        Returns area of rectangle
        """

        return self.__width * self.__height

    def __str__(self):
        """
        Represents the area of rectangle as string informally
        """

        return f"[Rectangle] {self.__width}/{self.__height}"
