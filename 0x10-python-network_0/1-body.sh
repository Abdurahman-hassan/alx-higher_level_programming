#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the body of the response if the status code is 200
curl -sL "$1"
