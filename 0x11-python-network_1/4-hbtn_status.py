#!/usr/bin/python3
"""
Script feching from a URL and displaying the response
"""

import requests
if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- type: {}".format(r.text))
