#!/usr/bin/python3
"""
A module that defines a function that prints first name
and last name as passed to it
"""


def say_my_name(first_name, last_name=""):
    """
    A function printing a sentence conataining
    first and last name
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
