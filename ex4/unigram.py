#!/usr/bin/python
# encoding: utf-8

import sys
from collections import defaultdict

lamb1 = 0.95
lamb_unk = 1 - lamb1
V = 10 ** 6

def train_file(filename):
  infile = open(filename, 'r')
  counts = defaultdict(lambda: 0)
  total = 0
  for line in infile:
    line = line.strip()
    words = line.split(' ')
    words.append('</s>')
    for word in words:
      counts[word] += 1
      total += 1
  probs = {}
  for word in counts:
    probs[word] = counts[word] / float(total)
  model = {}
  model['probs'] = probs
  model['total'] = total
  return model

def calc_p(model, word):
  p = lamb_unk / V
  if word in model['probs']:
    p += (lamb1 * model['probs'][word])
  return p

def is_in(model, word):
  return word in model['probs']

def load_model(modelfile):
  probs = {}
  infile = open(modelfile, 'r')
  for line in infile:
    line = line.strip()
    fields = line.split("\t")
    word = fields[0]
    prob = float(fields[1])
    probs[word] = prob
  model = {}
  model['probs'] = probs
  return model

