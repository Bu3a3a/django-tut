# encoding: utf-8
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.CourseSessionListView.as_view(), name='list_course_session'),
    url(r'^(?P<pk>\d+)/$', views.CourseSessionDetailView.as_view(), name='detail_course_session'),

    url(r'^user-courses/$', views.UserCourseSessionListView.as_view(), name='list_user_course_session'),
    url(r'^user-courses/(?P<pk>\d+)/$', views.UserCourseSessionDetailView.as_view(), name='detail_user_course_session'),
    url(r'^user-courses/create/$', views.UserCourseSessionCreateView.as_view(), name='create_user_course_session'),
]