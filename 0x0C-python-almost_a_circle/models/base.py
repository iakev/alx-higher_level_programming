#!/usr/bin/python3
"""
A module that defines a base class with
it's private attributes and a class constructor
"""

import json


class Base:
    """
    A base class to be inherited by further complicated classes
    down the line.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None and type(id) is int:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a JSON string representation of list_dictionaries.
        list_dictionaries is  a list of dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
