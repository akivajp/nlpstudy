#!/bin/bash

n=100

./train-perceptron.py ../data/titles-en-train.labeled $n > model
./test-perceptron.py model ../data/titles-en-test.word > predicted
./get_answer.py ../data/titles-en-test.labeled > answer
./count_diff.py answer predicted

