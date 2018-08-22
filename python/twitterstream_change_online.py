# -*- coding: utf-8 -*-
#!/usr/bin/python


from TwitterAPI import TwitterAPI

import sys
import time

from auth_robotgimse import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

stringToTrack = "#test12345"
tweet_count = 0

api = TwitterAPI(consumer_key, 
                 consumer_secret,
                 access_token,
                 access_token_secret)

while True:
    
    r = api.request('statuses/filter', {'track':stringToTrack})
    
    print('Twitter ready!')
    print(stringToTrack)
    print("----")
    
    for item in r:
        tweet = item['text']
        user = item['user']['screen_name']        

        print(user)
        tweet_count = tweet_count + 1
        print(tweet_count)

        if "#changestream_robotgimse" in tweet.split():
            tweet_temp = tweet.split()
            stringToTrack = tweet_temp[2]
            tweet_count = 0
            tweet_status = ("@" + str(user) + " Use: " + stringToTrack + " #changestream_robotgimse #your_new_stream to set new stream ")
            r = api.request('statuses/update', {'status': tweet_status})
            break
