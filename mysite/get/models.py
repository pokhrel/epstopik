from django.db import models

# Create your models here.

class NewsEvents(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    date = models.DateTimeField('pub_date')
