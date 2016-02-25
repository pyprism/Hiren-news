from hiren import JSON_DATA
from hn import rss
import tweepy


def api():
    """
    Post status(s) to twitter
    """
    auth = tweepy.OAuthHandler(JSON_DATA['consumer_key'], JSON_DATA['consumer_secret'])
    auth.set_access_token(JSON_DATA['access_token'], JSON_DATA['access_token_secret'])
    api = tweepy.API(auth)
    for i in rss.rss():
        api.update_status(i)


api()
