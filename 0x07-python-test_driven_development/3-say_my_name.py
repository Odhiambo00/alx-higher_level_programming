#!/usr/bin/python3

"""
A function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Prints names

    Args:
        first_name (str): the first name to print
        last_name (str): the second name to print

    Raises:
        TypeError: If first_name or last_name or both are not strings
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
