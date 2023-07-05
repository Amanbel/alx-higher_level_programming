#!/bin/bash
# gets the allowed request methods
curl -siX OPTIONS $1 | grep "Allow" | cut -d " " -f2-
