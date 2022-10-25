#!/usr/bin/python3
"""
This module contains a script that adds all arguments to a
python file and saves them to a file
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
try:
    with open(filename, encoding="utf-8") as f:
        ls = load_from_json_file(filename)
        for i in range(1, len(sys.argv)):
            ls.append(sys.argv[i])
        save_to_json_file(ls, filename)

except FileNotFoundError:
    with open(filename, 'w', encoding="utf-8") as f:
        ls = []
        save_to_json_file(ls, filename)
