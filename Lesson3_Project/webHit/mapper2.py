#!/usr/bin/python

# Get the number of hits to the site by different IP
#
# line format:
# 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469
#
# return by printing:
# <IP>	1

import sys
import re

for line in sys.stdin:
    regex = r'([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)'
    data = re.match(regex, line)
    if data and len(data.groups()) == 7:
        (IP, ID, usr, time, request, status, size) = data.groups()
        print "{0}\t{1}".format(IP, 1)