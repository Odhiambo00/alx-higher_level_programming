#!/usr/bin/python3

"""
Mylist class
"""


class MyList(list):
    """
    Inherits from list class
    """

    def __init__(self):
        """
        Initialises the object
        """

        super().__init__()

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """

        print(sorted(self))
