#!/usr/bin/python3
"""
A module that defines a function that
appends to a text file or creates it if it
doesn't exist.
"""


def append_write(filename="", text=""):
    """
    appends 'text' to end of 'filename' or
    creates 'filename' with 'text' if not in existance
    """

    with open(filename, "a", encoding="utf-8") as f:
        nb_chars = f.write(text)
    return nb_chars
