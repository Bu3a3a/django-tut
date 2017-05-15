from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, Group

from courses.models import Course


class Quiz(models.Model):
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)
    name = models.CharField(_('Name'), max_length=200)
    course = models.ForeignKey(Course, related_name='quizzes', null=True, verbose_name=_('Course'))
    start_time = models.DateTimeField(_('Starts at'), default=timezone.now)
    end_time = models.DateTimeField(_('Ends at'), null=True, blank=True)
    duration = models.DurationField(_('Duration'), null=True, blank=True)
    max_mark = models.PositiveIntegerField(_('Max mark'), default=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizzes')


class QuizFinished(models.Model):
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)
    student = models.ForeignKey(User, related_name='finished_quizzes', on_delete=models.CASCADE,
                                null=True, verbose_name=_('Student'))
    quiz = models.ForeignKey(Quiz, related_name='finished_quizzes', on_delete=models.CASCADE, verbose_name=_('Quiz'))
    mark = models.PositiveIntegerField(_('Mark'))

    class Meta:
        verbose_name = _('Finished quiz')
        verbose_name_plural = _('Finished quizzes')


class Question(models.Model):
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)
    quiz = models.ForeignKey(Quiz, related_name='questions', null=True, verbose_name=_('Quiz'))
    text = models.CharField(_('Text'), max_length=200)
    max_mark = models.PositiveIntegerField(_('Max mark'), default=1)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')


class Answer(models.Model):
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)
    question = models.ForeignKey(Question, related_name='answers', verbose_name=_('Question'))
    text = models.CharField(_('Text'), max_length=200)
    is_right = models.BooleanField(_('Is right'), default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')