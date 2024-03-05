#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter"""
import requests
import sys

if __name__ == "__main__":
    URL = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(URL, data={'email': email})
    print(response.text)
