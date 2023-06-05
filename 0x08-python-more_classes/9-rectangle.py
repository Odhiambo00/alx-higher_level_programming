#!/usr/bin/python3

"""
Defines a class rectangle
"""


class Rectangle:
    """
    class Rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle

        Args:
            width (int): The width of rectangle
            height (int): The height of rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def __str__(self):
        """
        Prints the rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ''
        for h in range(self.__height):
            for w in range(self.__width):
                try:
                    rectangle += str(self.print_symbol)
                except Exceeption:
                    rectangle += type(self).print_symbol
            if h < self.__height - 1:
                rectangle += '\n'
        return rectangle

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        """

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a string message for every deletion
        """

        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance with width == height == size
        """

        return Rectangle(size, size)
