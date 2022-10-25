#!/usr/bin/python3
"""
A module that defines a function that returns dictionary
representation with simple data struccture for JSON serialization of
an object
"""


def class_to_json(obj):
    """
    return a dictionary of 'obj' attributes
    """

    return obj.__dict__
