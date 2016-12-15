#!/usr/bin/python

import sys

total = 0.0
cnt = 0.0
oldKey = None

# Dataset: purchases.txt
# Objective: Get the mean of sales for each weekdays
#
# Loop around the data
# It will be in the format key\tval
# Where key is the weekday (Mon - 1, Tus - 2, ...), val is the sale amount
#
# return key- WeekDay, value- mean of the sale

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisValue = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", total/cnt
        oldKey = thisKey;
        total = 0.0
	cnt = 0.0

    oldKey = thisKey
    total += float(thisValue)
    cnt += 1.0

if oldKey != None:
    print oldKey, "\t", total/cnt

