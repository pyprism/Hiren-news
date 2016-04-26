from celery import shared_task
from news.posts import facebook_api, twitter_api


@shared_task
def run():
    twitter_api()
    facebook_api()
