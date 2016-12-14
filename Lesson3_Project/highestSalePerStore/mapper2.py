#!/usr/bin/python

# Get the highest sale of each store
#
# -- another method is to out put "<sale>	<store>"
# -- for each reducers, the input is already sorted by <sale>, we just need to maintain a hashset
#	 recording all the stores we've seen, and output '<sale>	<store>' pair for the store we see
#	 for the first time.
#
# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tabs

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(store, cost)

