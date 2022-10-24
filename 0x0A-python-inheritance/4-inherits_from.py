#!/usr/bin/python3
"""
A module that defines a function that
finds out if an object is an instance of a class
that is inherited from specified class directly
or indirectly
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is inherited from a_class
    directly or indirectly or False otherwise"""

    return isinstance(obj, a_class) and type(obj).__name__ != a_class.__name__
