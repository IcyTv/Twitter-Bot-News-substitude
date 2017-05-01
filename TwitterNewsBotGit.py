#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import tweepy as t
import time
import re
import unicodedata
import dct

def convert(stri):


    link = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', stri)

    for i in link:
        stri = re.sub(i, "", stri)

    if "https:/" in stri:
        stri = stri.replace(stri[stri.index("https"):], "")

    reload(dct)
    repl = dct.repl

    stri = stri.upper()

    for key, val in repl.iteritems():
        stri = stri.replace(key, val)

    return stri


consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = t.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = t.API(auth)

while 1:
    stuff = api.user_timeline(screen_name ='cnnbrk', count=1, include_rts=True)

    for status in stuff:
        status = status

    converted = convert(unicodedata.normalize('NFKD', status.text).encode("utf-8", "ignore")).strip()
    my = unicodedata.normalize('NFKD', api.user_timeline(count=1)[0].text).encode("utf-8", "ignore").strip()

    print converted
    print my

    if converted[:139] != my:
        try:
            print status.id
            api.update_status(status=converted)
        except t.error.TweepError:
            pass

        print "DONE"
    else:
        print "DEBUG: SLEEP"
        time.sleep(120)
