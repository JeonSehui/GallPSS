from django.db import models
from django.contrib.auth.models import AbstractUser
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Task(AbstractItem):

    """ Task Model Definition """

    class Meta:
        verbose_name = "Task Type"


class Serve(AbstractItem):

    """ Serve Model Definition """

    class Meta:
        verbose_name = "Serve Type"


class Title(AbstractItem):

    """ Title Model Definition """

    class Meta:
        verbose_name = "Title Type"


class User(AbstractUser):

    """ Custom User Model """

    PART_ACCOUNT = "회계"
    PART_CUSTOMER = "고객"
    PART_SALES = "영업"

    PART_CHOICE = [
        (PART_SALES, "영업"),
        (PART_CUSTOMER, "고객"),
        (PART_ACCOUNT, "회계"),
    ]

    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    telNo = models.CharField(max_length=140, null=True)
    phoneNo = models.CharField(max_length=140, null=True)
    part = models.CharField(
        null=True, choices=PART_CHOICE, max_length=10, blank=True
    )
    primeTask = models.ForeignKey(
        "Task", related_name="primeTask", on_delete=models.SET_NULL, null=True
    )
    subTask = models.ManyToManyField("Task", related_name="subTask", blank=True)
    serve = models.ForeignKey(
        "Serve", related_name="serve", on_delete=models.SET_NULL, null=True
    )
    title = models.ForeignKey(
        "Title", related_name="title", on_delete=models.SET_NULL, null=True
    )
    joinDate = models.DateField(blank=True, null=True)
