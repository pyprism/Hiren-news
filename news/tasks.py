from celery import shared_task
from news.posts import posts


@shared_task
def run():
    posts()
