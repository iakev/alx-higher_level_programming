#!/usr/bin/python3
"""
A module that defines a function
that returns 'True' if an object
is "exactly" an instance of specified
class otherwise 'False'
"""


def is_same_class(obj, a_class):
    """
    A function that determines if 'obj'
    is "exactly" an instance of 'a_class' or not;
    Returning a boolean accordingly.
    """

    return type(obj).__name__ == a_class.__name__
