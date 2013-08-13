from django.conf.urls import patterns, url

from nest import views

urlpatterns = patterns('',
    # ex: /artists/
    url(r'^$', views.index, name='index'),
    # ex: /artists/5/
    url(r'^(?P<artist_id>\d+)/$', views.detail, name='detail'),
)
