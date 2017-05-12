from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from taggit.managers import TaggableManager


class Project(models.Model):
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)
    name = models.CharField(_('Name'), max_length=250, unique=True)
    description = models.TextField(_('Description'))
    help_links = models.ManyToManyField('HelpLink', blank=True)
    max_mark = models.PositiveIntegerField(_('Max mark'), default=10)
    is_optional = models.BooleanField(_('Is optional'), default=False)
    optional_projects = models.ManyToManyField('self', blank=True)
    tags = TaggableManager()

    def get_tags(self):
        return self.tags.names()

    def get_tags_str(self):
        return ', '.join(self.tags.names())

    def get_students(self):
        return UserProject.objects.filter(project=self.id).values_list('student__username', flat=True)

    def get_teachers(self):
        return UserProject.objects.filter(project=self.id).values_list('teacher__username', flat=True)

    def __str__(self):
        return self.name


class UserProject(models.Model):
    student = models.ForeignKey(User, related_name=_('student_projects'))
    teacher = models.ForeignKey(User, related_name=_('teacher_projects'))
    project = models.ForeignKey(Project, related_name=_('user_projects'))
    started_at = models.DateTimeField(_('Started at'), auto_now_add=True)
    finished_at = models.DateTimeField(_('Finished at'), null=True, blank=True)
    mark = models.PositiveIntegerField(_('Mark'), default=0)

    def __str__(self):
        return ' '.join([self.student.username, self.project.name])


class HelpLink(models.Model):
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)
    name = models.CharField(_('Name'), max_length=250, unique=True)
    description = models.TextField(_('Description'), blank=True, null=True)
    help_link = models.URLField(_('Help link'))