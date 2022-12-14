#!/usr/bin/python3
"""
A model that defines an empty class called
'BaseGeometry'
"""


class BaseGeometry:
    """
    A class that generically defines different
    geometries
    """

    def area(self):
        """
        A method that implements the area of a geometry
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        A method that validates value
        """
        if type(name) != str:
            raise TypeError("name should be a string")
        elif type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        else:
            pass
