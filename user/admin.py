from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    empty_value_display = '--'
