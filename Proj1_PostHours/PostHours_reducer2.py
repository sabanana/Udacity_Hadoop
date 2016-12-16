#!/usr/bin/python

#
# Dataset: forum_node.tsv
# Objective: 
#   - For each user, get the hour of the day they posted a maximum number of posts. (ignore the time zone)
#   - MapReduce1's goal is to get <user, hour> as keys and <number_of_posts> as values so that
#   - MapReduce2 can get from this result to get the top-1 keys.
#
# input for reducer2 had already been grouped by authors and sorted by num_of_posts;
# thus, reducer2 only need to print out the last record in each author group


import sys

prevAuthor = None
maxHour = None
maxNum = 0

for line in sys.stdin:
    data_mapped = line.split(",")
    if len(data_mapped) != 2:
        continue

    thisAuthor, other = data_mapped
    thisHour, thisNum = other.split()

    if prevAuthor and prevAuthor != thisAuthor:
        print prevAuthor + '\t' + maxHour
        prevAuthor = thisAuthor
        maxNum = thisNum
        maxHour = thisHour

    prevAuthor = thisAuthor
    if thisNum > maxNum:
        maxNum = thisNum
        maxHour = thisHour
    elif thisNum == maxNum and thisHour != maxHour:
        # There's a tie for an author in different hours
        print thisAuthor + '\t' + thisHour

if prevAuthor != None:
    # print out the max for last author group
    print prevAuthor + '\t' + maxHour

