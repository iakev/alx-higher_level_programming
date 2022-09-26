#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a == ():
        return tuple_b
    if tuple_b == ():
        return tuple_a
    a, b = len(tuple_a), len(tuple_b)
    res = ((tuple_a[0] if a >= 1 else 0) + (tuple_b[0] if b >= 1 else 0),
           (tuple_a[1] if a >= 2 else 0) + (tuple_b[1] if b >= 2 else 0))
    return res
