# author = rhnvrm <hello@rohanverma.net>
import os
import tweepy
from tweepy import OAuthHandler


class TwitterClient(object):
    '''
    Generic Twitter Class for the App
    '''
    def __init__(self, query, retweets_only):
        # keys and tokens from the Twitter Dev Console
        consumer_key = os.environ['CONSUMER_KEY']
        consumer_secret = os.environ['CONSUMER_SECRET']
        access_token = os.environ['ACCESS_TOKEN']
        access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
        # Attempt authentication
        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.query = query
            self.retweets_only = retweets_only
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def set_query(self, query=''):
        self.query = query

    def set_retweet_checking(self, retweets_only=False):
        self.retweets_only = retweets_only

    def get_tweets(self, with_retweets=False):
        tweet_count_max = 100  # To prevent exceeding API Limits
        tweets = []

        try:
            recd_tweets = self.api.search(q=self.query, count=tweet_count_max)
            if not recd_tweets:
                pass
            for tweet in recd_tweets:
                if tweet.retweet_count > 0 and self.retweets_only:
                    if tweet not in tweets:
                        tweets.append(tweet)
                elif not self.retweets_only:
                    tweets.append(tweet)

            return tweets

        except tweepy.TweepError as e:
            print("Error : " + str(e))
