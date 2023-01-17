#!/usr/bin/python3
"""
script taking in a url and email as cmd line arguments sends a
POST request to the URL with the email as a parameter and display
body of response decoded in utf-8
"""

import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    r = requests.post(url, data=payload)
    print(r.text)
