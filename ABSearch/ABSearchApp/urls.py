__author__ = 'Craig'

from django.conf.urls import patterns, url
from ABSearchApp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))



