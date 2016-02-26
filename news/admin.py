from django.contrib import admin
from news.models import Bunny
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment_url', 'time']
    ordering = ['id']

admin.site.register(Bunny, AuthorAdmin)