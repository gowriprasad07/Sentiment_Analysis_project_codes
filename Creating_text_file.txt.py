import tweepy
import sys
import pickle
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
#import pandas as pd
import csv
import re #regular expression
#from textblob import TextBlob
import string
import preprocessor as p

f=open('NFL_Complete_V6_Pre_Processed.pickle','rb')
fb=open('Text_file3.txt','w',encoding="utf-8")


count=0     
while 1:
    try:
        a=pickle.load(f)
        fb.write(str(a["tweet_id"])+"\t"+a["tweet_text"].replace("\n","").replace("\r","")+'\n')
        count+=1
    except EOFError:
        flag=0
        break

f.close()
fb.close()
 
    
