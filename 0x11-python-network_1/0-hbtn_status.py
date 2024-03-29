#!/usr/bin/python3
""" Python script fetches https://alx-intranet.hbtn.io/status """

import urllib.request
"""This module is used to work with urls for html requests & responses"""


url = "https://alx-intranet.hbtn.io/status"
if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
