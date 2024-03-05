#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import requests
import sys

if __name__ == "__main__":
    URL = sys.argv[1]
    response = requests.get(URL)
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
