import feedparser
from db.models import Content
from hiren import db


def rss():
    """
    Call hacker news api
    :return: List of posts
    """
    feed = []
    bunny = feedparser.parse('https://news.ycombinator.com/rss')
    for i in bunny.entries:
        duplicate = Content.query.filter_by(comments_url=i.comments).first()
        if duplicate is None:
            feed.append(i.title_detail.value + ' : ' + i.link + " " + "Comments: " + i.comments)
            hiren = Content(i.comments)
            db.session.add(hiren)
            db.session.commit()
    return feed

