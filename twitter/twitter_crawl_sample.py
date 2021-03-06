#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import tweepy
import codecs

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

# このプログラムの使い方
# python twitter_crawl_sample.py takapon_jp 300 takapon_jp.txt
user = sys.argv[1]
max_count = int(sys.argv[2])
outfile = sys.argv[3]

count = 200
total = 0
oldest = -1

fp = codecs.open(outfile,"w","utf-8")

tweets = api.user_timeline(count=count, screen_name=user)
if len(tweets) == 0:
    fp.close()
    sys.exit()

for tweet in tweets:
    fp.write("%d\t%s\n" % (total, tweet.text))
    total += 1
    oldest = tweet.id
    if total >= max_count:
        fp.close()
        sys.exit()

if oldest != -1:
    while True:
        tweets = api.user_timeline(count=count, screen_name=user, max_id=oldest-1)
        if len(tweets) == 0:
            break
        for tweet in tweets:
            fp.write("%d\t%s\n" % (total, tweet.text))
            total += 1
            oldest = tweet.id
            if total >= max_count:
                fp.close()
                sys.exit()

fp.close()
