from django.db import models
import string
# Create your models here.

class NewsEvents(models.Model):
    title_en = models.CharField(max_length=100)
    title_ne = models.CharField(max_length=100)
    content_en = models.CharField(max_length=500)
    content_ne = models.CharField(max_length=500)
    date = models.DateField('pub_date')

class Exercise(models.Model):
    name_en = models.CharField(max_length=50)
    name_ne = models.CharField(max_length=50)
    questions = models.IntegerField()
    filename = models.FileField()
    def __str__(self):
        return self.name_en

