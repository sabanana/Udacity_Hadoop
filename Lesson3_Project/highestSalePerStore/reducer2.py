#!/usr/bin/python

# Get the highest sale of each store

import sys

largestValue = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# return(print) the largest value of each key

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", largestValue
        oldKey = thisKey;
        largestValue = 0

    oldKey = thisKey
    largestValue = max(largestValue, float(thisSale))

if oldKey != None:
    print oldKey, "\t", largestValue

