#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy   #TwitterAPI操作用のライブラリを導入

consumer_key        = 'MjFWBvCRciIiSmroC2m2Ox1eR'    #右の4つはAPIの操作に必要なコードです(本当は直書きはマズイ)
consumer_secret     = 'JwRC9Hj2OhhjPaKCwm2q5CY8hu32krIzzvXO3qgwkkv5jU7xNG'
access_token        = '800556259506171904-DkUFHNBdBB9oiaNd3e0ZEB2WhHmPsF5'
access_token_secret = 'vinXJMw8C7lVKU94MYM4zHCgXnj8YeUwlTDxwPlzQKrsd'

# Twitter OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)   #上にあるコードを引数に認証します
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

# Twitter API
api = tweepy.API(auth)

# Mentionの取得
# 自分宛てのツイートを取得して表示
# mentions = api.mentions_timeline(count=10)
# for tweet in mentions:
#     print tweet.text, tweet.user.screen_name

# ツイートを送信
try:
    # api.update_status(status='Hello, world!')
    print api.direct_messages()[0]
except tweepy.TweepError as e:
    print e

#自分宛てのDMを取得して表示する
