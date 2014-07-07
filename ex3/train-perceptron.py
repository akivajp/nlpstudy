#!/usr/bin/python
# encoding: utf-8

import sys
from collections import defaultdict

import common

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print "usage: %s epoch_count train_file" % (sys.argv[0])
    sys.exit(1)
  w = defaultdict(lambda: 0)
  n = int(sys.argv[2])
  for i in range(0, n + 1):
    infile = open(sys.argv[1])
    for line in infile:
      line = line.strip()
      fields = line.split("\t")
      #print "fields: %s" % (fields)
      y = int(fields[0])
      x = fields[1]
      phi = common.create_features(x)
#      print "phi: %s" % (dict(phi))
      y_pred = common.predict_one(w, phi)
#      print "w: %s" % (dict(w))
#      print "y: %s, y_pred: %s" % (y, y_pred)
      if y_pred != y:
        common.update_weights(w, phi, y)

  model = {}
  model['w'] = dict(w)
  print model

