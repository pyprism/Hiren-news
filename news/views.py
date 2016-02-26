from django.http import HttpResponse
from news.models import Bunny


def index(request):
    return HttpResponse('Number of Bunny(s): ' + str(Bunny.objects.all().count()))
