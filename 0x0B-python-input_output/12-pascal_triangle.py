#!/bin/python3
"""
A module that contains functions that print pascal's
trinagle
"""


def pascal_triangle(n):
    """
    A function that prints pascal's
    triangle using list until the level
    specified by n
    """

    i = 0
    ls = [[]]

    if int(n) <= 0:
        return ls
    recursive_pascal_triangle(i, ls, int(n))
    return ls


def recursive_pascal_triangle(i, ls, n):
    """
    a recursive function that helps print the
    pascal triangle function above
    """

    # base case
    if i == n:
        return
    elif i == 0:
        ls1 = [1]
        ls[0] = ls1
        recursive_pascal_triangle(i + 1, ls, n)
    elif i == 1:
        ls1 = [1, 1]
        ls.append(ls1)
        recursive_pascal_triangle(i + 1, ls, n)
    else:
        ls2 = []
        for j in range(len(ls[i-1])):
            if j+1 < len(ls[i-1]):
                ans = ls[i-1][j] + ls[i-1][j+1]
                ls2.append(ans)
        ls2.insert(0, 1)
        ls2.append(1)
        ls.append(ls2)
        recursive_pascal_triangle(i + 1, ls, n)
