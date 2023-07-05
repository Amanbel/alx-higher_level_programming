#!/bin/bash
# write out you got me
curl -o /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me
