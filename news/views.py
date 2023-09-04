from django.http import HttpResponse
from news.models import Bunny
from .posts import posts
from datetime import datetime, timedelta
from .models import Bunny


def index(request):
    """
    Returns number of db row
    :param request:
    :return:
    """
    return HttpResponse('Number of Bunny(s): ' + str(Bunny.objects.count()))


def send_post(request):
    """
    Post status(s) to fb
    :return:
    """
    posts()
    return HttpResponse("Hello Hiren :D !")


def scrapper(request):
    """
    cron based job runner ! :/
    :param request:
    :return:
    """
    posts()
    return HttpResponse("Hello Hiren :D !")


def cleaner(request):
    """
    Cron endpoint for db cleanup
    :param request:
    :return:
    """
    last_month = datetime.today() - timedelta(days=30)
    news = Bunny.objects.filter(time__lte=last_month)
    news.delete()
    return HttpResponse("Bunny Nuked!")


