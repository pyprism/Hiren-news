from django.http import HttpResponse
from news.models import Bunny
from .posts import posts


def index(request):
    """
    Returns number of db row
    :param request:
    :return:
    """
    return HttpResponse('Number of Bunny(s): ' + str(Bunny.objects.count()))


def scheduler(request):
    """
    cron based job runner ! :/
    :param request:
    :return:
    """
    posts()
    return HttpResponse("Hello Hiren :D !")
