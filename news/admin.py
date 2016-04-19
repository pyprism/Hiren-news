from django.contrib import admin
from news.models import Bunny, Tag
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment_url', 'time']
    ordering = ['id']


class TagEditor(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    ordering = ['id']


admin.site.register(Tag, TagEditor)
admin.site.register(Bunny, AuthorAdmin)
