#!/usr/bin/python3
"""
A real definition of Recatngle
class using positive integer values only
"""


class Rectangle:
    """
    Actual definition of Rectngle objects
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        An initialisizing methods that sets instance
        variables to initial values ensuring they are positive
        integers and keeps track of objects present
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
            type(self).number_of_instances += 1

    def __del__(self):
        """
        Instance method called when an object of this class is destroyed
        or deleted. Also keeps track of objects present
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

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

    def __str__(self):
        """
        A method that defines user friendly representation
        of rectangle objects
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    string += str(self.print_symbol)
                if i < self.__height - 1:
                    string += "\n"
            return string

    def __repr__(self):
        """
        Return code that can recreate the current rectangle object
        """
        return f"Rectangle({self.__width}, {self.__height})"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method that compares sizes of rectangles and returns
        the bigger one
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_1 if rect_1.area() > rect_2.area() else rect_2
