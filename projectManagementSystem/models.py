__author__ = 'Petyo'

from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    todo = models.IntegerField()
    actual = models.IntegerField()
    estimate = models.IntegerField()
    done = models.BooleanField(default=False)


