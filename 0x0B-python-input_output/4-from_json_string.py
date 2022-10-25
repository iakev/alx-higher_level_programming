#!/usr/bin/python3
"""
A module that defines a function that converts
a json string representation to a python object
"""

import json


def from_json_string(my_str):
    """
    deserializes 'my_str' back to python object
    """

    return json.loads(my_str)
