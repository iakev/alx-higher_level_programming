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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes JSON string representation of list_objs to
        a file
        """
        try:
            filename = str(type(list_objs[0]).__name__)
            filename = filename + ".json"
            list_dictionaries = []
            for obj in list_objs:
                list_dictionaries.append(obj.to_dictionary())
            with open(filename, "w", encoding="utf-8") as f:
                f.write(cls.to_json_string(list_dictionaries))

        except Exception:
            filename = cls.__name__ + ".json"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(cls.to_json_string(None))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns pytyon list of JSON string representation 'json_string'
        """

        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes set
        """

        try:
            if cls.__name__ == "Rectangle":
                rec = cls(12, 6)
                rec.update(**dictionary)
                return rec
            elif cls.__name__ == "Square":
                sqr = cls(12)
                sqr.update(**dictionary)
                return sqr
        except Exception:
            raise Exception

    @classmethod
    def load_from_file(cls):
        """
        A class returning a list of instances
        """

        ls = []
        filename = cls.__name__ + ".json"
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
        if not text:
            return ls
        list_output = cls.from_json_string(text)
        for dic in list_output:
            ls.append(cls.create(**dic))
        return ls
