#!/usr/bin/python3
"""Fetches https://api.github.com/user"""
import requests
import sys

if __name__ == "__main__":
    URL = "https://api.github.com/user"
    response = requests.get(URL, auth=(sys.argv[1], sys.argv[2]))
    print(response.json().get('id'))
