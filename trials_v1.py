#Basic auth and tweet collection

import tweepy
import sys

non_bmp_map=dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


api_key="8baNfgPjy4QTp1S6a9wqNfqcw"
api_seckey="rnKeBtQvcf9fWPwQ4bdvvrth2GkBHWTW7wFRCdqq7DnDKwT8oq"

acc_tok="4820003121ZVSx6DOVJaGxIWcogms0uWJ55Z4CFTOFe3O1XMY"
acc_toksec="dhlIsadIAwTwFGeoXmseyAtMFjOWTZALUCXJoikV0nAfv"

auth=tweepy.AppAuthHandler(api_key,api_seckey)
#auth=tweepy.OAuthHandler(api_key,api_seckey)
#auth.set_access_token(acc_tok,acc_toksec)

api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Verified")
except:
    print("Some error")



test=[]

for i in tweepy.Cursor(api.search,q='#coronavirus',languages=["en"],tweet_mode='extended').items(10):
    print(i.full_text.translate(non_bmp_map))
    test.append(i)


    
    
"""
for i in dir(test):
    print(i)

	
__class__
__delattr__
__dict__
__dir__
__doc__
__eq__
__format__
__ge__
__getattribute__
__getstate__
__gt__
__hash__
__init__
__le__
__lt__
__module__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__setattr__
__sizeof__
__str__
__subclasshook__
__weakref__
_api
_json
author
contributors
coordinates
created_at
destroy
display_text_range
entities
favorite
favorite_count
favorited
full_text
geo
id
id_str
in_reply_to_screen_name
in_reply_to_status_id
in_reply_to_status_id_str
in_reply_to_user_id
in_reply_to_user_id_str
is_quote_status
lang
metadata
parse
parse_list
place
retweet
retweet_count
retweeted
retweeted_status
retweets
source
source_url
truncated
user
"""
