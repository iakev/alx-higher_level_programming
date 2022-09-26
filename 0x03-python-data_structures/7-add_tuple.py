#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a or tuple_b:
        if tuple_a == ():
            return tuple_b
        if tuple_b == ():
            return tuple_a
        if len(tuple_a) == 1:
            tuple_a = (tuple_a + (0,))
        if len(tuple_b) == 1:
            tuple_b = (tuple_b + (0,))

        res = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
        return res
