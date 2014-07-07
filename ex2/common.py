#!/usr/bin/python
# encoding: utf-8

import string

# 単語リストwords から i 番目の単語の n-gram フレーズを取得する
def get_phrase(words, i, n):
  return ' '.join(words[i-(n-1):i+1])

# n-gram フレーズから、(n-1)-gram コンテキストを取得する
def get_context(phrase):
  words = phrase.split(' ')
  return ' '.join(words[:-1])

def get_lambda(model, phrase):
  context = get_context(phrase)
  if not context in model['ucounts']:
    return 0
  u = model['ucounts'][context]
  c = model['context_counts'][context]
  return (1 - u / float(u + c))

