#!/usr/bin/python
# encoding: utf-8

from collections import defaultdict
import math
import sys
import string

import common

V = 10**5
#lamb1 = 0.95
#lamb2 = 0.95
#lamb_unk = 1 - lamb1

#def calc_lamb2(model, context):
#  context_counts = model['context_counts']
#  if not context in context_counts:
#    return 0
#  c = model['context_counts'][context]
#  u = model['ucounts'][context]
#  lamb2 = 1 - (u / float(u + c))
#  print "context: %s" % (context)
#  print "lamb2: %s" % (lamb2)
#  return lamb2

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print "usage: %s model_file test_text" % (sys.argv[0])
    sys.exit(1)

  word_count = 0
#  unknown_count = 0
  H = 0

  model_file = open(sys.argv[1], 'r')
  test_file = open(sys.argv[2], 'r')

  # loading model
  model = eval(model_file.read())
  probs = model['probs']
  n = model['n']
  ucounts = model['ucounts']
  context_counts = model['context_counts']
  p_unknown = ucounts[''] / float(context_counts[''])

  for line in test_file:
    line = line.strip()
    words = line.split(' ')
    words.insert(0, '<s>')
    words.append('</s>')
    for i in range(1, len(words)):
      # i-番目の単語について
      word_count += 1
      p = [ p_unknown / float(V) ]
      for j in range(1, i + 2):
        # j-gram を取得する
        phrase = common.get_phrase(words, i, j)
#        print "phrase: %s" % (phrase)
        lamb = common.get_lambda(model, phrase)
#        print "lambda: %s" % (lamb)

        p.append(p[-1] * (1 - lamb))
        if phrase in probs:
          p[-1] += probs[phrase] * lamb

#        print "p: %s" % (p)
      # エントロピーを加える
      H -= math.log(p[-1], 2)
#      print "H: %s" % (H)
#      print ""

  print "entropy = %f" % (H / word_count)
#  cov = (word_count - unknown_count) / float(word_count)
#  print "covorage = %f" % (cov)

