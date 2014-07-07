#!/usr/bin/python
# encoding: utf-8

from collections import defaultdict
import math
import sys
import string

V = 10**6
lamb1 = 0.95
lamb_unk = 1 - lamb1

if __name__ == "__main__":
  word_count = 0
  unknown_count = 0
  H = 0

  model_file = open(sys.argv[1], 'r')
  test_file = open(sys.argv[2], 'r')

  # loading model
  model = eval(model_file.read())
  probs = model['probs']
  total = model['total']

  for line in test_file:
    line = line.strip()
    words = line.split(' ')
    words.append('</s>')
    for word in words:
      word_count += 1
      p = lamb_unk / V
      if word in probs:
        p += lamb1 * probs[word]
      else:
        unknown_count += 1
      H -= math.log(p, 2)
#      print "H: %s" % (H)
#      print ""

  print "entropy = %f" % (H / word_count)
  cov = (word_count - unknown_count) / float(word_count)
  print "covorage = %f" % (cov)

