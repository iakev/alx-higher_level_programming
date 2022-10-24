#!/usr/bin/python3
"""
A module that defines a square class that
inherits from the previously defined rectangle class
in '9-rectangle.py'
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class that defines a square class inheriting
    from Rectangle
    """

    def __init__(self, size):
        """
        Initilaizing square with an equal side 'size'
        """
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return f"[{Rectangle.__name__}] {self.__size}/{self.__size}"
