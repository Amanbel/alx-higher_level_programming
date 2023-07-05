#!/bin/bash
# posts a valid json file
curl -s -X POST $1 -H 'Content-Type: applicatioin/json'
