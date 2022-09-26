#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list:
        truth = []
        for n in my_list:
            if n % 2 == 0:
                truth.append(True)
            else:
                truth.append(False)
    return truth
