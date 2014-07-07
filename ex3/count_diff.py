#!/usr/bin/python

import sys

total = 0
collect = 0
infile1 = open(sys.argv[1])
infile2 = open(sys.argv[2])

lines1 = infile1.readlines()
lines2 = infile2.readlines()
for i in range(0, len(lines1)):
  total += 1
  if lines1[i] == lines2[i]:
    collect += 1

print "total: %s, collect: %s" % (total, collect)
print "accuracy: %s" % (collect / float(total))

