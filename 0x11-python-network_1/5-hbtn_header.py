#!/usr/bin/python3
"""
script taking in a url as a cmd line argument sends a
request to the URL and display value of X-Request_id variable
"""

import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
