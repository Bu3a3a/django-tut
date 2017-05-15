from django.contrib import admin

from .models import Quiz, QuizFinished, Question, Answer


class QuestionInline(admin.TabularInline):
    model = Question


class AnswerInline(admin.TabularInline):
    model = Answer


class QuizAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None, {
    #         'fields': ['name', 'help_links', 'max_mark', 'description', 'main_project', 'tags'],
    #     }),
    #     (_('Date information'), {
    #         'fields': ['created_at', 'updated_at'],
    #         'classes': ['collapse'],
    #     }),
    # ]
    # student = models.ForeignKey(User, related_name='finished_quizzes', on_delete=models.CASCADE,
    #                             verbose_name=_('Student'))
    # created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    # updated_at = models.DateTimeField(_('Updated at'), auto_now=True)
    # name = models.CharField(_('Name'), max_length=200)
    # course = models.ForeignKey(Course, related_name='quizzes', null=True, verbose_name=_('Course'))
    # start_time = models.DateTimeField(_('Starts at'), default=timezone.now)
    # end_time = models.DateTimeField(_('Ends at'), null=True, blank=True)
    # duration = models.DurationField(_('Duration'), null=True, blank=True)
    # max_mark = models.PositiveIntegerField(_('Max mark'), default=15)
    inlines = [QuestionInline]
    list_display = ('name', 'course', 'max_mark', 'duration', 'start_time', 'end_time', 'updated_at')
    list_filter = ['course', 'max_mark', 'start_time']
    search_fields = ['name', 'course']
    date_hierarchy = 'start_time'
    readonly_fields = ('created_at', 'updated_at')


class QuizFinishedAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None, {
    #         'fields': ['name', 'help_links', 'max_mark', 'description', 'main_project', 'tags'],
    #     }),
    #     (_('Date information'), {
    #         'fields': ['created_at', 'updated_at'],
    #         'classes': ['collapse'],
    #     }),
    # ]
    # student = models.ForeignKey(User, related_name='finished_quizzes', on_delete=models.CASCADE,
    #                             verbose_name=_('Student'))
    # quiz = models.ForeignKey(Quiz, related_name='finished_quizzes', on_delete=models.CASCADE, verbose_name=_('Quiz'))
    # started_at = models.DateTimeField(_('Started at'), auto_created=timezone.now())
    # finished_at = models.DateTimeField(_('Finished at'), null=True, blank=True)
    # mark = models.PositiveIntegerField(_('Mark'))
    list_display = ('quiz', 'student', 'mark', 'created_at', 'updated_at')
    list_filter = ['quiz', 'student', 'created_at', 'mark']
    search_fields = ['quiz', 'student']
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')


class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None, {
    #         'fields': ['name', 'help_links', 'max_mark', 'description', 'main_project', 'tags'],
    #     }),
    #     (_('Date information'), {
    #         'fields': ['created_at', 'updated_at'],
    #         'classes': ['collapse'],
    #     }),
    # ]
    # created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    # updated_at = models.DateTimeField(_('Updated at'), auto_now=True)
    # quiz = models.ManyToManyField(Quiz, related_name='questions')
    # text = models.CharField(_('Text'), max_length=200)
    # max_mark = models.PositiveIntegerField(_('Max mark'), default=1)
    inlines = [AnswerInline]
    list_display = ('quiz', 'max_mark', 'created_at', 'updated_at')
    list_filter = ['quiz', 'max_mark', 'created_at', 'updated_at']
    search_fields = ['quiz', 'max_mark']
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Quiz)
admin.site.register(QuizFinished, QuizFinishedAdmin)
admin.site.register(Question, QuestionAdmin)