#!/usr/local/bin/python3
"""Fetches the 10 most recent commits from the repository specified"""
import requests
import sys

if __name__ == "__main__":
    URL = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1])
    response = requests.get(URL)
    commits = response.json()
    for commit in commits[:10]:
        print("{}: {}".format(commit.get('sha'), commit.get('commit').get('author').get('name')))
