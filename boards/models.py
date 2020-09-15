from django.db import models
from core import models as core_models

# Create your models here.


class Board(models.Model):

    """ Board Model Definition """

    CLASS_CATEGORY = "카테고리"
    CLASS_ITEM = "중분류"
    CLASS_DETAIL = "소분류"

    CLASS_CHOICE = [
        (CLASS_CATEGORY, "카테고리"),
        (CLASS_ITEM, "중분류"),
        (CLASS_DETAIL, "소분류"),
    ]

    boardid = models.AutoField(primary_key=True)
    categoryid = models.CharField(max_length=100, null=False, blank=False)
    itemid = models.CharField(max_length=100, null=False, blank=False)
    detailid = models.CharField(max_length=100, null=False, blank=False)
    boardname = models.CharField(max_length=150, null=False, blank=False)
    classification = models.CharField(choices=CLASS_CHOICE, max_length=10, blank=True)
    writeauth = models.ManyToManyField("users.Part", related_name="writeauth", blank=True)
    leaderauth = models.BooleanField(default=False)
    qualityauth = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Board Type"

    def __str__(self):
        return self.boardname


class BoardItem(core_models.TimeStampedModel):

    """ BoardItem Model Definition """

    itemid = models.AutoField(primary_key=True)
    assginboardid = models.ForeignKey(
        "Board", related_name="assginboardid", on_delete=models.SET_NULL, null=True
    )
    itemtitle = models.CharField(max_length=150, null=False, blank=False)
    itemcontent = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name = "Board Item"

    def __str__(self):
        return self.itemtitle
