#!/usr/bin/python
# -*- coding: utf-8 -*-
#私	ワタシ	私	名詞-代名詞-一般
import codecs
import re

# dict = {}
#
# for line in codecs.open("okashira.txt.chasen","r","euc-jp"):
#     line = line.rstrip('\r\n')
#     if line == "EOS":
#         pass
#     else:
#         lis = line.split("\t")
#         if re.search(ur"名詞",lis[3]):
#             if lis[0] in dict:
#                 dict[lis[0]] += 1
#             else:
#                 dict[lis[0]] = 1
#
# for x in sorted(dict.items(),key=lambda x:x[1], reverse=True):
#     print x[0], x[1]


inm_re_lists = []
for line in codecs.open("inm_re_lists.txt", "r", "utf-8"):
    inm_re_lists.append(line.rstrip().encode('utf-8'))

for line in inm_re_lists:
    print line.decode('utf-8')

test_text = 'FF外から失礼するゾ～（謝罪） このツイート面白スギィ！！！！！自分、RTいいっすか？ 淫夢知ってそうだから淫夢のリストにぶち込んでやるぜー いきなりリプしてすみません！許してください！なんでもしますから！(なんでもするとは言ってない)'

# matchOB = re.search(re_words, test_text)
#
# if matchOB:
#     print matchOB.group()

# matchedList = re.findall(re_words,test_text)
# if matchedList:
#     print matchedList

inm_re = '(?:'+ "|".join(inm_re_lists) +')'
# print results

matchedList = re.findall(inm_re,test_text)
if matchedList:
    print len(matchedList)
    if len(matchedList) == 1:
        print ('淫夢語録が1語含まれていますが、ネタ度は低いと思われます')
    elif len(matchedList) > 1 and len(matchedList) < 5:
        print ('淫夢語録が') + str(len(matchedList)) + ('語含まれているので投稿主は淫夢民である可能性があります。')
    elif len(matchedList) >= 5:
        print ('淫夢語録が') + str(len(matchedList)) + ('語含まれてる。間違いなく淫夢厨だってハッキリわかんだね')
    else:
        print('分析ができませんでした')
