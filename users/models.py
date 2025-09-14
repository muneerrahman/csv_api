from django.db import models
from django.db.models import IntegerField
from rest_framework.fields import CharField, EmailField


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()

    def __str__(self):
        return self.name