#!/usr/bin/python

import sys

infile = open(sys.argv[1])
for line in infile:
  line = line.strip()
  fields = line.split("\t")
  y = fields[0]
  print y

