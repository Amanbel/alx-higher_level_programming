#!/bin/bash
# write out you got me
curl -s -o /dev/null -w "You got me!" 0.0.0.0:5000
