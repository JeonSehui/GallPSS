from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Board)
class BoardAdmin(admin.ModelAdmin):

    """ Board Admin """

    list_display = ("boardid", "categoryid", "itemid", "detailid", "boardname", "classification", "leaderauth", "qualityauth", )

    fieldsets =  (
        ("order info", {"fields": ("categoryid", "itemid", "detailid", )},),
        ("board info", {"fields": ("boardname", "classification", )},),
        ("auth info", {"fields": ("writeauth", "leaderauth", "qualityauth", )}),
    )


@admin.register(models.BoardItem)
class BoardItemAdmin(admin.ModelAdmin):

    """ Board Admin """

    list_display = (
        "itemid",
        "itemtitle",
        "assginboardid",
    )
