import feedparser
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hiren.settings")
django.setup()

from news.models import Bunny


def rss():
    """
    Call hacker news api
    :return: List of posts
    """
    feed = []
    bunny = feedparser.parse('https://news.ycombinator.com/rss')
    for i in bunny.entries:
        duplicate = Bunny.objects.filter(comment_url=i.comments)
        if duplicate.exists() is False:
            feed.append(i.title_detail.value + ' : ' + i.link + " " + "Comments: " + i.comments)
            Bunny(comment_url=i.comments).save()
    return feed
