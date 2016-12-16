#!/usr/bin/python

#
# Dataset: forum_node.tsv
# Objective: 
#   - For each user, get the hour of the day they posted a maximum number of posts. (ignore the time zone)
#   - MapReduce1: Count the number of posts for each user in each hour;
#   -             Output "(<userID>, <hour>)"\t<num_of_posts>
#   - MapReduce2: From MapReduce1's output, for each user, get the hour of max number of posts;
#
# 	mapper2 get the maximum records on its local machine.

import sys

prevAuthor = None
maxHour = None
maxPost = 0

for line in sys.stdin:
    data_mapped = line.split(",")
    if len(data_mapped) != 2:
        continue

    thisAuthor, other = data_mapped
    thisHour, thisNum = other.split()

    if prevAuthor and prevAuthor != thisAuthor:
    	print prevAuthor + ',' + maxHour + '\t' + maxPost
    	prevAuthor = thisAuthor
    	maxHour = thisHour
    	maxPost = thisNum

    prevAuthor = thisAuthor
    if int(thisNum) > int(maxPost):
    	maxPost = thisNum
    	maxHour = thisHour
    elif int(thisNum) == int(maxPost) and thisHour != maxHour:
    	# There's a tie for an author in different hours
    	print thisAuthor + ',' + thisHour + '\t' + thisNum

if prevAuthor != None:
    # print out the max for last author group
    print prevAuthor + ',' + maxHour + '\t' + maxPost
    
