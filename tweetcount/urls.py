from django.conf.urls import url

from . import views
import os

urlpatterns = [

	url(r'^$', views.index, name='index'),
	url(r'^fetching/$', views.get_tweet, name='fetching'),
]