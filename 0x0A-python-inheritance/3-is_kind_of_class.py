#!/usr/bin/python3
"""
A module that defines a function
that returns 'True' if an object
is an instance of specified
class or a class that inherited from specified class
otherwise 'False'
"""


def is_kind_of_class(obj, a_class):
    """
    A function that determines if 'obj'
    is instance of 'a_class' or inherits from it;
    Returning a boolean accordingly.
    """

    return isinstance(obj, a_class)
