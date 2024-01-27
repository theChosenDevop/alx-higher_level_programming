#!/usr/binpython3
""" Script takes in a URL, sends a request to the URL
    and displays the body of the response (decoded in utf-8).
"""
import urllib.error
import urllib.request
import sys
"""Modules manage request and error messages"""


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            print(html)
    except urllib.error.HTTPError as e:
        print("Error Code: {}".format(e.code))
