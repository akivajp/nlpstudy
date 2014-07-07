#!/usr/bin/python
# encoding: utf-8

from collections import defaultdict;
import math
import string
import sys

if __name__ == "__main__":
  infile = open(sys.argv[1], 'r')
  counts = defaultdict(lambda: 0)
  total = 0

  for line in infile:
    line = line.strip()
    words = line.split(' ')
    for word in words:
      counts[word] += 1
      total += 1
    counts['</s>'] += 1
    total += 1

  probs = { }
  for word, count in counts.items():
    probs[word] = counts[word] / float(total)

  # serialize
  model = { }
  model['total'] = total
  model['probs'] = probs
  print model

