from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        ("Custom Profile", {"fields": ("avatar", "telNo", "phoneNo", "title")},),
        ("Task Filed", {"fields": ("part", "task", "leader")},),
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "title",
        "serve",
        "telNo",
        "phoneNo",
    )


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):

    """ Task Admin Definition """

    list_display = ("taskid", "taskname", "assignpart")


@admin.register(models.Part)
class PartAdmin(admin.ModelAdmin):

    """ Part Admin Definition """

    list_display = ("partid", "partname")

