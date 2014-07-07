#!/usr/bin/python
# encoding: utf-8

from collections import defaultdict
import math
import sys
import string

V = 10**6
lamb1 = 0.95
lamb2 = 0.95
lamb_unk = 1 - lamb1

def calc_lamb2(model, context):
  context_counts = model['context_counts']
  if not context in context_counts:
    return 0
  c = model['context_counts'][context]
  u = model['context_variety'][context]
  lamb2 = 1 - (u / float(u + c))
  print "context: %s" % (context)
  print "lamb2: %s" % (lamb2)
  return lamb2

if __name__ == "__main__":
  word_count = 0
  unknown_count = 0
  H = 0

  model_file = open(sys.argv[1], 'r')
  test_file = open(sys.argv[2], 'r')

  # loading model
  model = eval(model_file.read())
  probs = model['probs']
#  total = model['total']

  for line in test_file:
    line = line.strip()
    words = line.split(' ')
    words.insert(0, '<s>')
    words.append('</s>')
    for i in range(1, len(words)):
      word_count += 1
      phrase = ' '.join(words[i-1:i+1])
      p1 = lamb_unk / V
      print "phrase: %s" % (phrase)
      lamb2 = calc_lamb2(model, words[i-1])
      if words[i] in probs:
        p1 += lamb1 * probs[words[i]]
      else:
        unknown_count += 1
      if phrase in probs:
        p2 = probs[phrase] * lamb2 + (1 - lamb2) * p1
      else:
        p2 = (1 - lamb2) * p1
      print "p2: %s" % (p2)
      H -= math.log(p2, 2)
      print "H: %s" % (H)
      print ""

  print "entropy = %f" % (H / word_count)
#  cov = (word_count - unknown_count) / float(word_count)
#  print "covorage = %f" % (cov)

