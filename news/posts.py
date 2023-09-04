import urllib

import django
import os

from .models import Bunny

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hiren.settings")
django.setup()

from hiren.settings import JSON_DATA
from .hn import rss
import requests


def posts():
    """
    Post status(s) to fb
    get permanent access_token= http://stackoverflow.com/questions/17197970/facebook-permanent-page-access-token
    :return:
    """
    hn_posts = Bunny.objects.filter(posted=False)[:5]
    for i in hn_posts:
        url = f"https://graph.facebook.com/{JSON_DATA['fb_page']}/feed?message={urllib.parse.quote(i.title)}&link={i.main_url}&access_token={JSON_DATA['fb_page_token']}"
        response = requests.post(url)
        print(response.status_code)
        if response.status_code == 200:
            Bunny.objects.filter(main_url=i.main_url).update(posted=True)
        else:
            raise Exception("Error while posting to fb")



