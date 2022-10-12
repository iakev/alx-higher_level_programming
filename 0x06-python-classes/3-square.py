#!/usr/bin/python3
"""
A module that highlights how to create a square class with initialization
"""


class Square:
    """
    A class that abstracts the square shape object currently has a size
    """

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
