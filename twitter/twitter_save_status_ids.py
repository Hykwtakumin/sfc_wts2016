#!/usr/bin/python
# -*- coding: utf-8 -*-
from os.path import isfile
import fcntl
from fcntl import flock
import tweepy
import codecs
import re

consumer_key        = 'MjFWBvCRciIiSmroC2m2Ox1eR'    #右の4つはAPIの操作に必要なコードです(本当は直書きはマズイ)
consumer_secret     = 'JwRC9Hj2OhhjPaKCwm2q5CY8hu32krIzzvXO3qgwkkv5jU7xNG'
access_token        = '800556259506171904-DkUFHNBdBB9oiaNd3e0ZEB2WhHmPsF5'
access_token_secret = 'vinXJMw8C7lVKU94MYM4zHCgXnj8YeUwlTDxwPlzQKrsd'

# Twitter OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

# Twitter API
api = tweepy.API(auth)

# これまでに対応したstatus idのリスト格納用
data = []

if isfile('log.txt'):
    f = open('log.txt', 'r')
    flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
    for line in f.readlines():
        data.append(int(line.strip()))
    flock(f, fcntl.LOCK_UN)
    f.close()
else:
    print 'Warning: log.txt not found'

# 自分への未応答のメンションのそれぞれについて応答
mentions = api.mentions_timeline(count=10)
for tweet in mentions:
    if not tweet.id in data:
        try:
            # api.update_status(
            #     status='@%s Hello!' % (tweet.user.screen_name),
            #     in_reply_to_status_id=tweet.id
            # )
            test_text = tweet.text
            print test_text
            pattern = re.compile(r'[こそ]れ?マジ?[\?？]')
            matchObj = pattern.search(test_text)
            if matchObj:
                print matchObj.group()
                api.update_status(
                    status = u'@%s 語録が検出されました' % (tweet.user.screen_name),
                    in_reply_to_status_id=tweet.id
                )
            else:
                api.update_status(
                    status = u'@%s 語録は検出されませんでした' % (tweet.user.screen_name),
                    in_reply_to_status_id=tweet.id
                )
            data.append(tweet.id)
            print str(data)
        except tweepy.TweepError as e:
            print e
    else:
        print 'INFO: already replied %d' % tweet.id

# 更新された status_id のリストを書き出し
f = open('log.txt', 'w')
flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
for item in data:
    f.write('%d\n' % item)
flock(f, fcntl.LOCK_UN)
f.close()
