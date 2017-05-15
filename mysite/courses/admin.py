from django.contrib import admin

from .models import Course, CourseSession, UserCourseSession


class UserCourseSessionInline(admin.TabularInline):
    model = UserCourseSession


class CourseSessionAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None, {
    #         'fields': ['name', 'help_links', 'max_mark', 'description', 'main_project', 'tags'],
    #     }),
    #     (_('Date information'), {
    #         'fields': ['created_at', 'updated_at'],
    #         'classes': ['collapse'],
    #     }),
    # ]
    # course = models.ForeignKey(Course, related_name=_('course_sessions'))
    # teacher = models.ForeignKey(User, related_name=_('teacher_courses'), limit_choices_to={'groups__name': 'teachers'})
    # start_time = models.DateTimeField(_('Starts at'))
    # end_time = models.DateTimeField(_('Ends at'))
    # active = models.BooleanField(_('Active'), default=True)
    inlines = [UserCourseSessionInline]
    list_display = ('course', 'active', 'teacher', 'created_at', 'updated_at', 'start_time', 'end_time')
    list_filter = ['start_time', 'end_time', 'course', 'teacher']
    search_fields = ['course', 'teacher']
    date_hierarchy = 'start_time'
    readonly_fields = ('created_at','updated_at')


admin.site.register(Course)
admin.site.register(CourseSession, CourseSessionAdmin)