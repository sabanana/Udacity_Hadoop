#!/usr/bin/python
#
# Dataset: Forum Posts with NodeID
# Objective: Get the inverted index (every word and the list of nodeId they can be found in) of all
# 			 words exists in the posts.

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t', quoting=csv.QUOTE_NONE)
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    if len(line) < 5:
	continue
    nodeID = line[0]
    wordList = re.findall(r"[\w]+", line[4])
    for w in wordList:
	if not w.isdigit() and len(w) > 1:
	    print w.lower() + '\t' + nodeID
