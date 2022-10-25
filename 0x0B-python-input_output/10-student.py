#!/usr/bin/python3
"""
A module that contains definition for
a Student class
"""


class Student:
    """
    A class contiaining initialization of specified public instance attributes
    and a method giving dictionary rep of object
    """

    def __init__(self, first_name, last_name, age):
        """
        initializing magic function
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary represenatation
        of self
        """
        if attrs is None:
            return self.__dict__
        else:
            selected = {}
            for key in attrs:
                if type(key) == str and key in self.__dict__.keys():
                    selected[key] = self.__dict__[key]
            return selected
