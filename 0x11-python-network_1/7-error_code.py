#!/usr/bin/python3
"""Script takes in a URL, sends a request to the URL
    and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    reqBody = requests.get(url)
    if reqBody.status_code >= 400:
        print("Error code: {}".format(reqBody.status_code))
    else:
        print(reqBody.text)
