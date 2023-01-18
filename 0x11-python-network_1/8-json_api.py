#!/usr/bin/python3
"""
Script taking in a letter sending a POST request to a URL and displaying
the resulting JSON if valid
"""

import requests
import sys
if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    try:
        letter = sys.argv[1]
        payload = {'q': letter}
    except IndexError:
        payload = {'q': ""}
    try:
        r = requests.post(url, data=payload)
        try:
            json_dict = r.json()
            if json_dict:
                print("[{}] {}"
                      .format(json_dict.get('id'), json_dict.get('name')))
            else:
                print("No result")
        except JSONDecodeError as e:
            print("Not a valid JSON")
    except r.raise_for_status():
        pass
