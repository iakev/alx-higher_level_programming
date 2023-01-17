#!/usr/bin/python3
"""
script taking in a url as a cmd line argument sends a
request to the URL and display value of X-Request_id variable
"""

import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(response.headers.get("X-Request-Id"))
