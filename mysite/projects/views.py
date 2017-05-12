from django.shortcuts import render
from django.views import generic

from .models import Project


class DetailView(generic.DetailView):
    model = Project
    template_name = 'projects/detail.html'

    def get_queryset(self):
        """
        Excludes any optional projects.
        """
        return Project.objects.filter(is_optional=False)
