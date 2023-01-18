#!/usr/bin/python3
"""
script taking my Github credentials, uses Githu API to display my id
"""

import requests
import sys
if __name__ == "__main__":
    github_url = 'https://api.github.com/user'
    uname = sys.argv[1]
    token = sys.argv[2]
    token = "Bearer " + token
    headers = {"Accept": "application/vnd.github+json",
               "Authorization": token,
               "X-Github-Api-Version": "2022-11-28"}
    r = requests.get(github_url, headers=headers)
    json_dict = r.json()
    print("{}".format(json_dict.get('id')))
