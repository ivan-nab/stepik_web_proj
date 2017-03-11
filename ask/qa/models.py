from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User  
# Create your models here.
class QuestionManager(models.Manager):
    def new():
        pass
    def popular():
        pass 
        
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User)
    objects = QuestionManager()


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = ForeignKey(User)