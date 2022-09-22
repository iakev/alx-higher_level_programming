#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) > 2:
        print(f"{len(sys.argv) - 1} arguments:")
        for i in range(1, len(sys.argv)):
            print(f"{i:d}: {sys.argv[i]}")
    elif len(sys.argv) == 1:
        print(f"{0} arguments.")
    else:
        print(f"{len(sys.argv) - 1} argument:")
        print(f"1: {sys.argv[1]}")
