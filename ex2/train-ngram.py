#!/usr/bin/python
# encoding: utf-8

from collections import defaultdict;
import math
import string
import sys

import common

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print "usage: %s n_of_ngram train_text" % (sys.argv[0])
    sys.exit(1)
  n = int(sys.argv[1])
  trainfile = sys.argv[2]

  infile = open(trainfile, 'r')
  counts = defaultdict(lambda: 0)
  context_counts = defaultdict(lambda: 0)

  for line in infile:
    line = line.strip()
    words = line.split(' ')
    words.insert(0, '<s>')
    words.append('</s>')
    for i in range(1, len(words)):
      # i 番目の単語について
      for j in range(1, n + 1):
        # j-gram を取得する
        if i - (j-1) < 0:
          # i 番目の単語の j-gram を取得できない
          continue
        # j-gram フレーズ
        phrase = common.get_phrase(words, i, j)
        # (j-1)-gram コンテキスト
        context = common.get_context(phrase)
        counts[phrase] += 1
        context_counts[context] += 1
        # print "%s-th word, %s-gram, phrase: %s,\t context: '%s'" % (i, j, phrase, context)

  probs = { }
  for phrase, count in counts.items():
    context = common.get_context(phrase)
    #print "phrase: '%s' context: '%s'" % (phrase, context)
    #print "count: %d, count: %d" % (counts[phrase], context_counts[context])
    probs[phrase] = count / float(context_counts[context])

  ucounts = defaultdict(lambda: 0)
  for context in context_counts:
    for phrase in counts:
#      if phrase.find(context + " ") >= 0:
      if context == common.get_context(phrase):
        print "match! '%s' => '%s'" % (phrase, context)
        ucounts[context] += 1

  # serialize
  model = { }
#  model['counts'] = counts
  model['context_counts'] = dict(context_counts)
  model['ucounts'] = dict(ucounts)
  model['probs'] = probs
  model['n'] = n
  print model

