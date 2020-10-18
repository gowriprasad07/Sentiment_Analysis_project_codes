import pickle
import tweepy

api_key="8baNfgPjy4QTp1S6a9wqNfqcw"
api_seckey="rnKeBtQvcf9fWPwQ4bdvvrth2GkBHWTW7wFRCdqq7DnDKwT8oq"

acc_tok="4820003121-ZVSx6DOVJaGxIWcogms0uWJ55Z4CFTOFe3O1XMY"
acc_toksec="dhlIsadIAwTwFGeoXmseyAtMFjOWTZALUCXJoikV0nAfv"
auth=tweepy.OAuthHandler(api_key,api_seckey)
auth.set_access_token(acc_tok,acc_toksec)

api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
f=open('consolidate_Twitter.pickle','rb')
fbb=open('SingleTweet.txt','w')


tw=[]
te=[]

try:
    for i in range(20):
        #tweet = status.retweeted_status.extended_tweet["full_text"]
        p=pickle.load(f)
        tw.append(p[0])
        te.append(p[1])
        #print(str(p)+'\n')
except EOFError:
    pass

d=api.statuses_lookup(tw,tweet_mode='extended')

f.close()
fbb.close()
