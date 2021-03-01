from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Book(models.Model):
    gid = models.CharField(max_length=300)
    started = models.DateField(null=True)
    finished = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='readingList')
