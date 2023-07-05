#!/bin/bash
# posts a valid json file
curl -sX POST $1 -H 'Content-Type: application/json' -d @$2 -L
