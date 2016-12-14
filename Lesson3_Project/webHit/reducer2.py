#!/usr/bin/python

# Get the number of hits to the site by different IP
#
# line format: <IP> 1
# return by printing: <IP> <hitCnt>

import sys

hitCnt = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisCnt = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", hitCnt
        oldKey = thisKey;
        hitCnt = 0

    oldKey = thisKey
    hitCnt += int(thisCnt)

if oldKey != None:
    print oldKey, "\t", hitCnt

