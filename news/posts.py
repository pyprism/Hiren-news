import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hiren.settings")
django.setup()

from hiren.settings import JSON_DATA
from .hn import rss
import tweepy
import facebook


def posts():
    """
    Post status(s) to fb and twitter
    :return:
    """
    auth = tweepy.OAuthHandler(JSON_DATA['consumer_key'], JSON_DATA['consumer_secret'])
    auth.set_access_token(JSON_DATA['access_token'], JSON_DATA['access_token_secret'])
    api = tweepy.API(auth, wait_on_rate_limit=True)

    graph = facebook.GraphAPI(access_token=JSON_DATA['fb_page_token'], version='2.5')  # access_token= http://stackoverflow.com/questions/17197970/facebook-permanent-page-access-token

    for i in rss():
        try:
            api.update_status(i['message'])
        except Exception as e:
            print(e, i)

        try:
            res = graph.put_object(JSON_DATA['fb_page'], 'feed', message=i['message'], link=i['link'])
        except Exception as e:
            print(res, e)


