#!/usr/bin/python
# encoding: utf-8

import math
from collections import defaultdict

import unigram

def split(model, ustr):
#  best_score = [0]
  best_edge = defaultdict(lambda: None)
  best_score = defaultdict(lambda: 10**10)
  best_score[0] = 0
  for word_end in range(1, len(ustr)):
    for word_begin in range(0, word_end - 1):
      word = ustr[word_begin:word_end]
      encoded = word.encode('utf-8')
      if len(word) == 1 or unigram.is_in(model, encoded):
        p = unigram.calc_p(model, encoded)
        score = best_score[word_begin] + (-math.log(p))
        print "word:%s p:%s score:%s" % (encoded, p, score)
        if score < best_score[word_end]:
          best_score[word_end] = score
          best_edge[word_end] = (word_begin, word_end)
#  print(best_score)
#  print(best_edge)

  words = []
  next_edge = best_edge[len(best_edge) - 1]

