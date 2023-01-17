#!/usr/bin/python3
"""
script taking in a URL, sending a request to the URL and
displaying response body. if HTTPError throw an exceptions and highlight
the status code
"""

import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
