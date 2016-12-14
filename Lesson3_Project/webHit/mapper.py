#!/usr/bin/python

# Get number of hits for each url
#
# Input log file format:
# 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469
# IP, ID, usr, time, request, status, size

import sys
import re

for line in sys.stdin:
    regex = r'([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)'
    data = re.match(regex, line)
    if data and len(data.groups()) == 7:
        (IP, ID, usr, time, request, status, size) = data.groups()
        if len(request.split(' ')) == 3:
	    url = request.split(' ')[1]
            print "{0}\t{1}".format(url, 1)