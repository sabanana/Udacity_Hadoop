#!/usr/bin/python

# Get the total sale vale and sale number across all stores

import sys

salesTotal = 0  # total value of sales per store
salesCnt = 0  # total number of sales per store

# Loop around the data
# It will be in the format key\tval1\tval2
# Where key is the store name, val1 is the sale amount, val2 == 1
#
# return by printing out "salesTotal	salesCnt"

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale, thisCnt = data_mapped

    salesTotal += float(thisSale)
    salesCnt += int(thisCnt)



print salesTotal, "\t", salesCnt

