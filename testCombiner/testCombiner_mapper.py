#!/usr/bin/python

#
# Dataset: purchases.txt
# Objective: Run MapReduce with Combiner to get sum of sales for each weekdays.
#
# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment

import sys
from datetime import datetime

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
	weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
        print "{0}\t{1}".format(weekday, cost)

