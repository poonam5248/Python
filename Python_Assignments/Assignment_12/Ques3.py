#Ques 3. Using Tweepy library try to extract tweets from Twitter.


import tweepy

consumer_key_052='**********************'
consumer_secret_052='******************'


access_token_052='**********************'
access_token_secret_052='**************************'



auth = tweepy.OAuthHandler(consumer_key_052,consumer_secret_052)
auth.set_access_token(access_token_052, access_token_secret_052)
api = tweepy.API(auth)


tweets = api.search('#MondayMotivation', lang="en", count=15, tweet_mode="extended")


#print tweets

for tweet in tweets:
    print("-----------------------------------")
    print(tweet.full_text)
    print("-----------------------------------")
