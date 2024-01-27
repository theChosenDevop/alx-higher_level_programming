#!/usr/bin/python3
"""
    Python script that takes 2 arguments list 10 commits
    (from the most recent to oldest) of the repository “rails”
    by the user “rails”
"""

import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    ownerRepo = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(ownerRepo, repo)
    response = requests.get(url)
    json_data = response.json()

    for commit in json_data[:10]:
        sha = commit.get('sha')
        author_name = commit['commit']['author']['name']
        print("{}: {}".format(sha, author_name))
