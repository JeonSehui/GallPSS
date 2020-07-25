from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    
    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "telNo",
                    "phoneNo",
                    "joinDate",
                )
            }
        ),
        (
            "Task Case",
            {
                "fields": (
                    "part",
                    "primeTask",
                    "subTask",
                    "serve",
                    "title",
                )
            }
        )
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "title",
        "serve",
        "primeTask",
        "telNo",
        "phoneNo",
    )


@admin.register(models.Task, models.Title, models.Serve)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """
    pass
