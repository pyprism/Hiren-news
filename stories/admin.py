from django.contrib import admin
from stories.models import Story

def lower_case_title(obj):
	return obj.title.lower()
lower_case_title.short_description = 'title'

class StoryAdmin(admin.ModelAdmin):
	list_display = ("__unicode__", 'domain' , 'moderator' ,  'updated_at' ,'created_at')
	list_filter = ('created_at' , 'updated_at')
	search_fields = ('title',)


admin.site.register(Story,StoryAdmin)