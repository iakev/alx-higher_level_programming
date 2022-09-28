#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50,
                  "C": 100, "D": 500, "M": 1000}
    res = 0
    i = len(roman_string) - 1
    while i >= 0:
        if roman_string[i] in roman_dict:
            if (roman_dict[roman_string[i]] > roman_dict[roman_string[i - 1]]
                    and i != 0):
                res += (roman_dict[roman_string[i]] -
                        roman_dict[roman_string[i - 1]])
                i -= 1
            else:
                res += roman_dict[roman_string[i]]
        else:
            return res
        i -= 1
    return res
