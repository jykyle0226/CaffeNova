from operator import length_hint
from django.db import models

# Create your models here.

class Cafe(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  review = models.FloatField()
  note = models.TextField(max_length=1000)

