#!/bin/bash
# Sends a GET request to the URL passed as the first argument and displays the body of the response, A header variable X-School-User-Id is sent with the value 98
curl -sX GET -H "X-School-User-Id: 98" "$1"
