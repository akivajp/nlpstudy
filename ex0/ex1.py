#!/usr/bin/python

import sys
import string
from collections import defaultdict

counts = defaultdict(lambda: 0)

infile = open(sys.argv[1], 'r')

for line in infile:
  line = line.strip()
  words = line.split(' ')
  for word in words:
    counts[word] += 1

for word, count in sorted(counts.items()):
  print "%s %d" % (word, count)

print ""
print "number of different: %d" % (len(counts))

