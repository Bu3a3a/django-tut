# encoding: utf-8
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.ProjectListView.as_view(), name='list_project'),
    url(r'^(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name='detail_project'),

    url(r'^user-project/$', views.UserProjectListView.as_view(), name='list_user_project'),
    url(r'^user-project/create/$', views.UserProjectCreateView.as_view(), name='create_user_project'),
]