from django.http import HttpResponse
from news.models import Bunny
from .posts import posts


def index(request):
    """
    Returns number of db row
    :param request:
    :return:
    """
    return HttpResponse('Number of Bunny(s): ' + str(Bunny.objects.all().count()))

def scheduler(request):
    """
    Just a simple golang-python hybrid scheduler :P lol !
    :param request:
    :return:
    """
    #posts()
    print('sssss')
    return HttpResponse("Hello Hiren :D !")