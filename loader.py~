from __future__ import print_function

# Setup the Django environment so we can access our models
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackernews.settings')

import sys
import json
import urllib2

from datetime import datetime, timedelta

from django.utils.timezone import utc
from django.contrib.auth.models import User

from stories.models import Story


# This script made possible with the help of the Unofficial Hacker News API
# provided by Ronnie Roller (http://ronnieroller.com)
HACKER_NEWS_API_URL = 'http://api.ihackernews.com/page'

# The Hacker News API errors out from time to time, this number controls
# how many times the script attempts to retrieve the data from the service.
RETRY_ATTEMPTS = 3

# TODO: change the username to your username
USERNAME='croach'

def created_at(item):
    # Get the value and precision from the item
    if item.get('postedAgo') == None:
        (value, precision) = '0', 'minutes'
    else:
        (value, precision) = item['postedAgo'].split()[:2]

    # Figure out the multiplier for the given precision
    if precision in ['minute', 'minutes']:
        multiplier = 60
    elif precision in ['hour', 'hours']:
        multiplier = 60*60
    elif precision in ['day', 'days']:
        multiplier = 60*60*24
    else:
        multiplier = 0
        print("Could not match the precision '%s'" % precision, file=sys.stderr)

    # Figure out how many hours ago the item was submitted and create
    # the corresponding datetime object
    seconds_ago = int(value) * multiplier
    return (datetime.utcnow() - timedelta(seconds=seconds_ago)).replace(tzinfo=utc)

def main():
    # Attempt to retrieve and process the data from the Unoffical Hacker News API
    for i in range(RETRY_ATTEMPTS + 1):
        try:
            response = urllib2.urlopen(HACKER_NEWS_API_URL)
            status_code = response.code
        except urllib2.HTTPError, e:
            status_code = e.code

        # If the service errored, hit it again
        if status_code != 200:
            if i <= RETRY_ATTEMPTS:
                print("An error occured while retrieving the data, retrying (%d)..." % (i+1), file=sys.stderr)
            continue

        # If everything went ok, try to load the data
        try:
            items = json.load(response)['items']
            break
        except ValueError, e:
            if i <= RETRY_ATTEMPTS:
                print("An error occurred while loading the data, retrying (%d)..." % i+1, file=sys.stderr)
            continue
    else:
        sys.exit("Too many errors occurred while attempting to retrieve the data")

    # Add the stories to the database
    moderator = User.objects.get(username=USERNAME)
    for item in items:
        story = Story(
            title=item['title'],
            url=item['url'],
            points=item['points'],
            moderator=moderator)
        story.save()
        story.created_at = created_at(item)
        story.save()

if __name__ == '__main__':
    main()
