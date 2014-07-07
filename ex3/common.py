#!/usr/bin/python
# encoding: utf-8

from collections import defaultdict

def create_features(x):
  phi = defaultdict(lambda: 0)
  words = x.split(' ')
  for word in words:
    phi["UNI:"+word] += 1
  return phi

def predict_one(w, phi):
  score = 0
  for name, value in phi.items():
    if name in w:
      score += value * w[name]
#  print "score: %s" % (score)
  if score >= 0:
    return 1
  else:
    return -1

def update_weights(w, phi, y):
  for name, value in phi.items():
    w[name] += value * y

