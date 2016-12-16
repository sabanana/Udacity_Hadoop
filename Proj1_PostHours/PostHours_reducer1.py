#!/usr/bin/python

#
# Dataset: forum_node.tsv
# Objective: 
#   - For each user, get the hour of the day they posted a maximum number of posts. (ignore the time zone)
#   - MapReduce1: Count the number of posts for each user in each hour;
#   -             Output "(<userID>, <hour>)"\t<num_of_posts>
#   - MapReduce2: From MapReduce1's output, for each user, get the hour of max number of posts;

import sys

value = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisValue = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, '\t', str(value)
        oldKey = thisKey
        value = 0

    oldKey = thisKey
    value += int(thisValue)

if oldKey != None:
    print oldKey, '\t', str(value)

