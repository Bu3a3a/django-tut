import datetime
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Poll(models.Model):
    question = models.CharField(_('Question'), max_length=200)
    pub_date = models.DateTimeField(_('Date published'), auto_created=timezone.now())

    def __str__(self):
        return self.question

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date < now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = _('Published recently?')


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(_('Text'), max_length=200)
    votes = models.IntegerField(_('Votes'), default=0)

    def __str__(self):
        return self.choice_text