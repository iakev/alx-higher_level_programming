#!/usr/bin/python3
"""
A module that deserializes a json rep from an external file
to a python object
"""

import json


def load_from_json_file(filename):
    """
    Deserializes json from filename and returns a
    corresponding python object
    """

    with open(filename, encoding="utf-8") as f:
        return json.load(f)
