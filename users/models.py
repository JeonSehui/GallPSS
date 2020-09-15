from django.db import models
from django.contrib.auth.models import AbstractUser


class Part(models.Model):

    """ Part Model Definition """

    partid = models.CharField(max_length=120, primary_key=True)
    partname = models.CharField(max_length=120, null=False, blank=False)

    class Meta:
        verbose_name = "Part Type"

    def __str__(self):
        return self.partname


class Task(models.Model):

    """ Task Model Definition """

    taskid = models.CharField(max_length=120, primary_key=True)
    taskname = models.CharField(max_length=120, null=False, blank=False)
    assignpart = models.ForeignKey(
        "Part", related_name="assignpart", on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name = "Task Type"

    def __str__(self):
        return self.taskname


class User(AbstractUser):

    """ Custom User Model """

    SERVE_OFFICE = "재직"
    SERVE_LEAVE = "휴직"
    SERVE_RETIRE = "퇴직"

    SERVE_CHOICE = [
        (SERVE_OFFICE, "재직"),
        (SERVE_LEAVE, "휴직"),
        (SERVE_RETIRE, "퇴직"),
    ]

    TITLE_CLERK = "사원"
    TITLE_ASSISTANT = "대리"
    TITLE_MANAGER = "과장"
    TITLE_DEPUTY = "차장"
    TITLE_GENERAL = "부장"

    TITLE_CHOICE = [
        (TITLE_CLERK, "사원"),
        (TITLE_ASSISTANT, "대리"),
        (TITLE_MANAGER, "과장"),
        (TITLE_DEPUTY, "차장"),
        (TITLE_GENERAL, "부장"),
    ]

    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    telNo = models.CharField(max_length=140, null=True)
    phoneNo = models.CharField(max_length=140, null=True)
    part = models.ForeignKey(
        "Part", related_name="part", on_delete=models.SET_NULL, null=True
    )
    task = models.ManyToManyField("Task", related_name="task", blank=True)
    serve = models.CharField(choices=SERVE_CHOICE, max_length=10, blank=True)
    title = models.CharField(choices=TITLE_CHOICE, max_length=10, blank=True)
    leader = models.BooleanField(default=False)
