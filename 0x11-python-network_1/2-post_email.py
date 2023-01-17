#!/usr/bin/python3
"""
script taking in a url and email as cmd line arguments sends a
POST request to the URL with the email as a parameter and display
body of response decoded in utf-8
"""

import urllib.request
import sys
from pprint import pprint
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print(f"{content.decode('utf-8')}")
