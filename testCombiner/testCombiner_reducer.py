#!/usr/bin/python
#
# Dataset: purchases.txt
# Objective: Run MapReduce with Combiner to get sum of sales for each weekdays.
#

import sys

total = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisValue = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", total
        oldKey = thisKey;
        total = 0

    oldKey = thisKey
    total += float(thisValue)

if oldKey != None:
    print oldKey, "\t", total

