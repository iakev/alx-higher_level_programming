#!/usr/bin/python3
"""
A module that defines a class 'MyInt'
that inherits from 'int'
"""


class MyInt(int):
    """
    class that inherits from int but overwrites
    functionality for __eq__ and __ne__
    """

    def __init__(self, value):
        """
        Initialisation of MyInt
        """
        super().__init__()

    def __eq__(self, *args):
        """
        Method that inverts normal operation
        of '==' operator with '!=' for 'MyInt' class
        """

        return super().__ne__(*args)

    def __ne__(self, *args):
        """
        Metjod that inverts '!=' with '=='
        functionality
        """

        return super().__eq__(*args)
