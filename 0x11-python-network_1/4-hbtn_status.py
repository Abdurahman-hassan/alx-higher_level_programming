#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
    URL = "https://alx-intranet.hbtn.io/status"
    response = requests.get(URL)
    response = """Body response:
    - type: {}
    - content: {}""".format(type(response.text), response.text)
    print(response)
