import feedparser
import django
import os
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hiren.settings")
django.setup()

from news.models import Bunny, Tag


def rss():
    """
    Call hacker news api
    :return: List of posts
    """
    feed = []
    tags = Tag.objects.all()
    bunny = feedparser.parse('https://news.ycombinator.com/rss')
    for i in bunny.entries:
        duplicate = Bunny.objects.filter(comment_url=i.comments)
        if duplicate.exists() is False:
            _hash = ''
            for bunny in tags:    # search for predefined value in post title
                if re.match('\\b' + bunny.name + '\\b', i.title_detail.value, re.I):
                    _hash = _hash + ' #' + bunny.name
            if len(_hash):   # if _hash has value append to end of the post
                feed.append(i.title_detail.value + ' : ' + i.link + _hash + " " + "Comments: " + i.comments)
            else:
                feed.append(i.title_detail.value + ' : ' + i.link + " " + "Comments: " + i.comments)
            Bunny(comment_url=i.comments).save()
    return feed
