#!/bin/bash
# prints the content length from the response header
curl -sI $1 | grep  -o 'Content-Length: [0-9]*' | grep -o "[0-9]*$"
