#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import tweepy

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

current = datetime.datetime.now()
deadline = datetime.datetime(2017, 1, 17, 13, 0, 0, 0)
diff = deadline - current
days = diff.days
hours = diff.seconds / 3600 + days * 24

text = u'最終発表会まであと%d日(%d時間)です。' % (days, hours)

# ツイートを送信
try:
    api.update_status(status=text)
except tweepy.TweepError as e:
    print e
