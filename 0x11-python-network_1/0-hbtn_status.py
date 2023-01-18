#!/usr/bin/python3
"""
Python script fetching from supplied url and
displaying the response body
"""

import urllib.request
if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        charset = response.headers.get_content_charset()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode(charset)))
