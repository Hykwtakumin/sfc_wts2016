#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import re

text = '\'@wts2016team4\n当日なのに動かんとかこれマジ?'
pattern = re.compile('[こそ]れ?マジ?[\?？]') # 3で始まり7で終わる最短の文字列
# 文字列を走査して正規表現がどこにあるか調べる
matchObj = pattern.search(text)
if matchObj:
    print matchObj.group() # <_sre.SRE_Match object at 0xNNNNNNNNN>
