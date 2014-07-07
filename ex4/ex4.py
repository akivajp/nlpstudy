#!/usr/bin/python
# encoding: utf-8

import sys

import unigram
import split

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print("usage: %s train_file split_target")
    sys.exit(1)
  model1 = unigram.load_model(sys.argv[1])
  print(model1)
  infile = open(sys.argv[2], 'r')
  for line in infile:
    line = line.strip()
    ustr = unicode(line, "utf-8")
    print("splitting: %s" % ustr)
    word = split.split(model1, ustr)

