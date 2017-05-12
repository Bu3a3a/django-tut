# encoding: utf-8
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
]