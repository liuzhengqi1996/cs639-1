#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 17:47:10 2019

@author: abc
"""
import re
import sys
import json

def preprocess_word(word):
    # Remove punctuation
    word = word.strip('\'"?!,.():;')

    # Convert more than 2 letter repetitions to 2 letter. Example: funnnnny --> funny
    #TODO: The next line should implement the functionality in the above comment.
    pattern = re.compile(r"(.)\1{2,}",re.DOTALL)
    word = pattern.sub(r"\1\1",word)
  #  print word
    

    # Remove - & '
    # TODO: The next line should implement the functionality in the above comment.
    pattern2 = re.compile(r"[-']" ,re.DOTALL)
    word = pattern2.sub("",word)
    return word


def preprocess_tweet(tweet):
   # processed_tweet = []
    # Convert to lower case
    tweet = tweet.lower()
    # Replaces URLs with the empty string
    tweet = re.sub(r'((www\.[\S]+)|(https?://[\S]+))', ' ', tweet)
    # Replace @handle with the empty string
    tweet = re.sub(r'@[\S]+', '', tweet)

    # Replaces #hashtag with hashtag. Example #DataScience should be DataScience
    # TODO: The next line should implement the functionality in the above comment.
    tweet = re.sub("#",'',tweet)    

    # Remove RT (retweet)
    # TODO: The next line should implement the functionality in the above comment.
    tweet = re.sub("rt",'',tweet)
    tweet = re.sub("retweet",'',tweet)
    
    # Replace 2+ dots with space
    # TODO: The next line should implement the functionality in the above commen
    tweet = re.sub("\.\.+",' ',tweet)
    
    return tweet