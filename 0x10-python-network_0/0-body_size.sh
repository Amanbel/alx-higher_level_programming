#!/bin/bash

curl -sI $1 | grep  -o 'Content-Length: [0-9]*' | grep -o "[0-9]*$"
