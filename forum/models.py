from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class QuestionPost(models.Model):
    question = models.CharField(max_length=1000)
    tag = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

class AnswerPost(models.Model):
    answer_text = models.CharField(max_length=1000)
    answer_rate = models.IntegerField()

