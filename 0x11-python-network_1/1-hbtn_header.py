#!/usr/bin/python3
""" Script takes in a URL,sends a request to the URL and
    displays the value of the X-Request-Id variable found in
    the header of the response
"""
import urllib.request
import sys
""" This module help to get the url X-Request-Id """


url = sys.argv[1]
if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
