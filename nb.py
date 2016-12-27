#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import re
import math

pos_dict = {}
neg_dict = {}

for line in codecs.open("positive.prob","r","euc-jp"):
    line = line.rstrip()
    lis = line.split("\t")
    pos_dict[lis[0]] = float(lis[1])

for line in codecs.open("negative.prob","r","euc-jp"):
    line = line.rstrip()
    lis = line.split("\t")
    neg_dict[lis[0]] = float(lis[1])

pos_prob = 0
neg_prob = 0

for line in codecs.open("test.txt.chasen","r","euc-jp"):
    line = line.rstrip('\r\n')
    if line == "EOS":
        pass

    else:
        lis = line.split("\t")
        if lis[0] in pos_dict:
            pos_prob +=  pos_dict[1]
        else:
            pos_prob += 0.00001

        if lis[0] in neg_dict:
            neg_prob +=  neg_dict[1]
        else:
            neg_prob += 0.00001
