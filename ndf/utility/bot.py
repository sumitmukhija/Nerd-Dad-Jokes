from ndf import app as appl
from .singleton import singleton
from random import randrange
import tweepy

@singleton
class Bot(object):
    """A SINGLETON class that interacts with Twitter using Tweepy.
    
    Arguments:
        object -- Base class
    """

    def __init__(self):
        self.app = appl.create_app()

    def get_auth(self):
        """Creates auth to interact with Twitter API
        
        Returns:
            auth -- Twitter authentication
        """
        auth = tweepy.OAuthHandler(self.app.config['CONSUMER_KEY'], self.app.config['CONSUMER_KEY_SECRET'])
        auth.set_access_token(self.app.config['ACCESS_TOKEN'],self.app.config['ACCESS_TOKEN_SECRET'] )
        return auth

    def make_public_tweet(self, tweet_content):
        """Posts a public Tweet
        
        Arguments:
            tweet {str} -- Content of the tweet
        
        Exception:
            [TweepError] -- Exception if Tweepy fails
        """
        try:
            api = tweepy.API(self.get_auth())
            api.update_status(tweet_content)
        except tweepy.TweepError as err:
            return err


    def get_random_dad_joke_with_hashtag(self, api, hashtag = "#techdadjokes"):
        """creates an api instance and gets a random tweet from twitter with given hashtag
        
        Keyword Arguments:
            api {API} -- Twitter API instance. Returned by get_auth
            hashtag {str} -- Hashtag to search for (default: {"#techdadjoke"})

        Returns:
            {Status} -- Tweet instance
        
        Exception:
            [TweepError] -- Exception if Tweepy fails
        """
        try:
            searched_tweets = [status for status in tweepy.Cursor(api.search, q=str(hashtag)).items(100)]
            random_tweet_index = randrange(len(searched_tweets))
            tweet = searched_tweets[random_tweet_index]
            return tweet
        except tweepy.TweepError as err:
            return err

    def retweet_dad_joke(self):
        """Retweets a random dad joke from Twitter
        
        Exception:
            [TweepError] -- Exception if Tweepy fails
        """
        try:
            api = tweepy.API(self.get_auth())
            tweet = self.get_random_dad_joke_with_hashtag(api=api)
            api.retweet(tweet.id)
        except tweepy.TweepError as err:
            print(err)
            return err
