from __future__ import unicode_literals
from django.db import models


# Create your models here.

class UserInfo(models.Model):
    email = models.CharField(max_length=128)
    pwd = models.CharField(max_length=64)
