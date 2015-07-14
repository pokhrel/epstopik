from django.db import models
import string
# Create your models here.

class NewsEvents(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    date = models.DateTimeField('pub_date')

class ExerciseChoice(models.Model):
    choice = models.CharField(max_length=50)
    def __str__(self):
        return self.choice

class ExerciseQuestion(models.Model):
    question = models.CharField(max_length=50)
    answers = models.ManyToManyField(ExerciseChoice)
    def my_answers(self):
        return ', '.join([answer.choice for answer in self.answers.all()])
