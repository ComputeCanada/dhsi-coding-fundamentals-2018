# more on mining twitter at https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/

# before you can run this code, you will need to log in to https://apps.twitter.com and create an "app" to get a consumer key, consumer secret, access token, and access secret
# DO NOT SHARE THIS CODE WITH YOUR consumer key/secret and access token/secret included!!!! 

# before you can run this code, you may also need to install tweepy, nltk, textblob, etc. on your computer - you can do this by running "pip install tweepy" (etc) on the command line

# import modules
import tweepy
import json
from datetime import datetime, timezone, timedelta
from textblob import TextBlob
import matplotlib.pyplot as plt
from numpy.random import rand

# connect to Twitter API
from tweepy import OAuthHandler

consumer_key = "insert-your-consumer-key-here"
consumer_secret = "insert-your-consumer-secret-here"
access_token = "insert-your-access-token-here"
access_secret = "insert-your-access-secret-here"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# scrape the last 100 tweets for a hashtag from the Twitter API and save to JSON file
hashtag = "#metoo"
fname = hashtag + ".json"
results = api.search(hashtag, count=100)       #100 is the max allowable number
with open(fname,"w") as file:
    for tweet in results:
        file.write(json.dumps(tweet._json) + "\r\n")

#perform sentiment analysis on file of tweets
each_tweet=[]

#drawing on http://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/
#drawing on http://stackoverflow.com/questions/796008/cant-subtract-offset-naive-and-offset-aware-datetimes
datemin = None
datemax = None

with open(fname, 'r') as f:
    for line in f:
        tweet = json.loads(line)
        #print(tweet['text'])
        each_tweet.append([tweet['created_at'],tweet['text']])
        #print(each_tweet)
    points=[]
    for tweet_deets in each_tweet:
        blob = TextBlob(tweet_deets[1])
        
        #print(blob)
        #print(tweet_deets[0][:50], " : ", blob.sentiment.polarity)
        
        #Time directives taken from https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
        #Date conversion from http://stackoverflow.com/questions/2265357/parse-date-string-and-change-format
        tweet_date = datetime.strptime(tweet_deets[0], '%a %b %d %H:%M:%S %z %Y')
        
        #print(type(tweet_date),tweet_date)
        
        if datemax is None or tweet_date > datemax:
            datemax = tweet_date
        if datemin is None or tweet_date < datemin:
            datemin = tweet_date
        points.append([tweet_date,blob.sentiment.polarity])
        #print(tweet_date)

# make a visual plot of the tweets according to sentiment
# Drawing on http://matplotlib.org/examples/lines_bars_and_markers/scatter_with_legend.html 
# Also drawing on http://matplotlib.org/examples/pylab_examples/date_demo_rrule.html
    
plt.scatter([item[0] for item in points] , [item[1] for item in points], c='red', alpha=0.3, edgecolors='none')
plt.xlim(datemin - timedelta(days=0.001),datemax + timedelta(days=0.001))
plt.xticks(rotation='45')
plt.grid(True)

plt.show()