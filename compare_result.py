#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import re
import math

origin_dic ={}
nbpy_dic = {}

for line in codecs.open("sfc_pn_test.csv","r","euc-jp"):
    line = line.rstrip()
    lis = line.split(",")
    origin_dic[lis[0]] = lis[2]
