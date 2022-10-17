#!/usr/bin/python3
"""
A real definition of Recatngle
class using positive integer values only
"""


class Rectangle:
    """
    Actual definition of Rectngle objects
    """

    def __init__(self, width=0, height=0):
        """
        An initialisizing methods that sets instance
        variables to initial values ensuring they are positive
        integers
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = width
            self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Returns the area of the rectangle provided the width
        and height are viable
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle if width or height are zero
        returns a zero
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
