from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy


class IndexView(generic.TemplateView):
    template_name = 'core/index.html'


class LoginView(auth_views.LoginView):
    template_name = 'core/login.html'


class LogoutView(auth_views.LogoutView):
    template_name = 'core/logout.html'


class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'core/password_reset.html'
    success_url = reverse_lazy('core:password_reset_done')
    email_template_name = 'core/password_reset_email.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    success_url = reverse_lazy('core:password_reset_complete')
    template_name = 'core/password_reset_confirm.html'


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'core/password_reset_complete.html'


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'core/password_reset_done.html'


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    login_url = reverse_lazy('core:login')
    template_name = 'core/profile.html'

    # def get_context_data(self, **kwargs):
    #
    #     return super().get_context_data(**kwargs)
