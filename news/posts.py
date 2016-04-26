import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hiren.settings")
django.setup()

from hiren.settings import JSON_DATA
from .hn import rss
import tweepy
import facebook


posts_collection = rss()


def twitter_api():
    """
    Post status(s) to twitter
    """
    auth = tweepy.OAuthHandler(JSON_DATA['consumer_key'], JSON_DATA['consumer_secret'])
    auth.set_access_token(JSON_DATA['access_token'], JSON_DATA['access_token_secret'])
    api = tweepy.API(auth, wait_on_rate_limit=True)
    for i in posts_collection:
        try:
            api.update_status(i)
        except Exception as e:
            print(e, i)


def facebook_api():
    """
    Post status to fb page
    """
    graph = facebook.GraphAPI(access_token=JSON_DATA['fb_page_token'], version='2.5')
    for i in posts_collection:
        try:
            res = graph.put_object(JSON_DATA['fb_page'], 'feed', message=i)
        except Exception as e:
            print(res, e)

