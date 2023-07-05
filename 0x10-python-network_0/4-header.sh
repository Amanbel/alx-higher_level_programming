#!/bin/bash
# sends a request with a header variable
curl -sX GET $1 -H "X-HolbertonSchool-User-Id: 98" -L
