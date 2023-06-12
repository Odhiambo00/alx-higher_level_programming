#!/usr/bin/python3

"""
Class MyInt
"""


class MyInt(int):
    """
    contarary version on integer
    """

    def __new__(cls, *args, **kwargs):
        """
        create new instance of class
        """

        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """
        what was not equal now is
        """

        return int(self) != other

    def __ne__(self, other):
        """
        what was equal now isn't
        """

        return int(self) == other
