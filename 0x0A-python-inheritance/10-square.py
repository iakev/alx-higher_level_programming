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

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        compute area of square
        """

        return self.__size ** 2

    def __str__(self):
        """
        Reresentation of square class
        """
        return f"[{Rectangle.__name__}] {self.__size}/{self.__size}"
