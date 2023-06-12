#!/usr/bin/python3

"""
Defines class Square which inherits from class Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square
    """

    def __init__(self, size):
        """
        Initializes class Square instance attributes
        """

        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square
        """

        return self.__size ** 2

    def __str__(self):
        """
        Informal string representation of square
        """

        return f"[Square] {self.__size}/{self.__size}"
