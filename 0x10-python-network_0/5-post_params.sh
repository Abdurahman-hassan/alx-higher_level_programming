#!/bin/bash
# Sends a POST request to the URL passed as the first argument and displays the body of the response, A variable email is sent with the value test@gmail.com, A variable subject is sent with the value I will always be here for PLD
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
