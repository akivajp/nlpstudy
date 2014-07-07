#!/usr/bin/python
# encoding: utf-8

import sys

import common

if __name__ == "__main__":
  infile = open(sys.argv[1])
  model = eval(infile.read())
  testfile = open(sys.argv[2])
  w = model['w']
  for line in testfile:
    line = line.strip()
#    fields = line.split("\t")
#    y = fields[0]
#    x = fields[1]
    x = line
    phi = common.create_features(x)
    y_pred = common.predict_one(w, phi)
    print y_pred

