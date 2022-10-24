#!/usr/bin/python3
"""
A module that defines a function that list all available
methods and attributes of an object
"""


def lookup(obj):
    """
    A function that returns a list containing
    methods and attributes of an object 'obj'
    """

    return dir(obj)
