#!/usr/bin/python3
"""Sends a POST request to the passed URL with the letter as a parameter"""

import requests
import sys

if __name__ == "__main__":
    # Set q to the first command line argument
    # or an empty string if not provided
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': letter}
    URL = 'http://0.0.0.0:5000/search_user'
    try:
        # Sending a POST request with the letter as data
        response = requests.post(URL, data=payload)

        # Attempting to parse the JSON response
        json_response = response.json()

        if json_response:
            # If there is a response, display the id and name
            print("[{}] {}".format(json_response.get('id'),
                                   json_response.get('name')))
        else:
            # If the response is empty
            print("No result")
    except ValueError:
        # If there is an error parsing JSON
        print("Not a valid JSON")
