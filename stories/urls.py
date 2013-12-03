from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'stories.views.index'),
    url(r'^story/$', 'stories.views.story'),
)