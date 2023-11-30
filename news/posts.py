import logging
import urllib

import django
import os

from .models import Bunny

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hiren.settings")
django.setup()

from hiren.settings import JSON_DATA
from .hn import rss
import requests

logger = logging.getLogger(__name__)

def posts():
    """
    Post status(s) to fb
    get permanent access_token= http://stackoverflow.com/questions/17197970/facebook-permanent-page-access-token
    updated info: https://developers.facebook.com/docs/pages/access-tokens
    :return:
    """
    hn_posts = Bunny.objects.filter(posted=False, permission_error=False)[:8]
    for i in hn_posts:
        url = f"https://graph.facebook.com/{JSON_DATA['fb_page']}/feed?message={urllib.parse.quote(i.title)}&link={i.main_url}&access_token={JSON_DATA['fb_page_token']}"
        response = requests.post(url, timeout=50)

        if response.status_code == 200:
            Bunny.objects.filter(main_url=i.main_url).update(posted=True)
        elif response.status_code == 403:
            Bunny.objects.filter(main_url=i.main_url).update(permission_error=True)
        elif response.status_code == 400:
            error_message = "Your message couldn't be sent because it includes content that other people on Facebook have reported as abusive."
            resp = response.json()
            if resp["error"]["message"] == error_message:
                Bunny.objects.filter(main_url=i.main_url).update(permission_error=True)
            else:
                logger.warning(f"Error while posting to fb; status code: {response.status_code}")
                logger.error(f"Error while posting to fb: {response.text}")
                raise Exception("Error while posting to fb")
        else:
            logger.warning(f"Error while posting to fb; status code: {response.status_code}")
            logger.error(f"Error while posting to fb: {response.text}")
            raise Exception("Error while posting to fb")



