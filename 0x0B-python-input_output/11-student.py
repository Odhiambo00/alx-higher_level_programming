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

        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except:
                pass
        return new_dict

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance:
        """

        for key in json:
            if key in self.__dict__:
                setattr(self, key, json[key])
