#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 23:26:16 2019

@author: abc
"""
"""
test = "aw be cr dt"
succ= test.split( )
print len(succ)

input_file = open("test.txt", 'r')
s = {}
for line in input_file:
    div = line.split( )
    print div
    s[div[0]] = div[1] 
"""

import re
import sys
import json


def create_sent_dict(sentiment_file):
    """A function that creates a dictionary which contains terms as keys and their sentiment score as value

        Args:
            sentiment_file (string): The name of a tab-separated file that contains
                                     all terms and scores (e.g., the AFINN file).

        Returns:
            dicitonary: A dictionary with schema d[term] = score
    """
    scores = {}
    input_file = open(sentiment_file, 'r')
    for line in input_file:
       div1 = line.split("\t")
       scores[div1[0]] = int(div1[1])
    return scores

def get_tweet_sentiment(tweet, sent_scores):
    """A function that find the sentiment of a tweet and outputs a sentiment score.

            Args:
                tweet (string): A clean tweet
                sent_scores (dictionary): The dictionary output by the method create_sent_dict

            Returns:
                score (numeric): The sentiment score of the tweet
        """
    score = 0  
    #YOUR CODE GOES HERE
    div3 = tweet.split( )
    num = len(div3)
    for i in range(0,num):
        if div3[i] in sent_scores:
            score = score+sent_scores[div3[i]]
    return score


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
    pattern = re.compile(r"[-']" ,re.DOTALL)
    word = pattern.sub("",word)
    return word


    
    




        