#!/usr/bin/python

# this reducer needs to do nothing
# the intermediate data from mapper is already sorted by key(hit count)

import sys

for line in sys.stdin:
    print line