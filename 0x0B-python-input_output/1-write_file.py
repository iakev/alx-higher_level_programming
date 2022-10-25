#!/usr/bin/python3
"""
A module defining a function that writes 'text'
to 'file'
"""


def write_file(filename="", text=""):
    """
    Writes 'text' string to newly created
    'filename' or overwrites it's contents
    """

    with open(filename, "w", encoding="utf-8") as f:
        nb_chars = f.write(text)
    return nb_chars
