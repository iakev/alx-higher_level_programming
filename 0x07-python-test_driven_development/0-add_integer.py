#!/usr/bin/python3
"""
A module that defines addition functions for integers and float types
"""


def add_integer(a, b=98):
    """
    A function that adds two integers a and b if floats first converts them to
    integers
    """
    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    elif type(b) not in [float, int]:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
