#!/usr/bin/python3
"""Sends a POST request to a URL with a parameter"""
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    URL = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')
    req = urllib.request.Request(URL, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
