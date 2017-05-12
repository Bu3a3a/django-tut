from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import UserProject, Project, HelpLink


class UserProjectInline(admin.TabularInline):
    model = UserProject


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['name', 'help_links', 'max_mark', 'is_optional', 'description', 'optional_projects', 'tags'],
        }),
        (_('Date information'), {
            'fields': ['created_at', 'updated_at'],
            'classes': ['collapse'],
        }),
    ]
    inlines = [UserProjectInline]
    list_display = ('name', 'is_optional', 'get_tags_str', 'created_at', 'updated_at')
    list_filter = ['created_at', 'is_optional', 'tags__name']
    search_fields = ['name', 'tags__name']
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at','updated_at')


class HelpLinkAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['name', 'help_link', 'description'],
        }),
        (_('Date information'), {
            'fields': ['created_at', 'updated_at'],
            'classes': ['collapse'],
        }),
    ]
    list_display = ('name', 'help_link', 'created_at', 'updated_at')
    list_filter = ['name', 'created_at']
    search_fields = ['name', 'description']
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Project, ProjectAdmin)
admin.site.register(HelpLink, HelpLinkAdmin)