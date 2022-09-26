#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    res = (length, sentence[0]) if length > 0 else (length, None)
    return res
