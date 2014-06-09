__author__ = 'prism'
from flask import Flask, jsonify
import os
from hn import HN
import redis

hn = HN()
r = redis.StrictRedis(host='localhost', port=6379, db=0)
app = Flask(__name__)


def news():
    hiren = []
    nisha = {}
    for story in hn.get_stories(story_type='', limit=30):
        if not r.get(story.title):
            r.setex(story.title, 100, "Hi hiren ! :D")
            hiren.append((story.title, story.link, story.comments_link))
    nisha['hiren'] = hiren
    return nisha


@app.route('/')
def index():
    return jsonify(news())


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)