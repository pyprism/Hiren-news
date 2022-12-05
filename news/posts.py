import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hiren.settings")
django.setup()

from hiren.settings import JSON_DATA
from .hn import rss
import facebook


def posts():
    """
    Post status(s) to fb
    :return:
    """
    graph = facebook.GraphAPI(access_token=JSON_DATA['fb_page_token'], version='15.0')  # access_token= http://stackoverflow.com/questions/17197970/facebook-permanent-page-access-token

    for i in rss():
        try:
            graph.put_object(JSON_DATA['fb_page'], 'feed', message=i['message'], link=i['link'])
        except Exception as e:
            print(e)


