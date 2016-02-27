from celery import shared_task
from  news.twitter import api


@shared_task
def run():
    api()
