from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, Group


class Quiz(models.Model):
    name = models.CharField(_('Name'), max_length=200)
    pub_date = models.DateTimeField(_('Date published'))
    accessible_for = models.ManyToManyField(Group, related_name='accessible_quizzes', verbose_name=_('Accessible for'))
    duration = models.DurationField(_('Duration'), null=True, blank=True)

    def __str__(self):
        return self.name


class QuizFinished(models.Model):
    user = models.ForeignKey(User, related_name='finished_quizzes', on_delete=models.CASCADE, verbose_name=_('User'))
    quiz = models.ForeignKey(Quiz, related_name='finished_quizzes', on_delete=models.CASCADE, verbose_name=_('Quiz'))
    started_at = models.DateTimeField(_('Started at'), auto_created=timezone.now())
    finished_at = models.DateTimeField(_('Finished at'), null=True, blank=True)
    mark = models.PositiveIntegerField(_('Mark'))


class Question(models.Model):
    quiz = models.ManyToManyField(Quiz, related_name='questions')
    text = models.CharField(_('Text'), max_length=200)
    pub_date = models.DateTimeField(_('Date published'), auto_created=timezone.now())

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', verbose_name=_('Question'))
    text = models.CharField(_('Text'), max_length=200)
    is_right = models.BooleanField(_('Is right'), default=False)

    def __str__(self):
        return self.text