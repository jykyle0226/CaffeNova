from operator import length_hint
from django.db import models
from django.urls import reverse
# Create your models here.

class Cafe(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  review = models.FloatField()
  note = models.TextField(max_length=1000)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'cafe_id': self.id})