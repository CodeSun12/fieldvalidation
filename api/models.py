from django.db import models
import rest_framework


# Create your models here.
class Squad(models.Model):
    name = models.CharField(max_length=100)
    members = models.IntegerField()
    color = models.CharField(max_length=100)
