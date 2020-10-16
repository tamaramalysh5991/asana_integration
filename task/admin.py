from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('description', 'assignee', )
    search_fields = ('description', 'assignee')
    exclude = ('gid',)
    empty_value_display = '--'
