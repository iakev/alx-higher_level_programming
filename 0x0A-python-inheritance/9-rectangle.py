#!/usr/bin/python3
"""
A module that defines a reectangle based upon 7-base_geomtry.py
BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class that defines a reactangle
    and it inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Rectangle's initializer function
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        A method to calculate the area of
        the rectangle
        """

        return self.__width * self.__height

    def __str__(self):
        """
        Magic method definig how the rectangle object
        is displayed to the user in a friendly way
        """

        return f"[{type(self).__name__}] {self.__width}/{self.__height}"
