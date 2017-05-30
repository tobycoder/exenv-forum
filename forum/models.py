from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class QuestionPost(models.Model):
    question = models.CharField(max_length=1000)
    tag = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(QuestionPost, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

