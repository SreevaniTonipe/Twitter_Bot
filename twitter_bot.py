import tweepy
import time

#Just for testing purpose
print('This is my twitter bot')

consumer_key = 'boRXx3tn3xz4TOk5s4zgr5ipt'
consumer_secret = 'PToGJsnBuQtb8y7gzz7yIQASJO4FX3TARNrfksOr8pHX7kjhiM'
access_key = '1288513060198420480-j2JhNRGjuiOzAuvkc2zNqRGpw4yJvq'
access_secret ='LYlryMRKzTEjtRhHIB2VdIxLLcXjQsz13iux0Wbh2abAX'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#Twitter bot will automatically like posts for the given username or hashtag search
search1 = '#NewEducationPolicy'
search2 = 'Narendra Modi'
nrTweets = 500
for tweet in (tweepy.Cursor(api.search,search1).items(nrTweets) or tweepy.Cursor(api.search,search2).items(nrTweets)):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
