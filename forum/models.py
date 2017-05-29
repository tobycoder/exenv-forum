from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class QuestionPost(models.Model):
    question = models.CharField(max_length=1000)
    tag = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

class AnswerPost(models.Model):
    post = models.ForeignKey(QuestionPost, related_name='comments', default='Post')
    author = models.CharField(max_length=200, default="FloDeBo")
    text = models.TextField(default="FloDeBo")
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
