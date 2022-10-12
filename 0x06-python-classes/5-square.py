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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#",end="")
            print()
