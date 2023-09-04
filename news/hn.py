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
    # time_threshold = datetime.now() - timedelta(hours=35)
    time_threshold = timezone.now() - timedelta(hours=100)
    tags = Tag.objects.all()
    bunny = feedparser.parse('https://news.ycombinator.com/rss')
    for i in bunny.entries:
        if not Bunny.objects.filter(main_url=i.link).exists():
            _hash = ''
            for bunny in tags:    # search for predefined value in post title
                if re.findall('\\b' + bunny.name + '\\b', i.title_detail.value, re.I):
                    _hash = _hash + ' #' + bunny.name
            if len(_hash):   # if _hash has value append to end of the post
                title = i.title_detail.value + ' : ' + i.link + _hash + " " + "Comments: " + i.comments
                Bunny(main_url=i.link, title=title).save()
            else:
                title = i.title_detail.value + ' : ' + i.link + " " + "Comments: " + i.comments
                Bunny(main_url=i.link, title=title).save()
