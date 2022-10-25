#!/usr/bin/python3
"""
A module that defines a function that serializes a python object to
a text file in json format
"""

import json


def save_to_json_file(my_obj, filename):
    """
    serializes 'my_obj' to a text file in json string
    format
    """

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
