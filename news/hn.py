import feedparser
import django
import os
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hiren.settings")
django.setup()

from news.models import Bunny, Tag
from datetime import datetime, timedelta
from django.utils import timezone


def rss():
    """
    Call hacker news api
    :return: List of posts
    """
    feed = []
    # time_threshold = datetime.now() - timedelta(hours=35)
    time_threshold = timezone.now() - timedelta(hours=35)
    tags = Tag.objects.all()
    bunny = feedparser.parse('https://news.ycombinator.com/rss')
    for i in bunny.entries:
        if Bunny.objects.filter(comment_url=i.comments, time__gt=time_threshold).exists() is False:
            _hash = ''
            post = {'message': '', 'link': ''}
            for bunny in tags:    # search for predefined value in post title
                if re.findall('\\b' + bunny.name + '\\b', i.title_detail.value, re.I):
                    _hash = _hash + ' #' + bunny.name
            if len(_hash):   # if _hash has value append to end of the post
                post['message'] = i.title_detail.value + ' : ' + i.link + _hash + " " + "Comments: " + i.comments
                post['link'] = i.link
                feed.append(post)
            else:
                post['message'] = i.title_detail.value + ' : ' + i.link + " " + "Comments: " + i.comments
                post['link'] = i.link
                feed.append(post)
            Bunny(comment_url=i.comments).save()
    return feed
