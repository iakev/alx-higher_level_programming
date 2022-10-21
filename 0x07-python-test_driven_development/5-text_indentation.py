#!/usr/bin/python3
"""
A module that contains a function that prints a text with 2 new lines
after each of the following character '.', '?' and ':'
"""


def text_indentation(text):
    """
    A function that prints a text with 2 spaces after certain characters
    i.e. '.', '?' and ':'
    """

    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        flag = False
        strlist = list(text)
        for item in strlist:
            if item == '.' or item == '?' or item == ':':
                print(item)
                print()
                flag = True
            elif flag and item == " ":
                continue
            else:
                print(item, end="")
                flag = False
