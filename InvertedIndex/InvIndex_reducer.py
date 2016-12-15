#!/usr/bin/python

#
# Dataset: Forum Posts with NodeID
# Objective: Get the inverted index (every word and the list of nodeId they can be found in) of all
#            words exists in the posts.

import sys

value = ''
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisValue = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", value
        oldKey = thisKey;
        value = ''

    oldKey = thisKey
    value = value + ', ' + thisValue

if oldKey != None:
    print oldKey, "\t", value

