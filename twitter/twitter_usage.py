#!/usr/bin/python
# -*- coding: utf-8 -*-
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

# Mentionの取得
# 自分宛てのツイートを取得して表示
count = 3
print u'[ Mentions Timeline (あなた宛のツイート) : 最新 %d件 ]' % count
timeline = api.mentions_timeline(count=count)
for tweet in timeline:
    print '--'
    print u'発 言 者:\t%s' % tweet.user.screen_name
    print u'本 　 文:\t%s' % tweet.text
    print u'MssageId:\t%s' % tweet.id
    print u'発言時間:\t%s' % tweet.created_at

# Timelineの取得 (1)
# 自分がフォロー関係のツイートを取得する
print u'[ Home Timeline : 最新 %d件 ]' % count
timeline = api.home_timeline(count=count)
for tweet in timeline:
    print '--'
    print u'発 言 者:\t%s' % tweet.user.screen_name
    print u'本 　 文:\t%s' % tweet.text
    print u'MssageId:\t%s' % tweet.id
    print u'発言時間:\t%s' % tweet.created_at

# Timelineの取得 (2)
# 特定の「ある人」のツイートだけを取得する
screen_name = 'kotone_nyt'
print u'[ %s さん のツイート : 最新 %d件 ]' % (screen_name, count)
timeline = api.user_timeline(screen_name=screen_name, count=count)
for tweet in timeline:
    print '--'
    print u'発 言 者:\t%s' % tweet.user.screen_name
    print u'本 　 文:\t%s' % tweet.text
    print u'MssageId:\t%s' % tweet.id
    print u'発言時間:\t%s' % tweet.created_at

# ツイートを送信
text = u'メッセージの重複投稿のerrocodeが187だったんけどちょっと待ってそれってクッキー☆ネタだよね?'
try:
    api.update_status(status=text)
    print u'[以下の内容でツイートしました]'
    print text
except tweepy.TweepError as e:
    print u'[Updateに失敗しました]'
    print e

# リプライを送信
user = 'wts16test'
text = u'@%s メッセージの重複投稿のerrocodeが187だったんけどちょっと待ってそれってクッキー☆ネタだよね?' % user
try:
    api.update_status(status=text)
    print u'[以下の内容でリプライしました]'
    print text
except tweepy.TweepError as e:
    print u'[Updateに失敗しました]'
    print e
