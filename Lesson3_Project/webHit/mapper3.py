#!/usr/bin/python

# From the result of number of hits per pages, find the most popular url and its number of hits
#
# Input line format: <url>	<cnt>

# return by printing:
# <cnt> <url>

import sys
import re

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    url, cnt = data_mapped
    print "{0}\t{1}".format(cnt, url)