#!/usr/bin/python3
"""
Module contains a function that converts python
objects to JSON representation
"""

import json


def to_json_string(my_obj):
    """
    Returns a json string representation of 'my_obj'
    """

    return json.dumps(my_obj)
