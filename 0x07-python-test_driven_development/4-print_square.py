#!/usr/bin/python3
"""
A module that defines a function that prints a
square with the '#' character
"""


def print_square(size):
    """
    A function that prints a square with the
    '#' character
    """

    if type(size) != int and type(size) != float:
        raise TypeError("size must be an integer")
    elif type(size) == int and size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(int(size)):
            for j in range(int(size)):
                print('#', end="")
            print()
