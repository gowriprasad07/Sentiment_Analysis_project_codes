import pickle
import tweepy
import sys
import re
f=open('consolidate_Twitter.pickle','rb')
fb=open('Full_text_without_emoji_NewVersion.pickle','wb')
api_key="8baNfgPjy4QTp1S6a9wqNfqcw"
api_seckey="rnKeBtQvcf9fWPwQ4bdvvrth2GkBHWTW7wFRCdqq7DnDKwT8oq"

acc_tok="4820003121-ZVSx6DOVJaGxIWcogms0uWJ55Z4CFTOFe3O1XMY"
acc_toksec="dhlIsadIAwTwFGeoXmseyAtMFjOWTZALUCXJoikV0nAfv"
auth=tweepy.OAuthHandler(api_key,api_seckey)
auth.set_access_token(acc_tok,acc_toksec)

api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

non_bmp_map=dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)



flag=1
count=0
count1=0

"""
def deEmojify(inputString):
    returnString = ""
    for character in inputString:
        try:
            character.encode('ascii')
	    returnString+=character
	except UnicodeEncodeError:
            returnString+=''
    
    return returnString

"""

def deEmojify(ip):
    st=''
    for c in ip:
        try:
            c.encode("ascii")
            st+=c
        except UnicodeEncodeError:
            pass
    return st

while 1:
    li=[]
    try:
        for i in range(100):
            a=pickle.load(f)
            li.append(a[0])
    except EOFError:
        flag=0
        
    p=api.statuses_lookup(li,tweet_mode='extended')
    count+=len(p)
    if count>1000:
        count1+=1
        print(count1)
        count=0

    for i in p:
        text=''
        if hasattr(i,'retweeted_status'):
            try:
                text=i.retweeted_status.full_text
            except:
                text=i.retweeted_status.full_text
        else:
            try:
                text=i.extended_tw2eet['full_text']
            except:
                text=i.full_text

        loc=''
        if i.geo!=None:
            loc=str(i.geo["coordinates"])
        else:
            loc=None
        
        l=[i.id,
           deEmojify(text),
           i.created_at,
           loc,
           i.favorite_count,
           deEmojify(i.source),
           i.retweet_count,
           i.retweeted,
           i.author.id,
           deEmojify(i.author.name),
           deEmojify(i.author.screen_name),
           i.author.followers_count,
           deEmojify(i.author.location),
           i.author.created_at]
        """
        for j in l:
            print(str(j).translate(non_bmp_map),end=",")
        print()

        """
            


        pickle.dump(l,fb)

    if flag==0:
        
        break
f.close()
fb.close()


    

    
