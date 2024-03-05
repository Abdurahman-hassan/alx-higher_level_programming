#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io"""
import urllib.request
import sys

if __name__ == "__main__":
    URL = sys.argv[1]
    with urllib.request.urlopen(URL) as response:
        print(response.headers['X-Request-Id'])
