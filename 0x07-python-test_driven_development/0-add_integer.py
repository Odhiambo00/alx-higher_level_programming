#!/usr/bin/python3

"""
A function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Returns the integer sum of a and b

    If a or b or both are floats, the're typecast into integers before adding

    Raises:
        TypeError: If both a and b or either is a non-integer or non-float/both
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
