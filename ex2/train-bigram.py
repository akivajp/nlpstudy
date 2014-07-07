#!/usr/bin/python
# encoding: utf-8

from collections import defaultdict;
import math
import string
import sys

if __name__ == "__main__":
  infile = open(sys.argv[1], 'r')
  counts = defaultdict(lambda: 0)
  context_counts = defaultdict(lambda: 0)

  for line in infile:
    line = line.strip()
    words = line.split(' ')
    words.insert(0, '<s>')
    words.append('</s>')
    for i in range(1, len(words)):
      phrase = ' '.join(words[i-1:i+1])
      context = words[i-1]
      counts[phrase] += 1
      context_counts[context] += 1
      counts[words[i]] += 1
      context_counts[''] += 1

  probs = { }
  for phrase, count in counts.items():
    context_list = phrase.split(' ')[:-1]
    context = ' '.join(context_list)
#    print "context: %s" % (context)
#    print "count: %d" % (context_counts[context])
    probs[phrase] = count / float(context_counts[context])

  context_variety = defaultdict(lambda: 0)
  for context in context_counts:
    for phrase in counts:
      if phrase.find(context + " ") >= 0:
        context_variety[context] += 1

  # serialize
  model = { }
#  model['counts'] = counts
  model['context_counts'] = dict(context_counts)
  model['context_variety'] = dict(context_variety)
  model['probs'] = probs
  print model

