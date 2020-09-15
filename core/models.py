from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    """ auto_now_add: 모델 생성시/ auto_now: update """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:

        """ abstract를 적용하면 이 모델은 database에 적용되지 않는다 """

        abstract = True
