#!/usr/bin/python3
"""
Module that defines a Rectangle class inheriting from
Base class
"""

from models.base import Base


class Rectangle(Base):
    """
    A class rectangle that inherits from Base
    and defines properties and methods for rectangles
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialise all private variables of rectangle
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        getter for width
        """

        return self.__width

    @width.setter
    def width(self, val):
        """
        setter ensuring int before
        setting
        """

        type(self).validate_height_width("width", val)
        self.__width = val

    @property
    def height(self):
        """
        getter for height
        """

        return self.__height

    @height.setter
    def height(self, val):
        """
        setter ensuring int or float before
        setting
        """

        type(self).validate_height_width("height", val)
        self.__height = val

    @property
    def x(self):
        """
        getter for x
        """

        return self.__x

    @x.setter
    def x(self, val):
        """
        setter ensuring int before
        setting
        """

        type(self).validate_x_y("x", val)
        self.__x = val

    @property
    def y(self):
        """
        getter for y
        """

        return self.__y

    @y.setter
    def y(self, val):
        """
        setter ensuring int before setting
        """

        type(self).validate_x_y("y", val)
        self.__y = val

    @staticmethod
    def validate_height_width(str, val):
        """
        a static method that validates inputs
        """
        if type(val) != int:
            raise TypeError(f"{str} must be an integer")
        if val <= 0:
            raise ValueError(f"{str} must be > 0")

    @staticmethod
    def validate_x_y(str, val):
        """
        a static method that validates inputs
        """
        if type(val) != int:
            raise TypeError(f"{str} must be an integer")
        if val < 0:
            raise ValueError(f"{str} must be >= 0")

    def area(self):
        """
        Returns area value of the Rectangle
        instance
        """

        return self.__width * self.__height

    def display(self):
        """
        method printing out Rectangle
        with # characters to stdout
        """

        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """
        customize string representation
        of Rectangle
        """

        return f"[Rectangle] ({self.id}) " \
            f"{self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute from args
        """

        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                setattr(self, key, kwargs[key])
