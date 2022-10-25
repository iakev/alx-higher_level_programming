#!/usr/bin/python3
"""
A module that defines a function that reads a UTF-8
encoded text file and prints it to stdout
"""


def read_file(filename=""):
    """
    reads text file 'filename' and prints contents
    to stdout
    """

    with open(filename, encoding="utf-8") as f:
        text = f.read()
        print(text, end="")
