# encoding: utf-8
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),  # translations

    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^password_reset/$', views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done/$', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^password_reset/complete/$', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    url(r'^accounts/profile/$', views.ProfileView.as_view(), name='profile'),

    url(r'^$', views.IndexView.as_view(), name='index'),
]