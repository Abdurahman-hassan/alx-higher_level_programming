#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import requests
import sys

if __name__ == "__main__":
    URL = sys.argv[1]
    response = requests.get(URL)
    print(response.headers['X-Request-Id'])
