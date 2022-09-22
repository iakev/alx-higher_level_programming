#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for item in sorted(dir(hidden_4)):
        if (item[0:2] != "__"):
            print(f"{item}")
