from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from taggit.managers import TaggableManager


class Course(models.Model):
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)
    name = models.CharField(_('Name'), max_length=250, unique=True)
    description = models.TextField(_('Description'))
    max_mark = models.PositiveIntegerField(_('Max mark'), default=100)
    tags = TaggableManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')


class CourseSession(models.Model):
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)
    course = models.ForeignKey(Course, related_name=_('course_sessions'))
    teacher = models.ForeignKey(User, related_name=_('teacher_courses'), limit_choices_to={'groups__name': 'teachers'})
    start_time = models.DateTimeField(_('Starts at'), default=timezone.now)
    end_time = models.DateTimeField(_('Ends at'), null=True, blank=True)
    active = models.BooleanField(_('Active'), default=True)

    def session_num(self):
        return len(self.objects.filter(course=self.course))

    def get_name(self):
        return self.course.name + ' (' + str(self.session_num()) + ')'

    def __str__(self):
        return self.get_name()

    class Meta:
        verbose_name = _('Course session')
        verbose_name_plural = _('Course sessions')


class UserCourseSession(models.Model):
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)
    finished_at = models.DateTimeField(_('Finished at'), null=True, blank=True)
    student = models.ForeignKey(User, related_name=_('student_courses'), limit_choices_to={'groups__name': 'students'})
    course_session = models.ForeignKey(CourseSession, related_name=_('user_courses'))
    current_mark = models.PositiveIntegerField(_('Current mark'))

    def __str__(self):
        return ' '.join([self.student.username, self.course_session.get_name()])

    class Meta:
        verbose_name = _("User's course")
        verbose_name_plural = _("User's courses")