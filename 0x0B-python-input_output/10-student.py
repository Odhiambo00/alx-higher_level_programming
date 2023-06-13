#!/usr/bin/python3

"""
class Student
"""


class Student:
    """
    Represents a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of student instance
        """

        try:
            for attrs in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        new_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict
