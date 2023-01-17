#!/usr/bin/python3
"""
script taking in a URL, sending a request to the URL and
displaying response body. if HTTPError throw an exceptions and highlight
the status code
"""

import urllib.request
import urllib.error
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print("{}".format(body.decode('utf-8')))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
