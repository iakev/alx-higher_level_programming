#!/usr/bin/python3
"""
script taking my Github credentials, uses Githu API to display my id
"""

import requests
import sys
if __name__ == "__main__":
    github_url = 'https://api.github.com/users/'
    uname = sys.argv[1]
    token = sys.argv[2]
    github_url = github_url + uname
    r = requests.get(github_url, auth=('uname', 'token'))
    json_dict = r.json()
    print("{}".format(json_dict.get('id')))
