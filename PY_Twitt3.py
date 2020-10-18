import tweepy
api_key="8baNfgPjy4QTp1S6a9wqNfqcw"
api_seckey="rnKeBtQvcf9fWPwQ4bdvvrth2GkBHWTW7wFRCdqq7DnDKwT8oq"

acc_tok="4820003121-ZVSx6DOVJaGxIWcogms0uWJ55Z4CFTOFe3O1XMY"
acc_toksec="dhlIsadIAwTwFGeoXmseyAtMFjOWTZALUCXJoikV0nAfv"
auth=tweepy.OAuthHandler(api_key,api_seckey)
auth.set_access_token(acc_tok,acc_toksec)

api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
#api.statuses_lookup(_[include_entities][trim_user][map_][include_ext_alt_text][include_card_uri])
