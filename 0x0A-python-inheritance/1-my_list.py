#!/usr/bin/python3
"""
A module that defines a class called
'MyList' that subclasses/inherits from
'list' class
"""


class MyList(list):
    """
    A class that defines a custom list object
    that inherits from Python's 'list' class
    """

    def print_sorted(self):
        """
        A function that sorts and prints integer elements of a list
        in ascending order
        """
        order = self[:]
        order.sort()
        print(order)

    def append(self, val):
        if type(val) != int:
            raise TypeError("values needs to be an integer")
        else:
            super().append(val)
