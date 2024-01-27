#!/usr/bin/python3
""" Python script that takes your GitHub credentials (username and
    password) and uses the GitHub API to display your id
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    url = 'https://api.github.com/user'

    token = HTTPBasicAuth(username, passwd)
    response = requests.get(url, auth=token)
    json_data = response.json()
    print(json_data.get('id'))
