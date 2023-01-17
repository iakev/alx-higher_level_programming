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
        print("Body response:")
        print(f"\t - type: {type(content)}")
        print(f"\t - content: {content}")
        print(f"\t - utf8 content: {response.msg}")
