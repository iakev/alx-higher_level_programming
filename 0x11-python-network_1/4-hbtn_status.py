#!/usr/bin/python3
"""
Script feching from a URL and displaying the response
"""

import requests
if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    print("Body response:\n \t - type: {}\n \t - content: {}"
          .format(type(r.text), r.text))
