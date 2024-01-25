#!/usr/bin/env bash
# Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

curl -s --head "$1" | grep -i Content-Length | awk '{print $2}'
