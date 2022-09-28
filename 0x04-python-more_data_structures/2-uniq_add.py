#!/usr/bin/python3
def uniq_add(my_list=[]):
    sumer = 0
    for n in set(my_list):
        sumer += n

    return sumer
