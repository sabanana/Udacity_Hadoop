#!/usr/bin/python

#
# Dataset: forum_node.tsv
# Objective: 
#   - For each user, get the hour of the day they posted a maximum number of posts. (ignore the time zone)
#   - MapReduce1's goal is to get <user, hour> as keys and <num_of_posts> as values so that
#   - MapReduce2 can get from this result to get the top-1 keys.

import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t', quoting=csv.QUOTE_NONE)
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    if len(line) < 19 or line[0] == "\"id\"":
	continue
    
    authorID = line[3]
    date_added = line[8]
    #print date_added[1:-4]

    # ignore timezone offset. e.g. +01
    hour = datetime.strptime(date_added[1:-4], "%Y-%m-%d %H:%M:%S.%f").hour

    key = authorID.strip('\"') + ',' + str(hour)
    print key, '\t', 1
