from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .models import Project, UserProject


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project
    template_name = 'projects/project_detail.html'

#
# class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
#     model = Project
#     template_name = 'projects/userproject_create.html'
#     success_url = reverse_lazy('projects:list_user_project')
#     fields = ['student', 'teacher', 'project', 'mark']


class UserProjectListView(LoginRequiredMixin, generic.ListView):
    model = UserProject


class UserProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = UserProject
    template_name = 'projects/userproject_create.html'
    success_url = reverse_lazy('projects:list_user_project')
    fields = ['student', 'teacher', 'project', 'mark']

