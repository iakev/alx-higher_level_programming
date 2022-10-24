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
