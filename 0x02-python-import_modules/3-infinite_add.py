#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    sm = 0
    if len(argv) == 1:
        sm = sm + 0
    else:
        for i in range(1, len(argv)):
            sm = sm + int(argv[i])
    print(f"{sm}")
