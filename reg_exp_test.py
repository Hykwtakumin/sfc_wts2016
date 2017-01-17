#!/usr/bin/python
# -*- coding: utf-8 -*-
#私	ワタシ	私	名詞-代名詞-一般
import codecs
import re



for line in codecs.open("inm_re_lists.txt", "r", "utf-8"):
    line = line.rstrip('\r\n')
    if line == "EOS":
        pass
    else:
        test_text = 'やっぱ中野くんの料理を...最高やな!'
        # print 'r\'' + line + '\''
        pattern = re.compile('r\'' + line + '\'')
        print line
        matchOB = pattern.search(test_text)
        if matchOB:
            print matchOB.group()  # 'ca'
            print ('マッチを検出')


    # matchedList = re.findall(line,test_text)
    # if matchedList:
    #     print len(matchedList)
    #     if len(matchedList) == 1:
    #         print ('淫夢語録が1語含まれていますが、ネタ度は低いと思われます')
    #         for matched in (matchedList):
    #             print str(matched).decode("utf-8")
    #     elif len(matchedList) > 1 and len(matchedList) < 5:
    #         print "matched: ", matchedList
    #         print ('淫夢語録が') + str(len(matchedList)) + ('語含まれているので投稿主は淫夢民である可能性があります。')
    #         for matched in (matchedList):
    #              print str(matched).decode("utf-8")
    #     elif len(matchedList) >= 5:
    #         print u'%s'%(matchedList)
    #         print ('淫夢語録が') + str(len(matchedList)) + ('語含まれてる。間違いなく淫夢厨だってハッキリわかんだね')
    #     else:
    #         print('分析ができませんでした')
    # inm_re_lists.append(line.rstrip().encode('utf-8'))
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

# for line in inm_re_lists:
#     print line

# test_text = 'FF外から失礼するゾ～（謝罪） このツイート面白スギィ！！！！！自分、RTいいっすか？ 淫夢知ってそうだから淫夢のリストにぶち込んでやるぜー いきなりリプしてすみません！許してください！なんでもしますから！(なんでもするとは言ってない)'
# test_text = r'最終発表会まであと2日(55時間)です。'
# print test_text
# matchOB = re.search(re_words, test_text)
#
# if matchOB:
#     print matchOB.group()

# matchedList = re.findall(re_words,test_text)
# if matchedList:
#     print matchedList

# inm_re = '(?:'+ "|".join(inm_re_lists) +')'
# print inm_re
#
# matchedList = re.findall(inm_re,test_text)
# if matchedList:
#     print len(matchedList)
#     if len(matchedList) == 1:
#         print ('淫夢語録が1語含まれていますが、ネタ度は低いと思われます')
#         for matched in (matchedList):
#             print str(matched).decode("utf-8")
#     elif len(matchedList) > 1 and len(matchedList) < 5:
#         print "matched: ", matchedList
#         print ('淫夢語録が') + str(len(matchedList)) + ('語含まれているので投稿主は淫夢民である可能性があります。')
#         for matched in (matchedList):
#              print str(matched).decode("utf-8")
#     elif len(matchedList) >= 5:
#         print u'%s'%(matchedList)
#         print ('淫夢語録が') + str(len(matchedList)) + ('語含まれてる。間違いなく淫夢厨だってハッキリわかんだね')
#     else:
#         print('分析ができませんでした')
#


# pattern = re.compile(inm_re)
# print inm_re
# pattern = re.compile(inm_re)
# print pattern
# iterator = pattern.finditer(test_text)
# for match in iterator:
#     print match.group()   # 1回目: 34567   2回目: 34567
#     # print match.start()   # 1回目: 3       2回目: 13
#     # print match.end()     # 1回目: 8       2回目: 18
#     # print match.span()    # 1回目: (3, 8)  2回目: (13, 18)
