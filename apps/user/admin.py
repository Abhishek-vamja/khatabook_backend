from django.contrib import admin

from apps.user.models import User


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     """Admin for User model."""
#     list_display = ("email", "name", "is_staff", "is_active")
#     search_fields = ("email", "name")
#     readonly_fields = ("created_at", "updated_at")
