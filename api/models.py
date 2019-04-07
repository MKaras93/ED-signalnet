from django.db import models
from django.utils import timezone


class SpaceSignal(models.Model):
    system = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(default=timezone.now())
    author = models.CharField(max_length=50)
    content = models.TextField(max_length=140) # TODO: force min length 50 characters.

